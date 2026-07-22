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

Random but plausible business datasets, e.g.: sales by region × quarter, headcount by division, market share by brand, revenue/costs/profit by year, survey results, production volumes. Units deliberately vary (thousands/millions, %, currency, index base-100) to exercise the unit traps. Each dataset renders across ~6 tabs as a mix of **bar / grouped-bar / stacked-bar / line charts and plain tables**, hand-rolled as **SVG** (legible, boring).

## 9. Coaching artefacts the format must support (Phase 3 hooks)

- Every item carries: the exact figures used, which tab(s) each came from, the step-by-step arithmetic, the decision-rule reasoning, and the trap category it targets — so the review screen can show a **worked solution** without re-deriving.
- Each answered item records **time-to-answer** and **tab-views** for diagnosis (slow-but-correct, wrong-tab, over-inference, etc.).

## 10. Explicit non-goals

- No live-test answer lookup, no proctoring evasion, no impersonation of Aon (styling is *evocative*, labelled a practice simulator, not claiming to be the real product).
- No hardcoded question bank — everything procedurally generated and verified.
- No backend/account/external API required for core functionality; runs offline via `npm run dev` (or open a file).
