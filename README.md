# CCAT Trainer

A complete, **offline** CCAT (Criteria Cognitive Aptitude Test) practice and
training application in a single self-contained file. Double-click
`index.html` and open it in Chrome — no build step, no dependencies, no CDN,
no network calls. All progress persists in `localStorage`.

> Independent study tool, unaffiliated with and not endorsed by Criteria Corp.
> CCAT is a registered trademark of Criteria Corp. All 600 questions are
> original and written for practice.

## What it does

- **Exact test replica** — 50 questions / 15 minutes, one global timer, ~18s
  budget, no calculator, **no skipping and no going back** (strict
  forward-only), mixed order, upward difficulty ramp, no negative marking,
  percentile vs the normative median 24 / SD 7, and a 35+ target band.
- **600-item bank** — ~210 math/logic, ~210 verbal, ~180 spatial across 26
  subtypes. Math and spatial items are produced by original generators that
  *compute* the correct answer and derive every distractor from a named trap
  (`unit-switch`, `reverse-percentage`, `off-by-one`, `near-synonym`,
  `wrong-relation`, `mirrored-figure`, `partial-transformation`, …). Spatial
  figures are inline SVG built around a chiral base shape, so rotation vs.
  reflection is always unambiguous.
- **The Pacing Ladder** — a five-rung on-ramp (untimed → generous → realistic
  → real conditions) that introduces the clock only once accuracy is
  established, with per-category tracking and stated unlock criteria.
- **Modes** — Full Simulation, Timed Drill, Untimed Learn, Speed Ladder, and a
  Weak-Spot Auto-Drill that targets your worst subtypes.
- **Timing instrumentation** — per-question timing everywhere, a per-question
  timeline chart with the 18s budget line, "time bled", sinkhole detection,
  accuracy-by-position, and a Triage Coach that names your failure mode.
- **Guides** — a full teaching curriculum: Orientation, Math (with a mental
  arithmetic bootcamp), Verbal (bridge sentences, a vocabulary list), Spatial,
  Timing & Triage, Test-Day Protocol, and the EPP personality module.
- **Dashboard & 7-day plan** — trend line, subtype heatmap, next-action
  recommendation, and an adaptive day-by-day study plan.
- Dark mode, keyboard-first (1–4 to answer, Enter to advance), mobile
  responsive, export/import backup, and a reset-all button.

## Usage

Open `index.html` in a browser. Start on the dashboard; the recommended next
action and the Pacing Ladder guide you from zero.
