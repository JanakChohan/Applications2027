from lib import *

def fig_moneyflow():
    b = ''
    # columns: funding -> balance sheet -> revenue -> costs -> profit
    b += text(20, 22, 'WHERE THE MONEY COMES FROM', 10, MUT, 'start', 'bold')
    b += text(260, 22, 'WHAT THE BANK DOES WITH IT', 10, MUT, 'start', 'bold')
    b += text(520, 22, 'WHAT IT EARNS AND SPENDS', 10, MUT, 'start', 'bold')
    b += node(20, 40, 200, 90, 'Customer deposits £44.7bn', 'Private clients, Investec Save savers, corporates. UK & Other: £22.5bn', fill=TEALS, stroke=TEAL)
    b += node(20, 145, 200, 70, 'Equity £6.1bn', 'Shareholders of Investec plc (LSE) and Investec Ltd (JSE)', fill=TEALS, stroke=TEAL)
    b += node(20, 230, 200, 60, 'Wholesale funding', 'Bonds and other market funding (size not extracted)', fill=SOFT, stroke=MUT)
    b += node(260, 40, 220, 95, 'Net core loans £35.5bn', 'UK & Other £17.8bn: mortgages to private clients, fund finance, direct lending, real estate, aviation, energy & infrastructure', fill=ACCS, stroke=ACC, subw=44)
    b += node(260, 150, 220, 55, 'Cash and near cash £18.2bn', 'Liquidity buffer (plc LCR 349%)', fill=ACCS, stroke=ACC)
    b += node(260, 220, 220, 70, 'Advice, broking, hedging, Rathbones stake', 'Earns fees, not interest; uses little balance sheet', fill=ACCS, stroke=ACC)
    for y1,y2 in [(85,85),(180,115),(260,178)]:
        b += arrow(222, y1, 258, y2)
    b += node(520, 40, 190, 70, 'Net interest income £1,335.8m', '58.6% of revenue (down 1.6%)', fill=GRNS, stroke=GRN)
    b += node(520, 120, 190, 85, 'Non-interest revenue £945.7m', 'Fees £506.0m, customer-flow trading £169.9m, investment £142.0m, other £27.6m', fill=GRNS, stroke=GRN)
    b += arrow(482, 85, 518, 75); b += arrow(482, 255, 518, 170)
    b += rect(520, 215, 190, 30, '#fff', NAVY2) + text(615, 235, 'Revenue £2,281.4m (+4.2%)', 11, NAVY, 'middle', 'bold')
    b += node(520, 260, 90, 60, 'Costs £1,205.3m', 'C/I 52.9%', fill=REDS, stroke=RED, size=10)
    b += node(620, 260, 90, 60, 'Credit losses £124.2m', '36bps', fill=REDS, stroke=RED, size=10)
    b += arrow(615, 246, 565, 258); b += arrow(615, 246, 665, 258)
    b += rect(470, 340, 240, 64, NAVY, NAVY) + text(590, 365, 'Adjusted operating profit £951.0m', 12.5, '#fff', 'middle', 'bold') + text(590, 384, 'ROE 13.6% · ROTE 15.7% · EPS 82.9p', 10, '#c9d3e6', 'middle') + text(590, 398, 'UK & Other £462.7m · Southern Africa £488.3m', 9.5, '#c9d3e6', 'middle')
    b += arrow(615, 322, 600, 338)
    b += node(20, 330, 200, 74, 'Dividend 38.5p a share', 'About 46% payout; plus buybacks (about £110m completed in FY26)', fill=SIGS, stroke=SIG)
    b += node(240, 330, 210, 74, 'Retained capital', 'Funds loan growth: CET1 plc 13.0% (standardised), Ltd 13.6% (AIRB)', fill=SIGS, stroke=SIG)
    b += arrow(470, 372, 452, 372) + path('M245,404 L245,412 L120,412 L120,406', MUT)
    b += text(20, 425, 'Items do not sum exactly: adjusted operating profit excludes some items and includes the share of associate (Rathbones) profit.', 9, MUT)
    return svg(720, 435, b)

def fig_layers():
    b = ''
    layers = [('CLIENTS', 'Entrepreneurs and high-income professionals · mid-market companies · PE sponsors and funds · savers', TEALS, TEAL),
              ('FRONT LINE: UK SPECIALIST BANK', 'Private Banking  |  Corporate & Investment Banking (lending niches, advisory, ECM and broking, Treasury Risk Solutions, transactional banking)', ACCS, ACC),
              ('THE CENTRE: IBP BUSINESS ENABLEMENT', 'Risk · Compliance · Legal · Finance · Treasury (own funding) · Technology & Digital · Change & Ops · People & Organisation · Marketing', SOFT, NAVY2),
              ('CAPITAL AND GOVERNANCE', 'Investec plc (LSE) and Investec Ltd (JSE) under one DLC board · PRA and FCA regulation · Rathbones associate stake', SIGS, SIG)]
    for i,(t,d,f,s) in enumerate(layers):
        y = 10 + i*78
        b += rect(110, y, 600, 64, f, s, 6, 1.5)
        b += text(125, y+24, t, 12, NAVY, 'start', 'bold')
        b += text(125, y+42, d, 9.6, NAVY2, 'start', width=108, lh=12)
    flows = [('needs, fees, deposits', 'service, credit, advice'), ('requests, risk to approve', 'approvals, systems, people'), ('capital and limits', 'returns and reports')]
    for i,(up,down) in enumerate(flows):
        y = 74 + i*78
        b += arrow(60, y+14, 60, y-2, MUT) + text(10, y+4, up, 8, MUT, width=12, lh=9)
        b += arrow(90, y-2, 90, y+14, ACC, accent=True)
    b += text(10, 330, 'Grey arrows: what flows up. Orange arrows: what flows down. Structure from Investec results and careers postings; centre labels are the careers-site categories.', 8.5, MUT)
    return svg(720, 340, b)

