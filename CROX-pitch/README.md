# CROX-pitch

Institutional-style stock pitch on Crocs, Inc. (NASDAQ: CROX), prepared 2026-11-26. Price $159.93 (Nasdaq close 2026-11-25).

**Recommendation: LONG, moderate conviction. Base target $207 (December 2027), probability-weighted value $199, bear $92, bull $289.** All price targets are my estimates from `model.xlsx`.

## Deliverables

| File | What it is |
|---|---|
| `deck.pptx` | 15 main slides plus a 10-slide appendix, takeaway titles, source lines, speaker notes |
| `pitch-memo.docx` | 5-page memo |
| `model.xlsx` | Forecast, three scenarios, DCF, reverse DCF, sensitivities, revenue-at-risk stress test, peers. 1,046 live formulas |
| `deep-dive.md` | Full research report, Phases 1-7 |
| `one-pager.md` | One-page summary |
| `risks-catalysts-mitigants-slides.pptx` | The catalysts, risks and mitigants section as editable slides: two core slides, a one-slide alternative in the layout Oakwood's Consumer team used before, and one backup slide. Speaking scripts are in the notes |
| `crocs-risk-catalyst-guide-easy-read.pdf` | Dyslexia-friendly, diagram-led version of the study guide (44 short pages): bottom line first, terminology built up level by level, risks, mitigants and catalysts, scripts and likely questions. Set in Lexend (SIL Open Font License, files in `assets/fonts/`) |
| `study-guide-risk-and-catalysts.pdf` | Beginner's study guide to the pitch, focused on risk and catalysts, with speaking scripts and likely questions |
| `qa-prep.md` | 20 toughest questions with 30-second answers |
| `cheat-sheet.md` | 25 numbers to know |
| `sources.md` | Every source with URL, label and as-of date; where sources disagree; what was not found |
| `verification.md` | Phase 9 checks and the list of uncertain or stale items |
| `checklist.md` | Task checklist by phase |
| `charts/` | 16 charts (PNG), each with its own source line |
| `data/` | Raw filings, market data, transcripts, research notes, derived datasets |
| `scripts/` | Everything is reproducible: `bash scripts/run_all.sh` (add `--offline` to skip downloads) |

## Choices made where the brief was blank

- **Peers:** Deckers (DECK), Birkenstock (BIRK), On Holding (ONON). Skechers, the closest on price point, went private in 2025.
- **Direction:** decided from the evidence (long).
- **Holding period:** 12-18 months; targets dated December 2027.
- **Audience:** a fundamental long/short PM with a value and cash-return tilt.
- **Format:** 15-minute pitch, 15 main slides plus appendix.

## Data-source notes

Yahoo Finance's price API and Macrotrends refused automated requests. Prices, short interest and one set of consensus numbers come from Nasdaq's public API; Yahoo's consensus and statistics pages were read separately; peer multiples come from StockAnalysis. Historical P/E is calculated from prices and reported EPS. Details in `sources.md`.

**Not committed to git:** full earnings-call transcripts (`data/transcripts/`) and raw vendor web pages (`data/sa/*.html`) are third-party copyrighted text. The notes with verbatim quotes and source URLs (`data/research/transcript_notes.md`) and the parsed tables (`data/sa/*.csv`) are included; `scripts/19_verify.py` needs the transcripts on disk for its quote checks.

This is research prepared with an AI assistant from public sources. It is not investment advice; verify the numbers flagged in `verification.md` before acting on it.
