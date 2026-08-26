# Work Experience Guide

`Work_Experience_Guide.pdf` — a 13-page A5 booklet for work experience students
(and useful for interns). Assumes zero knowledge of finance.

## Pages

| # | Page | What it does |
|---|---|---|
| — | Cover | Logo placeholder + name/dates/host fill-in |
| 1 | What's in this guide | Contents + the five rules that matter |
| 2 | Who we actually are | Group vs the four business lines |
| 3 | What asset management is | Explained as a shop: who we sell to, what we sell, how we get paid |
| 4 | How the business works | Marketing → Sales → RFP → Onboarding → Client Service → Reporting |
| 5 | How an investment happens | Research → PM → Trader → Execution → Ops → Trade Support → Reporting |
| 6 | Who does what | Every team, one line each, with a blank Floor column |
| 7 | Coffee chats | What they are actually for, and how to run 15 minutes |
| 8 | Questions to ask | ~24 questions grouped by type |
| 9 | Things we wish we'd known | The honest list |
| 10 | Useful links | Blank internal links + what to search |
| 11 | Your notes | People-met table + before-you-leave checklist |

## Before printing — three things to fill in

1. **Cover logo** — replace the dashed `Logo goes here` box with the official
   logo (`.logobox` in the CSS, or drop the image into the PDF).
2. **Team names** — `FRONT` and `BACK` lists in `build_guide.py`. Three blank
   rows are already there for teams to add. The Floor column is deliberately
   blank so students fill it in themselves.
3. **Links** — page 10 is intentionally half-blank; the internal link rows and
   the three recommended videos are for the host to complete.

## Printing

A5 portrait, 13 pages, in reading order — no imposition needed. Either print A5
direct, or print A4 with "2 pages per sheet" and trim. Staple top-left.

## Rebuilding

```
python3 build_guide.py
chromium --headless --no-pdf-header-footer \
  --print-to-pdf=Work_Experience_Guide.pdf file://$PWD/work_experience_guide.html
```

Needs `fonts_embedded.css` alongside it (Inter + Source Serif 4, base64
embedded). All diagrams are generated inline SVG — no external assets.
