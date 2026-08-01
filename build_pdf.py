#!/usr/bin/env python3
"""Assemble the guide's markdown chapters into a single typeset PDF."""
import re, html, pathlib, markdown

CH = pathlib.Path("output/chapters")
OUT = pathlib.Path("output/ultimate-online-assessment-guide.pdf")

# Book order: front matter, Part I providers, Part II cross-cutting, closing.
ORDER = [
    ("frontmatter", "00-frontmatter.md"),
    ("part", "Part I — The Providers"),
    ("chapter", "01-shl.md"),
    ("chapter", "02-aon-cute.md"),
    ("chapter", "03-arctic-shores.md"),
    ("chapter", "04-pymetrics.md"),
    ("chapter", "05-cappfinity.md"),
    ("chapter", "06-amberjack.md"),
    ("chapter", "07-plum.md"),
    ("chapter", "08-hirevue.md"),
    ("chapter", "09-willo.md"),
    ("chapter", "10-testgorilla.md"),
    ("chapter", "11-morgan-stanley.md"),
    ("part", "Part II — Cross-Cutting Reference"),
    ("chapter", "61-why-assessments-exist.md"),
    ("chapter", "62-vendor-landscape.md"),
    ("chapter", "63-psychometrics.md"),
    ("chapter", "64-construct-manual.md"),
    ("chapter", "65-prep-programme.md"),
    ("chapter", "66-integrity-taxonomy.md"),
    ("chapter", "67-legal.md"),
    ("chapter", "68-employer-mapping.md"),
    ("chapter", "69-appendices.md"),
    ("chapter", "99-closing-gaps.md"),
]

md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "toc", "sane_lists"])

toc_entries = []          # (id, title) for chapter-level TOC
body_parts = []
chap_n = 0

def render(fname):
    md.reset()
    text = pathlib.Path(CH / fname).read_text()
    # Pull the first H1 as the chapter title, keep rest of body.
    lines = text.split("\n")
    title = None
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            title = ln[2:].strip()
            lines = lines[i+1:]
            break
    body_md = "\n".join(lines)
    return title, md.convert(body_md)

# ---- Title page from frontmatter's first H1 ----
front_text = (CH / "00-frontmatter.md").read_text()
m = re.search(r"^# (.+)$", front_text, re.M)
book_title = m.group(1).strip()
# subtitle = first ### line
sub = re.search(r"^### (.+)$", front_text, re.M)
subtitle = sub.group(1).strip() if sub else ""

for kind, val in ORDER:
    if kind == "part":
        pid = "part-" + re.sub(r"[^a-z0-9]+", "-", val.lower()).strip("-")
        toc_entries.append(("PART", pid, val))
        body_parts.append(f'<section class="partdiv" id="{pid}"><h1 class="parttitle">{html.escape(val)}</h1></section>')
        continue
    title, htmlbody = render(val)
    if val == "00-frontmatter.md":
        # front matter: no chapter number, its own page, not in numbered TOC as chapter
        cid = "frontmatter"
        body_parts.append(f'<section class="frontmatter" id="{cid}">{htmlbody}</section>')
        continue
    chap_n += 1
    cid = "ch-" + re.sub(r"[^a-z0-9]+", "-", val.replace(".md","").lower()).strip("-")
    toc_entries.append(("CH", cid, title))
    body_parts.append(
        f'<section class="chapter" id="{cid}"><h1 class="chaptertitle">{html.escape(title)}</h1>{htmlbody}</section>'
    )

# ---- Build TOC HTML ----
toc_rows = []
for e in toc_entries:
    if e[0] == "PART":
        toc_rows.append(f'<li class="toc-part"><a href="#{e[1]}">{html.escape(e[2])}</a></li>')
    else:
        toc_rows.append(f'<li class="toc-ch"><a href="#{e[1]}">{html.escape(e[2])}</a></li>')
toc_html = '<section class="toc" id="toc"><h1 class="chaptertitle">Contents</h1><ul>' + "".join(toc_rows) + "</ul></section>"

