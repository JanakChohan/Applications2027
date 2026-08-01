# Chapter 4 — Pymetrics

> *Confidence tags (full explanation in Chapter 1): `[VENDOR]` / `[INDEPENDENT]` / `[CANDIDATE, n=X]` / `[INFERRED]` / `[UNKNOWN]` / `[PREP-VENDOR]`.*

> ### ⚡ At a glance — Pymetrics
> | | |
> |---|---|
> | **What it is** | A **game-based ("gamified") behavioural assessment** — you play a suite of **12 short neuroscience games** and the platform infers behavioural *traits* from how you play, then matches your profile to a role model. Now a **product line inside Harver** (which completed its acquisition of pymetrics on **11 August 2022**); the "pymetrics" brand persists candidate-facing. Founded **2013** by neuroscientist Frida Polli (with Julie Yoo). |
> | **Where in the funnel** | **Very early screen** — typically after the online application, at or before the HireVue video and numerical tests, well before the assessment centre. In UK finance, **J.P. Morgan** is the anchor user. |
> | **Format & timing** | **12 games**, ~**25–30 min**, **unproctored**, on web/iOS/Android. Pause allowed *between* games; you cannot restart a game mid-play. |
> | **Scoring model** | **No pass/fail score.** Gameplay → ~90 behavioural traits (a subset modelled) → an **SVM** predictive model → a **fit percentile** against a *role model* → a **recommendation tier**. It is **match-to-a-role**, not "how well did you do." |
> | **Typical finance cut-off** | `[UNKNOWN]` as a public number — internally, tiers are set at the **50th and 70th fit percentiles** (Do Not Recommend / Recommend / Highly Recommend), client-customisable. Not a population percentile — a *fit* percentile. |
> | **Integrity posture** | **Unproctored and hard-to-fake by design** — no "correct" answers to look up; behavioural traces (reaction time, risk consistency, altruism) can't be Googled. No webcam/lockdown option surfaced. `[UNKNOWN]` on anomaly flags. |
> | **Retake** | Generally **once every ~330 days**. Crucially, your results **carry across all pymetrics employers** in that window — you play the 12 games **once** and each firm re-scores your *same* traits against its *own* model. |
> | **Top 5 tips** | 1) Understand it's **fit, not performance** — there is no target to hit. 2) Read each game's instructions and don't waste early trials learning mechanics. 3) Be **consistent, not erratic**, especially on the risk games. 4) Don't try to fake a "trader" persona — you don't know the target and inconsistency hurts. 5) If you have a motor, visual, attention or colour-vision condition, **request the accommodation before you play** — the mis-match propagates for ~11 months. |
>
> *(Every figure above is unpacked, sourced and confidence-tagged below. This is one of the earliest gates in the J.P. Morgan pipeline, and — because results follow you — one of the highest-leverage single sittings in UK finance recruiting.)*

---

## 4.1 Snapshot

Pymetrics is the assessment most UK finance applicants mean when they say "I had to play those weird games." It is a **game-based (gamified) behavioural pre-employment assessment**: you play a suite of short, neuroscience-derived games, the platform captures **over a thousand behavioural data points** from how you play, and reduces them to a set of *traits* that a model then matches against a target profile for the role. `[VENDOR]` / `[PREP-VENDOR]` It was founded in **2013** by **Frida Polli**, a neuroscientist and former Harvard/MIT postdoc, with co-founder **Julie Yoo**. `[INDEPENDENT — Northeastern audit whitepaper]`

**The single most important corporate fact is that "pymetrics" is no longer an independent company — it is now a product line inside Harver.** Outmatch acquired Harver in May 2021, the combined company rebranded to **Harver** in late 2021, and **Harver then acquired pymetrics, with completion announced on 11 August 2022.** `[INDEPENDENT — PRNewswire/RecruitingDaily/HCM Technology Report, Aug 2022]` The deal price was **not disclosed** `[UNKNOWN]` (pre-acquisition pymetrics had raised over $56.6M `[INDEPENDENT]`). Inside Harver the tool is sold as **"pymetrics for Game-Based Assessments"** or the **"pymetrics Soft Skills Platform"**, and the most recent independent audit still names it internally as **"Harver's Soft Skills Platform"** — the same pymetrics engine. `[INDEPENDENT — BABL AI 2025 audit]` The practical point: the **"pymetrics" name is still used candidate-facing and in Harver marketing as of 2025**, so you meet it under its old name even though the company behind it changed. `[INFERRED from vendor pages carrying both names]`

For a finance candidate, pymetrics sits **very early in the funnel** — after your online application and at or before the HireVue video interview and numerical tests, well ahead of the assessment centre. `[PREP-VENDOR]` It is short (~25–30 minutes) but disproportionately consequential for a reason unique to this vendor: **your results follow you across every pymetrics-using employer for about 330 days** (§4.6). You are not sitting one firm's test; you are generating a behavioural profile that every pymetrics client re-scores for the next eleven months.

