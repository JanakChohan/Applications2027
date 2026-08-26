# -*- coding: utf-8 -*-
"""Builds the Pictet business guide: HTML -> (chromium) -> PDF."""
import os, html as _h

BASE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- palette ---
# Categorical slots: validated default palette (dataviz skill), light mode,
# used in fixed slot order and never cycled.
S1, S2, S3, S4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
S5, S6, S7, S8 = "#e87ba4", "#008300", "#4a3aa7", "#e34948"
CAT = [S1, S2, S3, S4, S5, S6, S7, S8]
# Sequential blue ramp (one hue, light -> dark)
B100, B200, B300, B450, B550, B650, B700 = (
    "#cde2fb", "#9ec5f4", "#6da7ec", "#2a78d6", "#1c5cab", "#104281", "#0d366b")

INK, INK2, INK3 = "#12110f", "#54524c", "#8a877e"
SURF, PANEL, RULE = "#ffffff", "#f7f6f2", "#e5e1d8"
NAVY = "#12324e"          # document chrome only, never a data series
GRID = "#e8e5dd"


def esc(t):
    return _h.escape(str(t))


def fmt(n, dp=0):
    s = f"{n:,.{dp}f}"
    return s


# ------------------------------------------------------------- primitives ---
def svg_open(w, h, cls="fig"):
    return (f'<svg class="{cls}" viewBox="0 0 {w} {h}" width="100%" '
            f'role="img" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Inter, sans-serif">')


def txt(x, y, s, size=11, fill=INK2, weight=400, anchor="start", ls="0"):
    return (f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'font-weight="{weight}" text-anchor="{anchor}" '
            f'letter-spacing="{ls}">{esc(s)}</text>')


def rrect(x, y, w, h, fill, r=3, extra=""):
    w = max(w, 0.01)
    return (f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" '
            f'rx="{r}" fill="{fill}" {extra}/>')


def bar_h(x, y, w, h, fill, r=4):
    """Horizontal bar: square at the baseline (left), 4px rounded data-end."""
    w = max(w, 0.01)
    if w <= r:
        return rrect(x, y, w, h, fill, r=0)
    return (f'<path d="M{x:.2f} {y:.2f} H{x+w-r:.2f} a{r} {r} 0 0 1 {r} {r} '
            f'V{y+h-r:.2f} a{r} {r} 0 0 1 -{r} {r} H{x:.2f} Z" fill="{fill}"/>')


def bar_v(x, y, w, h, fill, r=4):
    """Vertical column: square at the baseline (bottom), rounded top."""
    h = max(h, 0.01)
    if h <= r:
        return rrect(x, y, w, h, fill, r=0)
    return (f'<path d="M{x:.2f} {y+r:.2f} a{r} {r} 0 0 1 {r} -{r} '
            f'H{x+w-r:.2f} a{r} {r} 0 0 1 {r} {r} V{y+h:.2f} H{x:.2f} Z" '
            f'fill="{fill}"/>')


def gridline(x1, y, x2, w=1):
    return (f'<line x1="{x1}" y1="{y:.2f}" x2="{x2}" y2="{y:.2f}" '
            f'stroke="{GRID}" stroke-width="{w}"/>')


ARROW_DEFS = f'''<defs>
<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7"
 markerHeight="7" orient="auto-start-reverse">
 <path d="M0 0 L10 5 L0 10 z" fill="{INK3}"/></marker>
<marker id="ahb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7"
 markerHeight="7" orient="auto-start-reverse">
 <path d="M0 0 L10 5 L0 10 z" fill="{S1}"/></marker>
<marker id="aho" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7"
 markerHeight="7" orient="auto-start-reverse">
 <path d="M0 0 L10 5 L0 10 z" fill="{S2}"/></marker>
<marker id="aha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7"
 markerHeight="7" orient="auto-start-reverse">
 <path d="M0 0 L10 5 L0 10 z" fill="{S3}"/></marker>
</defs>'''


def arrow(x1, y1, x2, y2, color=INK3, marker="ah", w=1.6, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="{w}"{d} marker-end="url(#{marker})"/>')


def wrap(s, n):
    words, lines, cur = s.split(), [], ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if len(t) <= n:
            cur = t
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def box(x, y, w, h, title, body, fill=PANEL, stroke=RULE, tcol=INK,
        bcol=INK2, ts=11.5, bs=9.5, r=6, chars=None, accent=None):
    """Rounded label box with a title line and wrapped body text."""
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
         f'fill="{fill}" stroke="{stroke}" stroke-width="1"/>']
    if accent:
        o.append(f'<path d="M{x} {y+r} a{r} {r} 0 0 1 {r} -{r} H{x+r+2} '
                 f'V{y+h} H{x+r} a{r} {r} 0 0 1 -{r} -{r} Z" fill="{accent}"/>')
    cx = x + w / 2
    chars = chars or int(w / (bs * 0.52))
    ty = y + (18 if body else h / 2 + 4)
    if title:
        o.append(txt(cx, ty, title, ts, tcol, 600, "middle"))
    yy = ty + 14
    for ln in wrap(body, chars) if body else []:
        o.append(txt(cx, yy, ln, bs, bcol, 400, "middle"))
        yy += 12
    return "".join(o)


# ============================================================== CHARTS =====
# Fixed identity colours for the four business lines - held constant in every
# figure in this document so colour always means the same thing.
C_WM, C_AM, C_AA, C_AS = S1, S2, S3, S4


def chart_aum_history():
    data = [(2020, 609), (2021, 698), (2022, 612), (2023, 686),
            (2024, 724), (2025, 757)]
    W, H = 700, 300
    L, R, T, B = 46, 16, 34, 46
    pw, ph = W - L - R, H - T - B
    mx = 800
    o = [svg_open(W, H)]
    for v in range(0, 801, 200):
        y = T + ph - v / mx * ph
        o.append(gridline(L, y, W - R))
        o.append(txt(L - 8, y + 3.5, fmt(v), 9, INK3, 400, "end"))
    n = len(data)
    slot = pw / n
    bw = min(58, slot * 0.56)
    for i, (yr, v) in enumerate(data):
        cx = L + slot * (i + .5)
        bh = v / mx * ph
        col = S1 if yr == 2025 else B300
        o.append(bar_v(cx - bw / 2, T + ph - bh, bw, bh, col))
        o.append(txt(cx, T + ph - bh - 8, fmt(v), 11.5,
                     INK if yr == 2025 else INK2, 600, "middle"))
        o.append(txt(cx, T + ph + 18, str(yr), 10, INK2, 500, "middle"))
    o.append(f'<line x1="{L}" y1="{T+ph}" x2="{W-R}" y2="{T+ph}" '
             f'stroke="{RULE}" stroke-width="1"/>')
    o.append(txt(L, 14, "CHF billion, assets under management or custody, "
                        "31 December", 9.5, INK3))
    o.append(txt(L, T + ph + 38,
                 "2022 is the drawdown year - markets fell, not clients. "
                 "Net new money stayed positive throughout.", 9, INK3))
    o.append("</svg>")
    return "".join(o)


def chart_business_lines():
    rows = [("Wealth Management", 285, C_WM, "AUM"),
            ("Asset Management", 267, C_AM, "AUM"),
            ("Asset Services", 256, C_AS, "assets under custody, external only"),
            ("Alternative Advisors", 36, C_AA,
             "already counted inside WM and AM")]
    W = 700
    rowh, gap = 46, 12
    T, B = 30, 44
    L, R = 158, 16
    H = T + len(rows) * (rowh + gap) - gap + B
    pw = W - L - R
    mx = 300
    o = [svg_open(W, H)]
    for v in (0, 100, 200, 300):
        x = L + v / mx * pw
        o.append(f'<line x1="{x}" y1="{T-6}" x2="{x}" y2="{T+len(rows)*(rowh+gap)-gap}" '
                 f'stroke="{GRID}" stroke-width="1"/>')
        o.append(txt(x, T - 12, fmt(v), 9, INK3, 400, "middle"))
    y = T
    for name, v, col, note in rows:
        bw = v / mx * pw
        o.append(bar_h(L, y + 6, bw, 22, col))
        o.append(txt(L - 10, y + 17, name, 11, INK, 600, "end"))
        o.append(txt(L - 10, y + 30, note, 8.5, INK3, 400, "end"))
        o.append(txt(L + bw + 8, y + 21, f"CHF {v}bn", 11, INK, 600))
        y += rowh + gap
    o.append(txt(L, 14, "CHF billion", 9.5, INK3))
    o.append(txt(0, H - 24,
                 "These do not add to CHF 757bn. Alternative Advisors' assets sit "
                 "inside the other two lines, and CHF 202bn of group", 9, INK3))
    o.append(txt(0, H - 12,
                 "assets are double-counted (e.g. a Pictet fund held for a "
                 "Pictet wealth client). See page 'The 757 question'.", 9, INK3))
    o.append("</svg>")
    return "".join(o)


def chart_revenue_mix():
    rows = [("Commissions and services (net)", 2565.8, S1,
             "management fees, advisory fees, custody, fund fees, brokerage"),
            ("Net interest income", 417.6, S2,
             "the spread earned on client deposits and lending"),
            ("Trading and fair value", 216.7, S3,
             "client FX and securities execution, not proprietary risk"),
            ("Other ordinary income", 6.6, S4, "real estate, participations")]
    tot = sum(r[1] for r in rows)
    W = 700
    T, B, L, R = 58, 30, 0, 0
    rowh = 56
    H = T + len(rows) * rowh + B
    o = [svg_open(W, H)]
    # 100% stacked reference bar
    x = 0
    for name, v, col, _ in rows:
        seg = v / tot * W
        o.append(rrect(x, 12, max(seg - 2, 1), 22, col, r=3))
        if seg > 60:
            o.append(txt(x + seg / 2 - 1, 27, f"{v/tot*100:.0f}%", 11,
                         "#ffffff", 700, "middle"))
        x += seg
    o.append(txt(0, 50, "Share of CHF 3,206.8m operating income, 2025",
                 9.5, INK3))
    y = T
    for name, v, col, note in rows:
        o.append(rrect(0, y + 4, 4, 34, col, r=2))
        o.append(txt(14, y + 17, name, 11.5, INK, 600))
        o.append(txt(14, y + 32, note, 9.5, INK3))
        o.append(txt(W, y + 17, f"CHF {fmt(v,1)}m", 12, INK, 700, "end"))
        o.append(txt(W, y + 32, f"{v/tot*100:.1f}% of income", 9.5, INK3,
                     400, "end"))
        y += rowh
    o.append("</svg>")
    return "".join(o)


def chart_waterfall():
    steps = [("Operating\nincome", 3206.8, "total"),
             ("Personnel", -1614.5, "dec"),
             ("General &\nadmin", -694.1, "dec"),
             ("Depreciation", -39.4, "dec"),
             ("Provisions", -12.8, "dec"),
             ("Operating\nresult", 846.1, "total"),
             ("Tax", -178.8, "dec"),
             ("Consolidated\nprofit", 667.2, "total")]
    W, H = 700, 340
    L, R, T, B = 46, 8, 26, 62
    pw, ph = W - L - R, H - T - B
    mx = 3400
    o = [svg_open(W, H)]
    for v in range(0, 3401, 850):
        y = T + ph - v / mx * ph
        o.append(gridline(L, y, W - R))
        o.append(txt(L - 8, y + 3.5, fmt(v), 8.5, INK3, 400, "end"))
    slot = pw / len(steps)
    bw = min(52, slot * 0.62)
    run = 0.0
    prev_x2 = None
    for i, (name, v, kind) in enumerate(steps):
        cx = L + slot * (i + .5)
        if kind == "total":
            base, top, col = 0.0, v, B650
            run = v
        else:
            base, top, col = run + v, run, S8
            run = run + v
        y0 = T + ph - top / mx * ph
        y1 = T + ph - base / mx * ph
        o.append(bar_v(cx - bw / 2, y0, bw, y1 - y0, col, r=3))
        lab = f"{v:+,.0f}" if kind != "total" else f"{v:,.0f}"
        o.append(txt(cx, y0 - 7, lab, 9.5,
                     INK if kind == "total" else INK2, 700, "middle"))
        if prev_x2 is not None:
            yc = T + ph - run / mx * ph if kind != "total" else y1
            o.append(f'<line x1="{prev_x2}" y1="{T+ph-(run-v if kind!="total" else run)/mx*ph:.2f}" '
                     f'x2="{cx-bw/2}" y2="{T+ph-(run-v if kind!="total" else run)/mx*ph:.2f}" '
                     f'stroke="{INK3}" stroke-width="1" stroke-dasharray="2 2"/>')
        prev_x2 = cx + bw / 2
        for j, ln in enumerate(name.split("\n")):
            o.append(txt(cx, T + ph + 16 + j * 11, ln, 8.8, INK2, 500, "middle"))
    o.append(f'<line x1="{L}" y1="{T+ph}" x2="{W-R}" y2="{T+ph}" '
             f'stroke="{RULE}"/>')
    o.append(txt(L, 12, "CHF million, 2025", 9.5, INK3))
    o.append(txt(0, H - 22, "Every franc of income, and where it goes. "
                            "Half of all revenue is paid to staff.", 9.5, INK3))
    o.append(txt(0, H - 9, "Extraordinary items of CHF 0.1m are omitted.",
                 8.5, INK3))
    o.append("</svg>")
    return "".join(o)


def chart_peers():
    rows = [("UBS Global Wealth Management", 3760, True,
             "USD 4.7tn invested assets, Q1 2026"),
            ("LGT", 386, False, "AUM, 2025"),
            ("PICTET", 757, "hl", "AUM or custody, 2025"),
            ("Julius Baer", 521, False, "AUM, 2025"),
            ("Lombard Odier", 349, False, "total client assets, 2025"),
            ("Vontobel", 271, False, "advised client assets, 2025"),
            ("J. Safra Sarasin", 229, False, "AUM, 2025"),
            ("EFG International", 185, False, "AUM, 2025"),
            ("Union Bancaire Privee", 185, False, "client assets, 2025")]
    rows = sorted(rows, key=lambda r: -r[1])
    W = 700
    rowh = 34
    T, B, L, R = 48, 56, 190, 90
    H = T + len(rows) * rowh + B
    pw = W - L - R
    mx = 900          # scale caps: UBS is drawn clipped and labelled
    o = [svg_open(W, H)]
    for v in (0, 300, 600, 900):
        x = L + v / mx * pw
        o.append(f'<line x1="{x}" y1="{T-6}" x2="{x}" y2="{T+len(rows)*rowh-8}" '
                 f'stroke="{GRID}"/>')
        o.append(txt(x, T - 16, fmt(v), 9, INK3, 400, "middle"))
    y = T
    for name, v, flag, note in rows:
        clipped = v > mx
        bw = pw if clipped else v / mx * pw
        col = S1 if flag == "hl" else B200
        o.append(bar_h(L, y, bw, 20, col))
        if clipped:
            o.append(f'<path d="M{L+pw-14} {y} l10 10 l-10 10" fill="none" '
                     f'stroke="{SURF}" stroke-width="2.5"/>')
            o.append(f'<path d="M{L+pw-6} {y} l10 10 l-10 10" fill="none" '
                     f'stroke="{SURF}" stroke-width="2.5"/>')
        o.append(txt(L - 10, y + 10, name, 10.5, INK,
                     700 if flag == "hl" else 500, "end"))
        o.append(txt(L - 10, y + 21, note, 8, INK3, 400, "end"))
        val = "~3,760+" if clipped else fmt(v)
        o.append(txt(L + bw + 8, y + 14, val, 10.5, INK,
                     700 if flag == "hl" else 500))
        y += rowh
    o.append(txt(0, 14, "CHF billion (converted at approx. 0.80 USD/CHF where needed)",
                 9.5, INK3))
    o.append(txt(0, H - 38, "READ THIS BEFORE QUOTING THE CHART. Each firm "
                            "reports a different thing. Pictet's 757 includes "
                            "custody-only assets it does not", 9, INK3))
    o.append(txt(0, H - 26, "manage; Julius Baer's 521 is managed assets only; "
                            "Lombard Odier's 349 is total client assets against "
                            "CHF 223bn actually managed.", 9, INK3))
    o.append(txt(0, H - 14, "Like-for-like, Pictet and Julius Baer are much "
                            "closer than the bars suggest. Knowing this is the "
                            "point.", 9, INK, 600))
    o.append("</svg>")
    return "".join(o)


def chart_costincome():
    rows = [("Julius Baer (underlying)", 67.6, False),
            ("PICTET", 72.0, True),
            ("Swiss private bank median", 78.2, False)]
    W, H = 700, 188
    L, R, T = 210, 74, 38
    pw = W - L - R
    mx = 90
    o = [svg_open(W, H)]
    y = T
    for name, v, hl in rows:
        bw = v / mx * pw
        o.append(bar_h(L, y, bw, 26, S1 if hl else B200))
        o.append(txt(L - 10, y + 17, name, 11, INK, 700 if hl else 500, "end"))
        o.append(txt(L + bw + 8, y + 17, f"{v:.1f}%", 11.5, INK,
                     700 if hl else 500))
        y += 40
    o.append(txt(L, 16, "Operating costs as a share of operating income, 2025 "
                        "- lower is better", 9.5, INK3))
    o.append(txt(0, H - 20, "Pictet on the same basis as its own accounts "
                            "(personnel + G&A / operating income). Including "
                            "depreciation and provisions it is 73.6%.",
                 9, INK3))
    o.append(txt(0, H - 8, "Pictet is better than the sector but behind the "
                           "best listed operator - the price of a "
                           "people-heavy, service-heavy model.", 9, INK3))
    o.append("</svg>")
    return "".join(o)


