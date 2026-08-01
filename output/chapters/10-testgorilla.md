# Chapter 10 — TestGorilla

> *Confidence tags used throughout (full explanation in Chapter 1): `[VENDOR]` vendor's own claim; `[INDEPENDENT]` peer-reviewed/independent; `[CANDIDATE, n=X]` candidate testimony with count; `[INFERRED]` my reasoning, shown; `[UNKNOWN]` not public; `[PREP-VENDOR]` commercial practice-seller, corroborate.*

> ### ⚡ At a glance — TestGorilla
> | | |
> |---|---|
> | **What it is** | An Amsterdam-based **self-serve skills-testing SaaS** (founded 2019). Employers assemble an assessment from a library of **400+** short tests (cognitive, personality, situational judgement, language, software, coding, role-specific) plus their own custom questions. A "talent discovery platform" sold to SMEs, tech, scale-ups and mid-market. |
> | **Where in the funnel** | Early screening — often a **CV-replacement step at the very top of the funnel**, sent to applicants before any human reads the application. |
> | **Format & timing** | An assessment = **up to 5 tests** (most ~10 min each) + custom questions → typically **~30–60 min total**. Fixed-form multiple-choice modules — **not adaptive**. Browser-based; **one attempt**. |
> | **Scoring model** | Each test → a **percentage score (0–100)**; candidates **ranked relative to each other** within the assessment. **No formal pass/fail** — the employer sets an implicit rank threshold. |
> | **Typical finance cut-off** | `[UNKNOWN]` — no published norm or cut-score. Prep-vendor figures (~60+ entry, ~75+ mid, ~80+ select) are `[PREP-VENDOR ESTIMATE]`, not vendor-confirmed; §10.6. |
> | **Integrity posture** | Anti-cheating suite is a **marketed selling point** and unusually well-documented: **30-second webcam snapshots**, full-screen-exit and tab-switch detection, IP/location logging, copy-paste/screenshot/dev-tool detection, randomised retiring question pools, time limits, a timestamped behaviour log grouped into "tiers." Webcam is **optional and permissioned**. |
> | **Retake** | **One attempt** per assessment; the timer continues even if you disconnect. |
> | **Top 5 tips** | 1) Expect **genuine skill tests** (Excel, Xero, GAAP, a coding stack) — brush up the named tool, not "aptitude tricks." 2) Sit it full-screen, one tab, camera-permitted, in a closed quiet room — the behaviour log is granular. 3) Don't fake Big-5/DISC/16-type; answer decisively and role-aligned. 4) Use the 4–5 warm-up questions to calibrate; pace at ~30–60s/question. 5) Request accommodations **before** you sit (+20% non-native / +50% disability) — the condition is never shared with the employer. |
>
> *(Every figure above is unpacked, sourced and confidence-tagged below. Be clear-eyed about relevance: TestGorilla is a fintech / challenger-bank / mid-market tool, **not** a bulge-bracket front-office name — see §10.1 and §10.5.)*

---

## 10.1 Snapshot

TestGorilla is a self-serve online skills-assessment platform, and the honest first thing to say about it is where it sits in your world: it is the tool you are far more likely to meet at a **fintech, a challenger bank, a scale-up or a mid-market employer** than at a bulge-bracket investment bank. It was founded in **2019** by **Wouter Durville** (CEO) and **Otto Verhage** (a former Bain & Company partner), and is headquartered in **Amsterdam, Netherlands**. `[INDEPENDENT — Tracxn/Crunchbase/PitchBook via search]` It raised roughly **$81m** in total funding across three rounds, headlined by a **$70m Series A in 2022** led by Atomico with Balderton Capital and Notion Capital, raised on the explicit pitch of helping companies "eliminate hiring bias." `[INDEPENDENT + VENDOR blog]` Third-party estimates put annual recurring revenue around $36m and valuation around $109m, but these are unverified and low-confidence. `[INDEPENDENT — treat as ESTIMATE]`

What TestGorilla actually sells is a **library of tests** — marketed as "400+ scientifically validated" (older copy says 350+) — that an employer assembles, self-serve, into a single multi-test assessment. `[VENDOR]` The library spans cognitive ability, personality, situational judgement, language, software, programming and role-specific skills, and the employer can bolt on their own custom questions. The company positions itself as a **"talent discovery platform"** and claims **10,000+ customers** and "millions of candidates," naming non-finance clients such as Sony, PepsiCo, Bain & Company, Oracle, H&M and the UK NHS. `[VENDOR]`

