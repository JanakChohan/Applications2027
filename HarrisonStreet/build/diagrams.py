from svg import *

def d_onepicture():
    b = []
    b.append(box(10, 20, 170, 150, ['Pension funds', 'Sovereign wealth funds', 'Insurers', 'Endowments', 'Wealth advisers (RIAs)'],
                 fill=SIGL, stroke=SIG, title='INVESTORS (LPs)', tcolor='#1c6f65', size=10.5))
    b.append(box(265, 20, 170, 150, ['Raises the money', 'Reports on the money', 'Answers every question', 'Keeps the CRM', 'Runs the events'],
                 fill=ACCL, stroke=ACC, title='INVESTOR SOLUTIONS', tcolor='#9a6512', size=10.5))
    b.append(text(350, 186, 'the team you would join', 9.5, MUTE, italic=True))
    b.append(box(520, 20, 170, 150, ['Student housing', 'Senior housing', 'Life science, storage', 'Data centres', 'Infrastructure, credit'],
                 fill=PALE, stroke=NAVY2, title='FUNDS AND ASSETS', tcolor=NAVY, size=10.5))
    b.append(arrow(182, 70, 262, 70, SIG, 'capital', marker='arS'))
    b.append(arrow(262, 120, 182, 120, ACC, 'reports, cash', marker='arA', lcolor='#9a6512', size=9))
    b.append(arrow(437, 70, 517, 70, NAVY2, 'invested', size=9))
    b.append(arrow(517, 120, 437, 120, NAVY2, 'results', size=9))
    b.append(box(520, 215, 170, 70, ['Students, residents,', 'patients, tenants'], fill='#fff', stroke=LINE, title='OCCUPIERS', tcolor=MUTE, size=10))
    b.append(arrow(605, 213, 605, 173, MUTE, None))
    b.append(text(615, 200, 'pay rent', 9.5, MUTE, anchor='start'))
    b.append(box(10, 215, 425, 70, ['Your client is the INVESTOR, never the tenant. You sell a fund, not a building.',
                                     'Investors buy access to assets they could not find or run themselves.'],
                 fill=NAVY, stroke=NAVY, color='#fff', size=10.5, title='THE ONE-LINE ANSWER', tcolor=ACC))
    return svg(700, 300, ''.join(b))

def d_moneyflow():
    b = []
    b.append(box(20, 20, 200, 70, ['commit, e.g. $100m over 3-4 years'], fill=SIGL, stroke=SIG, title='Investors (LPs)', tcolor='#1c6f65', size=10))
    b.append(box(250, 140, 200, 80, ['a legal pot (often a limited', 'partnership) run by the GP'], fill=ACCL, stroke=ACC, title='The fund', tcolor='#9a6512', size=10))
    b.append(box(480, 20, 200, 70, ['GP / investment manager', 'Harrison Street'], fill=PALE, stroke=NAVY2, title='The manager', tcolor=NAVY, size=10))
    b.append(box(250, 300, 200, 70, ['buy, build, improve, run'], fill=PALE, stroke=NAVY2, title='Properties', tcolor=NAVY, size=10))
    b.append(box(20, 300, 165, 70, ['adds leverage (LTV)'], fill='#fff', stroke=LINE, title='Banks / lenders', tcolor=MUTE, size=10))
    b.append(box(515, 300, 165, 70, ['rent and fees'], fill='#fff', stroke=LINE, title='Occupiers', tcolor=MUTE, size=10))
    b.append(path('M120,92 L120,170 L247,170', SIG, marker='arS'))
    b.append(text(70, 130, '1. capital calls', 9.5, '#1c6f65', anchor='start'))
    b.append(arrow(350, 222, 350, 297, NAVY2, '2. equity in', lx=395, ly=262))
    b.append(arrow(187, 335, 247, 335, MUTE))
    b.append(text(217, 328, 'loan', 9.5, MUTE))
    b.append(arrow(512, 335, 452, 335, MUTE))
    b.append(text(482, 328, '3. income', 9.5, MUTE))
    b.append(path('M300,298 L300,240 L300,222', NAVY2, marker='ar', dash=True))
    b.append(text(265, 262, '4. cash', 9.5, NAVY2))
    b.append(path('M250,195 L150,195 L150,92', SIG, marker='arS', dash=True))
    b.append(text(150, 212, '5. distributions + sale proceeds', 9.5, '#1c6f65'))
    b.append(path('M452,170 L580,170 L580,92', ACC, marker='arA'))
    b.append(text(585, 130, '6. management fee', 9.5, '#9a6512', anchor='start'))
    b.append(text(585, 143, '+ carried interest', 9.5, '#9a6512', anchor='start'))
    b.append(text(585, 156, 'if returns beat hurdle', 9.5, '#9a6512', anchor='start'))
    b.append(arrow(477, 55, 223, 55, NAVY2, 'quarterly reports, NAV, answers (this is ISG)', ly=48))
    return svg(700, 380, ''.join(b))

