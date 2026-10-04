# Writer spec: Deloitte UK Consulting & Technology interview pack

You write HTML FRAGMENTS (not full documents) for one or more Parts of a single PDF report. A build script
(build.py) concatenates every file in build/parts/ in filename order, adds a cover and a contents page, converts
markers, renders to A4 PDF with Chromium and stamps running headers/footers. Read style.css in this folder to see the classes.

## Inputs you must read
- ../BRIEF.md (the task and hard rules)
- The findings files in ../findings/ named in your task (they are the ONLY factual base; every fact must come from them)
- This spec

## Hard content rules
- Never fabricate. Every non-obvious factual claim carries a source marker written as plain text `[S12]` (or `[S12, S40]`),
  using ONLY source IDs that appear in the findings files' source tables. The build turns these into links.
- Confidence tags in plain text: `[Confirmed]`, `[Reported]`, `[Inferred]`, `[Estimate]`, `[Anecdote]`. Put them after the claim.
- If findings say something is uncertain, say so, using a SOURCE UNCERTAIN callout.
- Write for a total beginner without dumbing down. Define each term in line the first time you use it, in plain English.
- Short sentences. Concrete nouns. British English. NO em dashes (use commas, colons, full stops or brackets). No "in today's
  rapidly evolving landscape", no "delve", no "tapestry", no triads of adjectives, no "not just X but Y" constructions, no hype.
  Write like a smart analyst briefing a colleague.
- People: public professional information only.
- The candidate: UK undergraduate applying for 2027 entry to Deloitte UK Consulting/Technology (grad, internship or placement),
  no interview booked yet, ~2/10 industry knowledge, visual learner.

