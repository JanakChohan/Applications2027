# CROX pitch - task checklist

| Phase | Task | Status | Output |
|---|---|---|---|
| 0 | Set up folder, data and scripts directories | [x] | `CROX-pitch/` |
| 0 | Download SEC filings (10-K x6, 10-Q x9, earnings releases x26, proxy, Form 4s, 13Gs) | [x] | `data/sec/`, `data/sec_txt/` |
| 0 | Market data, consensus, short interest, holders | [x] | `data/market/` (Nasdaq API; Yahoo price API and Macrotrends refused automated access, see sources.md) |
| 0 | Peer fundamentals and multiples | [x] | `data/sa/` |
| 0 | Earnings call transcripts (six calls) and web research | [x] | `data/transcripts/`, `data/research/` |
| 1 | Deep dive (11 sections) | [x] | `deep-dive.md` |
| 2 | Peer comparison, P/E history, premium/discount | [x] | `deep-dive.md`, `charts/08-10`, `model.xlsx` Peers |
| 3 | Bear case: 3 ranked red flags and checklist | [x] | `deep-dive.md` Phase 3 |
| 4 | Key debate, annotated price chart, revenue-at-risk analysis, stress test, sensitivity | [x] | `deep-dive.md` Phase 4, `charts/07, 12, 13`, `model.xlsx` RevAtRisk |
| 5 | Forecast, DCF, reverse DCF, scenarios, sensitivities | [x] | `model.xlsx` |
| 6 | Catalyst table | [x] | `deep-dive.md` Phase 6 |
| 7 | Thesis, variant perception, pillars, risks, kill criteria | [x] | `deep-dive.md` Phase 7 |
| 8 | deck.pptx (15 main slides plus appendix, speaker notes) | [x] | `deck.pptx` |
| 8 | pitch-memo.docx | [x] | `pitch-memo.docx` |
| 8 | model.xlsx, one-pager.md, qa-prep.md, cheat-sheet.md, sources.md | [x] | as named |
| 9 | Re-run scripts, formula-error scan, cross-document number check | [x] | `verification.md` |
