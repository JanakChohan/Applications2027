# 32 — Aon/cut-e: Personality & Motivation Instruments, vidAssess, Integrity Architecture — Raw Findings

**Researched:** 2026-08-01 (dedicated deep-dive slice). Builds on `02-aon-cute.md` — does not repeat scales/smartPredict mechanics.

**Key primary sources landed this pass:**
1. **cut-e Baltic official vendor deck** "Online Assessment with cut-e" (61-page PDF, cut-e branded, pre-2017-acquisition era), hosted at https://lpva.lv/storage/files/ZG9zRZObPYCKakdB5niVwOQjJBCeaj9EngDq0kl1.pdf — full text extracted. [VENDOR — legacy but authoritative on design philosophy]
2. **ACLU Model Cards for gridChallenge, ADEPT-15 and vidAssess-AI** (Oct 2024, built from Aon's own technical documentation cited in ACLU's FTC complaint): https://assets.aclu.org/live/uploads/2024/10/Model-Cards-for-gridChallenge-ADEPT-15-and-vidAssess.pdf — full text extracted. [INDEPENDENT — critical/adversarial but sourced to Aon technical docs]

---

## PART 1 — Personality / motivation instruments

### 1.1 shapes (adaptive personality questionnaire)

**Format & mechanics**
- Each questionnaire page presents a block of **3 statements**; candidate **allocates 6 points across the 3 statements** to weight how well each describes them. This is cut-e's **adalloc™** ("Adaptive Allocation of Consent") measurement technology — statements grouped into blocks of three, "differently weighted by the candidate". [VENDOR: cut-e deck + cut-e.de search snippet; PREP-VENDOR: psychometrictests.org agrees]
- **Adaptive personality — how:** which statements are grouped together on later pages depends on responses to earlier items ("statements are presented together based on the responses to earlier items by the test taker" — Aon shapes(management) product page snippet). adalloc thus adaptively pairs/blocks statements to sharpen discrimination between traits the candidate rates similarly, allowing "a highly sophisticated profile … with a very short questionnaire". [VENDOR]
- Also uses **random item selection** from the item pool (per deck: "random item selection and adalloc™ measuring technology") — so even the personality questionnaire has per-candidate item variation, contra the earlier note in 02 that only ability tests randomise. [VENDOR — deck, "shapes characteristics" slide] (02 file said personality/SJT excluded from unique-item generation [PREP-VENDOR]; conflict → vendor deck is more authoritative; record both.)
- **Timing:** approx. **15–20 min** (deck); prep vendors say 10–15 min for graduate variant. Untimed in the hard sense (no per-item clock). [VENDOR / PREP-VENDOR]
- Self-description ("based on self description; covers relevant behaviours, potentials and competences; various dimensions with at least six to eight items/statements each; up to 18 competences"). [VENDOR deck verbatim]

**Variants — VERIFIED from vendor deck (definitive list, 6 variants):** [VENDOR]
| Variant | Scales | Items/scale | Optimised for |
|---|---|---|---|
| shapes **basic** | **15** | 6 | administrative staff & apprentices; no management scales; no degree needed |
| shapes **graduate** | **18** | 6 | graduates; no management experience required |
| shapes **sales** | **24** | 6 | sales/direct customer contact |
| shapes **expert** | **18** | 8 | specialists without management/sales responsibility; no management scales |
| shapes **management** | **18** | 8 | middle/senior management behaviour & potential |
| shapes **executive** | **24** | 8 | senior management |
- Confirms brief's "~18 traits for graduates" ✓ and the basic/graduate/management/expert set ✓ (plus sales & executive).
- shapes(management) dimension examples from deck (grouped interaction/operational/emotional/intellectual): Influence, Networking, Execution, People development, Systematic approach, Constructive teamwork, Vision and strategy, Initiative and responsibility, Organizational awareness, Steadiness, Bottom-line focus, People management, Effective communication, Analysis and Judgement, Professional expertise, Innovation, Self development, Business development. [VENDOR deck]

