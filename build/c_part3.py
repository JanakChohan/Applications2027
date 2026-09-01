# -*- coding: utf-8 -*-
from pdfbuild import *

def build():
    F=[]; A=F.append
    A(PageBreak())
    A(heading('Part 3 — The business model, dissected', 0))
    A(Paragraph('Where every dollar comes from, and which parts of the firm actually carry the profit.', S['h1sub']))

    A(heading('3.1  The reporting structure — and the 2024 reorganisation', 1))
    A(P('JPMorgan reports in four segments. You must know that the structure <b>changed in the second quarter of 2024</b>, because '
        'a great deal of the material you will read while preparing predates the change and uses the old names.'))
    A(make_table(['Before Q2 2024','From Q2 2024','What actually happened'],
        [['Consumer &amp; Community Banking (CCB)','Consumer &amp; Community Banking (CCB)','Broadly unchanged.'],
         ['Corporate &amp; Investment Bank (CIB) <br/>+ Commercial Banking (CB) — two separate segments',
          'Commercial &amp; Investment Bank (CIB) — one segment',
          'The two were <b>merged</b>. Mid-sized corporate lending now sits alongside global markets and M&amp;A. Note that the acronym "CIB" survived the change but now means something different.'],
         ['Asset &amp; Wealth Management (AWM)','Asset &amp; Wealth Management (AWM)','Broadly unchanged.'],
         ['Corporate','Corporate','Treasury, the Chief Investment Office, and central functions.'],
        ], widths=[1.25,1.25,2.4]))
    A(callout('Two naming traps that will catch you out',
        '<b>(1)</b> "CIB" before mid-2024 means <i>Corporate &amp; Investment Bank</i>; after, it means <i>Commercial &amp; Investment '
        'Bank</i>. A 2023 article and a 2026 article using the same three letters are describing different perimeters.<br/>'
        '<b>(2)</b> Within the CIB, the client-coverage segment called <b>"Middle Market Banking" was renamed "Commercial &amp; '
        'Specialized Industries" in Q2 2025</b>. Same business, new label.', 'warn'))
    A(figure('f07_org','Figure 5. The firm on one page, with FY2025 revenue for every material business line. '
        'Source: 4Q25 earnings release financial supplement (managed basis).'))

    A(heading('3.2  The four segments, compared', 1))
    A(make_table(['FY2025, $m unless stated','CCB','CIB','AWM','Corporate','Firm'],
        [['Net revenue (managed)','76,029','78,454','24,073','7,025','185,581'],
         ['Noninterest expense','40,267','38,216','15,332','1,825','95,640'],
         ['Provision for credit losses','11,493','2,615','97','7','14,212'],
         ['<b>Net income</b>','<b>18,245</b>','<b>27,761</b>','<b>6,522</b>','<b>4,520</b>','<b>57,048</b>'],
         ['Return on equity','32%','18%','40%','—','17%'],
         ['Overhead ratio','53%','49%','64%','—','52%'],
         ['Average allocated equity','56,000','149,500','16,000','~111,254','332,754'],
         ['Employees (31 Dec 2025)','144,196','94,563','29,722','50,031','318,512'],
         ['Share of firm revenue','41.0%','42.3%','13.0%','3.8%','100%'],
         ['Share of firm net income','32.0%','48.7%','11.4%','7.9%','100%'],
         ['Revenue per employee','$527k','$830k','$810k','—','$583k'],
         ['Net income per employee','$127k','$294k','$219k','—','$179k'],
        ], widths=[1.6,0.75,0.75,0.75,0.85,0.85], small=True))
    A(Paragraph('Segment figures from the 4Q25 earnings release financial supplement, pages 12, 16, 20 and 23. Corporate allocated '
        'equity is the residual after the three operating segments and is the author\'s calculation. Revenue and net income per '
        'employee are also the author\'s calculations from disclosed figures, not JPMorgan disclosures; they use year-end headcount '
        'against full-year earnings, so treat them as indicative.', S['cap']))
    A(figure('f02_rev_vs_profit','Figure 6. The gap between the two bars is the story. Source: 4Q25 earnings supplement.'))
    A(P('The CIB produces 42% of revenue but <b>49% of profit</b>. CCB produces 41% of revenue but only <b>32% of profit</b>. '
        'The reason is credit and cost: CCB carried <b>$11.5bn</b> of the firm\'s $14.2bn credit provision and runs a 53% overhead '
        'ratio against the CIB\'s 49%. Consumer lending is a business where you book revenue up front and discover the cost later.'))
    A(figure('f06_mix','Figure 7. The same firm contains three completely different economic engines. Source: 4Q25 earnings supplement.'))

    A(heading('3.3  Consumer &amp; Community Banking (CCB)', 1))
    A(P('<b>What it is:</b> the American retail bank. Current accounts, savings, credit cards, car loans, mortgages, small business '
        'banking, and a fast-growing retail investing arm. Roughly 144,000 people — <b>45% of the entire firm\'s headcount</b>.'))
    A(make_table(['Sub-business','What it sells','FY2025 revenue','FY2024'],
        [['Banking &amp; Wealth Management','Current and savings accounts, branches, J.P. Morgan Wealth Management (mass-affluent investing)','$42,862m','$40,943m'],
         ['Card Services &amp; Auto','Credit cards, card partnerships, car loans and leases','$28,201m','$25,467m'],
         ['Home Lending','Mortgages, and servicing mortgages for others','$4,966m','$5,097m'],
        ], widths=[1.1,2.4,0.8,0.7]))
    A(P('<b>How it earns:</b> overwhelmingly spread. Net interest income was <b>$58.2bn of $76.0bn — 77%</b>. The remaining $17.8bn '
        'is card interchange, asset management fees on investment accounts, mortgage fees, and $3.8bn of car-lease income.'))
    A(P('<b>Capital and returns:</b> $56bn of allocated equity generating a <b>32% ROE</b>. Attractive, but the cycle sits inside it. '
        'The Card Services net charge-off rate was <b>3.14%</b> in Q4 2025 and <b>3.34%</b> by Q2 2026 — rising, and worth watching.'))
    A(P('<b>What drives it:</b> interest rates, employment, and consumer credit quality. It is the most rate-sensitive and most '
        'recession-exposed part of the firm. In 2025 it added 1.7 million net new checking accounts and 10.4 million credit card accounts.'))
    A(callout('London relevance: very low — and this is the single most common mistake candidates make',
        'CCB is a <b>United States</b> business. Its branches, cards and mortgages are American. If you are applying in London, CCB is '
        'essentially not available to you.<br/><br/>'
        'The UK equivalent is <b>Chase UK</b>, which sits in J.P. Morgan Europe Limited and is reported inside <b>International Consumer '
        'Banking</b> — not inside CCB\'s London headcount. The London graduate route into consumer banking is the <b>Chase Digital '
        'Development Programme</b>, not a CCB programme. Do not tell a London interviewer you are excited about Chase\'s branch network.', 'warn'))

    A(heading('3.4  Commercial &amp; Investment Bank (CIB) — where most London jobs are', 1))
    A(P('<b>What it is:</b> everything the firm does for companies, governments, financial institutions and investors. It is the '
        'largest profit pool in the firm — <b>$27.8bn of net income, 49% of the total</b> — and it is where the overwhelming majority '
        'of London front-office roles sit.'))
    A(figure('f04_cib','Figure 8. The CIB is not "the investment bank" in the popular sense. Trading is the biggest block, and Payments '
        'alone earns nearly twice what M&amp;A and underwriting earn combined. Source: 4Q25 earnings supplement.'))
    A(make_table(['CIB revenue line','FY2025','FY2024','Change','What it is'],
        [['Investment Banking','$10,198m','$9,636m','+6%','Advisory and underwriting fees ($9,735m of it is fees)'],
         ['Payments','$19,331m','$18,085m','+7%','Moving and holding corporate money'],
         ['Lending','$7,601m','$7,470m','+2%','Corporate loans held on balance sheet'],
         ['<i>Banking &amp; Payments subtotal</i>','<i>$37,136m</i>','<i>$35,267m</i>','<i>+5%</i>',''],
         ['Fixed Income Markets','$22,532m','$20,066m','+12%','Rates, credit, currencies, EM, securitised, commodities'],
         ['Equity Markets','$13,250m','$9,941m','+33%','Cash equities, derivatives, prime brokerage'],
         ['Securities Services','$5,599m','$5,084m','+10%','Custody, fund administration, collateral'],
         ['Credit adjustments &amp; other','($63m)','($244m)','—','Valuation adjustments on derivatives'],
         ['<i>Markets &amp; Securities Services subtotal</i>','<i>$41,318m</i>','<i>$34,847m</i>','<i>+19%</i>',''],
         ['<b>Total CIB</b>','<b>$78,454m</b>','<b>$70,114m</b>','<b>+12%</b>',''],
        ], widths=[1.5,0.8,0.8,0.6,2.0], small=True))

    A(heading('Investment Banking', 2))
    A(P('The advisory and underwriting business: <b>M&amp;A</b>, <b>equity capital markets</b>, <b>debt capital markets</b> and '
        '<b>leveraged finance</b>, organised around industry coverage groups, country coverage, and sponsor coverage. JPMorgan\'s own '
        '2027 London posting names its coverage sectors explicitly — Consumer &amp; Retail, Healthcare, Technology, Financial '
        'Institutions, Real Estate — and its product areas: M&amp;A, Corporate Finance Advisory, Infrastructure, Ratings Advisory, '
        'Sustainable Solutions, ECM and DCM.'))
    A(P('<b>League table position:</b> JPMorgan was <b>#1 globally for investment banking fees in 2025 with 8.4% wallet share</b>, and '
        '9.3% year-to-date at Q2 2026, when quarterly IB fees of $3.3bn were the highest since 2021. By product the picture is more '
        'contested: for 2025 M&amp;A, LSEG data had <b>Goldman Sachs first</b> on both volume ($1.48tn) and fee revenue ($4.6bn), with '
        'JPMorgan second on $3.1bn and Morgan Stanley third on $3.0bn. In debt capital markets JPMorgan led global and Americas volumes, '
        'while BNP Paribas led EMEA and HSBC led Asia-Pacific.'))
    A(callout('The honest reading of the league tables',
        'JPMorgan is <b>#1 by total fee wallet</b> — the broadest measure — because it is strong everywhere and dominant in debt. '
        'Goldman Sachs remains <b>#1 in pure M&amp;A</b>, particularly at the mega-deal end. Both statements are true. A candidate who '
        'knows the distinction, and knows that different data providers (LSEG, Dealogic) produce different tables, will sound '
        'considerably better informed than one who simply says "JPMorgan is number one".', 'key'))

    A(heading('Markets', 2))
    A(P('<b>Fixed Income Markets ($22.5bn)</b> covers <b>rates</b> (government bonds and interest-rate derivatives — the largest and '
        'most liquid market on earth), <b>credit</b> (corporate bonds and credit derivatives), <b>currencies and emerging markets</b>, '
        '<b>securitised products</b> (bonds backed by pools of loans), and <b>commodities</b>. In Q4 2025 the strength came from '
        'Securitised Products, Rates, and Currencies &amp; Emerging Markets, offset by weaker Credit.'))
    A(P('<b>Equity Markets ($13.3bn, up 33%)</b> covers <b>cash equities</b> (buying and selling shares for institutions), '
        '<b>equity derivatives</b>, and <b>prime brokerage</b> — the financing and servicing of hedge funds. JPMorgan attributed the '
        '40% fourth-quarter jump specifically to <b>Prime</b>, and Q2 2026 saw an extraordinary <b>86%</b> year-on-year rise. '
        'Prime brokerage is a financing business: it grows when hedge funds borrow more.'))
    A(P('This growth has a balance-sheet cost that is visible in the accounts. Trading assets rose from $637.8bn to $802.9bn during '
        '2025, CIB allocated equity rose 13% from $132bn to $149.5bn, and total firm assets reached $5.0tn by mid-2026. Markets revenue '
        'is not free — it is bought with balance sheet, which is precisely why the CIB\'s ROE is 18% rather than 40%.'))
    A(heading('Global Research, and why MiFID II matters', 2))
    A(P('Research analysts publish investment views on companies, sectors and economies. Research earns almost no direct revenue; '
        'it exists to win trading commissions and to support the franchise.'))
    A(P('<b>MiFID II</b>, the EU regulation applied from January 2018, forced <b>unbundling</b>: asset managers had to pay for research '
        'separately from trading execution, rather than receiving it "free" in exchange for directing trades. Research budgets fell '
        'sharply and coverage of smaller companies thinned.'))
    A(P('The UK has since reversed course. The FCA\'s <b>PS24/9</b> introduced <b>payment optionality</b>, allowing firms to pay for '
        'research bundled with execution again, subject to guardrails — a written policy, annual assessment of value and use, and '
        'clear separation of research charges. <b>PS25/4</b> extended the same optionality to fund managers. The UK Investment Research '
        'Review had concluded that unbundling damaged research provision in the UK.'))
    A(callout('Why a Research applicant should care',
        'This is the defining commercial question of the job you are applying to. Research spent seven years as a cost centre '
        'justified by regulation, and the regulation has now partially reversed. Whether that restores research budgets, and whether '
        'scale players like JPMorgan gain share as smaller providers exit, is genuinely open. It is the obvious "why now" question '
        'for a Global Research interview.', 'key'))
    A(heading('Payments — the most valuable business nobody has heard of', 2))
    A(P('<b>$19.3bn of revenue in 2025</b>, a record $5.1bn in the fourth quarter alone, and $5.3bn in Q2 2026. Payments is larger than '
        'the entire investment banking fee pool, and most candidates cannot describe it.'))
    A(P('It does three things. <b>Treasury services</b>: running the bank accounts of large corporates worldwide, moving their money '
        'between countries and currencies, managing their liquidity. <b>Merchant acquiring</b>: processing card payments on behalf of '
        'businesses. <b>Cross-border payments</b>: moving money internationally, including the correspondent banking network that '
        'smaller banks rely on.'))
    A(callout('Why this business is so prized',
        'Payments earns in two ways at once. It charges <b>fees</b> per transaction — and it holds the enormous <b>deposit balances</b> '
        'that corporate clients leave sitting in their accounts, which fund the bank cheaply and earn spread. That is why CIB net '
        'interest income grew 13% in 2025 while average client deposits grew 14%.<br/><br/>'
        'And it is extraordinarily <b>sticky</b>. A multinational that has plumbed its payroll, supplier payments and treasury systems '
        'into one bank across forty countries does not switch because a rival shaves a basis point. Payments consumes little capital, '
        'generates recurring revenue, and deepens every other relationship. It is arguably the highest-quality revenue in the firm.', 'key'))
    A(heading('Securities Services', 2))
    A(P('<b>$5.6bn, up 10%.</b> Custody means holding assets safely on behalf of institutional investors and keeping the records. '
        '<b>Fund administration</b> means calculating what a fund is worth and producing its reports. <b>Collateral management</b> means '
        'moving the security that backs derivatives trades.'))
    A(P('The economics: fees charged as a few basis points on assets held, plus interest on the cash balances that sit in custody. '
        'Capital-light, unglamorous, and remarkably durable — switching custodian is a multi-year operational project. Revenue rises '
        'with market levels even without winning a single new client.'))
    A(heading('Commercial Banking, and the Innovation Economy', 2))
    A(P('The former Commercial Bank now sits inside the CIB as client-coverage segments. Within Banking &amp; Payments revenue of '
        '$37.1bn, coverage splits as: <b>Global Corporate Banking &amp; Global Investment Banking $25,285m</b>; <b>Commercial Banking '
        '$11,851m</b>, comprising <b>Commercial &amp; Specialized Industries $8,306m</b> (renamed from Middle Market Banking in Q2 2025) '
        'and <b>Commercial Real Estate Banking $3,545m</b>.'))
    A(P('The <b>Innovation Economy</b> business serves startups, high-growth technology companies and their venture investors — the '
        'space Silicon Valley Bank occupied before its 2023 failure. It is live in London: current vacancies include a "UK Innovation '
        'Economy Payments Sales Manager", and there is a 2027 London <b>Innovation Development Program</b> full-time analyst role.'))
    A(heading('Quantitative Research', 2))
    A(P('Quants build the mathematical models that price derivatives, measure risk, and drive electronic trading. They sit alongside '
        'traders rather than in a back office: a trader quoting an exotic option is using a model a quant built and validated.'))
    A(P('JPMorgan runs several distinct quant populations, and the London 2027 postings make the split explicit — <b>Quantitative '
        'Research Markets</b>, <b>Quantitative Research Risk and Treasury</b>, and <b>Quantitative Research Asset Management</b>. '
        'There is also a separate model-risk function (VCG, Model Risk) that independently validates the models. Note carefully that '
        'in London these are advertised as <b>off-cycle internships</b>, not summer internships — see section 5.1.'))

    A(heading('3.5  Asset &amp; Wealth Management (AWM)', 1))
    A(P('<b>What it is:</b> managing money for institutions, funds and wealthy individuals. Two halves.'))
    A(make_table(['Business','What it does','FY2025 revenue','Pre-tax margin'],
        [['Asset Management','Runs funds and mandates for institutions and retail investors: equities, fixed income, multi-asset, ETFs, alternatives (private equity, real estate, infrastructure, hedge funds) and liquidity / money-market funds','$11,700m','35%'],
         ['Global Private Bank','Serves wealthy individuals and families: investment advice, lending against assets, deposits, estate and tax planning','$12,373m','37%'],
        ], widths=[0.85,3.0,0.75,0.7]))
    A(P('<b>Scale:</b> assets under management of <b>$4.8tn</b> and client assets of <b>$7.1tn</b> at end-2025, rising to <b>$5.1tn</b> '
        'and <b>$7.7tn</b> by 30 June 2026. The Global Private Bank employed <b>4,101 client advisors</b>, up 9% in a year — the firm '
        'is hiring aggressively here.'))
    A(callout('AUM versus client assets — a definition you will be asked about',
        '<b>Assets under management (AUM)</b> is money the firm actively manages and charges a management fee on. '
        '<b>Client assets</b>, sometimes called assets under supervision, is broader: everything the firm holds or oversees for '
        'clients, including assets merely held in custody or in brokerage accounts where the firm earns little or no management fee.'
        '<br/><br/>The gap is large — <b>$7.1tn of client assets versus $4.8tn of AUM</b>. Fee income tracks AUM far more closely. '
        'Quoting the bigger number as though it were fee-earning is a classic error.', 'key'))
    A(P('<b>How it earns:</b> fees. Asset management fees were <b>$15.5bn</b> of the segment\'s $17.2bn of noninterest revenue. '
        'Net interest income of $6.8bn comes almost entirely from the Private Bank lending to clients against their portfolios and '
        'holding their deposits.'))
    A(P('<b>Why it is the jewel:</b> AWM earned <b>$6.5bn of net income on just $16bn of allocated equity — a 40% return</b>, the '
        'highest of any segment, on 5% of the firm\'s capital. Its weakness is the 64% overhead ratio: paying investment professionals '
        'and private bankers is expensive, and the segment is directly exposed to market levels. A 20% equity market fall takes '
        'roughly 20% off the fee base with a largely fixed cost base underneath.'))
    A(figure('f05_capital','Figure 9. Three segments, three completely different capital models. Source: 4Q25 earnings supplement.'))

    A(heading('3.6  Corporate', 1))
    A(P('Not a business but a container. <b>Treasury and the Chief Investment Office (CIO)</b> manage the firm\'s own money: the '
        '$735bn average investment securities portfolio, the funding, and the interest-rate risk of the balance sheet as a whole. '
        '<b>Other Corporate</b> holds central items and one-offs.'))
    A(P('Corporate produced $7.0bn of revenue and $4.5bn of net income in 2025, against $17.4bn and $10.6bn in 2024 — a fall that is '
        'almost entirely the $7.9bn Visa gain in 2024 dropping out, plus $3.7bn less net interest income as rates fell. Corporate also '
        'houses <b>50,031 employees</b>: the centralised technology, operations, finance, risk, audit and HR functions. Several London '
        'graduate programmes — CADP, Global Finance &amp; Business Management, HR — recruit into this population.'))

    A(heading('3.7  The revenue map: three different answers to "what makes the most money"', 1))
    A(figure('f14_revenuemap','Figure 10. Size against capital consumed. Revenue is sourced; the capital-intensity score is the '
        'author\'s inference, since JPMorgan does not publish risk-weighted assets by revenue line.'))
    A(P('The question "which part of JPMorgan makes the most money" has three correct and different answers, and being able to '
        'separate them is a genuine test of whether you understand the firm.'))
    A(make_table(['The question','The answer','The evidence'],
        [['<b>1. Most absolute profit?</b>','The <b>Commercial &amp; Investment Bank</b>','$27.8bn of net income — 49% of the firm. Within it, Markets &amp; Securities Services at $41.3bn is the largest revenue block.'],
         ['<b>2. Most profit per unit of capital?</b>','<b>Asset &amp; Wealth Management</b>, comfortably','40% ROE versus CIB\'s 18%. AWM turns $16bn of equity into $6.5bn of profit — <b>$0.41 per dollar of equity</b>, against $0.33 for CCB and $0.19 for the CIB.'],
         ['<b>3. Most profit per head?</b>','The <b>CIB</b>','$294k of net income per employee, against $219k in AWM and $127k in CCB. CCB employs 45% of the firm to generate 32% of profit — retail banking is people-intensive by nature.'],
        ], widths=[0.95,1.0,3.0]))
    A(callout('And a fourth answer, which is the sophisticated one',
        'By <b>quality</b> of revenue — recurring, capital-light, sticky, not dependent on market direction — the best businesses in '
        'the firm are <b>Payments ($19.3bn)</b>, <b>Securities Services ($5.6bn)</b> and <b>Asset Management ($11.7bn)</b>. None is the '
        'largest. None is the most glamorous. All three would still be earning if markets fell 30% and no company did a deal for a year.'
        '<br/><br/>Say this in an interview and you will be making an argument, not reciting a figure.', 'key'))

    A(heading('3.8  The cost side', 1))
    A(make_table(['FY2025 expense line','$m','% of total','Comment'],
        [['Compensation','54,487','57.0%','The dominant cost. Rose 6% on higher revenue-related pay and front-office hiring.'],
         ['Professional and outside services','12,356','12.9%','Consultants, outsourced services, much of it technology.'],
         ['Technology, communications and equipment','11,029','11.5%','<b>Not</b> the full technology budget — see below.'],
         ['Marketing','5,531','5.8%','Card acquisition is the bulk of this.'],
         ['Occupancy','5,461','5.7%','Offices and branches.'],
         ['Other','6,776','7.1%','Includes firmwide legal expense of just $361m, down from $740m.'],
         ['<b>Total noninterest expense</b>','<b>95,640</b>','<b>100%</b>','Overhead ratio 52%.'],
        ], widths=[1.5,0.6,0.6,2.5]))
    A(callout('The technology number that everyone gets wrong',
        'The income statement shows <b>$11.0bn</b> of "technology, communications and equipment expense". That is not JPMorgan\'s '
        'technology budget. At the February 2026 Company Update the firm guided to <b>approximately $19.8bn of technology spend in '
        '2026, up 10%</b> — a management-defined figure that includes engineers\' compensation and outsourced development, which sit '
        'in other income-statement lines.<br/><br/>'
        'Within that, roughly <b>$1.2bn</b> of additional spend goes to major projects, against about <b>$600m</b> of identified '
        'efficiencies, "some of which are AI-related". Total 2026 adjusted expense is guided to <b>about $105bn</b>, up around $9bn.'
        '<br/><br/>If you cite the $11.0bn as the tech budget you will be wrong by nearly half. If you cite $19.8bn and can say why '
        'it differs from the income statement line, you will be right and will sound like you read the source.', 'warn'))
    A(P('The <b>overhead ratio</b> — expense divided by revenue — was <b>52%</b> in 2025, and management is explicit that it is not '
        'the target. In their words: "we are not managing the Firm for short-term operating leverage... long-term pre-provision net '
        'revenue growth is a much better lens through which to assess our investments." Expense discipline at JPMorgan means spending '
        'more than competitors while growing revenue faster still.'))

    A(heading('3.9  Cross-segment synergy — and how much of it is real', 1))
    A(P('Every universal bank claims its parts reinforce each other. At JPMorgan some of that claim is structural fact and some is '
        'presentation. It is worth separating them.'))
    A(make_table(['The claim','Verdict','Why'],
        [['Deposits fund lending cheaply','<b>Real, and large</b>','$2.56tn of deposits, roughly $604bn of it paying no interest at all. This is a genuine, measurable and enormous funding advantage over non-bank lenders.'],
         ['Corporate clients buy payments and markets services too','<b>Real</b>','Payments revenue of $19.3bn and 14% growth in CIB client deposits are the visible output. The merger of Commercial Banking into the CIB in 2024 was done explicitly to make this easier.'],
         ['Private bank clients buy asset management products','<b>Partly real</b>','Both sit in AWM and share investment platforms — but the Private Bank also sells third-party products, and the revenue is reported separately.'],
         ['One relationship across the whole firm','<b>Overstated</b>','A US credit-card holder and a European hedge fund have nothing in common. CCB and the CIB share technology, brand and funding — not clients.'],
        ], widths=[1.15,0.75,3.1]))
    A(P('The honest summary: synergy is <b>strongly real within the CIB</b>, <b>real within AWM</b>, real at the level of funding and '
        'technology across the whole firm, and largely <b>rhetorical between the consumer bank and the wholesale bank</b>. The 2024 '
        'reorganisation is itself evidence — the firm merged the two wholesale segments precisely because that is where the '
        'cross-selling genuinely exists.'))

    A(heading('3.10  Following the money through one deal', 1))
    A(P('Abstractions become concrete when you trace a single transaction. Suppose a UK-listed industrial company decides to buy a '
        'competitor for £2bn, funded with new debt.'))
    A(figure('f09_deal','Figure 11. One client decision, six teams, five distinct revenue lines — all inside a single reportable segment.'))
    A(P('Each step names a real team you could be interning on. The <b>coverage banker</b> in UK Industrials owns the relationship and '
        'earns no fee directly, which is why coverage bankers are measured on the total wallet their clients generate rather than on '
        'their own P&amp;L. <b>M&amp;A Advisory</b> earns a success fee only on completion. <b>Leveraged Finance or DCM</b> underwrites '
        'the debt and earns a fee for guaranteeing the proceeds. The <b>Rates and FX desks in Markets</b> sell the hedges and earn the '
        'bid-ask spread, not a fee. <b>Payments</b> moves the money and then runs the enlarged group\'s treasury for years afterwards. '
        '<b>Securities Services</b> may end up holding the assets.'))
    A(P('Two lessons. First, the fee revenue is a one-off; the payments and custody relationships are annuities that outlast it — '
        'which is why the unglamorous businesses are so valuable. Second, all of this books inside the <b>CIB</b>. When you read that '
        'the CIB earned $78.5bn, this is the machinery underneath it.'))
    return F
