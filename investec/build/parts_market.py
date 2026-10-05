from lib import *

def fig_spectrum():
    axes = [('Breadth of offer','Lender only','Lend + advise + private bank',[('OakNorth',0.08),('Shawbrook',0.15),('Close Bros',0.2),('Peel Hunt',0.25),('Coutts',0.45),('Investec',0.82),('HSBC UK',0.95)]),
            ('Client focus','Mass market','Mid-market and HNW',[('Santander UK',0.08),('HSBC UK',0.25),('Shawbrook',0.55),('OakNorth',0.7),('Investec',0.84),('Coutts',0.97)]),
            ('Scale (total assets)','Small','Very large',[('C. Hoare',0.04),('Arbuthnot',0.06),('Close Bros',0.12),('Investec UK',0.22),('Santander UK',0.78),('HSBC UK',0.95)]),
            ('Cost efficiency','Lean (low C/I)','High-touch (high C/I)',[('OakNorth',0.08),('HSBC CMB',0.15),('Shawbrook',0.3),('Investec UK',0.7)]),
            ('Wealth model','In-house','Partner / none',[('Coutts',0.05),('Barclays PB',0.1),('Arbuthnot',0.2),('Investec',0.75),('Shawbrook',0.95)])]
    b = ''
    for i,(t,l,r,pts) in enumerate(axes):
        y = 30 + i*72
        b += text(10, y-6, t, 11, NAVY, 'start', 'bold')
        b += f'<line x1="120" y1="{y+14}" x2="680" y2="{y+14}" stroke="{LINE}" stroke-width="6" stroke-linecap="round"/>'
        b += text(120, y+48, l, 8.5, MUT, italic=True) + text(680, y+48, r, 8.5, MUT, 'end', italic=True)
        for j,(n,v) in enumerate(pts):
            x = 120 + v*560; inv = 'Investec' in n
            b += f'<circle cx="{x:.0f}" cy="{y+14}" r="{7 if inv else 5}" fill="{ACC if inv else NAVY2}"/>'
            b += text(x, y+(1 if j%2 else 31) , n, 8.6, ACC if inv else NAVY, 'middle', 'bold' if inv else 'normal')
    return svg(720, 400, b)

def fig_size():
    items = [('HSBC UK (total assets)',355.9),('Santander UK (total assets)',266.8),('Investec Group (total assets)',63.8),('Investec plc (total assets)',32.0),('Shawbrook (loans)',19.2),('Investec UK SB (loans)',17.8),('Close Brothers (total assets)',12.1),('Arbuthnot (total assets)',5.0)]
    cols = [MUT,MUT,NAVY,NAVY,MUT,ACC,MUT,MUT]
    return hbar(items, label_w=230, unit='bn', valfmt='£{:,.1f}', colors=cols)

def fig_staff():
    items = [('Investec Group (FY26)',8000,'"8,000+"'),('Close Brothers (FY26)',2500,'about'),('Investec Bank plc (31 Mar 26)',2425,''),('C. Hoare & Co (Mar 25)',573,''),('Peel Hunt (Mar 26)',265,'')]
    return hbar(items, label_w=230, valfmt='{:,.0f}', colors=[NAVY,MUT,ACC,MUT,MUT])

