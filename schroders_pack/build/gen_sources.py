#!/usr/bin/env python3
"""Build Part 15 source table from research files; verify every cited [Sxx] resolves."""
import glob, html, json, os, re
ROOT = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(os.path.dirname(ROOT), "research")
src = {}
for f in sorted(glob.glob(os.path.join(RES, "WS*.md"))):
    ws = os.path.basename(f).split("_")[0]
    for line in open(f):
        l = line.strip()
        m = re.match(r"^[-|\s]*`?\[S(\d+)\]`?\s*\|(.*)$", l)
        if not m:
            continue
        n = int(m.group(1))
        parts = [p.strip() for p in m.group(2).strip().strip("|").split("|")]
        if len(parts) < 4:
            continue
        # normalise: outlet, title, date, url, accessed, status, note
        parts += [""] * (7 - len(parts))
        outlet, title, date, url, acc, status, note = parts[:7]
        acc = acc.replace("Accessed ", "")
        if n not in src:
            src[n] = dict(ws=ws, outlet=outlet, title=title, date=date, url=url, acc=acc, status=status, note=note)
own = {
 401: dict(ws="Main", outlet="FCA Handbook", title="COBS 4.2 Fair, clear and not misleading communications (COBS 4.2.1R)", date="current", url="https://www.handbook.fca.org.uk/handbook/COBS/4/2.html", acc="2026-09-29", status="FETCHED", note="Primary; rule text quoted"),
 402: dict(ws="Main", outlet="FCA", title="UK Market Abuse Regulation (UK MAR) overview", date="current", url="https://www.fca.org.uk/markets/market-abuse/regulation", acc="2026-09-29", status="FETCHED", note="Primary; inside information definition quoted"),
 403: dict(ws="Main", outlet="ICO", title="A guide to the data protection principles (UK GDPR)", date="current", url="https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/", acc="2026-09-29", status="FETCHED", note="Primary; accuracy and security principles quoted"),
}
src.update(own)
# cited ids
cited = set()
km = json.load(open(os.path.join(ROOT, "keymap.json")))
texts = [open(p).read() for p in [p for p in glob.glob(os.path.join(ROOT, "parts", "*.html")) if "150_sources" not in p] + glob.glob(os.path.join(ROOT, "fragments", "*.html"))]
texts += list(km.values())
for t in texts:
    for grp in re.findall(r"\[(S\d+(?:[,–\- ]+S?\d+)*)\]", t):
        for n in re.findall(r"\d+", grp):
            cited.add(int(n))
missing = sorted(c for c in cited if c not in src)
print("sources parsed:", len(src), "cited:", len(cited), "missing:", missing)
rows = []
for n in sorted(src):
    s = src[n]
    e = lambda x: html.escape(x.strip("`* ").replace("\u2014", "-").replace("\u2013", "-"))
    grey = "" if n in cited else " style='color:#7A808C'"
    rows.append(f"<p class='srow'{grey}><b>[S{n}]</b> {e(s['outlet'])}. <i>{e(s['title'])}</i>. {e(s['date'])}. "
                f"<span class='url'>{e(s['url'])}</span> Accessed {e(s['acc'])}. <b>{e(s['status'])}</b>. {e(s['note'])}</p>")
body = f'''<section class="part">
<div class="part-band" style="--band:#6B7A8F"><div class="pn">Part 15</div><h1 class="ph">Source table</h1>
<p class="lede">Every source marker in the pack, with outlet, title, publication date, URL, access date and how it was read. {len(src)} sources; {len(cited)} cited in the text. Grey rows were gathered in research but not cited.</p></div>
<p class="small"><b>Status:</b> FETCHED = page or PDF read in full; SNIPPET = seen only as a search-result summary (treat as [Reported]); PAYWALLED = headline only, not read. Ranges by workstream: S1 to S57 role and team; S70 to S108 firm; S120 to S149 competitors; S150 to S199 industry and regulation; S220 to S259 news; S260 to S298 interview process and Cappfinity; S300 to S330 why Schroders; S401 to S403 added during writing. Some documents appear under more than one ID because workstreams ran in parallel (for example the H1 2026 results are S28, S70, S120, S220 and S302); all resolve to the same document.</p>
<p class="small"><b>Format:</b> [ID] Outlet. <i>Title</i>. Publication date. URL. Access date. Status. Confidence note.</p>
<div class="srcs">{"".join(rows)}</div>
</section>'''
open(os.path.join(ROOT, "parts", "150_sources.html"), "w").write(body)
