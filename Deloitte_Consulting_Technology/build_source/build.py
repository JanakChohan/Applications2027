#!/usr/bin/env python3
"""Assemble parts -> HTML, two-pass render with real TOC page numbers, stamp running header/footer."""
import re, os, sys, glob, base64, subprocess, html, json
import pymupdf
B = os.path.dirname(os.path.abspath(__file__))
SP = os.path.dirname(B)
OUTNAME = sys.argv[1] if len(sys.argv) > 1 else "Deloitte_Consulting_Technology_Complete_Interview_Pack"
NODE_PATH = subprocess.run(["npm","root","-g"],capture_output=True,text=True).stdout.strip()

def b64(p): return base64.b64encode(open(p,"rb").read()).decode()
css = open(f"{B}/style.css").read().replace("__INTER__", b64(f"{B}/fonts/inter.woff2")).replace("__SERIF__", b64(f"{B}/fonts/serif.woff2"))

# ---------- sources ----------
src_rows = {}
for f in sorted(glob.glob(f"{SP}/findings/*.md")):
    for line in open(f):
        m = re.match(r"\s*[`\-\*]*\s*\[(S\d+)\]\s*\|(.*)", line)
        if m:
            sid = m.group(1); rest = [c.strip().strip("`") for c in m.group(2).split("|")]
            if sid not in src_rows: src_rows[sid] = rest
extra = f"{B}/extra_sources.md"
if os.path.exists(extra):
    for line in open(extra):
        m = re.match(r"\s*\[(S\d+)\]\s*\|(.*)", line)
        if m: src_rows[m.group(1)] = [c.strip() for c in m.group(2).split("|")]

def sid_key(s): return int(s[1:])

def build_source_table():
    rows = []
    for sid in sorted(src_rows, key=sid_key):
        c = src_rows[sid] + [""]*8
        outlet, title, pub, url, acc, status = c[0], c[1], c[2], c[3], c[4], c[5]
        note = " | ".join(x for x in c[6:] if x)
        u = html.escape(url)
        rows.append(f'<tr id="{sid}"><td style="white-space:nowrap"><b>{sid}</b></td><td>{html.escape(outlet)}</td><td>{html.escape(title)}</td><td>{html.escape(pub)}</td><td class="u">{u}</td><td>{html.escape(status)}</td><td>{html.escape(note)}</td></tr>')
    return ('<table class="data small srctab"><thead><tr><th style="width:5.5%">ID</th><th style="width:11%">Outlet</th><th style="width:22%">Title</th><th style="width:8%">Published</th><th style="width:28%">URL (all accessed 2026-10-04)</th><th style="width:7.5%">Status</th><th>Note</th></tr></thead><tbody>'
            + "\n".join(rows) + "</tbody></table>")

# ---------- transforms outside svg ----------
BADGE = {"Confirmed":"c-conf","Reported":"c-rep","Inferred":"c-inf","Estimate":"c-rep","Anecdote":"c-rep"}
def xform_text(t):
    t = re.sub(r"\[((?:S\d+)(?:\s*[,;/]\s*S\d+)*)\]", lambda m: "".join(f'<a class="s" href="#{s}">[{s}]</a>' for s in re.findall(r"S\d+", m.group(1))), t)
    t = re.sub(r"\[(Confirmed|Reported|Inferred|Estimate|Anecdote)\]", lambda m: f'<span class="c {BADGE[m.group(1)]}">{m.group(1)}</span>', t)
    t = t.replace(" — ", ", ").replace("—", ", ")
    return t
def xform(h):
    out, pos = [], 0
    for m in re.finditer(r"<svg\b.*?</svg>", h, flags=re.S):
        out.append(xform_text(h[pos:m.start()])); out.append(m.group(0).replace("—","-")); pos = m.end()
    out.append(xform_text(h[pos:])); return "".join(out)

# ---------- assemble ----------
parts = sorted(glob.glob(f"{B}/parts/p*.html"))
body = []
toc_entries = []  # (level, id, title)
hcount = 0
for p in parts:
    h = open(p).read()
    if "__SOURCE_TABLE__" in h: h = h.replace("__SOURCE_TABLE__", build_source_table())
    h = xform(h)
    # part id/title
    def part_sub(m):
        return m.group(0)
    for m in re.finditer(r'<section class="part[^"]*" id="(p\d+[a-z]?)"[^>]*data-title="([^"]+)"', h):
        toc_entries.append((1, m.group(1), m.group(2)))
    def h2sub(m):
        global hcount
        attrs, inner = m.group(1), m.group(2)
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm: hid = idm.group(1)
        else:
            hcount += 1; hid = f"h{hcount}"; attrs += f' id="{hid}"'
        txt = re.sub(r"<[^>]+>", "", inner)
        toc_entries.append((2, hid, txt))
        return f'<h2{attrs}><span class="marker" data-mk="{hid}"></span>{inner}</h2>'
    # process sequentially to keep order: split by sections
    h = re.sub(r'(<section class="part[^"]*" id="(p\d+[a-z]?)"[^>]*>)', lambda m: m.group(1)+f'<span class="marker" data-mk="{m.group(2)}"></span>', h)
    # rebuild toc order: entries were added part-first; fix by recomputing order below
    h = re.sub(r"<h2([^>]*)>(.*?)</h2>", h2sub, h, flags=re.S)
    body.append(h)