def build4():
    o = part('p4', 'Part 4', 'How Investec stands out, and what only it can claim', 'Eight to ten peers, the design choices where Investec sits at one end of a spectrum, and where it does not lead.')
    o += h2('p4a', 'The peer table')
    o += table(['Firm','Owner / listing','Size (dated)','Model','Recent results','vs Investec'],[
      ['**Investec UK**','DLC: plc LSE, Ltd JSE','UK loans £17.8bn; plc total assets £32.0bn (31 Mar 26)','Private bank + mid-market CIB + broking','Investec plc RoTE 13.7%, ROE 10.8% (FY26)','"Only integrated and diversified mid-market focused specialist bank" (its claim) [S121]'],
      ['Close Brothers','LSE','Loans £9.5bn; ~2,500 staff (31 Jul 26)','Specialist lender; sold asset management and Winterflood','Adj. op. profit £120.3m (−17%); RoTE 5.5%; ~£320m motor provision','Closest "merchant bank" analogue, now a pure lender [S140]'],
      ['Shawbrook','LSE since Oct 2025','Loans £19.2bn (31 Dec 25)','SME, real estate, consumer lender, savings-funded','Underlying RoTE 17.2% (FY25); 18.1% (H1 26)','Bigger UK loan book, higher returns, no private bank or advisory [S142, S240]'],
      ['OakNorth','Private','Facilities £7.2bn (2025)','Digital lender to lower mid-market, UK and US','PBT £223m; adj. ROE 22%; efficiency 26%','Same growth-company lending at far lower cost [S144]'],
      ['Arbuthnot Latham','AIM; family-controlled','Total assets £5.0bn (31 Dec 25)','Private and commercial bank, asset finance, wealth','PBT £24.2m (2025)','"Private bank for entrepreneurs" at about a seventh of Investec UK\'s size [S145]'],
      ['Coutts (NatWest)','Part of NatWest','AUMA £58.5bn; >£127bn with Evelyn','Private bank and wealth','PB&WM ROE 21.7% (2025)','Biggest UK private-bank brand; higher returns; no mid-market IB [S146, S147]'],
      ['Barclays Private Bank','Part of Barclays','Deposits £72.0bn (31 Dec 25)','Private bank and wealth with an IB next door','RoTE 26.3% (2025)','Full universal-bank shelf [S148]'],
      ['HSBC UK commercial','Ring-fenced HSBC sub','CMB loans £76.2bn','Full commercial bank; mid-market £15-350m turnover','CMB PBT £3,424m; C/I 30.5%','Targets the same mid-market; also measures cross-selling [S149]'],
      ['Santander UK CCB','Banco Santander','CCB loans £18.9bn','Corporate & commercial in a retail bank','CCB PBT £324m (2025)','Same-sized corporate book inside a mass bank [S300]'],
      ['Peel Hunt / Panmure Liberum / Deutsche Numis','AIM / private / Deutsche','Peel Hunt 147 retained clients','Research, broking, ECM, M&A','Peel Hunt revenue £143.5m, PBT £21.1m (FY26)','Compete for broking mandates but cannot lend [S305, S306, S307]'],
      ['Rothschild & Co','Family-controlled; delisted 2023','Revenue ~€3.0bn (2025)','Independent advisory + wealth','Net profit €413m (2025)','Far bigger in M&A; does not lend to mid-market [S302]']], cls='')
    o += P('<span class="small">All figures [C] from the cited results unless the source column of WS3 marks them Reported (Rothschild, Coutts+Evelyn AUMA, Panmure, Numis). Measures differ between firms: check like-for-like before comparing aloud.</span>')
    o += fig('Size: where Investec sits against peers', fig_size(), 'Sources: S149 (HSBC UK, 31 Dec 25), S300 (Santander UK, 31 Dec 25), S120 (Investec, 31 Mar 26), S142 (Shawbrook, 31 Dec 25), S140 (Close Brothers, 31 Jul 26), S145 (Arbuthnot, 31 Dec 25). Mixed measures (total assets vs loans) as labelled; not like-for-like.')
    o += fig('Staffing: Investec against peers', fig_staff(), 'Sources: S282 (Investec "8,000+", 21 May 26), S278 (IBP 2,425 at 31 Mar 26), S140 (Close Brothers ~2,500, FY26; Wikipedia gives ~3,000 [S299]), S308 (C. Hoare 573, Mar 25), S305 (Peel Hunt 265, Mar 26). Group figure is a floor ("8,000+").')
    o += h2('p4b', 'The design choices: where Investec sits at one end')
    o += fig('The competitive spectrum: five design axes', fig_spectrum(), 'Positions are the author\'s judgement [I] from the peer data above [S120-S149, S300-S308]. Not a measured scale. Cost efficiency axis uses reported cost-to-income or efficiency ratios.')
    o += h2('p4c', 'Six things only Investec can claim')
    o += table(['Claim','Evidence','Why it matters'],[
      ['A UK private bank, mid-market lending and its own ECM, M&A and broking arm, in one bank','Lenders do not advise (Close, Shawbrook, OakNorth); brokers do not lend (Peel Hunt, Numis); private banks do not do IB (Coutts, Hoare) [S140-S145, S305-S308]','One relationship can earn lending, fee and deposit income over a client\'s whole life'],
      ['#1 in Extel UK small and mid-cap broker rankings, four years running (2026)','S130 [R]','Proof that "investment bank capabilities for the mid-market" is real, not a slogan'],
      ['The only UK bank in this set with a UK/South Africa dual-listed structure, no cross-guarantees','S120, S121 [C]','Diversification across two economies; also complexity'],
      ['Private-client definition led by income and entrepreneurship, not just wealth','"We are not always especially useful to HNW individuals who are simply looking to preserve their wealth" (2018) [S123]','Targets people who need capital, not just safekeeping'],
      ['UK wealth delivered through a 41% stake in Rathbones, with Investec now leading the advice relationship','S120, S80 [C/R]','A partnership model instead of owning a wealth manager outright'],
      ['A new UK Corporate Bank launching 2026, built to feel like private banking','Credit Hub posting [S268]; Andy Hart quote [S226]','Interns in 2027 join a business being built, not a mature one']])
    o += h2('p4d', 'Where Investec does not lead')
    o += UL('**Returns.** Investec plc ROE 10.8% and RoTE 13.7% (FY26), below Shawbrook, OakNorth, Coutts and Barclays PBWM; above Close Brothers [C] [S120, S140-S148].',
            '**Efficiency.** UK cost-to-income 54.0% against about 26% (OakNorth), 30.5% (HSBC UK CMB) and 36% (Shawbrook) [C] [S120, S144, S149, S240].',
            '**Scale.** UK loans £17.8bn, smaller than Shawbrook\'s £19.2bn [C] [S120, S142].',
            '**Credit.** UK credit loss ratio 57bps, above the group\'s 25 to 45bps range [C] [S120].',
            '**Outlook.** FY27 is the "peak investment year"; UK H1 profit guided 2 to 6% lower [C] [S71].',
            '**Awards.** The 2025 Euromoney UK best private bank was Standard Chartered, not Investec [C] [S136].')
    o += box('dont', '"Investec is the best private bank in the UK" or "Investec has the highest returns." Neither is true. Say "distinctive", and show the mechanism.')
    o += END
    return o

