# 04 — Pymetrics (now part of Harver): RAW RESEARCH DUMP

> Raw sourced findings for book sections 5.1–5.13. NOT polished prose. Every claim tagged.
> Access date for ALL URLs below: **2026-08-01**.
> Evidence tags: `[VENDOR]` = pymetrics/Harver's own words · `[INDEPENDENT]` = academic/press/regulatory · `[CANDIDATE, n=X]` = forum/candidate testimony · `[PREP-VENDOR]` = test-prep sites (commercial, treat sceptically) · `[INFERRED]` = my reasoning shown · `[UNKNOWN]` = gap + why + proxy.
> STATUS NOTE: "pymetrics" is now a **product line inside Harver** (see §1). Brand persists as "pymetrics" / "pymetrics Soft Skills Platform" / "Game-Based Assessments by pymetrics". Standalone company pymetrics.ai largely folded into harver.com. Flag current-vs-legacy throughout.

---

## 1. OWNERSHIP / CORPORATE / WHAT IT IS

### Corporate lineage & acquisition
- pymetrics founded **2013** by **Frida Polli** (neuroscientist, ex-Harvard/MIT postdoc) and **Julie Yoo**. `[INDEPENDENT]` (Northeastern audit whitepaper §3, cbw.sh; superset.com founder profile). URL: https://cbw.sh/static/audit/pymetrics/pymetrics_audit_result_whitepaper.pdf
- Corporate chain: **Outmatch acquired Harver (May 2021)**, then the combined company **rebranded to "Harver" in late 2021**; **Harver then acquired pymetrics, completion announced 11 August 2022.** `[INDEPENDENT]` (PRNewswire/Yahoo/RecruitingDaily/HCM Technology Report, all Aug 2022). URLs:
  - https://www.prnewswire.com/news-releases/harver-acquires-pymetrics-further-enhancing-talent-decision-capabilities-across-the-employee-lifecycle-301603823.html
  - https://harver.com/harver-acquires-pymetrics/
  - https://recruitingdaily.com/news/harvers-acquisition-of-pymetrics-will-offer-wider-deeper-product-line/
- **Deal terms NOT disclosed.** `[UNKNOWN]` — no public purchase price in any press release. Proxy: pre-acquisition pymetrics raised ~$56.6M+ (Series A/B, Khosla Ventures $2.5M seed 2014 per TechCrunch). `[INDEPENDENT]`
- Executive quotes at acquisition `[VENDOR]`:
  - Scott Landers (Harver CEO): "An organization's people are the most essential and strategic part of the business. Together, we will help enterprises maximize the potential of their employee base."
  - Frida Polli (pymetrics CEO/Founder): "We have an incredible opportunity to reinvent the way talent decisions are made by creating a more effective and unbiased process across the talent lifecycle."
- Branding post-acquisition: product integrated as **"pymetrics for Game-Based Assessments"** / **"pymetrics Soft Skills Platform"** within Harver suite; retains "distinct identity". `[VENDOR]` (harver.com/harver-acquires-pymetrics/). The 2025 LL144 audit still names the tool **"Harver's Soft Skills Platform"** internally = the pymetrics engine. `[INDEPENDENT]` (BABL AI audit 2025).
- **Brand-persistence answer for §5.1:** YES, "pymetrics" name is still used candidate-facing and in Harver marketing as of 2025. Legacy domain pymetrics.ai still resolves for some content; harver.com is primary. `[INFERRED]` from vendor pages carrying both names.

### What it is / what it measures
- A **game-based (gamified) behavioral pre-employment assessment**: candidate plays a suite of short neuroscience-derived games; ~**thousands of behavioral data points** ("over a thousand" per GraduatesFirst) are captured and reduced to **traits**. `[VENDOR]`/`[PREP-VENDOR]`
- Trait-count claims VARY by source (flag inconsistency):
  - "**91 social, cognitive, and behavioral traits**" — JPMorgan-focused prep sources. `[PREP-VENDOR]`
  - "**49 different key cognitive and emotional traits**" — earlier press. `[INDEPENDENT]` (thedp.com 2014, legacy figure)
  - "up to ~**90 traits**" — psychometric-success. `[PREP-VENDOR]`
  - Northeastern audit: the audited SVM code used **64 features** (traits), final model **44–45 features**. `[INDEPENDENT]` (FAccT paper §3.2)
  - `[INFERRED]`: "traits" (marketing) ≠ "features" (model). Raw games emit ~60–90 candidate features; a fitted model keeps ~44–56. Use "~90 measured, subset modelled" framing.
- Candidate-facing **9 core trait families** shown in results: **Effort, Risk, Fairness, Emotion, Decision Making, Focus, Learning, Attention, Generosity.** `[PREP-VENDOR]` (Lumovest JPM guide)

### Stage & duration in UK finance
- **Stage:** very early screen — typically **after online application / before or alongside HireVue video + numerical tests**, pre-assessment-centre. `[PREP-VENDOR]` (GraduatesFirst, CareerTestPrep JPM)
- **Duration:** **~25–30 min** (sources give 20–35 min range; ~12 games at 1–3 min each). `[VENDOR]` "25 Minutes to complete" (harver.com/gamified-assessments); `[PREP-VENDOR]` 25–35 min.

---

## 2. WHY IT EXISTS / THE CONSTRUCT / VALIDITY

