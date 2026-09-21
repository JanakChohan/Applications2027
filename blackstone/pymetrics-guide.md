# Blackstone pymetrics — Complete Breakdown & Playbook

**Context:** Blackstone campus programme, invite from `Blackstone@pymetrics.com`, 3-day completion window, ~25–30 min battery.
**Provider:** pymetrics, acquired by **Harver** in 2022. Same engine, Harver branding creeping in.

---

## 0. READ THIS FIRST — the thing that probably explains your repeated failures

Two mechanics matter more than any game strategy:

### (a) The 330-day lockout
pymetrics normally lets you **replay the real battery only once every ~330 days** (many candidates report it as 365). Within that window, an employer **re-scores your existing gameplay** rather than letting you replay.

Your invite says this explicitly:

> "If you have already played pymetrics using this email address, you must still click the link above for your results to be submitted for this specific application (**you will not need to replay**)."

**What this means for you:** if you played pymetrics within the last ~11 months on `janak.chohan26@gmail.com`, then clicking Blackstone's link **submits your old gameplay**. No amount of prep changes this application's outcome. You are not failing a fresh test — you may be re-submitting the same profile to firm after firm, which is exactly the pattern of "I always fail it."

**Do this before anything else:**
1. Open the link. See whether it offers you the games or says your existing results will be used.
2. If it says results already exist → email `support@pymetrics.com` **immediately** (you have 3 days), state that you want to know your last play date and whether you are eligible for a fresh attempt.
3. If you are locked out, accept it for Blackstone, and put the prep below against the date you *become* eligible. Mark that date in your calendar now.

### (b) Your result is portable
One profile is reused across every pymetrics client (historically Bain, BCG, JPMorgan, Morgan Stanley, Citi, Blackstone). This cuts both ways: one good play helps everywhere; one bad play follows you for ~11 months. **Treat the next fresh attempt as a once-a-year event, not a casual afternoon.**

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

Prep-vendor analysis and Blackstone's stated competencies point to **calibrated (not reckless) risk tolerance, decision quality under uncertainty, sustained attention and focus, and fast learning from feedback.** Reported divisional variation: Real Estate leans long-horizon planning, PE leans adaptability. pymetrics sits after CV screen and before HireVue as **volume triage** — reported context is ~57,000 applications for ~138 entry-level seats.

### The finding that should change your application strategy

The 2026 monoculture study found something important:

- Of applicants who apply to ten pymetrics-mediated positions, **4% are rejected from all ten** — and rejections are **correlated across employers** far more than chance would predict, because **42 pymetrics models are shared across multiple companies**. A rejection under a shared model mechanically propagates.
- But the same study ran the counterfactual: if every applicant were scored by *every* pymetrics model, **every single applicant would be recommended by at least one.** There is no such thing as a universally unemployable profile.
- To get systemic rejection below 0.1%, applicants need roughly **25 applications** rather than 10.

**Translation: if pymetrics keeps blocking you, the highest-return response is breadth, not profile optimisation.** Your profile is not bad; it is being repeatedly matched against a narrow, correlated set of models. Widen the net.

## 2. Game-by-game breakdown

Each entry: **mechanics → metric extracted → what good looks like → how to play → what kills you.**

---

### 1. Keypresses — motor speed & instruction-following
- **Mechanics:** A brief READY period, then **GO** — press the spacebar as fast as you can until the **STOP** cue. Reported durations vary (roughly 10–60 seconds; practice versions use ~15s). **The live tap counter is deliberately hidden** so you cannot pace yourself against it.
- **Metrics:** total valid taps, **taps per second**, individual tap timestamps (so rhythm and consistency are visible), and **instruction-following — any press before GO or after STOP**.
- **Good:** a high, *even* rate and a clean stop.
- **Play:**
  - Use your **dominant index finger**, compact even motion, and **let the key fully reset between taps** — mashing a partly-depressed key registers fewer presses than it feels like.
  - **Establish your rhythm immediately** rather than starting slow and accelerating.
  - **Watch the cue, not your hand.**
  - Start from a neutral finger position — do not rest pressure on the key in anticipation.
  - On STOP, **lift your finger clear of the key** as a deliberate act.
