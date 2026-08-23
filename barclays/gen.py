# -*- coding: utf-8 -*-
"""Chart generator for the Barclays business-model report."""
import html, re

C = {
    'buk':  '#00AEEF',
    'ukcb': '#0F6FB5',
    'pbwm': '#00B39A',
    'ib':   '#16375C',
    'uscb': '#EF9B20',
    'ho':   '#9AA6B4',
    'ink':  '#0B1F35',
    'mut':  '#5B6B7F',
    'grid': '#DCE3EA',
    'red':  '#C1553B',
    'grn':  '#1E7A5E',
    'pale': '#EEF4F9',
}
F = 'Helvetica, Arial, sans-serif'


def esc(s):
    return html.escape(str(s))


def _t(x, y, s, size=11, fill=None, anchor='start', weight='400', ls='0'):
    fill = fill or C['ink']
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{F}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
            f'letter-spacing="{ls}">{esc(s)}</text>')


def _wrap(text, maxchars):
    words, lines, cur = text.split(), [], ''
    for wd in words:
        trial = (cur + ' ' + wd).strip()
        if len(trial) > maxchars and cur:
            lines.append(cur); cur = wd
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def _svg(w, h, body, title=None, sub=None):
    head = ''
    top = 0
    if title:
        head += _t(0, 14, title, 13.5, C['ink'], weight='700')
        top = 20
    if sub:
        base = top
        lines = _wrap(sub, int(w / 5.35))
        for i, ln in enumerate(lines):
            head += _t(0, base + 13 + i * 13, ln, 10.5, C['mut'])
        top = base + 13 * len(lines) + 8
    inner = f'<g transform="translate(0,{top})">{body}</g>' if top else body
    return (f'<svg class="chart" viewBox="0 0 {w} {h + top}" width="100%" '
            f'preserveAspectRatio="xMidYMid meet" role="img">{head}{inner}</svg>')


def hbar(rows, unit='', title=None, sub=None, w=720, rowh=30, labw=200,
         valw=96, fmt=lambda v: f'{v:,.0f}', vmax=None, ref=None, reflabel=None):
    """rows = [(label, value, colour), ...]"""
    plot_x = labw
    plot_w = w - labw - valw
    vmax = vmax or max(r[1] for r in rows) * 1.02
    h = rowh * len(rows) + 10
    b = []
    if ref is not None:
        rx = plot_x + plot_w * ref / vmax
        b.append(f'<line x1="{rx:.1f}" y1="0" x2="{rx:.1f}" y2="{rowh*len(rows):.1f}" '
                 f'stroke="{C["red"]}" stroke-width="1.2" stroke-dasharray="4 3"/>')
        if reflabel:
            b.append(_t(rx, rowh * len(rows) + 13, reflabel, 9.5, C['red'], anchor='middle'))
    for i, (lab, val, col) in enumerate(rows):
        y = i * rowh
        bw = max(1.5, plot_w * val / vmax)
        b.append(f'<rect x="{plot_x}" y="{y+6}" width="{bw:.1f}" height="{rowh-14}" '
                 f'rx="2" fill="{col}"/>')
        b.append(_t(plot_x - 10, y + rowh / 2 + 3.5, lab, 11, C['ink'], anchor='end'))
        b.append(_t(plot_x + bw + 8, y + rowh / 2 + 3.5, fmt(val) + unit, 11,
                    C['ink'], weight='700'))
    return _svg(w, h, ''.join(b), title, sub)


