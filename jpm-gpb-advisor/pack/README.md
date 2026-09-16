# Complete interview pack (master template run)

Built 11 September 2026 from the master prompt template for JPMorgan Chase / J.P. Morgan Global Private Bank, 2027 Advisor Summer Internship Program, London (req 210773470).

## Deliverables
- `JPMorgan_GPB_Advisor_Internship_Complete_Interview_Pack.pdf` (107 pages, 43 inline SVG figures, 16 parts, 376-row source table) and its `.html` source.
- `Cheat_Sheet.pdf` (one page).
- `Question_Bank.md` (45 questions with tests, structure, facts and traps, plus ten questions to ask).
- `Reading_List.md` (20 recurring sources with a seven-week plan).

## How it was built
- Nine research workstreams with their own source-ID ranges: WS1 (S1-S39) the posting and firm pages; WS1B (S40-S69) the team map from 17 live requisitions and leadership pages; WS2 (S70-S119) the firm as a business, entities, skeletons; WS4B (S120-S149) regulation and tax; WS3 (S150-S189) competitors; WS4 (S190-S219) industry; WS5 (S220-S259) six-month news sweep; WS6 (S260-S299) interview process; WS8 (S300-S339) filings, letters, Investor Days; S340+ miscellaneous and overflow.
- `sources_base.py` and `sources_extra.py` hold the registry; `build_pack.py` assembles `parts/*.html`, injects figures from `figs_def.py` and `figs_def2.py` (drawn with `svg.py`, `diagrams.py`, `diagrams2.py`, `charts.py`), rewrites `[Sxx]` markers to superscripts, and renders twice with headless Chromium (`topdf_pack.js`) so the contents page carries real page numbers.
- Rebuild: `python3 build_pack.py` inside `pack/`.

## Inputs assumed
No interview date, interviewer names, coordinator or insider intelligence were supplied; Part 0 of the pack states the assumptions. The stage is application and HireVue pending; the deadline is 1 November 2026 (rolling).

## Commercial awareness brief: evergreen private credit (added 16 September 2026)

- `Evergreen_Private_Credit_Brief.pdf` (15 pages, 11 of content plus sources): what evergreen / semi-liquid funds are from zero, the 5% rule, the Sept 2025 to Sept 2026 timeline, cases on Blue Owl, Partners Group and Blackstone, regulator and J.P. Morgan positions, the FT reading list, 71 sources, and the HireVue answer with timings and screen notes. Built by `evergreen.html.py` (diagrams in `diagrams3.py`, renderer `topdf_short.js`).
- `HireVue_Evergreen_Answer.md`: the script on its own for editing and rehearsal.
- Research notes: `../research/07_evergreen_mechanics_and_stress.md`, `08_partners_group_blue_owl_jpm.md`, `09_blackstone_and_landscape.md`.
