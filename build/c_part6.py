# -*- coding: utf-8 -*-
from pdfbuild import *

GLOSSARY = [
 ('Advanced / Standardized approaches','Two regulatory methods for calculating risk-weighted assets. Banks must satisfy both; whichever produces the lower ratio "binds". At end-2025 the Advanced approach became binding for JPMorgan.'),
 ('AUM — assets under management','Client money the firm actively manages and charges a management fee on. $4.8tn at end-2025.'),
 ('Assets under supervision / client assets','A broader measure including assets merely held or overseen, on which little or no management fee is earned. $7.1tn at end-2025.'),
 ('Basis point (bp)','One hundredth of one percent. 100bp = 1%.'),
 ('Bid-ask spread','The gap between the price a market maker will buy at and the price it will sell at. The core earnings mechanism of a trading desk.'),
 ('CET1 — Common Equity Tier 1','The highest-quality loss-absorbing capital: essentially ordinary shares and retained profits. The CET1 ratio divides it by risk-weighted assets.'),
 ('Charge-off','A loan written off as uncollectible. The net charge-off rate expresses these as a percentage of loans.'),
 ('CIB','Since Q2 2024, the Commercial &amp; Investment Bank. Before that, the Corporate &amp; Investment Bank — a different perimeter.'),
 ('Coverage','Organising client relationships by industry, country or product. A coverage banker owns the relationship rather than a product.'),
 ('Custody','Holding securities safely on a client\'s behalf and maintaining the records of ownership.'),
 ('DCM — debt capital markets','Raising money for clients by issuing bonds.'),
 ('Delta One','Desks trading instruments that move one-for-one with an underlying index, such as ETFs, swaps and futures.'),
 ('Derivative','A contract whose value derives from something else — a rate, price or index. Used to hedge risk or gain exposure without owning the underlying asset.'),
 ('ECM — equity capital markets','Raising money for clients by issuing shares, including IPOs.'),
 ('Flow vs structured','Flow is high-volume standardised trading at thin margins; structured is bespoke, complex and higher-margin.'),
 ('Goodwill','The accounting entry created when an acquirer pays more than the book value of what it buys. Excluded from tangible common equity because it cannot absorb losses.'),
 ('Leverage','Funding assets with borrowed money rather than equity. Magnifies both returns and losses.'),
 ('Leveraged finance','Arranging debt for already heavily-indebted borrowers, typically to fund private equity buyouts.'),
 ('LCR — liquidity coverage ratio','Whether a bank holds enough easily-sellable assets to survive 30 days of stress. Must exceed 100%; JPMorgan averaged 111%.'),
 ('M&amp;A','Mergers and acquisitions — advising companies on buying, selling or defending themselves.'),
 ('Managed basis','JPMorgan\'s internal presentation, which grosses up certain tax-advantaged revenue. Managed revenue exceeds reported revenue ($185.6bn vs $182.4bn in 2025).'),
 ('Market making','Continuously quoting buy and sell prices so clients can trade when they wish. Distinct from proprietary trading.'),
 ('MiFID II','EU regulation applied from 2018 that forced investment research to be paid for separately from trading execution. The UK has since partly reversed this.'),
 ('NII — net interest income','Interest earned minus interest paid. JPMorgan: $95.9bn managed in 2025.'),
 ('NIM — net interest margin','Net interest income as a percentage of interest-earning assets. JPMorgan: 2.50% in 2025; 3.75% excluding Markets.'),
 ('Overhead ratio','Noninterest expense divided by revenue. JPMorgan: 52% in 2025.'),
 ('PPNR — pre-provision net revenue','Revenue minus expense, before credit losses. Management\'s preferred growth measure.'),
 ('Prime brokerage','Financing, securities lending, custody and clearing sold to hedge funds. A major driver of recent Equity Markets growth.'),
 ('Proprietary trading','Betting the bank\'s own money on market direction. Largely banned for US banks by the Volcker Rule.'),
 ('Provision for credit losses','Money set aside in advance for loans expected to go bad. $14.2bn in 2025.'),
 ('Ring-fencing','UK rules requiring a large retail bank to sit in a separate, separately capitalised entity insulated from investment banking. Threshold £35bn of core deposits.'),
 ('ROTCE','Return on tangible common equity — profit as a percentage of shareholders\' equity excluding goodwill and intangibles. JPMorgan\'s through-the-cycle target is 17%.'),
 ('RWA — risk-weighted assets','Assets re-weighted by riskiness; the denominator of capital ratios. $1,984bn (Standardized) at end-2025.'),
 ('Securitised products','Bonds created by bundling together pools of loans such as mortgages or car finance.'),
 ('SLR — supplementary leverage ratio','Capital against total exposure with no risk-weighting. A backstop to the risk-based ratios.'),
 ('Sponsors','Private equity firms. The most commercially valuable client group in investment banking.'),
 ('Spread vs fee revenue','The two fundamental earnings modes: lending margin, versus charging for a service.'),
 ('Subscription finance','Lending to private-market funds against investors\' undrawn commitments. Named by management as a 2026 growth driver.'),
 ('TLAC','Total loss-absorbing capacity — capital plus debt that can be written down before depositors suffer. $590bn at Q2 2026.'),
 ('Underwriting','Guaranteeing that an issuer receives its money, then placing the securities with investors. The fee pays for taking that risk.'),
 ('Volcker Rule','US rule from the 2010 Dodd-Frank Act restricting banks from proprietary trading.'),
 ('Wallet share','A bank\'s percentage of the total industry fee pool. JPMorgan: 8.4% of global IB fees in 2025.'),
]