def fig_unit():
    b = node(250, 110, 220, 110, 'One lending team (e.g. Fund Solutions)', 'Bankers who originate deals, analysts who build models and credit papers, a team head', fill=ACCS, stroke=ACC, size=12)
    draws = [(20,20,'Credit risk','Independent approval at credit committee'),(250,10,'Treasury','Funding cost and liquidity for each loan'),
             (490,20,'Legal','Loan documents, security'),(20,250,'Compliance and KYC','Client onboarding, conflicts, financial crime'),
             (250,270,'Operations','Drawdowns, payments, loan servicing'),(490,250,'Finance and capital','Risk-weighted assets, P&L, reporting'),
             (20,135,'Technology','Systems, data, models'),(530,135,'People & Org','Hiring, interns, training')]
    for x,y,t,s in draws:
        b += node(x, y, 190, 60, t, s, fill=SOFT, stroke=NAVY2, size=10.5)
        cx, cy = x+95, y+30
        b += f'<line x1="{cx}" y1="{cy}" x2="360" y2="165" stroke="{LINE}" stroke-width="1.4" stroke-dasharray="4,3"/>'
    b = b.replace(node(250, 110, 220, 110, 'One lending team (e.g. Fund Solutions)', 'Bankers who originate deals, analysts who build models and credit papers, a team head', fill=ACCS, stroke=ACC, size=12), '')
    b += node(250, 110, 220, 110, 'One lending team (e.g. Fund Solutions)', 'Bankers who originate deals, analysts who build models and credit papers, a team head', fill=ACCS, stroke=ACC, size=12)
    return svg(720, 340, b)

def fig_history():
    ev = [(1974,'Founded in Johannesburg as a small leasing and finance company'),(1980,'Banking licence; about 8 people when Koseff joins'),
          (1992,'Enters the UK'),(1998,'Buys Guinness Mahon and Hambros (UK)'),(2002,'Dual-listed: Investec plc (LSE) + Investec Ltd (JSE)'),
          (2007,'Buys Kensington (UK subprime) just before the crisis'),(2011,'Buys Evolution Group (UK broking)'),
          (2014,'Sells Kensington (£180m) and Australia (A$440m)'),(2020,'Asset management demerged as Ninety One'),
          (2023,'UK wealth combined with Rathbones'),(2025,'Mid-market strategy launch'),(2026,'Private client strategy; FY26 profit £951m; 8,000+ staff')]
    x0, x1 = 55, 665; y = 150
    b = f'<line x1="{x0-25}" y1="{y}" x2="{x1+25}" y2="{y}" stroke="{NAVY}" stroke-width="3"/>'
    for i,(yr,t) in enumerate(ev):
        x = x0 + i*(x1-x0)/(len(ev)-1); up = i % 2 == 0
        b += f'<circle cx="{x:.1f}" cy="{y}" r="5" fill="{ACC}"/>'
        ty = 40 if up else 182
        b += f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{ty+(52 if up else -12)}" stroke="{LINE}"/>'
        b += text(x, ty, str(yr), 10.5, ACC, 'middle', 'bold')
        b += text(x, ty+12, t, 8.2, NAVY, 'middle', width=21, lh=9.5)
    b += text(360, 268, 'Events evenly spaced; not to time scale.', 8.5, MUT, 'middle')
    return svg(720, 278, b)

def fig_stability():
    # UK Specialist Bank and Group adjusted operating profit
    data = [('FY25 group', 920.0, NAVY2), ('FY26 group', 951.0, NAVY2), ('FY25 UK SB', 410.4, ACC), ('FY26 UK SB', 401.6, ACC)]
    b = ''
    maxv = 1000
    for i,(l,v,c) in enumerate(data):
        x = 40 + i*90; h = v/maxv*190
        b += f'<rect x="{x}" y="{220-h:.1f}" width="60" height="{h:.1f}" fill="{c}" rx="2"/>'
        b += text(x+30, 214-h, f'£{v:,.1f}m', 9.5, NAVY, 'middle', 'bold') + text(x+30, 236, l, 9, MUT, 'middle')
    b += f'<line x1="30" y1="220" x2="400" y2="220" stroke="{MUT}"/>'
    b += text(220, 262, 'Adjusted operating profit, £m. Group vs UK & Other Specialist Banking.', 9, MUT, 'middle')
    ev = [('2008','Global crisis: no government bailout (Koseff)'),('2014','Sold Kensington and Australia; CET1 expected 8.8% to ~11.3%'),
          ('2020','Ninety One demerged'),('2023','UK wealth to Rathbones'),('FY27','"Peak investment year": UK H1 profit guided 2-6% lower')]
    for i,(d,t) in enumerate(ev):
        y = 30 + i*46
        b += f'<circle cx="440" cy="{y}" r="6" fill="{SIG}"/>' + text(456, y+4, d, 11, SIG, 'start', 'bold') + text(500, y+4, t, 9.2, NAVY, 'start', width=40, lh=11)
        if i < 4: b += f'<line x1="440" y1="{y+6}" x2="440" y2="{y+40}" stroke="{SIGS}" stroke-width="3"/>'
    return svg(720, 275, b)

def fig_centre():
    b = node(250, 10, 220, 46, 'Investec Bank plc (IBP) · CEO', fill=NAVY, stroke=NAVY, tc='#fff')
    fronts = ['Private Banking','Corporate Banking (mid-market)','Lending niches: Fund Solutions, Direct Lending, Real Estate, Aviation, Energy & Infra','Advisory, ECM, Corporate Broking','Treasury Risk Solutions / dealing']
    for i,t in enumerate(fronts):
        x = 10 + i*142
        b += node(x, 90, 132, 66, t, fill=ACCS, stroke=ACC, size=9.5)
        b += path(f'M360,56 L360,72 L{x+66},72 L{x+66},88', MUT)
    b += rect(10, 180, 700, 120, SOFT, NAVY2, 6, 1.2)
    b += text(360, 198, 'IBP BUSINESS ENABLEMENT (the centre)', 11, NAVY, 'middle', 'bold')
    cats = [('Business Enablement','19'),('Technology & Digital','10'),('Compliance, Risk & Legal','9'),('Change & Ops','3'),('HR & Marketing','2'),('Admin','3'),('Early Careers','1')]
    for i,(t,n) in enumerate(cats):
        x = 22 + i*98
        b += node(x, 212, 90, 76, t, f'{n} open roles', fill='#fff', stroke=LINE, size=9.2, subsize=8.6)
    b += text(360, 318, 'Open-role counts: Investec careers site categories, 5 Oct 2026 [S3]. Front-line labels from results and postings. Not an official org chart.', 8.5, MUT, 'middle')
    return svg(720, 326, b)

