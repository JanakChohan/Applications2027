# Blackstone pymetrics — Complete Breakdown & Playbook

**Context:** Blackstone campus programme, invite from `Blackstone@pymetrics.com`, 3-day completion window, ~25–30 min battery.
**Provider:** pymetrics, acquired by **Harver** in 2022. Same engine, Harver branding creeping in.

---

## 0. READ THIS FIRST — two findings that reframe the whole thing

### (a) At Blackstone, the games are probably not what is rejecting you

This is the most important thing in this document, and almost every prep site gets it wrong.

Candidate reports across Wall Street Oasis and r/FinancialCareers (2022 through September 2026) converge hard: **for US campus, sophomore and Future Leaders programmes, essentially everyone who completes the games gets invited to the next stage.** Specific first-hand reports:

- *"Yesterday I took the Pymetrics test (12 games), and today I received another email about a Pymetrics digital interview."* → reply: *"I think everyone gets it. I got it same day I finished the games or within 12 hours."*
- *"I got the games a day after I applied, then video like 40 minutes after I did games."* — a 40-minute turnaround is not a human review, and barely a model review.
- *"I did my games at like 7pm and heard back like literally 9am the next day. I think probably they have an automation or something for the games."*
- One candidate who was *"really good on the first 9 games, mediocre on 2–3"* still advanced.
- One candidate reports receiving the video interview **before finishing the games** — structurally impossible if the games gated it.

Blackstone's own 2026 Future Leaders posting lists the games as a **completeness requirement**, not a scored gate: *"Complete all steps in the application process, inclusive of Pymetrics Games and Digital Interview by the application deadline."*

**Nobody in any thread reported a "you did not pass the pymetrics games" rejection.** The failure mode people actually experience is silence — the Workday status quietly flips to "no longer under consideration."

The most-upvoted explanation on WSO, from someone who advanced: *"if you got a video interview, and not just pymetrics, it probably means ur resume had a high enough GPA, good enough buzzwords, and might've mentioned a target school."* And from a September 2026 candidate mapping the whole funnel: *"pymetrics digital interview… **Do well on this — it's the hardest part tbh.**"*

**So where are you actually being cut?** Most likely one of:
1. **The CV/eligibility screen**, running in parallel with the games.
2. **The digital interview** — the first genuine behavioural gate.
3. Later rounds.

Caveats worth stating honestly: **London/EMEA is slower and more selective** — several London candidates completed the games and never received the interview, and invites there go out in batches over days or weeks, so silence for a week is not a rejection. And this is candidate-reported evidence, not Blackstone policy, so treat it as strong indication rather than certainty.

**What this means for you:** if you have "failed so many times", it is worth working out *which stage* you actually failed at. If you completed games and then got a video interview and then heard nothing — the games were never the problem. Put your preparation into the digital interview and the CV, and give the games a competent, unpanicked run.

### (b) The 330-day lockout — one attempt, reused everywhere

pymetrics lets you play the real battery **only once every 330 days**. Official policy, from pymetrics' own support centre:

> "Pymetrics allow candidates to play the games **once every 330 days**. If you have completed the required games within the last 330 days then **you won't be required to replay. At the point of login, your existing gameplay data will be re-assessed against the new role profile you have applied to.**"

Your account identifier is **your email address**. Your invite's line about not needing to replay is simply this platform rule, not a Blackstone concession.

**Consequences:**
- **A previously poor performance is reused. There is no "keep the better attempt."** Within 330 days your raw trait vector is frozen; only the role model it is scored against changes.
- **One attempt is shared across every employer on the platform** — Blackstone, JPMorgan, Bain, BCG, Accenture, PwC, Unilever, LinkedIn, Goldman. As one candidate put it: *"One attempt follows you everywhere, so don't burn it on a firm you don't care about."*
- **Within Blackstone, one play covers every group and programme** you apply to in the cycle.
- **It also cuts favourably:** because each employer scores your identical profile against a different model, a rejection elsewhere says nothing about Blackstone. One Blackstone candidate's report captures the mechanism — *"I also got high risk tolerance which makes me doubt it is good for private equity."* Same data, different verdicts.

**So: before anything else, work out whether this is a fresh attempt or a replay.** Open the link and see whether it offers the games or tells you existing results will be used.

### One correction to the advice you will see elsewhere

**support@pymetrics.com will not grant you a do-over because you played badly.** Their documented remit is narrow:
- **Merging or updating account emails** (e.g. a lost university address).
- **Cross-region account transfers.** Employers choose where assessment data is hosted, and if a prior play sits in a different data region you may be prompted to create a new account under the same email — *"please contact support@pymetrics.com who will support you in transferring your account and gameplay."* **This is the one documented situation where results genuinely might not carry over** — and note it cuts both ways: if you want your good result to follow you, you have to actively ask.
- **Accommodations** (see below).
- **Genuine technical failure mid-session** — games cannot be paused, so a real crash is the realistic basis for a reset. Document it with screenshots and go through **Blackstone campus recruiting** as well as pymetrics support.

**Accommodations are worth knowing about and are underused.** pymetrics offers game configurations for **ADHD, dyslexia and colourblindness** via a "Game Configuration" pop-up **before you start** — and these **are not shared with the employer**. If any of those apply to you, this is a legitimate, confidential adjustment, and several of the games (Digits, Arrows, Stop, Lengths) are precisely the kind that an unaccommodated attention difference would distort.

Your real leverage, if you need any, is with **Blackstone campus recruiting** — they choose the model and decide how much weight the games carry. pymetrics support only administers platform rules.

---

## 1. How you are actually scored

Most prep content guesses at this. It does not need to be guessed: pymetrics' **source code was audited by Northeastern University researchers** in a peer-reviewed paper (FAccT '21), and a **2026 FAccT paper analysed 4,197,168 real pymetrics applications** across 1,746 positions and 156 employers. The mechanics are unusually well documented.

### The actual model

It is **not** a "personality match score". It is a **Support Vector Machine trained on ~64 gameplay features**.

1. **In group:** gameplay from **50–100 high-performing incumbents** in the target role at the client, identified by a job analysis.
2. **Out group:** a **random sample from pymetrics' database** approximating the general applicant pool.
3. The SVM is trained to **discriminate the in group from the out group**. The model does not learn "what a good employee looks like" in the abstract — it learns **what separates Blackstone's high performers from a random person**. Which employees the client nominates is described in the research as "the primary way that the employer influences the classifier."
4. **Bias group:** >10,000 held-out users with volunteered demographics, engineered to contain equal proportions of each EEOC protected group. Used **only** for evaluation, never training. pymetrics searches over feature permutations for "the most predictive, least biased permutation" — a model failing the **four-fifths rule** is not deployed at all.
5. Output is a probability **p ∈ [0,1]**, thresholded into tiers.

### What the threshold actually is

- Internally: thresholded at **p = 0.5** → "recommend" / "do not recommend".
- As presented to recruiters: **three tiers — Not Recommended / Recommended / Highly Recommended — at the 50th and 70th score percentiles** (customisable; some clients use five tiers or a red-amber-green display).

**It is a relative percentile cut, not an absolute standard.** You are ranked against a distribution.

### The number that should change how you feel about this

From the 4.2M-application dataset: **on average 58.2% of applicants per position are recommended.** Only 41.8% are not.