def d_clientmap():
    b = []
    cols = [
        ('DIRECT INSTITUTIONS', SIG, SIGL, '#1c6f65', ['Public pensions', '(CalSTRS, LGPS pools)', 'Corporate pensions', 'Sovereign wealth funds', '(Gulf, Asia)', 'Insurers', 'Endowments, foundations']),
        ('GATEKEEPERS', ACC, ACCL, '#9a6512', ['Investment consultants', '(Mercer, Aon, etc.)', 'OCIOs and fiduciaries', 'Pooled vehicles', '(UK LGPS pools)', 'Placement agents', '(GP-side, not client)']),
        ('WEALTH CHANNEL', NAVY2, PALE, NAVY, ['Registered investment', 'advisers (RIAs)', 'Private banks', 'Family offices', 'Interval funds, ETF', '(Harrison Street', 'Private Wealth)']),
    ]
    for i, (t, st, fi, tc, lines) in enumerate(cols):
        x = 15 + i * 230
        b.append(box(x, 15, 210, 190, lines, fill=fi, stroke=st, title=t, tcolor=tc, size=10.3))
    b.append(text(350, 228, 'HSAM reports >1,100 institutional investors and >300 RIAs (Sept 2026, firm release [F8])', 10, NAVY, 'bold'))
    b.append(box(15, 245, 670, 60, ['Consultants are not the money but they decide who gets shortlisted. Treat them as clients too.',
                                    'The JD names three audiences: current clients, consultants, prospective investors.'],
                 fill='#fff', stroke=LINE, size=10.3))
    return svg(700, 315, ''.join(b))

def d_fundraise():
    b = []
    stages = [('Map', 'target list,', 'CRM, research'), ('Pre-market', 'test interest', '(EU rules)'), ('Meet', 'first meetings,', 'pitch deck'),
              ('Diligence', 'DDQ, data room,', 'consultant review'), ('Approve', 'LP investment', 'committee'), ('Legal', 'LPA, side', 'letters'), ('Close', 'first, then', 'final close')]
    w = 92
    for i, (t, a, c) in enumerate(stages):
        x = 8 + i * 98
        fill = ACCL if i in (0, 2, 3) else PALE
        b.append(box(x, 30, w, 88, [a, c], fill=fill, stroke=ACC if fill == ACCL else NAVY2, title=t, tcolor=NAVY, size=9.6))
        if i < 6:
            b.append(arrow(x + w + 1, 74, x + 97, 74, NAVY2, sw=1.3))
    b.append(text(350, 18, 'The fundraising journey of one investor into one fund', 11, NAVY, 'bold'))
    b.append(f'<rect x="8" y="135" width="684" height="16" rx="3" fill="{PALE}"/>')
    b.append(f'<rect x="8" y="135" width="684" height="16" rx="3" fill="{SIG}" opacity="0.25"/>')
    b.append(text(350, 147, 'Average time a fund spends raising: 25 months for 2025 closes, an all-time high (PERE [I1])', 9.6, '#1c6f65', 'bold'))
    b.append(text(350, 172, 'Shaded stages are where an intern helps most: mapping, materials, diligence responses.', 9.6, MUTE, italic=True))
    return svg(700, 182, ''.join(b))

