# Chapter 2 — The Complete Product Catalogue, and How It Interlocks

SHL sells **a system, not tests** — and understanding the system is what lets you predict what a bank will send you and why. This chapter maps the whole catalogue, then explains the five mechanisms that bind it together.

> **A warning about prep material.** SHL renames and retires products constantly. A product described on a prep site but absent from shl.com is *probably legacy*; a name in SHL's release notes but not on its marketing pages is *probably new*. The most common candidate-facing error in circulation: prep vendors still describing the **legacy 30-question Verify G+ as if it were current**, when the live product is the **24-question adaptive Verify Interactive G+**. `[PREP-VENDOR error, identified by cross-check]`

## The catalogue

SHL's own taxonomy runs to six assessment categories plus video, platform and services. Its **"Featured Products"** — what it sells hardest — are: **OPQ · Global Skills Assessment · Job-Focused Assessments · Motivational Questionnaire · Situational Judgment Tests · SHL Verify · SHL 360.** `[VENDOR]`

### Cognitive — the Verify family
| Product | What it is | Status |
|---|---|---|
| **SHL Verify** | Umbrella cognitive brand — "potential to learn, adapt and perform" | Current `[VENDOR]` |
| **Verify Interactive** | The current gamified/drag-and-drop range: Numerical Calculation, Inductive, Deductive, Verbal | **Current** — Numerical Calculation named in SHL's Oct 2025 release notes `[VENDOR-PRIMARY]` |
| **Verify Interactive G+** | Adaptive composite of the Interactive subtests (~24 items / 36 min) | Current `[VENDOR]` |
| **Verify G+ (legacy)** | Button-click composite, ~30 items / 36 min | **Legacy** — still described as current by prep vendors `[flagged error]` |
| Standalone Verbal Reasoning | Separate verbal test | Likely legacy/standalone `[INFERRED]` |
| Checking / clerical / mechanical | Historic range | Absent from current SHL pages `[UNKNOWN — probably legacy]` |

### Personality and motivation
- **OPQ32** (current form **OPQ32r**) — 32 workplace traits; SHL calls it one of the most-used personality tests in the world. Full mechanics in Chapter 4. `[VENDOR]`
- **MQ — Motivational Questionnaire** — what energises and de-motivates someone at work; ~20 minutes. `[VENDOR name; timing PREP-VENDOR]`
- **RemoteWorkQ** — remote-work behavioural tendencies across three areas (Work Relationships, Work Habits, Self-Development & Well-Being); ~10 minutes, with its own manager report. Now derived from OPQ. `[VENDOR]`
- **ADEPT-15** — the 15-facet adaptive instrument previously recorded as SHL-licensed. **It did not appear on any current SHL page** in this research pass. `[UNKNOWN — possibly retired, renamed or region-specific; do not assume you'll meet it]`

### Behavioural and situational
- **Situational Judgment Tests (SJT)** — interactive work scenarios, customisable per employer, with competency weightings configured per client.
- **Global Skills Assessment (GSA)** — a featured behavioural product. Notably, SHL ships **both a "relative" (norm-referenced) and an "absolute" (criterion-referenced) development report from the same data** — an analytically important admission that the same performance can be presented two entirely different ways. `[VENDOR-PRIMARY — Oct 2025 release notes]`
- **Job-Focused Assessments (JFA)** — pre-packaged, role-specific batteries predicting "candidate readiness and fit."
- **Realistic Job Previews** — scenario previews that double as self-selection tools.

### The Universal Competency Framework — the keystone
The **UCF** is a three-tier model: **8 general competency factors → 20 competency dimensions → 96 component skills.** `[VENDOR]` The eight factors are SHL's "Great Eight," derived from the Bartram (2005) *Journal of Applied Psychology* paper. SHL defines competencies deliberately as "sets of behaviors that are instrumental in the delivery of desired results" — **behavioural, not technical knowledge**.

Critically, SHL doesn't just use the UCF internally: it **ships** it to clients as questionnaire items, **behavioural anchors**, **interview questions** and **assessment-centre exercises**. `[VENDOR]` That is the mechanism explored below.

SHL also markets **APTA™**, a tool claiming to measure all 96 UCF components in 15 minutes. `[VENDOR]` ⚠️ Ninety-six constructs in a quarter of an hour is an extraordinary claim; treat it as marketing pending a technical manual.

### Skills, simulations and technical
Coding simulations ("AI-powered coding challenges"), technical skills tests (~15 min), business skills (Microsoft Office/computer literacy), call-centre simulations, and AI-scored **language evaluation** — the last almost certainly powered by **SVAR**, the spoken-English engine inherited from Aspiring Minds and confirmed live in SHL's 2025 release notes. `[VENDOR + VENDOR-PRIMARY; the SVAR link is INFERRED]`