- **Kills you:** pressing before GO or continuing after STOP. Both are logged, and neither reads as enthusiasm — they read as poor impulse control and poor instruction-following. This game is close to free marks; the only way to lose them is sloppiness at the edges.

---

### 2. Balloons (BART — Balloon Analogue Risk Task) — risk calibration & learning
- **Mechanics:** ~39 balloons, recurring in **three colours**. Each pump = **$0.05**. Pop = lose that balloon's pot. "Collect" banks it.
- **The colour secret:** the colours have different burst distributions — commonly cited approximate first-pump pop odds: **orange ≈ 1/8 (bursts early), yellow ≈ 1/32 (medium), blue ≈ 1/128 (safe, goes long)**. Pop point is drawn per balloon; conditional risk rises with each safe pump.
- **Metrics:** total banked; **adjusted average pumps** (collected balloons only — the standard BART risk index); number popped; **per-colour differentiation**; pumping behaviour immediately after a pop (loss sensitivity).
- **Good:** In the academic 1–128 version, the expected-value optimum is **~64 pumps**; typical humans pump ~28 (44% of optimal) — i.e. **most people are far too conservative.** Practical benchmarks cited for the pymetrics version: collect **~30–31 balloons** and around **$17–18**.
- **Play:**
  - **Deliberately pop one of each colour early** (balloons 1–3). The information is worth more than the ~$1 you lose. This is the single highest-ROI move in the whole battery.
  - Then set a **per-colour pump policy** and hold it: high for blue, moderate for yellow, low for orange.
  - Sit a couple of pumps below the lowest pop you have seen for that colour, and creep up if you keep banking safely.
  - **Do not tilt after a pop.** Reverting to tiny pump counts after a burst reads as loss-aversion/poor emotional regulation; pump-count variance after losses is explicitly measured.
- **Kills you:** treating all balloons identically (reads as failure to learn), and banking at 5 pumps every time (reads as extreme risk aversion — and it is also just bad play).

---

### 3. Money Exchange #1 (Trust Game) — trust & reciprocity *(preference game)*
- **Mechanics:** **One round.** You hold **$10**, the partner holds $0. Send **$0–$10 in $1 increments**; it **triples** in transit. The (algorithmic) partner then returns a portion — reported default is a **seeded-random 30–70% of the tripled amount**. You then rate the exchange's fairness **0–10**.
- **Metrics logged:** amount sent, tripled amount, partner return, both final balances, your fairness rating, **reaction times**, timestamped events. **No score is assigned** — money retained is explicitly not a test score.
- **A quietly important bit of maths:** if the partner returns 30–70% of 3×, you get back **0.9× to 2.1×** what you sent, expected ≈ **1.5×**. Sending *more* is therefore expected-value-positive. So "send little" is not the safe play it feels like — it is simply a low-trust reading, and it also leaves money on the table.
- **What is measured, honestly:** there is no correct amount. $0 = zero trust. $10 = maximum trust. Guides converge on a moderate-to-substantial send — **$5 (half) is the most commonly recommended anchor**, with $3–$5 the cautious band.
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
- **Metrics:** **max span**, correct-round count, **best streak**, submission latency, and error *type* (transpositions = you held the digits but lost the order; omissions = span exceeded).
- **Because errors must be consecutive, one mistake is survivable.** Do not spiral after a miss — the next correct answer wipes the counter clean. Most people fail this game emotionally, not cognitively.
- **Benchmarks:** average max is **8–9 digits**. **~11 digits ≈ top 20%.** Aim **10–12**. (Some prep sites warn that 14–15 "flags manipulation" — on the documented pipeline it would more likely just be **clamped to the top of the range**, so it would not help you either. Either way there is no upside in writing digits down, and it is explicitly prohibited.)
- **Play:**
  - **Chunk** in 3s and 4s: `729481635` → "729 · 481 · 635".
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
- **Safe universal heuristic if you are unsure which mode you are in:** **take Hard when `p × reward ≥ $2`, otherwise Easy.** That is EV-positive under fixed rounds and roughly correct under the timed cap.
- **Quick mental shortcuts:** 88% ≈ "nearly all of it", 50% ≈ "half of it", 25% ≈ "a quarter of it". You do not need precision — you need the right side of $1–2.
- **Play:** Show *discriminating* effort. The trait is not "works hard", it is "spends effort where the numbers justify it". Decide fast — decision latency is logged, and in timed mode dithering costs you rounds.
- **Kills you:** always choosing Hard (indiscriminate, and in timed mode it tanks your earnings), always choosing Easy (low drive), letting the 5-second window lapse (logged as automatic), and worst of all **choosing Hard and failing to land 60 presses in 12 seconds**. That is 5 presses/second — practise it. If you cannot reliably hit it, your EV on every hard choice is lower than displayed.

