#!/usr/bin/env python3
"""Build a guide PDF from a markdown report.

Usage: build.py <report.md> <out.pdf> <config.json>

The config holds the cover text and layout hints for one guide. A line
`<!-- figure:name -->` in the markdown is replaced by figures/name.html.
Two passes: the first finds the page each section starts on, the second
writes those numbers into the contents page.
"""
import json
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).parent
SRC, OUT = Path(sys.argv[1]), Path(sys.argv[2])
CFG = json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
TITLE = CFG["title"]

CSS = r"""
@page { size: A4; margin: 20mm 19mm 21mm 19mm;
  @bottom-center { content: counter(page); font: 8.5pt Inter, sans-serif; color: #6b7480; }
  @bottom-left { content: "%%FOOTER%%"; font: 8pt Inter, sans-serif; color: #9aa2ac; }
}
@page :first { margin: 0; @bottom-center { content: none } @bottom-left { content: none } }
:root { --ink:#1b2230; --muted:#5d6673; --rule:#d9dee4; --accent:#0e5a6b; --accent-2:#b4532a;
  --tint:#eef4f5; --tint-2:#faf3ee; }
* { box-sizing: border-box; }
html { font-family: Inter, "Liberation Sans", sans-serif; font-size: 10.2pt; color: var(--ink);
  line-height: 1.52; font-feature-settings: "calt" 0, "case" 0; }
body { margin: 0; }
p { margin: 0 0 .72em; orphans: 3; widows: 3; }
strong { font-weight: 650; }
a { color: var(--accent); text-decoration: none; }
.cite a { font-size: .84em; color: #557a84; white-space: normal; }
.cite::before { content: "["; color:#9bb0b6; font-size:.84em; }
.cite::after { content: "]"; color:#9bb0b6; font-size:.84em; }

/* cover */
.cover { height: 297mm; padding: 34mm 24mm 24mm; background: #0f2f3a; color: #fff;
  display: flex; flex-direction: column; break-after: page; }
.cover .kicker { font-size: 9.5pt; letter-spacing: .14em; text-transform: uppercase; color: #8fc3cf; font-weight: 600; }
.cover h1 { font-family: "Inter Display", Inter, sans-serif; font-size: 39pt; line-height: 1.08; font-weight: 700;
  letter-spacing: -.02em; margin: 14mm 0 8mm; max-width: 150mm; }
.cover .sub { font-size: 13.5pt; line-height: 1.45; color: #d6e6ea; max-width: 135mm; }
.cover .points { margin-top: auto; border-top: 1px solid #386170; padding-top: 7mm; display: grid;
  grid-template-columns: 1fr 1fr 1fr; gap: 8mm; }
.cover .points div { font-size: 9.6pt; line-height: 1.45; color: #cfe1e5; }
.cover .points b { display: block; color: #fff; font-size: 10.5pt; margin-bottom: 1.5mm; font-weight: 650; }
.cover .meta { margin-top: 10mm; font-size: 8.8pt; color: #8fb0b9; }

/* contents */
.toc { break-after: page; }
.toc h2 { break-before: auto; }
.toc ol { list-style: none; padding: 0; margin: 6mm 0 0; counter-reset: sec; }
.toc li { counter-increment: sec; display: flex; align-items: baseline; gap: 3mm; padding: 2.6mm 0;
  border-bottom: 1px solid var(--rule); }
.toc li::before { content: counter(sec, decimal-leading-zero); color: var(--accent); font-weight: 650;
  font-size: 9pt; width: 7mm; flex: none; }
.toc li a { color: var(--ink); flex: 1; font-weight: 520; }
.toc li .pg { color: var(--muted); font-variant-numeric: tabular-nums; }
.toc .how { margin-top: 8mm; background: var(--tint); border-left: 3px solid var(--accent); padding: 4mm 5mm;
  font-size: 9.6pt; }
.toc .how p:last-child { margin: 0; }

/* headings */
h2 { font-family: "Inter Display", Inter, sans-serif; font-size: 20pt; line-height: 1.18; letter-spacing: -.012em;
  font-weight: 700; margin: 0 0 5mm; padding-bottom: 3.2mm; text-wrap: balance; border-bottom: 2px solid var(--accent);
  break-before: page; break-after: avoid; }
h3 { font-size: 12.4pt; line-height: 1.3; font-weight: 680; margin: 7mm 0 2.4mm; color: #123f4b; break-after: avoid; }
h2 + h3 { margin-top: 0; }

/* lists */
ul, ol { margin: 0 0 .8em; padding-left: 5.2mm; }
li { margin-bottom: .42em; }
.short li { margin-bottom: .75em; }
ul.task-list, ul.contains-task-list { list-style: none; padding-left: 0; }
ul.task-list li, ul.contains-task-list li { display: flex; gap: 2.6mm; align-items: flex-start; margin-bottom: .34em;
  break-inside: avoid; }
ul.task-list li label { display: contents; }
li input[type=checkbox] { appearance: none; width: 3.5mm; height: 3.5mm; border: 1.1px solid #56616d; border-radius: .6mm;
  flex: none; margin: .9mm 0 0; }

/* tables */
table { width: 100%; border-collapse: collapse; margin: 3.5mm 0 5.5mm; font-size: 8.9pt; line-height: 1.42; }
thead { display: table-header-group; }
th { text-align: left; background: #123f4b; color: #fff; font-weight: 600; padding: 2.1mm 2.6mm; vertical-align: bottom; }
td { padding: 2.1mm 2.6mm; border-bottom: 1px solid var(--rule); vertical-align: top; }
tbody tr:nth-child(even) td { background: #f7f9fa; }
tr { break-inside: avoid; }
td:first-child { font-weight: 560; }
table.wide-first td:first-child { width: 20%; }
table.wide-first td:nth-child(2) { width: 16%; }
table.keep { break-inside: avoid; }
table.narrow-first td:first-child { width: 9%; white-space: nowrap; }

/* quoted / worked answers */
blockquote { margin: 3mm 0 5mm; padding: 3.6mm 5mm 1.2mm; background: var(--tint-2); border-left: 3px solid var(--accent-2);
  font-size: 9.7pt; }
blockquote p { margin-bottom: .62em; }
blockquote { break-inside: avoid; }
p:has(+ blockquote), p:has(+ table), p:has(+ figure) { break-after: avoid; }

/* figures */
figure { margin: 5mm 0 6mm; break-inside: avoid; }
figcaption { font-size: 8.6pt; color: var(--muted); margin-top: 2.4mm; }
.flow { display: grid; grid-template-columns: 31mm 1fr; gap: 3mm 4mm; align-items: stretch; font-size: 8.7pt; line-height: 1.36; }
.flow .start { grid-row: 1 / span 2; background: #123f4b; color: #fff; border-radius: 1.5mm; padding: 3.5mm; display: flex;
  flex-direction: column; justify-content: center; font-weight: 600; }
.flow .start small { font-weight: 400; color: #c5dde2; margin-top: 1.5mm; font-size: 8pt; }
.route { border: 1px solid var(--rule); border-radius: 1.5mm; padding: 3mm 3.4mm; }
.route.human { border-left: 3px solid var(--accent); }
.route.ai { border-left: 3px solid var(--accent-2); }
.route .name { font-weight: 680; font-size: 9.3pt; margin-bottom: 2mm; }
.route .name span { font-weight: 400; color: var(--muted); }
.steps { display: flex; gap: 1.6mm; align-items: stretch; }
.steps .s { flex: 1; background: var(--tint); border-radius: 1mm; padding: 2mm 2.2mm; }
.route.ai .steps .s { background: var(--tint-2); }
.steps .arr { flex: none; align-self: center; color: #8b96a1; font-size: 10pt; }
.bar { display: flex; height: 13mm; border-radius: 1.5mm; overflow: hidden; font-size: 8.2pt; line-height: 1.2; color: #fff; }
.bar div { display: flex; flex-direction: column; justify-content: center; align-items: center; padding: 0 1mm; border-right: 1px solid #fff;
  overflow: hidden; white-space: nowrap; }
.bar b { font-weight: 650; }
.bar .h { background: #0e5a6b; } .bar .si { background: #5b8a94; } .bar .t { background: #7ea2aa; }
.bar .a { background: #b4532a; } .bar .r { background: #0e5a6b; } .bar .l { background: #8c97a2; }
.bar .spare { background: #eceff2; color: #6b7480; border-right: 0; }
.legend { display: flex; flex-wrap: wrap; gap: 1.5mm 5mm; font-size: 8.4pt; margin-top: 2.2mm; }
.legend i { display: inline-block; width: 2.6mm; height: 2.6mm; border-radius: .5mm; margin-right: 1.4mm; vertical-align: -0.3mm; }
.legend .h { background: #0e5a6b; } .legend .si { background: #5b8a94; } .legend .t { background: #7ea2aa; }
.legend .a { background: #b4532a; } .legend .r { background: #0e5a6b; } .legend .l { background: #8c97a2; }
.barlabel { display: flex; justify-content: space-between; font-size: 8pt; color: var(--muted); margin-top: 1.2mm; }
.dsteps { display: flex; gap: 1.8mm; align-items: stretch; }
.dsteps .d { flex: 1; background: var(--tint); border-top: 3px solid var(--accent); border-radius: 1mm; padding: 2.4mm 2.6mm 2.8mm; }
.d .n { font-weight: 700; color: var(--accent); font-size: 8.4pt; }
.d .t { font-weight: 680; font-size: 10.4pt; margin: .4mm 0 1mm; }
.d .q { font-size: 8.5pt; line-height: 1.34; font-weight: 560; margin-bottom: 1.6mm; }
.d .e { font-size: 8pt; line-height: 1.36; color: var(--muted); }
.burden { margin-top: 2mm; background: var(--tint-2); border-left: 3px solid var(--accent-2); padding: 2.6mm 3.4mm; font-size: 9pt; }
.entry { break-inside: avoid; margin: 0 0 4.2mm; padding: 3mm 4mm 1.4mm; border: 1px solid var(--rule); border-left: 3px solid var(--accent); border-radius: 1mm; }
.entry > p { margin-bottom: 1.6mm; font-size: 10pt; }
.entry ul { list-style: none; padding: 0; margin: 0 0 1mm; font-size: 9.3pt; }
.entry li { margin-bottom: .9mm; display: flex; align-items: baseline; }
.entry .val { flex: 1; }
.entry .lab { flex: 0 0 20mm; font-weight: 650; color: var(--accent); font-size: 8.4pt; text-transform: uppercase; letter-spacing: .03em; }
.card { break-inside: avoid; border: 1.2px solid #123f4b; border-radius: 1.6mm; padding: 4mm 5mm 2mm; margin: 0 0 5mm; }
.card h3 { margin-top: 0; }
.card table { margin-bottom: 2mm; }
"""