## HTML structure
Each Part is one section. Filenames: parts/pNN_slug.html where NN is the two-digit part number (00..16) plus a letter if split
(e.g. p11a_, p11b_). Only the first file of a Part opens the <section>; continuation files open
`<section class="part cont" id="p11b" data-title="Part 11: The scenario playbook (cont.)">` (cont. sections still start a new page; avoid splitting Parts unless it's very long).

```html
<section class="part" id="p3" data-title="Part 3: Why Deloitte is built this way">
  <div class="band b3"><span class="pnum">Part 3</span><h1>Why Deloitte is built this way</h1>
    <p class="lede">One or two sentences: what this part gives you.</p></div>
  <h2>Section heading (appears in contents)</h2>
  <p>...</p>
  <h3>Sub-heading (not in contents)</h3>
</section>
```
Band colour classes b2..b6 vary the left stripe; pick any.
Do not put id attributes on h2 unless needed; the build assigns them.

Components:
- Callouts (use generously, they are the visual rhythm):
  `<div class="callout term"><b class="ct">KEY TERM</b><p><b>Utilisation</b>: ...</p></div>`
  `<div class="callout say"><b class="ct">SAY THIS IN THE INTERVIEW</b><p>...</p></div>`
  `<div class="callout dont"><b class="ct">DON'T SAY THIS</b><p>...</p></div>`
  `<div class="callout opinion"><b class="ct">YOUR OPINION GOES HERE</b><p>prompt + both sides + a suggested stance</p></div>`
  `<div class="callout uncertain"><b class="ct">SOURCE UNCERTAIN</b><p>...</p></div>`
- KPI tiles: `<div class="kpi"><div><b>$70.5bn</b><span>Global revenue FY2025 [S80]</span></div>...4 tiles...</div>` (values must be sourced)
- Tables: `<table class="data">` (add `small` for dense ones). Use <thead>.
- Two/three columns: `<div class="two">...</div>`, `<div class="box">`.
- Scenario cards:
```html
<div class="card medium"><div class="card-h"><span>JD line 3 · Rung 2: Client changes scope mid-sprint</span><span>MEDIUM</span></div>
<div class="card-b"><span class="lbl">Setup</span><p>...</p><span class="lbl">The trap</span><p>...</p>
<span class="lbl">What to say</span><p>...</p><span class="lbl">Why it works</span><p>... [S350]</p>
<span class="lbl">The twist, and how to hold</span><p>...</p></div></div>
```
  classes: easy / medium / hard.
- Question bank entries: `<div class="q"><div class="qq">Q12. Why consulting rather than industry?</div><div class="qm"><b>Tests:</b> ... <b>Structure:</b> ... <b>Weave in:</b> ... <b>Trap:</b> ...</div></div>`

## Figures (inline SVG). These are the most important visual element.
```html
<figure class="fig" id="f07"><div class="fig-title"><span class="fn">Figure 7</span>Title that states the point</div>
<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg"> ... </svg>
<figcaption>Source: [S80] Deloitte Global Impact Report 2025 (Sep 2025); [S95]. Values for FY2026 are estimates. Read: one line on how to read it.</figcaption></figure>
```
- Use `class="fig full"` for a full-page figure (then use viewBox about 640 x 900).
- Number figures with the figure number given in your task. Put figure numbers in the fig-title only.
- viewBox width 640 (renders ~176mm wide, so 1 SVG unit ~ 0.275mm). Minimum font-size 9 in SVG units for labels, 11-13 for main labels, 15-18 for titles inside the figure. Use font-family inherited (Inter).
- TEXT MUST FIT. SVG does not wrap. Budget ~0.55 x font-size per character for Inter (e.g. 20 characters at size 11 = ~121 units). If a label is long, split it across several <text> lines (use <tspan x=".." dy="1.2em">) and make the box bigger. Leave 8+ units padding inside boxes. A QA script flags any text that spills out of the rect it sits in, overlaps other text or exits the viewBox; text that intentionally sits outside boxes (e.g. axis labels next to bars) is fine as long as it isn't centred inside a rect. Add attribute data-free="1" to a <text> that deliberately crosses a rect boundary.
- Palette for SVG fills/strokes: navy #0E2240, navy2 #1F3A5F, navy3 #3A5A86, light blues #DCE6F2 #BFD0E6, accent copper #C8742A, accent light #FBEEDF, signal violet #7A3FB0 (opinion only), good #1E7B4F/#E5F3EB, bad #B3261E/#FBE9E7, warn #B7791F/#FFF5E0, ink #1A1F2B, muted #5B6577, rules #D9DEE7, tint #F3F5F9. White text only on navy/navy2/copper/good/bad fills.
- Every figure that contains numbers has a caption naming the source ID and date. Estimates labelled "Estimate" ON the chart itself.
- Charts: draw axes and gridlines in #D9DEE7, label directly (avoid legends where possible), zero-based bars, show the value on each bar.
- Diagrams must show real mechanism (arrows with labels saying what flows), not decorative boxes. Use <defs><marker> arrowheads (give marker ids a unique prefix per figure, e.g. id="f07a", because all SVGs share one document).
- Do not use <foreignObject>, external images, or scripts.

## Validate before you finish (ALWAYS in a private copy; other writers work concurrently)
```
W=/tmp/claude-0/-home-user-Applications2027/e13d6d81-898d-57fb-9a03-1be32ed50df2/scratchpad/w_<yourname>
rm -rf $W && mkdir -p $W && cp -r ../build $W/ && cd $W/build && find parts -type f ! -name 'pNN*' -delete   # keep only your files
ln -s /tmp/claude-0/-home-user-Applications2027/e13d6d81-898d-57fb-9a03-1be32ed50df2/scratchpad/findings $W/findings
python3 build.py && node qa.js $PWD/Deloitte_Consulting_Technology_Complete_Interview_Pack.html
pdftoppm -r 60 -png out/Deloitte_Consulting_Technology_Complete_Interview_Pack.pdf $W/pg   # then Read the PNGs that hold figures
```
Write your real files into the SHARED build/parts/ folder, and copy them into the private copy to test (or edit in the private copy and copy back when done; make sure the shared folder ends with your final versions).
Fix every SPILL / OVERLAP / OVERFLOW / WIDE line for your figures, and look at every figure page image for clipped or cramped text.
Also check the printed "cited-but-missing" list: any source ID you cited that is not in the findings tables must be fixed.

Final message: list your files, figure numbers produced, word count estimate, any facts you wanted but could not source.
