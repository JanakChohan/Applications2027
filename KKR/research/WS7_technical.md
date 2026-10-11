# WS7: The technical content of a KCS seat at KKR

Workstream 7. Source range S420 to S489. Researched 2026-10-11.
Scope: the mechanical, product-level detail a KKR Global Client Solutions (KCS) intern would learn. WS1 already covers the KCS organisation, leadership, channels, K-Series AUM history and the Capital Group headline facts. This file avoids repeating those and goes one level deeper: what is inside each product, how the money moves, and the toolkit clients use to judge KKR.

Confidence tags: [Confirmed] = primary document read in full or two credible outlets. [Reported] = one credible source, or a search snippet of a primary source I could not open. [Inferred] = my own reasoning or arithmetic.

---

## 1. Findings

### 1.1 The K-Series: what the funds' own SEC filings say

The K-Series is KKR's family of "evergreen" (no end date) funds for individuals. WS1 gives the AUM history ($34bn at 31 Dec 2025, $42bn at 30 Jun 2026). Below is what sits inside four of them, from their own filings.

#### 1.1.1 K-PEC (KKR Private Equity Conglomerate LLC): the private equity vehicle

**Legal form.** A Delaware limited liability company formed on 6 December 2022. It began principal operations on 1 August 2023. It is a "holding company that seeks to acquire, own and control portfolio companies ... through Joint Ventures." [S420, Confirmed]

**Why "conglomerate" and not a "fund".** This is the single most technical idea in the K-Series. K-PEC is built so that it is NOT an "investment company" under the US Investment Company Act of 1940. If it were, the 1940 Act would restrict its leverage, its dealings with KKR affiliates and its fee structure, and it could not operate as planned. The 10-K explains the two legal tests [S420, Confirmed]:
- Section 3(a)(1)(A): a company is an investment company if it is "engaged primarily ... in the business of investing, reinvesting or trading in securities." K-PEC says it is not, because "through its Joint Ventures, the Company is primarily engaged in the businesses of its Joint Ventures, namely, the business of owning and controlling portfolio companies."
- Section 3(a)(1)(C), the "40% test": a company is an investment company if "investment securities" exceed 40% of its total assets (excluding government securities and cash). K-PEC's main asset is its stake in wholly owned "Operating Subsidiaries" (for example K-PEC Holdings LLC). Those subsidiaries hold *general partner* interests in each Joint Venture, and "such general partner interests are not 'investment securities'." So the only investment securities are in the liquidity sleeve, which K-PEC keeps below 40%.
- In plain English: K-PEC is legally an operating business that controls companies, like an old-style industrial conglomerate, not a fund that holds securities. That is why it can be an LLC that files 10-Ks like a normal company. [Inferred from S420]
- The structure has teeth. If the Management Agreement with KKR is terminated, K-PEC must "forfeit our controlling interest in any Joint Venture, which would likely require us to register as an investment company." [S420, Confirmed]

**How it holds assets alongside KKR's flagship funds.** K-PEC "expect[s] that we will own nearly all of our portfolio companies through Joint Ventures alongside one or more KKR Vehicles." K-PEC and the KKR flagship fund (for example North America Fund XIII or XIV) are "co-general partners" of each deal-level Joint Venture, with economic shares that "vary from acquisition to acquisition." [S420, Confirmed]
- Target mix: about 80% of assets in portfolio companies, up to 20% in a "Liquidity Portfolio" (cash, Treasuries, investment-grade and high-yield credit, CLOs, leveraged loans). No more than 5% in "blind pools" and no more than 10% in listed equities. No cryptocurrency. [S420, Confirmed]
- Sectors: Business & Financial Services; Consumer & Retail; Healthcare; Impact; Industrials; Technology, Media & Telecommunications. Strategies it can co-invest with: traditional PE, middle market, core equity, growth equity, Global Impact. [S420, Confirmed]
- Allocation rule (important for understanding conflicts): "the Company does not benefit from any mandatory minimum purchase rights or minimum purchase thresholds. As such the Company will not benefit from any priority acquisition allocation." Flagship funds have a mandatory minimum that is filled first. K-PEC is offered the "first tier" alongside nearly all KKR vehicles "up to a capped amount", and then may be offered part of any "second tier." [S420, Confirmed] This means institutional flagship LPs get first call on deals, and the wealth vehicle fills in behind them. [Inferred]
- K-PEC also bought stakes in two companies in 2025 ($165.5m) "from affiliated KKR-sponsored investment vehicles alongside the relevant flagship private equity vehicle as part of a sale and purchase between successive fund vintages." [S420, Confirmed] This is the "continuation" style transfer that ILPA DDQ section 6 asks about. [Inferred]

