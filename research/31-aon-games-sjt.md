# 31 — Aon (cut-e) Game-Based Assessments + SJT/Simulation Products — Raw Findings

**Researched:** 2026-08-18 (access dates on URLs as noted; default 2026-08-01 per project convention).
**Builds on:** `02-aon-cute.md` (do not duplicate; this file goes deeper on smartPredict games, chatAssess, squares).
**Tags:** [VENDOR] = Aon/cut-e primary; [PREP-VENDOR] = commercial prep site; [CANDIDATE] = forum/first-person; [INFERRED]; [UNKNOWN].

---

## 0. smartPredict — the official game roster [VENDOR via search snippet of aon-assessment-solutions.com]
Aon's own smartPredict page lists exactly **four** games, each mapped to a legacy cut-e scales instrument:
- **motionChallenge** — complex planning capability
- **gridChallenge** — executive attention
- **switchChallenge** — logical reasoning, "based on scales sx"
- **digitChallenge** — numeracy, "based on scales eql"
Each can be used in isolation or combined with each other/other Aon tests. [VENDOR snippet — URL: https://www.aon-assessment-solutions.com/nc/us/details/gamified-smartphone-optimized-assessment-series-smartpredict/ — direct fetch failed (DNS), content via Google snippet, accessed 2026-08-18]
- No fifth "focus/attention" standalone game found under smartPredict branding; the attention construct is covered by gridChallenge (executive attention) and the separate non-game scales e3+ concentration test (see file 02). [INFERRED from roster]
- Marketing claim: games capture "over a thousand behavioural data points" (reaction time, learning rate, error recovery, effort under pressure). [VENDOR-marketing, repeated by PREP-VENDORs — treat as unverified]

## 1. switchChallenge (deductive logic / "funnel" game)
- **Legacy basis:** cut-e **scales sx** (deductive reasoning). [VENDOR snippet]
- **Mechanic:** two rows of abstract symbols (three rows at harder levels); the upper row is transformed into the lower row by an "operator"/funnel represented as a **4-digit number giving the new positions of symbols** — candidate must identify which operator produces the shown output. [PREP-VENDOR: JobTestPrep]
- **Duration:** 6 minutes standard (some deployments 3 minutes); unlimited tasks — do as many as possible. [PREP-VENDOR: JobTestPrep, GraduatesFirst]
- **Adaptive:** YES — difficulty escalates with correct answers (more symbols, more/chained operators); **incorrect answers demote you to easier items**. [PREP-VENDOR: JobTestPrep]
- **Scoring:** quantity/level-based within time — score potential is capped if you get demoted early; i.e. the score reflects the difficulty level reached plus number correct, not just raw accuracy. Exact algorithm [UNKNOWN — Aon does not publish]. [PREP-VENDOR]
- **Winning technique:** prioritise accuracy on the first items (early errors are disproportionately costly under adaptivity); then speed up. [PREP-VENDOR: JobTestPrep tip]
- TODO: rounds/escalation detail, error-penalty specifics, telemetry.

## 2. gridChallenge (memory + interference loop)
- **Construct:** "executive attention" (working memory under interference). [VENDOR snippet]
- **Mechanic:** memorise highlighted dot position(s) on a grid → intervening distractor tasks (symmetry judgements, rotation checks) → recall dot positions **in order**. Load grows to 3–5 dots per round. [PREP-VENDOR: JobTestPrep, GraduatesFirst]
- **Duration/rounds:** 9 minutes, ~9 rounds. [PREP-VENDOR: GraduatesFirst]
- **Adaptive:** No (per JobTestPrep). [PREP-VENDOR — conflicts: none found yet]
- **Scoring:** accuracy on combined memory + interference questions. Exact weighting memory vs distractor accuracy [UNKNOWN].
- TODO: detail on ordered recall, P&G variant.

## 3. digitChallenge (mental arithmetic)
- **Legacy basis:** scales eql. [VENDOR snippet]
- **Mechanic:** shown a completed answer; fill in missing digits/figures (and possibly operators) to make the equation true — addition, subtraction, multiplication. [PREP-VENDOR]
- **Duration:** 5 minutes, unlimited tasks, escalating. [PREP-VENDOR]
- **Adaptive:** YES (JobTestPrep). **Scoring:** speed + accuracy; demotion on errors → same "protect early accuracy" technique. [PREP-VENDOR]

## 4. motionChallenge (planning / Rush-Hour-like)
- **Mechanic:** ball on a grid with ≥1 exit; slide movable obstacles (horizontal/vertical, only if path clear) to get ball to exit **in as few moves as possible**; immovable obstacles appear at higher difficulty. [PREP-VENDOR]
- **Duration:** 6 minutes, unlimited tasks, escalating. **Adaptive:** YES. [PREP-VENDOR]
- **Scoring:** "quantity of puzzles solved efficiently" — move-count efficiency appears to matter, not just completion. Exact penalty for excess moves [UNKNOWN]. [PREP-VENDOR: JobTestPrep]
- TODO: planning-time telemetry (does thinking-before-first-move get measured?).

## 5. Other gamified/adjacent products
- Short-term memory test (non-game): 5 min, 10 tasks, 8s exposure/7s gap — see file 02.
- TODO: sweep for any additional games (e.g. Aon "focus"?), vidAssess-AI overlap, other simulations.

## 6. chatAssess (chat-based SJT)
- **Format:** simulated messenger/chat conversation; scenario messages "arrive" from virtual colleagues; candidate picks from multiple-choice replies. Marketed as gamified SJT. [PREP-VENDOR]
- **Duration:** ~20 min (file 02); JobTestPrep sells a "90-minute chatAssess simulation" — likely their extended practice, not real length. [PREP-VENDOR — conflict noted]
- **Scoring:** responses compared against employer-keyed "best fit" answers; benchmarked vs norm group → percentile; per-competency sub-scores (e.g. communication, drive, analysis, people skills). Often untimed but **response latency may be recorded**. [PREP-VENDOR: general SJT + chatAssess sources]
- **Bespoke per employer:** content and keying customised (values/competency model of the client). [PREP-VENDOR/INFERRED]
- TODO: message-flow mechanics, employer examples (Morgan Stanley inbox SJT?), anti-fake.

## 7. squares (integrity questionnaire)
- **Vendor positioning:** integrity test predicting **counterproductive work behaviour (CWB)** — vendor page exists at cut-e.com/online-assessment/integrity-test/ (direct fetch failed DNS; content via snippets). [VENDOR via snippet]
- **Model:** situational model of CWB — "does not stigmatise" results, framed as trainable, to increase acceptance. CWB kinds listed: distraction, boredom, superficiality, indifference, ambiguity, opportunism. [VENDOR snippet]
- **Format:** online situational behaviour questionnaire, **~150 questions**; measures **six scales**: empathetic, honest, reflective, disciplined, conscientious, cautious ("ethical awareness" + "impulse control"). Valid for all job positions. [VENDOR snippet + PREP-VENDOR: psychometrictests.org/wikijob]
- **Scoring / faking detection:** [UNKNOWN — TODO]
- TODO: duration, faking/social-desirability handling, whether percentile or risk-band output.

## 8. Job simulations / other SJT products beyond these
- vidAssess-AI (video, AI-scored) — covered in file 02.
- TODO: any Aon "virtual assessment center", pilot simulations (flight/ATC uses of cut-e), other sims.

## 9. Practice resources per game [PREP-VENDOR]
- **JobTestPrep smartPredict pack** (paid): interactive replicas of all four games, unlimited algorithm-generated items, 3 diagrammatic tests, 8 math tests, 2 guides; tiered subscription (1wk/1mo/3mo), money-back guarantee. https://www.jobtestprep.co.uk/aon-smartpredict-challenges-practice (accessed 2026-08-18)
- **JobTestPrep chatAssess pack** (paid): 90-min simulation + 15 SJTs + guide. https://www.jobtestprep.com/chatassess-test (accessed 2026-08-18)
- **AssessmentDay gamified page** (free samples): https://www.assessmentday.com/gamified-assessments.htm
- TODO: free options, GraduatesFirst, WikiJob squares course.

## 10. Candidate testimony
- TODO: TSR + Reddit sweeps.

## 11. Anti-cheat relevance (games/SJT specific)
- Item-level randomisation + adaptivity means answer-sharing has low value for games. [INFERRED + file 02]
- TODO: any game-specific telemetry claims (mouse/touch patterns).

## SOURCES so far (accessed 2026-08-18 unless noted)
- JobTestPrep smartPredict (PREP-VENDOR): https://www.jobtestprep.co.uk/aon-smartpredict-challenges-practice
- Aon smartPredict product page [VENDOR, via snippet only]: https://www.aon-assessment-solutions.com/nc/us/details/gamified-smartphone-optimized-assessment-series-smartpredict/
- cut-e integrity/squares page [VENDOR, via snippet only]: https://www.cut-e.com/online-assessment/integrity-test/
- Aon game-based assessments PDF [VENDOR — downloaded, to read]: https://www.aon.com/getmedia/341ef8dd-4b2c-4ebc-994e-a3af91b144ef/game-based-assessments.pdf.aspx
- JobTestPrep chatAssess (PREP-VENDOR): https://www.jobtestprep.com/chatassess-test
- psychometrictests.org cut-e (PREP-VENDOR): https://www.psychometrictests.org/publishers/cut-e/
- WikiJob cut-e personality & integrity course (PREP-VENDOR): https://www.wikijob.co.uk/course/cut-e-personality-and-integrity-tests-aon-63179189
