# MASTER PROMPT: full interview research pack for any firm and role

How to use: fill in every field in the INPUTS block. Leave everything else as it is. Paste the whole thing as one message. The output is a single PDF report (plus its HTML source and three small companion files) that contains everything the Millennium pack contained across five separate documents: the role decoded, the team mapped, the firm explained from the inside, the industry from zero, the competitive landscape, what the firm's customers actually buy, why the firm is built the way it is, the non-investing or non-core side, live news, the interview process, a question bank, a scenario playbook with a frame-holding method, a CV grill, a cheat sheet, a glossary and a full source table.

---

# INPUTS (fill these in)

- FIRM: {{FIRM}} (full legal name of the employing entity if known, e.g. "{{LEGAL_ENTITY}}", registered address, regulator and registration number if any)
- ROLE: {{ROLE_TITLE}} (requisition ID {{REQ_ID}} if any), location {{CITY}}
- INTERVIEW: {{DATE}}, {{TIME}} {{TIMEZONE}}, {{DURATION}}, {{FORMAT: video/phone/in person}}, round {{ROUND}}
- INTERVIEWERS: {{NAMES AND TITLES IF KNOWN}}; coordinator {{NAME, FUNCTION}}
- PROCESS SO FAR: {{e.g. application form -> online assessment -> this interview}}
- CANDIDATE: {{degree, year, prior knowledge level of this industry (0-10), learning style, what they most want to be able to answer}}
- INSIDER INTELLIGENCE (optional): {{anything heard from people who interviewed or work there, e.g. "scenario-heavy, they try to break your frame", "mostly behavioural"}}
- JOB DESCRIPTION (verbatim, do not re-fetch):
{{PASTE THE FULL JD HERE}}
- TODAY'S DATE: check it. The interview may be imminent; prioritise the highest-value sections first and always produce a usable artefact.

---

# MISSION

Produce a complete interview preparation research pack for the candidate above. The candidate wants to go from their current knowledge level to being able to speak about the firm, the role and the industry fluently, form and defend their own opinions, and answer "why {{FIRM}}?" with a mechanism-based answer that no other candidate could give. The pack must read as if written by someone who worked at the centre of the firm, but be built only from public, sourced material.

# HARD RULES

1. Never fabricate. No invented figures, returns, headcounts, deal names, quotes or people. Every non-obvious factual claim carries an inline source marker [S12] resolving to a source table with outlet, title, publication date, URL and access date.
2. Flag confidence on every claim: [Confirmed] (primary source or two credible outlets), [Reported] (single credible source), [Inferred] (the author's reasoning). Private firms are mostly reported on by estimate; say so. "Press estimate, range X to Y, as of date" beats false precision.
3. Prefer primary sources: the firm's own site, careers pages and job postings (pull them through the careers API if one exists), regulatory filings (for a US-registered adviser: SEC Form ADV and 13F; for a UK entity: FCA Register, Companies House accounts, MIFIDPRU or equivalent disclosures; for a listed firm: annual report, investor day, earnings calls; adapt to the firm's jurisdiction), regulator policy papers relevant to the role, trade bodies, then quality press.
4. Paywalls: never guess unread content. Record headline, outlet, date, URL, mark PAYWALLED-NOT-READ, and look for a non-paywalled summary.
5. Write for a beginner without dumbing down. Define every term the first time it appears, in line, in plain English. Maintain a glossary.
6. No AI-slop prose. Short sentences. Concrete nouns. No "in today's rapidly evolving landscape", no triads of adjectives, no em dashes. Write like a smart analyst briefing a colleague.
7. People research is strictly public professional information: role, employer, tenure, career path, education, public professional writing or speaking. Nothing personal. If identity cannot be confirmed as the right person at the firm, exclude or flag.
8. Every figure in every diagram carries a source and date under it. Estimates are labelled as estimates on the chart itself.

# WORKING METHOD

