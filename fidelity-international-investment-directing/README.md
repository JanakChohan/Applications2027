# Fidelity International — Investment Directing Summer Internship 2027

Interview preparation pack. Compiled 16 September 2026 from public sources only.

## Files

| File | What it is |
|---|---|
| `Fidelity_International_Investment_Directing_Complete_Interview_Pack.pdf` | The full pack. 86 pages, 17 parts, 33 diagrams, 118 sourced references. |
| `…_Complete_Interview_Pack.html` | The HTML source the PDF is rendered from. |
| `Cheat_Sheet.pdf` | One page. Also Part 13 of the full pack. |
| `Question_Bank.md` | 47 questions with scaffolds, plus 10 questions to ask. Mirrors Part 9. |
| `Reading_List.md` | What to read, in what order, and a 20-minute daily routine. |
| `research/` | The ten raw workstream findings files, with their own source tables and gaps. |
| `src/build/` | The HTML chunks and `render.py`, the two-pass renderer. |

## Rebuilding the PDF

```
pip install playwright pypdf pypdfium2 pillow
python3 src/build/render.py
```

`render.py` renders twice: the first pass maps invisible anchor markers to page numbers,
the second writes those real page numbers into the contents page. It then runs an in-browser
layout audit that fails loudly on any SVG text escaping its viewBox or any element wider than
the printed content box. It expects Chromium at `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`;
change `CHROME` at the top if yours is elsewhere.

## Conventions used in the pack

- Every non-obvious claim carries a source marker `[Sxx]` resolving to the source table in Part 15.
- Every claim carries a confidence tag: **Confirmed** (primary source or two credible outlets),
  **Reported** (single credible source), **Inferred** (the author's reasoning).
- Part 16 lists what could not be established, and is not padding.

## Two things to know before reading

1. **Fidelity International is not Fidelity Investments.** Separate companies since 1980. Most
   "Fidelity" news online is about the Boston firm.
2. **Anne Richards is not the chief executive.** That was true from December 2018 and is now out of
   date; most preparation material on the internet still says it. See Part 0.