**The single most important conceptual thing to understand about pymetrics is that there is no score to beat.** The games are, in the vendor's own framing, "not meant to be won or lost." `[INDEPENDENT — audit §3.1]` There is no pass mark, no right answer, and no universally "good" profile. This chapter keeps that idea central, because almost every candidate mistake — and most of the prep industry's advice — comes from failing to internalise it.

## 4.2 Why this test exists

The problem pymetrics is sold to solve is **biased, low-signal early screening**. A bank running a graduate campaign receives far more applications than it can interview, and the traditional first filters — CV screens, "culture fit" chats — are slow and demonstrably prone to bias against non-traditional backgrounds. Pymetrics' pitch is that a **nonverbal, behaviour-based** assessment can screen at scale while *proactively removing* the adverse impact CV screens carry. `[VENDOR]`

The construct underneath is that the games are "derived from peer-reviewed psychological studies" and "purported to assess **intrinsic mental qualities** … not meant to be won or lost, but rather to surface information about players based on how they play." `[INDEPENDENT — audit whitepaper §3.1]` They measure a mix of **cognitive** traits (memory, attention, learning rate, processing speed, planning) and **emotional/social** traits (risk-taking under uncertainty, altruism, trust, fairness, emotion recognition, effort allocation). `[VENDOR]` / `[INDEPENDENT]` The vendor markets these as "soft skills." `[VENDOR — harver.com/gamified-assessments]`

**Here the honesty has to be blunt.** The public evidence that these games actually *predict job performance* is thin. Pymetrics claims ">90% accuracy in trait identification" and a "98% completion rate" `[VENDOR]` — but those are **engagement and measurement claims, not criterion validity against job performance**. The one serious validation study, Baker (2019), *Games, Measures and Factors: Measurement Validity*, is **confidential**; the Northeastern auditors were shown it privately and explicitly "encourage pymetrics to make these results public." `[INDEPENDENT — audit §6.3]` The auditors were equally clear they themselves **did not** validate the games: "We did not investigate the ability of pymetrics' games to measure human capabilities, whether those capabilities map to job performance, or whether other assessment methods would be superior." `[INDEPENDENT — audit §4.2]` And model performance from the audited engagement was **modest** — AUC ~**0.70–0.72**, accuracy ~**0.69–0.72**. `[INDEPENDENT — audit Table 3]` So the famous "audit" (§4.10) validated the *fairness plumbing*, not the proposition that the games predict a good analyst. **Independent, peer-reviewed criterion validity for pymetrics is a genuine `[UNKNOWN]`** — carry that scepticism, but also the reassurance that no one, including the firm, can tell you a "right" way to play. (See Chapter 6.3 on validity generally.)

## 4.3 Why a firm chooses Pymetrics specifically

Two things sell pymetrics to a bank, and they are inseparable: **proactive de-biasing** and a **bespoke model built from the client's own top performers.**

The core pitch is compliance-led. "One of the core assertions pymetrics makes … is that they pro-actively de-bias ML models before deployment to comply with the U.S. Uniform Guidelines on Employee Selection Procedures (UGESP)." `[INDEPENDENT — audit Exec Summary]` The marketing wraps this in language a bank's DEI and legal functions want: "validated for fairness across gender, ethnicity, and socioeconomic status"; "nonverbal and intuitive, minimizing cultural and language bias"; "fit, not background." `[VENDOR]` For a firm that must defend every selection tool, a vendor that **commissions and publishes external bias audits** offers exactly that audit-defensible story (§4.10).

**The bias-audit angle is simultaneously the selling point and the material that feeds the legal chapter — and the picture is genuinely mixed.** Three data points, without smoothing:

- **The 2020 Northeastern cooperative audit (PASS).** A Northeastern team given pymetrics' actual source code found the **baseline** pipeline correctly implements the four-fifths rule, passing four of five findings cleanly with one caveat (§4.10). `[INDEPENDENT]`
- **The 2025 BABL AI LL144 audit (PASS).** An independent audit on 2024 data found **all impact ratios ≥ 0.80** across race/ethnicity and gender — a pass under NYC's bias-audit law. `[INDEPENDENT]`
- **The 2024 FAccT "Algorithmic Monocultures in Hiring" study (the honest counter).** Re-analysing >4 million applications *position-by-position* rather than aggregated, researchers found **10.62% of individual positions still adversely impacted Black applicants** per federal guidelines. `[INDEPENDENT — via Fortune, 2026-05-26]`

All three can be true at once (§4.10): **fairness-at-build (aggregate) is not the same as fairness-in-deployment-per-role.** Neither swallow the marketing nor dismiss the audits as theatre. And note the ceiling: **audited AUC is only ~0.70–0.72, and independent games-to-job-performance criterion validity is not public** `[UNKNOWN]` — the fairness is better documented than the predictiveness.

