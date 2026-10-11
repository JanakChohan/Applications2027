# WS4: The industry from zero, the fundraising sub-industry, and its regulation

Workstream 4. Source ID range S260 to S329. Researched 2026-10-11. Written for a reader with no prior knowledge of private markets.

How to read the tags:
- [Confirmed] = primary source, or two credible outlets agree.
- [Reported] = one credible source only.
- [Inferred] = my own reasoning, or a standard textbook definition that I did not re-verify against a source this session.

A warning on numbers: every data provider (PitchBook, Preqin, Bain, McKinsey) defines "private markets" and "fundraising" differently. Some count venture capital, some do not. Some count only closed-end funds. So the totals below do not add up to each other. Always quote the provider and the scope together.

---

## 1. Findings

### 1A. Private markets from scratch

#### 1A.1 What "alternative assets" are
- "Traditional" investments are listed shares (stocks), government and company bonds, and cash. You can buy and sell them every day on an exchange at a public price. [Inferred]
- "Alternative" investments are everything else that big investors buy: private equity (buying whole companies that are not on the stock market), private credit (lending directly to companies, without a bank or a bond market), infrastructure (toll roads, pipelines, data centres, power grids), real estate (offices, warehouses, flats), hedge funds, and natural resources. [Inferred, standard definition]
- Preqin's own definition of "alternatives" for its 2030 forecast covers private equity, private credit, infrastructure, real estate, hedge funds and natural resources. [Reported, S269]
- The defining feature is that the assets are illiquid. You cannot sell them quickly at a known price. In return, investors hope to earn an "illiquidity premium", a higher return than public markets. [Inferred]

#### 1A.2 The GP / LP structure (who is who)
- A private fund is usually a limited partnership. [Inferred, standard]
- The **General Partner (GP)** is the manager. Firms like KKR, Blackstone, Apollo and Carlyle act as GP. The GP picks the investments, runs them, and decides when to sell. [Inferred]
- The **Limited Partners (LPs)** are the investors who supply most of the money. They are "limited" because they cannot lose more than they put in and they do not run the fund. [Inferred]
- The GP also commits some of its own money to the fund (the "GP commitment"), so it has "skin in the game". ILPA lists "alignment of interest" as one of its three guiding principles, alongside governance and transparency. [Confirmed, S317]
- The contract between GP and LPs is the **Limited Partnership Agreement (LPA)**. Individual LPs often negotiate extra terms in a **side letter**. [Inferred]

#### 1A.3 How a closed-end fund works (the life cycle)
Think of it as a ten-year journey in four stages. [Inferred, standard model]
1. **Fundraising and commitment.** The GP markets the fund. LPs sign a promise (a "commitment") to give, say, $100 million when asked. No cash moves yet. The fund holds a "first close" and later a "final close".
2. **Investment period (roughly years 1 to 5).** When the GP finds a deal, it sends a **capital call** (also called a drawdown) asking each LP for its share. LPs must pay within days. Money not yet called is "dry powder" or "unfunded commitments".
3. **Harvest period (roughly years 4 to 10).** The GP improves the companies and then sells them (an "exit": a sale to another company, a sale to another fund, or a stock market listing / IPO).
4. **Distribution.** Cash from exits goes back to LPs. The fund usually has a 10-year life, often with extensions of 1 to 2 years.

Why this matters today: exits have been slow, so cash is not coming back. PitchBook says almost $5 trillion sits in funds that are 7 years old or older, which is 39% of total NAV as of December 2025. [Reported, S260] Bain counts roughly 32,000 unsold portfolio companies worth about $3.8 trillion. [Confirmed, S262, S326]

#### 1A.4 Fees: "2 and 20", hurdle, catch-up, waterfall
[Inferred, standard industry definitions; exact terms vary by fund]
- **Management fee (the "2")**: around 1.5% to 2% a year of committed capital during the investment period, often stepping down later to invested capital. Pays for salaries and running costs. Large LPs often negotiate lower rates.
- **Carried interest (the "20")**: the GP's share of profits, typically 20%.
- **Hurdle rate (preferred return)**: LPs must first earn a minimum return, commonly 8% a year, before the GP gets carry.
- **Catch-up**: once the hurdle is cleared, the GP receives a large share of the next profits until it has "caught up" to its 20% of total profit.
- **Waterfall**: the order in which cash is paid out. A "European" (whole-of-fund) waterfall pays carry only after LPs get all their money back plus the hurdle across the whole fund. An "American" (deal-by-deal) waterfall can pay carry deal by deal, which is better for the GP. ILPA's Principles have long favoured whole-of-fund waterfalls and a "clawback" (the GP pays back carry if later losses mean it was overpaid). ILPA Principles 2.0 (2011) added a Clawback appendix. [Confirmed for the appendix, S317]
- Placement agents typically charge success fees of around 2% to 2.5% of capital raised, with some charging more for hard raises. [Reported, low-quality secondary source, S322 snippet context; treat as indicative]

#### 1A.5 Performance metrics in plain English
[Inferred, standard definitions]
- **IRR (internal rate of return)**: the annualised return, taking timing into account. Returning money fast boosts IRR.
- **MOIC (multiple on invested capital)**: how many times your money you got back. $1 in, $2.5 out = 2.5x.
- **TVPI (total value to paid-in)**: (cash returned + value of what is still held) / cash paid in. The LP-level version of MOIC.
- **DPI (distributions to paid-in)**: cash actually returned / cash paid in. "Real money." DPI is today's most-watched metric because exits are slow.
- **RVPI (residual value to paid-in)**: value still held / cash paid in. TVPI = DPI + RVPI.
- **PME (public market equivalent)**: compares the fund with what the same cash flows would have earned in a stock index. Answers "did I beat the market for the extra risk and illiquidity?"
- Live evidence that DPI is the focus: Bain reports that distributions as a share of NAV were about 14% in 2025, and below 15% for four years running. [Confirmed, S262] McKinsey's 2026 report (via Dakota) says distributions fell to 6% of AUM versus a 2015 to 2019 average of 16%. [Reported, S261] Note: Bain's 2025 report described 2024 distributions as the lowest rate in over a decade (one reprint says 11%), which does not square neatly with "essentially flat at 14%" in the 2026 report. Treat the exact level as provider-specific. [Reported, S271]
- Bain cites an ILPA survey in which about two-thirds of LPs leaned towards waiting for a better MOIC rather than near-term liquidity, and 53% said undrawn commitments limit new PE commitments (up 15 percentage points). [Confirmed, S262]

#### 1A.6 How the four main asset classes differ
[Inferred, standard; figures sourced where given]
| Asset class | What it buys | Where return comes from | Typical risk | Notes |
|---|---|---|---|---|
| Private equity / buyout | Controlling stakes in companies | Growth, operational improvement, debt, selling at a higher multiple | High | Bain: 2025 buyout deal value up 44% to $904bn; exits up 47% to $717bn [Confirmed, S262] |
| Private credit | Loans to companies (direct lending, asset-based finance) | Interest income | Lower than equity, but leverage and opacity concerns | Preqin: $2.1tn in 2024, forecast $4.5tn by 2030 [Reported, S270] |
| Infrastructure | Essential physical assets (power, data centres, roads, fibre) | Long-term contracted or regulated cash flows | Lower to medium | Preqin: AUM around $3tn by end-2030 [Reported, S269] |
| Real estate | Buildings and land | Rent plus price growth | Medium; rate-sensitive | PitchBook: closed-end RE fundraising only $41.3bn in H1 2026, on track for weakest year since 2012 [Reported, S260] |

#### 1A.7 Alternative managers vs other financial firms
[Inferred]
- **Traditional asset managers (BlackRock, Vanguard)**: mostly run index funds and listed-stock/bond funds. Very low fees, huge scale, daily liquidity. BlackRock has been moving into alternatives by buying them: Global Infrastructure Partners (about $12.5bn, closed October 2024) and HPS Investment Partners (about $12bn all-stock, announced December 2024), and Preqin (about £2.55bn). [Reported, S290]
- **Hedge funds**: trade mostly liquid securities, often monthly or quarterly liquidity, aim for returns uncorrelated with markets.
- **Investment banks**: advise on deals (M&A, IPOs) and underwrite securities; they earn fees on transactions, not long-term management fees. They are the GP's counterparties and lenders. Some banks (Evercore, Lazard, PJT) also run placement and secondaries advisory businesses (see 1B).
- **Alternative asset managers (KKR, Blackstone, Apollo, Carlyle, Ares, Brookfield, EQT)**: run long-lived private funds, earn management fees plus carried interest, and increasingly own insurance companies and run retail products.

#### 1A.8 Who the LPs are
[Inferred, standard; no single 2026 breakdown found this session]
- Public and corporate pension funds (the largest group historically).
- Sovereign wealth funds (e.g. Gulf and Asian state funds).
- Insurance companies (growing fast because they want long-dated credit).
- Endowments and foundations (universities, charities).
- Family offices and funds of funds.
- Private wealth: high-net-worth and, increasingly, "mass affluent" individuals through feeder funds and evergreen vehicles.
- Bain: individual investors hold about 50% of global AUM ($275tn to $295tn) but only 16% of AUM held by alternative funds. This gap is the "democratisation" opportunity. [Reported, S293]