# ============================================================ DIAGRAMS =====
def badge(cx, cy, n, col=S1, r=11):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}"/>'
            + txt(cx, cy + 4, n, 11, "#ffffff", 700, "middle"))


def stack(x, y, w, lines, size=9.5, fill=INK2, lh=12, anchor="middle",
          weight=400):
    ax = x + w / 2 if anchor == "middle" else x
    return "".join(txt(ax, y + i * lh, ln, size, fill, weight, anchor)
                   for i, ln in enumerate(lines))


def diag_money_flow():
    W, H = 700, 372
    o = [svg_open(W, H), ARROW_DEFS]
    bw, by, bh = 156, 46, 96
    xs = [4, 272, 540]
    specs = [("THE OWNER OF THE MONEY", S1,
              ["A person, a family,", "a pension fund,", "an insurance company"]),
             ("THE ASSET MANAGER", S2,
              ["Decides what to buy,", "what to sell, and when.", "Never owns the money."]),
             ("THE ASSETS", S3,
              ["Shares in companies,", "government and company", "loans, property, funds"])]
    for x, (title, col, lines) in zip(xs, specs):
        o.append(rrect(x, by, bw, bh, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, by, bw, 5, col, 2))
        o.append(txt(x + bw / 2, by + 26, title, 10, INK, 700, "middle",
                     ".3"))
        o.append(stack(x, by + 44, bw, lines))
    # forward arrows
    gaps = [(xs[0] + bw + xs[1]) / 2, (xs[1] + bw + xs[2]) / 2]
    o.append(arrow(xs[0] + bw + 8, by + 48, xs[1] - 8, by + 48, S1, "ahb"))
    o.append(arrow(xs[1] + bw + 8, by + 48, xs[2] - 8, by + 48, S2, "aho"))
    for gx, n, col, l1, l2 in [(gaps[0], "1", S1, "Hands the money",
                                "over to manage"),
                               (gaps[1], "2", S2, "Buys the assets",
                                "with that money")]:
        o.append(badge(gx, by + 20, n, col))
        o.append(txt(gx, by + 76, l1, 9, INK2, 500, "middle"))
        o.append(txt(gx, by + 87, l2, 9, INK2, 500, "middle"))
    # return loop
    ry = 210
    o.append(f'<path d="M{xs[2]+bw/2} {by+bh+6} V{ry} H{xs[0]+bw/2} V{by+bh+10}" '
             f'fill="none" stroke="{S3}" stroke-width="2" '
             f'marker-end="url(#aha)"/>')
    o.append(badge(350, ry, "3", S3))
    o.append(txt(350, ry - 22,
                 "The assets earn dividends, interest and price gains - and "
                 "all of it belongs to the owner", 10, INK, 600, "middle"))
    o.append(txt(350, ry + 26,
                 "Value can fall as well as rise. The manager takes the "
                 "decisions; the owner takes the risk.", 9, INK3, 400,
                 "middle"))
    # fee
    fy = 268
    o.append(rrect(160, fy, 380, 80, PANEL, 8, f'stroke="{RULE}"'))
    o.append(badge(160, fy, "4", S4))
    o.append(txt(350, fy + 26, "THE ONLY THING THE MANAGER KEEPS: THE FEE",
                 10.5, INK, 700, "middle", ".3"))
    o.append(txt(350, fy + 46,
                 "A small slice of the money, charged every year, whether "
                 "markets rise or fall.", 9.5, INK2, 400, "middle"))
    o.append(txt(350, fy + 62,
                 "That is the entire business. Everything else is detail.",
                 9.5, INK, 600, "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_fee_machine():
    W, H = 700, 300
    o = [svg_open(W, H), ARROW_DEFS]
    o.append(txt(0, 14, "STEP 1  -  What a 'basis point' is", 10, INK, 700,
                 "start", ".4"))
    o.append(rrect(0, 26, 700, 62, PANEL, 8, f'stroke="{RULE}"'))
    cells = [("1%", "= 100 basis points", "= 1 franc per 100"),
             ("0.50%", "= 50 basis points", "= 50 centimes per 100"),
             ("0.10%", "= 10 basis points", "= 10 centimes per 100")]
    for i, (a, b, c) in enumerate(cells):
        cx = 116 + i * 233
        o.append(txt(cx, 50, a, 17, S1, 700, "middle"))
        o.append(txt(cx, 66, b, 9.5, INK2, 500, "middle"))
        o.append(txt(cx, 79, c, 9, INK3, 400, "middle"))
    o.append(txt(0, 116, "STEP 2  -  Why it turns into a real business", 10,
                 INK, 700, "start", ".4"))
    ys = 130
    o.append(rrect(0, ys, 700, 92, "#ffffff", 8,
                   f'stroke="{RULE}" stroke-width="1.2"'))
    parts = [("CHF 100bn", "money looked after", S1),
             ("x", "", None),
             ("42 bps", "average fee rate", S2),
             ("=", "", None),
             ("CHF 420m", "revenue, every year", S3)]
    x = 24
    widths = [150, 40, 130, 40, 170]
    for (big, small, col), wd in zip(parts, widths):
        cx = x + wd / 2
        if col:
            o.append(txt(cx, ys + 42, big, 19, col, 700, "middle"))
            o.append(txt(cx, ys + 62, small, 9, INK3, 400, "middle"))
        else:
            o.append(txt(cx, ys + 42, big, 19, INK3, 400, "middle"))
        x += wd
    o.append(txt(24, ys + 82,
                 "Pictet's actual 2025 rate: CHF 3,206.8m of income on CHF 757bn "
                 "of assets = 42.4 basis points.", 9.5, INK2))
    o.append(txt(0, 252, "STEP 3  -  The thing that makes it lucrative", 10,
                 INK, 700, "start", ".4"))
    o.append(txt(0, 272,
                 "Managing CHF 200bn does not cost twice as much as managing "
                 "CHF 100bn. The people, systems and research are largely "
                 "already paid for.", 9.5, INK2))
    o.append(txt(0, 286,
                 "So most of each new franc of fee income drops through to "
                 "profit. This is why every firm in the industry is obsessed "
                 "with gathering assets.", 9.5, INK2))
    o.append("</svg>")
    return "".join(o)


def diag_value_chain():
    W, H = 700, 300
    o = [svg_open(W, H), ARROW_DEFS]
    rows = [("THE ADVISER / DISTRIBUTOR", S1,
             "Finds the client, understands them, recommends what to do. In a "
             "private bank this is the relationship manager or 'private banker'."),
            ("THE PORTFOLIO MANAGER", S2,
             "Actually decides which shares, bonds or funds to hold. Supported "
             "by analysts, economists and risk teams."),
            ("THE TRADER / EXECUTION DESK", S3,
             "Buys and sells in the market at the best available price, "
             "quietly enough not to move it."),
            ("THE CUSTODIAN", S4,
             "Holds the assets safely in the client's name, collects the "
             "dividends, settles the trades. Boring, essential, and paid a fee."),
            ("THE FUND ADMINISTRATOR & AUDITOR", S7,
             "Prices the fund every day, keeps the register of who owns what, "
             "and gets independently checked.")]
    y = 8
    for i, (name, col, desc) in enumerate(rows):
        o.append(rrect(0, y, 6, 44, col, 3))
        o.append(txt(18, y + 17, name, 10.5, INK, 700, "start", ".2"))
        for j, ln in enumerate(wrap(desc, 108)):
            o.append(txt(18, y + 32 + j * 11, ln, 9.3, INK2))
        y += 56
    o.append(rrect(0, y + 2, 700, 34, PANEL, 6, f'stroke="{RULE}"'))
    o.append(txt(350, y + 23,
                 "Pictet does all five in-house. Most firms buy two or three "
                 "of them from someone else.", 10, INK, 600, "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_four_jobs():
    W, H = 700, 266
    o = [svg_open(W, H)]
    cards = [("WEALTH\nMANAGEMENT", C_WM, "Looking after rich families",
              ["A person with CHF 5m+ walks in.", "Pictet builds and runs a",
               "portfolio for them, lends", "against it, and plans the",
               "handover to their children."],
              "PICTET WEALTH MANAGEMENT"),
             ("ASSET\nMANAGEMENT", C_AM, "Running money for institutions",
              ["A pension fund needs someone", "to run CHF 500m of emerging",
               "market shares. Pictet runs it", "as a fund or a segregated",
               "mandate, for a fee."],
              "PICTET ASSET MANAGEMENT"),
             ("ALTERNATIVE\nINVESTMENTS", C_AA, "Things not on a stock market",
              ["Private companies, buildings,", "hedge funds, private loans.",
               "Harder to buy, harder to sell,", "higher fees, and clients",
               "increasingly want them."],
              "PICTET ALTERNATIVE ADVISORS"),
             ("ASSET\nSERVICING", C_AS, "Holding and administering",
              ["Another firm makes the", "investment decisions. Pictet",
               "holds the assets, settles the", "trades and does the reporting",
               "for a much smaller fee."],
              "PICTET ASSET SERVICES")]
    cw, ch = 168, 212
    for i, (title, col, sub, lines, maps) in enumerate(cards):
        x = i * (cw + 9)
        o.append(rrect(x, 8, cw, ch, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, 8, cw, 6, col, 3))
        ty = 34
        for ln in title.split("\n"):
            o.append(txt(x + cw / 2, ty, ln, 11, INK, 700, "middle", ".3"))
            ty += 14
        o.append(txt(x + cw / 2, ty + 6, sub, 9, col, 600, "middle"))
        yy = ty + 30
        for ln in lines:
            o.append(txt(x + cw / 2, yy, ln, 8.8, INK2, 400, "middle"))
            yy += 11.5
        o.append(rrect(x + 8, 8 + ch - 42, cw - 16, 34, PANEL, 5))
        for j, ln in enumerate(wrap(maps, 20)):
            o.append(txt(x + cw / 2, 8 + ch - 42 + 15 + j * 11, ln, 8.2, INK,
                         700, "middle"))
    o.append(txt(350, H - 30,
                 "Pictet is one of very few firms that does all four at scale. "
                 "Hold on to that - it is the whole argument.", 10, INK, 600,
                 "middle"))
    o.append(txt(350, H - 14,
                 "Most competitors are strong in one, present in a second, and "
                 "absent from the rest.", 9.5, INK3, 400, "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_revenue_engines():
    W, H = 700, 268
    o = [svg_open(W, H)]
    eng = [("RECURRING FEES", S1, "80%",
            ["Charged on the value of the", "assets, every year, whether",
             "the client trades or not.", "", "Predictable. Falls only if",
             "markets fall or clients leave."]),
           ("NET INTEREST", S2, "13%",
            ["Clients leave cash on deposit.", "The bank lends some of it out",
             "and invests the rest.", "", "Depends entirely on interest",
             "rates - outside the firm's control."]),
           ("TRADING & EXECUTION", S3, "7%",
            ["Clients buy and sell; the bank", "earns a spread or commission",
             "on doing it for them.", "", "Depends on how nervous or",
             "busy clients feel."])]
    cw = 226
    for i, (name, col, share, lines) in enumerate(eng):
        x = i * (cw + 11)
        o.append(rrect(x, 6, cw, 196, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, 6, cw, 6, col, 3))
        o.append(txt(x + cw / 2, 34, name, 10.5, INK, 700, "middle", ".3"))
        o.append(txt(x + cw / 2, 62, share, 24, col, 700, "middle"))
        o.append(txt(x + cw / 2, 76, "of Pictet's 2025 income", 8.5, INK3,
                     400, "middle"))
        yy = 100
        for ln in lines:
            o.append(txt(x + cw / 2, yy, ln, 8.8, INK2, 400, "middle"))
            yy += 11.5
    o.append(rrect(0, 214, 700, 48, PANEL, 8, f'stroke="{RULE}"'))
    o.append(txt(350, 234,
                 "WHY THIS MATTERS FOR 2025: Swiss interest rates fell back "
                 "towards zero, so engine two went quiet.", 10, INK, 700,
                 "middle"))
    o.append(txt(350, 250,
                 "Gross interest result fell 15% to CHF 417.8m. That is why "
                 "profit was flat in a record year for assets.", 9.5, INK2,
                 400, "middle"))
    o.append("</svg>")
    return "".join(o)


def _timeline(events, title, colmap):
    SPINE = 128
    top, lh = 30, 0
    rows = []
    y = top
    for yr, head, body, col in events:
        lines = wrap(body, 84)
        h = 20 + len(lines) * 11.5
        rows.append((y, yr, head, lines, col, h))
        y += h + 13
    H = y + 8
    W = 700
    o = [svg_open(W, H), ARROW_DEFS]
    o.append(f'<line x1="{SPINE}" y1="{top-14}" x2="{SPINE}" y2="{H-14}" '
             f'stroke="{RULE}" stroke-width="2"/>')
    for (yy, yr, head, lines, col, h) in rows:
        o.append(f'<circle cx="{SPINE}" cy="{yy+5}" r="5.5" fill="{col}"/>')
        o.append(f'<circle cx="{SPINE}" cy="{yy+5}" r="9" fill="none" '
                 f'stroke="{col}" stroke-width="1" opacity="0.35"/>')
        o.append(txt(SPINE - 20, yy + 9, yr, 12.5, INK, 700, "end"))
        o.append(txt(SPINE + 20, yy + 9, head, 11, col, 700))
        for j, ln in enumerate(lines):
            o.append(txt(SPINE + 20, yy + 24 + j * 11.5, ln, 9.3, INK2))
    o.append("</svg>")
    return "".join(o)


def diag_timeline_a():
    ev = [("1805", "Two men under 30 sign a deed",
           "On 23 July, Jacob-Michel-Francois de Candolle and Jacques-Henry "
           "Mallet found a partnership in Geneva with three silent partners and "
           "125,000 pounds of capital. Geneva has been annexed by France and the "
           "old banking houses have been wiped out by the Revolution. The firm "
           "is built in the ruins.", S1),
          ("1841", "The name arrives",
           "Edouard Pictet-Prevost becomes a partner. The name Pictet is added "
           "to the firm and has never left it. Note the order: the bank existed "
           "for 36 years before a Pictet was involved. It is not a family firm "
           "that hired outsiders - it is a partnership that a family joined.",
           S2),
          ("1856-1909", "Geneva goes global",
           "Under Edouard and then Ernest Pictet the firm moves into "
           "international securities - American railways, foreign government "
           "bonds. Calvinist rigour, discretion and an unusual openness to "
           "the outside world become the house style.", S3),
          ("1909-1950", "Two wars, one constant",
           "Through both world wars the firm stays small, liquid and cautious. "
           "The partners' own money is on the line, which shapes every "
           "decision. Switzerland's neutrality turns Geneva into a refuge for "
           "foreign capital.", S7),
          ("1950-1980", "The quiet accumulation",
           "Post-war prosperity, cross-border wealth and Swiss banking secrecy "
           "combine. Between 1960 and 2000 the assets deposited with Pictet "
           "multiply roughly fiftyfold. Headcount is still under 300 at the end "
           "of the period.", S5)]
    return _timeline(ev, "1805-1980", None)


def diag_timeline_b():
    ev = [("1980", "THE PIVOT - and the most important date in the firm",
           "Pictet forms an institutional asset management joint venture in "
           "London with Mellon Bank, later bought outright. For the first time "
           "the firm manages money for pension funds rather than families. "
           "Everything that makes Pictet unusual today starts here.", S2),
          ("1986-1991", "Building the institutional machine",
           "Tokyo entity (1986). Institutional Brokerage Services (1989). "
           "First alternatives co-investment (1992). The Emerging Markets fund "
           "(1991) makes Pictet an early mover in EM - still a core franchise.",
           S3),
          ("1995-2000", "Thematic investing is invented here",
           "The first thematic strategy, Biotech, launches in 1995. Water "
           "follows in 2000. The idea - buy the structural trend, not the "
           "sector or the index - becomes Pictet's single most distinctive "
           "product and is now copied industry-wide.", S1),
          ("1996-1999", "The plumbing gets built",
           "Pictet Fund Management SA (1996) to manufacture funds. The family "
           "office (1998), among the first in Europe. A dedicated platform for "
           "independent asset managers (1999). Institutional activities are "
           "grouped into one division: Pictet Asset Management.", S4),
          ("2005-2008", "Two hundred years, and a new house",
           "Bicentenary with over 2,000 staff. The Geneva businesses move under "
           "one roof at 60 route des Acacias (2006). The Prix Pictet "
           "photography prize launches (2008) and becomes the firm's public "
           "face.", S5),
          ("2014", "The end of unlimited liability",
           "On 1 January the firm converts from a general partnership into a "
           "corporate partnership limited by shares. Partners stop being "
           "personally liable for everything the bank does, and the group must "
           "publish accounts for the first time. Read this as the price of "
           "going global.", S8),
          ("2020", "Alternatives becomes a business in its own right",
           "Pictet Alternative Advisors is promoted to the fourth reporting "
           "business line in January. The group commits to net zero by 2050 and "
           "joins the Net Zero Asset Managers initiative.", S6),
          ("2023", "The reckoning with the past",
           "Banque Pictet enters a deferred prosecution agreement with the US "
           "Department of Justice and pays USD 122.9m over legacy undeclared US "
           "accounts held between 2008 and 2014. Marc Pictet is named as the "
           "next senior partner.", S8),
          ("2024", "A new generation takes over",
           "Marc Pictet becomes Senior Managing Partner on 1 July, succeeding "
           "Renaud de Planta. He is the ninth generation of the family in the "
           "firm, but leads a partnership of seven equals, two of whom are "
           "Pictets.", S1),
          ("2025", "220 years, a new campus, and a new wrapper",
           "Record CHF 757bn of assets. The move into the Campus Pictet de "
           "Rochemont in Geneva begins. In October the firm launches its first "
           "three actively managed ETFs in the US - a wrapper it had ignored "
           "for a decade.", S2),
          ("2026", "The private-markets and ETF year",
           "First direct private equity fund closes at EUR 403m. Five "
           "AI-enhanced active UCITS ETFs launch in Europe. USD 1.53bn raised "
           "for the sixth PE co-investment fund. The Zurich Marriott is bought "
           "outright. The shape of the firm is visibly changing.", S3)]
    return _timeline(ev, "1980-2026", None)


def diag_group_structure():
    W, H = 700, 372
    o = [svg_open(W, H), ARROW_DEFS]
    o.append(rrect(150, 6, 400, 62, "#ffffff", 8,
                   f'stroke="{NAVY}" stroke-width="1.6"'))
    o.append(txt(350, 28, "PICTET GROUP SCA", 13, INK, 700, "middle", ".6"))
    o.append(txt(350, 45, "A partnership limited by shares. No listing, no "
                          "outside shareholders.", 9, INK2, 400, "middle"))
    o.append(txt(350, 58, "Owned and run by 7 Managing Partners", 9, NAVY,
                 600, "middle"))
    o.append(rrect(0, 14, 138, 46, PANEL, 6, f'stroke="{RULE}"'))
    o.append(txt(69, 32, "SUPERVISORY BOARD", 8.5, INK, 700, "middle"))
    o.append(txt(69, 46, "9 members, independent", 8, INK3, 400, "middle"))
    o.append(f'<line x1="138" y1="37" x2="150" y2="37" stroke="{INK3}" '
             f'stroke-width="1.2"/>')
    o.append(rrect(562, 14, 138, 46, PANEL, 6, f'stroke="{RULE}"'))
    o.append(txt(631, 32, "42 EQUITY PARTNERS", 8.5, INK, 700, "middle"))
    o.append(txt(631, 46, "senior leaders, since 2006", 8, INK3, 400, "middle"))
    o.append(f'<line x1="550" y1="37" x2="562" y2="37" stroke="{INK3}" '
             f'stroke-width="1.2"/>')
    # spine
    o.append(f'<path d="M350 68 V96 M82 96 H619 M82 96 V116 M261 96 V116 '
             f'M440 96 V116 M619 96 V116" fill="none" stroke="{INK3}" '
             f'stroke-width="1.2"/>')
    lines = [("WEALTH\nMANAGEMENT", C_WM, "CHF 285bn",
              ["1,266 staff", "346 private bankers", "22 offices"],
              "Banque Pictet & Cie SA"),
             ("ASSET\nMANAGEMENT", C_AM, "CHF 267bn",
              ["1,167 staff", "405 investment pros", "9 investment centres"],
              "Pictet Asset Mgmt Holding SA"),
             ("ALTERNATIVE\nADVISORS", C_AA, "CHF 36bn",
              ["164 staff", "81 investment pros", "since 1989"],
              "Pictet Alternative Advisors Holding SA"),
             ("ASSET\nSERVICES", C_AS, "CHF 256bn",
              ["241 staff", "6 offices", "custody & fund services"],
              "Banque Pictet & Cie SA")]
    cw = 164
    for i, (name, col, aum, bullets, entity) in enumerate(lines):
        x = i * (cw + 15)
        o.append(rrect(x, 116, cw, 168, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, 116, cw, 6, col, 3))
        ty = 142
        for ln in name.split("\n"):
            o.append(txt(x + cw / 2, ty, ln, 10, INK, 700, "middle", ".3"))
            ty += 13
        o.append(txt(x + cw / 2, ty + 14, aum, 16, col, 700, "middle"))
        yy = ty + 34
        for b in bullets:
            o.append(txt(x + cw / 2, yy, b, 8.6, INK2, 400, "middle"))
            yy += 12
        o.append(rrect(x + 6, 240, cw - 12, 38, PANEL, 5))
        for j, ln in enumerate(wrap(entity, 24)):
            o.append(txt(x + cw / 2, 255 + j * 10.5, ln, 8, INK2, 500,
                         "middle"))
    o.append(rrect(0, 296, 700, 62, PANEL, 8, f'stroke="{RULE}"'))
    o.append(txt(350, 316, "PRINCIPAL LEGAL ENTITIES", 9.5, INK, 700,
                 "middle", ".4"))
    o.append(txt(350, 333, "Banque Pictet & Cie SA (Switzerland, with branches "
                           "in Hong Kong and Singapore)  -  Bank Pictet & Cie "
                           "(Europe) AG", 8.8, INK2, 400, "middle"))
    o.append(txt(350, 347, "Pictet Asset Management Holding SA  -  Pictet "
                           "Alternative Advisors Holding SA", 8.8, INK2, 400,
                 "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_partnership_chain():
    W, H = 700, 300
    o = [svg_open(W, H), ARROW_DEFS]
    steps = [("NO OUTSIDE SHAREHOLDERS", S1,
              "Seven partners own the whole firm. There is no share price, no "
              "quarterly earnings call and nobody to sell out to."),
             ("SO CAPITAL CAN BE HOARDED", S2,
              "Total capital ratio of 21.6% against a 12% requirement. Liquidity "
              "coverage of 191% against 100%. Roughly twice what is asked."),
             ("SO THE FIRM CAN SAY NO", S3,
              "It can soft-close a successful fund to protect returns, refuse "
              "acquisitions, and decline business that would embarrass it later."),
             ("SO IT CAN WAIT DECADES", S4,
              "Marc Pictet: 'It took us decades to open an office in New York.' "
              "Slow decisions, made once, that do not get reversed."),
             ("WHICH IS THE PRODUCT", S7,
              "Continuity is literally what the client is buying. A family "
              "planning three generations ahead needs a counterparty that will "
              "still be there.")]
    y = 6
    for i, (head, col, body) in enumerate(steps):
        o.append(rrect(0, y, 700, 46, "#ffffff", 6,
                       f'stroke="{RULE}" stroke-width="1.1"'))
        o.append(rrect(0, y, 5, 46, col, 2))
        o.append(badge(28, y + 23, str(i + 1), col, 10))
        o.append(txt(50, y + 20, head, 10.5, INK, 700, "start", ".3"))
        for j, ln in enumerate(wrap(body, 104)):
            o.append(txt(50, y + 35 + j * 11, ln, 9.2, INK2))
        if i < len(steps) - 1:
            o.append(f'<path d="M14 {y+46} v6" stroke="{INK3}" '
                     f'stroke-width="1.4" marker-end="url(#ah)"/>')
        y += 58
    o.append("</svg>")
    return "".join(o)


def diag_how_it_fits():
    W, H = 700, 438
    o = [svg_open(W, H), ARROW_DEFS]
    tri = [("WEALTH MANAGEMENT", C_WM,
            ["Rich families and", "individuals.", "High fee rate,",
             "people-heavy."]),
           ("ASSET MANAGEMENT", C_AM,
            ["Pension funds,", "insurers, fund", "distributors.",
             "Lower fee, scalable."]),
           ("ALTERNATIVE ADVISORS", C_AA,
            ["Private equity, real", "estate, hedge funds,",
             "private debt. Highest", "fee rate of the three."])]
    cw = 226
    for i, (name, col, lines) in enumerate(tri):
        x = i * (cw + 11)
        o.append(rrect(x, 6, cw, 108, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, 6, cw, 6, col, 3))
        o.append(txt(x + cw / 2, 32, name, 10, INK, 700, "middle", ".2"))
        yy = 52
        for ln in lines:
            o.append(txt(x + cw / 2, yy, ln, 9, INK2, 400, "middle"))
            yy += 12
        o.append(arrow(x + cw / 2, 118, x + cw / 2, 146, INK3, "ah", 1.6))
    cap = "the assets all end up in the same place"
    o.append(rrect(258, 124, 184, 14, "#ffffff", 3))
    o.append(txt(350, 134, cap, 9, INK3, 400, "middle"))
    o.append(rrect(0, 152, 700, 74, "#ffffff", 8,
                   f'stroke="{RULE}" stroke-width="1.2"'))
    o.append(rrect(0, 152, 700, 6, C_AS, 3))
    o.append(txt(350, 180, "PICTET ASSET SERVICES", 11, INK, 700, "middle",
                 ".4"))
    o.append(txt(350, 198, "Custody, settlement, fund administration, "
                           "valuation and reporting - built for the group's "
                           "own three businesses,", 9, INK2, 400, "middle"))
    o.append(txt(350, 212, "then sold to outsiders as a product in its own "
                           "right. CHF 256bn of that is third-party money.",
                 9, INK2, 400, "middle"))
    o.append(arrow(350, 230, 350, 250, C_AS, "ah", 1.6))
    o.append(rrect(0, 256, 700, 178, PANEL, 8, f'stroke="{RULE}"'))
    o.append(txt(350, 280, "WHY THE COMBINATION IS WORTH MORE THAN THE PARTS",
                 10.5, INK, 700, "middle", ".4"))
    pts = [("1", "Free distribution", "A Pictet wealth client buying a Pictet "
            "fund costs nothing to acquire. Rivals pay a distributor for that."),
           ("2", "Shared research", "One economics and investment team feeds a "
            "pension fund mandate and a family portfolio alike."),
           ("3", "Offsetting flows", "Institutions and private clients rarely "
            "panic at the same time, which steadies net new money."),
           ("4", "Fixed costs spread wider", "The custody platform, the risk "
            "systems and the Luxembourg fund range are paid for once.")]
    yy = 304
    for n, bold, rest in pts:
        o.append(badge(24, yy - 4, n, S1, 9.5))
        o.append(txt(42, yy, bold, 9.6, INK, 700))
        for j, ln in enumerate(wrap(rest, 118)):
            o.append(txt(42, yy + 13 + j * 11, ln, 9.2, INK2))
        yy += 30
    o.append("</svg>")
    return "".join(o)


def diag_thematic_funnel():
    stages = [("MEGATRENDS", B650, 356,
               "Slow, structural forces that do not care about the economic "
               "cycle: demographics, urbanisation, resource scarcity, "
               "automation, health."),
              ("THEMES", B550, 312,
               "Fourteen investable themes are carved out of them - water, "
               "robotics, security, nutrition, clean energy, biotech, premium "
               "brands, digital and more."),
              ("ADVISORY BOARD CHALLENGE", B450, 268,
               "Thirteen advisory boards of scientists, academics and industry "
               "operators exist to attack the thesis. This is the step "
               "competitors mostly skip."),
              ("PURITY SCREEN", B300, 224,
               "Only companies earning a real majority of revenue from the "
               "theme survive. A conglomerate with a small water division does "
               "not count."),
              ("THE PORTFOLIO", B200, 180,
               "A concentrated book of pure plays that looks almost nothing "
               "like a global index - which is the entire point, and the "
               "justification for an active fee.")]
    W = 700
    step = 62
    H = 8 + len(stages) * step + 62
    o = [svg_open(W, H), ARROW_DEFS]
    y = 8
    for i, (name, col, wdt, body) in enumerate(stages):
        dark = i < 3
        o.append(rrect(0, y, wdt, 44, col, 5))
        nm = wrap(name, 22)
        ny = y + (27 if len(nm) == 1 else 20)
        for ln in nm:
            o.append(txt(14, ny, ln, 10, "#ffffff" if dark else INK, 700,
                         "start", ".25"))
            ny += 12
        for j, ln in enumerate(wrap(body, 46)):
            o.append(txt(376, y + 15 + j * 11.5, ln, 9, INK2))
        if i < len(stages) - 1:
            o.append(f'<path d="M{wdt/2-7:.0f} {y+48} l7 8 l7 -8 z" '
                     f'fill="{INK3}"/>')
        y += step
    o.append(rrect(0, y - 6, 700, 52, PANEL, 8, f'stroke="{RULE}"'))
    o.append(txt(350, y + 14, "USD 62bn  -  16 strategies  -  13 advisory "
                              "boards  -  50+ investment professionals  -  "
                              "first strategy 1995", 10, INK, 700, "middle"))
    o.append(txt(350, y + 32, "The largest active thematic equity manager in "
                              "the world by assets. This is Pictet's single "
                              "most defensible product.", 9.3, INK2, 400,
                 "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_arenas():
    W, H = 700, 352
    o = [svg_open(W, H), ARROW_DEFS]
    o.append(rrect(200, 6, 300, 46, NAVY, 8))
    o.append(txt(350, 26, "PICTET", 13, "#ffffff", 700, "middle", "1"))
    o.append(txt(350, 42, "fights in three different markets at once", 9,
                 "#cfe0ee", 400, "middle"))
    cols = [("SWISS & EUROPEAN\nPRIVATE BANKING", C_WM,
             ["UBS Global Wealth Mgmt", "Julius Baer", "Lombard Odier",
              "J. Safra Sarasin", "Union Bancaire Privee", "EFG International",
              "Vontobel", "LGT", "Rothschild & Co", "Edmond de Rothschild"],
             "Competes on trust, continuity and pedigree. Pictet is top-three "
             "among the independents."),
            ("GLOBAL ASSET\nMANAGEMENT", C_AM,
             ["BlackRock", "Amundi", "Fidelity International", "Schroders",
              "Robeco", "AXA IM", "BNP Paribas AM", "Janus Henderson",
              "Thematics AM (Natixis)", "abrdn"],
             "Competes on performance and specialism. Far smaller than the "
             "giants - but number one in active thematics."),
            ("ASSET SERVICING\n& CUSTODY", C_AS,
             ["BNY", "State Street", "Northern Trust", "Citi Securities Svcs",
              "CACEIS", "BNP Paribas Securities", "UBS custody",
              "Credit Suisse legacy book", "Apex Group", "Zurcher Kantonalbank"],
             "Competes on service, not scale. Deliberately targets the "
             "under-served independent manager niche.")]
    cw = 226
    for i, (name, col, names, note) in enumerate(cols):
        x = i * (cw + 11)
        o.append(arrow(350, 54, x + cw / 2, 74, INK3, "ah", 1.4))
        o.append(rrect(x, 78, cw, 222, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, 78, cw, 6, col, 3))
        ty = 102
        for ln in name.split("\n"):
            o.append(txt(x + cw / 2, ty, ln, 9.8, INK, 700, "middle", ".3"))
            ty += 12
        yy = ty + 12
        for nm in names:
            o.append(f'<circle cx="{x+18}" cy="{yy-3.5}" r="2.2" fill="{col}"/>')
            o.append(txt(x + 28, yy, nm, 8.8, INK2))
            yy += 12.4
        o.append(rrect(x + 6, 248, cw - 12, 44, PANEL, 5))
        for j, ln in enumerate(wrap(note, 34)):
            o.append(txt(x + cw / 2, 262 + j * 10, ln, 8.1, INK2, 500,
                         "middle"))
    o.append(txt(350, 322, "Almost nobody else is a serious competitor in all "
                           "three columns. That is the structural answer to "
                           "'what makes Pictet different'.", 9.6, INK, 600,
                 "middle"))
    o.append(txt(350, 338, "The cost of it: Pictet is not the biggest name in "
                           "any single column, and has to justify the "
                           "spread every day.", 9.2, INK3, 400, "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_pushes():
    W, H = 700, 372
    o = [svg_open(W, H)]
    cols = [("PUSH ONE\nPRIVATE MARKETS", S1,
             "Defend the fee rate",
             [("Mar 2026", "EUR 403m first direct private equity fund, "
               "Entrepreneur Capital I - majority stakes in founder-owned "
               "B2B services and education businesses in DACH and the UK"),
              ("Jun 2026", "USD 1.53bn for the sixth private equity "
               "co-investment fund - the largest such raise the firm has done"),
              ("Jun 2026", "Zurich Marriott Hotel bought outright for the "
               "direct real estate strategy"),
              ("2026", "Dutch and German logistics platforms with Stoneweg "
               "and Scantum; Copenhagen development JV with Catella"),
              ("Jul 2026", "USD 253m first environment co-investment fund")]),
            ("PUSH TWO\nVEHICLES & DISTRIBUTION", S2,
             "Get into the wrapper clients now want",
             [("Oct 2025", "First three actively managed US ETFs: AI Enhanced "
               "International Equity, Cleaner Planet, AI & Automation"),
              ("Feb 2026", "Fourth US ETF - AI Enhanced US Equity"),
              ("Apr 2026", "Five AI-enhanced active UCITS ETFs launched in "
               "Europe (PQUS, PQWD, PQEM, PQEU, PQWX), built on the 30-year-old "
               "Quest quantitative franchise"),
              ("Apr 2026", "US emerging market ETFs: EMFI for EM debt and RISE "
               "for EM ex-China"),
              ("Feb 2026", "Pictet Asset Services wins Pareto Asset Management "
               "as a servicing client")]),
            ("PUSH THREE\nCOST AND PLACE", S3,
             "Make the operating model cheaper",
             [("May 2025", "New financial technology hub opened in Lisbon - "
               "a lower-cost engineering base"),
              ("2025-26", "Move into the Campus Pictet de Rochemont in Geneva; "
               "2,500 workplaces consolidated, building carbon cut from 900 to "
               "150 tonnes a year"),
              ("Jul 2026", "Kelvin Tay appointed Chief Investment Officer for "
               "Asia - investment authority moved closer to the fastest-growing "
               "client pool"),
              ("Ongoing", "Singapore reinforced as the Asian booking centre "
               "alongside the Hong Kong branch")])]
    cw = 226
    for i, (name, col, sub, items) in enumerate(cols):
        x = i * (cw + 11)
        o.append(rrect(x, 6, cw, 356, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, 6, cw, 6, col, 3))
        ty = 30
        for ln in name.split("\n"):
            o.append(txt(x + cw / 2, ty, ln, 9.6, INK, 700, "middle", ".3"))
            ty += 12
        o.append(txt(x + cw / 2, ty + 6, sub, 8.8, col, 600, "middle"))
        yy = ty + 30
        for when, what in items:
            o.append(txt(x + 12, yy, when, 8.2, col, 700))
            yy += 11
            for ln in wrap(what, 36):
                o.append(txt(x + 12, yy, ln, 8.4, INK2))
                yy += 10.2
            yy += 7
    o.append("</svg>")
    return "".join(o)


def diag_mandate_types():
    W, H = 700, 192
    o = [svg_open(W, H)]
    cards = [("DISCRETIONARY", S1, "The manager decides",
              "You set the objective and the constraints. After that the "
              "manager buys and sells without asking. Highest fee, most "
              "scalable, most of Pictet's institutional business."),
             ("ADVISORY", S2, "The manager suggests, you decide",
              "Every trade needs the client's yes. Labour-intensive, so it "
              "carries a fee plus transaction charges. Common with "
              "entrepreneurs who want to stay involved."),
             ("EXECUTION ONLY", S3, "You decide, they just do it",
              "No advice, no fee on assets, just a charge per trade and for "
              "safekeeping. Cheapest for the client, least attractive for the "
              "bank.")]
    cw = 226
    for i, (name, col, sub, body) in enumerate(cards):
        x = i * (cw + 11)
        o.append(rrect(x, 6, cw, 150, "#ffffff", 8,
                       f'stroke="{RULE}" stroke-width="1.2"'))
        o.append(rrect(x, 6, cw, 6, col, 3))
        o.append(txt(x + cw / 2, 32, name, 10.5, INK, 700, "middle", ".3"))
        o.append(txt(x + cw / 2, 48, sub, 9, col, 600, "middle"))
        yy = 72
        for ln in wrap(body, 36):
            o.append(txt(x + cw / 2, yy, ln, 8.8, INK2, 400, "middle"))
            yy += 11.5
    o.append(txt(350, 178, "CHF 133.8bn of Pictet's assets sit under "
                           "discretionary agreements and CHF 226.1bn in its "
                           "own funds. The rest is advised or simply held.",
                 9.3, INK2, 400, "middle"))
    o.append("</svg>")
    return "".join(o)


def diag_757():
    W, H = 700, 268
    o = [svg_open(W, H), ARROW_DEFS]
    rows = [("Assets in Pictet's own funds", 226.1, S1),
            ("Discretionary management agreements", 133.8, S2),
            ("Other assets under custody", 598.8, S3)]
    L, R, T = 268, 96, 34
    pw = W - L - R
    mx = 620
    y = T
    for name, v, col in rows:
        bw = v / mx * pw
        o.append(bar_h(L, y, bw, 22, col))
        o.append(txt(L - 10, y + 15, name, 10, INK, 500, "end"))
        o.append(txt(L + bw + 8, y + 15, fmt(v, 1), 10.5, INK, 600))
        y += 32
    o.append(f'<line x1="{L}" y1="{y+2}" x2="{W-R}" y2="{y+2}" '
             f'stroke="{RULE}"/>')
    y += 20
    o.append(txt(L - 10, y, "Total including double counting", 10, INK, 700,
                 "end"))
    o.append(txt(L, y, "CHF 958.7bn", 10.5, INK, 700))
    y += 20
    o.append(txt(L - 10, y, "Less: double counting", 10, S8, 600, "end"))
    o.append(txt(L, y, "- CHF 202.0bn", 10.5, S8, 600))
    y += 22
    o.append(rrect(L - 260, y - 15, 560, 30, PANEL, 5))
    o.append(txt(L - 10, y + 5, "HEADLINE FIGURE", 10, INK, 700, "end"))
    o.append(txt(L, y + 5, "CHF 756.7bn", 12, NAVY, 700))
    o.append(txt(0, 232, "Double counting happens when a Pictet wealth client "
                         "holds a Pictet fund: the money is counted once in "
                         "Wealth Management", 9, INK3))
    o.append(txt(0, 244, "and once in Asset Management. Note also that CHF "
                         "598.8bn is custody - assets Pictet holds and "
                         "administers but does", 9, INK3))
    o.append(txt(0, 256, "not necessarily choose the investments for. Fee "
                         "rates on custody are a fraction of management fees.",
                 9, INK3))
    o.append("</svg>")
    return "".join(o)


# ========================================================== COMPONENTS =====
def fig(svg, num, cap, sub=""):
    s = f'<p class="figsub">{sub}</p>' if sub else ""
    return (f'<figure><figcaption><span class="fignum">Figure {num}</span>'
            f'{esc(cap)}</figcaption>{svg}{s}</figure>')


def callout(kind, title, body, items=None):
    li = ""
    if items:
        li = "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    b = f"<p>{body}</p>" if body else ""
    return (f'<div class="callout {kind}"><h4>{esc(title)}</h4>{b}{li}</div>')


def table(headers, rows, cls="", widths=None, note=""):
    cg = ""
    if widths:
        cg = "<colgroup>" + "".join(f'<col style="width:{w}">'
                                    for w in widths) + "</colgroup>"
    th = "".join(f"<th>{h}</th>" for h in headers)
    tb = ""
    for r in rows:
        tb += "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    n = f'<p class="tnote">{note}</p>' if note else ""
    return (f'<div class="tablewrap"><table class="{cls}">{cg}<thead><tr>{th}'
            f'</tr></thead><tbody>{tb}</tbody></table>{n}</div>')


def stats(items, cols=4):
    cells = ""
    for big, lab, sub in items:
        s = f'<span class="stsub">{esc(sub)}</span>' if sub else ""
        cells += (f'<div class="stat"><span class="stbig">{big}</span>'
                  f'<span class="stlab">{esc(lab)}</span>{s}</div>')
    return f'<div class="statgrid c{cols}">{cells}</div>'


def quote(text, who):
    return (f'<blockquote><p>{esc(text)}</p>'
            f'<cite>{esc(who)}</cite></blockquote>')


CSS = f"""
@page {{ size: A4; margin: 16mm 15mm 16mm 15mm; }}
* {{ box-sizing: border-box; -webkit-print-color-adjust: exact;
     print-color-adjust: exact; }}
html {{ font-size: 10.2pt; }}
body {{ margin: 0; font-family: Inter, 'Liberation Sans', sans-serif;
        color: {INK2}; line-height: 1.62; background: {SURF};
        font-variant-numeric: tabular-nums; }}
h1, h2, h3, h4 {{ color: {INK}; line-height: 1.22; margin: 0; }}
p {{ margin: 0 0 0.72em; }}
a {{ color: {S1}; text-decoration: none; }}
strong {{ color: {INK}; font-weight: 600; }}
em.k {{ font-style: normal; background: #fdf3d6; padding: 0 2px;
        border-radius: 2px; color: {INK}; font-weight: 500; }}

/* ---- cover ---- */
.cover {{ height: 258mm; display: flex; flex-direction: column;
          justify-content: space-between; break-after: page; }}
.cover .rule {{ height: 6px; background: {NAVY}; width: 100%; }}
.cover h1 {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 46pt;
             font-weight: 600; letter-spacing: -0.02em; margin: 0 0 6px;
             color: {NAVY}; }}
.cover .sub {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 17pt;
               color: {INK2}; line-height: 1.32; max-width: 155mm; }}
.cover .kicker {{ font-size: 8.6pt; letter-spacing: .22em; font-weight: 600;
                  text-transform: uppercase; color: {S2}; margin-bottom: 10mm; }}
.cover .meta {{ font-size: 8.6pt; color: {INK3}; border-top: 1px solid {RULE};
                padding-top: 5mm; }}
.cover .meta b {{ color: {INK}; }}
.coverbars {{ display: flex; gap: 4px; margin: 8mm 0; }}
.coverbars i {{ height: 10px; flex: 1; border-radius: 2px; }}

/* ---- structure ---- */
.part {{ break-before: page; }}
.parthead {{ border-top: 4px solid {NAVY}; padding-top: 5mm;
             margin-bottom: 7mm; }}
.parthead .pnum {{ font-size: 8.4pt; letter-spacing: .2em; font-weight: 700;
                   text-transform: uppercase; color: {S2}; display: block;
                   margin-bottom: 3mm; }}
.parthead h1 {{ font-family: 'Source Serif 4', Georgia, serif;
                font-size: 25pt; font-weight: 600; letter-spacing: -0.015em;
                color: {NAVY}; }}
.parthead .dek {{ font-size: 10.4pt; color: {INK2}; margin-top: 3mm;
                  max-width: 160mm; }}
h2 {{ font-family: 'Source Serif 4', Georgia, serif; font-size: 15.5pt;
      font-weight: 600; margin: 8mm 0 3mm; letter-spacing: -0.01em;
      break-after: avoid; }}
h2:first-of-type {{ margin-top: 2mm; }}
h3 {{ font-size: 9.2pt; font-weight: 700; text-transform: uppercase;
      letter-spacing: .14em; color: {S2}; margin: 6mm 0 2.5mm;
      break-after: avoid; }}
.lead {{ font-size: 11pt; color: {INK}; line-height: 1.55; }}

/* ---- figures ---- */
figure {{ margin: 5mm 0 6mm; break-inside: avoid; }}
figcaption {{ font-size: 9.3pt; font-weight: 600; color: {INK};
              margin-bottom: 2.5mm; padding-bottom: 2mm;
              border-bottom: 1px solid {RULE}; }}
.fignum {{ display: inline-block; font-size: 7.6pt; letter-spacing: .12em;
           text-transform: uppercase; color: {SURF}; background: {NAVY};
           padding: 1.5px 6px; border-radius: 3px; margin-right: 7px;
           font-weight: 700; vertical-align: 1.5px; }}
svg.fig {{ display: block; }}
.figsub {{ font-size: 8.2pt; color: {INK3}; margin: 2mm 0 0; }}

/* ---- callouts ---- */
.callout {{ border: 1px solid {RULE}; border-left: 4px solid {S1};
            background: {PANEL}; border-radius: 5px; padding: 4mm 5mm;
            margin: 4mm 0; break-inside: avoid; font-size: 9.5pt; }}
.callout h4 {{ font-size: 8.6pt; text-transform: uppercase;
               letter-spacing: .13em; font-weight: 700; margin-bottom: 2mm;
               color: {S1}; }}
.callout p, .callout li {{ margin-bottom: 0.45em; }}
.callout ul {{ margin: 0; padding-left: 4.5mm; }}
.callout li {{ margin-bottom: 1.4mm; }}
.callout.warn {{ border-left-color: {S8}; background: #fdf2f2; }}
.callout.warn h4 {{ color: #b32b2b; }}
.callout.win {{ border-left-color: {S6}; background: #f1f8f1; }}
.callout.win h4 {{ color: #086108; }}
.callout.key {{ border-left-color: {S4}; background: #fdf7e8; }}
.callout.key h4 {{ color: #8a5e00; }}
.callout.dark {{ border: none; border-left: 4px solid {S2};
                 background: {NAVY}; color: #d9e4ee; }}
.callout.dark h4 {{ color: {S4}; }}
.callout.dark strong {{ color: #ffffff; }}

blockquote {{ margin: 4mm 0; padding: 0 0 0 6mm;
              border-left: 3px solid {S2}; break-inside: avoid; }}
blockquote p {{ font-family: 'Source Serif 4', Georgia, serif;
                font-size: 12pt; line-height: 1.44; color: {INK};
                margin-bottom: 2mm; }}
blockquote cite {{ font-style: normal; font-size: 8.4pt; color: {INK3};
                   letter-spacing: .06em; text-transform: uppercase;
                   font-weight: 600; }}

/* ---- tables ---- */
.tablewrap {{ margin: 4mm 0 5mm; }}
thead {{ display: table-header-group; }}
tr {{ break-inside: avoid; }}
table {{ width: 100%; border-collapse: collapse; font-size: 8.7pt; }}
th {{ text-align: left; font-size: 7.6pt; text-transform: uppercase;
      letter-spacing: .1em; color: {INK3}; font-weight: 700;
      padding: 0 6px 2.5mm; border-bottom: 1.5px solid {INK3};
      vertical-align: bottom; }}
td {{ padding: 2.2mm 6px; border-bottom: 1px solid {RULE};
      vertical-align: top; line-height: 1.42; }}
td:first-child, th:first-child {{ padding-left: 0; }}
td:last-child, th:last-child {{ padding-right: 0; }}
tr td:first-child {{ color: {INK}; font-weight: 600; }}
table.num td:not(:first-child) {{ text-align: right; }}
table.num th:not(:first-child) {{ text-align: right; }}
.tnote {{ font-size: 7.9pt; color: {INK3}; margin: 2mm 0 0; }}
.pos {{ color: #086108; font-weight: 600; }}
.neg {{ color: #b32b2b; font-weight: 600; }}

/* ---- stat grid ---- */
.statgrid {{ display: grid; gap: 3mm; margin: 4mm 0 5mm;
             break-inside: avoid; }}
.statgrid.c4 {{ grid-template-columns: repeat(4, 1fr); }}
.statgrid.c3 {{ grid-template-columns: repeat(3, 1fr); }}
.statgrid.c2 {{ grid-template-columns: repeat(2, 1fr); }}
.stat {{ border: 1px solid {RULE}; border-radius: 5px; padding: 3mm;
         background: {SURF}; border-top: 3px solid {S1}; }}
.stat:nth-child(4n+2) {{ border-top-color: {S2}; }}
.stat:nth-child(4n+3) {{ border-top-color: {S3}; }}
.stat:nth-child(4n+4) {{ border-top-color: {S4}; }}
.stbig {{ display: block; font-size: 16pt; font-weight: 700; color: {INK};
          line-height: 1.1; letter-spacing: -0.02em; }}
.stlab {{ display: block; font-size: 8pt; color: {INK2}; margin-top: 1.5mm;
          line-height: 1.32; font-weight: 500; }}
.stsub {{ display: block; font-size: 7.3pt; color: {INK3}; margin-top: 1mm;
          line-height: 1.3; }}

/* ---- misc ---- */
.twocol {{ column-count: 2; column-gap: 8mm; }}
.twocol p {{ margin-bottom: 0.6em; }}
ul.plain {{ margin: 0 0 3mm; padding-left: 4.5mm; }}
ul.plain li {{ margin-bottom: 1.6mm; }}
ol.steps {{ margin: 0 0 3mm; padding-left: 5mm; }}
ol.steps li {{ margin-bottom: 2.2mm; }}
.avoid {{ break-inside: avoid; }}
.pb {{ break-before: page; }}
.toc {{ font-size: 9.4pt; }}
.toc .row {{ display: flex; justify-content: space-between; gap: 6mm;
             padding: 2.2mm 0; border-bottom: 1px dotted {RULE}; }}
.toc .row b {{ color: {INK}; font-weight: 600; }}
.toc .row span {{ color: {INK3}; font-size: 8.4pt; text-align: left;
                  width: 88mm; flex: 0 0 88mm; }}
.srcs {{ font-size: 8.1pt; color: {INK2}; }}
.srcs li {{ margin-bottom: 1.4mm; word-break: break-word; }}
"""


# ============================================================= CONTENT =====
def cover():
    bars = "".join(f'<i style="background:{c}"></i>' for c in
                   [S1, S2, S3, S4, S5, S7, S6, S8])
    return f'''<section class="cover">
<div>
  <div class="rule"></div>
  <div style="height:26mm"></div>
  <div class="kicker">A ground-up business guide</div>
  <h1>Pictet</h1>
  <p class="sub">What the firm actually is, how it makes money, why it is
  built the way it is - and what it is doing right now.</p>
  <div class="coverbars">{bars}</div>
  <p style="font-size:10pt;max-width:150mm;color:{INK2}">
  Written for a reader starting from zero. Part one explains asset management
  itself with no assumed knowledge. Everything after that is a deep dive into
  Pictet: the four business lines, the partnership, the economics line by line,
  the competitive set, and the strategic moves of 2025 and 2026.</p>
  <div style="height:14mm"></div>
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;
       border-top:1px solid {RULE};padding-top:6mm;max-width:170mm">
    <div><div style="font-size:7.6pt;letter-spacing:.16em;font-weight:700;
      text-transform:uppercase;color:{S1};margin-bottom:2mm">Start here</div>
      <div style="font-size:8.8pt;color:{INK2};line-height:1.5">Parts 1 and 2.
      What the industry is, and the twelve Pictet numbers worth knowing by
      heart.</div></div>
    <div><div style="font-size:7.6pt;letter-spacing:.16em;font-weight:700;
      text-transform:uppercase;color:{S2};margin-bottom:2mm">The business</div>
      <div style="font-size:8.8pt;color:{INK2};line-height:1.5">Parts 3 to 7.
      The history, the partnership, the four business lines and the 2025
      accounts taken apart line by line.</div></div>
    <div><div style="font-size:7.6pt;letter-spacing:.16em;font-weight:700;
      text-transform:uppercase;color:{S3};margin-bottom:2mm">The argument</div>
      <div style="font-size:8.8pt;color:{INK2};line-height:1.5">Parts 8 to 11.
      Competitors, what genuinely sets Pictet apart, what it is doing now, and
      how to talk about it.</div></div>
  </div>
</div>
<div class="meta">
  <b>Prepared 26 August 2026.</b> Twenty-one figures and diagrams. Figures are Pictet's audited 2025 results
  (published 10 February 2026) unless stated otherwise; news is current to
  July 2026. Pictet's half-year 2026 results had not been published at the
  time of writing. Sources are listed in full at the end.
</div>
</section>'''


def contents():
    rows = [("Part 1", "Asset management, explained from zero",
             "What the industry is, who pays whom, and how a fee becomes a "
             "business"),
            ("Part 2", "Pictet at a glance",
             "The numbers that matter and what they mean"),
            ("Part 3", "The story: 220 years in two pages",
             "How a bank founded in the wreckage of the French Revolution "
             "became a global asset manager"),
            ("Part 4", "How Pictet is built",
             "The partnership, the seven owners, and why the ownership "
             "structure is the strategy"),
            ("Part 5", "The four business lines",
             "Wealth Management, Asset Management, Alternative Advisors, "
             "Asset Services"),
            ("Part 6", "How Pictet actually makes money",
             "The 2025 income statement taken apart, with the margins "
             "calculated"),
            ("Part 7", "The investment engine",
             "Thematics, emerging markets, the house view, and what they "
             "genuinely sell"),
            ("Part 8", "The competitive landscape",
             "Three arenas, the peer numbers, and the definitional trap in "
             "every league table"),
            ("Part 9", "What actually makes Pictet different",
             "The brochure answer, the real answer, and the honest weaknesses"),
            ("Part 10", "What is happening right now",
             "The 2025-26 moves decoded and what they signal"),
            ("Part 11", "Interview toolkit",
             "Numbers to memorise, five things most candidates will not say, "
             "and questions to ask"),
            ("Appendix", "Data notes, caveats and sources",
             "Where every figure came from and what it does and does not mean")]
    body = "".join(f'<div class="row"><b>{p} &nbsp;&middot;&nbsp; {t}</b>'
                   f'<span>{d}</span></div>' for p, t, d in rows)
    return f'''<section>
<div class="parthead"><span class="pnum">Contents</span>
<h1>What is in this guide</h1>
<p class="dek">Read it in order if you are new to the industry. If you already
know what an asset manager does, start at Part 2 - but Figure 7 in Part 1 is
worth two minutes anyway, because it sets up the argument the whole document
makes.</p></div>
<div class="toc">{body}</div>
{callout("key", "A note on honesty",
 "This document deliberately includes the things Pictet's own marketing does "
 "not say: the flat profit in a record year, the middling cost-income ratio, "
 "the 2023 US Department of Justice settlement, and the fact that the "
 "headline asset figure is not comparable with its rivals'. If you are using "
 "this to prepare for an interview, that material is more useful than the "
 "good news, because everyone else will have read the good news.")}
</section>'''


PART1 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 1</span>
<h1>Asset management, explained from zero</h1>
<p class="dek">No jargon, no assumed knowledge. By the end of this part you
will understand what the industry does, who pays whom, why the fee is charged
the way it is, and what the four kinds of firm in it are. Everything about
Pictet then becomes easy.</p></div>

<h2>The whole industry in one sentence</h2>
<p class="lead">Asset management is looking after other people's money and
being paid a small slice of it every year for doing so.</p>
<p>That is genuinely all of it. Every firm in this industry - a Swiss private
bank, a giant American index house, a hedge fund, a pension consultant - is a
variation on that sentence. The differences are in <em>whose</em> money,
<em>what</em> they buy with it, and <em>how big</em> the slice is.</p>

{fig(diag_money_flow(), 1,
     "The four steps that make up the entire business",
     "The single most important thing on this page is step 4. The manager "
     "never owns the money, never keeps the returns and does not take the "
     "loss. It is paid a fee for making the decisions.")}

<h2>Why the fee is charged the way it is</h2>
<p>Fees are quoted in <strong>basis points</strong>, usually shortened to
<em class="k">bps</em> and said out loud as "bips". One basis point is one
hundredth of one per cent. The reason the industry uses such a small unit is
that the numbers it is applied to are very large.</p>

{fig(diag_fee_machine(), 2,
     "How a fraction of a per cent becomes a large business")}

{callout("key", "The one economic idea to take away",
 "Costs in this industry are mostly fixed and revenue is mostly variable with "
 "the size of the assets. A firm's research team, technology and compliance "
 "department cost roughly the same whether they are running CHF 100bn or CHF "
 "200bn. So growth in assets flows to profit at a very high rate - and falls "
 "in assets hurt just as fast. This is why every conversation in the industry "
 "eventually becomes a conversation about net new money.")}

<h2>Who the money belongs to</h2>
<p>There are three broad sources, and they behave completely differently. Most
firms specialise in one. A key fact about Pictet, which we will come back to
repeatedly, is that it is roughly half and half in the first two.</p>

{table(["Source of money", "Who they are", "What they want", "Typical fee"],
 [["Private clients",
   "Wealthy individuals and families. In Pictet's case, usually CHF 5m and "
   "upwards, and often far more.",
   "Preservation first, growth second, plus tax, succession and family "
   "governance help. They are buying a relationship.",
   "60-120 bps"],
  ["Institutions",
   "Pension funds, insurance companies, sovereign wealth funds, university "
   "endowments, central banks.",
   "A specific job done well at a specific risk level, measured against a "
   "benchmark, reported on rigorously. They are buying a capability.",
   "15-75 bps"],
  ["Intermediaries",
   "Other banks, independent financial advisers, independent asset managers, "
   "fund platforms who sell your funds to their own clients.",
   "Products they can put in front of their own clients, plus the "
   "infrastructure to hold them.",
   "Varies; a large part is paid back out as distribution fees"]],
 "num" if False else "",
 ["19%", "30%", "36%", "15%"])}

<h2>The four kinds of firm - and the four parts of Pictet</h2>
<p>Once you know who the money belongs to, the shape of the industry follows.
There are four distinct jobs, and they map exactly onto Pictet's four business
lines. If you learn this one diagram you have learned the company's
structure.</p>

{fig(diag_four_jobs(), 3,
     "The four jobs in the industry, and the Pictet division that does each")}

<h2>Three ways a client can be looked after</h2>
<p>Within wealth management especially, the same client can be served in three
different ways, and the choice determines both the fee and how much work the
bank has to do.</p>

{fig(diag_mandate_types(), 4, "Discretionary, advisory and execution-only")}

<h2>Everyone who touches the money</h2>
<p>A single share bought for a single client passes through five distinct
functions. Some firms do one of them; a few do all five. It is worth knowing
who does what, because a firm's answer to "which of these do you own?" tells
you most of what you need to know about its business model.</p>

{fig(diag_value_chain(), 5, "The value chain, top to bottom")}

<h2>Where a private bank's revenue actually comes from</h2>
<p>A pure asset manager has one revenue engine: fees on assets. A private
bank, because it is also a <em>bank</em>, has three. This distinction explains
most of what happened to Pictet's profits in 2025.</p>

{fig(diag_revenue_engines(), 6, "The three engines of a private bank")}

<h2>The vocabulary you need, and nothing more</h2>
{table(["Term", "What it actually means", "Why it matters"],
 [["AUM", "Assets under management. The money the firm makes the investment "
   "decisions for.",
   "This is the number every firm leads with, and the one every firm defines "
   "slightly differently."],
  ["AUC", "Assets under custody. Money the firm holds and administers but "
   "does not choose the investments for.",
   "Earns perhaps 2-10 bps against 40-100 bps for management. Mixing the two "
   "into one headline flatters the total."],
  ["Net new money (NNM)",
   "New client money in, minus money withdrawn. Excludes market movements.",
   "The single cleanest measure of whether a firm is winning. Markets are "
   "luck; net new money is skill."],
  ["Mandate",
   "A segregated portfolio run for one client under an agreed set of rules.",
   "The institutional alternative to a fund. No other investors to share the "
   "portfolio with."],
  ["Fund", "A pooled vehicle many investors buy units in.",
   "Cheaper to run per franc, easier to distribute, and the basis of most of "
   "Pictet Asset Management's business."],
  ["Active vs passive",
   "Active means a human tries to beat the market. Passive means tracking it "
   "for a very low fee.",
   "Passive has taken enormous market share. Every active manager must now "
   "justify its fee - this is the central industry pressure."],
  ["Public vs private markets",
   "Public means listed and tradeable daily. Private means unlisted - "
   "companies, buildings, direct loans.",
   "Private assets carry several times the fee rate. This is why every firm, "
   "Pictet included, is pushing into them."],
  ["Basis point (bp)", "One hundredth of one per cent.",
   "The unit fees are quoted in. 100 bps = 1%."],
  ["Cost-income ratio",
   "Operating costs divided by operating income.",
   "The industry's efficiency measure. Lower is better; the Swiss private "
   "bank median in 2026 was 78.2%."],
  ["Discretionary",
   "The manager trades without asking the client each time.",
   "Higher fee, and far more scalable than advisory."]],
 "", ["16%", "44%", "40%"])}
</section>'''


PART2 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 2</span>
<h1>Pictet at a glance</h1>
<p class="dek">The audited 2025 numbers, published on 10 February 2026, plus
the operating figures from the annual review. Learn the first eight of these
and you will be ahead of most people in the room.</p></div>

{stats([("CHF 757bn", "Assets under management or custody", "31 Dec 2025, up 4.5%"),
        ("CHF 19bn", "Net new money in 2025", "up from CHF 11bn in 2024"),
        ("CHF 3.21bn", "Operating income", "up 1.5% year on year"),
        ("CHF 846m", "Operating result", "up 3.7%"),
        ("CHF 667m", "Consolidated profit", "flat on 2024's CHF 665m"),
        ("5,507", "Full-time equivalent staff", "group-wide"),
        ("31 / 20", "Offices / countries", "headquartered in Geneva"),
        ("220", "Years old", "founded 23 July 1805"),
        ("7", "Managing Partners", "who own the entire firm"),
        ("42", "Equity Partners", "senior leaders, at 1 April 2026"),
        ("21.6%", "Total capital ratio", "against a 12% requirement"),
        ("191%", "Liquidity coverage ratio", "against a 100% requirement")])}

<h2>The elevator description</h2>
<p class="lead">Pictet is a 220-year-old Geneva partnership, owned outright by
seven working partners, that does four things: it looks after the money of
wealthy families, runs investment funds and mandates for institutions, invests
in private markets, and holds and administers assets for other firms. It has
no investment bank, no retail bank, no shareholders and no stock market
listing. It is roughly the size of Julius Baer in wealth and roughly the size
of a mid-tier European fund house in institutional asset management - and
almost uniquely, it is genuinely both.</p>

{fig(chart_aum_history(), 7, "Assets under management or custody, 2020-2025")}

<h2>The 757 question - what that number actually contains</h2>
<p>This matters more than it sounds. Pictet reports "assets under management
<em>or custody</em>", which is a wider definition than most of its rivals use.
Understanding the composition is the difference between quoting a marketing
number and understanding a business.</p>

{fig(diag_757(), 8, "How CHF 757bn is built up",
     "Source: note 25 to the 2025 consolidated accounts.")}

{callout("warn", "Do not skip this",
 "CHF 598.8bn of the gross figure is 'other assets under custody'. Custody "
 "earns a small fraction of what management earns. So a firm reporting CHF "
 "757bn of 'AUM or custody' is not twice the business of a firm reporting CHF "
 "380bn of pure AUM. When you compare Pictet to a peer, always ask what each "
 "one is counting. Part 8 works through this properly.")}

<h2>The margins, calculated</h2>
<p>None of these are published as ratios; all are computed from the audited
income statement and balance sheet. Doing this arithmetic yourself is the
single fastest way to sound like you have actually read the accounts.</p>

{table(["Measure", "Working", "2025"],
 [["Revenue margin on assets", "CHF 3,206.8m income / CHF 757bn assets",
   "<b>42.4 bps</b>"],
  ["Cost-income ratio",
   "CHF 2,308.6m operating expenses / CHF 3,206.8m income", "<b>72.0%</b>"],
  ["Cost-income including depreciation and provisions",
   "CHF 2,360.7m / CHF 3,206.8m", "<b>73.6%</b>"],
  ["Operating margin", "CHF 846.1m / CHF 3,206.8m", "<b>26.4%</b>"],
  ["Net margin", "CHF 667.2m / CHF 3,206.8m", "<b>20.8%</b>"],
  ["Staff costs as a share of income", "CHF 1,614.5m / CHF 3,206.8m",
   "<b>50.3%</b>"],
  ["Revenue per employee", "CHF 3,206.8m / 5,507 FTE",
   "<b>CHF 582,000</b>"],
  ["Staff cost per employee", "CHF 1,614.5m / 5,507 FTE",
   "<b>CHF 293,000</b>"],
  ["Profit per employee", "CHF 667.2m / 5,507 FTE", "<b>CHF 121,000</b>"],
  ["Return on year-end equity", "CHF 667.2m / CHF 3,283.5m", "<b>20.3%</b>"],
  ["Return on average equity", "CHF 667.2m / CHF 3,532.8m average",
   "<b>18.9%</b>"],
  ["Organic growth rate",
   "CHF 19bn net new money / CHF 724bn opening assets", "<b>2.6%</b>"],
  ["Effective tax rate", "CHF 178.8m / CHF 846.0m pre-tax", "<b>21.1%</b>"]],
 "num", ["36%", "42%", "22%"],
 "All figures from the Pictet Group Annual Report 2025. Ratios are the "
 "author's calculation, not Pictet's disclosure.")}

{callout("win", "The number that will impress",
 "A 42.4 basis point revenue margin sounds thin for a private bank - peers "
 "are often quoted at 60-80 bps. It is thin <b>because the denominator "
 "includes CHF 599bn of low-fee custody assets</b>. Strip the custody "
 "business out and the margin on genuinely managed money is far higher. "
 "Spotting that the ratio is an artefact of the disclosure, not a sign of "
 "weakness, is exactly the kind of reading an interviewer is testing for.")}
</section>'''


PART3 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 3</span>
<h1>The story: 220 years in two pages</h1>
<p class="dek">Pictet is old, and it uses that fact constantly in its
marketing. But the history is genuinely load-bearing: three specific moments
explain why the firm is shaped the way it is today. They are marked in the
timeline below.</p></div>

{fig(diag_timeline_a(), 9, "1805 to 1980: the private bank")}

{callout("key", "Moment one - 1841, and a detail almost everyone gets wrong",
 "Pictet was not founded by a Pictet. The firm was founded in 1805 by de "
 "Candolle and Mallet; Edouard Pictet-Prevost joined as a partner 36 years "
 "later and the name stuck. This is not trivia. It is the origin of the whole "
 "governance philosophy: the partnership came first and the family joined it, "
 "which is why partners have never had to be family and why ownership has "
 "never been inheritable. Pictet calls this 'transmission without DNA'.")}

{fig(diag_timeline_b(), 10, "1980 to 2026: the asset manager")}

{callout("win", "Moment two - 1980, the date that actually matters",
 "In 1980 Pictet set up an institutional asset management joint venture in "
 "London with Mellon Bank. Before that it was a private bank. After it, it "
 "was a private bank <b>and</b> an institutional fund manager - and that dual "
 "identity is now the single most distinctive thing about the firm. "
 "Institutional asset management now accounts for roughly the same assets as "
 "wealth management. Almost no European private bank can say that. If you are "
 "asked what makes Pictet different, this is a better answer than 'it is 220 "
 "years old'.")}

{callout("warn", "Moment three - 2014, the end of unlimited liability",
 "For over two centuries the partners were personally, jointly and severally "
 "liable for everything the bank did. On 1 January 2014 the firm converted "
 "into a corporate partnership limited by shares. Partners' personal wealth "
 "is no longer on the hook for the group's obligations, and the group must now "
 "publish audited accounts - which is why the figures in this document exist "
 "at all. The trade was legal protection and international expansion in "
 "exchange for the purest form of the partnership ideal. Lombard Odier made "
 "the same change at the same time. Expect a thoughtful interviewer to ask "
 "whether the culture survived it.")}

<h2>The pattern in the history</h2>
<p>Read end to end, the same three behaviours repeat in every era. They are
worth naming because they are also the firm's stated strategy today.</p>
<ul class="plain">
<li><strong>It never buys anyone.</strong> In 220 years there is essentially no
history of acquisitions. Growth comes from hiring and from launching products.
Francois Pictet's stated view is that growth by hiring the right people is
more effective than M&amp;A, which damages culture. In an industry currently
consolidating hard, this is a genuine strategic choice with real costs.</li>
<li><strong>It enters markets late and then stays forever.</strong> Marc
Pictet's own line is that it took the firm decades to open an office in New
York. The upside is that it has almost never had to retreat from one.</li>
<li><strong>It invents products rather than copying them.</strong> Emerging
markets in 1991, thematic equities in 1995, water in 2000, robotics in 2015.
The firm's best businesses were all things nobody else was doing at the
time.</li>
</ul>
</section>'''


PART4 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 4</span>
<h1>How Pictet is built</h1>
<p class="dek">The ownership structure is not a quirk of the firm. It is the
firm's strategy, its risk framework and its marketing pitch simultaneously.
This is the part of the business most candidates describe badly.</p></div>

{fig(diag_group_structure(), 11, "The Pictet Group: ownership, oversight and "
     "the four business lines")}

<h2>The rules of the partnership</h2>
<p>These are unusually strict and unusually specific, and they are the reason
the firm behaves the way it does.</p>

{table(["Rule", "The detail", "What it produces"],
 [["Seven owners, equal shares",
   "The Managing Partners hold equal stakes and equal voting rights. Decisions "
   "are taken by consensus, in practice unanimously.",
   "No single person can force a decision, and no faction can outvote another. "
   "Marc Pictet: 'we aim to take the pressure out of the system.'"],
  ["Partners must work in the business",
   "Every partner works at the bank full time and lives in Geneva. There are "
   "no passive owners.",
   "The people taking the risk are the people running the business. There is "
   "no absentee shareholder to please."],
  ["Mandatory retirement at 65",
   "No exceptions, including for family members.",
   "Forced generational turnover. Succession is a scheduled event, not a "
   "crisis."],
  ["Ownership cannot be inherited",
   "Departing partners sell their stake at book value. Incoming partners buy "
   "in, funded by a loan from the bank.",
   "Nobody ever gets rich by selling the firm. There is no windfall from "
   "growing the balance sheet and cashing out - which removes the single "
   "biggest incentive for reckless expansion in finance."],
  ["Partners are chosen unanimously",
   "On expertise and cultural fit. Marc Pictet: 'what matters most is that we "
   "also enjoy each other's company.'",
   "Extreme continuity. Only 47 partners in 220 years, with an average tenure "
   "of over 21 years."],
  ["Equity Partners since 2006",
   "42 senior executives now hold this rank, each leading a strategically "
   "important function.",
   "Lets the firm grow without every decision bottlenecking at seven people. "
   "Marc Pictet: 'without that change we would not be where we are today.'"],
  ["Independent supervisory board",
   "Nine members, chaired by Shelby du Pasquier, including former senior "
   "partners Nicolas Pictet, Remy Best and Renaud de Planta.",
   "Oversight without ownership dilution."]],
 "", ["22%", "42%", "36%"])}

{quote("It took us decades to open an office in New York.",
       "Marc Pictet, Senior Managing Partner, on how the partnership decides")}

<h2>Why the structure is the strategy</h2>
<p>The chain below is the argument to make if you are asked why the ownership
model matters commercially rather than sentimentally. Each step is verifiable
in the accounts.</p>

{fig(diag_partnership_chain(), 12,
     "From ownership structure to client proposition, in five steps")}

<h2>The current partners</h2>
<p>Worth knowing by name. Marc Pictet became Senior Managing Partner on 1 July
2024, succeeding Renaud de Planta. He is the ninth generation of the family
in the firm, and one of two Pictets among the seven.</p>
{table(["Managing Partner", "Note"],
 [["Marc Pictet", "Senior Managing Partner since 1 July 2024"],
  ["Laurent Ramsey", "Long-standing asset management and distribution "
   "background"],
  ["Sebastien Eisinger", "Head of Asset Management and Deputy CEO"],
  ["Elif Aktug", "The first woman to become a Managing Partner at Pictet"],
  ["Francois Pictet", "Ninth generation; has articulated the anti-M&amp;A "
   "position publicly"],
  ["Sven Holstenson", "Wealth management"],
  ["Raymond Sagayam", "Has spoken publicly on the emerging markets push"]],
 "", ["30%", "70%"],
 "As at 2026. Alongside them sit 42 Equity Partners as at 1 April 2026.")}

{callout("key", "The strategic tension worth naming",
 "The partnership model buys continuity and independence, and it costs speed "
 "and scale. Pictet cannot issue shares to fund an acquisition, cannot use "
 "stock to pay for a team lift-out, and cannot move faster than seven people "
 "can agree. In a decade when the Swiss private banking sector has shrunk from "
 "156 banks to 79 through consolidation, choosing not to participate is a real "
 "bet - that organic growth compounds faster than integration risk destroys "
 "value. So far, at 2.6% organic asset growth in 2025, the bet is working but "
 "not spectacularly.")}
</section>'''


PART5 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 5</span>
<h1>The four business lines</h1>
<p class="dek">What each one sells, who buys it, how it charges, and what job
it does for the group. Pictet has reported in this shape since Alternative
Advisors was promoted to a full business line in January 2020.</p></div>

{fig(chart_business_lines(), 13, "Assets by business line, 31 December 2025")}

<h2>1. Pictet Wealth Management</h2>
<p><strong>CHF 285bn &middot; 1,266 staff &middot; 629 investment
professionals, of whom 346 are private bankers &middot; 22 offices</strong></p>
<p>The original business, and still the largest. It serves wealthy individuals
and families - the practical entry point is around CHF 5m, and the firm's real
focus is well above that, up to the dynastic families with USD 100m and more
whose affairs span several countries and generations.</p>
<p>What it actually sells is a bundle: a discretionary or advisory investment
portfolio, lending against that portfolio, custody, and then the things that
are hard to buy anywhere else - succession planning, family governance,
philanthropy structuring, and a family office service that Pictet was among the
first European banks to launch, in 1998. The ratio to hold on to is
<strong>346 private bankers for CHF 285bn</strong>: roughly CHF 824m of assets
per banker, which tells you immediately that this is not a mass-market
business.</p>
{callout("", "How the money is actually made here",
 "Three ways at once, and this is the bit people miss. First, a management fee "
 "on the portfolio. Second, transaction income when the client trades. Third - "
 "and this is the invisible one - <b>net interest</b>. Wealth clients leave "
 "very large cash balances: Pictet held CHF 31.5bn of customer deposits at "
 "end-2025 against CHF 8.1bn of loans to customers and CHF 17.5bn of financial "
 "investments. The spread on that is real money, and it is why a private bank "
 "is a bank and not just a manager.")}

<h2>2. Pictet Asset Management</h2>
<p><strong>CHF 267bn at end-2025, USD 354bn at 30 June 2026 &middot; 1,167
staff &middot; 405 investment professionals &middot; 9 investment centres
&middot; 18 offices &middot; institutional manager since 1980</strong></p>
<p>This is the half of Pictet that most people do not know exists, and it is
almost as big as the private bank. Its clients are pension funds, insurers,
sovereign wealth funds, central banks, and - increasingly important - other
banks and platforms that distribute Pictet funds to their own clients.</p>
<p>The product range is genuinely differentiated rather than a full-line
supermarket: thematic equities (the crown jewel, covered in Part 7), emerging
market equity and debt, multi-asset, fixed income, and the Quest quantitative
franchise built over more than thirty years. The firm states explicitly that
it will <strong>soft-close strategies to protect returns</strong> rather than
keep taking money - a claim that is unusual because it is checkable and costs
real revenue.</p>

<h2>3. Pictet Alternative Advisors</h2>
<p><strong>CHF 36bn &middot; 164 staff &middot; 81 investment professionals
&middot; investing in alternatives since 1989, first co-investment 1992
&middot; a full business line since January 2020</strong></p>
<p>Hedge funds, private equity, private debt and real estate. The critical
accounting point, which is easy to get wrong: <strong>this CHF 36bn is not
additive</strong> - it is client money already counted inside Wealth
Management and Asset Management, reported separately because it is managed by
a different team with different skills.</p>
<p>This is the fastest-moving part of the group and, as Part 10 shows, where
almost every strategic announcement of 2026 has come from. The direction of
travel is unmistakable: from picking other people's funds, to co-investing
alongside them, to buying assets outright. Each step up that ladder multiplies
the fee Pictet can charge.</p>

<h2>4. Pictet Asset Services</h2>
<p><strong>CHF 256bn of third-party assets under custody, of which CHF 135bn
in fund services &middot; 241 staff &middot; 6 offices &middot; one global
platform</strong></p>
<p>The least glamorous and most strategically interesting line. It provides
custody, settlement, fund administration, valuation, reporting and trading
services - originally built for Pictet's own three investment businesses, then
sold to outsiders as a product in its own right. Its target clients are
independent asset managers, external wealth managers, fund managers, pension
funds and family offices.</p>
<p>Its stated positioning is to be the <em>finest, not the biggest</em>, which
is a sensible way of saying it cannot outspend BNY or State Street on
technology and does not intend to try. Its genuine competitive claim is
structural: <strong>because Pictet has no investment bank, it has no
proprietary trading desk that could be on the other side of a client's
trade</strong>. For an independent manager choosing a custodian, that absence
of conflict is worth paying for.</p>

{fig(diag_how_it_fits(), 14, "How the four lines reinforce each other")}

{callout("key", "The most useful sentence in this document",
 "Pictet is roughly half private bank and half institutional asset manager, "
 "sitting on top of its own custody platform, with a private-markets arm "
 "feeding product into both halves. Almost every competitor is heavily one "
 "thing with a token presence in the others. When you are asked to describe "
 "the business model, describe that shape - not the four boxes.")}
</section>'''


PART6 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 6</span>
<h1>How Pictet actually makes money</h1>
<p class="dek">The 2025 consolidated income statement, taken apart. Pictet does
not publish revenue or profit by business line, so this is the group picture -
but the group picture is unusually revealing.</p></div>

{fig(chart_revenue_mix(), 15, "Where the CHF 3,206.8m of 2025 income came from")}

<h2>The commission line, gross and net</h2>
<p>The headline commission figure is not what Pictet keeps. Working through it
is worth doing because the gap is enormous.</p>
{table(["Line", "CHF m", "What it is"],
 [["Commission income from securities trading and investment activities",
   "3,473.0", "Management fees, advisory fees, fund fees, custody fees and "
   "brokerage - the core of the business"],
  ["Commission income from lending activities", "3.2",
   "Fees on Lombard and mortgage lending"],
  ["Commission income from other services", "23.7", "Everything else"],
  ["<span class='neg'>Commission expenses</span>",
   "<span class='neg'>(934.1)</span>",
   "Paid away to distributors, sub-custodians, exchanges and platforms who "
   "bring or hold the business"],
  ["<b>Net commission result</b>", "<b>2,565.8</b>",
   "<b>80% of total operating income</b>"]],
 "num", ["58%", "14%", "28%"])}
{callout("", "Why that CHF 934m matters",
 "Pictet pays away 27 centimes of every franc of gross commission income. That "
 "is the cost of distribution - the platforms, banks and intermediaries that "
 "sell Pictet funds to clients Pictet does not own. It is also, precisely, the "
 "cost that its own wealth management arm avoids: a Pictet private client "
 "buying a Pictet fund generates no distribution payment at all. That is the "
 "financial mechanism behind the 'free distribution' point in Figure 14.")}

<h2>Every franc of income, and where it goes</h2>
{fig(chart_waterfall(), 16, "From operating income to consolidated profit, 2025")}

{table(["Income statement", "2025", "2024", "Change"],
 [["Net interest result", "417.6", "491.7", "<span class='neg'>-15%</span>"],
  ["Net commission and services", "2,565.8", "2,474.5",
   "<span class='pos'>+4%</span>"],
  ["Trading and fair value", "216.7", "188.9", "<span class='pos'>+15%</span>"],
  ["Other ordinary result", "6.6", "5.1", "<span class='pos'>+30%</span>"],
  ["<b>Operating income</b>", "<b>3,206.8</b>", "<b>3,160.2</b>",
   "<b class='pos'>+1%</b>"],
  ["Personnel expenses", "(1,614.5)", "(1,573.0)",
   "<span class='neg'>+3%</span>"],
  ["General and administrative expenses", "(694.1)", "(715.1)",
   "<span class='pos'>-3%</span>"],
  ["Depreciation and amortisation", "(39.4)", "(37.4)", "+5%"],
  ["Provisions and losses", "(12.8)", "(18.4)", "-30%"],
  ["<b>Operating result</b>", "<b>846.1</b>", "<b>816.3</b>",
   "<b class='pos'>+4%</b>"],
  ["Taxes", "(178.8)", "(157.6)", "+13%"],
  ["<b>Consolidated profit</b>", "<b>667.2</b>", "<b>665.4</b>", "<b>0%</b>"]],
 "num", ["46%", "18%", "18%", "18%"],
 "CHF million. Source: Pictet Group Annual Report 2025, consolidated income "
 "statement.")}

{callout("warn", "The single best insight in the 2025 accounts",
 "Assets hit a record. Net new money nearly doubled to CHF 19bn. Commission "
 "income rose 4%. And profit was <b>completely flat</b>, at CHF 667m against "
 "CHF 665m. The reason is one line: the net interest result fell 15%, from "
 "CHF 491.7m to CHF 417.6m, as Swiss interest rates fell back towards zero. "
 "The fee engine did its job and the rate engine gave the gains straight back. "
 "If you say only one thing about Pictet's 2025 results, say this.")}

<h2>The balance sheet, and the thing hiding in it</h2>
{table(["Balance sheet at 31 December", "2025", "2024"],
 [["Total assets", "42,928", "43,236"],
  ["Customer deposits", "31,537", "30,278"],
  ["Loans to customers", "8,057", "7,273"],
  ["Financial investments", "17,466", "16,048"],
  ["<b>Trading portfolio assets</b>", "<b>8.0</b>", "<b>19.9</b>"],
  ["Total equity", "3,283", "3,782"],
  ["Total capital ratio", "21.6%", "-"],
  ["Liquidity coverage ratio", "191%", "-"]],
 "num", ["52%", "24%", "24%"],
 "CHF million except ratios.")}

{callout("win", "The stat that proves the marketing claim",
 "Pictet's trading portfolio assets were <b>CHF 8.0m</b> against total assets "
 "of <b>CHF 42.9bn</b>. That is 0.02% of the balance sheet - two hundredths of "
 "one per cent. When Pictet says it takes no proprietary risk and has no "
 "conflicts of interest with clients, the balance sheet does not merely support "
 "the claim, it makes it almost tautological. Very few banks can show a number "
 "like that. It is the most quotable fact in the accounts.")}

{callout("", "One more thing worth noticing",
 "Total equity <i>fell</i> from CHF 3.78bn to CHF 3.28bn during a profitable "
 "year. The cash flow statement shows CHF 1,070m of dividends paid in 2025 "
 "(relating to 2024) against 2024 profit of CHF 665m - a payout well above "
 "earnings. Read together with a 21.6% capital ratio against a 12% "
 "requirement, this says the partners judged the firm to be carrying more "
 "capital than the business needs and returned the excess to themselves. It is "
 "a small window into how a partnership allocates capital differently from a "
 "listed bank.")}

{fig(chart_costincome(), 17, "Cost-income ratio against the market")}
</section>'''


PART7 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 7</span>
<h1>The investment engine</h1>
<p class="dek">What Pictet actually sells to investors, which of it is
genuinely distinctive, and what the firm currently believes about markets.
This is the part to read the night before an interview.</p></div>

<h2>Thematic equities: the crown jewel</h2>
<p>Pictet did not join thematic investing, it largely invented it as a
commercial discipline. The first strategy, Biotech, launched in 1995. Water
followed in 2000 and has just passed its 25th anniversary; Robotics launched in
2015 and passed ten years in October 2025 with roughly USD 13bn in its main
fund alone.</p>
<p>The franchise today: <strong>around USD 62bn across 16 strategies, more
than 50 dedicated investment professionals and 13 advisory boards</strong>.
Pictet was the largest active thematic fund provider in the world by assets as
at June 2025.</p>

{fig(diag_thematic_funnel(), 18, "How a megatrend becomes a portfolio")}

{callout("key", "Why the advisory boards are the actual moat",
 "Anyone can launch a robotics fund. What is hard to copy is thirteen standing "
 "boards of scientists, academics and industry operators whose job is to "
 "attack the investment thesis - plus a partnership with the Copenhagen "
 "Institute for Futures Studies to identify themes in the first place. That is "
 "an expensive, slow-to-build apparatus that a competitor cannot buy off the "
 "shelf, and it is the honest answer to 'why is Pictet better at this than "
 "BlackRock?'")}

<p>The second half of the argument is portfolio construction. Themes are
deliberately built from <em>pure plays</em> - companies earning a real majority
of revenue from the theme - which is why the portfolios look almost nothing
like a global index. When Pictet's equity CIO noted years ago that only 15% of
the Global Megatrend fund's holdings were in the MSCI World index, that was the
whole product proposition in one number: you cannot get this exposure from a
tracker, so an active fee is defensible.</p>

<h2>The other pillars</h2>
{table(["Capability", "Since", "What it is and why it matters"],
 [["Emerging markets", "1991",
   "Pictet launched an EM fund in 1991, well before it was fashionable, and "
   "built out both EM equity and EM debt. It remains a core institutional "
   "franchise and is central to the current house view."],
  ["Thematic equities", "1995",
   "16 strategies, roughly USD 62bn. The largest active thematic manager "
   "globally. Discussed above."],
  ["Multi-asset", "-",
   "Regionally tailored balanced portfolios - the workhorse product for both "
   "wealth clients and smaller institutions."],
  ["Fixed income", "-",
   "Including a well-regarded emerging market debt team. Benefits from the "
   "shift back into bonds after the rate cycle."],
  ["Quest (quantitative)", "1990s",
   "More than thirty years of systematic research. Now the engine behind the "
   "AI-enhanced ETF range launched in 2025-26 - an old capability finding a "
   "new distribution channel."],
  ["Alternatives", "1989",
   "Hedge funds, private equity, private debt and real estate; increasingly "
   "direct rather than fund-of-funds."]],
 "", ["20%", "10%", "70%"])}

<h2>What Pictet currently thinks about markets</h2>
<p>Useful to be able to summarise, because it shows you have read past the
corporate pages. The 2026 outlook and the ten-year Secular Outlook broadly
say:</p>
<ul class="plain">
<li><strong>The near term is constructive but unspectacular.</strong> World GDP
growth of about 2.6%, roughly trend, which limits inflationary pressure. The
divergent, "K-shaped" economy is expected to close from the bottom.</li>
<li><strong>Equities up modestly, emerging markets leading.</strong> Global
equities are expected to deliver something like 5% in 2026, with emerging
market stocks among the best performers.</li>
<li><strong>The dollar weakens.</strong> A fall of roughly 5% is expected, as
the yield gap between US and non-US developed government bonds narrows.
Government bond yields edge higher.</li>
<li><strong>Over ten years, 60/40 is not enough.</strong> The Secular Outlook
argues investors will need income-generating assets, active currency
management, secular growth themes such as AI, and a bigger allocation to
private assets to get real returns.</li>
<li><strong>US exceptionalism fades.</strong> Market leadership is expected to
change, with selected European and emerging market assets offering better
long-run prospects.</li>
</ul>
{callout("", "How this connects to the strategy",
 "Notice that the house view and the corporate strategy are the same argument. "
 "'Look beyond 60/40 and use more private assets' is an investment opinion; it "
 "is also the justification for the direct private equity fund, the real "
 "estate purchases and the co-investment vehicles described in Part 10. "
 "'Emerging markets will lead' is a forecast; it is also why the firm launched "
 "EM ETFs in April 2026. Being able to join those two dots is worth a lot in "
 "an interview.")}

<h2>Sustainability, stated plainly</h2>
<p>Pictet was the <strong>first Swiss financial institution to set externally
validated science-based climate targets</strong> for 2030 consistent with 1.5
degrees, and has committed to net zero by 2050 as a signatory of the Net Zero
Asset Managers initiative. As at the most recent report, 48% of companies in
its managed portfolios had science-based targets, against a 40% target for
end-2025.</p>
<p>The approach is deliberately <em>engagement over exclusion</em>: rather than
selling out of fossil fuel companies, the firm says it prefers to press them to
set 1.5-degree-aligned targets. Firm-wide it excludes thermal coal mining above
25% revenue exposure, and its dedicated responsible investment strategies add
exclusions for coal-fired power, unconventional oil and gas extraction, and oil
and gas production.</p>
</section>'''


PART8 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 8</span>
<h1>The competitive landscape</h1>
<p class="dek">Pictet does not have one competitive set, it has three, and it
is a different size in each. Getting this right - including the trap in every
published league table - is what separates a good answer from a generic
one.</p></div>

{fig(diag_arenas(), 19, "Three arenas, three sets of rivals")}

<h2>The peer numbers - and the trap</h2>
{fig(chart_peers(), 20, "European wealth managers by their own headline "
     "asset figure, 2025-26")}

{callout("warn", "The definitional trap",
 "These numbers are not comparable and the industry knows it. Pictet reports "
 "'assets under management <b>or custody</b>' - CHF 757bn, of which CHF 599bn "
 "is custody. Julius Baer reports assets under management only - CHF 521bn. "
 "Lombard Odier reports CHF 349bn of total client assets but only CHF 223bn "
 "actually under management. UBS reports 'invested assets'. Vontobel reports "
 "'advised client assets'. Anyone who quotes these side by side without saying "
 "so is quoting marketing. Say so, and you will be the only candidate who "
 "does.")}

<h2>Head to head</h2>
{table(["Firm", "Ownership", "Headline assets", "Business mix", "Distinctive"],
 [["<b>Pictet</b>", "7 working partners; unlisted",
   "CHF 757bn (AUM or custody)",
   "Roughly half wealth, half institutional, plus custody and alternatives",
   "The only one of these with genuine scale in both wealth and institutional "
   "asset management. Largest active thematic manager globally."],
  ["UBS Global Wealth Mgmt", "Listed; part of UBS Group",
   "USD ~4.7tn invested assets",
   "Universal bank: wealth, asset management, investment bank, Swiss retail",
   "Overwhelming scale after the Credit Suisse integration. The conflict "
   "profile is the mirror image of Pictet's."],
  ["Julius Baer", "Listed", "CHF 521bn AUM",
   "Pure-play wealth management",
   "Best-in-class cost discipline (67.6% cost-income) but a series of credit "
   "and governance episodes to live down."],
  ["Lombard Odier", "Partnership; unlisted",
   "CHF 349bn client assets / CHF 223bn AUM",
   "Wealth, asset management and a technology platform sold to other banks",
   "Pictet's closest structural analogue - same city, same 1796-era vintage, "
   "same partnership logic, made the same 2014 legal conversion."],
  ["Vontobel", "Listed; family-anchored", "CHF 271bn advised assets",
   "Wealth and asset management, plus structured products",
   "Strong asset management brand; smaller wealth footprint."],
  ["J. Safra Sarasin", "Family-owned", "CHF 228.5bn AUM",
   "Wealth management with an asset management arm",
   "Deep-pocketed family owner; acquisitive where Pictet is not."],
  ["EFG International", "Listed; anchored by BTG Pactual",
   "CHF 185bn AUM", "Wealth management",
   "Grows through hiring relationship managers - the purest organic model in "
   "the peer group."],
  ["Union Bancaire Privee", "Family-owned", "CHF 184.5bn client assets",
   "Wealth and asset management",
   "Explicitly acquisitive: 2025 growth of 19.5% was driven by acquisitions, "
   "the strategy Pictet refuses."],
  ["LGT", "Princely House of Liechtenstein", "CHF 386bn AUM",
   "Wealth and a large alternatives arm (LGT Capital Partners)",
   "The other great non-listed, family-anchored competitor, and strong exactly "
   "where Pictet is now pushing - private markets."]],
 "", ["13%", "14%", "16%", "24%", "33%"])}

<h2>Where Pictet is genuinely, checkably first or unusual</h2>
<ul class="plain">
<li><strong>Largest active thematic equity manager in the world by
assets.</strong> Not a claim about quality - a measurable position, as at June
2025.</li>
<li><strong>Roughly 50/50 wealth and institutional.</strong> Every named peer
above is heavily one or the other. This is the structural difference and it is
under-discussed.</li>
<li><strong>No investment bank at all.</strong> Not a small one - none. The CHF
8.0m trading book proves it.</li>
<li><strong>Partner-owned at this scale.</strong> Lombard Odier is the only
close comparison in Switzerland, and it is roughly a third of the size on
managed assets.</li>
<li><strong>Manufacturing and custody in one house.</strong> Pictet builds the
funds, runs the mandates, and holds the assets - and sells that custody
platform to outsiders as a fourth business.</li>
</ul>

<h2>The market Pictet is competing in</h2>
<p>Context worth having, because it explains the urgency behind everything in
Part 10:</p>
<ul class="plain">
<li>The number of Swiss private banks has fallen to <strong>79, from 156 in
2010</strong>. Banks below roughly CHF 10bn of assets face existential
cost pressure.</li>
<li>The <strong>median cost-income ratio rose to 78.2%</strong> from 75.6%.
Profitability across the sector sits below what investors expect.</li>
<li><strong>Swiss interest rates returned to 0%</strong>, removing the interest
income buffer that flattered 2023 and 2024 results across the whole
sector.</li>
<li>Regulatory cost layers and the global minimum tax are grinding margins
lower on every franc of assets.</li>
</ul>
{callout("key", "The one-line competitive summary",
 "Pictet is not the biggest in any single arena it competes in, and it has "
 "chosen a growth model - organic only, no acquisitions - that guarantees it "
 "never will be. Its bet is that being the only firm credible in all three "
 "arenas at once, with an ownership structure nobody can replicate, is worth "
 "more over decades than winning any one of them.")}
</section>'''


PART9 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 9</span>
<h1>What actually makes Pictet different</h1>
<p class="dek">Every candidate will say "independence, partnership, long-term
thinking, 220 years". Here is what those words mean when you attach numbers to
them - and, just as important, where the story is weak.</p></div>

<h2>The brochure answer versus the real answer</h2>
{table(["What the brochure says", "What it actually means, with the evidence"],
 [["&ldquo;We are independent&rdquo;",
   "There is no external shareholder to satisfy, so capital can be retained "
   "rather than distributed on a schedule. The total capital ratio is "
   "<b>21.6% against a 12% requirement</b> and liquidity coverage is "
   "<b>191% against 100%</b>. Roughly double what is asked in both cases. "
   "Independence here is a balance sheet fact, not a slogan."],
  ["&ldquo;We are a partnership&rdquo;",
   "Seven people own it, work in it, live in Geneva, retire at 65 and sell "
   "their stake at <b>book value</b>. Nobody can get rich by inflating the "
   "firm and selling out. That single rule removes the incentive behind most "
   "value destruction in finance."],
  ["&ldquo;We think long term&rdquo;",
   "The firm states it will soft-close successful strategies to protect "
   "returns - a deliberate sacrifice of fee income. And it has made "
   "essentially no acquisitions in 220 years while its sector consolidated "
   "from 156 banks to 79."],
  ["&ldquo;We have no conflicts of interest&rdquo;",
   "There is no investment bank, no corporate finance arm, no research to sell "
   "to issuers, and a trading book of <b>CHF 8.0m against CHF 42.9bn of total "
   "assets - 0.02%</b>. The claim is verifiable in the accounts, which is rare."],
  ["&ldquo;We are 220 years old&rdquo;",
   "True but almost the least interesting fact. The load-bearing date is "
   "<b>1980</b>, when the firm entered institutional asset management and "
   "stopped being only a private bank."]],
 "", ["26%", "74%"])}

<h2>The three things that are genuinely structural</h2>
<ol class="steps">
<li><strong>The dual engine.</strong> Wealth management is high-margin,
relationship-driven and people-heavy. Institutional asset management is
lower-margin, scalable and product-driven. Running both at similar size means
the fixed costs of research, risk and technology are spread across two revenue
pools whose flows do not move together - institutions and families rarely panic
in the same month. Nearly every competitor is 80-90% one or the other.</li>
<li><strong>Owning the plumbing.</strong> Pictet manufactures the funds, runs
the mandates <em>and</em> custodies the assets. Most rivals rent at least one
of those. It also means the group can sell the platform to third parties - CHF
256bn of external custody - turning a cost centre into a fourth business
line.</li>
<li><strong>Product invention as a habit.</strong> Emerging markets in 1991,
thematics in 1995, water in 2000, robotics in 2015. The firm's most profitable
franchises were all created rather than acquired, which is the only kind of
growth its ownership model permits.</li>
</ol>

<h2>The honest weaknesses - read these carefully</h2>
{callout("warn", "Where the story is soft", "",
 ["<b>Profit was flat in a record year.</b> CHF 667m against CHF 665m, "
  "despite record assets and near-doubled net new money. The rate cycle gave "
  "back everything the fee engine earned.",
  "<b>The cost-income ratio is middling.</b> 72.0% on Pictet's own basis, "
  "73.6% including depreciation and provisions - better than the 78.2% sector "
  "median but well behind Julius Baer's 67.6%. A partnership can afford this; "
  "it is still a gap.",
  "<b>Organic-only growth caps the rate.</b> Net new money of CHF 19bn on CHF "
  "724bn of opening assets is 2.6%. Respectable, not transformational, and "
  "there is no acquisition lever available to accelerate it.",
  "<b>The headline asset figure flatters.</b> CHF 599bn of the CHF 757bn is "
  "custody, and CHF 202bn of the gross figure is double-counted. Anyone who "
  "has read note 25 knows this.",
  "<b>The 2023 US settlement.</b> Banque Pictet entered a deferred prosecution "
  "agreement and paid USD 122.9m over 1,637 undeclared US accounts holding "
  "USD 5.6bn between 2008 and 2014, and was subsequently the subject of a "
  "Senate Finance Committee inquiry. The firm self-disclosed in 2014 and "
  "cooperated extensively - but a business whose product is trust does not get "
  "to treat this as ancient history.",
  "<b>The ETF push is late and small.</b> The first US active ETFs gathered "
  "roughly USD 72m and USD 12m in their early months. Entering a wrapper a "
  "decade after it started growing is defensible; being sub-scale in it is "
  "still a risk.",
  "<b>Style concentration.</b> The thematic franchise is structurally tilted "
  "towards growth equities and mid-caps. A prolonged value or large-cap regime "
  "hurts the firm's single most distinctive business disproportionately."])}

{callout("win", "How to use the weaknesses",
 "Do not lead with them and do not dwell. But if you are asked 'what worries "
 "you about Pictet?' or 'what would you change?', having a specific, "
 "numerate answer - the interest-rate dependency, or the sub-scale ETF "
 "position - is far stronger than praising the partnership again. It signals "
 "that you evaluated the firm rather than admired it.")}
</section>'''


PART10 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 10</span>
<h1>What is happening right now</h1>
<p class="dek">Pictet has been unusually busy since late 2025. Almost every
announcement falls into one of three pushes, and read together they describe a
firm responding to a specific commercial problem.</p></div>

<h2>The problem Pictet is solving</h2>
<p>Set the scene first, because the moves only make sense against it. Swiss
interest rates went back to zero, so the interest engine that flattered
2023 and 2024 across the whole sector switched off - visible in Pictet's own
15% drop in net interest result. Passive funds keep taking share from
traditional active management, compressing fees. Regulatory cost and the global
minimum tax grind margins lower. The sector's median cost-income ratio has
risen to 78.2%, and the number of Swiss private banks has halved since 2010.</p>
<p><strong>A firm that refuses to make acquisitions has exactly two levers in
that environment: charge more for something, or cost less to run.</strong>
Every move below is one of those two.</p>

{fig(diag_pushes(), 21, "The three strategic pushes of 2025-26")}

<h2>What each push actually means</h2>

<h3>Push one - private markets, and moving up the fee ladder</h3>
<p>This is the most important of the three and the most commonly
misunderstood. Pictet has invested in alternatives since 1989, so the news is
not that it is entering private markets. The news is <em>how</em> it is doing
it now. There is a ladder:</p>
{table(["Rung", "What Pictet does", "Roughly what it can charge"],
 [["Fund of funds", "Picks other managers' private equity funds",
   "Thin - a fee on top of someone else's fee"],
  ["Co-investment", "Invests alongside a lead manager in specific deals",
   "Better - and the sixth such fund raised USD 1.53bn in June 2026, the "
   "firm's largest"],
  ["Direct investment",
   "Buys control of companies itself. Entrepreneur Capital I closed at EUR "
   "403m in March 2026, taking majority stakes in founder- and family-owned "
   "B2B services and education businesses in the DACH region and the UK, led "
   "by Edmund Buckley. Five deals done: Pareto FM, Technology Services Group, "
   "QGroup, Tretor and one further holding.",
   "Full private equity economics - several times a long-only fee"],
  ["Direct real assets",
   "Buys buildings outright. The Zurich Marriott Hotel in June 2026, logistics "
   "platforms in the Netherlands and Germany with Stoneweg and Scantum, a "
   "Copenhagen development joint venture with Catella.",
   "Management fee plus performance, on assets with no daily price"]],
 "", ["16%", "56%", "28%"])}
{callout("key", "The read-through",
 "This is a <b>margin</b> strategy, not an asset-gathering strategy. EUR 403m "
 "is a rounding error against CHF 757bn. But a franc in a direct private "
 "equity fund earns several times what a franc in a long-only equity mandate "
 "earns, and it is locked up for years rather than redeemable on a bad "
 "Tuesday. Pictet is buying revenue quality, not revenue volume. If you can "
 "articulate that distinction, you will be ahead of almost everyone.")}

<h3>Push two - getting into the wrapper clients now want</h3>
<p>Pictet had essentially no ETF presence until October 2025, when it launched
its first three actively managed US ETFs. A fourth followed in February 2026,
two emerging market ETFs in April 2026, and - most significantly - a range of
five AI-enhanced active UCITS ETFs in Europe in April 2026, listed in Ireland
under the tickers PQUS, PQWD, PQEM, PQEU and PQWX.</p>
<p>The interesting detail is that these are not new investment capabilities.
They are the thirty-year-old <strong>Quest</strong> quantitative franchise put
into a new container. That is the whole logic of the active ETF boom: the
wrapper is what changed, not the investing. Pictet is late - the early US funds
had gathered only around USD 72m and USD 12m - but the strategic reasoning is
sound, because a firm that cannot be bought and cannot buy anyone must at least
be present wherever money is flowing.</p>

<h3>Push three - cost and geography</h3>
<p>Less glamorous, equally deliberate. A new financial technology hub in
Lisbon opened in May 2025 - a lower-cost engineering base than Geneva. The move
into the Campus Pictet de Rochemont consolidates 2,500 workplaces in Geneva and
cuts the annual carbon footprint of the firm's Geneva buildings from around 900
tonnes to 150. And in Asia, Kelvin Tay was appointed Chief Investment Officer
for Asia in July 2026, moving investment authority closer to the fastest-growing
pool of new wealth, with Singapore reinforced as the regional booking
centre alongside the Hong Kong branch.</p>

<h2>The full 2025-26 news ledger</h2>
{table(["Date", "Announcement", "Why it matters"],
 [["May 2025", "Lisbon financial technology hub opens", "Cost base"],
  ["Aug 2025", "First-half 2025 results: CHF 711bn of assets",
   "Assets dipped 2% on markets before recovering strongly in H2"],
  ["Sep 2025", "Dutch logistics platform 'Axis' launched with Stoneweg",
   "Direct real estate build-out"],
  ["Oct 2025", "First three US active ETFs launch", "New distribution wrapper"],
  ["Feb 2026", "Full-year 2025 results: record CHF 757bn, profit flat",
   "The headline year"],
  ["Feb 2026", "Fourth US ETF; Pareto Asset Management signed by Asset Services",
   "Third-party servicing wins"],
  ["Mar 2026", "EUR 403m Entrepreneur Capital I closes",
   "First direct private equity fund - a genuine first"],
  ["Mar 2026", "Catella joint venture in Copenhagen", "Development exposure"],
  ["Apr 2026", "Five AI-enhanced active UCITS ETFs in Europe; US EM ETFs",
   "The European ETF entry"],
  ["Apr 2026", "Viga joint venture expanded with Project Delta",
   "Real estate partnership model"],
  ["May-Jun 2026", "Logistics assets added in Kerpen and the Netherlands",
   "Platform build-out"],
  ["Jun 2026", "USD 1.53bn sixth private equity co-investment fund",
   "Largest PE raise the firm has done"],
  ["Jun 2026", "Zurich Marriott Hotel acquired",
   "Direct hospitality real estate, betting on constrained Swiss supply and "
   "rising visitor numbers"],
  ["Jul 2026", "USD 253m first environment co-investment fund",
   "Sustainability meets private markets"],
  ["Jul 2026", "Kelvin Tay appointed CIO Asia", "Asia investment leadership"]],
 "", ["12%", "46%", "42%"],
 "Half-year 2026 results had not been published as at 26 August 2026; on "
 "recent practice they are expected in late August or early September.")}
</section>'''


PART11 = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Part 11</span>
<h1>Interview toolkit</h1>
<p class="dek">Everything above, compressed into what you can actually deploy
in a conversation.</p></div>

<h2>The fifteen numbers to memorise</h2>
{table(["Number", "What it is"],
 [["CHF 757bn", "Assets under management or custody, 31 December 2025, up 4.5%"],
  ["CHF 19bn", "Net new money in 2025, up from CHF 11bn"],
  ["CHF 3.21bn", "Operating income, up 1.5%"],
  ["CHF 667m", "Consolidated profit - flat on 2024"],
  ["80%", "Share of income that is net commissions and services"],
  ["-15%", "Fall in the net interest result, the reason profit was flat"],
  ["72.0%", "Cost-income ratio (73.6% including depreciation and provisions)"],
  ["42.4 bps", "Revenue margin on assets - flattered down by custody assets"],
  ["CHF 8.0m", "Trading portfolio assets, against CHF 42.9bn of total assets"],
  ["21.6% / 191%", "Total capital ratio and liquidity coverage, against 12% "
   "and 100% requirements"],
  ["5,507", "Full-time equivalent staff; 31 offices in 20 countries"],
  ["285 / 267 / 36 / 256",
   "CHF bn in Wealth Management, Asset Management, Alternative Advisors "
   "(inside the other two) and third-party Asset Services custody"],
  ["7 and 42", "Managing Partners and Equity Partners"],
  ["USD 62bn / 16", "Thematic equity assets and number of strategies - the "
   "largest active thematic manager in the world"],
  ["1805 and 1980", "Founded; and the year it became an institutional asset "
   "manager, which matters more"]],
 "", ["24%", "76%"])}

<h2>Five things to say that most candidates will not</h2>
<ol class="steps">
<li><strong>"The 2025 result is a rates story, not a business story."</strong>
Record assets, near-doubled net new money, commissions up 4% - and profit
completely flat, because the net interest result fell 15% as Swiss rates went
back to zero. The fee engine worked; the rate engine handed the gains back.</li>
<li><strong>"The trading book is CHF 8m on a CHF 42.9bn balance
sheet."</strong> Two hundredths of one per cent. When Pictet says it has no
conflicts of interest, that is not a value statement, it is an accounting
fact.</li>
<li><strong>"The CHF 757bn is not comparable with Julius Baer's CHF
521bn."</strong> Pictet reports assets under management <em>or custody</em>;
CHF 599bn of it is custody and CHF 202bn of the gross figure is double-counted.
Knowing the composition shows you read the notes, not the press release.</li>
<li><strong>"The direct private equity move is about margin, not
scale."</strong> EUR 403m is immaterial against CHF 757bn. But it moves Pictet
from picking other people's funds to owning companies outright, which is
several times the fee rate on money that cannot run away.</li>
<li><strong>"Pictet is roughly half wealth and half institutional, and almost
nobody else is."</strong> That, not the 220 years, is the structural
difference. It dates from the 1980 Mellon joint venture in London.</li>
</ol>

<h2>Questions you could ask them</h2>
<ul class="plain">
<li>With rates back at zero, how much of the growth plan now has to come from
fee margin rather than asset growth - and is that what the private markets push
is for?</li>
<li>The firm has always grown organically. As the Swiss sector consolidates
from 156 banks to 79, does never acquiring start to become a competitive
disadvantage rather than a cultural strength?</li>
<li>The active ETF range launched in Europe this year is built on the Quest
franchise. Is the ambition to distribute existing capability more widely, or to
build genuinely new strategies in that wrapper?</li>
<li>Asset Services targets independent managers and says it wants to be the
finest rather than the biggest. Where does that stop being viable against the
scale of BNY or State Street?</li>
<li>How does a partnership where seven people must agree, and where partners
retire at 65, keep pace when a competitor can approve an acquisition in a
board meeting?</li>
</ul>

<h2>A two-minute "why Pictet" answer</h2>
{callout("dark", "Say something close to this",
 "Pictet interests me because it is two businesses that almost never sit "
 "together at this size. It is a 220-year-old Geneva private bank with CHF "
 "285bn for wealthy families, and it is a CHF 267bn institutional asset "
 "manager that happens to be the largest active thematic equity house in the "
 "world - and that second half only exists because of a joint venture in "
 "London in 1980. Underneath both sits its own custody platform, which it also "
 "sells to outsiders. What makes that combination hold together is the "
 "ownership: seven working partners, equal votes, retirement at 65, stakes "
 "sold at book value, so nobody can ever get rich by inflating the firm. You "
 "can see the consequences in the accounts - a 21.6% capital ratio against a "
 "12% requirement, and a trading book of CHF 8m on a CHF 43bn balance sheet. "
 "It is a firm that has chosen to compound slowly and refuse things, and I "
 "would rather learn the industry somewhere that has to be right over decades "
 "than somewhere that has to be right this quarter.")}

<h2>Likely questions, and the shape of a good answer</h2>
{table(["If they ask", "Go here"],
 [["What does Pictet do?",
   "The four business lines, but framed as the shape: half wealth, half "
   "institutional, on its own custody platform, with alternatives feeding "
   "both. Figure 14."],
  ["How does Pictet make money?",
   "80% net commissions, 13% net interest, 7% trading. Then the 2025 rates "
   "point, which is the interesting half of the answer."],
  ["What makes it different from Julius Baer or Lombard Odier?",
   "The institutional asset management half, and the thematic franchise. "
   "Julius Baer is a pure-play wealth manager; Lombard Odier is closer "
   "structurally but roughly a third the size on managed assets."],
  ["What is the biggest risk?",
   "Pick one and be specific: rate dependency, organic-only growth in a "
   "consolidating market, or style concentration in the thematic book."],
  ["What would you change?",
   "The sub-scale ETF position, or the cost-income gap to Julius Baer. Both "
   "are real, both are fixable, neither is disrespectful."],
  ["Why not a bigger firm?",
   "The ownership structure and what it does to time horizons. Use the "
   "soft-closing example - it is a checkable sacrifice of revenue."],
  ["Tell me something recent about the firm",
   "Entrepreneur Capital I, the first direct private equity fund, closed at "
   "EUR 403m in March 2026 - and explain the fee-ladder logic behind it."]],
 "", ["30%", "70%"])}
</section>'''


APPENDIX = lambda: f'''<section class="part">
<div class="parthead"><span class="pnum">Appendix</span>
<h1>Data notes, caveats and sources</h1></div>

<h2>What is a fact and what is a calculation</h2>
<ul class="plain">
<li><strong>Reported by Pictet:</strong> all balance sheet and income statement
figures, the asset breakdown in Figure 8, business line assets and headcount,
capital and liquidity ratios, office and staff counts, and every dated news
item.</li>
<li><strong>Calculated for this document:</strong> every ratio in the margin
table in Part 2 - revenue margin, cost-income, operating and net margin,
per-employee figures, returns on equity, organic growth rate and effective tax
rate. Pictet does not publish these. The workings are shown so they can be
checked.</li>
<li><strong>Estimated or approximate:</strong> the fee ranges in the client
table in Part 1 are industry norms, not Pictet disclosures. The currency
conversions in Figure 20 use an approximate rate.</li>
</ul>

<h2>Caveats that matter</h2>
<ul class="plain">
<li>Pictet does not disclose revenue or profit by business line. Any split of
profitability between wealth management and asset management is inference, not
fact, and this document deliberately does not attempt one.</li>
<li>Peer asset figures use each firm's own reporting basis and are not
like-for-like. This is flagged in Part 8 and is the single most common error in
casual comparisons.</li>
<li>Pictet Asset Management's assets are quoted at two dates on two bases: CHF
267bn at 31 December 2025 in the annual review, and USD 354bn at 30 June 2026
on the firm's own website. Both are correct; they are six months and one
currency apart.</li>
<li>Thematic assets of about USD 62bn across 16 strategies is the most recent
figure located; other public sources quote EUR 61bn across 17 strategies at
September 2024 and a USD 79bn figure for a wider thematic grouping. Treat it as
"around USD 60-80bn depending on definition".</li>
<li>Half-year 2026 results were not published as at the date of writing.</li>
</ul>

<h2>Sources</h2>
<p class="srcs"><b>Primary - Pictet</b></p>
<ul class="plain srcs">
<li>Pictet Group Annual Report 2025 (audited consolidated financial statements)
- pictet.com/content/dam/www/documents/publications/financial-reports/</li>
<li>Pictet Group Annual Review 2025-26 (business line figures, headcount,
partner list) - pictet.com/.../annual-review/2025/</li>
<li>"Pictet announces full-year results for 2025", 10 February 2026 -
pictet.com/corporate-news/release-full-year-2025-figures</li>
<li>"Release of first-half 2025 figures", 29 August 2025</li>
<li>Pictet media releases index, 2025 and 2026 -
pictet.com/corporate-news/media-releases</li>
<li>"Pictet raises over EUR 400m for first direct private equity strategy",
25 March 2026</li>
<li>Pictet &amp; Cie - 200 years of history (corporate history publication)</li>
<li>The Pictet Partners and Partnership Model; "Succession without DNA";
Marc Pictet interview, WIR Magazin, July 2026; "Ninth-generation Pictet leader
banks on organic growth and partnerships"</li>
<li>Pictet Asset Management: Thematics capability page; "Reflecting on 30 years
of active thematic equities"; Secular Outlook 2026; Annual outlook for 2026;
About us - am.pictet.com</li>
<li>Pictet Asset Services - pictet.com/asset-services; Campus Pictet de
Rochemont - campus.pictet.com</li>
<li>Pictet sustainability report and climate action plan; Net Zero Asset
Managers initiative signatory page</li>
</ul>
<p class="srcs"><b>Peers, market and press</b></p>
<ul class="plain srcs">
<li>Julius Baer Group 2025 full-year results - juliusbaer.com</li>
<li>Lombard Odier full-year 2025 results, 19 February 2026 -
lombardodier.com</li>
<li>Union Bancaire Privee annual results 2025 - ubp.com; EFG International
full-year 2025; Vontobel full-year report 2025; J. Safra Sarasin 2025 media
release; LGT financial results 2026</li>
<li>UBS quarterly results and Global Wealth Report 2026 - ubs.com</li>
<li>KPMG "Clarity on Swiss Private Banks"; PwC Switzerland Private Banking
Market Update 2026; EY Banking Barometer 2026; Swiss Banking Outlook 2026</li>
<li>ZHAW Wealth Management Blog, largest Swiss private banks by AUM 2025</li>
<li>US Department of Justice, "Swiss Private Bank Banque Pictet Admits to
Conspiring with U.S. Taxpayers", 4 December 2023; US Senate Finance Committee
inquiry announcement; CNBC, Forbes and Banking Dive coverage</li>
<li>QuotedData, "Pictet enters active ETF market with five AI-enhanced funds",
April 2026; ETFGI, Pictet emerging market ETF launches, April 2026; Waystone
UCITS ETF range announcement</li>
<li>finews.com and finews.asia results coverage; Private Banker International;
WealthBriefing; Institutional Investor, "For Swiss Bank Pictet, Thematic
Investing Pays Off"</li>
<li>Baker McKenzie newsroom, Zurich Marriott acquisition, June 2026</li>
<li>INSEAD case study, "Banque Pictet &amp; Cie SA: A Family-Run Firm with a
Unique Co-Evolution"</li>
</ul>

{callout("", "A closing note on how to use this",
 "Nothing here is confidential and none of it is hard to find - but almost "
 "nobody assembles it. The advantage is not in knowing a secret; it is in "
 "having done the arithmetic, read note 25, noticed the trading book, and "
 "connected the house view to the corporate strategy. That is what reads as "
 "genuine interest rather than preparation.")}
</section>'''


def main():
    fonts = open(os.path.join(BASE, "fonts_embedded.css")).read()
    body = "".join([cover(), contents(), PART1(), PART2(), PART3(), PART4(),
                    PART5(), PART6(), PART7(), PART8(), PART9(), PART10(),
                    PART11(), APPENDIX()])
    doc = ("<!doctype html><html lang='en'><head><meta charset='utf-8'>"
           "<title>Pictet - A Ground-Up Business Guide</title>"
           f"<style>{fonts}</style><style>{CSS}</style></head>"
           f"<body>{body}</body></html>")
    out = os.path.join(BASE, "pictet_guide.html")
    open(out, "w").write(doc)
    print("wrote", out, len(doc), "bytes")


if __name__ == "__main__":
    main()