def d_lifecycle():
    b = []
    b.append(text(350, 16, 'One closed-end fund, one investor, ten years', 11, NAVY, 'bold'))
    b.append(arrow(78, 150, 690, 150, NAVY2))
    b.append(arrow(78, 230, 78, 30, NAVY2))
    b.append(text(72, 90, 'cash to LP', 9, MUTE, anchor='end'))
    b.append(text(72, 215, 'cash from LP', 9, MUTE, anchor='end'))
    # J-curve bars
    vals = [-30, -40, -35, -20, -5, 10, 30, 45, 55, 40]
    for i, v in enumerate(vals):
        x = 92 + i * 58
        h = abs(v) * 1.4
        y = 150 - h if v > 0 else 150
        b.append(f'<rect x="{x}" y="{y}" width="38" height="{h}" fill="{SIG if v > 0 else RED}" opacity="0.75"/>')
        b.append(text(x + 19, 245, f'Y{i+1}', 9, MUTE))
    b.append(text(210, 40, 'Investment period: capital calls', 9.6, RED, 'bold'))
    b.append(text(210, 53, '(red = money going in)', 9, RED))
    b.append(text(520, 40, 'Harvest: sales and distributions', 9.6, '#1c6f65', 'bold'))
    b.append(text(520, 53, '(green = money coming back)', 9, '#1c6f65'))
    b.append(text(350, 262, 'Illustrative shape only, not Harrison Street data. [Inferred]', 9, MUTE, italic=True))
    b.append(box(40, 270, 640, 46, ['Every quarter, all ten years: report, NAV, capital account statement, answer questions, AGM once a year.',
                                     'Same LP is then pitched the next fund. Fund IX: ~60% of capital came from existing investors [F6].'],
                 fill=ACCL, stroke=ACC, size=9.8))
    return svg(700, 322, ''.join(b))

def d_twohalves():
    b = []
    b.append(box(15, 15, 320, 210, ['Prospect mapping and research', 'Pitch books and presentations', 'RFPs and DDQs for new money',
                                    'Consultant meetings', 'Conferences and events', 'Tracking competitor raises'],
                 fill=SIGL, stroke=SIG, title='HALF 1: RAISE (capital formation)', tcolor='#1c6f65', size=12))
    b.append(box(365, 15, 320, 210, ['Quarterly and annual reports', 'Ad hoc information requests', 'Capital calls and distributions notices',
                                     'Annual meeting, advisory committee', 'Keeping Salesforce right', 'Client needs met, then exceeded'],
                 fill=ACCL, stroke=ACC, title='HALF 2: RETAIN (client service)', tcolor='#9a6512', size=12))
    b.append(path('M500,228 C500,265 180,265 180,232', NAVY2))
    b.append(text(340, 278, 'good service today is the cheapest fundraising for the next fund (re-ups)', 10, NAVY, 'bold'))
    return svg(700, 290, ''.join(b))

def d_jobsgrid():
    b = []
    b.append(f'<rect x="80" y="20" width="600" height="300" fill="#fff" stroke="{LINE}"/>')
    b.append(f'<line x1="380" y1="20" x2="380" y2="320" stroke="{LINE}"/><line x1="80" y1="170" x2="680" y2="170" stroke="{LINE}"/>')
    b.append(text(230, 14, 'FACES INVESTORS (capital)', 10, NAVY, 'bold'))
    b.append(text(530, 14, 'FACES BUILDINGS (assets)', 10, NAVY, 'bold'))
    b.append(f'<text x="30" y="95" font-size="10" fill="{NAVY}" font-weight="bold" text-anchor="middle" transform="rotate(-90 30 95)">FUND / FIRM LEVEL</text>')
    b.append(f'<text x="30" y="245" font-size="10" fill="{NAVY}" font-weight="bold" text-anchor="middle" transform="rotate(-90 30 245)">DEAL / BUILDING LEVEL</text>')
    b.append(box(95, 35, 270, 60, ['Raise and service money for whole funds', 'Clients: pensions, SWFs, RIAs'], fill=ACCL, stroke=ACC, title='Fund IR / ISG (this role)', tcolor='#9a6512', size=9.8, sw=2.4))
    b.append(box(95, 103, 270, 58, ['Shareholders, analysts, results days', 'Bound by market abuse rules'], fill=PALE, stroke=NAVY2, title='Listed REIT investor relations', tcolor=NAVY, size=9.8))
    b.append(box(395, 35, 270, 60, ['Choose what the fund buys and sells', 'Model returns, negotiate deals'], fill=PALE, stroke=NAVY2, title='Investment / acquisitions', tcolor=NAVY, size=9.8))
    b.append(box(395, 103, 270, 58, ['Run the portfolio to plan,', 'business plans, capex, exits'], fill=PALE, stroke=NAVY2, title='Asset / portfolio management', tcolor=NAVY, size=9.8))
    b.append(box(95, 185, 270, 60, ['Raise money for one deal or building', 'Paid one-off fees (CBRE, JLL, Colliers)'], fill=PALE, stroke=NAVY2, title='Agency capital markets', tcolor=NAVY, size=9.8))
    b.append(box(95, 253, 270, 58, ['Find a lender for a deal'], fill=PALE, stroke=NAVY2, title='Debt advisory / lending', tcolor=NAVY, size=9.8))
    b.append(box(395, 185, 270, 60, ['Rent collection, maintenance,', 'tenants and residents'], fill=PALE, stroke=NAVY2, title='Property management', tcolor=NAVY, size=9.8))
    b.append(box(395, 253, 270, 58, ['Find tenants, sell buildings', 'for a commission'], fill=PALE, stroke=NAVY2, title='Leasing / investment agency', tcolor=NAVY, size=9.8))
    return svg(700, 330, ''.join(b))

