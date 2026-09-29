# Schroders Client Group Internship 2027: interview research pack

Built 29 September 2026 from public sources.

## Deliverables
- `Schroders_Client_Group_Internship_2027_Complete_Interview_Pack.pdf` (and `.html` source): the full pack, Parts 0 to 16.
- `Schroders_Client_Group_2027_Question_Bank.pdf`: Cappfinity video prompts, ranked work-simulation scenarios, and the 44-question bank.
- `Schroders_Client_Group_2027_Reading_List.pdf`: sources to follow.
- `Schroders_Client_Group_2027_Cheat_Sheet.pdf`: the one-page cheat sheet (also Part 13).

## Research
`research/WS*.md`: workstream findings files. Each has findings, a key numbers table, verbatim quotes, source rows, gaps and interview angles.

## Rebuild
Requires Python with `playwright`, `pymupdf` and `pypdf`, the preinstalled Chromium, and the Source Sans 3 and Source Serif 4 fonts in `~/.fonts`.

```
cd build
python3 figs_playbook.py && python3 figs_industry.py && python3 figs_firm.py && python3 figs_role.py
python3 gen_playbook.py && python3 gen_qbank.py && python3 gen_sources.py
python3 build.py --png   # two-pass render; PNGs of every page go to build/_tmp/png
python3 check_svg.py     # flags SVG text or shapes outside the viewBox, or overlapping labels
```