def build():
    o = part('p2', 'Part 2', 'The firm as a business, from the inside', 'How Investec was founded, how it makes money, what it promises each kind of client, how it controls risk, and what it has got wrong.')
    o += h2('p2a', 'A. The founding insight')
    o += P('Investec started in Johannesburg in 1974 as a small leasing and finance company called Investors, Technical and Executors [R] [S83]. Founder lists vary between sources. The safe line is: founded in 1974 by a small group led by Ian Kantor; Bernard Kantor joined in 1978 and Stephen Koseff in 1980 [R] [S83, S85].',
           'What the founders did before matters, because it explains the design. Ian Kantor was an electrical engineer with an MBA who had worked at IBM and came from Lease Plan International. Leasing experience gave the firm its first idea: lend into a niche you understand better than the big banks do [R] [S83]. Stephen Koseff was a chartered accountant who joined when the firm had about 8 people [R] [S83, S84]. The firm got its banking licence in 1980 and entered the UK in 1992 [R] [S83].',
           'Kantor describes a founding rule in which each founder had a veto: "This thing of \'you can do anything you like as long as there is consensus\' became the basis of Investec\'s culture" [R] [S83]. Three habits trace back to that start [I]: decisions made by consensus after challenge (the "dedicated partnership" value), lending into niches learned in leasing, and moving money offshore to diversify away from South African rand risk, which led to London.')
    o += box('term', '<b>Dual-listed company (DLC)</b>: two separately listed parent companies that run as one economic group with one board. Investec plc is listed in London and Investec Limited in Johannesburg, since July 2002. There are no cross-guarantees between them, so the UK bank\'s creditors rely on the UK side only [C] [S70, S120].')
    o += P('**Purpose and values.** Investec states its purpose as "to create enduring worth" and pairs it with the brand promise "Out of the Ordinary" [R] [S107]. Fani Titi used the purpose line in the FY26 results [C] [S70]. The four values are **Client focus, Cast-iron integrity, Distinctive performance, Dedicated partnership** [R] [S106]. The names are well corroborated, but investec.com blocked direct reading, so paraphrase the descriptions rather than quoting them.')
    o += box('say', '"What I find interesting is that the culture has a mechanism behind it. Ian Kantor says the founders each had a veto, so you could do anything as long as there was consensus. That is where the dedicated partnership value comes from: test your idea, invite challenge, then own the result."')
    o += fig('Investec in twelve dates, 1974 to 2026', fig_history(), 'Sources: S83, S84, S85 (founding, milestones: Reported); S102, S103 (2014 disposals); S78 (Rathbones 2023); S70 (FY26). JSE listing year is disputed (1986 or 1988) and is left off. Staff numbers: "about 8 people" in 1980 [S83] and "about 8,000" in 2026 [S70] (Reported).')

    o += h2('p2b', 'B. How the firm makes money')
    o += P('A bank borrows money cheaply (deposits from savers), lends it at a higher rate, and keeps the difference. That difference is **net interest income**. It also charges fees for advice, arranging deals, hedging and broking, which are **non-interest revenue**. Take away staff and system costs, and the money set aside for loans that go bad, and what is left is profit [C] [S70].',
           'In the year to 31 March 2026 (FY26) the group earned revenue of £2,281.4m. Net interest income was £1,335.8m (58.6%) and non-interest revenue £945.7m (41.4%). Costs were £1,205.3m, so the cost-to-income ratio was 52.9%. Credit losses were £124.2m, a credit loss ratio of 36 basis points. Adjusted operating profit was £951.0m, up 3.4% [C] [S70].',
           'Two things moved. Net interest income fell 1.6% as UK rates came down. Fees rose 14.7% to £506.0m [C] [S70]. The mix is shifting toward fees, which fits a strategy to depend less on interest rates [I].')
    o += fig('The money flow through Investec, FY26 (year to 31 March 2026)', fig_moneyflow(), 'Source: Investec Final Results 31/03/2026, RNS 21 May 2026 [S70] (Confirmed; key figures re-checked against the RNS on 5 Oct 2026). Group figures unless marked UK & Other. Wholesale funding size not extracted.', full=True)
    o += table(['Metric (FY26)', 'Group', 'Investec plc (UK & Other)', 'UK & Other Specialist Bank'],
        [['Adjusted operating profit','£951.0m (+3.4%)','£462.7m','£401.6m (−2.1%)'],['ROE / ROTE','13.6% / 15.7%','10.8% / 13.7%','n/a'],
         ['Cost-to-income','52.9%','52.5%','54.0%'],['Credit loss ratio','36bps','n/a','57bps'],['Net core loans','£35.5bn','n/a','£17.8bn'],
         ['Customer deposits','£44.7bn','£22.5bn','£22.5bn'],['CET1 ratio','n/a (each entity reports its own)','13.0% (standardised)','n/a']])
    o += P('<span class="small">Sources: S70, S120 [C]. Southern Africa earned £488.3m and an ROE of 18.2%, far above the UK. The UK earns lower returns than South Africa. That gap is the central tension in the strategy [C] [S70] [I].</span>')
    o += box('term', '<b>Basis point (bp)</b>: one hundredth of one percent. A credit loss ratio of 57bps means the bank set aside 0.57p for bad debts for every £1 of loans in the year.')
    o += box('term', '<b>ROE and ROTE</b>: return on equity is profit divided by shareholders\' money in the business. ROTE strips out goodwill and other intangibles. Investors compare it with the cost of that money, often around 10 to 13% for banks [I].')

    o += h2('p2c', 'C. The "contracts": what each client group gives and gets')
    o += table(['Client group','What Investec gives','What Investec gets','Evidence'],[
      ['Private clients (high-income professionals, entrepreneurs, HNW)','Mortgages and lending tailored to complex incomes, savings, a named relationship manager. From H2 2027: current accounts, a first UK credit card, rewards, advice with Rathbones','Interest margin on mortgages, sticky deposits, and the chance to be the client\'s main bank','S89, S92, S123 [C/R]'],
      ['Mid-market companies','Specialist and structured lending, advisory and ECM, broking, FX and rate hedging, and (from Nov 2025) transactional banking','Lending margin, fees (IBP fee income +28% in H1 FY26), operational deposits','S75, S90, S121 [C/R]'],
      ['PE sponsors and funds','Fund finance (subscription and NAV lines), acquisition finance','Fees and secured lending to institutions','S120, S22 [C/R]'],
      ['Savers (Investec Save)','Above-high-street rates on easy access, notice and fixed-term deposits, sold online and through platforms such as Raisin','Branchless, stable retail funding for niche lending','S88, S133 [R]'],
      ['Shareholders','Dividend (38.5p FY26), buybacks','Capital to lend against','S70 [C]']])
    o += P('Ryan Tholet, head of UK Private Banking: "Our shift from mortgage banker to relationship manager enables a greater offering at the source of any lending, increasing our relevance" [R] [S89]. Andy Hart, head of Corporate Banking: "We see a clear strategic growth opportunity to extend our offering and bring a private client banking experience to UK mid-market corporates" [R] [S90].',
           'The deal with savers is simple [I]. Investec pays above-high-street rates for a stable, branchless deposit base. That funds niche lending without the cost of branches. The price is a higher cost of funds than the clearing banks pay. The UK bank\'s deposits (£22.5bn) exceed its loans (£17.8bn), so it is not stretched for funding [C] [S70].')

    o += h2('p2d', 'D. The risk and control architecture')
    o += P('Investec Bank plc is authorised by the PRA and regulated by the FCA and PRA, firm reference number 172330 [R] [S88]. Its Companies House number is 00489604, incorporated 1950, registered at 30 Gresham Street, London EC2V 7QP [C] [S86].',
           'The group describes a board-approved risk appetite framework, three lines of defence, and a rule to lend to "clients we know and understand". An older annual report gives single-name limits of 7.5% of CET1 for Investec plc and a global credit committee meeting twice a week [R] [S111]. That source dates from about 2017, so treat the exact limits as possibly out of date.',
           'The through-the-cycle credit loss range for the group is 25 to 45bps. The UK runs higher: 57bps in FY26 [C] [S70]. That is the price of lending to niches the big banks avoid. The bank charges more for that risk, and needs good credit judgement to keep losses inside the price [I].')
    o += box('term', '<b>Three lines of defence</b>: the business that takes the risk (first line) owns it; independent risk and compliance teams (second line) set limits and check; internal audit (third line) tests whether the whole system works.')
    o += box('term', '<b>Standardised vs IRB</b>: under the standardised approach the regulator sets how much capital each loan needs. Under internal ratings-based (IRB) models the bank uses its own approved models, often needing less capital for good-quality loans. Investec plc uses standardised; Investec Ltd uses advanced IRB. The UK business says it is "on its journey" to IRB [C] [S174]. This is part of why UK returns trail South Africa [I].')
    o += box('say', '"The UK credit loss ratio of 57 basis points is above the group\'s 25 to 45 range. I read that as the cost of lending into niches. The question I would want to understand is how the bank prices that risk and when it walks away."')

    o += h2('p2e', 'E. The UK business mix, and what has grown')
    o += UL('**Private Banking.** Mortgages and lending to high-income and HNW clients, savings and transactional banking. Residential mortgages were the fastest-growing book in H1 FY26, at 9.6% annualised [C] [S75]. About 8,200 UK private clients [R] [S124].',
            '**Corporate & Investment Banking.** Specialist lending (Fund Solutions, Direct Lending, growth and leveraged finance, real estate, aviation, energy and infrastructure, asset finance), Treasury Risk Solutions, and advisory, ECM and corporate broking. Investec bought Evolution Group in 2011, which built the broking arm [R] [S85]. About 110 listed broking clients [R] [S129]. Ranked first overall in the Extel UK small and mid-cap broker rankings for the fourth year in 2026 [R] [S130].',
            '**Wealth.** Investec Wealth & Investment UK combined with Rathbones on 21 September 2023 in an all-share deal valued at about £839m [C] [S78]. Investec now holds 29.9% of the votes and about 41% of the economics, and books a share of Rathbones\' profit (£76.6m in FY26) [C/R] [S70, S80].',
            '**What grew:** mortgages, fund and direct lending, fees. **What shrank:** net interest income as rates fell, and UK profit (FY26 −2.1%; H1 FY27 guided 2 to 6% lower) because FY27 is the "peak investment year" [C] [S70, S71].')

    o += h2('p2f', 'F. Listed status, and what it means for research')
    o += P('Investec is listed, which is good news for research: almost every number in this pack comes from published results. There are four report sets: the combined group results; Investec plc and Investec Limited (each with its own capital ratio); and Investec Bank plc\'s own annual and half-year reports [C] [S70, S74, S75]. Investec plc trades on the LSE as INVP, Companies House 03633621 [C] [S86]. Its index membership (FTSE 100 or FTSE 250) was disputed between sources on 5 Oct 2026; check the FTSE Russell list before quoting it [R] [S85, S113].')
    o += box('unc', 'Index membership (FTSE 100 or 250) and the JSE listing year (1986 or 1988) were not confirmed from a primary source. Avoid stating them as facts. Confirmed instead: the group says "8,000+ employees" [C] [S282]; Investec Bank plc had 2,425 employees at 31 March 2026 [C] [S278]; Ruth Leas is IBP chief executive per its 2026 annual statements [C] [S278].')

    o += h2('p2g', 'G. Leadership\'s view of the future')
    o += P('Fani Titi has been group chief executive since 2018 [R] [S85]. Henrietta Baldock became group chair on 6 August 2026, and Stephen Koseff retired from the board the same day [C] [S73]. With Koseff gone, no founder-era figure remains on the board [I].',
           'Targets: ROE 13 to 17% and ROTE 14 to 18% over the medium term; about 16% ROE and 18% ROTE by FY2030. FY27 is "the peak investment year", with earnings growth expected to pick up from FY28. UK & Other ROTE is guided at 12.5 to 13.5% for FY27, near the bottom of its range [C] [S70].',
           'Titi in May 2026: "We are hiring within the UK corporate mid-market and looking to launch a fully functional service in the second half of 2027. We will go much harder at the affluent sector" [R] [S89]. On private clients: "We regard private client as a heritage franchise for us. This is where we developed who we are" [R] [S92].')
    o += box('op', 'The author\'s inference from hiring and moves [I]: Investec UK is converting from a specialist lender into a primary bank for two client types, the affluent professional and the mid-market company. A 2027 summer intern arrives exactly as the "fully functional" UK mid-market service and the new private-client current accounts are due. Your view: is the extra cost worth it, and what would prove it by FY28?')

    o += h2('p2h', 'H. Recent moves, October 2024 to October 2026')
    o += table(['Date','Move','Source'],[
      ['5 Aug 2025','After the Supreme Court motor finance ruling, Investec says its £30m provision "remains adequate"','S96 [C]'],
      ['20 Nov 2025','Half-year results plus the corporate mid-market strategy: a unified mid-market division, transactional banking','S72, S90, S121 [C/R]'],
      ['30 Mar 2026','FCA confirms motor finance redress scheme; Investec keeps the £30m provision','S70 [C]'],
      ['21 May 2026','FY26 results: profit £951.0m, dividend 38.5p, about £110m buyback completed; private client strategy; FY2030 targets','S70, S89, S92 [C/R]'],
      ['16 Jun 2026','Rathbones discloses an FCA-prompted review found Consumer Duty and compliance weaknesses; £60m remediation; shares fell 16 to 19%','S81, S82 [R]'],
      ['12 Jul 2026','Terry Koizou hired as head of client relationship management, UK Corporate Banking; team to grow past 40 relationship managers','S226 [R]'],
      ['13 Jul 2026','Rathbones ends its buyback because Investec\'s voting stake reached the 29.9% cap','S80, S227 [R]'],
      ['6 Aug 2026','AGM: Henrietta Baldock becomes chair; Philip Hourquebie and Stephen Koseff retire','S73 [C]'],
      ['18 Sep 2026','Pre-close statement: UK H1 FY27 profit guided 2 to 6% lower; interim results on 19 Nov 2026','S71, S222 [C]']])

    o += h2('p2i', 'I. The skeletons, told straight')
    o += P('Nothing here should surprise you in an interview. Know it, and say it calmly if asked.')
    o += UL('**Kensington (2007 to 2014).** Investec bought UK subprime mortgage lender Kensington on 8 August 2007, just before the crisis. Impairments followed for years. Koseff later said "the timing of the Kensington deal was very unfortunate". It was sold to Blackstone and TPG in September 2014 for £180m [R] [S84, S102].',
            '**2008: no bailout.** Koseff: "seven of the 10 big UK banks had to get a government bailout. We survived that crises without any help from anyone" [R] [S84].',
            '**Investec Australia.** Losses led to a sale to Bank of Queensland for A$440m, completed 31 July 2014. With Kensington, the sales were expected to lift Investec plc\'s CET1 from 8.8% to about 11.3% [R] [S102, S103].',
            '**UK motor finance.** Investec entered in 2015 and had a £555m book (about 1% market share) by 2021. It took a £30m provision in FY24 and has kept it [R/C] [S95, S70]. Close Brothers holds about £320m [C] [S140].',
            '**Cum-ex (Germany).** News24 reported in 2021 that Investec\'s Dublin office allegedly financed cum-ex trades in 2008 to 2012. Investec said no employee or the bank had been charged. It is disclosed as a contingent liability. No outcome after 2021 was found [R] [S98].',
            '**South Africa AML fine.** In August 2016 the SARB fined Investec Bank Limited R20m for weak anti-money-laundering controls. The SARB said the banks had not facilitated money laundering [R] [S99].',
            '**Steinhoff.** Investec first called its exposure negligible and ultimately lost about R220m (reported May 2018) [R] [S100].',
            '**FSA undertaking (2013).** Investec Bank plc agreed to change terms in a structured product after the FSA said some terms might be unfair. It was an undertaking, not a fine [C] [S87].',
            '**Rathbones (2026).** Investec\'s largest associate is under FCA-prompted remediation, a risk to the advice model at the centre of the May 2026 private client plan [R] [S81] [I].')
    o += box('say', '"Kensington is the lesson I took from reading the history. Buying into a market at the top cost years of impairments. Selling Kensington and Australia in 2014, and folding wealth into Rathbones in 2023, show a firm that will simplify when something is not working."')
    o += box('dont', 'Do not raise cum-ex or the SARB fine unprompted, and never describe allegations as findings. If asked, state the facts, the date and the source, and move on.')
    o += END
    return o