#### 1A.9 The denominator effect
- When public markets fall fast (as in 2022), the value of a pension fund's listed shares drops immediately, but private holdings are revalued only quarterly and more slowly. Private assets therefore become a bigger percentage of the total, even though nothing was bought. The fund may then be "over-allocated" and stop making new commitments. [Reported, S323]
- Eaton Vance's analysis of 2022 found prior PE outperformance was the top contributor, followed by lagged PE marks and pre-existing over-allocation. [Reported, S323]
- The problem persisted: S&P Global found 174 of 298 pension funds analysed were over-allocated to private equity in Q1 2025. [Reported, S324]
- PitchBook adds that institutional allocations are "bumping up against risk limits" and that negative net cash flows since 2022 have tested LPs. [Reported, S260]

#### 1A.10 Secondaries and continuation vehicles
- **LP-led secondary**: an LP sells its fund stake to a specialist buyer, usually at a price near NAV, to get cash early. [Inferred]
- **GP-led secondary / continuation vehicle (CV)**: the GP moves one or more prized assets from an old fund into a new vehicle. Old LPs can cash out or roll over; new investors come in. [Inferred]
- Evercore (H1 2026 review, July 2026): total secondary volume $121bn in H1 2026, up 19% year on year, the strongest first half on record. GP-led $65bn (+35%), LP-led $56bn (+4%). Full-year 2025 volume topped $226bn, more than 40% above 2024. High-quality buyout interests clearing at around 90% of NAV. Dedicated secondary dry powder about $194bn. [Confirmed, S267; FY2025 also reported as $240bn by a Ropes & Gray summary using a different dataset, S268]
- Evercore: "Single-asset continuation vehicles represented the largest share of GP-led activity." [Confirmed, S267]
- Bain: CV transaction value grew 62% year over year in 2025, but CVs were still less than 10% of exit value. [Confirmed, S262]
- ILPA has issued draft new continuation vehicle guidance (process integrity, election options, conflicts, pricing validation, transparency). Still a draft at time of writing. [Reported, S319]

#### 1A.11 Evergreen / semi-liquid funds
- These funds have no fixed end date. Investors can subscribe monthly and ask to redeem (usually quarterly) up to a cap, often 5% of the fund per quarter. Examples: non-traded BDCs (business development companies, US private credit vehicles), non-traded REITs, ELTIFs in Europe, LTAFs in the UK. [Inferred; caps confirmed in S278]
- Evercore: semi-liquid evergreen vehicles account for about $500bn of industry AUM. [Reported, S267]
- PitchBook: US evergreen PE AUM nearly doubled from $51.3bn (end-2024) to $99.3bn (Q1 2026), and "funnels more capital into the hands of the largest GPs with established wealth products." [Reported, S260]
- Stress test of the model in 2026: see 1A.14 (BDC redemptions).

#### 1A.12 Size of the industry
- PitchBook: private capital AUM nearly tripled from $6.1 trillion (2016) to $16.7 trillion (December 2025). [Reported, S260]
- Preqin "Private Markets in 2030" (16 October 2025): global alternatives AUM forecast to reach about $32 trillion by 2030. Preqin is now owned by BlackRock. [Confirmed, S269 plus multiple outlets]
- Preqin via Paul Weiss: PE AUM reached an all-time high in 2025 (exact figure truncated in extraction); PE dry powder $2.347tn at the latest reading, 25% of AUM in Q4 2025. [Reported, S266]
- McKinsey Global Private Markets Report 2025 ("Braced for shifting weather"): fundraising across all asset classes in 2024 fell to its lowest level since 2016. A secondary summary gives $589bn of closed-end commitments, down 24%. [Reported, S264; McKinsey site returned 503 so full report NOT READ]
- McKinsey Global Private Markets Report 2026: first chapter "Clearer view, tougher terrain" (private equity). Buyout and growth deals above $500m rose 44% to over $1 trillion in 2025, a record for that size. PE-backed exit value rose more than 40%. Closed-end PE fundraising down about 17% to roughly $616bn. [Reported, S261, S263] Its total AUM figure was not found.
- Bain Global Private Equity Report 2026 (published 24 February 2026): total private capital raised about $1.3 trillion in 2025, about even with 2024; buyout fundraising $395bn, down 16% (fourth straight annual decline); funds closed down 18% overall and 23% for buyout. [Confirmed, S262, S326]
- BCG: capital "remains concentrated in funds above $5B" (via Dakota summary). No BCG figures read directly. [Reported, S261]

#### 1A.13 Fundraising environment, 2024 to 2026 YTD
**2024**
- Bain's 2025 report: fundraising fell around 23% to 24% across private market asset classes; Bain blamed the "persistent liquidity situation" for LPs. [Reported, S271]
- McKinsey: lowest fundraising since 2016. [Reported, S264]
- PitchBook: median time to close a PE fund hit 18.6 months in H2 2024, versus 14.7 in 2023 and 11.2 in 2022. [Reported, secondary snippet; not directly read]

**2025**
- Bain: about $1.3tn total, flat; buyout $395bn, down 16%. Growth came from infrastructure and secondaries. [Confirmed, S262]
- Preqin (via Paul Weiss): global PE fundraising (ex-VC) $660.7bn in FY2025, down 9% from $728.3bn. 1,205 funds closed, down 26% from 1,632. Buyout funds took an average 18.5 months to close, down from 20.6 months in 2024. Q4 2025 was the weakest PE quarter in several years ($124bn). [Confirmed, S265]
- Cambridge Associates (via Dakota): fundraising "troughed in 2025 at roughly one-third of 2021 levels". [Reported, S261]

**2026 YTD (to 30 June 2026)**
- PitchBook (published 3 September 2026): $658.1bn raised across 1,499 funds in H1 2026. Trailing 12 months $1,348.0bn, down 12.7%, fund count down 37%. If the pace holds, 2026 will be the fifth straight annual decline. [Confirmed, S260]
- By strategy (trailing 12 months, PitchBook): PE $468.8bn (-12.1%), VC $183.1bn (-4.2%), real estate $90.7bn (-32.5%), real assets $137.3bn (-26.2%), private debt $309.1bn (+14.0%), secondaries $95.1bn (-20.6%). Private debt is the only strategy growing; H1 2026 debt fundraising up 27.3%. [Confirmed, S260]
- Preqin (via Paul Weiss, Q2 2026): average time to close fell to 15.7 months in H1 2026 from 19.1 months in FY2025; 82% of PE funds closed at or above target, the highest in at least six years; 7,739 funds on the road, the most in five years; only 284 PE funds closed in Q2, the fewest in any quarter for five years. [Confirmed, S266]

**Concentration ("flight to scale")**
- PitchBook: funds larger than $1bn took 78.2% of all private capital raised in H1 2026, up from 59.1% in 2021. In PE, 77% of capital since 2024 went to funds over $1bn. [Confirmed, S260]
- Preqin: the 10 largest funds closed in Q2 2026 took 49% of capital raised that quarter (46% in Q4 2025). [Confirmed, S265, S266]
- PitchBook: only 36 first-time PE funds closed in H1 2026, totalling $7.7bn. [Confirmed, S260]
- PitchBook's explanation: allocators gravitate "toward GPs with established track records and broad market validation rather than expending the resources required to underwrite smaller, less-proven vehicles." [Confirmed, S260]
- Bain: "Investors more than ever are focused on funds that have a clear, repeatable, and easily explained strategy." [Confirmed, S262]

#### 1A.14 Structural forces now

**(a) Retail and private wealth "democratisation"**
- US Executive Order 14330, "Democratizing Access to Alternative Assets for 401(k) Investors", signed 7 August 2025. It told the Department of Labor (DOL) to re-examine ERISA fiduciary guidance within 180 days, to consider rescinding the DOL's December 2021 private equity statement, and to work with the SEC. [Confirmed, S273]
- DOL proposed rule announced 30 March 2026: a process-based safe harbour for 401(k) fiduciaries selecting any "designated investment alternative", with six factors (performance, fees, liquidity, valuation, benchmarks, complexity). Comments were due 1 June 2026. [Confirmed, S272, S274] As of 11 October 2026 I found no evidence of a final rule. [Gap]
- H.R. 5748, the Retirement Investment Choice Act (Rep. Troy Downing, October 2025), would codify the order. [Reported, S273 context]
- SEC: roundtable on retail access to private/alternative investments on 4 March 2026. [Reported, S277] Around 30 September 2026 the SEC published proposals to widen the "accredited investor" definition for individuals: a FINRA-developed accredited investor exam (pass valid 10 years), plus FINRA Series 79, 86 and 87, US CPA licence, CFA charter and CFP certification. 60-day comment period after Federal Register publication. Press release 2026-96. [Reported, S275; Bloomberg Tax preview S276 PAYWALLED-NOT-READ]
- Chairman Paul Atkins: "accredited investor access to private offerings should not be limited solely to individuals satisfying financial thresholds." [Reported, S275]
- Bain projections (via CAIA): private wealth allocations to alternatives could grow from about $4tn (2022) to over $13tn by 2032. [Reported, S293]
- Europe: ELTIF 2.0 has produced 189 new ELTIFs since start-2024 (Morningstar), a record 113 launches in 2025 and about €34bn of assets at end-2025, up 55% (Scope). [Reported, S302]

