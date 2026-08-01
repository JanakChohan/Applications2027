# 10 — TestGorilla — Raw Research Notes

**Researched:** 2026-08-01 (agent thread, direct WebSearch + WebFetch). All URLs accessed 2026-08-01.
**Coverage:** 5.1✅ 5.2✅ 5.3✅ 5.4✅ 5.5✅ 5.6🟡 5.7🟡 5.8✅ 5.9✅ 5.10✅ 5.11✅ 5.12🟡 5.13✅

> **HEADLINE / HONESTY FLAG:** TestGorilla is a **self-serve SME/SMB/tech/scale-up** skills-testing platform, NOT a bulge-bracket front-office IB tool. Vendor's own finance page names **fintech/scale-up** clients (Revolut, Volt, Embrace, Tresl) and its finance tests are **accounting / back-office / compliance** (GAAP, IFRS, Xero, accounts receivable, Excel). **NO** evidence of front-office IB / trading / M&A / wealth graduate-scheme usage. A UK finance early-careers candidate is far more likely to meet SHL/Aon/HireVue/Amberjack at a bulge bracket; TestGorilla surfaces at **fintechs, challenger banks, mid-market, and non-finance grad employers**. Treat its relevance to this book as "adjacent / fintech tier," not core IB. [INDEPENDENT + VENDOR — see §5.11]

---

## 5.1 Ownership / corporate / what it is

- **Founded 2019** by **Wouter Durville (CEO)** and **Otto Verhage** (ex-Bain & Company partner). HQ **Amsterdam, Netherlands**. Private company. [INDEPENDENT — Tracxn/Crunchbase/PitchBook via search]
- **Funding:** ~**$81.2M** total across 3 rounds; headline **$70M Series A (2022)** led by Atomico, with Balderton Capital, Notion Capital. Balderton/UNLEASH press confirm the raise "to help companies eliminate hiring bias." [INDEPENDENT + VENDOR blog]
- Third-party estimates (getlatka, unverified): ~$36.2M ARR, ~$108.6M valuation. [INDEPENDENT — treat as ESTIMATE, low confidence]
- **What it is:** a **self-serve online skills-assessment SaaS**. Employers assemble a multi-test assessment from a library of **400+** (marketing) / **350+** (older copy) "scientifically validated" tests. Vendor positions it as a **"talent discovery platform"** (sourcing + screening + assessment). [VENDOR — testgorilla.com]
- Scale claim: **10,000+ customers**, "millions of candidates." Named non-finance clients: **Sony, PepsiCo, Bain & Company, Oracle, H&M, UK NHS.** [VENDOR — finance/blog pages]
- **Stage in funnel:** early screening / CV-replacement step, sent to applicants (often at top of funnel). **Duration:** an assessment = **up to 5 tests** (most ~10 min each) + custom questions → typically **~30–60 min total**. [VENDOR + PREP-VENDOR]

## 5.2 Why it exists

- Core pitch = **skills-based hiring replacing CV/résumé screening**, marketed as **bias-reducing** and **accessible to smaller employers** who can't afford enterprise SHL/Aon. [VENDOR — Series A messaging: "eliminate hiring bias"]
- Explicitly targets SMB/mid-market self-serve buyers: free tier + low-commitment annual subscription (vs enterprise sales motion of SHL/Aon). [INDEPENDENT — pricing sources §5.3]

## 5.3 Why a firm picks it / differentiators / pricing

**Differentiators [VENDOR + INDEPENDENT review sites]:**
- **Huge, broad test library** (400+): cognitive, personality, language, coding, software, role-specific, SJT — pick-and-mix.
- **Custom questions** (video/essay/file-upload/MCQ/coding) alongside library tests.
- **Price + ease + self-serve** — no enterprise contract needed; free forever tier.
- **Skills-based-hiring / anti-bias marketing** as the brand wedge.
- **Anti-cheating suite** marketed as a selling point (see §5.8).