def build3():
    o = part('p3', 'Part 3', 'Why Investec is built this way', 'Structure, collaboration, what clients actually buy, and the size and wiring of the centre.')
    o += h2('p3a', '1. Why one specialist bank, not a lender plus a separate private bank?')
    o += P('Most UK competitors do one thing. Close Brothers, Shawbrook and OakNorth lend. Peel Hunt, Panmure Liberum and Deutsche Numis advise and broke. Coutts and C. Hoare run private banks. HSBC, Barclays and Santander offer everything at mass scale [C] [S140-S149, S305-S308].',
           'Investec puts a private bank and a mid-market corporate and investment bank under one roof. Its own description: "the only integrated and diversified mid-market focused specialist bank, providing the capabilities of global investment banks to the corporate mid-market" [C] [S121]. Ruth Leas in 2022: "the only bank providing a combined offering across the personal and business journeys of our target clients" [C] [S125].',
           '**The theory** [I]. The same person is often both clients. A founder needs growth debt for the company, then advice on a sale or listing, then a mortgage, deposits and wealth advice when the money arrives. If one bank serves each stage, it knows the client better, wins referrals at low cost, and holds deposits that stick. The business also balances itself: fees from advice rise in good markets; interest income holds up when deals are scarce.',
           '**What it costs** [I]. Running many small specialist teams is expensive: Investec UK\'s cost-to-income ratio is 54.0%, against about 26% at OakNorth and 36% at Shawbrook [C] [S120, S144, S240]. Specialist teams can depend on a few people. And integration is only worth paying for if clients really cross between businesses, which Investec does not publish for the UK [C] [S120].')
    o += fig('Monoline lender vs integrated specialist bank', fig_models(), 'Sources: Investec HY Sep-2025 and FY26 RNS [S120, S121]; peer results [S140, S142, S144]. Client journey is illustrative [I].')
    o += fig('One client, one bank: the founder lifecycle', fig_lifecycle(), 'Illustrative [I], built from the products Investec lists in its results [S120, S121] and Leas\'s "personal and business journeys" [S125]. Investec does not publish how many UK clients use more than one business.')

    o += h2('p3b', '2. How do the businesses work together, and where does collaboration actually live?')
    o += P('Investec\'s own wording, read precisely:',)
    o += UL('"the power of One Investec" (FY26, describing Private Client) [C] [S120].',
            '"further entrench clients in our ecosystem, grow market share and drive cross-divisional and cross-border collaboration" (HY Sep-2025) [C] [S121].',
            '"we completed an internal restructuring to create a unified Corporate mid-market division that is focused on a single integrated strategy" (HY Sep-2025) [C] [S121].',
            '"we are evolving our strategic partnership [with Rathbones] from a referral-based model to an integrated assets-under-advice model. Investec will now lead the client relationship and advice" (FY26) [C] [S120].')
    o += P('Read the verbs. "Entrench", "drive", "evolving": these describe an aim, not a finished state [I]. The concrete evidence is structural: a single mid-market division, a corporate banking team built to "feel like private banking" (Andy Hart) [R] [S226], and the Rathbones relationship moving from referral to Investec-led advice.',
           'Collaboration lives in three places [I]: (1) the **relationship manager**, who is the client\'s single door into the bank; (2) **credit**, where every lending team draws on the same risk and capital; (3) **referral routes**, between corporate bankers, private bankers and Rathbones.',
           'The honest counter-case: HSBC UK also measures cross-selling. Referrals from its commercial bank to its private bank rose 8% in 2025 [C] [S149]. So the edge is not the idea of collaboration. It is doing it in the mid-market, with lending, advice and broking together, at a size where people know each other [I].')
    o += fig('The hub: why a relationship model needs a centre', fig_hub(), 'Illustrative [I]. Left: without a single door, every client deals with every product team. Right: the relationship manager routes needs to specialist teams and keeps the relationship.')
    o += fig('The scarce-resource collision: how the bank allocates capital and people', fig_collision(), 'Illustrative [I]. Capital figures: Investec plc CET1 13.0% (31 Mar 26) and RWAs £20.5bn (30 Jun 26) [S70, S77]; credit committee and limits [S111, older source]. The same logic applies when two seniors compete for an intern\'s time (Part 11).')
    o += fig('The walls between businesses: what is shared, what is never shared', fig_walls(), 'Information barriers are a standard regulatory requirement for firms that advise listed companies (UK Market Abuse Regulation; FCA rules on conflicts) [I]. Specific Investec procedures were not published in sources read.')
    o += box('term', '<b>Inside information</b>: precise, non-public information that would likely move a listed company\'s share price if it were known, such as an unannounced takeover. Using or passing it on is a crime. A bank that advises listed companies keeps those teams behind an information barrier (a "Chinese wall") on the "private side".')

    o += h2('p3c', '3. What do clients actually buy, and why do they accept the price?')
    o += P('**Private clients.** In 2018 the UK private bank targeted people earning about £300,000 a year or more with net assets above £3m: corporate executives, entrepreneurs, internationals and professionals [C] [S123]. Its head said: "We are not always especially useful to high net worth individuals who are simply looking to preserve their wealth" [C] [S123]. The 2026 strategy adds the affluent segment through an omni-channel model [R] [S124]. The thresholds date from 2018 and may have changed.',
           'What they buy [I]: a lender who can underwrite complex income (bonuses, carried interest, business ownership) that a high-street mortgage algorithm cannot; speed; a named person. Titi\'s standard: "if a client calls in, the phone should not ring for more than three rings" [R] [S225].',
           '**Mid-market companies** buy "the capabilities of global investment banks" at a size bulge-bracket banks under-serve [C] [S121]. Leas: "the midmarket space is particularly underserviced by the bulge bracket banks" [C] [S125].',
           '**Why accept the price?** Specialist credit costs more than a commodity loan. Clients pay because the alternative is no loan, a slower loan, or a loan from a bank that does not understand the asset [I].')
    o += fig('What a client gets elsewhere: returns and efficiency of the alternatives', fig_returns(), 'Sources: S120 (Investec plc FY26), S142 (Shawbrook FY25 underlying RoTE), S144 (OakNorth 2025 adjusted ROE, company-defined), S146 (NatWest PB&WM 2025 ROE), S148 (Barclays PBWM 2025 RoTE), S140 (Close Brothers FY26 RoTE). Measures differ (ROE vs RoTE; adjusted vs statutory). Not like-for-like.')
    o += box('op', 'The counter-case, with numbers from both sides: Coutts and Barclays Private Bank earn returns of 22 to 26% with bigger balance sheets [C] [S146, S148]. OakNorth and Shawbrook lend at far lower cost [C] [S144, S142]. HSBC UK was named Euromoney Best Bank for Corporates in the UK [C] [S149]. Investec\'s case depends on depth of relationship and integration, not on price or scale. Decide where you stand.')

    o += h2('p3d', '4. The non-core side: the centre')
    o += P('The internship requisition sits in Department "People & Organisation", Division "IBP Business Enablement" [C] [S1]. The same division label appears on central-function jobs such as an operations junior analyst [C] [S19]. So the label is an administrative home, not a sign that interns work in HR [I].')

    o += P('**How big is the centre?** Investec Bank plc had 2,425 employees at 31 March 2026 (2,367 permanent), up from 2,374 a year earlier. Staff costs were £411.8m, about £174,000 per average permanent employee fully loaded [C] [S278]. The bank does not disclose a split between front office and support. The only proxy is the mix of open roles: 38 of 52 live vacancies (73%) carry a non-client-facing role category [C] [S261, S277]. That is a flow, not a stock, so do not quote it as the share of staff [I].',
           '**How it is organised.** Postings use two meanings of "Business Enablement". As a role category it means any non-client-facing job. As a division, "IBP Business Enablement" is narrower: it holds People & Organisation (this internship and a Senior Reward Manager), Company Secretarial, Lending Operations, Finance & Tax, marketing operations, and a credit hub in Mumbai. Technology ("IBP Digital and Technology") and second-line risk ("IBP Risk & Compliance") are posted as separate divisions [C] [S277].',
           '**Who sits at the top.** The IBP board as at 12 June 2026: Ruth Leas (CEO), Kevin McKenna (Chief Risk Officer), Marlé van der Walt (Finance Director, also responsible for Operations) and Fani Titi (Group CEO) as executive directors; Vivek Ahuja chairs the bank since 20 March 2026 [C] [S278]. The UK executive committee beyond the board was not published in sources read.',
           '**Hub and spoke.** 15 of 52 live roles (29%) are in Mumbai at Investec Global Services India, including a 25-person "credit centre of excellence" [C] [S268, S277]. London owns and leads; Mumbai delivers at scale [I].')
    o += P('**How the centre is wired to the front line**, in the postings\' own words:')
    o += UL('Deal Manager: "Acting as a key partner to the lending businesses... You will work closely with Relationship Managers and stakeholders across Treasury, Client Services, Legal Risk, Group Risk, Financial Control, Settlements, Credit Services, and Financial Crime and Fraud" [C] [S269].',
            'Head of Transactional Banking Technology: owns features "on the core banking platform only, while relying on specialist enterprise platforms and teams for payments processing, cards, digital channels, onboarding" [C] [S270]. That is embedded technology resting on firm-wide utilities.',
            'First-line operational risk: "Reporting to the Chief Operating Officer, this role will partner closely with business and functional leaders... across our corporate banking activities" [C] [S271]. Risk embedded in the business.',
            'Credit Hub: "providing independent credit support to Private Markets, Private Clients, TRS and Credit across the Group... Investec is also establishing a new Corporate Bank, launching in 2026, which the Hub will support" [C] [S268].',
            'Senior Reward Manager: "partners closely with senior business leaders, People & Organisation colleagues, Finance and governance forums" [C] [S264]. A connective role.',
            'Company Secretarial: "not simply an administrative function" [C] [S265].')
    o += fig('How a front-line team is wired into the centre: embedded, connective, utility', fig_wiring(), 'Classification by the author [I] from posting text [S264, S265, S268, S269, S270, S271, S277].')
    o += box('say', '"I noticed the internship sits in IBP Business Enablement under People & Organisation, and that most of the central hiring right now supports the new Corporate Bank. I would be interested in how a team like Lending Operations scales for a thousand new mid-market clients."')
    o += fig('The centre as the careers site organises it', fig_centre(), 'Source: Investec careers home page category counts, 5 Oct 2026 [S3, Confirmed]. Not an official org chart; categories are the site\'s own labels.')
    o += fig('Anatomy of one front-line team and what it draws from the centre', fig_unit(), 'Illustrative [I], built from standard bank control functions and the roles listed on Investec\'s careers site [S3, S21].')
    o += END
    return o

