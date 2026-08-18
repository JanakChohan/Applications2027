# Chapter 4 — The smartPredict Games: switchChallenge, gridChallenge, digitChallenge, motionChallenge

> ### ⚡ The official roster — exactly four games
> Aon's own product page lists precisely four smartPredict games, each mapped to a legacy cut-e instrument: **motionChallenge** ("complex planning capability"), **gridChallenge** ("executive attention"), **switchChallenge** ("logical reasoning — based on scales sx"), **digitChallenge** ("numeracy — based on scales eql"). Each can be used alone or combined with any other Aon test. There is **no fifth game** — claims of extra smartPredict games are prep-site padding. The series is designed **smartphone-first**. `[VENDOR — smartPredict product page]`

**How the games are scored — the shared model.** None of the four shows you a score, and none has a documented points formula. What the evidence supports instead is an **adaptive ladder**: answer correctly and you are promoted to harder, higher-value items; answer wrongly and you are **demoted to easier content, "limiting your score potential."** The de-facto penalty for errors on the games is therefore **demotion, not a stated point deduction** — whether an explicit deduction *also* applies is `[UNKNOWN]` (unlike the scales tests, where negative marking is documented — Chapter 8). Output is a **percentile against a norm group**, and the vendor markets the capture of "**over a thousand behavioural data points**" (reaction time, learning rate, error recovery, effort under pressure) — a marketing figure with no published telemetry specification. `[PREP-VENDOR — JobTestPrep, 12minprep; VENDOR-marketing; UNKNOWN exact algorithms]`

The strategic consequence is identical across all four: **protect early accuracy.** Early errors drop you down the ladder, and "the more questions you get wrong, the harder it is to recover and achieve a good grade." Speed matters only after accuracy is secured.

---

## switchChallenge — deductive "funnel" logic (based on scales sx)

**What it is.** Rows of abstract symbols pass through a "funnel" — an **operator written as a 4-digit number** whose digits specify the new order of the symbol positions (operator 3421 = third symbol first, then fourth, second, first). You choose which operator produces the transformation shown. Difficulty escalates from two rows to three and from single operators to **chained multiple funnels**. **Six minutes standard (a 3-minute variant exists at some employers), unlimited item supply, adaptive.** `[PREP-VENDOR — JobTestPrep, 12minprep, consistent]`

**How it is marked.** The adaptive ladder above: correct → harder/higher-value; wrong → demoted. Percentile output. Exact points per tier `[UNKNOWN]`.

**How to win.** Learn to read a 4-digit operator as a **position map**, not by re-deriving each symbol: "3421" should *feel* like "third-fourth-second-first" the way a word feels like a word. That single automation is most of the score. Then: nail the early items at whatever pace accuracy requires (they set your ladder), and only then accelerate. On chained funnels, apply operators one at a time on the middle row rather than attempting the composition in your head. UK finance note: this game appears in real bank batteries — BNP Paribas's 2026 graduate online test included switchChallenge, which candidates called "always demanding." `[CANDIDATE — TSR thread, snippet-level]` Morgan Stanley also deploys it. `[PREP-VENDOR]`

## gridChallenge — working memory under interference (executive attention)

**What it is.** A complex-span design in a game skin. The loop: memorise a highlighted **dot position** on a grid → answer one or more **interference tasks** (symmetry judgements, rotation checks, shape combinations) → memorise another dot → … → at round end, **recall all dot positions in order**. Memory load runs **3–5 dots per round** with matching interleaved questions. Duration is reported as **9 minutes/~9 rounds** (UK sources) or **6 minutes** (US/P&G sources) — likely employer-variant lengths, treat as 6–9 minutes. Adaptivity is reported both ways; the more detailed source describes real-time adaptation with harder items "worth more points." `[PREP-VENDOR — conflicting on duration/adaptivity; both recorded]`

**How it is marked.** **Both streams score** — the dot recalls *and* the interference answers — on the point-weighted ladder; the weighting between them is `[UNKNOWN]`. This is the single most misunderstood fact about the game: candidates who sacrifice the symmetry questions to rehearse dots are throwing away scored items.

