import re, markdown, datetime
from weasyprint import HTML, CSS

SRC = "/home/user/Applications2027/blackstone/pymetrics-guide.md"
OUT = "/home/user/Applications2027/blackstone/Blackstone-pymetrics-Playbook.pdf"

md = open(SRC).read()

# Strip the H1 (goes on the cover) and the two context lines + first rule
lines = md.split("\n")
assert lines[0].startswith("# ")
body_md = "\n".join(lines[1:]).lstrip("\n")
body_md = re.sub(r'^\*\*Context:\*\*.*?\n\*\*Provider:\*\*.*?\n\n---\n', '', body_md, flags=re.S)

# Python-Markdown needs a blank line before a list that follows a paragraph.
def fix_lists(text):
    out, prev = [], ""
    for ln in text.split("\n"):
        is_item = bool(re.match(r'^\s*([-*+]|\d+\.)\s+', ln))
        prev_is_item = bool(re.match(r'^\s*([-*+]|\d+\.)\s+', prev))
        prev_blank = prev.strip() == ""
        prev_struct = prev.lstrip().startswith(("#", ">", "|", "```"))
        if is_item and not prev_blank and not prev_is_item and not prev_struct:
            out.append("")
        out.append(ln)
        prev = ln
    return "\n".join(out)

body_md = fix_lists(body_md)

html_body = markdown.markdown(
    body_md,
    extensions=["extra", "tables", "fenced_code", "sane_lists", "toc"],
    extension_configs={"toc": {"toc_depth": "2-2", "anchorlink": False}},
)
mdx = markdown.Markdown(extensions=["extra","tables","fenced_code","sane_lists","toc"],
                        extension_configs={"toc":{"toc_depth":"2-2"}})
html_body = mdx.convert(body_md)
toc = mdx.toc

today = datetime.date.today().strftime("%d %B %Y")

CSS_TEXT = """
@page {
  size: A4;
  margin: 20mm 18mm 18mm 18mm;
  @top-left  { content: "Blackstone pymetrics — Playbook"; font-family: "DejaVu Sans", sans-serif;
               font-size: 7.5pt; color: #8A93A6; letter-spacing: .04em; }
  @bottom-right { content: counter(page); font-family: "DejaVu Sans", sans-serif;
                  font-size: 8pt; color: #6B7280; }
}
@page cover { margin: 0; @top-left { content: none; } @bottom-right { content: none; } }

:root { --ink:#15192B; --muted:#5A6376; --line:#E2E6EF; --accent:#1F3A6E; --accentsoft:#F3F6FC; }

html { font-size: 10pt; }
body { font-family: "DejaVu Sans", sans-serif; color: var(--ink);
       line-height: 1.55; hyphens: none; }

/* ---------- cover ---------- */
.cover { page: cover; height: 297mm; position: relative; page-break-after: always;
         background: var(--accent); color: #fff; }
.cover .inner { position: absolute; left: 20mm; right: 20mm; top: 62mm; }
.cover .eyebrow { font-size: 9.5pt; letter-spacing: .22em; text-transform: uppercase;
                  color: #A9BEE4; margin-bottom: 10mm; }
.cover h1 { font-size: 34pt; line-height: 1.12; margin: 0 0 7mm 0; font-weight: 700;
            color:#fff; border:0; padding:0; }
.cover .sub { font-size: 12.5pt; line-height: 1.5; color: #CBD8EE; max-width: 130mm; }
.cover .rule { width: 26mm; height: 3px; background: #6E93D6; margin: 9mm 0; }
.cover .meta { position: absolute; left: 20mm; right: 20mm; bottom: 20mm;
               font-size: 9pt; color: #9FB4D8; line-height: 1.7; }

/* ---------- contents ---------- */
.toc-page { page-break-after: always; }
.toc-title { font-size: 17pt; color: var(--accent); margin: 0 0 6mm 0; font-weight: 700; }
.toc ul { list-style: none; margin: 0; padding: 0; }
.toc li { padding: 2.6mm 0; border-bottom: 1px solid var(--line); font-size: 10.5pt; }
.toc a { color: var(--ink); text-decoration: none; }
.toc a::after { content: " · p" target-counter(attr(href), page); color: var(--muted); font-size: 9pt; }

/* ---------- headings ---------- */
h2 { font-size: 16pt; color: var(--accent); margin: 0 0 5mm 0; padding-bottom: 2.5mm;
     border-bottom: 2px solid var(--accent); page-break-after: avoid;
     page-break-before: always; font-weight: 700; }
h2:first-of-type { page-break-before: avoid; }
h3 { font-size: 12pt; color: var(--ink); margin: 7mm 0 2.5mm 0; page-break-after: avoid; font-weight: 700; }
h4 { font-size: 10.5pt; margin: 5mm 0 2mm 0; page-break-after: avoid; }

p { margin: 0 0 3mm 0; orphans: 2; widows: 2; }
strong { color: #0B1020; }
em { color: inherit; }
a { color: var(--accent); text-decoration: none; word-break: break-word; }

ul, ol { margin: 0 0 3.5mm 0; padding-left: 5.5mm; }
li { margin-bottom: 1.6mm; }
li > ul, li > ol { margin-top: 1.6mm; }

hr { border: 0; border-top: 1px solid var(--line); margin: 6mm 0; }

/* ---------- tables ---------- */
table { width: 100%; border-collapse: collapse; margin: 3.5mm 0 5mm 0;
        font-size: 8.8pt; page-break-inside: avoid; }
th { background: var(--accent); color: #fff; text-align: left; font-weight: 700;
     padding: 2.2mm 2.6mm; font-size: 8.5pt; }
td { padding: 2.2mm 2.6mm; border-bottom: 1px solid var(--line); vertical-align: top; }
tbody tr:nth-child(even) { background: #F7F9FD; }

/* ---------- blockquote ---------- */
blockquote { margin: 4mm 0; padding: 3mm 5mm; background: var(--accentsoft);
             border-left: 3px solid var(--accent); color: #23304A;
             font-size: 9.5pt; page-break-inside: avoid; }
blockquote p:last-child { margin-bottom: 0; }

/* ---------- code ---------- */
code { font-family: "DejaVu Sans Mono", monospace; font-size: 8.6pt;
       background: #EEF1F7; padding: 0.4mm 1.1mm; border-radius: 2px; }
pre { background: #10162A; color: #DCE4F5; padding: 4mm; border-radius: 3px;
      font-size: 8pt; line-height: 1.45; overflow: hidden; page-break-inside: avoid; margin: 4mm 0; }
pre code { background: none; color: inherit; padding: 0; font-size: 8pt; }

/* keep short blocks together */
h3 + p, h3 + ul, h3 + table { page-break-before: avoid; }
"""

html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><title>Blackstone pymetrics Playbook</title></head>
<body>
<div class="cover"><div class="inner">
  <div class="eyebrow">Assessment Preparation</div>
  <h1>Blackstone<br/>pymetrics</h1>
  <div class="rule"></div>
  <div class="sub">A complete breakdown of the twelve games, how the scoring model actually works,
  what the integrity controls really are, and what to do about it.</div>
</div>
<div class="meta">
  Prepared for Janak Chohan · {today}<br/>
  pymetrics (Harver) · 12-game battery · ~25–30 minutes · 3-day completion window
</div></div>

<div class="toc-page">
  <div class="toc-title">Contents</div>
  <div class="toc">{toc}</div>
</div>

{html_body}
</body></html>"""

HTML(string=html).write_pdf(OUT, stylesheets=[CSS(string=CSS_TEXT)])
print("written:", OUT)
