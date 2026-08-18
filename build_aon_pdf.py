#!/usr/bin/env python3
"""Assemble the dedicated Aon (cut-e) deep-dive report into its own PDF."""
import re, html, pathlib, markdown

CH = pathlib.Path("output/aon-report")
OUT = pathlib.Path("output/aon-deep-dive.pdf")

ORDER = [
    ("frontmatter", "00-frontmatter.md"),
    ("part", "Part I — The Ability Tests (scales)"),
    ("chapter", "01-scales-numerical-verbal.md"),
    ("chapter", "02-scales-logic.md"),
    ("chapter", "03-scales-speed-skills.md"),
    ("part", "Part II — Games, Judgement & Simulation"),
    ("chapter", "04-smartpredict-games.md"),
    ("chapter", "05-chatassess-squares.md"),
    ("part", "Part III — Personality, Motivation & Video"),
    ("chapter", "06-personality-motivation.md"),
    ("chapter", "07-vidassess.md"),
    ("part", "Part IV — Scoring & Integrity, Consolidated"),
    ("chapter", "08-how-aon-marks.md"),
    ("chapter", "09-anti-cheating.md"),
    ("chapter", "10-practice-resources.md"),
    ("chapter", "11-confidence-register.md"),
]

md = markdown.Markdown(extensions=["tables", "fenced_code", "attr_list", "toc", "sane_lists"])

toc_entries = []
body_parts = []

def render(fname):
    md.reset()
    text = pathlib.Path(CH / fname).read_text()
    lines = text.split("\n")
    title = None
    for i, ln in enumerate(lines):
        if ln.startswith("# "):
            title = ln[2:].strip()
            lines = lines[i+1:]
            break
    return title, md.convert("\n".join(lines))

front_text = (CH / "00-frontmatter.md").read_text()
m = re.search(r"^# (.+)$", front_text, re.M)
book_title = m.group(1).strip()
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
        body_parts.append(f'<section class="frontmatter" id="frontmatter">{htmlbody}</section>')
        continue
    cid = "ch-" + re.sub(r"[^a-z0-9]+", "-", val.replace(".md","").lower()).strip("-")
    toc_entries.append(("CH", cid, title))
    body_parts.append(f'<section class="chapter" id="{cid}"><h1 class="chaptertitle">{html.escape(title)}</h1>{htmlbody}</section>')

toc_rows = []
for e in toc_entries:
    cls = "toc-part" if e[0] == "PART" else "toc-ch"
    toc_rows.append(f'<li class="{cls}"><a href="#{e[1]}">{html.escape(e[2])}</a></li>')
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
.titlepage { page: titlepage; break-after: page; text-align: left; padding-top: 30mm; }
.titlepage h1 { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 30pt; line-height: 1.15; color: #7a1f1f; margin: 0 0 10mm 0; border: none; }
.titlepage .subtitle { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 13pt; color: #6e3737; font-weight: 400; line-height: 1.4; margin-bottom: 14mm; }
.titlepage .meta { font-size: 10pt; color: #555; border-top: 2px solid #7a1f1f; padding-top: 6mm; }
h1.chaptertitle, h1.parttitle { string-set: runhead content(); font-family: 'Helvetica Neue', Arial, sans-serif; color: #7a1f1f; font-size: 20pt; break-before: page; padding-bottom: 3mm; border-bottom: 2px solid #7a1f1f; margin: 0 0 6mm 0; }
.partdiv { break-before: page; padding-top: 60mm; text-align: center; }
h1.parttitle { border: none; font-size: 26pt; break-before: avoid; }
h2 { font-family: 'Helvetica Neue', Arial, sans-serif; color: #8a2c2c; font-size: 13.5pt; margin-top: 7mm; margin-bottom: 2mm; break-after: avoid; }
h3 { font-family: 'Helvetica Neue', Arial, sans-serif; color: #2a2a2a; font-size: 11.5pt; margin-top: 5mm; margin-bottom: 1.5mm; break-after: avoid; }
p { margin: 0 0 2.4mm 0; text-align: justify; }
a { color: #7a1f1f; text-decoration: none; }
strong { color: #111; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.6pt; background: #f5efef; padding: 0 2px; border-radius: 2px; word-break: break-word; }
blockquote { background: #faf4f4; border-left: 3px solid #a94444; margin: 4mm 0; padding: 3mm 4mm; break-inside: avoid; font-size: 10pt; }
blockquote h3 { margin-top: 0; color: #7a1f1f; }
blockquote p { text-align: left; }
table { border-collapse: collapse; width: 100%; margin: 3mm 0; font-size: 8.6pt; line-height: 1.35; table-layout: fixed; }
th, td { border: 0.5pt solid #cdb8b8; padding: 1.4mm 2mm; text-align: left; vertical-align: top; word-wrap: break-word; overflow-wrap: anywhere; }
th { background: #7a1f1f; color: #fff; font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 600; font-size: 8.4pt; }
tr:nth-child(even) td { background: #faf6f6; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
ul, ol { margin: 1mm 0 3mm 0; padding-left: 6mm; }
li { margin-bottom: 1.2mm; text-align: justify; }
hr { border: none; border-top: 0.5pt solid #ccc; margin: 5mm 0; }
.toc { break-before: page; }
.toc ul { list-style: none; padding-left: 0; }
.toc li { margin-bottom: 1.6mm; }
.toc a { display: block; }
.toc a::after { content: target-counter(attr(href), page); float: right; color: #555; font-variant-numeric: tabular-nums; }
.toc-part a { font-family: 'Helvetica Neue', Arial, sans-serif; font-weight: 700; color: #7a1f1f; margin-top: 4mm; font-size: 11pt; }
.toc-ch a { padding-left: 5mm; font-size: 10pt; }
.chapter, .frontmatter { break-before: page; }
"""

titlepage = (f'<section class="titlepage"><h1>{html.escape(book_title)}</h1>'
             f'<div class="subtitle">{html.escape(subtitle)}</div>'
             f'<div class="meta">Version 1.0 &nbsp;·&nbsp; Generated 1 August 2026<br>'
             f'Companion volume to <i>The Definitive Guide to UK Finance Early-Careers Online Assessments</i></div></section>')

fm_idx = next(i for i,b in enumerate(body_parts) if 'id="frontmatter"' in b)
body_parts[fm_idx] = re.sub(r'<h3>.*?</h3>', '', body_parts[fm_idx], count=1, flags=re.S)

doc = ("<!DOCTYPE html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>"
       + titlepage + toc_html + "".join(body_parts) + "</body></html>")

pathlib.Path("output/_aon_book.html").write_text(doc)

from weasyprint import HTML
HTML(string=doc, base_url=".").write_pdf(str(OUT))
print("PDF written:", OUT)