**(b) Insurance and private credit convergence**
- Large managers own or partner with life insurers (Apollo with Athene, KKR with Global Atlantic, Brookfield, Blackstone partnerships). The insurer collects premiums and invests them in long-dated private credit originated by the manager. [Reported, S285; analyst framing, not primary disclosures]
- Apollo argues private credit is a market "of over $40 trillion", mostly investment grade, with only about $2tn being below-investment-grade levered lending. [Reported, S285] Critics say this counts all non-traded credit including bank loans, and that "private credit" as most people mean it is about $1.7tn to $3tn. [Reported, S286]
- The IMF (April 2024 GFSR) flagged that some insurers and pension funds have "significantly expanded" holdings of private credit and illiquid assets, and listed fragile borrowers, semi-liquid vehicles, multiple layers of leverage and stale valuations as vulnerabilities. [Reported, S287]

**(c) Private credit growth and the 2025 to 2026 stresses**
- Tricolor Holdings (US subprime auto lender) filed for Chapter 7 liquidation on 10 September 2025 in the Northern District of Texas. [Reported, S282]
- First Brands Group (US auto parts) filed for Chapter 11 around 28 September 2025 in the Southern District of Texas, with liabilities over $10bn and alleged double-pledging of invoices; the DOJ reportedly opened a criminal investigation. In August 2026 the judge rejected its plan and the case moved to Chapter 7 liquidation. [Reported, S283, S284]
- JPMorgan took a $170m loss on Tricolor. Jamie Dimon on the Q3 2025 call (14 October 2025): "I probably shouldn't say this, but when you see one cockroach, there are probably more." [Confirmed, S280, S281]
- Counter-view (BlueBay's Mark Dowding): Tricolor was "corporate fraud rather than an underlying symptom of credit market conditions." [Reported, S281]
- 2026 BDC redemptions: in Q1 2026 investors asked to withdraw $5.4bn from Blue Owl's two non-traded BDCs (OCIC about 22% of shares, OTIC about 41%). On 2 April 2026 Blue Owl enforced a 5% quarterly cap, joining Apollo, Ares and BlackRock. Apollo Debt Solutions received requests of 11.2% and honoured 5%. Blackstone's BCRED paid 100% of record requests of 7.9% of NAV. Earlier, in February 2026, Blue Owl Capital Corporation II ended quarterly redemption offers. More than $11bn left private credit funds over two quarters. The US Treasury convened regulators on private credit liquidity. [Reported, S278; some AltsWire figures do not reconcile internally, noted]
- Q2 2026: Blue Owl requests fell to $4.7bn; cap kept at 5%. Drivers cited: credit quality worries and AI disruption risk to software borrowers (software is 64% of OTIC). [Reported, single source S279]
- PitchBook contrast: closed-end private debt funds had a 24.1% distribution rate and record 2025 net cash flow of $39.5bn, behaving "differently from evergreen vehicles that have been battered by outflows." [Reported, S260]
- UK: the Bank of England launched a private markets "system-wide exploratory scenario" (SWES) in December 2025; scenario sent to participants 19 June 2026 (five-year severe global recession); final report expected early 2027. [Reported, S288]

**(d) AI, data centres and infrastructure capex**
- Meta and Blue Owl formed a joint venture for the Hyperion data centre campus in October 2025: Blue Owl funds 80%, Meta 20%; $27bn of bonds issued via Beignet Investor LLC, described as the largest private credit deal ever. Meta's lease renews every four years, which S&P called unusually short. [Reported, S289]
- Morgan Stanley estimated big tech would spend about $400bn on AI infrastructure in 2025. [Reported, S289]
- Preqin cites AI-related demand as a driver of infrastructure and PE growth to 2030. [Reported, S269]
- PitchBook: AI was 65.5% of US VC deal value in 2025. [Reported, S260]

**(e) GP consolidation and GP stakes**
- BlackRock bought GIP and HPS, "the two largest-ever acquisitions of alternative asset managers in less than a year". [Reported, S290]
- 2026: Nuveen's $13.5bn bid for Schroders (citing Schroders' $41.6bn of private debt and credit alternatives); reports of Ares in talks for Leonard Green. Campbell Lutyens reported record GP-stakes/GP transaction volumes in 2025, mostly minority deals. Morgan Stanley and Oliver Wyman forecast more than 1,500 asset manager M&A deals through 2029. [Reported, S291; Ares talks unconfirmed]
- GP stakes: specialist funds (e.g. Blue Owl GP Stakes, Goldman Petershill) buy minority stakes in alternative managers' fee streams. Navigator bought revenue-share interests in 17 managers from Stable for $195m in 2026. [Reported, S291]

**(f) Tokenisation**
- On 13 September 2022 Securitize launched a tokenised feeder giving exposure to KKR's Health Care Strategic Growth Fund II on the Avalanche blockchain, a Reg D 506(c) offering for accredited investors only. KKR called it the first time a KKR strategy was offered in digital format in the US. [Confirmed, S292]
- Preqin lists tokenisation and digital platforms among drivers of wider access. [Reported, S269]

#### 1A.15 Three (plus) competing views on the next 3 to 5 years
1. **"Structural growth via wealth and insurance" (bull case).** Preqin forecasts $32tn of alternatives AUM by 2030 [S269]; Apollo argues private credit is a $40tn+ market mostly investment grade [S285]; Bain sees private wealth allocations tripling to $13tn by 2032 [S293]. The industry becomes a mainstream part of retirement savings, helped by EO 14330 and SEC accredited investor reform. [Reported]
2. **"Maturity, tougher terrain, back to basics" (structural slowdown).** McKinsey 2026 argues shifts in deployment, returns, value creation and fundraising "previously considered to be episodic are more likely structural features of a maturing industry." [Reported, S263] PitchBook says PE "need[s] to go back to their guiding principles to jump-start the fundraising engine": buying, improving, and exiting at a profit in a reasonable time. [Reported, S260] Bain's "12 is the new 5" framing: deals need about 12% annual EBITDA growth versus about 5% historically. [Reported, S262 coverage] Winners will be the large, multi-strategy platforms; small and first-time managers struggle.
3. **"Hidden risk / correction" (sceptic case).** IMF warned private credit vulnerabilities "could become systemic" if growth continues under limited oversight [S287]. Dimon's "cockroach" remark [S280]. Critics of the $40tn claim [S286]. BDC gating in 2026 [S278]. BoE's SWES assumes a shock worse than the GFC [S288]. In this view, retail money arrives just as liquidity mismatches are exposed.
4. **(A fourth, middle view) "Liquidity reinvented".** Evercore: secondaries have evolved "from an episodic liquidity solution into a structural portfolio management channel" [S267]; continuation vehicles and evergreen funds become permanent plumbing. [Reported]

### 1B. The fundraising / investor relations / private wealth distribution sub-industry

#### 1B.1 History and roles
[Mostly Inferred, standard industry knowledge; specific facts sourced]
- In the 1980s to 1990s, GPs raised money mostly through partners' personal networks. As funds grew to tens of billions and LPs multiplied, big GPs built in-house **investor relations (IR) / client solutions** teams: relationship managers per region or client type, product specialists per strategy, and junior generalists. KKR's Global Client Solutions team, described in the candidate brief, is exactly this model.
- **Placement agents** are outside firms hired to raise funds, especially for mid-sized or first-time managers or to reach new LP types. Major names: Evercore (Private Capital Advisory), Campbell Lutyens, Park Hill (part of PJT Partners), Lazard, plus independents such as Rede Partners and Asante. PEI's ranking for the 12 months to May 2024 covered 38 agents raising $41bn of "new" capital (first-time LP relationships only). Rede says it ranked top in Europe and second globally in PEI's 2025 ranking. [Reported, S322, S325] Evercore calls its PCA team "the world's leading secondaries advisory business" (self-description). [Confirmed as a quote, S267]
- **Investment consultants / gatekeepers** advise LPs on which funds to back: Cambridge Associates, Mercer, Aon, Hamilton Lane, StepStone (the latter two also manage money directly as fund-of-funds and secondaries managers). [Inferred; no AUM figures gathered this session]
- **ILPA** (Institutional Limited Partners Association) is the LP trade body, with offices in Toronto, Washington DC and London. It writes best-practice standards. [Confirmed, S317]
  - ILPA Principles 1.0: September 2009. 2.0: January 2011 (added Clawback appendix). 3.0: June 2019, "Fostering Transparency, Governance and Alignment of Interests for General and Limited Partners". [Confirmed, S317] Principles 3.0 expanded from 24 to 44 pages and added topics such as GP-led secondaries and subscription lines of credit. [Reported, S317 search context]
  - ILPA DDQ: first 2013, updated 2016 and 2018; DDQ 2.0 plus a Diversity Metrics Template published November 2021, adding sections on succession planning, co-investment, GP-led secondaries, credit facilities, cybersecurity. Its ESG section is based on PRI's LP due diligence questionnaire. [Reported, S320]
  - ILPA Reporting Template v2.0 and new Performance Template: released January 2025. Reporting template applies to funds in their investment period in Q1 2026 and funds starting on or after 1 January 2026; first delivery covers Q1 2026. Performance Template data capture starts Q1 2026 with first delivery in Q1 2027. Voluntary. [Confirmed, S318]
  - I found no "Principles 4.0" or 2025 Principles update. [Gap]
