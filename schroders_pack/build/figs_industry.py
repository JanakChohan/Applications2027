#!/usr/bin/env python3
"""Figures for Parts 5 and 6 (industry and regulation)."""
import os
from svglib import *

ROOT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(ROOT, "fragments")


def save(name, s):
    open(os.path.join(FR, f"fig_{name}.html"), "w").write(s)


def buyside_map():
    out = [arrow_defs("bm")]
    # Money owners on left, managers middle, markets right
    out.append(text(90, 18, "WHO OWNS THE MONEY", 9.5, MUTED, "middle", 700)[0])
    out.append(text(340, 18, "WHO RUNS IT (BUY SIDE)", 9.5, MUTED, "middle", 700)[0])
    out.append(text(590, 18, "WHERE IT GOES", 9.5, MUTED, "middle", 700)[0])
    owners = ["Pension schemes (DB, DC, LGPS)", "Insurers", "Sovereign funds and central banks", "Endowments, charities, family offices", "Individuals (via advisers, platforms, wealth managers)"]
    for i, o in enumerate(owners):
        out.append(box(8, 30 + i * 52, 164, 44, o, "#fff", S[0], INK, 10))
    mgrs = [("Asset manager", "fee as % of assets (bps)", NAVY), ("Wealth manager", "% of assets + planning fees", NAVY2),
            ("Hedge fund", "management + performance fee", "#4A5A75"), ("Private markets manager", "fee on commitments + carried interest", "#4A5A75")]
    for i, (m, sub, col) in enumerate(mgrs):
        out.append(box(250, 34 + i * 62, 180, 52, m, col, col, "#fff", 11.5, 700, sub=sub, subsize=9, subcol="#DDE4EF"))
    mk = ["Listed shares", "Bonds (gilts, corporate)", "Private companies, private credit", "Property and infrastructure", "Cash and money markets"]
    for i, m in enumerate(mk):
        out.append(box(510, 30 + i * 52, 164, 44, m, WASH, LINE, INK, 10))
    for i in range(5):
        out.append(line(174, 52 + i * 52, 246, 60 + min(i, 3) * 62, "bm", MUTED, 1))
    for i in range(4):
        out.append(line(432, 60 + i * 62, 506, 52 + i * 52 + (26 if i == 3 else 0), "bm", MUTED, 1))
    out.append(box(250, 292, 180, 44, "Investment bank (sell side)", "#fff", ACC, INK, 10.5, 700, sub="advises companies, trades, sells research to the buy side", subsize=8.5, dash="4 3"))
    out.append(path("M430,314 C470,314 480,290 506,280", "bm", ACC, 1.2, dash="4 3"))
    out.append(text(340, 356, "Schroders sits in the middle column: asset manager, wealth manager and private markets manager in one group.", 10, INK2, "middle")[0])
    save("buyside", figure(svg(680, 366, "".join(out)),
        "Who is who in investment. Owners hand money to managers, who invest it in markets. Fee models from the IA and industry sources [S150, S154]. Schroders' business mix from its annual report (see Part 2)."))


def uk_clients():
    rows = [("Overseas clients", 51, None), ("UK clients", 49, None)]
    out = []
    # two stacked 100% bars
    def stacked(y, segs, title):
        o = [text(8, y - 6, title, 10.5, NAVY, weight=700)[0]]
        x = 8
        for lab, v, col in segs:
            w = 664 * v / 100
            o.append(f'<rect x="{x:.1f}" y="{y}" width="{w-2:.1f}" height="26" rx="3" fill="{col}"/>')
            if w > 60:
                o.append(text(x + 6, y + 17, f"{lab} {v}%", 10, "#fff", weight=600)[0])
            x += w
        return "".join(o)
    out.append(stacked(22, [("Overseas clients", 51, S[0]), ("UK clients", 49, "#6B7A8F")], "Who the UK industry manages money for (share of £10.0trn, end-2024)"))
    out.append(stacked(82, [("Institutional", 71, NAVY2), ("Retail", 28, S[1]), ("", 1, LINE)], "Institutional versus retail (share of AUM)"))
    out.append(stacked(142, [("Active (nearly two-thirds)", 65, S[2]), ("Index / passive", 35, "#6B7A8F")], "Active versus index (share of AUM; active is IA's 'nearly two-thirds', shown as 65%)"))
    out.append(stacked(202, [("Top 10 firms", 60, S[3]), ("Everyone else", 40, "#6B7A8F")], "Concentration: share of UK AUM run by the ten largest firms"))
    out.append(text(8, 250, "Source: Investment Association, Investment Management in the UK 2024-2025, data at end-2024, published Oct 2025 [S150]. Next edition (end-2025 data) not yet found.", 8.5, MUTED)[0])
    save("uk_clients", figure(svg(680, 258, "".join(out)),
        "The UK asset management industry in four bars. Figures are IA survey data at end-2024 [S150] [Confirmed]."))


