# -*- coding: utf-8 -*-
import os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
from gen import C

HERE = os.path.dirname(os.path.abspath(__file__))
CH = {}

CH['TREEMAP'] = gen.treemap()
CH['LADDER'] = gen.ladder()
CH['ASSETS'] = gen.assets_stack()
CH['REVMODEL'] = gen.revmodel()

CH['RANKINC'] = gen.hbar(
    [('1 · Investment Bank', 13055, C['ib']),
     ('2 · Barclays UK', 8708, C['buk']),
     ('3 · US Consumer Bank', 3681, C['uscb']),
     ('4 · UK Corporate Bank', 2064, C['ukcb']),
     ('5 · Private Bank & Wealth', 1380, C['pbwm'])],
    unit='m', fmt=lambda v: f'£{v:,.0f}',
    title='Ranked by income — the direct answer',
    sub='FY2025 total income by division. Head Office (£252m) is a central cost centre, not a business, and is excluded.')

CH['RANKROTE'] = gen.hbar(
    [('1 · Private Bank & Wealth', 26.3, C['pbwm']),
     ('2 · Barclays UK', 20.7, C['buk']),
     ('3 · UK Corporate Bank', 18.9, C['ukcb']),
     ('4 · US Consumer Bank', 11.0, C['uscb']),
     ('5 · Investment Bank', 10.6, C['ib'])],
    unit='%', fmt=lambda v: f'{v:.1f}',
    title='Ranked by return on capital — the ranking flips',
    sub='FY2025 RoTE. The smallest division by income is the most profitable per pound of shareholder capital in the entire group.')

CH['GROWTH'] = gen.grouped_bars(
    ['FY2025 vs FY2024', 'H1 2026 vs H1 2025'],
    [('Income growth', [5.0, 2.0], C['pbwm']),
     ('Cost growth', [10.0, 11.0], C['red'])],
    title='The honest picture: costs are growing faster than income',
    sub='Year-on-year percentage change. This is deliberate — Barclays is spending ahead of the revenue — but it is why profit fell.',
    h=232, fmt=lambda v: f'+{v:.0f}%')

CH['ROTETREND'] = gen.steps([
    ('FY2024', 28.1, 'pre-investment', False),
    ('H1 2025', 33.2, 'peak', False),
    ('FY2025', 26.3, 'spending starts', False),
    ('H1 2026', 26.1, 'latest', False),
    ('2026 target', 25.0, '> 25%', True),
    ('2028 target', 25.0, '> 25%', True),
], title='Return on tangible equity — still comfortably above target',
   sub='The fall from 33.2% is the cost of the growth plan, not a deterioration in the business. The division is still the best-returning in Barclays.')

CH['UKAUM'] = gen.hbar(
    [('NatWest + Evelyn (combined)', 128.0, C['red']),
     ('Evelyn Partners (alone)', 69.0, C['ho']),
     ('NatWest PB&WM incl. Coutts', 58.5, C['ho']),
     ('Barclays PB&WM — AUM', 55.8, C['pbwm'])],
    unit='bn', fmt=lambda v: f'£{v:.1f}',
    title='The UK league table — and what NatWest just did to it',
    sub='Assets under management, most recent disclosure. NatWest agreed to buy Evelyn Partners for £2.7bn in February 2026, beating Barclays in the auction. On AUM alone that leapfrogs Barclays overnight.')

CH['TIMELINE'] = gen.timeline([
    ('1690', 'Barclays begins on Lombard Street', 'Two Quaker goldsmith-bankers. Private banking for wealthy families is the original business — the retail bank came later.'),
    ('1864', 'Presence begins across Asia', 'The foundation of what is now the international private bank.'),
    ('~1920s', 'Over a century in the Crown Dependencies', 'Jersey, Guernsey and the Isle of Man — still core booking centres today.'),
    ('1922', 'Monaco', 'Barclays is the longest-serving foreign wealth manager in the Principality.'),
    ('mid-1980s', 'Geneva and Zurich established', 'Swiss booking capability — the entry ticket to serving international wealth.'),
    ('1990', 'India', 'Investment services begin; India is now a named growth hub.'),
    ('2003', 'Gerrard acquired for £210m', 'Bought from Old Mutual with £12.5bn of assets and 116,000 clients. Combined with Barclays Investment Management it created a ~£21bn business — then the UK’s largest adviser to wealthy investors.'),
    ('2000s', 'Barclays Wealth formed', 'Private Bank, Stockbrokers, International Private Bank, Gerrard, Estates & Trust pulled into one division.'),
    ('2015', 'The US wealth business is sold to Stifel', '~180 advisers and ~$56bn of client assets. Barclays gave up on American wealth — and has ruled out going back.'),
    ('Feb 2024', 'Made a standalone reporting division', 'Sasha Wiggins appointed CEO. Wealth Management & Investments transferred in from Barclays UK.'),
    ('Dec 2024', 'Business deep dive sets the growth plan', 'RoTE target of >25%, tech spend up more than 75%, international build-out.'),
    ('Feb 2026', 'Barclays bids for Evelyn Partners — and loses', 'NatWest pays £2.7bn. Barclays commits to organic growth instead.'),
    ('Apr 2026', 'Premier Wealth Management launches', 'Advice from £150k invested, no upfront fee. Direct Investing custody fees removed.'),
    ('2026', 'Singapore booking centre; GoHenry acquired', 'A full return to Asian on-the-ground presence, and the bottom rung of the ladder bought for ~£180m.'),
], title='Barclays has been doing this for 335 years',
   sub='Longevity is not just heritage here — booking centres, trust licences and cross-border permissions take decades to build and are a genuine barrier to entry.')

def build():
    parts = sorted(glob.glob(os.path.join(HERE, 'parts2', '*.html')))
    body = '\n'.join(open(p, encoding='utf-8').read() for p in parts)
    def sub(m):
        k = m.group(1)
        if k not in CH:
            raise SystemExit(f'MISSING CHART: {k}')
        return CH[k]
    body = re.sub(r'\{\{([A-Z_]+)\}\}', sub, body)
    css = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()
    out = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<title>Barclays Private Bank &amp; Wealth Management</title>'
           f'<style>{css}</style></head><body>{body}</body></html>')
    dest = os.path.join(HERE, 'wealth-report.html')
    open(dest, 'w', encoding='utf-8').write(out)
    print(f'wrote {dest} ({len(out):,} bytes, {len(parts)} parts)')

if __name__ == '__main__':
    build()
