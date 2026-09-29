#!/usr/bin/env python3
"""Figures for Parts 2, 3, 4, 7, 12 (firm, structure, competition, news, why)."""
import os
from svglib import *

ROOT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(ROOT, "fragments")


def save(name, s):
    open(os.path.join(FR, f"fig_{name}.html"), "w").write(s)


def moneyflow():
    W, out = 680, [arrow_defs("mf")]
    y = 8
    out.append(text(340, y + 12, "FY2025, year to 31 December 2025. All figures adjusted unless marked. Source: Schroders annual results 2025 [S71] and AR 2025 [S72].", 9.5, MUTED, "middle")[0])
    y = 30
    # Layer 1: clients
    out.append(text(8, y + 10, "1  CLIENTS HAND OVER CAPITAL", 10, NAVY, weight=700)[0])
    chans = [("Institutional", "64% of AUM", S[0]), ("Intermediary", "19% of AUM", S[1]), ("Wealth", "17% of AUM", S[2])]
    for i, (c, s, col) in enumerate(chans):
        out.append(box(8 + i * 226, y + 18, 214, 44, c, "#fff", col, INK, 12, 700, sub=s, subsize=9.5, sw=2))
        out.append(line(115 + i * 226, y + 64, 340, y + 96, "mf", MUTED, 1.2))
    y += 98
    out.append(box(170, y, 340, 52, "Assets under management £823.7bn", NAVY, NAVY, "#fff", 13, 700,
                   sub="incl. JVs, record. Gross inflows £142.0bn; net new business +£11.2bn (ex JVs). Average AUM ex JVs £686.2bn", subsize=9, subcol="#DDE4EF"))
    y += 60
    out.append(line(340, y, 340, y + 22, "mf"))
    y += 26
    out.append(text(8, y + 10, "2  EACH BUSINESS CHARGES A FEE RATE ON ITS ASSETS (net operating revenue, margin ex performance fees)", 10, NAVY, weight=700)[0])
    biz = [("Equities", "£225.1bn", "45bp", "£945.2m"), ("Fixed income", "£87.0bn", "34bp", "£281.7m"),
           ("Multi-asset", "£102.4bn", "24bp", "£234.5m"), ("Core solutions", "£118.6bn", "6bp", "£66.5m"),
           ("Schroders Capital", "£72.6bn", "57bp", "£438.7m"), ("Wealth Mgmt", "£123.9bn", "40 to 48bp", "£537.7m")]
    bw = 106
    for i, (n, a, m, r) in enumerate(biz):
        x = 8 + i * (bw + 5)
        col = S[0] if i < 4 else (S[3] if i == 4 else S[2])
        out.append(f'<rect x="{x}" y="{y+18}" width="{bw}" height="92" rx="4" fill="#fff" stroke="{col}" stroke-width="1.6"/>')
        out.append(f'<rect x="{x}" y="{y+18}" width="{bw}" height="22" rx="4" fill="{col}"/>')
        out.append(text(x + bw / 2, y + 33, n, 9.8, "#fff", "middle", 700)[0])
        out.append(text(x + bw / 2, y + 56, "AUM " + a, 9.5, INK2, "middle")[0])
        out.append(text(x + bw / 2, y + 76, m, 15, NAVY, "middle", 700)[0])
        out.append(text(x + bw / 2, y + 100, "Rev " + r, 10, INK, "middle", 600)[0])
        out.append(line(x + bw / 2, y + 112, 340, y + 150, "mf", MUTED, 1))
    y += 152
    out.append(box(150, y, 380, 52, "Net operating revenue £2,504.3m", "#EEF3FA", S[0], INK, 13, 700,
                   sub="incl. £79.4m performance fees and carry. Blended rate about 36.5bp [Inferred: 2,504.3 / 686.2]. Plus JV profits £49.3m = adjusted net operating income £2,589.8m", subsize=9))
    y += 60
    out.append(line(340, y, 340, y + 22, "mf"))
    y += 26
    out.append(text(8, y + 10, "3  COSTS COME OUT FIRST", 10, NAVY, weight=700)[0])
    out.append(box(40, y + 18, 280, 58, "Compensation £1,138.5m", "#F9E7E7", HARD, INK, 12, 700, sub="about 44% of adjusted income [Inferred]. Pay for fund managers, sales, operations", subsize=9))
    out.append(box(360, y + 18, 280, 58, "Non-compensation £694.7m", "#F9E7E7", HARD, INK, 12, 700, sub="technology, data, premises, outsourcing (UST), marketing", subsize=9))
    out.append(text(340, y + 94, "Adjusted operating expenses £1,833.2m (flat). Adjusted cost:income ratio 71% (FY24 75%; H1 2026 68%) [S70, S71]", 9.5, INK2, "middle")[0])
    y += 102
    out.append(line(340, y, 340, y + 20, "mf"))
    y += 24
    out.append(text(8, y + 10, "4  WHAT IS LEFT", 10, NAVY, weight=700)[0])
    out.append(box(170, y + 18, 340, 50, "Adjusted operating profit £756.6m (+25%)", EASY, EASY, "#fff", 13, 700,
                   sub="Statutory profit before tax £673.8m after £152.5m transformation costs and a £113.3m SPW gain", subsize=9, subcol="#E8F4EE"))
    y += 70
    out.append(line(280, y, 170, y + 26, "mf"))
    out.append(line(400, y, 510, y + 26, "mf"))
    y += 28
    out.append(text(8, y + 10, "5  WHERE PROFIT GOES", 10, NAVY, weight=700)[0])
    out.append(box(20, y + 18, 300, 62, "Dividends paid in 2025: £335.8m", ACC_L, ACC, INK, 12, 700,
                   sub="21.5p a share. About 44% (roughly £149m, estimate) to the Schroder family's Principal Shareholder Group [Inferred]; the rest to public shareholders", subsize=9))
    out.append(box(360, y + 18, 300, 62, "Retained and reinvested", ACC_L, ACC, INK, 12, 700,
                   sub="e.g. up to £500m seed and co-investment for Schroders Capital; growth hires in Client Group and Wealth", subsize=9))
    y += 90
    out.append(box(20, y, 640, 44, "From 1 Oct 2026 the shareholder layer changes: Nuveen (TIAA) owns 100% after paying 590p cash plus up to 22p of dividends per share, about £9.9bn [S75, S76]. The family receives roughly £4.2bn to £4.4bn [Inferred] [S77].", OPI, OPI, "#fff", 10, 600))
    y += 52
    save("moneyflow", f'<figure class="fig-full" id="fig-moneyflow">{svg(W, y, "".join(out))}<figcaption><b>Figure #.</b> How money flows through Schroders, from client capital to dividends. Revenue by business sums to the group net operating revenue. Colours: Public Markets blue, private markets purple, Wealth green (40bp excluding adviser fees; Cazenove 48bp). Estimates are labelled. Sources: FY25 results [S71], AR 2025 [S72], H1 2026 [S70], deal documents [S75, S76, S77].</figcaption></figure>')


