# 07 — Plum (Plum.io / Plum Discovery / Match Scores) — Raw Research Notes

**Researched:** 2026-08-01 (agent thread, WebSearch + WebFetch, US-routed). All URLs accessed 2026-08-01.
**Coverage vs brief:** 5.1✅ 5.2✅ 5.3🟡 (pricing undisclosed) 5.4✅ 5.5✅ 5.6✅ 5.7✅ 5.8🟡 5.9🟡(inferred) 5.10✅ 5.11✅
**Evidence tags:** `[VENDOR]` `[INDEPENDENT]` `[CANDIDATE, n=X]` `[PREP-VENDOR]` `[INFERRED]` `[UNKNOWN]`

> ⚠️ **HEADLINE / VOLATILITY FLAG:** **Plum was acquired by Phenom (Philadelphia) — announced 28 April 2026, ~3 months before this research date.** `plum.io/personality-test` now **301-redirects to phenom.com**. Plum products are being folded into Phenom's platform. Anything below about "Plum as a standalone vendor" is legacy-in-transition; re-verify branding/URLs before publication. [VENDOR/INDEPENDENT]

> ⚠️ **SOURCE-CONFLICT FLAG (Citi):** UK prep vendors disagree on what "Citi's Plum assessment" actually is. jobtestprep.co.uk + aptitudeprep say it IS the plum.io Discovery Survey; graduatesfirst says Citi's tests are "powered by Korn Ferry Talent Q" (numerical/logical/SJT). Do not state Citi-uses-plum.io as settled fact — see §5.11.

> ⚠️ **TALENT-COUNT CONFLICT:** Prep vendors uniformly list **"10 Plum Talents"** (named list). Plum's own audited system description (FairNow) says candidates receive scores for **12 Talents**. Treat "10 named talents" as the candidate-facing marketing list and "12" as the underlying scored set; flagged throughout.

---

## 5.1 — Ownership / corporate / what it is

- **Legal entity:** Plum.io Inc. **Founded 2012**, **Kitchener-Waterloo, Ontario, Canada**. Founder & CEO **Caitlin MacGregor**. [INDEPENDENT — BetaKit; cross-checked founding year across G2/CBInsights]
- **Former name: Cream.HR** (rebranded to Plum). [INDEPENDENT — WebSearch/G2 seller summary; corroborated as commonly cited]
- **Funding (pre-acquisition):** ~**$19M CAD** total raised; last round ~$8M CAD early 2023. Investors incl. BDC Capital Women in Technology Venture Fund, Export Development Canada, Real Ventures, Pearson Ventures, JFF Ventures, Strada Education Network, EduLab Capital Partners, Impact Engine. [INDEPENDENT — BetaKit]
- **ACQUISITION:** Acquired by **Phenom** (Philadelphia AI-hiring platform). Press/blog date **28 April 2026**; BetaKit frames announcement as **May 2026, deal closed the prior month**. Terms **not disclosed**. All Plum employees joined Phenom's **~1,600-person** team. Plum was **Phenom's 3rd acquisition of 2026** (Jan: "Included"; Feb: "Be Applied"; then Plum), assembling a "full-spectrum assessment stack." [VENDOR — phenom.com/press-release; INDEPENDENT — BetaKit, technical.ly, staffingindustry.com, The Logic, Nucleus Research]
- **What it is:** Psychometric + behavioural talent-assessment SaaS. Measures **personality (Five-Factor Model), cognitive/problem-solving ability, and social intelligence**, distilled into **"Talents"** (recurring patterns of thought/feeling/behaviour = soft skills), then produces **role-specific Match Scores**. Phenom markets Plum's tech as validating "durable skills AI can't fake … emotional intelligence, adaptability, sound judgment, resilience," with proprietary **Role Model™** technology. [VENDOR — phenom]
- **Named pre-acquisition customers:** **Scotiabank** (Canadian bank), **Hyundai**, **Whirlpool**. [INDEPENDENT — BetaKit]
- **Candidate-facing platform:** "Plum Discovery Survey" (candidate) + recruiter dashboard with Match Scores. Help centre at help.plum.io (returned **HTTP 403** to automated fetch on 2026-08-01 — content below reconstructed from prep-vendor paraphrase + FairNow audit + search snippets). [UNKNOWN — direct vendor help pages not fetchable this session]

## 5.2 — Why it exists / rationale / predictive-validity claims