That is a far softer filter than candidates assume. pymetrics is very unlikely to be the main reason you are not getting Blackstone offers — the CV screen and the ~0.2–0.5% overall acceptance rate are doing most of the cutting. Which also means: **do not catastrophise this test.** It is a wide gate you are trying not to trip over, not a needle to thread.

### Data cleaning — three rules with real consequences

1. **More than two missing games = your session is marked incomplete and you are removed from analysis.** Finish everything. If a game glitches, complete the rest anyway.
2. **Outlier clamping:** values outside psychometrically-set bounds (several SDs from the mean) are **rounded down to the min/max of the range — not rejected, and not flagged.** So an implausibly good score does not set off an alarm; it just silently stops helping you.
3. **Median imputation:** missing feature values are filled with the population median.

### The 9 trait dimensions (~91 traits)

| Dimension | What it captures | The two poles |
|---|---|---|
| Attention | Reviewing information before acting | Methodical ↔ speed-focused |
| Decision Making | Time and planning invested in decisions | Deliberative ↔ instinctive |
| Effort | Effort as a function of reward size and probability | Hard-working ↔ outcome-driven |
| Emotion | What you rely on to read others | Facial expression ↔ situational context |
| Fairness | Reading situations as fair/unfair; response to inequity | Tolerant ↔ strongly reciprocal |
| Focus | Speed of thought; managing change and distraction | Sustained ↔ flexible |
| Generosity | Personal sacrifice for others' benefit | Self-interested ↔ altruistic |
| Learning | Adaptation to feedback | Fast adapter ↔ steady |
| Risk Tolerance | Calibration of risk against reward | Cautious ↔ risk-seeking |

Note every dimension is a **spectrum with two named poles, not a "more is better" scale.** pymetrics has never published the full 91-trait list; any prep vendor claiming to have it is reconstructing.

### Three consequences most candidates miss

- **"Maximise everything" is the wrong instinct.** The target is a specific profile, not an extreme. Maximum risk tolerance is not better than moderate — for some roles it is worse.
- **The 10 skill games do have better and worse play.** Attention, memory, learning and planning games have real performance metrics. Practice genuinely lifts these (one platform reports a **median +16% improvement between first and fifth practice attempt**).
- **The 2 Money Exchange games genuinely have no right answer.** They are preference measures and are explicitly not scored good/bad.

### What Blackstone specifically appears to weight

**Blackstone uses the standard 12-game battery — no custom subset.** So prepare all twelve; there is no Blackstone-specific shortlist to hunt for.

There is **no published Blackstone model** — it is proprietary. But two things are informative.

**Blackstone's own stated values:** relentlessly pursue excellence · never compromise integrity · outperform through innovation ("builder mindset") · deliver for our clients ("meticulous custodians of capital") · work humbly, work together. Plus stated analyst criteria: intellectual curiosity, attention to detail, resilience.

**Actual candidate trait printouts** (the platform shows you your top traits at the end). Among Blackstone candidates who advanced: **Fairness, Effort, Decision Making, Learning** in one report; **Learning, Generosity, Decision Making** in another. That second candidate added the most telling line in all the research: *"I also got **high risk tolerance** which makes me doubt it is good for private equity."*

Mapping values to dimensions — **this is inference, not fact:**

| Dimension | Likely direction | Why |
|---|---|---|
| **Risk Tolerance** | **Calibrated / mid-range — explicitly not maximal.** | "Meticulous custodians of capital." A PE/credit/RE manager is a downside-protection culture. This is the dimension most likely to be non-monotonic. |
| **Attention / Focus** | High | "Attention to detail" is Blackstone's own stated criterion. |
| **Decision Making** | **Accuracy-weighted, with steady — not frantic — speed** | Judgment culture, not trading-floor reflex. One vendor page claims hesitation is penalised; every other source contradicts it. Discount that. |
| **Learning** | High | "Outperform through innovation", builder mindset. |
| **Effort** | High | "Relentlessly pursue excellence." |
| **Fairness / Generosity** | Mid-to-upper, not extreme | "Work humbly, work together" + integrity. Extreme generosity plausibly reads as poor capital discipline; extreme selfishness as a teamwork flag. |
| **Emotion** | Moderate weight | Client-facing culture, but typically lower-weighted for junior analyst models. |

**Treat division-level claims with suspicion.** Prep vendors assert that Real Estate and Credit weight long-term planning while PE and Tactical Opportunities weight adaptability, and that Analyst vs. VP profiles differ. These are plausible and entirely unsourced. Reported context for scale: ~57,000 applications for ~138 entry-level seats.

### Where it sits, and what comes next

The games arrive **within hours to a couple of days of applying** (reports range from one hour to five days) — which is why prep has to happen *before* you apply, not after the invite lands. The confirmed funnel:

```
Workday application (CV + questions)
      ↓  hours → ~2 days, largely automated
pymetrics 12-game battery      ~25 min · one attempt · camera OFF · 3-day window
      ↓  minutes → ~4 days; frequently same day
pymetrics Digital Interview    one-way video · camera ON · 2-day window  ← THE REAL GATE
      ↓  ~1–3 weeks
First round — live Zoom with a talent specialist (some groups add a timed maths test)
      ↓  ~1–3 weeks
Superday — in person for investing roles, virtual for corporate; ~5 × 30-min back to back
```

Whole process runs roughly 24–45 days. Interviews are scored against **Blackstone's Leadership Framework: drive, judgment, inclusive leadership.**

**The 3-day window is real** — the invite states the application will otherwise be discarded — though one candidate reported being four days late and still receiving the next stage. Do not rely on that.

**Check your dashboard's home tab and complete every listed item.** Harver warns that "some pymetrics assessments require additional games and/or steps" — some employers add five gamified numerical/logical games on top of the twelve. No Blackstone candidate has reported these, but the 12-game count is not guaranteed.

### The stage you should actually be preparing for

Since the games appear near-automatic and the digital interview is where candidates say the process gets hard, here is what is known about it:

- **Delivered on the pymetrics platform, not HireVue** — though everyone, including some Blackstone recruiters, calls it "HireVue". The mechanics below are pymetrics', so expect these.
- **~3–5 questions in about 4 minutes total.** Camera on.
- **Unlimited practice on a test question up front** — use it properly, it costs nothing.
- **3 minutes to prepare before each real question.** Self-view and the timer can both be toggled off. 10-second warning before time expires.
- **2-day completion window.**

Reported questions, from candidates:
- *"Macroeconomic trends and alternative investments"*
- *"Greatest challenge you've overcome"*
- *"What do you want to gain from the programme"*
- *"If you had X amount of money, what would you invest it in and why"*
- BXCI version: *"very behavioural — how you dealt with feedback from a higher-up"*
- Recurring: **"talk about a recent Blackstone deal"** — *"Blackstone always ask you to talk about a recent deal made by them."* Have two ready, with a view on them.

One candidate who received an offer from the Future Women Leaders programme with **no referrals** described it as: pymetrics → a week later the video (no technicals; diversity commitment, behaviourals, and a Blackstone deal) → offer a week or two after.

Note: if you apply to several groups, some candidates report **one video response being reused across all of them** — so a single strong recording can carry multiple applications, and a weak one can sink them together.

### The finding that should change your application strategy

The 2026 monoculture study found something important:

