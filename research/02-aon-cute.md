# 02 — Aon / cut-e — Raw Research Notes

**Researched:** 2026-08-01 (main thread, direct). Confidence tags per §3.3.
**Coverage:** 5.1✅ 5.2✅ 5.3✅ 5.4✅ 5.5🟡 5.6✅ 5.7✅ 5.8✅ 5.9🟡 5.10✅ 5.11✅ 5.12✅ 5.13✅

> **Cross-provider note:** **ADEPT-15 is Aon's own personality product** (developed by Aon/cut-e lineage). SHL "ADEPT-15 where licensed" in the scope refers to a licence, not ownership — correct the SHL chapter accordingly.

---

## Ownership / platform (5.1)
- **cut-e** (German assessment firm, founded 2002) **acquired by Aon 2017**; now **Aon Assessment Solutions**. Product line rebranded "Aon's Assessment" but legacy "cut-e" naming persists in candidate communities. [PREP-VENDOR consistent; corporate fact]
- Platform: **Aon Assessment platform** (formerly "mapTQ" / cut-e portal). [PREP-VENDOR: passpsychometric mentions "map-tq"]

## The signature design (5.1 / 5.2 / 5.6)
- **Extreme time pressure by design** — many tests have more tasks than anyone can finish; "solve as many as you can" formats. The **time constraint is the primary differentiator**, not content difficulty. [PREP-VENDOR strongly consistent across graduatesfirst, testsolve, mconsulting]
- **Short, single-construct modules** — a battery of 5–12 min tests rather than one long test. [PREP-VENDOR consistent]
- **Unique per-candidate item bank** — each test generated from a large pool at launch (except personality & SJT), so candidates get different items → anti-cheating baked into design. [PREP-VENDOR: multiple agreeing]

## Mechanics — scales aptitude (5.4) [source: graduatesfirst, careertestprep — PREP-VENDOR, cross-checked, generally consistent]
| Test | Code | Time | Tasks | Measures | Adaptive? |
|---|---|---|---|---|---|
| Numerical reasoning | scales nmg / lst-num | 12 min | ~**37** | data interpretation, tables/figures, True/False/Cannot-Say | No (fixed pool) |
| Verbal reasoning | scales sxs | 12 min | ~**49** (~14s/item) | text inference, T/F/Cannot-Say, passage-only | No |
| Inductive-logical | scales cls | 12 min | ~12 | rule ID across 6 tables → apply to 4 more | No |
| Inductive (odd-one-out) | scales ix | 5–6 min | up to 20 | which of 9 shapes breaks the rule | No |
| Inductive (grid-pair) | scales clx | 6 min | unlimited | 2 grids share rule; find matching 2 of 4; no return | No |
| Deductive-logical | scales lst | 6 min | unlimited | 4×4 grid → larger; find missing symbol; blank tiles to test | **Yes** (grid grows) |
| Basic numeracy | scales eql | 5 min | unlimited | mental arithmetic | No |
| Concentration/attention | scales e3+ | 2 min | many | sustained attention/error-detection speed | No |
- Note earlier search gave cls=12 tasks/12min, ix=20/5min — consistent with above. Question counts vary slightly by source; treat as **~figures**, label [CANDIDATE/PREP-VENDOR].

## Mechanics — smartPredict games (5.4) [graduatesfirst — PREP-VENDOR]
- **switchChallenge** — 6 min, unlimited tasks; deductive logic/attention/resilience; identify operator transforming symbol sequence ("funnel logic"); operators increase → harder. 
- **gridChallenge** — 9 min, 9 rounds; spatial + working memory; memorise dot position → intervening symmetry/rotation checks → recall.
- **digitChallenge** — 5 min, unlimited; numeracy; fill missing numbers/operators to reach given answer; escalates.
- **motionChallenge** — 6 min, unlimited; planning/complex problem-solving; slide obstructing blocks so ball reaches exit (Rush-Hour-like); harder over time.
- (Short-term memory test — 5 min, 10 tasks, 8s exposure, 7s breaks, no pause.)
- Games capture **"over a thousand behavioural data points"** (reaction time, learning rate, error recovery, effort under pressure). [PREP-VENDOR/VENDOR-marketing]

