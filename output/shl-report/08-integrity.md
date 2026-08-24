# Chapter 8 — The Integrity Architecture: What SHL Detects

SHL's anti-cheating stack has changed substantially since 2023, and most published candidate guidance describes the old version. This chapter is built from **SHL's own release notes** — public, unauthenticated PDFs on its support domain — which document the current architecture by name and function.

The headline: SHL has moved from a purely **psychometric** integrity model (catch inflated scores statistically) to a layered model that adds **behavioural surveillance** (image, audio, browser telemetry) rolled up into a single flag called the **Proctoring Index**. Both layers matter, and the honest news for an anxious candidate is at the end.

## Layer 1 — Design security: randomised item banks

Every candidate receives a **different set of items** drawn from an IRT-calibrated bank, with difficulty parameters placing different item sets on a common scale. SHL states this explicitly as the reason hit rate ≠ percentile (Chapter 6). `[VENDOR-manual + VENDOR sample report]`

Consequence: **leaked question banks and shared answers are worthless.** There is no fixed form to leak, and your friend's "question 7" is not your question 7. Item-exposure caps, bank sizes and rotation schedules are not published. `[UNKNOWN]`

## Layer 2 — The verification test (the classic model — and a significant finding)

The long-standing SHL model was: sit the test **unsupervised**, then optionally sit a shorter **supervised verification test** with different items but matched difficulty. A **Confidence Indicator** compares the two scores; a statistically improbable gap returns **"Not Verified"** rather than a number. It was validated by Monte Carlo simulation — 10,000 simulated candidates, cheating modelled as a **+2 standard-deviation** score inflation. `[VENDOR-manual — quantified, primary]`

Crucially, **SHL's own manual frames "Not Verified" as requiring investigation, not conviction**, listing innocent causes: distractions, not attempting all items, physical or psychological state on the day, and whether the candidate had used the free practice materials. `[VENDOR-manual]` It also notes that telling candidates up front that verification will be used **reduces cheating** — deterrence by disclosure is part of the design.

Every employer-facing Verify Ability Test Report still carries the printed recommendation `[VENDOR, verbatim]`:

> "If these tests were unsupervised, there is a small possibility that these scores do not represent their actual level of ability. **A Verification Test is recommended to verify these scores.**"

**The significant finding:** the verification test appears to be **absent from the current Verify Interactive report's "How to verify a result" table.** `[VENDOR — comparison of the two report generations]` The inference is that SHL has **dropped the verification-test backstop for its current Interactive range**, replacing it with the proctoring stack below. `[INFERRED — not stated by SHL; flagged as an open question in Chapter 12]` If correct, it is a meaningful shift: from catching inflated scores *statistically after the fact* to watching candidates *during the test*.

## Layer 3 — The proctoring stack (current, and documented by name)

SHL's release notes document a **proctoring feature menu**, enabled at company level. Confirmed features:

| Signal | Status |
|---|---|
| **Periodic image capture** (candidate snapshots at intervals) | ✅ `[VENDOR]` |
| **Browser off-focus** — captured as **% of assessment time** spent toggling away, not merely a switch count | ✅ `[VENDOR]` |
| **Multi-face detection** — snapshot if more than one person is in frame | ✅ `[VENDOR]` |
| **Copy-paste attempt count** | ✅ `[VENDOR]` |
| **Print-screen count** | ✅ `[VENDOR]` |
| **Periodic audio snippets + Multiple Voice Detection (AI)** — detects "whether someone is **prompting/helping the candidate through verbal cues**" | ✅ `[VENDOR — July 2023 release]` |
| **Face Match (AI biometric)** — matches an **ID-card image capture** against in-test snapshots | ✅ `[VENDOR]` |
| **Advanced plagiarism detection** — "automatic pattern matching across candidate responses and internet content" | ✅ `[VENDOR]` — applies to constructed-response/text items |
| **Snapshot capture at 120-second intervals during interviews** (Smart Interview Professional) | ✅ `[VENDOR-PRIMARY — Oct 2025 release notes]` |

Two critical qualifications, both from SHL's own documentation:

**It is OFF by default.** "These features are switched **OFF by default** until the client requests to enable them," and the Proctoring Index specifically "will have to be requested to be switched on by a company… actioned by their SHL account manager." `[VENDOR, verbatim]` **Most high-volume graduate sifts run unproctored.** The prep-industry habit of describing full webcam surveillance as standard SHL practice is wrong.

