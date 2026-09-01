# -*- coding: utf-8 -*-
from pdfbuild import *

def build():
    F=[]; A=F.append
    A(PageBreak())
    A(heading('Part 2 — What JPMorganChase actually is', 0))
    A(Paragraph('Scale, lineage, who runs it, and — at length — what it does in London.', S['h1sub']))

    A(heading('2.1  How it got here: a firm assembled from crises', 1))
    A(P('JPMorganChase is not an organically grown company. It is a stack of acquisitions, several of them made during '
        'financial panics when the target had no other options. Understanding the lineage explains why the firm looks the way it does.'))
    A(make_table(['Year','What was acquired','Why it mattered'],
        [['1799–1877','Predecessor institutions including the Bank of the Manhattan Company and Chemical Bank','The New York retail and commercial banking roots that eventually became Chase.'],
         ['1871','J.P. Morgan &amp; Co. founded','The blue-chip corporate advisory franchise and the name. For a century this was the most powerful private bank in America.'],
         ['2000','Chase Manhattan merges with J.P. Morgan &amp; Co.','Married a large commercial bank to an elite advisory house. This is the origin of the universal-bank model the firm still runs.'],
         ['2004','Bank One','Brought a huge credit-card business, a Midwest branch network — and Jamie Dimon, who became CEO in 2005.'],
         ['2008','Bear Stearns','A collapsing investment bank bought in days during the financial crisis, with Federal Reserve support. Added prime brokerage and clearing.'],
         ['2008','Washington Mutual','The largest bank failure in US history, bought out of receivership. Added West Coast retail deposits and branches.'],
         ['2023','First Republic Bank','Seized by regulators during the 2023 regional-banking crisis and sold to JPMorgan. Added a wealthy coastal client base and private-banking relationships.'],
         ['2025–26','Apple Card portfolio','JPMorgan agreed to become the issuer of the Apple Card. It booked a <b>$2.2bn reserve</b> in 4Q25 for the forward purchase commitment and took roughly 25bp off its CET1 ratio.'],
        ], widths=[0.55,1.4,3.0]))
    A(Paragraph('The pre-2008 lineage above is general business history rather than a figure taken from a document, and is marked '
        'as background knowledge. The 2023 First Republic transaction, and the 2025–26 Apple Card reserve and capital impact, are '
        'sourced to the FY2025 Form 10-K and the 4Q25 earnings release.', S['cap']))
    A(callout('The pattern worth noticing',
        'Three of JPMorgan\'s most important acquisitions — Bear Stearns, Washington Mutual and First Republic — were bought in a '
        'crisis, cheaply, because the firm was one of very few institutions strong enough to buy anything at all. This is the '
        '"fortress balance sheet" doctrine paying for itself, and it is the strategic argument that runs through section 4.1. '
        'Being over-capitalised looks wasteful for nine years and decisive in the tenth.', 'key'))

    A(heading('2.2  Scale today', 1))
    A(make_table(['Metric','2025','2024','2023','Note'],
        [['Total net revenue','$182.4bn','$177.6bn','$158.1bn','2024 included a $7.9bn one-off Visa gain'],
         ['Net income','$57.0bn','$58.5bn','$49.6bn','2025 fall is optical: see note'],
         ['Diluted EPS','$20.02','$19.75','$16.23','Rose despite lower net income — buybacks'],
         ['ROE','17%','18%','17%',''],
         ['ROTCE','20%','22%','21%','Target is 17% through the cycle'],
         ['Overhead ratio','52%','52%','55%','Expense as % of revenue'],
         ['Total assets','$4,424.9bn','$4,002.8bn','$3,875.4bn','$5.0tn by 30 June 2026'],
         ['Deposits','$2,559.3bn','$2,406.0bn','$2,400.7bn',''],
         ['Loans','$1,493.4bn','$1,348.0bn','$1,323.7bn',''],
         ['Common equity','$342.4bn','$324.7bn','$300.5bn',''],
         ['CET1 ratio','14.6%','15.7%','15.0%','Apple Card cost ~25bp'],
         ['Market capitalisation','$868.8bn','$670.6bn','$489.3bn','Up 78% over two years'],
         ['Tangible book value / share','$107.56','$97.30','$86.08',''],
         ['Employees','318,512','317,233','309,926','66 countries; 58% in the US'],
         ['Net charge-off rate','0.74%','0.68%','0.52%','Credit normalising upward'],
        ], widths=[1.25,0.75,0.75,0.75,1.6]))
    A(Paragraph('Source: FY2025 Form 10-K, three-year summary of consolidated financial highlights, page 46. Filed 13 February 2026. '
        'All figures as at or for the year ended 31 December.', S['cap']))
    A(figure('f03_trend','Figure 3. Net income dipped in 2025 only because 2024 contained a $7.9bn one-off gain on Visa shares. '
        'Underlying pre-provision profit rose. Source: FY2025 Form 10-K.'))
    A(P('Assets under management reached <b>$4.8tn</b> at end-2025 and total client assets <b>$7.1tn</b>, both up around 18–20%. '
        'By 30 June 2026 those had reached <b>$5.1tn</b> and <b>$7.7tn</b>. The firm extended $1.9tn of credit and capital in the '
        'first half of 2026 alone.'))
    A(callout('Read the most recent quarter carefully — it is not a run-rate',
        'In Q2 2026 JPMorgan reported its highest quarterly profit ever: net income of <b>$21.2bn</b> and ROTCE of <b>29%</b>. '
        'Both are flattered. The quarter included a <b>$4.6bn gain</b> from a Visa share exchange and $1.0bn of other equity '
        'investment gains, and Equity Markets revenue jumped <b>86%</b> year on year. Excluding those significant items, net income '
        'was <b>$16.9bn</b> and ROTCE <b>23%</b>. Quote the adjusted number in an interview, and say why. '
        '<i>Source: 2Q26 earnings release, filed as an SEC 8-K exhibit.</i>', 'warn'))

    A(heading('2.3  Leadership — and a genuinely important recent change', 1))
    A(P('<b>Jamie Dimon</b> has been Chairman and Chief Executive since 2005–06 and is the dominant figure in global banking. '
        'The succession question has hung over the firm for a decade. In June 2026 it moved decisively.'))
    A(callout('25 June 2026 — the succession field narrowed',
        'JPMorganChase named <b>Doug Petno</b> and <b>Troy Rohrbaugh</b> as <b>Co-Presidents of the firm</b>, effective immediately. '
        'Both had been Co-CEOs of the Commercial &amp; Investment Bank. Petno becomes <b>sole CEO of the CIB</b>; Rohrbaugh moves '
        'across to become <b>CEO of Consumer &amp; Community Banking</b>.<br/><br/>'
        '<b>Marianne Lake</b>, the CEO of CCB and for years regarded as the leading internal successor, is <b>retiring</b> after more '
        'than 25 years.<br/><br/>'
        'Dimon called it "an important step in our Board\'s thoughtful process around succession planning". No timetable for his own '
        'departure was given. Retention equity awards granted the previous day reinforced the ranking: <b>$30m each</b> to Petno and '
        'Rohrbaugh, <b>$20m each</b> to Mary Erdoes and Jennifer Piepszak.<br/><br/>'
        '<i>If you interview using an org chart more than a few months old you will name the wrong CCB head.</i>', 'warn'))
    A(make_table(['Operating Committee member','Title'],
        [['Jamie Dimon','Chairman and Chief Executive Officer'],
         ['Doug Petno','Co-President of JPMorganChase &amp; CEO of Commercial &amp; Investment Bank'],
         ['Troy Rohrbaugh','Co-President of JPMorganChase and CEO of Consumer &amp; Community Banking'],
         ['Mary Callahan Erdoes','CEO, Asset &amp; Wealth Management'],
         ['Jennifer Piepszak','Chief Operating Officer of JPMorganChase'],
         ['Jeremy Barnum','Chief Financial Officer'],
         ['Ashley Bacon','Chief Risk Officer'],
         ['Stacey Friedman','General Counsel'],
         ['Lori Beer','Global Chief Information Officer'],
         ['Teresa Heitsenrether','Chief Data &amp; Analytics Officer'],
         ['Robin Leopold','Head of Human Resources'],
         ['Tim Berry','Global Head of Corporate Responsibility and Chairman of the Mid-Atlantic Region'],
        ], widths=[1.3,2.7]))
    A(Paragraph('Source: jpmorganchase.com/about/leadership, accessed 31 August 2026.', S['cap']))
    A(heading('EMEA and UK leadership', 2))
    A(P('<b>Conor Hillery</b> and <b>Matthieu Wiltz</b> were appointed <b>co-CEOs for EMEA</b> in October 2025. Hillery previously '
        'ran EMEA investment banking, and before that UK investment banking — a useful signal that the UK coverage franchise is a '
        'route to the top of the region. This is press-sourced rather than taken from a JPMorgan filing.'))
    A(callout('An honest gap',
        'I could <b>not</b> identify a currently-named <b>Senior Country Officer for the UK</b> from any primary source. Rather than '
        'guess, treat this as not found. If you need it, the places to look are: the directors\' list in the J.P. Morgan Securities plc '
        'annual report at Companies House; the FCA Financial Services Register, which shows approved senior managers (SMF roles) for '
        'J.P. Morgan Securities plc and J.P. Morgan Europe Limited; and JPMorgan\'s own EMEA press releases. Do not repeat a name in an '
        'interview that you have not verified.', 'warn'))

    A(heading('2.4  The London footprint', 1))
    A(callout('The most important methodological point in this report',
        'JPMorgan\'s group accounts contain <b>no UK line and no London line</b>. The finest geographic cut in the FY2025 Form 10-K is '
        '<b>EMEA: 31,030 employees</b>. Anyone who quotes you a "London revenue" figure taken from group accounts has made it up. '
        'Genuine UK numbers exist in one place only: the statutory accounts of the UK legal entities, filed at Companies House. '
        'Everything in this section is labelled by which of the two it came from.', 'warn'))

    A(heading('The legal entities, and what each one is for', 2))
    A(figure('f08_uk_entities','Figure 4. Where London activity actually books. Sources: FY2025 Form 10-K Exhibit 21; CRD IV Governance '
        'Disclosures (September 2025); J.P. Morgan Securities plc FY2025 statutory accounts filed at Companies House 10 May 2026.'))
    A(P('JPMorgan\'s own <b>CRD IV Governance Disclosures</b> state plainly that the UK\'s two <i>significant</i> entities are '
        '<b>J.P. Morgan Securities plc</b> and <b>J.P. Morgan Europe Limited</b>. A third UK presence, the <b>London Branch of '
        'JPMorgan Chase Bank N.A.</b>, is a branch of the US bank rather than a UK subsidiary.'))
    A(heading('J.P. Morgan Securities plc — the London engine room', 2))
    A(P('This is the entity that matters most for anyone applying to a markets or investment banking role in London. Its own '
        'accounts describe it in terms a candidate should be able to paraphrase:'))
    A(callout('J.P. Morgan Securities plc, FY2025 annual report — strategic report',
        '"JPMS plc is an <b>international flagship entity for equity and debt securities across the Markets business</b>. JPMS plc is '
        'the <b>client facing and traders\' employing entity for the majority of Markets (EMEA ex EU)</b>; and the <b>primary Banking '
        'M&amp;A advisory entity</b>."<br/><br/>'
        'In other words: if you join Markets or M&amp;A in London, this is very likely the company that employs you.', 'key'))
    A(make_table(['J.P. Morgan Securities plc (USD thousands)','2025','2024'],
        [['Net operating income','9,542,478','9,144,072'],
         ['Profit before taxation','3,272,409','3,836,861'],
         ['Profit after tax','2,344,078','2,596,449'],
         ['Total assets','830,883,547','697,596,028'],
         ['Common Equity Tier 1 capital','37,434,585','36,053,977'],
         ['Total capital','55,987,951','55,806,030'],
         ['Risk-weighted assets','227,965,642','195,273,360'],
         ['Leverage exposure','757,149,645','607,589,034'],
         ['CET1 ratio','16.4%','18.5%'],
         ['Total capital ratio','24.6%','28.6%'],
         ['Leverage ratio','6.3%','7.6%'],
         ['Return on assets','0.3%','0.4%'],
        ], widths=[2.1,1.0,1.0]))
    A(Paragraph('Source: J.P. Morgan Securities plc, full accounts for the year ended 31 December 2025, filed at Companies House '
        '10 May 2026 (company number 02711006). The filed document is a scanned image; figures were read by optical character '
        'recognition and cross-checked against the narrative text in the same document, which independently states "$9.5 billion", '
        '"$3.3 billion" and "$830.9 billion".', S['cap']))
    A(P('Three things to take from that table. First, <b>scale</b>: a single UK subsidiary holds $831bn of assets — larger than '
        'most European banks in their entirety. Second, <b>direction</b>: net operating income rose, driven in the company\'s own '
        'words by "increased client activity in Markets lines of business", while pre-tax profit fell because expenses, "mainly '
        'brokerage fees", rose faster. Third, <b>intensity</b>: risk-weighted assets grew 17% and the CET1 ratio fell from 18.5% to '
        '16.4%. The entity is being worked harder.'))
    A(callout('A calibration, clearly marked as inference',
        'JPMS plc\'s $9.5bn of net operating income sits against group CIB revenue of $78.5bn — roughly <b>12%</b>. That is a useful '
        'order of magnitude for "how big is London within the CIB", but it is <b>inference, not a disclosed figure</b>. The two '
        'measures are not defined identically, JPMS plc books some activity for other regions, and London activity also books through '
        'the N.A. London Branch. Treat 12% as an anchor, not a fact.', 'info'))
    A(P('The accounts also record three structural changes worth knowing: the Zurich branch continues, focused on sales across '
        'Investment Banking, Equities and Corporate Banking; the <b>Paris branch was deregistered on 13 November 2025</b>; and a new '
        'branch in <b>GIFT City, India was registered on 8 January 2026</b>.'))

    A(heading('Headcount and sites', 2))
    A(P('JPMorgan does not publish a UK headcount. Press reporting in April 2026 put the <b>UK workforce at around 23,000</b>, up from '
        'roughly 18,000 a decade earlier. Set against the audited EMEA figure of 31,030, that would make the UK about three-quarters of '
        'the region — a ratio that is indicative only, since one number is press-sourced and the other audited.'))
    A(P('The UK sites are not a matter of inference: they appear as locations on live job requisitions read on 31 August 2026. '
        '<b>London</b>, <b>Bournemouth</b> (Dorset), <b>Glasgow</b>, and <b>Edinburgh</b> all carry current vacancies, and a Global '
        'Private Bank programme also lists <b>Manchester</b>. Glasgow and Bournemouth are substantial technology and operations centres, '
        'not satellite offices — several 2027 graduate programmes are based there rather than in London.'))
    A(P('On the office estate: JPMorgan occupies <b>25 Bank Street</b> in Canary Wharf, which is also cited as Chase UK\'s registered '
        'address. Press reports from November 2025 describe plans for a new Canary Wharf headquarters of around <b>three million square '
        'feet</b> housing up to <b>12,000 staff</b>, co-developed with Canary Wharf Group and designed by Foster + Partners, with a '
        'roughly six-year build. I could not find a JPMorgan press release confirming those dimensions, so treat them as press-reported.'))

    A(heading('Brexit — and the quiet partial reversal', 2))
    A(P('After the 2016 referendum JPMorgan built out <b>J.P. Morgan SE</b> in Germany as its EU-facing bank and expanded in Paris, '
        'Dublin, Luxembourg, Milan and Madrid. The consensus expectation was a permanent drain of London jobs.'))
    A(P('That is not what happened. In <b>April 2026</b> JPMorgan moved a number of trading roles <b>from Paris back to London</b>, '
        'with executives reportedly concluding they had <b>overestimated how many EU-based staff the post-Brexit rules actually '
        'required</b>. Paris headcount had grown to over 1,000 since Brexit — against a UK workforce of about 23,000.'))
    A(P('That reporting is press-sourced, but there is a corroborating fact in audited accounts: the <b>Paris branch of J.P. Morgan '
        'Securities plc was deregistered on 13 November 2025</b>. A press claim supported by an independent primary document is worth '
        'considerably more than either alone, and this is a good example of how to test a story you read.'))

    A(heading('Chase UK, and the ring-fencing question', 2))
    A(P('<b>Chase UK</b> is JPMorgan\'s digital retail bank — a current account and savings proposition with no branches. It is the '
        'firm\'s only scaled consumer bank outside the United States, and it sits inside <b>J.P. Morgan Europe Limited</b>. Press '
        'reporting put it at more than <b>2.5 million customers</b> as at February 2025 and roughly <b>$31bn</b> of UK deposits. It has '
        'been loss-making by design during build-out.'))
    A(callout('Ring-fencing: the live regulatory story, and the best UK talking point available',
        'UK <b>ring-fencing</b>, in force since 2019, forces a bank whose retail deposits exceed a threshold to place its retail '
        'business in a legally separate, separately capitalised entity that cannot conduct most investment-banking activity. The '
        'threshold was <b>raised from £25bn to £35bn in February 2025</b>.<br/><br/>'
        'J.P. Morgan Europe Limited has disclosed that management "has been considering the strategy and long-term implications of the '
        'regulatory requirements for ring-fencing the Chase business if its total core deposits exceed the ring-fencing deposits '
        'threshold of £35 billion... as Chase\'s deposit balances increase."<br/><br/>'
        'Meanwhile the regime itself is being loosened. On <b>18 May 2026</b> HM Treasury published <i>"Safeguarding Stability, Enabling '
        'Growth: The Ring-Fencing Review"</i>, confirming relaxation including a <b>"New Growth Allowance"</b> permitting ring-fenced '
        'banks to undertake some currently prohibited activities, and a commitment to review the £35bn threshold every three years. '
        'Delivery is via the Financial Services and Markets Bill 2026-27, secondary legislation and PRA rule changes.<br/><br/>'
        '<b>Why this is the single best thing to raise in a Chase UK or UK-focused interview:</b> Chase UK\'s entire strategy is to '
        'grow deposits fast. Doing so walks it toward a regime that would impose a costly restructuring — at exactly the moment the '
        'Government is making that regime less onerous. The commercial outcome genuinely depends on legislation being drafted now.', 'key'))
    A(P('The banks currently inside the regime are Barclays, HSBC, Lloyds, NatWest and Santander UK. JPMorgan is not — it is '
        'approaching the line, not over it.'))

    A(heading('What London is a hub for, and what it is not', 2))
    A(P('Sourced from primary documents: London is the <b>EMEA regional headquarters</b>; it is where Markets for EMEA ex-EU is traded '
        'and booked; it is the primary M&amp;A advisory entity; and it hosts the firm\'s only large non-US retail bank. Current London '
        'vacancies span commodities trading technology, equity-derivatives front office, rates technology, credit quantitative trading, '
        'securitised products underwriting, EMEA sponsors lending and fund finance, MENAT private banking, and cross-currency payments '
        'product management. That is a genuine global hub, not a regional sales office.'))
    A(P('What London is <i>not</i>, and this is inference rather than a sourced statement: it is not where firm-level capital is '
        'allocated. Every segment CEO and every Operating Committee member is US-based. London runs the EMEA franchise and books global '
        'risk; New York decides how much capital the franchise gets.'))
    return F