- Of applicants who apply to ten pymetrics-mediated positions, **4% are rejected from all ten** — and rejections are **correlated across employers** far more than chance would predict, because **42 pymetrics models are shared across multiple companies**. A rejection under a shared model mechanically propagates.
- But the same study ran the counterfactual: if every applicant were scored by *every* pymetrics model, **every single applicant would be recommended by at least one.** There is no such thing as a universally unemployable profile.
- To get systemic rejection below 0.1%, applicants need roughly **25 applications** rather than 10.

**Translation: if pymetrics keeps blocking you, the highest-return response is breadth, not profile optimisation.** Your profile is not bad; it is being repeatedly matched against a narrow, correlated set of models. Widen the net.

## 2. Game-by-game breakdown

Each entry: **mechanics → metric extracted → what good looks like → how to play → what kills you.**

Every game is a repackaged academic task, and **pymetrics' own patent (US9842314B2) names them** — so the published literature on each task tells you exactly what is being measured. Where the patent and the prep vendors disagree, the patent wins.

---

### 1. Keypresses — motor speed & instruction-following
- **Mechanics:** A brief READY period, then **GO** — press the spacebar as fast as you can until the **STOP** cue. Reported durations vary (roughly 10–60 seconds; practice versions use ~15s). **The live tap counter is deliberately hidden** so you cannot pace yourself against it.
- **Metrics:** total valid taps, **taps per second**, individual tap timestamps (so rhythm and consistency are visible), and **instruction-following — any press before GO or after STOP**.
- **Good:** a high, *even* rate and a clean stop.
- **The underlying task:** the **Halstead–Reitan Finger Tapping Test**. Normative dominant-hand rate is **~55 taps per 10 seconds (~5.5 Hz)**. Aim for a steady **5–7 Hz**.
- **Play:**
  - Use your **dominant index finger**, compact even motion, and **let the key fully reset between taps** — mashing a partly-depressed key registers fewer presses than it feels like.
  - **Do not alternate hands or use two fingers.** At least one prep vendor recommends this to beat the baseline; it is off-protocol, it contradicts the instruction you are given, and inter-press-interval structure may expose it. It is the riskiest single piece of advice in the prep literature.
  - **Establish your rhythm immediately** rather than starting slow and accelerating.
  - **Watch the cue, not your hand.**
  - Start from a neutral finger position — do not rest pressure on the key in anticipation.
  - On STOP, **lift your finger clear of the key** as a deliberate act.
- **Kills you:** pressing before GO or continuing after STOP. Both are logged, and neither reads as enthusiasm — they read as poor impulse control and poor instruction-following. This game is close to free marks; the only way to lose them is sloppiness at the edges.

---

### 2. Balloons (BART — Balloon Analogue Risk Task) — risk calibration & learning
- **Mechanics:** ~39 balloons, recurring in **three colours**. Each pump = **$0.05**. Pop = lose that balloon's pot. "Collect" banks it.
- **The colour mechanic — the single most important thing in this game:** the colours have **different, hidden burst distributions**. One colour bursts early, one is medium, one goes long. Commonly cited approximate first-pump pop odds are **1/8, 1/32 and 1/128** across the three colours. The pop point is drawn per balloon and conditional risk rises with each safe pump.
- **⚠️ Do NOT memorise which colour is which.** Prep sources flatly contradict each other — one says orange is the fragile one and blue the safe one; another says red and yellow are the favourable colours and blue the weak one. Colour assignment is not reliably documented and may vary. **Walking in with a memorised mapping is worse than walking in with none**, because you will act on it confidently and wrongly. Learn the mapping live, in the first few balloons. The game is explicitly testing whether you *can*.
- **Metrics:** total banked; **adjusted average pumps** (collected balloons only — the standard BART risk index); number popped; **per-colour differentiation**; pumping behaviour immediately after a pop (loss sensitivity).
- **The actual optimum.** pymetrics appears to reuse Lejuez's three original arrays (pop point drawn without replacement from 1–8, 1–32, 1–128). For a uniform draw from N, expected value is maximised at exactly **N/2 pumps**:

  | Array | Optimal pumps | EV at optimum |
  |---|---|---|
  | 1–8 (fragile) | **4** | $0.10 |
  | 1–32 (medium) | **16** | $0.40 |
  | 1–128 (safe) | **64** | $1.60 |

  **The EV curve is very flat near the peak**, which is the single most useful fact here. On the safe colour, 50 pumps returns 95% of maximum value and 40 pumps returns 86%. So **pumping 45–55 rather than 64 costs you almost nothing in money while reading as materially less reckless** — a genuinely free hedge given Blackstone's "custodians of capital" framing. Typical humans manage only ~28 on the safe balloon, so even 45 puts you well above average.
- **Benchmarks** (JobTestPrep practice data): average candidate banks **24–25 of 39 balloons and ~$18**. A cautious profile lands ~30–31 balloons and $17–18; an adventurous one ~18–19 balloons and $20–23. EV-maximising play across all 39 would be around **$27**.
- **Play:**
  - **Deliberately pop one of each colour early** (balloons 1–3) to find where each colour fails. Because "learning from outcomes" is itself scored, the exploration reads well even as it costs money.
  - **But do not over-explore.** You get ~13 balloons per colour. Burning five on deliberate pops leaves only eight to exploit. One per colour, maybe two on the colour you are least sure about — then switch to earning.
  - Then set a **per-colour pump policy** and hold it: high for blue, moderate for yellow, low for orange.
  - Sit a couple of pumps below the lowest pop you have seen for that colour, and creep up if you keep banking safely.
  - **Do not tilt after a pop.** Reverting to tiny pump counts after a burst reads as loss-aversion/poor emotional regulation; pump-count variance after losses is explicitly measured.
- **Kills you:**
  - **Treating all three colours identically.** If you finish pumping the fragile and safe colours the same number of times, you have demonstrated **zero outcome learning** regardless of how much money you banked. Your pump counts should visibly diverge by colour by around balloon 15 — this is probably the most commonly failed signal in the battery.
  - **Loss-chasing** — a pop followed by a much deeper pump run. Reads as poor impulse control, not boldness.
  - **Reflexive collecting at 5–10 pumps every time.** Reads as extreme risk aversion *and* non-learning, and caps you at pennies per balloon.

---

### 3. Money Exchange #1 (Trust Game) — trust & reciprocity *(preference game)*
- **Mechanics:** **One round.** You hold **$10**, the partner holds $0. Send **$0–$10 in $1 increments**; it **triples** in transit. The (algorithmic) partner then returns a portion — reported default is a **seeded-random 30–70% of the tripled amount**. You then rate the exchange's fairness **0–10**.
- **Metrics logged:** amount sent, tripled amount, partner return, both final balances, your fairness rating, **reaction times**, timestamped events. **No score is assigned** — money retained is explicitly not a test score.
- **A quietly important bit of maths:** if the partner returns 30–70% of 3×, you get back **0.9× to 2.1×** what you sent, expected ≈ **1.5×**. Sending *more* is therefore expected-value-positive. So "send little" is not the safe play it feels like — it is simply a low-trust reading, and it also leaves money on the table.
- **What is measured, honestly:** there is no correct amount. $0 = zero trust. $10 = maximum trust. **In Berg, Dickhaut & McCabe's original 1995 trust game the mean amount sent was $5.16 of $10** — so half is both the commonly recommended anchor and the empirically typical human behaviour. $3–$5 is the cautious band.
- **Play:** Send around half. Then **rate fairness against what actually happened**, not against an imagined ideal — if they returned a lot, say it was fair; if they returned almost nothing, say it was not. The coherence between your send and your rating is the signal.
- **Kills you:** sending $0 or $1 (reads as low trust and low risk tolerance simultaneously), or a fairness rating that contradicts the outcome you just saw.