def fig_models():
    b = rect(5, 5, 345, 300, SOFT, LINE) + rect(370, 5, 345, 300, ACCS, ACC)
    b += text(177, 28, 'Monoline specialist lender', 13, NAVY, 'middle', 'bold') + text(177, 44, 'e.g. Close Brothers, Shawbrook, OakNorth', 9.5, MUT, 'middle')
    b += text(542, 28, 'Integrated specialist bank', 13, NAVY, 'middle', 'bold') + text(542, 44, 'Investec UK', 9.5, MUT, 'middle')
    b += node(100, 60, 155, 40, 'Company (borrower)', fill='#fff', stroke=NAVY2, size=10)
    b += node(100, 150, 155, 40, 'Lending team', fill='#fff', stroke=NAVY2, size=10)
    b += arrow(177, 100, 177, 148) + text(185, 128, 'loan', 9, MUT)
    b += text(20, 225, 'Owner\'s personal banking, the sale of the company and its listing all go to other firms.', 9.5, NAVY, width=58)
    b += text(20, 265, 'Strength: low cost, focus. Weakness: one revenue line, sees one slice of the client.', 9.5, MUT, width=58)
    b += node(380, 60, 120, 40, 'Company', fill='#fff', stroke=NAVY2, size=10) + node(585, 60, 120, 40, 'Founder / owner', fill='#fff', stroke=NAVY2, size=10)
    teams = [('Lending',385),('Advisory / ECM',470),('Hedging',555),('Private Bank',640)]
    for t,x in teams: b += node(x, 160, 75, 40, t, fill='#fff', stroke=ACC, size=9)
    for t,x in teams[:3]: b += arrow(440, 100, x+37, 158)
    b += arrow(645, 100, 677, 158) + arrow(645, 100, 600, 158, dash=True)
    b += path('M500,80 L583,80', ACC, dash=True, accent=True) + text(541, 74, 'referral', 8.5, ACC, 'middle')
    b += text(385, 225, 'Same people on both sides: company and owner are both clients, with Rathbones behind the private bank for investments.', 9.5, NAVY, width=58)
    b += text(385, 265, 'Strength: more revenue per relationship, sticky deposits. Weakness: cost-to-income 54% vs ~26-36% at monolines.', 9.5, MUT, width=58)
    return svg(720, 310, b)