def d_listed_vs_private():
    b = []
    rows = [('Who owns it', 'thousands of shareholders', 'tens of professional LPs'),
            ('How they buy', 'press a button on an exchange', 'commit for 7-10+ years, negotiated'),
            ('Exit', 'sell shares any day', 'wait for distributions or redemption queue'),
            ('Key rule', 'MAR Art. 17 / Reg FD: no selective disclosure', 'marketing rules: AIFMD, NPPR, s21 FSMA'),
            ('Rhythm', 'quarterly results, analyst calls', 'fundraises, DDQs, quarterly LP reports'),
            ('Success =', 'fair valuation, stable share register', 'capital committed, re-ups, low churn')]
    b.append(box(170, 10, 255, 34, [], fill=NAVY, stroke=NAVY, title='LISTED COMPANY IR', tcolor='#fff', size=10))
    b.append(box(435, 10, 255, 34, [], fill=ACC, stroke=ACC, title='PRIVATE FUND IR (ISG)', tcolor='#fff', size=10))
    for i, (k, a, c) in enumerate(rows):
        y = 52 + i * 40
        b.append(box(10, y, 152, 34, [k], fill=PALE, stroke=LINE, size=10, color=NAVY))
        b.append(box(170, y, 255, 34, [a], fill='#fff', stroke=LINE, size=9.8))
        b.append(box(435, y, 255, 34, [c], fill=ACCL, stroke=LINE, size=9.8))
    return svg(700, 298, ''.join(b))

def d_open_closed():
    b = []
    b.append(box(15, 10, 320, 30, [], fill=NAVY, stroke=NAVY, title='OPEN-END (evergreen) e.g. Core Property Fund', tcolor='#fff', size=9.8))
    b.append(box(365, 10, 320, 30, [], fill=ACC, stroke=ACC, title='CLOSED-END e.g. Real Estate Partners IX', tcolor='#fff', size=9.8))
    b.append(f'<rect x="95" y="60" width="160" height="120" rx="10" fill="{PALE}" stroke="{NAVY2}"/>')
    b.append(text(175, 115, 'Fund never ends', 10.5, NAVY, 'bold'))
    b.append(text(175, 132, 'priced at NAV', 9.8))
    b.append(arrow(30, 90, 92, 100, SIG, marker='arS')); b.append(text(45, 82, 'join', 9.5, '#1c6f65'))
    b.append(arrow(258, 140, 320, 150, RED)); b.append(text(305, 132, 'leave', 9.5, RED))
    b.append(text(175, 200, 'Investors subscribe and redeem over time;', 9.6))
    b.append(text(175, 214, 'in stress, exits can queue.', 9.6))
    b.append(text(175, 232, 'IR: continuous selling + reporting', 9.8, NAVY, 'bold'))
    for i, (lab, col) in enumerate([('Raise', ACC), ('Invest', NAVY2), ('Manage', NAVY2), ('Sell, return', SIG)]):
        x = 375 + i * 78
        b.append(box(x, 90, 72, 50, [lab], fill='#fff', stroke=col, size=10))
        if i < 3: b.append(arrow(x + 73, 115, x + 77, 115))
    b.append(text(525, 165, 'Fixed life, typically ~10 years [Reported I43]', 9.6))
    b.append(text(525, 183, 'Commit once, money called as deals happen', 9.6))
    b.append(text(525, 232, 'IR: big raise every 2-4 years, then service', 9.8, NAVY, 'bold'))
    return svg(700, 245, ''.join(b))