full = "\n".join(body)
# ordered toc by position in document
order = []
for m in re.finditer(r'data-mk="([A-Za-z0-9_\-]+)"', full): order.append(m.group(1))
tdict = {e[1]:e for e in toc_entries}
toc_ordered = [tdict[i] for i in order if i in tdict]

def toc_html(pages):
    rows = []
    for lvl, i, t in toc_ordered:
        pg = pages.get(i, "")
        cls = "tp" if lvl == 1 else "ts"
        rows.append(f'<a href="#{i}" class="{cls}"><span class="tt">{t}</span><span class="pg">{pg}</span></a>')
    return "\n".join(rows)

def doc(pages):
    cover = open(f"{B}/cover.html").read()
    toc = f'<section class="part" id="toc" data-title="Contents"><div class="band"><span class="pnum">Contents</span><h1>What is in this pack</h1></div><div class="toc">{toc_html(pages)}</div></section>'
    return f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>Deloitte Consulting Interview Pack</title><style>{css}</style></head><body>{cover}{toc}{full}</body></html>'

def render(htmltext, pdf):
    hp = f"{B}/{OUTNAME}.html"; open(hp,"w").write(htmltext)
    subprocess.run(["node", f"{B}/render.js", hp, pdf], check=True, env={**os.environ, "NODE_PATH": NODE_PATH})
    return hp

def find_pages(pdf):
    """Map anchor id -> 1-based page using the named destinations Chromium writes for the contents links."""
    d = pymupdf.open(pdf); res = {}
    for pg in d:
        for L in pg.get_links():
            if L.get("nameddest") and L.get("page", -1) >= 0:
                res.setdefault(L["nameddest"], L["page"] + 1)
    return res, len(d)

tmp = f"{B}/pass.pdf"
# pass 1 with placeholder numbers of same width
render(doc({e[1]:"000" for e in toc_ordered}), tmp)
pages, n = find_pages(tmp)
render(doc(pages), tmp)
pages2, n2 = find_pages(tmp)
if pages2 != pages:
    print("page map shifted; third pass"); pages = pages2; render(doc(pages), tmp); pages, n2 = find_pages(tmp)
# stamp header/footer
d = pymupdf.open(tmp)
part_starts = sorted([(pages[e[1]], e[2]) for e in toc_ordered if e[0]==1 and e[1] in pages])
for i, pg in enumerate(d):
    pno = i+1
    if pno == 1: continue
    cur = ""
    for s, t in part_starts:
        if s <= pno: cur = t
    W, H = pg.rect.width, pg.rect.height
    pg.insert_text((48, 32), "DELOITTE UK  |  CONSULTING & TECHNOLOGY  |  INTERVIEW RESEARCH PACK", fontsize=6.5, fontname="hebo", color=(0.055,0.133,0.25))
    tw = pymupdf.get_text_length(cur, fontname="helv", fontsize=7)
    pg.insert_text((W-48-tw, 32), cur, fontsize=7, fontname="helv", color=(0.36,0.4,0.47))
    pg.draw_line((48, 37), (W-48, 37), color=(0.85,0.87,0.9), width=0.5)
    pg.draw_line((48, H-36), (W-48, H-36), color=(0.85,0.87,0.9), width=0.5)
    pg.insert_text((48, H-24), "Built from public sources only. Sources in Part 15. Prepared 4 October 2026.", fontsize=6.5, fontname="helv", color=(0.36,0.4,0.47))
    t = f"Page {pno} of {len(d)}"; tw = pymupdf.get_text_length(t, fontname="hebo", fontsize=7.5)
    pg.insert_text((W-48-tw, H-24), t, fontsize=7.5, fontname="hebo", color=(0.055,0.133,0.25))
final = f"{B}/out/{OUTNAME}.pdf"; os.makedirs(f"{B}/out", exist_ok=True)
d.save(final, garbage=3, deflate=True)
import shutil; shutil.copy(f"{B}/{OUTNAME}.html", f"{B}/out/{OUTNAME}.html")
json.dump({"pages": pages, "n": len(d)}, open(f"{B}/pagemap.json","w"), indent=1)
# report citations missing from table
cited = set(re.findall(r'href="#(S\d+)"', full)); missing = sorted(cited - set(src_rows), key=sid_key)
print("PAGES", len(d), "| sources in table", len(src_rows), "| cited", len(cited), "| cited-but-missing", missing[:40])
print("EMDASH", full.count("—"))