def opmodel():
    out = [arrow_defs("om")]
    layers = [("CLIENTS AND OWNERS OF CAPITAL", "Pensions, insurers, official institutions, wealth intermediaries, families, charities. 47% UK, 25% APAC, 16% EMEA, 12% Americas by AUM [S72]", WASH, INK),
              ("CLIENT GROUP (the client-facing centre)", "Sales, Client Service, Product, Marketing across all regions. Value Proposition | Sales Activation | Delivery [S306, S263]", S[1], "#fff"),
              ("THE BUSINESSES (front line)", "Public Markets (9 leading capabilities) | Schroders Capital (private markets) | Wealth Management (Cazenove Capital)", NAVY, "#fff"),
              ("CORPORATE CENTRE AND PLATFORM", "Technology, Operations (with UST), Finance, Risk & Compliance, People & Culture, Legal, Internal Audit, Tax [S72]", "#4A5A75", "#fff"),
              ("OWNERSHIP", "Until 30 Sep 2026: listed plc, family 44.27%. From 1 Oct 2026: Nuveen (TIAA) [S72, S75]", OPI, "#fff")]
    y = 6
    for i, (t, sub, col, tc) in enumerate(layers):
        out.append(box(140, y, 400, 56, t, col, col if col != WASH else LINE, tc, 12, 700, sub=sub, subsize=9.5, subcol=tc if tc == "#fff" else INK2))
        y += 72
    flows = [("mandates, money", "service, reporting", 62), ("client insight, demand", "propositions, products", 134),
             ("systems, data, control", "fees, requirements", 206), ("capital, oversight", "profits, dividends", 278)]
    for l, r, yy in flows:
        out.append(line(130, yy, 130, yy + 16, "om", S[0]))
        out.append(text(124, yy + 12, l, 8.5, S[0], "end")[0])
        out.append(line(550, yy + 16, 550, yy, "om", ACC, accent=True))
        out.append(text(556, yy + 12, r, 8.5, ACC)[0])
    save("opmodel", figure(svg(680, y, "".join(out)),
        "Schroders' operating model as five layers, and what flows between them (blue down, orange up). Layer names follow the firm's own wording in the annual report and ExCo page [S72, S306]; the arrows are the author's reading [Inferred]."))


