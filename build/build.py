#!/usr/bin/env python3
"""Build the GSAM CSG study project from one evidence base.

    python3 build/build.py            # dossier (Markdown), HTML app, print HTML
    python3 build/build.py --pdf      # also render the PDF (needs Node + Playwright)

Inputs : content/chapters/*.md, data/**/*.json
Outputs: dossier/GSAM_CSG_2027_Master_Dossier.md
         gsam_csg_command_center.html      (single file, no network requests)
         build/out/print.html -> GSAM_CSG_2027_Dossier.pdf
         build/out/build_report.json       (validation warnings)
"""
import argparse
import datetime
import html
import json
import pathlib
import re
import subprocess
import sys

import markdown

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from calc import fee_model, money  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "build" / "out"
RESEARCH_DATE = "14 November 2026"
WARN = []

STATUS = {
    "Verified": ("V", "✔"),
    "Supported inference": ("SI", "≈"),
    "Unverified account": ("UA", "?"),
    "Illustrative example": ("IL", "✎"),
    "Conflicting evidence": ("CE", "⇄"),
    "Not publicly established": ("NPE", "∅"),
}
CODE2STATUS = {v[0]: k for k, v in STATUS.items()}
STATUS_HELP = {
    "Verified": "The supporting passage was read on a primary or credible source.",
    "Supported inference": "Reasoned from verified facts or general industry practice; not itself a disclosed fact.",
    "Unverified account": "Known only from one person's account (for example the former intern's call).",
    "Illustrative example": "Invented to teach a mechanism. Not a real client, fee or event.",
    "Conflicting evidence": "Credible sources disagree, or the account conflicts with a source.",
    "Not publicly established": "Searched for and not found in public sources.",
}
LAYER = {"A": "Layer A · verified fact", "B": "Layer B · interpretation", "C": "Layer C · personal fit"}
BOX = {
    "l1": "Level 1 · First principles",
    "l2": "Level 2 · Institutional mechanics",
    "note": "Note",
    "warn": "Limits and caveats",
    "example": "Illustrative example",
    "workproduct": "Sample work product (fictional)",
    "dialogue": "Realistic conversation (illustrative)",
    "check": "Check your understanding",
}


def warn(msg):
    WARN.append(msg)


def jload(path, default=None):
    p = pathlib.Path(path)
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        warn(f"JSON error in {p.relative_to(ROOT)}: {e}")
        return default


def merge(kind):
    """Merge data/fragments/<kind>.*.json, de-duplicating by id (first wins)."""
    seen, out = set(), []
    for f in sorted((DATA / "fragments").glob(f"{kind}.*.json")):
        for row in jload(f, []) or []:
            if not isinstance(row, dict):
                continue
            rid = row.get("id")
            if rid in seen:
                if kind != "glossary":  # glossary overlap between streams is expected; first definition wins
                    warn(f"duplicate id {rid} in {f.name}")
                continue
            seen.add(rid)
            row["_stream"] = f.stem.split(".", 1)[1]
            out.append(row)
    return out


# The former intern named two companies as confidential clients. One relationship is confirmed by the
# manager's own press release and is named. The other has no public confirmation, so its name is removed
# from every generated output (the raw research notes in research/evidence keep the audit trail).
REDACT = re.compile(r"Jaguar Land Rover|Jaguar and Land Rover|Land Rover|Jaguar|\bJLR\b", re.I)
REDACT_TEXT = "[second company named by the former intern; name withheld because no public source confirms the relationship]"


def redact(o):
    if isinstance(o, str):
        return REDACT.sub(REDACT_TEXT, o)
    if isinstance(o, list):
        return [redact(x) for x in o]
    if isinstance(o, dict):
        if any(isinstance(v, str) and REDACT.search(v) for k, v in o.items() if k in ("url", "title", "publisher")):
            o = dict(o)
            if "url" in o:
                o["url"] = ""
            if "title" in o and "published" in o:
                o["title"] = "Pension scheme annual report (scheme name withheld)"
                o["publisher"] = "Scheme trustee (name withheld)"
        return {k: redact(v) for k, v in o.items()}
    return o


def load_all(public=False):
    return redact(_load_all())