**Pricing model — subscription + credits [INDEPENDENT — Capterra/spotsaas/xpay, 2026]:**
- **Free forever:** 5 tests, AI resume scoring, up to 5 custom questions/assessment, no ATS/video/coding, no full library.
- **Core:** ~**$1,700/yr** (~$135/mo billed annually), reported ~400 credits + 2 premium seats.
- **Plus:** custom pricing, from ~$400/mo — adds ATS integrations, more seats.
- **Annual commitment only** on paid plans; **credits don't roll over**. [INDEPENDENT — pricingnow/xpay; numbers vary by source → treat as ESTIMATE ranges]

**Reference clients:** Revolut (case study, "40% faster hiring"), Sony, PepsiCo, Bain, Oracle, H&M, NHS. [VENDOR]

## 5.4 FULL MECHANICS

**Assessment build [VENDOR help-center + PREP-VENDOR]:**
- An assessment = **max 5 tests** from the library + **10 or 20 custom questions** (plan-dependent; free tier = 5 custom questions).
- **Custom question types (5):** (1) pre-recorded **video** (webcam response to prompt), (2) **essay**, (3) **file upload** (CV/cover letter/take-home), (4) **multiple-choice**, (5) **coding**. [VENDOR help-center via search]

**Library categories & counts [VENDOR test-library page]:**
| Category | ~Count |
|---|---|
| Role-specific skills | 162 |
| Programming skills | 83 |
| Software skills | 59 |
| Language (CEFR-graded) | 37 |
| Cognitive ability | 17 |
| Situational judgement | 13 |
| Personality & culture | 6 |
| Typing speed | 4 |

**Cognitive-ability subtests [VENDOR cognitive-ability library page] — all Multiple choice, mostly ~10 min, FIXED (not adaptive):**
- Problem Solving 9 min; RCI (Rapid Cognitive Index) 10 min; Abstract Reasoning 10 min; Critical Thinking 12 min (advanced); Numerical Reasoning 10 min; Verbal Reasoning 10 min; Reading Comprehension 13 min; Attention to Detail (Textual) 12 min / (Visual) 10 min; Spatial Reasoning 10 min; Mechanical Reasoning 10 min; Intermediate/Basic Math variants 10 min; Computational Thinking 10 min; Understanding Instructions 10 min.
- **Per-question timing:** PREP-VENDOR give conflicting figures — prepclubs cites a "40 Q / 20 min" combined cognitive test (~30s/Q) and shorter modules (e.g. Numerical 20Q/10min); jobtestprep says "~1 minute per question on average." → **Treat per-Q timing as ~30s–60s depending on module; question counts not published by vendor.** [PREP-VENDOR, conflicting → label ESTIMATE]
- 4–5 practice questions typically shown before a timed test starts. [PREP-VENDOR — jobtestprep]

**Personality (6) [VENDOR personality library]:**
- **Big 5 (OCEAN)** — Five-Factor Model; self-report, rate statements 1 (very inaccurate) – 5 (very accurate); placed on each of 5 spectra. Self-report, "no right/wrong."
- **DISC** (Marston model: Dominance/Influence/Steadiness/Conscientiousness).
- **16 Personality Types** (Myers-Briggs-style / Enneagram-adjacent), **Culture Add**, Enneagram-alternative content.
- Vendor guidance: personality tests **should not be used alone** — combine with cognitive + role tests for a "holistic view." [VENDOR]

**Situational judgement (13):** leadership, communication, time management, ethics themes. [VENDOR library]
- **Adaptive?** Generally **NO** — fixed-form multiple-choice modules (contrast with SHL/Aon adaptive engines). [INFERRED from library format; vendor does not advertise IRT/adaptive]
- **Device:** browser-based; webcam used if proctoring on; coding tests in-browser IDE. [VENDOR/PREP-VENDOR]

## 5.5 Tailoring / benchmarking