# Applied on top of CSS when the config sets "style": "accessible".
# Follows the British Dyslexia Association style guide: clear sans serif,
# larger text, wide line and paragraph spacing, short left-aligned lines,
# an off-white background, bold for emphasis and no italics or capitals.
CSS_ACCESSIBLE = r"""
@font-face { font-family: "Atkinson Hyperlegible"; font-weight: 400; src: url("%%FONTS%%/atkinson-hyperlegible-latin-400-normal.woff2") format("woff2"); }
@font-face { font-family: "Atkinson Hyperlegible"; font-weight: 700; src: url("%%FONTS%%/atkinson-hyperlegible-latin-700-normal.woff2") format("woff2"); }
@page { size: A4; margin: 21mm 30mm 23mm 30mm; background: #fbf6ea;
  @bottom-center { content: counter(page); font: 10pt "Atkinson Hyperlegible", sans-serif; color: #4f5661; }
  @bottom-left { content: none; }
}
@page :first { margin: 0; }
:root { --ink:#1c2230; --muted:#454c58; --rule:#cfc8b6; --accent:#0b4f6c; --accent-2:#8a4b12; --tint:#e9f1f5; --tint-2:#f4ead8; }
html { font-family: "Atkinson Hyperlegible", "DejaVu Sans", Arial, sans-serif; font-size: 12.5pt; line-height: 1.72;
  letter-spacing: .012em; word-spacing: .06em; background: #fbf6ea; font-feature-settings: normal; }
p { margin: 0 0 1em; text-align: left; hyphens: none; }
strong, b { font-weight: 700; }
em, i { font-style: normal; font-weight: 700; }
a { color: var(--accent); font-weight: 700; }
h2 { font-family: inherit; font-size: 23pt; line-height: 1.25; letter-spacing: 0; border-bottom: 3px solid var(--accent);
  padding-bottom: 4mm; margin-bottom: 7mm; }
h3 { font-size: 16pt; line-height: 1.35; margin: 10mm 0 3.5mm; color: var(--accent); }
h4 { font-size: 13.5pt; margin: 7mm 0 2.5mm; break-after: avoid; }
ul, ol { padding-left: 7mm; margin-bottom: 1em; }
li { margin-bottom: .62em; padding-left: 1mm; }
ol > li::marker { font-weight: 700; color: var(--accent); }
table { font-size: 11pt; line-height: 1.5; margin: 4mm 0 7mm; }
th { background: var(--accent); padding: 2.8mm 3.2mm; }
td { padding: 2.8mm 3.2mm; border-bottom: 1px solid var(--rule); }
tbody tr:nth-child(even) td { background: #f5efdf; }
blockquote { margin: 4mm 0 7mm; padding: 4.5mm 6mm 1.5mm; font-size: 12pt; border-radius: 1.5mm;
  background: var(--tint); border-left: 5px solid var(--accent); }
blockquote.weak { background: #ecebe6; border-left-color: #6d7178; }
blockquote.strong { background: #e4f0e9; border-left-color: #1f6b4a; }
blockquote.say { background: var(--tint); border-left-color: var(--accent); }
blockquote.remember { background: var(--tint-2); border-left-color: var(--accent-2); }
blockquote.try { background: #fffdf6; border: 1.5px solid var(--accent); border-left-width: 5px; }
blockquote .tag { display: block; font-weight: 700; font-size: 11pt; margin-bottom: 1.2mm; }
blockquote.weak .tag { color: #4a4e55; } blockquote.strong .tag { color: #1f6b4a; }
blockquote.say .tag { color: var(--accent); } blockquote.remember .tag { color: var(--accent-2); }
blockquote.try .tag { color: var(--accent); }
figcaption { font-size: 10.5pt; }
.cover { background: #fbf6ea; color: var(--ink); padding: 36mm 30mm 26mm; border-left: 12mm solid var(--accent); }
.cover .kicker { color: var(--accent); text-transform: none; letter-spacing: .02em; font-size: 12pt; font-weight: 700; }
.cover h1 { font-family: inherit; font-size: 40pt; line-height: 1.16; letter-spacing: 0; max-width: 140mm; }
.cover .sub { color: var(--ink); font-size: 15pt; line-height: 1.55; max-width: 130mm; }
.cover .points { border-top: 2px solid var(--accent); grid-template-columns: 1fr; gap: 4mm; }
.cover .points div { color: var(--ink); font-size: 12pt; line-height: 1.55; }
.cover .points b { color: var(--accent); font-size: 12.5pt; display: inline; margin-right: 1.5mm; }
.cover .meta { color: var(--muted); font-size: 10.5pt; }
.toc li { padding: 3.2mm 0; }
.toc li::before { font-size: 11pt; width: 9mm; }
.toc li a { font-weight: 400; }
.toc .how { font-size: 11.5pt; background: var(--tint); }
.card { border: 2px solid var(--accent); padding: 5mm 6mm 2mm; background: #fffdf6; }
.entry .lab { text-transform: none; letter-spacing: 0; font-size: 10.5pt; }
li input[type=checkbox] { width: 4.4mm; height: 4.4mm; border: 1.5px solid var(--ink); margin-top: 1.4mm; background: #fffdf6; }
"""