- Read the JD line by line before searching. Every duty line becomes (a) a decode target, (b) a scenario in the playbook.
- Run the research workstreams in parallel where the environment allows (research agents), each with its own source-ID range (e.g. WS1 S1-S39, WS1B S40-S69, WS2 S70-S119, WS3 S120-S149, WS4 S150-S219, WS5 S220-S259, WS6 S260-S279, WS7 S280-S299, WS8 S300-S339, WS9 S340-S399). Each agent writes a findings file with six sections: findings, key numbers table, verbatim quotes actually read, source table rows in the format `[Sxx] | Outlet | Title | Pub date | URL | Accessed YYYY-MM-DD | FETCHED/SNIPPET/PAYWALLED | confidence note`, gaps, interview angles.
- At least 12 distinct search queries and 8 full-page fetches per workstream. Snippets are not enough.
- Job postings are the best window into a private firm's internal structure. Fetch every current posting that touches the role's function, its sibling functions, and the central functions (risk, technology, operations, compliance, treasury, business management). Quote the sentences that describe who partners with whom.
- After each workstream, record what could not be established and carry it honestly into the report's gaps section.
- Build the report as one self-contained HTML file with print CSS, render to PDF with headless Chromium via Playwright (A4, printBackground, margins, running header and footer with page numbers). Use inline SVG for every diagram. Two-pass render so the contents page shows real page numbers (render once, map anchor markers to pages, re-render). Keep the HTML alongside the PDF. Rasterise the figure pages and check them for clipped or overflowing text before delivering; fix and re-render.

# WORKSTREAM 1: DECODE THE JOB DESCRIPTION

Work through the JD line by line. For each duty line, explain what it actually involves day to day, who the counterparties are, what "good" looks like, what tools are used, and what structural fact about the firm it reveals. Then:
- A realistic worked day in the seat, hour by hour.
- The full taxonomy of the function's activities and formats.
- Who the internal clients and external counterparties are, concretely.
- What the team is judged on.
- The compliance or control dimension of the role: what bright lines exist, which regulations bind them, why the firm cares, and what a candidate should be able to say unprompted.
- A realistic career path from this seat.

# WORKSTREAM 1B: MAP THE ACTUAL TEAM

The firm probably publishes no org chart. Reconstruct it. Sources: careers postings across all offices (the set of open roles is an org chart in disguise), public professional profiles and aggregators, regulator registers, company filings, conference agendas, trade press, and forum anecdotes marked as such. Deliver: a reconstructed org chart colour-coded by confidence; a headcount estimate with a stated range and the method shown; how the work splits (region, channel, event type, sector, seniority); where the team sits in the firm and who the senior owner is; whether the interviewers sit on this team; a benchmark against peers' equivalent teams.

# WORKSTREAM 2: THE FIRM AS A BUSINESS, FROM THE INSIDE

Explain the firm as an operating model, not a brochure. Cover:
A. The founding insight: what the founder did for a living before, and how that shaped the design. The firm's own words on its mission, the founder's rare public remarks, dated.
B. How the firm makes money: trace the flow from customer capital or revenue through the operating units to costs, fee or margin structure, payouts and net return. Quantify from sources.
C. The "contracts" the business is made of: what each key stakeholder gives and gets (front-line producers, customers or investors, financing counterparties or suppliers). Reconstruct from the firm's own postings, filings and press; label reported norms as norms.
D. The risk or control architecture: what limits exist, who sets them, what happens when they are breached, and why this produces the firm's characteristic result (for a hedge fund: low volatility and a high Sharpe; adapt for other industries).
E. The strategy or business mix and what has grown.
F. Public or private, and what that means for research.
G. The leadership's stated view of the firm's future, and the author's inference from hiring patterns, office expansion and recent moves.
H. Recent moves, last 24 months, date-stamped.
I. The 2005-style skeleton in the cupboard: any regulatory settlement, litigation or public failure, told straight, so nothing surprises the candidate.

# WORKSTREAM 3: COMPETITIVE LANDSCAPE

A comparison table of the firm versus 6 to 10 peers: founded, ownership, size (dated, sourced), model, mix, unit or team count, headcount, fee or pricing structure, recent results, positioning, and how each handles the candidate's function. Then the design choices on which the firm sits at one end of a spectrum (for a multi-manager hedge fund: team independence, capital terms, size of the centre, buying other platforms, ownership and succession; adapt the axes to the industry). Identify the five to seven things the candidate can say about this firm that cannot be said about any rival, each with evidence and a "why it matters". State plainly where the firm does not lead (e.g. not the highest returns) so the candidate never overclaims.

# WORKSTREAM 4: THE INDUSTRY FROM ZERO