def fig_balance():
    b = rect(140, 20, 440, 240, '#fff', NAVY, 4, 2) + f'<line x1="360" y1="20" x2="360" y2="260" stroke="{NAVY}" stroke-width="2"/>'
    b += text(250, 42, 'ASSETS (what the bank owns)', 11, NAVY, 'middle', 'bold') + text(470, 42, 'LIABILITIES + EQUITY (who funded it)', 11, NAVY, 'middle', 'bold')
    b += node(155, 55, 190, 110, 'Loans', 'Mortgages, business loans, fund finance. Earn interest. Can go bad.', fill=ACCS, stroke=ACC)
    b += node(155, 175, 190, 70, 'Cash and liquid assets', 'Ready to pay depositors who want money back', fill=SOFT, stroke=MUT)
    b += node(375, 55, 190, 110, 'Deposits', 'Savers and businesses. Bank pays interest. Can leave quickly.', fill=TEALS, stroke=TEAL)
    b += node(375, 175, 190, 35, 'Wholesale funding', fill=SOFT, stroke=MUT, size=10)
    b += node(375, 215, 190, 35, 'Equity (capital): absorbs losses', fill=SIGS, stroke=SIG, size=9.5)
    b += text(360, 285, 'Profit = interest on loans − interest on deposits + fees − costs − bad debts', 11, NAVY, 'middle', 'bold')
    return svg(720, 300, b)

def fig_rates():
    pts = [('Aug 23',5.25),('Aug 24',5.0),('Nov 24',4.75),('Feb 25',4.5),('May 25',4.25),('Aug 25',4.0),('Dec 25',3.75),('Feb 26',3.75),('Apr 26',3.75),('Jun 26',3.75),('Sep 26',3.75)]
    b = ''; x0=50; w=640; y0=230; sc=lambda v: y0-(v-3)*70
    for v in [3,3.5,4,4.5,5,5.5]:
        b += f'<line x1="{x0}" y1="{sc(v)}" x2="{x0+w}" y2="{sc(v)}" stroke="{LINE}"/>' + text(x0-6, sc(v)+4, f'{v:.2f}%', 8.5, MUT, 'end')
    xs = [x0 + i*w/(len(pts)-1) for i in range(len(pts))]
    d = ' '.join(f'{"M" if i==0 else "L"}{x:.0f},{sc(v):.0f}' for i,(x,(l,v)) in enumerate(zip(xs,pts)))
    b += f'<path d="{d}" fill="none" stroke="{NAVY}" stroke-width="2.5"/>'
    for x,(l,v) in zip(xs,pts):
        b += f'<circle cx="{x:.0f}" cy="{sc(v):.0f}" r="4" fill="{ACC}"/>' + text(x, y0+18, l, 8.5, MUT, 'middle') + text(x, sc(v)-8, f'{v}', 8.5, NAVY, 'middle')
    b += text(560, 70, 'Sep 2026: 6-3 vote to hold;', 9.5, RED, 'middle', 'bold') + text(560, 83, 'three members wanted 4%', 9.5, RED, 'middle', 'bold')
    return svg(720, 255, b)

def fig_shift():
    forces = [('Rates: cuts paused at 3.75%; hike debate','Margins hold up; credit stress rises',ACC),('Private credit ($1.5-2tn globally)','Takes riskier mid-market loans; also a client for fund finance',RED),
              ('Consolidation (TSB, Virgin, Co-op, Tesco Bank)','Scale wins; sub-scale banks sell',NAVY2),('Regulation eases (Basel 3.1 calibration, ring-fence allowance, SM&CR)','Mid-sized banks can grow; big banks lend more too',GRN),
              ('Deposit competition; FSCS £120k; cash ISA cut 2027','Funding costs and saver behaviour shift',TEAL),('Wealth transfer (~£5.5tn over 30 years)','Demand for private banking and advice',SIG),
              ('IPO market recovering (H1 2026 +215%)','Fees for ECM and broking',ACC),('AI and digital','Lower cost to serve; new competitors',NAVY2)]
    b = node(255, 140, 210, 80, 'UK mid-market and specialist banking', fill=NAVY, stroke=NAVY, tc='#fff', size=12)
    import math
    for i,(f,e,c) in enumerate(forces):
        a = i/8*2*math.pi - math.pi/2
        x = 360 + 270*math.cos(a) - 85; y = 180 + 145*math.sin(a) - 26
        b += f'<line x1="360" y1="180" x2="{x+85:.0f}" y2="{y+26:.0f}" stroke="{c}" stroke-width="1.5"/>'
        b += rect(x, y-6, 170, 64, '#fff', c, 5, 1.5) + text(x+85, y+8, f, 8.6, NAVY, 'middle', 'bold', width=36, lh=10) + text(x+85, y+40, e, 8, MUT, 'middle', width=38, lh=9)
    b = b.replace(node(255, 140, 210, 80, 'UK mid-market and specialist banking', fill=NAVY, stroke=NAVY, tc='#fff', size=12), '', 1)
    b += node(265, 150, 190, 60, 'UK mid-market and specialist banking', fill=NAVY, stroke=NAVY, tc='#fff', size=11)
    return svg(720, 380, b)