---

### 7. Stop (Stop-Signal / Go-No-Go) — impulse control
- **Mechanics:** roughly **80 circles over ~2 minutes**, arriving at about **one per second**. Default rule: **red = press spacebar, green = withhold.** At least one source reports the reverse mapping, so **read the instruction screen** — do not assume.
- **Metrics:** hits, **misses** (failed to press on red), **correct inhibitions**, **false alarms** (pressed on green — the headline impulsivity measure), reaction time on correct presses, and — tellingly — **the length of the preceding "go" streak before each response**.
- **The trap, and it is a designed one:** reds heavily outnumber greens, so you build a pressing habit. **False alarms cluster immediately after long runs of red.** pymetrics logs the go-streak length precisely because it wants to see whether your inhibition survives momentum.
- **Play:** Rest your finger *near* the spacebar, not on it. **After three or four reds in a row, consciously flag the next circle as a fresh decision** rather than another press. Accuracy dominates speed here — a slightly slow correct response beats a fast false alarm every time.
- **Kills you:** autopilot. Pressing on green is the single loudest impulsivity signal in the battery, and it happens to almost everyone at exactly the same moment — deep into a red streak.

---

### 8. Cards (Iowa Gambling Task) — learning from feedback under risk
- **Mechanics:** Four face-down decks in fixed positions. Start with **$2,000**, **80 draws total**. Usually untimed.
- **The structure (from the IGT):** two decks are **advantageous** — **$50-scale gains**, penalties small enough to leave a positive long-run return. Two are **disadvantageous** — **$100-scale gains** with penalties large enough to make them net-losing (classic IGT: roughly **+25 vs. −25 net per draw**). Loss *frequency* varies independently: one good and one bad deck have rare-but-large losses; the others frequent-but-small. **The big-payout, rare-large-loss deck is the trap** — it feels excellent for many draws before it punishes you.
- **THE KEY METRIC:** the headline score is the **percentage of draws from net-positive decks in your FINAL 40 choices.** Also logged: final balance, overall good-deck share, **number of decks explored**, reaction times.
- **This gives you an explicit game plan, because the scoring splits the session in half:**
  - **Draws 1–~30: explore all four decks** roughly evenly. Breadth of sampling is itself a measured variable, and you cannot identify the good decks without it. Early losses here cost you nothing that matters.
  - **Draws ~40–80: commit almost entirely to the two net-positive decks.** This is the scored window. The cleaner your commitment here, the higher your percentile.
  - Track **net, not gross**. A deck paying $100 that hits you for $350 is a losing deck. Rough mental tally per deck is enough — you do not need exact arithmetic, just the sign.
  - Require **repeated evidence** before switching your belief about a deck, and do not abandon a good deck after one bad card.
- **Kills you:** chasing the high-payout deck because the numbers look big. That is the exact failure mode the task was built to detect.

---

### 9. Arrows (Eriksen Flanker + task switching) — focus & cognitive flexibility
- **Mechanics:** **~135 trials in ~3 minutes** (~1.3s each). A row of five arrows appears in a colour:
  - **Blue or black → answer the MIDDLE arrow's direction**
  - **Red → answer the OUTER (side) arrows' direction**
  - Answer with Left/Right arrow keys. Rules switch randomly. Trials are **congruent** (all arrows same way) or **incongruent** (middle opposes sides).