### Construct
- Games "derived from peer-reviewed psychological studies" and "purported to assess **intrinsic mental qualities**"; "not meant to be won or lost, but rather to surface information about players based on how they play." `[INDEPENDENT]` (audit whitepaper §3.1, direct quote)
- Measures a mix of **cognitive** (memory, attention, learning rate, processing speed, planning) and **emotional/social** (risk under uncertainty, altruism, trust, fairness, emotion recognition, effort allocation) traits. `[VENDOR]`/`[INDEPENDENT]`
- Vendor construct framing: "soft skills" — adaptability, attention, decision-making, risk tolerance, effort, focus, learning, fairness, generosity, emotion. `[VENDOR]` (harver.com/gamified-assessments)

### Predictive validity evidence
- Vendor claim: ">90% accuracy in trait identification", "98% completion rate". `[VENDOR]` — NOTE these are engagement/measurement claims, NOT criterion validity vs job performance.
- **Validation studies are largely CONFIDENTIAL.** Northeastern auditors were shown "a confidential presentation containing results from game validation studies [Baker 2019, Games, Measures and Factors: Measurement Validity]" and explicitly **"encourage pymetrics to make these results public."** `[INDEPENDENT]` (audit §6.3) — i.e., independent published criterion-validity evidence is THIN. `[UNKNOWN]` gap: peer-reviewed job-performance predictive validity. Proxy = the confidential Baker (2019) deck + client-side longitudinal back-testing pymetrics runs but doesn't publish.

### Critiques of the construct
- Northeastern team EXPLICITLY did NOT validate the games: "We did not investigate the ability of pymetrics' games to measure human capabilities, whether those capabilities map to job performance, or whether other assessment methods would be superior." `[INDEPENDENT]` (audit §4.2) — important: the famous "audit" validated FAIRNESS PLUMBING, not that the games predict performance.
- "Drawing a direct line from laboratory experiments to real-world job performance is challenging." `[INDEPENDENT]` (audit §6.3)
- Candidate/practitioner critique: assessment "attempts to force intangibles about a person into data points and introduces confusion into the hiring process." `[CANDIDATE, n=unclear]` (WSO thread summary — see §11 gap note; thread returned 403, sentiment via search snippet only)

---

## 3. WHY A FIRM PICKS PYMETRICS — BIAS REDUCTION + BESPOKE MODEL

### Central selling point
- Core pitch = **proactive de-biasing / removal of adverse impact** + a **bespoke model built from the client's OWN top performers**. "One of the core assertions pymetrics makes… is that they pro-actively de-bias ML models before deployment to comply with the U.S. Uniform Guidelines on Employee Selection Procedures (UGESP)." `[INDEPENDENT]` (audit Exec Summary)
- Marketing: "Validated for fairness across gender, ethnicity, and socioeconomic status"; "nonverbal and intuitive, minimizing cultural and language bias"; "fit, not background"; co-founded by "a neuroscientist and AI ethicist". `[VENDOR]` (harver.com/gamified-assessments)

### Success-model-building process (the mechanic behind the pitch)
6-step client engagement `[INDEPENDENT]` (audit §3, FAccT §3 — DIRECT, authoritative):
1. Employer ("client") contracts pymetrics to build a predictive model for a target role.
2. A pymetrics **job analyst** surveys the client on the role (job description, seniority) + the metrics the client uses to judge performance.
3. Client has **incumbent employees in that role play the games** + supplies their **existing job-performance data**. This = the **labelled training data**.
4. A pymetrics **data scientist** builds the model (in a template Jupyter notebook) → trains, tests for adverse impact.
5. Best-performing model that PASSES fairness is deployed. Applicants play games; model predicts who resembles high-performing incumbents; high scorers passed to client.
6. Pymetrics does **longitudinal back-testing** post-deployment on real applicant pool + hired-cohort performance.

### CORE vs CUSTOM algorithm distinction (§5.5 key differentiator)
- **CUSTOM (bespoke) model:** built from a specific client's incumbents. **In-group typically 50–100 incumbent players.** `[INDEPENDENT]` (FAccT §3.2 DIRECT: "The in group dataset typically contains data on 50–100 players.")
- **CORE model:** a standardised/generic model used when a client lacks enough incumbents or wants a general-fit screen. The **12 games are identical** whether applying to a warehouse or a finance desk — only the MODEL/benchmark differs. `[PREP-VENDOR]`/`[INFERRED]` (search corroboration; exact pymetrics "core model" spec is proprietary). `[UNKNOWN]` precise minimum-incumbent cutoff to qualify for custom vs falling back to core — 50 is the cited floor. Proxy = FAccT "50–100 players".
- Three datasets in training `[INDEPENDENT]` (FAccT §3.2):
  - **in group** = high-performing incumbents (50–100).
  - **out group** = random sample from pymetrics' historical player database, approximating the applicant pool (used as contrast).
  - **bias group** = players who volunteered demographic labels; **typically >10k users**, engineered to hold equal proportions of each EEOC protected group; used ONLY for adverse-impact testing.