def build5():
    o = part('p5', 'Part 5', 'The industry from zero', 'What a bank is, the types of UK bank, the products, the vocabulary, and the forces reshaping the sector.')
    o += h2('p5a', 'What a bank actually does')
    o += P('A bank does five things [I] [S150-S205 background]. It **takes deposits**, money it owes back. It **lends** that money out, which earns interest. It **keeps the spread**: interest received minus interest paid is net interest income. It **earns fees** for advice, arranging deals, managing investments and hedging. And it **holds capital**, shareholders\' money that absorbs losses before depositors lose anything. Regulators set how much capital it needs for each pound of risky loans.')
    o += fig('A bank\'s balance sheet in one picture', fig_balance(), 'Generic illustration [I]. Investec figures for each box are in Figure 2.')
    o += box('term', '<b>Net interest margin (NIM)</b>: net interest income divided by the assets that earn interest. It is the bank\'s "spread". It usually widens when rates rise (loans reprice faster than deposits) and narrows when rates fall.')
    o += h2('p5b', 'Types of UK bank, and where Investec fits')
    o += table(['Type','What they are','Examples'],[
      ['Large ring-fenced banks','Must separate retail deposits from investment banking once core deposits pass £35bn','Barclays, HSBC, Lloyds, NatWest, Santander UK [S161]'],
      ['Building societies','Mutuals owned by members; mortgages and savings','Nationwide, Coventry'],
      ['Challenger banks','Smaller banks on mainstream products','TSB, Metro [S186]'],
      ['Specialist banks','Focus on specialist lending','Paragon, Shawbrook, Close Brothers [S186]'],
      ['Digital banks','Technology-led','Starling, Zopa, Monzo [S186]'],
      ['Private banks','Lending, deposits and service for wealthy individuals','Coutts, C. Hoare, Investec Private Bank'],
      ['Investment banks','Advice, capital markets, trading','Goldman Sachs, JPMorgan, Barclays IB']])
    o += P('Investec is a mid-sized specialist bank that also runs a private bank and an advisory and broking arm. It is far below the £35bn ring-fencing threshold [C] [S120, S161]. That makes it a hybrid: specialist lender, private bank and small investment bank in one [I].')
    o += h2('p5c', 'Private banking vs wealth management vs retail')
    o += UL('**Retail banking**: mass-market current accounts, savings, mortgages, cards, standardised at scale.',
            '**Private banking**: balance-sheet products for wealthy individuals (bespoke mortgages, lending, deposits, FX), relationship-managed. Earns interest.',
            '**Wealth management**: managing and advising on investments for a fee, usually a percentage of assets. Needs little capital.',
            'Investec UK keeps private banking in-house and delivers wealth through Rathbones [C] [S120].')
    o += h2('p5d', 'Corporate and investment banking for the mid-market')
    o += table(['Product','Plain English','Investec UK team'],[
      ['Fund finance','Loans to investment funds, secured on investors\' promises to invest (subscription lines) or on the fund\'s assets (NAV loans)','Fund Solutions'],
      ['Direct lending / growth and leveraged finance','Loans to companies, often owned by private equity, sized against earnings','Direct Lending, Growth & Acquisition Finance'],
      ['Real estate lending','Loans secured on property; loan-to-value measures risk','Real Estate'],['Aviation, energy and infrastructure','Loans secured on aircraft, power plants, infrastructure','Specialist sectors'],
      ['Asset finance','Leasing and hire-purchase for equipment and vehicles','Asset Finance (Reading)'],['Advisory / M&A','Fees for advising on buying or selling companies','Advisory'],
      ['ECM and corporate broking','Helping companies raise equity; being a listed company\'s link to investors','ECM, Corporate Broking'],['Hedging','FX forwards, rate swaps and caps for clients','Treasury Risk Solutions']])
    o += P('<span class="small">Product definitions [S150-S205]; team names from Investec pages and postings [S22, S120, S277] (Reported where from snippets).</span>')
    o += h2('p5e', 'The rate cycle, verified')
    o += fig('Bank of England Bank Rate, August 2023 to September 2026', fig_rates(), 'Sources: Bank of England MPS pages [S150-S156, S230-S235]. Aug 2023 to Nov 2024 levels are background, not re-fetched. Feb 2025 was a cut to 4.5% (some aggregators wrongly say hold) [S152]. September 2026 vote checked on the BoE page on 5 Oct 2026. Next decision 5 Nov 2026.')
    o += P('Rates were cut from 5.25% to 3.75% between August 2024 and December 2025. Since then the Monetary Policy Committee has held at 3.75% at every meeting of 2026, and the debate has turned toward hiking. In September 2026 the vote was 6 to 3, with Megan Greene, Catherine Mann and Huw Pill voting for 4% [C] [S150, S230]. The Bank blames "protracted conflict in the Middle East" pushing energy prices up. CPI inflation was 3.1% in August 2026 and is expected above 4% in early 2027 [C] [S230].',
           '**What it means for a bank like Investec** [I]: a pause in cuts protects net interest income, which fell in FY26 as rates came down. But higher-for-longer rates and an energy shock put pressure on leveraged borrowers and property, where a specialist lender is exposed.')
    o += h2('p5f', 'The forces reshaping the sector')
    o += fig('The industry shift map', fig_shift(), 'Sources: S150 (rates), S188 (private credit, FSB, 6 May 2026), S193-S196 (consolidation), S157, S161, S165 (regulation), S176, S198 (FSCS, ISA), S199 (wealth transfer, industry estimate), S183 (IPOs, EY data via secondary), S191 (AI, Deloitte). Arrows show influence, not measured size.')
    o += UL('**Consolidation.** Nationwide bought Virgin Money (completed 1 Oct 2024), Barclays bought Tesco Bank (1 Nov 2024), Coventry bought Co-operative Bank (1 Jan 2025), Santander UK bought TSB for £2.65bn (completed 30 Apr 2026) [R/C] [S193-S196, S242]. EY: "M&A across this segment is poised to accelerate" [C] [S187].',
            '**Mid-tier squeeze.** EY found the challenger and specialist cohort\'s ROE fell to 6.9% in 2024 from 8.8%; specialists 5.5% [C] [S187].',
            '**Mid-tier banks matter.** Small and mid-tier banks provide about 60% of UK SME lending, "a doubling over the last decade" [C] [S186].',
            '**Private credit.** The FSB estimates non-bank direct lending to mid-sized firms at $1.5 to 2tn globally (end-2024); the UK is the third-largest market. Banks also lend to these funds: about $220bn of credit lines in member data, possibly more than twice that [C] [S188].',
            '**Growth agenda.** The Leeds Reforms (15 July 2025) aim to make the UK "the number one destination for financial services companies by 2035" [R] [S197].')
    o += h2('p5g', 'Where it goes in three to five years: four views')
    o += table(['View','Argument','Evidence','What it means for Investec [I]'],[
      ['A. Private credit eats the mid-market','Post-crisis rules and faster non-bank lenders pull riskier lending off bank balance sheets','FSB cites bank regulation and demand for "fast execution" [S188]; McKinsey names asset classes where private credit gains [S190]','Pressure on direct lending and leveraged finance margins'],
      ['B. Frenemies','Banks lend to funds, sell risk to them, partner on origination','~$220bn+ bank lines to funds [S188]; McKinsey on partnering [S189]','Fund Solutions is the bridge: Investec earns from the boom'],
      ['C. Tailwinds favour scaled specialists','Basel 3.1 SME adjustments, higher MREL thresholds, IRB help for mid-sized banks, consolidation','S157, S158, S178, S187','Reaching IRB and scale lifts UK returns'],
      ['D. Margin squeeze','Rate cuts and cost inflation squeeze the middle; lending growth slows','EY ROE data [S187]; EY ITEM sees lending growth of 2.2% in 2027 [S185]','UK cost-to-income of 54% leaves little room']])
    o += box('op', 'A defensible synthesis [I]: B plus C. Banks keep the relationship, hedging, deposits and fund finance, and pass the riskiest tranches to private credit. Mid-tier banks consolidate. Winners have cheap sticky deposits, capital-efficient models and fee streams. Where do you land, and what evidence would change your mind?')
    o += END
    return o