def central_vs_embedded():
    out = [arrow_defs("ce")]
    out.append(text(165, 16, "A. Sales inside each business (common model)", 11, NAVY, "middle", 700)[0])
    out.append(text(510, 16, "B. One central Client Group (Schroders)", 11, NAVY, "middle", 700)[0])
    # left
    for i, b in enumerate(["Public Markets", "Private Markets", "Wealth"]):
        x = 10 + i * 108
        out.append(box(x, 30, 100, 40, b, NAVY, NAVY, "#fff", 10, 700))
        out.append(box(x, 84, 100, 36, "own sales + marketing", S[1], S[1], "#fff", 9))
        out.append(line(x + 50, 70, x + 50, 82, "ce"))
        out.append(line(x + 50, 120, 165, 176, "ce", HARD, 1.2))
    out.append(box(95, 178, 140, 40, "Client (pension scheme)", WASH, LINE, INK, 10, 700))
    out.append(text(165, 238, "3 teams call the same CIO", 10, HARD, "middle", 700)[0])
    out.append(text(165, 254, "3 product shelves, 3 CRMs", 9.5, INK2, "middle")[0])
    # right
    for i, b in enumerate(["Public Markets", "Private Markets", "Wealth"]):
        x = 355 + i * 108
        out.append(box(x, 30, 100, 40, b, NAVY, NAVY, "#fff", 10, 700))
        out.append(line(x + 50, 70, 510, 90, "ce"))
    out.append(box(400, 92, 220, 40, "Client Group", S[1], S[1], "#fff", 12, 700, sub="fewer core propositions", subsize=9, subcol="#fff"))
    out.append(line(510, 132, 510, 176, "ce", EASY, 1.6))
    out.append(box(440, 178, 140, 40, "Client (pension scheme)", WASH, LINE, INK, 10, 700))
    out.append(text(510, 238, "1 relationship owner", 10, EASY, "middle", 700)[0])
    out.append(text(510, 254, "shared CRM, data, marketing", 9.5, INK2, "middle")[0])
    out.append(f'<line x1="340" y1="24" x2="340" y2="258" stroke="{LINE}" stroke-dasharray="4 3"/>')
    out.append(text(340, 280, "Exception Schroders itself makes: a dedicated 40-person Schroders Capital business development team for private markets [S71].", 9.5, OPI, "middle", 600)[0])
    save("central_vs_embedded", figure(svg(680, 290, "".join(out)),
        "Two ways to organise selling. Schroders chose a central Client Group and in 2025 refocused it on \"fewer core propositions\" [S72]. The contrast is the author's illustration [Inferred]."))


