"""Assemble the Weatherbys pack HTML, companion markdown files, and check sources."""
import html, re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from questions import QB
from content import SCEN, GLOSS

B = pathlib.Path(__file__).parent
OUT = B.parent
esc = html.escape

def src_tags(s):
    return re.sub(r"\[(S\d+[a-z]?)\]", r'<span class="src">[\1]</span>', s)

# Question bank table
rows = []
for i, (g, q, t, st, f, tr) in enumerate(QB, 1):
    rows.append(f"<tr><td>{i}</td><td><b>{esc(q)}</b><br><small>{esc(g)}</small></td><td>{esc(t)}</td><td>{esc(st)}</td><td>{src_tags(esc(f)) or '-'}</td><td>{esc(tr)}</td></tr>")
qb_table = ('<table style="font-size:7.9pt"><tr><th>#</th><th style="width:20%">Question</th><th>Really testing</th>'
            '<th>Structure</th><th>Facts to weave in</th><th>Trap</th></tr>' + "".join(rows) + "</table>")

# Scenarios
lvl = {"easy": ("easy", "t-easy", "Easy"), "med": ("med", "t-med", "Medium"), "hard": ("hard", "t-hard", "Hard")}
sc = []
for crit, items in SCEN:
    sc.append(f"<h3>{esc(crit)}</h3>")
    for (l, setup, trap, say, why, twist) in items:
        c, t, name = lvl[l]
        sc.append(f'<div class="card {c}"><h4><span class="tag {t}">{name}</span>{esc(setup)}</h4>'
                  f'<b>Trap:</b> {esc(trap)}<br><b>Say:</b> {esc(say)}<br><b>Why it works:</b> {src_tags(esc(why))}<br>'
                  f'<b>Twist and hold:</b> {esc(twist)}</div>')
scen = "\n".join(sc)

gloss = '<table class="gloss">' + "".join(f"<tr><td>{esc(a)}</td><td>{src_tags(esc(b))}</td></tr>" for a, b in GLOSS) + "</table>"

# Sources
srcrows = {}
for f in ["WS_Firm_Findings.md", "WS_Industry_Findings.md"]:
    for line in (OUT / "research" / f).read_text().splitlines():
        m = re.match(r"^-?\s*\[(S\d+[a-z]?)\]\s*\|(.*)$", line.strip())
        if m:
            parts = [p.strip() for p in m.group(2).split("|")]
            srcrows[m.group(1)] = parts
def skey(k):
    m = re.match(r"S(\d+)([a-z]?)", k); return (int(m.group(1)), m.group(2))
st = ['<table class="srctab"><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL</th><th>Status</th><th>Note</th></tr>']
for k in sorted(srcrows, key=skey):
    p = srcrows[k] + [""] * 8
    outlet, title, date, url, _acc, status, note = p[:7]
    st.append(f"<tr><td><b>{k}</b></td><td>{esc(outlet)}</td><td>{esc(title)}</td><td>{esc(date)}</td>"
              f"<td><a href=\"{esc(url.split(' ;')[0])}\">{esc(url)}</a></td><td>{esc(status)}</td><td>{esc(note)}</td></tr>")
st.append("</table>")
sources = "".join(st)

cheat = (B / "cheat.html").read_text()
parts = ["00_head.html", "01_front.html", "02_partA.html", "03_part1.html", "04_part2.html",
         "05_part3_4.html", "06_part5_8.html", "07_part9_13.html", "08_end.html"]
doc = "".join((B / p).read_text() for p in parts) + "</body></html>"
doc = (doc.replace("{{QB_TABLE}}", qb_table).replace("{{SCENARIOS}}", scen)
          .replace("{{GLOSS}}", gloss).replace("{{SOURCES}}", sources).replace("{{CHEAT}}", cheat))

# Move long in-SVG captions out to HTML so they wrap instead of clipping
def lift_captions(doc):
    pat = re.compile(r'<text x="10" y="\d+" fill="#5b6475"[^>]*>(.*?)</text>')
    def fix(m):
        svg = m.group(0)
        ms = list(pat.finditer(svg))
        first = next((i for i, t in enumerate(ms) if len(re.sub(r"<[^>]+>", "", t.group(1))) > 120), None)
        if first is None:
            return svg
        lifted = ms[first:]
        for t in reversed(lifted):
            svg = svg[:t.start()] + svg[t.end():]
        return svg + '<div class="cap">' + " ".join(t.group(1) for t in lifted) + "</div>"
    return re.sub(r"<svg .*?</svg>", fix, doc, flags=re.S)
doc = lift_captions(doc)

# Check every cited source exists
cited = set(re.findall(r"\[(S\d+[a-z]?)\]", re.sub(r"<table class=\"srctab\">.*?</table>", "", doc, flags=re.S)))
missing = sorted(cited - set(srcrows), key=skey)
if missing:
    print("MISSING SOURCES:", missing)
emd = doc.count("—")
print(f"sources in table: {len(srcrows)}, cited: {len(cited)}, glossary: {len(GLOSS)}, questions: {len(QB)}, em dashes: {emd}")
(OUT / "Weatherbys_Private_Banking_Internship_Complete_Pack.html").write_text(doc)

# Cheat sheet standalone
head = (B / "00_head.html").read_text().replace("<title>Weatherbys Internship Pack</title>", "<title>Weatherbys Cheat Sheet</title>")
(B / "cheat_standalone.html").write_text(head + '<div class="band"><div class="kicker">Weatherbys Private Banking Internship 2027</div><h1>Cheat sheet</h1></div>' + cheat + "</body></html>")

# Question bank markdown
md = ["# Weatherbys Private Banking Internship 2027: Question Bank", "",
      "44 practice questions. Scaffolds, not scripts. Source IDs [Sxx] resolve to Part 15 of the complete pack.", ""]
cur = None
for i, (g, q, t, s, f, tr) in enumerate(QB, 1):
    if g != cur:
        md += [f"## {g}", ""]; cur = g
    md += [f"### {i}. {q}", f"- **Really testing:** {t}", f"- **Structure:** {s}", f"- **Facts to weave in:** {f or '-'}", f"- **Trap:** {tr}", ""]
md += ["## Questions to ask them", "",
       "1. Since the APR and BPR cap came in last April, how have conversations with farming and landed clients changed?",
       "2. The CEO has talked about a ceiling of 10,000 to 15,000 relationships. Where is the bank against that?",
       "3. Lombard lending now works against portfolios held elsewhere. Has that changed how bankers win new clients?",
       "4. How does the Business Bank work with the Private Bank?",
       "5. With several senior hires from Coutts, what do they say is different here?",
       "6. What separates an intern who goes on to the APB programme from one who doesn't?",
       "7. How is the new digital platform changing what a banker's assistant does?",
       "8. What does a good first year look like for a new APB in terms of qualifications?",
       "9. If rates rise again, how does that change the bank's priorities?", ""]
(OUT / "Question_Bank.md").write_text("\n".join(md))