def pandoc(md: str) -> str:
    return subprocess.run(
        ["pandoc", "-f", "gfm+smart", "-t", "html", "--wrap=none", "--columns=100000"],
        input=md, capture_output=True, text=True, check=True).stdout


def build_html(pages: dict) -> str:
    md = SRC.read_text(encoding="utf-8")
    md = re.sub(r"^# .*\n", "", md, count=1)
    body = pandoc(md)

    # muted, bracketed source links
    body = re.sub(r"\((<a href=\"[^\"]+\">[^<]+</a>)\)", r'<span class="cite">\1</span>', body)

    # opening section gets its own heading
    first_h2 = body.index("<h2")
    lead = body[:first_h2].replace("<ul>", '<ul class="short">', 1)
    rest = body[first_h2:]
    lead_title = CFG.get("lead_title", "The short answer")
    lead_id = re.sub(r"[^a-z0-9]+", "-", lead_title.lower()).strip("-")
    body = f'<h2 id="{lead_id}">{html.escape(lead_title)}</h2>\n' + lead + rest

    # figures
    def figure(m):
        return (HERE / "figures" / (m.group(1) + ".html")).read_text(encoding="utf-8")
    body = re.sub(r"<!--\s*figure:([a-z0-9_-]+)\s*-->", figure, body)

    # table column hints, keyed by the first header cell
    for first, cls in CFG.get("table_classes", {}).items():
        body = re.sub(r'<table>(\s*<thead>\s*<tr[^>]*>\s*<th>' + re.escape(first) + '</th>)',
                      r'<table class="' + cls + r'">\1', body)

    # callouts: a blockquote whose first words are a bold tag gets a class
    tags = {"weak": "weak", "strong": "strong", "say": "say", "remember": "remember", "try": "try"}
    def callout(m):
        word = m.group(2).split()[0].lower().strip(".:")
        cls = tags.get(word)
        if not cls:
            return m.group(0)
        return f'<blockquote class="{cls}">{m.group(1)}<span class="tag">{m.group(2).rstrip(".: ")}</span>'
    body = re.sub(r"<blockquote>(\s*<p>)<strong>([^<]{2,40})</strong>\s*", callout, body)

    # boxed entries: a bold numbered question line followed by its labelled list
    def entry(m):
        inner = re.sub(r"<li>([A-Z][A-Za-z ]{2,11}):\s*(.*?)</li>",
                       r'<li><span class="lab">\1</span><span class="val">\2</span></li>', m.group(0), flags=re.S)
        return '<div class="entry">' + inner + "</div>"
    body = re.sub(r"<p><strong>\d+\. .*?</p>\s*<ul>.*?</ul>", entry, body, flags=re.S)

    # boxed cards: every h3 block inside the configured section
    card_id = CFG.get("card_section")
    if card_id:
        a = body.index(f'<h2 id="{card_id}"')
        a = body.index("</h2>", a) + len("</h2>")
        b = body.find("<h2", a)
        b = len(body) if b < 0 else b
        chunks = re.split(r"(?=<h3)", body[a:b])
        body = body[:a] + chunks[0] + "".join(f'<div class="card">{c}</div>' for c in chunks[1:]) + body[b:]

    def keep(m):
        t = m.group(0)
        return t.replace("<table", '<table class="keep"', 1) if t.count("<tr") <= 10 and t.startswith("<table>") else t
    body = re.sub(r"<table.*?</table>", keep, body, flags=re.S)

    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc_items = "\n".join(
        f'<li><a href="#{i}">{t}</a><span class="pg">{pages.get(i, "")}</span></li>' for i, t in heads)
    toc = f"""<section class="toc"><h2>Contents</h2><ol>{toc_items}</ol>
<div class="how">{"".join(f"<p>{p}</p>" for p in CFG["how"])}</div></section>"""

    points = "".join(f"<div><b>{p['head']}</b>{p['text']}</div>" for p in CFG["points"])
    cover = f"""<section class="cover">
<div class="kicker">{CFG["kicker"]}</div>
<h1>{html.escape(TITLE)}</h1>
<div class="sub">{html.escape(CFG["subtitle"])}</div>
<div class="points">{points}</div>
<div class="meta">{CFG["meta"]}</div>
</section>"""

    css = CSS.replace("%%FOOTER%%", TITLE.replace('"', "'"))
    if CFG.get("style") == "accessible":
        css += CSS_ACCESSIBLE.replace("%%FONTS%%", (HERE / "fonts").as_uri())
    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{html.escape(TITLE)}</title><style>{css}</style></head>