def unit_anatomy():
    out = [arrow_defs("ua")]
    out.append(f'<circle cx="340" cy="150" r="78" fill="{NAVY}"/>')
    out.append(text(340, 132, "One capability", 12, "#fff", "middle", 700)[0])
    out.append(text(340, 150, "e.g. Global Credit", 11, "#DDE4EF", "middle")[0])
    out.append(text(340, 170, "PMs, analysts, traders", 9.5, "#DDE4EF", "middle")[0])
    parts = [("Client Group: Value Proposition", "which products, which share classes, pricing, competitor view", 90, 36, S[1]),
             ("Client Group: Sales Activation", "clients, consultants, fund selectors, events", 590, 36, S[1]),
             ("Client Group: Delivery", "CRM, data, sales enablement tools", 590, 264, S[1]),
             ("Risk & Compliance", "limits, approvals, financial promotions", 90, 264, HARD),
             ("Operations and Technology", "trading, fund accounting, reporting (partly via UST)", 90, 150, "#4A5A75"),
             ("Economics & research", "house views, Global Investor Insights Survey", 590, 150, S[2])]
    for t, sub, x, y, col in parts:
        out.append(box(x - 85, y - 26, 170, 52, t, "#fff", col, INK, 10, 700, sub=sub, subsize=8.5, subcol=INK2, sw=1.8))
        dx, dy = 340 - x, 150 - y
        d = (dx * dx + dy * dy) ** 0.5
        out.append(line(f"{x + dx/d*88:.0f}", f"{y + dy/d*30:.0f}", f"{340 - dx/d*82:.0f}", f"{150 - dy/d*82:.0f}", "ua", col, 1.3))
    save("unit_anatomy", figure(svg(680, 300, "".join(out)),
        "Anatomy of one front-line investment capability and what it draws from the centre. Functions from the AR 2025 and the Client Group JD [S72, S263]; the example capability and the arrows are illustrative [Inferred]."))


def growth():
    rows = [("2013", 262.9, "Group"), ("2014", 300.0, "Group"), ("2019", 500.2, "ex JVs"), ("2020", 574.4, "ex JVs"),
            ("2021", 731.6, "incl JVs"), ("2022", 737.5, "incl JVs"), ("2023", 750.6, "incl JVs"), ("2024", 778.7, "incl JVs"),
            ("2025", 823.7, "incl JVs"), ("Jun 2026", 867.8, "incl JVs")]
    out = []
    bw, gap, base, hmax = 52, 12, 250, 200
    out.append(text(8, 14, "AUM, £bn, year end (bars change colour where the reporting basis changes)", 10.5, NAVY, weight=700)[0])
    for i, (yr, v, basis) in enumerate(rows):
        x = 20 + i * (bw + gap)
        h = hmax * v / 900
        col = {"Group": "#6B7A8F", "ex JVs": S[2], "incl JVs": S[0]}[basis]
        out.append(f'<rect x="{x}" y="{base - h:.1f}" width="{bw}" height="{h:.1f}" rx="3" fill="{col}"/>')
        out.append(text(x + bw / 2, base - h - 5, f"{v:,.0f}", 9.5, INK, "middle", 600)[0])
        out.append(text(x + bw / 2, base + 14, yr, 9.5, INK2, "middle")[0])
    out.append(line(14, base, 666, base, "g", INK2, 1, arrow=False))
    out.append(text(8, base + 34, "Grey: group AUM (2013-14) [S100]. Green: excluding JVs (2019-20) [S98, snippet]. Blue: including JVs (2021 on) [S99, S101, S71, S70]. 2015 to 2018 not verified, so not shown.", 8.5, MUTED)[0])
    # staff panel
    y0 = base + 58
    out.append(text(8, y0, "Employees (different bases, not a continuous series)", 10.5, NAVY, weight=700)[0])
    staff = [("2021 year end", 5750), ("2022 year end", 6434), ("2024 avg", 6385), ("2025 avg", 6110), ("Web, Sep 2026", 5419)]
    for i, (l, v) in enumerate(staff):
        x = 20 + i * 130
        w = 110 * v / 7000
        out.append(f'<rect x="{x}" y="{y0+12}" width="{w:.0f}" height="18" rx="3" fill="{S[3]}"/>')
        out.append(text(x, y0 + 46, f"{v:,}", 11, INK, weight=700)[0])
        out.append(text(x, y0 + 60, l, 9, INK2)[0])
    out.append(text(8, y0 + 80, "Sources: [S99] 2021-22; [S73] 2024-25 monthly averages; [S108] website figure, basis unstated. The internship advert says around 5,500 people in 36 locations [S263].", 8.5, MUTED)[0])
    save("growth", figure(svg(680, y0 + 88, "".join(out)),
        "Schroders' growth: assets more than tripled from 2013 to mid-2026 while headcount has recently fallen. Bases differ and are colour-coded [Confirmed] except where marked."))


