# Authoring rules for report parts (read fully before writing)

You write ONE OR MORE HTML fragment files in /home/user/Applications2027/LSEG/build/parts/. They are concatenated in filename order into one A4 print document styled by /home/user/Applications2027/LSEG/build/style.css (read it: it defines every class below). No <html>, <head>, <body>, <style> or <script> tags in your fragment. No external images. All diagrams are inline SVG.

## Reader
A UK penultimate-year undergraduate, finance beginner (knowledge ~3/10), visual learner, applying to the LSEG Business Management Summer Internship 2027 (Markets side: London Stock Exchange, LSEG FX, Tradeweb, Turquoise, LCH). Stage now: application (deadline 30 Oct 2026, rolling); next stages: untimed Immersive Online Assessment, strengths-based video interview, half-day virtual assessment centre. Interviewers are not named. Candidate CV details are NOT known: where a section needs them (CV grill), give a method and worked placeholders, clearly marked.

## Voice
Short sentences. Concrete nouns. Smart analyst briefing a colleague. Define every term the first time it appears, inline, in plain English (and use a KEY TERM callout for the big ones). NO em dashes (use commas, colons, full stops, or "to" for ranges). No "in today's rapidly evolving landscape", no adjective triads, no "delve", "crucial", "landscape", "robust", "seamless", "leverage" (verb), "pivotal", "testament". Write British English.

## Evidence rules (non-negotiable)
- Only use facts present in the research files in /home/user/Applications2027/LSEG/research/ (WS*.md). Never invent figures, names, dates, quotes, deals.
- Every non-obvious factual claim gets a source marker using the SAME source IDs as the research files: `<span class="s">[S74]</span>` (several: `[S74, S81]`).
- Confidence tags after claims where useful: `<span class="c c-conf">Confirmed</span>`, `<span class="c c-rep">Reported</span>`, `<span class="c c-inf">Inferred</span>`. Use Inferred for your own reasoning.
- If research files disagree or are thin, say so in a SOURCE UNCERTAIN callout.

## Structure
Each Part file starts with:
```html
<section class="part" id="p2" data-toc="Part 2: The firm as a business, from the inside">
<div class="band b2"><div class="num">Part 2</div><h1>The firm from the inside</h1><p class="lede">One-sentence lede.</p></div>
...content...
</section>
```
Band colour classes: band (navy), b2, b3, b4, b5. Every main section heading is `<h2 id="p2-money">How LSEG makes money</h2>` (unique ids, prefix with part id). These h2s populate the contents page, so keep titles short (under 60 chars). Use h3/h4 below that freely.

## Components (exact markup)
Callouts:
```html
<div class="callout key"><span class="lab">Key term</span><p><b>CCP (central counterparty)</b>: ...</p></div>
<div class="callout say"><span class="lab">Say this in the interview</span><p>...</p></div>
<div class="callout dont"><span class="lab">Don't say this</span><p>...</p></div>
<div class="callout opinion"><span class="lab">Your opinion goes here</span><p>Prompt + both sides + a suggested position.</p></div>
<div class="callout uncertain"><span class="lab">Source uncertain</span><p>...</p></div>
<div class="callout note"><span class="lab">Why this matters</span><p>...</p></div>
```
KPI tiles: `<div class="kpis"><div class="kpi"><div class="v">£8.6bn</div><div class="l">Total income FY2025 [S74]</div></div>...</div>` (4 per row).
Scenario card:
```html
<div class="card medium"><div class="hd"><span>Title</span><span class="lvl">Medium</span></div><div class="bd">
<div class="row"><b>Setup</b> ...</div><div class="row"><b>Trap</b> ...</div><div class="row"><b>Say</b> ...</div><div class="row"><b>Why</b> ... [Sxx]</div><div class="row"><b>Twist</b> ... <i>Hold:</i> ...</div></div></div>
```
Question bank item: `<div class="qa"><div class="q">Q12. Why LSEG and not ICE?</div><div class="m"><b>Testing</b> ... <b>Structure</b> ... <b>Weave in</b> ... <b>Trap</b> ...</div></div>`
Tables: plain `<table><thead><tr><th>..</th></tr></thead><tbody>..</tbody></table>`; add class "tight" for dense ones.
Layout helpers: `.grid2`, `.grid3`, `.two` (two text columns), `.pb` (force page break), `.avoid`, `.small`, `.muted`, `.pill`.