- **Feeder fund platforms**: iCapital (founded 2013) and CAIS let wealth advisers put many clients into one feeder that invests in a GP's fund, handling paperwork, minimums and reporting. iCapital raised $820m in July 2025 at a reported $7.5bn valuation; aggregator data says it serves 100,000+ advisers and passed $200bn of platform assets in 2024 (not primary). [Reported, S321]
- **Wirehouses** (Morgan Stanley, Merrill, UBS, Wells Fargo) and private banks distribute evergreen funds and feeders to wealthy clients. [Inferred]

#### 1B.2 How LPs select managers
[Inferred, standard process; ILPA facts sourced]
1. Screening (track record, strategy fit, team stability).
2. Investment due diligence (deal-by-deal attribution, PME, DPI, reference calls).
3. **Due diligence questionnaire (DDQ)**, often the ILPA DDQ 2.0 format [S320].
4. **Operational due diligence (ODD)**: separate review of back office, valuation policy, cybersecurity, compliance, fund administrator, auditor. The FCA's March 2025 review of private market valuation practices found weaknesses in valuation governance records, conflicts identification, independence and ad hoc revaluations. [Reported, S310]
5. Legal negotiation: LPA terms, **side letters** (fee breaks, reporting rights, ESG, co-investment rights, excuse rights), and **MFN (most-favoured-nation)** clauses that let an LP claim terms given to similar or smaller LPs.
6. Commitment and ongoing monitoring (quarterly reports, AGMs, LPAC seats).

#### 1B.3 What LPs value today
- **DPI and liquidity**: see Bain and McKinsey distribution data above. [Confirmed, S262]
- **Clear, repeatable strategy**: Bain quote above. [Confirmed, S262]
- **Co-investment** (investing directly alongside the fund, usually with no or low fees): PitchBook tracks $37.5bn of co-investment fundraising in the 12 months to June 2026. [Confirmed, S260]
- **Fee discounts and scale**: inferred from concentration data; large LPs consolidate relationships with fewer GPs. PitchBook notes "ongoing consolidation of LP relationships". [Reported, S260]
- **Transparency and standardised reporting**: ILPA templates [S318].
- **ESG and DEI reporting**: built into ILPA DDQ 2.0 [S320]; politically contested in the US in 2025 to 2026. [Inferred]

### 1C. Regulation (exact names and dates)

#### 1C.1 European Union
- **AIFMD, Directive 2011/61/EU**: signed 8 June 2011; entry into force 21 July 2011 (some sources say 22 July); transposition deadline 22 July 2013. Created a marketing "passport" for EU managers selling EU funds to professional investors across the EU from 22 July 2013. Non-EU managers rely on national private placement regimes (NPPRs) under Article 42. [Confirmed, S300]
- **AIFMD II, Directive (EU) 2024/927**: published in the Official Journal 26 March 2024; entered into force 15 April 2024; transposition and application deadline 16 April 2026 (some reporting deadlines later). [Confirmed, S296, S294]
  - **Loan origination**: harmonised rules for loan-originating AIFs (those mainly originating loans, or whose originated loans are at least 50% of NAV). Leverage caps of 175% (open-ended) and 300% (closed-ended); 20% single-borrower limit where the borrower is a financial undertaking, AIF or UCITS; retain 5% of each originated loan that is sold; ban on "originate-to-distribute"; must be closed-ended unless the manager shows its liquidity system fits. Grandfathering for funds set up before 15 April 2024 until 16 April 2029 (or indefinitely if no new capital raised). [Confirmed, S295, S297]
  - **Liquidity management tools (LMTs)**: open-ended AIFs must choose at least two from a list in Annex V (gates, notice periods, redemption fees, swing pricing, dual pricing, anti-dilution levy, redemption in kind, side pockets; suspension available to all). [Confirmed, S295, S294] Commission adopted LMT RTS on 17 November 2025; ESMA LMT guidelines formally published 12 March 2026. [Reported, S298]
  - **Delegation**: more detailed reporting to regulators on delegation and sub-delegation; at least two full-time EU-resident people running the business. [Reported, S294]
  - **NPPR tightening**: non-EU managers and funds must not be in jurisdictions on the EU AML high-risk list or EU tax non-cooperative list. [Reported, S294]
  - Implementation: some states (e.g. Belgium) had not published transposing law by the deadline. [Reported, S294] In October 2025 the Commission said non-essential Level 2 measures would be delayed until after 1 October 2027. [Reported, S298]