def margins():
    rows = [("Schroders Capital", 57), ("Cazenove & other Wealth", 48), ("Equities", 45), ("Fixed income", 34), ("Multi-asset", 24), ("Benchmark", 21), ("Core solutions", 6)]
    cols = [S[3], S[2], S[0], S[0], S[0], S[2], S[0]]
    body, h = hbar(rows, label_w=180, unit="bp", colors=cols, val_fmt="{:.0f}")
    out = body.replace("</svg>", "")
    extra = text(8, h + 14, "Revenue from £1bn of new money: Schroders Capital ≈ £5.7m a year; core solutions ≈ £0.6m [Inferred].", 10, OPI, weight=600)[0]
    extra += text(8, h + 30, "Source: Schroders annual results 2025, net operating revenue margins excluding performance fees [S71].", 8.5, MUTED)[0]
    s = svg(680, h + 38, body[body.index(">") + 1:-6] + extra)
    save("margins", figure(s, "Why the mix matters: fee margins by business, FY2025, in basis points [Confirmed]. This is the economic logic behind reinvesting in private markets and wealth [S71]."))


def boundary():
    out = []
    cols = [("SHARED FREELY", EASY, ["Approved fund performance and factsheets", "House economic views and published insights", "Brand, templates, approved pitch material", "CRM activity (who met whom, when)", "Product shelf and share-class data"]),
            ("SHARED WITH CARE", MED, ["Client holdings and mandates: need-to-know only", "Pipeline and fee negotiations", "Unapproved drafts (internal only until signed off)", "Wealth clients' personal data (Cazenove)", "Nuveen integration plans (as disclosed)"]),
            ("NEVER SHARED", HARD, ["Inside information about listed companies (UK MAR)", "One client's confidential data with another client", "Portfolio trades before they happen", "Personal data outside approved systems (UK GDPR)", "Anything that would mislead a client (COBS 4)"])]
    for i, (t, col, items) in enumerate(cols):
        x = 6 + i * 226
        out.append(f'<rect x="{x}" y="6" width="218" height="214" rx="4" fill="#fff" stroke="{col}" stroke-width="2"/>')
        out.append(f'<rect x="{x}" y="6" width="218" height="28" rx="4" fill="{col}"/>')
        out.append(text(x + 109, 25, t, 11.5, "#fff", "middle", 700)[0])
        for j, it in enumerate(items):
            out.append(text(x + 10, 54 + j * 34, "• " + it, 9.5, INK, width=40)[0])
    save("boundary", figure(svg(680, 226, "".join(out)),
        "The boundaries around Client Group information: what is shared, what is shared with care, and what never crosses. Rules from UK MAR, UK GDPR and COBS 4 [S402, S403, S401]; the grouping is the author's [Inferred]."))


