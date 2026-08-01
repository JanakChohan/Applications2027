# 00 — Master Plan & Progress Tracker

**Project:** The Definitive UK Finance Early-Careers Online Assessment Guide
**Branch:** `claude/uk-finance-assessment-guide-b9y99i`
**Started:** 2026-08-01
**Deliverable:** `output/ultimate-online-assessment-guide.pdf` (+ markdown source + raw research)

---

## Tooling confirmed (Phase 1)

| Tool | Status | Notes |
|---|---|---|
| WebSearch | ✅ Working | **US-routed** — surfaces UK sources (assessmentday.co.uk etc.) but ranking is US-biased. Mitigate with `site:` and `.co.uk`/`site:thestudentroom.co.uk` targeted queries. |
| WebFetch | ✅ Working | Fetches full pages incl. UK pages & PDFs. Cross-host redirects returned, not followed. Cannot access auth-gated pages (Glassdoor/Blind/WSO paywalls may partial-fail). |
| GitHub MCP | ✅ Available | For commit/push only; not a research source. |
| PDF skill | To confirm in Phase 6 | Check `/mnt/skills/public/pdf/SKILL.md`. |

**Known limitations to state in the output:**
- WSO, Glassdoor, Blind, Fishbowl often auth-gate content → candidate testimony from these may be thin; corroborate via Reddit/TSR which are open.
- Vendor technical manuals are increasingly gated behind sales contact forms → some psychometric detail will be `[UNKNOWN]` with reasoned proxy.
- WebSearch US routing weakens UK-forum surfacing → compensate with direct `site:` queries and direct fetches.

---

## Providers (Section 2) — chapter checklist

Each provider needs all of 5.1–5.13. Legend: ⬜ not started · 🟡 researching · 🟩 research done · ✍️ drafted · ✅ in PDF

| # | Provider | Research | Draft |
|---|---|---|---|
| 01 | SHL | 🟩 | ✍️ (sample chapter drafted for checkpoint) |
| 02 | Aon / cut-e | 🟩 | ⬜ |
| 03 | Arctic Shores | ⬜ | ⬜ |
| 04 | Pymetrics (Harver) | ⬜ | ⬜ |
| 05 | Cappfinity | ⬜ | ⬜ |
| 06 | Amberjack | ⬜ | ⬜ |
| 07 | Plum | ⬜ | ⬜ |
| 08 | HireVue | ⬜ | ⬜ |
| 09 | Willo | ⬜ | ⬜ |
| 10 | TestGorilla | ⬜ | ⬜ |
| 11 | Morgan Stanley (firm-built) | ⬜ | ⬜ |
| 12 | Other firm-built (rolling capture) | ⬜ | ⬜ |

### Per-provider subsection grid (mark ✅ / [UNKNOWN] as filled)
For every provider row above, track: 5.1 Snapshot · 5.2 Why exists · 5.3 Why this vendor · 5.4 Mechanics · 5.5 Role-tailoring · 5.6 Scoring/norms/cut-offs · 5.7 How to score well · 5.8 Integrity detection · 5.9 How candidates trip it (incl. false positives) · 5.10 Being unambiguously clean · 5.11 If flagged/rejected (+templates) · 5.12 Step-by-step playbook · 5.13 Sources.

(Detailed tick-grid maintained per-file at top of each `research/NN-*.md`.)

---

## Cross-cutting chapters (Section 6) checklist

| Ref | Chapter | Status |
|---|---|---|
| 6.1 | Why online assessments exist | ⬜ |
| 6.2 | Vendor landscape & procurement | ⬜ |
| 6.3 | Psychometrics for candidates | ⬜ |
| 6.4 | Construct-by-construct performance manual | ⬜ |
| 6.5 | 6-week preparation programme | ⬜ |
| 6.6 | Integrity monitoring cross-provider taxonomy | ⬜ |
| 6.7 | Legal rights & regulatory picture (UK/EU) | ⬜ |
| 6.8 | Employer → provider mapping (by programme type) | ⬜ |
| 6.9 | Quick-reference appendices | ⬜ |

### Prompt-specific additions to honour
- **§3.1 Tier 5:** add UK-specific communities — WSO London/UK forums, r/FinancialCareers UK threads, r/UKPersonalFinance-adjacent careers, **The Student Room IB & Finance forums**, UK finance LinkedIn/Instagram creators, university IB/finance society shared docs.
- **§6.8:** table split by **programme type** (spring week / summer / off-cycle / grad). Establish where **off-cycle skips/compresses the OA** vs summer — this changes which assessments matter.
- **New §5.6 subsection (per firm):** distinguish **OA sift vs CV/cover-letter sift vs HireVue** — locate where the *largest cut* actually happens in the funnel. Thesis to test: in UK IB the OA is often NOT the tightest hurdle.
- **Rolling deadlines as first-class variable** throughout 5.6: does the sift threshold move as slots fill; practical timing implication.

---

## Target employers to anchor the mapping (UK London/EMEA)
Bulge brackets: Goldman Sachs, Morgan Stanley, JPMorgan, BofA, Citi, Barclays, UBS, Deutsche Bank, HSBC.
Elite boutiques: Evercore, Centerview, PJT, Lazard, Moelis, Rothschild, Perella Weinberg, Greenhill/Houlihan Lokey, Robey Warshaw.
Mid-market: Jefferies, RBC, Nomura, BNP Paribas, SocGen, Macquarie, Numis/Deutsche Numis, Peel Hunt.
Asset managers: BlackRock, Fidelity, Schroders, M&G, Legal & General IM, abrdn, Baillie Gifford, Wellington, PIMCO, Invesco, JPMAM.
Buy-side / hedge / private markets: Bridgewater, Citadel, Point72, Millennium, Man Group, Marshall Wace, Brevan Howard, Blackstone, Apollo, KKR, Carlyle, CVC, EQT.

---

## Phase roadmap & status

- [x] **Phase 1 — Scoping.** Dirs created, tools confirmed, plan written. → *Awaiting user OK on plan.*
- [ ] **Phase 2 — Provider research.** One file per provider. **CHECKPOINT after SHL + Aon/cut-e:** show sample chapter, confirm depth/format before continuing the other 10.
- [ ] **Phase 3 — Cross-cutting research.**
- [ ] **Phase 4 — Gap audit.** Re-run ≥2 searches per unchecked item before conceding `[UNKNOWN]`.
- [ ] **Phase 5 — Drafting** into `output/chapters/`.
- [ ] **Phase 6 — Assembly + PDF** (check PDF skill first; verify render, TOC, page numbers, no clipped tables).

## Evidence discipline (applied everywhere)
Tags: `[VENDOR]` `[INDEPENDENT]` `[CANDIDATE]` (state # of agreeing reports) `[INFERRED]` (show reasoning) `[UNKNOWN]` (say why + proxy). No invented numbers. Conflicts shown both ways. Current vs legacy flagged. Quotes <15 words, one per source. No live test items.