**It runs invisibly.** "On candidate experience there are **no visible changes** while Audio and Video proctoring are background functions." `[VENDOR, verbatim]` SHL surfaces no in-test indicator, which means **whether you are told depends entirely on the employer's invitation email and consent notice** — not on SHL. Given that the stack includes **biometric face matching and audio capture**, that is a live UK GDPR question, and SHL's consent-capture mechanics are undocumented. `[UNKNOWN]`

## Layer 4 — The Proctoring Index: the flag employers actually see

Introduced July 2025, this is the aggregation layer, and SHL's own description is the most important sentence in this chapter `[VENDOR, verbatim]`:

> "Proctoring index is the flag that conveys the **likelihood of a candidate exhibiting suspicious behavior or using unfair means**. **The recruiter is expected to use this information and manually review further to take a final decision.**"

Mechanics:
- Threshold breaches across the enabled features roll up into an index, originally **High/Medium/Low**, moving to **High/Low** in the July 2025 release.
- Clients may choose *which subset* of features feeds the index — but, verbatim: "**While the features can be selected, the individual feature thresholds cannot be altered/customised.** These are set & maintained based on studies that ensure consistency, accuracy, and correctness."
- The index is distributed into **candidate reports (a dedicated proctoring section), project listings, Excel exports, and pushed back to the ATS**. Recruiters can manually review captured audio/video snippets with timestamps.

**The thresholds themselves are not published.** `[UNKNOWN — SHL says they exist and are study-derived; no numbers, no study]` Nor is any false-positive rate.

## What this means for an honest candidate

Read the architecture carefully and it is **less hostile than it looks**:

- **Most graduate sifts are unproctored.** Proctoring is opt-in, per company, off by default.
- **The index is explicitly triage, not verdict.** SHL states the recruiter "is expected to… manually review further to take a final decision." A flag routes you to a human, it does not auto-reject you.
- **The historic backstop was designed with innocence in mind** — SHL's manual lists mundane explanations for a failed verification and instructs investigation rather than conviction.

The genuine risks are therefore mundane and avoidable rather than sinister — and, notably, the two most common honest-candidate flags map to things you can simply not do: **browser off-focus** (measured as a percentage of test time, so notifications and tab-checking accumulate) and **copy-paste attempts** (counted, even innocent ones).

**The clean-sitting checklist:**
- Close every other application and tab **before** launching; disable notifications; disconnect a second monitor.
- Don't copy or paste anything, including your own working.
- Sit alone, front-lit, face in frame, in one uninterrupted window on a stable connection.
- If proctoring is on you may not be told in-test — so **ask the recruiter in writing beforehand** whether the assessment is proctored, and whether ID capture is required. That answer also tells you what consent you're giving.
- Request adjustments in writing, in advance, through the employer.

## AI-era cheating: SHL's stated position

SHL published its own study of ChatGPT against its portfolio in 2023. Its stated findings `[VENDOR]`: **personality and competency-based assessments were "not susceptible to inflated scores"**, as were simulations and assessment-centre exercises; **constructed-response and text-based ability tests were measurably impacted**. SHL also markets an AI-text classifier claiming to detect "at least **7x more** candidates using ChatGPT."

Two honest caveats. First, **the 7x figure is scoped narrowly**: it is versus SHL's *own prior* textual pattern-matching baseline — **not versus competitors, and not an absolute detection rate.** `[VENDOR, precisely scoped]` Do not restate it as "SHL catches 7x more cheats." Second, the study is **from 2023, tested ChatGPT as it then was, and is SHL's own research on its own products.** Multimodal frontier models handle image-based items far better than the 2023 baseline, so the "interactive formats are safe" conclusion is **dated and vendor-interested.** No updated SHL study was located. `[UNKNOWN]`

A structural observation worth more than either claim: the **verification-test design never needed to detect AI at all.** It detects *any* unexplained score inflation — proxy, collusion, leaked items, or LLM — because it compares your unsupervised score to a supervised one. That is why score-comparison designs are more robust than content forensics, and why its apparent removal from the Interactive range (Layer 2) is a genuinely consequential change.
