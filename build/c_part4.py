# -*- coding: utf-8 -*-
from pdfbuild import *

def build():
    F=[]; A=F.append
    A(PageBreak())
    A(heading('Part 4 — What makes JPMorgan different, and where it is exposed', 0))

    A(heading('4.1  The fortress balance sheet', 1))
    A(P('"Fortress balance sheet" is Jamie Dimon\'s phrase and it has been the firm\'s organising doctrine for twenty years. '
        'It means holding more capital and more liquidity than regulators demand, accepting a lower return in good years in exchange '
        'for the ability to act in bad ones.'))
    A(P('At end-2025 that meant a <b>CET1 ratio of 14.6%</b>, <b>$1.5tn of cash and marketable securities</b>, a <b>liquidity coverage '
        'ratio of 111%</b>, and by mid-2026 <b>$590bn of total loss-absorbing capacity</b> — the layer of capital and debt that can be '
        'written down before depositors are touched.'))
    A(callout('Why this is strategy rather than caution',
        'Excess capital looks like waste until the moment it does not. JPMorgan bought <b>Bear Stearns</b> and <b>Washington Mutual</b> '
        'in 2008 and <b>First Republic</b> in 2023 — in each case because it was among the very few institutions with the balance sheet '
        'to absorb a failing bank at short notice, and in each case at a price no competitive auction would have produced.<br/><br/>'
        'The 2023 US regional banking crisis is the cleanest illustration. Deposits fled smaller banks and a large share of them landed '
        'at JPMorgan. The firm was paid for its strength twice over: it gained deposits for nothing, and it acquired First Republic\'s '
        'wealthy client base cheaply. A crisis is a redistribution, and the fortress decides which side of it you are on.', 'key'))

    A(heading('4.2  Scale as strategy — and the counter-argument', 1))
    A(P('<b>The bull argument.</b> Banking has become a fixed-cost industry. Technology, regulatory compliance, cyber security and data '
        'infrastructure cost roughly the same whether you serve 10 million or 80 million customers. JPMorgan will spend about '
        '<b>$19.8bn on technology in 2026</b>. Very few institutions on earth can match that, and those that cannot must either '
        'specialise or fall behind. Spend more, build better, take share in every product at once, and the advantage compounds.'))
    A(P('There is evidence for it. In 2025 the firm was #1 in global investment banking fees, grew Markets revenue 19%, grew Payments '
        'to a record, grew AUM 18%, opened 1.7 million net new checking accounts and 10.4 million credit card accounts — simultaneously.'))
    A(P('<b>The bear argument</b> has three parts, and they deserve to be taken seriously.'))
    A(Paragraph('<b>The law of large numbers.</b> On $57bn of net income and $4.4tn of assets, growth becomes arithmetically hard. '
        'There is no acquisition large enough to move the needle that regulators would permit.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Spending is not the same as building.</b> $19.8bn buys a great deal of legacy maintenance as well as innovation. '
        'Management itself said the firm is "probably past the point of peak modernization" and has shifted focus to "modernizing the '
        'underlying application code and data" — an admission that the hard part is not finished.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Size is taxed.</b> Systemic capital surcharges rise with size and complexity. Each increment of scale requires '
        'more capital per unit of risk than the last.', S['bullet'], bulletText='•'))

    A(heading('4.3  The competitive landscape', 1))
    A(figure('f10_competitors','Figure 12. Scale comparison, FY2025. Definitions differ between firms and between currencies; '
        'treat as orders of magnitude rather than a like-for-like table.'))
    A(make_table(['Competitor','Strategy and product mix','London presence','How it competes with JPMorgan'],
        [['<b>Bank of America</b><br/>FY25 revenue ~$113bn, net income $30.5bn','Universal bank; huge US retail deposit base; strong markets franchise','Large London investment bank and trading floor','The closest structural analogue. Similar model, meaningfully lower returns.'],
         ['<b>Citigroup</b><br/>FY25 net income $14.3bn','Universal bank with unmatched global corporate network; multi-year restructuring','Major London hub','Genuinely competitive in <b>payments and treasury services</b> — arguably JPMorgan\'s only peer in global cash management.'],
         ['<b>Wells Fargo</b>','Predominantly US commercial and retail; small investment bank','Limited','Barely competes outside US lending.'],
         ['<b>Goldman Sachs</b><br/>FY25 revenue $58.3bn, net income $17.2bn, ROE 15.0%','Advisory and trading elite; asset management growing; consumer retreat','Major London office; EMEA advisory powerhouse','<b>#1 in M&amp;A</b> by volume and fee revenue in 2025. The primary rival for advisory prestige and talent. No deposit base of comparable scale.'],
         ['<b>Morgan Stanley</b><br/>FY25 revenue $70.6bn, net income $16.9bn, ROTCE 21.6%','Wealth management as ballast plus a strong institutional bank','Large London presence','The highest-returning large US bank in 2025. Its wealth-led model is the main strategic alternative to JPMorgan\'s.'],
         ['<b>Barclays</b><br/>FY25 income £29.1bn, PBT £9.1bn, RoTE 11.3%','The only UK bank with a genuine full-service investment bank','Headquartered in London','Competes directly in London markets and DCM. Returns roughly a third of JPMorgan\'s.'],
         ['<b>HSBC</b><br/>FY25 revenue $68.3bn, PBT $29.9bn, RoTE 13.3%','Asia-focused commercial and trade bank','London-headquartered','Dominant in Asian trade finance; not a serious M&amp;A rival.'],
         ['<b>UBS</b>','World\'s largest wealth manager post-Credit Suisse; deliberately smaller investment bank','Significant London markets presence','Competes hardest with <b>AWM</b>, not the CIB.'],
         ['<b>Deutsche Bank / BNP Paribas</b>','European universal banks; BNP led <b>EMEA DCM</b> in 2025','Both large in London','BNP is a real European rival in debt and financing; Deutsche in rates.'],
         ['<b>NatWest / Lloyds / Santander UK</b>','UK ring-fenced retail and commercial banks','UK-only','Compete with <b>Chase UK</b>, not with the CIB.'],
        ], widths=[1.15,1.5,0.9,2.0], small=True))
    A(heading('The boutiques — a different kind of threat', 2))
    A(P('<b>Evercore, Centerview, Lazard, PJT, Rothschild, Moelis, Perella Weinberg</b> offer advisory only. No trading, no lending, no '
        'balance sheet, and therefore no conflict of interest — a genuine selling point when a board wants advice unclouded by the '
        'adviser\'s desire to underwrite the financing.'))
    A(P('They cannot underwrite a multi-billion acquisition facility, which is exactly what JPMorgan sells. But they compete '
        'ferociously for <b>people</b>, offering higher pay per head and faster responsibility. Evercore ranked fifth by M&amp;A fee '
        'revenue in 2025 with $1.7bn — remarkable for a firm a fraction of JPMorgan\'s size. If you are weighing an investment banking '
        'career, this is the real trade-off: balance sheet and breadth against focus and economics.'))
    A(heading('The non-bank encroachers', 2))
    A(make_table(['Threat','What is happening','JPMorgan\'s response'],
        [['<b>Private credit</b> — Apollo, Ares, Blackstone, HPS','Direct lending funds now finance buyouts banks used to. The asset class reached roughly $3tn globally entering 2025 and is forecast toward $5tn by 2029. They offer speed, certainty and lighter regulation.','JPMorgan committed <b>$50bn</b> to its own direct lending platform in 2025, plus $15bn from co-lenders — joining rather than resisting. Management named "subscription finance" and acquisition finance as 2026 growth drivers.'],
         ['<b>Payments fintech</b> — Stripe, Adyen','Better technology and developer experience in merchant acquiring, particularly for e-commerce.','Scale, global reach and the ability to hold the client\'s actual bank account. Payments revenue still grew 7% to $19.3bn.'],
         ['<b>Digital retail banks</b> — Revolut, Monzo, Starling','Winning UK current accounts on user experience.','Chase UK is JPMorgan\'s direct answer — and it competes as a challenger, not an incumbent.'],
        ], widths=[0.95,2.2,2.1]))

    A(heading('4.4  An honest assessment', 1))
    A(heading('Where JPMorgan genuinely stands out', 2))
    A(Paragraph('<b>Breadth without obvious weakness.</b> Most banks are strong somewhere and mediocre elsewhere. JPMorgan is top-three '
        'in essentially every wholesale product and #1 in the aggregate fee wallet.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Funding.</b> $2.56tn of deposits, a large slice of it costing nothing. No private credit fund, no fintech and no '
        'boutique has anything comparable.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Consistency of returns.</b> ROTCE above 17% in most years and above the cost of equity in bad ones. Management '
        'showed at the 2026 Company Update that its ability to earn above its cost of equity is, in their words, "unrivalled by peers".', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Countercyclical capacity.</b> The ability to buy distressed institutions during panics is worth more than any '
        'single year\'s earnings.', S['bullet'], bulletText='•'))
    A(heading('Where it is exposed', 2))
    A(make_table(['Exposure','The concern','Evidence in the numbers'],
        [['Interest rates','Roughly half of revenue is spread income; falling rates compress it directly.','NIM fell 2.63% to 2.50% in 2025. 2026 guidance assumes an ~$2bn rate headwind on 83bp lower average rates.'],
         ['Consumer credit','CCB is 41% of revenue and the first place a recession appears.','Card net charge-off rate rose from 3.14% (Q4 25) to 3.34% (Q2 26). Firm charge-off rate rose 0.52% → 0.68% → 0.74% over three years.'],
         ['Private credit','Lending is migrating to funds that are cheaper to run and less regulated.','$50bn committed to its own direct lending platform — a defensive move by definition.'],
         ['Markets concentration','Recent results lean heavily on trading, the least predictable revenue.','Equity Markets +33% in 2025 and +86% in Q2 2026, much of it Prime. Trading assets grew $637.8bn → $802.9bn.'],
         ['Capital and regulation','Larger balance sheet, more capital required; rules can change abruptly.','CET1 fell 15.7% → 14.6%; RWAs rose; the Advanced approach became the binding constraint at end-2025.'],
         ['Succession','One individual has defined the firm for two decades.','June 2026 clarified the field but set no timetable. Marianne Lake\'s departure removed a long-assumed successor.'],
         ['Size itself','Growth is arithmetically harder from a $57bn base.','2026 expense guidance of ~$105bn is up ~9%, faster than most plausible revenue growth.'],
        ], widths=[0.85,1.6,2.4], small=True))
    A(heading('Bull and bear cases over five years', 2))
    A(make_table(['','Bull case','Bear case'],
        [['<b>Rates</b>','Rates settle at a level historically normal rather than near zero; spread income stays structurally higher than the 2010s.','Rates fall further and faster than the forward curve implies; the post-2022 windfall unwinds.'],
         ['<b>Share</b>','Scale and technology spending keep taking share; competitors retrench; the fee wallet consolidates further.','Private credit takes the profitable lending; fintech takes payments margin; the bank keeps only the regulated, low-return residue.'],
         ['<b>Credit</b>','Consumer credit normalises without a recession; reserves prove conservative.','Unemployment rises; card losses accelerate from an already-rising base; CCB profit halves.'],
         ['<b>Technology</b>','AI delivers real efficiency — the firm has already identified ~$600m of savings — and JPMorgan\'s data scale becomes a durable moat.','$19.8bn a year buys parity, not advantage; expense growth outpaces revenue and the overhead ratio drifts up.'],
         ['<b>Leadership</b>','An orderly handover to a proven internal successor; the model outlasts the individual.','A disorderly transition, or a successor who changes a strategy that was working.'],
        ], widths=[0.55,2.2,2.2]))
    A(callout('The balanced judgement',
        'JPMorgan is the best-run large bank in the world by most measurable standards, and it is priced accordingly — a market '
        'capitalisation of $869bn at end-2025, up 78% in two years. The realistic risk is not that it fails; the fortress makes that '
        'improbable. The realistic risk is that it becomes a very good, very large, slower-growing utility whose returns drift from 20% '
        'toward the 17% through-the-cycle target and stay there — which is, notably, exactly what management itself is guiding toward.', 'info'))
    return F
