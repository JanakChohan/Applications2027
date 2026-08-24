# Chapter 6 — How SHL Scoring Actually Works

Almost everything candidates believe about SHL scoring is wrong in the same direction: they imagine a mark out of 100 and a pass line. Neither exists. This chapter sets out the real pipeline, using SHL's own sample reports — which are publicly downloadable from SHL's support domain and were text-extracted for this report.

## The pipeline

```
item responses → IRT ability estimate (theta, weighted by item difficulty)
              → norm lookup against an employer-chosen Comparison Group
              → Percentile + T-score + Sten (+ A–E band on candidate reports)
```

Each step discards a different intuition. Let's take them in turn.

## Fact 1: your raw number correct is *not* your score

SHL states this outright in its own employer-facing report `[VENDOR — Verify Ability Test Report v2.0, verbatim]`:

> "…because each candidate receives a different set of items, there is not a direct correlation between Hit rate/Accuracy and the Percentile, T or Sten score achieved; **an individual with a lower hit rate may achieve a higher percentile score and vice-versa.**"

This is the single most important scoring fact in the report. Because items are drawn from a randomised bank with IRT-calibrated difficulty parameters, **getting fewer, harder items right can outrank getting more, easier items right.** Candidates who leave a test thinking "I got about 22 out of 30, so that's 73%" are reasoning about a quantity that does not determine their result.

## Fact 2: the employer sees your speed and your accuracy separately

The same report defines three distinct reported quantities `[VENDOR, verbatim]`:

- **Number Attempted** — "the number of questions the candidate has seen during the test. The total may include questions that the candidate has not provided a response to."
- **Work rate** — "a measure of how far the candidate has got through the test… the number attempted divided by the total number of questions."
- **Hit rate** — "a measure of accuracy… the number of questions the candidate has answered correctly divided by the total number of questions attempted."

So the recruiter sees a **speed dimension and an accuracy dimension alongside the normed score.** A candidate who answered few but got them right shows high hit rate, low work rate; the reverse pattern is equally visible. This is why the pacing advice in Chapter 3 matters beyond the score itself: your *profile of behaviour* is on the page, not just your outcome.

## Fact 3: the comparison group decides what your percentile means

Your score is normed against a **comparison group the employer selects**. SHL maintains roughly **70** of them across the Verify range (test type × job level × industry). `[VENDOR-manual]` The sample report carries an explicit "Assessment Methodology" table pairing each subtest with its group — and the real examples are revealing:

| Test | Comparison Group |
|---|---|
| Graduate/University Numerical Reasoning UKE | **General Population 2006** |
| Graduate/University Inductive Reasoning UKE | **General Population 2007** |
| Verify – Operational Checking UKE | **General Population 2009** |

`[VENDOR — verbatim from the sample report]`

Three things follow, and each is genuinely useful:

1. **Norm groups are frozen, year-stamped standardisation samples** — not rolling averages of current applicants. A report issued years later was still norming against a 2006 sample.
2. **Test difficulty level and comparison group are independent axes.** A *Graduate-level* test can be normed against a *General Population* group — which flatters graduate candidates relative to being normed against other graduates.
3. **Language/locale is a third axis** (the "UKE" suffix = UK English).

**Why this matters more than your performance.** The same answers can produce a materially different percentile depending on the group chosen. Against a General Population norm, a strong graduate looks exceptional; against a Finance Graduates norm, the same performance is unremarkable, because everyone in that reference pool is already numerically strong. **You are almost never told which group was used.** When a prep site tells you "banks want the 80th percentile," it is quoting a number whose meaning is undefined without naming the group.

## Fact 4: the SHL report contains no pass mark, and no recommendation

This was verified directly against SHL's sample reports: the employer-facing Verify Ability Test Report shows percentile, T-score, sten, level, comparison group, a narrative interpretation sentence, work rate and hit rate — **and no cut-score, no pass/fail line, and no hire/no-hire verdict.** `[VENDOR — absence observed across the full report]`

SHL's own framing is that the score "should be used as part of a broader evaluation," and it gates interpretation behind trained users: "The use of these tests is limited to those people who have received the necessary training in their use and interpretation." `[VENDOR, verbatim]`

**The threshold is 100% the employer's decision.** SHL supplies a measurement; the bank decides what to do with it. Chapter 7 takes this apart properly.

One further disclosure from the report deserves flagging, because it affects how you should read any feedback you're given `[VENDOR, verbatim]`:

> "This report has been generated electronically - **the user of the software can make amendments and additions to the text of the report.** SHL Global Management Limited and its associated companies cannot guarantee that the contents of this report are the unchanged output of the computer system."

In other words, anything an employer shows you may not be SHL's unaltered output.

## Fact 5: what *you* see is deliberately coarser

SHL ships a **separate candidate-facing report**, and it shows less. In the sample: a **grade letter on an A–E five-band scale** rendered as a segmented bar, a narrative sentence ("your verbal reasoning ability is well below average when compared to the comparison group"), and developmental tips — but **no numeric percentile, no T-score and no sten.** `[VENDOR — Verify Candidate Report sample]`

Two corrections follow. First, the widely-repeated prep-vendor claim that SHL uses an **A–D** band scale is **wrong** for this report: SHL's own candidate report uses **A–E, five bands.** `[VENDOR overrides PREP-VENDOR]` Second, the percentile boundaries for those bands are **not printed anywhere in the report** — the commonly-cited 10/20/40/20/10 split is a plausible convention but **is not confirmed by any SHL source.** `[UNKNOWN — do not rely on it]`

The candidate report also states something practically useful: **"test results remain valid for about 12 to 18 months."** `[VENDOR, verbatim]` That is the nearest thing to an SHL-sanctioned score shelf-life, and it bears directly on retake questions (below).

Finally, the candidate report's own construct definitions are worth internalising because they tell you what is *not* being tested:

- **Verbal reasoning** — "emphasises understanding, using and evaluating verbal information **rather than language usage, spelling or grammar**."
- **Numerical reasoning** — "the emphasis is on **understanding and evaluating data rather than on computation**."
- **Inductive reasoning** — "work with incomplete information and create solutions to novel problems from first principles."

## Retakes and score reuse

**Retake policy is set by the employer, not SHL** — there is no retake rule anywhere in SHL's reports. `[PREP-VENDOR consistent; corroborated by absence]` Most graduate schemes allow no retake within a cycle, with cooling-off periods of six to twelve months commonly reported. `[PREP-VENDOR]`

Two SHL-sourced facts refine this. The **12–18 month validity window** is SHL's own statement on how long a result stands. And the **Smart Assessment Workflow** (Chapter 2) means that, for certain products within a single client, **prior scores are copied into a new attempt** if you re-apply within a defined window — so a result can follow you across applications at the same employer. `[VENDOR-PRIMARY]`

One structural point worth knowing: because item banks are randomised and scoring is IRT-based, **an immediate retake would not present the same test anyway.** Retake restrictions exist for practice-effect fairness and applicant-pool policy, not to protect item exposure from you individually. `[INFERRED]`