- **Cross-border distribution package: Directive (EU) 2019/1160 and Regulation (EU) 2019/1156**: published OJ 12 July 2019; in force 1 August 2019; applied from 2 August 2021. Harmonised definition of **pre-marketing** (testing interest before a fund is set up or notified, without an offer). EU managers must notify their home regulator within two weeks of starting pre-marketing. Any subscription by professional investors within 18 months of pre-marketing is treated as marketing, which effectively blocks later reliance on **reverse solicitation** (where the investor approaches the manager on its own initiative). [Confirmed, S299]
- **ELTIF 2.0, Regulation (EU) 2023/606**: applies from 10 January 2024; opens European Long-Term Investment Funds more widely to retail (removed €10,000 minimum, widened eligible assets). RTS adopted as Commission Delegated Regulation (EU) 2024/2759, published OJ 25 October 2024 (in force next day), covering redemption policies and LMTs. [Confirmed, S301, S302; the brief's "RTS adopted 2025" appears to be incorrect, the RTS were published in 2024]
- **MiFID II product governance**: MiFID II (Directive 2014/65/EU) applied from 3 January 2018; requires manufacturers and distributors to define a target market for each product. [Inferred; dates not re-verified this session]

#### 1C.2 United Kingdom
- **UK AIFM regime**: the UK implemented AIFMD in 2013 (The Alternative Investment Fund Managers Regulations 2013) and kept it as "onshored" law after Brexit. NPPR remains the route for overseas funds. [Reported, S304]
- **Reform**: HM Treasury consultation and FCA Call for Input published 7 April 2025, closing 9 June 2025. Proposed three tiers of AIFM by NAV. [Confirmed, S304] FCA **CP26/28 "The UK AIFM Regime"** published July 2026 (Debevoise dated 23 July 2026; another source says proposals came out 14 July 2026); comments due 14 October 2026. Tiers: small below £750m NAV, medium £750m to £5bn, large above £5bn. New "ALTS" sourcebook. NPPR kept with limited changes; UK AIFMs marketing UK AIFs move from 20-day pre-approval to simple notification. HMT draft statutory instrument comments also due 14 October 2026. Policy statement 2027; rules in force 2028. Companion papers: CP26/27 (remuneration) and CP26/26 (FRAME, replacing Annex IV reporting). [Confirmed, S303]
- **LTAF (Long-Term Asset Fund)**: rules in force 15 November 2021; originally a Non-Mass Market Investment. **PS23/7** (29 June 2023) recategorised LTAF units as Restricted Mass Market Investments from 3 July 2023, opening them to retail investors (with protections), self-select DC pensions and SIPPs. [Confirmed, S305, S306]
- **Financial promotions exemptions (high-net-worth and sophisticated investors)**: on 31 January 2024 thresholds rose to £170,000 income or £430,000 net assets; after industry backlash, a new order in force 27 March 2024 restored £100,000 and £250,000 and reinstated the "two or more unlisted investments" criterion for self-certified sophisticated investors. Statements under the January rules stayed valid until 30 January 2025. [Confirmed, S307]
- **Consumer Duty**: applied to open products from 31 July 2023 and closed products from 31 July 2024. [Confirmed, S308]
- **SMCR** (Senior Managers and Certification Regime): extended to FCA solo-regulated firms (which include most UK private markets managers) on 9 December 2019 (PS19/20). [Confirmed, S309]
- **FCA private market valuations review**: published 5 March 2025, 36 firms surveyed. [Reported, S310]
- **Mansion House Accord**: announced 13 May 2025. 17 workplace pension providers (covering about 90% of active DC savers) committed to invest at least 10% of DC default funds in private markets by 2030, with at least 5% in the UK. Could unlock up to £50bn, about £25bn in the UK. [Confirmed, S315]
- **Pension Schemes Act 2026**: Bill introduced 5 June 2025; Royal Assent 29 April 2026 after extended ping-pong. Compromise limits any mandation power to the levels in the voluntary Accord. Most provisions commence later. [Confirmed, S316]

#### 1C.3 United States
- **Regulation D**: Rule 506(b) allows private offerings with no general solicitation (up to 35 non-accredited investors); Rule 506(c), effective 23 September 2013 under the JOBS Act, allows general solicitation if all buyers are verified accredited investors. [Confirmed, S314]
- **Accredited investor** (individuals): income over $200,000 ($300,000 joint) in each of the last two years, or net worth over $1m excluding home. August 2020 amendments added professional-licence routes (Series 7, 65, 82). [Confirmed for thresholds, S314; 2020 amendment Reported, S275 context] 2026 proposals: see 1A.14.
- **Marketing Rule (Rule 206(4)-1)**: adopted 22 December 2020; effective 4 May 2021; compliance date 4 November 2022. Replaced the advertising and cash solicitation rules. [Confirmed, S313]
- **Private Fund Adviser Rules**: adopted August 2023 (quarterly statements, audits, restricted activities, preferential treatment, adviser-led secondaries). Vacated in full by the Fifth Circuit on 5 June 2024 in *National Association of Private Fund Managers v. SEC*. [Confirmed, S311, S312]
- **Retail access agenda 2025 to 2026**: EO 14330 (7 Aug 2025); DOL proposal (30 Mar 2026); SEC roundtable (4 Mar 2026); SEC accredited investor proposals (~30 Sep 2026). [Confirmed/Reported as tagged above]

#### 1C.4 Regulation timeline table
| Date | Jurisdiction | Measure | What it does | Source |
|---|---|---|---|---|
| Sep 2009 | Global (LP body) | ILPA Principles 1.0 | First LP best-practice terms | S317 |
| Jan 2011 | Global | ILPA Principles 2.0 | Adds clawback appendix | S317 |
| 8 Jun 2011 | EU | AIFMD (2011/61/EU) signed | Regulates managers of alternative funds | S300 |
| 22 Jul 2013 | EU / UK | AIFMD transposition deadline; passport live | EU marketing passport for EU AIFMs | S300 |
| 23 Sep 2013 | US | Rule 506(c) effective | General solicitation to accredited investors | S314 |
| Jun 2019 | Global | ILPA Principles 3.0 | Transparency, governance, alignment | S317 |
| 1 Aug 2019 | EU | Cross-border distribution Dir. 2019/1160 in force | Pre-marketing regime | S299 |
| 9 Dec 2019 | UK | SMCR extended to solo-regulated firms | Personal accountability for senior managers | S309 |
| 22 Dec 2020 | US | SEC Marketing Rule adopted | Modern advertising rules | S313 |
| 2 Aug 2021 | EU | Pre-marketing rules apply | 2-week notification; 18-month rule | S299 |
| 15 Nov 2021 | UK | LTAF rules in force | UK open-ended long-term fund | S306 |
| Nov 2021 | Global | ILPA DDQ 2.0 | Standard due diligence questionnaire | S320 |
| 4 Nov 2022 | US | Marketing Rule compliance date | | S313 |
| 3 Jul 2023 | UK | PS23/7 in force | LTAF to retail (RMMI) | S305 |
| 31 Jul 2023 | UK | Consumer Duty (open products) | Good outcomes for retail customers | S308 |
| Aug 2023 | US | Private Fund Adviser Rules adopted | | S311 |
| 10 Jan 2024 | EU | ELTIF 2.0 (Reg. 2023/606) applies | Retail-friendlier long-term funds | S301, S302 |
| 31 Jan 2024 | UK | HNW/sophisticated thresholds raised | £170k / £430k | S307 |
| 26 Mar 2024 | EU | AIFMD II published in OJ | | S296 |
| 27 Mar 2024 | UK | HNW thresholds reverted | £100k / £250k | S307 |
| 15 Apr 2024 | EU | AIFMD II in force | Loan origination, LMTs, delegation | S296 |
| 5 Jun 2024 | US | Fifth Circuit vacates Private Fund Adviser Rules | | S311 |
| 31 Jul 2024 | UK | Consumer Duty (closed products) | | S308 |
| 25 Oct 2024 | EU | ELTIF RTS (Del. Reg. 2024/2759) published | Redemption/liquidity detail | S301 |
| Jan 2025 | Global | ILPA Reporting & Performance Templates released | | S318 |
| 5 Mar 2025 | UK | FCA valuation practices review | | S310 |
| 7 Apr 2025 | UK | HMT consultation + FCA Call for Input on AIFM reform | | S304 |
| 13 May 2025 | UK | Mansion House Accord | 10% private markets by 2030, 5% UK | S315 |
| 5 Jun 2025 | UK | Pension Schemes Bill introduced | | S316 |
| 7 Aug 2025 | US | Executive Order 14330 | Alternatives in 401(k)s | S273 |
| 17 Nov 2025 | EU | Commission adopts LMT RTS under AIFMD II | | S298 |
| 1 Jan 2026 | Global | ILPA Reporting Template v2.0 applies to new funds | | S318 |
| 4 Mar 2026 | US | SEC roundtable on retail access to alternatives | | S277 |
| 12 Mar 2026 | EU | ESMA LMT guidelines published | | S298 |
| 30 Mar 2026 | US | DOL proposed 401(k) safe harbour | | S272, S274 |
| 16 Apr 2026 | EU | AIFMD II transposition deadline | | S294, S296 |
| 29 Apr 2026 | UK | Pension Schemes Act 2026 Royal Assent | | S316 |
| Jul 2026 | UK | FCA CP26/28 (new UK AIFM regime) | 3 tiers by NAV | S303 |
| ~30 Sep 2026 | US | SEC accredited investor proposals | Exam, CFA/CPA/CFP routes | S275 |
| 14 Oct 2026 | UK | CP26/28 and HMT draft SI comment deadline | | S303 |
| 2027 (exp.) | UK | FCA AIFM policy statement; BoE SWES final report | | S303, S288 |
| 2028 (exp.) | UK | New UK AIFM regime in force | | S303 |
| 16 Apr 2029 | EU | AIFMD II loan-origination grandfathering ends | | S297 |

---

## 2. Key numbers table

| Metric | Value | As-of date | Source | Confidence |
|---|---|---|---|---|
| Private capital AUM (PitchBook) | $16.7tn (from $6.1tn in 2016) | Dec 2025 | S260 | Reported |
| Alternatives AUM forecast (Preqin) | ~$32tn | 2030 | S269 | Confirmed |
| Private credit AUM (Preqin) | $2.1tn to $4.5tn forecast | 2024 to 2030 | S270 | Reported |
| Total private capital raised (Bain) | ~$1.3tn, flat YoY | 2025 | S262 | Confirmed |
| Buyout fundraising (Bain) | $395bn, -16% | 2025 | S262 | Confirmed |
| Closed-end PE fundraising (McKinsey) | ~$616bn, -17% | 2025 | S261 | Reported |
| Global PE fundraising ex-VC (Preqin) | $660.7bn, -9% | FY2025 | S265 | Confirmed |
| PE funds closed (Preqin) | 1,205, -26% | FY2025 | S265 | Confirmed |
| Private capital raised H1 (PitchBook) | $658.1bn, 1,499 funds | H1 2026 | S260 | Confirmed |
| Private capital raised TTM (PitchBook) | $1,348.0bn, -12.7% | 30 Jun 2026 | S260 | Confirmed |
| Private debt TTM fundraising (PitchBook) | $309.1bn, +14.0% | 30 Jun 2026 | S260 | Confirmed |
| Share to funds >$1bn (PitchBook) | 78.2% (59.1% in 2021) | H1 2026 | S260 | Confirmed |
| First-time PE funds (PitchBook) | 36 funds, $7.7bn | H1 2026 | S260 | Confirmed |
| Top 10 funds' share of quarter (Preqin) | 49% | Q2 2026 | S266 | Confirmed |
| Avg months to close, buyout (Preqin) | 18.5 (20.6 in 2024) | FY2025 | S265 | Confirmed |
| Avg months to close, PE (Preqin) | 15.7 (19.1 FY2025) | H1 2026 | S266 | Confirmed |
| PE funds on the road (Preqin) | 7,739 | Q2 2026 | S266 | Confirmed |
| Distributions / NAV (Bain) | ~14%, <15% for 4 years | 2025 | S262 | Confirmed |
| Distributions / AUM (McKinsey) | 6% vs 16% 2015-19 avg | 2025 | S261 | Reported |
| Unsold PE companies (Bain) | ~32,000, ~$3.8tn | early 2026 | S262 | Confirmed |
| Aging NAV in funds 7+ years (PitchBook) | ~$5tn, 39% of NAV | Dec 2025 | S260 | Reported |
| Buyout deal value (Bain) | $904bn, +44% | 2025 | S262 | Confirmed |
| Buyout-backed exit value (Bain) | $717bn, +47% | 2025 | S262 | Confirmed |
| Secondary volume (Evercore) | $121bn, +19% | H1 2026 | S267 | Confirmed |
| Secondary volume (Evercore) | >$226bn, +40%+ | FY2025 | S267 | Confirmed |
| GP-led / LP-led (Evercore) | $65bn / $56bn | H1 2026 | S267 | Confirmed |
| Semi-liquid evergreen AUM (Evercore) | ~$500bn | mid-2026 | S267 | Reported |
| US evergreen PE AUM (PitchBook) | $51.3bn to $99.3bn | end-2024 to Q1 2026 | S260 | Reported |
| Blue Owl BDC redemption requests | $5.4bn (Q1), $4.7bn (Q2) | 2026 | S278, S279 | Reported |
| Standard BDC redemption cap | 5% per quarter | 2026 | S278 | Reported |
| Meta Hyperion financing | $27bn, Blue Owl 80% / Meta 20% | Oct 2025 | S289 | Reported |
| New ELTIFs since 2024 | 189 | early 2026 | S302 | Reported |
| ELTIF assets | ~€34bn, +55% | end-2025 | S302 | Reported |
| Mansion House Accord | 17 providers, 10% private by 2030, 5% UK | 13 May 2025 | S315 | Confirmed |
| UK AIFM tiers (proposed) | <£750m / £750m-£5bn / >£5bn | Jul 2026 | S303 | Confirmed |
| AIFMD II loan-origination leverage cap | 175% open / 300% closed | from 16 Apr 2026 | S295, S297 | Confirmed |
| iCapital funding round | $820m at ~$7.5bn valuation | Jul 2025 | S321 | Reported |

---

## 3. Verbatim quotes actually read

| Quote | Speaker / document | Date | Source |
|---|---|---|---|
| "Funds larger than $1 billion continue to capture a greater share of total fundraising, reaching 78.2% in H1 2026, up from 59.1% in 2021." | PitchBook Q2 2026 Global Private Market Fundraising Report (Juan Mier) | 3 Sep 2026 | S260 |
| "We read this as allocators gravitating toward GPs with established track records and broad market validation rather than expending the resources required to underwrite smaller, less-proven vehicles." | PitchBook Q2 2026 report | 3 Sep 2026 | S260 |
| "Growing inflows from retail investors are becoming the main source of new capital" | PitchBook Q2 2026 report (PE section) | 3 Sep 2026 | S260 |
| "Deal and exit value surged reassuringly in 2025 in a narrow recovery powered by megadeals." | Bain Global Private Equity Report 2026 | Feb 2026 | S262 |
| "Investors more than ever are focused on funds that have a clear, repeatable, and easily explained strategy." | Bain Global Private Equity Report 2026 | Feb 2026 | S262 |
| "Single-asset continuation vehicles represented the largest share of GP-led activity, concentrated in high quality assets." | Evercore H1 2026 Secondary Market Review | Jul 2026 | S267 |
| "reinforcing secondaries' evolution from an episodic liquidity solution into a structural portfolio management channel." | Evercore H1 2026 Secondary Market Review | Jul 2026 | S267 |
| "I probably shouldn't say this, but when you see one cockroach, there are probably more." | Jamie Dimon, JPMorgan Q3 2025 earnings call | 14 Oct 2025 (reported 15 Oct) | S280 |
| "corporate fraud rather than an underlying symptom of credit market conditions." | Mark Dowding, BlueBay, on Tricolor | Oct 2025 | S281 |
| "accredited investor access to private offerings should not be limited solely to individuals satisfying financial thresholds" | SEC Chairman Paul Atkins, statement | ~30 Sep 2026 | S275 |
| "financial sophistication can scarcely be measured by income or net worth alone." | Paul Atkins, remarks | Feb 2026 (quoted Oct 2026) | S275 |
| "Within two weeks of starting to pre-market, an EU AIFM must send an informal letter or email to its home regulator" | AIMA on the Cross-Border Distribution Directive | 2019 article | S299 |
| "with the sole purpose of transferring those loans or exposures to third parties" (originate-to-distribute ban wording) | AIFMD II text as quoted by Hogan Lovells | 14 Mar 2024 | S295 |
| "At least 5 percent of these portfolios will be ringfenced for the UK." | HM Treasury / gov.uk, Mansion House Accord | 13 May 2025 | S315 |
| "Through our Plan for Change, we are choosing to back British businesses and British workers." | Chancellor Rachel Reeves | 13 May 2025 | S315 |
| "the FCA does not propose to make malus and clawback mandatory" | Debevoise summary of CP26/27 | 23 Jul 2026 | S303 |
| "form the essence of an effective private equity partnership" (on alignment, governance, transparency) | ILPA Principles page | accessed Oct 2026 | S317 |
| "closed-end private equity fundraising down 17% year over year to roughly $616B" | Dakota News summarising McKinsey 2026 | 24 Feb 2026 | S261 |

---

## 4. Source table

| ID | Outlet | Title | Pub date | URL | Accessed | Status | Confidence note |
|---|---|---|---|---|---|---|---|
| [S260] | PitchBook | Q2 2026 Global Private Market Fundraising Report | 2026-09-03 | https://pitchbook.brightspotcdn.com/74/45/4f36da844589a606c5cea79f2aeb/q2-2026-global-private-market-fundraising-report.pdf | 2026-10-11 | FETCHED (PDF text extracted) | Primary data provider |
| [S261] | Dakota News | McKinsey, Cambridge, BCG review 2025 PE data | 2026-02-24 | https://news.dakota.com/p/mckinsey-cambridge-bcg-review-2025-pe-data | 2026-10-11 | FETCHED | Secondary summary of reports |
| [S262] | Bain & Company | Global Private Equity Report 2026: Outlook, gaining traction | 2026-02 | https://www.bain.com/insights/outlook-gaining-traction-global-private-equity-report-2026 | 2026-10-11 | FETCHED | Primary |
| [S263] | Azalea (Temasek-linked) | McKinsey Global Private Markets Review 2026 summary | 2026 | https://www.azalea.com.sg/investor-education/mckinsey-global-private-markets-review-2026 | 2026-10-11 | FETCHED | Secondary summary |
| [S264] | McKinsey | Global Private Markets Report 2025: Braced for shifting weather | 2025 | https://www.mckinsey.com/industries/private-equity/our-insights/global-private-markets-report-2025 | 2026-10-11 | SNIPPET (site returned 503) | Not read in full |
| [S265] | Paul, Weiss (Preqin data) | PE Fundraising at a Glance Q4 2025 | early 2026 | https://www.paulweiss.com/media/mqvfp5lw/pe_fundraising_at_a_glance_q4_2025.pdf | 2026-10-11 | FETCHED | Preqin data compiled by law firm |
| [S266] | Paul, Weiss (Preqin data) | PE Fundraising at a Glance Q2 2026 | mid-2026 | https://www.paulweiss.com/media/05uhvzek/pe_fundraising_at_a_glance_q2_2026.pdf | 2026-10-11 | FETCHED | Preqin data |
| [S267] | Evercore | H1 2026 Secondary Market Review | 2026-07 | https://www.evercore.com/wp-content/uploads/2026/07/Evercore-H1-2026-Secondary-Market-Review.pdf | 2026-10-11 | FETCHED | Primary (adviser) |
| [S268] | Ropes & Gray | Secondaries update full year 2025 | 2026-03 | https://www.ropesgray.com/-/media/files/alerts/2026/03/secondaries-update-full-year-2025.pdf | 2026-10-11 | SNIPPET | Different dataset |
| [S269] | Preqin / Business Wire | Preqin Releases Private Markets in 2030 Report | 2025-10-16 | https://www.businesswire.com/news/home/20251016075672/en/Preqin-Releases-Private-Markets-in-2030-Report | 2026-10-11 | SNIPPET (403) | Multiple outlets agree on $32tn |
| [S270] | Alternative Credit Investor | Global alts AUM to hit $32tn by 2030 | 2025-10-16 | https://alternativecreditinvestor.com/2025/10/16/global-alts-aum-to-hit-32tn-by-2030/ | 2026-10-11 | SNIPPET | |
| [S271] | Chronograph | Top takeaways from Bain's 2025 PE report | 2025 | https://www.chronograph.pe/top-takeaways-from-bains-2025-private-equity-report/ | 2026-10-11 | SNIPPET | |
| [S272] | US Department of Labor | EBSA news release (proposed rule) | 2026-03-30 | https://www.dol.gov/newsroom/releases/ebsa/ebsa20260330 | 2026-10-11 | SNIPPET (403) | Primary, not fully read |
| [S273] | White House / GovInfo | EO 14330 Democratizing Access to Alternative Assets for 401(k) Investors | 2025-08-07 | https://www.whitehouse.gov/presidential-actions/2025/08/democratizing-access-to-alternative-assets-for-401k-investors/ | 2026-10-11 | SNIPPET | Primary |
| [S274] | Gibson Dunn / Sidley | DOL proposes safe harbor for selection of DIAs | 2026-04 | https://gibsondunn.com/dol-proposes-safe-harbor-for-selection-of-designated-investment-alternatives-in-401k-plans | 2026-10-11 | SNIPPET | Law firm |
| [S275] | Mayer Brown | Proposed expansions to the accredited investor definition for natural persons | 2026-10-02 | https://www.mayerbrown.com/zh-hans/insights/publications/2026/10/proposed-expansions-to-the-accredited-investor-definition-for-natural-persons | 2026-10-11 | FETCHED | Law firm; SEC release not read |
| [S276] | Bloomberg Tax | SEC Eyes 'Accredited Investor' Change to Expand Market Access | 2026-09-25 | https://news.bloombergtax.com/securities-law/sec-eyes-accredited-investor-change-to-expand-market-access | 2026-10-11 | PAYWALLED-NOT-READ | |
| [S277] | Proskauer | SEC holds roundtable on the retailization of private/alternative investments | 2026-03 | https://www.proskauer.com/alert/sec-holds-roundtable-on-the-retailization-of-privatealternative-investments-a-hint-of-the-agencys-direction | 2026-10-11 | SNIPPET | |
| [S278] | AltsWire | Blue Owl caps withdrawals as private credit exodus intensifies | 2026-04-02 | https://altswire.com/blue-owl-caps-withdrawals-as-private-credit-exodus-intensifies/ | 2026-10-11 | FETCHED | Some internal figures do not reconcile |
| [S279] | The Standard (HK) / Reuters | Blue Owl keeps withdrawal limits even as redemption pressure modestly eases | 2026-07 (approx.) | https://www.thestandard.com.hk/finance/article/336246/Blue-Owl-keeps-withdrawal-limits-even-as-redemption-pressure-modestly-eases | 2026-10-11 | SNIPPET | Single source |
| [S280] | Fortune | Jamie Dimon issues private credit warning | 2025-10-15 | https://fortune.com/2025/10/15/jamie-dimon-issues-private-credit-warning-when-you-see-one-cockroach-there-are-probably-more | 2026-10-11 | FETCHED | |
| [S281] | Alternative Credit Investor | 'Cockroach' fears overblown after Tricolor and First Brands fallout | 2025-10-27 | https://alternativecreditinvestor.com/2025/10/27/cockroach-fears-overblown-after-tricolor-and-first-brands-fallout/ | 2026-10-11 | FETCHED | |
| [S282] | Cleary Gottlieb | Tricolor: The Road to Ruin | 2025/26 | https://content.clearygottlieb.com/corporate/global-restructuring-insights/tricolor-the-road-to-ruin/ | 2026-10-11 | SNIPPET | |
| [S283] | Business Standard | First Brands files for bankruptcy protection with liabilities over $10 bn | 2025-09-29 | https://www.business-standard.com/amp/companies/news/first-brands-files-for-bankruptcy-protection-with-liabilities-over-10-bn-125092901274_1.html | 2026-10-11 | SNIPPET | |
| [S284] | Truck Parts & Service | First Brands judge rejects plan, sending company to liquidation | 2026-08 | https://www.truckpartsandservice.com/business/finance/article/15833339/judge-orders-chapter-7-liquidation-for-first-brands-group | 2026-10-11 | SNIPPET | Year inferred as 2026 |
| [S285] | Apollo | Insights: private credit as >$40tn market | 2025 | https://www.apollo.com/insights-news/insights/2025/12/a-financial-system-built-for-purpose | 2026-10-11 | SNIPPET | Interested party |
| [S286] | Paul Kedrosky (blog) | Private credit talks back | 2025 | https://paulkedrosky.com/private-credit-talks-back/ | 2026-10-11 | SNIPPET | Commentary |
| [S287] | IMF | Global Financial Stability Report, April 2024 (private credit chapter) | 2024-04-16 | https://www.imf.org/en/Publications/GFSR/Issues/2024/04/16/global-financial-stability-report-april-2024 | 2026-10-11 | SNIPPET | Primary; quotes via coverage |
| [S288] | AIMA / Regulation Tomorrow | BoE private markets SWES scenario | 2026-06 | https://www.regulationtomorrow.com/2026/06/boe-launches-the-scenario-phase-of-the-private-markets-system-wide-exploratory-scenario/ | 2026-10-11 | SNIPPET | |
| [S289] | NPR (via WLRN) | Meta is building a massive data center: why it's fueling fears of an AI bubble | 2025-12-05 | https://www.wlrn.org/npr-breaking-news/2025-12-05/meta-is-building-a-massive-data-center-why-its-fueling-fears-of-an-ai-bubble | 2026-10-11 | SNIPPET | |
| [S290] | American Banker (Bloomberg) | BlackRock buys credit firm HPS in $12 billion all-stock deal | 2024-12 | https://asreport.americanbanker.com/articles/blackrock-buys-credit-firm-hps-in-12-billion-all-stock-deal | 2026-10-11 | SNIPPET | |
| [S291] | AI-CIO / Alternative Credit Investor | Asset manager consolidation continues; Private credit consolidation continues | 2026-05 | https://alternativecreditinvestor.com/2026/05/19/private-credit-consolidation-continues/ | 2026-10-11 | SNIPPET | Ares/Leonard Green unconfirmed |
| [S292] | Business Wire | Securitize launches fund providing tokenized exposure to KKR fund | 2022-09-13 | https://www.businesswire.com/news/home/20220913005384/en/ | 2026-10-11 | SNIPPET | Press release |
| [S293] | CAIA (citing Bain) | Young money: quantifying the private wealth management opportunity | 2025-01-13 | https://caia.org/blog/2025/01/13/young-money-quantifying-private-wealth-management-opportunity/ | 2026-10-11 | SNIPPET | Bain original not read |
| [S294] | Mondaq (Altius) | 16 April 2026: AIFMD II finally takes effect | 2026-04 | https://www.mondaq.com/fund-management-reits/1774368/16-april-2026-aifmd-ii-finally-takes-effect | 2026-10-11 | FETCHED | Belgian law firm |
| [S295] | Hogan Lovells (Cadwalader redirect) | Liquidity management, loan origination and credit funds under AIFMD II | 2024-03-14 | https://www.hlc.com/en/publications/liquidity-management-loan-origination-and-credit-funds-under-aifmd-ii | 2026-10-11 | FETCHED | |
| [S296] | Freshfields | Client briefing AIFMD II | 2024-04-10 | https://corporatecrime.freshfields.com/497c98/contentassets/e2addb75cb2c4696b9cc146a85d75977/client-briefing-aifmd-ii_10-april-2024.pdf | 2026-10-11 | SNIPPET | |
| [S297] | BCLP | AIFMD II leverage limits and single borrower exposure restriction | 2024 | https://www.bclplaw.com/en-US/events-insights-news/aifmd-ii-leverage-limits-and-single-borrower-exposure-restriction.html | 2026-10-11 | SNIPPET | |
| [S298] | Regulation Tomorrow (Norton Rose) | AIFMD II LMT RTS / ESMA guidelines | 2026 | https://www.regulationtomorrow.com/?p=56668 | 2026-10-11 | SNIPPET | |
| [S299] | AIMA | New rules for pre-marketing funds and reverse solicitation | 2019 | https://www.aima.org/article/new-rules-for-pre-marketing-funds-and-reverse-solicitation.html | 2026-10-11 | FETCHED | Trade body |
| [S300] | European Parliament OEIL / Hedgeweek | AIFMD 2011 procedure; AIFM Directive to come into force 21 July | 2011 | https://oeil.europarl.europa.eu/oeil/en/document-summary?id=1158669 | 2026-10-11 | SNIPPET | |
| [S301] | Maples / Regulation Tomorrow | ELTIF 2.0 RTS Delegated Regulation enters into force | 2024-10 | https://maples.com/knowledge/eltif-2-0-rts-delegated-regulation-enters-into-force | 2026-10-11 | SNIPPET | |
| [S302] | Morningstar / Scope (via Green Man) / EFAMA | The State of ELTIFs 2026; ELTIF market grew 55% in 2025 | 2026 | https://www.morningstar.com/en-uk/lp/european-long-term-investment-funds | 2026-10-11 | SNIPPET | |
| [S303] | Debevoise & Plimpton | The UK's new regulatory landscape: new rules on AIFM regime, remuneration and fund reporting | 2026-07-23 | https://www.debevoise.com/insights/publications/2026/07/the-uks-new-regulatory-landscape-new-rules-on-aifm | 2026-10-11 | FETCHED | |
| [S304] | Latham & Watkins / Paul Hastings | FCA and HM Treasury consult on proposals to reform UK AIFM regulation | 2025-04 | https://www.lw.com/en/insights/2025/04/FCA-and-HM-Treasury-Consult-on-Proposals-to-Reform-UK-AIFMs-Regulation | 2026-10-11 | SNIPPET | |
| [S305] | FCA | PS23/7: Broadening retail access to the long-term asset fund | 2023-06-29 | https://www.fca.org.uk/publications/policy-statements/ps23-7-broadening-retail-access-long-term-asset-fund | 2026-10-11 | SNIPPET | Primary |
| [S306] | AIMA | UK Long Term Asset Fund (LTAF) | n.d. | https://www.aima.org/regulation/keytopics/loan-fund-vehicles/uk-ltaf.html | 2026-10-11 | SNIPPET | |
| [S307] | Goodwin / HSF / Burges Salmon | HNW and sophisticated investor exemptions changes reversed | 2024-03 | https://www.burges-salmon.com/articles/102j2v1/high-net-worth-and-sophisticated-investor-exemptions-changes-reversed | 2026-10-11 | SNIPPET | Multiple firms agree |
| [S308] | Womble Bond Dickinson / Hogan Lovells | Consumer Duty deadlines | 2023/24 | https://www.womblebonddickinson.com/uk/node/11113 | 2026-10-11 | SNIPPET | |
| [S309] | FCA | Optimising SMCR: PS19/20 | 2019 | https://www.fca.org.uk/news/news-stories/optimising-senior-managers-and-certification-regime-policy-statement-19-20-and-feedback-cp-19-4 | 2026-10-11 | SNIPPET | Primary |
| [S310] | FCA | Private market valuation practices (multi-firm review) | 2025-03-05 | https://www.fca.org.uk/publications/multi-firm-reviews/private-market-valuation-practices | 2026-10-11 | SNIPPET | Primary, not fully read |
| [S311] | Morrison Foerster | Fifth Circuit vacates SEC private fund adviser rules | 2024-06-12 | https://www.mofo.com/resources/insights/240612-fifth-circuit-vacates-sec-private-fund-adviser-rules | 2026-10-11 | SNIPPET | |
| [S312] | SEC | Announcement regarding Private Fund Advisers rules | 2024-10-31 | https://www.sec.gov/announcement-regarding-private-fund-advisers-rules | 2026-10-11 | SNIPPET | Primary |
| [S313] | Foley Hoag | Marketing Rule's transition period set to expire | 2022-10 | https://foleyhoag.com/news-and-insights/publications/alerts-and-updates/2022/october/marketing-rules-transition-period-set-to-expire-sec-enforcement-to-follow/ | 2026-10-11 | SNIPPET | |
| [S314] | SEC | Small entity compliance guide: eliminating the prohibition against general solicitation | 2013 | https://www.sec.gov/info/smallbus/secg/general-solicitation-small-entity-compliance-guide | 2026-10-11 | SNIPPET | Primary |
| [S315] | GOV.UK (HM Treasury) | Pension schemes back British growth | 2025-05-13 | https://www.gov.uk/government/news/pension-schemes-back-british-growth | 2026-10-11 | FETCHED | Primary |
| [S316] | Clifford Chance / Burges Salmon / Hymans | Pension Schemes Bill gains Royal Assent; Pension Schemes Act 2026 | 2026-04/05 | https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2026/04/pension-scheme-bill-gains-royal-assent.pdf | 2026-10-11 | SNIPPET | Several firms agree on 29 Apr 2026 |
| [S317] | ILPA | ILPA Principles | n.d. | https://ilpa.org/ilpa-principles/ | 2026-10-11 | FETCHED | Primary; body text partly placeholder |
| [S318] | ILPA / Citco | ILPA Templates FAQs v1.1; ILPA reporting and new performance template | 2025 | https://ilpa.org/wp-content/uploads/2025/04/ILPA-Templates-FAQs-v1.1.pdf | 2026-10-11 | SNIPPET | |
| [S319] | ILPA | Draft new Continuation Vehicle (CV) guidance | 2026 | https://ilpa.org/resources-tools/resource-library/draft-new-continuation-vehicle-cv-guidance/ | 2026-10-11 | SNIPPET | Draft |
| [S320] | Haynes Boone / ILPA | Fund finance impact of ILPA DDQ 2.0 and Diversity Metrics Template | 2021-11-15 | https://www.haynesboone.com/news/alerts/fund-finance-impact-of-ilpa-ddq-2-and-diversity-metrics-template | 2026-10-11 | SNIPPET | |
| [S321] | AltsWire | iCapital to allocate $820M capital raise to acquisitions, tech | 2025-07 | https://altswire.com/icapital-to-allocate-820m-capital-raise-to-acquisitions-tech-enhancements/ | 2026-10-11 | SNIPPET | Platform-size figures from aggregators |
| [S322] | Private Equity International | Top private equity placement agents | 2024 | https://www.privateequityinternational.com/top-private-equity-placement-agents/ | 2026-10-11 | SNIPPET | Likely partly paywalled |
| [S323] | Eaton Vance (Morgan Stanley) | Deconstructing the denominator effect | n.d. | https://eatonvance.com/insights/articles/deconstructing-the-denominator-effect.html | 2026-10-11 | SNIPPET | |
| [S324] | S&P Global Market Intelligence | Pension funds record overallocation to private equity in Q1 2025 | 2025-04/05 | https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/5/more-than-half-of-pension-funds-exceed-private-equity-allocation-targets-89164143 | 2026-10-11 | SNIPPET | |
| [S325] | Rede Partners | Rede ranked top fundraiser in Europe in PEI Placement Agent Ranking 2025 | 2025 | https://www.rede-partners.com/news-insights-database/pei-awards-2025 | 2026-10-11 | SNIPPET | Self-reported |
| [S326] | Bain (Germany press release) | Global PE Report 2026 press release | 2026-02-24 | https://www.bain.com/de/ueber-uns/presse/pressemitteilungen/germany/2026/global-pe-report-2026/ | 2026-10-11 | SNIPPET | Primary |

---

## 5. Gaps

- McKinsey Global Private Markets Report 2025 and 2026: site returned errors; total AUM figures and full fundraising tables not read. Only secondary summaries used.
- BCG private markets report: no direct read.
- DOL 401(k) rule: no evidence of a final rule as of 11 October 2026. Status should be re-checked in the Federal Register.
- SEC accredited investor proposals: SEC press release 2026-96 not read directly; vote date (~30 September 2026) inferred from Mayer Brown. Other same-day SEC proposals on registered funds (e.g. limits on closed-end funds holding private funds) not verified.
- AIFMD II: which member states transposed on time (beyond Belgium being late) not established.
- UK: exact CP26/28 publication date (14 vs ~23 July 2026) differs between sources.
- ILPA: no confirmation of any Principles update after 3.0 (2019). Draft CV guidance content not read.
- Placement agent league tables for Evercore, Campbell Lutyens, Park Hill, Lazard: not found. Consultant AUM/AUA (Cambridge, Mercer, Aon, Hamilton Lane, StepStone): not gathered.
- CAIS platform size: not found. iCapital platform size only from aggregators.
- LP-type breakdown of global private capital (share from pensions, SWFs, insurers, wealth): no 2026 figure found.
- Bain distribution rates: 2025 report (11% for 2024, per a reprint) and 2026 report (~14% "essentially flat") are hard to reconcile.
- Blue Owl Q1 2026 OCIC percentages in AltsWire do not reconcile with the $5.4bn total.
- MiFID II (3 January 2018) and UK AIFM Regulations 2013 dates are from my background knowledge, not re-verified this session.
- First Brands conversion to Chapter 7: year of the August ruling inferred as 2026.
- Fee terms (2 and 20, 8% hurdle) are standard textbook norms, not drawn from a 2026 survey.

---

## 6. Interview angles

**Why this matters for KCS specifically**
- KCS is the "fundraising and distribution" engine. Every trend above lands on its desk: concentration favours big platforms like KKR; private wealth is "becoming the main source of new capital" (PitchBook); insurance-linked capital (Global Atlantic) is a structural edge; secondaries and CVs give LPs liquidity. A candidate can say: "The industry has stopped growing in aggregate but the big multi-strategy firms keep taking share, so the client solutions function is where that share is won."

**Opinions a candidate could hold (and defend)**
1. "Flight to scale is structural, not cyclical." Evidence: 78.2% of capital to $1bn+ funds; only 36 first-time PE funds in H1 2026. Counter: emerging-manager share rose in VC.
2. "DPI is the new IRR." LPs are cash-starved; distributions under 15% of NAV for four years (Bain). GPs who return cash (via exits, CVs, NAV loans) win re-ups.
3. "Retail is the growth engine, but 2026 BDC gating shows product design matters." Liquidity terms, valuation transparency and adviser education are now part of the job.
4. "Regulation is turning from restriction to access." EO 14330, DOL safe harbour, SEC accredited investor reform, ELTIF 2.0, LTAF, Mansion House Accord and the Pension Schemes Act 2026 all widen the investor base. AIFMD II and the BoE SWES are the counterweight on credit.

**Smart questions to ask KKR people**
- "How is KCS splitting coverage between institutional LPs and the private wealth channel now that wealth is a main source of new capital?"
- "How did the Q1 2026 BDC redemption wave change how you talk to wealth advisers about liquidity terms?"
- "With AIFMD II's loan-origination rules live from April 2026, has it changed how KKR structures European private credit products for EU investors?"
- "How are UK DC pension schemes, after the Mansion House Accord and the Pension Schemes Act 2026, approaching KKR? Through LTAFs, or other vehicles?"
- "Do LPs ask for the new ILPA reporting and performance templates on KKR's 2026 vintage funds?"
- "How do you see the role of KCS in working with Capital Markets on syndication, given continuation vehicles and co-investment demand?"

**Facts worth memorising (high leverage, exact dates)**
- AIFMD II: Directive (EU) 2024/927, OJ 26 Mar 2024, in force 15 Apr 2024, apply 16 Apr 2026.
- ELTIF 2.0: Regulation (EU) 2023/606, applies 10 Jan 2024.
- SEC Private Fund Adviser Rules: adopted Aug 2023, vacated by Fifth Circuit 5 Jun 2024.
- Marketing Rule compliance: 4 Nov 2022.
- EO 14330: 7 Aug 2025. DOL proposal: 30 Mar 2026.
- Mansion House Accord: 13 May 2025, 17 providers, 10% / 5%.
- Pension Schemes Act 2026: Royal Assent 29 Apr 2026.
- UK AIFM reform: FCA CP26/28 (Jul 2026), new regime expected 2028.
- Consumer Duty: 31 Jul 2023. LTAF retail access: 3 Jul 2023.