- **Metrics:** overall accuracy (the headline percentile), mean RT, **switch-trial accuracy vs. repeat-trial accuracy**, **incongruent accuracy**, and **RT switch cost**.
- **Play:**
  - Collapse it to **two rules, not three colours**: *"blue/black = middle, red = sides."* Drill that phrase until automatic.
  - **Look at the colour first**, then the arrows. Colour determines everything.
  - Silently label "middle" or "sides" before pressing.
  - Deliberately **slow down slightly on switch trials** and let repeat trials run fast. Accuracy is weighted more heavily than raw speed.
  - Keep both index fingers resting on the arrow keys.
- **Kills you:** losing the rule after a switch and then cascading errors for several trials. If you notice you have lost it, take one deliberate beat and reset rather than guessing through.

---

### 10. Lengths — perceptual attention & reward responsiveness
- **Mechanics:** **90 scored trials.** A near-identical cartoon face flashes for about **100 milliseconds**; judge whether the **mouth is short or long** — the difference is roughly **10%**. Left arrow = short, right = long. ~500ms between trials.
- **The hidden mechanic:** one of the two mouth variants is secretly designated **"rich"** and receives a **+$0.20** reward on correct trials **three times as often** as the "lean" variant. You are never told which. Crucially, **an incorrect answer and an unrewarded correct answer look identical** — both show the same blank 500ms screen. So absence of reward tells you nothing about correctness.
- **What it really is:** a **probabilistic reward task**. It measures **response bias** (reported as a log-b style statistic) — whether you unconsciously drift toward the more-rewarded variant — alongside raw perceptual accuracy and earnings.
- **Metrics:** accuracy (correct ÷ 90), response bias, total earnings.
- **Play:** Lock the mapping in before you start ("left = short, right = long"). Look **only at the mouth**, using one fixed internal reference for what counts as short vs. long. Answer from the immediate impression — do not try to reconstruct the image after it disappears. **Let reward pull you naturally; do not try to deduce or force the rich variant.** Bias is recorded as a neutral trait observation, not as a failure — but accuracy is scored, and chasing the reward wrecks it.
- **Kills you:** overthinking each face and timing out, or inferring "no reward = I got it wrong" and second-guessing a correct strategy. Silence means nothing. Trust the first read, 90 times.

---

### 11. Towers (Tower of London) — planning
- **Mechanics:** **Five coloured discs** across **three towers** (five slots each). Rearrange to match a target image — **the target stays visible throughout** — in the **fewest moves**. **2-minute limit.** Only the top disc of a tower can move. Interaction is **click source tower, then click destination**. Undo and Reset are available.
- **Metrics:** your move count against **the true minimum, computed by breadth-first search**, scored 0–100; **time to first move**; successful forward moves; **undo and reset counts**; invalid attempts.
- **This is the one game where hesitating is rewarded.** First-move latency is a separate, explicitly tracked planning signal. A pause says you inspected the target and built a sequence before acting.
- **Play:**
  - **Spend ~15–25 seconds motionless before your first click.** This is scored. Do not skip it even if you think you see the answer.
  - **Work backwards from the target, comparing bottom-up.** The bottom disc must be placed first and moves last, so ask: which disc ends up at the bottom of each tower, and what must clear out of the way?
  - **Nominate one tower as scratch space** for temporary parking. This is the standard trick and it collapses most configurations quickly.
  - Then execute. Re-check every 2–3 moves rather than running blind to the end.
  - **Use Undo immediately for a single misclick** — one undo is cheaper than the extra moves needed to fix it. Save Reset for when the structure is genuinely unrecoverable.
- **Kills you:** clicking instantly and solving by trial and error. Even if you finish inside 2 minutes, **fast-first-move plus high-move-count is the worst possible planning signature** — it reads as impulsive and unplanned, which is precisely the opposite of what an investment firm's model is looking for.