## Personality / SJT / video (5.4)
- **ADEPT-15** — Aon's personality: ~100 items, slider paired-statement, up to ~30 min (usually untimed), 5 dimensions (with 15 facets); can't leave a slider unmoved; no back-navigation across pages. [PREP-VENDOR] — **Aon-owned.**
- Legacy cut-e personality: **"views"** (work values) and **"shapes"** (personality); scope's "vluu/views" = these. [INFERRED — confirm in gap audit]
- **chatAssess** — 20-min chat-style SJT/job-sim; scenario messages arrive live; competency + values scored. [PREP-VENDOR]
- **vidAssess-AI** — async video, 600+ question pool, **AI NLP scoring** across competencies. [PREP-VENDOR/VENDOR] — verify current facial-analysis stance in gap audit.

## Scoring / norms / cut-offs (5.6)
- **Percentile vs norm group** (typically recent graduates or role-specific). Adaptive tests (lst, and smartPredict) give stable percentile estimates. [PREP-VENDOR]
- Aptitude scored on **accuracy**, with timed performance contributing; SJT → percentile band; personality → dimensional, no pass/fail. [PREP-VENDOR]
- **Cut-off estimates [PREP-VENDOR ESTIMATE, not Aon-confirmed]:** standard roles 50th–75th; competitive grad 70th–80th. SJT "good" ~70th–80th. Present as range, label.
- **Speed vs accuracy:** because many sections are "do as many as you can", *unanswered ≈ not attempted*; the score is items-correct within time → **attempt rate matters**. [INFERRED from design] Negative marking not indicated. Confirm per test.
- Norm group = graduates / firm applicant pool depending on employer config. [PREP-VENDOR]

## Integrity (5.8)
- **Unique item bank per candidate** is the primary anti-cheat. [PREP-VENDOR consistent]
- **Webcam proctoring offered but NOT default**; most Aon deployments unproctored. [PREP-VENDOR: careertestprep/psychometric-success]
- No prominent "verification test" like SHL's, BUT extreme time limits + item randomisation reduce collusion value. [INFERRED]
- Less documented on tab-switch/clipboard telemetry than SHL — **gap**, flag [UNKNOWN] and note in gap audit.

## Role tailoring (5.5)
- Employer selects which modules + norm group + (for SJT/chatAssess) company-values keying. Core instruments standardised. [INFERRED from VENDOR structure]

## Employer mapping — finance (5.3 / 6.8)
- **Deutsche Bank** — confirmed cut-e user (scales numerical, verbal + motive.q). [PREP-VENDOR, repeated]
- **BNP Paribas** — listed Aon user. [PREP-VENDOR]
- Others (non-finance but shows breadth): P&G, Deloitte, Siemens, Airbus, Amazon, Lufthansa, Lidl/Aldi, IBM, Vodafone, Shell, Arup. [PREP-VENDOR]
- **Volatility flag:** provider choice changes year-to-year; re-verify in §6.8.

## Adjustments / legal (5.10/5.11)
- Aon offers adjustments via employer; extra time possible. [INFERRED — fetch Aon accessibility page in gap audit]

## SOURCES (5.13) — access 2026-08-01
- GraduatesFirst Aon/cut-e guide (PREP-VENDOR, UK, detailed): https://www.graduatesfirst.com/aon-cut-e-practice-assessments
- CareerTestPrep cut-e (PREP-VENDOR): https://www.careertestprep.com/knowledge/cut-e-tests
- JobTestPrep smartPredict (PREP-VENDOR): https://www.jobtestprep.co.uk/aon-smartpredict-challenges-practice
- AssessmentDay Aon (PREP-VENDOR): https://www.assessmentday.com/aon.htm
- TestSolve Aon (PREP-VENDOR): https://www.testsolve.ai/tests/aon/
- GBA Workshop smartPredict vendor deck (INDEPENDENT-ish, 2019): https://gbaworkshop.tntlab.org/wp-content/uploads/2019/08/Vendor-5-Siemsen.pdf ← FETCH in gap audit for trait model
- passpsychometric map-tq (PREP-VENDOR): https://passpsychometric.com/cut-e-psychometric-tests/

## RESIDUAL GAPS
- Aon official product pages (assessment.aon.com) — fetch for VENDOR-primary mechanics & validity.
- cut-e technical/validity documentation & any bias audit.
- Confirm "views"/"shapes" vs vluu naming.
- Integrity telemetry specifics (tab-switch/clipboard) — poorly documented.
- vidAssess-AI current facial-analysis stance.
- First-person UK candidate testimony (Deutsche Bank/BNP) with real timings.