---

### 4. Money Exchange #2 (Dictator / take-option) — generosity & fairness *(preference game)*
- **Mechanics:** Two rounds, **a different partner each time**, and the roles are **reversed between them**:
  - **Round 1 — you are passive.** You and Partner 1 both start with **$5**; the *partner* receives an extra $5 and decides what to allocate to you. You then rate the fairness **0–10**.
  - **Round 2 — you are the allocator.** You and Partner 2 both start with $5; **you** get the extra $5 and control a **give/take slider in $0.50 increments**: positive gives them up to $5, zero keeps everything as-is, **negative takes up to $5 away from their original $5**. Then you rate fairness again.
- **Metrics:** both allocations, final balances, both fairness ratings, reaction times.
- **The real question being asked:** you experience an allocation done *to* you, then immediately make one *yourself*. The interesting variable is **whether being treated badly in round 1 changes how you behave in round 2** — norm enforcement and reciprocity versus a stable disposition.
- **Play:** **Splitting to equality is the clean anchor** — giving $2.50 leaves you both on $7.50. Moderate-to-positive generosity is the safer read. **Taking is the genuinely risky move**: it is the one action here that can flag as a conflict risk. Note the slider defaults to zero, which is *not* neutral in effect — it keeps the whole bonus for you.
- **On "consistency":** do not mechanically engineer round 2 to mirror your round 1 rating. Role-dependent preferences — behaving differently as recipient and as allocator — are treated as **valid behavioural information, not as a contradiction**. Over-choreographing here substitutes a performance for a signal, and it is more likely to hurt than help.
- **Kills you:** taking the maximum $5 from your partner, or rating an obviously lopsided split as perfectly fair.

---

### 5. Digits (Digit Span) — working memory
- **Mechanics:** Starts at about **4 digits**, shown roughly **~900ms per digit**. Type them back in order. Correct → next sequence is **one digit longer**; incorrect → **one shorter**. It is a ±1 staircase that hunts your limit. **Ends after 3 *consecutive* errors — and a single correct answer resets the counter.**
- **Metrics:** **max span**, correct-round count, **best streak**, **submission latency**, and error *type* (transpositions = you held the digits but lost the order; omissions = span exceeded). Note latency is a real feature: slower accuracy-focused play reads as "methodical", faster error-prone play reads as "biased to action". Type at a steady rhythm rather than racing.
- **Because errors must be consecutive, one mistake is survivable.** Do not spiral after a miss — the next correct answer wipes the counter clean. Most people fail this game emotionally, not cognitively.
- **Benchmarks:** average max is **8–9 digits**. **~11 digits ≈ top 20%.** Aim **10–12**. (Some prep sites warn that 14–15 "flags manipulation" — on the documented pipeline it would more likely just be **clamped to the top of the range**, so it would not help you either. Either way there is no upside in writing digits down, and it is explicitly prohibited.)
- **Play:**
  - **Chunk** in 2s or 3s: `729481635` → "729 · 481 · 635". **Pick one chunk size and never switch mid-sequence.**
  - **Use an actual mnemonic, not repetition.** JobTestPrep's data across ~1,000 test-takers is unusually clear: candidates who practised *with a mnemonic technique* gained about **3 digits**; those who simply repeated the game **gained nothing**. This is the highest-return hour of prep available anywhere in the battery.
  - **Subvocalise / say them aloud** — the phonological loop is the actual bottleneck.
  - Convert chunks to familiar numbers (years, ages, phone prefixes).
  - Type immediately; do not rehearse silently while the clock runs.
- **Kills you:** writing digits down — prohibited, and out-of-range values get clamped anyway. More realistically: giving up mentally after two misses, when a single correct answer would have reset the counter.

---

### 6. Easy or Hard (EEfRT — Effort Expenditure for Rewards Task) — effort allocation
- **Mechanics:** Each round gives you **5 seconds to choose** (let it lapse and it **auto-selects Easy and logs that it was automatic** — avoid this):
  - **Easy:** 5 spacebar presses in 3 seconds → **a guaranteed $1.00**
  - **Hard:** **60 presses in 12 seconds** → **$1.24–$4.30**, paid only with the **displayed probability**
  - Probabilities are shown each round. The parent academic task (EEfRT) uses **12% / 50% / 88%**; the pymetrics version may show whole percentages anywhere from ~10–90%. Format is either **12 fixed rounds** or a **2-minute cap**, depending on configuration.
- **⚠️ The easy task is NOT probabilistic — it is a guaranteed $1.** Most online guides get this wrong and apply the probability to both options. Only the hard task is a gamble.
- **Metrics — and this is the important one:** alongside rounds completed, dollars earned, decision reaction time, every keystroke and completion status, pymetrics records **"EV-aligned choices" — the percentage of your decisions that match expected-value logic.** Your rationality is being scored directly and explicitly. This is the most transparently optimisable game in the battery.
- **The maths.** Hard's expected value is `p × reward`. Compare to Easy's guaranteed $1:
  - **If your session is a fixed number of rounds** (time not binding), the rule is simply **take Hard when `p × reward > $1`.**
    - $4.30 at 88% = **$3.78** → Hard, easily.
    - $4.30 at 50% = **$2.15** → Hard.
    - $4.30 at 12% = **$0.52** → Easy.
    - $2.00 at 50% = **$1.00** → a coin flip; take Easy.
    - $1.50 at 88% = **$1.32** → marginally Hard.
  - **If your session is the 2-minute timed mode**, time is the scarce resource and the bar rises, because Hard eats 12s against Easy's 3s. Including the ~5s decision window, Easy earns ~$0.125/s; Hard needs roughly **`p × reward > $2.00–2.50`** to beat that. In practice: **take Hard only at high probability (~50%+) combined with a reward near the top of the range.**
- **⚠️ One complication worth knowing.** In the *canonical* EEfRT the displayed probability applies to **whichever option you pick**, not just the hard one — in which case p cancels and naive per-trial EV says "always Hard", which is obviously wrong. The pymetrics reconstruction describes Easy as a guaranteed $1. Since you cannot be certain which reading applies, use a policy that is correct under **both**:
- **The reading-invariant policy — use this one:**
  - **p below ~35% → Easy, regardless of the reward.** Always.
  - **p above ~75% and reward above ~$2 → Hard.**
  - **In between → Hard only in the top third of the reward range (roughly $3.20+).**
  - Target total around **$8–10**.
- Under either reading, the **clock** is the real scarce resource: a Hard cycle costs roughly 2.5× the time of an Easy one, which is why the bar for Hard is much higher than naive EV suggests.
- **Quick mental shortcuts:** 88% ≈ "nearly all of it", 50% ≈ "half of it", 25% ≈ "a quarter of it". You do not need precision — you need the right side of $1–2.
- **Play:** Show *discriminating* effort. The trait is not "works hard", it is "spends effort where the numbers justify it". Decide fast — decision latency is logged, and in timed mode dithering costs you rounds.
- **What is actually scored:** not your rate of Hard choices, but **whether that rate rises with probability and reward**. Flat behaviour reads badly in both directions — always-Easy regardless of a 90%/$4.30 cue reads as low motivation; always-Hard regardless of a 12%/$1.24 cue reads as poor judgement.
- **Kills you:**
  - Letting the 5-second window lapse — logged as an Easy choice you did not make, corrupting both your choice rate and your latency.
  - **Choosing Hard and failing to land 60 presses in 12 seconds.** That is 5 presses/second — actually test that you can do it. A failed Hard is worse than a taken Easy on both money and persistence.
  - **Switching to Easy because you lost an 88% roll.** Each trial is independent; outcome-driven switching is exactly the noise this task exists to detect.

