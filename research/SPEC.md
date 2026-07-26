# SPEC — Format the practice app must replicate

Derived from `FINDINGS.md`. This is the *authentic-format* contract for the build. Where the real test is uncertain, the choice is stated with its rationale. Target test: **Aon scales numerical** (True/False/Cannot Say over ~6 tabbed data displays).

---

## 1. Screen layout (one question at a time)

```
┌────────────────────────────────────────────────────────────┐
│  cut-e-style header    [ Question 7 / 37 ]        ⏱ 08:42   │  ← whole-test countdown
├────────────────────────────────────────────────────────────┤
│ [ Income ][ Costs ][ Market Share ][ Employees ][ ROE ][ Outlook ]  │ ← ~6 TABS
│ ┌──────────────────────────────────────────────────────┐   │
│ │                                                      │   │
│ │        ACTIVE TAB: chart or table (SVG)              │   │  ← the data display
│ │        footnote: "All figures in $ thousand"         │   │
│ └──────────────────────────────────────────────────────┘   │
├────────────────────────────────────────────────────────────┤
│  Statement:  "Research costs in FY8 exceeded $7 million."   │  ← ONE statement
│                                                            │
│     [  True  ]   [  False  ]   [  Cannot Say  ]            │  ← 3 answer buttons
├────────────────────────────────────────────────────────────┤
│  ◀ Prev            [ Skip ]            Next ▶      [ ☐ calc ]│  ← nav + calculator
└────────────────────────────────────────────────────────────┘
```

**Non-negotiable format fidelity (must match the real test):**
- **~6 tabbed data displays** across the top; clicking a tab swaps the display; **data does not change during the test**; **each statement relates to the data, and the required figure lives on one or more specific tabs**.
- **One statement visible at a time**, sharing the tabbed dataset.
- **Exactly three answer buttons: True / False / Cannot Say.**
- **Single whole-test countdown timer** (not per-question). At 0:00 the test auto-submits.
- **Boring, legible, corporate styling** — plain sans-serif, muted palette, thin gridlines. Deliberately *not* a pretty redesign.

---

## 2. Timing model

| Mode | Items | Time | Pace | Notes |
|---|---|---|---|---|
| **Full (authentic default)** | 37 | 12:00 | ~19 s/item | The real long form |
| **Short (authentic)** | 18 | 6:00 | ~20 s/item | The real short form |
| **"As remembered"** | 18 | 12:00 | ~40 s/item | Your recollection — labelled *non-standard, gentler* |
| **Untimed drill** | configurable (default 15) | none | — | Coaching/learning mode |

- Countdown is the whole-test clock. A per-question *stopwatch* runs invisibly to record **time-per-item** for coaching (this is measured, not enforced — matches the real whole-test clock).
- ~4 min of real-test instructions/practice are **not** simulated in timed score (optional warm-up screen only).

## 3. Answer & navigation behaviour

- **Back-navigation ON by default** (weight of evidence: AssessmentDay + GraduatesFirst confirm you can revisit/change answers; this also proves the test is *not* item-adaptive). Provided as a **toggle** so the user can simulate a stricter no-back variant.
- **Skip** leaves an item **blank** (distinct from an answered state) and is reversible via back-nav.
- Selecting an answer highlights it; it can be changed while the clock runs.
- An item is one of: `unanswered/blank`, or answered `True|False|Cannot Say`.

## 4. Scoring model (simulate faithfully, and teach it)

```
raw   = (#correct × +1) + (#wrong × −1) + (#blank × 0)      // negative marking
```
- **Wrong answers are penalised (−1). Blanks are 0. Blind guessing is negative-EV.** The results screen shows correct/wrong/blank counts and the raw penalised score, and explicitly contrasts it with a naive "just count correct" score so the penalty is visceral.
- **Norm-referenced presentation:** since there is no public pass mark, the app reports a **Stanine (1–9)** and an approximate **percentile** against a *synthetic, transparent norm curve* (clearly labelled "illustrative, not an official Aon norm"). Stanine 5 = middle.
- **"Not expected to finish"** is surfaced: coverage (items attempted) is shown separately from accuracy, and the coaching stresses accuracy-over-coverage.
- **Wrong-tab discipline (optional realism toggle, default ON):** if the user submits an answer while a tab *other than a required tab* is displayed, the app records a "wrong-tab" flag and (in strict mode) applies the documented point reduction — mirroring the real quirk. Off by default in learning modes; the flag is always shown in review.