def butterfly(rows, title=None, sub=None, w=720, rowh=32, labband=200):
    """rows = [(label, left_pct, right_pct, colour)] -- left=capital, right=income."""
    mid = w / 2
    lax = mid - labband / 2
    rax = mid + labband / 2
    lspan = lax - 40
    rspan = w - rax - 40
    m = max(max(r[1] for r in rows), max(r[2] for r in rows)) * 1.06
    top = 20
    h = rowh * len(rows) + top + 8
    b = [_t(lax, 10, 'SHARE OF GROUP CAPITAL (RWAs)', 8.6, C['mut'], anchor='end', weight='700', ls='0.7'),
         _t(rax, 10, 'SHARE OF GROUP INCOME', 8.6, C['mut'], weight='700', ls='0.7')]
    for i, (lab, lv, rv, col) in enumerate(rows):
        y = i * rowh + top
        lw = lspan * lv / m
        rw = rspan * rv / m
        b.append(f'<rect x="{lax-lw:.1f}" y="{y+5}" width="{lw:.1f}" height="{rowh-14}" '
                 f'rx="2" fill="{col}" opacity="0.40"/>')
        b.append(f'<rect x="{rax}" y="{y+5}" width="{rw:.1f}" height="{rowh-14}" '
                 f'rx="2" fill="{col}"/>')
        b.append(_t(mid, y + rowh / 2 + 2.5, lab, 10.2, C['ink'], anchor='middle', weight='700'))
        b.append(_t(lax - lw - 7, y + rowh / 2 + 2.5, f'{lv:.0f}%', 10, C['mut'],
                    anchor='end', weight='700'))
        b.append(_t(rax + rw + 7, y + rowh / 2 + 2.5, f'{rv:.0f}%', 10, C['ink'], weight='700'))
    b.append(f'<line x1="{lax}" y1="{top}" x2="{lax}" y2="{h-6}" stroke="{C["grid"]}" stroke-width="1"/>')
    b.append(f'<line x1="{rax}" y1="{top}" x2="{rax}" y2="{h-6}" stroke="{C["grid"]}" stroke-width="1"/>')
    return _svg(w, h, ''.join(b), title, sub)


def bubbles(pts, title=None, sub=None, w=720, h=330):
    """pts = [(label, rwa_bn, rote_pct, income_m, colour)]"""
    ml, mr, mt, mb = 52, 122, 28, 40
    px, pw, py, ph = ml, w - ml - mr, mt, h - mt - mb
    xmax, ymax = 220.0, 30.0
    b = []
    for gv in range(0, 31, 5):
        gy = py + ph - ph * gv / ymax
        b.append(f'<line x1="{px}" y1="{gy:.1f}" x2="{px+pw}" y2="{gy:.1f}" stroke="{C["grid"]}" stroke-width="0.8"/>')
        b.append(_t(px - 8, gy + 3.5, f'{gv}%', 9.5, C['mut'], anchor='end'))
    for gv in range(0, 221, 50):
        gx = px + pw * gv / xmax
        b.append(f'<line x1="{gx:.1f}" y1="{py}" x2="{gx:.1f}" y2="{py+ph}" stroke="{C["grid"]}" stroke-width="0.8"/>')
        b.append(_t(gx, py + ph + 16, f'£{gv}bn', 9.5, C['mut'], anchor='middle'))
    ty = py + ph - ph * 12 / ymax
    b.append(f'<line x1="{px}" y1="{ty:.1f}" x2="{px+pw}" y2="{ty:.1f}" stroke="{C["red"]}" stroke-width="1.2" stroke-dasharray="4 3"/>')
    b.append(_t(px + pw, py - 8, 'dashed line = Group 2026 target of RoTE > 12%', 9.5, C['red'], anchor='end', weight='700'))
    for lab, rwa, rote, inc, col in pts:
        cx = px + pw * rwa / xmax
        cy = py + ph - ph * rote / ymax
        r = max(7.0, (inc / 29140.0) ** 0.5 * 62)
        b.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{col}" opacity="0.72"/>')
        b.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="none" stroke="{col}" stroke-width="1.2"/>')
        b.append(_t(cx + r + 6, cy + 3.5, lab, 10, C['ink'], weight='700'))
    b.append(_t(px, py + ph + 33, 'Capital consumed  →  risk weighted assets (£bn)', 9.5, C['mut'], weight='700'))
    b.append(_t(px + pw, py + ph + 33, 'bubble size = income', 9, C['mut'], anchor='end'))
    return _svg(w, h, ''.join(b), title, sub)