def spectrum():
    axes = [("Active only", "Passive at scale", [("Schroders", 0.08), ("Jupiter", 0.02), ("Amundi", 0.55), ("L&G", 0.8), ("BlackRock", 0.92)]),
            ("Public markets only", "Large private markets", [("Jupiter", 0.05), ("Schroders", 0.4), ("M&G", 0.5), ("L&G", 0.48), ("Nuveen+Schroders", 0.72)]),
            ("Pure asset manager", "Asset + wealth in one group", [("BlackRock", 0.05), ("Amundi", 0.15), ("aberdeen (platforms)", 0.55), ("Schroders (Cazenove)", 0.85)]),
            ("Widely held / listed", "Controlled owner", [("aberdeen", 0.05), ("M&G", 0.25), ("Amundi (Crédit Agricole)", 0.7), ("Fidelity Intl (family)", 0.95), ("Schroders from 1 Oct 26 (Nuveen)", 0.82)]),
            ("UK-centric", "Global", [("Jupiter", 0.12), ("aberdeen", 0.28), ("Schroders", 0.72), ("BlackRock", 0.97)]),
            ("Sales by channel", "Integrated client group", [("M&G", 0.1), ("Jupiter", 0.18), ("Janus Henderson", 0.45), ("Schroders", 0.9)])]
    out = []
    y = 10
    for l, r, pts in axes:
        out.append(text(8, y + 14, l, 9.5, INK2)[0])
        out.append(text(672, y + 14, r, 9.5, INK2, "end")[0])
        out.append(f'<line x1="60" y1="{y+28}" x2="620" y2="{y+28}" stroke="{LINE}" stroke-width="3" stroke-linecap="round"/>')
        placed = []
        for name, v in pts:
            x = 60 + 560 * v
            is_s = "Schroders" in name
            col = ACC if is_s else S[0]
            out.append(f'<circle cx="{x:.0f}" cy="{y+28}" r="{7 if is_s else 5}" fill="{col}" stroke="#fff" stroke-width="2"/>')
            lvl = sum(1 for px in placed if abs(px - x) < 95)
            ty = y + 46 + lvl * 12
            anchor = "middle" if 60 < x < 620 else ("start" if x <= 60 else "end")
            out.append(text(f"{x:.0f}", ty, name, 8.8, NAVY if is_s else INK, anchor, 700 if is_s else 400)[0])
            placed.append(x)
        y += 72
    save("spectrum", figure(svg(680, y + 4, "".join(out)),
        "Design choices on which firms sit at different ends. Positions are the author's judgement from the facts in Part 4 [Inferred]; Schroders in orange. Sources for the underlying facts: [S70, S130, S131, S132, S133, S136, S139]."))


def aum_staff():
    rows = [("BlackRock", 456), ("Amundi", 409), ("Janus Henderson", 178), ("Jupiter (pre-CCLA staff)", 167), ("Schroders", 152),
            ("aberdeen", 131), ("Ninety One", 128), ("M&G (incl. insurance)", 60)]
    cols = [S[0]] * 8
    cols[4] = ACC
    body, h = hbar(rows, label_w=190, unit="", colors=cols, val_fmt="£{:.0f}m", est={r[0] for r in rows})
    extra = text(8, h + 14, "AUM per employee, £m. All values are estimates: native AUM converted at an assumed £1 = $1.35 = €1.17, divided by the latest headcount found.", 9, INK2)[0]
    extra += text(8, h + 28, "Headcount bases differ (year-end vs average; group vs asset management). Sources: [S147, S137, S148, S120, S130, S131, S132, S134, S136, S138, S140].", 8.5, MUTED)[0]
    save("aum_staff", figure(svg(680, h + 36, body[body.index(">") + 1:-6] + extra),
        "Size against staffing: passive-heavy scale players run roughly 2.5 to 3 times the assets per employee of active managers. Schroders sits mid-pack. Estimates, labelled on the chart [Inferred]."))


def record():
    out = []
    out.append(text(8, 16, "A. Schroders: share of assets beating their comparator (internal, mostly gross of fees)", 10.5, NAVY, weight=700)[0])
    data = [("FY24", [70, 58, 76]), ("FY25", [71, 70, 73]), ("H1 26", [72, 71, 69])]
    for i, (p, vals) in enumerate(data):
        for j, v in enumerate(vals):
            x = 30 + i * 210 + j * 60
            h = 120 * v / 100
            out.append(f'<rect x="{x}" y="{160-h:.0f}" width="44" height="{h:.0f}" rx="3" fill="{[S[0], S[1], S[2]][j]}"/>')
            out.append(text(x + 22, 155 - h, f"{v}%", 10, INK, "middle", 700)[0])
            out.append(text(x + 22, 174, ["1y", "3y", "5y"][j], 9, INK2, "middle")[0])
        out.append(text(30 + i * 210 + 82, 192, p, 10.5, NAVY, "middle", 700)[0])
    out.append(line(20, 160, 660, 160, "r", INK2, 1, arrow=False))
    out.append(text(8, 212, "Source: FY25 results [S71], H1 2026 [S70]. Excludes £86.9bn of assets; 70% measured vs benchmark, rest vs peers, absolute or cash targets [S71].", 8.5, MUTED)[0])
    out.append(text(8, 240, "B. Industry: share of European active equity funds that survived and beat passive peers (Morningstar)", 10.5, NAVY, weight=700)[0])
    ind = [("1 year (2024 data)", 29.1), ("10 years (2024 data)", 14.2)]
    for i, (l, v) in enumerate(ind):
        y = 254 + i * 28
        out.append(text(170, y + 14, l, 10, INK, "end")[0])
        out.append(f'<rect x="180" y="{y}" width="{v*4.5:.0f}" height="20" rx="3" fill="#6B7A8F"/>')
        out.append(text(186 + v * 4.5, y + 14, f"{v}%", 10, INK2)[0])
    out.append(text(8, 326, "Source: Morningstar European Active/Passive Barometer via DIY Investor [S319]. Not like-for-like with panel A: different measure, period and universe.", 8.5, MUTED)[0])
    save("record", figure(svg(680, 334, "".join(out)),
        "The client's view of the record. Panel A is Schroders' own measure; panel B is the industry base rate a sceptical client will quote. Do not compare the bars directly; use them to hold both sides of the argument."))