## 5. Difficulty tiers

| Tier | Tabs to cross-reference | Arithmetic | Unit trickiness | Cannot-Say subtlety |
|---|---|---|---|---|
| **medium** | usually 1 | lookup / single step | single consistent unit | obvious missing data |
| **intermediate** | 1–2 | %-change, ratio | one unit conversion (thousands) | missing period/row |
| **hard** | 2–3 | multi-step, compound %, pp-vs-% | mixed units + index/base-100 | data-type mismatch, subtle omission |

## 6. Item-type coverage (mixed per session)

Every generated session mixes these, weighted by tier:
1. **direct lookup** — read one figure.
2. **single-step arithmetic** — one add/subtract/×/÷.
3. **percentage change** — divide by *original*.
4. **percentage points vs percent** — the pp/% trap.
5. **ratio / share** — share-of-total vs absolute.
6. **multi-tab combination** — figures from 2 tabs, or chart-% × caption total.
7. **trend / direction** — up/down/flat over periods.
8. **rank / comparison** — biggest/smallest, A vs B (biggest-absolute ≠ biggest-%).
9. **insufficient-data trap ("Cannot Say")** — a required figure is deliberately withheld.

## 7. How "Cannot Say" items are generated honestly (critical design rule)

The generator **knows the full ground-truth dataset**. It cannot generate a "Cannot Say" by being vague. The **only honest construction** is:

> Build a statement that *would be* decidable (True or False), then **withhold from the rendered tabs exactly one figure the statement requires** (a period, an entity row, a quantity type, or a base value). Because the required datum is provably absent from what the user can see, the correct label is provably **Cannot Say**.

Every item — including Cannot Say — is checked by an **independent verifier** (`verify/`) that re-derives the label *only from the rendered/visible data*, before the item is ever shown. A mismatch between generator-intended label and verifier-derived label = the item is **rejected and regenerated**. A generated item with a wrong label is the worst possible bug (it would teach the wrong reasoning), so verification is mandatory and tested.

## 8. Data domains (procedural, never hardcoded banks)

Random but plausible business datasets, e.g.: sales by region × quarter, headcount by division, market share by brand, revenue/costs/profit by year, survey results, production volumes. Units deliberately vary (thousands/millions, %, currency, index base-100) to exercise the unit traps.