def d_spectrum():
    b = []
    b.append(f'<defs><linearGradient id="g1" x1="0" x2="1"><stop offset="0" stop-color="{SIG}"/><stop offset="1" stop-color="{RED}"/></linearGradient></defs>')
    b.append('<rect x="20" y="40" width="660" height="22" rx="11" fill="url(#g1)" opacity="0.85"/>')
    b.append(text(20, 30, 'lower risk, mostly income', 10, '#1c6f65', 'bold', anchor='start'))
    b.append(text(680, 30, 'higher risk, mostly capital growth', 10, RED, 'bold', anchor='end'))
    cols = [('CORE', 'max 15% non-income assets', 'LTV label: 40% or less', 'HS Core Property Fund ($15.1bn GAV)'),
            ('VALUE-ADD', '15-40% non-income assets', 'max LTV 40-60%', '(core-plus maps here or core)'),
            ('OPPORTUNISTIC', 'beyond value-add limits', 'LTV above 60%', 'HS Real Estate Partners series')]
    for i, (t, a, c, d) in enumerate(cols):
        x = 20 + i * 225
        b.append(box(x, 75, 210, 105, [a, c, '', d], fill=PALE if i != 1 else ACCL, stroke=NAVY2, title=t, tcolor=NAVY, size=9.6))
    b.append(text(350, 200, 'Thresholds: INREV fund style classification (2012 revision), via summary [I51]. HS fund sizes: Form ADV, 31 Mar 2026 [F11].', 9, MUTE))
    return svg(700, 210, ''.join(b))

def d_timeline():
    ev = [(2005, 'Founded, Chicago', 'Merrill + Galvins'), (2011, 'Open-end core fund', 'launched'), (2015, 'European platform', 'London entity'),
          (2018, 'Colliers buys 75%', '$450m + earn-out'), (2022, 'Colliers buys Basalt,', 'Rockwood, Versus'), (2024, 'Fund IX closes', '~$2.5bn'),
          (2025, 'Rebrand to HSAM;', 'RoundShield 60%'), (2026, 'HSAM Europe;', 'ISG hits 50')]
    b = []
    b.append(f'<line x1="30" y1="80" x2="670" y2="80" stroke="{NAVY}" stroke-width="3"/>')
    for i, (yr, a, c) in enumerate(ev):
        x = 45 + i * 87
        up = i % 2 == 0
        b.append(circle(x, 80, 7, ACC, NAVY))
        b.append(text(x, 104 if up else 66, str(yr), 10.5, NAVY, 'bold'))
        yy = 30 if up else 118
        if up:
            b.append(text(x, 32, a, 9.2)); b.append(text(x, 45, c, 9.2, MUTE))
        else:
            b.append(text(x, 124, a, 9.2)); b.append(text(x, 137, c, 9.2, MUTE))
    return svg(700, 150, ''.join(b))

def d_aum():
    data = [('May 2018', 14.6, 'F2'), ('Oct 2024', 55, 'F6'), ('Jun 2025', 56, 'F14'), ('Dec 2025', 108.2, 'F3'), ('Sep 2026', 110, 'F8')]
    b = []
    base = 230; scale = 1.75
    b.append(f'<line x1="60" y1="{base}" x2="680" y2="{base}" stroke="{LINE}"/>')
    for i, (lab, v, s) in enumerate(data):
        x = 90 + i * 120
        h = v * scale
        col = NAVY2 if i < 3 else ACC
        b.append(f'<rect x="{x}" y="{base-h}" width="70" height="{h}" fill="{col}"/>')
        b.append(text(x + 35, base - h - 6, f'${v:g}bn', 10.5, NAVY, 'bold'))
        b.append(text(x + 35, base + 15, lab, 9.8))
        b.append(text(x + 35, base + 28, f'[{s}]', 9, MUTE))
    b.append(text(70, 62, 'July 2025: Colliers folds its other managers', 9.6, '#9a6512', 'bold', anchor='start'))
    b.append(text(70, 75, 'into the HS brand. Mostly a merger, not growth.', 9.6, '#9a6512', anchor='start'))
    b.append(path('M290,82 C360,95 400,110 445,120', ACC, marker='arA'))
    b.append(text(60, 20, 'Assets under management (AUM), US$bn, firm and Colliers figures', 10, NAVY, 'bold', anchor='start'))
    return svg(700, 266, ''.join(b))