def flows_timeline():
    out = []
    out.append(text(8, 16, "Net new business excluding JVs, £bn", 10.5, NAVY, weight=700)[0])
    pts = [("FY24", -10.8), ("H1 25", 4.5), ("FY25", 11.2), ("H1 26", -8.3)]
    zero = 110
    for i, (l, v) in enumerate(pts):
        x = 60 + i * 140
        h = abs(v) * 6
        col = EASY if v > 0 else HARD
        y = zero - h if v > 0 else zero
        out.append(f'<rect x="{x}" y="{y:.0f}" width="70" height="{h:.0f}" rx="3" fill="{col}"/>')
        out.append(text(x + 35, (y - 5) if v > 0 else (y + h + 14), f"{v:+.1f}", 11, INK, "middle", 700)[0])
        out.append(text(x + 35, zero - 6 if v < 0 else zero + 15, l, 10, INK2, "middle", 600)[0])
    out.append(f'<line x1="40" y1="{zero}" x2="600" y2="{zero}" stroke="{INK2}" stroke-width="1"/>')
    out.append(text(560, 150, "H1 26 includes one", 9, HARD)[0])
    out.append(text(560, 162, "£6.6bn low-margin", 9, HARD)[0])
    out.append(text(560, 174, "redemption", 9, HARD)[0])
    out.append(text(8, 222, "Adjusted cost:income ratio", 10.5, NAVY, weight=700)[0])
    ci = [("FY24", 75), ("FY25", 71), ("H1 26", 68)]
    for i, (l, v) in enumerate(ci):
        x = 60 + i * 200
        out.append(box(x, 232, 150, 44, f"{v}%", WASH, LINE, NAVY, 18, 700, sub=l, subsize=9, subcol=INK2))
    out.append(text(8, 296, "Target below 70% met within 18 months. Sources: FY25 results [S71]; H1 2026 results [S70]; H1 25 comparative from [S70].", 8.5, MUTED)[0])
    save("flows_timeline", figure(svg(680, 304, "".join(out)),
        "Revenue stability: flows swing year to year while the cost base has been cut. Separate panels, not a dual axis [Confirmed]."))