- **Thesis:** match people to roles on **psychometric fit** rather than résumé/credentials; surface candidates "that never would have been discovered through a traditional hiring process." [VENDOR — VentureBeat interview headline]
- **Predictive-validity marketing claim:** Plum data is **"4× more predictive of future job success than a resume"** / "assessment accuracy proven four times greater than resume screening alone." [VENDOR — repeated across G2 summary + phenom press release; NOT independently verified; no peer-reviewed citation located this session]
- Underlying science framing: Talents "grounded in years of research on personality, cognitive ability, and social intelligence"; **derived from the Five-Factor Model (FFM)** plus facets of cognitive ability. [VENDOR — as quoted verbatim in FairNow independent audit "System description"]

## 5.3 — Why a firm picks Plum / differentiators / pricing

- **Differentiators marketed:**
  - **Match Scores** — single 0–99 fit number per candidate-per-role (see §5.6). [VENDOR/PREP-VENDOR]
  - **Reusable candidate profile** — one Discovery Survey serves all Plum employers + internal roles (see §5.6). [VENDOR — help-centre snippets]
  - **Internal mobility / "Talent Re-Discovery"** — search existing applicant/employee pool against new roles without re-assessment. [PREP-VENDOR paraphrase of vendor feature]
  - **DEI / fairness / "blind" behavioural matching** — matches on Talents not credentials; markets bias audits (see §5.10). [VENDOR]
  - **Role definition by top performers** — Match Criteria Survey completed by internal experts/top performers (see §5.5). [VENDOR/PREP-VENDOR]
- **Pricing:** **NOT publicly disclosed** — quote/contact-sales model (TrustRadius, Capterra, GetApp, SoftwareSuggest all list "contact for pricing"). No per-candidate or seat figure located. [UNKNOWN — vendor quote-based]
- **Third-party ratings:** G2 ~**4.4/5** (~71 reviews); praised for ease of setup + depth of competency breakdown. Named "Hot Company to Watch 2023" by Nucleus Research. [INDEPENDENT — G2; VENDOR PR — GlobeNewswire]
- **Reference clients (any sector):** Scotiabank, Hyundai, Whirlpool [INDEPENDENT — BetaKit]; Citi, Bloomberg, Deloitte [PREP-VENDOR claims — see §5.11 caveats].

## 5.4 — FULL MECHANICS: Plum Discovery Survey

**Duration/format:** **~25 minutes, UNTIMED** ("no time limit," "no record of how long it took," "time taken has no impact on results"). Delivered online via **email invitation**; completion window **72 hours (jobtestprep.com) / 5 days (jobtestprep.co.uk)** — varies by employer config. [PREP-VENDOR consistent across jobtestprep, aptitudeprep, assessmentcentrehq; echoes vendor FAQ snippet]

**Structure — 5 sections (prep-vendor reconstruction; Plum FAQ says "sections 1&3 = personality, 2&4 = problem-solving, 5 = workplace behaviour"):**

| # | Section | Format | ~Items | Measures |
|---|---|---|---|---|
| 1 | Priorities & Preferences | Forced-choice: pick statement **most** and **least** like your view | ~**20** statements | Personality (FFM facets — e.g. creativity/change, structure, dynamism) |
| 2 | Problem-Solving / Cognitive | Abstract reasoning — **"select the missing piece / next in series"**; matrix grids (9 grids × 9 coloured boxes) and/or domino-sequence variants | ~**7** (jobtestprep) / **7–8** (Bloomberg variant) | Fluid reasoning / cognitive ability |
| 3 | "You" Descriptor | Adjective lists — choose **3 most** + **3 least** describe you | ~**5** | Personality dimensions |
| 4 | Problem-Solving / Cognitive | As section 2 | ~**7** | Cognitive ability |
| 5 | Social Interaction | **SJT** — workplace scenario, rank responses **most→least effective** | ~**7** scenarios | Social intelligence / behaviour |

[PREP-VENDOR — jobtestprep.com, jobtestprep.co.uk, aptitudeprep, assessmentcentrehq, assessmentpass.co.uk; item counts labelled "about"; treat as ~figures]

- **Personality basis:** **Yes, Big Five / Five-Factor Model.** Explicit in Plum's own system description ("Talents are derived from the Five-Factor Model (FFM) of personality as well as facets of cognitive ability"). [VENDOR-verbatim, via FairNow audit]
- **Cognitive/problem-solving section:** the **only objectively-scored** part (right/wrong); abstract non-verbal "next-in-series" pattern completion. [PREP-VENDOR — assessmentcentrehq: "only logic puzzles have objective scoring"]
- **Adaptivity:** **No evidence of item-level adaptivity.** Untimed, fixed-form described. [INFERRED — absence in all sources; flag [UNKNOWN] for definitive]
- **Device:** desktop/online browser via email link; no explicit mobile guidance found. [UNKNOWN — not stated]
- **Output to candidate:** personalised **Plum Profile** = top-3 Talents, preferred working environment/style, self-reflection/interview prompts. [PREP-VENDOR + VENDOR]