<body>{cover}{toc}<main>{body}</main></body></html>""", heads


def render(html_text: str, out: Path):
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d) / "guide.html"
        tmp.write_text(html_text, encoding="utf-8")
        subprocess.run(["node", str(HERE / "render.js"), str(tmp), str(out)], check=True)


def find_pages(pdf: Path, heads) -> dict:
    reader = PdfReader(str(pdf))
    texts = [re.sub(r"[^A-Za-z0-9]", "", p.extract_text() or "") for p in reader.pages]
    pages = {}
    for hid, title in heads:
        key = re.sub(r"[^A-Za-z0-9]", "", html.unescape(re.sub(r"<[^>]+>", "", title)))
        for n, t in enumerate(texts):
            if n < 2:  # cover and contents
                continue
            if key in t[:len(key) + 90]:
                pages[hid] = n + 1
                break
        else:
            raise SystemExit(f"heading not found: {title}")
    return pages


first, heads = build_html({})
render(first, OUT)
pages = find_pages(OUT, heads)
final, _ = build_html(pages)
render(final, OUT)
assert find_pages(OUT, heads) == pages, "page numbers moved between passes"
print(len(PdfReader(str(OUT)).pages), "pages")
for hid, title in heads:
    print(f"{pages[hid]:>3}  {re.sub('<[^>]+>', '', title)}")