def exco():
    out = [arrow_defs("ex")]
    out.append(box(250, 6, 180, 42, "Richard Oldfield", NAVY, NAVY, "#fff", 12, 700, sub="Group CEO (from Nov 2024)", subsize=9, subcol="#DDE4EF"))
    groups = [("Businesses", S[0], [("Johanna Kyrklund", "Group CIO; CEO Public Markets"), ("Georg Wunderlin", "CEO, Schroders Capital"), ("Oliver Gregson", "CEO, Wealth Management")]),
              ("Client", S[1], [("Matt Oomen", "Global Head of Client Group"), ("Karine Szenberg", "Executive Vice Chair, strategic partnerships")]),
              ("Centre", "#4A5A75", [("Meagen Burnett", "CFO; ops, tech, transformation"), ("Sonia Jenkins", "Chief People Officer"), ("Neil Tomlinson", "General Counsel"), ("Ed Houghton", "Strategy & Investor Engagement")])]
    x = 6
    widths = [208, 208, 238]
    for (g, col, ms), w in zip(groups, widths):
        out.append(line(340, 48, x + w / 2, 70, "ex", MUTED, 1))
        out.append(f'<rect x="{x}" y="72" width="{w}" height="24" rx="3" fill="{col}"/>')
        out.append(text(x + w / 2, 88, g.upper(), 10.5, "#fff", "middle", 700)[0])
        for j, (n, t) in enumerate(ms):
            out.append(box(x, 102 + j * 50, w, 44, n, "#fff", col, INK, 11, 700, sub=t, subsize=9, subcol=INK2, sw=1.5))
        x += w + 7
    out.append(text(340, 318, "Client Group below Oomen (reported): Head of UK Phil Middleton; Head of Client Group Europe Patrick Schwyzer; Asia Gopi Mirchandani; Strategy Execution & Delivery Ed Mitchell [S269, S93, S271].", 9, INK2, "middle", width=120)[0])
    save("exco", figure(svg(680, 346, "".join(out)),
        "The centre as the firm publishes it: the Group Executive Committee, grouped by the author into businesses, client and centre. Names and titles from the ExCo page as read on 29 Sep 2026 [S306]; groupings [Inferred]. Post-completion changes under Nuveen not yet published."))


def nuveen_timeline():
    ev = [(0, "12 Feb 2026", "Offer announced: 590p + up to 22p; £9.9bn", NAVY, 0),
          (1.8, "Apr 2026", "Shareholders approve (over 99%)", NAVY, 3),
          (7.3, "22 Sep to 2 Oct 2026", "Approvals; court sanction 29 Sep; effective 1 Oct; delisted 2 Oct", HARD, 1),
          (16, "Jun to Aug 2027", "Your internship", S[2], 3),
          (19.6, "Oct 2027", "Earliest end of 12-month standalone period", OPI, 0),
          (31.6, "Oct 2028", "End of 2-year no-material-job-cuts intention", OPI, 4)]
    out = []
    x0, x1, tmax = 20, 660, 32
    out.append(f'<line x1="{x0}" y1="120" x2="{x1}" y2="120" stroke="{NAVY}" stroke-width="3"/>')
    out.append(f'<rect x="{x0 + (x1-x0)*7.65/tmax:.0f}" y="112" width="{(x1-x0)*12/tmax:.0f}" height="16" fill="{OPI}" fill-opacity="0.18"/>')
    out.append(text(x0 + (x1 - x0) * 13.6 / tmax, 108, "standalone for at least 12 months", 9, OPI, "middle", 600)[0])
    levels = {0: 22, 1: 62, 3: 160, 4: 200}
    for t, d, lab, col, lv in ev:
        x = x0 + (x1 - x0) * t / tmax
        up = lv < 2
        ly = levels[lv]
        out.append(f'<circle cx="{x:.0f}" cy="120" r="6" fill="{col}" stroke="#fff" stroke-width="2"/>')
        out.append(f'<line x1="{x:.0f}" y1="{120 + (-8 if up else 8)}" x2="{x:.0f}" y2="{ly + (18 if up else -12)}" stroke="{col}" stroke-width="1"/>')
        anchor = "start" if x < 450 else "end"
        out.append(text(f"{x:.0f}", ly, d, 10, col, anchor, 700)[0])
        out.append(text(f"{x:.0f}", ly + 13, lab, 9, INK, anchor)[0])
    save("nuveen", figure(svg(680, 226, "".join(out)),
        "The Nuveen deal timeline and where the internship falls. Dates from the court sanction RNS and deal announcements [S75, S76, S77, S309]. The standalone period and employment intention are stated intentions, not guarantees."))


if __name__ == "__main__":
    moneyflow(); opmodel(); central_vs_embedded(); unit_anatomy(); growth(); margins(); boundary(); spectrum()
    aum_staff(); record(); flows_timeline(); exco(); nuveen_timeline()
    print("firm figs done")