**Finance usage.** The anchor UK-finance user is **J.P. Morgan**, described across prep sources as "unique among big banks in mandating Pymetrics games for almost all junior roles." `[PREP-VENDOR — Lumovest, CareerTestPrep, HackingTheCaseInterview]` **BNP Paribas** is confirmed by a **2023 LL144 bias-audit posting** naming them on the pymetrics/Harver platform — a *dated primary* source, the strongest kind. `[INDEPENDENT]` Beyond those two, treat every "X uses pymetrics" claim with caution: prep-vendor rosters (which list HSBC, RBS/NatWest and others) are **marketing aggregations, often stale** — a firm listed as a user may have used it in 2019–2021 and quietly moved to a competitor (Arctic Shores, HireVue's games, SHL) after the 2022 Harver acquisition. `[PREP-VENDOR]` / `[INFERRED]` **Do not assume a firm currently uses pymetrics without a dated primary source.** (By contrast, **Goldman Sachs** historically used its *own* bespoke assessment plus HireVue, *not* pymetrics — not every bulge-bracket bank picks this tool. `[PREP-VENDOR]`)

## 4.4 What the assessment actually is — full mechanics

You play a **core set of twelve games** — the "pymetrics suite." `[INDEPENDENT — audit §3.1]` (Some clients bolt on an optional add-on suite of four numerical/logical-reasoning games introduced around 2020 `[INDEPENDENT — audit §3.1 footnote]`, and Harver separately cross-sells five *cognitive-ability* tests — Perceptual Speed, Verbal, Spatial, Logical, Mathematical Reasoning — but **those are Harver products, not the pymetrics neuroscience twelve** `[PREP-VENDOR]`; keep them distinct.) The whole thing runs **~25–30 minutes** (sources give a 20–35 min range; ~1–3 min per game), **unproctored**, on web, iOS or Android. `[VENDOR]` / `[INDEPENDENT]`

**Burn this into memory before reading the game list: there is no pass/fail score.** The games are "not meant to be won or lost"; the output is a **match/fit to a role model, not a raw score.** `[INDEPENDENT — audit §3.1]` Roughly **1,000+ behavioural data points** are collected — not self-report, but behavioural traces (how fast, how consistently, how much you risk, whether you adapt). `[VENDOR]` / `[PREP-VENDOR]` What follows is each game's mechanic, the trait it is used to infer, and the telemetry it captures.

| # | Game | Mechanic | Trait(s) inferred | Telemetry captured |
|---|---|---|---|---|
| 1 | **Balloons (BART — Balloon Analogue Risk Task)** | Pump a balloon; each pump adds money to a temporary bank; bank it before it pops or lose that round. Pop thresholds vary. | **Risk tolerance, decision-making under uncertainty, learning** | Pumps per balloon, money banked vs lost, adaptation across trials, consistency/erraticness `[PREP-VENDOR]` |
| 2 | **Keypress** | Press a specified key (often spacebar) **as fast as possible** for a set duration. | Processing speed, **attention/focus, motor tempo** (some sources: drive) | Keypress rate, rhythm/consistency `[PREP-VENDOR]` |
| 3 | **Digits (digit-span memory)** | A number sequence flashes; recall and type it back in order; sequences lengthen. | **Working memory**, attention span, learning | Max span reached, error rate by length `[PREP-VENDOR]` |
| 4 | **Arrows (Flanker / task-switching)** | Coloured arrows appear; the rule depends on colour (e.g. blue/black → respond to the *centre* arrow; red → respond to the *side* arrows). Rules change, so you must switch. | **Task-switching, attention to detail, learning from mistakes, adaptability** | Accuracy, reaction time, error-recovery, cost of switching `[PREP-VENDOR]` |
| 5 | **Lengths** | Judge which face has the **longer/shorter mouth** (subtle perceptual differences); the rule can flip. | Attention to detail, **effort, adaptive learning**, perception | Accuracy on subtle differences, effort sustained, adaptation `[PREP-VENDOR]` |
| 6 | **Cards (Iowa Gambling Task)** | Start with ~$2,000; draw from four decks with different reward/penalty structures; maximise winnings. | **Reward sensitivity, risk under uncertainty, pattern recognition/learning, decision-making** | Shift toward advantageous decks over time (learning rate), risk profile `[PREP-VENDOR]` |
| 7 | **Tower (Tower of London)** | Rearrange coloured rings/discs to match a target configuration in the **minimum number of moves**. | **Planning, problem-solving** | Moves vs optimal, planning time before first move `[PREP-VENDOR]` |
| 8 | **Money Exchange #1 (Trust game)** | You get ~$10 and choose how much to send a partner; the sent amount is **tripled** on receipt; the partner may return some. | **Trust, risk tolerance, fairness, altruism** | Amount sent (trust), expectation of reciprocity `[PREP-VENDOR]` |
| 9 | **Money Exchange #2 (trust/reciprocity, second role)** | Both start ~$5; one randomly gets +$5; players decide how much to give/take over two rounds. | **Trust, altruism, fairness, generosity, decision-making** | Give/take amounts, reciprocity behaviour `[PREP-VENDOR]` |
| 10 | **Easy-or-Hard (effort/motivation)** | Each round, choose a **low-reward/high-probability (easy)** task or a **high-reward/low-probability (hard)** task, sometimes with stated reward and odds. | **Effort allocation, motivation, risk tolerance, rational reward-maximising, resilience** | Hard/easy choice ratio vs stated odds, effort under varying incentive `[PREP-VENDOR]` |
| 11 | **Stop (Go/No-Go — response inhibition)** | Press only when a target shape/colour appears; withhold for others (which flash rapidly). | **Impulse control, attention, focus, reaction time** | Commission errors (pressing on no-go), omission errors, reaction time `[PREP-VENDOR]` |
| 12 | **Faces (emotion recognition)** | Identify the emotion in facial expressions; sometimes paired with a short context/story that may contradict the face. | **Emotion recognition, emotional intelligence, empathy** | Accuracy, use of context vs face `[PREP-VENDOR]` |

Across all twelve, the telemetry themes are the same: reaction time, accuracy, risk-taking under uncertainty, learning rate, altruism/fairness, effort allocation, impulse control, planning depth, working-memory span — all behavioural, none self-reported. `[INFERRED from the above + INDEPENDENT audit]`

**How many "traits" is contested, and it matters.** Prep sources aimed at J.P. Morgan cite "**91 social, cognitive, and behavioral traits**"; earlier press said "**49**"; the audited SVM code actually used **64 features**, with the final fitted models keeping **44–45**. `[PREP-VENDOR]` / `[INDEPENDENT — FAccT §3.2]` The clean way to think about it: **"traits" is marketing language and "features" is model language** — the raw games emit roughly 60–90 candidate features, and a fitted model keeps ~44–56 of them. `[INFERRED]` Candidate-facing results, when shown at all, come back as **9 trait families**: Effort, Risk, Fairness, Emotion, Decision Making, Focus, Learning, Attention, Generosity. `[PREP-VENDOR — Lumovest JPM guide]`

**Logistics.** Available on web/iOS/Android, translated into several languages. `[INDEPENDENT]` A prep-vendor consensus is that a **PC is recommended over a phone**, and that you may **pause *between* games but cannot restart a game mid-play.** `[PREP-VENDOR — GraduatesFirst]` There are **built-in accommodations for colour-blindness and dyslexia** at the game level (§4.9). `[INDEPENDENT]` One data rule matters for anyone who gets interrupted: a player who misses **more than two games** is treated as incomplete and dropped from analysis, and missing individual feature values are **median-imputed.** `[INDEPENDENT — FAccT §3.2]` Official mid-game disconnect/reconnect behaviour is **not documented** `[UNKNOWN]`; the inference is that a mid-game disconnect voids that game's traits, which are then imputed. `[INFERRED]`

## 4.5 Is it tailored to the role?

**Yes — and this is the differentiator that everything else hangs on.** The 12 games and your raw traits are *constant*; what changes between firms is the **model you are matched against.** There are two kinds:

- A **custom (bespoke) model** is built from a *specific client's own incumbents* — the firm's current high performers in the target role, as judged by the firm's own performance metrics. The **in-group dataset typically contains 50–100 incumbent players.** `[INDEPENDENT — FAccT §3.2, direct]`
- A **core model** is a standardised, generic model used when a client lacks enough incumbents or wants a general-fit screen. `[PREP-VENDOR]` / `[INFERRED]`

The exact minimum-incumbent cut-off that separates "we can build you a custom model" from "you fall back to core," and the precise architecture of the core model, are **proprietary** `[UNKNOWN]` — the only cited floor is the ~50-player figure from the audit. Either way, **the 12 games are identical whether you are applying to a warehouse or a trading desk; only the benchmark differs.** `[PREP-VENDOR]` / `[INFERRED]`

The consequence is counter-intuitive: **the exact same trait profile can *match* firm A and *not match* firm B**, because different roles reward different trait combinations. "There is no universal 'good' profile — different roles require different trait combinations." `[PREP-VENDOR, consistent with the audit's role-specific in-group design]` A high risk-tolerance, fast, low-altruism profile might resemble one firm's sales-and-trading incumbents and be a poor match for another's operations or research desk. **This is why "faking the trader" is a losing strategy (§4.7): you don't know which traits your target firm's model weights, and no single profile wins everywhere.**

Customisation goes further than most candidates realise, which matters for the legal chapter. Pymetrics may "customize their model training and adverse impact assessment process for specific clients … even swapping out the four-fifths fairness metric for an entirely different fairness criteria." `[INDEPENDENT — audit §4.4 Limitations]` **The audited fairness guarantees apply to the *baseline* codebase, not to every bespoke variant.** Clients can also customise report *language* to their own "capability language" (one used a "Head, Heart, Hands" ethos). `[VENDOR]` And if no model can meet *both* the performance and fairness bars, the job analyst re-engages the client to refine the role or re-select incumbents; if it still can't be done, **no model is deployed at all.** `[INDEPENDENT — audit §3.3]`

## 4.6 How they screen and filter — scoring, norms, cut-offs, ranking

The pipeline is: **gameplay → traits/features → an SVM (support-vector-machine) predictive model → a percentile-based fit score → a recommendation tier.** `[INDEPENDENT — FAccT §3.2]`

The model is built from **three datasets** `[INDEPENDENT — FAccT §3.2]`:

- the **in-group** — the client's high-performing incumbents (typically 50–100 players);
- the **out-group** — a random sample from pymetrics' historical player database (600k+ players), used as a contrast that approximates the applicant pool;
- the **bias group** — players who volunteered demographic labels, **typically more than 10,000 users**, engineered to hold equal proportions of each EEOC protected group, and used **only** for adverse-impact testing, never as a training feature.

Your fit is expressed as a **fit percentile against the role model** and mapped to **three tiers**: **Highly Recommended / Recommended / Do Not Recommend** (some docs "Not Recommended"). `[INDEPENDENT — audit §3.3; BABL AI 2025]` The thresholds are typically **the 50th and 70th**: **≥70th = Highly Recommended, 50th–70th = Recommended, <50th = Do Not Recommend**, client-customisable. `[INDEPENDENT — FAccT §3.2, direct]` **The subtlety: this is *not* a classic norm-referenced percentile against the general population** — it is a **fit percentile against the role model**, i.e. how close you are to the target profile, not "you beat 70% of people." `[INFERRED from the tier construction + the audit's "fit percentile" language]`

**What the recruiter sees:** a recommendation tier plus a trait profile per candidate, on which they may apply further filters (e.g. a CV screen) before interview. The recruiter does **not** get a single number you could appeal. `[INDEPENDENT — audit §3, step 5]` **What you see:** very little — usually a **trait report/personality description across the 9 trait families**, with **no score** and **no indication of how you compare to the firm's target profile.** Some employers email a result; some show nothing. `[PREP-VENDOR — Lumovest, GraduatesFirst]`

**Two candidate-facing facts dominate here.** First, **retake:** you generally **cannot retake for ~330 days** ("once every 330 days"). `[PREP-VENDOR]` Second — the one most candidates miss — **your results follow you across employers.** You play the 12 games **once**, and **each pymetrics-using employer you apply to within the ~330-day window re-scores your *same* traits against its *own* model.** `[PREP-VENDOR — Lumovest, CareerTestPrep, stated repeatedly]` This cuts both ways: a profile you're unhappy with can't be re-attempted for about eleven months, **but** a profile that *fails* firm A may still *pass* firm B, because their models differ (§4.5). `[INFERRED]`

**The funnel point (per the §5.6 brief).** In a J.P. Morgan-style pipeline the pymetrics stage is an **early, broad screen** ahead of the HireVue and the assessment centre, designed to thin a large applicant pool. It is not usually the single tightest cut (the CV screen and final assessment centre remove large numbers too), but it is unusually **high-leverage** for one reason no other stage shares: **you sit it once and it gates every pymetrics firm for eleven months.** Treat it as the most consequential 30 minutes in your early pipeline. (Chapter 6.8 maps where each firm's real chokepoint sits.)

## 4.7 How to score well — legitimate, specific, actionable

**Start from the truth that there is nothing to "score well" on.** There are no right answers and no target you can see, so the legitimate goal is to **play authentically, cleanly and consistently** so that your genuine profile is measured accurately — then let the matching do what it does. `[PREP-VENDOR]` / `[INDEPENDENT]` Everything below serves *accurate measurement of the real you*, not "beating" the test.

**Learn the formats in advance so you don't waste live trials figuring out mechanics.** The single most concrete, legitimate edge is **format familiarity**: because several games *measure learning rate across trials*, spending your first few balloon-pumps or card-draws working out the rules can distort the very trait being measured. Read each game's instructions carefully, and know roughly what each of the twelve does (the table in §4.4) so you start "on trait" rather than confused. `[PREP-VENDOR — psychometric-success, JobTestPrep]`

**Play when you are mentally fresh, with distractions removed and a stable connection.** Morning, quiet room, PC over phone, notifications off. `[PREP-VENDOR — GraduatesFirst]` This is not superstition: reaction-time and attention games directly capture tiredness and interruption.

**Be consistent, not erratic — especially on the risk games.** This is the most useful specific nuance. Wildly inconsistent balloon-pumping or card-drawing produces a **noisy, hard-to-match profile**; measured, internally-consistent risk behaviour reads as a stable risk trait that a model can actually place. Aim for a coherent approach you hold across trials rather than swinging between reckless and timid. `[PREP-VENDOR]` / `[INFERRED]`

**Do not try to fake a persona — the debunk matters.** Because the model matches you to a role whose target profile you *cannot see*, deliberately playing "like a trader" can backfire: you don't know which traits that firm's model weights, and the inconsistency of acting a part *hurts* your signal. `[INFERRED from mechanics + §4.5]` Several games are **hard to fake convincingly** by design — the trust/altruism money games and reaction-time games resist gaming, and pymetrics' own auditors noted that faking a whole workforce would require "train[ing] human beings to play the games in very specific ways, or writ[ing] software to emulate a human." `[INDEPENDENT — audit §5.1 footnote]` The same logic defeats an individual candidate. **The winning move is to be a clean, consistent, well-rested version of your real self.**

**On the prep-vendor simulations.** JobTestPrep, GameAssessmentPrep, CogniPrep and others sell practice packs (from ~$59). Their genuine value is **format familiarity** — seeing the twelve games once so the live sitting isn't your first — **not** a route to "beat" the assessment, which their commercial incentive encourages them to imply exists. `[PREP-VENDOR — note commercial bias]` A free read of §4.4 delivers most of that value.

## 4.8 Integrity monitoring — what Pymetrics actually detects

Pymetrics' integrity posture is unusual and, for most candidates, **reassuringly light**. The assessment is **typically unproctored** — you play remotely, unsupervised, on your own device, and **no webcam or lockdown-browser option surfaced** in any vendor or independent source. `[INFERRED from remote web/mobile delivery + no proctoring mention anywhere]` (Whether any device/keystroke anomaly flag exists is a genuine `[UNKNOWN]`; the platform *does* capture fine-grained keypress timing on the keypress and stop games, which could in principle flag bot-like input, but there is no public confirmation it does.)

The reason it can afford to be unproctored is that it is **hard to fake by design** — and the vendor sells this as a virtue *over* proctoring:

- There are **no "correct" answers to look up** — behavioural traces like reaction time, risk consistency and altruism are not answerable from a search engine. `[INFERRED]` / `[VENDOR]`
- Its manipulation-resistance was formally tested from the *client* side: the Northeastern auditors "were unable to circumvent the fairness checks … by manipulating in group data," and concluded that faking a workforce would take trained humans or bots. `[INDEPENDENT — audit §5.1]`

There is **one candidate-side integrity weakness worth naming honestly**: the **Digits (memory) game** instructs you "do not write your answers down," but this is unenforceable on an unproctored assessment — a flaw one prep source calls "a major flaw … that compromises the integrity of the assessment." `[PREP-VENDOR — Lumovest]` Writing the digits down could inflate the **working-memory trait** — but note the caveat: that is **one trait among ~90**, with no reason to think it's weighted the way you'd hope in your target firm's model (§4.5). Inflating one trait toward an unknown target is as likely to *distort* your match as improve it. It is not worth doing, and it is dishonest.

## 4.9 How candidates commonly trip the system — including honestly

Because the assessment is unproctored and hard-to-fake by design, its **false-positive surface is small** — genuinely good news for anyone flagged by a proctored exam elsewhere who fears every assessment is a trap. There is no eye-tracking to misread you, no tab-logging to panic over, no facial analysis. The ways candidates come unstuck here are different and mostly *honest*:

- **Erratic play producing a noisy profile.** Not cheating — just inconsistency (§4.7). A candidate who swings wildly on the risk games generates a profile that matches nothing cleanly, and can be tiered out despite being a strong hire. `[INFERRED]`
- **Learning the mechanics on the clock.** Wasting the first trials of a learning-rate game working out the rules depresses the very trait being measured. Fixed by format familiarity (§4.4, §4.7). `[INFERRED]`
- **Motor / reaction-time differences.** Several games have **inherent speed and rapid-click demands**; a slower motor tempo — through age, injury, or a motor condition — can shift reaction-time traits away from a target profile. `[INDEPENDENT — MIT Technology Review, 2021-07-21]`
- **Colour-vision deficiency.** Games like **Arrows** and **Stop** use **colour-coded rules**; uncorrected colour-blindness can produce errors that read as poor attention or impulse control rather than a perceptual issue. `[INFERRED from mechanics]`
- **Flashing images and attention demands** can disadvantage candidates with visual-processing, attention or epilepsy-related conditions. `[INDEPENDENT — MIT Technology Review]`
- **A mid-game interruption or disconnect.** Miss more than two games and you're dropped as incomplete; a single dropped game is median-imputed, blurring your profile (§4.4). `[INDEPENDENT / INFERRED]`

**These disability and difference risks are the real false-positive vector here** — aggravated by the ~330-day carry: a well-qualified candidate with slow reaction time, ADHD or a colour-vision deficiency who does *not* request an accommodation could be mis-matched to "Do Not Recommend," and that **mis-match then propagates across every pymetrics firm for eleven months.** `[INFERRED]` That is why §4.10's central instruction is to request accommodations *before* you play.

**The documented critique history** (for context and your rights). The **2020 Northeastern audit** found the baseline pipeline fair-by-construction but explicitly did **not** validate that the games predict job performance (§4.2, §4.10). `[INDEPENDENT]` The **2024 FAccT "Algorithmic Monocultures" study** found that, deployed per-position across 156 employers, **10.62% of positions still adversely impacted Black applicants**, with **~25.87% of Black applicant submissions** going to positions with "discriminatory outcomes" per federal guidelines. `[INDEPENDENT — via Fortune]` **MIT Technology Review (2021)** documented the disability-access concerns above. `[INDEPENDENT]` None of this makes the tool uniquely dangerous — but it means the accommodation and data-rights routes (§4.10–4.11) are real and worth using.

## 4.10 How to be unambiguously clean

The good news is that "clean" here is easy, because there is little to police. The important moves are about **accurate measurement** and **pre-empting a mis-match**:

- **Request accommodations *before* you play** if you have a motor, visual, visual-processing, attention/neurodevelopmental (autism, ADD/ADHD, dyslexia, dyscalculia), or speech/language condition, or a colour-vision deficiency. Pymetrics offers, on candidate self-selection from a disability list before play: a **modified colour palette for colour-blindness**, and **more time on time-sensitive games plus an adjusted font** for the conditions above. `[VENDOR — Accessibility Accommodations PDF]` Crucially, **the employer is *not* told which candidates requested accommodations** — the selection is confidential. `[INDEPENDENT — MIT Tech Review]` / `[VENDOR]` This is the single most protective step a disadvantaged candidate can take, and because results carry ~330 days, it is worth getting right the first time.
- **Know the hard stops.** Pymetrics tells candidates to **stop and not play** if they have a visual impairment needing a braille display, or dominant-hand motor/mobility/coordination issues — in which case the **employer must offer an alternative selection process.** `[VENDOR]` For some conditions (e.g. cerebral palsy, MS, epilepsy, non-dominant-hand motor issues, mental-health conditions) the games are **not modified**, and you're directed to contact support after playing if you struggled — a weaker safeguard, so raise it proactively in writing.
- **Play the real you, consistently.** Don't write the digits down, don't try to act a persona, don't let anyone else play. Not because you'll be caught (you probably won't) but because a faked or inflated profile is more likely to *mis*-match than help (§4.7–4.8).
- **Sit it once, properly.** Fresh, quiet, PC, stable connection, notifications off — so a dropped game or an attention lapse doesn't blur your profile.

## 4.11 If you are flagged or rejected

Your full rights are in Chapter 6.7; the pymetrics-specific points follow. Because pymetrics rarely "flags" in the proctoring sense, the realistic scenario is a **"Do Not Recommend" tier or a silent rejection you suspect was driven by the games**, possibly reached with little human involvement.

**Use the corrected UK automated-decision framework.** The old shorthand of an "Article 22 prohibition" on solely-automated decisions is **out of date.** Under **Articles 22A–22C UK GDPR, as amended by the Data (Use and Access) Act 2025 (in force 5 February 2026)**, the regime is a *safeguards* model: where a decision about you is solely automated and has legal or similarly significant effects, you have the right to be **informed**, to **make representations**, to **obtain human intervention**, and to **contest** it. A pymetrics tier used to auto-reject with no human looking would sit squarely in that regime; a tier a recruiter genuinely reviews may not. Either way, invoking these rights forces the firm to confirm whether a human reviewed you. **Cross-reference Chapter 6.7 for the full mechanics.**

- **Ask for feedback and human review.** Email the recruiter; where the decision may have been solely automated, invoke the **Article 22C safeguards** — representations, human intervention, contest.
- **DSAR (Article 15).** Request your **trait profile**, any **derived fit scores / recommendation tier**, confirmation of **which model** (custom or core) was used and whether a **human reviewed** the outcome. One month, free.
- **Special-category / disability angle.** If a motor, visual, attention or speech difference effectively caused the mis-match, that can bring **special-category data** and the **Equality Act 2010** duty to make reasonable adjustments into play — a stronger argument, and grounds to ask that you be re-assessed by an alternative method (§4.10).
- **The carry-forward point.** Because your result propagates for ~330 days, a mis-match is worth challenging *promptly* — both to correct this application and to avoid the same profile gating you elsewhere.

**Template — pre-assessment adjustment / accommodation request:**
> Subject: Reasonable adjustment request — [name], [role/ref]
> Dear [team], I've been invited to complete the pymetrics game-based assessment for [role]. I have [a motor / visual / visual-processing / attention / neurodevelopmental / speech-language condition / colour-vision deficiency], which the timed, reaction-based games disadvantage. Under the Equality Act 2010 I request [the built-in accommodated version (extra time / modified colour palette / adjusted font) / an alternative selection method if the games cannot be adjusted for my condition]. I can provide documentation. Please confirm what can be arranged, that my accommodation will remain confidential from the hiring team, and the deadline.

**Template — post-rejection query / data + human review:**
> Subject: Assessment outcome — request for review and data — [name], [ref]
> Dear [team], Thank you for the update. If my pymetrics result contributed to this decision, I request confirmation of whether a human reviewed the outcome and — under Articles 22A–22C UK GDPR (as amended by the Data (Use and Access) Act 2025) — I wish to make representations and obtain human intervention. Separately, under Article 15 I request my trait profile, any fit score or recommendation tier, and confirmation of which model was applied. Please respond within one month.

## 4.12 Step-by-step: how to win this assessment

1. **Reframe first.** Internalise that there is **no score and no target** — your job is to be measured *accurately*, consistently and cleanly, not to hit a profile you can't see. Half of all candidate mistakes die here.
2. **T-minus a few days — learn the twelve formats.** Read §4.4 so you know what each game measures. The goal is to start *on trait*, not to spend live trials learning the rules — which matters because several games measure *learning rate*.
3. **Sort accommodations now, not later.** If you have any motor, visual, visual-processing, attention, neurodevelopmental, speech, or colour-vision condition, self-select the accommodated version or send the §4.11 request **before you play**. It's confidential from the employer, and — because results carry ~330 days — you want it right first time.
4. **Set up for accurate measurement.** PC over phone, quiet room, stable connection, notifications off, at your sharpest time of day. A dropped game or an attention lapse blurs your profile.
5. **Play consistently — especially the risk games.** Pick a coherent approach to the balloons and cards and hold it; erratic play produces a noisy, hard-to-match profile.
6. **Do not fake a persona.** You can't see the target, faking introduces inconsistency that hurts, and the trust and reaction-time games resist gaming. Be a clean, rested version of your real self.
7. **Play it as one continuous, honest sitting.** Don't write the digits down, don't let anyone else play, don't restart games — a distorted profile mis-matches more often than it helps.
8. **Remember it follows you.** You're setting the profile every pymetrics employer re-scores for ~330 days. That's the reason to sit it at your best.
9. **If tiered out or silently rejected, act promptly.** Send the §4.11 human-review and DSAR requests; raise any disability/adjustment angle under the Equality Act and Articles 22A–22C, before the mis-match gates you elsewhere.
10. **Debrief.** Note which firm, whether you got a result back, and (if you can tell) whether it felt custom or core — useful next time a pymetrics firm appears within the window.

## 4.13 Sources for this chapter

All accessed 2026-08-01. Confidence tags as used above.

**Independent:**
- Wilson, Mislove, Ghosh, Jiang — "Auditing the pymetrics Model Generation Process" (Northeastern whitepaper); the authoritative source on mechanics, de-biasing, in/out/bias groups, safeguards, five findings, and scope limits — https://cbw.sh/static/audit/pymetrics/pymetrics_audit_result_whitepaper.pdf
- FAccT '21 — "Building and Auditing Fair Algorithms: A Case Study in Candidate Screening" (SVM, 50–100 in-group, 64 features, 50/70 percentile tiers, IR≥0.8, AUC ~0.70–0.72) — https://www.ccs.neu.edu/home/amislove/publications/Pymetrics-FAccT.pdf
- BABL AI (2025) — LL144 Bias Audit of Harver's Soft Skills Platform (2024 impact-ratio tables, PASS, scope exclusions) — https://harver.com/wp-content/uploads/2025/11/pymetrics-Soft-Skills-Platform-2025-Bias-Audit.pdf
- "Algorithmic Monocultures in Hiring" (FAccT 2024), via Fortune (2026-05-26) — per-position adverse-impact critique and the 10.62% / 25.87% / 14.74% figures — https://fortune.com/2026/05/26/ai-hiring-algorithm-racial-disparities-pymetrics-stanford-study/
- MIT Technology Review (2021-07-21) — disability rights and AI hiring — https://www.technologyreview.com/2021/07/21/1029860/disability-rights-employment-discrimination-ai-hiring/
- Harver acquisition press (PRNewswire) — 11 Aug 2022 completion — https://www.prnewswire.com/news-releases/harver-acquires-pymetrics-further-enhancing-talent-decision-capabilities-across-the-employee-lifecycle-301603823.html
- ACLU LL144 audit tracker — https://github.com/aclu-national/tracking-ll144-bias-audits

**Vendor:**
- Harver — "Harver acquires pymetrics" (branding, distinct identity) — https://harver.com/harver-acquires-pymetrics/
- Harver — gamified assessments product page (soft-skills framing, 25-min duration, client names) — https://harver.com/gamified-assessments/
- pymetrics — Accessibility Accommodations PDF (accommodation list, hard stops, confidentiality) — https://s3.amazonaws.com/pymetrics-public-content-production/pdf/accessibility-accommodations.pdf
- audit-AI (open-source four-fifths bias-testing library) — https://github.com/pymetrics/audit-ai

**Prep-vendor (mechanics/logistics/UK-finance stage; corroborate — commercially biased):**
- GraduatesFirst — pymetrics practice games (12-game logistics, PC-over-phone, 330-day retake, UK client lists) — https://www.graduatesfirst.com/pymetrics-practice-games-digital-video-interviews
- JobTestPrep — Harver/pymetrics assessment pack — https://www.jobtestprep.com/harver-assessment
- psychometric-success — pymetrics test types — https://psychometric-success.com/aptitude-tests/test-types/pymetrics
- Lumovest — J.P. Morgan pymetrics guide (9 trait families, results-follow-you, digits-game flaw) — https://www.lumovest.com/library/careers/jp-morgan-pymetrics/

**Candidate (testimony; treated cautiously — see gap note).** Wall Street Oasis ("Pymetrics… What the fuck??") and The Student Room threads (AstraZeneca pymetrics t=6265898; GSK/AZ apprenticeship t=7179651) returned **HTTP 403** to the fetcher on the access date, so no verbatim quotes or commenter counts could be extracted; sentiment above is via search-snippet summaries only, and `[CANDIDATE, n=X]` counts are therefore **unavailable**. `[CANDIDATE]`

*(Residual gaps — undisclosed acquisition price; no public peer-reviewed criterion-validity study (Baker 2019 confidential); exact custom-vs-core incumbent cut-off and core-model architecture (proprietary); mid-game disconnect policy; whether any anti-cheat/anomaly flags exist; the current 2026 live UK-finance client roster beyond JPM and BNP Paribas; and post-2022 codebase changes since the 2020 audit — are logged in research/04-pymetrics.md and the master gap register.)*
