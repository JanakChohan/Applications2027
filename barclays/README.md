# Barclays — A Complete Business Breakdown

Research report prepared for the **Barclays Insight Day × SEO London, 14 September 2026**.

**Deliverable:** `Barclays-Business-Breakdown.pdf` (38 pages, A4)

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

## Rebuilding

```
python3 build.py          # parts/*.html + gen.py charts -> report.html
chrome --headless --print-to-pdf=Barclays-Business-Breakdown.pdf --no-pdf-header-footer report.html
```

- `gen.py` — inline-SVG chart generator (no external libraries)
- `parts/*.html` — report content, concatenated in filename order
- `style.css` — A4 print stylesheet
