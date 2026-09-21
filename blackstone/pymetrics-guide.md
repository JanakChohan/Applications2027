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

There is **no pass mark and no single score**. The pipeline:

1. Blackstone has ~50+ current high performers in the target role play the games.
2. pymetrics averages their trait vectors → this becomes the **role model** ("ideal" profile).
3. Your gameplay produces a vector across **~91 traits in 9 dimensions**.
4. You are scored on **distance from that model**, then bias-tested (pymetrics de-biases against the EEOC four-fifths rule, and open-sourced its `audit-AI` tooling).
5. Output to the recruiter is usually a **match/recommendation tier**, not a number.

### The 9 trait dimensions
| Dimension | What it captures |
|---|---|
| Attention | Systematic/sustained vs. fast/loose |
| Decision Making | Gut instinct vs. deliberate analysis |
| Effort | How you allocate effort against reward and probability |
| Emotion | Reading faces vs. reading context |
| Fairness | How you judge fair/unfair outcomes |
| Focus | Handling distraction, rule-switching, multitasking |
| Generosity | Self-interest vs. resource sharing |
| Learning | Updating from feedback and outcomes |
| Risk Tolerance | Conservative vs. risk-seeking, and how calibrated |

### Three consequences that most candidates miss
- **Extremes are usually penalised.** Distance-from-centroid scoring means being maximally risk-seeking is as far from a balanced model as being maximally risk-averse. "Max out every game" is the wrong instinct.
- **The 10 skill games do have better and worse play.** Attention, memory, learning and planning games have real performance metrics. Practice genuinely lifts these (one platform reports a **median +16% improvement between first and fifth practice attempt**).
- **The 2 Money Exchange games genuinely have no right answer** — they are preference measures. Trying to fake them is where inconsistency shows up.

### What Blackstone specifically appears to weight
Prep-vendor analysis and Blackstone's own stated competencies point to: **calibrated (not reckless) risk tolerance, decision quality under uncertainty, sustained attention and focus, and fast learning from feedback.** Reported divisional variation: Real Estate leans long-horizon planning; PE leans adaptability. Selectivity context: reported ~0.2–0.5% acceptance, ~57,000 applications for ~138 entry-level seats — pymetrics is a **volume triage gate** sitting after CV screen and before HireVue.

---

## 2. Game-by-game breakdown

Each entry: **mechanics → metric extracted → what good looks like → how to play → what kills you.**

---

### 1. Keypresses — motor speed & instruction-following
- **Mechanics:** ~20 seconds. Press spacebar as fast as possible after "GO". Stop on cue. ~40 reps.
- **Metrics:** tap rate, latency after GO, **presses after the stop cue**.
- **Good:** high consistent rate, clean stop.
- **Play:** Use index+middle finger alternating on the spacebar. Start the instant GO appears. **Stop dead** when told.
- **Kills you:** pressing before GO or continuing after stop. That is logged as impulse-control failure, not enthusiasm. This game is nearly free marks — do not lose them on sloppiness.

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
- **Mechanics:** Two independent rounds. Both start with ~$5; one player gets a bonus $5. Round 1: choose how much to **give** ($0–$5). Round 2: you can **give or take**. Fairness rating after each.
- **Metrics:** giving amount, whether you **take**, and consistency between the give-frame and take-frame (framing sensitivity).
- **Play:** **Split to equality** — sending $2.50 leaves both on $7.50. Moderate-to-high generosity is the safer read; taking aggressively flags as a potential conflict source.
- **Kills you:** being generous in round 1 and exploitative in round 2. That inconsistency across framings is precisely the signal the game is designed to catch.

---

### 5. Digits (Digit Span) — working memory
- **Mechanics:** Starts at about **4 digits**, shown roughly **~900ms per digit**. Type them back in order. Correct → next sequence is **one digit longer**; incorrect → **one shorter**. It is a ±1 staircase that hunts your limit. **Ends after 3 *consecutive* errors — and a single correct answer resets the counter.**
- **Metrics:** **max span**, correct-round count, **best streak**, submission latency, and error *type* (transpositions = you held the digits but lost the order; omissions = span exceeded).
- **Because errors must be consecutive, one mistake is survivable.** Do not spiral after a miss — the next correct answer wipes the counter clean. Most people fail this game emotionally, not cognitively.
- **Benchmarks:** average max is **8–9 digits**. **~11 digits ≈ top 20%.** Aim **10–12**. Note: **14–15 looks implausible and may flag manipulation** (i.e. writing it down).
- **Play:**
  - **Chunk** in 3s and 4s: `729481635` → "729 · 481 · 635".
  - **Subvocalise / say them aloud** — the phonological loop is the actual bottleneck.
  - Convert chunks to familiar numbers (years, ages, phone prefixes).
  - Type immediately; do not rehearse silently while the clock runs.
- **Kills you:** writing digits down. It is explicitly prohibited, and an unnatural span is the one metric in this battery with an obvious implausibility ceiling.

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

## 3. Integrity, detection, and what actually happens if you try to game it

You asked directly about cheating measures. Straight answer:

**There is no webcam proctoring and no live invigilation.** That is not the constraint. The constraints are statistical:

| Control | What it catches |
|---|---|
| **Internal consistency checks** | Preference games measure the same constructs from different angles (give-frame vs. take-frame; trust amount vs. fairness rating). Contradictory patterns are detectable and are explicitly flagged as such by the vendor. |
| **Implausibility ceilings** | A 14–15 digit span, superhuman reaction times, or perfect accuracy at maximum speed are outside human distributions. |
| **Reaction-time floors** | Sub-human RTs indicate scripting or anticipation rather than response. |
| **Timing from trial one** | Reaction-time games are scored **from the first trial**. Learning the controls during the live run costs you real signal — this is the argument for practising, not for cheating. |
| **Cross-game coherence** | Your 91-trait vector has to hang together. A profile assembled from per-game "optimal" answers can land as an internally incoherent outlier, which is *further* from the centroid, not closer. |
| **Downstream mismatch** | Blackstone's HireVue and superday come next. A profile you faked is a profile you then have to perform in a live interview. Vendors and coaches consistently flag this as where fakers fall over. |

**The honest strategic verdict:** on the **10 skill games**, "gaming" and "playing well" are the same thing — practice, know the rules, execute cleanly. That is fully legitimate and it is where your gains are. On the **2 preference games**, there is no target to hit, faking is the detectable part, and a moderate consistent position is both the safest and the truest play. Attempting to reverse-engineer Blackstone's exact centroid is not possible from outside — the models are proprietary and role-specific — and over-correcting toward an imagined ideal is how people land further from it.

**Also note:** senior bankers at some firms have pushed back on pymetrics and a few have dropped it (JPMorgan has reportedly retired theirs). Candidates on Wall Street Oasis report identical results passing one firm and failing another — because each firm's model differs. **A past rejection is not evidence that you are bad at this.** It may mean one firm's centroid, or a stale reused profile.

---

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