ASSUMPTIONS = [
 ('A1','The 1 November 2026 deadline is a genuine backstop, and places fill earlier.',
  'JPMorgan states in 35 of 43 UK postings that it fills classes "on a rolling basis" and urges early application. The stated close date is in the requisition metadata.',
  'If wrong and the process is not really rolling, applying in September costs you nothing. The advice is asymmetric, which is why I give it confidently.'),
 ('A2','The 43 UK requisitions found represent essentially all currently-open UK early-careers programmes.',
  '2,751 requisitions were harvested across ~35 keyword queries and filtered to the UK. Coverage is broad but keyword-driven.',
  'A programme with unusual title wording could have been missed. Check the Oracle listing filtered to United Kingdom yourself — it takes five minutes and is the authoritative source.'),
 ('A3','No UK Spring Week is currently open, rather than my having failed to find one.',
  '"Spring week" returned zero requisitions globally; "insight week", "early insight" and "discovery" returned matches, none in the UK.',
  'If one opens later in the autumn — which history suggests is likely — first-year students would have an additional route. This is the single most likely thing in this report to change within two months.'),
 ('A4','J.P. Morgan Securities plc is the entity most London Markets and M&amp;A candidates would join.',
  'Its own FY2025 accounts describe it as "the client facing and traders\' employing entity for the majority of Markets (EMEA ex EU); and the primary Banking M&amp;A advisory entity".',
  'Some London staff are employed by JPMorgan Chase Bank N.A. London Branch or other entities. This affects which accounts describe your employer, not your job.'),
 ('A5','JPMS plc revenue of $9.5bn against group CIB revenue of $78.5bn implies London is roughly 12% of the CIB.',
  'Both figures are primary, but they are not defined identically and the entity does not map cleanly to the segment.',
  'The true figure could plausibly be anywhere from 10% to 20%. Marked as inference throughout; do not quote it as a JPMorgan disclosure.'),
 ('A6','UK headcount is approximately 23,000.',
  'Press reporting (Bloomberg and others, April 2026). JPMorgan publishes no UK headcount.',
  'Could be materially different. The audited EMEA figure of 31,030 is the only firm anchor, and it caps the UK number.'),
 ('A7','The role-comparison scores in Figure 14 are reasonable.',
  'Derived from the requisition text and the business analysis in Part 3.',
  'These are judgements, not data. If you disagree with one, your disagreement is as valid as my score — argue with it rather than adopting it.'),
 ('A8','Recruitment stage detail (online assessment, HireVue, assessment centre) is broadly accurate.',
  'Recruitment aggregators and candidate reports. JPMorgan does not publish its process.',
  'Stages could differ by programme or have changed for this cycle. Only the application step and dates are primary. Do not build your preparation on the assumption that the sequence is fixed.'),
 ('A9','Q2 2026 results are not representative of run-rate earnings.',
  'The quarter contained a $4.6bn Visa gain and an 86% jump in Equity Markets. JPMorgan itself reports figures excluding significant items.',
  'If the elevated trading environment persists, I will have understated the firm\'s earnings power. Using the adjusted figure is the conservative choice.'),
 ('A10','Chase UK remains loss-making and below the ring-fencing threshold.',
  'Press reporting and JPMEL\'s own disclosure about "considering the strategy and long-term implications" of crossing £35bn.',
  'I could NOT retrieve JPMEL\'s FY2025 profit or loss — see section 6.3. If Chase UK has reached profitability, the strategic story changes materially.'),
 ('A11','Pre-2008 corporate history is accurate.',
  'General business knowledge, not verified against a document for this report. Marked as background knowledge in section 2.1.',
  'Dates could be imprecise. The 2023 First Republic acquisition and the 2025-26 Apple Card items are sourced to filings.'),
 ('A12','Competitor figures are comparable enough to be placed in one table.',
  'Each is taken from that firm\'s own 2025 results reporting.',
  'They are NOT strictly like-for-like: revenue definitions differ, HSBC reports in USD, Barclays in GBP, and RoTE and ROTCE are calculated differently. Treat Figure 12 as orders of magnitude only.'),
]