---

### 7. Stop (Stop-Signal / Go-No-Go) — impulse control
- **Mechanics:** roughly **80 circles over ~2 minutes**, arriving at about **one per second**. Default rule: **red = press spacebar, green = withhold.** At least one source reports the reverse mapping, so **read the instruction screen** — do not assume.
- **It is a Go/No-Go task, not a stop-signal task** — pymetrics' patent says so. If a prep guide quotes you an "SSRT" figure for this game, it is wrong; no stop signal means no SSRT.
- **Metrics:** hits, **misses** (failed to press on red), **correct inhibitions**, **false alarms** (pressed on green — the headline impulsivity measure), go reaction time, **RT variability**, and — tellingly — **the length of the preceding "go" streak before each response**.
- **Benchmark:** aim for **70+ correct out of ~80**. There is **no feedback** during the real assessment, so you will not know how you are doing — do not let that rattle you.
- **Colourblind note:** the accommodation marks red with **stripes and a "P"** and green with **dots and an "H"**, and the configuration is **not shared with the employer**.
- **The trap, and it is a designed one:** reds heavily outnumber greens, so you build a pressing habit. **False alarms cluster immediately after long runs of red.** pymetrics logs the go-streak length precisely because it wants to see whether your inhibition survives momentum.
- **Play:** Rest your finger on the key but fully release between presses. Hold **one** verbal rule ("red = press") rather than tracking both. Keep your gaze centred; do not scan. **After three or four reds in a row, consciously flag the next circle as a fresh decision** rather than another press. Accept a slightly slower go RT in exchange for zero false alarms — commission errors load on impulsivity far more heavily than 30ms of extra latency loads on processing speed.
- **Consistency beats speed:** low RT *variability* matters more than a fast mean, and so does not drifting in the second half.
- **Kills you:** autopilot. Pressing on green is the single loudest impulsivity signal in the battery, and it happens to almost everyone at exactly the same moment — deep into a red streak.

---

### 8. Cards (Iowa Gambling Task) — learning from feedback under risk
- **Mechanics:** Four face-down decks in fixed positions. Start with **$2,000**, **80 draws total**. Usually untimed.
- **The structure (from the IGT):** two decks are **advantageous** — **$50-scale gains**, penalties small enough to leave a positive long-run return. Two are **disadvantageous** — **$100-scale gains** with penalties large enough to make them net-losing (classic IGT: roughly **+25 vs. −25 net per draw**). Loss *frequency* varies independently: one good and one bad deck have rare-but-large losses; the others frequent-but-small. **The big-payout, rare-large-loss deck is the trap** — it feels excellent for many draws before it punishes you.
- **THE KEY METRIC:** the headline score is the **percentage of draws from net-positive decks in your FINAL 40 choices.** Also logged: final balance, overall good-deck share, **number of decks explored**, reaction times.
- **This gives you an explicit game plan, because the scoring splits the session in half:**
  - **Early trials: sample every deck ~4–5 times.** Breadth of sampling is itself a measured variable. (Draw count is disputed — sources say anywhere from 30–40 up to 80. If the counter suggests a short game, compress exploration to ~8–12 draws total.)
  - **Then commit.** The widely-repeated allocation heuristic is roughly **50% of remaining draws to your best deck, 40% split across the middling ones, 10% to the worst.** Pure exploitation of a single deck reads as rigid; continued even rotation reads as non-learning. A realistic good finish is **$6,000–7,000**.
  - Track **net, not gross**. A deck paying $100 that hits you for $350 is a losing deck. Rough mental tally per deck is enough — you do not need exact arithmetic, just the sign.
  - Require **repeated evidence** before switching your belief about a deck, and do not abandon a good deck after one bad card.
- **Kills you:** chasing the high-payout deck because the numbers look big — the exact failure mode the task was built to detect. And it is the *normal* failure: across 17 published IGT studies, **13 found the rare-large-loss bad deck chosen as often as or more than the genuinely good decks.** Most healthy adults are avoiding frequent small losses rather than maximising net value. Beating that baseline — actually finding both good decks rather than settling on the comfortable bad one — is precisely the distinguishing behaviour.

---

### 9. Arrows (Eriksen Flanker + task switching) — focus & cognitive flexibility
- **Mechanics:** **~135 trials in ~3 minutes** (~1.3s each). A row of five arrows appears in a colour:
  - **Blue or black → answer the MIDDLE arrow's direction**
  - **Red → answer the OUTER (side) arrows' direction**
  - Answer with Left/Right arrow keys. Rules switch randomly. Trials are **congruent** (all arrows same way) or **incongruent** (middle opposes sides).
- **Metrics:** overall accuracy (the headline percentile), mean RT, **switch-trial accuracy vs. repeat-trial accuracy**, **incongruent accuracy**, and **RT switch cost**.
- **Play:**
  - Collapse it to **two rules, not three colours**: *"blue/black = middle, red = sides."* Drill that phrase until automatic.
  - **On the one apparent conflict:** a couple of sources describe the red rule as "press the *opposite* of the central arrow" rather than "the direction of the side arrows". For a five-arrow array these are **behaviourally identical** — on incongruent trials the sides point opposite the centre, and on congruent trials both rules give the same key. So it does not matter which phrasing you learned. Still read the instruction screen.
  - **The hidden trap: a colour change from blue to black is a REPEAT, not a switch.** Both mean "middle". People who encode *colour* rather than *rule* treat it as a switch and lose the trial. Encode the rule.
  - **Look at the colour first**, then the arrows. Colour determines everything.
  - Silently label "middle" or "sides" before pressing.
  - Deliberately **slow down slightly on switch trials** and let repeat trials run fast. Accuracy is weighted more heavily than raw speed.
  - Keep both index fingers resting on the arrow keys.
  - **Benchmark:** around **124/135 correct** is a strong target; accuracy above ~92% with a congruency cost under ~40ms is the high-performer shape. What is actually measured is whether your switch cost **shrinks** across the run — so absorb the hit on the first switch rather than trying to eliminate it.
- **Kills you:** losing the rule after a switch and then cascading errors for several trials. If you notice you have lost it, take one deliberate beat and reset rather than guessing through.

---