**The named "10 Plum Talents" (candidate marketing list):** Adaptation, Communication, Conflict Resolution, Decision Making, Embracing Diversity, Execution, Innovation, Managing Others, Persuasion, Teamwork. [PREP-VENDOR — jobtestprep/aptitudeprep; **NB audit says candidates are scored on 12 Talents — count conflict**]

## 5.5 — Tailoring: role-specific Match Scores

- **Match Criteria Survey (employer side):** internal **expert contributors / top performers** complete a **~6–8 minute** survey defining the behavioural requirements of a role. Aggregated results reveal the **top 5 Talents** most critical for that role. [VENDOR/PREP-VENDOR — help-centre snippets + jobtestprep]
- **Best practice:** minimum **3, ideally ~8** contributors per role; ask **top performers** to complete the Match Criteria Survey (not the Discovery Survey) so high performers "define what a top performer looks like." [VENDOR — help.plum.io "Match Criteria Best Practices" snippet]
- **Mechanism:** the same candidate Discovery profile (12 Talent scores) is scored **differently per role** — Match Score = alignment between candidate's Talent set and that role's ranked top-5 Talents. One profile → many role-specific Match Scores. [VENDOR — FairNow system description: "Talent Match model combines candidate Talent results and the ranked Talents from the employer to calculate scores reflecting alignment"]

## 5.6 — Scoring / norms / cut-offs / reusability

- **Match Score scale:** candidate-facing/help-centre says **1–99**; the audited model outputs **30–99** ("Each application receives a score ranging from 30 to 99"). Use **30–99** as the technically-audited range; note 1–99 is the marketing statement. [VENDOR help-centre snippet = 1–99; INDEPENDENT audit = 30–99 — mild conflict, flagged]
- **Interpretation benchmarks:** **>80 = strong** (Plum suggests shortlisting if >80 and other specs met); **61 = average.** [VENDOR — help.plum.io "What are Match Scores…"]
- **NOT a percentile, NOT pass/fail:** "there is **not a designated pass/fail cutoff**; all candidates are shown to the recruiter, **ranked by match score**." Score = fit-to-*this*-role, not norm-percentile. [VENDOR-verbatim via FairNow]
- **What recruiter sees:** every candidate, ranked by Match Score, for the given requisition. [VENDOR via FairNow]
- **REUSABLE PROFILE (key selling point):** Discovery Survey **only needs to be completed once**; the resulting Plum Profile is **reusable across all employers that use Plum**, because raw results "are not job-specific until combined with the employer's Match Criteria." Candidates can **link a profile to a new account/email** and submit an existing profile to new applications without retaking. [VENDOR — help.plum.io "Can I re-do…", "How can I submit my existing Plum Profile…", "How will my profile be used"]
- **Retake policy:** cannot redo immediately; per prep vendors, **retake possible after ~1 year**. Re-doing changes the profile. [PREP-VENDOR — assessmentcentrehq "after a year or more"; VENDOR help-centre article "If I re-do my Plum Discovery Survey, will my results change"]
- **Norms:** no traditional norm-group percentile; scoring is relative to the **role's Match Criteria**, not a demographic norm sample. For the bias audit, "scoring rate" was computed **vs the median score** across the sample (audit methodology, not operational cut-off). [INDEPENDENT — FairNow]

## 5.7 — How to prepare

- **Largely authenticity-based.** All prep vendors + vendor agree: personality/behaviour sections have **no right answers**; time taken doesn't matter; answer honestly. [PREP-VENDOR consensus + VENDOR]
- **Faking debunk:** because the score is *fit to a specific role's* Talent profile (unknown to candidate) and combines multiple instruments, "gaming" toward a generic "good" answer is largely futile — "you can't get a perfect score … what each employer is looking for is different." Forced-choice most/least (ipsative) format further resists uniform faking. [PREP-VENDOR — assessmentcentrehq; INFERRED re: ipsative resistance]
- **Practicable part = cognitive/problem-solving** (sections 2 & 4): abstract reasoning / next-in-series / matrices — prep vendors sell practice packs specifically for these + SJT. [PREP-VENDOR — jobtestprep, aptitudeprep, assessmentpass]
- **SJT tip:** answer "what *should* I do" (best practice) not "what *would* I do." [PREP-VENDOR — jobtestprep]
- Practical: well-rested, distraction-free environment (untimed, so no speed pressure). [PREP-VENDOR]