def grouped_bars(cats, series, title=None, sub=None, w=720, h=250, unit='%',
                 fmt=lambda v: f'{v:.1f}'):
    """cats=[labels]; series=[(name, [vals], colour)]"""
    ml, mr, mt, mb = 42, 12, 26, 44
    px, pw, py, ph = ml, w - ml - mr, mt, h - mt - mb
    vmax = max(v for _, vals, _ in series for v in vals) * 1.16
    n = len(series)
    slot = pw / len(cats)
    bw = min(28.0, (slot - 16) / n)
    b = []
    for i in range(0, 6):
        gv = vmax * i / 5
        gy = py + ph - ph * gv / vmax
        b.append(f'<line x1="{px}" y1="{gy:.1f}" x2="{px+pw}" y2="{gy:.1f}" stroke="{C["grid"]}" stroke-width="0.8"/>')
        b.append(_t(px - 7, gy + 3.5, f'{gv:.0f}', 9, C['mut'], anchor='end'))
    for ci, cat in enumerate(cats):
        base = px + slot * ci + (slot - bw * n) / 2
        for si, (nm, vals, col) in enumerate(series):
            v = vals[ci]
            bh = ph * v / vmax
            x = base + si * bw
            b.append(f'<rect x="{x:.1f}" y="{py+ph-bh:.1f}" width="{bw-3:.1f}" height="{bh:.1f}" rx="1.5" fill="{col}"/>')
            b.append(_t(x + (bw - 3) / 2, py + ph - bh - 5, fmt(v), 8.6, C['ink'], anchor='middle', weight='700'))
        b.append(_t(px + slot * ci + slot / 2, py + ph + 15, cat, 9.6, C['ink'], anchor='middle'))
    lx = px
    for nm, _, col in series:
        b.append(f'<rect x="{lx}" y="{py+ph+26}" width="9" height="9" rx="1.5" fill="{col}"/>')
        b.append(_t(lx + 13, py + ph + 34, nm, 9.4, C['mut']))
        lx += 16 + len(nm) * 5.3
    return _svg(w, h, ''.join(b), title, sub)


def stacked_tree(title=None, sub=None, w=720):
    """Investment Bank income decomposition, FY2025."""
    rows = [
        ('Global Markets', 8654, C['ib'], [
            ('FICC — rates, credit, FX, commodities, securitised', 5429),
            ('Equities — cash, derivatives, prime/financing', 3225)]),
        ('Investment Banking', 4401, C['ukcb'], [
            ('Debt Capital Markets + leveraged finance', 1510),
            ('Advisory (M&A)', 676),
            ('Equity Capital Markets', 278),
            ('International Corporate Bank (transaction banking)', 1937)]),
    ]
    total = 13055
    b, y = [], 0
    barx, barw = 300, 300
    for nm, val, col, subs in rows:
        b.append(_t(0, y + 13, nm, 11.5, C['ink'], weight='700'))
        b.append(_t(0, y + 27, f'£{val:,}m  ·  {val/total*100:.0f}% of IB income', 9.6, C['mut']))
        b.append(f'<rect x="{barx}" y="{y+2}" width="{barw*val/total:.1f}" height="20" rx="2" fill="{col}"/>')
        y += 36
        for snm, sval in subs:
            b.append(_t(16, y + 11, '·  ' + snm, 10, C['mut']))
            b.append(f'<rect x="{barx}" y="{y+2}" width="{barw*sval/total:.1f}" height="13" rx="1.5" fill="{col}" opacity="0.45"/>')
            b.append(_t(barx + barw * sval / total + 7, y + 12, f'£{sval:,}m', 9.4, C['ink'], weight='700'))
            y += 20
        y += 10
    return _svg(w, y, ''.join(b), title, sub)