def _load_all():
    D = {}
    src = {}
    for f in sorted((DATA / "sources").glob("*.json")):
        for s in jload(f, []) or []:
            if s.get("id") in src:
                warn(f"duplicate source id {s.get('id')}")
            s["_stream"] = f.stem
            src[s["id"]] = s
    D["sources"] = src
    claims = []
    for f in sorted((DATA / "claims").glob("*.json")):
        for c in jload(f, []) or []:
            c["_stream"] = f.stem
            claims.append(c)
    D["claims"] = claims
    for kind in ("people", "mandates", "developments", "competitors", "glossary"):
        D[kind] = merge(kind)
    # glossary: de-duplicate by lower-case term too, sort
    seen, g2 = set(), []
    for g in D["glossary"]:
        key = (g.get("term") or "").strip().lower()
        if key in seen:
            continue
        seen.add(key)
        g2.append(g)
    D["glossary"] = sorted(g2, key=lambda g: (g.get("term") or "").lower())
    D["teams"] = jload(DATA / "teams.json", {"axes": {"geographies": [], "segments": [], "functions": []}, "teams": [], "matrix": []})
    D["lifecycle"] = jload(DATA / "lifecycle.json", {"stages": [], "tpw_variant": []})
    D["roles"] = jload(DATA / "roles.json", [])
    D["why"] = jload(DATA / "why_trees.json", {"trees": []})
    D["interview"] = jload(DATA / "interview.json", {"criteria": [], "questions": [], "cases": []})
    D["cases"] = jload(DATA / "cases.json", {"cases": []})
    D["coverage"] = (jload(DATA / "coverage_register.json", []) or []) + merge("coverage")
    D["coverage"].sort(key=lambda c: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", str(c.get("section") or ""))])
    D["intern_claims"] = jload(DATA / "intern_claims.json", [])
    D["routes"] = jload(DATA / "routes.json", [])
    D["search_strings"] = jload(DATA / "search_strings.json", [])
    D["personal"] = jload(DATA / "personal_ledger.json", None)
    for c in D["cases"]["cases"]:
        c["result"] = fee_model(c["params"])
    return D


# ---------------------------------------------------------------- inline helpers
def esc(s):
    return html.escape(str(s), quote=True)


def badge(status):
    if status not in STATUS:
        return f'<span class="badge badge-x">{esc(status)}</span>' if status else ""
    code, sym = STATUS[status]
    return (f'<span class="badge badge-{code.lower()}" title="{esc(STATUS_HELP[status])}">'
            f'<span aria-hidden="true">{sym}</span> {esc(status)}</span>')


def cite(sid, D):
    if sid not in D["sources"]:
        warn(f"citation to unknown source {sid}")
        return f'<span class="cite cite-missing" title="Source id not in register">[{esc(sid)}?]</span>'
    s = D["sources"][sid]
    return (f'<a class="cite" href="#src-{esc(sid)}" data-src="{esc(sid)}" '
            f'title="{esc((s.get("publisher") or "") + ": " + (s.get("title") or ""))}">{esc(sid)}</a>')


def cites(ids, D):
    if not ids:
        return ""
    if isinstance(ids, str):
        ids = [ids]
    return " ".join(cite(i, D) for i in ids)


RE_CITE = re.compile(r"\[@([A-Za-z0-9][A-Za-z0-9\-_.]*)\]")
RE_BADGE = re.compile(r"\{\{(V|SI|UA|IL|CE|NPE)\}\}")
RE_LAYER = re.compile(r"\{\{L:([ABC])\}\}")


def decorate(h, D):
    """Turn citation / badge / layer markers into HTML (works on already-escaped HTML)."""
    h = RE_CITE.sub(lambda m: cite(m.group(1), D), h)
    h = RE_BADGE.sub(lambda m: badge(CODE2STATUS[m.group(1)]), h)
    h = RE_LAYER.sub(lambda m: f'<span class="layer layer-{m.group(1).lower()}">{LAYER[m.group(1)]}</span>', h)
    return h


def inline(text, D):
    """Plain data string -> safe HTML with citations, badges, **bold** and line breaks."""
    if text is None or text == "":
        return '<span class="na">Not publicly disclosed</span>'
    t = esc(text)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = t.replace("\n", "<br>")
    return decorate(t, D)


def value_html(v, D):
    if v is None or v == "" or v == []:
        return '<span class="na">Not publicly disclosed</span>'
    if isinstance(v, bool):
        return "Yes" if v else "No"
    if isinstance(v, (int, float)):
        return esc(v)
    if isinstance(v, str):
        return inline(v, D)
    if isinstance(v, list):
        if all(isinstance(x, str) for x in v):
            return "<ul>" + "".join(f"<li>{inline(x, D)}</li>" for x in v) + "</ul>"
        return "<ul>" + "".join(f"<li>{value_html(x, D)}</li>" for x in v) + "</ul>"
    if isinstance(v, dict):
        rows = []
        for k, x in v.items():
            if k.startswith("_"):
                continue
            if k == "sources":
                rows.append(f"<dt>Sources</dt><dd>{cites(x, D)}</dd>")
            elif k == "status":
                rows.append(f"<dt>Evidence</dt><dd>{badge(x)}</dd>")
            else:
                rows.append(f"<dt>{esc(label(k))}</dt><dd>{value_html(x, D)}</dd>")
        return '<dl class="kv">' + "".join(rows) + "</dl>"
    return esc(v)


def label(k):
    return k.replace("_", " ").strip().capitalize()


def slug(s):
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s[:60] or "x"


def strip_tags(h):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip()


# ---------------------------------------------------------------- generic cards
def card(e, D, title_key, fields, sub=None, status_key="status", data_attrs=None, cls="card", tag="h3", extra=""):
    attrs = ""
    for k in (data_attrs or []):
        v = e.get(k)
        if isinstance(v, list):
            v = "|".join(str(x) for x in v)
        attrs += f' data-{k.replace("_", "-")}="{esc(v if v not in (None, "") else "Unclear")}"'
    subs = " · ".join(str(e.get(k)) for k in (sub or []) if e.get(k))
    st = badge(e.get(status_key)) if status_key and e.get(status_key) else ""
    rows = []
    for k, lab in fields:
        if k not in e:
            continue
        rows.append(f"<dt>{esc(lab)}</dt><dd>{value_html(e.get(k), D)}</dd>")
    if e.get("sources"):
        rows.append(f"<dt>Sources</dt><dd>{cites(e['sources'], D)}</dd>")
    return (f'<article class="{cls}" id="{esc(e.get("id", ""))}" data-search data-kind="{cls}"{attrs}>'
            f'<{tag} class="card-title">{esc(e.get(title_key) or "(unnamed)")}</{tag}>'
            f'<p class="card-sub">{esc(subs)} {st} <span class="idtag">{esc(e.get("id", ""))}</span></p>'
            f'<dl class="kv">{"".join(rows)}</dl>{extra}</article>')


F_PEOPLE = [("title_class", "Title class"), ("coverage", "Covers clients in"), ("segment", "Client segment"),
            ("function_interpretation", "Function (our interpretation)"), ("function_basis", "Basis for that interpretation"),
            ("career_history", "Career history (public)"), ("evidence_date", "Evidence date"),
            ("current_as_of_cutoff", "Still in post at cutoff?"), ("confidence", "Classification confidence"), ("notes", "Notes")]
F_MANDATE = [("client_type", "Client type"), ("country", "Country"), ("date", "Event date"), ("kind", "Kind of event"),
             ("strategy", "Strategy"), ("amount", "Amount as disclosed"), ("amount_basis", "What the amount measures"),
             ("rationale", "Stated rationale"), ("consultant", "Consultant involvement"), ("decision_makers", "Decision-makers"),
             ("gs_team_attribution", "Public attribution to a GS team"), ("notes", "Notes")]
F_DEV = [("event_date", "Event date"), ("publication_date", "Publication date"), ("what_happened", "1 · What happened"),
         ("client_effect", "2 · How it affects the client"), ("decision_that_changes", "3 · What decision changes"),
         ("existing_investments", "4 · Implications for existing investments"),
         ("possible_gsam_response", "5 · Possible GSAM response (interpretation, not a GS statement)"),
         ("sales_angle", "6 · Sales responsibility"), ("rm_angle", "7 · Relationship-management responsibility"),
         ("risks_counterarguments", "8 · Risks and counterarguments"), ("client_question", "A question to ask a client"),
         ("watch", "Indicators to watch"), ("base_case", "Base case"), ("alternatives", "Plausible alternatives"),
         ("would_change_view", "Evidence that would change the view")]
F_COMP = [("current_name_verified", "Current business name"), ("aum", "Assets"), ("aum_date", "As at"),
          ("relevant_to", "Relevant to which client problem"), ("capabilities", "Capabilities"), ("recent_events", "Recent events"),
          ("where_stronger_than_gs", "Where it may be stronger than GSAM"), ("where_gs_may_be_stronger", "Where GSAM may be stronger (interpretation)")]
F_TEAM = [("name_basis", "Where the name comes from"), ("kind", "Kind of unit"), ("summary", "In one paragraph"),
          ("intern_account", "Former intern's account"), ("public_evidence", "What public sources establish"),
          ("clients", "Clients"), ("decision_makers", "Who decides on the client side"), ("needs", "Investment needs"),
          ("products", "Products and strategies"), ("channels", "Distribution channels"), ("process", "Commercial process"),
          ("specialists", "Specialist dependencies"), ("business_model", "How the business model differs"),
          ("languages", "Languages (job-description evidence only)"), ("recruitment", "Recruitment evidence"),
          ("open_questions", "Unresolved questions")]
F_ROLE = [("purpose", "Purpose"), ("recurring_tasks", "Recurring tasks"), ("work_products", "Work products"),
          ("stakeholders", "Stakeholders"), ("decision_rights", "Decision rights"), ("measures_of_success", "Measures of success"),
          ("notes", "Notes")]
F_STAGE = [("plain", "In plain English"), ("what_happens", "What happens"), ("who_leads", "Who leads"), ("who_supports", "Who supports"),
           ("junior_produces", "What the junior person produces"), ("client_side", "On the client side"),
           ("good_execution_changes", "What good execution changes for the client"), ("failure_points", "Failure points"),
           ("sales_vs_rm", "Sales versus relationship management (illustrative; varies)"), ("duration_note", "Timing")]
F_GLOSS = [("plain", "Plain English"), ("technical", "Mechanics"), ("why_it_matters", "Why it matters to this role")]


# ---------------------------------------------------------------- specialised renderers
def render_matrix(D):
    T = D["teams"]
    geos, segs = T["axes"]["geographies"], T["axes"]["segments"]
    if not geos:
        return '<p class="na">Coverage matrix not yet built.</p>'
    cells = {(c["geo"], c["segment"]): c for c in T["matrix"]}
    h = ['<div class="table-wrap"><table class="matrix"><caption>Coverage matrix: client geography by client segment. '
         'Each cell shows the evidence status. An empty-looking cell is never a zero: it says what was or was not established.</caption>',
         "<thead><tr><th scope=\"col\">Covers clients in</th>"]
    h += [f'<th scope="col">{esc(s["name"])}</th>' for s in segs]
    h.append("</tr></thead><tbody>")
    for g in geos:
        h.append(f'<tr><th scope="row">{esc(g["name"])}</th>')
        for s in segs:
            c = cells.get((g["id"], s["id"]))
            if not c:
                h.append('<td class="cell cell-none"><span class="na">Not investigated</span></td>')
                continue
            link = f'<a class="teamlink" href="#/teams/{esc(c["team"])}" data-team="{esc(c["team"])}">Open team</a>' if c.get("team") else ""
            h.append(f'<td class="cell">{badge(c.get("status"))}<div class="cell-note">{inline(c.get("note"), D)}</div>'
                     f'{link} {cites(c.get("sources"), D)}</td>')
        h.append("</tr>")
    h.append("</tbody></table></div>")
    return "".join(h)


def render_orgmap(D):
    """2D map. Nesting means 'grouped under for explanation', NOT a reporting line."""
    T = D["teams"]
    teams = T["teams"]
    if not teams:
        return '<p class="na">Organisational map not yet built.</p>'
    kids = {}
    for t in teams:
        kids.setdefault(t.get("group"), []).append(t)

    def box(t):
        inner = "".join(box(k) for k in kids.get(t["id"], []))
        return (f'<div class="org-box" data-status="{esc(t.get("name_status") or t.get("status") or "")}">'
                f'<a class="teamlink org-name" href="#/teams/{esc(t["id"])}" data-team="{esc(t["id"])}">{esc(t["name"])}</a>'
                f'<div class="org-meta">{badge(t.get("name_status") or t.get("status"))}</div>'
                f'{"<div class=org-kids>" + inner + "</div>" if inner else ""}</div>')

    tops = kids.get(None, []) + kids.get("", [])
    rel_rows = []
    for t in teams:
        for r in t.get("relations") or []:
            rel_rows.append(f'<tr><td>{esc(t["name"])}</td><td><strong>{esc(r.get("type"))}</strong></td><td>{esc(r.get("target"))}</td>'
                            f'<td>{badge(r.get("status"))}</td><td>{inline(r.get("note") or "", D) if r.get("note") else ""} {cites(r.get("sources"), D)}</td></tr>')
    rel = ""
    if rel_rows:
        rel = ('<h4>Relationships between units</h4><p>Four different relationships are kept apart. '
               'Two units that work together are not shown as reporting to each other.</p>'
               '<div class="table-wrap"><table class="rel"><thead><tr><th>Unit</th><th>Relationship</th><th>Target</th><th>Evidence</th><th>Note and sources</th></tr></thead><tbody>'
               + "".join(rel_rows) + "</tbody></table></div>")
    return ('<p class="org-legend"><strong>How to read this map.</strong> A box inside another box means "grouped under it for explanation". '
            'It does <em>not</em> mean "reports to". Reporting lines are shown only in the relationship table, and only where a source supports them.</p>'
            '<div class="org-map">' + "".join(box(t) for t in tops) + "</div>" + rel)


def team_related(t, D):
    pm = t.get("people_match") or {}
    people = []
    for p in D["people"]:
        seg_ok = (not pm.get("segment")) or any(s.lower() in (p.get("segment") or "").lower() for s in pm["segment"])
        cov_ok = (not pm.get("coverage_contains")) or any(c.lower() in ((p.get("coverage") or "") + " " + (p.get("title_public") or "")).lower() for c in pm["coverage_contains"])
        if pm and seg_ok and cov_ok:
            people.append(p)
    ids = set(t.get("mandate_ids") or [])
    tags = set(x.lower() for x in (t.get("mandate_tags") or []))
    mandates = [m for m in D["mandates"] if m.get("id") in ids or (tags and any(tag in json.dumps(m).lower() for tag in tags))]
    dtags = set(t.get("development_tags") or [])
    devs = [d for d in D["developments"] if dtags & set(d.get("teams") or [])]
    return people, mandates, devs


def render_team(t, D):
    people, mandates, devs = team_related(t, D)

    def lst(items, fmt, empty):
        if not items:
            return f'<p class="na">{empty}</p>'
        return "<ul>" + "".join(fmt(i) for i in items) + "</ul>"

    extra = ['<details class="rel-block"><summary>People linked by public evidence (' + str(len(people)) + ")</summary>",
             lst(people, lambda p: f'<li><a href="#/people/{esc(p["id"])}">{esc(p["name"])}</a>, {esc(p.get("title_public") or "title unclear")} '
                 f'<span class="muted">({esc(p.get("confidence") or "?")} confidence)</span></li>',
                 "No one is linked to this unit by public evidence. That is a statement about the evidence, not about headcount."),
             "</details>",
             '<details class="rel-block"><summary>Public mandates and commercial events (' + str(len(mandates)) + ")</summary>",
             lst(mandates, lambda m: f'<li><a href="#/mandates/{esc(m["id"])}">{esc(m.get("client"))}</a>, {esc(m.get("kind") or "")}, {esc(m.get("date") or "date not disclosed")} {badge(m.get("status"))}</li>',
                 "No public mandate is linked to this unit. Public announcements rarely name the originating team."),
             "</details>",
             '<details class="rel-block"><summary>Commercial issues (' + str(len(devs)) + ")</summary>",
             lst(devs, lambda d: f'<li><a href="#/awareness/{esc(d["id"])}">{esc(d.get("title"))}</a> <span class="muted">{esc(d.get("event_date") or "")}</span></li>',
                 "No commercial-awareness card is tagged to this unit yet."),
             "</details>"]
    rels = t.get("relations") or []
    if rels:
        extra.append("<h4>Relationships</h4><ul>" + "".join(
            f'<li><strong>{esc(r.get("type"))}</strong>: {esc(r.get("target"))} {badge(r.get("status"))} {inline(r.get("note"), D) if r.get("note") else ""} {cites(r.get("sources"), D)}</li>'
            for r in rels) + "</ul>")
    e = dict(t)
    e["status"] = t.get("name_status") or t.get("status")
    return card(e, D, "name", F_TEAM, sub=["kind"], cls="card team-card", extra="".join(extra))


def render_tree_node(n, D, depth=1, open_=False):
    kids = "".join(render_tree_node(k, D, depth + 1, open_) for k in (n.get("children") or []))
    rows = "".join(f"<dt>{lab}</dt><dd>{inline(n.get(k), D)}</dd>" for k, lab in [
        ("claim", "Claim"), ("plain_meaning", "Plain-English meaning"), ("actual_task", "The actual task"),
        ("reasoning_or_source", "Reasoning or source"), ("strongest_objection", "Strongest objection"),
        ("boundary", "Where the claim stops being valid")] if n.get(k))
    return (f'<details class="why-node" data-depth="{depth}"{" open" if open_ else ""}><summary><span class="why-depth">Why {depth}</span> '
            f'{inline(n.get("challenge") or n.get("claim") or "", D)}</summary><dl class="kv">{rows}</dl>{kids}</details>')


def render_tree(t, D, open_=False):
    nodes = "".join(render_tree_node(n, D, 1, open_) for n in (t.get("nodes") or []))
    cf = "".join(
        f'<details{" open" if open_ else ""}><summary>{inline(c.get("question"), D)}</summary><dl class="kv">'
        f'<dt>If yes</dt><dd>{inline(c.get("if_yes"), D)}</dd><dt>If no</dt><dd>{inline(c.get("if_no"), D)}</dd>'
        f'<dt>What that suggests</dt><dd>{inline(c.get("what_it_suggests"), D)}</dd></dl></details>'
        for c in (t.get("counterfactuals") or []))
    return (f'<article class="card why-tree" id="{esc(t.get("id"))}" data-search data-kind="why-tree">'
            f'<h3 class="card-title">{esc(t.get("title"))}</h3>'
            f'<p class="card-sub"><span class="layer layer-c">{LAYER["C"]}</span> <span class="idtag">{esc(t.get("id"))}</span></p>'
            f'<p><strong>Opening claim:</strong> {inline(t.get("opening_claim"), D)}</p>'
            f'<div class="box box-warn"><p class="box-title">What this tree does not prove</p><p>{inline(t.get("warning"), D)}</p></div>'
            f'{nodes}<h4>Counterfactual tests</h4>{cf or "<p class=na>None recorded.</p>"}'
            f'<dl class="kv"><dt>Valuable is not the same as enjoyable</dt><dd>{inline(t.get("value_vs_enjoyment"), D)}</dd>'
            f'<dt>An answer that points to a different role</dt><dd>{inline(t.get("different_role_signal"), D)}</dd>'
            f'<dt>Where the tree ends</dt><dd>{inline(t.get("terminus"), D)}</dd></dl></article>')


def render_question(q, D, open_=False):
    op = " open" if open_ else ""
    fu = "".join(
        f'<li><strong>{inline(f.get("q"), D)}</strong>'
        + (f'<br><span class="muted">Why it is asked:</span> {inline(f.get("pressure"), D)}' if f.get("pressure") else "")
        + (f'<br><span class="muted">How to think about it:</span> {inline(f.get("how_to_think"), D)}' if f.get("how_to_think") else "")
        + "</li>" for f in (q.get("followups") or []))
    return (f'<article class="card iq" id="{esc(q.get("id"))}" data-search data-kind="interview" data-category="{esc(q.get("category") or "General")}">'
            f'<h3 class="card-title">{esc(q.get("question"))}</h3>'
            f'<p class="card-sub">{esc(q.get("category") or "")} <span class="idtag">{esc(q.get("id"))}</span></p>'
            f'<details{op}><summary>Underlying argument</summary><div>{value_html(q.get("underlying_argument"), D)}</div>'
            f'<p><strong>Depends on:</strong> {inline(q.get("evidence_needed"), D)} {cites(q.get("sources"), D)}</p></details>'
            f'<details{op}><summary>A weak answer, and why it is weak</summary><blockquote>{inline(q.get("weak_answer"), D)}</blockquote><p>{inline(q.get("why_weak"), D)}</p></details>'
            f'<details{op}><summary>About 30 seconds</summary><p>{inline(q.get("answer_30s"), D)}</p></details>'
            f'<details{op}><summary>About 60 to 90 seconds</summary><p>{inline(q.get("answer_60_90s"), D)}</p></details>'
            f'<details{op}><summary>Harder follow-ups</summary><ol>{fu}</ol></details></article>')


def render_icase(c, D, open_=False):
    op = " open" if open_ else ""
    return (f'<article class="card icase" id="{esc(c.get("id"))}" data-search data-kind="practice-case">'
            f'<h3 class="card-title">{esc(c.get("title"))}</h3><p class="card-sub">{badge("Illustrative example")} <span class="idtag">{esc(c.get("id"))}</span></p>'
            f'<p><strong>Situation:</strong> {inline(c.get("situation"), D)}</p><p><strong>Your role:</strong> {inline(c.get("your_role"), D)}</p>'
            f'<details{op}><summary>What good looks like</summary>{value_html(c.get("what_good_looks_like"), D)}</details>'
            f'<details{op}><summary>Traps</summary>{value_html(c.get("traps"), D)}</details>'
            f'<details{op}><summary>Model reasoning</summary><p>{inline(c.get("model_reasoning"), D)}</p></details>'
            f'<details{op}><summary>Follow-ups</summary>{value_html(c.get("followups"), D)}</details></article>')


def render_case_table(c):
    r = c["result"]
    p = r["params"]
    cur = p["currency"]
    rows = "".join(
        f'<tr><td>Year {y["year"]}{"" if y["months"] == 12 else " (" + str(y["months"]) + " months)"}</td>'
        f'<td>{money(y["avg_fee_base"], cur)}</td><td>{money(y["fees"], cur)}</td>'
        f'<td>{"n/a (no fee-bearing assets)" if y["effective_bps_annualised"] is None else format(y["effective_bps_annualised"], ".1f") + "bp"}</td>'
        f'<td>{money(y["end_balance"], cur)}</td></tr>' for y in r["years"])
    return (f'<div class="case" id="{esc(c["id"])}" data-search data-kind="fee-case"><h4>{esc(c["title"])} {badge("Illustrative example")}</h4>'
            f'<p>{esc(c["teaches"])}</p><div class="table-wrap"><table><thead><tr><th>Period</th><th>Average fee base</th><th>Gross management fee</th>'
            f'<th>Effective annual rate</th><th>Assets at period end</th></tr></thead><tbody>{rows}</tbody>'
            f'<tfoot><tr><th colspan="2">Total over {p["months"]} months</th><th colspan="3">{money(r["total_fees"], cur)}</th></tr></tfoot></table></div></div>')


def render_cases(D, group=None, cid=None):
    out, last = [], None
    for c in D["cases"]["cases"]:
        if group and c["group"] != group:
            continue
        if cid and c["id"] != cid:
            continue
        if c["group"] != last and not cid:
            out.append(f'<h3>{esc(c["group"])}</h3>')
            last = c["group"]
        out.append(render_case_table(c))
    return "".join(out) or '<p class="na">Case not found.</p>'


def render_personal(D):
    P = D.get("personal") or {}
    head = ("<p>This ledger is deliberately empty. No personal records are used in this project, and no experience, feeling or motive has been written on your behalf. "
            "Fill it in yourself, one row per experience, and keep the columns separate: doing something does not show that you enjoyed it.</p>"
            '<div class="table-wrap"><table class="ledger"><thead><tr><th>What happened</th><th>What I actually did</th><th>What I enjoyed or disliked</th>'
            "<th>What this might suggest</th><th>Alternative explanation</th><th>What still needs testing</th></tr></thead><tbody>")
    rows = ""
    for e in P.get("experiences", []):
        rows += "<tr>" + "".join(f"<td>{value_html(e.get(k), D)}</td>" for k in
                                 ("what_happened", "what_i_did", "enjoyed_or_disliked", "might_suggest", "alternative_explanation", "needs_testing")) + "</tr>"
    if not rows:
        rows = ('<tr><td colspan="6" class="na">Empty. Example of the standard to hold yourself to: "Ran the weekly client report for ten weeks" (what I did) is a fact; '
                '"I like client work" is a conclusion that needs a row of its own evidence.</td></tr>')
    qs = "".join(f"<li>{inline(q, D)}</li>" for q in P.get("reflection_questions", []))
    return (head + rows + "</tbody></table></div>"
            + (f"<h4>Reflection questions that would fill the gaps</h4><ol>{qs}</ol>" if qs else ""))


def render_intern_claims(D):
    rows = "".join(
        f'<tr id="{esc(c.get("id"))}" data-search data-kind="claim-audit"><td>{inline(c.get("claim"), D)}</td><td>{badge(c.get("status"))}</td>'
        f'<td>{inline(c.get("finding"), D)} {cites(c.get("sources"), D)}</td><td>{inline(c.get("use_in_interview"), D)}</td></tr>'
        for c in D["intern_claims"])
    if not rows:
        return '<p class="na">Audit not yet written.</p>'
    return ('<div class="table-wrap"><table class="audit"><thead><tr><th>What the former intern said</th><th>Evidence status</th>'
            '<th>What the research found</th><th>How to use it</th></tr></thead><tbody>' + rows + "</tbody></table></div>")


def render_coverage(D):
    rows = "".join(
        f'<tr data-search data-kind="coverage"><td>{esc(c.get("section"))}</td><td>{inline(c.get("topic"), D)}</td><td>{inline(c.get("evidence_found"), D)}</td>'
        f'<td>{inline(c.get("unresolved"), D)}</td><td><strong>{esc(c.get("completion"))}</strong></td></tr>' for c in D["coverage"])
    if not rows:
        return '<p class="na">Coverage register not yet written.</p>'
    return ('<div class="table-wrap"><table class="coverage"><thead><tr><th>Brief section</th><th>Topic</th><th>Evidence found</th>'
            '<th>Unresolved</th><th>Status</th></tr></thead><tbody>' + rows + "</tbody></table></div>")


def render_search_strings(D):
    if not D["search_strings"]:
        return '<p class="na">Search strings not yet recorded.</p>'
    out = []
    for g in D["search_strings"]:
        out.append(f'<h4>{esc(g.get("purpose"))}</h4><pre class="queries">' + esc("\n".join(g.get("queries") or [])) + "</pre>")
    return "".join(out)


def render_sources(D):
    rows = []
    for sid, s in sorted(D["sources"].items()):
        url = s.get("url") or ""
        link = f'<a href="{esc(url)}" rel="noopener noreferrer" target="_blank">{esc(s.get("title") or url)}</a>' if url.startswith("http") else esc(s.get("title") or "")
        rows.append(
            f'<tr id="src-{esc(sid)}" data-search data-kind="source" data-type="{esc(s.get("type") or "other")}" data-stream="{esc(s.get("_stream"))}">'
            f'<td class="idtag">{esc(sid)}</td><td>{link}<div class="muted">{esc(s.get("publisher") or "")}</div></td>'
            f'<td>{esc(s.get("published") or "n.d.")}</td><td>{esc(s.get("type") or "")}{"" if s.get("fetched", True) else " · snippet only"}</td>'
            f'<td>{inline(s.get("note") or "", D) if s.get("note") else ""}</td></tr>')
    return ('<div class="table-wrap"><table class="sources"><thead><tr><th>ID</th><th>Source</th><th>Published</th><th>Type</th><th>What it establishes</th></tr></thead><tbody>'
            + "".join(rows) + "</tbody></table></div>")


def render_claims(D):
    rows = "".join(
        f'<tr id="{esc(c.get("id"))}" data-search data-kind="claim" data-status="{esc(c.get("status"))}"><td class="idtag">{esc(c.get("id"))}</td>'
        f'<td>{inline(c.get("claim"), D)}'
        + (f'<div class="passage">“{esc(c.get("passage"))}”</div>' if c.get("passage") else "")
        + (f'<div class="muted">{inline(c.get("notes"), D)}</div>' if c.get("notes") else "")
        + f'</td><td>{badge(c.get("status"))}</td><td>{esc(c.get("event_date") or c.get("period") or "")}</td><td>{cites(c.get("sources"), D)}</td></tr>'
        for c in D["claims"])
    return ('<div class="table-wrap"><table class="claims"><thead><tr><th>ID</th><th>Claim, supporting passage and limits</th><th>Evidence</th><th>Date or period</th><th>Sources</th></tr></thead><tbody>'
            + rows + "</tbody></table></div>")


def render_people_table(D):
    rows = "".join(
        f'<tr><td><strong>{esc(p.get("name"))}</strong><div class="idtag">{esc(p.get("id"))}</div></td><td>{esc(p.get("title_public") or "Unclear")}<div class="muted">{esc(p.get("office") or "")}</div></td>'
        f'<td>{esc(p.get("coverage") or "Unclear")} · {esc(p.get("segment") or "Unclear")}</td>'
        f'<td>{esc(p.get("function_interpretation") or "Unclear")}<div class="muted">{esc(p.get("confidence") or "")} confidence</div></td>'
        f'<td>{esc(p.get("evidence_date") or "")}<div class="muted">In post at cutoff: {esc(p.get("current_as_of_cutoff") or "Unknown")}</div></td>'
        f'<td>{cites(p.get("sources"), D)}</td></tr>' for p in D["people"])
    return ('<div class="table-wrap"><table class="people"><thead><tr><th>Name</th><th>Public title and office</th><th>Coverage · segment</th>'
            '<th>Function (interpretation)</th><th>Evidence date</th><th>Sources</th></tr></thead><tbody>' + rows + "</tbody></table></div>")


def people_stats(D):
    n = len(D["people"])
    if not n:
        return '<p class="na">No people recorded yet.</p>'

    def count(key):
        c = {}
        for p in D["people"]:
            c[p.get(key) or "Unclear"] = c.get(p.get(key) or "Unclear", 0) + 1
        return c

    f = count("function_interpretation")
    sales, rm = f.get("Sales", 0), f.get("Relationship management", 0)
    other = n - sales - rm
    lines = "".join(f"<li>{esc(k)}: {v}</li>" for k, v in sorted(f.items(), key=lambda kv: -kv[1]))
    seg = "".join(f"<li>{esc(k)}: {v}</li>" for k, v in sorted(count("segment").items(), key=lambda kv: -kv[1]))
    return (f'<div class="box box-warn"><p class="box-title">Observed public-profile sample, not headcount</p>'
            f'<p>The directory holds <strong>{n}</strong> people found in public sources. Of these, <strong>{sales}</strong> are classified as sales, '
            f'<strong>{rm}</strong> as relationship management and <strong>{other}</strong> as blended, leadership, specialist or unclear. '
            f'Numerator and denominator are both this sample. Senior and externally visible people are over-represented, and titles rarely state the function, '
            f'so this says nothing reliable about the real sales-to-relationship-management ratio, team sizes or hiring odds.</p></div>'
            f'<div class="cols2"><div><h4>By function (interpretation)</h4><ul>{lines}</ul></div><div><h4>By client segment</h4><ul>{seg}</ul></div></div>')


# ---------------------------------------------------------------- chapters
def preprocess_md(md, chname):
    out, stack, in_code = [], [], False
    for ln in md.splitlines():
        if ln.strip().startswith("```"):
            in_code = not in_code
            out.append(ln)
            continue
        if not in_code:
            m = re.match(r"^:::\s*([a-z0-9]+)\s*(.*)$", ln)
            if m and m.group(1) in BOX:
                t, title = m.group(1), m.group(2).strip()
                stack.append(t)
                cls = {"l1": "lvl lvl-1", "l2": "lvl lvl-2"}.get(t, f"box box-{t}")
                head = BOX[t] + (f": {title}" if title else "")
                out += ["", f'<div class="{cls}" markdown="1">', "", f'<p class="box-title">{esc(head)}</p>', ""]
                continue
            if m and m.group(1) not in BOX:
                warn(f"{chname}: unknown container :::{m.group(1)}")
            if re.match(r"^:::\s*$", ln):
                if stack:
                    stack.pop()
                    out += ["", "</div>", ""]
                else:
                    warn(f"{chname}: stray closing :::")
                continue
        out.append(ln)
    if stack:
        warn(f"{chname}: unclosed containers {stack}")
        out += ["", "</div>", ""] * len(stack)
    return "\n".join(out)


PLACEHOLDER = re.compile(r"<!--\s*(?:DATA:)?([A-Za-z\-]+)(?::([^>]*?))?\s*-->")


def fill_placeholders(h, D):
    def rep(m):
        name, arg = m.group(1).lower(), (m.group(2) or "").strip()
        if name == "personal-ledger":
            return render_personal(D)
        if name == "case":
            return render_cases(D, cid=arg) if arg.startswith("CASE-") else render_cases(D, group=arg)
        if name == "cases":
            return render_cases(D)
        if name == "teams-matrix":
            return render_matrix(D)
        if name == "org-map":
            return render_orgmap(D)
        if name == "intern-claims":
            return render_intern_claims(D)
        if name == "coverage-register":
            return render_coverage(D)
        if name == "people-summary":
            return people_stats(D)
        if name == "search-strings":
            return render_search_strings(D)
        if name == "compensation-evidence":
            warn("placeholder COMPENSATION-EVIDENCE still present")
            return ""
        return m.group(0)
    return PLACEHOLDER.sub(rep, h)


def render_chapter(path, D):
    chid = "ch" + path.name[:2]
    md = path.read_text(encoding="utf-8")
    if REDACT.search(md):
        warn(f"{path.name}: withheld client name found in chapter text; redacted")
        md = REDACT.sub(REDACT_TEXT, md)
    pre = preprocess_md(md, path.name)
    h = markdown.markdown(pre, extensions=["tables", "md_in_html", "sane_lists", "fenced_code"])
    h = fill_placeholders(h, D)
    h = decorate(h, D)
    h = h.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    h = h.replace('<div class="table-wrap"><div class="table-wrap">', '<div class="table-wrap">').replace("</table></div></div>", "</table></div>")
    leftovers = re.findall(r"\{\{[^}]{1,12}\}\}|\[@[^\]]{1,30}\]", h)
    if leftovers:
        warn(f"{path.name}: unprocessed markers {sorted(set(leftovers))[:8]}")
    used, outline, title = set(), [], path.stem

    def hid(m):
        nonlocal title
        lvl, inner = int(m.group(1)), m.group(2)
        text = strip_tags(inner)
        if lvl == 1:
            title = text
            return f'<h1 id="{chid}">{inner}</h1>'
        base = f"{chid}-{slug(text)}"
        i, sid = 2, base
        while sid in used:
            sid = f"{base}-{i}"
            i += 1
        used.add(sid)
        if lvl <= 3:
            outline.append({"id": sid, "title": text, "level": lvl})
        return f'<h{lvl} id="{sid}">{inner}</h{lvl}>'

    h = re.sub(r"<h([1-4])>(.*?)</h\1>", hid, h, flags=re.S)
    # wrap h2 sections for search
    parts = re.split(r'(?=<h2 id=")', h)
    body = parts[0]
    for part in parts[1:]:
        sid = re.match(r'<h2 id="([^"]+)"', part).group(1)
        body += f'<section class="sec" data-search data-kind="chapter" data-sec="{sid}">{part}</section>'
    words = len(strip_tags(h).split())
    return {"id": chid, "file": path.name, "title": title, "html": body, "outline": outline, "words": words, "md": md}


def md_export_chapter(md):
    """Chapter Markdown -> portable Markdown for the master dossier."""
    out, stack = [], []
    for ln in md.splitlines():
        m = re.match(r"^:::\s*([a-z0-9]+)\s*(.*)$", ln)
        if m and m.group(1) in BOX:
            stack.append(m.group(1))
            head = BOX[m.group(1)] + (f": {m.group(2).strip()}" if m.group(2).strip() else "")
            out += ["", ">" * len(stack) + f" **[{head}]**", ">" * len(stack)]
            continue
        if re.match(r"^:::\s*$", ln) and stack:
            stack.pop()
            out.append("")
            continue
        out.append((">" * len(stack) + " " + ln) if stack else ln)
    t = "\n".join(out)
    t = RE_BADGE.sub(lambda m: f"*[{CODE2STATUS[m.group(1)]}]*", t)
    t = RE_LAYER.sub(lambda m: f"*[{LAYER[m.group(1)]}]*", t)
    t = RE_CITE.sub(lambda m: f"[{m.group(1)}]", t)
    return t


def md_value(v, indent=0):
    pad = "  " * indent
    if v is None or v == "" or v == []:
        return "Not publicly disclosed"
    if isinstance(v, str):
        t = RE_BADGE.sub(lambda m: f"[{CODE2STATUS[m.group(1)]}]", v)
        return RE_CITE.sub(lambda m: f"[{m.group(1)}]", t).replace("\n", " ")
    if isinstance(v, list):
        return "".join(f"\n{pad}  - {md_value(x, indent + 1)}" for x in v)
    if isinstance(v, dict):
        return "".join(f"\n{pad}  - **{label(k)}:** {md_value(x, indent + 1)}" for k, x in v.items() if not k.startswith("_"))
    return str(v)


def md_entity(e, title_key, fields, level="###"):
    lines = [f"{level} {e.get(title_key) or '(unnamed)'} `{e.get('id', '')}`", ""]
    if e.get("status"):
        lines.append(f"- **Evidence status:** {e['status']}")
    for k, lab in fields:
        if k in e:
            lines.append(f"- **{lab}:** {md_value(e.get(k))}")
    if e.get("sources"):
        lines.append(f"- **Sources:** {', '.join(e['sources'])}")
    lines.append("")
    return "\n".join(lines)


def md_tree_node(n, depth=1):
    pad = "  " * (depth - 1)
    out = [f"{pad}- **Why {depth}: {md_value(n.get('challenge') or '')}**"]
    for k, lab in [("claim", "Claim"), ("plain_meaning", "Plain meaning"), ("actual_task", "Actual task"), ("reasoning_or_source", "Reasoning or source"),
                   ("strongest_objection", "Strongest objection"), ("boundary", "Boundary")]:
        if n.get(k):
            out.append(f"{pad}  - *{lab}:* {md_value(n[k])}")
    for k in n.get("children") or []:
        out.append(md_tree_node(k, depth + 1))
    return "\n".join(out)


def build_dossier_md(chapters, D):
    L = ["# GSAM Client Solutions Group 2027: Master Dossier", "",
         f"Research date and information cutoff: {RESEARCH_DATE}. Generated by `build/build.py` from `content/` and `data/`. "
         "The interactive study application and the PDF are generated from the same files.", "",
         "Evidence statuses: " + " · ".join(STATUS), "",
         "Citations appear as source IDs in square brackets, for example `[R2-S01]`, and resolve in Appendix O.", "", "## Contents", ""]
    for c in chapters:
        L.append(f"- {c['title']}")
    L += ["- Appendices A to P: teams, people, mandates, developments, competitors, lifecycle, roles, why-trees, interview bank, fee cases, glossary, claim audit, coverage register, search strings, sources, claims", ""]
    for c in chapters:
        L += [md_export_chapter(c["md"]), "", "---", ""]
    T = D["teams"]
    L += ["# Appendix A: Teams and coverage", ""]
    for t in T["teams"]:
        e = dict(t)
        e["status"] = t.get("name_status") or t.get("status")
        L.append(md_entity(e, "name", F_TEAM + [("relations", "Relationships")]))
    L += ["## Coverage matrix", "", "| Geography | Segment | Evidence | Note | Sources |", "|---|---|---|---|---|"]
    gname = {g["id"]: g["name"] for g in T["axes"]["geographies"]}
    sname = {s["id"]: s["name"] for s in T["axes"]["segments"]}
    for c in T["matrix"]:
        L.append(f"| {gname.get(c['geo'], c['geo'])} | {sname.get(c['segment'], c['segment'])} | {c.get('status')} | {md_value(c.get('note'))} | {', '.join(c.get('sources') or [])} |")
    L += ["", "# Appendix B: Public people directory", "",
          "Public professional information only. Titles are as publicly stated on the evidence date. The function column is our interpretation.", ""]
    for p in D["people"]:
        L.append(md_entity(p, "name", [("title_public", "Public title"), ("office", "Office")] + F_PEOPLE))
    L += ["# Appendix C: Mandates and commercial events", ""]
    for m in D["mandates"]:
        L.append(md_entity(m, "client", F_MANDATE))
    L += ["# Appendix D: Commercial developments", ""]
    for d in D["developments"]:
        L.append(md_entity(d, "title", [("teams", "Teams")] + F_DEV))
    L += ["# Appendix E: Competitors", ""]
    for c in D["competitors"]:
        L.append(md_entity(c, "name", F_COMP))
    L += ["# Appendix F: Client lifecycle", ""]
    for s in D["lifecycle"].get("stages", []):
        L.append(md_entity(s, "name", F_STAGE))
    if D["lifecycle"].get("tpw_variant"):
        L += ["## Wealth-intermediary variant", ""]
        for s in D["lifecycle"]["tpw_variant"]:
            L.append(md_entity(s, "name", F_STAGE + [(k, label(k)) for k in s if k not in dict(F_STAGE) and k not in ("id", "name")]))
    L += ["# Appendix G: Roles and decision rights", ""]
    for r in D["roles"]:
        r2 = dict(r)
        r2["status"] = r.get("evidence_status")
        L.append(md_entity(r2, "name", F_ROLE))
    L += ["# Appendix H: Why-trees", ""]
    for t in D["why"].get("trees", []):
        L += [f"### {t.get('title')} `{t.get('id')}`", "", f"**Opening claim:** {md_value(t.get('opening_claim'))}", "",
              f"**What this does not prove:** {md_value(t.get('warning'))}", ""]
        L += [md_tree_node(n) for n in t.get("nodes") or []]
        L += ["", "**Counterfactual tests**", ""]
        for c in t.get("counterfactuals") or []:
            L.append(f"- {md_value(c.get('question'))}\n  - If yes: {md_value(c.get('if_yes'))}\n  - If no: {md_value(c.get('if_no'))}\n  - Suggests: {md_value(c.get('what_it_suggests'))}")
        L += ["", f"**Valuable is not enjoyable:** {md_value(t.get('value_vs_enjoyment'))}", "",
              f"**Signal for a different role:** {md_value(t.get('different_role_signal'))}", "", f"**Terminus:** {md_value(t.get('terminus'))}", ""]
    L += ["# Appendix I: Interview practice bank", "", md_value(D["interview"].get("framework_note") or ""), ""]
    for q in D["interview"].get("questions", []):
        L.append(md_entity(q, "question", [("category", "Category"), ("underlying_argument", "Underlying argument"), ("evidence_needed", "Depends on"),
                                            ("weak_answer", "Weak answer"), ("why_weak", "Why it is weak"), ("answer_30s", "About 30 seconds"),
                                            ("answer_60_90s", "About 60 to 90 seconds"), ("followups", "Follow-ups")]))
    for c in D["interview"].get("cases", []):
        L.append(md_entity(c, "title", [("situation", "Situation"), ("your_role", "Your role"), ("what_good_looks_like", "What good looks like"),
                                         ("traps", "Traps"), ("model_reasoning", "Model reasoning"), ("followups", "Follow-ups")]))
    L += ["# Appendix J: Illustrative fee cases", "", D["cases"].get("note", ""), ""]
    for c in D["cases"]["cases"]:
        r = c["result"]
        L += [f"### {c['title']} `{c['id']}`", "", c["teaches"], "", "| Period | Average fee base | Gross management fee | Effective annual rate |", "|---|---|---|---|"]
        for y in r["years"]:
            eff = "n/a" if y["effective_bps_annualised"] is None else f"{y['effective_bps_annualised']:.1f}bp"
            L.append(f"| Year {y['year']} | {money(y['avg_fee_base'])} | {money(y['fees'])} | {eff} |")
        L += [f"| **Total** | | **{money(r['total_fees'])}** | |", ""]
    L += ["# Appendix K: Glossary", ""]
    for g in D["glossary"]:
        L.append(f"- **{g.get('term')}**" + (f" ({g.get('expansion')})" if g.get("expansion") else "") + f": {md_value(g.get('plain'))} "
                 + (f"*Mechanics:* {md_value(g.get('technical'))} " if g.get("technical") else "")
                 + (f"*Why it matters:* {md_value(g.get('why_it_matters'))}" if g.get("why_it_matters") else ""))
    L += ["", "# Appendix L: Audit of the former intern's claims", "", "| Claim | Status | Finding | Sources |", "|---|---|---|---|"]
    for c in D["intern_claims"]:
        L.append(f"| {md_value(c.get('claim'))} | {c.get('status')} | {md_value(c.get('finding'))} | {', '.join(c.get('sources') or [])} |")
    L += ["", "# Appendix M: Coverage register", "", "| Section | Topic | Evidence found | Unresolved | Status |", "|---|---|---|---|---|"]
    for c in D["coverage"]:
        L.append(f"| {c.get('section')} | {md_value(c.get('topic'))} | {md_value(c.get('evidence_found'))} | {md_value(c.get('unresolved'))} | {c.get('completion')} |")
    L += ["", "# Appendix N: Reproducible search strings", ""]
    for g in D["search_strings"]:
        L += [f"**{g.get('purpose')}**", "", "```", *(g.get("queries") or []), "```", ""]
    L += ["# Appendix O: Source register", "", "| ID | Source | Publisher | Published | Type | URL |", "|---|---|---|---|---|---|"]
    for sid, s in sorted(D["sources"].items()):
        L.append(f"| {sid} | {(s.get('title') or '').replace('|', '/')} | {(s.get('publisher') or '').replace('|', '/')} | {s.get('published') or 'n.d.'} | {s.get('type') or ''}{'' if s.get('fetched', True) else ' (snippet only)'} | {s.get('url') or ''} |")
    L += ["", "# Appendix P: Claim register", "", "| ID | Claim | Status | Sources |", "|---|---|---|---|"]
    for c in D["claims"]:
        L.append(f"| {c.get('id')} | {md_value(c.get('claim')).replace('|', '/')} | {c.get('status')} | {', '.join(c.get('sources') or [])} |")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- assemble views
def build_views(chapters, D, print_mode=False):
    op = print_mode
    V = {}
    T = D["teams"]
    V["matrix"] = render_matrix(D)
    V["orgmap"] = render_orgmap(D)
    V["teams"] = "".join(render_team(t, D) for t in T["teams"]) or '<p class="na">No team profiles yet.</p>'
    V["people"] = "".join(card(p, D, "name", F_PEOPLE, sub=["title_public", "office"], status_key=None,
                               data_attrs=["segment", "title_class", "function_interpretation", "confidence", "current_as_of_cutoff"], cls="card person")
                          for p in D["people"])
    V["people_table"] = render_people_table(D)
    V["people_stats"] = people_stats(D)
    V["mandates"] = "".join(card(m, D, "client", F_MANDATE, sub=["kind", "date"], data_attrs=["kind", "country", "status", "client_type"], cls="card mandate")
                            for m in D["mandates"])
    V["developments"] = "".join(card(d, D, "title", F_DEV, sub=["event_date"], data_attrs=["teams", "status"], cls="card dev",
                                     extra="") for d in D["developments"])
    V["competitors"] = "".join(card(c, D, "name", F_COMP, data_attrs=["relevant_to"], status_key=None, cls="card comp") for c in D["competitors"])
    roles = []
    for r in D["roles"]:
        r2 = dict(r)
        r2["status"] = r.get("evidence_status")
        roles.append(card(r2, D, "name", F_ROLE, cls="card role"))
    V["roles"] = "".join(roles)
    V["lifecycle"] = "".join(card(s, D, "name", F_STAGE, status_key=None, cls="card stage") for s in D["lifecycle"].get("stages", []))
    V["lifecycle_tpw"] = "".join(
        card(s, D, "name", F_STAGE + [(k, label(k)) for k in s if k not in dict(F_STAGE) and k not in ("id", "name") and not k.startswith("_")],
             status_key=None, cls="card stage") for s in D["lifecycle"].get("tpw_variant", []))
    V["why"] = "".join(render_tree(t, D, op) for t in D["why"].get("trees", []))
    I = D["interview"]
    V["criteria"] = "".join(f'<li><strong>{esc(c.get("name"))}</strong>: {inline(c.get("description"), D)}</li>' for c in I.get("criteria", []))
    V["framework_note"] = inline(I.get("framework_note") or "", D) if I.get("framework_note") else ""
    V["questions"] = "".join(render_question(q, D, op) for q in I.get("questions", []))
    V["icases"] = "".join(render_icase(c, D, op) for c in I.get("cases", []))
    V["cases"] = render_cases(D)
    V["glossary"] = "".join(
        f'<article class="card gloss" id="{esc(g.get("id"))}" data-search data-kind="glossary" data-term="{esc((g.get("term") or "").lower())}">'
        f'<h3 class="card-title">{esc(g.get("term"))}{" · <span class=expansion>" + esc(g.get("expansion")) + "</span>" if g.get("expansion") and g.get("expansion") != g.get("term") else ""}</h3>'
        f'<dl class="kv">' + "".join(f"<dt>{lab}</dt><dd>{inline(g.get(k), D)}</dd>" for k, lab in F_GLOSS if g.get(k)) + "</dl>"
        + (f'<p class="muted">Sources: {cites(g.get("sources"), D)}</p>' if g.get("sources") else "") + "</article>" for g in D["glossary"])
    V["sources"] = render_sources(D)
    V["claims"] = render_claims(D)
    V["intern_claims"] = render_intern_claims(D)
    V["coverage"] = render_coverage(D)
    V["search_strings"] = render_search_strings(D)
    V["personal"] = render_personal(D)
    routes = []
    for r in D["routes"]:
        steps = "".join(f'<li><label><input type="checkbox" class="route-step" data-step="{esc(r["id"])}:{i}"> '
                        f'<a href="{esc(s["href"])}">{esc(s["label"])}</a></label><span class="muted"> {esc(s.get("why") or "")}</span></li>'
                        for i, s in enumerate(r.get("steps", [])))
        routes.append(f'<article class="card route" id="{esc(r["id"])}"><h3 class="card-title">{esc(r["title"])}</h3>'
                      f'<p class="card-sub">{esc(r.get("time") or "")}</p><p>{esc(r.get("purpose") or "")}</p><ol>{steps}</ol></article>')
    V["routes"] = "".join(routes)
    V["chapters"] = "".join(f'<article class="chapter" id="art-{c["id"]}" data-chapter="{c["id"]}">{c["html"]}</article>' for c in chapters)
    V["chapter_nav"] = "".join(
        f'<li><a href="#/read/{c["id"]}" data-chapter-link="{c["id"]}">{esc(c["title"])}</a><ul>'
        + "".join(f'<li><a href="#/read/{c["id"]}/{o["id"]}">{esc(o["title"])}</a></li>' for o in c["outline"] if o["level"] == 2)
        + "</ul></li>" for c in chapters)
    counts = {"sources": len(D["sources"]), "claims": len(D["claims"]), "people": len(D["people"]), "mandates": len(D["mandates"]),
              "developments": len(D["developments"]), "glossary": len(D["glossary"]), "teams": len(T["teams"]),
              "words": sum(c["words"] for c in chapters)}
    sc = {}
    for c in D["claims"]:
        sc[c.get("status")] = sc.get(c.get("status"), 0) + 1
    V["status_counts"] = "".join(f"<li>{badge(k)} {v} claims</li>" for k, v in sorted(sc.items(), key=lambda kv: -kv[1]))
    V["legend"] = "".join(f"<li>{badge(k)} {esc(v)}</li>" for k, v in STATUS_HELP.items())
    V["counts"] = counts
    return V


def fill(template, mapping):
    def rep(m):
        k = m.group(1)
        if k not in mapping:
            warn(f"template slot {k} has no value")
            return ""
        return str(mapping[k])
    return re.sub(r"\[\[([a-z_0-9.]+)\]\]", rep, template)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", action="store_true")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    D = load_all()
    chapters = [render_chapter(p, D) for p in sorted((ROOT / "content" / "chapters").glob("[0-9][0-9]-*.md"))]
    suffix = ""

    (ROOT / "dossier").mkdir(exist_ok=True)
    (ROOT / "dossier" / f"GSAM_CSG_2027_Master_Dossier{suffix}.md").write_text(build_dossier_md(chapters, D), encoding="utf-8")

    app = ROOT / "build" / "app"
    V = build_views(chapters, D)
    counts = V.pop("counts")
    js_data = {
        "matrix": D["teams"]["matrix"], "axes": D["teams"]["axes"],
        "teams": [{"id": t["id"], "name": t["name"], "status": t.get("name_status") or t.get("status")} for t in D["teams"]["teams"]],
        "glossary": [{"id": g.get("id"), "term": g.get("term"), "expansion": g.get("expansion"), "plain": g.get("plain")} for g in D["glossary"]],
        "cases": [{"id": c["id"], "group": c["group"], "title": c["title"], "teaches": c["teaches"], "params": c["params"],
                   "expected_total": c["result"]["total_fees"]} for c in D["cases"]["cases"]],
        "criteria": D["interview"].get("criteria", []),
        "sources": {k: {"t": s.get("title"), "p": s.get("publisher"), "u": s.get("url"), "d": s.get("published")} for k, s in D["sources"].items()},
    }
    mapping = dict(V)
    mapping.update({f"n_{k}": f"{v:,}" for k, v in counts.items()})
    mapping.update({
        "css": (app / "app.css").read_text(encoding="utf-8"),
        "js": (app / "app.js").read_text(encoding="utf-8"),
        "data_json": json.dumps(js_data, ensure_ascii=False).replace("</", "<\\/"),
        "research_date": RESEARCH_DATE,
        "built": datetime.date(2026, 11, 14).isoformat(),
        "public_note": "No personal records are used: the personal-fit ledger is a blank template for you to fill in.",
    })
    page = fill((app / "template.html").read_text(encoding="utf-8"), mapping)
    (ROOT / f"gsam_csg_command_center{suffix}.html").write_text(page, encoding="utf-8")

    PV = build_views(chapters, D, print_mode=True)
    pcounts = PV.pop("counts")
    pm = dict(PV)
    pm.update({f"n_{k}": f"{v:,}" for k, v in pcounts.items()})
    toc = []
    for c in chapters:
        toc.append(f'<li class="toc-ch"><a href="#{c["id"]}"><span class="toc-t">{esc(c["title"])}</span><span class="toc-p" data-dest="{c["id"]}"></span></a></li>')
        for o in c["outline"]:
            if o["level"] == 2:
                toc.append(f'<li class="toc-sec"><a href="#{o["id"]}"><span class="toc-t">{esc(o["title"])}</span><span class="toc-p" data-dest="{o["id"]}"></span></a></li>')
    pm.update({
        "css": (app / "app.css").read_text(encoding="utf-8") + "\n" + (app / "print.css").read_text(encoding="utf-8"),
        "toc": "".join(toc), "research_date": RESEARCH_DATE,
        "chapters": "".join(f'<article class="chapter" id="art-{c["id"]}">{c["html"]}</article>' for c in chapters),
        "public_note": mapping["public_note"],
    })
    (OUT / f"print{suffix}.html").write_text(fill((app / "print_template.html").read_text(encoding="utf-8"), pm), encoding="utf-8")

    report = {"warnings": WARN, "counts": counts, "chapters": [{"id": c["id"], "file": c["file"], "title": c["title"], "words": c["words"]} for c in chapters]}
    (OUT / "build_report.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    print(f"chapters={len(chapters)} words={counts['words']:,} sources={counts['sources']} claims={counts['claims']} people={counts['people']} "
          f"mandates={counts['mandates']} developments={counts['developments']} glossary={counts['glossary']} warnings={len(WARN)}")
    for w in WARN[:40]:
        print("  WARN", w)
    if a.pdf:
        subprocess.run(["node", str(ROOT / "build" / "make_pdf.js"), str(OUT / f"print{suffix}.html"),
                        str(ROOT / f"GSAM_CSG_2027_Dossier{suffix}.pdf")], check=True)


if __name__ == "__main__":
    main()