SOURCES = [
 ('PRIMARY — JPMorganChase filings and disclosures', [
  'JPMorganChase, <b>Annual Report on Form 10-K for the year ended 31 December 2025</b>, filed 13 February 2026. Downloaded and text-extracted in full (410 pages). https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/corp-10k-2025.pdf — accessed 31 August 2026. <i>Used for: three-year financial highlights (p.46), human capital and workforce by region and line of business (p.9), significant subsidiaries (Exhibit 21).</i>',
  'JPMorganChase, <b>Fourth-quarter and full-year 2025 earnings press release</b>, 13 January 2026. https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/d868c7ef-1670-465d-ba75-c2b36ddbcc6b.pdf — accessed 31 August 2026.',
  'JPMorganChase, <b>Earnings release financial supplement, fourth quarter 2025</b>. https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/ff69a4a4-ab52-4a38-b82a-f153ba695e41.pdf — accessed 31 August 2026. <i>The single most useful document in this report: full-year segment income statements, revenue by sub-business, allocated equity, and the managed-basis reconciliation.</i>',
  'JPMorganChase, <b>Second-quarter 2026 earnings release</b>, SEC Form 8-K Exhibit 99.1. https://www.sec.gov/Archives/edgar/data/0000019617/000162828026048078/a2q26erfexhibit991narrative.htm — accessed 31 August 2026.',
  'JPMorganChase, <b>2026 Company Update — full event transcript</b>, 23 February 2026. https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/2026-company-updates/company-update-full-event-transcript.pdf — accessed 31 August 2026. <i>Note: this replaces what was previously called Investor Day. Source for the 17% ROTCE target, $19.8bn technology spend and ~$105bn expense guidance.</i>',
  'JPMorganChase, <b>CRD IV Governance Disclosures</b>, September 2025. https://www.jpmorgan.com/content/dam/jpm/global/disclosures/by-region/crd4_governance.pdf — accessed 31 August 2026. <i>Primary source confirming that J.P. Morgan Securities plc and J.P. Morgan Europe Limited are the UK "significant entities", and that JPMEL operates the Chase-branded UK digital consumer bank.</i>',
  'JPMorganChase, <b>Leadership</b>. https://www.jpmorganchase.com/about/leadership — accessed 31 August 2026.',
  'JPMorganChase, <b>"JPMorganChase names Doug Petno and Troy Rohrbaugh Co-Presidents of the company"</b>, press release, 25 June 2026. https://www.jpmorganchase.com/newsroom/press-releases/2026/jpmc-names-doug-petno-and-troy-rohrbaugh-co-presidents-of-the-company — accessed 31 August 2026.',
  'J.P. Morgan, <b>About us — United Kingdom</b>. https://www.jpmorgan.com/GB/en/about-us — accessed 31 August 2026.',
 ]),
 ('PRIMARY — UK statutory filings (Companies House)', [
  '<b>J.P. Morgan Securities plc</b>, full accounts for the year ended 31 December 2025, filed 10 May 2026, company number 02711006. https://find-and-update.company-information.service.gov.uk/company/02711006/filing-history — accessed 31 August 2026. <i>Filed as a scanned image; read by optical character recognition and cross-checked against narrative text in the same document.</i>',
  '<b>J.P. Morgan Europe Limited</b>, company number 00938937, filing history. https://find-and-update.company-information.service.gov.uk/company/00938937/filing-history — accessed 31 August 2026. <i>Accounts retrieved but not machine-readable; see section 6.3.</i>',
 ]),
 ('PRIMARY — live recruitment data', [
  'JPMorganChase Oracle Recruiting Cloud, public requisition API and candidate site (site CX_1001). Search endpoint: https://jpmc.fa.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions — queried 31 August 2026. Human-readable listing: https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions <i>2,751 unique requisitions harvested; 43 UK early-careers requisitions analysed in full.</i>',
  'JPMorganChase careers pages: https://www.jpmorganchase.com/careers/explore-opportunities/students-and-graduates and .../programs — accessed 31 August 2026. <i>Content shells; no live listings rendered.</i>',
 ]),
 ('SECONDARY — regulation', [
  'HM Treasury, <b>"Safeguarding Stability, Enabling Growth: The Ring-Fencing Review"</b>, policy paper, 18 May 2026 — as summarised by Linklaters, Freshfields, Norton Rose Fulbright and the Bank of England. Accessed 31 August 2026.',
  'Bank of England / PRA, <b>CP10/26 "Ring-fenced bodies: Changes to the continuity of provision of services rules"</b>, July 2026; and PRA announcement on ring-fence change, May 2026. https://www.bankofengland.co.uk — accessed 31 August 2026.',
  'FCA, <b>PS24/9</b> (payment optionality for investment research) and <b>PS25/4</b> (extension to fund managers); FCA multi-firm review of MiFID II research unbundling. https://www.fca.org.uk — accessed 31 August 2026.',
 ]),
 ('SECONDARY — trade press and peer reporting', [
  'Bloomberg, <b>"JPMorgan Moves Some Paris Traders to London in Brexit Rethink"</b>, 27 April 2026 — and corroborating coverage in City AM and Business Matters. Accessed 31 August 2026.',
  'Fortune, coverage of JPMorgan\'s planned Canary Wharf headquarters, 27 November 2025. Accessed 31 August 2026.',
  'Reuters Breakingviews, <b>"JPMorgan German retail bank has weak UK launchpad"</b>, 4 September 2025 — source for Chase UK customer and deposit figures. Accessed 31 August 2026.',
  'The Irish Times, <b>"JP Morgan names Irishman Conor Hillery co-CEO of Europe"</b>, 6 October 2025. Accessed 31 August 2026.',
  'CNBC, <b>"JPMorgan names Doug Petno and Troy Rohrbaugh co-presidents as longtime exec Marianne Lake exits"</b>, 25 June 2026. Accessed 31 August 2026.',
  'LSEG / Dealogic 2025 full-year league table reporting, via Reuters and Dealogic Global Markets Rankings FY2025. Accessed 31 August 2026.',
  'Peer full-year 2025 results: Goldman Sachs (15 January 2026), Morgan Stanley, Bank of America (14 January 2026), Citigroup, Barclays PLC 2025 Results Announcement, HSBC Holdings plc Annual Results 2025 (25 February 2026). Accessed 31 August 2026.',
  'CNBC, <b>"Private credit\'s cracks open door for Wall Street banks\' comeback"</b>, 27 March 2026, and associated private-credit market sizing. Accessed 31 August 2026.',
 ]),
 ('UNVERIFIED — treated as colour only, not fact', [
  'Recruitment aggregators and candidate-experience sites (Extern, FE Training, IGotAnOffer, Leland, Glassdoor, Wall Street Oasis, Bright Network, TargetJobs) used <b>only</b> for the recruitment-stage descriptions in section 5.5, and flagged as such there. No financial figure, deadline, org-chart entry or programme detail in this report rests on any of them.',
 ]),
]