def fig_lifecycle():
    st = [('Start-up / growth','Growth and venture debt; FX for exports','Lending'),('Scale-up','Acquisition finance; hedging; transactional banking','CIB'),
          ('Exit or listing','M&A advice, ECM, corporate broking','Advisory'),('Liquidity event','Deposits, mortgage, lending against assets','Private Bank'),('Long-term wealth','Investment advice via Rathbones','Wealth partner')]
    b = ''
    for i,(t,d,k) in enumerate(st):
        x = 8 + i*142
        b += f'<path d="M{x},40 L{x+128},40 L{x+140},75 L{x+128},110 L{x},110 L{x+12},75 Z" fill="{[TEALS,TEALS,ACCS,GRNS,SIGS][i]}" stroke="{[TEAL,TEAL,ACC,GRN,SIG][i]}"/>'
        b += text(x+70, 70, t, 10.5, NAVY, 'middle', 'bold', width=18)
        b += text(x+70, 132, d, 9, NAVY2, 'middle', width=24, lh=11)
        b += text(x+70, 26, k, 9, MUT, 'middle', 'bold')
    b += text(360, 190, 'Each arrow is a moment the client needs something new. A bank that served the last stage is first in line for the next.', 10, NAVY, 'middle', 'bold', width=110)
    return svg(720, 210, b)

