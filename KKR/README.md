# KKR London Summer Internship 2027: research packs

Prepared 11-12 October 2026 for an application to KKR's London 2027 summer internship (via SEO London), first choice Global Client Solutions (KCS).

## Deliverables (`output/`)
| File | What it is |
|---|---|
| `KKR_Client_Solutions_KCS_Deep_Dive.pdf` (+ `.html`) | 212-page deep dive on KCS: private markets from zero, KKR from the inside, KCS history, channels, products and team map, the role decoded line by line, competitive research on peer client teams, regulation, news, debates, KCS question bank, scenario playbook, why KCS/why KKR, cheat sheet, glossary, sources, gaps |
| `KKR_London_Summer_Internship_2027_Complete_Interview_Pack.pdf` (+ `.html`) | 195-page complete pack: all six London teams decoded and linked, the firm, why it is built this way, how it stands out, industry, regulation, news, debates, interview, interviewer briefing, scenario playbook, why KKR, cheat sheet, glossary, sources, gaps |
| `KKR_KCS_What_You_Will_Learn_Technical_Guide.pdf` (+ `.html`) | 160-page technical guide to what the KCS seat teaches, built around the application question "What do you hope to learn?" |
| `Learning_Question_Answers.md` | Three answers under 1,000 characters |
| `KKR_KCS_Previous_Experience_Pictet_Guide.pdf` (+ `.html`) | 108-page guide: Pictet from zero, the client-group role decoded, the bridge to KKR KCS |
| `Experience_Question_Answers.md` | Three answers under 1,000 characters |
| `Cheat_Sheet.pdf` | One page |
| `Question_Bank.md` | Every interview question with what it tests, structure, facts to weave in and traps |
| `Reading_List.md` | Sources to follow, with a 7-day plan |

## How it was built
- `research/`: seven workstream findings files (WS1 KCS function, WS1B team map, WS2 firm, WS3 competitors, WS4 industry and regulation, WS5 news, WS6 interview), each with a source table. Source IDs `[Sxx]` in the PDFs resolve to these.
- `build/`: HTML parts, shared sections, `style.css`, `build.py` (two-pass Playwright render with real contents page numbers), `gen_sources.py`, `gen_qbank.py`.
- Rebuild: `cd build && python3 gen_sources.py && python3 build.py kcs && python3 build.py main && python3 build.py learn && python3 build.py pictet && python3 build.py cheat && python3 gen_qbank.py`.