### 10. Lengths — perceptual attention & reward responsiveness
- **Mechanics:** **90 scored trials.** A near-identical cartoon face flashes for about **100 milliseconds**; judge whether the **mouth is short or long** — the difference is roughly **10%**. Left arrow = short, right = long. ~500ms between trials.
- **The hidden mechanic:** one of the two mouth variants is secretly designated **"rich"** and receives a **+$0.20** reward on correct trials **three times as often** as the "lean" variant. You are never told which. Crucially, **an incorrect answer and an unrewarded correct answer look identical** — both show the same blank 500ms screen. So absence of reward tells you nothing about correctness.
- **What it really is — and almost every prep site gets this wrong:** it is Pizzagalli's **Probabilistic Reward Task**, and **it is not an attention-to-detail test.** It measures **response bias** (log b) — whether you implicitly drift toward the more-rewarded variant — alongside discriminability (log d). In the clinical literature, *failure to develop the bias* is the anhedonia signature. Two independent axes are being read: can you see the difference, and does reward move you.
- **Benchmark:** around **87+/90 correct** is a strong target.
- **Metrics:** accuracy (correct ÷ 90), response bias, total earnings.
- **Play:** Lock the mapping in before you start ("left = short, right = long"). Build an **absolute internal midpoint** between the two mouth lengths early and judge every face against *that* — the main source of drift is comparing each mouth to the previous one, so a run of longs makes the next long look short. Fixate the mouth region, not the face. Trust the 100ms impression; the afterimage misleads.
- **On the reward: let it pull you naturally, and do not try to engineer it.** A bias that emerges implicitly is the healthy pattern. A manufactured bias that wrecks your accuracy reads worse than either signal alone.
- **Kills you:** overthinking each face and timing out, or inferring "no reward = I got it wrong" and second-guessing a correct strategy. Silence means nothing. Trust the first read, 90 times.

---

### 11. Towers (Tower of London) — planning
- **Mechanics:** **Five coloured discs** across **three towers** (five slots each). Rearrange to match a target image — **the target stays visible throughout** — in the **fewest moves**. **2-minute limit.** Only the top disc of a tower can move. Interaction is **click source tower, then click destination**. Undo and Reset are available.
- **Not Tower of Hanoi** — there is **no disc-size rule**. A disc just needs to be uncovered and the destination needs a free slot. Do not over-constrain your search.
- **Metrics:** your move count against **the true minimum, computed by breadth-first search**, scored 0–100; **time to first move**; successful forward moves; **undo and reset counts**; invalid attempts. Typical puzzles have a minimum of around **8–10 moves** (9 is the commonly reported figure).
- **⚠️ The move counter is cumulative across Undo and Reset.** You cannot clean up a messy attempt by resetting — it makes your efficiency score strictly worse.
- **This is the one game where hesitating is rewarded.** First-move latency is a separate, explicitly tracked planning signal. A pause says you inspected the target and built a sequence before acting.
- **Play:**
  - **Spend ~15–25 seconds motionless before your first click.** This is scored. Do not skip it even if you think you see the answer.
  - **Work backwards from the target, comparing bottom-up.** The bottom disc must be placed first and moves last, so ask: which disc ends up at the bottom of each tower, and what must clear out of the way?
  - **Nominate one tower as scratch space** for temporary parking. This is the standard trick and it collapses most configurations quickly.
  - Then execute. Re-check every 2–3 moves rather than running blind to the end.
  - **Use Undo immediately for a single misclick** — one prompt undo reads as error monitoring. Ten undos read as confusion, and because the counter is cumulative they cost you twice.
  - **Do not take notes or diagram it.** One prep vendor suggests this; it pushes your first-move latency into outlier territory and eats your 120 seconds.
- **Kills you:** clicking instantly and solving by trial and error. Even if you finish inside 2 minutes, **fast-first-move plus high-move-count is the worst possible planning signature** — it reads as impulsive and unplanned, which is precisely the opposite of what an investment firm's model is looking for.

---

### 12. Faces — emotion recognition & context integration
- **Mechanics:** **~14 trials.** Two types:
  - **Photo only: 7 seconds**
  - **Photo + written situation: 30 seconds**
  - Choose from ten labels: **Anger, Determination, Disgust, Fear, Happiness, Hope, Pain, Sadness, Surprise, Puzzlement.**
- **This is a performance game, not a preference game — there is a keyed correct answer per item.** Do not look for a "socially desirable" response.
- **Metrics:** overall accuracy, **context-trial accuracy**, and — the key feature — **the lift from photo-only to context performance.** The question being asked is whether adding verbal evidence actually improves you. Two failure shapes: good on faces with **no lift** from context (you ignore verbal evidence), or context accuracy *below* photo accuracy (you let the story override a clear face).
- **The ten labels deliberately contain near-neighbour pairs** — fear/surprise, pain/disgust, hope/happiness, determination/anger, puzzlement/surprise. Discriminating between neighbours *is* the measurement, and it is exactly what you can prepare for.
- **Play:**
  - **Read the whole face first** for a global impression, then check eyebrows, eyes and mouth to confirm. Do not fixate on one feature.
  - Eliminate obviously wrong labels, then use the **story to break ties between close pairs** — anger vs. determination, fear vs. surprise, pain vs. sadness, hope vs. happiness.
  - The intended answer must fit **both** face and context. Where they genuinely conflict, find the label plausible for both — though when context is present, most sources advise weighting it.
  - Learn the confusable pairs above in advance — that is most of the available gain.
- **Kills you:** timing out on 7-second trials. Commit to your first strong read.

---

### Seven cross-cutting mistakes that produce bad readings

Worth reading once before you play — several of these are recommended by prep vendors and are actively harmful.

1. **Abandoning games.** More than two missing and you are dropped entirely. One or two missing and you get **median-imputed** — assigned a dead-average value on that construct. Finish everything.
2. **Playing a persona instead of playing.** Balloons, Cards and both Money Exchange games probe risk and trust from different angles. The SVM reads 64 features jointly, so an assembled profile tends to contradict itself.
3. **Chasing extremes.** Features are winsorised to bounds several standard deviations from the mean. **Maximal play on any single metric is clipped and buys you nothing** past the bound.
4. **Confusing "no wrong answers" with "no measurement."** Only the two Money Exchange games are genuinely preference games. **The other ten have real correct answers and real optima.**
5. **Latency blindness.** Time-to-first-move (Towers), decision latency (Easy or Hard), and the speed/accuracy trade-off (Stop, Arrows, Digits) are all separately modelled. Right-but-slow and right-but-fast are **different profiles**, not the same one.
6. **Off-protocol aids.** Pen and paper for Digits, two-handed tapping for Keypresses, note-taking for Towers — each is recommended by at least one prep vendor, and each pushes one feature toward a clipped outlier while distorting the latency features sitting next to it.
7. **Under-weighting the instructions.** With one attempt per ~11 months, getting the *rules* right — especially the Arrows colour rule and the Stop colour mapping, which vendors describe inconsistently — is worth more than any strategy optimisation.

---

## 3. Integrity, detection, and whether gaming it works

You asked directly about cheating measures. Here is the honest picture, separating what is **documented** from what prep vendors **assert**.

### What actually exists

**On the pymetrics games themselves: essentially no proctoring.** No webcam monitoring, no live invigilation, no screen-share detection. This is not a gap in the research — the Northeastern auditors who read the source code treated scripted play as theoretically possible and practically hard, which implies no strong automated defence existed in the code they reviewed.

**Harver launched an anti-fraud and proctoring suite in September 2025** — periodic photo capture for identity verification, copy-paste blocking, and **alerts to recruiters when candidates switch browser tabs, windows, or apps** — plus a fraud-detection layer using application method, **location**, and **whether a candidate submitted multiple applications**. Machine learning flags; a **human makes the final call**; flagged behaviour is logged on a Candidate Detail Page.

**Important caveat:** Harver documents these against its **platform generally**. No public source confirms they apply to the pymetrics game battery. They may; it is not established.

### The controls that are definitely real