def d_platform():
    b = []
    b.append(box(250, 10, 200, 46, ['listed, Toronto and Nasdaq'], fill='#fff', stroke=LINE, title='Colliers International', tcolor=NAVY, size=9.6))
    b.append(arrow(350, 58, 350, 82, NAVY2, None))
    b.append(text(395, 74, '82% economic interest [F3]', 9.2, MUTE, anchor='start'))
    b.append(box(170, 84, 360, 50, ['$110bn AUM, 600+ staff, CEO Christopher Merrill [F8, F1]'], fill=NAVY, stroke=NAVY, color='#fff',
                 title='Harrison Street Asset Management (HSAM)', tcolor=ACC, size=9.8))
    plats = [('Harrison Street', 'alternative real estate', 'the original firm'), ('Basalt', 'mid-market', 'infrastructure'),
             ('Rockwood', 'US real estate', 'New York'), ('HS Private Wealth', 'ex-Versus Capital', 'interval funds, ETF'),
             ('Colliers Global', 'Investors', '(ex-Antirion)'), ('HSAM Europe', 'HS Europe +', 'RoundShield credit')]
    for i, (t, a, c) in enumerate(plats):
        x = 8 + i * 116
        fill = ACCL if i in (0, 5) else PALE
        b.append(box(x, 175, 110, 70, [a, c], fill=fill, stroke=ACC if fill == ACCL else NAVY2, title=t, tcolor=NAVY, size=8.9))
        b.append(arrow(350, 136, x + 55, 172, LINE, sw=1.1))
    b.append(box(8, 262, 684, 42, ['Investor Solutions Group (50 people) sells across the whole shelf. London ISG sits in HSAM Europe\'s orbit. [F8, F12]'],
                 fill=SIGL, stroke=SIG, size=9.8, color='#1c6f65'))
    return svg(700, 312, ''.join(b))

def d_sectors():
    b = []
    cx, cy = 350, 160
    b.append(circle(cx, cy, 62, NAVY))
    b.append(text(cx, cy - 6, 'DEMAND,', 11, '#fff', 'bold'))
    b.append(text(cx, cy + 9, 'NOT MACRO', 11, ACC, 'bold'))
    b.append(text(cx, cy + 24, '[F5]', 9, '#c9d1e3'))
    import math
    items = [('Student housing', 'more students than beds'), ('Senior housing', 'ageing population'), ('Healthcare delivery', 'medical office'),
             ('Life sciences', 'labs, science parks'), ('Storage', 'moves, downsizing'), ('Data centres', 'AI and cloud demand'),
             ('Build-to-rent', 'renters for longer'), ('Infrastructure', 'utility, digital, social')]
    for i, (t, a) in enumerate(items):
        ang = -math.pi / 2 + i * 2 * math.pi / len(items)
        x = cx + 245 * math.cos(ang); y = cy + 118 * math.sin(ang)
        b.append(f'<line x1="{cx + 62*math.cos(ang):.0f}" y1="{cy + 62*math.sin(ang):.0f}" x2="{x:.0f}" y2="{y:.0f}" stroke="{LINE}"/>')
        b.append(box(x - 72, y - 22, 144, 44, [a], fill=ACCL if i % 2 == 0 else PALE, stroke=ACC if i % 2 == 0 else NAVY2, title=t, tcolor=NAVY, size=9.3))
    return svg(700, 320, ''.join(b))

