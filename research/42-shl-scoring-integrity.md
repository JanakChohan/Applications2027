# 42 — SHL: Scoring, Filtering & Integrity Architecture — Raw Sourced Findings

**Researched:** 2026-08-01. Builds on `research/01-shl.md` (do not re-derive: reliability 0.77–0.84; theta→T(50/10)/sten(5.5/2); percentiles ordinal; SEM=√(1−rxx)·SD; verification-test + Confidence Indicator model; ability↔verification r≥0.70; Monte Carlo 10,000 candidates, cheating modelled +2SD, ability↔cheating-propensity r=−0.3; "Not Verified" = investigate, not convict).

**Evidence tags:** [VENDOR] = SHL's own material · [INDEPENDENT] = academic/journalistic/third-party · [PREP-VENDOR] = commercial prep site (biased) · [INFERRED] = my reasoning · [UNKNOWN] = gap.

> **Standing caution (carried from 01-shl.md):** prep vendors routinely (a) state confidential cut-scores as fact and (b) conflate unproctored Verify with webcam-proctored delivery. The base Verify model is *unsupervised test + supervised verification test*; webcam/screen-capture proctoring is a **separate optional layer** the employer must switch on.

---

# PART 1 — SCORING & FILTERING

## 1.1 The scoring pipeline (raw → scaled → normed) — VENDOR PRIMARY

Established in 01-shl.md and confirmed by the sample report below:

`item responses → IRT theta (ability estimate, item-difficulty-weighted) → norm lookup against a chosen Comparison Group → Percentile + T-score + Sten (+ letter Grade on candidate reports)`

**Critical mechanic, stated by SHL verbatim** [VENDOR — Verify Ability Test Report v2.0 sample, p.8]:

> "It is important to understand that because each candidate receives a different set of items, there is not a direct correlation between Hit rate/Accuracy and the Percentile, T or Sten score achieved; **an individual with a lower hit rate may achieve a higher percentile score and vice-versa.**"

This is the single most important scoring fact for a candidate: **raw number-correct is not the score.** Because items are drawn from a randomised bank with IRT difficulty parameters, getting fewer harder items right can outrank getting more easy items right. Source: https://service.shl.com/docs/Verify%20Ability%20Report%20v2.0%20English%20International.pdf (accessed 2026-08-01)

Also defined verbatim in the same report [VENDOR]:
- **"Number Attempted"** — "the number of questions the candidate has seen during the test. The total may include questions that the candidate has not provided a response to."
- **"Work rate"** — "a measure of how far the candidate has got through the test... the number attempted divided by the total number of questions in the test. This is expressed both as a percentage and as raw data."
- **"Hit rate"** — "a measure of accuracy... the number of questions the candidate has answered correctly divided by the total number of questions attempted. Expressed both as a percentage and as raw data."

→ [INFERRED] The employer therefore sees *speed* and *accuracy* as separate reported dimensions alongside the normed score. A candidate who answers few but gets them right has a high hit rate / low work rate; both are visible.

## 1.2 Comparison (norm) groups — VENDOR PRIMARY

- 01-shl.md: **~70 comparison groups** across the Verify range (test type × job level × industry) [VENDOR-manual].
- The sample Ability Test Report carries an explicit **"ASSESSMENT METHODOLOGY"** table pairing each test with its comparison group [VENDOR, verbatim]:

| Questionnaire / Ability Test | Comparison Group |
|---|---|
| Graduate/University Inductive Reasoning UKE | General Population 2007 |
| Graduate/University Numerical Reasoning UKE | General Population 2006 |
| Graduate/University Verbal Reasoning UKE | General Population 2006 |
| Verify - Operational Checking UKE | General Population 2009 |
| Verify - Operational Calculation UKE | General Population 2009 |

Key observations [VENDOR + INFERRED]:
1. **Comparison groups are year-stamped** ("General Population 2006/2007/2009") — norms are frozen standardisation samples, not rolling. A 2018-issued report was still norming against a 2006 sample.
2. **Test "Level" is a separate axis from comparison group.** The report shows a `Level:` field per subtest — e.g. `Level: Graduate/University` for reasoning, `Level: Operational` for Checking/Calculation. So a *Graduate-level test* can be normed against a *General Population* group. Difficulty level and reference population are configured independently.
3. **`UKE` suffix** = UK English variant; `Language: English - International` is reported separately. Language/locale is a third axis.
4. The report is explicit that the comparison group is chosen by the client: SHL's Verify G+ product page states the report gives scores "using the comparison group selected by the user" [VENDOR, shl.com product catalog].

**Named norm groups beyond General Population** — 01-shl.md lists Graduate (UK/Global), Finance Graduates, Professional/Managerial, IT Professionals, industry variants [PREP-VENDOR: careertestprep]. **A definitive SHL-published catalogue of all ~70 groups was NOT located on the open web.** [UNKNOWN] — it appears to live behind the TalentCentral client portal / Verify User Guide.

