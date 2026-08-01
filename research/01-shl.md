# 01 — SHL — Raw Research Notes

**Researched:** 2026-08-01 (main thread, direct). **Confidence tags** per §3.3.
**Subsection coverage:** 5.1✅ 5.2✅ 5.3✅ 5.4✅ 5.5✅ 5.6✅ 5.7✅ 5.8✅ 5.9✅ 5.10✅ 5.11✅ 5.12✅ 5.13✅ (all have ≥ some sourcing; gaps flagged inline as [UNKNOWN]).

> **Analyst caution flag (applies throughout):** Most open web sources on SHL are prep-vendors (JobTestPrep, CareerTestPrep, PrepTerminal, PrepClubs, AssessmentDay, GraduatesFirst) — commercially biased toward "you need our practice." They frequently (a) state confidential cut-scores as if fact, and (b) **conflate SHL's unproctored Verify G+ with webcam-proctored delivery**. The classic Verify model is *unsupervised test + supervised verification test*; webcam/screen-capture is a separate optional layer many employers do NOT switch on for graduate Verify. Corroborate any integrity claim against this distinction.

---

## Ownership / corporate (5.1)
- SHL = one of the oldest occupational-psychometrics firms (Saville & Holdsworth Ltd, UK-founded 1977). Owned by **The Heritage Group / Exponent** (PE) through recent years; previously part of CEB (CEB acquired SHL 2012; Gartner acquired CEB 2017; SHL divested to Exponent 2018). [VENDOR/INDEPENDENT — corporate history, verify exact current owner in gap audit]
- Platform: **SHL TalentCentral** (delivery + reporting). [VENDOR] shl.com

## Product family (5.1 / 5.4)
- **Verify G+ / Verify Interactive G+** — general mental ability (GMA). [VENDOR] shl.com/products/assessments/cognitive-assessments/
- **Verify Interactive** subtests: Numerical, Inductive, Deductive (Verbal exists in legacy range). [VENDOR]
- **OPQ32** — Occupational Personality Questionnaire, 32 traits, forced-choice (OPQ32i / OPQ32r). [VENDOR]
- **MQ** — Motivation Questionnaire. [VENDOR — needs its own fetch in gap audit]
- **ADEPT-15** — personality (SHL-licensed, 15 facets). [VENDOR — needs fetch]
- **Smart Interview On Demand** (async video), **Smart Interview Live** (live), **Smart Interview Live Coding** (compiler). [VENDOR] shl.com/products/video-interviews/
- **RemoteWorkQ / Workplace** assessments. [mentioned in scope — verify]

## Mechanics — Verify G+ / Interactive (5.4)
- **Verify Interactive G+**: 24 questions, 36-minute total cap; adaptive — correct answers → harder, higher-value items; produces Deductive + Inductive + Numerical sub-abilities. [CANDIDATE/PREP-VENDOR, multiple agreeing: prepterminal, aptitudetests.org, practiceaptitudetests] — figure of **24 Q / 36 min** appears consistently.
- **Legacy Verify G+** (button-click, pre-Interactive): **30 questions / 36 min**, split ~10 numerical / 10 inductive / 10 deductive. [PREP-VENDOR, multiple agreeing: assessmentday, aptitudeace] — this is the *older* fixed-ish form; note current vs legacy.
- Time is **whole-test**, not per-section. [PREP-VENDOR, consistent]
- **Randomised item bank** — each candidate draws different items so no two tests identical; even spread of correct answers across A–E. [VENDOR/INDEPENDENT — SHL Verify Technical Manual v2.0 Oct 2007, hrmforce.com/wp-content/uploads/2021/03/Verify-Technical-Manual.pdf — PDF is graphics-encoded, did not text-extract; figures below from search-index of it]
- Delivery: "automated, remotely proctored"; uses drag-and-drop / gamified interactions in Interactive range. [VENDOR] cognitive-assessments page
- Partial-scoring methodology mentioned. [VENDOR]