def d_isg_org():
    b = []
    CF, RP, IN = SIG, ACC, PURP
    def nb(x, y, w, t, a, col):
        return box(x, y, w, 46, [a], fill='#fff', stroke=col, title=t, tcolor=NAVY, size=9.2, sw=2)
    b.append(nb(230, 10, 240, 'Global Co-Heads, ISG', 'G. Regnery (also Co-President), J. Sheehan', CF))
    b.append(nb(10, 90, 160, 'US ISG Co-Heads', 'D. Fanelli, J. Choi', CF))
    b.append(nb(180, 90, 165, 'Head of ISG, Europe', 'M. Kojuri, London', CF))
    b.append(nb(355, 90, 165, 'Head of IR, Middle East', 'H. Nasser, Abu Dhabi', CF))
    b.append(nb(530, 90, 160, 'Asia ISG Co-Head', 'M. Humphrey, Singapore', CF))
    for x in (90, 262, 437, 610):
        b.append(arrow(350, 58, x, 87, LINE, sw=1.1))
    b.append(nb(100, 175, 170, 'MD, infrastructure IR', 'J. Bowes (joined Aug 2026)', CF))
    b.append(nb(280, 175, 170, 'Associates / analysts', 'reporting, RFPs, CRM', IN))
    b.append(nb(460, 175, 150, 'Summer intern', 'YOU (2027)', RP))
    for x in (185, 365, 535):
        b.append(arrow(262, 138, x, 172, LINE, sw=1.1))
    b.append(nb(10, 255, 200, 'Investor Services', 'reporting, notices [Reported]', RP))
    b.append(nb(250, 255, 200, 'Marketing', 'brand, materials [Reported F20b]', RP))
    b.append(nb(490, 255, 200, 'Consultant relations', 'gatekeeper coverage [F19]', RP))
    b.append(text(350, 330, 'Sibling sub-teams that work alongside the front-line ISG (from job postings)', 9.4, MUTE, italic=True))
    for i, (lab, col) in enumerate([('Confirmed: firm release or bio', CF), ('Reported: job posting snippet', RP), ('Inferred: author reasoning', IN)]):
        x = 30 + i * 225
        b.append(f'<rect x="{x}" y="342" width="14" height="10" fill="#fff" stroke="{col}" stroke-width="2"/>')
        b.append(text(x + 20, 351, lab, 9.2, INK, anchor='start'))
    return svg(700, 360, ''.join(b))

def d_request():
    steps = [('Request in', 'LP or consultant', 'email'), ('Log', 'Salesforce', 'case + owner'), ('Gather', 'finance, PM,', 'legal, ops'),
             ('Draft', 'answer + data', 'source each number'), ('Check', 'compliance +', 'senior sign-off'), ('Send + log', 'on time,', 'record kept')]
    b = []
    for i, (t, a, c) in enumerate(steps):
        x = 8 + i * 115
        fill = ACCL if t in ('Log', 'Draft') else (REDL if t == 'Check' else PALE)
        stc = ACC if fill == ACCL else (RED if fill == REDL else NAVY2)
        b.append(box(x, 20, 105, 80, [a, c], fill=fill, stroke=stc, title=t, tcolor=NAVY, size=9.6))
        if i < 5: b.append(arrow(x + 106, 60, x + 114, 60, NAVY2, sw=1.3))
    b.append(text(350, 125, 'Red = the step you never skip. Amber = where interns add most. [Inferred from JD and industry practice]', 9.4, MUTE, italic=True))
    return svg(700, 135, ''.join(b))

def d_day():
    slots = [('08:30', 'Scan news and AI digest: competitor raises, LP moves', SIGL), ('09:30', 'Team check-in: who needs what today', PALE),
             ('10:00', 'Update pitch deck pages with new quarter numbers', ACCL), ('11:30', 'Log last week\'s meetings in Salesforce', PALE),
             ('13:30', 'Draft answers to a consultant DDQ section', ACCL), ('15:00', 'Research list: Gulf and Nordic investors for a strategy', SIGL),
             ('16:30', 'Conference logistics: delegates, meetings grid', PALE), ('17:30', 'Send drafts for review; note open items', PALE)]
    b = []
    for i, (t, a, f) in enumerate(slots):
        y = 8 + i * 34
        b.append(box(8, y, 70, 28, [t], fill=NAVY, stroke=NAVY, color='#fff', size=10))
        b.append(box(86, y, 604, 28, [a], fill=f, stroke=LINE, size=10))
    return svg(700, 284, ''.join(b))

