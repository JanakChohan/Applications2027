# -*- coding: utf-8 -*-
import os, sys, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen
from gen import C

HERE = os.path.dirname(os.path.abspath(__file__))

CHARTS = {}

CHARTS['ORG'] = gen.orgchart()
CHARTS['ENGINES'] = gen.engines()

CHARTS['INCOME'] = gen.hbar(
    [('Investment Bank', 13055, C['ib']),
     ('Barclays UK', 8708, C['buk']),
     ('US Consumer Bank', 3681, C['uscb']),
     ('UK Corporate Bank', 2064, C['ukcb']),
     ('Private Bank & Wealth', 1380, C['pbwm']),
     ('Head Office', 252, C['ho'])],
    unit='m', fmt=lambda v: f'£{v:,.0f}',
    title='Where the £29.1bn of FY2025 income came from',
    sub='Total income by division, year ended 31 December 2025')

CHARTS['PBT'] = gen.hbar(
    [('Investment Bank', 4614, C['ib']),
     ('Barclays UK', 3413, C['buk']),
     ('UK Corporate Bank', 970, C['ukcb']),
     ('US Consumer Bank', 515, C['uscb']),
     ('Private Bank & Wealth', 375, C['pbwm'])],
    unit='m', fmt=lambda v: f'£{v:,.0f}',
    title='Where the profit came from',
    sub='Profit before tax by division, FY2025. Head Office ran a £748m loss, which is why these sum to more than the £9,139m Group figure.')

CHARTS['BUTTERFLY'] = gen.butterfly(
    [('Investment Bank', 55.1, 44.8, C['ib']),
     ('Barclays UK', 24.0, 29.9, C['buk']),
     ('US Consumer Bank', 7.7, 12.6, C['uscb']),
     ('UK Corporate Bank', 7.4, 7.1, C['ukcb']),
     ('Private Bank & Wealth', 2.2, 4.7, C['pbwm'])],
    title='The single most important chart in this report',
    sub='Bars pointing left = how much of the Group’s regulatory capital a division ties up. Bars pointing right = how much income it earns. Where left beats right, the division is diluting returns.')

CHARTS['ROTE'] = gen.grouped_bars(
    ['Barclays UK', 'UK Corporate', 'Private Bank', 'Investment Bank', 'US Consumer', 'GROUP'],
    [('FY2025', [20.7, 18.9, 26.3, 10.6, 11.0, 11.3], C['ho']),
     ('H1 2026', [20.1, 20.6, 26.1, 15.5, 24.2, 14.8], C['buk'])],
    title='Return on tangible equity by division',
    sub='RoTE is the number that matters: profit earned per pound of shareholder capital. The Group must clear 12% in 2026 and 14% by 2028.')

CHARTS['BUBBLE'] = gen.bubbles(
    [('Barclays UK', 85.8, 20.7, 8708, C['buk']),
     ('UK Corporate Bank', 26.5, 18.9, 2064, C['ukcb']),
     ('Private Bank & Wealth', 8.0, 26.3, 1380, C['pbwm']),
     ('Investment Bank', 196.7, 10.6, 13055, C['ib']),
     ('US Consumer Bank', 27.4, 11.0, 3681, C['uscb'])],
    title='The whole business on one chart (FY2025)',
    sub='Ideal position is top-left: high return, little capital. The Investment Bank sits bottom-right — the strategic problem Barclays has spent three years fixing.')

CHARTS['IBTREE'] = gen.stacked_tree(
    title='What the Investment Bank actually sells',
    sub='FY2025 income, £13,055m. Bar lengths are shares of divisional income.')