### Reference clients
- **JPMorgan Chase** — most-cited finance user; "unique among big banks in mandating Pymetrics games for almost all junior roles." `[PREP-VENDOR]` (Lumovest, CareerTestPrep, HackingTheCaseInterview)
- Vendor-named clients: **Sage** (early careers), **Chalhoub Group**. `[VENDOR]` (harver.com/gamified-assessments)
- Other commonly listed users (mixed sectors, verify individually): Unilever, Accenture, BCG, Bain, PwC, EY, Mastercard, Coca-Cola, HSBC, RBS/NatWest, AstraZeneca, GSK, Swarovski, ANZ. `[PREP-VENDOR]` — TREAT AS UNVERIFIED marketing/prep aggregation; see §11 volatility flag.
- BNP Paribas: confirmed user via a 2023 LL144 bias-audit posting (BABL AI, 6/29/2023, hosted on Paramount's site oddly — cross-listed). `[INDEPENDENT]`

---

## 4. FULL MECHANICS — THE GAMES

**Total games:** **12 core games** (the "pymetrics suite"). `[INDEPENDENT]` (audit §3.1 "a core set of twelve games"). Plus an OPTIONAL add-on suite of **numerical/logical reasoning games** (4 games; "recently introduced" as of 2020) that clients may bolt on. `[INDEPENDENT]` (audit §3.1 footnote). Harver also cross-sells 5 separate cognitive-ability tests (Perceptual Speed, Verbal, Spatial, Logical, Mathematical Reasoning) — these are HARVER products, NOT the pymetrics neuroscience 12. `[PREP-VENDOR]` (GraduatesFirst) — keep distinct.

**No pass/fail "score":** games "not meant to be won or lost." Output is **match/fit to a role model**, NOT a raw score. `[INDEPENDENT]` (audit §3.1) — REINFORCE THIS in §5.6.

**~1,000+ behavioural data points collected.** `[PREP-VENDOR]`/`[VENDOR]`

### The 12 games (mechanic · instructions · traits · telemetry)
Canonical list `[INDEPENDENT]`/`[PREP-VENDOR]` (GraduatesFirst, JobTestPrep, psychometric-success, careertestprep — cross-checked):

1. **Balloon / Money game (BART — Balloon Analogue Risk Task)**
   - Mechanic: pump a balloon; each pump adds money to a temporary bank; bank it before it pops or lose the round's money. Balloons vary in pop threshold.
   - Traits: **risk tolerance, decision-making under uncertainty, learning** (do you adjust pump count as you learn pop points?).
   - Telemetry: pumps per balloon, money banked vs lost, adaptation across trials, consistency/erraticness. `[PREP-VENDOR]`

2. **Keypress game**
   - Mechanic: press a specified key (often spacebar) **as fast as possible** for a set duration.
   - Traits: processing speed, **attention/focus, motor tempo**; some sources say emotion/drive.
   - Telemetry: keypress rate, rhythm/consistency. `[PREP-VENDOR]`

3. **Digits (memory / digit-span) game**
   - Mechanic: a number sequence flashes; recall and type it back in order; sequences lengthen.
   - Traits: **working memory**, attention span, learning.
   - Telemetry: max span reached, error rate by length. `[PREP-VENDOR]`

4. **Arrows (task-switching / Flanker-style) game**
   - Mechanic: coloured arrows appear; rule depends on colour (e.g. blue/black → respond to CENTRE arrow direction; red → respond to SIDE arrows). Rules change → must switch.
   - Traits: **task-switching, attention to detail, learning from mistakes, adaptability.**
   - Telemetry: accuracy, reaction time, error-recovery, cost of switching. `[PREP-VENDOR]`

5. **Lengths game**
   - Mechanic: judge which face has the **longer/shorter mouth** (subtle perceptual differences); rule can flip.
   - Traits: attention to detail, **effort, adaptive learning**, perception.
   - Telemetry: accuracy on subtle differences, effort sustained, adaptation. `[PREP-VENDOR]`

6. **Cards game (Iowa Gambling Task)**
   - Mechanic: start with ~$2,000; draw from four decks with different reward/penalty structures; maximise winnings.
   - Traits: **reward sensitivity, risk under uncertainty, pattern recognition/learning, decision-making.**
   - Telemetry: deck-selection shift toward advantageous decks over time (learning rate), risk profile. `[PREP-VENDOR]`

7. **Tower (Tower of London) game**
   - Mechanic: rearrange coloured rings/discs to match a target configuration in the **minimum number of moves**.
   - Traits: **planning, problem-solving.**
   - Telemetry: moves vs optimal, planning time before first move. `[PREP-VENDOR]`

8. **Money Exchange #1 (Trust game)**
   - Mechanic: you get ~$10, choose how much to send a partner; sent amount is **tripled** on receipt; partner may return some.
   - Traits: **trust, risk tolerance, fairness, altruism.**
   - Telemetry: amount sent (trust), expectation of reciprocity. `[PREP-VENDOR]`

9. **Money Exchange #2 (Trust/reciprocity, second role)**
   - Mechanic: both start ~$5; one randomly gets +$5; players decide how much to give/take over two rounds.
   - Traits: **trust, altruism, fairness, generosity, decision-making.**
   - Telemetry: give/take amounts, reciprocity behaviour. `[PREP-VENDOR]`

10. **Easy-or-Hard task (effort / motivation)**
    - Mechanic: per round, choose a **low-reward/high-probability (easy)** task or a **high-reward/low-probability (hard)** task, sometimes with stated reward + probability.
    - Traits: **effort allocation, motivation, risk tolerance, rational reward-maximising, resilience.**
    - Telemetry: hard/easy choice ratio vs stated odds, effort under varying incentive. `[PREP-VENDOR]`

11. **Stop (Go/No-Go — impulsivity/response inhibition) game**
    - Mechanic: press spacebar/button ONLY when a target shape/colour appears; withhold for others (which flash rapidly).
    - Traits: **impulse control, attention, focus, reaction time.**
    - Telemetry: commission errors (pressing on no-go), omission errors, reaction time. `[PREP-VENDOR]`

12. **Faces (emotion recognition) game**
    - Mechanic: identify the emotion in facial expressions; sometimes paired with a short context/story that may contradict the face.
    - Traits: **emotion recognition, emotional intelligence, empathy.**
    - Telemetry: accuracy, use of context vs face. `[PREP-VENDOR]`

### Telemetry themes captured across games `[INFERRED]` from the above + audit
- Reaction time, accuracy, **risk-taking under uncertainty**, **learning rate** (adaptation across trials), **altruism/fairness** (money games), **effort allocation**, impulse control, planning depth, working-memory span. NOT self-report — behavioural traces only. `[INDEPENDENT]` (audit: features derive from gameplay).

### Device / platform / logistics
- Available on **web, iOS, and Android**; translated into several languages. `[INDEPENDENT]` (audit §3.1)
- Built-in accommodations for **colour-blindness and dyslexia** at the game level. `[INDEPENDENT]` (audit §3.1) — see §9.
- Prep-vendor guidance: works on Chrome/Firefox/Safari/Edge; **PC recommended over phone**. `[PREP-VENDOR]` (GraduatesFirst)
- **Pause:** allowed BETWEEN games; you **cannot restart** a game mid-play. `[PREP-VENDOR]` (GraduatesFirst)
- Missing-data rule: a player with **>2 missing games** is treated as incomplete and dropped from analyses; missing feature values are **median-imputed**. `[INDEPENDENT]` (FAccT §3.2)
- `[UNKNOWN]` official disconnect/reconnect behaviour mid-game. Proxy: prep vendors say you can pause between games but not restart a game; a mid-game disconnect likely voids that game's traits → imputation. `[INFERRED]`

---

## 5. TAILORING (KEY DIFFERENTIATOR)

- **Same game data, different verdict per firm.** The 12 games and your raw traits are constant, but the **role model** you're matched against is built from a specific firm/role's incumbents (custom) or a core model. Your trait profile can MATCH firm A's trader model and NOT match firm B's — because different roles reward different trait combinations. `[INDEPENDENT]`/`[PREP-VENDOR]`
- "There is no universal 'good' profile — different roles require different trait combinations." `[PREP-VENDOR]` (aggregated); consistent with audit's role-specific in-group design. `[INDEPENDENT]`
- **Bespoke criterion validation:** the in-group = the firm's own high performers as judged by the firm's own performance metrics → this is criterion-referenced to that employer, not a universal norm. `[INDEPENDENT]` (audit §3 steps 2–3)
- Customisation extends to: which traits/features are included, which demographic groups get fairness-tested, even swapping the fairness metric — "pymetrics may customize their model training and adverse impact assessment process for specific clients… even swapping out the four-fifths fairness metric for an entirely different fairness criteria." `[INDEPENDENT]` (audit §4.4 Limitations) — IMPORTANT for legal chapter: the audited guarantees apply to the BASELINE codebase, NOT bespoke variants.
- Report-language customisation: Harver lets clients "customize the language in reports" to their "unique capability language" (e.g. one client's "Head, Heart, Hands" ethos). `[VENDOR]` (harver.com/blog/pymetrics-customizable-capabilities)
- If no model meets BOTH performance and fairness bars, the job analyst re-engages the client to refine role definition / re-select incumbents / improve performance metrics; if still impossible, **no model is deployed**. `[INDEPENDENT]` (audit §3 footnote 3, §3.3)

---

## 6. SCORING / OUTPUT

- Pipeline: gameplay → traits/features → **SVM predictive model** → percentile-based **fit score** → **recommendation tier.** `[INDEPENDENT]` (FAccT §3.2)
- **Three tiers:** **"Highly Recommended", "Recommended", "Not Recommended"** (some docs "Do Not Recommend"). `[INDEPENDENT]` (audit §3.3; BABL AI 2025 audit uses "Do Not Recommend / Recommend / Highly Recommend").
- **Percentile thresholds:** typically **50th and 70th** — ≥70th percentile = Highly Recommended; 50th–70th = Recommended; <50th = Not Recommended. Client-customisable. `[INDEPENDENT]` (FAccT §3.2 DIRECT).
- **NOT a classic norm-referenced percentile vs the general population** in the psychometric sense — it's a **fit percentile against the role model** (how close your behaviour is to the target trait profile). `[INFERRED]` from tier construction + "fit percentile" language (audit §3.3 "50% and 70% fit percentile thresholds").
- **What the recruiter sees:** a recommendation tier + trait profile per candidate; can apply further filters (resume screen) before interview. `[INDEPENDENT]` (audit §3 step 5). Recruiter does NOT get a single number the candidate can appeal.
- **What the candidate sees:** limited. A **trait report / personality description across the 9 trait families** (Effort, Risk, Fairness, Emotion, Decision Making, Focus, Learning, Attention, Generosity). Candidate is **NOT shown a score** nor how they compare to the firm's target profile. `[PREP-VENDOR]` (Lumovest). Some employers email a result; some show nothing. `[PREP-VENDOR]` (GraduatesFirst)
- **Retake policy:** you generally **cannot retake for ~330 days** (some sources "once every 330 days"). `[PREP-VENDOR]` (GraduatesFirst "once every 330 days"; Lumovest "330 days").
- **Results FOLLOW YOU across employers:** your gameplay results are **reused for every pymetrics-using employer you apply to within the ~330-day window** — you play the 12 games ONCE, and each firm's model re-scores your SAME traits against its OWN model. `[PREP-VENDOR]` (Lumovest, CareerTestPrep — strongly and repeatedly stated). This is a MAJOR candidate-facing point for §5.6.
  - `[INFERRED]` implication: a "bad" trait profile can't be re-attempted for ~11 months, but a profile that fails firm A may still pass firm B because models differ (§5).

---

## 7. HOW TO "PREPARE"

- **You largely cannot study for it** — no right/wrong answers, it's fit-based. Legit approach = **be authentic + understand it's about fit, not performance.** `[PREP-VENDOR]`/`[INDEPENDENT]`
- Legitimate prep steps commonly advised `[PREP-VENDOR]` (psychometric-success, JobTestPrep): read each game's instructions carefully; do it when mentally fresh (morning); remove distractions; stable internet; familiarise yourself with game FORMATS so you don't waste the first trials learning mechanics.
- **Risk-game nuance (important):** don't be ERRATIC. Consistency reads as a stable risk profile; wildly inconsistent balloon-pumping/card-drawing produces a noisy, hard-to-match profile. Aim for measured, internally-consistent risk behaviour rather than "gaming" a target. `[PREP-VENDOR]`/`[INFERRED]`
- **Faking debunk:** because the model matches you to a role you don't know the target profile for, deliberately faking a "trader" persona can backfire (you don't know which traits that firm's model weights, and inconsistency hurts). The trust/altruism money games and reaction-time games are hard to fake convincingly. `[INFERRED]` from mechanics + audit's note that faking requires "train[ing] human beings to play the games in very specific ways, or writ[ing] software to emulate a human" (audit §5.1 footnote 8, re CLIENT manipulation but same logic applies to candidates).
- Prep vendors DO sell simulations (JobTestPrep pack from ~$59; GameAssessmentPrep, CogniPrep, iPrep) — value is **format familiarity**, not a way to "beat" it. `[PREP-VENDOR]` — note commercial incentive.

---

## 8. INTEGRITY / PROCTORING

- pymetrics is **typically UNPROCTORED** — candidate plays remotely, unsupervised, own device. `[INFERRED]` from remote web/mobile delivery + no proctoring mention in vendor/audit docs. `[UNKNOWN]` any webcam/lockdown option — none surfaced; proxy: no source mentions proctoring, and Harver markets frictionless candidate experience.
- **Hard to fake BY DESIGN** — this is a selling point vs proctoring:
  - No "correct" answers to look up; behavioural traces (reaction time, risk consistency, altruism) aren't answerable from Google. `[INFERRED]`/`[VENDOR]`
  - Client-side manipulation resistance was formally tested: auditors "were unable to circumvent the fairness checks… by manipulating in group data"; faking a workforce would require training humans or bots to play in specific ways. `[INDEPENDENT]` (audit §5.1)
- **Known integrity WEAKNESS (candidate-side):** the **Digits memory game** instructs "do not write your answers down," but this is unenforceable — flagged as "a major flaw in the system that compromises the integrity of the assessment." `[PREP-VENDOR]` (Lumovest). `[INFERRED]`: writing digits down could inflate the working-memory trait — but that's ONE trait among ~90 and may not match any firm's weighting.
- Monitoring signals: `[UNKNOWN]` whether pymetrics captures device/keystroke anomaly flags. Proxy: it captures fine-grained keypress timing (keypress/stop games) which could in principle flag bot-like input, but no public confirmation.

---

## 9. FALSE-POSITIVE / DISABILITY RISKS

- **Structural risk:** games have inherent **speed/reaction-time demands** (rapid clicks/taps) and **flashing images** → can disadvantage candidates with motor, visual-processing, attention, or epilepsy-related conditions. `[INDEPENDENT]` (MIT Technology Review, 2021-07-21, disability-rights-in-AI-hiring). URL: https://www.technologyreview.com/2021/07/21/1029860/disability-rights-employment-discrimination-ai-hiring/
- **Colour-blindness:** several games use colour-coded rules (Arrows, Stop) → risk if uncorrected. `[INFERRED]` from game mechanics. Mitigated by accommodation (below).
- **pymetrics accommodations offered** `[VENDOR]` (Accessibility Accommodations PDF, s3.amazonaws.com/pymetrics-public-content-production/pdf/accessibility-accommodations.pdf):
  1. **Modified colour palette for colour-blindness** ("coming soon: select your own palette").
  2. **More time on time-sensitive games + adjusted font** for: Visual Impairment; Visual Processing Disorder; Neurodevelopmental (Autism, ADD, ADHD, Dyslexia, Dyscalculia, Intellectual Developmental Disorder); Speech/Language (Aphasia, Apraxia).
  - Candidate **self-selects** the accommodated version from a disability list before playing.
  - Candidates told to **STOP / not play** if they have visual impairments needing a braille display, or **dominant-hand** motor/mobility/coordination issues → employer must offer an **alternative selection process**. `[VENDOR]`
  - For many other conditions (Cerebral Palsy, MS, Epilepsy, non-dominant-hand motor issues, mental-health conditions, etc.) games are **NOT modified**; candidate directed to contact support post-play if they struggled. `[VENDOR]`
- **Employer is NOT told which candidates requested accommodations** — kept confidential. `[INDEPENDENT]` (MIT Tech Review) / `[VENDOR]` (accommodations PDF: accommodation selection not shared).
- **Vendor's fairness defence:** "candidates are not evaluated in the abstract but only relative to the role… it is not predetermined that people with certain disabilities will be disadvantaged" (e.g. a shorter attention span may be beneficial or irrelevant for a role). pymetrics claims it compared match rates of accommodated-version players to general population and "found no adverse impact." `[VENDOR]` (accommodations PDF) — self-reported, not independently verified. `[UNKNOWN]` independent disability-adverse-impact study; note LL144 audit EXCLUDES disability (see §10).
- `[INFERRED]` false-positive vector for the book: a well-qualified candidate with slow reaction time, ADHD, or colour-vision deficiency who does NOT request accommodation could be mis-matched (Not Recommended) despite being a strong hire — and because results carry ~330 days, the mis-match propagates across firms.

---

## 10. THE BIAS-AUDIT ANGLE (feeds legal chapter)

### audit-AI (open-source tool) `[VENDOR]`/`[INDEPENDENT]`
- pymetrics open-sourced **audit-AI** (Python, on scikit-learn/pandas) for bias testing of ML: https://github.com/pymetrics/audit-ai
- Implements the **UGESP four-fifths (4/5) rule** via **minimum bias ratio / impact ratio** + statistical-significance tests (**Chi-square, Fisher's exact**, p<.05). `[INDEPENDENT]` (audit §3.3)

### How pymetrics de-biases (the mechanism) `[INDEPENDENT]` (audit §3.3, direct quotes from pymetrics docs)
- "All pymetrics models are proactively de-biased before they are deployed… Models must pass the 4/5ths rule when performance is compared across demographic groups during model build."
- **Bias set** = withheld users with known demographics (each EEOC race/ethnicity + gender group).
- **min bias ratio (Impact Ratio)** = (lowest-passing group's selection rate) / (highest-passing group's selection rate), per category.
- **Threshold, not gradient:** a model **passes or fails**; among passing models, where validity is equal, pick the least-biased.
- Checked at **both 50% and 70% fit-percentile thresholds**.
- If NO fair model can be built → **no model deployed** (the "abandon" fallback). `[INDEPENDENT]`

### The Northeastern cooperative audit (2020) — the famous one `[INDEPENDENT]`
- Auditors: **Christo Wilson, Alan Mislove, Avijit Ghosh, Shan Jiang**, Khoury College, **Northeastern University**. Contract signed **March 2020**; audit run **summer 2020**.
- **pymetrics PAID ~$105,000** (structured as a grant to Northeastern, paid up-front, not contingent on outcome, to preserve independence). `[INDEPENDENT]` (press) / whitepaper describes the arrangement.
- Type: **cooperative code audit** — auditors got the source code (template Jupyter notebook + Python modules: biased SVM, Beam search, min-bias-ratio), 8 notebooks (1 blank template, 6 completed client engagements, 1 complete engagement WITH data), representative datasets, on a pymetrics-provisioned AWS VM. Did NOT tell pymetrics their methods in advance.
- Published: whitepaper (cbw.sh) + peer-reviewed **FAccT '21** paper "Building and Auditing Fair Algorithms: A Case Study in Candidate Screening."
- **5 findings — ALL PASS** `[INDEPENDENT]` (audit Exec Summary):
  1. **Correctness** — source code correctly implements 4/5 rule via min bias ratio for the 7 EEOC groups (male, female, White, Black, Hispanic, Asian, ≥2 races). ✔
  2. **Direct discrimination** — models do NOT use demographics as training features; demographics used ONLY in post-training bias testing. ✔
  3. **De-biasing circumvention** — auditors tried malicious/crafted in-group data to sneak a biased model through; ALL failed (all control-flow paths hit the fairness test). ✔
  4. **Sociotechnical safeguards** — human data scientists build models by hand, BUT a **>100-question compliance checklist** + **second data scientist sign-off** required before deployment (would take collusion of two to deploy a biased model). ✔
  5. **Sound assumptions** — median imputation DOES have differential impact by demographic (esp. Black players missing more traits; decision-tree/extra-trees imputers would be statistically better), BUT this did NOT materially change 4/5 compliance. ✔ (with caveat)
- **CRITICAL SCOPE LIMITS (for legal chapter):**
  - Audit ONLY covered the **baseline, non-customised** model pipeline. Bespoke client variants NOT audited. `[INDEPENDENT]` (audit §4.4)
  - Auditors **did NOT** assess whether games measure real ability or predict job performance. `[INDEPENDENT]` (§4.2)
  - Did NOT question the CHOICE of 4/5 rule / min-bias-ratio / EEOC categories (agreed off-limits pre-audit). `[INDEPENDENT]` (§4.2)
  - Did NOT test intersectional groups (e.g. Black women) — EEOC doesn't treat them as protected. `[INDEPENDENT]` (§4.2)
  - Only players who opt into demo survey enter the bias group (>75% opt-in claimed); bias group drawn from historical players (600k+), which may not represent a given applicant pool. `[INDEPENDENT]` (§6.2)
  - Model perf figures from the audited engagement: AUC ~0.70–0.72, accuracy ~0.69–0.72 — **modest predictive power.** `[INDEPENDENT]` (audit Table 3)

### The 2024 Stanford/Chapman/Northeastern critique — "Algorithmic Monocultures in Hiring" `[INDEPENDENT]`
- Presented **ACM FAccT 2024 (Montreal)**. Authors from Stanford, Chapman, Northeastern.
- Data: **>4 million applications from ~3 million applicants across 156 employers** (mostly $5B+ revenue), using pymetrics algorithms in finance/manufacturing/tech.
- **Method critique:** pymetrics reported fairness AGGREGATED across employers/occupation groups; researchers re-analysed **position-by-position**, which is how the 4/5 rule is legally meant to apply.
- **Findings** (quote these numbers, Fortune 2026-05-26 write-up): URL https://fortune.com/2026/05/26/ai-hiring-algorithm-racial-disparities-pymetrics-stanford-study/
  - **10.62%** of individual positions showed adverse impact on **Black** applicants.
  - **~30%** of Black applicants applied to ≥1 such position.
  - **25.87%** of all Black applicant submissions (~40,000) went to positions with "discriminatory outcomes" per federal guidelines.
  - **14.74%** of Asian applicant submissions went to such positions.
  - Argument: "aggregating from individual positions to occupation groups suffices to mask the per-position adverse impact" → aggregate-only reporting is "improper, or at minimum an incomplete" reading of federal guidance.
- **Tension to flag:** the 2020 audit said the BASELINE code passes 4/5 in aggregate; the 2024 study says PER-POSITION deployment still produced adverse impact in ~1/10 roles. Both can be true — fairness-at-build ≠ fairness-in-deployment-per-role. Big point for legal/limitations chapter. `[INFERRED]`
- Counter-view exists: a prep/industry blog ("placementist") frames the Stanford study as "fear-farming" — note as a partisan rebuttal, low weight. `[PREP-VENDOR]`

### NYC Local Law 144 posture `[INDEPENDENT]`
- **LL144 (of 2021, enforced from July 2023):** any AEDT used to "substantially assist or replace" hiring/promotion decisions for NYC roles needs a **yearly independent bias audit** assessing disparate impact, publicly posted, + candidate notice.
- pymetrics/Harver is squarely an AEDT-type tool (produces scores/tiers) → subject to LL144 when used for NYC candidates.
- **Public LL144 bias audits exist for the pymetrics/Harver tool:**
  - **BABL AI, 6/29/2023**, for **BNP Paribas** using "pymetrics inc. (Harver) Soft Skills Platform." `[INDEPENDENT]`
  - **BABL AI, dated 07/17/2025** (V1.0), "Audit of Harver's Soft Skills Platform for NYC LL144." Hosted: https://harver.com/wp-content/uploads/2025/11/pymetrics-Soft-Skills-Platform-2025-Bias-Audit.pdf
- **2025 BABL AI audit — details & ACTUAL NUMBERS** `[INDEPENDENT]`:
  - Auditor: **BABL AI Inc.** (Iowa City); ForHumanity-certified lead auditors; independence per ForHumanity + Sarbanes-Oxley; fees not contingent on outcome.
  - Tool output described: recommendation tier (Do Not Recommend / Recommend / Highly Recommend) based on **percentile rank vs a validated model**; selection rate computed at the **50th percentile** ("Recommend" default band).
  - Data window: **Jan 2024 – Dec 2024**; recruitment use cases; candidates who completed the games.
  - **Metric:** selection/scoring rate + **impact ratio** (4/5 rule); flags any group <0.80.
  - **RESULT: PASS** on Disparate Impact, Governance, Risk Assessment, and Overall.
  - **Impact ratios (all ≥0.8 → pass):**
    - Gender: Male 0.545 selection rate (IR 1.000); Female 0.540 (IR **0.992**). n=164,014 / 119,242.
    - Race/ethnicity: Black/African American 0.590 (IR 1.000, reference); White 0.571 (0.967); Hispanic/Latino 0.542 (0.918); **Asian 0.539 (IR 0.914 — lowest but still >0.8)**; smaller groups (Native Hawaiian/PI, Two-or-more, Native American) marked N/A (<2% of N).
    - Intersectional lowest: **Hispanic-or-Latino Male IR 0.917**, Non-Hispanic Asian Male 0.921, Non-Hispanic Asian Female 0.921 — all pass.
  - **SCOPE EXCLUSIONS (legal-chapter gold):** audit covered ONLY race/ethnicity + gender; **did NOT** test age, disability, religion, sexual orientation, national origin, veteran status, pregnancy, etc.; did **NOT** certify the model "bias-free"; not for compliance with any law other than LL144. `[INDEPENDENT]`
- ACLU maintains a crowd-sourced LL144 audit tracker (github.com/aclu-national/tracking-ll144-bias-audits) — useful cross-ref. `[INDEPENDENT]`
- Academic caveat on LL144 generally: "Null Compliance: NYC Local Law 144 and the Challenges of Algorithm Accountability" (arxiv 2406.01399) documents widespread non-posting/gaming of the law. `[INDEPENDENT]`

---

## 11. UK FINANCE EMPLOYER USAGE (stages / years / sources / VOLATILITY)

- **JPMorgan Chase & Co.** — the anchor UK-finance user. Pymetrics 12 games as an **early online-assessment stage** for junior/analyst/grad roles; "mandating Pymetrics games for almost all junior roles"; ~20–30 min. Followed by HireVue + numerical tests. `[PREP-VENDOR]` (Lumovest, CareerTestPrep, GraduatesFirst JPM guide, HackingTheCaseInterview). Years: cited across 2023–2026 prep guides → active at least 2019–2026. `[PREP-VENDOR]`
- **BNP Paribas** — confirmed user (2023 LL144 audit names them on pymetrics/Harver platform). `[INDEPENDENT]`
- **HSBC, RBS/NatWest** — listed as pymetrics users by GraduatesFirst. `[PREP-VENDOR]` — UNVERIFIED against primary source; treat cautiously.
- Consulting-adjacent finance/pro-services often lumped in: **BCG** (BCG Pymetrics Test is heavily documented), PwC, EY, Accenture, Bain. `[PREP-VENDOR]`
- **Goldman Sachs = CONTRAST, not a user:** historically used its OWN bespoke assessment (numerical + SJT) + HireVue, NOT pymetrics. Good for "why some firms DON'T pick it." `[PREP-VENDOR]`
- Non-finance UK grad users frequently cited: AstraZeneca, GSK (pharma), Unilever (FMCG). Candidate chatter exists on TSR for AstraZeneca pymetrics. `[CANDIDATE]`/`[PREP-VENDOR]`

### VOLATILITY FLAG (important for a book — this moves)
- Vendor client rosters SHIFTED after the Harver acquisition (2022) and rebranding; some firms have quietly moved to competitors (Arctic Shores, HireVue game-based, SHL). `[INFERRED]` from the acquisition + prep-vendor churn.
- Prep-vendor client lists are **marketing aggregations, often stale** — a firm listed as a "pymetrics user" may have used it in ~2019–2021 and since dropped it. DO NOT state a firm currently uses pymetrics without a dated primary source. `[INFERRED]`/`[UNKNOWN]`
- Best DATED primary anchors for "who uses it": the LL144 audit postings (BNP Paribas 2023; the 2025 Harver platform audit implies live enterprise use through 2024 data). `[INDEPENDENT]`

---

## STRONGEST SOURCES (for citation)
1. **Wilson, Mislove, Ghosh, Jiang — "Auditing the pymetrics Model Generation Process"** (Northeastern whitepaper). https://cbw.sh/static/audit/pymetrics/pymetrics_audit_result_whitepaper.pdf `[INDEPENDENT]` — THE authoritative source on mechanics, de-biasing, in/out/bias groups, safeguards, scope limits.
2. **FAccT '21 peer-reviewed version** — "Building and Auditing Fair Algorithms: A Case Study in Candidate Screening." https://www.ccs.neu.edu/home/amislove/publications/Pymetrics-FAccT.pdf `[INDEPENDENT]` — SVM, 50–100 in-group, 64 features, 50/70 percentile tiers, IR≥0.8.
3. **BABL AI 2025 LL144 Bias Audit of Harver's Soft Skills Platform.** https://harver.com/wp-content/uploads/2025/11/pymetrics-Soft-Skills-Platform-2025-Bias-Audit.pdf `[INDEPENDENT]` — actual 2024 impact-ratio tables, PASS, scope exclusions.
4. **"Algorithmic Monocultures in Hiring" (FAccT 2024) via Fortune 2026-05-26.** https://fortune.com/2026/05/26/ai-hiring-algorithm-racial-disparities-pymetrics-stanford-study/ `[INDEPENDENT]` — per-position adverse-impact critique + numbers.
5. **Harver acquisition press.** https://www.prnewswire.com/news-releases/harver-acquires-pymetrics-further-enhancing-talent-decision-capabilities-across-the-employee-lifecycle-301603823.html + https://harver.com/harver-acquires-pymetrics/ `[VENDOR]`/`[INDEPENDENT]`
6. **pymetrics Accessibility Accommodations PDF.** https://s3.amazonaws.com/pymetrics-public-content-production/pdf/accessibility-accommodations.pdf `[VENDOR]`
7. **MIT Technology Review — disability & AI hiring (2021-07-21).** https://www.technologyreview.com/2021/07/21/1029860/disability-rights-employment-discrimination-ai-hiring/ `[INDEPENDENT]`
8. **audit-AI GitHub.** https://github.com/pymetrics/audit-ai `[VENDOR]`
9. Vendor product page: https://harver.com/gamified-assessments/ `[VENDOR]`
10. Prep guides (format/logistics/UK-finance stage, LOW weight): GraduatesFirst https://www.graduatesfirst.com/pymetrics-practice-games-digital-video-interviews ; JobTestPrep https://www.jobtestprep.com/harver-assessment ; psychometric-success https://psychometric-success.com/aptitude-tests/test-types/pymetrics ; Lumovest JPM https://www.lumovest.com/library/careers/jp-morgan-pymetrics/ `[PREP-VENDOR]`

---

## RESIDUAL GAPS (explicit — do NOT fabricate to fill)
- **Deal price** for Harver→pymetrics acquisition: undisclosed. `[UNKNOWN]`
- **Independent, peer-reviewed CRITERION validity** (do the games actually predict job performance): NOT public. Baker (2019) "Games, Measures and Factors" validation deck is CONFIDENTIAL; Northeastern auditors urged pymetrics to publish it and it appears still unpublished. Only proxy = vendor "90% accuracy" marketing + audited AUC ~0.70–0.72 (modest). `[UNKNOWN]`
- **Exact minimum-incumbent cutoff** separating "custom" from fallback "core" model, and the precise architecture of the CORE model: proprietary. Floor cited = ~50 in-group players. `[UNKNOWN]`
- **Direct candidate testimony (n counts):** Wall Street Oasis thread ("Pymetrics… What the fuck??") and The Student Room threads returned **HTTP 403** to the fetcher — could NOT extract individual quotes or count commenters. Candidate sentiment above is via search-snippet summaries only, so `[CANDIDATE, n=X]` counts are UNAVAILABLE. Recommend a manual browser pass on WSO + TSR (AstraZeneca pymetrics thread t=6265898; GSK/AZ apprenticeship t=7179651) for verbatim quotes and n.
- **Current (2026) live UK-finance client roster:** prep-vendor lists are stale/marketing; only dated primaries are BNP Paribas (2023 audit) and JPM (continuous prep coverage). Whether HSBC/NatWest still use it in 2026 = `[UNKNOWN]`; flag volatility.
- **Mid-game disconnect/reconnect official policy:** not documented by vendor; inferred only. `[UNKNOWN]`
- **Proctoring/anti-cheat signals:** no public confirmation pymetrics captures anomaly/bot flags beyond raw keypress timing. `[UNKNOWN]`
- **Post-2022 changes to the pipeline:** the authoritative audit is from **summer 2020**; Harver may have altered the codebase/thresholds since. The 2025 BABL AI audit confirms the SAME tier/percentile structure persists, but internal ML details post-acquisition are `[UNKNOWN]`.
