import sys, importlib.util
sys.path.insert(0, '/home/user/Applications2027/investec/build')
from lib import *
import lib

SRC = {
 1:('Investec case study (search extract)','A £7.65m mortgage in 12 business days','undated','https://www.investec.com/en_gb/focus/intermediary-mortgages/case-study-a-7-65m-mortgage-in-12-business-days.html'),
 2:('Investec case study (search extract)','Tailored mortgage for private equity partner with carried interest bonus income in euros','undated','https://www.investec.com/en_gb/focus/prime-property/case-study-tailored-mortgage-for-private-equity-partner-with-carried-interest-bonus-income-in-euros.html'),
 3:('Investec case study (search extract)','90% LTV with discretionary USD bonus and stock awards','undated','https://www.investec.com/en_gb/focus/intermediary-mortgages/case-study-90-ltv-with-discretionary-usd-bonus-and-stock-awards.html'),
 4:('Investec case study (search extract)','Remortgaging without an income','undated','https://www.investec.com/en_gb/focus/intermediary-mortgages/case-study-remortgaging-without-an-income.html'),
 5:('Investec client stories (search extract)','Client stories','undated','https://www.investec.com/en_gb/individuals/bank-accounts/client-stories.html'),
 6:('Investec case study (search extract)','High-value mortgage for hedge fund owner','undated','https://www.investec.com/en_gb/focus/intermediary-mortgages/case-study-high-value-mortgage-for-hedge-fund-owner.html'),
 7:('Investec case study (search extract)','A £12m remortgage across two homes for a technology entrepreneur','undated','https://www.investec.com/en_gb/focus/intermediary-mortgages/case-study-a-12m-remortgage-across-two-homes-for-a-technology-entrepreneur.html'),
 8:('Rathbones (Investec private banking page)','Private banking with Investec','fetched Oct 2026','https://www.rathbones.com/en-gb/wealth-management/private-banking-with-investec'),
 9:('Money Helpdesk (broker guide)','Investec mortgages','18 Dec 2025','https://www.moneyhelpdesk.com/mortgages/mortgage-lenders/investec/'),
 10:('Finder','Investec current accounts review','25 Jun 2025','https://www.finder.com/uk/current-accounts/investec-current-accounts-review'),
 11:('Investec (search extract)','Voyage Account','undated','https://www.investec.com/en_gb/individuals/bank-accounts/voyage-account.html'),
 12:('Investec (search extract)','Who we work with: private equity professionals','undated','https://www.investec.com/en_gb/individuals/bank-accounts/our-clients/private-equity-professionals.html'),
 13:('Investec (search extract)','Who we work with: business owners','undated','https://www.investec.com/en_gb/individuals/bank-accounts/our-clients/business-owners.html'),
 14:('Investec (search extract)','GP financing','undated','https://www.investec.com/en_gb/private-equity/fund-finance/gp-financing.html'),
 15:('Financial Reporter','Investec provides £14m funding to management of Clyde Blowers Capital','10 Oct 2011','https://2025.financialreporter.co.uk/savings-and-investments/investec-provides-14m-funding-to-management-of-clyde-blowers-capital.html'),
 16:('Mortgage Solutions','Investec launches bespoke BTL deal for expats','7 May 2025','https://www.mortgagesolutions.co.uk/news/2025/05/07/investec-launches-bespoke-btl-deal-for-expats/'),
 17:('FStech','Investec updates private client growth strategy to target UK wealthy','22 May 2026','https://www.fstech.co.uk/fst/Investec_updates_private_client_growth_strategy_to_target_UK_wealthy.php'),
 18:('Victrex plc RNS (via ticker.app)','Appointment of Joint Corporate Broker','18 Jun 2025','https://www.ticker.app/lse/VCT/rns/2025-06-18/Appointment-of-Joint-Corporate-Broker/2681N'),
 19:('Cohort plc RNS via Investegate','Proposed placing to raise £40 million','21 Nov 2024','https://www.investegate.co.uk/announcement/rns/cohort--chrt/proposed-placing-to-raise-40-million/8563368'),
 20:('Investec deal page (search extract) / Morningstar','Takeover offer for N Brown Group plc; N Brown backs £191m buyout','Oct 2024','https://www.investec.com/advisory/deals/takeover-offer-for-n-brown-group-plc/'),
 21:('Morningstar UK','N Brown backs £191 million buyout by founding family member','17 Oct 2024','https://www.morningstar.co.uk/uk/news/AN_1729163541995729800/n-brown-backs-gbp191-million-buyout-by-founding-family-member.aspx'),
 22:('Treatt plc RNS via Investegate (search extract)','Recommended cash acquisition of Treatt plc','29 Apr 2026','https://www.investegate.co.uk/announcement/rns/treatt--tet/recommended-cash-acquisition-of-treatt-plc-/9542891'),
 23:('Miami International Holdings','Offer to acquire The International Stock Exchange','Mar 2025','https://www.miaxglobal.com/news/miami-international-holdings-announces-offer-acquire-international-stock'),
 24:('Walkers','Advising on Investec subscription line facility (Goldenpeak Fund I)','24 Mar 2026','https://www.walkersglobal.com/en/About-us/News/2026/03/Advising-on-Investec-subscription-line-facility'),
 25:('Alternative Credit Investor','Investec Fund Solutions surpasses €10bn fund finance loans in 12 months','11 May 2026','https://alternativecreditinvestor.com/2026/05/11/investec-fund-solutions-surpasses-e10bn-fund-finance-loans-in-12-months/'),
 26:('National Wealth Fund','Fidra Energy reaches financial close on the UK\'s largest battery energy storage project','10 Sep 2025','https://www.nationalwealthfund.org.uk/news-and-publications/news/fidra-energy-reaches-financial-close-on-the-uks-largest-battery-energy-storage-project-backed-by-eig-and-the-national-wealth-fund/'),
 27:('Investec press release (search extract)','Sole MLA and bookrunner on a £360m debt financing for AMP Clean Energy','undated','https://www.investec.com/en_gb/welcome-to-investec/press/investec-acts-as-sole-mandated-lead-arranger-and-bookrunner-on-a-360m-debt-financing-for-amp-clean-energy.html'),
 28:('Mortgage Solutions','Investec completes £922m in real estate lending','28 May 2026','https://www.mortgagesolutions.co.uk/specialist-lending/2026/05/28/investec-completes-922m-in-real-estate-lending/'),
 29:('Investec press release (search extract)','Investec Aviation strengthens global AELF partnership','undated','https://www.investec.com/en_us/welcome-to-investec/press/investec-aviation-strengthens-global-aelf-partnership.html'),
 30:('Treasury Today','Investec expands Treasury Risk Solutions business into Europe','Aug 2024','https://treasurytoday.com/insight-and-analysis/press-release-investec-expands-successful-treasury-risk-solutions-business-into-europe'),
 31:('BusinessDay','Investec declares war in corporate mid-market','20 Nov 2025','https://www.businessday.co.za/companies/company-strategy/2025-11-20-investec-declares-war-in-corporate-midmarket'),
 32:('Investec careers','Corporate Banking Relationship Director (13005)','2026','https://careers.investec.co.uk/jobs/vacancy/corporate-banking-relationship-director-13005/13023/description/'),
 33:('Investec careers','Private Client Relationship Manager (13796)','2026','https://careers.investec.co.uk/jobs/vacancy/private-client-relationship-manager-13796/13814/description/'),
 34:('Investec plc RNS via Investegate','Final Results 31/03/2026','21 May 2026','https://www.investegate.co.uk/announcement/rns/investec--invp/final-results-31-03-2026/9578809'),
 35:('Investec','Pillar 3 disclosure report, March 2024','2024','https://www.investec.com/content/dam/investor-relations/financial-information/group-financial-results/2024/Investec-plc-group-and-Investec-Bank-plc-Pillar-3-disclosure-report-March-2024.pdf'),
 36:('WealthBriefing','Targeting Restless Entrepreneurs: Investec\'s UK Private Bank','16 Oct 2018','https://www.wealthbriefing.com/html/article.php/Targeting-Restless-Entrepreneurs:-Investec\'s-UK-Private-Bank'),
 37:('City AM','Investec eyes City hiring spree in major move into UK private banking','21 May 2026','https://www.cityam.com/investec-eyes-city-hiring-spree-in-major-move-into-uk-private-banking/'),
 38:('Extel','Investec retains the UK SMID crown','Jun 2026','https://www.extelinsights.com/results/uk-small-mid-cap-brokers/uk-small-mid-cap/2026/investec-retains-the-uk-smid-crown'),
 39:('Investec (search extract)','What private banking support can Investec provide fund managers?','undated','https://www.investec.com/en_gb/focus/my-money/what-private-banking-support-can-investec-provide-fund-managers.html'),
}
def S(*n): return '[' + ', '.join(f'S{i}' for i in n) + ']'