def timeline(events, title=None, sub=None, w=720):
    """events = [(year, headline, detail)]"""
    rowh = 46
    h = rowh * len(events) + 6
    axis = 74
    b = [f'<line x1="{axis}" y1="6" x2="{axis}" y2="{h-16}" stroke="{C["grid"]}" stroke-width="2"/>']
    for i, (yr, head, det) in enumerate(events):
        y = i * rowh + 14
        b.append(f'<circle cx="{axis}" cy="{y}" r="5" fill="{C["buk"]}"/>')
        b.append(f'<circle cx="{axis}" cy="{y}" r="9" fill="none" stroke="{C["buk"]}" stroke-width="1" opacity="0.35"/>')
        b.append(_t(axis - 18, y + 4, yr, 11.5, C['ink'], anchor='end', weight='700'))
        b.append(_t(axis + 18, y - 1, head, 11, C['ink'], weight='700'))
        b.append(_t(axis + 18, y + 13, det, 9.8, C['mut']))
    return _svg(w, h, ''.join(b), title, sub)


def pyramid(tiers, title=None, sub=None, w=720, h=300):
    """tiers = [(label, right_text, colour)] top -> bottom"""
    n = len(tiers)
    th = (h - 20) / n
    cx = 232
    b = []
    for i, (lab, right, col) in enumerate(tiers):
        y = i * th
        wtop = 60 + (cx * 2 - 60) * i / n
        wbot = 60 + (cx * 2 - 60) * (i + 1) / n
        pts = f'{cx-wtop/2:.1f},{y:.1f} {cx+wtop/2:.1f},{y:.1f} {cx+wbot/2:.1f},{y+th-4:.1f} {cx-wbot/2:.1f},{y+th-4:.1f}'
        b.append(f'<polygon points="{pts}" fill="{col}" opacity="0.9"/>')
        b.append(_t(cx, y + th / 2 + 2, lab, 10.4, '#ffffff', anchor='middle', weight='700'))
        b.append(_t(cx + wbot / 2 + 16, y + th / 2 + 2, right, 9.8, C['mut']))
    return _svg(w, h, ''.join(b), title, sub)


def steps(points, title=None, sub=None, w=720, h=240):
    """points = [(label, value, note, is_target)]"""
    ml, mr, mt, mb = 44, 22, 16, 48
    px, pw, py, ph = ml, w - ml - mr, mt, h - mt - mb
    raw = max(p[1] for p in points) * 1.18
    stepv = max(1, int(round(raw / 6.0)))
    ticks = 6
    vmax = stepv * ticks
    n = len(points)
    xs = [px + pw * (i + 0.5) / n for i in range(n)]
    b = []
    for k in range(ticks + 1):
        gv = stepv * k
        gy = py + ph - ph * gv / vmax
        b.append(f'<line x1="{px}" y1="{gy:.1f}" x2="{px+pw}" y2="{gy:.1f}" stroke="{C["grid"]}" stroke-width="0.8"/>')
        b.append(_t(px - 7, gy + 3.5, f'{gv}%', 9, C['mut'], anchor='end'))
    path = ' '.join(f'{"M" if i==0 else "L"}{xs[i]:.1f},{py+ph-ph*points[i][1]/vmax:.1f}' for i in range(n))
    b.append(f'<path d="{path}" fill="none" stroke="{C["buk"]}" stroke-width="2.4"/>')
    for i, (lab, val, note, tgt) in enumerate(points):
        x, y = xs[i], py + ph - ph * val / vmax
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{"#ffffff" if tgt else C["buk"]}" stroke="{C["buk"]}" stroke-width="2.4"/>')
        b.append(_t(x, y - 13, f'{val:.1f}%', 10.6, C['ink'], anchor='middle', weight='700'))
        b.append(_t(x, py + ph + 17, lab, 10, C['ink'], anchor='middle', weight='700'))
        b.append(_t(x, py + ph + 30, note, 8.8, C['mut'], anchor='middle'))
    b.append(_t(px, py + ph + 46, 'Hollow markers are targets, not results.', 8.8, C['mut']))
    return _svg(w, h, ''.join(b), title, sub)