**Chart types matched to the real test** (from Aon's official practice PDF — its 5 worked examples use exactly these forms; see the chart-types research):
- **Plain data table** — dark-slate header, bold "Total" row, zebra rows, units in a footnote ("All data in thousand dollars"). The most common form.
- **Doughnut (ring) chart** — % labels beside each arc, legend below, and an absolute-**total caption** underneath ("Total revenue: $X million") that combination items rely on.
- **Stacked vertical bar** — values printed **inside** each segment, unit in the rotated axis title ("… in thousands").
- **Grouped *horizontal* bar** (Aon's FORECAST form) — category axis vertical, value axis horizontal titled with the unit ("… in million"), value printed at each bar's end.
- **Line chart** — a metric over time (vendor-attested).

Styling replicates Aon's signature: flat 2D (no 3D/shadow), UPPERCASE titles, light horizontal gridlines only, small-square legends below the plot, data values on the marks, a compact red/teal/green/orange/magenta palette. Each metric maps to its realistic chart (share → doughnut, headcount → stacked column, a metric across future periods → grouped horizontal bar, costs → table, trends → line). Hand-rolled as **SVG**.

## 9. Coaching artefacts the format must support (Phase 3 hooks)

- Every item carries: the exact figures used, which tab(s) each came from, the step-by-step arithmetic, the decision-rule reasoning, and the trap category it targets — so the review screen can show a **worked solution** without re-deriving.
- Each answered item records **time-to-answer** and **tab-views** for diagnosis (slow-but-correct, wrong-tab, over-inference, etc.).

## 10. Explicit non-goals

- No live-test answer lookup, no proctoring evasion, no impersonation of Aon (styling is *evocative*, labelled a practice simulator, not claiming to be the real product).
- No hardcoded question bank — everything procedurally generated and verified.
- No backend/account/external API required for core functionality; runs offline via `npm run dev` (or open a file).

---

# SPEC — additional modules (verbal + logical/inductive)

Derived from `research/FINDINGS_verbal_logical.md`. The app becomes a **multi-module trainer**: a home
screen picks the test type; each module is self-contained (`modules/<name>/generator.js` + `verifier.js`
+ `render.js` + `review.js`) but shares the timer, negative-marking scoring, progress store, coaching
diagnosis, and adaptive drilling. The existing numerical module is left intact and registered as one
module among several. Difficulty tiers are named **beginner / intermediate / advanced** for the new
modules (all modules, numerical included, use beginner/intermediate/advanced). All offer **timed and untimed**.

**Shared item contract** (so coaching/scoring work uniformly): every module's item exposes
`{ module, type, tier, prompt, choices, answer, label?, traps[], solution{steps[], rationale}, requiredTab? }`
and is produced with `generate → independent verify → drop on mismatch`, exactly like numerical.

## 11. Module: scales verbal (True / False / Cannot Say over text)

- **Layout:** ~6 topic **tabs**, each a **short generated passage** (2–3 sentences) about ONE fictional
  company; one statement at a time; **True / False / Cannot Say** buttons; whole-test countdown.
  Real form ≈ 49 tasks / 12:00 (~15 s/item); app modes: Full 30/8:00-ish and drills (configurable),
  untimed. You must pick the right tab yourself → **wrong-tab** is tracked (penalty toggle).
- **Generation (provably-correct labels via a structured fact world):**
  1. Build a **fact world**: entities (company, people, products, locations, values) each with typed
     **attributes** and **relations** (e.g. `HQ(city)`, `foundedYear`, `sells(product)`, `courseMode=on-site`).
  2. Assign each fact to a **tab** and render that tab's prose from its facts (deterministic templates).
  3. Derive a statement whose **label is computed from the fact world**, never asserted:
     - **TRUE** — entailed by the relevant tab's facts (optionally via a *matching* synonym/paraphrase).
     - **FALSE** — contradicts a fact in the relevant tab (a swapped attribute value; **any** contradicted
       element ⇒ False, per Aon Ex4).
     - **CANNOT SAY** — about an entity/attribute **deliberately withheld** from all passages, or requiring
       an unstated cross-inference (Aon Ex3/Ex5). Withholding is the ONLY honest Cannot Say.
  4. Record the exact **passage span** (fact) that decides it, for the worked solution.
- **Independent verifier:** re-derives the label from the fact world by its own code path (checks whether
  the statement's asserted (entity, attribute, value) is entailed / contradicted / absent), and drops any
  item whose label disagrees. A statement referencing a withheld attribute must resolve to Cannot Say.
- **Traps by tier:** beginner = literal restatement / clear contradiction / obviously-absent;
  intermediate = synonym-match (True) vs paraphrase-flip (False), absent-attribute Cannot Say;
  advanced = absolute-quantifier overreach ("all/always/only"), near-synonym that doesn't quite match,
  plausible-but-unstated outside-knowledge lure.
- **Coaching:** quote the exact sentence that entails/contradicts; name why the other two options are
  wrong; for Cannot Say, name the missing attribute. Diagnosis: missed-Cannot-Say, used-outside-knowledge,
  wrong-tab, quantifier-overreach, paraphrase-miss, panic-guess, timeout.

## 12. Module: scales lst (shape-sudoku / gapChallenge)

- **Layout:** one N×N grid of **SVG shapes** (N=4 beginner/intermediate, 5 advanced), each shape once per
  row and column; one cell shows **"?"**; choose from N shape options. **Blank cells are pre-fillable**
  for scratch reasoning (click to cycle a candidate; not scored). Timed (~6:00) and untimed.
- **Generation:** build a **valid Latin square** over N shapes (randomised via row/column permutations of a
  base square), then blank one cell. The solution is **unique by construction** (a Latin square fixes every
  cell), so the ground truth is exact. Difficulty raises N and reduces immediately-adjacent givens.
- **Verifier:** independently confirm every row and column is a permutation of the N shapes, that the "?"
  cell has exactly one shape consistent with Latin-square constraints, and that it equals the stored answer.
- **Coaching:** show the **deduction chain** — the row and column that between them eliminate all but one
  shape for the "?" cell.
- **Diagnosis:** wrong-shape (checked only row or only column), ran-out-of-time, panic-guess.

## 13. Module: scales ix (odd-one-out / discovering rules)

- **Layout:** a series of **9 SVG shape-objects**; click the **one** that breaks the shared rule. Real form
  ≈ 20 tasks / 5:00 (~15 s/item); app runs a sequence of such items. Timed and untimed.
- **Generation:** pick an explicit **rule** over object attributes (e.g. *rotation advances 45° each step*,
  *inner/middle/outer shapes cycle*, *side-count follows a sequence*, *fill alternates*, *count increases*).
  Build 8 objects that **obey** the rule and inject exactly **one rule-breaker** at a known index — that
  index **is** the verified answer. Advanced tiers vary 2+ attributes at once (only one is the "rule";
  others are decoys) to punish checking a single property.
- **Verifier:** re-evaluate the rule over all 9 objects by its own code path; confirm exactly one object
  violates it and that its index equals the stored answer (reject if 0 or >1 violators).
- **Coaching:** **state the rule** in words and show how the odd object breaks it (and why each other object
  obeys). Diagnosis: wrong-rule, checked-only-one-property, pattern-arithmetic slip, timeout, panic-guess.

## 14. Module: scales cls (grid categorisation by a hidden rule)

- **Layout:** ten **3×3 grids** of letters/numbers; **6 are pre-marked** into two colour groups (Group A /
  Group B); **assign the 4 unmarked grids** to a group by clicking. Real form 12 tasks / 12:00. Each "task"
  = 4 assignments; app scores per assignment. Timed and untimed.
- **Generation:** pick a **hidden binary rule** over grid contents FIRST (e.g. *contains ≥3 of letter X*,
  *count of distinct symbols is even*, *a fixed cell holds a vowel*, *sum of digits > k*). Generate grids
  and label each by evaluating the rule → its true group is known. Show 6 correctly-coloured examples
  (3 per group, guaranteed to separate on the rule) + 4 unmarked to assign. Advanced tiers use subtler
  rules and closer decoys.
- **Verifier:** re-evaluate the hidden rule over every grid by its own code path; confirm the 6 examples are
  correctly coloured and that each unmarked grid's stored group matches the rule's verdict.
- **Coaching:** **state the hidden rule** and show, grid by grid, why each lands in its group.
  Diagnosis: wrong-rule, over/under-counted, timeout, panic-guess.

> **clx note:** research shows `clx` is a *different* "match 2 of 4 shape-grids to a reference rule" test,
> not a colour-sort. We build the **cls colour-sort** (matching the described mechanic) and mention clx in
> the GUIDE as a sibling; it can be added later as its own module using the same rule-first discipline.

## 15. Shared behaviour across new modules

- **Negative marking** everywhere: correct +1, wrong −1, blank 0 (research §C) → skip-vs-guess coaching.
- **Norm-referenced** synthetic Stanine/percentile, clearly labelled illustrative.
- **Back-navigation** per the research per module (verbal: allowed but "work in order"; shapes: forward with
  optional revisit) — provided as a toggle where sources conflict.
- **Honest integrity note** in the GUIDE: unsupervised scores are re-verified by a **supervised module
  retest at interview**, the item bank is randomised (nothing to memorise), and scoring is norm-referenced —
  so only the trained *skill* transfers. No proctoring-evasion content anywhere.
