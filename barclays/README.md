# Barclays — A Complete Business Breakdown

Research report prepared for the **Barclays Insight Day × SEO London, 14 September 2026**.

**Deliverables**

| File | Pages | Covers |
|---|---|---|
| `Barclays-Business-Breakdown.pdf` | 38 | The whole firm — all five divisions |
| `Barclays-Wealth-Management-Deep-Dive.pdf` | 23 | Private Bank & Wealth Management only |

## What's in it

| Part | Covers |
|---|---|
| 1 | What Barclays is; 335-year history; the ring-fenced legal structure |
| 2 | How a bank makes money — net interest income, the structural hedge, fee income |
| 3 | The five divisions and their sub-divisions, with full FY2025 scorecard |
| 4 | Which parts make the money — income vs. capital consumed |
| 5 | Strategy: the 2024–26 plan and the 2026–28 successor |
| 6 | Acquisitions and disposals, explained (BZW, Lehman, Absa, Kensington, Tesco, Best Egg) |
| 7 | Relationship banking and how mandates are actually won |
| 8 | Competitors, and what makes Barclays a category of one |
| 9–10 | Client segments and the full product catalogue |
| 11 | Market view: earnings calls, analysts, press, industry forums |
| 12 | Live 2026 issues: rates, motor finance redress, IB leadership, capital returns |
| 13 | Choosing a division, key numbers, questions to ask on the day |
| 14 | Sources and method |

## Wealth deep dive contents

| Part | Covers |
|---|---|
| 1 | The group revenue split drawn to scale, ranked two ways |
| 2 | How the division splits — PBWM UK vs International, the client ladder and its thresholds |
| 3 | The revenue model: 58% interest / 42% fees, and AUM vs AUS vs client assets |
| 4 | The numbers read honestly — why profit fell while returns stayed best-in-group |
| 5 | Where it ranks globally and in the UK, and the NatWest/Evelyn deal |
| 6 | Target clients: the ~4m customers with £250k–£3m |
| 7 | 335 years of history as a competitive moat; the 2003 Gerrard deal |
| 8 | News, deals, wins and losses since 2025 |
| 9 | Why a client picks Barclays over UBS, Coutts, Julius Baer or an independent |
| 10 | Roles, the case for and against, and questions to ask |

## Rebuilding

```
python3 build.py    # parts/*.html  + gen.py charts -> report.html
python3 build2.py   # parts2/*.html + gen.py charts -> wealth-report.html
chrome --headless --print-to-pdf=OUT.pdf --no-pdf-header-footer IN.html
```

- `gen.py` — inline-SVG chart generator (no external libraries)
- `parts/`, `parts2/` — report content, concatenated in filename order
- `style.css` — shared A4 print stylesheet