**How to win.** Encode dots verbally/spatially in one beat ("top-right", "centre-left") rather than staring; answer the interference items **fast and honestly** — they are the recoverable stream; keep the dot sequence as a rehearsed chant between interruptions. Expect the 5-dot rounds to feel beyond you — they are normed that way.

**A fairness note you should know.** Aon's own (later-withdrawn) technical documentation, as cited in the ACLU's 2024 FTC complaint, reported **race disparities on gridChallenge** — non-white test-takers scoring lower on average, with the largest gap for Black test-takers. Aon markets the games as bias-reducing; the dispute is unresolved and both positions are recorded in Chapter 9 and the companion guide. `[INDEPENDENT — ACLU citing Aon's technical documentation; VENDOR claims contrary]`

## digitChallenge — mental arithmetic (based on scales eql)

**What it is.** Inverted arithmetic: you see the **answer** and an equation with missing figures; fill in the missing digits (and in some builds, operators) to make it true. **Five minutes, unlimited tasks, adaptive.** `[PREP-VENDOR + VENDOR mapping to scales eql]`

**How it is marked.** Speed + accuracy on the adaptive ladder; demotion on errors; percentile output. `[PREP-VENDOR; exact model UNKNOWN]`

**How to win.** Work backwards from the **units digit**; know times tables cold; use magnitude bounds to reject candidate digits without full computation. As always: early accuracy first, speed second.

## motionChallenge — planning (Rush-Hour-style)

**What it is.** A ball on a grid must reach an exit; obstacles of different sizes block it; movable obstacles slide horizontally/vertically only when the path is clear; some obstacles are immovable. Solve **in as few moves as possible**. **Six minutes, unlimited puzzles, adaptive.** `[PREP-VENDOR consistent]`

**How it is marked.** Both **throughput and move-efficiency** count — a solved puzzle with wasted moves is worth less. Whether **planning latency** before your first move is itself scored is `[UNKNOWN]` — the "behavioural data points" marketing implies telemetry like this exists, but nothing is published. `[PREP-VENDOR + VENDOR-marketing]`

**How to win.** This is the one game where *pausing is strategy*: **plan the complete move sequence before touching anything**, because moves — not seconds — are the scarce currency within each puzzle. Work backwards from the exit: which obstacle must clear the final corridor, and what must move to free it? Committing to a half-plan and improvising is exactly what the efficiency scoring punishes.

---

## Anti-cheat notes (all four games)

The games inherit the platform's strongest protections: **item streams are generated per candidate and the path adapts to your answers**, so no two candidates play the same sequence and leaked "answer keys" are meaningless — the realistic threat model is a proxy player, against which the (optional) webcam proctoring and any later supervised re-test are the controls (Chapter 9). No game-specific telemetry disclosure exists `[UNKNOWN]`, but platform-wide **window-switch logging** is confirmed. The honest-candidate implications: play in one clean sitting on a stable connection, and don't be alarmed by the difficulty ramp — feeling out of your depth by the end is the adaptive design working, and it means climbing, not failing.

## Practice (all four)

Because content is generated and adaptive, **memorising questions is worthless — practice buys mechanic familiarity and speed automation**, which is genuinely valuable (especially operator-reading in switchChallenge and slide-heuristics in motionChallenge). Free: **Aon's own demo video of the series** (the best authentic look at the real UI), AssessmentDay's free gamified samples, GraduatesFirst's guide. Paid: JobTestPrep's smartPredict pack (interactive replicas of all four with unlimited generated items), and its P&G-flavoured grid/switch/digit pack. `[PREP-VENDOR — compared properly in Chapter 10]` One employer-specific data point circulating: JobTestPrep claims under 20% pass P&G's full interactive assessment, with a 12-month reapply cooldown — P&G-specific, unverified, and a reminder that thresholds are employer property, not game property. `[PREP-VENDOR, unverified]`
