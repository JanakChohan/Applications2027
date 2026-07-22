# Aon “scales numerical” practice trainer

A local, offline web app for practising the Aon (formerly cut-e) **scales numerical** assessment —
tabbed data displays, **True / False / Cannot Say**, a countdown, negative marking — plus a coaching
layer that teaches the underlying reasoning. Questions are **procedurally generated** (never a fixed
bank) and **every item is independently verified** so the answer key is provably correct.

> **Preparation only.** This is a practice simulator, not affiliated with Aon, with no live-test
> answer lookup and nothing to help during a real assessment. The Stanine/percentile it shows is a
> clearly-labelled *synthetic* estimate — Aon’s real norms are confidential.

---

## Run it

Requires Node 18+.

```bash
npm install
npm run dev        # opens http://localhost:5173
```

Other commands:

```bash
npm run build      # static bundle in dist/ (open dist/index.html offline)
npm run preview    # serve the built bundle
npm test           # run the vitest suite (generator, verifier, coaching)
npm run audit      # generate 200+ items and self-audit correctness + duplication
```

There is no backend, account, or external API. Progress is saved in your browser’s `localStorage`.

---

## What it replicates (and why)

All format/scoring decisions come from Phase 1 research — see **`research/FINDINGS.md`** (every claim
cited, with confidence ratings and conflicts left open) and **`research/SPEC.md`** (the exact format
contract). Highlights:

- **Six tabbed data displays**, fixed for the whole session, one statement at a time, True/False/Cannot Say.
- **Negative marking:** correct **+1**, wrong **−1**, blank **0** → blind guessing is negative-EV; skip beats guess.
- **Wrong-tab penalty:** answering with the wrong tab showing costs points (toggleable).
- **Norm-referenced result:** synthetic Stanine (1–9) + illustrative percentile; you are *not* expected to finish.
- **Timing:** three real-style modes plus untimed and adaptive.

| Mode | Items | Time | Notes |
|---|---|---|---|
| Full mock | 37 | 12:00 | the real long form (~20s/item) |
| Short mock | 18 | 6:00 | the real short form |
| As remembered | 18 | 12:00 | *non-standard* — your recollection, gentler |
| Untimed drill | 15 | — | learn the reasoning |
| Adaptive drill | 15 | — | serves more of your weakest categories |

Difficulty tiers **medium / intermediate / hard** control how many tabs you must cross-reference,
arithmetic complexity, unit trickiness, and how subtle the Cannot-Say traps are.

---

## How “Cannot Say” stays honest

The generator knows the full ground-truth dataset, so it can’t make a vague statement. A “Cannot Say”
item is only ever built by **withholding a required figure** — a period outside the shown range, an
entity on no tab, or a quantity type that isn’t displayed (the classic *units-vs-revenue* mismatch).
Because a needed datum is provably absent from the six displays, the correct label is provably
Cannot Say. Then an **independent verifier** re-derives every item’s label from scratch (its own
visibility map, its own arithmetic) and the session drops any item whose two labels disagree. A
mislabelled item would teach the wrong reasoning — the worst possible bug — so the answer is computed
twice, by different code, and only agreement is trusted.

---

## Project layout

```
src/
  generators/     dataset + question generation
    rng.js          seedable PRNG (deterministic, testable)
    dataset.js      procedural 6-tab "world" with latent data for Cannot Say
    claim.js        structured statement schema + generator-side evaluator
    items.js        the 9 item-type generators (English rendered FROM the claim)
    session.js      assembles a verified, de-duplicated, label-balanced session
    format.js       value/unit formatting shared across the app
  verify/
    verifier.js     INDEPENDENT ground-truth checker (rejects mislabelled items)
  ui/
    charts.js       hand-rolled SVG bar/grouped/stacked/line/pie + tables
    calculator.js   on-screen calculator
    styles.css      deliberately plain, corporate styling
  coaching/
    scoring.js      negative marking, wrong-tab, Stanine/percentile
    diagnosis.js    classifies WHY each item was wrong (or slow)
    store.js        localStorage progress store
    adaptive.js     weakest-category weighting for adaptive drills
    norms.js        synthetic norm curve (labelled illustrative)
  main.js           screen state-machine tying it all together
tests/            vitest: hand-computed cases + pipeline invariants + coaching
scripts/audit.js  the 200-item self-audit
research/         FINDINGS.md (cited research) + SPEC.md (format contract)
GUIDE.md          the coaching playbook (also viewable in-app)
```

### Adding your own question type

1. Write a generator in `src/generators/items.js` that returns a **claim** (see `claim.js`) and renders
   its English text *from* that claim. Register it in `GENERATORS`.
2. That’s it — `session.js` will verify it automatically, and any mislabelled output is rejected by
   `verify/verifier.js`. Add a hand-computed test in `tests/` and run `npm run audit`.

---

## A suggested 2-week training plan

Grounded in the research (see `research/FINDINGS.md §4`, `GUIDE.md`). ~30–40 min/day. Accuracy first,
speed second — you are *not* meant to finish the real test.

**Week 1 — accuracy & the decision rule (untimed → lightly timed)**

- **Day 1** — Read `GUIDE.md` in the app. Do one **Untimed drill (medium)**. After it, read *every*
  worked solution, even the ones you got right. Goal: internalise True vs False vs **Cannot Say**.
- **Day 2** — Untimed (medium). Focus on the **Cannot Say** rule: if any needed figure is missing, don’t
  compute. Check your “missed Cannot Say” count on the results screen — drive it toward zero.
- **Day 3** — Untimed (intermediate). Traps: **units** (thousands vs millions) and **percent vs
  percentage points**. Do the arithmetic on paper.
- **Day 4** — **Adaptive drill**. It serves your weakest categories. Read the diagnosis on each miss.
- **Day 5** — Untimed (intermediate), then one **Short mock (6:00)** to feel the clock. Don’t chase
  completion — note where accuracy breaks under time.
- **Day 6** — Adaptive drill (intermediate/hard). Target: no “wrong tab” flags — confirm the tab before
  answering, every time.
- **Day 7** — Review the Progress screen. Note your two weakest types and your most common “why wrong”.
  Rest or a light untimed set.

**Week 2 — speed & test simulation (timed)**

- **Day 8** — **Short mock (6:00)**, intermediate. Practise the **skip rule**: abandon anything not cracked
  by ~30s. Blanks are free; wrong answers cost you.
- **Day 9** — Adaptive drill on the week-1 weak spots, then a Short mock. Compare accuracy to Day 8.
- **Day 10** — **Full mock (12:00)**, intermediate. Expect not to finish — aim for high accuracy on what
  you attempt. Review all misses by category.
- **Day 11** — Adaptive drill (hard). Hard tier adds multi-tab combinations and subtler Cannot-Say traps.
- **Day 12** — **Full mock (hard)**. Watch the naive-vs-net score gap on the results screen — closing it
  means fewer careless wrong answers.
- **Day 13** — Two Short mocks back-to-back (intermediate then hard). Keep pace at ~20s/item; leave the
  hard ones blank rather than guessing.
- **Day 14** — One **Full mock** at your target tier as a dress rehearsal. Then read the Progress trend:
  your accuracy line should be rising and your wrong-tab / missed-Cannot-Say counts falling.

Throughout: after every session, spend as long reviewing as you did answering. The review screen — not
the score — is where the improvement comes from.