---

### 12. Faces — emotion recognition & context integration
- **Mechanics:** **~14 trials.** Two types:
  - **Photo only: 7 seconds**
  - **Photo + written situation: 30 seconds**
  - Choose from ten labels: **Anger, Determination, Disgust, Fear, Happiness, Hope, Pain, Sadness, Surprise, Puzzlement.**
- **Metrics:** overall accuracy, **context-trial accuracy**, and **the gap between photo-only and context performance** — i.e. do you read faces, read situations, or integrate both?
- **Play:**
  - **Read the whole face first** for a global impression, then check eyebrows, eyes and mouth to confirm. Do not fixate on one feature.
  - Eliminate obviously wrong labels, then use the **story to break ties between close pairs** — anger vs. determination, fear vs. surprise, pain vs. sadness, hope vs. happiness.
  - The intended answer must fit **both** face and context. Where they conflict, find the label that is plausible for both rather than siding with one.
  - Learn the confusable pairs above in advance — that is most of the available gain.
- **Kills you:** timing out on 7-second trials. Commit to your first strong read.

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

## 4. Your 3-day plan

### Day 0 — tonight (30 min, do this first)
- [ ] Open the invite link. Determine: fresh play available, or existing results being reused?
- [ ] If results are being reused → email `support@pymetrics.com` now, ask for last play date and replay eligibility.
- [ ] If fresh play available → **do not play yet.** Close it. You have 3 days.

### Day 1 — learn the rules cold (90 min)
- [ ] Memorise per-game rules, especially **Arrows** ("blue/black = middle, red = sides") and **Stop** (which colour presses).
- [ ] Internalise the **Cards** deck structure and the **Balloons** colour strategy.
- [ ] Learn the **Faces** confusable pairs.
- [ ] Do free practice sims (see resources below).

### Day 2 — drill the trainable games (90 min)
These respond to practice most: **Digits, Arrows, Towers, Stop, Lengths.**
- [ ] Digit span: practise chunking to a reliable 10–11.
- [ ] Flanker/task-switching drills for Arrows.
- [ ] Tower of London puzzles — practise *planning before moving*.
- [ ] Reaction-time/go-no-go drills.
- [ ] Rehearse the Easy-or-Hard EV rule until it is automatic.

### Day 3 — play
- [ ] **Laptop/desktop with a real keyboard.** Not phone (several games need fast spacebar/arrow input; mobile disadvantages you). Not tablet — explicitly unsupported.
- [ ] Wired or strong Wi-Fi. Close every other tab and app. Notifications off, phone away.
- [ ] Well-rested, mid-morning or whenever your reaction time is best. Not after a night out, not at 1am.
- [ ] One coffee about 30 minutes before — helps RT games. Not three.
- [ ] Warm up your hands: 2 minutes of typing before you start.
- [ ] **Read every instruction screen fully.** Several games invert their rules between versions.
- [ ] One sitting, no breaks mid-game.

---

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

**Generic but effective drills:** Human Benchmark (reaction time, number memory), PsyToolkit (flanker, IGT, BART, digit span — the actual academic tasks), any Tower of London / Towers of Hanoi app.

---

## 6. The five things that matter most

1. **Find out whether you are even getting a fresh attempt.** If your old profile is being reused, that is the whole story, and prep belongs on your next eligibility date.
2. **Balloons: pop one of each colour early on purpose.** Highest-value single decision in the battery.
3. **Towers: sit still for 20–30 seconds before your first move.** Latency is scored.
4. **Cards: explore all four decks for the first ~30 draws, then commit hard to the two net-positive decks.** Your score is the share of good-deck draws in the **final 40**, so the back half is the only part that counts.
5. **Easy or Hard: choose on expected value per second, not on effort appetite.** Discrimination is the trait.

And the meta-point: on the skill games, prepare hard — that is legitimate and it is where the movement is. On the two preference games, be consistent and moderate, because inconsistency is the one thing the system reliably catches.

---

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