**CURRENT-PRODUCT comparison-group names — VENDOR PRIMARY** (SHL Verify Interactive Report sample, https://service.shl.com/docs/Verify%20Interactive%20Ability%20Report%20DNI%20UKE.pdf, accessed 2026-08-01):

| Test (internal code) | Comparison Group |
|---|---|
| `TC_Verify_Interactive_Inductive_Reasoning_USE` | Interactive Inductive Reasoning General Composite (INT) v1 |
| `TC_Verify_Interactive_Numerical_Reasoning_USE` | Interactive Numerical Reasoning General Composite (INT) v1 |
| `TC_Verify_Interactive_Deductive_Reasoning_USE` | Interactive Deductive Reasoning General Composite (INT) v1 |

Also named in the same report's worked example: **"Verify G Plus General Population (INT) 2016"**.

→ [VENDOR] Naming convention decoded: `<Product> <Subtest> <Population> (<Locale: INT = International>) <version or year>`. "General Composite" and "General Population" are the *default* groups shipped with the Interactive range; the year/`v1` stamp again shows frozen standardisation samples. Note the Interactive range abandons the "Level: Graduate/University vs Operational" field present in the legacy Verify report — the legacy report carried Level as a separate axis, the Interactive sample does not display one.

**Why this matters to a candidate** [INFERRED, high confidence]: the *same performance* yields a materially different percentile depending on group. A General Population norm inflates a graduate's percentile relative to a Graduate or Finance-Graduate norm. Prep-vendor sources make the same point ("the single most important factor in determining what a good score means") [PREP-VENDOR: careertestprep].

## 1.3 What the reports actually show — VENDOR PRIMARY (two distinct reports)

SHL ships **separate employer-facing and candidate-facing reports** from the same test event. They show different things. Both sample PDFs are publicly downloadable from SHL's own support domain.

### (a) Employer/user-facing: **Verify Ability Test Report v2.0**
https://service.shl.com/docs/Verify%20Ability%20Report%20v2.0%20English%20International.pdf (accessed 2026-08-01) [VENDOR]

Per subtest it shows:
- **Percentile** ("Percentile compared to the General Population 2007 comparison group") with a graphic
- **T-score** (e.g. `T-score: 57`)
- **Sten score** (e.g. `Sten-Score: 6`, `Sten score: 7`)
- `Level:` (e.g. Graduate/University, Operational), `Language:`, `Comparison Group:`, `Type of Test:`
- A **narrative interpretation sentence**, e.g. verbatim: *"Sample Candidate's estimated numerical critical reasoning ability is **above average** when compared to the comparison group. The candidate's result is **better than 87% of the people in this group**. This suggests that the candidate will display a high level of ability in understanding or interpreting numerical data and mathematical calculations as compared to the group."*
- **Number Attempted / Work rate / Hit rate** (see 1.1)
- **Assessment Methodology** table (test ↔ comparison group)

**There is NO "recommended / not recommended" verdict and NO pass/fail line in this report.** [VENDOR — absence observed across the full 9-page extract]. The report outputs *scores and descriptors only*; the sift decision is the employer's. This directly corroborates 01-shl.md's inference that SHL supplies the metric and the employer sets the threshold.

**Verbatim front-page caveat** [VENDOR — this is the key integrity sentence in the employer report]:
> "This Ability Test Report provides the scores from Sample Candidate's Verify Ability Tests. **If these tests were unsupervised, there is a small possibility that these scores do not represent their actual level of ability. A Verification Test is recommended to verify these scores.** (See the following page for guidance.)"

**Verbatim "ABOUT THIS REPORT"** [VENDOR]:
> "This report shows the result(s) obtained from ability test(s). **The use of these tests is limited to those people who have received the necessary training in their use and interpretation.** The report herein is generated from the results of test(s) answered by the respondent. **This report has been generated electronically - the user of the software can make amendments and additions to the text of the report.** SHL Global Management Limited and its associated companies cannot guarantee that the contents of this report are the unchanged output of the computer system."

→ [INFERRED, notable] SHL explicitly warns that the client can **edit the report text**. Anything a candidate is shown by an employer may not be SHL's unaltered output.

### (b) Candidate-facing: **Verify Candidate Report (TC Version)**
https://service.shl.com/docs/Verify%20Candidate%20Report%20(TC%20Version)%20English%20International.pdf (accessed 2026-08-01) [VENDOR]

Shows something **different and coarser**:
- **Grade letter on an A–E band scale**, rendered as a 5-segment bar labelled `E D C B A` (left to right). Sample shows `Grade E`.
- The header still reads "Percentile compared to the General Population 2006 comparison group" — but **no numeric percentile, no T-score, no sten is printed to the candidate** in this sample. Only the band.
- Narrative: *"Your performance on this test indicates that your verbal reasoning ability is **well below average** when compared to the comparison group..."*
- **"Ideas to help improve your skills"** — developmental tips per subtest (read widely, crosswords, business journals, etc.)
- Verbatim caveats:
  > "The tests that you completed provide a fair and objective assessment of your cognitive ability. Research has shown that these tests can provide reliable information concerning future performance in many different jobs. **However, many other factors also play an important role in predicting job success.**"
  > "This report is confidential and is intended for your personal use only. Please note that **test results remain valid for about 12 to 18 months.**"
- Verbatim definition of norming: *"your performance has been compared to that of a large group of individuals who have taken these tests in the past. This is known as a comparison group."*
- Verbatim subtest construct definitions (useful for what's actually measured):
  - *Verbal reasoning*: "measures the ability to evaluate the logic of various kinds of arguments... emphasises understanding, using and evaluating verbal information **rather than language usage, spelling or grammar**."
  - *Numerical reasoning*: "make correct decisions or inferences from numerical data... emphasis is on **understanding and evaluating data rather than on computation**."
  - *Inductive reasoning*: "work with incomplete information and create solutions to novel problems from first principles."
  - *Checking*: "compare information quickly and accurately."

**Band scale correction to 01-shl.md:** the prep-vendor claim of an **A–D** band scale is WRONG for this report; SHL's own candidate report uses **A–E (five bands)**. [VENDOR overrides PREP-VENDOR]. The percentile-to-band boundaries are **not printed in the report** [UNKNOWN — standard SHL practice historically maps A=top 10%, B=next 20%, C=middle 40%, D=next 20%, E=bottom 10%, i.e. a 10/20/40/20/10 split, but **this specific mapping is NOT confirmed by any SHL source located here — treat as unverified**].

- **Result validity window: "about 12 to 18 months"** [VENDOR, verbatim, candidate report]. This is an SHL statement, and it bears directly on retake/re-use policy (§1.6).

### (c) CURRENT product: **SHL Verify Interactive Report** (employer-facing) — VENDOR PRIMARY
https://service.shl.com/docs/Verify%20Interactive%20Ability%20Report%20DNI%20UKE.pdf (accessed 2026-08-01)

This is the report for the **current** Verify Interactive range and differs from the legacy Verify Ability Test Report in several material ways.

- **"Overview" page** = a single horizontal percentile bar chart, axis labelled `1 … 30 … 70 … 99 Percentile`, with all three sub-abilities stacked and the numeric percentile printed at the right:
  - Inductive Reasoning — **28**
  - Numerical Reasoning — **57**
  - Deductive Reasoning — **67**
  (sub-test detail pages use a `10 30 50 70 90 Percentile` axis)
- **Sub-abilities are Inductive / Numerical / Deductive** — **no Verbal** in the Interactive range (matches 01-shl.md).
- **Details page per subtest**: construct definition, percentile bar, `Language:`, `Percentile compared to the <name> comparison group`, and a narrative sentence with the explicit percentile, e.g. verbatim: *"Her result is better than 28% of the people in this group. This suggests that she will have difficulty in understanding incomplete information and solving novel problems by creating solutions from first principles."*
- **Technical information page**: `T-score:` and `Sten-Score:` per subtest (worked sample: Inductive T=44/Sten 4; Numerical T=52/Sten 6; Deductive T=54/Sten 6), prefaced verbatim: *"T-scores and Sten scores are provided for users who are trained in their appropriate use and interpretation."*
- **NO letter grade band** (A–E is the *candidate*-facing legacy report only).
- **NO Work Rate / Hit Rate / Number Attempted** in the Interactive sample — those speed/accuracy fields appear in the legacy Verify Ability Test Report but not here. [VENDOR, absence observed]
- **NO overall composite "General Ability" score printed** in this sample — only the three sub-abilities. [VENDOR, absence observed; note Verify **G+** reports may differ]
- **Again NO pass/fail, NO cut-score, NO hire recommendation.**
- Same "ABOUT THIS REPORT" boilerplate: trained-users-only; *"the user of the software can make amendments and additions to the text of the report"*; SHL disclaims that the contents are unchanged output.

**⚠️ SIGNIFICANT FINDING — the Verification Test is MISSING from the Interactive report.** Compare the two "How to verify a result" tables verbatim:

| Legacy *Verify Ability Test Report v2.0* (2018) | Current *SHL Verify Interactive Report* (2019) |
|---|---|
| **"Administer a Verification Test — Administering a supervised Verification Test is the most consistent way to verify the original test results. This is strongly recommended."** | *(row absent)* |
| Consider information from other competency assessments | Consider information from other competency assessments |
| Use information from other sources | Use information from other sources |
| Use structured interviewing techniques to probe related competencies | Use structured interviewing techniques to probe related competencies |

And the front-page caveat differs: the legacy report says *"…A Verification Test is recommended to verify these scores."*; the Interactive report's caveat stops at *"…there is a small possibility that these scores do not represent her actual level of ability."* with **no verification-test recommendation**.

→ [INFERRED, moderate-to-high confidence] **SHL does not appear to offer a Verification Test for the Verify Interactive range.** The Interactive report instead pushes clients toward triangulation (other assessments, attainment data, structured interview). This is a meaningful change from the classic model and should be flagged as such — but it is inferred from *absence* in one sample report, not from an SHL statement, so mark it as strong-but-unconfirmed. It is consistent with SHL's pivot to platform-level **proctoring** (§2.3) as the primary integrity layer for current products.

**Both reports share this verbatim client-facing guidance** [VENDOR]:
> "The final decision on how to confirm and use the person's test results should follow internal policies and guidelines. Companies should evaluate the risks involved, corporate policy/governance, the use of other screening and selection tools, time, cost and other factors."

and this verbatim validity claim [VENDOR]:
> "Cognitive ability is the most effective, single predictor of future performance in many different jobs. However, many other factors also play an important role in predicting job performance. **The information in this document should be used as part of a broader evaluation of this person's suitability and potential for the job.**"

→ [INFERRED] SHL's own reports therefore *discourage* using the test score as a sole gate — which is precisely what a percentile cut-off sift does. Useful tension to note: SHL's documented guidance and common employer practice diverge.

## 1.4 Cut-scores: how employers set them — **PARTIALLY ESTABLISHED**

**What is solidly established:**
1. [VENDOR, from report structure] SHL's ability reports contain **no cut-score, no pass mark, and no hire recommendation**. The instrument outputs percentile/T/sten/band + work rate + hit rate. **The threshold is 100% an employer decision.**
2. [VENDOR] "The use of these tests is limited to those people who have received the necessary training in their use and interpretation" — SHL gates interpretation behind trained users (historically BPS Test User Occupational Ability certification in the UK).
3. [INFERRED, high confidence] Because scores are **norm-referenced**, any cut-score is inherently **relative to the chosen comparison group**, not to an absolute standard of competence. A "75th percentile cut" means nothing without naming the group.

**SHL's own published guidance document on setting cut-scores was NOT located on the open web.** [UNKNOWN] — Searches for `SHL setting cut scores guidance`, `SHL cut score best practice` returned only prep-vendor pages. SHL's cut-score guidance appears to sit in client-only material (TalentCentral Learning Portal, Verify User Guide) and in consulting engagements. **Do not fabricate.**

**Prep-vendor claims about employer cut-scores — ALL ESTIMATES, NOT SHL-CONFIRMED** [PREP-VENDOR]:
- "Most competitive graduate employers set cutoffs between the **70th and 85th percentile**"; finance/consulting "**75th–80th or above**"; most other graduate roles "**65th–70th** is competitive"; some roles as low as **40th**; elite finance "top **10–15%**". Source: careertestprep, jobtestprep, prepclubs (accessed 2026-08-01).
- 01-shl.md's figures: bulge-bracket IB ~75th–90th; Big Four ~60th–75th; consulting ~75th–85th. **Two prep sources disagreed on IB, hence a range.**
- **Conflict noted both ways:** these are self-disclaimed as estimates; sources state "cut scores vary by year and applicant pool size." No SHL or employer publication confirms any of them.

**Two filtering architectures described** [PREP-VENDOR, but structurally plausible / INFERRED]:
- **Absolute cut score** — below the line = automatic rejection; above = progress regardless of margin.
- **Rank/top-down sift** — top N% of the applicant pool advance; the effective threshold floats with pool strength and headcount.
→ [INFERRED] The rank model explains why prep vendors say cut-offs "vary by year": under top-down selection there *is* no fixed cut-score, and the same score can pass one cycle and fail the next.

**Multi-hurdle vs compensatory:** [UNKNOWN — no SHL-sourced statement located]. Verify G+ internally produces an overall General Ability score *plus* Numerical/Deductive/Inductive sub-abilities (01-shl.md), which structurally permits either an overall-score hurdle or per-subtest hurdles. Employers can "set their own cut-offs **or weightings across sections**" [PREP-VENDOR]. Not verified.

## 1.5 Pass rates / sift severity
**[UNKNOWN]** — No published SHL or employer pass-rate figures were located. Any number circulating on prep sites should be treated as marketing. **Explicitly do not invent.**
→ [INFERRED, arithmetic only] If an employer sets a 75th-percentile cut against a *graduate* norm group and its applicant pool resembles that norm group, ~25% pass the test stage by construction. That is a property of norm-referencing, not an observed pass rate. If the applicant pool is stronger than the norm group (likely for a competitive scheme normed on General Population), a larger fraction passes.

## 1.6 Retake policy
- **Set by the employer, not SHL** [PREP-VENDOR consistent; corroborated by the absence of any retake rule in SHL's reports].
- [VENDOR, verbatim, candidate report] "**test results remain valid for about 12 to 18 months**" — this is SHL's own statement on score shelf-life and is the nearest thing to an SHL-sanctioned retake interval located.
- 01-shl.md: cooling-off typically 6–12 months; many employers enforce no-retake within a cycle [PREP-VENDOR].
- [INFERRED] Because item banks are randomised (§2.1) and scoring is IRT-based, an immediate retake does not present the same test — so retake restrictions are about practice-effect fairness and applicant-pool policy, not item exposure to the individual.

---

# PART 2 — INTEGRITY / ANTI-CHEATING ARCHITECTURE

## 2.1 Randomised item banks
- [VENDOR, Verify Technical Manual + confirmed by the report caveat in §1.1] **Each candidate receives a different set of items** drawn from a bank; item difficulty parameters are IRT-calibrated so different item sets are placed on a common scale. SHL states this explicitly as the reason hit rate ≠ percentile.
- 01-shl.md: even spread of correct answers across options A–E; no two tests identical.
- **Item exposure control / item-bank security specifics:** [UNKNOWN] — SHL does not publish exposure-rate caps, bank sizes, or rotation schedules on the open web.

## 2.2 Verification test — still the core mechanism
- Model (01-shl.md, VENDOR-manual): unsupervised test → optional **supervised Verification Test**, shorter, same format/difficulty, **different items**; output "Verified"/"Not Verified" via a **Confidence Indicator** comparing the two scores.
- **Still current in the product line and still recommended by default in the report itself** [VENDOR, 2018 report v2.0, front page]: *"If these tests were unsupervised, there is a small possibility that these scores do not represent their actual level of ability. **A Verification Test is recommended to verify these scores.**"* — This sentence is printed on every employer-facing Verify Ability Test Report where administration was unsupervised.
- **Deployment in practice** [PREP-VENDOR, multiple agreeing: assessmentday, graduatesfirst, careertestprep]: employers commonly require the supervised verification re-sit **at the assessment centre / on assessment day**; it is a shorter version of the same test type; online and re-sit scores are compared; significant discrepancies flag to recruiters.
- **2025–26 currency:** [PARTIAL] SHL's Verify range documentation and prep-vendor 2025/2026 guides both still describe verification testing as available. No SHL announcement of its withdrawal was found. [UNKNOWN — which specific current products (Verify Interactive G+ vs legacy Verify) support a verification form is not confirmed by a VENDOR source here.]

## 2.3 Proctoring options SHL offers now — **VENDOR PRIMARY, 2023 & 2025 release notes**

Two SHL Release Notes PDFs were fetched and text-extracted. These are SHL's own client-facing product documentation and are the strongest integrity sources in this dump after the Technical Manual.

- **SHL Release Notes, 14 July 2023** — https://support.shl.com/documents/935/attachments/4915 (accessed 2026-08-01) ✅
- **SHL Release Notes, 17 July 2025 — "Customized proctoring index"** — https://support.shl.com/documents/1090/attachments/7154 (accessed 2026-08-01) ✅

### Proctoring taxonomy — CONFIRMED [VENDOR]
The 2023 release notes describe the project-configuration UI verbatim: *"Under Proctoring setting you will see two things — 1.1. **Automated proctoring** 1.2. **Live proctoring**. Note: By default, all the standard proctoring features will be turned ON."*

So SHL natively offers **both automated (record-and-review/AI) and live (human) proctoring**, selected per project. This resolves the [UNKNOWN] in earlier notes: **live proctoring is an SHL-native option.**

Full flavour ladder [VENDOR + INFERRED]:
1. **Unproctored** — no proctoring enabled at company level (the default state for a company that never asked for it; see enablement below).
2. **Automated proctoring** — image/audio/video capture + browser/clipboard telemetry + AI analysis. Candidate-invisible.
3. **Live proctoring** — human invigilation, project-level setting.
4. **Supervised Verification Test** — the classic backstop; appears to survive only in the legacy Verify range (§1.3c).

### Enablement path — CONFIRMED [VENDOR, verbatim]
- *"These features will have to be switched 'ON' for a company to enable the recruiter to start using it for their project."*
- *"Existing Customers — There's no change for existing customers. **These features are switched OFF by default until the client requests to enable them.**"*
- *"Customers can get this enabled with the help of Account manager/ Managed services (MS)."*
- Proctoring Index specifically: *"**Proctoring index will have to requested to be switched on by a company**, this can be actioned on by their SHL account manager."* and *"The Proctoring Index feature can only be enabled for a company if Proctoring is enabled for that company."*

→ [VENDOR, decisive] **Proctoring is opt-in at the company level, then configured per project.** This directly vindicates the standing caution in 01-shl.md: prep-vendor claims that "SHL watches you via webcam" are true *only where the employer bought and switched it on*. Many high-volume graduate Verify sifts will have none of it.

### The Proctoring Index — the flag employers actually see [VENDOR, verbatim, July 2025]
> "Proctoring index is the flag that conveys the **likelihood of a candidate exhibiting suspicious behavior or using unfair means**. **The recruiter is expected to use this information and manually review further to take a final decision.**"

> "Currently recruiters must review all candidates and their individual violations on the report / excel to take a call whether a candidate has used unfair means or not. In a high candidate volume scenario this becomes tedious. **This flag allows the recruiter to decide which candidates to review first** based on the likelihood of suspicious behavior."

> "SHL has a defined set of features, which contribute to the calculation of proctoring index. These features were decided after **internal studies**, keeping the correctness of the flag in mind. The system reviews the violations made by the candidate against these features, **considering the type as well as the frequency of the violation** — Based on whether the candidate **surpasses the permissible threshold** for any of these features, candidates are assigned a proctoring index: High, Medium, or Low."

**July 2025 changes** [VENDOR]:
- **Company-level feature selection**: clients may now choose *which subset* of proctoring features feeds the index. Verbatim caveat: *"**While the features can be selected, the Individual feature thresholds cannot be altered/customised.** These are set & maintained based on studies that ensure consistency, accuracy, and correctness with which the system flags the likelihood of candidate's suspicious behaviour."*
- **Three-band → two-band**: *"The current three-band system (High, Medium, Low) will be replaced with a **two-band system (High, Low)** to remove ambiguity in candidate evaluation that the medium band introduces."*
- Platform: **TalentCentral+ only** (the 2025 note's platform checkbox marks TalentCentral+ ☒, TalentCentral ☐). Availability **7 July 2025**.
- Distribution: *"Proctoring Index on the candidate reports, project listing & excels or even **pushback the value to the ATS (TCI integrations)**… These results will be presented under a **dedicated proctoring section in reports**."*

**Thresholds themselves are NOT published.** [UNKNOWN] — SHL states they exist, are study-derived, and are not client-alterable, but publishes no numbers.

### Proctoring features (the telemetry menu) — [VENDOR, named in SHL's own docs/portal]
- **Periodic Image Capture** — candidate's image at set intervals.
- **Browser Off Focus** — *"captures the percentage of assessment time that the candidate tries to toggle away"* (a **% of time**, not merely a count).
- **Multi-face Detection** — *"takes a snapshot if more than one person is present in the frame."*
- **Print Screen Count** — *"counts the number of times the candidate attempts to take a screenshot."*
- **Copy Paste Attempt** — *"captures the number of times candidate attempts copy-pastes from the test."*
- **Remote Video Proctoring** (new July 2023) — periodic **video snippets** with timestamps.
- **Remote Audio Proctoring** (new July 2023) — periodic **audio snippets** with timestamps.
- **Multiple Voice Detection** (AI, new July 2023) — *"detect if there were multiple voices present or not in the audio snippets captured."* Rationale verbatim: *"Customers are not able to identify whether someone is **prompting/helping the candidate through verbal cues** while taking an assessment."* Reported as an overall Yes/No metric plus a `Multiple voice detected` column in the standard Excel export.
- **Face Match** (AI) — *"we detect if the participant's picture taken during the **id card image capture** matches with participant's snapshots taken throughout the participant journey."* → confirms **ID-document capture + biometric identity verification** exists in the stack.

**Coverage / limits** [VENDOR]:
- Audio/video proctoring is *"available for non-audio/video input-based assessments. It's not available for 'Smart Interview On Demand' and 'SVAR' yet."* (2023)
- Report rendering *"Only supported on Reportica"* (SHL's reporting engine).
- Works on SHL App and web; older candidate experience (`amcatglobal`) and new (`SHLE`) noted.
- **Conflict flagged both ways:** a search-index summary of SHL's Remote Proctoring Guide states *"proctoring is available for Smart Interview On Demand, Smart Interview Live and Virtual Assessment and Development Centres, but proctoring is not available for job-focused assessments"* — which contradicts the 2023 release note's statement that audio/video proctoring is *not* available for Smart Interview On Demand. Most likely resolution [INFERRED]: the two statements concern *different feature subsets* (general proctoring vs. the new audio/video capture) and different dates. **Unresolved — do not assert either.**

### Candidate visibility [VENDOR, verbatim]
> "On Candidate experience there are **no visible changes** while Audio and Video proctoring are background functions."

→ [VENDOR, decisive] **Audio and video proctoring run invisibly to the candidate.** SHL does not surface an in-test indicator. Whether the candidate is informed at all therefore depends entirely on the employer's invitation email / consent notice. [UNKNOWN — no SHL statement located on mandatory candidate disclosure or consent capture; note this is a live GDPR/UK-GDPR question given biometric Face Match and audio capture.]

### Still-unfetched
SHL **Remote Proctoring Guide** — https://talentcentral.learning.shl.com/pluginfile.php/448/mod_resource/content/11/Remote%20Proctoring%20Guide.pdf — HTTP 503 ×2 + TLS-blocked direct download. Mirror https://talentcentralcn.learning.shl.com/mod/page/view.php?id=256&lang=en also 503. [access attempted 2026-08-01] — would add the admin-side combined proctoring report detail.

## 2.4 Telemetry — DOCUMENTED vs ASSERTED

| Signal | Status |
|---|---|
| Browser off-focus / tab-switch, as **% of assessment time** | [VENDOR-via-index] SHL Remote Proctoring Guide — named feature |
| Periodic webcam image capture | [VENDOR-via-index] named feature |
| Multi-face detection (2nd person in frame) | [VENDOR-via-index] named feature |
| Combined per-candidate proctoring report to admins | [VENDOR-via-index] named feature |
| Score-discrepancy detection (unsupervised vs verification) via Confidence Indicator | [VENDOR — Technical Manual, primary, quantified] |
| Work rate / hit rate reported to employer | [VENDOR — sample report, primary] |
| **Copy Paste Attempt** — count of copy-paste attempts from the test | ✅ **[VENDOR] CONFIRMED** — named proctoring feature; also named in SHL's ChatGPT blog as a proctoring signal |
| **Print Screen Count** — count of screenshot attempts | ✅ **[VENDOR] CONFIRMED** — named proctoring feature |
| **Periodic audio snippets + Multiple Voice Detection (AI)** | ✅ **[VENDOR] CONFIRMED** — July 2023 release |
| **Periodic video snippets** | ✅ **[VENDOR] CONFIRMED** — July 2023 release |
| **Face Match (ID-card image ↔ in-test snapshots, AI biometric)** | ✅ **[VENDOR] CONFIRMED** |
| **Proctoring Index (High/Medium/Low → High/Low)** aggregating threshold breaches | ✅ **[VENDOR] CONFIRMED** — July 2025 release |
| **AI-generated-response detection** (text pattern matching + ML classifier) | ✅ **[VENDOR] CONFIRMED** — see §2.7 |
| Device / IP fingerprinting | [PREP-VENDOR only] — **not documented by SHL** |
| Gaze-direction anomalies / "looking at their phone, looking around, gazing sideways" | [VENDOR — named as the *motivation* for video proctoring in the 2023 release notes, i.e. the recruiter reviews snippets manually for this; **not** stated as an automated AI classifier]. Device substitution: **not documented by SHL** |
| Response-time anomaly / "statistically improbable answer patterns" flagged algorithmically | [PREP-VENDOR] for the *live product*; **but** the underlying statistical-aberrance logic IS vendor-documented in the Technical Manual as the Confidence Indicator |
| Answer-pattern similarity **across candidates** (collusion detection) | [UNKNOWN] — no SHL source located. The Monte Carlo work modelled collusion/proxy as a +2SD inflation but that is detection *via verification*, not via cross-candidate matching |

**Revised key distinction:** SHL's integrity stack is now **two-layered and both layers are vendor-documented**:
- **Psychometric layer** — verification test + Confidence Indicator, the only mechanism documented in *quantified, peer-reviewable* form (Technical Manual, Monte Carlo). Appears to be legacy-Verify-only now (§1.3c).
- **Behavioural/platform layer** — the proctoring feature menu + Proctoring Index, documented by *name and function* in SHL release notes but with **thresholds and decision rules withheld** ("cannot be altered/customised… set & maintained based on studies").
Only device/IP fingerprinting and cross-candidate collusion analytics remain purely prep-vendor assertion.

## 2.5 How flags are actioned; what the candidate is told
- [VENDOR, Technical Manual, 01-shl.md] "Not Verified" is framed as requiring **investigation, not conviction** — legitimate causes listed include distractions, not attempting all items, physical/psychological state on the day, and whether the candidate had used shldirect.com practice materials.
- [VENDOR, Technical Manual] Telling candidates **up front** that honesty is expected and that verification will be used **reduces cheating incidence** — i.e. SHL's own position is that *deterrence by disclosure* is part of the architecture.
- [VENDOR, sample report] Employer receives scores + work/hit rate; proctoring data arrives as a **separate combined proctoring report** [VENDOR-via-index]. The score report itself carries no flag field.
- **VENDOR PRIMARY on actioning, July 2025 release notes** — verbatim:
  > "Proctoring index is the flag that conveys the likelihood of a candidate exhibiting suspicious behavior or using unfair means. **The recruiter is expected to use this information and manually review further to take a final decision.**"
  > "Recruiter takes the next set of actions for candidates: The next set of recommended actions include, **manually verifying and rejecting the candidates** based on the proctoring results in the reports."
  → [VENDOR] SHL's documented design is **triage, not adjudication**: the index ranks who to review first; the human recruiter decides. This is the same posture as the Technical Manual's "Not Verified = investigate". **Consistent across 18 years of SHL documentation.**
  → [INFERRED, and a real risk to flag] SHL *recommends* manual review, but also ships the index **into the ATS via TCI integrations and into Excel exports**. A "High" value in an ATS column is trivially filterable. The architecture permits automated rejection even though the guidance forbids it; nothing in the documentation prevents it.
- **What the employer receives**: score report (no flag) + a **dedicated proctoring section in the report** + project listing + Excel export columns (incl. `Multiple voice detected` Yes/No) + optional ATS pushback of the Proctoring Index. Recruiters can **manually review the captured audio/video snippets** with timestamps.
- **Consequence of a flag:** entirely employer-determined. [PREP-VENDOR] large discrepancies often mean disqualification at top IB / Civil Service — label as estimate.
- **Is the candidate told?** **[VENDOR — likely NOT, during the test]**: *"On Candidate experience there are no visible changes while Audio and Video proctoring are background functions."* No SHL statement located on notifying candidates of a flag or a "Not Verified" outcome afterwards. [INFERRED] The candidate-facing report contains no integrity section at all, so candidates are not informed by SHL; any communication comes from the employer. Notification/consent is pushed onto the client. [UNKNOWN — SHL's consent-capture mechanics and its LL144/GDPR handling of biometric Face Match and audio capture.]

## 2.6 Data forensics / statistical cheat detection
- **Documented:** the Confidence Indicator and its Monte Carlo validation (10,000 simulated candidates, 100 IRT-built tests, cheating = +2SD inflation, ability↔cheating-propensity r = −0.3 per Cizek 1999, "benefits ratio" quantifying detection at cut-scores e.g. 30th vs 70th percentile) [VENDOR-manual, primary — see 01-shl.md].
- **Item-exposure monitoring / known-leaked-item detection:** [UNKNOWN] — no SHL public statement located. Randomised banks + IRT calibration make exposure monitoring technically routine, but SHL does not publish it.
- **Cross-candidate collusion analytics:** **PARTIALLY RESOLVED** — SHL's "Advanced Plagiarism Detection" is described as *"automatic pattern matching across candidate responses and internet content"* [VENDOR, ChatGPT blog]. So cross-candidate matching exists **for constructed-response/text items**. Whether any equivalent answer-string similarity analysis runs on multiple-choice cognitive tests: [UNKNOWN].
- **"Internet content" matching** implies SHL scans for **leaked items circulating online** as part of plagiarism detection — but SHL does not say so explicitly, and does not describe an item-retirement process. [INFERRED, weak].
- **Proctoring Index thresholds** are described as derived from *"internal studies"* and explicitly **not client-alterable**; the studies themselves are unpublished. [VENDOR + UNKNOWN].

## 2.7 AI-era cheating (ChatGPT and successors) — **SHL POSITION FOUND, VENDOR PRIMARY**

### SHL's own study of ChatGPT vs its assessment portfolio
Source: "ChatGPT and Talent Assessment at SHL" (2023) — https://www.shl.com/resources/by-type/blog/2023/chatgpt-and-talent-assessment-at-shl/ (accessed 2026-08-01) [VENDOR]
Companion eBook: "SHL's Exploration of ChatGPT" — https://www.shl.com/resources/by-type/guides-and-ebooks/shls-exploration-of-chatgpt/ (landing page only; **eBook is gated behind a download — quantified findings NOT retrieved**) [UNKNOWN]. Webinar: https://www.shl.com/resources/by-type/webinars/chatgpt-and-the-future-of-talent-assessments/

SHL describes "a large-scale, systematic investigation of SHL assessments to evaluate the potential of AI-based content-generating tools for improving candidates' assessment scores." Headline: **"low to moderate overall impact."** [VENDOR]

**Vulnerability ranking as SHL states it** [VENDOR]:
- **Not susceptible / minimal**: *"Personality and Competency-based assessments were not susceptible to inflated scores from ChatGPT"*; simulations; assessment centre exercises; clerical skills tests.
- **More resistant**: *"Interactive and image-based cognitive tests proved more resistant than text-based reasoning tests."*
- **Measurably impacted**: constructed-response formats and text-based ability/skills tests — though even there ChatGPT produced *"inconsistent and incorrect responses"* to some items.
- Client guidance verbatim in substance: organisations can *"feel confident that most SHL assessment formats can continue to be used without hesitation,"* particularly those with **forced-choice, empirical, simulation, or image-based** elements.

→ [INFERRED, important for a candidate-facing chapter] This is SHL's commercial justification for the **Verify Interactive** (drag-and-drop, image-based) and **OPQ32r forced-choice** designs: they are the formats SHL claims LLMs cannot help with. It also implies the *legacy text-based verbal/numerical* Verify tests are the ones SHL itself concedes are exposed.

**Caveat [INFERRED]:** this study is from **2023**, tested **ChatGPT** as it then was, and is **SHL's own research on SHL's own products**. It is not independent, and multimodal frontier models of 2025–26 handle image-based items far better than the 2023 baseline. Treat the "interactive is safe" conclusion as **dated and vendor-interested**. No updated SHL study for 2024–26 was located. [UNKNOWN]

### SHL's AI-generated-response detector
Source: "Becoming 7X More Efficient in Detecting AI Generated Response" (2023) — https://www.shl.com/resources/by-type/blog/2023/be-7x-more-effective-at-identifying-ai-generated-responses-in-language-assessments/ (accessed 2026-08-01) [VENDOR]
- Method: *"textual pattern matching along with a **custom-trained machine learning classifier**."*
- **The 7x claim, precisely scoped**: the classifier *"helps detect at least 7x more candidates who are using ChatGPT **as compared to only textual pattern matching algorithms**."* → **7x is versus SHL's own prior naive baseline, NOT versus competitors and NOT an absolute detection rate.** Do not restate it as "SHL catches 7x more cheats."
- Study base: *"over **160,000 language assessments (i.e., essays)** from an English-language assessment between **December 2022 and April 2023**."*
- Accuracy claim: *"over **99% accuracy** in distinguishing between AI-generated and human-written text"* on a database of **1 million essays**.
- **Scope limit: this is for WRITTEN LANGUAGE / essay assessments.** It does not apply to multiple-choice or interactive cognitive tests. [VENDOR + INFERRED]
- **False-positive rate: NOT PUBLISHED.** [UNKNOWN] — a >99% accuracy figure on a balanced research corpus says nothing about precision at operational base rates. Given the Kofinas finding below, this is the single most important missing number.
- The 2023 ChatGPT blog listed this detector as *"under development"*; the detection blog reports it operating — [INFERRED] it shipped during 2023.

### SHL's three stated anti-cheating layers (verbatim structure, ChatGPT blog) [VENDOR]
1. **Proctoring Signals** — "detection of copy-paste, screen captures, and browser switching; AI-generated signals monitor face detection and switching." (independently corroborates §2.3/2.4)
2. **Advanced Plagiarism Detection** — *"automatic pattern matching across candidate responses **and internet content**."* → [VENDOR] this IS a **cross-candidate response-matching** capability, partially closing the §2.6 gap: SHL does compare responses *between candidates*, at least for constructed-response items.
3. **AI-Generated Response Detection** — the classifier above.
Plus, per SHL FAQ-level material: *"randomizing question order, using timed conditions, and in some cases, employing remote proctoring or browser monitoring."*

### SHL's platform framing
The detection blog notes SHL's platform uses *"**deterministic and probabilistic** proctoring signals to monitor candidates during assessments"* [VENDOR] — i.e. hard-rule triggers (copy-paste count, print-screen count) alongside statistical/ML signals (voice detection, face match, AI-text classifier, Proctoring Index).

### Independent context (NOT SHL-specific)
- **Context, independent, NOT SHL-specific** [INDEPENDENT]: survey/estimate literature reports large and rising rates of generative-AI use in assessment contexts (figures circulating for 2025 include ~88% of students admitting GenAI use for tests vs ~53% in 2024, and estimates that ~14% openly admit GenAI use in an assessment context against an estimated true rate of 35–42%). **These figures are from third-party/aggregator sources of mixed quality, are about students/general assessment rather than SHL, and should be cited only as context with heavy caveats.** Sources: aiseptor.com/research/ai-cheating-statistics-2026; arxiv.org/pdf/2510.18881 (behaviour-analytics detection of AI-assisted cheating); bera-journals.onlinelibrary.wiley.com/doi/full/10.1111/bjet.13585 (Kofinas et al. 2025, BJET).
- [INDEPENDENT, Kofinas et al. 2025, BJET] Human markers both **false-positived** (flagged genuine work as AI) and **false-negatived** (missed AI-generated work) — the general finding that detection-by-inspection is unreliable, which is why score-comparison designs like SHL's verification test are structurally more defensible than content forensics.
- [INFERRED, structural] SHL's architecture is comparatively resistant to LLM assistance in one specific way: the **verification test** does not attempt to detect AI use at all — it detects *any* unexplained score inflation, whatever its cause (proxy, collusion, LLM, leaked items). A candidate who used an LLM unsupervised and then sits a supervised verification test faces exactly the same +2SD-style discrepancy the model was built to catch. Conversely, **interactive/drag-and-drop item formats** (Verify Interactive) are harder to feed to a text LLM than legacy multiple-choice text items. Neither point is claimed by SHL; both follow from the design.

---

## KEY SOURCES (all accessed 2026-08-01)
**PRIMARY VENDOR (highest value):**
- SHL **Verify Ability Test Report v2.0** sample (employer-facing) — https://service.shl.com/docs/Verify%20Ability%20Report%20v2.0%20English%20International.pdf ✅ fetched & text-extracted
- SHL **Verify Candidate Report (TC Version)** sample (candidate-facing, A–E grades) — https://service.shl.com/docs/Verify%20Candidate%20Report%20(TC%20Version)%20English%20International.pdf ✅ fetched & text-extracted
- SHL **Verify Technical Manual v2.0** (Oct 2007) — https://hrmforce.com/wp-content/uploads/2021/03/Verify-Technical-Manual.pdf (already extracted → research/_shl_manual.txt)
- SHL **Verify Interactive Report** sample (CURRENT product, employer-facing) — https://service.shl.com/docs/Verify%20Interactive%20Ability%20Report%20DNI%20UKE.pdf ✅ fetched & text-extracted
- SHL **Release Notes, 17 July 2025 — "Customized proctoring index"** — https://support.shl.com/documents/1090/attachments/7154 ✅ fetched & text-extracted — **best single integrity source found**
- SHL **Release Notes, 14 July 2023 — Remote Audio & Video Proctoring, Face Match** — https://support.shl.com/documents/935/attachments/4915 ✅ fetched & text-extracted
- SHL blog, "ChatGPT and Talent Assessment at SHL" (2023) — https://www.shl.com/resources/by-type/blog/2023/chatgpt-and-talent-assessment-at-shl/ ✅
- SHL blog, "Becoming 7X More Efficient in Detecting AI Generated Response" (2023) — https://www.shl.com/resources/by-type/blog/2023/be-7x-more-effective-at-identifying-ai-generated-responses-in-language-assessments/ ✅
- SHL eBook "SHL's Exploration of ChatGPT" — https://www.shl.com/resources/by-type/guides-and-ebooks/shls-exploration-of-chatgpt/ ⚠️ gated, landing page only
- SHL webinar "ChatGPT and the Future of Talent Assessments" — https://www.shl.com/resources/by-type/webinars/chatgpt-and-the-future-of-talent-assessments/ [not fetched]
- SHL **Remote Proctoring Guide** — https://talentcentral.learning.shl.com/pluginfile.php/448/mod_resource/content/11/Remote%20Proctoring%20Guide.pdf ❌ HTTP 503 ×2 + TLS-blocked direct download. **RETRY IN GAP AUDIT.**
- SHL Remote Proctoring user-guide page (CN mirror) — https://talentcentralcn.learning.shl.com/mod/page/view.php?id=256&lang=en ❌ HTTP 503
- SHL Verify Candidate Report, US variant — https://service.shl.com/docs/Verify%20Candidate%20Report%20(TC%20Version)%20English%20(US).pdf [not fetched]
- **Method note for future agents:** `support.shl.com/documents/<id>/attachments/<id>` hosts SHL release notes as public PDFs, and `service.shl.com/docs/<Report Name>.pdf` hosts public sample reports. Both are unauthenticated and highly productive. WebFetch cannot parse the PDFs but **saves them to disk** — run `pdftotext -layout` on the saved path.
- SHL Verify G+ Ability Test Report product page — https://www.shl.com/solutions/products/product-catalog/view/verify-g-ability-test-report/ [not fetched]
- Other SHL sample reports discovered (useful for other slices): High-Potential Assessment Report https://service.shl.com/docs/High-Potential%20Assessment%20Report%20Std%20v2.0%20English%20International.pdf ; MQ Profile https://service.shl.com/docs/MQ%20Profile%20(TC%20Version)%20English%20International.pdf ; MQ Motivation Pack https://service.shl.com/docs/MQ%20Motivation%20Pack%20Std%20v2.0%20English%20International.pdf

**PREP-VENDOR (estimates only, biased):**
- careertestprep.com/knowledge/what-is-a-good-shl-score ; /blog/shl-test-scores-explained ; /knowledge/shl-test-results ; /knowledge/shl-cheating ; /knowledge/shl-retake-policy
- jobtestprep.co.uk/shl-test-results and /images/free-pdf/shl-test-results-scores.pdf
- prepclubs.com/blog/shl-general-ability-test-format-and-cutoffs
- assessmentday.co.uk/shl-verify-interactive.htm ; graduatesfirst.com/psychometrics/shl-verify-top-practice-tips-and-examples

**INDEPENDENT (AI-integrity context, not SHL-specific):**
- Kofinas et al. 2025, *BJET* — https://bera-journals.onlinelibrary.wiley.com/doi/full/10.1111/bjet.13585
- "Detecting AI-Assisted Cheating in Online Exams through Behavior Analytics" — https://arxiv.org/pdf/2510.18881

---

## HEADLINE ANSWERS (for the chapter author)

**"How well do I need to do?"** — SHL cannot answer this, by design. Its reports contain **no cut-score, no pass mark, no recommendation** [VENDOR, verified across three sample reports]. It emits percentile + T + sten (+ A–E band on the legacy candidate report) against an **employer-chosen, year-frozen comparison group**, and explicitly tells clients the score *"should be used as part of a broader evaluation."* The threshold is the employer's, is often a **floating top-N rank sift** rather than a fixed cut, and is not published by anyone. The 70th–85th-percentile figures circulating for competitive graduate schemes are **prep-vendor estimates only** and must be presented as such.

**Second-order but decisive:** because items are randomised and IRT-weighted, **raw accuracy ≠ percentile** — SHL states verbatim that *"an individual with a lower hit rate may achieve a higher percentile score and vice-versa."* Chasing "number correct" is the wrong mental model.

**Integrity architecture, in one line:** an opt-in, company-level, per-project **proctoring feature menu** (image/audio/video capture, browser off-focus %, copy-paste and print-screen counts, multi-face detection, AI multiple-voice detection, AI face-match against an ID document) whose threshold breaches roll up into a **Proctoring Index** (High/Medium/Low, moving to High/Low in July 2025) that SHL says is **triage for human review**, pushed into reports, Excel exports and the ATS — layered over the older, better-evidenced **verification-test + Confidence Indicator** psychometric backstop, which appears to have been dropped from the current Verify Interactive range.

---

## RESIDUAL GAPS
1. **SHL Remote Proctoring Guide PDF** — 503 twice. Would confirm the full feature list and the admin-side combined proctoring report. (Much of what it would have said is now covered by the release notes.)
2. **Proctoring Index thresholds** — SHL states they exist, are study-derived, and are not client-alterable, but publishes **no numbers** and no study. Highest-value remaining unknown on the integrity side.
3. **False-positive rate of the AI-response classifier** — SHL claims >99% accuracy on a research corpus; operational precision unpublished. Critical, because a false AI-cheating flag is career-damaging.
4. **SHL's own cut-score guidance to employers** — not on open web; likely client-portal / consulting only. Nothing SHL-sourced on criterion- vs norm-referenced cut-scores, banding rules, or multi-hurdle vs compensatory batteries.
5. **The ~70 comparison-group catalogue** — no published list. Current-product group names are now known (§1.2) but the full catalogue, and whether a "Finance Graduates" group exists, remain prep-vendor-only.
6. **A–E band → percentile boundaries** — SHL prints the band but not the cut points. The 10/20/40/20/10 split is a plausible convention, **NOT verified**.
7. **Pass rates / sift severity** — nothing published; do not estimate.
8. **Confirmation that the Verification Test is genuinely discontinued for Verify Interactive** — currently inferred from its absence in the Interactive sample report (§1.3c). Needs a direct SHL statement or product-catalogue check.
9. **Any post-2023 SHL research on frontier multimodal LLMs vs Verify Interactive** — the "image-based tests are resistant" claim is a 2023 finding against 2023 ChatGPT and is likely stale.
10. **Cross-candidate matching on multiple-choice cognitive tests** (plagiarism detection is documented only for constructed-response/text) and any leaked-item / item-retirement process.
11. **Candidate consent and disclosure mechanics** for invisible audio/video capture and biometric Face Match — GDPR/UK-GDPR and NYC LL144 exposure; no SHL statement located.
12. **Whether the "Proctoring Index → ATS" pipeline is used for automated rejection in practice** — architecturally possible, contrary to SHL's stated guidance, unevidenced either way.
13. **TalentCentral vs TalentCentral+ split** — the 2025 Proctoring Index ships to **TalentCentral+ only**. Which platform a given UK graduate employer is on materially changes what integrity tooling exists. Unmapped.