# ---------------- figures ----------------
def fig_shop():
    b = ''
    # supermarket
    b += rect(8, 8, 300, 360, SOFT, MUT, 8, 1.6)
    b += rect(8, 8, 300, 40, MUT, MUT, 8) + text(158, 33, 'THE SUPERMARKET (high-street bank)', 11.5, '#fff', 'middle', 'bold')
    for i,(t) in enumerate(['Shelf: standard mortgage','Shelf: standard savings','Shelf: standard business loan']):
        b += rect(24, 62+i*44, 268, 34, '#fff', LINE, 4) + text(158, 84+i*44, t, 10, NAVY, 'middle')
    b += rect(24, 200, 268, 56, REDS, RED, 4) + text(158, 222, 'Self-checkout scanner = credit scorecard', 10, RED, 'middle', 'bold') + text(158, 240, '"Unexpected item": bonus, carry, shares, dollars', 9.2, RED, 'middle')
    b += text(158, 284, 'Serves millions cheaply.', 10, NAVY, 'middle', 'bold')
    b += text(158, 302, 'If your shape doesn\'t fit the', 9.5, MUT, 'middle') + text(158, 316, 'standard sizes, you leave', 9.5, MUT, 'middle') + text(158, 330, 'with nothing, or too little.', 9.5, MUT, 'middle')
    # tailor
    b += rect(330, 8, 382, 360, ACCS, ACC, 8, 1.6)
    b += rect(330, 8, 382, 40, ACC, ACC, 8) + text(521, 33, 'INVESTEC: the bespoke tailor', 12, '#fff', 'middle', 'bold')
    b += rect(346, 60, 350, 118, '#fff', TEAL, 6, 1.4) + text(521, 80, 'GROUND FLOOR: for the person (Private Bank)', 10.5, TEAL, 'middle', 'bold')
    for i,t in enumerate(['Made-to-measure suit = a mortgage sized on your real income','Accessories = accounts, savings, currency, travel perks','Partner next door (Rathbones) = looks after your investments']):
        b += text(358, 102+i*24, '• ' + t, 9.4, NAVY)
    b += rect(346, 188, 350, 118, '#fff', SIG, 6, 1.4) + text(521, 208, 'UPSTAIRS: for the person\'s business (CIB)', 10.5, SIG, 'middle', 'bold')
    for i,t in enumerate(['Workshop = loans for growth, buyouts, property, planes, batteries','Currency and rate insurance = hedging','Selling or listing the business = M&A, broking, share sales']):
        b += text(358, 230+i*24, '• ' + t, 9.4, NAVY)
    b += rect(346, 316, 350, 42, NAVY, NAVY, 6) + text(521, 334, 'THE TAILOR = your relationship manager', 10.5, '#fff', 'middle', 'bold') + text(521, 350, 'Takes your measurements once, then serves both floors', 9.2, ACC, 'middle')
    return svg(720, 376, b)

