# -*- coding: utf-8 -*-
from pdfbuild import *

def build():
    F=[]; A=F.append
    A(heading('Part 1 — Foundations: what a bank actually is', 0))
    A(Paragraph('Read this part even if you are tempted to skip it. Everything in Parts 3 to 5 depends on it.', S['h1sub']))

    A(heading('1.1  The two ways a bank makes money', 1))
    A(P('A bank is not one business. It is two quite different money-making machines bolted together, '
        'and almost every confusing thing about banking becomes clear once you can tell them apart.'))
    A(heading('The first machine: net interest income', 2))
    A(P('A <b>deposit</b> is money you hand to a bank for safekeeping. Legally it is a loan from you to the bank — '
        'which is why the bank can turn round and lend it to somebody else. A <b>loan</b> is money the bank hands out '
        'and expects back with interest.'))
    A(P('The bank pays you a low rate on your deposit and charges a borrower a high rate on their loan. The difference '
        'is the profit. That difference, added up across the whole balance sheet, is <b>net interest income</b> (NII) — '
        'interest earned minus interest paid. Bankers call it "spread" revenue.'))
    A(P('The efficiency of this machine is measured by the <b>net interest margin</b> (NIM): net interest income divided by '
        'the assets that earn interest, expressed as a percentage. It answers "for every £100 of loans and securities we hold, '
        'how many pounds of interest profit do we keep?"'))
    A(callout('The numbers, for JPMorgan, FY2025',
        'JPMorgan earned <b>$95.9bn</b> of net interest income in 2025. Its interest-earning assets yielded <b>5.05%</b> on average '
        'while its interest-bearing liabilities cost <b>3.09%</b> — a spread of 1.96 percentage points. Net interest margin was '
        '<b>2.50%</b>, down from 2.63% in 2024. Strip out the trading business, where huge low-margin balances distort the picture, '
        'and the margin on the real banking book was <b>3.75%</b>. <i>Source: 4Q25 earnings supplement, page 6.</i>', 'key'))
    A(P('Two things drive this machine, and you should be able to say both out loud in an interview.'))
    A(Paragraph('<b>Volume.</b> More deposits and more loans mean more spread, even at an unchanged margin. This is why banks '
        'fight so hard for current-account customers who never move.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Interest rates.</b> When central banks raise rates, the rate a bank charges borrowers reprices upward '
        'fast, while the rate it pays depositors reprices slowly — most current accounts pay nothing however high rates go. '
        'The gap widens and NII surges. When rates fall, the same mechanism runs in reverse.', S['bullet'], bulletText='•'))
    A(P('This is the single most important thing to understand about bank earnings between 2022 and 2026. The rate-rise cycle '
        'handed banks an enormous, largely unearned windfall. JPMorgan\'s guidance for 2026 assumes roughly <b>83 basis points</b> '
        'of lower average central-bank deposit rates year on year, producing a <b>$2bn headwind</b> to net interest income which '
        'the firm expects to more than offset with balance-sheet growth. A basis point is one hundredth of one percent.'))
    A(P('The other thing about lending: some borrowers do not pay you back. Banks set aside money in advance for this, called '
        'a <b>provision for credit losses</b>. Loans actually written off are <b>net charge-offs</b>. In 2025 JPMorgan took '
        '$14.2bn of provisions and charged off $9.8bn — a charge-off rate of 0.74% of loans. Credit costs are the tax that '
        'spread revenue pays, and they arrive exactly when the economy turns.'))

    A(heading('The second machine: fee and non-interest income', 2))
    A(P('The other machine does not require the bank to lend anybody anything. It charges for services. This is '
        '<b>non-interest revenue</b>, and it comes in five broad flavours.'))
    A(make_table(
        ['Type of fee','What the client is paying for','How it behaves','JPM FY2025'],
        [['Advisory fees','Advice on buying or selling a company','Lumpy; paid only on completion','Part of $9.6bn IB fees'],
         ['Underwriting fees','Raising money via shares or bonds; the bank guarantees the proceeds','Cyclical; dies in a downturn','Part of $9.6bn IB fees'],
         ['Trading revenue','Buying and selling securities for clients, capturing the spread','Volatile, but volatility helps it','$27.2bn principal transactions'],
         ['Asset management fees','Managing money — a percentage of assets each year','Beautifully recurring; tracks markets','$20.3bn'],
         ['Payment and card fees','Moving money, processing card transactions, custody','Utility-like; extremely sticky','$9.1bn lending/deposit fees + $4.7bn card income'],
        ], widths=[1.15,2.3,1.6,1.1]))
    A(Paragraph('Fee revenue lines, FY2025 reported basis. Source: 4Q25 earnings release financial supplement, page 4. '
        '"Principal transactions" is the accounting line that captures most trading revenue.', S['cap']))

    A(heading('Why the mix matters enormously', 2))
    A(P('Investors pay more for a pound of fee income than a pound of spread income, and the reason is worth internalising.'))
    A(Paragraph('<b>Spread income consumes capital.</b> To earn it you must hold a loan on your balance sheet, and regulators '
        'force you to hold shareholders\' money against that loan in case it goes bad. Fee income from advising on a merger '
        'consumes almost none.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Spread income is not really yours.</b> It is substantially a bet on interest rates set by a central bank. '
        'A bank whose profits doubled because the Federal Reserve raised rates has not become twice as good at banking.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Fee income can be recurring or violently cyclical, and the two are not alike.</b> Asset management fees '
        'arrive every year. Underwriting fees can fall 50% in a bad year. Lumping them together as "fees" hides more than it reveals.', S['bullet'], bulletText='•'))
    A(figure('f01_nii_fee','Figure 1. JPMorgan sits almost exactly on the 50/50 line between the two machines. Very few banks '
        'anywhere are this balanced, and the balance is deliberate. Source: 4Q25 earnings supplement (managed basis), FY2025.'))

    A(heading('1.2  What a "universal bank" is, and why JPMorgan is one', 1))
    A(P('A <b>universal bank</b> does all of it: takes deposits from the public, lends to households and companies, advises on '
        'takeovers, trades securities, processes payments, and manages investments. JPMorgan is the most complete example in the world.'))
    A(make_table(['Model','What it does','What it does not do','Examples'],
        [['Pure investment bank','Advises companies, underwrites securities, trades markets','No mass retail deposits, so funding is bought in wholesale markets',
          'Historically Goldman Sachs and Morgan Stanley; both now bank holding companies with growing deposit bases'],
         ['Pure commercial bank','Takes deposits, makes loans, runs branches and payments','Little or no advisory or trading','Lloyds, NatWest; largely Wells Fargo'],
         ['Pure asset manager','Invests other people\'s money for a fee','Holds no meaningful balance-sheet risk of its own','BlackRock, Schroders'],
         ['Universal bank','All of the above under one roof','—','JPMorgan, HSBC, Citigroup, BNP Paribas, Barclays'],
        ], widths=[0.9,1.7,1.6,1.5]))
    A(heading('Why the combination is a genuine advantage', 2))
    A(P('Three real reasons, not marketing ones.'))
    A(Paragraph('<b>Cheap, stable funding.</b> Retail and corporate deposits are the cheapest money in finance. JPMorgan held '
        '$2.56tn of deposits at end-2025, of which roughly $604bn on average paid <i>no interest at all</i>. A pure investment bank '
        'has to borrow in markets that slam shut in a crisis. This is not a small edge; it is the difference between surviving 2008 '
        'and not.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Cross-selling that is structurally real.</b> A company that borrows from you needs to hedge, to make payments, '
        'and eventually to buy something. Section 3.8 traces a single transaction through six teams.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Diversification of the cycle.</b> Trading thrives on volatility; advisory thrives on calm confidence; lending '
        'thrives on growth. Owning all three smooths earnings — 2025 is a textbook illustration, with Markets revenue up 19% while '
        'investment banking fees were soft.', S['bullet'], bulletText='•'))
    A(heading('And why it is a regulatory headache', 2))
    A(P('Governments dislike institutions that combine insured retail deposits with trading risk, because the state ends up '
        'underwriting the gamble. Three consequences shape JPMorgan\'s daily life:'))
    A(Paragraph('<b>Systemic capital surcharges.</b> The biggest banks must hold extra capital purely for being big and '
        'interconnected. Size is taxed.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>The Volcker Rule</b> (US, from the 2010 Dodd-Frank Act) bans banks from most speculative trading with '
        'their own money. See section 1.5 for what this actually changed.', S['bullet'], bulletText='•'))
    A(Paragraph('<b>Structural separation.</b> The UK\'s <b>ring-fencing</b> regime forces a large retail bank into a separate, '
        'separately capitalised legal entity walled off from investment banking. This is live and directly relevant to Chase UK — '
        'see sections 2.4 and 3.2.', S['bullet'], bulletText='•'))

    A(heading('1.3  The balance sheet, and the five ratios that matter', 1))
    A(P('A balance sheet has two sides that must equal each other. <b>Assets</b> are what the bank owns and is owed: loans, bonds, '
        'trading positions, cash. <b>Liabilities</b> are what it owes: deposits, borrowings. What is left over belongs to shareholders '
        'and is called <b>equity</b>, or capital.'))
    A(figure('f13_balancesheet','Figure 2. Deposits are the foundation of everything. Note how thin the equity layer is: $362bn of '
        'equity supports $4,425bn of assets. Source: FY2025 Form 10-K, 31 December 2025.'))
    A(P('That thinness is the entire point of banking and the entire reason regulators exist. If a bank funds itself with 8% equity '
        'and 92% borrowed money, then a loss of just 8% of its assets wipes out the shareholders completely. That amplification is '
        '<b>leverage</b>. It magnifies returns in good years and kills the institution in bad ones.'))
    A(P('Five terms will appear constantly. Learn them now.'))
    A(make_table(['Term','What it means in plain English','JPM at end-2025'],
        [['<b>RWA</b> — risk-weighted assets','Assets re-counted according to how dangerous they are. A government bond might count for almost nothing; a loan to a struggling company counts at full value or more. It is the denominator regulators care about.','$1,984bn (Standardized)'],
         ['<b>CET1 ratio</b>','Common Equity Tier 1 capital — the purest shareholder money — divided by RWAs. The headline measure of whether a bank can absorb losses. Regulators set a minimum; banks hold a buffer above it.','14.6% (Standardized)'],
         ['<b>LCR</b> — liquidity coverage ratio','Whether the bank holds enough instantly-sellable assets to survive 30 days of a run. Solvency and liquidity are different: banks usually die of the second.','111% (must exceed 100%)'],
         ['<b>Provisions / charge-offs</b>','Money set aside for loans expected to go bad, and loans actually written off.','$14.2bn / $9.8bn'],
         ['<b>ROTCE</b>','Return on tangible common equity. See below — this is the number.','20%'],
        ], widths=[1.05,3.1,0.95]))
    A(heading('ROTCE, properly explained', 2))
    A(P('Return on equity asks: for every pound shareholders have in this bank, how much profit does it make in a year? '
        '<b>Return on tangible common equity</b> asks the same question but first strips out <b>goodwill and intangibles</b> — '
        'the accounting entry created when a bank pays more for an acquisition than the acquired assets are worth on paper. '
        'Goodwill cannot absorb a loss. Removing it gives a harder, more honest denominator, which is why it is the standard.'))
    A(P('JPMorgan reported <b>20% ROTCE for 2025</b> (17% ROE). Its stated <b>through-the-cycle target is 17%</b>, and management '
        'was asked at the February 2026 Company Update whether that target should be raised, given performance has been above it. '
        'They said no, and the reasoning is the most useful thing a candidate can quote:'))
    A(callout('Jeremy Barnum, Chief Financial Officer, 2026 Company Update, 23 February 2026',
        '"ROTCE is an output, not an input. What we mean by that is that we do not make decisions in order to achieve a particular '
        'outcome on ROTCE. Our focus is on growing long-term shareholder value, which we believe is best approximated by our ability '
        'to deploy capital at returns in excess of our cost of equity."<br/><br/>'
        'The practical implication: JPMorgan will deliberately deploy capital into businesses returning <i>less</i> than 17%, so long '
        'as they beat the cost of equity, because that adds absolute economic profit even while diluting the percentage. If you say '
        'this in an interview you will be ahead of most candidates, who assume the firm is maximising a ratio.', 'key'))

    A(heading('1.4  Core investment banking concepts', 1))
    A(P('"Investment banking" in the narrow sense means helping companies do two things: buy and sell other companies, and raise money.'))
    A(heading('M&A advisory', 2))
    A(P('<b>Mergers and acquisitions</b> advisory means advising a company that is buying, selling or defending itself. The bank '
        'builds a valuation, advises on price and structure, manages the negotiation and the process. It is paid a <b>success fee</b>, '
        'typically a percentage of deal value, and typically <i>only if the deal completes</i>. This is pure intellectual-property '
        'revenue: it consumes essentially no capital, which is why it carries such prestige internally and why the returns are so high '
        'when volumes are good.'))
    A(heading('Capital markets: ECM and DCM', 2))
    A(P('<b>Equity capital markets</b> (ECM) raises money by selling shares — a company\'s first sale is an <b>IPO</b>, or initial '
        'public offering. <b>Debt capital markets</b> (DCM) raises money by selling bonds, which are tradeable IOUs paying interest.'))
    A(P('Both involve <b>underwriting</b>, and this is the concept people get wrong. Underwriting does not mean "selling". It means '
        'the bank <i>guarantees</i> the company will receive the money, and then takes the risk of placing the securities with investors. '
        'If demand collapses between pricing and settlement, the bank owns the stock. The fee — usually a percentage of the amount raised — '
        'is payment for absorbing that risk, not for the paperwork.'))
    A(P('<b>Leveraged finance</b> is the specialist end of DCM: arranging debt for companies that are already heavily indebted, most '
        'often to fund a private-equity buyout. Higher risk, materially higher fees. JPMorgan disclosed in 4Q25 that part of its credit '
        'provision came from "an update to loss assumptions on certain leveraged loans" — a reminder that the risk is real.'))
    A(heading('League tables, sponsors and coverage', 2))
    A(P('A <b>league table</b> ranks banks by deal volume or fees earned over a period. They matter more than they should: they are '
        'the industry\'s scoreboard, they are used in pitches, and bankers are measured against them. JPMorgan ranked <b>#1 for global '
        'investment banking fees in 2025 with an 8.4% share of the total fee pool</b>, and 9.3% year-to-date at the half-year 2026.'))
    A(P('<b>Sponsors</b> means private equity firms — funds that buy companies using large amounts of borrowed money, improve them, and '
        'sell them on. They are the most valuable client group in the industry because a single sponsor generates acquisition advisory, '
        'debt underwriting, later refinancing, and eventually an exit. Banks run dedicated <b>sponsor coverage</b> teams for this reason.'))
    A(P('<b>Coverage</b> is how banks organise client relationships: by <b>industry</b> (Healthcare, Technology, Consumer &amp; Retail, '
        'Financial Institutions, Real Estate), by <b>country</b>, or by <b>product</b>. The 2027 London investment banking posting names '
        'exactly these groups, which tells you the structure is real and current.'))

    A(heading('1.5  Core markets concepts', 1))
    A(P('"Markets" is the trading business. It is the part outsiders understand worst, largely because films have taught everyone '
        'the wrong model.'))
    A(heading('Sales versus trading', 2))
    A(P('<b>Sales</b> people cover investing institutions — pension funds, hedge funds, insurers, asset managers. They bring those '
        'clients ideas and take their orders. <b>Traders</b> price the risk and manage the resulting position. <b>Structurers</b> design '
        'bespoke instruments for clients with an unusual problem. They sit metres apart and are usually on the same desk.'))
    A(heading('Market making, and how a desk actually earns money', 2))
    A(P('A <b>market maker</b> quotes two prices continuously: the price at which it will buy (the <b>bid</b>) and the price at which '
        'it will sell (the <b>offer</b> or ask). The gap is the <b>bid-ask spread</b>, and that gap is the fee for providing '
        '<b>liquidity</b> — the service of being willing to trade when the client wants to, rather than when it happens to be convenient.'))
    A(P('This is the crucial distinction. <b>Proprietary trading</b> means betting the bank\'s own money on a market direction. '
        'The Volcker Rule largely banned it for US banks after 2010. Market making is different in kind: the desk is not trying to '
        'predict the market, it is trying to earn the spread many thousands of times while hedging the risk it accumulates in between.'))
    A(callout('So how does a modern trading desk make money?',
        'Chiefly four ways. <b>(1) Bid-ask spread</b> — earned in tiny amounts on enormous volume. <b>(2) Financing</b> — lending '
        'money and securities to clients, especially hedge funds, and charging for it. <b>(3) Structuring</b> — designing a bespoke '
        'derivative and charging a margin for the complexity. <b>(4) Residual risk</b> — a desk that has bought from a client holds '
        'the position for minutes or days before offsetting it, and is paid for warehousing that risk.<br/><br/>'
        'The phrase <b>"client franchise"</b> means the recurring flow of client business that generates all four. It is the asset. '
        'A desk with a strong franchise sees more orders, which means better information about supply and demand, which means it can '
        'quote tighter prices, which attracts more orders. Scale compounds. This is precisely why JPMorgan\'s Markets business is '
        'structurally hard to dislodge.', 'key'))
    A(heading('The vocabulary you will be expected to know', 2))
    A(make_table(['Term','Plain English'],
        [['Cash vs derivatives','"Cash" means trading the actual thing — a share, a bond. A "derivative" is a contract whose value is derived from something else, used to hedge or to take exposure without owning the underlying asset.'],
         ['Flow vs structured','"Flow" is high-volume standardised business earning thin margins. "Structured" is bespoke, complex and higher-margin.'],
         ['Prime brokerage','The bundle of services sold to hedge funds: lending them money to trade with (leverage), lending them shares to sell short, holding their assets, clearing their trades. Balance-sheet heavy, highly profitable, and the single largest driver of JPMorgan\'s 40% jump in Equity Markets revenue in 4Q25.'],
         ['Delta One','Desks trading instruments that move one-for-one with an underlying index — ETFs, swaps, futures. Systematic, technology-intensive.'],
         ['Securitised products','Loans (mortgages, car loans, credit-card receivables) bundled into tradeable bonds.'],
         ['Emerging markets','Trading in the currencies and debt of developing economies. Higher margin, higher risk.'],
        ], widths=[0.75,3.4]))
    return F
