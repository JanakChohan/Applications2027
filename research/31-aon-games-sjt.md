# 31 — Aon (cut-e) Game-Based Assessments + SJT/Simulation Products — Raw Findings

**Researched:** 2026-08-18 (URLs accessed 2026-08-18; project convention date 2026-08-01 where carried over from file 02).
**Builds on:** `02-aon-cute.md` (ownership, scales battery, negative-marking finding, employer map — not repeated here).
**Tags:** [VENDOR] = Aon/cut-e primary; [PREP-VENDOR] = commercial prep site; [CANDIDATE] = forum/first-person; [INFERRED]; [UNKNOWN]. Conflicts recorded both ways.

---

## 0. smartPredict — the official game roster
Aon's own smartPredict product page lists exactly **four** games, each explicitly mapped to a legacy cut-e scales instrument:
- **motionChallenge** — "complex planning capability"
- **gridChallenge** — "executive attention"
- **switchChallenge** — "logical reasoning (based on scales sx)"
- **digitChallenge** — "numeracy (based on scales eql)"
"Each smartPredict challenge can be used in isolation or in combination with the others, and also in combination with all other Aon tests." [VENDOR — URL: https://www.aon-assessment-solutions.com/nc/us/details/gamified-smartphone-optimized-assessment-series-smartpredict/ ; direct fetch failed (DNS via proxy), wording captured via Google result snippet, accessed 2026-08-18]
- **No fifth game exists under smartPredict branding** (no separate "focus"/proximity game found). The attention construct is gridChallenge; sustained concentration is the non-game scales e3+ (file 02). [INFERRED from vendor roster + prep-vendor sweep]
- Marketing claim: games capture **"over a thousand behavioural data points"** (reaction time, learning rate, error recovery, effort under pressure). [VENDOR-marketing, echoed by PREP-VENDORs — no published telemetry spec; exact data points captured = [UNKNOWN]]
- Designed smartphone-first ("gamified smartphone-optimized assessment series"). [VENDOR page title]
- Scale of operation context: Aon Assessment Solutions claims **30 million assessments/year, 90 countries, 40 languages**. [VENDOR — Rolls-Royce case-study PDF, https://www.aon.com/getmedia/341ef8dd-4b2c-4ebc-994e-a3af91b144ef/game-based-assessments.pdf.aspx]

---

## 1. switchChallenge (deductive "funnel" logic game) — DEEP DETAIL
- **Legacy basis:** cut-e **scales sx** deductive reasoning. [VENDOR snippet]
- **Mechanic:** each task shows two rows of abstract symbols (three rows in harder levels). The upper row has been transformed into the lower row by passing through a "funnel"/**operator represented as a 4-digit number** — the digits give the new order of the symbol positions (e.g. operator 3421 = the 3rd symbol comes first, etc.). Candidate must pick which operator (from options) produces the shown re-ordering. Harder levels chain multiple funnels/operators. [PREP-VENDOR: JobTestPrep UK + 12minprep search snippet, consistent]
- **Instructions to candidate:** solve as many as possible in the time; select the operator that explains the switch. [PREP-VENDOR]
- **Duration:** **6 minutes standard; a 3-minute variant exists** at some employers. Unlimited item supply. [PREP-VENDOR: JobTestPrep, 12minprep — consistent]
- **Rounds/escalation:** no fixed round structure — continuous item stream; escalation = more symbols per row, 2 rows → 3 rows, single operator → multiple chained operators. [PREP-VENDOR]
- **Adaptive & SCORING (top priority):** YES, adaptive — "difficulty level of the items will change according to your answer pattern" [PREP-VENDOR: 12minprep]. JobTestPrep: correct answers promote you to harder items; **incorrect answers demote you to easier content, "limiting your score potential"**. Score is therefore effectively **level-reached × volume-correct within time** (quantity-based on an adaptive ladder), reported as a **percentile vs norm group** (consistent with file 02's finding that adaptive cut-e tests yield stable percentile estimates). Whether an explicit per-wrong-answer point deduction applies (as on non-game scales tests — see file 02 negative-marking finding) is **[UNKNOWN] for the games specifically**; the documented penalty mechanism for games is DEMOTION, not stated point subtraction. [PREP-VENDOR; exact algorithm unpublished by Aon]
- **Is over-caution penalised?** Indirectly yes: with unlimited items in 6 min, slow-but-perfect play caps volume and level progression; but the adaptive demotion makes early errors costlier than lost seconds. [INFERRED from mechanics]
- **Winning technique:** [PREP-VENDOR: JobTestPrep] "Ace early questions" — protect accuracy at the start to climb the ladder, then increase speed; practise reading 4-digit operators as position maps rather than re-deriving each symbol.
- **Anti-cheat relevance:** adaptive + generated item stream → answer keys valueless; a stand-in solver is the main threat (no in-game verification documented — [UNKNOWN]). [INFERRED]

## 2. gridChallenge (memory + interference loop) — DEEP DETAIL
- **Construct:** "executive attention" [VENDOR snippet] — working memory maintenance under processing interference (classic complex-span design). [INFERRED characterisation]
- **Mechanic / the loop:** (1) a grid of dots is shown with one dot highlighted — memorise its location; (2) one or more **distractor tasks** interleave: symmetry judgements (is the figure mirror-symmetric?), rotation checks (matched at 90°/180°/270°?), or shape addition/subtraction "combination" questions; (3) another dot to memorise; loop repeats; (4) at round end, **recall the highlighted dot locations, in order**. Memory load per round: **3–5 dots**, with a matching 3–5 interleaved spatial questions. [PREP-VENDOR: JobTestPrep US grid-challenge page + UK page, consistent]
- **Instructions:** remember every highlighted dot in sequence while answering the interleaved questions correctly. [PREP-VENDOR]
- **Duration/rounds — CONFLICT:** JobTestPrep UK & GraduatesFirst: **9 minutes, ~9 rounds**. JobTestPrep US (P&G page): **6 minutes**. Both [PREP-VENDOR]; likely employer-variant lengths — treat as 6–9 min. 
- **Adaptive — CONFLICT:** JobTestPrep UK summary said not adaptive; JobTestPrep US P&G page says **"computer-based and adaptive — difficulty adjusts in real time"; correct answers trigger harder questions "worth more points", incorrect answers yield easier questions "worth fewer points", and "the more questions you get wrong, the harder it is to recover and achieve a good grade."** [PREP-VENDOR both ways; US page is more detailed/recent → lean adaptive, flag conflict]
- **SCORING:** combined accuracy across memory recalls AND distractor answers, on a point-weighted adaptive ladder (per US page); weighting between memory vs interference accuracy [UNKNOWN]. Output = percentile vs norm. Errors are penalised via demotion to lower-value items (explicit point deduction [UNKNOWN]). [PREP-VENDOR]
- **Winning technique:** don't sacrifice the distractor questions to rehearse dots (both are scored); use spatial chunking/verbal encoding for dot positions; answer symmetry items fast — they are the recoverable part. [PREP-VENDOR tips, paraphrased]
- **Employer note:** core component of **P&G's "Interactive Assessment"** (with switchChallenge + digitChallenge + PEAK Performance); JobTestPrep claims **<20% pass** P&G's full interactive assessment and a **12-month reapply cooldown** on failure. [PREP-VENDOR — P&G-specific, unverified by P&G]

## 3. digitChallenge (mental arithmetic game)
- **Legacy basis:** scales eql (basic numeracy). [VENDOR snippet]
- **Mechanic:** inverted arithmetic — you are shown the **answer** and an equation with missing figures; fill in the missing digits (addition, subtraction, multiplication) to make it true. [PREP-VENDOR: JobTestPrep — consistent with GraduatesFirst in file 02 which adds missing operators as well]
- **Duration:** 5 minutes, unlimited tasks. [PREP-VENDOR]
- **Adaptive & scoring:** YES adaptive (JobTestPrep); scored on **speed + accuracy within time**, with demotion on errors → same "protect early accuracy" dynamic. Percentile output. Exact points model [UNKNOWN]. [PREP-VENDOR]
- **Winning technique:** work backwards from the units digit; know times tables cold; accuracy first on early items. [PREP-VENDOR]

## 4. motionChallenge (planning, Rush-Hour-like)
- **Construct:** "complex planning capability." [VENDOR snippet]
- **Mechanic:** a ball sits on a grid with ≥1 exit; differently-sized obstacles block the path; movable obstacles slide horizontally/vertically only if the path is clear; get the ball to the exit **in as few moves as possible**. Escalation: larger and **immovable** obstacles appear. [PREP-VENDOR: JobTestPrep, 24practice-style guides consistent]
- **Duration:** 6 minutes, unlimited tasks. **Adaptive:** YES. [PREP-VENDOR]
- **SCORING:** "quantity of puzzles solved efficiently" — i.e. both throughput and **move-count efficiency** count; a solved puzzle with excess moves is worth less (exact penalty [UNKNOWN]). Percentile output. Whether planning latency before the first move is itself scored (a plausible behavioural-data-point) is **[UNKNOWN]** — vendors market "planning behaviour" capture but publish nothing. [PREP-VENDOR + VENDOR-marketing]
- **Winning technique:** plan the full move sequence before touching anything (moves, not time, are the scarce currency per puzzle); work backwards from the exit. [PREP-VENDOR tips]

## 5. Other gamified / adjacent products
- **Short-term memory test** (non-game module): 5 min, 10 tasks, 8s exposure/7s gap, no pause — see file 02. [PREP-VENDOR]
- **Pilot/aviation batteries:** cut-e scales instruments are heavily used in airline pilot selection (dedicated guides exist, e.g. pilotaptitudetest.com Aon/cut-e guide) — same instruments, aviation norm groups; not separate games. [PREP-VENDOR — https://pilotaptitudetest.com/aon-cut-e-pilot-assessment-guide-2026/]
- No evidence found of additional smartPredict games beyond the four. [Sweep result, 2026-08-18]

## 6. chatAssess (chat-based SJT / job simulation)
- **Format [VENDOR — Rolls-Royce case PDF]:** "A customised situational judgement questionnaire **embedded into an instant messaging simulation for smart devices**." Screenshots show a messenger UI (smartplayer.cut-e.com) with named virtual colleagues (e.g. "Sarah Walford", "Daniel Popper") sending messages; candidate replies via selectable message bubbles.
- **Mechanic:** scenario messages arrive live from multiple virtual colleagues; candidate picks from **multiple-choice reply options**; messages **may include media (images/videos)**; **additional messages arrive during the assessment, including replies to your responses** — i.e. a flowing conversation, though whether branching depends on your prior answers is [UNKNOWN — one prep source implies replies arrive, not confirmed adaptive branching]. [PREP-VENDOR: JobTestPrep/graduatesfirst-sphere snippets]
- **Duration:** **~20 minutes** [PREP-VENDOR, consistent with file 02]. (JobTestPrep's "90-minute chatAssess simulation" is their practice product length, NOT the real test — [PREP-VENDOR, conflict resolved].) Individual replies: overall time limit rather than per-message timer per most sources; **response latency may be recorded even when "untimed"**. [PREP-VENDOR]
- **SCORING:** answers compared to employer-keyed "best-fit" responses (keying set with the hiring organisation); benchmarked against a norm group → **percentile + per-competency sub-scores** (e.g. communication, drive, analysis, people skills / decision-making, adaptability, social interaction, workplace judgment). No universal pass mark; "right" answers tie to the employer's values/culture. [PREP-VENDOR: jobtestprep.com/chatassess-test + SJT guides]
- **Bespoke per employer — CONFIRMED [VENDOR]:** the Rolls-Royce case study explicitly calls it "a **customised** situational judgement questionnaire" built for RR's Business and Engineering streams. Morgan Stanley named by JobTestPrep among finance users (alongside Deloitte, Credit Suisse) [PREP-VENDOR]; the specific "Morgan Stanley email-inbox SJT keyed to Business Unit" claim: **not verified in this sweep — [UNKNOWN], check employer-specific chapter**.
- **Vendor validity/engagement claims [VENDOR — Rolls-Royce PDF, tag all as vendor case-study marketing]:**
  - High chatAssess scorers **50% more likely to get a job**; **65% more likely to perform highly at the Assessment Centre**.
  - Completion rates rose with chatAssess: Business stream 74%→96%, Engineering 81%→95%; 9,691 applicants → 9,138 completed all online tests (~98%).
  - **>60% of graduates prefer chatAssess** to previous online assessments; 75%+ rated experience good/very good.
- **Anti-fake:** SJT keying is employer-specific and scenarios are not per-candidate randomised (file 02: SJT/personality excluded from unique-item-bank generation) → answer-sharing is theoretically possible within one employer's cycle; mitigation is content refresh + latency telemetry [INFERRED; specifics [UNKNOWN]].

## 7. squares (integrity / CWB questionnaire) — CONFIRMED EXISTS
- **Vendor positioning [VENDOR via snippet — https://www.cut-e.com/online-assessment/integrity-test/, DNS-blocked for direct fetch]:** integrity test to "predict unproductive behaviours at work" — identifies proneness to **counterproductive work behaviour (CWB)**: "distraction, boredom, superficiality, indifference, ambiguity, opportunism." Based on a **situational model of CWB** ("takes into account the individual's specific situation… does not stigmatise… offers the opportunity for change through training", improving acceptance of results). Valid for all job positions.
- **Six scales:** how **empathetic, honest, reflective, disciplined, conscientious, cautious** the candidate is — grouped as ethical awareness + impulse control. [VENDOR snippet + PREP-VENDOR]
- **Format — CONFLICT to flag:** psychometrictests.org: self-assessment, **~10 minutes**, statements rated on a **sliding scale with three anchors — "holds less true for me than for others" / "equally true" / "more true for me than for others"** (any position selectable) — i.e. a self-vs-others comparative slider, same idiom as shapes/views. [PREP-VENDOR — https://www.psychometrictests.org/publishers/cut-e/] vs. an earlier search-snippet claim of **~150 questions** [PREP-VENDOR, source in wikijob/jobtestprep sphere]. 150 items in 10 min is implausible; likely the 150 figure conflates squares with the full shapes personality battery, or duration is longer. Record both; exact item count [UNKNOWN].
- **SCORING:** scores on the six scales are **compared against an "ideal candidate" profile** (alongside cut-e shapes results where both are used) — i.e. profile-match, not a simple percentile ladder; risk-flag output for CWB-proneness. [PREP-VENDOR: psychometrictests.org]
- **Faking detection:** **[UNKNOWN]** — no source in this sweep documents a lie/social-desirability scale for squares. The self-vs-others comparative slider format is itself argued (for cut-e's shapes/views family) to resist extreme-response faking [INFERRED from format; not vendor-confirmed for squares]. Flag for gap audit.
- **WikiJob has a dedicated paid course** "cut-e Personality and Integrity Tests (Aon)" — page 404'd on fetch (course may be retired); URL: https://www.wikijob.co.uk/course/cut-e-personality-and-integrity-tests-aon-63179189 [PREP-VENDOR, dead-link 2026-08-18]

## 8. Job simulations / virtual assessments beyond these
- **vidAssess-AI** — async video interview, AI-NLP-scored (file 02; not re-researched here).
- **chatAssess is Aon's flagship "job simulation"-style product** per vendor materials; no separate virtual-assessment-centre product surfaced in this sweep — Aon markets assessment-centre *services* (human-run) rather than a packaged VR/virtual AC tool. [Sweep result — [UNKNOWN] whether a virtual AC platform exists; check Aon corporate pages in gap audit]
- ATS integration: cut-e integrates with Taleo etc. (Rolls-Royce: seamless flow for 40,000+ candidates/yr). [VENDOR PDF]

## 9. Practice resources per game [PREP-VENDOR throughout]
**Paid:**
- **JobTestPrep smartPredict pack** — interactive replicas of all four games with **unlimited algorithm-generated questions**, + 3 diagrammatic tests, 8 maths tests, 2 study guides; tiered subscription (1 week / 1 month / 3 months), money-back guarantee. https://www.jobtestprep.co.uk/aon-smartpredict-challenges-practice (accessed 2026-08-18). US mirror: https://www.jobtestprep.com/aon-smartpredict
- **JobTestPrep P&G Grid Challenge pack** (P&G-flavoured grid+switch+digit): https://www.jobtestprep.com/grid-challenge-test
- **JobTestPrep chatAssess pack** — 90-min extended simulation + 15 SJT practice tests (5 graduate / 4 administrative / 5 management) + study guide + per-question explanations: https://www.jobtestprep.com/chatassess-test and https://www.jobtestprep.co.uk/chatassess
- **12minprep Switch Challenge course** (free practice + paid course claimed): https://www.12minprep.com/knowledge-hub/switch-challenge-test/ (403 on direct fetch 2026-08-18 — content via snippet)
**Free:**
- **AssessmentDay gamified assessments page** (free samples incl. Aon-style): https://www.assessmentday.com/gamified-assessments.htm
- **GraduatesFirst Aon/cut-e guide** (free explanations + some free questions): https://www.graduatesfirst.com/aon-cut-e-practice-assessments
- **24practice free Aon guide:** https://24practice.com/aon-formerly-cut%E2%80%91e-assessment-tests/
- **Aon's own YouTube demo** "smartPredict by Aon – the challenge series": https://www.youtube.com/watch?v=EWQ_SKqURRM [VENDOR — shows real game UI; best free look at authentic mechanics]
- Practice-relevance note: because real games are adaptive with generated items, memorising questions is useless — practice value is **mechanic familiarity + speed automation** (esp. reading 4-digit operators and Rush-Hour heuristics). [INFERRED]

## 10. Candidate testimony
- **The Student Room — 2026 BNP Paribas Graduate Online Test thread** (https://www.thestudentroom.co.uk/showthread.php?t=7622761 — direct fetch 403'd; via search snippet): BNP online tests included numerical, verbal, logical and **switchchallenge**; candidates describe the **switch challenge as "always demanding"** and the verbal reasoning as particularly hard. [CANDIDATE, thin — snippet only]
- Confirms file 02 note that candidate communities still say "cut-e" not "Aon". [CANDIDATE]
- Reddit sweep returned prep-vendor pages, no substantive threads captured this pass — **residual gap**: deeper Reddit/TSR mining for per-game scores/percentiles. [UNKNOWN]

## 11. Anti-cheat relevance (games/SJT-specific synthesis)
- **Games:** per-candidate generated item streams + adaptivity ⇒ leaked answer keys are worthless; the realistic cheat is a proxy test-taker or a solver tool. No game-specific tab-switch/telemetry disclosure found (consistent with file 02 gap). [INFERRED + [UNKNOWN]]
- **Behavioural data points** ("1000+") are marketed partly as consistency/effort signals, which could function as anomaly detection (e.g. superhuman response uniformity) — **no vendor documentation that they are used for cheat detection**; tag as [VENDOR-marketing]/[UNKNOWN].
- **chatAssess/squares:** fixed (non-randomised) content keyed per employer ⇒ within-cohort answer sharing is the exposure; latency recording is the only hinted countermeasure. [PREP-VENDOR/INFERRED]

---

## SOURCES (accessed 2026-08-18)
**Vendor-primary:**
- Aon/cut-e Rolls-Royce chatAssess case study PDF (fetched + read in full): https://www.aon.com/getmedia/341ef8dd-4b2c-4ebc-994e-a3af91b144ef/game-based-assessments.pdf.aspx
- Aon smartPredict product page [snippet only — DNS-blocked]: https://www.aon-assessment-solutions.com/nc/us/details/gamified-smartphone-optimized-assessment-series-smartpredict/
- cut-e integrity (squares) page [snippet only — DNS-blocked]: https://www.cut-e.com/online-assessment/integrity-test/
- Aon smartPredict demo video: https://www.youtube.com/watch?v=EWQ_SKqURRM
**Prep-vendor (fetched in full):**
- JobTestPrep UK smartPredict: https://www.jobtestprep.co.uk/aon-smartpredict-challenges-practice
- JobTestPrep US Grid Challenge / P&G: https://www.jobtestprep.com/grid-challenge-test
- JobTestPrep US chatAssess: https://www.jobtestprep.com/chatassess-test
- JobTestPrep UK chatAssess: https://www.jobtestprep.co.uk/chatassess
- psychometrictests.org cut-e (squares detail): https://www.psychometrictests.org/publishers/cut-e/
**Prep-vendor (snippet-level):**
- 12minprep switchChallenge: https://www.12minprep.com/knowledge-hub/switch-challenge-test/ (403)
- WikiJob cut-e Personality & Integrity course: https://www.wikijob.co.uk/course/cut-e-personality-and-integrity-tests-aon-63179189 (404 — possibly retired)
- 24practice Aon guide: https://24practice.com/aon-formerly-cut%E2%80%91e-assessment-tests/
- pilotaptitudetest.com Aon guide: https://pilotaptitudetest.com/aon-cut-e-pilot-assessment-guide-2026/
**Candidate:**
- TSR BNP Paribas 2026 thread (snippet; 403 on fetch): https://www.thestudentroom.co.uk/showthread.php?t=7622761

## RESIDUAL GAPS ([UNKNOWN] register)
- Exact scoring algorithms for all four games (point values per difficulty tier; whether explicit deduction exists on games as it does on scales tests).
- gridChallenge duration/adaptivity conflict (6 vs 9 min; adaptive vs not) — employer-variant hypothesis unconfirmed.
- squares item count (10-min slider format vs "~150 questions" claim) and any faking/SD scale.
- chatAssess branching (do prior answers change subsequent messages?); Morgan Stanley inbox-SJT specifics.
- Game telemetry specifics (planning latency, touch patterns) and any anti-cheat use of behavioural data.
- Deep Reddit/TSR first-person accounts with real score/percentile outcomes.
- Whether Aon offers a packaged virtual assessment centre product.