### Video and interview
- **Smart Interview On Demand (SIOD)** — asynchronous recorded video, optional AI scoring. Confirmed live. `[VENDOR-PRIMARY]`
- **Smart Interview Live** and **Smart Interview Live Coding** — real-time interviews, the latter with an in-browser compiler (50+ languages per prep sources).
- **Smart Interview Professional (SIP)** — explicitly called **"SHL's flagship interview product"** in the Oct 2025 release notes, and the focus of most 2025 development: SSO for interviewers, self-scheduling, an interviewer-analytics dashboard, a configurable skill framework (Category → Topic → Subtopic), **AI skill recommendations generated from an uploaded job description**, and O*NET job mapping. `[VENDOR-PRIMARY]`
- **AI Screener (SIA)** — a distinct asynchronously-scored product named alongside SVAR and SIOD. Details `[UNKNOWN]`; appears new.

**One finding here is genuinely important for Chapter 8:** SIP captures **candidate snapshots at 120-second intervals during interviews, displayed on the report** — and it is **configurable per company**. `[VENDOR-PRIMARY]` This is rare *first-party* confirmation of image-based monitoring inside an SHL product, and it confirms that monitoring is an employer choice rather than a universal default.

### Assessment centres, 360 and platform
**Virtual Assessment and Development Centers (VADC)** — a full product and an outsourced service. **SHL 360** — multi-rater feedback. And the platform estate, revealed by SHL's own release-note matrix: **TalentCentral · TalentCentral+ · 360/MFS · SHL Apps · Insights**. `[VENDOR-PRIMARY]`

**TalentCentral+ is where all 2025 feature work landed; classic TalentCentral received only content and localisation updates.** The strong inference is that **classic TalentCentral is being sunset in favour of TC+.** `[INFERRED — well-supported by the release-note pattern; not stated by SHL]`

## How it interlocks — five mechanisms

**1. The UCF is the connective tissue.** Because SHL ships the same competency model as questionnaire items, behavioural anchors, interview questions *and* assessment-centre exercises, an OPQ scale, an SJT scenario, an interviewer's scorecard rating and an AC observation can all be expressed **on the same competency axis**. That is what lets a bank aggregate radically different measurement methods into one profile — and it is the thing the bank is actually buying. No single test can do it.

**2. Job-Focused Assessments are the packaged composite.** JFAs are the retail form of the system: define the role's requirement in UCF terms, measure the candidate on the same terms, score the *distance*. It is competency-profile matching, not test-passing. `[VENDOR framing]`

**3. Scoring is relative by design.** SHL's platform ranks candidates not on absolute score but on performance **relative to past test-takers** — which is why the employer's choice of comparison group is load-bearing in every result (Chapters 6–7). The GSA's dual relative/absolute reports show SHL is fully aware of the distinction and sells both views. `[PREP-VENDOR + VENDOR-PRIMARY]`

**4. Compensatory within an instrument; multi-hurdle across the funnel.** Verify G+ combines sub-abilities into a composite, and the UCF rolls 96 skills into 20 dimensions into 8 factors — each level a weighted aggregation, i.e. compensatory. But **across** the funnel the products are sequenced as gates in an ATS-integrated workflow: sift assessment → verification test → SJT/JFA → Smart Interview → assessment centre. The **verification test is a pure hurdle** (Verified / Not Verified, not a score). Which model any given employer uses, and where, is **configured by the employer** — there is no universal SHL rule. `[INFERRED, consistent across sources]`

**5. Scores are becoming portable — the Smart Assessment Workflow.** This is the clearest evidence of system thinking, and it is new. From **14 August 2025**, if a candidate has completed SVAR, Smart Interview On Demand or AI Screener and is **re-invited within a defined window (e.g. 30 days)**, those assessments show as already complete and **the prior scores are copied into the new attempt** for the recruiter. Synchronously-scored assessments have prior *responses* copied and re-scored; asynchronously-scored ones have the *score* copied directly. Manually-evaluated scores are never reused, and proctoring data does not carry over. `[VENDOR-PRIMARY — Oct 2025 release notes, TalentCentral+ only]`

**What that means for you:** within a single employer, an SHL result can **follow you across applications**. SHL is building a candidate record, not a series of isolated tests. If you apply to two programmes at the same bank inside the window, assume your earlier result travels with you.

## What you'll actually meet in a banking funnel

Of that vast catalogue, a UK finance early-careers candidate realistically encounters: a **Verify Interactive cognitive assessment**, a **behavioural/personality instrument** (OPQ-derived or an SJT/strengths measure), sometimes a **video interview** (Smart Interview On Demand), and — for technology and quant streams — a **coding assessment**. Everything else in the catalogue is sold to the same client for other populations: 360 feedback for managers, VADC for experienced hires, MQ and RemoteWorkQ for development. Knowing the shape of the whole system helps you read your invitation email accurately; it does not mean you will sit all of it.