def fig_hub():
    b = rect(5,5,345,270,SOFT,LINE) + rect(370,5,345,270,'#fff',ACC)
    b += text(177, 26, 'Without a hub: the tangle', 12, NAVY, 'middle', 'bold') + text(542, 26, 'With a hub: the wheel', 12, NAVY, 'middle', 'bold')
    import math
    cl = [(60,80),(60,150),(60,220)]; pr = [(290,60),(290,110),(290,160),(290,210),(290,250)]
    for c in cl:
        for p in pr: b += f'<line x1="{c[0]}" y1="{c[1]}" x2="{p[0]}" y2="{p[1]}" stroke="{RED}" stroke-opacity=".35"/>'
    for c in cl: b += f'<circle cx="{c[0]}" cy="{c[1]}" r="14" fill="{TEAL}"/>' + text(c[0], c[1]+4, 'C', 10, '#fff', 'middle', 'bold')
    for p in pr: b += f'<rect x="{p[0]-14}" y="{p[1]-10}" width="40" height="20" rx="4" fill="{ACC}"/>'
    labs = ['Lend','Adv','FX','PB','Ops']
    for p,l in zip(pr,labs): b += text(p[0]+6, p[1]+4, l, 8.5, '#fff', 'middle', 'bold')
    b += text(177, 268, '3 clients x 5 teams = 15 links', 9.5, RED, 'middle')
    cx, cy = 542, 145
    b += f'<circle cx="{cx}" cy="{cy}" r="34" fill="{NAVY}"/>' + text(cx, cy-2, 'Relationship', 9, '#fff', 'middle', 'bold') + text(cx, cy+10, 'manager', 9, '#fff', 'middle', 'bold')
    for i,l in enumerate(['Lending','Advisory','FX / hedging','Private Bank','Operations','Credit risk']):
        a = i/6*2*math.pi - math.pi/2
        x, y = cx + 100*math.cos(a), cy + 95*math.sin(a)
        b += f'<line x1="{cx}" y1="{cy}" x2="{x:.0f}" y2="{y:.0f}" stroke="{ACC}" stroke-width="1.5"/>'
        b += f'<rect x="{x-38:.0f}" y="{y-11:.0f}" width="76" height="22" rx="4" fill="{ACCS}" stroke="{ACC}"/>' + text(x, y+4, l, 8.8, NAVY, 'middle', 'bold')
    b += f'<circle cx="395" cy="250" r="13" fill="{TEAL}"/>' + text(395, 254, 'C', 10, '#fff', 'middle', 'bold') + f'<line x1="406" y1="242" x2="515" y2="165" stroke="{TEAL}" stroke-width="2"/>'
    b += text(560, 268, 'Client has one door; the hub routes and coordinates', 9.5, GRN, 'middle')
    return svg(720, 280, b)