def retail_flows():
    rows = [("Index trackers", 12.8), ("Money market funds", 6.9), ("Mixed asset", 4.5), ("Fixed income", 1.1),
            ("UK equity funds", -11.1), ("Active funds (all)", -15.1), ("Total UK retail", -2.3)]
    out = []
    zero = 400; scale = 12
    out.append(line(zero, 6, zero, 8 + len(rows) * 30, "rf", INK2, 1, arrow=False))
    for i, (lab, v) in enumerate(rows):
        y = 10 + i * 30
        w = abs(v) * scale
        col = S[2] if v > 0 else S[4]
        x = zero if v > 0 else zero - w
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="20" rx="3" fill="{col}"/>')
        out.append(text(150, y + 14, lab, 10.5, INK, "end", 600 if "Total" in lab else 400)[0])
        vs = f"{'+' if v > 0 else '-'}£{abs(v):.1f}bn"
        out.append(text(x + w + 5 if v > 0 else x - 5, y + 14, vs, 10, INK2, "start" if v > 0 else "end")[0])
    out.append(text(8, 232, "Categories overlap (UK equity and trackers both sit inside 'all funds'); read each bar on its own. Source: IA press release, 5 Feb 2026 [S152].", 8.5, MUTED)[0])
    save("retail_flows", figure(svg(680, 240, "".join(out)),
        "UK retail fund net flows in 2025: money went to trackers and cash-like funds and left active and UK equity funds [S152] [Confirmed]."))


def shift_map():
    out = [arrow_defs("sm")]
    out.append(f'<circle cx="340" cy="200" r="70" fill="{NAVY}"/>')
    out.append(text(340, 195, "An active asset", 12, "#fff", "middle", 700)[0])
    out.append(text(340, 212, "and wealth manager", 12, "#fff", "middle", 700)[0])
    forces = [
        ("Passive and fee compression", "UK margin 18% vs 31% in 2019 [S150]", "t", 120, 40),
        ("Buyer consolidation", "6 LGPS pools; £25bn DC megafunds [S183, S185]", "t", 560, 40),
        ("US scale players", "54% of UK AUM run by N. American groups [S150]", "t", 112, 190),
        ("Growth mostly from markets", ">80% of 2025 revenue growth [S154]", "t", 568, 190),
        ("Private markets for DC and wealth", "Mansion House Accord 10% by 2030 [S181]", "o", 120, 330),
        ("Retail investing push", "ISA reform Apr 2027; targeted support Apr 2026 [S187, S170]", "o", 560, 330),
        ("Active ETFs and active bonds", "European active ETFs tripled in 2 years [S159]", "o", 340, 380),
        ("AI cost reset", "25 to 35% cost cut potential [S154]", "o", 340, 22),
    ]
    for t, sub, kind, x, y in forces:
        col = HARD if kind == "t" else EASY
        fill = "#F9E7E7" if kind == "t" else "#E8F4EE"
        if t.startswith("AI"):
            col, fill = OPI, "#F4ECF8"
        out.append(box(x - 105, y - 24, 210, 48, t, fill, col, INK, 10.5, 700, sub=sub, subsize=8.5, subcol=INK2))
        # arrow toward centre
        dx, dy = 340 - x, 200 - y
        d = (dx * dx + dy * dy) ** 0.5
        sx, sy = x + dx / d * 60, y + dy / d * 32
        ex, ey = 340 - dx / d * 76, 200 - dy / d * 76
        out.append(line(f"{sx:.0f}", f"{sy:.0f}", f"{ex:.0f}", f"{ey:.0f}", "sm", col, 1.3))
    out.append(f'<rect x="8" y="418" width="12" height="12" fill="#F9E7E7" stroke="{HARD}"/>')
    out.append(text(26, 428, "Pressure (threat to revenue)", 9.5, INK2)[0])
    out.append(f'<rect x="210" y="418" width="12" height="12" fill="#E8F4EE" stroke="{EASY}"/>')
    out.append(text(228, 428, "Opportunity (new demand)", 9.5, INK2)[0])
    out.append(f'<rect x="400" y="418" width="12" height="12" fill="#F4ECF8" stroke="{OPI}"/>')
    out.append(text(418, 428, "Both (cost lever, but everyone gets it)", 9.5, INK2)[0])
    save("shift_map", figure(svg(680, 466, '<g transform="translate(0,26)">' + "".join(out) + '</g>'),
        "The industry shift map: eight forces acting on a firm like Schroders, 2025 to 2027. Classification as threat or opportunity is the author's [Inferred]; each figure is sourced in the box."))