def build():
    F=[]; A=F.append
    A(PageBreak())
    A(heading('Part 6 — Reference material', 0))

    A(heading('6.1  Glossary', 1))
    A(make_table(['Term','Meaning'], [[t, d] for t, d in GLOSSARY], widths=[1.0,3.5], small=True))

    A(PageBreak())
    A(heading('6.2  Assumptions register', 1))
    A(P('Every assumption I made, why I made it, and what changes if it is wrong. If you challenge one item in this report, '
        'challenge something here.'))
    A(make_table(['#','Assumption','Why I made it','What changes if it is wrong'],
        [[n, a, w, c] for n, a, w, c in ASSUMPTIONS], widths=[0.2,1.5,1.9,1.9], small=True))

    A(heading('6.3  Open questions — what I could not verify, and where you should look', 1))
    A(make_table(['Gap','Status','Where to resolve it'],
        [['<b>Chase UK / J.P. Morgan Europe Limited FY2025 profit or loss</b>','Not retrieved. The Companies House filing is a scanned image and defeated the text extraction available to me.','Companies House company 00938937, most recent full accounts. Order the PDF and read the income statement and the ring-fencing discussion directly.'],
         ['<b>UK Senior Country Officer</b>','Not found in any primary source.','The directors\' list in the J.P. Morgan Securities plc annual report; the FCA Financial Services Register (senior manager approvals for JPMS plc and JPMEL).'],
         ['<b>J.P. Morgan Securities plc employee headcount</b>','Not retrieved — the staff-numbers note sits deeper in the accounts than I extracted.','Same Companies House filing, the "Employee information" or "Staff costs" note.'],
         ['<b>J.P. Morgan International Bank Ltd</b>','Named in the brief but <b>not present</b> in the FY2025 10-K significant-subsidiary list. I could not confirm its current status.','Companies House name search; the FCA Register. It may have been merged, renamed or fallen below the significance threshold.'],
         ['<b>Intake sizes for any programme</b>','Not published. The field is null on every requisition.','Ask a recruiter directly at a campus event. No public source exists.'],
         ['<b>Return-offer conversion rates</b>','Not published by JPMorgan, and I found no credible primary figure.','Ask current interns or recent joiners. Treat any published percentage as an estimate.'],
         ['<b>Visa sponsorship policy for UK programmes</b>','Mostly silent; two Data &amp; AI postings explicitly exclude sponsorship.','The application form itself, and the recruiter. <b>Resolve this before applying if it affects you.</b>'],
         ['<b>Technology spend split by line of business</b>','Referenced in the Company Update transcript but the figures are in the slide deck, which I did not retrieve.','The 2026 Company Update presentation PDF on jpmorganchase.com/ir.'],
         ['<b>Whether a UK Spring Week will open</b>','Unknown. None posted as at 31 August 2026.','Re-check the Oracle UK listing monthly from October.'],
        ], widths=[1.05,1.7,2.3], small=True))

    A(heading('6.4  Reading list', 1))
    A(make_table(['What to read','Why it is worth your time'],
        [['<b>1.</b> JPMorganChase FY2025 Form 10-K — read pages 46 to 60 only','The financial highlights and the executive overview. Do not read all 410 pages. This gives you every headline number with its footnotes.'],
         ['<b>2.</b> 4Q25 earnings release financial supplement','Twenty-nine pages of tables. Pages 12, 16, 20 and 23 are the four segments. If you read one document before an interview, read this one.'],
         ['<b>3.</b> The 2026 Company Update transcript, 23 February 2026','How management explains itself in its own words. The ROTCE-as-output passage alone is worth the read.'],
         ['<b>4.</b> Jamie Dimon\'s annual letter to shareholders','Long, opinionated, and the single most quoted document in banking interviews. Read the most recent one and know two arguments from it.'],
         ['<b>5.</b> J.P. Morgan Securities plc statutory accounts (Companies House)','Almost no candidate does this. It tells you what London actually is, in audited numbers.'],
         ['<b>6.</b> The requisition text of the two programmes you apply to','Interviewers ask "why this programme". The answer is in the posting, and most applicants have not read it carefully.'],
         ['<b>7.</b> HM Treasury\'s Ring-Fencing Review (May 2026)','The live UK regulatory story. Essential for Chase UK, useful everywhere in London.'],
         ['<b>8.</b> FCA PS24/9 and PS25/4 on research payment optionality','Essential if you are applying to Research; good context otherwise.'],
         ['<b>9.</b> Goldman Sachs and Morgan Stanley FY2025 results','You cannot argue that JPMorgan is well run without knowing what the alternatives look like.'],
         ['<b>10.</b> Barclays FY2025 results','The clearest illustration of why scale matters: a good UK bank earning roughly a third of JPMorgan\'s return.'],
         ['<b>11.</b> Andrew Ross Sorkin, <i>Too Big to Fail</i>','How Bear Stearns and Washington Mutual happened, and why the fortress doctrine exists.'],
         ['<b>12.</b> Duff McDonald, <i>Last Man Standing</i>','A biography of Dimon and the Bank One turnaround. Explains the culture you would be joining.'],
         ['<b>13.</b> Financial News London and eFinancialCareers','The best sources on the London market specifically — hiring, pay, and who is moving where.'],
         ['<b>14.</b> The FT Lex column and Bloomberg banking coverage','Daily habit. You need one current story you can discuss for any interview.'],
         ['<b>15.</b> Aswath Damodaran\'s free valuation materials','If you are applying to Investment Banking and have never built a DCF, start here rather than with a paid course.'],
        ], widths=[1.3,3.0], small=True))

    A(PageBreak())
    A(heading('6.5  Sources', 1))
    A(P('All web sources accessed <b>31 August 2026</b>. Documents were downloaded and text-extracted locally where possible so that '
        'figures were read from the source rather than from a summary of it.'))
    for hdr, items in SOURCES:
        A(Paragraph(hdr, S['h3']))
        for it in items:
            A(Paragraph('• ' + it, S['src']))
    A(Spacer(1,6))
    A(callout('A closing note on how to use this report',
        'The financial analysis in Parts 1 to 4 will stay broadly valid for a year. The recruitment information in Part 5 will not — '
        'it is a photograph of one day, 31 August 2026, and the cycle it describes closes on 1 November 2026.<br/><br/>'
        'Before you apply, spend five minutes at '
        'https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions filtered to the United Kingdom, and '
        'check the programmes you care about are still open. That is the authoritative source. This report is a considered reading '
        'of it, not a replacement for it.', 'info'))
    return F
