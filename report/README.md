# Blackstone — Deep Dive Briefing

A 44-page briefing prepared ahead of the Blackstone SEO Networking Evening
(2 September 2026, 40 Berkeley Square, London).

**Deliverable:** `Blackstone-Deep-Dive-Briefing.pdf`

## Contents

Part 0 covers the foundations (what an alternative asset manager is, the GP/LP
structure, the fund lifecycle, fee mechanics, vocabulary). Parts 1–4 cover
history, business structure, the revenue model and the four segments. Part 5 is
the client-facing franchise — institutional, insurance and private wealth
channels. Parts 6–10 cover leadership, current strategy, the competitive
landscape, Europe/London and the criticisms. Part 11 is a pre-event playbook
with tiered questions and a jargon reference.

All figures are drawn from public sources to 2 September 2026 (SEC filings,
the Q2 2026 earnings call, press releases and mainstream financial press).
Derived or approximate numbers are flagged in the text.

## Rebuilding the PDF

```
node render.js          # renders _cover.pdf (full bleed) and _body.pdf (margins + page numbers)
python3 -c "..."        # merge with pypdf — see git history for the merge snippet
```

Requires Playwright's bundled Chromium. Fonts (Inter, Source Serif 4) are
vendored in `fonts/` so rendering is deterministic and offline.

- `blackstone-briefing.html` — full source, including all inline SVG diagrams
- `style.css` — print stylesheet (A4)
- `shots.js` — screenshots each `<figure>` for visual QA