| Control | What it does |
|---|---|
| **Outlier clamping** | Values several SDs outside each game's psychometric bounds are **rounded to the min/max — not rejected, not flagged.** An implausibly good result does not trip an alarm; it just silently stops counting. |
| **>2 missing games = incomplete** | Your whole session is dropped from analysis. Finish every game. |
| **The 330-day lock** | The strongest integrity control, and it is **structural, not technological**. There is no replay mechanism to defeat. |
| **Millisecond timing** | Leaving the tab mid-trial corrupts your own reaction latencies whether or not anyone is alerted. |
| **Within-game variance as a measured trait** | Traits like "processing consistency" are computed *from* your variance. Deliberately modulating your behaviour creates exactly the erratic signature you would want to avoid. |

Claims that pymetrics **flags** faked profiles are repeated confidently across prep sites but appear in **no pymetrics, Harver, or peer-reviewed source.** The defensible version is weaker but still decision-relevant: faking produces an **incoherent profile that is less likely to match the benchmark** — not that a fraud alarm sounds.

### So — does faking work?

The best evidence is a 2025 *Journal of Business and Psychology* study (171 participants, honest vs. faking-instructed conditions). Finding: people **could** distort their responses on a game-based assessment, but **the faking effect was significantly smaller than on a traditional questionnaire.** Game-based assessments are fakeable. They are just meaningfully harder to fake.

The useful frame from that literature: faking needs **opportunity, ability and motivation**, and only one needs to fail. For pymetrics:
- **Motivation** — high, obviously.
- **Opportunity** — constrained. Games are millisecond-timed and many features derive from implicit behaviour and variance, not deliberate choices.
- **Ability — this is the binding constraint.** To fake successfully you would need to know (a) which of ~91 traits Blackstone's SVM actually weights, (b) in which direction, and (c) how to produce that value through gameplay. **All three are hidden, and (a) and (b) differ per employer.** Two clients can want opposite profiles from the identical game.

Add to that: the target is **similarity to a profile, not maximisation**; **two games have no correct answer**; and **64 features is far too many to steer simultaneously under time pressure.**

### The honest strategic verdict

On the **10 skill games**, "gaming it" and "playing well" are the same activity. Knowing the rules, having practised the interface, not fumbling the first trials — that is legitimate, it is what every prepared candidate does, and **it is where essentially all of your available gain sits.** Familiarity removes friction; it is not faking.

On the **2 preference games**, there is no target to hit. Be moderate and coherent.

Trying to reverse-engineer Blackstone's centroid from outside is not possible, and over-correcting toward an imagined ideal moves you *away* from a real one. The rational strategy is: **know the mechanics cold, play attentively and consistently, finish every game — and apply broadly**, because the 4.2M-application data says breadth is what defeats systemic rejection, not profile optimisation.

### Finally, some perspective on your past rejections

- The average position **recommends 58.2% of applicants.** Most people clear this gate.
- Candidates on Wall Street Oasis consistently report **identical results passing one firm and failing another** — because every employer's model differs.
- Some firms have dropped pymetrics after internal pushback; **JPMorgan has reportedly retired theirs.** BCG says the games are "never used as a filter to cut candidates on their own."
- pymetrics has **never published its validity studies.** The auditors who reviewed the code explicitly urged them to, noted they did not investigate whether the games predict job performance at all, and listed it as an open question. One GBA study found test-retest reliability around r = 0.68 — meaning a meaningful share of any score is measurement noise.

**A pymetrics rejection is weak evidence about you.** It is substantially evidence about which model you happened to be scored against — and possibly about a stale profile being reused.

## 4. Your plan — it branches

Everything depends on the answer to one question, so resolve that first.

### Step 1 — tonight, 15 minutes: find out if you are even getting a fresh attempt

Open the invite link. It will either offer you the games, or tell you your existing results will be used.

- **If it offers a fresh play → close it immediately. Do not play tonight.** You have 3 days. Go to Track A.
- **If it says results already exist → go to Track B.**

If it is ambiguous, email `support@pymetrics.com` today (you have 3 days, so do not sit on this): ask for **your last completion date** and **whether you are eligible to replay**. Also worth asking whether a session you believe glitched can be invalidated — candidates report mixed success, but it costs one email.

---

### Track A — you have a fresh attempt (3 days)

This attempt sets your profile at every pymetrics employer for the next 11 months. Treat it accordingly.

**Day 1 — learn the rules cold (90 min).** Rules first, drilling second. Confusion on trial one is pure lost signal.
- [ ] Memorise **Arrows**: "blue/black = middle, red = sides."
- [ ] Memorise **Stop**: confirm which colour presses (check on the day — it can be inverted).
- [ ] Internalise the **Cards** plan: explore ~30 draws, then commit — your score is the **final 40**.
- [ ] Internalise the **Balloons** plan: pop one of each colour early, then set per-colour policies. **Do not pre-load a colour mapping.**
- [ ] Internalise the **Easy or Hard** rule: take Hard when `p × reward ≥ $2`.
- [ ] Internalise **Towers**: sit still 15–25 seconds before the first click.
- [ ] Learn the **Faces** confusable pairs: anger/determination, fear/surprise, pain/sadness, hope/happiness.
- [ ] Play through one free simulator run of all 12 games.

**Day 2 — drill the trainable games (90 min).** These are where practice actually moves the number.
- [ ] **Arrows** — flanker drills. Highest-volume game (135 trials), most drillable.
- [ ] **Digits** — chunking practice to a reliable 10–11.
- [ ] **Towers** — Tower of London puzzles, practising *plan-then-execute*.
- [ ] **Stop** — go/no-go drills, specifically practising inhibition after long go-streaks.
- [ ] **Easy or Hard** — check you can actually hit **60 spacebar presses in 12 seconds** (5/sec). If you cannot, every Hard choice is worth less than displayed.
- [ ] **Lengths** — any quick perceptual discrimination drill.

**Day 3 — play.**
- [ ] **Laptop or desktop with a real keyboard.** Not a phone — several games need fast spacebar and arrow input and mobile disadvantages you. **Not a tablet — explicitly unsupported.**
- [ ] Wired ethernet or strong Wi-Fi. Close every other tab and application.
- [ ] Notifications off, phone in another room, door shut. A mid-game interruption on a millisecond-timed task is unrecoverable.
- [ ] Well-rested, at whatever time of day your reaction time is genuinely best. Not after a night out. Not at 1am.
- [ ] One coffee ~30 minutes before. Not three — jitter costs you on Stop and Lengths.
- [ ] Warm up your hands: two minutes of typing.
- [ ] **Read every instruction screen in full.** Several games vary their rules between versions, and the instruction screen is untimed.
- [ ] One sitting, no breaks mid-game.
- [ ] **Finish all 12 games no matter how badly one goes.** More than two missing games and your entire session is discarded. A bad game is survivable; an incomplete session is not.

---

### Track B — your old results are being reused

Accept it for Blackstone. This application will be scored on gameplay you cannot change, and nothing in this guide alters that outcome. That is genuinely not your fault, and it is the most likely explanation for a run of failures that felt inexplicable.

What to do instead:
- [ ] **Find your replay eligibility date** (last completion + 330 days) and put it in your calendar with a reminder two weeks before.
- [ ] **Do the Track A prep in the week before that date**, then replay immediately once eligible. That single replay resets your profile across every pymetrics employer at once — it is the highest-leverage two hours in your entire recruiting cycle.
- [ ] **Keep applying to Blackstone and everyone else in the meantime.** Pymetrics is one input, the recommendation rate averages 58%, and some employers weight it lightly or have dropped it.
- [ ] **Widen your application set now.** The 4.2M-application study is unambiguous: because models are correlated and some are shared across firms, breadth is what defeats systemic rejection. Ten applications leaves ~4% of people rejected everywhere; ~25 drives it below 0.1%. And every applicant in that dataset would have been recommended by *at least one* model. There is no profile that no employer wants — there are only too few draws.