- Employer **self-assembles** up to 5 tests + writes custom questions (or uses vendor's video-question library with "science-backed scoring rubrics" on paid tiers). [VENDOR]
- Employers **weight modules** by preference; candidates never see the weighting. [PREP-VENDOR — prepclubs]
- Benchmarking = candidates ranked **relative to each other** within the same assessment; each test also scored vs a norm/benchmark. [VENDOR + PREP-VENDOR — see §5.6]

## 5.6 SCORING / NORMS / CUT-OFFS

- Each test → **percentage score (0–100)**; prepclubs also cites a **percentile vs norm group** per module. [PREP-VENDOR — treat percentile claim as ESTIMATE; vendor public copy emphasises % + ranking, not published norms]
- **No formal pass/fail:** vendor states *"There's no 'pass' or 'fail'… It's about showcasing your abilities and how they align with the role."* Practically, employers **rank** candidates and shortlist top scorers — **de-facto cut-off is a rank/threshold the employer sets**, not a published one. [VENDOR blog]
- Recruiter **dashboard** shows per-test scores, an overall/ranked view of candidates, custom-question responses (video/essay/file) for manual review, and the **anti-cheating behaviour log** (§5.8). [PREP-VENDOR + VENDOR — dashboard specifics thin in public sources → 🟡]
- **Retakes: ONE attempt** — "You'll have one attempt to complete your assessment"; timer continues even if you disconnect. [VENDOR blog + PREP-VENDOR]
- Candidates are **not** given their own scores by default; employer may choose to share. [PREP-VENDOR — jobtestprep]
- **Cut-off numbers:** prepclubs floats entry ~60+, analyst/mid ~75+, "select Bain/Revolut ~80+" — **[PREP-VENDOR ESTIMATE, NOT vendor-confirmed]**, present only as illustrative.

## 5.7 How to prepare 🟡

- **Cognitive:** timed multiple-choice numerical/verbal/abstract — practise speed + accuracy; ~30–60s/Q; use the 4–5 warm-up questions. [PREP-VENDOR]
- **SJT:** research the employer's stated values; pick the "most effective + most in-character" response. [PREP-VENDOR]
- **Personality (Big 5/DISC/16-type):** answer consistently and honestly but aligned to role competencies; no back-navigation assumed. [PREP-VENDOR]
- **Role/software/coding tests:** genuine skill — brush up on the named tool (Excel, Xero, GAAP, language, the programming stack). [VENDOR library]
- Prep ecosystem exists (JobTestPrep, iPrep, prepclubs, easy-quizzz) — all **[PREP-VENDOR]**, commercial, question banks not official.

## 5.8 INTEGRITY / ANTI-CHEATING SUITE (a marketed selling point)

**Features [VENDOR help-center + VENDOR blog "cheating-detection-skills-assessments" + PREP-VENDOR, cross-confirmed]:**
- **Webcam snapshots** — image captured **every ~30 seconds** to verify identity; **optional, taken with candidate permission**; detects if camera disabled/off. Snapshots retained **6 months** (privacy policy). [VENDOR]
- **Full-screen exit detection** — flags leaving full-screen mode.
- **Tab-switch detection** — flags switching browser tabs (distinguishes one-off vs "15 switches in a 20-min test").
- **IP-address / approximate-location logging** — identifies multiple attempts / unauthorised access.
- **Screenshot detection** and **developer-tool detection**.
- **Copy-paste disabled/detected.**
- **Randomised question banks** + **question-retirement system** (items retired after exposure limit) + **large pools** → anti-memorisation.
- **Time limits** on tests to prevent extended research.
- **NOTE:** public sources do **NOT** confirm a dedicated **mouse-leave/focus-loss** telemetry as a distinct named feature (tab-switch + full-screen exit are the analogues) — [UNKNOWN, gap]. No prominent **AI-answer / plagiarism** detector named in the sources found (contrast newer rivals) — [UNKNOWN, gap; possible but unconfirmed].

**How flags surface + "behavior tiers" [VENDOR]:**
- Events logged with **timestamps** in a **candidate behaviour log** on the recruiter dashboard; grouped into **behaviour tiers** (help-center article "Understanding anti-cheating measures and behavior tiers" — URL returns 403 to bot, title/snippets confirm existence).
- Vendor philosophy explicitly **anti-"gotcha"**: *"we focus on cheating prevention and spotting outlier behaviors… instead of assuming every red flag is definitive proof."* Flags = "starting points for follow-up, not instant disqualifiers." Recommends employer **contacts candidate** for explanation. [VENDOR blog]
- **Candidate told?** Candidate consents to webcam (optional/permissioned); proctoring presence is disclosed at assessment start. Whether the candidate sees their own flags: **not** — flags go to employer. [VENDOR/PREP-VENDOR]

## 5.9 FALSE-POSITIVE risks

- Vendor itself acknowledges honest triggers: exiting full-screen to close a **system notification**, a quick tab-switch to check a permitted requirement, "life happens," slight delays, careful reading, accidental clicks. [VENDOR blog — unusually candid on this]
- **Honest-candidate risk:** webcam-off or poor lighting → identity flag; single tab-switch logged; disabled webcam if no camera. Because employer sets interpretation, a **less-sophisticated SME recruiter could over-read the log** despite vendor guidance. [INFERRED]
- **Disability risk:** ADHD/anxiety fidgeting, assistive tech, screen readers could increase full-screen/tab anomalies → mitigated by accommodations (§5.10) but only if candidate requests. [INFERRED]

## 5.10 Adjustments / accessibility

- **Accommodations [VENDOR help-center via search]:**
  - **Non-native language:** **+20% time.**
  - **Disability/condition** (e.g. ADHD, dyslexia, autism): **+50% time.**
  - **As of June 2026:** candidates **no longer asked** to share disability info with employer; **this info is never shared** with employer. Employer told **that** a request was made and how accommodation was applied, but **not the details/condition**. [VENDOR — recent policy change, note the date]
- Dedicated candidate accessibility help page exists (candidates.testgorilla.com/…/Accessibility-and-accommodations) — 403 to bot; existence + policy confirmed via search snippet.

## 5.11 GDPR / bias / fairness posture

- **GDPR-compliant** (EU/Amsterdam-based). Candidate rights: access, rectification, erasure. Encryption "state-of-the-art." [VENDOR privacy policy via search]
- **Retention:** candidate data **2 years**; **webcam anti-cheat images 6 months.** [VENDOR]
- Has a **customer Data Processing Agreement (DPA).** [VENDOR]
- **Bias/fairness:** whole brand is "skills-based hiring eliminates bias" (Series A thesis). Tests marketed "scientifically validated." **Independent validity/adverse-impact audits not located** in this research → [UNKNOWN, gap]. Claims are largely **vendor self-assertion**; treat "scientifically validated" as marketing until a technical manual is found.

## 5.12 UK EMPLOYER USAGE — finance penetration (HONEST) 🟡

- **Finance offering is back-office/accounting-oriented:** vendor finance solutions page lists tests for financial analysis, compliance, risk, IFRS, GAAP, Excel, BI, Xero, accounts receivable. **No front-office IB/trading/M&A/wealth content.** [VENDOR]
- **Named finance/fintech clients (all fintech/scale-up, not bulge bracket):** **Revolut** (flagship case study, UK/EU challenger bank, "40% faster hiring"), **Volt, Embrace, Tresl, Lillab.** [VENDOR]
- **Revolut** is the one genuinely UK-relevant, finance-adjacent, high-volume employer confirmed. [VENDOR case study]
- **Bain & Company** named (consulting, not finance) — relevant only as adjacent grad employer. [VENDOR + PREP-VENDOR]
- **Honest verdict:** For **UK front-office bulge-bracket finance early careers, TestGorilla penetration is thin-to-nil.** It belongs to the **fintech / challenger-bank / mid-market / non-finance grad** tier. A UK finance applicant most likely encounters it at a **fintech or scale-up**, not at Goldman/JPM/Morgan Stanley (those use SHL/Aon/HireVue/Amberjack). Say this plainly in the book. [INDEPENDENT + VENDOR synthesis]
- **Volatility flag:** self-serve SaaS → client roster churns; re-verify named clients before publication.

## 5.13 SOURCES (access 2026-08-01)

**VENDOR (testgorilla.com / support / candidates):**
- Test library: https://www.testgorilla.com/test-library/
- Cognitive-ability tests: https://www.testgorilla.com/test-library/cognitive-ability-tests/
- Personality & culture: https://www.testgorilla.com/test-library/personality-culture-tests/ (Big5, DISC subpages)
- Finance solutions: https://www.testgorilla.com/solutions/finance-companies/
- Cheating-detection blog (KEY, candid on false positives): https://www.testgorilla.com/blog/cheating-detection-skills-assessments/
- Anti-cheating behavior tiers help (403 to bot; title/snippets only): https://support.testgorilla.com/hc/en-us/articles/9028797639451-Understanding-anti-cheating-measures-and-behavior-tiers
- Q&A / scoring & retakes blog: https://www.testgorilla.com/blog/testgorilla-questions-answers/
- Series A / anti-bias: https://www.testgorilla.com/blog/testgorilla-secures-70m-series-a-funding-to-help-companies-eliminate-hiring-bias/
- Privacy policy: https://www.testgorilla.com/privacy-policy/ ; DPA: https://www.testgorilla.com/dpa/
- Accessibility/accommodations (403 to bot; snippet): https://candidates.testgorilla.com/hc/en-us/articles/28302003990427-Accessibility-and-accommodations-for-assessments

**INDEPENDENT:**
- Balderton Series A: https://www.balderton.com/news/testgorilla-secures-70m-series-a-to-help-companies-eliminate-hiring-bias/
- UNLEASH Series A: https://www.unleash.ai/skills-development/testgorilla-secures-70m-in-series-a/
- Tracxn profile: https://tracxn.com/d/companies/testgorilla/...
- Capterra pricing: https://www.capterra.com/p/203823/TestGorilla/pricing/
- Trustpilot (1,707 reviews, TrustScore 4/5): https://uk.trustpilot.com/review/testgorilla.com
- G2 discussions: https://www.g2.com/products/testgorilla/discuss

**PREP-VENDOR (commercial, uncorroborated numbers):**
- JobTestPrep: https://www.jobtestprep.com/testgorilla-assessment-practice
- PrepClubs: https://prepclubs.com/tests/testgorilla
- iPrep: https://www.iprep.online/courses/testgorilla-practice-test/

## RESIDUAL GAPS
- **Behavior-tiers help article + candidate accessibility page = 403 to bot** — fetch via browser/authenticated for exact tier definitions and consent wording.
- **Mouse-leave/focus telemetry** as a distinct feature: unconfirmed.
- **AI-answer / plagiarism detection:** not found in sources — confirm whether TestGorilla has added an AI-detection feature (rivals have, 2025–26).
- **Independent validity / adverse-impact / bias audit:** none located — all "scientifically validated" claims are vendor self-assertion.
- **First-person UK candidate testimony** (n=0 direct Reddit threads captured — search returned only G2/Trustpilot aggregate). Reddit/student-forum testimony still needed for real timings and false-positive anecdotes.
- **Exact question counts per cognitive module** not published by vendor; PREP-VENDOR figures conflict.
- **Norm groups / percentile methodology:** vendor public copy says % + ranking, "no pass/fail"; percentile claim is PREP-VENDOR only — verify whether real norm tables exist.