def views():
    items = [("1. Barbell", "Passive giants and private-markets specialists win. Mid-sized active houses merge or niche.", "Evidence: top-10 share 60%, margins 18% [S150]; institutional fees -3% a year [S154].", HARD),
             ("2. Great convergence", "Public and private markets blend and move into wealth and DC pensions.", "Evidence: retail drove 61% of 2020-25 growth [S154]; Mansion House 10% target [S181].", S[0]),
             ("3. Active rebound, private caution", "Private markets over-sold; active bonds and active ETFs recover.", "Evidence: BoE warns on retail fund redemptions [S196]; 81% of fund selectors see bigger active bond role [S194].", S[2]),
             ("4. AI operating reset", "Lower cost-to-serve; one salesperson covers 3 to 5 times more clients.", "Evidence: BCG 2026 [S154]. Winners personalise at scale.", OPI)]
    out = []
    for i, (t, a, ev, col) in enumerate(items):
        x, y = 6 + (i % 2) * 338, 6 + (i // 2) * 118
        out.append(f'<rect x="{x}" y="{y}" width="330" height="110" rx="4" fill="#fff" stroke="{col}" stroke-width="1.6"/>')
        out.append(f'<rect x="{x}" y="{y}" width="330" height="26" rx="4" fill="{col}"/>')
        out.append(text(x + 10, y + 18, t, 12, "#fff", weight=700)[0])
        out.append(text(x + 10, y + 44, a, 10.5, INK, width=58)[0])
        out.append(text(x + 10, y + 80, ev, 9, INK2, width=64, italic=True)[0])
    out.append(text(340, 256, "Schroders, with public, private and wealth arms, is in effect betting on views 2 and 4 while defending against view 1 [Inferred].", 10, OPI, "middle", 600)[0])
    save("views", figure(svg(680, 266, "".join(out)),
        "Four competing views of the industry over the next three to five years. Views summarised by the author from the sources cited in each box."))


def reg_timeline():
    ev = [("31 Dec 2012", "RDR bans commission to advisers", "S177"),
          ("6 Apr 2014", "Platform rebate ban (PS13/1)", "S178"),
          ("3 Jan 2018", "MiFID II: target market, inducements", "S176"),
          ("10 Jun 2019", "CMA Order on investment consultants", "S179"),
          ("30 Sep 2019", "Assessment of Value begins", "S163"),
          ("31 Jul 2023", "Consumer Duty (open products)", "S161"),
          ("31 May 2024", "Anti-greenwashing rule", "S165"),
          ("31 Jul 2024", "SDR labels; Duty for closed products", "S165"),
          ("2 Dec 2024", "SDR naming and marketing rules", "S166"),
          ("13 May 2025", "Mansion House Accord", "S181"),
          ("6 Apr 2026", "Targeted support live; CCI optional", "S170"),
          ("29 Apr 2026", "Pension Schemes Act 2026", "S183"),
          ("29 Sep 2026", "YOU ARE HERE", ""),
          ("6 Apr 2027", "Cash ISA limit cut to £12,000", "S187"),
          ("8 Jun 2027", "CCI mandatory (replaces PRIIPs KID)", "S168"),
          ("14 Jun 2027", "YOUR INTERNSHIP STARTS (to 20 Aug)", "")]
    out = []
    n = len(ev)
    y0 = 20
    out.append(f'<line x1="120" y1="{y0}" x2="120" y2="{y0 + (n-1)*34}" stroke="{NAVY}" stroke-width="3"/>')
    for i, (d, t, s_) in enumerate(ev):
        y = y0 + i * 34
        special = s_ == ""
        future = "2027" in d
        col = S[2] if special else (ACC if future else NAVY)
        out.append(f'<circle cx="120" cy="{y}" r="{8 if special else 6}" fill="{col}" stroke="#fff" stroke-width="2"/>')
        out.append(text(108, y + 4, d, 10.5, col, "end", 700)[0])
        out.append(text(134, y + 4, t, 10.5, col if special else INK, weight=700 if special else 400)[0])
        if s_:
            out.append(text(672, y + 4, f"[{s_}]", 9, S[0], "end")[0])
    save("reg_timeline", figure(svg(680, y0 + n * 34 + 4, "".join(out)),
        "Regulation timeline for UK fund distribution. Dates checked against FCA and government sources where marked [Confirmed]; the MiFID II date is general knowledge [Reported]. Orange = still to come. CCI goes mandatory one week before the internship starts."))


if __name__ == "__main__":
    buyside_map(); uk_clients(); retail_flows(); shift_map(); views(); reg_timeline()
    print("industry figs done")