## 5. Practice resources

**Free simulators:**
- gameassessmentprep.com/pymetrics — free practice for all 12 games, per-game guides with the most precise mechanical detail found
- jobtestprep.com/free-pymetrics-games and jobtestprep.co.uk/free-pymetrics-games
- iprep.online/courses/pymetrics-games-test-assessment/ — free practice plus per-game breakdowns

**Paid (worth it only if you have a fresh attempt available):**
- **JobTestPrep PrepPack** (~$59–79) — most complete set of 12 game simulations with feedback; the short plan suits a sub-week timeline
- **iPREP** — simulations plus video explanations
- GraduatesFirst — pairs pymetrics-style practice with HireVue prep, useful since Blackstone's video round follows; note it does not cover the full game set

**YouTube:** iPREP's per-game tutorial series (e.g. "Pymetrics Faces Game — iPREP's Pymetrics Games Tutorials"), JobTestPrep walkthroughs, CareerVidz/Richard McMunn, Practice Aptitude Tests. Search each game by name plus "pymetrics" for real gameplay footage.

**Generic but effective drills:** Human Benchmark (reaction time, number memory), PsyToolkit (flanker, IGT, BART, digit span — these are the *actual academic tasks* the games are built from, and they are free), any Tower of London / Towers of Hanoi app.

**Dedicated Arrows drill:** there is an Android app, *Pymetrics Practice: PyPractice*, built specifically for the Arrows/flanker game. Arrows is the most drillable game in the battery (135 trials, pure speed-accuracy under rule switching), so this is worth the time if you have an Android device.

---

## 6. The things that actually matter

**Before you play:**
1. **Establish whether you are getting a fresh attempt.** If your old profile is being reused, that is the whole story of this application, and your prep belongs on your replay date instead.
2. **Never sit pymetrics casually again.** One play locks your profile across every platform employer for 330 days. If you did that once for a throwaway application, it may have been quietly costing you ever since.

**During the games — the five highest-leverage moves:**
3. **Balloons: deliberately pop one of each colour early.** Best single decision in the battery. Learn the mapping live; do not pre-load one.
4. **Cards: explore all four decks for ~30 draws, then commit hard to the two net-positive ones.** Your score is the good-deck share of the **final 40 draws** — the back half is the part that counts.
5. **Towers: sit still for 15–25 seconds before your first click.** First-move latency is separately scored, and fast-first-move plus high-move-count is the worst planning signature you can produce.
6. **Easy or Hard: decide on expected value, not effort appetite** — Hard when `p × reward ≥ $2`. "EV-aligned choices" is a literal recorded metric.
7. **Stop: after three or four reds in a row, consciously treat the next circle as a fresh decision.** False alarms cluster at the end of go-streaks, and the streak length is logged.

**And two on mindset:**
8. **Finish all twelve games regardless.** More than two missing and the whole session is discarded.
9. **Stop treating this as the thing that is rejecting you.** The average position recommends **58% of applicants**. Blackstone takes roughly 0.2–0.5% overall. The maths says the CV screen, the HireVue and the superday are where your candidacy is actually being decided — and a pymetrics rejection is weak evidence about you, because the same profile passes at one firm and fails at another depending on whose model it meets.

The one genuine strategic lever the data supports is **breadth**. Prepare properly for one clean attempt, then apply widely enough that no single correlated model can shut you out.

## Sources

- https://www.gameassessmentprep.com/pymetrics
- https://www.gameassessmentprep.com/tips/pymetrics-balloons-guide
- https://www.gameassessmentprep.com/tips/pymetrics-arrows-guide
- https://www.gameassessmentprep.com/tips/pymetrics-faces-guide
- https://www.gameassessmentprep.com/tips/pymetrics-money-exchange-1-guide
- https://www.iprep.online/courses/pymetrics-games-test-assessment/
- https://www.jobtestprep.co.uk/free-pymetrics-games
- https://www.jobtestprep.com/pymetrics-games
- https://www.jobtestprep.com/pymetrics-balloon-game
- https://www.jobtestprep.com/pymetrics-digits-game
- https://www.jobtestprep.com/pymetrics-tower-game
- https://www.jobtestprep.com/pymetrics-money-exchange-game-1
- https://www.jobtestprep.com/blog/best-pymetrics-preparation
- https://www.casebasix.com/pages/bcg-pymetrics-test-ultimate-guide
- https://www.hackingthecaseinterview.com/pages/bcg-pymetrics-test
- https://www.preplounge.com/en/blog/consulting/interview/pymetrics-online-games
- https://www.joinleland.com/library/a/blackstone-pymetrics
- https://www.graduatesfirst.com/blackstone-game-assessment
- https://www.jobtestprep.com/blackstone-group-tests
- https://www.careertestprep.com/knowledge/pymetrics-test
- https://prepmatter.com/blog/pymetrics-test
- https://www.wallstreetoasis.com/forum/investment-banking/truth-about-pymetrics
- https://www.wallstreetoasis.com/forum/investment-banking/pymetrics-what-the-fuck
- https://link.springer.com/article/10.3758/s13428-018-1094-8 (BART optimal pumping)
- https://www.impulsivity.org/measurement/bart/
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0006598 (EEfRT)
- https://www.millisecond.com/library/effortexpenditureforrewardtask
- https://journals.sagepub.com/doi/10.1177/2158244019856911 (Iowa Gambling Task review)
- https://www.psytoolkit.org/experiment-library/igt.html

**Primary / peer-reviewed (the authoritative sources on scoring and integrity):**
- Wilson, Ghosh, Jiang, Mislove, Baker, Szary, Trindel, Polli (2021), *Building and Auditing Fair Algorithms: A Case Study in Candidate Screening*, FAccT '21 — the source-code audit — https://mislove.org/publications/Pymetrics-FAccT.pdf
- Bommasani et al. (2026), *Algorithmic Monocultures in Hiring*, FAccT '26 — 4.2M applications — https://arxiv.org/pdf/2605.27371
- *Game on, Faking off? Are Game-Based Assessments Less Susceptible to Faking?*, J. Business and Psychology (2025) — https://www.econstor.eu/bitstream/10419/333366/1/10869_2025_Article_10019.pdf
- *Game-related assessments for personnel selection: A systematic review*, Frontiers in Psychology (2022) — https://pmc.ncbi.nlm.nih.gov/articles/PMC9554090/

**Vendor / regulatory:**
- https://harver.com/gamified-assessments/
- https://harver.com/blog/hiring-integrity-anti-fraud-proctoring-harver/ (anti-fraud suite, Sept 2025)
- https://harver.com/wp-content/uploads/2025/11/pymetrics-Soft-Skills-Platform-2025-Bias-Audit.pdf (BABL AI NYC LL144 bias audit, July 2025)
- https://github.com/pymetrics/audit-ai (pymetrics' open-source fairness testing library)
- https://pymetrics.zendesk.com/hc/en-us/articles/24084100889489-I-ve-previously-completed-the-games-can-I-play-again (official replay policy)