**Share classes and selling fees.** Investor classes on offer at 31 Dec 2025: S, D, U and I. Early-bird classes R-S, R-D, R-U and R-I "were available for purchase only during the 18-month period following August 1, 2023" and closed on 2 January 2025. KKR holds classes E, F, G, H ("KKR Shares"). [S420, Confirmed]
- Class S: sales load up to 3.00% plus dealer-manager fee 0.50% (total capped at 3.50%).
- Ongoing fees paid to KKR Capital Markets LLC (as dealer-manager): 0.85% of NAV a year for S and U (0.60% distribution plus 0.25% servicing); 0.25% for D; none for I. [S420, Confirmed]
- Translation for a beginner: Class S is sold through brokers who take a commission; Class D through fee-based advisers; Class I through institutional or advisory accounts with no trail; Class U is a platform-specific variant. [Inferred, labels follow industry convention; K-PEC's 10-K does not define the intended channel per class]

**Fees to KKR.**
- Management fee: 1.25% a year of month-end NAV for S, D, U and I. For the R classes, 1.00% for 60 months from 1 August 2023, then 1.25%. Payable monthly; KKR may take it in Class F shares instead of cash. [S420, Confirmed]
- Fee offset: the management fee is reduced, not below zero, by transaction, monitoring and break-up fees ("Other Fees") allocable to investors. [S420, Confirmed]
- Performance Participation Allocation (the evergreen version of carried interest): "15.0% of the Total Return attributable to Investor Shares, subject to a 5.0% Hurdle Amount and a High Water Mark, with a 100% Catch-Up." Measured and paid annually, accrued monthly. [S420, Confirmed]
- How the waterfall works: first, any return above the 5% hurdle plus any "Loss Carryforward Amount" goes 100% to KKR until KKR has 15% of the total; after that, 15% to KKR and 85% to investors. [S420, Confirmed; plain-English gloss Inferred]
- Alignment rule: since 1 July 2025 KKR may only ask to cash in Class F shares received as performance fee at the earlier of five years from issue or a stated later event. [S420, Confirmed, sentence truncated in my extract]
- Termination fee if K-PEC fires the manager without cause: three times the average annual management fee plus average annual performance allocation over the prior 24 months. [S420, Confirmed]

**NAV and dealing.**
- Subscriptions: "a continuous private offering of our Shares on a monthly basis" to US accredited investors (Regulation D) and non-US persons (Regulation S). [S420, Confirmed]
- Price: the "Transactional Net Asset Value" per share at the end of the prior month. An investor subscribes a dollar amount and only learns the share count afterwards; for example a subscription accepted on 1 September is priced at the 31 August NAV. [S420, Confirmed]
- Valuation: the Manager "determines the NAV of our Shares monthly"; an Administrator computes the per-share figure. All portfolio companies are Level III (no market price). A 10% fall in their fair value would cut net assets by $898.6m. [S420, Confirmed]
- Transactional NAV differs from GAAP NAV mainly because GAAP books the lifetime cost of distribution fees up front: GAAP NAV $9.495bn vs Transactional NAV $9.932bn at 31 Dec 2025. [S420, Confirmed]

**Liquidity (the repurchase plan).**
- Quarterly. Total repurchases capped at "no more than 5.0% of our aggregate NAV ... per calendar quarter." The Board can repurchase less or nothing. [S420, Confirmed]
- Early Repurchase Fee: 5.0% of NAV if shares are redeemed within 24 months of issue; retained by the fund for remaining holders; may be waived for death, disability or divorce. [S420, Confirmed]
- Overflow: if requests exceed 5%, the Board may run a tender for "Excess Shares" at "at or about a 10% discount to the most recent NAV." [S420, Confirmed] This is an unusual feature: a paid exit valve above the gate. [Inferred]
- Minimum remaining balance after a partial repurchase: $1,000. [S420, Confirmed]
- Actual 2025 repurchases: about $26.4m net of early repurchase fees (cash flow statement), against $9.9bn NAV, roughly 0.3% for the year. [S420 Confirmed for the $26.4m; ratio Inferred]

**Leverage.** Recourse borrowing at the K-PEC level is capped at 30% of total assets (excluding short-term bridge borrowing); there is no cap on non-recourse debt inside portfolio companies. A third-party revolving facility was upsized to $1.0bn in March 2026 (accordion to $1.5bn; matures 23 Dec 2027). A KKR-affiliate line of credit charges up to SOFR plus 3.50%. KKR Capital Markets earned $2.0m of arranger fees on the revolver in Q4 2025. [S420, Confirmed]

**Size and performance at 31 Dec 2025** [S420, Confirmed]:
- Transactional NAV $9.93bn; 296.9m shares; Class I NAV per share $33.80.
- 2025 subscriptions $4.18bn, used partly to buy interests in 27 portfolio companies plus add-ons, total $3.85bn.
- Unfunded commitments to portfolio companies $154.2m.
- 2025 total return: Class I 16.81%, Class D 14.80%, Class U 15.78%, Class R-I 16.79%. Inception-to-date annualised: Class I 12.94% (since Sept 2023), R-I 13.22% (since Aug 2023). No distributions have ever been paid.
- K-PEC had 7.9m D, 62.9m I, 0.7m S, 73.9m U, 11.3m R-D, 60.3m R-I and 102.5m R-U shares on 20 Mar 2026. The early R-U class is the largest. [S420, Confirmed]

#### 1.1.2 K-INFRA (KKR Infrastructure Conglomerate LLC)

Same "conglomerate" design, adapted for infrastructure [S421, Confirmed]:
- Delaware LLC formed 23 September 2022. Owns "Infrastructure Assets" through Joint Ventures with KKR vehicles: Global Infrastructure Investors II to V, Asia Pacific Infrastructure Investors I to III, the Diversified Core Infrastructure Fund and the Global Climate Fund.
- Target mix: about 85% Infrastructure Assets (no more than 15% in non-OECD countries) and about 15% Liquidity Portfolio.
- Classes on offer: S, D and I. Closed early classes: U, R-D, R-S, R.
- Management fee: 1.25% of month-end NAV (D, I, S); 1.00% for 60 months from 1 June 2023 for early classes bought via an intermediary aggregate subscription of at least $100,000 in the first 12 months.
- Performance Participation Allocation: 12.5% of Total Return over a 5.0% hurdle, high-water mark, 100% catch-up. That is lower than K-PEC's 15%, matching the lower expected return of infrastructure. [S421 Confirmed; interpretation Inferred]
- Repurchases: quarterly, capped at 5% of NAV; 5.0% early repurchase fee within 24 months.
- Distributions: monthly declared from July to December 2023, then quarterly from January 2024. The 10-K warns distributions "may and are expected to exceed our earnings and cash flow from operating activities" and may be paid from borrowings or offering proceeds.
- Leverage: recourse borrowing capped at 30% of total assets; may exceed this in ramp-up, downturns or large deals.
- Size at 31 Dec 2025: Transactional NAV $6.47bn; 215.9m shares; $980m cash. 2025 subscriptions $2.84bn, used to buy more of existing assets, with unused money in money market assets.
- 2025 total return: Class I 10.13% (inception-to-date 10.06% annualised); Class S 9.15%; Class R 10.17%.
- Warehousing: KKR or a bank warehouse may buy an asset first and later sell it to K-INFRA (or K-INFRA may syndicate a "Warehoused Asset" to others) "at cost, or cost plus an interest rate or carrying cost", even if fair value has moved. The 10-K flags that conflicts here "may not be resolved in favor of the Company." [S421, Confirmed] This is the same buy-then-syndicate engine that KCS and KCM run for institutional co-investors. [Inferred]

#### 1.1.3 K-FIT and K-FITS (KKR FS Income Trust and KKR FS Income Trust Select): private credit

Different legal answer: these ARE registered under the 1940 Act framework, as Business Development Companies (BDCs). [S422, Confirmed]
- K-FIT: "an externally managed, non-diversified, closed-end management investment company that has elected to be regulated as a business development company." Formed 4 Feb 2022 as a Delaware statutory trust; operations from 25 Jul 2022; elected BDC status 31 Mar 2023. Also a RIC for tax (pays no corporate tax if it distributes income). [S422, Confirmed]
- Adviser: FS/KKR Advisor, LLC, "jointly operated by KKR Credit and by FSJV Holdco, LLC, an affiliate of Franklin Square Holdings L.P. (which does business as Future Standard, formerly FS Investments)." [S422, Confirmed]
- "Perpetual-life BDC": sold monthly at NAV; quarterly repurchase offers of "up to 5% of our Common Shares outstanding" via tender at quarter-end NAV; 2% "Early Repurchase Deduction" if tendered within 12 months; $500 minimum balance. [S422, Confirmed]
- Offering: private offering of up to $5bn of Class I shares; partly via drawdown "Capital Commitments". Sponsors seeded $35m. [S422, Confirmed]
- Portfolio rules: at least 60% of total assets in first lien senior secured loans to private US middle-market companies (EBITDA $50m to $150m); up to 30% in asset-based finance (ABF) and subordinated loans. ABF examples: auto loans, royalties, aircraft leasing, real estate development lending. A majority of ABF is "directly originated and proprietary, including through ... lending and servicing platform businesses established by KKR Credit." [S422, Confirmed]
- Fees: base fee 1.25% of average monthly net assets. Income incentive fee: nothing below a 1.25% quarterly (5.0% annualised) hurdle; 100% "catch-up" between 1.25% and 1.43% per quarter (5.72% annualised); then 12.5% of income. Capital gains incentive fee 12.5% of cumulative realised gains net of losses. [S422, Confirmed]
- Leverage: BDC asset coverage of 150% (debt up to roughly 2x equity), adopted by shareholders 25 Jul 2022. [S422 Confirmed; "2x" Inferred]
- Size at 31 Dec 2025: investments at fair value $2.63bn; total assets $2.75bn; shareholders' equity $1.54bn; NAV per share $29.75. [S422, Confirmed]
- K-FITS (the "Select" sibling, Class S shares): shareholders' equity $1.006bn at 30 Jun 2026; base fee 1.25% (waived through 30 Sep 2025); same 5% quarterly tender approach. [S423, Confirmed]
- Observation: the private credit K-Series vehicles are small (about $2.5bn equity combined) next to K-PEC ($9.9bn) and K-INFRA ($6.5bn). That fits Nuttall's statement in WS1 that "roughly 85% of K Series is in private equity and infrastructure." [Inferred from S420 to S423]

#### 1.1.4 KREST (KKR Real Estate Select Trust Inc.): real estate

A third legal answer: a *registered* closed-end fund under the 1940 Act (the N-2 cover ticks "Registered Closed-End Fund", not "Interval Fund"). [S424, Confirmed]
- Invests at least 80% of net assets in real estate (property, debt, and some listed real estate securities). Adviser: KKR Registered Advisor LLC. Distributor: KKR Capital Markets LLC. [S424, Confirmed]
- Classes S, D, U, I. Minimum initial investment $10,000 for S, D and U; $1,000,000 for I; $500 subsequent. [S424, Confirmed] This is the only K-Series vehicle where I found a published minimum.
- Fees: management fee 1.25% of average daily net assets; incentive fee 12.5% of quarterly "Portfolio Operating Income" (net operating income plus net investment income less expenses). KREST charges no incentive fee on capital gains. [S424, Confirmed]
- Selling: Class S up to 3.0% sales load plus 0.5% dealer-manager fee (total cap 3.5%); 0.85% annual distribution plus servicing for S and U; 0.25% for D. [S424, Confirmed]
- Liquidity: "intends, but is not obligated, to conduct quarterly tender offers for up to 5.0% of the aggregate NAV"; the N-2 admits repurchases "have in the past been and may in the future be oversubscribed." [S424, Confirmed]
- Leverage: 1940 Act limit of 33 1/3% on fund-level borrowing, with property-level mortgages outside that limit; preferred stock up to 50% of total assets. [S424, Confirmed]
- Alignment: the Adviser takes fees in Class I shares and owned about $255.2m of Class I at 31 Mar 2025. Expense cap: certain expenses capped at 0.50% of net assets through 30 Apr 2027. Estimated average net assets: about $1.53bn. [S424, Confirmed]

#### 1.1.5 Comparison table of the four structures

| Feature | K-PEC | K-INFRA | K-FIT | KREST |
|---|---|---|---|---|
| Legal form | Delaware LLC "conglomerate", outside 1940 Act | Delaware LLC "conglomerate", outside 1940 Act | BDC (1940 Act), RIC | Registered closed-end fund (1940 Act) |
| Investors | US accredited (Reg D) and non-US (Reg S) | Same | Private offering, Class I | Public, registered offering |
| Management fee | 1.25% of NAV | 1.25% of NAV | 1.25% of net assets | 1.25% of net assets |
| Performance fee | 15% over 5% hurdle, HWM, 100% catch-up | 12.5% over 5% hurdle, HWM, 100% catch-up | 12.5% of income over 5% annual hurdle (catch-up to 5.72%) plus 12.5% of realised gains | 12.5% of operating income, none on gains |
| Liquidity | Quarterly, 5% of NAV cap; 5% fee within 24 months; overflow tender at about 10% discount | Quarterly, 5% cap; 5% fee within 24 months | Quarterly tender up to 5%; 2% within 12 months | Quarterly tender up to 5%, discretionary |
| NAV | Monthly | Monthly | Monthly | Daily accrual of fees; NAV-based pricing |
| Fund-level leverage cap | 30% recourse | 30% recourse | 150% asset coverage | 33 1/3% borrowing |
| Size (latest) | $9.93bn (Dec 2025) | $6.47bn (Dec 2025) | $1.54bn equity (Dec 2025) | about $1.53bn (est.) |
Sources: S420, S421, S422, S424 [Confirmed]

#### 1.1.6 K-PRIME and Europe

- K-PRIME is KKR Private Markets Equity Fund SICAV SA (Luxembourg), described in search snippets of its own documents as an open-ended Part II UCI under the 2010 Luxembourg law, supervised by the CSSF, with a feeder sub-fund ("K-PRIME Feeder-I") investing into KKR Private Markets Equity Fund (Master) FCP; inception 1 May 2023; prospectus dated 31 March 2024; an August 2024 monthly report showed inflows "of more than $2.5 billion" and NAV of about $2.78bn. [S429, Reported: the kseries.kkr.com PDFs now return 404 and the Emirates NBD copy of the KID was not text-readable, so I could not verify this from the document myself]
- WS1 already confirms from the K-PEC 10-K that K-PRIME is the non-US twin with "similar objectives and strategies".
- I found no evidence of a KKR ELTIF or a KKR UK LTAF. Competitor EQT launched an evergreen infrastructure ELTIF in April 2026 [S464, Reported]. [Gap for KKR]

### 1.2 Capital Group KKR interval funds: the mechanics

WS1 covers the partnership history. Here is the plumbing from the registration statements.

**Capital Group KKR Core Plus+** [S426, Confirmed]:
- A "non-diversified, closed-end management investment company that continuously offers its common shares and is operated as an 'interval fund.'" Delaware statutory trust organised 4 October 2024.
- Allocation: "approximately 60% of its net assets to public debt assets (to be managed by the investment adviser) and approximately 40% to private credit assets (to be managed by the sub-adviser)." Adviser: Capital Research and Management Company. Sub-adviser: KKR Credit Advisors (US) LLC. The sub-adviser "will be paid solely by the investment adviser out of the investment adviser's fees."
- Rule 23c-3 liquidity: a "fundamental policy" (only changeable by a shareholder vote) to make quarterly repurchase offers of "between 5% and 25% of its outstanding shares at net asset value". The fund "currently expects to offer to repurchase 10%." First repurchase offer expected November 2025. Oversubscribed offers are prorated.
- Contrast with K-Series: an interval fund *must* make the offer every quarter; a K-Series board *may* repurchase less or nothing. [Inferred from S420 and S426] That is the key trade-off: interval funds give firmer liquidity but must hold more liquid assets, which is why the private sleeve is only 40%. [Inferred]
- Classes A, A-2, F-2, F-3, R-6. Minimum initial investment "normally $1,000 per account"; $1m for F-3 held directly with the transfer agent; $50 to add.
- Fees: management fee 0.61% for all classes. Total annual expenses after a 0.30% waiver: A 1.27%, A-2 1.54%, F-2 0.98%, F-3 0.84%, R-6 0.84%. Front-end sales charge up to 3.75% (A) and 2.00% (A-2).
- Warehouse: a financing provider pre-bought private credit assets; once fund net assets reach $150m the fund must buy up to $2m of them, rising to $8m at $400m, and up to 2% of net assets at $500m. This is how a new fund launches with a seasoned private portfolio. [S426, Confirmed; interpretation Inferred]

**Capital Group KKR U.S. Equity+** [S427, Confirmed]:
- Also an interval fund. "approximately 60% of its net assets in publicly traded equity securities and approximately 40% of its net assets in private equity securities."
- The private 40% is "approximately 30% of its net assets in K-PEC and approximately 10% of its net assets in co-investments" alongside K-PEC or other KKR PE vehicles. It buys K-PEC units monthly like any investor, and its K-PEC stake can only be redeemed through K-PEC's 5%-per-quarter plan.
- Repurchases: quarterly offers "for 5% of its outstanding shares under ordinary circumstances."
- Management fee at the fund level: 0.350% of average daily net assets (K-PEC's own fees sit underneath on the 30% invested there). [S427 Confirmed for 0.350%; layering Inferred]
- Why this matters for KCS: this is a "fund of KKR" built by a third party. KKR's K-PEC becomes an ingredient in someone else's mass-market product, and co-investment flows from KKR deals go straight into a retail wrapper. [Inferred]

### 1.3 KKR Insights a KCS intern would actually use

#### 1.3.1 The Total Portfolio Approach (TPA): two papers

**Paper 1.** "The Total Portfolio Approach: A Practical Framework", KKR Multi-Asset Strategies, February 2026 (web page dated 26 Feb 2026; "Insights | Volume 15"); authors Henry H. McVey, David McNellis, Christian Olinger. PDF: https://www.kkr.com/content/dam/kkr/insights/pdf/kmas-feb-2026-total-portfolio-approach.pdf [S435, S462, Confirmed]
- Definition: "a whole-portfolio decision and governance framework that evaluates investment opportunities across Public and Private Markets based on their contributions to total portfolio objectives, rather than within static asset-class sleeves." [S435, Confirmed]
- Contrast with Strategic Asset Allocation (SAA). Under TPA, "The board sets a reference portfolio (for instance, 70% Public Equity/30% Fixed Income) and risk appetite ... and delegates allocation authority to the CIO within a total portfolio risk budget." Table 1 contrasts: fixed asset-class targets vs dynamic weights; many benchmarks vs "Single reference portfolio and risk budget"; diversification "Through asset classes" vs "Through risk factors". [S435, Confirmed]
- Why TPA helps private markets investors: "improved liquidity management, steadier commitment pacing, better vintage diversification, and greater flexibility through drawdowns and denominator effects." Exhibit 3 models a hypothetical 40% public equity drawdown that mechanically makes private assets look overweight (the "denominator effect"). [S435, Confirmed]
- Worked example: optimise to match the factor exposures of a "70% Equities/30% Bonds reference portfolio", allowing "up to 30% of total portfolio capital to be allocated to Private Markets" and "up to 10% total portfolio leverage." The optimised private sleeve includes categories that "don't fit cleanly into buckets, such as Capital Solutions and Reinsurance." [S435, Confirmed]
- "Minimum viable TPA": an on-ramp that "can include centralizing portfolio-level functions, strengthening in-house portfolio construction and relative-value capabilities, refreshing views more frequently, and piloting TPA through a dedicated sleeve that has clear risk and liquidity guardrails." [S435, Confirmed]

**Paper 2.** "The Dog Has Caught the Bus: The Total Portfolio Approach", Global Macro Trends, July 2026 (web page dated 29 Jul 2026); authors Henry H. McVey (Head of Global Macro & Asset Allocation, CIO of KKR's Balance Sheet), Dave McNellis (Co-Head of Global Macro and Head of Portfolio Construction and Multi-Asset Strategies for Private Markets), Christian Olinger (Director, Multi-Asset Strategies), Amy Dai (Associate, GMAA). PDF: https://www.kkr.com/content/dam/kkr/insights/pdf/2026-july-total-portfolio-approach-update.pdf [S436, Confirmed]
- Title meaning: "interest in TPA has surged dramatically ... Simply stated, the proverbial TPA 'dog has caught the bus.'" CIOs moved from "whether" to "how". [S436, Confirmed]
- The analogy KCS uses with clients: TPA as "zero-based budgeting for portfolio construction ... if every investment had to earn its place in the portfolio today, how would capital be allocated?" [S436, Confirmed]
- Five client FAQs: (1) TPA does not abandon asset allocation; it "competes with" SAA as an operating model, not with having a view; (2) TPA helps bottom-up family offices gain structure as much as it helps big institutions gain flexibility; (3) "Implementation should begin with the investment objective, not the checklist"; (4) use a parsimonious top-down risk lens plus a granular bottom-up lens; (5) private markets are the hardest frontier. [S436, Confirmed]
- Three private-markets challenges (Exhibit 5): opportunity set and relative value; risk measurement ("Investors often commit capital before knowing the exposures they will ultimately own", i.e. blind pool risk); dynamism (illiquidity). Responses: strategy-level benchmarks, public comparables, pacing and recycled distributions, "secondaries and liquidity facilities available during dislocations." [S436, Confirmed]
- Key number: "Across private market strategies, annual distributions have historically averaged approximately 10-30% of NAV." [S436, Confirmed]
- KKR links TPA to its own capital markets engine: inside KKR, portfolio-level exposure observations "inform future deployment decisions, including where to lean in and where to syndicate through co-investment." KKR's "Capital Markets capabilities, and balance sheet investment portfolio provide us with a differentiated perspective on relative value." KKR expanded its Capital Market Assumptions platform "in early 2026" with more granular private-markets assumptions. [S436, Confirmed]
- My read: TPA is the intellectual bridge that lets KCS sell multi-asset "solutions" (strategic partnerships, SMAs, co-invest) instead of single funds. [Inferred]

#### 1.3.2 KKR's model portfolios for advisers (the "beyond 60/40" pitch)

On kkr.com/wealth KKR publishes three illustrative model portfolios built by its Global Macro & Asset Allocation (GMAA) team, using Burgiss, Bloomberg and NCREIF data for 2006 to 2024 and "No specific KKR products referenced." [S437, Confirmed]

| Model | What moves | Private sleeve | Stated historical result |
|---|---|---|---|
| Growth | "shifts 15% of the Public Equity allocation into Private Equity, and 15% of Public Bonds into higher returning private asset classes" | PE 15%, Private Credit 5%, Infrastructure 5%, Real Estate 5% | "an additional 50 basis points of return annually compared to the traditional 60/40, while still maintaining 70% of the portfolio in liquid assets"; $100 grew to $555 vs $464 (2005 to 2024) |
| Income | "maintains its 40% Public Bond allocation, while reallocating out of Public Equity" (30%) | Private Credit 15%, Infrastructure 7.5%, Real Estate 7.5% | "4.5% yield, higher than the 3.1% yield of the traditional 60/40" |
| Capital preservation | Keeps 40% bonds, tilts equity into four private classes | Private Credit 12.5%, Infrastructure 7.5%, PE 5%, Real Estate 5% | "comparable returns to the 60/40 portfolio with less volatility (from 11.6% to 8.5%)" |
Source: S437 [Confirmed]

- Arithmetic: the growth model is 45% equity / 25% bonds / 30% private; income and capital preservation are 30% equity / 40% bonds / 30% private. So KKR's house answer to "how much private?" is 30% of a balanced portfolio. [Inferred from S437] The brief's "40/30/30" does not match KKR's published wealth models exactly; the closest are 45/25/30 and 30/40/30. [Inferred]
- The same page argues "Correlations between these two traditional asset classes have risen meaningfully, reducing the diversification benefits that once anchored the 60/40" and that "the number of publicly listed U.S. companies has declined by nearly 50%" since 2000. [S437, Confirmed]

#### 1.3.3 Asset-based finance (ABF)

- KKR wealth explainer: "Asset-Based Finance: What You Need to Know" (kkr.com, data notes dated 6 June 2025). Definition: "private credit investments backed by large, diversified pools of hard or financial assets. Given the nature of these investments, private ABF is considered non-corporate credit." [S434, Confirmed]
- Market size claim: "We estimate the private ABF market today is larger than the syndicated loan, high yield bond, and direct lending markets combined, and it could reach approximately $9.2 trillion by 2029." Source line: Integer Advisors and KKR Credit research, data as of 31 Mar 2024. [S434, Confirmed] A search snippet of the same page gives "over $6.1 trillion today" and a pre-GFC peak of "$3.1 trillion in 2006" [S434 snippet, Reported].
- Why it grew: "Post-crisis regulation and resulting higher capital requirements have reduced banks' risk appetites." [S434, Confirmed]
- Mechanics vs direct lending: ABF investors "receive front-loaded principal payments plus interest, similar to the way homeowners make their mortgage payments" ("self-amortizing"), while direct lending pays "interest-only coupons" with principal at the end. [S434, Confirmed]
- Fund: Asset-Based Finance Partners II closed July 2025 at $5.6bn plus nearly $1bn of SMAs, $6.5bn total, more than twice ABF Partners I. Daniel Pietrzak: "The $6 trillion Asset-Based Finance (ABF) market, projected to exceed $9 trillion by 2029, is one of the most dynamic opportunity sets today, yet it remains relatively undercapitalized." KKR began ABF in 2016 and reported $74bn+ of ABF assets and 18 captive platforms. [S433, Reported: multiple outlets carry the same release; I did not open kkr.com's copy]

#### 1.3.4 Insurance CIO survey and NAIC updates (insurance client content)

- "2026 KKR Insurance CIO Survey" (published 2 Oct 2026): about 50 US insurers with nearly $2.6tn of AUM. "Nearly 80% expect to maintain or accelerate their pace of private capital investment, while 91% plan to maintain or increase credit exposure." "Every major Private Credit category is a net add in the survey, led by Asset-Based Finance." CIO concerns: "Asset-liability matching, illiquidity limits, regulatory capital, reinvestment risk." The full deck is available via "your Relationship Manager", i.e. KCS. [S438, Confirmed]
- "Highlights from the NAIC's 2026 Spring National Meeting" (7 Apr 2026, Andrew Phillips): a regulatory digest KKR sends to insurer clients ("reach out to your relationship manager or kkrinsurance@kkr.com"). [S439, Confirmed] Key numbers:
  - Proposed CLO capital factors: senior tranches (Aaa to A2) "roughly 0.03-0.14%"; A3 to Baa3 "1.8-2.7%"; a Baa3 tranche thinner than 4% would face "a 12.5% charge". NAIC targets year-end 2026.
  - Collateral loans currently carry "a uniform base factor of 6.8% for life insurers"; loans backed by JV/LLC or residual interests have underlying charges of "30-45%". A look-through framework is proposed (adoption "likely for year-end 2027").
  - On 1 Jan 2026 the Valuation of Securities Task Force was replaced by the Invested Assets (E) Task Force.
  - RBC model governance principles adopted in Fall 2025 focus on "equal capital for equal risk."

#### 1.3.5 Infrastructure content

- KKR wealth page "infrastructure-investing-approach" and Infrastructure 101 exist on kkr.com/wealth [S465, Confirmed link list]. I did not fetch a dedicated "case for infrastructure" paper with numbers [Gap]. The quantitative infrastructure facts below come from the GII V release.

### 1.4 Flagship and institutional products

#### 1.4.1 Global Infrastructure Investors V (GII V)

From KKR's press release of 3 August 2026 [S430, Confirmed]:
- "$19.2 billion Core+ fund focused on investing in critical infrastructure assets and businesses primarily in North America and Western Europe." Fifth vintage; "KKR's largest infrastructure fund raised to date."
- Contributes to "approximately $45 billion raised across KKR's latest infrastructure vehicle vintages globally" (footnote: drawdown funds in investment period at 30 Jun 2026 plus infrastructure perpetual vehicles over the last twelve months, which includes K-INFRA). [S430, Confirmed]
- Platform: about $120bn of infrastructure equity, "up from just $13 billion in 2019"; more than 100 investments; about 160 dedicated infrastructure executives; over $70bn of equity committed across the Global Infrastructure strategy in North America and Europe.
- Already committed over $9bn: Altitude III, EDF power solutions North America, Enilive, FiberCop, Global Technical Realty, Gulf Data Hub, Metronet, Sempra Infrastructure, The Parking Spot.
- Investor types: "pension plans, sovereign wealth funds, insurance companies, asset managers, private wealth platforms, and family offices."
- Primary fund counsel: Debevoise & Plimpton.
- Comparison with GII IV: GII IV closed at $17bn on 14 March 2022, more than double its $7.2bn predecessor (GII III), with about $1bn committed by KKR's balance sheet, affiliates and employees. [S431, Reported via Business Wire search snippet] GII V is therefore about 13% larger than GII IV [Inferred], a much smaller step-up than IV over III, in a harder fundraising market [Inferred].

#### 1.4.2 Diversified Core Infrastructure Fund (DCIF): an institutional open-ended template

A 2021 consultant recommendation memo to the Rhode Island State Investment Commission (Cliffwater, 11 May 2021) is the best public look at DCIF terms [S432, Confirmed]:
- "an open-ended fund that will focus on critical core infrastructure investments with low volatility and strong downside protection"; "buy simplicity and hold simplicity".
- Targets: gross return 8% to 10%; time-weighted net 7% to 9%. Sectors: water, wastewater, electricity and gas distribution, digital, renewables, contracted transport, energy transition. OECD only. Initial deal size $250m to $750m.
- Terms: management fee 0.8% of NAV for commitments under $200m; 0.6% for the first six years for $50m to $200m commitments made within a year of first close. "three-year hard lock-up followed by a three-year soft lock-up with a 5% early redemption fee." No performance fee for six years, then "carried interest equal to 5% of the asset level cash yield subject to a minimum asset level cash yield hurdle of 4%." KKR committed at least $500m.
- Cliffwater recommended up to $100m.
- Note for the candidate: the memo contains errors ("founded in 1996"; KKR was founded in 1976). Consultant memos are a gatekeeping tool that KCS must influence, and they are not always accurate. [S432 Confirmed for the text; interpretation Inferred]
- Contrast: institutional open-ended core fund (0.6% to 0.8% fee, cash-yield carry, multi-year lock-up) vs K-INFRA for wealth (1.25% fee, 12.5% over 5%, quarterly 5% liquidity after a 24-month soft lock). Same infrastructure team, different wrappers and economics. [Inferred from S421, S432]

#### 1.4.3 Other flagship data points

- North America Fund XIV: final close reported at about $23bn in April 2026, above its $20bn target and $22bn hard cap, vs $19bn for Fund XIII. [S459, Reported; I did not read KKR's own release]
- Asian Fund V: named in KKR's Q2 2026 release as a driver of PE fundraising (see WS1). Size not established here [Gap].

#### 1.4.4 Insurance sidecars: the Ivy vehicles

- KKR 10-K: "we also sponsor investment vehicles raised from third-party capital, such as the Ivy investment vehicles, to participate alongside Global Atlantic's institutional and individual market activities. These Global Atlantic sponsored vehicles provide third-party capital to support various combinations of reinsurance, insurance and other potentially strategic activities. As of December 31, 2025, $58 billion of Global Atlantic AUM is provided by these Global Atlantic sponsored vehicles." [S425, Confirmed]
- How they work: they are "commitment-based structures with third-party investors" that "participate alongside Global Atlantic through reinsurance in certain insurance business which Global Atlantic writes during the co-invest vehicles' investment periods." Risk: a vehicle may "fail or refuse to fund their portion", and GA's remedy is against the vehicle, "but not directly against their shareholders or lenders." [S425, Confirmed]
- Regulation: GA's Bermuda insurers and "reinsurance co-investment vehicles sponsored by Global Atlantic are subject to regulation and supervision by the Bermuda Monetary Authority." [S425, Confirmed]
- Q2 2026: IV-related AUM "$62 billion ... up from approximately $50 billion just a year ago"; "$6 billion of dry powder that we think translates to north of $60 billion of buying power on the liability side." KKR receives fees from "IV-related vehicles" plus GA-related capital markets fees "which we think can reach hundreds of millions annually over time." Total insurance economics were $2bn net of compensation over the last twelve months. [S440, Confirmed]
- Plain English: an investor (often a sovereign fund or pension, raised by KCS) commits equity to an Ivy vehicle. When GA writes a block of annuities or reinsures another insurer's book, the vehicle takes a share of that block as reinsurer. Equity of about $1 supports about $10 of liabilities, hence $6bn dry powder for $60bn of capacity. The investor earns the spread between asset yields and liability costs; KKR earns fees on the vehicle and on managing the assets. [Inferred from S425, S440]

### 1.5 Co-investment syndication: how KCM and KCS make money from it

- KCM "provides syndication services for co-investments in transactions participated in by KKR, our investment vehicles, Global Atlantic, and third-party clients, which may entitle the firm to receive transaction fees, management fees, and a carried interest." [S425, Confirmed]
- Underwrite-then-sell: "We have used our balance sheet in our capital markets business to underwrite loans, securities or other financial instruments, which we generally expect to syndicate to third parties." KKR also uses "arrangements with third parties that reduce our risk associated with holding unsold securities ... which enables our capital markets business to underwrite a larger amount." [S425, Confirmed]
- KCM revenue 2025: $930m of capital markets transaction fees; 404 transactions (49 equity, 355 debt) vs 397 in 2024 (56 equity, 341 debt); fee rates "generally higher with respect to underwriting or syndicating equity offerings than ... debt offerings"; about 15% of fees from unaffiliated third parties (13% in 2024); about 54% earned outside North America (47% in 2024). The 10-K bar chart labels $757m, $490m and $184m as "average capital markets transaction fees of the periods represented"; the period labels did not survive text extraction. [S425, Confirmed for values; periods Gap]
- The co-invest economics lever: "Since 2014, our fund agreements typically require us to share 100% of any monitoring, transaction, and break-up fees that are allocable to a fund ... with fund investors, therefore these types of fees, when generated, are uniquely driven by co-investment opportunities." And "transaction fees earned in our capital markets business are not shared with fund investors." [S425, Confirmed] So every dollar of co-investment KCS places outside the fund can create fee income that fund LPs do not offset. [Inferred]
- Accounting: capital syndicated by KCM to third parties (other than KKR funds or the balance sheet) is excluded from KKR's "capital invested" metric. [S425, Confirmed]
- Competitive pressure on terms: KKR may have to grant "reduced management fees, fee holidays, increased co-investment rights or other economic or governance concessions." [S425, Confirmed] Co-investment rights are a bargaining chip in fundraising. [Inferred]
- Evergreen K-Series vehicles add a new co-invest buyer: K-PEC fills "second tier" allocations [S420], and Capital Group U.S. Equity+ puts about 10% of NAV into co-investments [S427, Confirmed].
- How LPs test this: ILPA DDQ 2.0 section 5 asks whether predecessor funds charged LP co-investors a transaction fee, management fee or carry; whether co-investments were "of a syndicated nature"; whether any "involved co-underwriting pre-signing"; and how "broken-deal expenses associated with co-investments are handled." [S444, Confirmed]

### 1.6 The LP toolkit

**ILPA DDQ 2.0** (updated November 2021; 58 pages) [S444, Confirmed]:
- 20 numbered sections: 1 Firm: General Information; 2 Fund: General Information; 3 Succession Planning / Key Persons; 4 Investment Strategy; 5 Co-Investments; 6 GP-Led Secondaries / Continuation Funds; 7 Credit Facilities; 8 Investment Process; 9 Team; 10 Alignment of Interests; 11 Market Environment; 12 Fund Terms; 13 Firm Governance / Risk / Compliance; 14 Track Record; 15 Accounting / Valuation; 16 Reporting; 17 Legal; 18 Data Security / Technology / Third-Party(s); 19 ESG (per PRI's LP PE Responsible Investment DDQ); 20 Diversity, Equity and Inclusion.
- Appendices A to H: Requested Documents; Team Members; References; Third-Party(s) and Technology Tool(s); Fund; Portfolio Investments; GP-Led Secondaries / Continuation Funds; Credit Facilities.
- Roughly 320 numbered question lines (my count of "x.y" items in the text; approximate). [Inferred]
- Junior KCS staff typically draft or update DDQ answers with the product team. [Inferred; consistent with the DDQ duties quoted in WS1]

**ILPA Reporting Template and Performance Template** (released January 2025) [S445, S446, Confirmed]:
- Reporting Template: recommended for funds "still in their investment period during Q1 2026" or starting on or after 1 January 2026. Adds a gross-to-net management fee reconciliation (rebates, waivers, offsets), granular partnership expenses including chargebacks to the GP, capitalised transaction fees, and "granular accounting of incentive allocation amounts." [S445]
- Performance Template: for funds starting on or after 1 January 2026; first delivery four full fiscal quarters later. Two methods: "granular" (fund-to-investor cash flows, itemised calls) and "gross-up". Standardises IRR and TVPI/MOIC, gross and net, "with and without the impact of fund-level subscription facilities." [S445]
- The Capital Call and Distribution Template was refreshed later in 2025; a Portfolio Company Template refresh is slated for January 2027. [S446]

**Side letters and MFN** [S456, Confirmed; S457, Reported]:
- CMS: an MFN "typically entitles an investor to elect the benefit of rights contained in other investors' side letters and potentially also the right to view the other investors' side letters." Sponsors "require MFN elections to be submitted within a certain period following closing" and "Late MFN election submissions are at risk of being rejected." Sponsors use carve-outs to "afford larger, first close or repeat investors more favourable rights." The process places "additional financial, administrative and disclosure burdens on sponsors, particularly in open-ended products." [S456]
- Common practice (secondary sources): MFN rights are tiered so an LP can only elect terms given to LPs with equal or smaller commitments; standard carve-outs cover legal/regulatory/tax-status terms, LPAC seats, co-investment rights and size-based fee breaks. [S457, Reported]

**Commitment pacing: the Takahashi-Alexander ("Yale") model.**
- Published as Takahashi and Alexander, "Illiquid Alternative Asset Fund Modeling", Journal of Portfolio Management 28(2), 2002, pp. 90 to 100. [S454, Confirmed citation]
- "There are six inputs in order to predict capital contributions, distributions, and net asset value of a private equity fund: RC (rate of contribution), CC (capital commitment), L (life of the fund), B (bow factor describing changes on the rate of distribution over time), G (annual growth rate), and Y (yield percentage)." It is "a discrete-time deterministic model." [S454, Confirmed]
- Mechanics in words: each year the fund calls RC times the unfunded commitment; NAV grows at G; distributions are a rising share of NAV whose shape is set by the bow B (higher bow means later distributions). A pacing model runs this for each planned commitment to keep total private exposure near a target. [S455, Reported; gloss Inferred]
- KKR's TPA paper argues for "steadier commitment pacing" and recycling distributions of "10-30% of NAV" a year. [S435, S436, Confirmed]

**Kaplan-Schoar PME.**
- Kaplan and Schoar, "Private Equity Performance: Returns, Persistence, and Capital Flows" (NBER working paper 2003; Journal of Finance 2005). [S453, Confirmed for WP text; JF publication Reported]
- Definition: "The PME measures the discounted value of the cash outflows of the fund relative to the discounted value of the cash inflows (all net of fees), where discounting is undertaken using the total return to the S&P 500. This calculation has the effect of comparing investing in the fund to investing in the S&P 500." A PME above 1.0 means the fund beat the index. [S453, Confirmed; "above 1.0" Inferred]
- Findings: average net returns roughly equal the S&P 500, with large dispersion and strong persistence across a GP's successive funds. [S453, Reported via abstract]

**Operational due diligence (ODD).**
- Cambridge Associates (27 Jun 2025): ODD's lens on valuation is "not to audit or underwrite specific asset valuations, but rather to assess a manager's controls, policy, oversight, and governance." It stresses open-end and evergreen funds, "where transactions are based on the fund's NAV", and that "Fee calculations rely on accurate valuations." Oversight should come from "a valuation committee, fund auditors, and the board." [S458, Confirmed]
- Wider ODD scope (secondary): fund administration, cash controls, compliance, business continuity, cybersecurity, service providers. [S458 plus search context, Reported]
- Link to K-Series: monthly NAV with Level III assets is exactly where ODD teams focus; K-PEC's NAV is set by the Manager under Board-approved policies with an Administrator computing per-share values. [S420, S458; link Inferred]

### 1.7 European and UK rules for semi-liquid funds

WS4 gives the timeline. Extra technical detail:

**AIFMD II liquidity management tools (LMTs).**
- Open-ended AIFs must select "at least two appropriate LMTs ... from those listed in points 2 to 8" of Annex V: redemption gates; extension of notice periods; redemption fees; swing pricing; dual pricing; anti-dilution levies; redemption in kind. Suspension and side pockets sit outside this count as exceptional tools. "This cannot be done by selecting only dual and swing pricing." Redemptions in kind only for professional investors. [S449, Confirmed; S450, Reported]
- Level 2: Commission Delegated Regulation (EU) 2026/465 (RTS on LMT characteristics), published in the Official Journal on 27 February 2026, applying from 16 April 2026. Funds constituted before that date are "deemed to comply with the RTS until 16 April 2027." [S449, Confirmed]
- ESMA: final draft RTS and guidelines on 15 April 2025 [S448, Confirmed]; amended guidelines dated 18 December 2025 per Debevoise [S449, Confirmed]. WS4 cites formal publication on 12 March 2026 [S298 in WS4]; the likely explanation is that the March date is the translated publication that starts the comply-or-explain clock [Inferred, unverified]. ESMA recommends, but does not require, choosing "at least one quantitative LMT and one Anti-Dilution Tool." [S448, Confirmed]
- Gates can be set at fund level, investor level or both; ESMA's alternative method lets orders at or below a set size be paid in full while larger orders are gated. [S448, S449, Confirmed]

**ELTIF 2.0 RTS (Delegated Regulation (EU) 2024/2759)** [S447, Confirmed]:
- Adopted 19 July 2024; OJ 25 October 2024; in force 26 October 2024.
- No fixed minimum holding period; the manager sets it. Redemptions more often than quarterly must be justified.
- If the notice period is under 3 months, the manager must tell its regulator and explain why.
- Two ways to size the maximum redemption: Annex I uses redemption frequency and notice period (example: quarterly with 3 months' notice allows redemptions of up to 33.3% of liquid assets); Annex II uses frequency and a minimum share of liquid assets (example: quarterly with at least 20% liquid assets allows up to 50%). The base includes cash flows forecast prudently over 12 months.
- Matching of exiting and incoming investors is allowed under a policy.

**UK LTAF.**
- Secondary sources describe the LTAF as open-ended with dealing no more often than monthly and a notice period of at least 90 days for redemptions. [S451, Reported; the FCA rulebook (COLL 15) was not read directly]
- An FCA deputy chief executive's May 2026 speech put LTAF AUM at £7.5bn, up from £5bn in under a year. [S452, Reported]

**FCA Consumer Duty.**
- Private fund managers with institutional bases "may still fall in scope where they sit in a distribution chain to retail customers" [S452, Reported]. Wealth managers must show "fair value" and suitable target markets; commentary flags semi-liquid structures as a risk where investors do not understand them. [S452, Reported]
- Implication for KKR London KCS: when K-PRIME or a KKR fund is sold through a UK private bank, KKR must supply target market and fair value information so the distributor can meet its own duty. [Inferred]

### 1.8 KKR on education, AI and "solutions"

- KKR Academies (adviser education): Scott Nuttall on the Q2 2026 call (30 July 2026), answering Morgan Stanley's Michael Cyprys: "the first thing is education ... we are running multiple -- it seems lately KKR Academies a week, having 100 advisers at a time come in, spend a dinner in a day with us ... We've invested a lot in that over the last few years. And that's a global effort. We're running those U.S., Europe and Asia. The second thing I would say is, obviously, you need access and you need distribution." [S440, Confirmed]
- Digital education: "Alternatives Unlocked", launched January 2024 [S442, Reported], is live on kkr.com/wealth with Private Equity 101, Private Credit 101, Infrastructure 101, Real Estate 101 and a video library. [S465, Confirmed]
- "Solutions" target: "we feel really good about the target of $100-plus billion of AUM from our solutions business over time" (CFO Robert Lewin, Q2 2026, in the context of the Arctos integration). [S440, Confirmed] This refers to the KKR Solutions investing business, not KCS (see WS1).
- K-Series reporting: K-Series PE realised performance fees now count as fee-related performance revenue, "subject to a 15% to 20% compensation rate" vs 70% to 80% before (Q2 2026 call summary). [S440, Confirmed via transcript page summary]
- Q1 2026: K-Series raised $4bn of gross inflows against about $250m of redemptions; AUM over $38bn. [S441, Reported]
- AI: I found no public KKR statement on how KCS itself uses AI. KKR's Technology team advertised an "AI Platform Lead" (Director of AI Platforms) in New York to "Define, build, and scale a centralized AI platform to enable a new generation of intelligent, business-facing applications" and "Drive the adoption of Generative AI, NLP, and ML across the firm" (listing removed 23 Feb 2026). [S443, Confirmed] Plausible KCS uses (DDQ drafting, RFP search, meeting notes, CRM summaries) are not confirmed. [Inferred, Gap]

### 1.9 Insurance as a client: why insurers buy private credit

- Insurers' required capital (US life RBC) depends on the NAIC designation of each asset, which depends on credit ratings: "the determination of RBC is based on the NAIC designation of the assets in which Global Atlantic invests. NAIC designation for certain investments depends on the applicable NRSRO rating." [S425, Confirmed]
- So an insurer prefers assets that are investment-grade rated (low capital charge) but pay more than public bonds of the same rating. Private IG credit and ABF fit this. [Inferred] The NAIC moved from 6 to 20 bond designation categories with year-end 2021 factors. [S461, Reported]
- Regulators are tightening: the 10-K notes NAIC changes on filing-exempt ratings "may result in ... the capital charge treatment of any such investment being less favorable." Bermuda's BMA keeps reviewing the BSCR "to maintain its equivalency with Solvency II." [S425, Confirmed]
- KKR's insurer pitch combines asset origination with capital advice: survey data (80% maintaining or accelerating private capital) [S438] plus NAIC factor tracking (0.03% to 12.5% CLO factors; 6.8% collateral loan factor) [S439].
- Global Atlantic is both a client and a capital source: GA's balance sheet is 22% of KKR AUM (WS1); GA-sponsored vehicles add $58bn (Dec 2025) [S425]; GA generates capital markets fees [S440]; and Lewin described Arctos as a way to "create flow for Global Atlantic." [S440, Confirmed]
- KKR on the insurance cycle (Lewin, Q2 2026): in volatile markets "you're going to have less competition on the asset side ... spreads are going to expand ... less competition on the liability side," and KKR is set up with "longer duration liabilities, real linkage between liability origination and asset origination." [S440, Confirmed]

---

## 2. Key numbers table

| Metric | Value | As-of date | Source | Confidence |
|---|---|---|---|---|
| K-PEC Transactional NAV | $9.93bn | 31 Dec 2025 | S420 | Confirmed |
| K-PEC GAAP NAV | $9.495bn | 31 Dec 2025 | S420 | Confirmed |
| K-PEC 2025 subscriptions | $4.18bn | FY2025 | S420 | Confirmed |
| K-PEC new portfolio companies in 2025 | 27 | FY2025 | S420 | Confirmed |
| K-PEC Class I 2025 return / ITD annualised | 16.81% / 12.94% | 31 Dec 2025 | S420 | Confirmed |
| K-PEC management fee | 1.25% (R classes 1.00% for 60 months) | 2026 | S420 | Confirmed |
| K-PEC performance allocation | 15% over 5% hurdle, HWM, 100% catch-up | 2026 | S420 | Confirmed |
| K-PEC repurchase cap | 5% of NAV per quarter | 2026 | S420 | Confirmed |
| K-PEC early repurchase fee | 5% within 24 months | 2026 | S420 | Confirmed |
| K-PEC overflow tender price | about 10% below NAV | 2026 | S420 | Confirmed |
| K-PEC recourse leverage cap | 30% of total assets | 2026 | S420 | Confirmed |
| K-PEC revolver | $1.0bn (accordion $1.5bn) | Mar 2026 | S420 | Confirmed |
| K-PEC 2025 repurchases | about $26.4m (about 0.3% of NAV) | FY2025 | S420 | Confirmed / ratio Inferred |
| Distribution plus servicing fee (S, U) | 0.85% a year | 2026 | S420, S424 | Confirmed |
| K-INFRA Transactional NAV | $6.47bn | 31 Dec 2025 | S421 | Confirmed |
| K-INFRA 2025 subscriptions | $2.84bn | FY2025 | S421 | Confirmed |
| K-INFRA Class I 2025 return | 10.13% | 31 Dec 2025 | S421 | Confirmed |
| K-INFRA performance allocation | 12.5% over 5% hurdle | 2026 | S421 | Confirmed |
| K-INFRA asset mix | about 85% infra / 15% liquidity; max 15% non-OECD | 2026 | S421 | Confirmed |
| K-FIT shareholders' equity | $1.54bn | 31 Dec 2025 | S422 | Confirmed |
| K-FIT investments at fair value | $2.63bn | 31 Dec 2025 | S422 | Confirmed |
| K-FIT income hurdle / catch-up | 1.25% a quarter (5.0%) / to 1.43% (5.72%) | 2026 | S422 | Confirmed |
| K-FIT early repurchase deduction | 2% within 12 months | 2026 | S422 | Confirmed |
| K-FITS shareholders' equity | $1.006bn | 30 Jun 2026 | S423 | Confirmed |
| KREST minimum investment | $10,000 (S, D, U); $1m (I) | Jan 2026 | S424 | Confirmed |
| KREST incentive fee | 12.5% of operating income; none on gains | Jan 2026 | S424 | Confirmed |
| KREST estimated average net assets | about $1.53bn | Jan 2026 | S424 | Confirmed |
| Capital Group KKR Core Plus+ mix | about 60% public / 40% private credit | Apr 2025 | S426 | Confirmed |
| Core Plus+ repurchase | 5% to 25% policy; 10% expected per quarter | Apr 2025 | S426 | Confirmed |
| Core Plus+ management fee / net TER | 0.61% / 0.84% (F-3, R-6) to 1.54% (A-2) | Apr 2025 | S426 | Confirmed |
| Core Plus+ minimum | $1,000 (most classes) | Apr 2025 | S426 | Confirmed |
| Capital Group KKR U.S. Equity+ mix | about 60% public / 30% K-PEC / 10% co-invest | Feb 2026 | S427 | Confirmed |
| U.S. Equity+ repurchase / fee | 5% per quarter / 0.350% | Feb 2026 | S427 | Confirmed |
| GII V final close | $19.2bn | 3 Aug 2026 | S430 | Confirmed |
| GII IV final close | $17bn | 14 Mar 2022 | S431 | Reported |
| KKR infrastructure equity managed | about $120bn (vs $13bn in 2019) | Aug 2026 | S430 | Confirmed |
| Latest infra vintages raised | about $45bn | 30 Jun 2026 | S430 | Confirmed |
| DCIF management fee | 0.8% (0.6% early, $50m to $200m) | May 2021 | S432 | Confirmed |
| DCIF carry | 5% of asset cash yield over 4% hurdle, after year 6 | May 2021 | S432 | Confirmed |
| DCIF lock-up | 3 years hard plus 3 years soft (5% fee) | May 2021 | S432 | Confirmed |
| ABF Partners II | $5.6bn fund plus about $1bn SMAs = $6.5bn | Jul 2025 | S433 | Reported |
| Private ABF market forecast | about $9.2tn by 2029 | Jun 2025 | S434 | Confirmed |
| KCM transaction fees | $930m | FY2025 | S425 | Confirmed |
| KCM transactions | 404 (49 equity, 355 debt) | FY2025 | S425 | Confirmed |
| KCM fees from third parties / outside N. America | about 15% / about 54% | FY2025 | S425 | Confirmed |
| GA-sponsored vehicle AUM | $58bn | 31 Dec 2025 | S425 | Confirmed |
| IV-related vehicle AUM | $62bn (about $50bn a year earlier) | Q2 2026 | S440 | Confirmed |
| Sidecar dry powder / buying power | $6bn / over $60bn | Q2 2026 | S440 | Confirmed |
| Private markets annual distributions | about 10% to 30% of NAV | Jul 2026 | S436 | Confirmed |
| TPA worked example | 70/30 reference; up to 30% private; 10% leverage | Feb 2026 | S435 | Confirmed |
| KKR growth model | +50bp a year vs 60/40; 70% liquid; $555 vs $464 | 2005 to 2024 data | S437 | Confirmed |
| KKR income model yield | 4.5% vs 3.1% | 2006 to 2024 data | S437 | Confirmed |
| KKR capital preservation volatility | 8.5% vs 11.6% | 2006 to 2024 data | S437 | Confirmed |
| Insurance CIO survey sample | about 50 insurers, about $2.6tn AUM | Oct 2026 | S438 | Confirmed |
| Insurers maintaining/accelerating private capital | nearly 80% | Oct 2026 | S438 | Confirmed |
| Proposed CLO RBC factors | 0.03% to 0.14% (Aaa to A2); 12.5% thin Baa3 | Apr 2026 | S439 | Confirmed |
| Life RBC base factor, collateral loans | 6.8% | Apr 2026 | S439 | Confirmed |
| KKR Academies cadence | "multiple ... a week", about 100 advisers each | 30 Jul 2026 | S440 | Confirmed |
| ILPA DDQ 2.0 | 20 sections, 8 appendices, 58 pages | Nov 2021 | S444 | Confirmed |
| AIFMD II minimum LMTs | 2 from Annex V points 2 to 8 | from 16 Apr 2026 | S449 | Confirmed |
| AIFMD II grandfathering | existing funds compliant until 16 Apr 2027 | 2026 | S449 | Confirmed |
| ELTIF RTS example | quarterly + 3m notice: up to 33.3% of liquid assets | Oct 2024 | S447 | Confirmed |
| LTAF notice period | at least 90 days | 2021 rules | S451 | Reported |
| UK LTAF AUM | £7.5bn | May 2026 | S452 | Reported |
| North America Fund XIV | about $23bn | Apr 2026 | S459 | Reported |

---

## 3. Verbatim quotes actually read

| Quote | Speaker / document | Date | Source |
|---|---|---|---|
| "We are a holding company that seeks to acquire, own and control portfolio companies with the objective of generating attractive risk-adjusted returns and achieving medium-to-long-term capital appreciation through Joint Ventures" | K-PEC 10-K | 26 Mar 2026 | S420 |
| "Rather, through its Joint Ventures, the Company is primarily engaged in the businesses of its Joint Ventures, namely, the business of owning and controlling portfolio companies." | K-PEC 10-K | 26 Mar 2026 | S420 |
| "the Company does not benefit from any mandatory minimum purchase rights or minimum purchase thresholds. As such the Company will not benefit from any priority acquisition allocation" | K-PEC 10-K | 26 Mar 2026 | S420 |
| "KKR is allocated a 'Performance Participation Allocation' equal to 15.0% of the Total Return attributable to Investor Shares subject to a 5.0% annual Hurdle Amount and a High Water Mark, with a 100% Catch-Up" | K-PEC 10-K | 26 Mar 2026 | S420 |
| "Our distributions may and are expected to exceed our earnings and cash flow from operating activities" | K-INFRA 10-K | 26 Mar 2026 | S421 |
| "The Manager may cause these transfers to be made at cost, or cost plus an interest rate or carrying cost charged from the time of acquisition to the time of transfer" | K-INFRA 10-K (warehousing) | 26 Mar 2026 | S421 |
| "We are a non-exchange traded, perpetual-life BDC" | K-FIT 10-K | 12 Mar 2026 | S422 |
| "The Fund intends, but is not obligated, to conduct quarterly tender offers for up to 5.0% of the aggregate NAV of its outstanding Common Stock" | KREST N-2 | 27 Jan 2026 | S424 |
| "Since 2014, our fund agreements typically require us to share 100% of any monitoring, transaction, and break-up fees that are allocable to a fund ... therefore these types of fees, when generated, are uniquely driven by co-investment opportunities." | KKR & Co. 10-K | 27 Feb 2026 | S425 |
| "we also sponsor investment vehicles raised from third-party capital, such as the Ivy investment vehicles, to participate alongside Global Atlantic's institutional and individual market activities" | KKR & Co. 10-K | 27 Feb 2026 | S425 |
| "the fund will seek to allocate approximately 60% of its net assets to public debt assets ... and approximately 40% to private credit assets" | Capital Group KKR Core Plus+ N-2/A | 16 Apr 2025 | S426 |
| "Normally, the fund expects to invest approximately 30% of its net assets in K-PEC and approximately 10% of its net assets in co-investments." | Capital Group KKR U.S. Equity+ N-2/A | 19 Feb 2026 | S427 |
| "It reflects the trust our investors have placed in our team, the strength of the global platform we've built together, and our conviction that the opportunity in infrastructure has never been greater." | Raj Agrawal, Global Head of Real Assets, KKR | 3 Aug 2026 | S430 |
| "We believe this result speaks to our differentiated investment approach and the growing recognition of infrastructure as an essential long-term allocation" | Brandon Donnenfeld, MD and Chief Development Officer, KKR infrastructure | 3 Aug 2026 | S430 |
| "The Fund has a three-year hard lock-up followed by a three-year soft lock-up with a 5% early redemption fee." | Cliffwater memo on DCIF | 11 May 2021 | S432 |
| "One analogy that consistently resonated with clients was to think about TPA as 'zero-based budgeting for portfolio construction.'" | McVey, McNellis, Olinger, Dai, KKR | Jul 2026 | S436 |
| "Across private market strategies, annual distributions have historically averaged approximately 10-30% of NAV" | KKR GMAA | Jul 2026 | S436 |
| "One practical on-ramp we think that warrants all investor attention is a 'minimum viable TPA'." | KKR Multi-Asset Strategies | Feb 2026 | S435 |
| "The growth portfolio framework historically delivered an additional 50 basis points of return annually compared to the traditional 60/40, while still maintaining 70% of the portfolio in liquid assets." | KKR wealth model portfolios page | accessed Oct 2026 | S437 |
| "We estimate the private ABF market today is larger than the syndicated loan, high yield bond, and direct lending markets combined, and it could reach approximately $9.2 trillion by 2029." | KKR, "Asset-Based Finance: What You Need to Know" | 2025 | S434 |
| "Every major Private Credit category is a net add in the survey, led by Asset-Based Finance." | 2026 KKR Insurance CIO Survey | 2 Oct 2026 | S438 |
| "Currently, collateral loans are subject to a uniform base factor of 6.8% for life insurers." | KKR NAIC Spring 2026 update (Andrew Phillips) | 7 Apr 2026 | S439 |
| "we are running multiple -- it seems lately KKR Academies a week, having 100 advisers at a time come in, spend a dinner in a day with us" | Scott Nuttall, Co-CEO, Q2 2026 call | 30 Jul 2026 | S440 |
| "fees from IV-related vehicles, where we have $62 billion of AUM, up from approximately $50 billion just a year ago" | Robert Lewin, CFO, Q2 2026 call | 30 Jul 2026 | S440 |
| "Define, build, and scale a centralized AI platform to enable a new generation of intelligent, business-facing applications." | KKR AI Platform Lead job posting | removed 23 Feb 2026 | S443 |
| "The PME measures the discounted value of the cash outflows of the fund relative to the discounted value of the cash inflows (all net of fees), where discounting is undertaken using the total return to the S&P 500." | Kaplan and Schoar, NBER WP | 2003 | S453 |
| "The ODD team's lens while evaluating valuation is not to audit or underwrite specific asset valuations, but rather to assess a manager's controls, policy, oversight, and governance" | Cambridge Associates | 27 Jun 2025 | S458 |
| "Late MFN election submissions are at risk of being rejected by the fund manager." | CMS Funds Group | undated | S456 |

---

## 4. Source table

| ID | Outlet | Title | Pub date | URL | Accessed | Status | Confidence note |
|---|---|---|---|---|---|---|---|
| [S420] | SEC EDGAR | KKR Private Equity Conglomerate LLC Form 10-K FY2025 | 2026-03-26 | https://www.sec.gov/Archives/edgar/data/1957845/000195784526000029/kkr-20251231.htm | 2026-10-11 | FETCHED | Primary; full text read |
| [S421] | SEC EDGAR | KKR Infrastructure Conglomerate LLC Form 10-K FY2025 | 2026-03-26 | https://www.sec.gov/Archives/edgar/data/1948056/000194805626000023/kkr-20251231.htm | 2026-10-11 | FETCHED | Primary |
| [S422] | SEC EDGAR | KKR FS Income Trust Form 10-K FY2025 | 2026-03-12 | https://www.sec.gov/Archives/edgar/data/1930679/000162828026017326/kfit-20251231.htm | 2026-10-11 | FETCHED | Primary |
| [S423] | SEC EDGAR | KKR FS Income Trust Select Form 10-Q Q2 2026 | 2026-08-12 | https://www.sec.gov/Archives/edgar/data/1975736/000162828026056136/kfits-20260630.htm | 2026-10-11 | FETCHED | Primary |
| [S424] | SEC EDGAR | KKR Real Estate Select Trust Inc. Form N-2 | 2026-01-27 | https://www.sec.gov/Archives/edgar/data/1803958/000119312526022997/d920471dn2.htm | 2026-10-11 | FETCHED | Primary |
| [S425] | SEC EDGAR | KKR & Co. Inc. Form 10-K FY2025 | 2026-02-27 | https://www.sec.gov/Archives/edgar/data/1404912/000140491226000007/kkr-20251231.htm | 2026-10-11 | FETCHED | Primary; chart period labels lost in extraction |
| [S426] | SEC EDGAR | Capital Group KKR Core Plus+ Form N-2/A | 2025-04-16 | https://www.sec.gov/Archives/edgar/data/2040315/000110465925035232/tm2510815d1_n2a.htm | 2026-10-11 | FETCHED | Primary (pre-effective; terms may have changed) |
| [S427] | SEC EDGAR | Capital Group KKR U.S. Equity+ Form N-2/A | 2026-02-19 | https://www.sec.gov/Archives/edgar/data/2078301/000110465926017516/tm265650d1_n2a.htm | 2026-10-11 | FETCHED | Primary |
| [S428] | SEC EDGAR full-text search | EFTS queries for K-Series and Capital Group KKR names | n/a | https://efts.sec.gov/LATEST/search-index?q=%22KKR%20Private%20Equity%20Conglomerate%22 | 2026-10-11 | FETCHED | Used to locate filings |
| [S429] | kseries.kkr.com / Emirates NBD (search snippets) | K-PRIME prospectus, KID, monthly report Aug 2024 | 2024 | https://kseries.kkr.com/wp-content/uploads/2024/04/KKR-Private-Markets-Equity-Fund-SICAV-SA-I-Prospectus.pdf | 2026-10-11 | SNIPPET | PDFs now 404; KID unreadable; Reported only |
| [S430] | KKR (press release PDF) | KKR Closes $19.2 Billion Infrastructure Fund | 2026-08-03 | https://www.kkr.com/content/dam/kkr/country-sites/fr/press-release/20260803-kkr-closes-19-billion-infrastructure-fund.pdf | 2026-10-11 | FETCHED | Primary |
| [S431] | Business Wire (snippet) | KKR Closes $17 Billion Global Infrastructure Fund | 2022-03-14 | https://www.businesswire.com/news/home/20220314005151/en/KKR-Closes-$17-Billion-Global-Infrastructure-Fund | 2026-10-11 | SNIPPET | KKR release via search; also ESG Today, BNN |
| [S432] | Rhode Island Treasury / Cliffwater | Recommendation for KKR Diversified Core Infrastructure Fund | 2021-05-11 | https://data.treasury.ri.gov/dataset/3336b5f1-8552-4362-8760-5e89cab068c8/resource/c9f20ce7-3206-496e-bab7-770ed96a0047/download/cliffwater-kkr-diversified-core-infrastructure-fund-recommendation-memo-05112021.pdf | 2026-10-11 | FETCHED | Consultant memo; contains factual slips |
| [S433] | SFNet / Alternative Credit Investor / Pulse 2.0 (snippets) | KKR completes $6.5bn ABF fundraise | 2025-07-30 | https://alternativecreditinvestor.com/2025/07/30/kkr-closes-asset-based-finance-fundraise-at-6-5bn/ | 2026-10-11 | SNIPPET | Same release in several outlets |
| [S434] | KKR | Asset-Based Finance: What You Need to Know | 2025 (data 6 Jun 2025) | https://www.kkr.com/wealth/insights/asset-based-finance | 2026-10-11 | FETCHED | $6.1tn figure only in snippet |
| [S435] | KKR Multi-Asset Strategies | The Total Portfolio Approach: A Practical Framework (Insights Vol. 15) | 2026-02 | https://www.kkr.com/content/dam/kkr/insights/pdf/kmas-feb-2026-total-portfolio-approach.pdf | 2026-10-11 | FETCHED | Primary; 22 pages |
| [S436] | KKR Global Macro Trends | The Dog Has Caught the Bus: The Total Portfolio Approach | 2026-07-29 | https://www.kkr.com/content/dam/kkr/insights/pdf/2026-july-total-portfolio-approach-update.pdf | 2026-10-11 | FETCHED | Primary |
| [S437] | KKR wealth | Model Portfolios with Private Markets (Growth, Income, Capital Preservation pages) | accessed 2026-10 | https://www.kkr.com/wealth/model-portfolios | 2026-10-11 | FETCHED | Primary |
| [S438] | KKR | 2026 KKR Insurance CIO Survey | 2026-10-02 | https://www.kkr.com/wealth/insights/2026-insurance-cio-survey | 2026-10-11 | FETCHED | Primary |
| [S439] | KKR (Andrew Phillips) | Highlights from the NAIC's 2026 Spring National Meeting | 2026-04-07 | https://www.kkr.com/wealth/insights/naic-spring-update-2026 | 2026-10-11 | FETCHED | Primary |
| [S440] | The Motley Fool via Webull | KKR (KKR) Q2 2026 Earnings Call Transcript | 2026-07-30 | https://www.webull.com/news/15319182954619905 | 2026-10-11 | FETCHED | Third-party transcript |
| [S441] | Yahoo Finance / Insider Monkey (snippets) | KKR Q1 2026 earnings call | 2026-05 | https://www.insidermonkey.com/blog/kkr-co-inc-nysekkr-q1-2026-earnings-call-transcript-1754860/ | 2026-10-11 | SNIPPET | Not read in full |
| [S442] | Business Wire (snippet) | KKR Launches New Digital Global Education Platform for Financial Advisors and Individual Investors | 2024-01-17 | https://www.businesswire.com/news/home/20240117397591/en/ | 2026-10-11 | SNIPPET | 403 on fetch |
| [S443] | Built In NYC | KKR AI Platform Lead job posting | removed 2026-02-23 | https://www.builtinnyc.com/job/ai-platform-lead/7110423 | 2026-10-11 | FETCHED | Job ad, intent not deployment |
| [S444] | ILPA | Due Diligence Questionnaire 2.0 | 2021-11 | https://ilpa.org/wp-content/uploads/2021/11/ILPA-DDQ-2.0.pdf | 2026-10-11 | FETCHED | Primary |
| [S445] | Alston & Bird | ILPA updated Reporting and Performance Templates | 2025-02-24 | https://alston.com/en/insights/publications/2025/02/ilpa-updated-reporting-performance-templates | 2026-10-11 | FETCHED | Law firm summary |
| [S446] | ILPA | Updated ILPA Templates Hub | accessed 2026-10 | https://ilpa.org/industry-guidance/templates-standards-model-documents/updated-ilpa-templates-hub/ | 2026-10-11 | FETCHED | Primary |
| [S447] | Arthur Cox | ELTIF RTS published, paving the way for open-ended ELTIFs with limited liquidity | 2024-10-25 | https://www.arthurcox.com/insights/eltif-rts-published-paving-the-way-for-open-ended-eltifs-with-limited-liquidity | 2026-10-11 | FETCHED | Law firm summary |
| [S448] | Simmons & Simmons | ESMA publishes Final Draft RTS & Guidelines on LMTs | 2025-04-17 | https://www.simmons-simmons.com/en/publications/cm9l2wwe20096upcse89uowom/esma-publishes-final-draft-rts-guidelines-on-lmts | 2026-10-11 | FETCHED | Law firm summary |
| [S449] | Debevoise & Plimpton | Liquidity Management for Open-Ended AIFs: Level 2 Measure Published in the Official Journal | 2026-04 | https://www.debevoise.com/insights/publications/2026/04/liquidity-management-for-open-ended-aifs-level-2 | 2026-10-11 | FETCHED | Law firm summary |
| [S450] | Simmons & Simmons 2026 / MFSA circular (snippets) | LMTs under AIFMD II; MFSA clarifications circular | 2026-04 | https://www.mfsa.mt/wp-content/uploads/2026/04/Circular-Providing-Clarifications-on-Liquidity-Management-Requirements-introduced-under-AIFMD-II-and-UCITS-VI.pdf | 2026-10-11 | SNIPPET | Annex V list; EUR-Lex blocked |
| [S451] | Farrer & Co / Macfarlanes / Schroders (snippets) | LTAF final rules; How does liquidity work in an LTAF? | 2021 onward | https://www.farrer.co.uk/news-and-insights/the-new-long-term-asset-fund-ltaf-final-rules-and-guidance-published/ | 2026-10-11 | SNIPPET | FCA rulebook not read |
| [S452] | Macfarlanes / Ropes & Gray / GrowthInvest (snippets) | Investment management update June 2026; Consumer Duty and private funds | 2026-06 | https://www.macfarlanes.com/insights/102n2ww/investment-management-update-june-2026 | 2026-10-11 | SNIPPET | |
| [S453] | NBER | Kaplan and Schoar, Private Equity Performance: Returns, Persistence and Capital Flows (WP) | 2003 | https://users.nber.org/~confer/2003/cfs03/kaplan.pdf | 2026-10-11 | FETCHED | JF 2005 version not read |
| [S454] | arXiv | Karatas, Klinkert, Hirsa, Supervised Neural Networks for Illiquid Alternative Asset Cash Flow Forecasting (describes Takahashi-Alexander) | 2021 | https://arxiv.org/pdf/2108.02853 | 2026-10-11 | FETCHED | Secondary on the model |
| [S455] | PitchBook / Addepar / PGIM (snippets) | Commitment pacing and cash flow forecasting pieces | various | https://www.pgim.com/white-paper/building-and-maintaining-desired-exposure-private-markets | 2026-10-11 | SNIPPET | |
| [S456] | CMS | Back to basics: Most Favoured Nations (MFN) | undated | https://cms.law/en/nld/publication/cms-funds-group-back-to-basics-briefings/most-favoured-nations-mfn | 2026-10-11 | FETCHED | Law firm |
| [S457] | Glossary/blog sources (snippets) | MFN tiering and carve-outs | various | https://dannybloomstine.beehiiv.com/p/most-favored-nation-elections-how-funds-manage-tiered-access | 2026-10-11 | SNIPPET | Low-authority sources |
| [S458] | Cambridge Associates | ODD in Focus: Valuation | 2025-06-27 | https://publishedresearch.cambridgeassociates.com/wp-content/uploads/2025/06/2025-06-ODD-in-Focus-Valuation.pdf | 2026-10-11 | FETCHED | Consultant |
| [S459] | Bebeez / Private Equity Wire / Bloomberg Gov (snippets) | KKR attracts $23bn for North America Fund XIV | 2026-04-07 | https://bebeez.eu/2026/04/07/kkr-attracts-23-billion-us-dollars-for-for-north-america-fund-xiv-limited-partners-carry-on-a-strict-selection-of-general-partners/ | 2026-10-11 | SNIPPET | KKR release not read |
| [S460] | BNN Bloomberg (snippet) | KKR investment vehicle for mass affluent raises $1.8 billion | 2024-05-02 | https://www.bnnbloomberg.ca/kkr-investment-vehicle-for-mass-affluent-raises-1-8-billion-1.2068186 | 2026-10-11 | SNIPPET | Headline only; not used for numbers |
| [S461] | Sidley (snippet) | Regulatory Update: NAIC Summer 2021 National Meeting | 2021-09 | https://www.sidley.com/en/insights/newsupdates/2021/09/regulatory-update-naic-summer-2021-national-meeting | 2026-10-11 | SNIPPET | 6 to 20 designation categories |
| [S462] | KKR | The Total Portfolio Approach (web page, metadata) | 2026-02-26 | https://www.kkr.com/insights/total-portfolio-approach | 2026-10-11 | FETCHED | Date and authors from page metadata |
| [S463] | KKR | Total Portfolio Approach FAQ web page | 2026-07-29 | https://www.kkr.com/wealth/insights/total-portfolio-approach-faq | 2026-10-11 | FETCHED | Same content as S436 |
| [S464] | EQT (snippet) | EQT introduces new ELTIF evergreen fund | 2026-04-29 | https://eqtgroup.com/news/eqt-makes-infrastructure-more-accessible-to-individual-investors-across-europe-introduces-new-eltif-evergreen-fund-2026-04-29 | 2026-10-11 | SNIPPET | Competitor context |
| [S465] | KKR | kkr.com/wealth home and navigation (Alternatives Unlocked, 101 courses, model portfolios) | accessed 2026-10 | https://www.kkr.com/wealth | 2026-10-11 | FETCHED | Primary |

---

## 5. Gaps

1. **K-PEC and K-INFRA minimum investments.** Not stated in the 10-Ks. The subscription agreement exhibits are scanned images; kkrpec.com returned 403. Only KREST ($10,000 / $1m) is confirmed. Do not quote a K-PEC minimum.
2. **K-PRIME primary documents.** The prospectus and monthly report URLs now 404; the KID copy I found is not machine-readable. Fees, dealing frequency, redemption terms and current size are unverified.
3. **KKR ELTIF or LTAF.** No evidence found that KKR has launched either. EQT, StepStone and others have.
4. **KCM fee history periods.** The 10-K chart values ($757m, $490m, $184m averages) lost their period labels in text extraction.
5. **AIFMD II Annex V text from EUR-Lex.** EUR-Lex blocked automated access; the list comes from law firm summaries (consistent across Debevoise and others). ESMA guideline dates differ between sources (18 Dec 2025 vs 12 Mar 2026 in WS4).
6. **LTAF 90-day notice and monthly dealing.** From secondary summaries; COLL 15 not read directly.
7. **KCS use of AI.** No public KKR statement. Only a firm-wide AI platform job ad.
8. **"KKR Academies" format details.** Only Nuttall's remark; no KKR page describing the programme. The digital programme is "Alternatives Unlocked".
9. **ABF $6.1tn current-size figure.** Seen in a snippet of KKR's page but not in my extracted text; the $9.2tn 2029 forecast is confirmed.
10. **GII IV press release.** Read via search snippet only. GII V vs IV investor counts or re-up rates are not disclosed.
11. **Asian Fund V size and North America XIV KKR release.** Not read.
12. **Original Takahashi-Alexander and Kaplan-Schoar journal versions.** Read via a secondary paper and the NBER working paper.
13. **The brief's "40/30/30" and "Racim Allouani".** KKR's published models are 45/25/30 and 30/40/30. The TPA papers are by McVey, McNellis, Olinger (and Dai); I found no Racim Allouani authorship.
14. **NAIC bond RBC factors by designation.** The 6-to-20 category change is reported; exact factor values not verified.
15. **Capital Group fund terms after launch.** S426 is a pre-effective N-2/A from April 2025; final prospectus terms could differ slightly.

---

## 6. Interview angles

### 6.1 Technical things a KCS intern at KKR would learn that they could not easily learn elsewhere

1. **How to make a private equity fund legally "not a fund".** K-PEC uses co-GP Joint Ventures so its main asset is a GP interest, not an "investment security", passing the 1940 Act 40% test [S420]. Few firms explain this structure; Blackstone's BXPE and Apollo use other routes. A candidate who can explain the 40% test in one sentence will stand out.
2. **How the same deal is split between an institutional flagship and a retail vehicle.** First-tier and second-tier allocation, with K-PEC getting no priority [S420]. This is the core conflict that KCS must explain honestly to both sets of clients.
3. **Evergreen fee mechanics in exact numbers.** 1.25% plus 15% (PE) or 12.5% (infra) over a 5% hurdle with a high-water mark and 100% catch-up; 0.85% trail on S shares paid via KCM [S420, S421]. Being able to compute a year's performance fee is a real day-one skill.
4. **Liquidity engineering.** 5% quarterly gate, 5% early fee for 24 months, overflow tender at about 10% below NAV (K-PEC); 2% within 12 months (K-FIT); interval fund 5% to 25% fundamental policy with 10% target (Capital Group) [S420, S422, S426]. Each wrapper trades liquidity against private exposure.
5. **A retail fund built from KKR parts.** Capital Group U.S. Equity+ holds about 30% in K-PEC and 10% in KKR co-investments [S427]. Distribution partnerships can turn KKR products into ingredients.
6. **Why co-investment is a profit engine.** Fund-level deal fees are 100% offset to LPs, but KCM fees are not shared; co-investment creates fee income outside the offset [S425]. KCS's job of placing co-invest is tied directly to KCM's $930m fee line.
7. **Insurance capital maths.** $6bn of Ivy sidecar dry powder supports over $60bn of liabilities [S440]; NAIC factors from 0.03% to 12.5% on CLOs and 6.8% on collateral loans [S439]. KCS insurance specialists sell on capital efficiency, not just return.
8. **Institutional vs wealth wrappers for the same team.** DCIF: 0.6% to 0.8% fee, carry on cash yield above 4%, six-year lock [S432]. K-INFRA: 1.25% fee, 12.5% over 5%, quarterly 5% liquidity [S421]. Same infrastructure team, two price lists.
9. **TPA as a sales framework.** "Zero-based budgeting", reference portfolios, "minimum viable TPA", 10-30% annual distributions for recycling [S435, S436]. This is how KCS moves a client conversation from "buy Fund X" to "let us build your private markets programme".
10. **The LP's toolkit from the GP side.** Filling ILPA DDQ 2.0 section 5 (co-invest fees, syndication, co-underwriting) [S444]; the 2025 Performance Template's "with and without subscription facilities" IRR [S445]; MFN election windows [S456]; ODD's focus on NAV governance for evergreen funds [S458].
11. **European liquidity rules as product design constraints.** Two LMTs from Annex V, no swing-plus-dual only, in-kind only for professionals [S449]; ELTIF redemption sizing via notice period or liquid-asset floor [S447]. A London intern on K-PRIME would live with these.

### 6.2 Opinions a candidate could form (each defensible from the sources)

- "The K-Series is a distribution innovation more than an investment one. The deals are the same as the flagships; the innovation is the legal wrapper and the liquidity engineering." [S420, S421]
- "Interval funds and evergreen funds are not the same product. One promises a repurchase every quarter; the other allows the board to say no. Clients need to know which they own." [S420, S426]
- "Co-investment is where KCS, KCM and the deal teams meet. It lowers average fees for the client but can raise KKR's fee income, so transparency (ILPA DDQ section 5) matters." [S425, S444]
- "GII V's 13% step-up over GII IV is solid in a tough market, but the bigger story is that $45bn came across all infrastructure vintages, including perpetual vehicles like K-INFRA." [S430, S431]
- "TPA is KKR's intellectual answer to the 'solutions' business: it gives large clients a reason to hire one big multi-asset partner." [S435, S436]

### 6.3 Smart questions to ask interviewers

1. "When K-PEC and a flagship fund both want more of a deal than the first tier allows, how does KCS explain the second-tier allocation to a wealth platform's due diligence team?" [S420]
2. "For K-PRIME in Europe, which two Annex V tools did you choose under AIFMD II, and did the choice change how private banks distribute it?" [S449]
3. "How do the Capital Group interval funds change KCS's work with US advisers, given that Capital Group owns the adviser relationship?" [S426, S427]
4. "In the KKR Academies, what is the question advisers ask most often about liquidity gates?" [S440]
5. "On the insurance side, how much of KCS's conversation with an insurer CIO is about NAIC capital charges versus expected return?" [S438, S439]
6. "Is the TPA framework something KCS uses in live client mandates, or mainly as thought leadership to open doors?" [S435, S436]
7. "How does KCS decide which LPs see a co-investment from KCM first: commitment size, speed, or strategic relationship?" [S425, S444]

### 6.4 Watch-outs for the candidate

- Do not quote a K-PEC minimum investment; it is not in the filings I read.
- Do not say KKR has an ELTIF or LTAF; I found no evidence.
- Use "Alternatives Unlocked" for the digital platform and "KKR Academies" only as Nuttall's description of in-person adviser days.
- The DCIF terms are from 2021 and may have changed.