def fig_regtl():
    ev = [('2013','PRA and FCA created (1 Apr)'),('2016','SM&CR for banks (7 Mar)'),('2019','Ring-fencing in force (1 Jan)'),('2023','Consumer Duty (31 Jul)'),
          ('Feb 25','Ring-fence threshold £35bn (4 Feb)'),('Jul 25','Leeds Reforms; MREL £25-40bn; Basel dates (15 Jul)'),('Aug 25','Supreme Court motor ruling (1 Aug)'),
          ('Dec 25','FSCS £120k (1 Dec); FPC benchmark 13% (2 Dec)'),('Jan 26','PS1/26 Basel 3.1 final; PS4/26 small banks (20 Jan)'),('Mar 26','Motor redress PS26/3 £9.1bn (30 Mar)'),
          ('Apr 26','SM&CR first wave (22 Apr)'),('May 26','Ring-fencing review: 10% growth allowance (18 May)'),('Jul 26','Tribunal partly suspends motor scheme'),
          ('Jan 27','Basel 3.1 and small-bank capital regime in force (1 Jan)'),('Jan 28','Basel 3.1 market-risk models')]
    b = ''
    for i,(d,t) in enumerate(ev):
        col = i // 8; row = i % 8
        x = 20 + col*350; y = 14 + row*44
        hot = d in ('Jan 27','Jan 26','Mar 26','Jul 26')
        b += rect(x, y, 70, 34, ACC if hot else NAVY, 'none', 4) + text(x+35, y+22, d, 10.5, '#fff', 'middle', 'bold')
        b += rect(x+76, y, 262, 34, ACCS if hot else SOFT, LINE, 4) + text(x+84, y+14, t, 9.2, NAVY, width=48, lh=11)
    return svg(720, 380, b)