def fig_fit():
    b = text(360, 20, 'Same person, two banks', 13, NAVY, 'middle', 'bold')
    b += node(270, 36, 180, 80, 'A PE partner\'s pay', 'Salary €  ·  bonus €  ·  carried interest (lumpy, years later)', fill=SOFT, stroke=NAVY2, size=11)
    b += arrow(270, 90, 150, 140) + arrow(450, 90, 570, 140)
    b += node(30, 140, 240, 110, 'Scorecard bank', 'Counts the salary only. Bonus and carry "too volatile". Foreign currency marked down. Result: small loan or a "no".', fill=REDS, stroke=RED, size=11)
    b += node(450, 140, 240, 110, 'Investec banker', 'Reads career history, the fund, how carry pays out. Counts it all. Result: 75% LTV, 2-year fix on a 4-bed London home [S2].', fill=GRNS, stroke=GRN, size=11)
    b += text(360, 280, 'Investec makes money where the scanner says "unexpected item".', 11, NAVY, 'middle', 'bold')
    return svg(720, 292, b)

def fig_door():
    b = node(270, 120, 180, 70, 'THE MORTGAGE', 'the front door: biggest, most urgent need', fill=ACCS, stroke=ACC, size=12)
    rooms = [(20,10,'Current account','£10/month; Voyage £500/yr with lounges, travel cover, free international payments [S10, S11]'),
             (500,10,'Savings','Instant access and notice accounts, in 15 currencies [S8]'),
             (20,230,'Foreign exchange','Spot, forward (lock today\'s rate), orders at a target rate [S8]'),
             (500,230,'Investments and advice','Run by Rathbones; Investec now leads the advice [S34]'),
             (260,250,'From 2026/27','Credit card and rewards: become the main bank [S17]')]
    for x,y,t,d in rooms:
        b += f'<line x1="360" y1="155" x2="{x+100}" y2="{y+35}" stroke="{TEAL}" stroke-width="1.6" stroke-dasharray="5,3"/>'
        b += node(x, y, 200, 70, t, d, fill=TEALS, stroke=TEAL, size=10.5, subsize=8.6)
    b = b.replace(node(270, 120, 180, 70, 'THE MORTGAGE', 'the front door: biggest, most urgent need', fill=ACCS, stroke=ACC, size=12), '', 1)
    b += node(270, 120, 180, 70, 'THE MORTGAGE', 'the front door: biggest, most urgent need', fill=ACCS, stroke=ACC, size=12)
    return svg(720, 330, b)

