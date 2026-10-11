#!/usr/bin/env python3
"""Generate shared/sources.html from the source tables in ../research/WS*.md"""
import re, html, pathlib
R = pathlib.Path(__file__).resolve().parent.parent / "research"
NAMES = {"WS1_kcs_function": "WS1 · KCS function (S70-S139)", "WS1B_team_map": "WS1B · Team map (S140-S199)",
         "WS2_firm": "WS2 · The firm (S1-S69)", "WS3_competitors": "WS3 · Competitors (S200-S259)",
         "WS4_industry_regulation": "WS4 · Industry and regulation (S260-S329)", "WS5_news": "WS5 · Live news (S330-S369)",
         "WS6_interview": "WS6 · Interview intelligence (S370-S419)"}
order = ["WS2_firm", "WS1_kcs_function", "WS1B_team_map", "WS3_competitors", "WS4_industry_regulation", "WS5_news", "WS6_interview"]
out = ['<h2 id="src-how">How to read this table</h2><p>Every <span class="src">[Sxx]</span> marker in the text resolves to a row below. '
       'Status: FETCHED means the full page or document was read; SNIPPET means only a search-result extract was seen (treat as weaker); '
       'PAYWALLED means the article itself was not read. All sources accessed between 11 and 12 October 2026. Each workstream had its own ID range, so gaps in numbering are expected.</p>']
seen = set()
for stem in order:
    f = R / f"{stem}.md"
    if not f.exists():
        continue
    rows = []
    for line in f.read_text().splitlines():
        m = re.match(r"^\|?\s*\[(S\d+)\]\s*\|(.*)$", line)
        if not m or m.group(1) in seen:
            continue
        cells = [c.strip() for c in m.group(2).strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        seen.add(m.group(1))
        outlet, title, pub, url = cells[0], cells[1], cells[2], cells[3]
        status = cells[5] if len(cells) > 5 else ""
        note = " | ".join(cells[6:]) if len(cells) > 6 else ""
        rows.append((int(m.group(1)[1:]), m.group(1), outlet, title, pub, url, status, note))
    rows.sort()
    out.append(f'<h2 id="src-{stem[:4].lower()}">{NAMES[stem]}</h2><table class="src-table tight"><thead><tr><th>ID</th><th>Outlet</th><th>Title</th><th>Published</th><th>URL</th><th>Status · note</th></tr></thead><tbody>')
    for _, sid, outlet, title, pub, url, status, note in rows:
        e = html.escape
        out.append(f"<tr><td>{sid}</td><td>{e(outlet)}</td><td>{e(title)}</td><td>{e(pub)}</td><td>{e(url)}</td><td>{e(status)}{' · ' + e(note) if note else ''}</td></tr>")
    out.append("</tbody></table>")
pathlib.Path(__file__).resolve().parent.joinpath("shared/sources.html").write_text("\n".join(out))
print(len(seen), "sources")
