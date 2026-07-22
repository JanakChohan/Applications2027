# Phase 1 Research Findings — Aon / cut-e "scales" Assessments

**Purpose:** Ground-truth research to drive a *legitimate practice* app. Nothing here is for use during a live assessment.
**Date compiled:** 2026-07-22
**Method:** Four parallel web-research passes reading primary (Aon's own practice PDF) and secondary sources (JobTestPrep, AssessmentDay, Practice Aptitude Tests, GraduatesFirst, psychometric-success, psychometrictests.org, fintest.io, MConsultingPrep, 123test, graduatemonkey). Every claim carries a **confidence rating** and a source. Where sources conflict, both sides are shown and left unresolved rather than forced.

**Confidence key:** **High** = primary Aon source or unanimous across established vendors · **Medium** = several vendors agree, no primary confirmation · **Low** = single/low-authority source or my own synthesis.

**Source-authority note:** I separate *established* vendors (AssessmentDay, JobTestPrep, Practice Aptitude Tests, psychometric-success, psychometrictests.org, fintest.io, GraduatesFirst, 123test, MConsultingPrep) from *low-authority / likely-AI-generated* sites (testsolve.ai, careertestprep.com, forgeprep.io, prepclubs.com). Low-authority sites produce confident but unverifiable specifics (e.g. "70% accuracy yields Stanine 7"); their unique claims are rated **Low** and flagged.

---

## 0. Headline correction to the brief

You described the test as **~18 questions in ~12 minutes, ~6 tabbed data displays, True/False/Cannot Say**. Three of those four facts are confirmed exactly. The **18-questions-in-12-minutes** figure does **not** match any documented form:

| Documented form | Items | Time | Pace |
|---|---|---|---|
| scales numerical — **full/long** | **37 tasks** | **12 min** | ~19–20 s/item |
| scales numerical — **short** | **18 tasks** | **6 min** | ~20 s/item |

Your "**18 in 12 min**" almost certainly = the **short-form item count (18) fused with the long-form time limit (12 min)** from memory, **or** a client-configured form (Aon tailors length by role/sector), **or** you reached ~18 items of a 37-item form before time ran out (these tests are deliberately not finishable). **Confidence: High** that the real published pace is **~20 s/item, not the ~40 s/item that "18 in 12 min" implies.** This matters a lot for the app's timing model — see SPEC.

**What this means for the build:** the app defaults to the **authentic ~20 s/item pace**, and offers both real forms (37/12:00 and 18/6:00) plus your remembered "18 in 12:00" as a gentler configurable option, clearly labelled as non-standard.

---

## 1. Which exact test — and the family

### The match: **Aon "scales numerical"** (a.k.a. cut-e Numerical Ability / scales cls-numerical). Confidence: **High.**

The signature — **~6 data displays (graphs/tables) as clickable tabs above the question**, each question a **statement judged True / False / Cannot Say** — is unique to **scales numerical**. The only other tab-based T/F/CS test is **scales verbal**, but that uses *written text* data sheets, not graphs/tables. You saw graphs/tables → numerical. `smartPredict`, `gridChallenge`, `scales cls`-inductive are ruled out (no T/F/CS-over-charts format).

- *"At the top of your screen are several tabs; each has a chart, table or diagram that displays data regarding different aspects of the task."* — JobTestPrep (High)
- Example six-tab sets from sources: `Income · Costs · Market Shares · Employees · Return on Equity · Outlook`; `Revenues · Expenses · R&D Costs · Regional Growth · Stocks · Future Value`. (High that data spreads across ~6 tabs.)
- Three **subject versions** exist (consumer / finance / industrial); *"the difference is not in the level of difficulty... but subject matter only"* — graduatemonkey (Medium).

### The wider "scales" + smartPredict family (employers often combine these)

| Test | Measures | Format | Timing / items | Confidence |
|---|---|---|---|---|
| **scales numerical** | Interpret data in charts/tables | Statement → T/F/CS across ~6 tabs | 37/12 min (full), 18/6 min (short) | High |
| **scales verbal** | Logical conclusions from text | T/F/CS across topic tabs (text sheets) | 12 min; ~47–49 tasks *(sources: 47 vs 49)* | High format / Medium count |
| **scales eql** (digitChallenge) | Basic mental arithmetic | Fill missing digits 1–9, **no calculator** | ~5 min; ~15 tasks | Med-High |
| **scales lst / gapChallenge** | Deductive logic | Sudoku-like symbol grids | ~6 min | Med-High |
| **switchChallenge (scales sx)** | Deductive-logical | Identify the operator reordering figures | ~6 min, **adaptive** | High |
| **gridChallenge (scales e3+)** | Working memory / spatial | Recall dot sequences w/ distractors | ~9 min; ~9 rounds | High format / *adaptivity disputed* |
| **smartPredict** | Gamified battery | switch + grid + digit + motion challenges | each 5–9 min; mobile-first, adaptive | High |
| **scales cls** (inductive) | Inductive rule inference | Categorise number/letter/colour grids by rule | 12 min; 12 tasks | Med-High |

**Naming ambiguity flagged:** the brief's "scales cls = I-M-P checking / applied numeracy" label is **not corroborated** — sources describe `cls` as *inductive rule/pattern categorisation*. cut-e's logic-test naming (cls / clx / ix) is inconsistent across sources. Confidence on the "I-M-P checking" label specifically: **Low.**

---

## 2. How it is actually scored (the most important section)

| Property | Finding | Confidence |
|---|---|---|
| **Number-correct vs speed-weighted** | **Accuracy-based** (number correct minus penalty). Speed matters only *indirectly* — pressure means faster candidates attempt more items. **No per-item time bonus** on scales numerical/verbal. (Reaction-time weighting is real but only on cut-e *integrity/personality* "squares" and the *gamified* smartPredict challenges.) | Med-High |
| **Adaptive?** | Standard scales numerical/verbal are **NOT item-by-item adaptive (not CAT/IRT)**. They are **fixed-length tests drawn from a large randomized item bank** — each candidate gets a different, roughly equal-difficulty set (anti-cheat parallel forms). **Load-bearing evidence:** free back-navigation + answer-changing is *incompatible* with item-by-item adaptive selection. Aon *does* sell separately-adaptive products (smartPredict). Some sites loosely mislabel scales as "adaptive." | Med-High |
| **Wrong answers penalised?** | **YES — negative marking.** *"you are deducted one mark for every incorrect answer"* (psychometrictests.org); *"points are given for correct answers and deducted for incorrect ones... different from SHL, where there are no penalties"* (MConsultingPrep). | **High** |
| **Unanswered = wrong?** | **No.** A blank scores **0** (not negative); a wrong answer scores **negative**. Therefore **skipping beats blind guessing**. But blanks earn no points, so they still cap your raw score. | **High** |
| **Penalty magnitude** | Flat **−1 per wrong** is the best-supported figure (psychometric-success, psychometrictests.org). A fractional −⅓/−¼ "formula scoring" claim appears **only in low-authority sites** and is likely fabricated. Exact ratio not confirmed by any Aon primary source. | High (penalty exists) / Low (exact ratio) |
| **Norm-referenced?** | **YES.** No universal pass mark. Raw score → compared against a **norm/comparison group**, reported as **percentile + Stanine (1–9)** (Stanine 5 = average, 9 = top). *"There is no set pass mark... Each employer sets its own benchmark"* (Practice Aptitude Tests). Norm groups ≈ country + role-type (e.g. graduate) pools; cut-e's Hamburg heritage makes Stanine reporting natural. | High (norm-ref) / Medium (group specifics) |
| **Is finishing expected?** | **No.** Deliberately over-length/speeded; *"you are not expected to complete all the questions"* (psychometric-success); *"you may not be able to complete the test"* (JobTestPrep). **No trustworthy "strong candidates finish X of N" number exists** — any such figure traces to low-authority sites. | High (not expected) / Low (any number) |
| **Wrong-tab scoring quirk** | *"submitting your answer while the wrong tab is on display will reduce points from your score, even if your answer is correct."* Repeated across JobTestPrep, GraduatesFirst, MConsultingPrep, psychometrictests.org. Plausible but a prep-vendor claim, not Aon-confirmed. | Med-High |
| **Published reliability/validity** | Technical manuals **exist** (Aon is an EFPA/BPS-registered publisher) but are **not public**. *"Aon is known for keeping its scoring system a secret."* No Cronbach's alpha / validity coefficients found online. | High (unavailability) |

**Net scoring model the app should teach and simulate:**
`score = (#correct × +1) − (#wrong × 1) + (#blank × 0)`, then interpreted **relative to a norm group** (percentile/Stanine), on a test **you are not meant to finish**, where **accuracy dominates coverage** and **blind guessing is negative-EV**.

---

## 3. The reasoning traps (from Aon's own worked examples + vendor guidance)

**Primary source:** Aon's official practice PDF (`aon.com/.../practice-tasks-numerical-reasoning.pdf`) — 5 worked examples with Aon's *own* rationale. Quotes below are verbatim from it unless attributed otherwise.

### The decision rule (the heart of it). Confidence: **High.**
- **TRUE** = statement is *"logically and unequivocally correct, based on the precise information given"* — data confirms it.
- **FALSE** = statement *"cannot possibly be true"* — a value you *can* compute/compare **contradicts** it.
- **CANNOT SAY** = *"not enough information... to be absolutely certain"* — a required figure is **absent** from the displays.
- Operational test: *Can I prove it 100% true or 100% false from the data?* If a single required number is missing → **Cannot Say**. If all numbers are present but disagree → **False**.
- *"You are not required to have any previous knowledge of the subject matter"* — never use outside knowledge; never over-infer. **Over-inference to "True" is the single biggest score-killer.**

### The specific traps

1. **Mixed units (thousands/millions/currency).** Aon's most-demonstrated trap. Ex.1: footnote *"All data in thousand dollars,"* value 7,256 → **$7.256 M** → statement "over $7 million" is **TRUE**. Ex.4: chart *"in thousands,"* 1550 = 1,550,000 people. **Technique:** read the unit footnote/axis *first*; convert into the statement's units explicitly. (High)
2. **"Close but not exact" ⇒ FALSE.** Ex.4: 3850−2300 = 1550 (→1,550,000) vs stated 1,500,000. *"The figures are close, but the statement was not asking for an approximation."* → **FALSE**. **Technique:** unless the statement says "about/approximately," any mismatch = False. (High)
3. **Missing period/row/year ⇒ CANNOT SAY.** Ex.3: table has Years 6/5/4; statement references Year 3 → *"the table does not provide data for fiscal year 3 and therefore we cannot say."* Ex.5: chart has FY+1/2/3; statement needs FY+4 → Cannot Say. **Technique:** confirm the exact entity/period named exists in the display before computing. (High)
4. **Percentage vs percentage-points.** Share 10%→15% is **+5 percentage points** but **+50% relative** (5÷10×100). "Grew 5%" would be False; "rose 5 points" True. **Technique:** decide "of" (relative → divide by **original**) vs "points" (subtract shares); never subtract two percentages and call it a percentage change. (High principle / Medium that Aon items always exploit the wording)
5. **Data-type mismatch ⇒ CANNOT SAY.** JobTestPrep worked item: statement about **"products sold"** but display only shows **"proceeds"** (revenue share). Revenue share ≠ unit share → **Cannot Say**, even though the numbers look addable. **Technique:** verify the statement's *quantity type* matches the display's. (High)
6. **Combining two displays.** Aon Ex.2: needs pie-chart % (Footwear 38% + Accessories 7% = 45%) **and** the caption total ($86M): 45% × 86 = $38.7M ≠ $32M → **FALSE**. Aon's estimation shortcut: *"45% is almost 50%... 50% of $86M is $43M... quite different from $32M... likely false."* **Technique:** identify every figure needed and locate each; combine chart-% with caption totals. (High)
7. **Cumulative / YTD vs per-period.** A "YTD/Total" column read as a single period. E.g. months 100/120/90 + YTD 310; "March = 310" is False (March = 90). **Technique:** match the statement's time granularity to the column's; never let a bold Total row stand in for a line item. (High principle / Medium prevalence in scales specifically)
8. **Index / base-100 (rebased) figures.** Index 100→130 means +30% **only because base = 100**; index values are **never** absolute quantities. "Revenue was 130" → Cannot Say; "rose 30%" → True. **Technique:** check axis/legend for "Index / base = 100 / rebased" first. (High method / Low prevalence in scales bank specifically — Aon's PDF uses absolute figures)
9. **Total-row distractor.** Bold "Total" rows sit adjacent to line items (Aon Ex.1/Ex.3) — fast readers grab them. **Technique:** read the exact row label. (High)
10. **Compound % added linearly.** +12% then −8% is **not** +4%; chain ×1.12×0.92 = −0.96% net. **Technique:** chain multiplicatively. (High)
11. **Biggest absolute ≠ biggest %.** Largest raw move often comes off the largest base. **Technique:** divide each change by its own base before ranking. (High)
12. **Axis misreading / non-zero or rebased scales.** **Technique:** check axis scale/units before reading bar heights. (High)

---

## 4. Time-allocation strategy (strong-candidate playbook)

- **~20 s/item** is the real target (37/12 min or 18/6 min). No source supports 40 s. **Skip rule (synthesis):** abandon anything not cracked by ~30 s (1.5× budget). (High pace / Medium exact skip threshold)
- **Guess vs blank:** because wrong = −1 and blank = 0, **blind guessing is negative-EV → leave it blank.** Guess **only** when you can eliminate ≥1 of the 3 options (narrowed 50/50 turns EV non-negative). (High penalty facts / Medium the eliminate-one heuristic)
- **Skim-all-tabs vs question-first — sources genuinely conflict.** GraduatesFirst: explore all tabs before deciding. MConsultingPrep: many candidates address questions individually to avoid irrelevant data; *"respond with the minimal necessary data."* **Reconciliation:** a *brief* few-second orientation to learn which tab holds what, then **read statement → identify the one figure/tab needed → open only that tab → verify.** (Medium; flagged conflict)
- **Confirm the right tab is displayed before submitting** (wrong-tab penalty). Most-repeated warning across all sources. (Med-High)
- **Calculator:** scales numerical **provides an on-screen calculator**; **pen & paper allowed**. (scales *eql* is mental-only, no calculator.) *"Compare before you compute"* — many T/F items only need "is A > B?", not an exact quotient. (High)
- **Accuracy over coverage:** the construct is *speeded accuracy*; a strong percentile comes from a high correct-count with few penalties, not from reaching the last item. (High)
- **What employers measure:** *"analyse data out of diagrams and tables... perform arithmetic... in a very short and limited time"* — numerical reasoning + decision-making under pressure; test difficulty scales with role seniority. (High)

---

## 5. Walkthroughs / candidate accounts

- Concrete techniques (each cited in §3–4) came from JobTestPrep, MConsultingPrep, AssessmentDay, GraduatesFirst, Practice Aptitude Tests, and Aon's own PDF.
- **Gap (stated honestly):** verbatim Reddit/StudentRoom candidate posts were **not** retrievable for these queries, and a cut-e Scales YouTube walkthrough (`youtube.com/watch?v=Zrt-dN2ElWs`) was blocked by a Google CAPTCHA redirect. No candidate quotes were fabricated. Candidate-voice evidence is therefore weaker than vendor evidence; vendor pages are the primary basis.
- **Compliance:** every source offering live-test answer lookup or proctoring evasion was ignored. This app is preparation-only.

---

## 6. Open conflicts & gaps (unresolved on purpose)

1. **Your "18 in 12 min"** vs published 18/6 or 37/12 — likely memory conflation or a client-configured form. **Unresolved.**
2. **Penalty magnitude** — flat −1 (well-supported) vs fractional −⅓/−¼ (low-authority only).
3. **Adaptive?** — authoritative tier says randomized-fixed-form (not adaptive); some sites say adaptive. Weight of evidence → *not* item-adaptive for scales numerical/verbal.
4. **Back-navigation** — affirmed by AssessmentDay & GraduatesFirst; unmentioned by others. (App will support it, per weight of evidence, with a toggle.)
5. **Skim-all vs question-first** — genuine expert disagreement.
6. **scales verbal item count** (47 vs 49); **gridChallenge adaptivity**; **scales cls naming**.
7. **No public technical manual** — reliability/validity coefficients live in Aon's non-public manuals; would require a direct request to Aon.
8. **Could not reach Aon's own site** (DNS failure) beyond the practice PDF; UI-mechanics claims rest on prep vendors → capped at Med-High.

---

## Sources

**Primary (Aon):**
- https://www.aon.com/getmedia/3cc4d7fa-531f-4c0d-b4b3-e88afb130b74/practice-tasks-numerical-reasoning.pdf — official practice tasks, 5 worked examples w/ rationale

**Established vendors / publishers:**
- https://www.jobtestprep.co.uk/cut-e-numerical-practice · https://www.jobtestprep.com/aon-numerical-test · https://www.jobtestprep.co.uk/cut-e-tests · https://www.jobtestprep.co.uk/aon-assessment · https://www.jobtestprep.co.uk/true-false-cannot-say · https://www.jobtestprep.co.uk/graphs-and-tables · https://www.jobtestprep.co.uk/aon-smartpredict-challenges-practice
- https://www.assessmentday.co.uk/cut-e.htm · https://www.assessmentday.com/aon.htm · https://www.assessmentday.co.uk/resources/numerical-reasoning-tips.html
- https://www.practiceaptitudetests.com/testing-publishers/cut-e/ · https://www.practiceaptitudetests.com/testing-publishers/aon/ · https://www.practiceaptitudetests.com/resources/verbal-reasoning-test-practice-true-false-cannot-say/ · https://www.practiceaptitudetests.com/resources/numerical-reasoning-graduate-guide/
- https://www.graduatesfirst.com/aon-cut-e-practice-assessments
- https://psychometric-success.com/aptitude-tests/test-types/cut-e-test · https://psychometric-success.com/aptitude-tests/test-types/aon-assessment-test
- https://www.psychometrictests.org/publishers/cut-e/
- https://www.fintest.io/publishers/cut-e/
- https://mconsultingprep.com/aon-assessments
- https://www.123test.com/assessment-training/cut-e/
- https://www.graduatemonkey.com/courses/cut-e-numerical-reasoning-test-practice-course/
- https://www.testsolve.ai/blog/numerical-reasoning-tips/

**Low-authority (flagged, used only where noted):** testsolve.ai/tests/aon · careertestprep.com/knowledge/cut-e-tests · forgeprep.io · prepclubs.com