def fig_pe():
    b = node(250, 8, 220, 56, 'A private equity firm', 'e.g. a new fund like Goldenpeak Fund I [S24]', fill=NAVY, stroke=NAVY, tc='#fff', size=11)
    b += node(20, 100, 210, 78, 'The fund', 'Fund Solutions: subscription line so it can buy companies before investors pay in [S24, S25]', fill=SIGS, stroke=SIG, size=10.5)
    b += node(255, 100, 210, 78, 'The partners personally', 'GP financing for their own stake in the fund [S14, S15]; mortgages counting carry [S2, S12]', fill=TEALS, stroke=TEAL, size=10.5)
    b += node(490, 100, 210, 78, 'The companies the fund buys', 'Acquisition loans, hedging, later an exit via M&A or a share sale', fill=ACCS, stroke=ACC, size=10.5)
    for x in (125, 360, 595): b += arrow(360, 64, x, 98)
    b += node(140, 210, 440, 60, 'One relationship, three wallets', 'Investec lends to the fund, the people who run it and the businesses it owns. Each feeds the others.', fill=GRNS, stroke=GRN, size=11)
    for x in (125, 360, 595): b += arrow(x, 180, 360 if x==360 else (240 if x<360 else 480), 208, accent=True)
    return svg(720, 280, b)

def fig_lifecycle():
    st = [('Years 0-5','Growing','Growth or acquisition loan; currency hedging; later transactional banking','Upstairs',SIG,SIGS),
          ('Years 5-10','Scaling','Bigger loans; broker and research if listed; share sales to fund deals','Upstairs',SIG,SIGS),
          ('Exit day','Selling','M&A advice on the sale, or take-private financing (e.g. N Brown [S20])','Upstairs',ACC,ACCS),
          ('Years 10+','Wealthy founder','Mortgage, deposits of sale proceeds, FX, advice via Rathbones','Ground floor',TEAL,TEALS),
          ('Next venture','Investor again','Private Capital; loans to back new start-ups; the cycle restarts','Both floors',GRN,GRNS)]
    b = ''
    for i,(t,h,d,f,c,fl) in enumerate(st):
        x = 6 + i*143
        b += f'<path d="M{x},34 L{x+128},34 L{x+140},84 L{x+128},134 L{x},134 L{x+12},84 Z" fill="{fl}" stroke="{c}" stroke-width="1.5"/>'
        b += text(x+70, 62, t, 10.5, c, 'middle', 'bold') + text(x+70, 80, h, 11, NAVY, 'middle', 'bold') + text(x+70, 104, f, 9, MUT, 'middle', italic=True)
        b += text(x+70, 158, d, 8.8, NAVY, 'middle', width=25, lh=10.5)
    b += text(360, 18, 'One founder, ten to twenty years, both floors of the shop', 12, NAVY, 'middle', 'bold')
    b += text(360, 230, 'Timings are illustrative [I]. The N Brown deal is the best published case of one client using advice, financing, FX and private banking together [S20].', 9, MUT, 'middle', width=120)
    return svg(720, 248, b)

def fig_thread():
    b = ''
    items = [('Know the client deeply','A human reads complex income, assets and plans'),('Say yes where others say no','Less competition, so better pricing'),
             ('Hold the loan','Investec keeps loans to maturity [S35]'),('Grow the wallet','Add accounts, FX, advice, business banking [S33]'),('Follow the life','Company, exit, wealth, next venture')]
    for i,(t,d) in enumerate(items):
        x = 6 + i*143
        b += node(x, 30, 132, 100, t, d, fill=[TEALS,ACCS,SOFT,GRNS,SIGS][i], stroke=[TEAL,ACC,NAVY2,GRN,SIG][i], size=10.5, subsize=8.8)
        if i < 4: b += arrow(x+133, 80, x+142, 80)
    b += rect(6, 150, 708, 40, NAVY, NAVY, 6) + text(360, 175, 'The thread through everything: one banker who understands the client better than a computer can', 11, '#fff', 'middle', 'bold')
    return svg(720, 198, b)

# ---------------- content ----------------
def case(title, who, problem, did, why, src):
    return (f'<div class="card med"><h4>{md(title)}</h4><dl><dt>Who</dt><dd>{md(who)}</dd><dt>Problem</dt><dd>{md(problem)}</dd>'
            f'<dt>Investec did</dt><dd>{md(did)}</dd><dt>Why it fits</dt><dd>{md(why)}</dd><dt>Source</dt><dd>{md(src)}</dd></dl></div>')

