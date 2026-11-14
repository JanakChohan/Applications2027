# GSAM Client Solutions Group 2027: research dossier and study platform

Preparation material for the **2027 | EMEA | London | Asset Management, Client Solutions Group | Summer Analyst** programme at Goldman Sachs. Independent work: not produced by, endorsed by or affiliated with Goldman Sachs.

Research date and information cutoff: **14 November 2026**.

## What is here

| File | What it is |
|---|---|
| `gsam_csg_command_center.html` | The interactive study application. One file, works offline, makes no network requests |
| `GSAM_CSG_2027_Dossier.pdf` | Printable study guide, 539 pages, with linked contents and page numbers. Contains everything in the application with every panel opened |
| `dossier/GSAM_CSG_2027_Master_Dossier.md` | The master dossier in Markdown: twelve chapters and appendices A to T |
| `content/chapters/` | The chapter sources (about 88,000 words) |
| `data/` | The structured evidence base: sources, claims, teams, people, mandates, developments, glossary, why-trees, interview bank, quiz, key numbers, charts |
| `research/evidence/` | Raw research notes per stream, with search logs and "searched, not established" lists |
| `research/CONVENTIONS.md` | Schemas, evidence vocabulary and writing conventions |
| `build/` | Generation and test scripts |

All three outputs are generated from `content/` and `data/` by one script, so the website, PDF and dossier cannot disagree. Entities carry stable IDs (for example `R2-S01` for a source, `M-R7-01` for a mandate, `P-R6-01` for a person) that are the same in every output.

## The application

Open `gsam_csg_command_center.html` in any modern browser. Sections:

- **Mission control**: dashboard, section tiles, top intel, numbers, learning routes, XP level.
- **Intel**: 62 evidence-backed findings, each with what a quick read gets wrong and how to use it.
- **Numbers to know**: 45 figures with caveats, a "Test me" mode, and nine charts of Goldman's own disclosures.
- **Read the dossier**: twelve chapters with Beginner, Technical or Both views and glossary pop-ups.
- **Teams and coverage**: coverage matrix (default), organisational map, optional 3D explorer, and a briefing per team with talking points, questions to ask and watch-outs.
- **People directory**, **Mandates and events**, **Commercial awareness** (with competitors): filterable cards with sources.
- **Role comparison**, **Client lifecycle**, **Fee calculator** (with fifteen worked cases).
- **Why-trees**, **Interview practice** (34 questions, six cases, silent timer, self-scoring) and **Arcade** (quiz of 110 questions, glossary flashcards, "Verified or rumour?", number recall).
- **Glossary** and **Sources and evidence** (source register, claim register, audit of the former intern's account, coverage register, search strings).

Every claim carries one of six evidence statuses, shown as a badge with a symbol and a written label: Verified, Supported inference, Unverified account, Illustrative example, Conflicting evidence, Not publicly established.

Progress and XP are kept in memory only. Ticking "Keep my XP and progress in this browser" stores them in that browser's local storage; unticking or "Reset progress" removes them. Nothing is sent anywhere. Practice mode uses an on-screen timer only: no microphone, no recording.

## Rebuilding

```bash
pip install markdown pypdf
```

```bash
python3 build/build.py --pdf
```

```bash
node build/test_app.js
```

The PDF step and the tests need Node with Playwright and Chromium. `build/build.py` without `--pdf` regenerates the dossier and the HTML only. `build/calc.py` is the fee model; the same algorithm is implemented in JavaScript in `build/app/app.js`, and the tests check that the two agree on every worked case.

## What was tested (14 November 2026)

`node build/test_app.js` ran 87 checks and all 87 passed. They cover:

- Loads with no network requests; no external scripts, stylesheets, images or fonts.
- All 16 sections open one at a time with correct navigation state.
- Full-text search returns results, links through, and reports zero results honestly.
- Filters on intel, people and mandates; team selection; matrix cell links; tabs by keyboard; 3D explorer draws.
- Beginner view hides Level 2 blocks and keeps caveats visible; glossary pop-up opens and closes with Escape.
- Calculator: £500m at 20bp = £1,000,000; tranche funding = £750,000; tiered £600m = £1,275,000; committed-capital base ignores drawdown and markets; a withdrawal cannot go below zero; JavaScript equals Python on all fifteen cases.
- Lifecycle stepping and both paths; why-trees expand, collapse and open from the keyboard.
- Practice timer, reveal, scoring and history; quiz round scoring and XP; flashcards; "Verified or rumour?"; number recall.
- Nothing stored unless saving is switched on; reset and switch-off clear it; no microphone or recording code in the page.
- No unresolved citations; every cited source has a register row; no "undefined", "NaN" or missing value shown as zero; no blank matrix cells.
- The one client name without public confirmation appears nowhere.
- Skip link is the first Tab stop; "/" focuses search; landmarks, language, one h1 per section, labelled controls; badges carry text.
- No horizontal page scroll on ten sections at phone width; mobile menu opens and closes; reduced-motion disables smooth scrolling and celebration animation.

The PDF was rendered and sample pages inspected from the contents, chapters, matrix, people table, fee cases, source register, numbers and charts, quiz bank and claim register: tables fit the page, contents entries carry page numbers (141 numbered), no clipped text seen in the sample. Not every one of the 539 pages was inspected by eye.

Not tested: screen readers, browsers other than Chromium, and printing the HTML directly from a browser.

## Known limits

- **The search allowance ran out during research.** Several streams stopped before their plan was complete. The coverage register (Sources view, Appendix M) separates "searched, not established" from "not investigated".
- **Goldman's careers site could not be read directly.** Most job-advertisement evidence comes from mirrors or search summaries and is capped at "Supported inference".
- **The people directory is a sample of publicly visible professionals**, not a headcount. It cannot support a sales-to-relationship-management ratio or any estimate of hiring odds.
- **No mandate is attributed to a London team or person**, because no public source does so.
- **One client named in the starting account has no public confirmation** and is withheld from every generated output by the build (`REDACT` in `build/build.py`). The raw notes in `research/evidence/` keep the audit trail, so check those before sharing the repository itself.
- **No personal records are used.** The personal evidence ledger is a blank template.
- **Nothing has been published or hosted.** The HTML is a local file. To host it, upload the single file to any static host; check the people directory and source register first and decide what you are comfortable circulating.
- **Interpretation is labelled, not proven.** Layer B passages are arguments; practice criteria are a proposed framework, not Goldman's.