CSS = r"""
@page {
  size: A4; margin: 22mm 20mm 20mm 20mm;
  @bottom-center { content: counter(page); font-family: Georgia, serif; font-size: 9pt; color: #555; }
  @top-right { content: string(runhead); font-family: Georgia, serif; font-size: 8.5pt; color: #777; font-style: italic; }
}
@page :first { @top-right { content: none; } @bottom-center { content: none; } }
@page titlepage { @top-right { content: none; } @bottom-center { content: none; } }
html { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.5; color: #1a1a1a; }
body { margin: 0; }
h1.booktitle { string-set: runhead ""; }
.titlepage { page: titlepage; break-after: page; text-align: left; padding-top: 30mm; }
.titlepage h1 { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 30pt; line-height: 1.15; color: #12335a; margin: 0 0 10mm 0; border: none; }
.titlepage .subtitle { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13pt; color: #37506e; font-weight: 400; line-height: 1.4; margin-bottom: 14mm; }
.titlepage .meta { font-size: 10pt; color: #555; border-top: 2px solid #12335a; padding-top: 6mm; }
h1.chaptertitle, h1.parttitle { string-set: runhead content(); font-family: 'Helvetica Neue', Arial, sans-serif; color: #12335a; font-size: 20pt; break-before: page; padding-bottom: 3mm; border-bottom: 2px solid #12335a; margin: 0 0 6mm 0; }
.partdiv { break-before: page; padding-top: 60mm; text-align: center; }
h1.parttitle { border: none; font-size: 26pt; break-before: avoid; }
.frontmatter { }
h2 { font-family: 'Helvetica Neue', Arial, sans-serif; color: #1c4a7a; font-size: 13.5pt; margin-top: 7mm; margin-bottom: 2mm; break-after: avoid; }
h3 { font-family: 'Helvetica Neue', Arial, sans-serif; color: #2a2a2a; font-size: 11.5pt; margin-top: 5mm; margin-bottom: 1.5mm; break-after: avoid; }
p { margin: 0 0 2.4mm 0; text-align: justify; }
a { color: #12335a; text-decoration: none; }
strong { color: #111; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #eef1f5; padding: 0 2px; border-radius: 2px; word-break: break-word; }
/* Confidence tags like [VENDOR] rendered inline in code fences */
/* Blockquotes = the at-a-glance boxes and callouts */
blockquote { background: #f2f6fb; border-left: 3px solid #2a6bb0; margin: 4mm 0; padding: 3mm 4mm; break-inside: avoid; font-size: 10pt; }
blockquote h3 { margin-top: 0; color: #12335a; }
blockquote p { text-align: left; }
/* Tables */
table { border-collapse: collapse; width: 100%; margin: 3mm 0; font-size: 8.6pt; line-height: 1.35; table-layout: fixed; }
th, td { border: 0.5pt solid #b8c2ce; padding: 1.4mm 2mm; text-align: left; vertical-align: top; word-wrap: break-word; overflow-wrap: anywhere; }
th { background: #12335a; color: #fff; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 8.4pt; }
tr:nth-child(even) td { background: #f4f7fa; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
ul, ol { margin: 1mm 0 3mm 0; padding-left: 6mm; }
li { margin-bottom: 1.2mm; text-align: justify; }
hr { border: none; border-top: 0.5pt solid #ccc; margin: 5mm 0; }
em { color: #333; }
/* TOC */
.toc { break-before: page; }
.toc ul { list-style: none; padding-left: 0; }
.toc li { margin-bottom: 1.6mm; }
.toc a { display: block; }
.toc a::after { content: target-counter(attr(href), page); float: right; color: #555; font-variant-numeric: tabular-nums; }
.toc-part a { font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 700; color: #12335a; margin-top: 4mm; font-size: 11pt; }
.toc-ch a { padding-left: 5mm; font-size: 10pt; }
.chapter, .frontmatter { break-before: page; }
"""

titlepage = (f'<section class="titlepage"><h1 class="booktitle">{html.escape(book_title)}</h1>'
             f'<div class="subtitle">{html.escape(subtitle)}</div>'
             f'<div class="meta">Version 1.0 &nbsp;·&nbsp; Generated 1 August 2026<br>'
             f'A source-backed reference for UK finance early-careers candidates</div></section>')

# Remove the duplicate title/subtitle from the frontmatter body (already on title page)
fm_idx = next(i for i,b in enumerate(body_parts) if 'id="frontmatter"' in b)
# strip a leading <h3>subtitle</h3> and the bold intro line if present
body_parts[fm_idx] = re.sub(r'<h3>.*?</h3>', '', body_parts[fm_idx], count=1, flags=re.S)

doc = ("<!DOCTYPE html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>"
       + titlepage + toc_html + "".join(body_parts) + "</body></html>")

pathlib.Path("output/_book.html").write_text(doc)

from weasyprint import HTML
HTML(string=doc, base_url=".").write_pdf(str(OUT))
print("PDF written:", OUT)