def orgchart(w=720):
    """Barclays PLC legal + divisional structure."""
    b = []
    def box(x, y, bw, bh, t1, t2, fill, stroke, tcol='#ffffff', s1=11, s2=8.8):
        b.append(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="4" fill="{fill}" stroke="{stroke}" stroke-width="1"/>')
        b.append(_t(x + bw / 2, y + (bh / 2 - 3 if t2 else bh / 2 + 3.5), t1, s1, tcol, anchor='middle', weight='700'))
        if t2:
            b.append(_t(x + bw / 2, y + bh / 2 + 11, t2, s2, tcol, anchor='middle'))
    def link(x1, y1, x2, y2):
        my = (y1 + y2) / 2
        b.append(f'<path d="M{x1:.1f},{y1:.1f} L{x1:.1f},{my:.1f} L{x2:.1f},{my:.1f} L{x2:.1f},{y2:.1f}" fill="none" stroke="{C["grid"]}" stroke-width="1.6"/>')

    box(250, 0, 220, 40, 'Barclays PLC', 'Listed holding company (LSE / NYSE)', C['ink'], C['ink'])
    link(360, 40, 175, 74); link(360, 40, 545, 74)
    box(30, 74, 290, 42, 'Barclays Bank UK PLC', 'RING-FENCED · UK retail + smaller business', C['buk'], C['buk'])
    box(400, 74, 290, 42, 'Barclays Bank PLC', 'NON-RING-FENCED · international + markets', C['ib'], C['ib'])

    b.append(f'<line x1="360" y1="60" x2="360" y2="330" stroke="{C["red"]}" stroke-width="1.4" stroke-dasharray="6 4" opacity="0.55"/>')
    b.append(_t(360, 340, 'the ring-fence — capital, funding and boards kept legally separate', 9, C['red'], anchor='middle', weight='700'))

    y0 = 150
    box(30, y0, 290, 34, 'Barclays UK', '', C['pale'], C['buk'], C['ink'], 11)
    box(30, y0 + 42, 290, 34, 'Barclays UK Corporate Bank', '', C['pale'], C['ukcb'], C['ink'], 11)
    box(400, y0, 290, 34, 'Barclays Investment Bank', '', C['pale'], C['ib'], C['ink'], 11)
    box(400, y0 + 42, 290, 34, 'Barclays US Consumer Bank', '', C['pale'], C['uscb'], C['ink'], 11)
    box(215, y0 + 100, 290, 34, 'Private Bank & Wealth Management', '', C['pale'], C['pbwm'], C['ink'], 11)
    link(175, 116, 175, y0); link(175, 116, 175, y0 + 42)
    link(545, 116, 545, y0); link(545, 116, 545, y0 + 42)
    b.append(_t(360, y0 + 158, 'PB&WM straddles the fence — UK wealth sits inside it, international private banking outside', 9, C['mut'], anchor='middle'))
    return _svg(w, 366, ''.join(b),
                'How Barclays is put together',
                'Two banks under one holding company, five reporting divisions')


def engines(w=720):
    """The two income engines."""
    b = []
    b.append(f'<rect x="0" y="0" width="342" height="200" rx="6" fill="{C["pale"]}" stroke="{C["buk"]}" stroke-width="1.2"/>')
    b.append(f'<rect x="378" y="0" width="342" height="200" rx="6" fill="#F4F1EC" stroke="{C["uscb"]}" stroke-width="1.2"/>')
    b.append(_t(18, 24, 'ENGINE 1 — NET INTEREST INCOME', 10.5, C['buk'], weight='700', ls='0.6'))
    b.append(_t(18, 44, '£16.0bn', 21, C['ink'], weight='700'))
    b.append(_t(112, 44, 'FY2025 · ~55% of income', 9.6, C['mut']))
    for i, ln in enumerate([
        'Take deposits at a low rate. Lend at a higher one.',
        'Keep the spread. Barclays holds ~£430bn of customer',
        'deposits, much of it paying little or nothing.',
        '',
        'The structural hedge: Barclays parks a rolling ~5-year',
        'ladder of swaps/gilts against deposits that pay no',
        'interest. As old low-rate tranches mature and reprice',
        'into today’s higher rates, income rises mechanically —',
        'even if the Bank of England is cutting. This is the',
        'single biggest reason UK bank earnings keep climbing.',
    ]):
        b.append(_t(18, 70 + i * 12.8, ln, 9.6, C['ink'] if i in (4,) else C['mut']))
    b.append(_t(396, 24, 'ENGINE 2 — FEES, COMMISSIONS & TRADING', 10.5, C['uscb'], weight='700', ls='0.6'))
    b.append(_t(396, 44, '£13.1bn', 21, C['ink'], weight='700'))
    b.append(_t(490, 44, 'FY2025 · ~45% of income', 9.6, C['mut']))
    for i, ln in enumerate([
        'Charge for doing something, not for lending money.',
        '',
        '· Trading spreads — buy at the bid, sell at the offer,',
        '  thousands of times a day, for institutional clients.',
        '· Underwriting fees — a % of every bond or share issue.',
        '· Advisory fees — a % of M&A deal value, paid on close.',
        '· Transaction-banking and card interchange fees.',
        '· Management fees on private-bank assets.',
        '',
        'Higher margin, no capital tied up in loans — but cyclical.',
    ]):
        b.append(_t(396, 70 + i * 12.8, ln, 9.6, C['mut']))
    return _svg(w, 208, ''.join(b),
                'The two ways Barclays turns a balance sheet into revenue',
                'Every line of every division reduces to one of these two, or a blend')


def treemap(w=720, h=360):
    """Group income FY2025 as area. Five operating divisions; Head Office excluded."""
    D = [
        ('Investment Bank', 13055, C['ib'], 'Trading, advisory, bond & share issuance,\ntransaction banking for multinationals'),
        ('Barclays UK', 8708, C['buk'], 'Current accounts, mortgages,\nBarclaycard, Tesco Bank'),
        ('US Consumer Bank', 3681, C['uscb'], 'American co-brand\ncredit cards'),
        ('UK Corporate Bank', 2064, C['ukcb'], 'SME and mid-cap\nbanking'),
        ('Private Bank\n& Wealth', 1380, C['pbwm'], 'Wealthy individuals\nand families'),
    ]
    tot = sum(d[1] for d in D)
    g = 3
    b = []

    def cell(x, y, bw, bh, name, val, col, desc, big):
        b.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" rx="3" fill="{col}"/>')
        tight = (not big) and bw < 115
        pad = 8 if tight else 11
        nf = 13 if big else (9.0 if tight else 10.8)
        vf = 17 if big else (11.5 if tight else 13)
        lh = 15 if big else (11 if tight else 12.5)
        ty = last = y + pad + (13 if big else 11)
        for i, ln in enumerate(name.split('\n')):
            b.append(_t(x + pad, ty + i * lh, ln, nf, '#ffffff', weight='700'))
            last = ty + i * lh
        b.append(_t(x + pad, last + (22 if big else 18), f'£{val:,}m', vf, '#ffffff', weight='700'))
        share = f'{val/tot*100:.1f}%' if tight else f'{val/tot*100:.1f}% of income'
        b.append(_t(x + pad, last + (39 if big else 31), share, 8.6 if tight else 9.4,
                    '#ffffff', ls='0.4'))
        if big:
            for i, ln in enumerate(desc.split('\n')):
                b.append(_t(x + pad, y + bh - 26 + i * 12, ln, 9.4, '#ffffff'))

    # Left column: the Investment Bank, full height.
    wA = (w - g) * D[0][1] / tot
    cell(0, 0, wA, h, D[0][0], D[0][1], D[0][2], D[0][3], True)
    # Right column: Barclays UK on top, three smaller divisions beneath.
    xB, wB = wA + g, w - wA - g
    hTop = (h - g) * D[1][1] / (tot - D[0][1])
    cell(xB, 0, wB, hTop, D[1][0], D[1][1], D[1][2], D[1][3], True)
    yBot, hBot = hTop + g, h - hTop - g
    rest = sum(d[1] for d in D[2:])
    x = xB
    for nm, val, col, desc in D[2:]:
        cw = (wB - 2 * g) * val / rest
        cell(x, yBot, cw, hBot, nm, val, col, desc, False)
        x += cw + g
    return _svg(w, h, ''.join(b),
                'The whole firm, drawn to scale',
                'Every box is one division. Box AREA = share of the £29.1bn of FY2025 income. This is the answer to "which division is biggest".')


def ladder(w=720):
    """The Barclays wealth ladder, entry threshold by tier."""
    T = [
        ('GoHenry', 'ages 6–18', 'Kids’ money app. £180m acquisition announced June 2026,\ncompleting Q4 2026. ~500,000 UK children.', C['ho']),
        ('Barclays UK', 'everyday banking', 'Current account, savings, mortgage. ~20 million customers —\nthe top of the funnel for everything above.', C['buk']),
        ('Premier Banking', '£75k income or £100k held', 'Mass-affluent tier. Relationship banking, preferential rates,\nand the recruiting ground for the wealth business.', C['ukcb']),
        ('Premier Wealth Management', '£150k to invest', 'Launched April 2026. Dedicated planning and advice,\nno upfront fee for the initial review.', C['pbwm']),
        ('Private Bank — UK', '~£3m investable', 'Dedicated private banker, discretionary and advisory\nportfolios, bespoke lending, trusts and estate planning.', C['pbwm']),
        ('Private Banking — International', '£5m+ investable', 'Booked in Switzerland, Monaco, the Crown Dependencies\nand, from 2026, Singapore. Cross-border families.', C['ib']),
    ]
    rowh, h = 62, 62 * len(T) + 8
    b = []
    for i, (nm, thr, desc, col) in enumerate(T):
        y = h - (i + 1) * rowh
        step_w = 130 + i * 26
        b.append(f'<rect x="0" y="{y:.1f}" width="{step_w}" height="{rowh-6}" rx="3" fill="{col}"/>')
        cap = int((step_w - 20) / 5.5)
        b.append(_t(10, y + 22, nm if len(nm) <= cap else nm[:cap - 1] + '…', 10.4, '#ffffff', weight='700'))
        b.append(_t(10, y + 37, thr, 9.2, '#ffffff'))
        for j, ln in enumerate(desc.split('\n')):
            b.append(_t(step_w + 16, y + 20 + j * 13, ln, 9.6, C['mut']))
        b.append(_t(w - 2, y + 22, f'TIER {len(T)-i}', 8.4, C['grid'], anchor='end', weight='700', ls='1.2'))
    return _svg(w, h, ''.join(b),
                'The wealth ladder — every rung is a Barclays product',
                'Read bottom to top. No competitor owns this many rungs, and that is the whole commercial argument.')


def assets_stack(w=720):
    """FY2025 client assets and liabilities, decomposed. Invested-asset components first."""
    parts = [('Assets under supervision', 87.7, C['pbwm'], 'advised / overseen'),
             ('Assets under management', 52.9, C['ib'], 'discretionary — fee-richest'),
             ('Deposits', 72.0, C['buk'], 'cash held with the bank'),
             ('Lending', 14.7, C['uscb'], 'secured')]
    tot = sum(p[1] for p in parts)
    invested = parts[0][1] + parts[1][1]
    y = 34
    b = [_t(0, 16, 'CLIENT ASSETS & LIABILITIES  ·  £227.6bn as reported', 12, C['ink'],
            weight='700', ls='0.4')]
    x = 0
    for i, (nm, v, col, note) in enumerate(parts):
        cw = w * v / tot
        narrow = cw < 95
        b.append(f'<rect x="{x:.1f}" y="{y}" width="{cw-2:.1f}" height="42" rx="3" fill="{col}"/>')
        b.append(_t(x + (6 if narrow else 10), y + 19, f'£{v:.1f}bn', 10 if narrow else 12.5,
                    '#ffffff', weight='700'))
        b.append(_t(x + (6 if narrow else 10), y + 33, f'{v/tot*100:.0f}%', 8.6 if narrow else 9.2, '#ffffff'))
        last = (i == len(parts) - 1)
        cx = w if last else x
        b.append(_t(cx, y + 60, nm, 9.8, C['ink'], weight='700', anchor='end' if last else 'start'))
        b.append(_t(cx, y + 72, note, 8.8, C['mut'], anchor='end' if last else 'start'))
        x += cw
    iw = w * invested / tot
    b.append(f'<path d="M0,{y+86} L0,{y+92} L{iw-2:.1f},{y+92} L{iw-2:.1f},{y+86}" fill="none" stroke="{C["pbwm"]}" stroke-width="1.8"/>')
    b.append(_t(iw / 2, y + 107, 'INVESTED ASSETS £140.6bn — the number that earns fees', 9.4,
                C['pbwm'], anchor='middle', weight='700'))
    return _svg(w, 152, ''.join(b),
                'Three different asset numbers, and why people confuse them',
                'Barclays quotes AUM, assets under supervision and client assets & liabilities. They mean different things and only one of them is the fee engine. FY2025 figures; components sum to £227.3bn against £227.6bn reported.')


def revmodel(w=720):
    """How PB&WM earns its £1,380m."""
    b = []
    b.append(f'<rect x="0" y="0" width="352" height="188" rx="6" fill="{C["pale"]}" stroke="{C["buk"]}" stroke-width="1.2"/>')
    b.append(f'<rect x="368" y="0" width="352" height="188" rx="6" fill="#EDF9F7" stroke="{C["pbwm"]}" stroke-width="1.2"/>')
    b.append(_t(18, 24, 'INTEREST — 58% OF INCOME', 10.4, C['buk'], weight='700', ls='0.6'))
    b.append(_t(18, 48, '£799m', 22, C['ink'], weight='700'))
    for i, ln in enumerate([
        'Wealthy clients hold a lot of cash. The division held',
        '£72.0bn of deposits against just £14.7bn of lending —',
        'a five-to-one surplus it passes to the wider group.',
        '',
        'Lending is secured against portfolios and property,',
        'structured case by case. Credit losses are close to',
        'zero: FY2025 booked an £8m impairment RELEASE.',
        '',
        'Rate-sensitive, so it falls as rates fall.',
    ]):
        b.append(_t(18, 74 + i * 12.6, ln, 9.5, C['mut']))
    b.append(_t(386, 24, 'FEES — 42% OF INCOME', 10.4, '#007F6E', weight='700', ls='0.6'))
    b.append(_t(386, 48, '£581m', 22, C['ink'], weight='700'))
    for i, ln in enumerate([
        'Charged as a percentage of invested assets, roughly',
        '0.50%–1.45% a year, billed whether markets rise or fall.',
        '',
        'Three kinds (H1 2024 disclosure, £234m total):',
        '·  Advisory and management fees — £156m',
        '·  Brokerage and execution — £62m',
        '·  Transactional banking fees — £16m',
        '',
        'Recurring, capital-light, and what investors pay up for.',
    ]):
        b.append(_t(386, 74 + i * 12.6, ln, 9.5, C['mut']))
    return _svg(w, 196, ''.join(b),
                'How the wealth division earns its £1,380m',
                'FY2025. The split matters: interest income is rate-driven and shrinking in importance; fee income is what the strategy is chasing.')