def d_regs():
    ev = [('2 Aug 2021', 'EU pre-marketing', 'rules apply'), ('15 Nov 2021', 'UK LTAF', 'rules in force'), ('10 Jan 2024', 'ELTIF 2.0', 'applies'),
          ('31 May 2024', 'FCA anti-', 'greenwashing rule'), ('16 Apr 2026', 'AIFMD II', 'applies in EU'), ('14 Jul 2026', 'FCA CP26/28', 'UK AIFM reform'),
          ('14 Oct 2026', 'CP26/28', 'consultation closes'), ('~2028', 'New UK AIFM regime;', 'SFDR 2.0 (proposed)')]
    b = []
    b.append(f'<line x1="25" y1="70" x2="675" y2="70" stroke="{NAVY}" stroke-width="3"/>')
    for i, (d, a, c) in enumerate(ev):
        x = 45 + i * 87
        fut = i >= 6
        b.append(circle(x, 70, 7, '#fff' if fut else ACC, NAVY))
        up = i % 2 == 0
        y1 = 25 if up else 98
        b.append(text(x, y1, d, 9.6, NAVY, 'bold'))
        b.append(text(x, y1 + 13, a, 9.1)); b.append(text(x, y1 + 25, c, 9.1, MUTE))
    b.append(text(350, 145, 'Hollow dots = future or proposal, not yet law. Sources: [I14] [I66] [I65] [I13] [I8] [I6] [I11]', 9, MUTE, italic=True))
    return svg(700, 152, ''.join(b))

def d_fundraising_chart():
    data = [(2020, 213.85), (2021, 304.45), (2022, 266.57), (2023, 204.25), (2024, 172.42), (2025, 222.16)]
    b = []
    base = 240; sc = 0.62
    b.append(f'<line x1="50" y1="{base}" x2="680" y2="{base}" stroke="{LINE}"/>')
    for i, (y, v) in enumerate(data):
        x = 80 + i * 100
        h = v * sc
        col = RED if y == 2024 else (SIG if y == 2025 else NAVY2)
        b.append(f'<rect x="{x}" y="{base-h:.0f}" width="60" height="{h:.0f}" fill="{col}"/>')
        b.append(text(x + 30, base - h - 6, f'${v:.0f}bn', 10.5, NAVY, 'bold'))
        b.append(text(x + 30, base + 16, str(y), 10.5))
    b.append(text(50, 18, 'Global private real estate capital raised, US$bn (PERE Fundraising Report FY2025 [I1])', 10, NAVY, 'bold', anchor='start'))
    b.append(text(50, 270, 'PERE counts differently from Preqin (Preqin: $155bn for 2025 [I34]). Use one source and name it.', 9.2, MUTE, italic=True, anchor='start'))
    return svg(700, 280, ''.join(b))

def d_isg_inside():
    b = []
    b.append(circle(350, 150, 58, ACC))
    b.append(text(350, 146, 'ISG', 15, '#fff', 'bold'))
    b.append(text(350, 163, 'the hub', 10, '#fff'))
    import math
    nodes = [('Deal and portfolio teams', 'track record, pipeline'), ('Finance / fund accounting', 'NAV, returns, cash flows'),
             ('Legal and compliance', 'sign-off, LPAs, side letters'), ('Research', 'market views, charts'),
             ('Marketing and brand', 'design, website, PR'), ('Senior leadership', 'meetings, roadshows'),
             ('Investors and consultants', 'the clients'), ('Investor Services', 'notices, onboarding')]
    for i, (t, a) in enumerate(nodes):
        ang = -math.pi / 2 + i * 2 * math.pi / len(nodes)
        x = 350 + 250 * math.cos(ang); y = 150 + 110 * math.sin(ang)
        b.append(f'<line x1="{350+58*math.cos(ang):.0f}" y1="{150+58*math.sin(ang):.0f}" x2="{x:.0f}" y2="{y:.0f}" stroke="{ACC}" stroke-width="1.4"/>')
        clients = t.startswith('Investors')
        b.append(box(x - 85, y - 21, 170, 42, [a], fill=SIGL if clients else PALE, stroke=SIG if clients else NAVY2, title=t, tcolor=NAVY, size=9))
    return svg(700, 300, ''.join(b))
