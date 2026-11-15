# GSAM Client Solutions Group 2027: guide and research dossier

Preparation material for the **2027 | EMEA | London | Asset Management, Client Solutions Group | Summer Analyst** programme at Goldman Sachs. Independent work: not produced by, endorsed by or affiliated with Goldman Sachs.

Research date and information cutoff: **14 November 2026**.

## What is here

| File | What it is |
|---|---|
| `gsam_csg_command_center.html` | The website. One file, works offline, makes no network requests, stores nothing |
| `GSAM_CSG_2027_Dossier.pdf` | Printable guide, 591 pages, with linked contents and page numbers. Opens with the three beginner pages and their diagrams. Set for easier reading: sans-serif, larger text, wider spacing, cream pages, no italics |
| `dossier/GSAM_CSG_2027_Master_Dossier.md` | Everything in Markdown |
| `content/chapters/` | The text. `0A`, `0B` and `0C` are the three beginner guide pages; `00` to `11` are the deeper chapters |
| `data/` | The evidence base: sources, checked claims, teams, people, mandates, market changes, glossary, interview bank, quiz, numbers, charts |
| `research/evidence/` | Raw research notes per stream, with search logs |
| `build/` | Scripts that generate and test everything |
| `archive/` | Removed material: the earlier site design, the why-tree exercises and the motivation chapter |

The website, the PDF and the Markdown dossier are generated from `content/` and `data/` by one script, so they cannot disagree.

## The website

Open `gsam_csg_command_center.html` in a browser. It is deliberately plain: one typeface, one accent colour, no points or games.

- **Home**: three pages to read in order.
- **The role**: what you are applying to, from zero. Whose money it is, how the firm is paid, what a junior person does.
- **Relationships**: who a client relationship is with, what starts it, what continues it, what builds it, how it ends, where the work happens, why it matters, what it looks like over 1 to 40 years and in year one, and how to talk about it.
- **Sales and RM**: how a client is won step by step, how the relationship is kept, how the two jobs differ, with every step expandable.
- **Teams**: each team's clients, talking points, questions to ask and watch-outs, plus the coverage map.
- **Facts**: numbers with caveats, key findings, charts, and the check of the former intern's account.
- **Practise**: interview questions with reasoning, a silent timer, a quick quiz and cases.
- **Library**: the deeper chapters, people, mandates, market changes, roles, fee calculator, glossary and sources.

Every fact shows its evidence: Verified, Supported inference, Unverified account, Illustrative example, Conflicting evidence or Not publicly established.

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

The PDF step and the tests need Node with Playwright and Chromium.

## What was tested (15 November 2026)

`node build/test_app.js` ran 78 checks and all 78 passed. They cover:

- Loads with no network requests; nothing written to browser storage; no microphone or recording code.
- Home and all seven sections open; the home page leads with the three guide pages.
- The Relationships page contains every topic asked for and its diagrams; the Sales page has the step-by-step process with expandable steps.
- Why-trees, points, levels and game tiles are gone.
- Diagrams: none has text outside its picture; each has a text description; no duplicate ids.
- Links inside pages, links to mandates and source codes all open the right place.
- Search, filters, team selection, the coverage map, numbers "test me", charts, timed practice, quiz scoring, chapter reader, reading level, glossary definitions.
- Calculator arithmetic against an independent Python implementation on all fifteen examples.
- Every citation resolves; no missing values shown as text; the one unconfirmed client name appears nowhere.
- Keyboard: skip link, "/" for search; labelled controls; no italic text; body text at least 17px with 1.6 line height.
- No sideways scrolling on eleven pages at phone width; reduced-motion and dark device settings respected.

The PDF was rendered and sample pages were inspected by eye. Not every page was inspected. Not tested: screen readers and browsers other than Chromium.

## Known limits

- The search allowance ran out during research, so some topics are marked "not investigated" in the coverage list (Library, Sources).
- Goldman's careers site could not be read directly; most job-advertisement evidence is from mirrors and is marked as inference.
- The people directory is a sample of publicly visible professionals, not a headcount.
- No mandate is attributed to a London team or person, because no public source does so.
- Most of the Relationships and Sales pages describe general industry practice. Those parts are labelled "Supported inference". They are not published Goldman procedures.
- One client named in the starting account has no public confirmation and is withheld from every generated output. The raw notes in `research/evidence/` still contain it, so check those before sharing the repository.
- No personal records are used.
- Nothing has been published or hosted. The HTML is a local file.
