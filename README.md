# Applications2027

## LSEG: Business Management Summer Internship 2027 (R0123386)

| File | What it is |
|---|---|
| `LSEG/LSEG_Business_Management_Summer_Internship_Complete_Interview_Pack.pdf` | The full research pack, 260 pages, Parts 0 to 16, 45 figures |
| `LSEG/LSEG_Business_Management_Summer_Internship_Complete_Interview_Pack.html` | Self-contained HTML source of the pack |
| `LSEG/Cheat_Sheet.pdf` | Two-page cheat sheet (also Part 13 of the pack) |
| `LSEG/Question_Bank.md` | 58 questions with scaffolds, plus 10 questions to ask |
| `LSEG/Reading_List.md` | Sources to follow and a daily routine |
| `LSEG/research/` | Workstream findings files with full source rows |
| `LSEG/build/` | Report fragments (`parts/`), stylesheet and build scripts |

Rebuild: `node LSEG/build/build.js` (needs Playwright and poppler `pdftotext`; `python3 LSEG/build/gen_sources.py` regenerates the source table first).