def build():
    lib.FIGS.clear()
    o = part('p0', 'Start here', 'The shop analogy', 'One picture that explains who Investec serves and what it sells.')
    o += P('Think of the big high-street banks as **supermarkets**. They sell standard products off the shelf, very cheaply, to millions of people. At the checkout a scanner, the **credit scorecard**, decides in seconds whether you get a loan. It works well for people with a normal salary.',
           'Investec is a **bespoke tailor** in the same street. It serves people whose financial "body shape" does not fit standard sizes: pay that arrives as big bonuses, shares, a cut of a fund\'s profits, dividends from their own company, or dollars and euros. The scanner flags these as "unexpected items". The tailor measures them properly and makes something that fits.',
           'The tailor\'s shop has **two floors**. On the ground floor it dresses the person (the **Private Bank**). Upstairs it equips the person\'s business (**Corporate and Investment Banking**, or CIB). The same tailor, the client\'s **relationship manager**, knows both, so a customer who comes in for one thing tends to stay for years and use both floors.')
    o += fig('Investec as a bespoke tailor on a high street of supermarkets', fig_shop(), 'Analogy by the author [I]. Products and roles are from the sources cited in the following pages.', full=False)
    o += box('say', '"High-street banks are supermarkets with a scanner at the checkout. Investec is a tailor for people whose income doesn\'t fit standard sizes, and it has a second floor for their businesses. The same banker serves both, so one mortgage can become a lifetime relationship."', 'The analogy in one breath')
    o += END

    o += part('p1', 'Part 1', 'Who the target clients are', 'Not just "rich people". A very specific kind of rich person.')
    o += P('Investec\'s published entry bar for the UK Private Bank is roughly **£300,000 a year of income** and **over £3m of net worth**, for UK residents [C] ' + S(8) + '. Mortgages usually start at **£1m** [R] ' + S(9) + '. But the real filter is not size of wealth. It is **shape of income**. Investec\'s own client pages group them like this [R, search extracts] ' + S(12, 13, 39) + ':')
    o += table(['Client type','Why their money is "awkward"','What they typically need first'],[
      ['Private equity partners and fund managers','Salary plus bonus plus **carried interest**: a share of the fund\'s profits, paid years later and unpredictably. In Investec\'s survey, 43.5% said lenders struggle to understand their income [R] ' + S(12),'A large mortgage that counts the carry'],
      ['Hedge fund partners and owners','Partnership profit shares and bonuses that swing year to year [R] ' + S(6),'A mortgage or a loan against property to fund their firm'],
      ['Investment bankers, lawyers at US firms','Big bonuses, deferred shares (RSUs), pay in dollars [R] ' + S(3, 5),'A high loan-to-value mortgage; currency planning'],
      ['Founders and business owners','Wealth locked in their company; pay taken as dividends [R] ' + S(1, 13),'Speed and a lender that values the business'],
      ['Tech executives','Shares that vest over time; lump sums on leaving [R] ' + S(5),'Currency hedging and investment advice'],
      ['International families moving to the UK','Assets in foreign trusts and companies [R] ' + S(9),'A UK mortgage that recognises overseas wealth'],
      ['UK expats in Dubai or Switzerland','Live abroad, own UK property [R] ' + S(16),'Buy-to-let mortgages from £1m']])
    o += box('term', '<b>Loan-to-value (LTV)</b>: the loan as a share of the property\'s value. A £3m home with a £2.7m loan is 90% LTV. Most lenders cap large loans well below that.')
    o += box('note', 'In 2018 the head of the UK Private Bank said: "We are not always especially useful to high net worth individuals who are simply looking to preserve their wealth" [R] ' + S(36) + '. Investec wants people who are **making** money and will keep needing things, not people who just want to sit on it.', 'The key filter')
    o += END

    o += part('p2', 'Part 2', 'What private banking actually means', 'Ground floor of the shop: the products, and what problem each one solves.')
    o += P('Private banking is not a mysterious service. At Investec it is mainly **lending**, with everyday banking and investment advice built around it. The single most important product is the **mortgage**: a loan secured on a home [R] ' + S(9) + '. Everything else hangs off it.')
    o += fig('Why the scanner says no and the tailor says yes', fig_fit(), 'Example: Investec case study [S2] (search extract). Scorecard behaviour is a general description [I], supported by the broker statement that Investec does "not use standard credit scorecards" [S9].')
    o += h2('p2a', 'The products, in plain English')
    o += table(['Product','What it is','What it solves for the client'],[
      ['Large or complex mortgage','A home loan, usually from £1m, sometimes up to 90-95% LTV, counting bonuses, carry, shares, profit shares and foreign pay [R] ' + S(9),'Buy the home they want now, not when the bonus lands'],
      ['Interest-only with "capital reductions"','Pay only interest monthly; repay chunks of the loan when bonuses arrive [R] ' + S(1, 3),'Matches lumpy income instead of fighting it'],
      ['Revolving facility','A big overdraft secured on the home: draw, repay, redraw [R] ' + S(9),'Cash on tap for opportunities or a business'],
      ['Remortgage to release cash','A new loan on a home they own [R] ' + S(6, 7),'Raise money for their business without selling shares'],
      ['Bridging loan','Short-term loan to buy before selling the old home [R] ' + S(9),'No missed house because of timing'],
      ['Buy-to-let, including for expats','Loans on homes to rent out; expat version from £1m (May 2025) [R] ' + S(16),'Grow a property portfolio'],
      ['Portfolio loan','Borrow against investments managed by Rathbones, in £, $ or € [R] ' + S(8),'Cash without selling investments'],
      ['Current accounts','Private Bank Account £10/month; Voyage £500/year with airport lounges, travel insurance, free international payments [R] ' + S(10, 11),'Everyday banking that fits a global life'],
      ['Savings','Instant access and 1- or 3-month notice, in 15 currencies [C] ' + S(8),'Somewhere to park big bonuses and sale proceeds'],
      ['Foreign exchange','Spot, forward contracts to lock a rate, and orders that trigger at a target rate [C] ' + S(8),'Protect dollar or euro pay from currency swings'],
      ['Advice and investments','Run by Rathbones; Investec now leads the advice relationship [C] ' + S(34),'Long-term wealth planning'],
      ['Credit card and rewards (new)','Announced in the May 2026 plan [R] ' + S(17),'Makes Investec the client\'s main bank']])
    o += fig('The mortgage is the front door; the other products are the rooms behind it', fig_door(), 'Products: S8, S10, S11, S17, S34. Layout is the author\'s analogy [I].')
    o += h2('p2b', 'Five real (anonymised) Investec clients')
    o += P('<span class="small">All from Investec\'s own published case studies. investec.com blocks automated reading, so these were seen as search extracts [R]; check the wording in a browser before quoting it word for word.</span>')
    o += case('The shipping founder in a hurry','Co-founder, CEO and majority owner of a UK shipping company; wealth tied up in the company and an offshore trust.','Another lender could not complete in 3 weeks at the loan size he needed; his pay had just switched to dividends.','**£7.65m** at 75% LTV, 10-year interest-only, with a planned paydown to 65% after 2 years. Money drawn **12 working days** after first contact.','Speed plus understanding of a founder\'s company income.', S(1))
    o += case('The PE partner paid in euros','Private equity partner who had just joined a new firm; salary, discretionary bonus and carried interest, all in euros.','Variable, foreign-currency income; buying a 4-bed London family home.','75% LTV, 2-year fixed, based on his career history and Investec\'s understanding of PE pay.','Carry is exactly the income scanners reject.', S(2))
    o += case('The couple paid partly in shares','Married couple; bonus split into US dollar cash and RSUs (shares that vest over 2 years).','Irregular income.','**90% LTV from day one**, 25-year interest-only, with paydowns when they choose.','Investec counts shares that have not yet vested.', S(3))
    o += case('The banker with no salary','Ex-investment banker now investing in start-ups; net assets over £10m; no salary.','Wanted to fund 5 years of living costs until his investments pay out.','5-year fixed, interest-only remortgage on a prime central London home.','Lends on wealth and future earnings, not on a payslip.', S(4))
    o += case('The tech executive with a dollar lump sum','C-suite executive at a tech platform; Voyage and deposit client for years.','About to step away and receive a large US dollar payout.','Banker set up **currency hedging** with Investec\'s dealers and brought in the wealth team to invest the money.','Best published example of one client moving from accounts to FX to investments.', S(5))
    o += END

    o += part('p3', 'Part 3', 'Why Investec chooses these clients', 'The business logic. Investec does not spell all of this out, so most of it is reasoning from the evidence.')
    o += table(['Reason','How it makes money','Evidence'],[
      ['1. Less competition','The scanner banks say no or lend too little, so Investec competes with a handful of private banks, not the whole market. That supports better pricing [I]','Investec does "not use standard credit scorecards" [R] ' + S(9)],
      ['2. Good credit risk despite the "awkward" income','Clients are wealthy, loans are paid down from bonuses, and LTVs fall over time [I]','Case studies with planned paydowns, e.g. 90% to 65% [R] ' + S(6, 1)],
      ['3. One sale leads to many','A mortgage leads to deposits, FX on foreign pay, accounts and advice [I]','RM adverts target "wallet share across lending, FX, investments, wealth management" [C] ' + S(33)],
      ['4. Hard to leave','A banker who understands your carried interest is hard to replace [I]','Long-standing client in the tech-executive story [R] ' + S(5)],
      ['5. Cheap, stable funding','Wealthy clients leave large deposits, which fund Investec\'s lending [I]','Strategy to become the "primary bank" [R] ' + S(17, 37)],
      ['6. Tomorrow\'s business clients','Today\'s founder or PE partner brings their company or fund upstairs [I]','Corporate RMs must partner "with Private Client teams when personal and business needs intersect" [C] ' + S(32)]])
    o += box('op', 'The trade-off: tailoring is expensive. Investec\'s UK cost-to-income ratio is 54% [C] ' + S(34) + ', far above lean, computer-led lenders. The bet is that deeper, longer relationships pay for the extra people.', 'The catch')
    o += END

    o += part('p4', 'Part 4', 'Upstairs: what the investment bank side sells', 'Corporate and Investment Banking for mid-sized companies, funds and projects, with real named deals.')
    o += P('Upstairs the customer is a **business**, not a person. Investec focuses on the **mid-market**: established companies too big for small-business banking and too small for the global investment banks. It now aims to bank 1,000 of them by 2030, out of 60,000+ UK mid-sized firms [R] ' + S(31) + '.')
    o += table(['Product','Plain English','Named example'],[
      ['Corporate broking and research','An ongoing retainer: the listed company\'s link to investors, advice on its share price, research, and running any share sale','**Victrex plc** appointed Investec joint corporate broker with J.P. Morgan, 18 Jun 2025 [C] ' + S(18) + '. Investec was #1 UK small and mid-cap broker in Extel 2026 [C] ' + S(38)],
      ['Equity capital markets (ECM)','Helping a company sell new shares to investors','**Cohort plc** (defence tech): £40m placing to buy EM Solutions, Investec sole bookrunner, 21 Nov 2024 [C] ' + S(19)],
      ['M&A advice','Advising a buyer or seller on price, negotiation and takeover rules','**N Brown** (JD Williams, Simply Be): £191m take-private by founding-family member Joshua Alliance; Investec sole adviser to the bidder, agreed Oct 2024 [R] ' + S(20, 21) + '. **Treatt plc**: Investec co-advised the board through rival bids to a 305p offer, Apr 2026 [R] ' + S(22) + '. **TISE**: sold to Miami International for £70.4m, 2025 [R] ' + S(23)],
      ['Fund finance (Fund Solutions)','Short-term loans to private equity funds, secured on investors\' promises to pay in','**Goldenpeak Fund I**: subscription line, Mar 2026 [C] ' + S(24) + '. Over €10bn of fund finance in 12 months to May 2026 [R] ' + S(25)],
      ['Energy and infrastructure','Long loans repaid from a project\'s own income','**Fidra Energy, Thorpe Marsh**: one of 13 lenders on £594m for the UK\'s largest battery project, Sep 2025 [C] ' + S(26) + '. **AMP Clean Energy**: £360m, Investec sole lead arranger [R] ' + S(27)],
      ['Real estate lending','Loans to property developers and investors','£922m lent in FY25/26, including **£26m to Moorfield** for 204-bed student housing in Bristol [R] ' + S(28)],
      ['Aviation finance','Loans secured on aircraft, mostly to leasing companies','**AELF**: loan for an Airbus A330 leased to Hawaiian Airlines, its second deal with Investec [R] ' + S(29)],
      ['Hedging (Treasury Risk Solutions)','Contracts that fix an exchange or interest rate in advance','Clients not named publicly; team expanded into Europe Aug 2024 [R] ' + S(30)],
      ['Transactional banking (new)','Payments, cash management, day-to-day business accounts','Launched Nov 2025 for the mid-market build; no named clients yet [R] ' + S(31)]])
    o += box('note', 'Why these products? Each one lets Investec sit close to an **owner or decision-maker** rather than a procurement department: the founder selling a company, the family taking a business private, the partners running a fund. Those are the same people the ground floor wants as private clients [I].', 'The common thread')
    o += END

    o += part('p5', 'Part 5', 'How the two floors connect', 'The investment bank and the private bank serve the same people at different moments.')
    o += h2('p5a', 'Connection 1: the private equity ecosystem')
    o += P('Investec lends to private equity **funds** (Fund Solutions), to the **partners personally** for their own stake in the fund (GP financing) and with mortgages that count their carried interest, and to the **companies** those funds buy [R] ' + S(12, 14, 24) + '. A dated but clear example: in 2011 Investec lent £14m to the managers of Clyde Blowers Capital so they could invest more of their own money in their £350m fund [R] ' + S(15) + '.')
    o += fig('One private equity relationship, three wallets', fig_pe(), 'Sources as marked. Arrow logic is the author\'s [I].')
    o += h2('p5b', 'Connection 2: the founder\'s life story')
    o += P('The best published example is **N Brown**. Investec says its M&A team worked "extensively with other teams from the bank, including Investec Private Capital, FX & Treasury solutions, and Private Banking" on Joshua Alliance\'s £191m take-private [R] ' + S(20) + '. One family client got advice, financing, currency services and private banking from one bank.',
           'Investec\'s job adverts make the link official: corporate relationship directors partner "with Private Client teams when personal and business needs intersect" [C] ' + S(32) + '. Investec has published **no figures** on how many clients cross between the floors, so the scale of this is not proven [I].')
    o += fig('A founder\'s journey through both floors', fig_lifecycle(), 'Illustrative timeline [I].')
    o += h2('p5c', 'How long does a relationship last?')
    o += UL('**Corporate broking has no end date.** It is a retainer that runs for years and produces extra fees on each share sale or bid. Cohort shows one broking relationship producing a share sale and a takeover mandate in a single deal [C] ' + S(19) + '.',
            '**Lending repeats.** AELF came back for a second aircraft deal [R] ' + S(29) + '. Fund managers return for each new fund (Inferred).',
            '**Mortgages run 5 to 25 years**, and many are interest-only with planned paydowns, so the banker stays in touch through each bonus round [R] ' + S(1, 3, 4) + '.',
            '**Investec holds most loans to maturity** rather than selling them on, "thereby developing a \'hands-on\' and long-standing relationship" [C] ' + S(35) + '.',
            'No published figure for average client tenure exists.')
    o += END

    o += part('p6', 'Part 6', 'What links the client to the product, and why', 'The single idea that ties the whole model together.')
    o += P('Across every product, the link is the same: **a person at Investec understands the client\'s situation better than a computer or a generalist would**, and that understanding is what lets Investec say yes, price the risk, and then offer the next thing.')
    o += fig('The thread through the whole model', fig_thread(), 'Synthesis [I] of S9, S33, S35 and the examples above.')
    o += h2('p6a', 'Why they do it this way')
    o += UL('**It is where the margin is.** Standard products are a price war. Complex clients pay for fit [I].',
            '**Their pay system rewards it.** Bonus pools come from profit after a charge for the capital used, not from sales volume, and loans are approved by committees needing unanimous consent [C] ' + S(35) + '. That favours careful, repeat business with known clients.',
            '**It is a strategy, not an accident.** Investec says "We do not seek to be all things to all people" and focuses on "select market niches". Its 2026 plan pushes both floors further: a full private bank and a corporate bank that feels like private banking [C/R] ' + S(34, 37) + '.')
    o += box('say', '"Investec targets people whose wealth is real but awkward, like PE partners paid in carry or founders paid in dividends. It wins them with a mortgage a scoring machine would refuse, then adds accounts, currency and advice. Upstairs it lends to and advises their funds and companies, from fund finance to M&A. One banker knows both sides, so a single loan can turn into a relationship that lasts the client\'s whole career."', 'Say this in an interview')
    o += h2('p6b', 'What is not public')
    o += UL('Interest rates, maximum loan sizes and bridging terms.', 'How many clients use both floors, and how long they stay.',
            'Named hedging or transactional-banking clients; a named 2023-26 IPO led by Investec.', 'Exact dates on Investec\'s own case-study pages, which were seen only as search extracts.')
    o += END

    o += part('p7', 'Back matter', 'Sources', 'All accessed 7 October 2026. [C] Confirmed in a primary document; [R] Reported or search extract; [I] author\'s reasoning.')
    o += '<table class="src"><thead><tr><th style="width:28px">ID</th><th>Outlet</th><th>Title</th><th>Date</th><th>URL</th></tr></thead><tbody>' + ''.join(
        f'<tr><td>S{n}</td><td>{esc(a)}</td><td>{esc(t)}</td><td>{esc(d)}</td><td style="word-break:break-all">{esc(u)}</td></tr>' for n,(a,t,d,u) in SRC.items()) + '</tbody></table>'
    o += END
    return o

def main():
    body = build().replace('—', ', ')
    spec = importlib.util.spec_from_file_location('b', '/home/user/Applications2027/investec/build/build.py'); B = importlib.util.module_from_spec(spec); spec.loader.exec_module(B)
    cover = ('<div class="cover"><div class="k">The shop guide</div><h1>Who Investec serves,<br>and what it sells</h1>'
             '<div class="sub">The target clients with real examples, what private banking actually does for them, what the investment bank sells, how the two connect, and the one thread that ties it all together. Explained with a shop analogy.</div>'
             '<div class="meta">Prepared 7 October 2026 for the Investec UK Summer Internship 2027 application.<br>Built from Investec case studies, company announcements, law-firm and press releases. Every claim carries a tag and a source number.</div></div>')
    css = open('/home/user/Applications2027/investec/build/style.css').read() + '.card dl{grid-template-columns:86px 1fr}'
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Investec Clients and Products</title><style>{css}</style></head><body>'
            f'{cover}{B.toc(body)}{B.markers(body)}</body></html>')
    open('/home/user/Applications2027/investec/Investec_Clients_and_Products_Shop_Guide.html','w',encoding='utf8').write(page)
    print('figs', len(lib.FIGS))
main()