def build6():
    o = part('p6', 'Part 6', 'The role\'s own industry and its regulation', 'For an intern in a UK specialist bank, the "sub-industry" is UK bank regulation. Dates and instrument names checked against the Bank of England, FCA and Treasury.')
    o += P('Get these dates exactly right. They are the highest-leverage technical points you can make, and most candidates get them wrong.')
    o += fig('UK bank regulation timeline, 2013 to 2028', fig_regtl(), 'Sources: S157, S158, S159, S161, S165, S167, S169, S172, S173, S176, S178 (BoE, PRA, FCA, HMT; Confirmed except Supreme Court date, Reported via law firms). 2013 to 2019 dates are background. Orange = live in the next 12 months.', full=True)
    o += h2('p6a', 'Who regulates a UK bank')
    o += UL('**PRA** (part of the Bank of England): safety and soundness. Capital, liquidity, governance.',
            '**FCA**: conduct. Fair treatment of customers (Consumer Duty), markets, listing rules, consumer credit.',
            '**Financial Policy Committee** (Bank of England): the whole system. Countercyclical buffer (2%), stress tests [C] [S178, S179].',
            '**HM Treasury**: writes the laws (FSMA 2000 and 2023; ring-fencing orders).',
            'Dual regulation began on 1 April 2013 [background].')
    o += h2('p6b', 'Basel 3.1')
    o += P('The PRA published its final rules, **PS1/26**, on **20 January 2026**. They apply from **1 January 2027**, except the internal model approach for market risk, from **1 January 2028** [C] [S157]. The output floor stops banks using models from cutting risk-weighted assets below 72.5% of the standardised figure, phased in to 2030 [R] [S157]. SME and infrastructure adjustments are meant to ensure that removing old support factors "does not cause an increase in overall capital requirements" [C] [S157].')
    o += box('say', '"Basel 3.1 goes live on 1 January 2027 under PS1/26. For Investec plc, which is on the standardised approach and says it is on its journey to IRB, the revised standardised risk weights and the route to IRB matter directly to how cheaply it can lend."')
    o += h2('p6c', 'Ring-fencing')
    o += P('The threshold rose from £25bn to **£35bn** of core deposits on **4 February 2025**, through SI 2025/30. This was the "Smarter Ring-Fencing Reforms", not the Leeds Reforms [C] [S161, S163]. The Ring-Fencing Review published on **18 May 2026** kept £35bn, set reviews every three years from **Q2 2028**, and proposed a **growth allowance** of up to 10% of Pillar 1 credit-risk RWAs, which could unlock "up to £80 billion of financing" [C] [S161, S162]. Investec\'s UK deposits (£22.5bn) are well below the threshold, so it is very likely not ring-fenced, but no Investec statement saying so was found [I] [S120].')
    o += h2('p6d', 'Small and mid-sized banks')
    o += UL('**Strong and Simple**: a simpler regime for banks with no more than £20bn of total assets; simplified capital from **1 January 2027** under PS4/26 [C] [S159]. Investec is too large and pursues IRB, so it is not eligible [I].',
            '**MREL** (bail-in debt): indicative thresholds raised to £25 to 40bn of total assets, effective 1 January 2026 [C/R] [S158, S164].',
            '**FPC benchmark**: system Tier 1 capital benchmark cut from about 14% to about 13% of RWAs on 2 December 2025 [C] [S178].')
    o += h2('p6e', 'Conduct: Consumer Duty and motor finance')
    o += P('**Consumer Duty** (PS22/9): in force 31 July 2023 for open products and 31 July 2024 for closed ones. "A firm must act to deliver good outcomes for retail customers." Four outcomes: products and services; price and value; consumer understanding; consumer support [C] [S167, S168].',
           '**Motor finance.** The Supreme Court ruled on 1 August 2025 that dealers were not fiduciaries, but upheld one claim of an unfair relationship under s.140A of the Consumer Credit Act [R] [S173]. The FCA consulted (CP25/27, 7 Oct 2025), then confirmed a redress scheme in **PS26/3 on 30 March 2026**: 12.1m agreements, £7.5bn of redress, £9.1bn total cost [C] [S169]. On 2 July 2026 the Upper Tribunal partly suspended it pending challenges; hearing 14 to 18 December 2026 or 16 to 26 February 2027 [C] [S172, S237]. Investec: "its existing £30 million provision... remains appropriate" [C] [S70].')
    o += h2('p6f', 'Accountability, deposits and listings')
    o += UL('**SM&CR**: applies to banks since 7 March 2016. First wave of reforms confirmed 22 April 2026: about 15% fewer certification roles, thresholds raised 30% [C] [S165].',
            '**FSCS**: deposit protection rose from £85,000 to **£120,000 on 1 December 2025** [C] [S176].',
            '**Listing Rules**: single ESCC category from 29 July 2024 [R] [S181]. **PISCES** sandbox opened June 2025 [R] [S182]. Seven UK IPOs raised £577m in H1 2026, up 215% [R] [S183].')
    o += box('unc', 'The SM&CR commencement date is given as 22 April 2026 (FCA press release date) in one source and 24 April in another. The Santander/TSB completion is 30 April 2026 per Santander [S242]. The £173bn figure for UK banks\' private-markets exposure was seen only in a snippet; do not quote it.')
    o += END
    return o