For a finance early-careers applicant, the part that matters is honest calibration. This is an **SME/SMB/tech/scale-up screening tool sold on price, breadth and a "skills-based hiring reduces bias" message** — a fundamentally different animal from the enterprise psychometrics of SHL or Aon (Chapters 1 and 2). In the funnel it typically sits **very early**, often as a CV-replacement screen sent to applicants before any human reads the form. An assessment is **up to five tests** (most about ten minutes each) plus custom questions, so **~30–60 minutes total**. `[VENDOR + PREP-VENDOR]`

---

## 10.2 Why this test exists

The problem TestGorilla is built to solve is not the bulge bracket's problem. A large bank drowning in twenty thousand applications for three hundred seats needs enterprise-grade, legally bulletproof, high-throughput psychometrics, and it can afford the six-figure enterprise contract that SHL or Aon charges. A **smaller employer — a fifty-person fintech, a growing SaaS company, a regional professional-services firm — has the same screening problem at smaller scale and none of that budget.** TestGorilla's entire reason to exist is to serve that under-served middle: a self-serve platform with a free tier and a low-commitment annual subscription, bought by a hiring manager with a company card rather than sold by an enterprise account team. `[INDEPENDENT — pricing sources, §10.3]`

The pitch layered on top is **skills-based hiring**: the claim that testing what a candidate can actually *do* — write the SQL, reconcile the ledger, reason through the numbers — predicts performance better and more fairly than screening a CV for the right university and the right internships. The Series A was explicitly messaged around **"eliminating hiring bias,"** the argument being that a blind skills test gives a state-school graduate or a career-changer a route past the CV filter that would otherwise reject them. `[VENDOR — Series A messaging]` That is a genuinely attractive proposition, and for many candidates it is a fairer door than the one SHL guards. It is also, at this stage, **largely a vendor self-assertion**: independent validity or adverse-impact audits of TestGorilla's library were not located in the research for this chapter, so treat "scientifically validated" and "bias-reducing" as marketing claims until a technical manual or third-party study surfaces. `[UNKNOWN — no independent audit located; §10.11]`

The broader debate about whether skills-based screening actually reduces adverse impact, and whether it merely relocates bias into the choice of which skills to test, is developed in the cross-cutting Chapter 6.1.

---

## 10.3 Why a firm chooses TestGorilla specifically

A firm does not choose TestGorilla because its tests are psychometrically superior — they are not marketed on validity coefficients or norm-group depth the way SHL's are. It chooses TestGorilla for **price, breadth and self-serve ease**. `[VENDOR + INDEPENDENT review sites]`

The library is the headline: **400+ pick-and-mix tests** across cognitive ability, personality and culture, situational judgement, language (CEFR-graded), programming, software and role-specific skills, plus five types of **custom question** (video, essay, file-upload, multiple-choice, coding) the employer writes themselves. A hiring manager can, in an afternoon, build a bespoke-feeling assessment for a very specific role without commissioning anything. `[VENDOR]`

The commercial model is what really separates it from the incumbents. There is a **free-forever tier** (five tests, AI résumé scoring, up to five custom questions per assessment, but no ATS integration, no video, no coding and no full library), and paid tiers layered on top:

| Plan | Approx. price | What it adds |
|---|---|---|
| Free | £0 | 5 tests, AI résumé scoring, ≤5 custom questions, no full library |
| Core | ~$1,700/yr (~$135/mo billed annually) | ~400 credits, ~2 premium seats |
| Plus | Custom, from ~$400/mo | ATS integrations, more seats |

`[INDEPENDENT — Capterra/spotsaas/xpay 2026; numbers vary by source, treat as ESTIMATE ranges]` Paid plans are **annual-commitment only** and **credits do not roll over** — a detail that matters to you only in that it explains the vendor's incentive to be sent to as many candidates as possible. `[INDEPENDENT]`

Rounding out the sales case: the **anti-cheating suite** is itself marketed as a differentiator (§10.8), and the **skills-based, anti-bias brand** is the wedge that lets a founder feel good about the buy. Where TestGorilla names finance-adjacent reference clients they are fintechs and scale-ups — **Revolut** ("40% faster hiring" case study), Volt, Embrace, Tresl — not banks. `[VENDOR]` That client list is the single most important signal of where you will actually meet this test, and §10.5 returns to it plainly.

---

## 10.4 What the assessment actually is — full mechanics

An assessment is **assembled, not fixed**. The employer selects **up to five tests** from the library and adds **custom questions** (10 or 20 depending on plan; the free tier caps at five). Everything is browser-based, fixed-form multiple-choice at the module level, and — importantly — **not adaptive**: unlike SHL's Verify Interactive or Aon's adaptive engines, a TestGorilla cognitive module does not get harder as you answer correctly. `[VENDOR + INFERRED from library format; the vendor does not advertise IRT/adaptivity]`

