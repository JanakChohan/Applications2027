# Aon “scales” practice trainer

A local, offline web app for practising the Aon (formerly cut-e) **scales** assessments — a home
screen picks the test type, then you drill it with a countdown, negative marking, and a coaching layer
that teaches the underlying reasoning. Questions are **procedurally generated** (never a fixed bank)
and **every item is independently verified** by a separate code path, so the answer key is provably
correct.

**Modules**

| Module | Task | Answer |
|---|---|---|
| **scales numerical** | interpret charts/tables across 6 tabs | True / False / Cannot Say |
| **scales verbal** | read short company passages across tabs | True / False / Cannot Say |
| **scales ix** | nine objects, eight share a rule | click the odd one out |
| **scales lst** | shape-sudoku (Latin square), one blank | pick the shape for “?” |
| **scales cls** | six grids colour-sorted by a hidden rule | classify the new grid |

Each module is self-contained (`src/modules/<id>/` with `generate` + `verify` + view) but shares the
timer, negative-marking scoring, progress store, coaching diagnosis, and adaptive drilling.

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
npm test           # run the vitest suite (generators, verifiers, coaching, modules)
npm run audit      # numerical: 200+ items, self-audit correctness + duplication
npm run audit:modules  # verbal/ix/lst/cls: 150+ items each, independent-oracle audit
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

## How the answer key stays provably correct

The same discipline runs in every module: an item is **generated, then re-checked by an independent
verifier written as a separate code path**, and the session drops any item whose two labels disagree.
A mislabelled item would teach the wrong reasoning — the worst possible bug — so the answer is computed
twice and only agreement is trusted.

- **numerical / verbal “Cannot Say”** is only ever built by **withholding a required figure/fact** (a
  period outside the range, an entity/attribute on no tab, a quantity type that isn’t shown). Because the
  needed datum is provably absent, Cannot Say is provably correct — not vague. The verifier rebuilds
  “what’s shown” from the tabs and re-derives the label.
- **ix** injects exactly one rule-breaker; the verifier confirms *exactly one* object violates the rule.
- **lst** is a genuine Latin square; the verifier confirms the “?” is *uniquely* forced.
- **cls** defines the rule first; the verifier recomputes each grid’s group from the rule.

---

## Project layout

```
src/
  modules/          one folder per test type (self-contained, add your own here)
    numerical/        adapts the numerical engine below to the module interface
    verbal/           fact-world → passages; generate / verify / view
    ix/               odd-one-out; generate / verify / view
    lst/              shape-sudoku (Latin square); generate / verify / view
    cls/              grid categorisation; generate / verify / view
    index.js          the module registry
  generators/       numerical engine: rng, dataset world, claim schema, items, session
  verify/verifier.js  numerical INDEPENDENT ground-truth checker
  ui/
    charts.js         hand-rolled SVG charts + tables (numerical)
    shapes.js         SVG shape primitives (ix / lst / cls)
    calculator.js     on-screen calculator (numerical)
    styles.css        deliberately plain, corporate styling
  coaching/
    scoring.js        module-agnostic negative marking, wrong-tab, Stanine/percentile
    diagnosis.js      classifies WHY each item was wrong (per-module reasons)
    store.js          localStorage progress by module / skill / tier / reason
    adaptive.js       weakest-category weighting + focus for adaptive drills
    norms.js          synthetic norm curve (labelled illustrative)
  main.js           the multi-module shell (screen state-machine)
tests/            vitest: hand-computed cases + per-module pipeline invariants
scripts/
  audit.js          numerical 200-item self-audit
  audit-modules.js  verbal/ix/lst/cls audit with independent oracles
  build-artifact.mjs  single-file standalone build
research/         FINDINGS*.md (cited research) + SPEC.md (format contract)
GUIDE.md          the coaching playbook for every module (also viewable in-app)
```

### Adding your own module or question type

- **New item type in an existing module** (e.g. numerical): add a generator that returns a **claim** and
  renders its text *from* that claim, register it, and the session verifies it automatically. Any
  mislabelled output is rejected by the module's verifier.
- **A whole new module** (e.g. `clx`): create `src/modules/<id>/` with `generate.js`, `verify.js` (an
  INDEPENDENT re-derivation of the answer), and an `index.js` exporting the module interface
  (`generate / answerOf / renderReview / diagnose / …`), then add it to `src/modules/index.js`. The shell,
  scoring, progress and adaptive drilling pick it up with no further changes. Add a pipeline test in
  `tests/modules.test.js` and an oracle in `scripts/audit-modules.js`.

---

## A suggested 2-week training plan (all modules)

Grounded in the research (`research/FINDINGS*.md`, `GUIDE.md`). ~30–40 min/day. Accuracy first, speed
second — you are *not* meant to finish any of these tests, and **blind guessing loses points**. Read the
relevant `GUIDE.md` section before drilling a module. If you know which module(s) your employer uses,
weight those days; otherwise this rotation covers all five.

**Week 1 — learn each module's decision rule (untimed → lightly timed)**

- **Day 1 — Numerical.** Read the Guide. Untimed drill. Read *every* worked solution. Goal: True vs False
  vs **Cannot Say**, and the units/percentage-points traps.
- **Day 2 — Verbal.** Untimed. Answer only from the passage — kill the outside-knowledge habit. Watch
  absolute words ("all/always/only"). Drive your "used outside knowledge" and "missed Cannot Say" counts down.
- **Day 3 — ix (odd-one-out).** Untimed. Practise scanning *every* attribute (shape, sides, fill, rotation,
  inner shape) before choosing. Read the rule the review names on each miss.
- **Day 4 — lst (shape-sudoku).** Untimed. Solve each "?" from **both** its row and column; use pre-fill on
  5×5 grids. Then **cls**: untimed, state the rule as one testable property before classifying.
- **Day 5 — Numerical + Verbal**, one short timed mock each. Feel the ~15–20s/item pace; note where accuracy
  breaks under the clock.
- **Day 6 — Adaptive drills** on your two weakest modules (the Progress screen shows them). Read the diagnosis
  on every miss.
- **Day 7 — Review.** Open Progress; note your weakest *skill* within each module and your most common
  "why wrong". Light untimed set or rest.

**Week 2 — speed & simulation (timed) + weakness targeting**

- **Day 8 — Numerical full mock (12:00).** Practise the **skip rule**: abandon anything not cracked by ~1.5×
  the per-item budget; blanks are free, wrong answers cost you.
- **Day 9 — Verbal full mock**, then an adaptive verbal drill on your weak trap (synonym / contradiction /
  Cannot Say). Confirm the right tab before every answer.
- **Day 10 — ix + lst timed sets** at intermediate/advanced. Keep pace; leave the ones you can't crack blank.
- **Day 11 — cls timed set** + adaptive drill on your weakest rule type. Count carefully.
- **Day 12 — Your target module(s) at the hardest tier.** Watch the naive-vs-net score gap on the results
  screen shrink — that gap is careless wrong answers.
- **Day 13 — Mixed simulation:** one timed set from each module your employer uses, back to back, to build
  context-switching stamina.
- **Day 14 — Dress rehearsal** at your target tier across your modules. Then read the Progress trend: your
  accuracy lines should be rising and your wrong-tab / missed-Cannot-Say / wrong-rule counts falling.

Throughout: after every session, spend as long reviewing as you did answering. The review screen — not the
score — is where the improvement comes from. And remember the integrity note: the real test re-verifies you
under supervision, so the trained skill is the only thing that transfers.