## Figures (inline SVG): the most important quality bar
```html
<figure class="fig" id="fig-07">
<div class="ft">Figure 7</div><div class="fh">Short headline that states the point</div>
<svg viewBox="0 0 700 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="...">...</svg>
<figcaption>One or two sentences telling the reader what to notice.</figcaption>
<div class="fsrc">Source: LSEG Annual Report 2025 [S74], FY2025 figures; headcount is a press estimate [S88], 2026.</div>
</figure>
```
Add class "full" (`<figure class="fig full">`) for full-page figures (they start a new page; use viewBox about 700x900).
SVG rules (violations cause clipping, which we check by rasterising):
- Always use a viewBox, width 700 units. The printable width is ~178mm, so 700 units ≈ 0.25mm per unit. Minimum font-size 10 units (body labels 11-13, titles 14-16). Never smaller than 10.
- Text never runs past its box: estimate 0.55 × font-size per character for width. Wrap long labels manually with multiple <text> or <tspan x=.. dy=..> lines. Keep 8 units padding inside boxes. Keep everything inside the viewBox with 10 units margin.
- Palette only: navy #0B1F3A, #17345F, #2C4F86, light #DCE6F3, mist #F3F6FA, accent #D9762B (light #FBEBDD), signal violet #6A3FC8 (light #EFE8FB), green #2E8B57 (#E4F3EA), amber #C98A12 (#FBF1DC), red #B8352A (#F8E3E0), ink #1B2333, muted #5B6577, lines #D5DCE6. White text only on dark fills.
- Set font-family is inherited from CSS (Inter). Use font-weight 700/800 for emphasis.
- Every figure that shows numbers carries its source and date in .fsrc, and estimates are labelled "est." ON the chart itself.
- Charts drawn to scale (compute bar lengths from the numbers). Axis labels and units present.
- Diagrams show a mechanism (flows with arrows, layers, who-gives-what), not decorative boxes. Arrowheads: define a <marker> inside <defs> with a unique id per figure (e.g. id="ar7") to avoid id clashes across figures.

## Length
Be substantive. A part typically runs 6 to 20 printed pages. Prefer depth with structure (tables, callouts, figures) over walls of text.

## When done
Validate your fragment is well-formed (balanced tags; run `python3 -c "import html.parser"`-style check or `xmllint --html` if available) and report the file names, the figure numbers you produced, and any source IDs you used that you were not sure about.

## Cross-pack facts to keep consistent (from research; cite the IDs)
- UK politics as of Oct 2026: Andy Burnham became Prime Minister on 20 Jul 2026; John Healey replaced Rachel Reeves as Chancellor [S242, S243, S244]. Reeves gave the 14 Jul 2026 Mansion House speech before leaving. Never call Reeves the current Chancellor. Autumn Budget: 28 Oct 2026.
- LSEG owns about 94.2% of LCH Group after 2024 purchase (WS3), and H1 2026 says it is buying out remaining minorities to take it above 95% (WS5). Not 82.6%.
- LSEG H1 2026 (30 Jul 2026): total income £4,799m, +8.4%; Markets division fastest growing at +11.9% (WS4/WS5).
- Bond consolidated tape: ETS Connect UK, live 22 Jun 2026. PS24/14 is the transparency policy statement, not the tape appointment.
- 1963 Eurobond (Autostrade) was arranged in London but listed in Luxembourg.
- Today's date is 5 Oct 2026. LSEG Q3 trading statement expected 22 Oct 2026 (not yet out).
- LSEG has FOUR divisions (2026): Data & Analytics, FTSE Russell, Risk Intelligence, Markets. Markets is about 40% of revenue, +11.9% in H1 2026, 58.6% margin (WS2).
- Headcount: 28,516 at end 2025 per Annual Report (WS2); the JD says "25,000 people across 65 countries". Flag the mismatch rather than pick one silently.
- Tradeweb: LSEG economic interest about 50.9% (WS2); voting about 89.9% (WS3). Say "majority-owned".
- FY2025: income ex recoveries £8,986m (+7.1% organic), adj EBITDA £4,523m (50.3%), recurring 73% (WS2).
- Share price derating: 12,095p (5 Feb 2025) to 7,170p (4 Feb 2026), -12.8% on 3 Feb 2026 on AI-tool fears; Elliott stake reported Feb 2026; about 8,216p on 5 Oct 2026 (WS2). CEO David Schwimmer, CFO Michel-Alain Proch, Chair Don Robert, unchanged.
- TradElect outage was 8 Sep 2008 (not 2009).
- LCH stake: Annual Report 2025 says 94.4% (WS8, S3xx); WS3 says 94.2%. Use "about 94%" and cite both, rising above 95% after the July 2026 deal.
- Ownership: Tradeweb 50.9% economic; Turquoise 84.2%; Post Trade Solutions 80% (11 banks bought 20% for £170m, Oct 2025) (WS8).
- Customers: 44,000+ in 170+ countries (not ~40,000); FXall 2,400+ institutional clients, 200+ liquidity providers (WS8).
- Daniel Maguire runs LSEG Markets and LCH, the division this internship sits in (WS8). Check WS8 exec list for names/dates.
- Do NOT claim commercial bundling of SwapClear with Tradeweb or ForexClear with FXall: no LSEG statement found, and open access makes it unlikely.
- No named Bank of England fine on LCH was found: do not cite one.
