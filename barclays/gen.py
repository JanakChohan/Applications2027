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
    vmax = 18.0
    n = len(points)
    xs = [px + pw * (i + 0.5) / n for i in range(n)]
    b = []
    for gv in range(0, 19, 3):
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