def fig_walls():
    b = ''
    b += rect(10, 30, 210, 230, REDS, RED) + text(115, 52, 'PRIVATE SIDE', 12, RED, 'middle', 'bold')
    b += text(115, 70, 'Advisory, ECM, corporate broking, deal teams with inside information', 9.2, NAVY, 'middle', width=36)
    b += rect(500, 30, 210, 230, TEALS, TEAL) + text(605, 52, 'PUBLIC SIDE', 12, TEAL, 'middle', 'bold')
    b += text(605, 70, 'Research, sales and trading (customer flow), anyone who deals in markets', 9.2, NAVY, 'middle', width=36)
    b += f'<rect x="300" y="20" width="18" height="250" fill="{NAVY}"/>' + text(309, 285, 'Information barrier', 9.5, NAVY, 'middle', 'bold')
    b += rect(235, 110, 50, 70, '#fff', LINE) + text(260, 135, 'Lending,', 8.5, NAVY, 'middle') + text(260, 147, 'Private', 8.5, NAVY, 'middle') + text(260, 159, 'Bank', 8.5, NAVY, 'middle')
    b += rect(335, 110, 150, 70, GRNS, GRN) + text(410, 128, 'SHARED', 9.5, GRN, 'middle', 'bold') + text(410, 143, 'Brand, capital, risk and', 8.8, NAVY, 'middle') + text(410, 155, 'compliance, technology,', 8.8, NAVY, 'middle') + text(410, 167, 'public client information', 8.8, NAVY, 'middle')
    b += text(115, 200, 'Never shared: unannounced deals, client names on live mandates', 9, RED, 'middle', width=36)
    b += text(605, 200, 'Can cross only by "wall crossing": approved by compliance, logged, person becomes an insider', 9, TEAL, 'middle', width=36)
    return svg(720, 295, b)

def fig_returns():
    items = [('Barclays PBWM (RoTE, 2025)',26.3,ACC),('OakNorth (adj. ROE, 2025)',22.0,ACC),('Coutts / NatWest PB&WM (ROE, 2025)',21.7,ACC),
             ('Shawbrook (underlying RoTE, 2025)',17.2,ACC),('Investec plc (RoTE, FY26)',13.7,NAVY),('Investec plc (ROE, FY26)',10.8,NAVY),('Close Brothers (RoTE, FY26)',5.5,MUT)]
    return hbar([(l,v) for l,v,_ in items], label_w=250, unit='%', valfmt='{:.1f}', colors=[c for *_,c in items])

def fig_wiring():
    b = node(260, 8, 200, 54, 'Front-line team', 'e.g. UK Corporate Banking', fill=ACCS, stroke=ACC, size=12)
    cols = [('EMBEDDED (inside the business)', 15, ['Corporate Banking Technology','Private Bank Technology','First-line operational risk (reports to COO)'], TEAL, TEALS, '0'),
            ('CONNECTIVE (bridges)', 255, ['Deal Manager, Lending Operations','People & Organisation Leads','Finance Business Partner'], ACC, ACCS, '6,3'),
            ('UTILITY (serves the whole bank)', 495, ['Shared Platform Tech (payments, cards, onboarding)','Credit Hub, Mumbai','Company Secretarial, Reward'], SIG, SIGS, '2,3')]
    for t,x,items,c,f,dash in cols:
        b += f'<path d="M360,62 L360,80 L{x+105},80 L{x+105},100" fill="none" stroke="{c}" stroke-width="1.6" stroke-dasharray="{dash}"/>'
        b += rect(x, 100, 210, 26, c, c, 5) + text(x+105, 117, t, 9.5, '#fff', 'middle', 'bold')
        for i,it in enumerate(items):
            b += node(x, 134 + i*46, 210, 38, it, fill=f, stroke=c, size=9.4)
    return svg(720, 275, b)

def fig_collision():
    b = node(250, 8, 220, 56, 'Scarce: capital and credit appetite', 'Investec plc RWAs £20.5bn; CET1 must stay above target', fill=NAVY, stroke=NAVY, tc='#fff', size=11)
    asks = [('Private Bank','More mortgages for new clients'),('Corporate Banking','Facilities for the 1,000-client build'),('Fund Solutions','Bigger subscription lines'),('Real Estate','A development loan')]
    for i,(t,d) in enumerate(asks):
        x = 10 + i*178
        b += node(x, 90, 165, 54, t, d, fill=ACCS, stroke=ACC, size=10.5)
        b += arrow(x+82, 90, 360, 66, dash=True)
    steps = [('1 Risk appetite','Board-set limits by sector and single name'),('2 Credit committee','Independent approval, deal by deal'),('3 Pricing','Return on capital must beat its cost'),('4 Decision','Approve, resize or decline; record why')]
    for i,(t,d) in enumerate(steps):
        x = 10 + i*178
        b += node(x, 175, 165, 58, t, d, fill=GRNS, stroke=GRN, size=10.5)
        if i < 3: b += arrow(x+166, 204, x+177, 204)
    b += text(360, 262, 'Same principle for an intern with two urgent tasks: make the clash visible, let the right person set the order, record it.', 9.6, NAVY2, 'middle', 'bold', width=120)
    return svg(720, 285, b)