### The library you are drawn from

The vendor's own test-library page groups the catalogue roughly as follows:

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

`[VENDOR — test-library page]`

### Cognitive-ability subtests

The cognitive modules are all multiple-choice, mostly around **ten minutes each**, and fixed-form. They include Problem Solving (9 min), a Rapid Cognitive Index / RCI (10 min), Abstract Reasoning (10 min), Critical Thinking (12 min, advanced), Numerical Reasoning (10 min), Verbal Reasoning (10 min), Reading Comprehension (13 min), Attention to Detail — Textual (12 min) and Visual (10 min), Spatial Reasoning (10 min), Mechanical Reasoning (10 min), Basic/Intermediate Math variants (10 min), Computational Thinking (10 min) and Understanding Instructions (10 min). `[VENDOR — cognitive-ability library page]` **Per-question timing is not published by the vendor**, and prep vendors disagree — one cites a combined "40 questions / 20 minutes" (~30s each), another says "about a minute per question." Treat per-question pace as **roughly 30–60 seconds depending on the module**, and expect **4–5 practice questions** before a timed test begins. `[PREP-VENDOR, conflicting → ESTIMATE]`

### Personality and culture

Six instruments, all self-report with "no right or wrong answers": the **Big 5 / OCEAN** Five-Factor model (rate statements 1 = very inaccurate to 5 = very accurate, placed on five spectra), **DISC** (Marston's Dominance/Influence/Steadiness/Conscientiousness), a **16-Personality-Types** (Myers-Briggs-style) test, a **Culture Add** test and Enneagram-adjacent content. The vendor's own guidance is that personality tests **should not be used alone** and should be combined with cognitive and role tests for a "holistic view." `[VENDOR — personality library]`

### Situational judgement, language, software and coding

Thirteen SJT modules cover leadership, communication, time management and ethics themes — fixed-form, scenario-then-options. `[VENDOR]` Language tests are CEFR-graded. Software and role-specific tests probe genuine tool skill (Excel, Xero, an accounting or BI package); coding tests run in an **in-browser IDE**. `[VENDOR/PREP-VENDOR]`

### The five custom question types

On top of the library tests the employer can add their own questions in five formats: **pre-recorded video** (a webcam response to a text prompt), **essay**, **file upload** (CV, cover letter, or a take-home deliverable), **multiple-choice**, and **coding**. `[VENDOR — help-centre via search]` The video and essay answers are stored for **manual review** by the recruiter, not auto-scored on the free/lower tiers.

### A realistic walkthrough

You receive a link (often before any human has read your CV). You consent to the terms and — if the employer has enabled it — to **webcam snapshots**. The assessment presents your tests in sequence: perhaps a 10-minute Numerical Reasoning module, a 10-minute Excel test, a Big 5 questionnaire, an SJT, and three custom questions ending in a two-minute recorded video answer. Most tests open with a handful of untimed practice questions, then the clock runs. **You have one attempt**, and the timer keeps running even if your connection drops. At the end you submit; you usually receive no score. `[VENDOR + PREP-VENDOR]`

---

## 10.5 Is it tailored to the role?

**Yes at the assembly level, no at the item level** — and the distinction cuts the opposite way from SHL. With SHL the item bank is generic and the *interpretation* (norm group, competency weighting) is where tailoring happens. With TestGorilla the tailoring is blunt and visible: the employer **hand-picks up to five tests and writes their own custom questions**, so a finance-company assessment might literally be Numerical Reasoning + Excel + an IFRS or GAAP knowledge test + a Big 5 + a video question. `[VENDOR]` The individual test inside is off-the-shelf and identical for every employer who selects it, but the *combination* is bespoke to the role in a way a candidate can often infer just by reading which tests they were sent.

This is the moment to be blunt about **what "finance" means on TestGorilla**, because it is not what a front-office applicant assumes. The vendor's finance solutions page offers tests for **financial analysis, compliance, risk, IFRS, GAAP, Excel, business intelligence, Xero and accounts receivable** — that is a **back-office / accounting / finance-operations** toolkit. There is **no front-office investment-banking, trading, M&A or wealth-management content** in the library. `[VENDOR]` So even where a finance employer uses TestGorilla, the role being screened is far more likely to be an accounting, finance-ops, analyst-support or fintech role than a bulge-bracket deal seat.

The employer also **weights the modules** to taste, and candidates never see the weighting. `[PREP-VENDOR — prepclubs]` Truly bespoke criterion-validation against a specific firm's performance data is not something TestGorilla markets; the tailoring is selection-and-weighting, not psychometric re-validation. `[INFERRED]`

---

## 10.6 How they screen and filter — scoring, norms, cut-offs, ranking

Read this section knowing that TestGorilla is deliberately **less numerically prescriptive** than SHL, and that much of the precise-sounding detail online comes from prep vendors rather than the vendor.

**The scoring pipeline.** Each test produces a **percentage score from 0 to 100**. `[VENDOR]` One prep vendor additionally claims a **percentile against a norm group** per module, but the vendor's own public copy emphasises the percentage and a **candidate ranking**, not published norm tables — so treat the percentile claim as an estimate until a real norm methodology surfaces. `[PREP-VENDOR — ESTIMATE; percentile methodology is a documented gap, §10.13]`

**Ranking, not a pass mark.** The vendor is explicit: *"There's no 'pass' or 'fail'… It's about showcasing your abilities and how they align with the role."* `[VENDOR blog]` In practice the recruiter dashboard **ranks candidates relative to each other** within the same assessment, and the employer shortlists from the top of that ranking. The de-facto cut-off is therefore **a rank threshold the employer chooses**, not a published score — and it moves with the size and strength of the applicant pool, exactly like the rolling-sift dynamic in Chapter 6.8. `[VENDOR + INFERRED]`

**What the recruiter sees.** A dashboard showing per-test percentage scores, an overall ranked view of all candidates, the raw **custom-question responses** (video, essay, file) for manual review, and the **anti-cheating behaviour log** (§10.8). Public detail on the exact dashboard layout is thin. `[PREP-VENDOR + VENDOR — 🟡 thin]`

**Do you see your score?** Generally **no** — candidates are not given their own scores by default, though an employer can choose to share them. `[PREP-VENDOR — jobtestprep]`

**Retakes.** **One attempt.** The vendor states plainly, *"You'll have one attempt to complete your assessment,"* and the timer continues even if you disconnect — so a dropped connection eats your clock rather than pausing it. `[VENDOR blog + PREP-VENDOR]`

**The reported cut-off numbers — and why to distrust them.** One prep site floats an entry threshold around **60+**, an analyst/mid threshold around **75+**, and "select Bain/Revolut" around **80+**. Every one of these is a **`[PREP-VENDOR ESTIMATE]`, not vendor-confirmed**, and is presented here only as an illustrative shape, not a target you can trust. TestGorilla does not publish employer cut-scores, and because the sift is a *relative ranking*, no fixed number would be stable even if it did. The usable takeaway is directional: **be comfortably in the upper part of the pool on every module the employer weighted**, and treat clearing any implied threshold as necessary, not sufficient.

---

## 10.7 How to score well — legitimate, specific, actionable

TestGorilla rewards something refreshingly honest: **actual skill with the named tool**, plus clean test-taking discipline. There is far less "aptitude-test technique" to game than with SHL, because the software, role and coding tests measure real competence. Chapter 6.4 is the general construct manual; here is the TestGorilla-specific layer.

**Role, software and coding tests — this is where the marks are.** If you were sent an **Excel** test, drill Excel: lookups, pivot tables, common functions, keyboard efficiency under a clock. If it is **Xero, GAAP or IFRS**, revise the actual standard or the actual software. If it is a coding stack, practise in that language in a browser IDE against the clock. These modules reward genuine preparation more than any trick, and they are the most controllable part of your score. `[VENDOR library]`

**Cognitive modules.** Timed multiple-choice numerical, verbal and abstract reasoning at roughly **30–60 seconds a question**. Practise **speed with accuracy**; the modules are fixed-form and non-adaptive, so — unlike SHL — a fast wrong answer does not hand you an easier next item, it simply costs you a mark. Use the **4–5 warm-up questions** to calibrate the interface before the clock matters. Since back-navigation is not assumed to be available, answer each question decisively and move on. `[PREP-VENDOR]`

**Situational judgement.** Research the **employer's stated values** first, then pick the response that is both **most effective and most in character** for that firm. SJT modules are keyed to a "best" answer even under "no right answer" framing. `[PREP-VENDOR]`

**Personality (Big 5 / DISC / 16-type) — do not fake.** The honest reason mirrors §1.7's argument for SHL: a faked profile is optimised against a competency model you cannot see, tends to read as internally inconsistent, and — because the vendor's own guidance is to combine personality with cognitive and role tests — will be cross-checked against evidence you cannot fake. Read the firm's published values, decide which **genuine** facets of yourself are most role-relevant, and answer **decisively and consistently** from that authentic self rather than clustering everything at the mid-point. `[VENDOR guidance + INFERRED]`

**Set-up.** Sit it on a **laptop or desktop with a full-size screen**, **full-screen, one tab**, notifications off, on a stable connection, camera permitted and your face lit from the front. Every one of those is both a performance choice and an integrity choice — §10.8 explains why the behaviour log makes the two inseparable.

---

## 10.8 Integrity monitoring — what TestGorilla actually detects

This is the strong section, because TestGorilla's anti-cheating suite is **marketed as a selling point and unusually well-documented** — the vendor publishes what it detects, which most competitors do not. The full cross-vendor treatment of remote proctoring and its false-positive literature is Chapter 6.6; here is the TestGorilla-specific machinery.

**What it captures** `[VENDOR help-centre + VENDOR blog "cheating-detection-skills-assessments" + PREP-VENDOR, cross-confirmed]`:

- **Webcam snapshots** — a still image captured roughly **every 30 seconds** to verify identity. This is **optional and taken with the candidate's permission**, and the system also detects if the camera is disabled or off. Snapshots are retained for **6 months** (§10.11).
- **Full-screen-exit detection** — flags leaving full-screen mode.
- **Tab-switch detection** — flags switching browser tabs, and explicitly distinguishes a one-off from a pattern ("15 switches in a 20-minute test").
- **IP-address and approximate-location logging** — to spot multiple attempts or access from an unexpected place.
- **Screenshot detection** and **developer-tool detection**.
- **Copy-paste disabled/detected.**
- **Randomised question banks**, a **question-retirement system** (items are retired after an exposure limit) and **large pools** — the anti-memorisation layer, analogous to SHL's item randomisation.
- **Time limits** on every test to prevent extended off-screen research.

**How flags surface.** Events are logged with **timestamps** in a **candidate behaviour log** on the recruiter dashboard, and grouped into **behaviour tiers** (a help-centre article, "Understanding anti-cheating measures and behavior tiers," confirms the tiering exists, though its exact definitions were behind a bot-blocked page in the research). `[VENDOR — tier definitions a documented gap, §10.13]`

**The vendor's candid, anti-"gotcha" stance — and why it matters to you.** TestGorilla states its philosophy explicitly: *"we focus on cheating prevention and spotting outlier behaviors… instead of assuming every red flag is definitive proof."* Flags are framed as **"starting points for follow-up, not instant disqualifiers,"** and the vendor **recommends the employer contact the candidate for an explanation** before acting. `[VENDOR blog]` This is a genuinely more humane documented posture than most of the industry, and it is the single most useful fact in this chapter if you are ever flagged — the *vendor's own written guidance* is that a flag should trigger a conversation, not a rejection.

**Two honest limits of the record.** First, no dedicated **mouse-leave / focus-loss** telemetry is confirmed as a distinct named feature in the public sources — tab-switch and full-screen-exit are the analogues. `[UNKNOWN — gap]` Second, no prominent **AI-answer / plagiarism detector** is named in the sources found, unlike some 2025–26 rivals; it may exist but is unconfirmed. `[UNKNOWN — gap]` And the crucial caveat throughout: the **employer, not TestGorilla, interprets the log**, and a less-sophisticated SME recruiter can over-read it despite the vendor's guidance — which is why §10.9 and §10.10 matter.

---

## 10.9 How candidates commonly trip the system — including honestly

This is the section written for someone who has been flagged before, or fears they will be. It is deliberately concrete.

**Genuine cheating that is detected (stated as risk, not instruction).** Opening a second tab to look up an answer is caught by **tab-switch detection**; leaving full-screen to run another tool is caught by **full-screen-exit detection**; copying the question out to solve elsewhere is caught by **copy-paste and screenshot detection**; taking the test again under a different identity is caught by **IP/location logging and the one-attempt rule**; and memorising a shared question bank is undercut by **randomisation and question retirement**. None is worth the risk, and all are why this guide's value is legitimate preparation.

**The false-positive catalogue — how an honest candidate gets flagged.** Notably, **the vendor itself acknowledges most of these** as innocent triggers, which is unusually candid `[VENDOR blog]`:

- **Leaving full-screen to dismiss a system notification** — a calendar alert, an OS update prompt, a security-software pop-up — a behaviour the vendor names explicitly as honest.
- **A single quick tab-switch** to check a permitted requirement or the instructions — logged, but the vendor distinguishes it from a pattern.
- **A dropped or unstable connection** producing full-screen-exit or timing anomalies (and remember the timer keeps running).
- **Webcam off, disabled, or poorly lit** — a laptop with no working camera, backlighting from a window behind you, or the camera losing your face intermittently — registering as an identity flag. As Chapter 6.6 documents with independent evidence, face-detection has historically been **less reliable for darker skin tones**, a real demographic disparity that carries into any snapshot-based system. `[INDEPENDENT]`
- **Another person entering the room or audible nearby** — a housemate, a parent, a flatmate — appearing in a snapshot.
- **Glasses glare, a headscarf or a face covering** confusing face-presence detection in the snapshots.
- **Careful, slow reading, slight delays, or an accidental click** — the vendor's own "life happens" list.
- **Disability-related behaviour** — ADHD or anxiety restlessness, autistic self-regulation, or the use of a **screen reader or other assistive technology** — which can raise full-screen, tab or focus anomalies. This risk is real but is directly mitigated by the accommodations route in §10.10, *if you request it.* `[INFERRED]`
- **Sitting the test in a library or shared space**, where other faces and movement in a snapshot are unavoidable.

Because the **employer interprets the log**, the practical danger is not the vendor's algorithm — whose documented stance is lenient — but a **naive recruiter over-reading a single event**. The defence is to remove ambiguity in advance (§10.10) and, if flagged, to invoke the vendor's own "contact the candidate first" guidance (§10.11).

---

## 10.10 How to be unambiguously clean — pre-flight checklist

The goal is to make sure no honest behaviour can be misread. Print this.

- **Confirm the format in writing first.** Ask the recruiter (email is fine) whether **webcam snapshots** are enabled, whether any tools (a calculator, a spreadsheet, an IDE) are permitted for a given test, and whether there is a time limit per test. Their answer tells you which risks apply and creates a record.
- **Environment:** a quiet room you can close, door shut with a note on it, no one within camera or earshot range. Tidy desk.
- **Lighting:** a light source **in front of you, not behind** — no window at your back. If snapshots are on, check your face is evenly lit and fully in frame before you start.
- **Device:** a laptop or desktop with a **full-size screen and a working webcam**. **Disconnect any second monitor.** Close every other application and browser tab so you can stay in **full-screen, single-tab** for the whole assessment.
- **Notifications:** enable Do Not Disturb / Focus mode, and **pause OS and security-software auto-updates** for the window — these are the commonest cause of an innocent full-screen exit, and the vendor names them.
- **Network:** the most stable connection you have — wired if possible. Remember the **timer does not pause** on a disconnect, so reliability is a score issue as well as an integrity one. Avoid a VPN, which can trip IP/location logging.
- **Camera permission:** if snapshots are enabled, **grant permission and keep the camera on** — a disabled camera is itself an identity flag. If you have no working camera, tell the recruiter *before* you sit.
- **Stay in frame, one tab, full-screen.** Don't switch tabs to "just check" anything; don't drop out of full-screen. If you genuinely must (a fire alarm, a medical need), the vendor's guidance is that a flag prompts a conversation — so be ready to explain it.
- **Adjustments:** if you have a disability or are a non-native speaker, **request accommodations in writing before you sit** (§10.11). Do not wait until the day.

---

## 10.11 If you are flagged or rejected

You have real rights here, and TestGorilla's EU base and candid policies make some of them unusually usable. The full legal treatment is Chapter 6.7; this is the TestGorilla-specific playbook.

**First, lean on the vendor's own stance.** TestGorilla's published guidance is that a flag is a **"starting point for follow-up, not an instant disqualifier,"** and that the employer should **contact the candidate for an explanation.** `[VENDOR blog]` So the first move is to make that conversation easy to have: email the recruitment team promptly, reference your application, and offer the innocent explanation for whatever might have been logged (a notification pop-up, a dropped connection, a permitted look-away). You are not begging a favour — you are invoking the vendor's own documented process.

**Accommodations — a genuine positive, request them early.** TestGorilla's accommodations are better than most and worth using. The documented provision is **+20% time for non-native-language candidates** and **+50% time for a disability or condition** (ADHD, dyslexia, autism, and similar). `[VENDOR help-centre via search]` Crucially — and this is a real candidate-protection improvement — **as of June 2026 the candidate is no longer asked to share the disability itself with the employer, and the condition is never shared**: the employer is told only *that* an accommodation was requested and how it was applied, not what the underlying condition is. `[VENDOR — recent policy change, note the date]` Request the accommodation **before** you sit, via the recruiter or the candidate accessibility page.

**Then use your data-protection rights.** Under **UK GDPR Article 15 (right of access)** you can submit a **Data Subject Access Request (DSAR)** to the **employer** (the data controller), who must respond within **one month**, free of charge. Ask specifically for: your **per-test scores**; your **anti-cheating behaviour log with the specific timestamped events and behaviour-tier assigned**; any **webcam snapshots** held; the **decision logic**; and confirmation of **whether a human was involved**. Where a rejection was based *solely* on automated processing, the safeguards in **Articles 22A–22C UK GDPR (as amended by the Data (Use and Access) Act 2025, in force 5 February 2026)** entitle you to make representations, **obtain human intervention**, and contest the decision — the old blanket "Article 22 prohibition" framing is out of date; see Chapter 6.7. `[REGULATORY — DUAA 2025]` Note TestGorilla's own retention limits, which bound what can still exist: **candidate data is retained 2 years; webcam anti-cheat snapshots 6 months.** `[VENDOR]` If the employer stonewalls, you can complain to the **Information Commissioner's Office (ICO)**.

**Disclosing a disability.** If a false flag stems from a disability, disclosing it and requesting a reasonable adjustment under the **Equality Act 2010** is often the most effective route to a re-sit, because the duty to make reasonable adjustments is a legal obligation, not a favour — and TestGorilla's "condition never shared with the employer" policy lowers the personal cost of doing so.

**Realistic expectations.** Straightforward rank rejections are rarely overturned — the employer simply had stronger candidates. **Integrity flags are more contestable**, especially given the vendor's explicit "contact the candidate" guidance and any documented innocent cause. But SME recruiters move unpredictably, and a live role may fill before an appeal resolves — so the higher-value use of these rights is often evidence for next time.

**Template wording.**

*(a) Pre-assessment accommodations request (send before you sit):*
> Subject: Accommodation request — [your name], [role/ref]
> Dear [team], I have been invited to complete a TestGorilla assessment for [role]. I have [a disability/condition, e.g. dyslexia / ADHD] / I am a non-native English speaker, and I request the corresponding accommodation (additional assessment time). I understand the details of my condition are not shared with the employer. I can provide supporting documentation. Please confirm what can be arranged and the revised deadline. Thank you.

*(b) Post-rejection / flag query:*
> Subject: Assessment outcome — request for information — [name], [ref]
> Dear [team], Thank you for the update. So that I can improve, please could you tell me whether my performance on, or any anti-cheating flag arising from, the TestGorilla assessment contributed to the decision. If a behaviour was flagged, I would welcome the chance to explain it — [brief innocent explanation]. Thank you.

*(c) DSAR (escalation):*
> Subject: Data Subject Access Request — [name], [ref]
> Dear [team], Under Article 15 of the UK GDPR I request access to the personal data you hold about my application, specifically: my per-test assessment scores; my anti-cheating behaviour log, including the timestamped events and any behaviour-tier assigned; any webcam snapshots held; the logic of any automated decision-making (Articles 22A–22C UK GDPR, as amended by the Data (Use and Access) Act 2025); and whether a human was involved in the decision. Please respond within one month. Thank you.

---

## 10.12 Step-by-step: how to win this assessment

A numbered playbook from invitation to debrief.

1. **On invitation — read what you were sent.** The tests in the link tell you the role's priorities. Sent an Excel test and an IFRS test? That is a finance-operations or accounting screen — prepare the tools, not "aptitude tricks."
2. **T-minus — identify the skill tests and drill the real skill.** Excel, Xero, GAAP/IFRS, a coding stack — these are the most controllable marks in the whole assessment. Practise the actual tool against a clock. `[VENDOR library]`
3. **Diagnose the cognitive modules.** Sit one timed practice numerical/verbal/abstract set cold. Note your pacing at ~30–60s a question. Remember the modules are **fixed-form, so never leave a question you can reason at** — there is no adaptive penalty for a wrong answer beyond the lost mark.
4. **Prepare the behavioural pieces.** Read the employer's published values before the SJT. For Big 5 / DISC / 16-type, decide in advance which genuine, role-relevant facets of yourself to answer decisively from — do not fake.
5. **Sort accommodations now.** If you need +20% (non-native) or +50% (disability) time, request it in writing **before** you sit (§10.11a). Do not leave it to the day.
6. **Confirm the format in writing.** Ask whether webcam snapshots are on, whether any tool is permitted per test, and the time limits. This creates a record and tells you which integrity risks apply.
7. **Day before — set up the room.** Charge the laptop, test the connection (the timer won't pause on a drop), disconnect the second monitor, clear the desk, prepare a quiet closable room, and check the webcam and front lighting.
8. **30 minutes before.** Close everything, go **full-screen and single-tab**, enable Do Not Disturb, pause OS/security auto-updates (the top cause of an innocent full-screen exit), grant camera permission, do a two-minute warm-up on the practice questions.
9. **In-test discipline.** Stay **in frame, one tab, full-screen** the whole way. Use the 4–5 warm-up questions to calibrate. Pace to the per-test clock; answer every question you can reason at. If something genuinely forces you out of frame, be ready to explain it — the vendor's process invites that conversation.
10. **Debrief.** Immediately after, write three notes: which tests you actually got (for next time and this guide's accuracy), what went well, and what you'd change. If you suspect a flag, send the §10.11(b) query while the recruiter still has the log in view.

---

## 10.13 Sources for this chapter

All accessed 2026-08-01. Confidence tags as used above.

**Vendor (primary):**
- TestGorilla, *Test Library* — https://www.testgorilla.com/test-library/ `[VENDOR]`
- TestGorilla, *Cognitive-ability tests* — https://www.testgorilla.com/test-library/cognitive-ability-tests/ `[VENDOR]`
- TestGorilla, *Personality & culture tests* (Big 5, DISC subpages) — https://www.testgorilla.com/test-library/personality-culture-tests/ `[VENDOR]`
- TestGorilla, *Finance companies solutions* — https://www.testgorilla.com/solutions/finance-companies/ `[VENDOR]`
- TestGorilla blog, *Cheating detection in skills assessments* (KEY — candid on false positives) — https://www.testgorilla.com/blog/cheating-detection-skills-assessments/ `[VENDOR]`
- TestGorilla help-centre, *Understanding anti-cheating measures and behavior tiers* (403 to bot; title/snippets only) — https://support.testgorilla.com/hc/en-us/articles/9028797639451-Understanding-anti-cheating-measures-and-behavior-tiers `[VENDOR — tier definitions unresolved]`
- TestGorilla blog, *Questions & answers* (scoring, one-attempt retake) — https://www.testgorilla.com/blog/testgorilla-questions-answers/ `[VENDOR]`
- TestGorilla blog, *$70M Series A to eliminate hiring bias* — https://www.testgorilla.com/blog/testgorilla-secures-70m-series-a-funding-to-help-companies-eliminate-hiring-bias/ `[VENDOR]`
- TestGorilla, *Privacy policy* (retention: 2yr data / 6mo webcam) and *DPA* — https://www.testgorilla.com/privacy-policy/ ; https://www.testgorilla.com/dpa/ `[VENDOR]`
- TestGorilla candidate help, *Accessibility and accommodations* (403 to bot; snippet confirms +20%/+50% and June 2026 policy) — https://candidates.testgorilla.com/hc/en-us/articles/28302003990427-Accessibility-and-accommodations-for-assessments `[VENDOR]`

**Independent:**
- Balderton Capital, *TestGorilla secures $70M Series A* — https://www.balderton.com/news/testgorilla-secures-70m-series-a-to-help-companies-eliminate-hiring-bias/ `[INDEPENDENT]`
- UNLEASH, *TestGorilla secures $70M Series A* — https://www.unleash.ai/skills-development/testgorilla-secures-70m-in-series-a/ `[INDEPENDENT]`
- Tracxn company profile — https://tracxn.com/d/companies/testgorilla/ `[INDEPENDENT]`
- Capterra pricing — https://www.capterra.com/p/203823/TestGorilla/pricing/ `[INDEPENDENT — pricing an ESTIMATE, varies by source]`
- Trustpilot (1,707 reviews, TrustScore ~4/5) — https://uk.trustpilot.com/review/testgorilla.com `[INDEPENDENT — aggregate]`
- G2 discussions — https://www.g2.com/products/testgorilla/discuss `[INDEPENDENT — aggregate]`
- Buolamwini & Gebru (2018), *Gender Shades*; NIST FRVT demographic evaluations — face-detection accuracy disparities `[INDEPENDENT — full cite in §6.6]`

**Prep-vendor (format detail; corroborate — commercially biased):**
- JobTestPrep — https://www.jobtestprep.com/testgorilla-assessment-practice
- PrepClubs — https://prepclubs.com/tests/testgorilla
- iPrep — https://www.iprep.online/courses/testgorilla-practice-test/

**Candidate (testimony; thin — to deepen in gap audit):**
- No first-person UK candidate thread captured in this research; only G2/Trustpilot aggregate. `[CANDIDATE, n=0 direct — gap]`

*(Residual TestGorilla gaps — exact behaviour-tier definitions and candidate consent wording (both bot-blocked); whether a distinct mouse-leave/focus telemetry or an AI-answer/plagiarism detector exists; any independent validity / adverse-impact audit behind the "scientifically validated" claim; real norm-group / percentile methodology; per-module question counts; and first-person UK candidate testimony — are logged in research/10-testgorilla.md and the master gap register.)*
