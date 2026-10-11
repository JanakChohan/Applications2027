# Writer style guide for the KKR packs

You write HTML fragments (no <html>/<head>/<body>) into a parts folder. The build script
(`python3 build.py kcs|main [--only 03_,04_] [--png]`) concatenates every `*.html` in the folder in
filename order, inlines `style.css`, builds the contents page with real page numbers, and renders a PDF.
Preview only your own files with `--only <prefix>`; output lands in `../output/_preview_<key>_<prefix>/` with
PNGs of every page in `_png_<key>/` when you pass `--png`. LOOK at the PNGs of every page with a figure
(Read tool on the .png) and fix clipped, overlapping or overflowing text before you finish.

## Reader
A UK undergraduate with near-zero finance knowledge, a visual learner, applying to KKR London's 2027
summer internship, first choice Global Client Solutions (KCS). They want to understand the role and firm
better than any other applicant and give answers nobody else can give. Write for a beginner without
dumbing down. Define every term in line the first time, in plain English.

## Prose rules
- Short sentences. Concrete nouns. Smart analyst briefing a colleague.
- NO em dashes (—) anywhere. Use commas, colons, full stops or brackets. No en-dash as a dash either (ranges like 2024-2026 with a hyphen are fine).
- No filler ("in today's rapidly evolving landscape", "plays a pivotal role", "delve", "tapestry", "robust", "seamless", "navigate the complexities"). No triads of adjectives.
- Never fabricate. Only facts in the research files under `../research/`. Every non-obvious claim carries its source ID exactly as written in the research files, e.g. `[S12]`, and a confidence tag `[Confirmed]`, `[Reported]` or `[Inferred]`. The build turns these into styled markers automatically. Your own reasoning is `[Inferred]`.
- Estimates are labelled "estimate" with a range and an as-of date.

## Structure markup
```html
<section class="part" id="k3">          <!-- unique id; prefix k for KCS pack, m for main pack -->
  <div class="part-band"><div class="num">Part 3</div><h1>Title</h1><p>One-line promise of this part.</p></div>
  <h2 id="k3-what">Section title</h2>     <!-- every h2 needs a unique id: it goes in the contents page -->
  <h3>Sub-heading</h3> <p>...</p>
</section>
```
Use `<div class="part-band alt">` for a teal variant on alternate parts if you like.

## Callouts (use often; they make the pack scannable)
```html
<div class="box term"><span class="lbl">Key term</span><p><b>Limited partner (LP):</b> ...</p></div>
<div class="box say"><span class="lbl">Say this in the interview</span><p>...</p></div>
<div class="box dont"><span class="lbl">Don't say this</span><p>...</p></div>
<div class="box opinion"><span class="lbl">Your opinion goes here</span><p>...</p></div>
<div class="box unsure"><span class="lbl">Source uncertain</span><p>...</p></div>
<div class="box key"><span class="lbl">Why this matters</span><p>...</p></div>
```
Other components: `<div class="two">..</div>` / `<div class="three">` grids; stat tiles
`<div class="tile"><div class="big">$744bn</div><div class="lab">AUM, 30 Jun 2026 [S5]</div></div>`;
`<table>` with `<thead>`; `<table class="tight">` for dense ones; Q&A blocks
`<div class="qa"><div class="q">Q</div><div class="m">What it tests: ...</div>...</div>`;
scenario cards:
```html
<div class="card easy|med|hard"><div class="hd"><span>Scenario title</span><span>EASY</span></div><div class="bd">
<p><b class="k">Setup</b> ...</p><p><b class="k">The trap</b> ...</p><p><b class="k">Say</b> ...</p>
<p><b class="k">Why it works</b> ...</p><p><b class="k">The twist</b> ...</p></div></div>
```
`<div class="pb"></div>` forces a page break.

## Figures (inline SVG; the reader is visual, so draw generously)
```html
<figure>
<svg viewBox="0 0 680 360" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Arial" font-size="11">
  ...
</svg>
<figcaption><span class="fig-num"></span> <b>Title.</b> What to notice. Source: KKR Q2 2026 earnings release [S5], as of 30 Jun 2026. Estimates labelled.</figcaption>
</figure>
```
- Always viewBox width 680. Height as needed. A full-page figure: wrap in `<figure class="fullpage">` with a viewBox like `0 0 680 900`.
- Rendered width is about 180mm, so 1 unit = 0.26mm. Minimum font-size 9.5; body labels 10.5 to 12; titles inside SVG 13 to 15.
- TEXT MUST FIT. SVG text does not wrap: break long labels into several `<text>`/`<tspan x=.. dy="1.2em">` lines yourself. Budget roughly 6.2 units per character at font-size 11. Keep 8+ units padding inside boxes.
- Palette (structure): navy #13294B, navy-2 #24467A, navy-soft #E8EDF5, accent #C8792B, accent-soft #FBF1E6, signal teal #0E8F7E, signal-soft #E3F4F1, red #B23A48, amber #D9A21B, green #2E7D32, ink #1B1F27, ink-2 #4A5160, rule #D5DAE3.
- Data series (categorical, in this fixed order): #2a78d6, #eb6834, #1baf7a, #eda100, #6250d6, #e34948. Text never takes the series colour: labels stay ink/ink-2. Direct-label series. One y-axis only. Thin bars with 2px gaps, recessive gridlines (#D5DAE3).
- Every figure that shows a number carries the source ID and as-of date in its caption; estimated numbers carry "est." on the chart itself.
- Use arrows with `<defs><marker id="arrUNIQUE" ...>`: make marker ids unique per figure (prefix with your part id) because all SVGs share one document.

## Addendum for the "What you will learn" technical guide (`parts_learn/`, build key `learn`, ids prefix `l`)
- The reader asked for MAXIMUM technical depth explained from zero: every mechanism shown step by step, with worked numerical examples (clearly labelled "illustrative numbers" unless sourced), formulas written out in plain words and symbols, and a diagram for every mechanism.
- Every module must answer three questions explicitly, in boxes: "What you will learn" (the technical skill), "Where you would meet it at KKR" (a specific fund, product, client type, team or news story, sourced), and "Why you could not learn this the same way elsewhere" (mechanism, honest, never overclaim; tag [Inferred] where reasoning).
- Use `<div class="box key"><span class="lbl">What you will learn</span>`, `<div class="box term"><span class="lbl">Where you meet it at KKR</span>`, `<div class="box opinion"><span class="lbl">Only at KKR</span>` for these three.
- End each module with "Say it in one line" (a SAY THIS box): one sentence the candidate could use in the application answer or interview.
- SVG text may contain source markers like [S12] in plain text (the build leaves SVG untouched), but keep them short.

## Addendum for the Pictet experience guide (`parts_pictet/`, build key `pictet`, ids prefix `p`)
- Reader: same candidate. They did a roughly six-week summer internship at Pictet Asset Management in what they call the "Global Client Group" (client servicing, client onboarding, client relationship management). Public sources do not use the name "Global Client Group"; write "the client group (the candidate's team name)" and never contradict the candidate's own account.
- HONESTY RULE: never invent what the candidate personally did, achieved or measured. Describe what such a team does and what interns in such seats typically do, labelled [Inferred] or sourced. When you show example CV bullets or stories, mark them "Template: keep only if true" and use [square-bracket slots] for their real specifics.
- Required boxes per major section: `box key` "What the work really is" (the technical content); `box term` "How it transfers to KKR KCS" (specific KKR product, client type, team or task, sourced); `box opinion` "Say it in one line".
- Same technical depth as the "What you will learn" guide: explain every mechanism from zero, worked examples, diagrams for every mechanism.