**Scoring & authenticity logic**
- Output = trait profile matched against a role/"ideal candidate" competency profile chosen by the employer; no absolute pass/fail. [PREP-VENDOR: psychometrictests.org; VENDOR structure]
- The ipsative-ish 6-points-across-3 format forces trade-offs (cannot rate everything "very me"), which is the built-in social-desirability control; the adaptive re-pairing of statements repeatedly re-tests the same traits in new combinations, making a consistent faked profile hard to maintain. [INFERRED from format; vendor markets adalloc as precise + low-dropout rather than explicitly as anti-faking]
- Explicit consistency/faking index in shapes reports: [UNKNOWN — not found in accessible documentation; deck's shapes slides don't name one]
- One prep source: candidates warned not to distort because "they might get further questions at a later stage for verification" (i.e., interview probing / assessment-centre follow-up). [PREP-VENDOR via search snippet, graduatesfirst-family]
- **Winning approach (authenticity logic):** consistent self-presentation targeted at the role's competency model; because scoring is profile-match, "high on everything" is impossible by design — points are zero-sum per page. Answer with a stable persona; wild point-splitting across pages produces incoherent trait estimates. [INFERRED]
- **shapes360 / snap-it:** deck shows a shapes360 multi-rater competency model and "snap-it" tool using "the validated shapes competency model". [VENDOR — exists; details thin]

### 1.2 views (values / motives / interests)
- **Purpose:** measures occupationally relevant **values, motives and interests** for person–culture fit (company/department/team). [VENDOR]
- **Model:** **18 characteristics in 3 areas** — **Objectives** (Professional challenge, Recognition of performance, Financial reward, Development opportunities, Fun while working, Identification), **Relationships** (Harmony, Honesty, Cooperativeness, Security, Fairness, Hierarchy), **Environment** (Structuring, Rate of change, Integrity, Absence of stress, Influence possibilities, Working environment). [VENDOR deck — verbatim slide]
- **Format:** 18 characteristics × 6 items = **108 items, in blocks of 3 = 36 questionnaire pages**; same adalloc 6-point allocation; **15–20 min** (prep sources say 10–20). [VENDOR deck]
- **Scoring:** "preferences profile" report; matched to employer culture/values profile. No right answers; fit-based. [VENDOR]
- Adaptive via adalloc like shapes ("basis views is an adaptive questionnaire system"). [VENDOR: cut-e.de snippet]

### 1.3 motive.q / "drives"
- 02 file: Deutsche Bank used scales numerical/verbal + **motive.q**. [PREP-VENDOR, repeated across guides]
- One prep snippet: "Unlike aptitude tests, **motive.q is assessed against a role-specific profile** — the ideal score depends on what the employer is hiring for." [PREP-VENDOR: psychometrictests.org-family]
- motive.q not present in the cut-e Baltic core-products deck (which lists shapes, views, squares, scales…) — suggests motive.q was a separate/regional or later-added motivation questionnaire. Relationship to any Aon "drives" product: **[UNKNOWN — no evidence found of a current 'drives' product; treat motive.q as legacy cut-e motivation questionnaire still deployed at some clients (e.g. Deutsche Bank per prep vendors)]**
- Current-catalogue status (2026): [UNKNOWN — Aon product sites unreachable from this environment; prep vendors still describe it for Deutsche Bank]