4A. The firm's industry from scratch: what the product is, who the customers are, how firms differ (for finance: hedge fund versus asset manager versus other buy-side, and versus banks and private equity; adapt for other sectors), the core vocabulary, and the structural forces reshaping the sector now, sourced from industry reports and regulator publications, with at least three competing views on where it goes over three to five years.
4B. The role's own sub-industry: its history, the regulation that shaped it, the current regulatory direction (get the dates and instrument names exactly right; this is usually the highest-leverage technical point for the role), the competitive map of suppliers, current issues, and what the internal clients actually value today.

# WORKSTREAM 5: LIVE COMMERCIAL AWARENESS

Sweep the last six months of quality press for the firm, its sector, and the role's regulation. For each of the 8 to 12 most relevant stories: headline, outlet, date, URL, a beginner-friendly explanation, why it matters to the firm, why it matters to the role, and one intelligent question or opinion the candidate could raise. Build a reading list of recurring sources to follow.

# WORKSTREAM 6: INTERVIEW INTELLIGENCE

Establish, with confidence levels, the number of rounds, what this round consists of, what follows, and timelines. Produce a question bank of 40+ questions grouped by type, each with what is really being tested, a structure for the answer, the firm facts to weave in and the traps. Scaffolds, not scripts. Produce 8 to 10 questions the candidate should ask that only someone who did real research could ask.

# WORKSTREAM 7: INTERVIEWER BACKGROUNDS

For each named interviewer: current role and team, tenure, career path, education, public professional writing or speaking. Public professional information only; verify identity against the firm and city; exclude anything unconfirmed. Determine whether they are practitioners in the function or recruiters, because that changes how every answer is pitched. No manipulation playbook; guidance on reading and adapting to interviewer type live.

# WORKSTREAM 8: WHY THE FIRM, BUILT FROM MECHANISM

