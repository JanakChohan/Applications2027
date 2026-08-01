# Chapter 6.3 — The Psychometrics You Need to Understand as a Candidate

You do not need a psychology degree to sit these assessments well, but you do need a working grasp of about ten concepts, because they determine what your score actually means, why two identical performances can produce different outcomes, and why some of the things you fear (a single unlucky question) matter less than you think while others (which norm group you're measured against) matter enormously. This chapter is the plain-English version. Every per-provider chapter refers back to it.

## Reliability: why your score is a range, not a point

**Reliability** is the consistency of a measurement — how much of your score reflects your true ability versus random noise (a lucky guess, a misread question, a lapse of attention). It is expressed as a coefficient between 0 and 1. A reliability of **0.80** means roughly 80% of the variation in scores across candidates reflects real differences in ability and about 20% is noise. `[INDEPENDENT — classical test theory]` For context, SHL's own technical manual reports internal-consistency reliability of **0.77–0.84** for its Verify ability tests — typical of good commercial cognitive tests. `[VENDOR-manual]`

The practical consequence is the single most under-appreciated fact in this whole field: **your score is not a precise point; it is the centre of a range.** That range is quantified by the **standard error of measurement (SEM)**, calculated as SEM = √(1 − reliability) × standard deviation. `[INDEPENDENT/VENDOR-manual]` If you sat the same test again tomorrow (with different items, no learning effect), your score would wobble within roughly one SEM most of the time. So the difference between the 68th and the 74th percentile is very possibly noise, not ability. This is why obsessing over a couple of percentile points is misguided, and why firms that set a hard cut-score at, say, exactly the 80th percentile are — whether they admit it or not — rejecting some candidates whose *true* ability is above the line. You cannot control the noise; you can only push your true score high enough that the range sits comfortably above the likely cut.

## Validity: does the test predict anything?

Reliability is necessary but not sufficient — a bathroom scale that consistently reads 5kg heavy is reliable but not valid. **Validity** asks whether the test measures what it claims and predicts what matters.

- **Construct validity**: does a "numerical reasoning" test actually measure numerical reasoning (and not, say, reading speed or test anxiety)?
- **Criterion validity / predictive validity**: does the score predict later job performance? This is the number that justifies the whole enterprise, and it is expressed as a correlation coefficient, **r**.

You will see confident claims that general mental ability predicts job performance at **r ≈ 0.5**. That figure comes from Schmidt and Hunter's influential 1998 meta-analysis. `[INDEPENDENT]` But you should know it has been **revised sharply downward.** A 2022 re-analysis by Sackett, Zhang, Berry and Lievens showed the older meta-analyses had over-corrected for "range restriction," and put the operational validity of cognitive-ability tests closer to **r ≈ 0.31.** `[INDEPENDENT — Sackett et al., 2022, Journal of Applied Psychology]`

## What an r of 0.3 actually means for you

This is worth internalising because it reframes how much any single test decides your fate. A correlation of 0.3 means the predictor explains about **9% of the variation** in job performance (you square the correlation to get the proportion of variance explained: 0.3² = 0.09). Even the old, optimistic 0.5 explained only 25%. `[INDEPENDENT]`

In human terms: a high score genuinely shifts the odds you'll perform well — but it is very far from destiny, and a large majority of what makes someone a good analyst is *not* captured by the test. Two implications follow. First, for the **employer**, even a modest correlation is worth having when you're sifting thousands of people, because small edges aggregate across a huge pool — which is why they use these tests despite the modest r. Second, for **you**, a rejection at this stage is not a verdict on your worth or even your ability; it is a probabilistic filter with a lot of noise in it. Clear the bar and move on; don't over-read it.

## Norm groups and percentiles: the thing that matters most

Almost every cognitive and many behavioural assessments are **norm-referenced**: your raw performance is converted into a **percentile** by comparing you to a **norm group** (also called a comparison or standardisation group). A percentile is a *rank*: the 70th percentile means you scored higher than 70% of that norm group. It says nothing directly about how many questions you got right. `[VENDOR-manual + INDEPENDENT]`

The norm group is the hidden variable that decides everything, and you rarely get told which one is used. The same raw performance can be:

- the **80th percentile** against a *general population* norm, but
- only the **55th percentile** against a *finance graduates* norm,

because the finance-graduate pool is already selected for numerical strength. `[INFERRED — direct consequence of norm-referencing]` When a guide tells you "investment banks want the 80th percentile," what that really encodes is *a demanding norm group plus a high threshold on top of it.* SHL alone offers around 70 comparison groups. `[VENDOR-manual]` You cannot usually discover which one a firm applied — so for a competitive finance role, assume the tough one and aim to be unambiguously above it.

A note on percentiles as a scale: they are **ordinal** (ranks), not equal-interval, so the gap between the 50th and 55th percentile is a different amount of "ability" than the gap between the 90th and 95th. This is why psychometricians convert to equal-interval **standard scores** for any maths: **T-scores** (mean 50, standard deviation 10) and **stens** (standard-ten: mean 5.5, SD 2, rounded to 1–10) are the two you'll meet. A sten of 8, for instance, sits around the 89th percentile. `[VENDOR-manual]`

## IRT and adaptivity: why the questions get harder

Older tests used **classical test theory (CTT)**, where every item counts the same and your score is essentially the number correct. Most modern tests — SHL Verify Interactive, Aon's adaptive modules — use **item response theory (IRT)**, which models each item's difficulty and discrimination and estimates your underlying ability (called **theta, θ**) from *both* how many items you got right and how hard they were. `[VENDOR-manual/INDEPENDENT]`

**Adaptive** delivery uses IRT live: answer correctly and the next item is harder (and more informative about your true level); answer wrong and it eases. Three things follow for you. (1) **Harder questions are a good sign** — the test is climbing because you're doing well; don't panic. (2) **Raw "number correct" isn't comparable between candidates**, because two people can answer the same count correct off very different difficulty ladders. (3) **You usually can't go back** — the algorithm has already used your answer to choose the next item. Under IRT, an early careless slip is more costly than a late one, so start carefully.

Because IRT tests draw from a large **item bank** and randomise, no two candidates get an identical test — which is simultaneously an anti-cheating feature (sharing answers is useless) and the reason practising specific "leaked" questions is pointless.

## Ipsative vs normative scoring: the personality-test trap

Personality and strengths questionnaires come in two flavours, and the difference dictates how to answer them.

- **Normative** ("Likert") items ask you to rate each statement independently ("I enjoy leading others: strongly agree → strongly disagree"). Your trait scores are compared to a norm group. These are, in principle, fakeable — you can agree with everything flattering.
- **Ipsative** (forced-choice) items make you *choose between* statements ("Which is MOST like you / LEAST like you?"), usually from blocks where all options are roughly equally desirable. This forces trade-offs, so you **cannot inflate every trait at once** — boosting one necessarily suppresses another. `[INDEPENDENT]` SHL's OPQ32i and Aon's ADEPT-15 use forced-choice designs precisely to blunt faking.

The practical upshot, developed in every behavioural section of this guide: on forced-choice instruments, trying to "game" the ideal profile tends to produce an **internally inconsistent** result that consistency and social-desirability checks flag, and that mismatches the (invisible) success model you were aiming at. Authentic, decisive, consistent answering beats strategic answering.

## Faking, social desirability and consistency scales

Vendors know candidates try to present their best self, so many questionnaires embed **social-desirability scales** (items that catch implausibly saintly response patterns) and **consistency checks** (near-duplicate items answered differently reveal random or strategic responding). `[VENDOR/INDEPENDENT]` SHL's OPQ32n, for example, includes a social-desirability indicator. A profile that trips these doesn't just look dishonest — it can be discounted entirely. The research consensus is that blatant faking is detectable and often counter-productive; subtle self-presentation (putting your best genuine foot forward) is normal and fine.

## Adverse impact and the four-fifths rule

**Adverse impact** occurs when a selection method passes one demographic group at a substantially lower rate than another, even without intent to discriminate. The US rule of thumb — the **four-fifths (80%) rule** — flags a problem if a protected group's selection rate falls below 80% of the highest group's rate. `[REGULATORY — US EEOC/UGESP]` UK law frames the same concern as **indirect discrimination** under the Equality Act 2010. This is why vendors invest heavily in bias audits and why some employers have moved from classic aptitude tests (which show well-documented group differences) toward game-based and strengths assessments marketed as lower-adverse-impact. Whether those alternatives actually reduce impact is contested — see the provider chapters and §6.6–6.7.

## Standard error, banding and the honest takeaway

Put reliability, SEM and adverse-impact awareness together and you arrive at **score banding**: the practice of treating scores within one SEM of each other as effectively equivalent rather than rank-ordering to false precision. Not all employers band — many apply a hard percentile cut — but understanding banding tells you the truth the cut-score hides: **near the threshold, the test cannot really tell you apart from the person just above or below you.** Your job as a candidate is therefore not to chase a perfect score but to lift your true ability far enough that measurement noise can't drop you below a plausible cut — and then to spend the rest of your energy on the stages where the real differentiation happens (Chapter 6.8 shows those are often *not* the online test).

---

*Sources for this chapter: SHL Verify Range Technical Manual (VENDOR-manual, definitions of reliability, SEM, percentiles, T/sten, theta, verification); Schmidt & Hunter (1998) and Sackett, Zhang, Berry & Lievens (2022) on GMA validity (INDEPENDENT); standard classical-test-theory and IRT references (INDEPENDENT); US EEOC Uniform Guidelines / four-fifths rule (REGULATORY). Full citations in the bibliography.*