## VERIFIED PRIMARY FIGURES — from SHL Verify Technical Manual (extracted via pdftotext, 2026-08-01) [VENDOR-manual, primary]
- **Reliability (internal consistency) of Verify Ability Tests: 0.77 to 0.84.** (manual p.15 area)
- Score reporting: theta → **T-scores (mean 50, SD 10)** and **Sten (mean 5.5, SD 2)**; percentiles are ordinal ("should not be averaged"). SEM = √(1−rxx)·SD.
- **Verification model, quantified:** ability & verification tests **correlated 0.70 and above**; a "Confidence Indicator (CI)" flags aberrant (cheating-consistent) scores. Validated by **Monte Carlo simulations**: 10,000-candidate normal theta distribution, 100 IRT-built tests, cheating modelled as **+2 SD** score inflation (proxy/collusion), assumed **−0.3 correlation between ability and propensity to cheat** (Cizek 1999). A "benefits ratio" quantifies detection at cut-scores (e.g. 30th vs 70th pct).
- Manual explicitly frames "Not Verified" as needing investigation (distractions, didn't attempt all items, physical/psychological factors, whether they used shldirect.com practice) — NOT auto-guilt. [VENDOR-manual]
- Manual cites **Schmidt & Hunter** for GMA as predictor of job performance; construct validity via Bartram (2005). 
- Telling candidates upfront that honesty is expected + verification will be used **reduces cheating incidence**. [VENDOR-manual]
- Extracted text saved: research/_shl_manual.txt (112k chars).

## Psychometrics (5.2 / 6.3)
- SHL Verify Technical Manual v2.0 (Oct 2007) — uses **both CTT and IRT**; reliability ~**0.80** cited ("80% of variance = true measurement"). [VENDOR-manual via search index] hrmforce PDF.
- **70 comparison groups** (test type × job level × industry) in the Verify range. [VENDOR-manual]
- Extensive global validation DB, meta-analytic criterion validity. [VENDOR] — cross-check independent GMA validity (Schmidt & Hunter; the 2022 Sackett et al. re-analysis that revised GMA validity *downward* from ~0.51 to ~0.31 corrected) in cross-cutting §6.3.

## Scoring / norms / cut-offs (5.6)
- **Norm-referenced percentile** vs a chosen **norm group**; employer picks the norm group at purchase. [VENDOR + PREP-VENDOR consistent]
- Grade bands A–D (A ≈ top ~15%, D ≈ bottom quartile) and **sten** scores (sten 7 ≈ 77th pct, sten 8 ≈ 89th pct). [PREP-VENDOR: careertestprep]
- Norm groups named: Graduate (UK/Global), **Finance Graduates**, Professional/Managerial, IT Professionals, General Population, industry variants. [PREP-VENDOR: careertestprep — plausible, matches SHL's 70-group structure]
- **Employer cut-score estimates — ALL PREP-VENDOR, SELF-DISCLAIMED AS ESTIMATES, NOT SHL-CONFIRMED. Treat as [CANDIDATE/PREP-VENDOR ESTIMATE].** Two sources disagree, so present as a *range*:
  - Bulge-bracket IB (GS/MS/JPM/Barclays): **~75th–90th percentile** (careertestprep says GS/MS 80–85th, JPM/Barclays 75–80th; another prep source said IB 80–90th). Finance-graduate norm group.
  - Big Four: ~60th–75th. Consulting streams: ~75th–85th.
  - **Do NOT present any single number as fact.** SHL does not publish employer cut-scores; sources explicitly disclaim ("cut scores vary by year and applicant pool size").
- Sift shape: usually a **fixed cut-score OR rank sift** interpreted by recruiter; SHL outputs percentile + band, recruiter/employer sets threshold. [INFERRED from norm-referenced design + VENDOR]

## Retake policy (5.6)
- **Employer-set, not SHL-set.** Many enforce no-retake within a cycle; cooling-off typically **6–12 months**. [PREP-VENDOR: careertestprep retake page; consistent]
- Scores generally NOT shared across employers (each employer's instance separate) — but the *verification* concept means a supervised re-test can be demanded. [INFERRED]

## Verification test — KEY integrity mechanism (5.8)
- Model: unsupervised online test → optional **supervised verification test** (shorter, same format/difficulty, *different items*). [VENDOR-manual concept + PREP-VENDOR, strongly consistent]
- Output usually **"Verified" / "Not Verified"**, not a score. Uses a **Confidence Indicator (CI)**: compares the two scores; if the gap is statistically improbable → "Not Verified". [VENDOR-manual language via search: "Confidence Indicator", "consistent with the score they achieved"]
- "Not Verified" can be innocent (candidate's physical/psychological state on the day). [VENDOR-manual]
- Consequence: employer-dependent; large discrepancy → often disqualification at top IB / Civil Service. [PREP-VENDOR, plausible; label estimate]

## Other integrity signals (5.8) — WITH THE CAUTION FLAG
- TalentCentral logs **focus-loss / tab-switch** with timestamps; count visible to employer. [PREP-VENDOR: careertestprep, process page] — plausible & standard.
- **Copy-paste / clipboard** detection; screenshot / print-screen detection. [PREP-VENDOR]
- **Random screen captures**, **webcam face-detection** (absence, extra person, gaze) — **ONLY when the employer enables webcam proctoring / Smart proctoring; NOT default on unproctored Verify.** [PREP-VENDOR conflates; INFERRED correction]
- Statistical answer-pattern anomaly flags. [PREP-VENDOR]
- Recruiter sees an **integrity report** alongside scores; single accidental tab-switch treated holistically, patterns are the problem. [PREP-VENDOR: careertestprep — reasonable]

## Personality — OPQ32 / faking (5.7 / 6.4)
- **OPQ32i**: forced-choice, choose most/least like you from blocks of 4; ~**104 forced-choice items** → 32 traits. Ipsative-style, designed to reduce social-desirability distortion. [PREP-VENDOR multiple agreeing: careertestprep/opq32, jobtestprep, graduatesfirst]
- **OPQ32n** (normative) includes a **Social Desirability scale** flagging faking. [PREP-VENDOR]
- BPS review of OPQ32 exists: hrmforce.com/.../OPQ32-BPS-Review-2007.pdf [INDEPENDENT — fetch in gap audit for reliability/validity of OPQ].
- Smart Interview On Demand: optional AI scoring of "spoken content, facial expressions, voice tonality, body language". [VENDOR] — **facial/body-language scoring is contentious; verify SHL's CURRENT stance in gap audit (post-HireVue 2021 climbdown on facial analysis).**

## Role tailoring (5.5)
- Same core instrument ships to all; employer configures **norm group** and (for SJT/behavioural) competency weightings; bespoke criterion-validation studies exist for big clients but not standard. [INFERRED from VENDOR structure — 70 comparison groups implies configuration not rebuild]

## Reasonable adjustments / legal (5.10 / 5.11 / 6.7)
- SHL has a **Disability Guidelines (UK)** page + FAQs and **Accessibility Support** on SHLDirect. [VENDOR] shl.com/legal/disability-guidelines-uk/faqs/ ; www2.shl.com/shldirect/en/assessment-advice/accessibility-support
- Adjustments incl. **extra time** (dyslexia/motor), presentation changes (dyslexia/visual). Declare **in advance**. [VENDOR]
- Standard extra-time norm elsewhere is 25%–50% (not SHL-specific figure). [INDEPENDENT context]

## Employer mapping — UK finance (5.3 / 6.8)
- SHL reportedly used by **Goldman Sachs, Barclays, Deutsche Bank, HSBC, UBS, JPM, RBC** + "most asset managers" / bulge brackets. [PREP-VENDOR + TSR — MIXED reliability; some employers have since MOVED to game-based (e.g., JPM→Pymetrics historically). MUST re-verify per employer & per year in §6.8. Providers change year-to-year.]
- **Citi → Korn Ferry Talent Q**, not SHL. [PREP-VENDOR] — shows mapping volatility.
- TSR thread (2013-era) "IB aptitude tests SHL Kenexa" — dated; use only for historical context. thestudentroom.co.uk/showthread.php?t=2458882

## KEY SOURCES (5.13) — with access date 2026-08-01
- SHL cognitive assessments (VENDOR): http://www.shl.com/products/assessments/cognitive-assessments/
- SHL Verify Interactive G+ product (VENDOR, redirects): shl.com/products/product-catalog/view/shl-verify-interactive-g/
- SHL Smart Interview On Demand (VENDOR): https://www.shl.com/products/video-interviews/smart-interview-on-demand/
- SHL Smart Interview OnDemand User Guide PDF (VENDOR primary): https://talentcentral.learning.shl.com/pluginfile.php/488/mod_resource/content/16/Smart%20Interview%20OnDemand%20User%20Guide%20V1%20Jan%202023.pdf  ← FETCH in gap audit
- SHL Verify Technical Manual v2.0 2007 (VENDOR-manual): https://hrmforce.com/wp-content/uploads/2021/03/Verify-Technical-Manual.pdf (graphics-encoded; needs OCR/alt)
- OPQ32 BPS Review 2007 (INDEPENDENT): https://hrmforce.com/wp-content/uploads/2021/03/OPQ32-BPS-Review-2007.pdf  ← FETCH
- SHL Disability Guidelines UK FAQ (VENDOR): https://www.shl.com/legal/disability-guidelines-uk/faqs/
- CareerTestPrep — good-SHL-score (PREP-VENDOR, self-disclaims estimates): https://www.careertestprep.com/knowledge/what-is-a-good-shl-score
- CareerTestPrep — SHL cheating (PREP-VENDOR): https://www.careertestprep.com/knowledge/shl-cheating
- CareerTestPrep — retake policy (PREP-VENDOR): https://www.careertestprep.com/knowledge/shl-retake-policy
- Recent Grads — UK IB aptitude tests guide 2025 (returned HTTP 500; retry): https://recentgrads.co.uk/2025/07/28/investment-banking-aptitude-tests-the-complete-guide-for-uk-candidates/

## RESIDUAL GAPS for SHL (for Phase 4)
- Exact CURRENT owner of SHL (Exponent vs successor). 
- MQ, ADEPT-15, RemoteWorkQ specifics.
- SHL's current documented stance on facial/emotion analysis in Smart Interview.
- Primary confirmation (non-prep-vendor) of tab-switch/clipboard logging in TalentCentral.
- Reddit/TSR first-person testimony with real timings (direct fetch needed; search operator failed).
- Any SHL bias-audit / adverse-impact publication; NYC LL144 posting.