This is the section that makes the pack different. Answer four questions with fresh research, not recycled adjectives:
1. Why is the business structured this way? Why this many units or teams rather than fewer bigger ones? What is the theory (for a platform: diversification maths, fee integrity, attributable pay, replaceable seats, information barriers) and what does the structure cost (duplication, no idea flow, turnover, crowding)?
2. How do the teams work together, and if they do not, why not, and where does collaboration actually live? Use the firm's own wording and read it precisely.
3. What is the fundamental value the firm gives its customers or investors? Who are they (from filings: ownership splits, investor types, minimums), what exactly are they buying (the risk profile, the record in bad years, the scale, the institutional durability), why do they accept the terms, and what is the counter-case with numbers from both sides?
4. What does the non-core side look like: how big is it in absolute terms and as a share of the firm, how does it compare with peers per unit of size, how is it organised (reproduce the firm's own leadership groupings), and how is it wired to the front line (embedded roles, firm-wide utilities, connective roles), with the quotations from postings that prove it?
Then write the answer to "why {{FIRM}}" in three lengths: thirty seconds, two minutes, and a close naming one specific thing the candidate wants to work on. Add a table of what most candidates will say versus what this candidate can say, and an honest counter-case list.

# WORKSTREAM 9: THE SCENARIO PLAYBOOK

Build the frame-holding method and the scenarios:
- A four-step protocol for answering any scenario (steady, sort, act, close) with the exact phrases that execute each step and the timing (45 to 75 seconds).
- The priority order for when good things collide in this role (typically: rules and the firm's name; fair service to every internal client; the process and the record; speed), with the one sentence that holds every frame.
- Eight ways interviewers break a frame (interruption, flat contradiction, silence, escalation, authority squeeze, false choice, knowledge trap, invitation to badmouth) and the counter to each.
- How to stay calm physically.
- Three scenarios for every duty line in the JD, easy to hard. Each card: the setup, the trap, what to say, why it works (with sources), and the twist the interviewer will add and how to hold.
- A composure set of five hard scenarios specific to the role (two senior people shouting over the same scarce resource; a senior person asking you to skip a control; hearing something in a meeting that might be confidential or inside information; a mistake you made; acting on incomplete information against a deadline), each with a decision tree the candidate can draw from memory.
- The CV grill: how a three-levels-deep attack works, eight attacks with frame-holding answers, and a four-line preparation drill for every CV bullet.
- A one-page cheat sheet: protocol, priority order, the never list, the counters, lines to have ready, numbers if asked, one question to ask.

# THE DELIVERABLE: ONE REPORT

Output one file: `{{FIRM}}_{{ROLE}}_Complete_Interview_Pack.pdf`, with its `.html` source alongside, plus `Question_Bank.md`, `Reading_List.md` and `Cheat_Sheet.pdf` (the cheat sheet is also the report's penultimate part). Do not split the substance across separate documents.

DESIGN. The reader is a visual learner. A defined palette (deep navy, a warm accent, one signal colour for opinion callouts, generous white space), section colour bands, a cover, a contents page with real page numbers, running headers and footers. Callout boxes: KEY TERM, SAY THIS IN THE INTERVIEW, DON'T SAY THIS, YOUR OPINION GOES HERE, SOURCE UNCERTAIN. Scenario cards colour-coded easy, medium, hard. At least 30 inline-SVG diagrams, including:
1. Money or value flow through the business, full page.
2. The firm's operating model as layers (front line, centre, capital or customers) and what flows between them.
3. The unit or team model versus the alternative model, side by side.
4. Anatomy of one front-line unit and what it draws from the centre.
5. Growth of the firm over time: staff, units, size.
6. Why the structure works (for platforms: the diversification multiple against correlation; adapt).
7. The boundary between units: what is shared, what is never shared, why.
8. The competitive spectrum: design axes and where each rival sits.
9. Size against staffing for the firm and peers.
10. The customer's or investor's view: the record against alternatives.
11. The capital or revenue stability timeline.
12. The centre's org map as the firm publishes it.
13. How a front-line unit is wired into the centre: embedded, connective, utility roles.
14. What the firm is hiring for: open roles by department and city.
15. The role's value chain from internal demand to outcome.
16. The two (or more) channels through which the role's work is done.
17. A worked day in the seat.
18. The reconstructed team org chart, colour-coded by confidence.
19. The hub diagram: why a central function exists (the tangle without it, the wheel with it).
20. The life of a request through the function.
21. The scarce-resource collision and how it is allocated.
22. The walls around the function and what crosses each.
23. The regulation timeline for the role's sub-industry.
24. The industry shift map.
25. The interview process funnel with the candidate's position marked.
26. The four-step answer protocol.
27. The priority order for collisions.
28. Eight frame-breaking tactics and counters.
29. The scenario ladder: every JD bullet, three rungs.
30. Two decision trees for the composure set.
31. "Why the firm" on one page.
32. The cheat sheet on one page.
33. The master diagram: firm model, industry, role, all connected.

STRUCTURE OF THE REPORT:
- Part 0: How to use this pack, and the 10-minute emergency version
- Part 1: The role, decoded line by line, and the team mapped
- Part 2: The firm as a business, from the inside (founding insight, the contracts, the risk architecture, the centre)
- Part 3: Why the firm is built this way: structure, collaboration, what customers buy, the non-core side
- Part 4: How the firm stands out, and what only it can claim
- Part 5: The industry from zero
- Part 6: The role's own industry and its regulation
- Part 7: What is happening right now
- Part 8: Forming your own view: both sides of every argument
- Part 9: The interview: process, question bank, questions to ask
- Part 10: Interviewer briefing
- Part 11: The scenario playbook: frame method, ladder, composure set, CV grill
- Part 12: "Why {{FIRM}}" in three lengths, and the counter-case
- Part 13: Cheat sheet
- Part 14: Glossary (60+ terms)
- Part 15: Source table, every [Sxx]
- Part 16: Gaps and open questions

# FINAL SELF-CHECK (state each explicitly)

- Every figure has a source and date; estimates are labelled as estimates on the chart.
- A total beginner could read Parts 1, 2 and 5 without another source.
- The "why {{FIRM}}" material is mechanism, not adjectives, and could not be transplanted to a rival without changing the words.
- The regulatory section for the role is current and dated correctly.
- The team section goes materially beyond the JD, with method shown and thin evidence admitted.
- Every JD bullet has three scenarios, and the composure set has decision trees.
- People sections contain only public professional information with identity uncertainty flagged.
- The PDF rendered, the contents page numbers are correct, and every figure was checked for clipping.
- What could not be found is listed.

Then print a short summary of the files created and the three things the candidate should read first, given how soon the interview is.
