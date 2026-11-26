#!/usr/bin/env python3
"""Build the HireVue guide PDF from the markdown report.

Usage: build.py <report.md> <out.pdf>
Two passes: the first finds the page each section starts on, the second
writes those numbers into the contents page.
"""
import html
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).parent
SRC, OUT = Path(sys.argv[1]), Path(sys.argv[2])
TITLE = "Pass HireVues by answering the marking scheme"
SUBTITLE = ("Why one-way video interviews get rejected, how they are really "
            "marked, and what to change. Written from zero.")
DATE = "26 November 2026"

CSS = r"""
@page { size: A4; margin: 20mm 19mm 21mm 19mm;
  @bottom-center { content: counter(page); font: 8.5pt Inter, sans-serif; color: #6b7480; }
  @bottom-left { content: "Pass HireVues by answering the marking scheme"; font: 8pt Inter, sans-serif; color: #9aa2ac; }
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
"""

FIG_ROUTES = """
<figure>
<div class="flow">
  <div class="start">Your recorded answers<small>The employer chooses which route applies. Most do not say.</small></div>
  <div class="route human">
    <div class="name">Route 1: people mark it <span>(what Goldman Sachs and PwC say they do)</span></div>
    <div class="steps">
      <div class="s">A recruiter or member of the business plays each answer, at any speed</div><div class="arr">&rarr;</div>
      <div class="s">Gives each question a star rating on a 3-, 4- or 5-point scale</div><div class="arr">&rarr;</div>
      <div class="s">System averages the stars; reviewer adds Yes, Maybe or No</div><div class="arr">&rarr;</div>
      <div class="s">You are ranked against other applicants, with your CV alongside</div>
    </div>
  </div>
  <div class="route ai">
    <div class="name">Route 2: AI scores it first <span>(optional extra; you see a consent page)</span></div>
    <div class="steps">
      <div class="s">Speech is turned into a typed transcript. Face, voice and background are not used</div><div class="arr">&rarr;</div>
      <div class="s">Words are compared with past answers that trained people marked 1 to 5</div><div class="arr">&rarr;</div>
      <div class="s">You get a percentile and a band: top, middle or bottom third</div><div class="arr">&rarr;</div>
      <div class="s">Top band advanced, middle band watched, bottom band often not watched</div>
    </div>
  </div>
</div>
<figcaption>What happens to a HireVue recording. Both routes use the same kind of marking scheme, so an answer built for that scheme serves both. Source: HireVue help centre and 2025 Explainability Statement, cited in the text.</figcaption>
</figure>
"""

FIG_BAR = """
<figure>
<div class="bar">
  <div class="h" style="flex:8">8s</div>
  <div class="si" style="flex:17">17s</div>
  <div class="t" style="flex:9">9s</div>
  <div class="a" style="flex:55"><b>Action: what you did, in &ldquo;I&rdquo; sentences</b>55s</div>
  <div class="r" style="flex:11">11s</div>
  <div class="l" style="flex:5">5s</div>
  <div class="spare" style="flex:15">unused</div>
</div>
<div class="barlabel"><span>0:00 recording starts</span><span>stop at about 1:45</span><span>2:00 cut-off</span></div>
<div class="legend">
  <span><i class="h"></i>Headline sentence</span><span><i class="si"></i>Situation</span><span><i class="t"></i>Task</span>
  <span><i class="a"></i>Action</span><span><i class="r"></i>Result</span><span><i class="l"></i>Lesson or link to the role</span>
</div>
<figcaption>A story answer inside a two-minute limit. More than half the time goes on your own actions. The last five seconds, the lesson or link to the role, is the part to drop if the clock is tight.</figcaption>
</figure>
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
    body = '<h2 id="the-short-answer">The short answer</h2>\n' + lead + rest

    # figures
    sec = body.index('<h2 id="what-a-hirevue-is')
    k = body.index("</p>", sec) + len("</p>")
    body = body[:k] + FIG_ROUTES + body[k:]
    i = body.index("90-second limit</th>")
    j = body.index("</table>", i) + len("</table>")
    body = body[:j] + FIG_BAR + body[j:]

    # table column hints
    for first, cls in (("Rank", "narrow-first"), ("Mark", "narrow-first"), ("Date", "narrow-first"), ("Claim", "wide-first")):
        body, n = re.subn(r'<table>(\s*<thead>\s*<tr[^>]*>\s*<th>' + first + '</th>)', r'<table class="' + cls + r'">\1', body)
        assert n == 1, first

    def keep(m):
        t = m.group(0)
        return t.replace("<table", '<table class="keep"', 1) if t.count("<tr") <= 10 and t.startswith("<table>") else t
    body = re.sub(r"<table.*?</table>", keep, body, flags=re.S)

    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body)
    toc_items = "\n".join(
        f'<li><a href="#{i}">{t}</a><span class="pg">{pages.get(i, "")}</span></li>' for i, t in heads)
    toc = f"""<section class="toc"><h2>Contents</h2><ol>{toc_items}</ol>
<div class="how"><p><strong>How to read this.</strong> Sections 1 to 6 explain how the stage works and why people are cut. Sections 7 to 10 are what to do about it. Square brackets in example answers, like [result you measured], mark facts only you can supply.</p>
<p><strong>Sources.</strong> Bracketed names in the text are links to the source for the sentence before them. Where the evidence is weak or sources disagree, the text says so.</p></div></section>"""

    cover = f"""<section class="cover">
<div class="kicker">HireVue deep dive &middot; 2027 applications</div>
<h1>{html.escape(TITLE)}</h1>
<div class="sub">{html.escape(SUBTITLE)}</div>
<div class="points">
<div><b>It is marked on content</b>HireVue&rsquo;s AI reads only a transcript of your words. Human markers count evidence against a rating scale.</div>
<div><b>It is a ranking, not a pass mark</b>Under 1% of applicants at the largest banks get an offer, and some rejections are decided before the video.</div>
<div><b>You can test which problem is yours</b>A one-week diagnosis separates content, script, camera and causes outside the video.</div>
</div>
<div class="meta">Prepared {DATE} &middot; Based on five research strands and 225 cited sources &middot; Evidence limits stated throughout</div>
</section>"""

    return f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{html.escape(TITLE)}</title><style>{CSS}</style></head>
<body>{cover}{toc}<main>{body}</main></body></html>""", heads


def render(html_text: str, out: Path):
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d) / "guide.html"
        tmp.write_text(html_text, encoding="utf-8")
        subprocess.run(["node", str(HERE / "render.js"), str(tmp), str(out)], check=True)


def find_pages(pdf: Path, heads) -> dict:
    reader = PdfReader(str(pdf))
    texts = [re.sub(r"\s+", "", p.extract_text() or "") for p in reader.pages]
    pages = {}
    for hid, title in heads:
        key = re.sub(r"\s+", "", html.unescape(re.sub(r"<[^>]+>", "", title)))
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