### 1.4 ADEPT-15 (Aon-owned, US lineage)
- **Model:** 15 personality "aspects" — 10 mapping to the Five-Factor Model + 5 leadership-relevant additions — grouped into **6 higher-order "styles": Task, Adaptation, Achievement, Interaction, Emotional, Teamwork**. Aspect names include Awareness, Positivity, Liveliness, Sensitivity, Drive. [VENDOR: aonhumancapital.co.in; INDEPENDENT: ACLU model card citing Aon technical documentation]
- **Format:** computerized **adaptive** test (CAT). Items are **pairs of statements**; candidate indicates **which statement they agree with more and how strongly** (slider between the pair — matches the ~100-pair slider description in 02). ~**25–30 min** (ACLU card citing Aon); prep vendors say ~20–30, usually untimed. [INDEPENDENT + PREP-VENDOR]
- **Version:** ADEPT-15 **Version 7.1 (2022-11-11)** was the version in Aon's technical documentation reviewed by ACLU. [INDEPENDENT]
- **Scoring (deep):** multidimensional forced-choice pairs scored with **IRT models: MUPP (Multi-Unidimensional Pairwise Preference) and GGUM (Generalized Graded Unfolding Model)**; the adaptive algorithm selects subsequent statement pairs based on prior responses. [VENDOR technical documentation, corroborated by search across academic + Aon India sources]
- **Faking resistance claims:** forced-choice between (desirability-matched) statements removes central-tendency and social-desirability response styles; CAT delivery "enhances accuracy and security and mitigates socially desirable responding"; vendor positions it as substantially harder to fake than Likert instruments. [VENDOR claim; the forced-choice→faking-resistance link has independent-literature support in general (meta-analysis PMC8511514) but that is about the format class, not ADEPT-15 specifically]
- **Explicit social-desirability/consistency index:** technical documentation reportedly covers response-process modelling; a named lie/SD scale: [UNKNOWN — not confirmed; the design position is that the format itself is the control]
- **Output:** scores on all 15 aspects, or employer-configured subset; can be aggregated with other assessments (e.g. gridChallenge) into composite ranks. [INDEPENDENT: ACLU citing Aon docs]
- **Criticism / fairness (conflict record):** ACLU FTC complaint (2024) alleges ADEPT-15 constructs are "closely tied to characteristics commonly associated with autism and mental health diagnoses"; that Aon's claims of "bias-free", "no adverse impact" are overstated; and that technical documentation shows no autism/mental-health-specific mitigation. Aon marketing claims the opposite ("developed from the ground up" for "minimal" demographic differences incl. disability). Both positions recorded. [INDEPENDENT (ACLU) vs VENDOR — unresolved; the technical documentation itself was withdrawn from public availability per ACLU footnote]
- Technical documentation PDF: was public ("ADEPT-15 Technical Documentation", copy visible on Course Hero: https://www.coursehero.com/file/148035925/ADEPT-15-Technical-Documentationpdf/); no longer published by Aon. [INDEPENDENT/ACLU footnote]

---

## PART 2 — vidAssess-AI

- **Question setup:** up to **10 fully customizable questions** — content, **recording time and number of retries all set per-question by the employer**; questions presented sequentially. Question pool of 600+ available (from 02). [VENDOR: aonhumancapital.com.au / aon-assessment-solutions.com snippets; PREP-VENDOR]
- **Scoring pipeline (confirmed, deepened):** (1) **speech-to-text** transcription of the spoken answer; (2) **NLP AI scores the transcript** — "scans the words spoken" and scores per competency area. **No facial analysis** — explicitly speech/text-only (confirms 02's stance). [VENDOR]
- **What the NLP scores against (key finding):** per ACLU model card citing Aon docs — **vidAssess-AI relies on ADEPT-15's personality model**. Employers' questions are mapped to specific ADEPT-15 constructs, and the NLP **associates words/phrases in the transcript with those personality constructs** (technical documentation pp. 89–97 per ACLU citations). So the AI layer is effectively a language-based ADEPT-15 construct scorer, not a generic "answer quality" grader. [INDEPENDENT — ACLU citing Aon technical documentation; strongest single fact in this section]
- **Human review:** AI scoring "assists" — positioned as decision support; scores "reported back to employers in a variety of formats"; recruiters can review the recorded videos themselves (asynchronous review model). Explicit human-in-the-loop requirement: [UNKNOWN — configurable by employer; vendor markets both AI-scored and human-scored competency-based use ("vidAssess" classic was competency-based video interviewing without AI, per cut-e deck)]. [VENDOR + INDEPENDENT]
- **Retake rules:** number of attempts per question is an **employer setting** ("amount of retries… completely customizable"); no universal retake right. [VENDOR]
- **Fairness claims/conflict:** Aon markets it as "fair", "minimiz[ing] human bias"; ACLU counters that speech-to-text/NLP systems perform measurably worse for Black speakers, non-native English speakers, and speakers with speech/other disabilities, so the pipeline risks amplifying ADEPT-15's alleged issues. [VENDOR vs INDEPENDENT — record both]
- Patent: Aon LinkedIn describes vidAssess-AI as "patented". [VENDOR marketing]

---

## PART 3 — Anti-cheating / integrity architecture (flagship)

### 3.1 Unique-per-candidate item generation [VENDOR — primary]
- cut-e deck, instrument principles slide, verbatim bullets: instruments are **"forgery-proof"** via:
  - **"item generation"** — items generated (rule-based/parameterised), not drawn from a small static bank;
  - **"individual parallel versions (sample solutions do NOT exist!)"** — every candidate gets a psychometrically parallel but different test, so leaked answer keys are useless;
  - **"adalloc™ measuring technology"** (questionnaires).
- scales marketing slide: **"Cheat-proof — our unique technology ensures that a different test is generated for each participant."** [VENDOR verbatim]
- playAssess slide repeats it: "Built from randomised questions, the presented assessment is different for each candidate." [VENDOR]
- Even shapes uses "random item selection" (see 1.1) — item-level randomisation extends into personality, though there the goal is bank security rather than answer-key defeat. [VENDOR]
- Vendor framing: parallel-form generation is the PRIMARY integrity control for unsupervised online testing; proctoring is secondary/optional. [VENDOR + INFERRED]

### 3.2 Extreme time pressure as anti-cheat design
- Vendor rationale (deck): "Short timed tests. A reliable and valid test result after only 15 minutes"; more-items-than-time formats mean a helper/friend or lookup adds little because throughput-under-pressure is the measured construct. Explicit vendor statement that time pressure is FOR anti-cheating: [not stated verbatim in accessible docs — the deck sells it as efficiency/reliability; the anti-collusion effect is prep-vendor/inferred]. [VENDOR (short-test rationale) + INFERRED/PREP-VENDOR (anti-cheat effect); 02 file's stronger claim stands as PREP-VENDOR-consistent]

### 3.3 Webcam proctoring — Aon "Virtual Proctoring" (FULL flyer extracted) [VENDOR — primary]
Source: Aon flyer "Virtual proctoring: verifying candidates who complete an assessment" (ref C1286INT, dated 01.21), https://hcc.icappeoplesolutions.com/wp-content/uploads/2022/05/FLY_Virtual-Proctoring_INT_7562-web.pdf — full text extracted.
- **How it works (4 steps, verbatim workflow):** (1) **Consent agreement** — candidate asked to consent to proctoring; (2) **Reference photo** captured; (3) **"Protecting"** — further webcam **photos captured throughout the assessment** (periodic snapshots, NOT continuous video); (4) **Rating** — "the system identifies any inconsistencies or discrepancies between photos" → AI-flagged photo comparison, i.e. identity-continuity checking ("'Eye in the Sky' technology… confirms that it is the same individual test taker throughout").
- **Also monitors navigation:** virtual proctoring "spots those who may be accessing other sites when completing the assessment" — and the flyer's own study stats prove Aon measures **active-test-window switching even in UNPROCTORED sittings** (see below). This closes 02's telemetry gap: **tab/window-switch telemetry exists platform-wide.** [VENDOR]
- **Employer controls:** quick to activate; mobile-enabled; employer "decide[s] whether or not to mandate verification — whether candidates must accept proctoring or if they are able to opt out — and what happens next." So opt-out and consequences are employer policy, not Aon policy. [VENDOR]
- **Compatibility limit:** "cannot be added to those assessments which already access the device's camera, such as vidAssess." [VENDOR verbatim]
- **Aon internal research (n>30,000 students) [VENDOR study, self-reported]:**
  - moderate cheating likelihood (per Eye-in-the-Sky ratings): **6.52% unproctored vs 2.25% proctored**
  - high cheating likelihood: **0.07% unproctored vs 0.02% proctored**
  - switched away from active test window ≥1×: **19.4% unproctored vs 12.3% proctored**
  - (Note the deterrence framing — proctoring roughly halves flagged behaviour. Also note base rates are low; and "reported to have a likelihood of cheating" is an algorithmic rating, not confirmed cheating → inherent false-positive surface, unquantified. [INFERRED])
- **Candidate notification:** consent is explicit and up-front (step 1); "candidates are aware that the selection process is being monitored" — deterrence is a stated benefit. [VENDOR]
- Not default: most deployments unproctored (02, PREP-VENDOR consistent). Flyer positions it as a COVID-era add-on for unsupervised-at-scale hiring. [VENDOR/INFERRED]

### 3.4 Retest / verification model — CONFIRMED
- cut-e deck, verbatim bullet under instrument security: **"onsite re-test for verification is possible."** [VENDOR — primary confirmation of the historical claim in the brief]
- Mechanism: because parallel forms are generated per sitting, a short supervised retest at the assessment centre can be compared with the online score; item generation guarantees the retest is a fresh form. [VENDOR design + INFERRED mechanics]
- Whether Aon currently productises this as a formal "verification test" à la SHL (auto flag + statistical comparison report): [UNKNOWN — no current-era documentation found; historically advocated, technically supported by parallel forms]
- Prep-vendor echo: distorted answers "might get further questions at a later stage for verification". [PREP-VENDOR]

### 3.5 Data forensics / platform rules (mapTQ)
- maptq.com direct fetch: not achieved this pass (domain reachable status [UNKNOWN]); rules below are prep-vendor renderings of candidate-facing guidance:
  - **No pausing** once a test starts. [PREP-VENDOR: practiceaptitudetests.com/jobtestprep]
  - **Calculators allowed in some assessments; "in case calculators are not allowed, you'll be informed."** [PREP-VENDOR quoting candidate instructions]
  - Stable internet + current browser required; smartphone/tablet compatible but PC/laptop recommended; interactive instructions/examples precede every test. [PREP-VENDOR]
- Statistical/response-pattern cheat detection claims (post-hoc data forensics à la Caveon): [UNKNOWN — no Aon claims found beyond the Eye-in-the-Sky photo-inconsistency ratings in 3.3]
- **Window-switch telemetry: CONFIRMED** — Aon's own proctoring flyer reports % of candidates who "switched away from the active test window" in both proctored AND unproctored settings, so the platform logs window/tab focus regardless of proctoring (see 3.3). [VENDOR]
- IP/device checks, clipboard telemetry: [UNKNOWN — still undocumented]
- Compliance/security posture (deck, legacy): DNV certification under the **International Test Commission framework**; exceeds **DIN 33430**; **ISO 27001/27002** certified; data processing under German BDSG §11; registered with Diagnostik- und Testkuratorium (DTK). [VENDOR — pre-GDPR era deck; see Part 4]

### 3.6 Consequences, flags, candidate notification
- What employer sees on suspected cheating / whether candidate is told: [UNKNOWN — no documentation found]
- Aon's structural answer is preventive (parallel forms) + verification retest rather than detection-and-accusation. [INFERRED from vendor materials]
- False-positive documentation: none found for cut-e/Aon integrity flags. The adjacent documented fairness dispute is the **ACLU FTC complaint (2024) + EEOC charges** re gridChallenge/ADEPT-15/vidAssess-AI discrimination (disability, race) — about construct fairness, not cheat flags. [INDEPENDENT]

### 3.7 squares — dedicated integrity test (bonus finding)
- cut-e also sells **squares**, an **integrity test**: online screening to "reduce the probability of counterproductive work behaviour", esp. security/risk-heavy jobs; also used for tenure prediction, safety, development. [VENDOR deck] — i.e., "integrity" at Aon means both platform anti-cheat AND a CWB-prediction instrument; don't conflate in the report.

---

## PART 4 — Adjustments, data protection, technical documentation

- **Accessibility (legacy vendor claim):** instruments are **"barrier-free"**, "based on the Equal Opportunities Act for Information Technology" (German BITV); hardware-independent vector graphics. [VENDOR deck]
- **Extra time / adjustments (current era):** Aon provides accommodations "like screen magnifiers for visual impairments and **extra time for individuals with dyslexia**", evaluated **case-by-case** (per LinkedIn article by an Aon work-experience author describing Aon's tools + Aon candidate-prep page at https://www.aon.com/en/capabilities/talent-and-rewards/prepare-for-your-online-assessment). Requests route via the employer/recruiting team. Implementation specifics (multiplier vs untimed): [UNKNOWN]. [VENDOR-adjacent + PREP-VENDOR; weak sourcing — verify against Aon candidate-prep page directly in a later pass]
- **UK GDPR:** current Aon Assessment privacy documentation not fetched (site unreachable); legacy posture: German data-protection law + ISO 27001/27002 (above). [VENDOR-legacy; current-era [UNKNOWN]]
- **Validity/technical documentation:**
  - Legacy cut-e: "standardisation and validation study with universities and partners"; continuous research programmes; 40 languages, translations culturally validated by local psychologists. [VENDOR deck]
  - **ADEPT-15 Technical Documentation v7.1** existed publicly, now withdrawn; contents partially reconstructed in ACLU FTC complaint & model cards (validity process, adverse-impact analyses — incl. reported race disparities on gridChallenge where "non-white assessment takers all scored lower than white… largest disparity for Black or African American test-takers", Aon's own tech doc p. 57). [INDEPENDENT citing VENDOR docs]
  - **cut-e Assessment Barometer** (global recruitment-trends survey cut-e ran periodically): referenced in brief; not located this pass — [UNKNOWN/not verified].
  - **BPS test reviews of shapes/scales:** not located in accessible sources (BPS PTC reviews are paywalled/registration) — [UNKNOWN]. cut-e deck notes DNV/ITC certification which in Europe often substitutes for BPS review. [VENDOR]

---

## SOURCES (all accessed 2026-08-01)
**Vendor / primary**
- cut-e Baltic deck "Online Assessment with cut-e" (61pp PDF): https://lpva.lv/storage/files/ZG9zRZObPYCKakdB5niVwOQjJBCeaj9EngDq0kl1.pdf — text-extracted; verbatim quotes above [VENDOR]
- Aon shapes (management) product page (snippet only, site unreachable): https://www.aon-assessment-solutions.com/nc/us/details/shapes-management-work-related-behavior/ [VENDOR]
- Aon vidAssess-AI pages (snippets): https://www.aonhumancapital.com.au/vidassess-ai ; https://www.aon-assessment-solutions.com/nc/us/details/video-interviewing-augmented-with-ai-vidassess/ [VENDOR]
- Aon ADEPT-15 (India): https://www.aonhumancapital.co.in/home/for-employers/assessment-solutions/leadership-assessments/adept [VENDOR]
- Aon virtual proctoring flyer (C1286INT 01.21, via ICAP mirror): https://hcc.icappeoplesolutions.com/wp-content/uploads/2022/05/FLY_Virtual-Proctoring_INT_7562-web.pdf — FULL TEXT EXTRACTED [VENDOR — primary for 3.3/3.5]
- Aon candidate prep page: https://www.aon.com/en/capabilities/talent-and-rewards/prepare-for-your-online-assessment [VENDOR — snippet only]
- cut-e.de questionnaire pages (snippets; cut-e.com DNS dead): https://www.cut-e.de/online-assessment/frageboegen-zur-persoenlichkeit/ [VENDOR]

**Independent**
- ACLU Model Cards (gridChallenge / ADEPT-15 / vidAssess-AI), Oct 2024: https://assets.aclu.org/live/uploads/2024/10/Model-Cards-for-gridChallenge-ADEPT-15-and-vidAssess.pdf — full text extracted [INDEPENDENT]
- ACLU Complaint to the FTC Regarding Aon Consulting, Inc. (referenced therein) [INDEPENDENT]
- Forced-choice faking-resistance meta-analysis (format-level): https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8511514/ [INDEPENDENT]

**Prep-vendor**
- psychometrictests.org cut-e: https://www.psychometrictests.org/publishers/cut-e/ — fetched [PREP-VENDOR]
- practiceaptitudetests.com cut-e: https://www.practiceaptitudetests.com/testing-publishers/cut-e/ [PREP-VENDOR]
- jobtestprep.co.uk maptq: https://www.jobtestprep.co.uk/maptq-test ; cut-e personality: https://www.jobtestprep.co.uk/cut-e-personality-integrity/ [PREP-VENDOR]
- graduatesfirst Aon guide: https://www.graduatesfirst.com/aon-cut-e-practice-assessments [PREP-VENDOR]
- ADEPT-15 Technical Documentation copy (Course Hero): https://www.coursehero.com/file/148035925/ADEPT-15-Technical-Documentationpdf/ [VENDOR doc, unofficial mirror]

**Dead/blocked this pass:** cut-e.com (ENOTFOUND), aon-assessment-solutions.com (ENOTFOUND), aptitudetests.org (403), m.moam.info views brochure (503), maptq.com (not attempted/unreachable status unknown).

## RESIDUAL GAPS ([UNKNOWN] summary)
- shapes named consistency/faking index; motive.q current catalogue status & scale model; ADEPT-15 named SD index.
- mapTQ first-party candidate FAQ text; IP/device/clipboard telemetry; post-hoc data-forensics claims; what a "moderate/high cheating likelihood" flag looks like in the employer report and whether the candidate is told of a flag; false-positive cases (none documented — the flyer's algorithmic "likelihood" ratings imply an unquantified false-positive surface).
- Current UK GDPR notice; adjustment request mechanics; Assessment Barometer; BPS reviews.
