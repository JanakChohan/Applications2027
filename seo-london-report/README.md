# SEO London — Deep-Dive Intelligence Report

A researched, multi-part PDF report on Sponsors for Educational Opportunity (SEO) London:
what it is, how its business model works, how it screens and recommends candidates, its
employer network, and how to position for the 2027 internship and graduate cycle.

## Files

| File | What it is |
|---|---|
| `SEO-London-Deep-Dive-Report.pdf` | The deliverable — 114 pages, 28 parts, 5 diagrams |
| `report.html` | Source. Edit this, then re-render |
| `render.py` | Renders `report.html` to PDF via headless Chromium |

## Regenerating the PDF

```bash
pip install playwright
python3 render.py report.html SEO-London-Deep-Dive-Report.pdf
```

The renderer uses the pre-installed Chromium at
`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; change `executable_path` in
`render.py` if yours differs.

## Evidence grading

Claims in the report are labelled **Confirmed**, **Inference**, **Anecdotal** or
**Analysis**. Sources and noted disagreements between them are listed in the
bibliography at the end.

## Currency

Researched 23 August 2026. Programme dates and the partner-firm list change every
cycle — Parts 4 and 25 should be rebuilt from the live SEO London portal each September.
The structural analysis in Parts 1–11 ages far more slowly.