## 5.8 — Integrity / proctoring

- **Typically UNPROCTORED.** No webcam/lockdown proctoring mentioned in any candidate/prep source; untimed remote email-link format. [INFERRED from absence across all sources + PREP-VENDOR silence]
- **Anti-faking relies on design not surveillance:** ipsative forced-choice, role-hidden scoring, multi-instrument blend (see §5.7). No tab-switch/keystroke telemetry documented. [INFERRED]
- **Cognitive section** is the only objectively-right/wrong content and is short (~14 items total) and untimed — limited integrity exposure. [PREP-VENDOR]
- **GAP:** no explicit vendor statement on proctoring, honesty/consistency scales, or response-pattern flagging located (help pages 403'd). Flag [UNKNOWN] for definitive integrity mechanics. [UNKNOWN]

## 5.9 — False-positive risks

- [INFERRED — no direct source] Because Match Score depends entirely on the employer's **Match Criteria Survey quality** (as few as 3 internal raters), a mis-specified "ideal profile" propagates: candidates matched to a **flawed top-5-Talent template** could rank highly yet be poor real-world fits. Top-performer-defines-role approach risks **cloning incumbents** (homogeneity/representativeness risk) — partially mitigated by bias auditing (§5.10) but a structural false-positive/negative vector.
- Ipsative (forced most/least) personality scoring limits cross-candidate comparability of raw traits; the Match Score abstracts this away, which can mask why a candidate scored high. [INFERRED]
- Reusable single profile means a candidate optimising once carries that profile everywhere — a one-off "good day"/coached run persists across employers. [INFERRED]

## 5.10 — Adjustments / accessibility / GDPR / bias audit

- **BIAS AUDIT (strong, independent):** **FairNow** conducted a disparate-impact audit of **Plum's Talent Match model**, report dated **7 Nov 2024**, aligned to **NYC Local Law 144 (AEDT law)**. [INDEPENDENT — FairNow PDF, use.plum.io]
  - **Sample:** **528,891 US applications** (22 Aug 2023–13 Sep 2024); **28,881** had gender/race demographics.
  - **Finding:** **No evidence of disparate impact** — no group's selection rate fell below 80% of the most-favoured group (4/5ths rule), for race, gender, or intersections.
  - **Gender impact ratios:** Female **95.9%**, Male 100% (reference).
  - **Race impact ratios:** White 97.2%, Two-or-more 100%, Asian 87.2%, Hispanic/Latino 91.7%, **Black/African-American 83.2%** (lowest univariate; still >80%). Indigenous N/A (<2% sample).
  - **Intersectional lowest:** **Black female 82.3%** (still passes 4/5ths).
  - **Method:** no pass/fail cutoff exists, so audit used LL144 **"scoring rate vs sample median."** Scores 30–99.
  - Data self-reported by Plum; FairNow did not independently verify data completeness. [caveat, stated in report]
- **Fairness marketing:** Plum publishes bias-audit resources + glossary/blog on adverse impact and the role of bias audits. [VENDOR — plum.io/blog, plum.io/glossary/adverse-impact, help.plum.io "Plum and Auditing for Bias"]
- **GDPR / data:** Plum has public **Terms of Service** (plum.io/terms) and candidate data-use FAQs ("How will my profile be used"). Specific GDPR/UK-GDPR lawful-basis, retention, and data-residency detail **not extracted this session** (help pages 403'd). [UNKNOWN — verify directly; note Canada-HQ + US data processing → adequacy/transfer questions for UK/EU candidates worth checking]
- **Accessibility/adjustments:** untimed design inherently aids some needs; no specific reasonable-adjustment / alternative-format process documented in sources found. [UNKNOWN — gap]

## 5.11 — UK FINANCE / early-careers employer usage (HONEST ASSESSMENT)

**Verdict: Present in UK graduate/early-careers finance pipelines — but narrowly, and evidence is prep-vendor-driven with a genuine identity conflict. NOT a front-office IB standard.**

- **Citi** — Multiple **UK** prep vendors (jobtestprep.co.uk, aptitudeprep) state Citi's early-stage online assessment **is the "Plum Discovery Survey"** (plum.io), post-application / pre-video-interview, screening out a large share of applicants. [PREP-VENDOR]
  - **Candidate corroboration:** The Student Room **"Citi Graduate 2024"** thread has applicants referring to a **"plum test"** in the Citi process. [CANDIDATE, n≥1 — thestudentroom.co.uk t=7409364; page returned 403 to fetch, evidenced via search snippet only]
  - **⚠️ CONFLICT:** graduatesfirst.com describes Citi's assessments as **"powered by Korn Ferry Talent Q"** (numerical + logical + SJT, 20–30 min each) — i.e. **NOT plum.io**. Possible explanations: (a) prep vendors conflate two different Citi tests; (b) Citi changed provider over time; (c) "Plum" mislabel. **Do not assert Citi=plum.io as fact.** [PREP-VENDOR conflict — flag]
- **Bloomberg** — Dedicated UK prep pages (jobtestprep.co.uk/bloomberg-plum-assessment, assessmentpass.co.uk 2023 post, aptitudeprep, graduatesfirst) describe a **Bloomberg "Plum Discovery Survey"** (~25 min, untimed, same 5-section structure, "10 talents essential for success at Bloomberg"). More consistent multi-vendor agreement than Citi. [PREP-VENDOR — multiple; Bloomberg = finance-data/tech, front-office-adjacent]
  - **Candidate corroboration:** LinkedIn posts of applicants sharing "my top Plum Talent" results (e.g. Sachin Heer, 2023). [CANDIDATE, n≥1 — LinkedIn]
- **Deloitte** — named alongside Citi/Bloomberg as a Plum user by prep vendors (professional services, finance-adjacent). [PREP-VENDOR — weaker sourcing]
- **Banking client (non-UK but relevant):** **Scotiabank** confirmed as a Plum customer by independent press. [INDEPENDENT — BetaKit] Demonstrates Plum *can* land bank clients, but this is Canadian retail/commercial banking, not UK IB.
- **Honest bottom line:** Plum's UK finance footprint is **real but shallow and concentrated in graduate/early-careers screening at Citi and Bloomberg** (both partly disputed / prep-vendor-sourced). It is **not** a recognised standard for UK front-office investment banking, where SHL, Aon/cut-e, Korn Ferry, and HireVue/game-based tools dominate. Penetration should be described as **niche/early-careers, not front-office**, and **volatile** given the April 2026 Phenom acquisition (branding and product may migrate to "Phenom" and change candidate-facing form). [INFERRED synthesis + flagged sourcing]

---

## Strongest / primary sources
- **FairNow independent bias audit (PDF, Nov 2024)** — the single best independent primary doc: system description (FFM, 12 Talents, 30–99 scale, no pass/fail), + LL144 disparate-impact results on 528,891 applications: https://use.plum.io/hubfs/Resources/Audit/2024-2025/Plum-Talent-Match-bias-audit-nov-2024.pdf
- **Phenom acquisition press release / blog (28 Apr 2026):** https://www.phenom.com/press-release/phenom-acquires-plum-ai ; https://www.phenom.com/blog/phenom-acquires-plum
- **BetaKit acquisition + corporate history:** https://betakit.com/plum-acquired-by-us-based-phenom-to-reduce-bad-hires-in-the-age-of-ai/
- **jobtestprep Discovery Survey mechanics:** https://www.jobtestprep.com/plum-assessment ; UK Citi page: https://www.jobtestprep.co.uk/citi-assessment-centre
- **Match Score / Match Criteria (search-surfaced vendor help snippets):** https://help.plum.io/hc/en-us/articles/360002475734-What-are-Match-Scores-and-what-is-a-good-Match-Score-
- **The Student Room Citi Graduate 2024 (candidate "plum test"):** https://www.thestudentroom.co.uk/showthread.php?t=7409364&page=2

## Residual gaps / to-verify before publication
- **help.plum.io returned HTTP 403 to automated fetch** — Discovery FAQ, retake, profile-use, proctoring, and bias-audit help pages reconstructed via prep-vendor paraphrase + search snippets. Verify directly (human browser) for exact wording.
- **Talent count 10 vs 12** unresolved — confirm which is candidate-facing vs internal.
- **Match Score range 1–99 vs 30–99** — reconcile (marketing vs audited operational floor).
- **Citi provider identity** — is Citi's screener plum.io or Korn Ferry Talent Q (or both, at different stages/years)? Needs a primary/candidate confirmation, ideally current-cycle.
- **Pricing** — entirely undisclosed (quote-based).
- **GDPR/UK-GDPR** specifics (lawful basis, retention, UK/EU↔Canada/US transfer) — not located; check Plum/Phenom privacy + terms.
- **Adjustments/accessibility** process — no documented reasonable-adjustment route found.
- **Post-Phenom branding** — confirm whether "Plum Discovery Survey" persists or is rebranded under Phenom before finalising the chapter; plum.io URLs already redirecting.
- **Predictive-validity "4×"** claim — no independent/peer-reviewed backing located; treat as vendor marketing.