CHARTS['TIMELINE'] = gen.timeline([
    ('1690', 'Two Quaker goldsmith-bankers set up on Lombard Street',
     'John Freame and Thomas Gould. Barclays still dates itself from here — 335 years.'),
    ('1736', 'James Barclay becomes a partner', 'The family name arrives and never leaves.'),
    ('1896', 'Twenty family banks merge into Barclay & Company',
     '£26m of deposits. The modern joint-stock bank is born — a federation, not a founder.'),
    ('1966', 'Barclaycard launches — Britain’s first credit card',
     'A genuine first. Sixty years on, cards are still a core Barclays skill on both sides of the Atlantic.'),
    ('1986', 'Big Bang: Barclays buys de Zoete & Bevan and Wedd Durlacher, forming BZW',
     'The first attempt to bolt an investment bank onto a clearing bank.'),
    ('1997', 'BZW’s equities and advisory arms are sold to CSFB',
     'The first attempt fails. What is kept — fixed income — is renamed Barclays Capital.'),
    ('2008', 'Barclays buys Lehman Brothers’ North American business out of bankruptcy',
     '$1.75bn for the US franchise, HQ and data centres — and none of the toxic assets. The defining act.'),
    ('2016–17', 'Barclays sells down Absa and exits Africa',
     'A deliberate retreat to two home markets: the UK and the US.'),
    ('2018', 'Ring-fencing splits the bank into two legal entities',
     'Barclays Bank UK PLC (retail) and Barclays Bank PLC (international) — by law.'),
    ('2023', 'Kensington Mortgages acquired', 'Specialist UK lending capability bought in.'),
    ('2024', 'Tesco Bank acquired; three-year plan launched',
     '£600m, plus a 10-year exclusive to sell financial products under the Tesco brand.'),
    ('2026', 'Best Egg bought, American Airlines portfolio sold',
     'Recycling US capital out of low-return co-brand cards into higher-return personal loans.'),
], title='Three hundred and thirty-five years in thirteen lines',
   sub='Barclays’ present shape is not a design. It is the residue of these decisions.')

CHARTS['PYRAMID'] = gen.pyramid([
    ('Governments, central banks, sovereign funds', 'Gilt and bond issuance, FX, reserves — Investment Bank', C['ib']),
    ('Large corporates & financial institutions', 'M&A, debt/equity raising, hedging, cash management', C['ib']),
    ('UK mid-cap and SME businesses', '~1 in 4 UK corporates — UK Corporate Bank', C['ukcb']),
    ('High-net-worth individuals and families', '£3m+ investable — Private Bank & Wealth', C['pbwm']),
    ('Mass-affluent and everyday consumers', '~20m UK customers + ~10m US cardholders', C['buk']),
], title='Who Barclays sells to', sub='Roughly 48 million customers, from a sovereign treasury to a current account.')

CHARTS['STEPS'] = gen.steps([
    ('2023', 9.0, 'before the plan', False),
    ('2024', 10.5, 'year 1 delivered', False),
    ('2025', 11.3, 'year 2 delivered', False),
    ('H1 2026', 14.8, 'running ahead', False),
    ('2026 target', 12.0, '> 12%', True),
    ('2028 target', 14.0, '> 14%', True),
], title='The turnaround, in one line',
   sub='Group RoTE. The 2026 target now looks conservative; management has already pointed past it to 2028.')

CHARTS['PEERS'] = gen.hbar(
    [('NatWest', 19.2, C['ho']),
     ('Standard Chartered', 14.7, C['ho']),
     ('HSBC', 13.3, C['ho']),
     ('Barclays', 11.3, C['buk']),
     ('— Barclays H1 2026 run-rate', 14.8, C['pbwm'])],
    unit='%', fmt=lambda v: f'{v:.1f}',
    title='Barclays vs its UK-listed peers — return on tangible equity, FY2025',
    sub='Lloyds does not report a directly comparable statutory RoTE on the same basis and is excluded; it guides to >16% for 2026. Barclays was the laggard on FY2025 — and is closing the gap fast.')

def build():
    parts = sorted(glob.glob(os.path.join(HERE, 'parts', '*.html')))
    body = '\n'.join(open(p, encoding='utf-8').read() for p in parts)
    def sub(m):
        k = m.group(1)
        if k not in CHARTS:
            raise SystemExit(f'MISSING CHART: {k}')
        return CHARTS[k]
    body = re.sub(r'\{\{([A-Z_]+)\}\}', sub, body)
    css = open(os.path.join(HERE, 'style.css'), encoding='utf-8').read()
    out = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
           '<title>Barclays — A Complete Business Breakdown</title>'
           f'<style>{css}</style></head><body>{body}</body></html>')
    dest = os.path.join(HERE, 'report.html')
    open(dest, 'w', encoding='utf-8').write(out)
    print(f'wrote {dest}  ({len(out):,} bytes, {len(parts)} parts)')

if __name__ == '__main__':
    build()