NEWS = [
 ('Investec FY26: steady growth, "peak investment year" ahead','Investec RNS, 21 May 2026','S220',
  'Adjusted operating profit up 3.4% to £951.0m; ROE 13.6%; dividend 38.5p. Southern Africa grew faster than the UK. Management calls FY27 the peak investment year, with UK RoTE guided 12.5 to 13.5%, near the bottom of the 13 to 17% range.',
  'The UK earns below its own range; the investment programme is the plan to close the gap.','New roles and projects sit in UK private banking and the mid-market corporate bank.',
  '"Which investments matter most for getting UK returns back into range, and how will you know by FY28 that they are working?"'),
 ('Pre-close update: South Africa strong, UK behind','Investec RNS, 18 Sep 2026','S222',
  'UK adjusted operating profit for the half to 30 Sep 2026 guided 2 to 6% behind; Southern Africa up to 6% ahead in rand. Loans £37.0bn, deposits £46.0bn. Interim results on 19 Nov 2026.',
  'UK profit falls while spending continues.','The latest official numbers you can quote. Re-read on 19 Nov.',
  '"Loans are growing faster than deposits. Is the new private bank current account meant to close that funding gap?"'),
 ('Investec\'s UK private bank push','City AM and Reuters, 21 May 2026','S225, S224',
  '£30m to expand the UK private bank; current accounts and a first UK credit card, full service in H2 2027. City AM reports doubling from 8,000 to 16,000 households; Reuters reports about 5,000 extra UK clients. The figures conflict.',
  'The main UK growth bet, built with Rathbones.','The 2027 cohort arrives just before launch.',
  '"How do you win affluent clients\' current accounts against Coutts and NatWest-Evelyn without competing on price?"'),
 ('Rathbones stops its buyback at Investec\'s 29.9% cap','Alliance News via AJ Bell, 13 Jul 2026','S227',
  'Rathbones ended its buyback because Investec\'s voting stake reached the 29.9% agreed in 2023 (41.25% economic). 30% is where the UK Takeover Code normally forces a bid.',
  'Rathbones is a big profit source and the investment engine of the private client plan.','Shows how deal structure (votes vs economics) shapes strategy later.',
  '"Is the Rathbones stake strategic or financial, now that votes are capped and Rathbones is in FCA remediation?"'),
 ('Corporate banking that "feels like private banking"','Bdaily, 12 Jul 2026','S226',
  'Terry Koizou hired to lead client relationship management in UK Corporate Banking; the team is to grow past 40 relationship managers. Andy Hart: "corporate banking that feels like private banking."',
  'The second half of the UK investment programme.','An internship could place you here. Learn the pitch.',
  '"OakNorth and Shawbrook lend at lower cost. What is the edge beyond service?"'),
 ('Bank of England: holding at 3.75%, three votes to hike','Bank of England, 17 Sep 2026','S230',
  'Vote 6 to 3 to hold; Greene, Mann and Pill wanted 4%. CPI 3.1% in August, seen above 4% in early 2027. Energy prices driven up by conflict in the Middle East. Next decision 5 Nov 2026.',
  'Supports interest income; tests credit quality.','Know the rate, the direction and the date.',
  '"In February the debate was when to cut. By September a third of the MPC wanted a hike. For a lender, does that become wage inflation or credit losses?"'),
 ('Budget on 28 October: are banks a target?','LBC citing The Telegraph, 29 Aug 2026; IfG, 7 Sep 2026','S246, S244',
  'The Chancellor is reported to be considering a windfall tax on banks and oil companies. Not confirmed. Banks already pay a 3% surcharge on top of 25% corporation tax. Andy Burnham became Prime Minister on 20 July 2026; John Healey is Chancellor.',
  'Investec plc is a UK bank; design of any tax decides whether mid-sized banks are hit.','Likely the news story around interview time.',
  '"A blunt windfall tax hits specialists that fund SME lending harder than the big four, and cuts against the growth agenda." Present as a debate.'),
 ('Motor finance redress: confirmed, then partly frozen','FCA, 30 Mar and 2 Jul 2026','S236, S237',
  '£7.5bn redress over 12.1m agreements; Upper Tribunal partly suspended the scheme on 2 Jul 2026 after challenges by lenders and a consumer group. Hearing Dec 2026 or Feb 2027. Investec\'s provision: £30m.',
  'Small exposure; but a test of UK regulatory predictability.','Links law, regulation and capital.',
  '"Does the saga argue for more predictable, less retrospective redress, or for stronger conduct rules?"'),
 ('Consolidation: NatWest buys Evelyn; Santander completes TSB','NatWest, 9 Feb 2026; Santander UK, 1 May 2026','S243, S242',
  'NatWest buying Evelyn Partners for £2.7bn (combined AUM ~£127bn). Santander completed TSB for £2.65bn, "the single largest investment in the sector for over 15 years".',
  'A much bigger rival in the affluent and HNW segment Investec targets.','Textbook strategic-rationale cases.',
  '"Scale is winning in UK wealth. Is Investec\'s partnership model as strong as owning a wealth manager?"'),
 ('Close Brothers: turnaround under motor finance pain','Close Brothers RNS, 29 Sep 2026','S239',
  'Adjusted operating profit down 17% to £120.3m; statutory loss £60.3m; motor provision about £320m; no final dividend. "Close Brothers decided not to challenge the scheme."',
  'Shows the value of Investec\'s diversification.','The obvious peer to compare.',
  '"Close is shrinking to its core while Investec invests to grow. Which strategy wins if rates stay high and credit turns?"'),
 ('Shawbrook one year after IPO; the IPO market','Shawbrook RNS, 5 Aug 2026; EY data, 8 Jul 2026','S240, S254',
  'Shawbrook H1 2026: underlying RoTE 18.1%, cost-to-income 36.4%. UK IPOs: seven deals raised £577m in H1 2026, up 215%.',
  'The benchmark investors use for Investec UK; a recovering IPO market helps broking and ECM.','London listings are a common interview topic.',
  '"Is Shawbrook\'s 18% RoTE a fair benchmark for a higher-touch model?"'),
 ('Regulation 2026: Basel 3.1, ring-fencing, SM&CR, private credit warnings','PRA 20 Jan; HMT 18 May; FCA 22 Apr; BoE FPC Sep 2026','S249-S252',
  'Basel 3.1 from 1 Jan 2027; ring-fencing growth allowance; lighter SM&CR; the FPC says "risk-taking in parts of private markets and risky credit markets remained elevated."',
  'Capital rules for SME and property lending change; private credit is both rival and client.','The growth agenda is the policy theme of 2026.',
  '"Is risk moving back into banks as rules ease, or just out of sight into private credit?"')]

def build7():
    o = part('p7', 'Part 7', 'What is happening right now', 'Twelve stories from the last nine months, each with why it matters and a question to raise. Check every one again before the interview.')
    o += box('unc', 'The 2026 backdrop is different from most interview guides: a Middle East conflict pushed Brent to $106 a barrel on 14 Sep 2026; Bank Rate has been held at 3.75% all year; Andy Burnham became Prime Minister on 20 Jul 2026 [C] [S230, S244]. The bank windfall tax is a press report, not policy [R] [S246]. Dates to watch: Budget 28 Oct; MPC 5 Nov; Investec interims 19 Nov; motor finance tribunal Dec 2026 or Feb 2027; Basel 3.1 1 Jan 2027.')
    for i,(h,d,s,what,firm,role,q) in enumerate(NEWS):
        o += (f'<div class="news"><div class="h">{i+1}. {esc(h)}</div><div class="d">{esc(d)} · [{s}]</div>'
              f'{md("<b>What happened:</b> " + what)}<br>{md("<b>Why it matters to Investec:</b> " + firm + " [I]")}<br>'
              f'{md("<b>Why it matters to you:</b> " + role)}<br>{md("<b>Raise:</b> " + q)}</div>')
    o += END
    return o

DEBATES = [
 ('Is One Investec a real edge or a slogan?','Real: unified mid-market division, Rathbones moving to Investec-led advice, Extel #1 broking alongside lending [S121, S120, S130].','Slogan: no UK cross-holding figure is published; HSBC UK also grows cross-referrals 8% [S149].'),
 ('Is the UK investment programme worth it?','Yes: fees grew 14.7%; primary-bank relationships give sticky deposits and fees that survive rate cuts [S70].','Not yet: UK RoTE guided 12.5 to 13.5%, UK H1 profit 2 to 6% lower; cost-to-income already 54% [S70, S71].'),
 ('Should Investec own its UK wealth business again?','Yes: Coutts-Evelyn shows scale wins; owning 100% captures all the fees [S243].','No: the 41% stake gives profit (£76.6m) without full capital and conduct risk; Rathbones\' 2026 remediation shows that risk [S70, S81].'),
 ('Is private credit a threat or an opportunity?','Threat: takes leveraged lending; faster and more flexible [S188].','Opportunity: fund finance lends to those funds; FSB counts ~$220bn+ of bank lines [S188].'),
 ('Is the DLC structure a strength?','Strength: diversification; South Africa (ROE 18.2%) carried FY26 [S70].','Weakness: complexity, two capital regimes, harder valuation [I].'),
 ('Should banks face a windfall tax?','For: higher rates lifted bank margins without extra effort.','Against: hits specialist SME lenders harder; contradicts the growth agenda [S246, S247].'),
 ('Is Basel 3.1 good for Investec?','Good: SME and infrastructure adjustments, clearer path to IRB [S157].','Bad: output floor and new standardised weights could raise capital for some books [I].'),
 ('High-touch vs low-cost lending?','High-touch: clients with complex needs pay for judgement and speed [S123, S125].','Low-cost: OakNorth (efficiency 26%) and Shawbrook (C/I 36%) earn more [S144, S240].')]

def build8():
    o = part('p8', 'Part 8', 'Forming your own view: both sides of every argument', 'Eight live debates. For each, the case for and against with sources, and a space for your own view.')
    for q,a,b in DEBATES:
        o += f'<div class="avoid"><h3>{esc(q)}</h3>' + table(['The case for','The case against'], [[a, b]]) + box('op', 'Write your one-sentence view, the strongest evidence for it, and what would change your mind.') + '</div>'
    o += box('say', 'Formula for any opinion: "On balance I think X, because [one fact with a source]. The best counter-argument is Y. What would change my mind is Z."')
    o += END
    return o
