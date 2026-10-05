# WS4: Financial Market Infrastructure from zero, plus UK capital markets, FX and clearing regulation

Prepared for: LSEG Business Management Summer Internship 2027 (Markets: London Stock Exchange, LSEG FX, Tradeweb, Turquoise, LCH)
Research date: 2026-10-05. Source IDs S150 to S219 only.
Tags: [Confirmed] = read in a primary or official source that I fetched. [Reported] = from a secondary source or a search snippet I did not fully read. [Inferred] = my own reasoning, no source says it directly.

Corrections to the brief (read these first):
1. The first Eurobond (Autostrade, July 1963) was lead-managed from London by S G Warburg, but it was listed on the Luxembourg Stock Exchange, not in London. Do not say "first Eurobond listed in London" in interview. [Confirmed on issuer, date, size and lead manager via ICMA S174; listing venue Reported via S175]
2. FCA PS24/14 is the bond and derivatives transparency policy statement (5 November 2024). It is not the document that appointed the tape provider. The bond tape provider is ETS Connect UK (Etrading Software), authorised May 2026, live 22 June 2026. [Confirmed S155, S156]
3. The prospectus regime policy statement is PS25/9 (15 July 2025), in force 19 January 2026. Your guess was correct. [Confirmed S151]
4. PISCES policy statement is PS25/6 (June 2025). LSE's PISCES venue is called the Private Securities Market (PSM). [Confirmed S152; PSM name Reported S154, and confirmed in LSEG H1 2026 results S195]
5. FX turnover is $9.6 trillion a day, UK share 37.8% (not 38%). [Confirmed S162, S163]

---

## 1) Findings

### 4A. Financial market infrastructure (FMI) from zero

#### 4A.1 What the main types of FMI are (plain English)

Think of a financial market like a giant marketplace. FMIs are the "plumbing": the shops, the tills, the receipts and the delivery vans. They do not usually take bets themselves. They make it possible for others to trade safely.

| Type | What it does in one line | Example in LSEG | Example competitors |
|---|---|---|---|
| Exchange (in law, a "regulated market" or RM) | A rule-based place where securities are listed (admitted) and traded, with the strictest rules. | London Stock Exchange Main Market | Euronext, Deutsche Boerse, Nasdaq, NYSE (ICE) |
| MTF (multilateral trading facility) | A trading venue run under lighter rules than an exchange; brings many buyers and sellers together under non-discretionary rules. | Turquoise (equities MTF); AIM and the International Securities Market (ISM) are MTFs operated by LSE [ISM as MTF Reported S176] | Cboe Europe, Aquis |
| OTF (organised trading facility) | A venue for bonds and derivatives where the operator has some discretion over how orders meet. [Inferred from general knowledge; definition not re-verified this pass] | Not a focus here | Interdealer brokers |
| CCP (central counterparty, a "clearing house") | Steps into the middle of a trade: becomes the buyer to every seller and the seller to every buyer, so if one side defaults the other still gets paid. Collects margin (collateral) to cover this risk. | LCH (LCH Ltd in London, LCH SA in Paris): SwapClear, ForexClear, RepoClear, CDSClear | CME Clearing, Eurex Clearing, ICE Clear |
| CSD (central securities depository) | Keeps the official electronic record of who owns which securities and moves them from seller to buyer at settlement. | Not LSEG's main business in the UK (UK CSD is Euroclear UK and International) [Inferred, general knowledge] | Euroclear, Clearstream |
| Trade repository (TR) | Collects reports of derivatives trades so regulators can see risk building up. Bank of England lists TR supervision on its site. [Confirmed that BoE has a TR page, S184 site navigation] | UnaVista (LSEG) [Inferred, general knowledge] | DTCC, Regis-TR |
| Index provider | Designs and calculates indices (for example the FTSE 100), and licenses them to fund managers who build index funds and ETFs. | FTSE Russell | S&P Dow Jones Indices, MSCI |
| Market data vendor | Collects, cleans and redistributes prices, news and reference data to traders and analysts on screens and via data feeds. | LSEG Data & Analytics (Workspace) | Bloomberg, S&P Global Market Intelligence, FactSet |

Key point: LSEG owns several of these at once (exchange, MTF, CCP, index, data). That "vertical" mix is why it is described as a "financial markets infrastructure and data" group rather than an exchange. [Inferred]

#### 4A.2 The trade lifecycle (step by step)

1. Pre-trade data: before trading, investors look at prices, quotes, news and analytics. Data vendors and venues sell this. (LSEG Data & Analytics, LSE market data.)
2. Execution: the buyer and seller agree a trade on a venue (exchange, MTF, RFQ platform like Tradeweb, FX platform like FXall) or directly "over the counter" (OTC).
3. Clearing: the trade is confirmed and, if centrally cleared, a CCP like LCH becomes the counterparty to both sides and collects margin.
4. Settlement: cash and securities actually change hands at a CSD (or, for FX, through a system like CLS). Under the UK's planned T+1 cycle this must happen no later than one business day after the trade, from 11 October 2027. [Confirmed S158]
5. Post-trade reporting: trades are published (transparency) and reported to the regulator (transaction reporting) or to a trade repository. Consolidated tapes bring the published trade data together in one feed. [Confirmed for bond tape S155]

The JD says LSEG Markets helps customers "across the trade life cycle, ensuring compliance and efficiency in clearing and reporting obligations". That maps directly to steps 2 to 5. [Confirmed, JD]

#### 4A.3 Basic market distinctions

- Primary market: where new securities are created and sold for the first time to raise money (an IPO of shares, or a new bond issue). The issuer gets the cash. LSE's listing and debt capital markets teams work here.
- Secondary market: where existing securities are traded between investors afterwards. The issuer gets no new money, but a liquid secondary market makes investors willing to buy in the primary market.
- Lit vs dark: on a lit venue, orders are visible to everyone before trading (pre-trade transparency). On a dark pool, orders are hidden until after execution, which helps big investors trade without moving the price. Turquoise runs both lit and dark (Turquoise Plato) books. [Inferred, general knowledge; Turquoise volume split not found S198]
- Order book (CLOB, central limit order book) vs RFQ (request for quote): an order book continuously matches anonymous buy and sell orders by price and time (how most shares trade). In RFQ, a client asks a few dealers for a price and picks the best (how most bonds, swaps and much FX trade, and Tradeweb's core model). LSE 24 will mix both: the LSEG release says it "intends to draw on elements of central limit order book and request-for-quote functionality". [Confirmed S196]
- OTC vs exchange-traded: OTC means negotiated directly between two parties, often a bank and a client (most FX, most bonds, most swaps). Exchange-traded means standardised products traded on a venue (shares, futures). After the 2008 crisis, G20 rules pushed standard OTC derivatives into central clearing, which is why LCH SwapClear is so large. [Inferred, general knowledge]

#### 4A.4 Who the customers are

| Customer | What they want from FMIs |
|---|---|
| Issuers (companies, governments, supranationals) | A place to list and raise capital cheaply, a deep investor base, visibility, an index inclusion (FTSE). |
| Banks and dealers (sell side) | Venues to trade and hedge, clearing to cut capital and margin costs, data to price trades. |
| Asset managers (buy side, e.g. pension funds, fund houses) | Best execution, low trading cost, reliable data, index licences for passive funds. |
| Hedge funds and proprietary trading firms | Speed, liquidity, data feeds, access to clearing. BCG says non-banks will take about 30% of trading volumes by 2030. [Reported S186] |
| Corporates (treasurers) | FX execution to hedge currency exposure, debt listing (for example on ISM). |
| Retail brokers | Access to UK shares, ETPs and data; extended hours (LSE 24). |

#### 4A.5 How FMIs make money

- Transaction fees: a small fee per trade (equity trading, Tradeweb, FX).
- Clearing fees and net treasury income: CCPs charge per trade cleared and also earn interest on margin they hold. [Inferred, general knowledge]
- Listing fees: admission fees and annual fees from issuers.
- Data and connectivity: real-time price feeds, terminals, reference data. This is subscription income and very sticky.
- Index licensing: fees, often based on assets tracking the index.

Evidence of the shift to subscriptions: LSEG's CEO said in July 2026 "Growth in our subscription businesses is accelerating." [Confirmed S195] Oliver Wyman says data and technology are now 30% of FMI sector revenue, up from 21% five years earlier. [Confirmed S185]

#### 4A.6 How LSEG differs from a bank, an asset manager and Bloomberg

- vs a bank: a bank lends, takes deposits and trades with its own balance sheet (it can lose money on positions). LSEG runs the venues and data that banks use. LCH does manage default risk, but it is a risk mutualiser, funded by members' margin and default fund, not a lender. [Inferred]
- vs an asset manager: an asset manager invests clients' money and earns a fee on assets. LSEG (through FTSE Russell) licenses the index that passive funds track, and sells them data, but does not manage the money. [Inferred]
- vs Bloomberg: Bloomberg is a private company built around its terminal and news. LSEG is listed on the LSE and combines data with regulated market infrastructure (venues and clearing). Bloomberg and LSEG are the two largest market data vendors, followed by S&P Global Market Intelligence. [Confirmed ranking S188, S189]

#### 4A.7 Structural forces now

1. Shift to data and subscriptions. Global market data spend rose 6.5% to a record $49.2bn in 2025 (Burton-Taylor). [Confirmed S188] It was $42bn in 2023, when Burton-Taylor said AI had "elevated the value of market data". [Confirmed S189]
2. Electronification of fixed income and FX. Coalition Greenwich reports electronic trading at about 44% of US investment-grade corporate bond volume in 2024, with Tradeweb at about 34% share vs MarketAxess 37%. [Reported S190] FX spot share of turnover rose to 31% in 2025 (from 28%) and LSEG FX average daily volume was $530bn in H1 2025, up 14.2%. [Confirmed BIS S163; LSEG figure Reported S198]
3. AI as threat and opportunity. Oliver Wyman: enterprise AI threatens about $12bn (9%) of FMI revenue, mostly undifferentiated analytics and data, but creates about $9bn of new revenue and over 20% cost reduction potential. [Confirmed S185] LSEG's answer: "LSEG Everywhere", delivering AI-ready data via MCP and partnerships with Amazon Quick and Google Gemini; 17,000 active users of AI Search in Workspace. [Confirmed S195]
4. Cloud and concentration risk. The UK critical third parties (CTP) regime started 1 January 2025; first designations took effect 13 July 2026. [Confirmed S170] Those designated were AWS, Google Cloud, Microsoft and Oracle. [Reported S171]
5. Tokenisation and digital assets. The Digital Securities Sandbox (DSS) came into force 8 January 2024 and opened 30 September 2024. [Reported S169; S168] LSEG notes a "Digital Securities Depository collaboration with HSBC on DIGIT". [Confirmed S195] Bank of England is consulting on "permitting tokenised assets as eligible collateral for CCPs". [Confirmed S184]
6. Private markets growth. PISCES lets private company shares trade at intermittent events; Mansion House Accord (13 May 2025) commits signatories to 10% of default funds in private markets by 2030, half in the UK. [Confirmed PISCES S152; Accord Reported S181] LSE PSM held its first auction on 25 March 2026. [Reported S154]
7. Passive investing and indexing. Index providers benefit as money moves to index funds. [Inferred; no sourced share figure this pass, see Gaps]
8. Clearing mandates and geopolitics. EMIR 3 forces some EU firms to hold an "active account" at an EU CCP from 25 June 2025, to reduce reliance on London (LCH). The EU extended UK CCP equivalence to 30 June 2028. [Reported S161; Confirmed S160]
9. Buy-side pressure on data fees. The FCA wholesale data market study (29 February 2024) found "users may be paying higher prices for the data they buy than if competition was working more effectively", but ruled out significant intervention. [Confirmed S165]
10. Consolidated tapes. UK bond tape live 22 June 2026; equity tape procurement early 2027, live "in 2027 or early 2028". [Confirmed S155, S157] A tape is a cheaper, public alternative for some trade data, a mild competitive threat to venue data revenues. [Inferred]

#### 4A.8 Three (plus one) competing views on the next 3 to 5 years

View 1: "Steady compounding, data and AI winners" (Oliver Wyman base case). FMI revenue pool grows about 8% a year to around $200bn by 2030 (bull case $230bn). Fastest growth: listed derivatives, commodities and digital assets. Winners focus on defensible core businesses rather than broad diversification after $88bn of data and tech acquisitions. [Confirmed S185; $88bn Reported via snippet]

View 2: "Disintermediation" (Oliver Wyman AI-headwinds and tokenisation risks; Morgan Stanley and Oliver Wyman). Growth slows to about 6% a year in an AI-headwinds case; tokenisation could shift 35% of current revenue (about $45bn) to new token-native infrastructure; incumbents face disintermediation in post-trade. [Confirmed S185] Morgan Stanley and Oliver Wyman see tokenised real-world assets at $2.3tn by 2030 in a base case, mostly collateral mobility. [Reported S191] The Bank of England frames this cautiously: technology can be adopted but trust must be built. [Confirmed S184]

View 3: "Non-banks and regulation reshape the client base" (BCG; FCA; EU). BCG says non-bank financial institutions will take about 20% of corporate and investment banking revenues and 30% of trading volumes by 2030: "NBFIs are no longer peripheral players". [Confirmed S186] Meanwhile regulators push down data costs (FCA study, consolidated tapes) and the EU pulls euro clearing away from London (EMIR 3). Venues must court proprietary traders and fight for regulatory share. [Inferred from S160, S165, S157]

View 4: "Financial data and markets infrastructure keeps modernising, with Big Tech as partner or rival" (McKinsey). McKinsey says the industry is "thriving" but disruption is forcing strategic change, with Big Tech partnering with incumbents. [Reported S187, page returned HTTP 503 so not read]

Interview takeaway: these views are not mutually exclusive. LSEG's own bet (Workspace AI, LSEG Everywhere, LSE 24, PSM, DIGIT) is a hedge across all of them. [Inferred]

---

### 4B. The role's sub-industry and regulation (UK capital markets, FX, clearing)

#### 4B.1 History in five steps

- 27 October 1986, "Big Bang": fixed commissions scrapped, foreign firms allowed to buy UK brokers, firms allowed to be both broker and dealer, and floor trading replaced by screens. [Reported S178]
- 1 November 2007, MiFID: EU rules allowed competition between exchanges and MTFs, which is how venues like Turquoise and Chi-X emerged. [Dates Reported S203; competition effect Inferred]
- 3 January 2018, MiFID II/MiFIR: more transparency, research unbundling, share and derivatives trading obligations, more reporting. [Reported S203]
- January 2021, Brexit: EU share trading moved from London to Amsterdam; Amsterdam averaged EUR 9.2bn a day in January 2021 vs London EUR 8.6bn, making it Europe's top share trading centre. [Reported S179]
- 2023 to 2026, UK rebuilds: share trading obligation scrapped (29 August 2023), listing rules rewritten (29 July 2024), prospectus regime replaced (19 January 2026), PISCES (June 2025), bond tape (June 2026), T+1 planned (11 October 2027). [Confirmed S167, S150, S151, S152, S155, S158]

#### 4B.2 Listings: UK Listing Rules (UKLR)

- FCA PS24/6 published 11 July 2024; rules in force 29 July 2024. [Confirmed S150]
- What it does: "removing our 'premium' and 'standard' listing segments in favour of a new commercial companies category for equity shares." [Confirmed S150] The category is commonly abbreviated ESCC (equity shares in commercial companies). [Reported, practitioner usage; acronym not seen in the fetched FCA text]
- The FCA called it "the most significant changes to the UK's listing regime in over 3 decades". [Confirmed S150]
- Relevance to LSEG: fewer hurdles (e.g. no mandatory shareholder votes on most large deals, dual-class share structures easier [Reported S202 law firm summaries, not fully read]) to win IPOs back from New York and Amsterdam.

#### 4B.3 Prospectus regime: POATRs

- Public Offers and Admissions to Trading Regulations 2024 (POATRs) replace the UK Prospectus Regulation. FCA final rules in PS25/9 (and PS25/10 for public offer platforms), both 15 July 2025. In force 19 January 2026. [Confirmed S151]
- PS25/9 creates the new Prospectus Rules: Admissions to Trading on Regulated Markets sourcebook (PRM). [Confirmed S151]
- Detail such as the 75% threshold for further issues without a prospectus was not shown on the page I read; see Gaps.

#### 4B.4 PISCES

- Legislation: The Financial Services and Markets Act 2023 (Private Intermittent Securities and Capital Exchange System Sandbox) Regulations 2025, laid 15 May 2025, "came into legal force on 5 June 2025". [Confirmed S152]
- FCA rules: PS25/6, June 2025; the FCA instrument "comes into force on 10 June 2025". [Confirmed S152]
- Sandbox end: "The Pisces sandbox regulations will cease to have effect on 5 June 2030." [Confirmed S152]
- What it is: "PISCES is a new type of share trading platform. It allows buyers and sellers of shares in private companies to trade those shares during intermittent trading periods." [Confirmed S152] It is secondary trading only (no new money raised). [Reported S154]
- LSE status: FCA approved LSE to run a PISCES platform (reported 26 August 2025) [Reported S153]; LSE's Private Securities Market rules published 5 February 2026; first permissioned auction completed 25 March 2026, a Tradeable Private Equity Investment Company holding shares in Oxford Science Enterprises. [Reported S154] LSEG's H1 2026 results cite "first Private Securities Markets transactions". [Confirmed S195]

#### 4B.5 Consolidated tapes (bond and equity)

- Transparency first: PS24/14 "Improving transparency for bond and derivatives markets", published 5 November 2024, rules in force 1 December 2025, "a simpler and more timely post-trade transparency regime based on fewer deferrals". [Confirmed S156]
- Bond tape: FCA authorised ETS Connect UK (Etrading Software) in May 2026; "ETS Connect UK launched the UK bond CT service on 22 June 2026"; 5-year term. [Confirmed S155] Contract value about GBP 4.8m and a High Court case that delayed the award (lifted December 2025). [Reported S155 search snippet; not on FCA page]
- Equity tape: FCA document CP26/31 (policy statement plus consultation), last updated 31 July 2026: tape will include post-trade data plus "the first level of pre-trade data (the attributed best bid and offer)"; CTP must share income with data contributors; procurement "early 2027"; operating "in 2027 or early 2028". [Confirmed S157]
- Relevance to LSEG: LSE and Turquoise will be data contributors and may get an income share; Tradeweb is a bond venue feeding the bond tape. [Inferred]

#### 4B.6 Wholesale Markets Review, reforms and tax

- Share trading obligation (Article 23 UK MiFIR) revoked 29 August 2023 by commencement of the Financial Services and Markets Act 2023 (FSMA 2023). [Confirmed S167]
- Edinburgh Reforms: announced by Chancellor Jeremy Hunt on 9 December 2022. [Reported S199]
- Mansion House Compact: 10 July 2023; nine DC pension providers aim for at least 5% of default funds in unlisted equities by 2030. [Reported S181]
- Mansion House Accord: 13 May 2025; 17 signatories, at least 10% of main default funds in private markets by 2030, half in the UK. [Reported S181]
- Leeds Reforms: announced 15 July 2025 alongside Rachel Reeves' Mansion House speech; aim to make the UK the number one destination for financial services by 2035. [Reported S180]
- Stamp duty: Autumn Budget 26 November 2025 created a three-year relief from 0.5% SDRT for shares of companies newly listed on a UK regulated market on or after 27 November 2025 ("UK Listing Relief"). [Reported S182; EY also mentions "the newly announced UK Listing Relief", Confirmed S192]
- ISAs: from 6 April 2027 the cash ISA limit falls to GBP 12,000 (overall GBP 20,000 limit unchanged), with older savers protected; the aim is to push more into stocks and shares. [Reported S183]

#### 4B.7 T+1 settlement

- UK: HM Treasury published a draft SI, "The Central Securities Depositories (Amendment) (Intended Settlement Date) Regulations 2026", on 20 November 2025 to make T+1 standard "from 11 October 2027"; comments due 27 February 2026. [Confirmed S158] Whether the final SI has been made is not confirmed; see Gaps.
- EU: Regulation (EU) 2025/2075 amending CSDR, published in the Official Journal 14 October 2025, applies from 11 October 2027. [Reported S159]
- Relevance: same day as the EU, so cross-border trades align; less time for post-trade fixing, more automation, less counterparty risk; LCH and venue operations must adapt. [Inferred]

#### 4B.8 Clearing

- EMIR 3 (EU): in force 24 December 2024; active account requirement applied from 25 June 2025; covers euro and Polish zloty interest rate derivatives and euro short-term interest rate derivatives; at least five trades per sub-category per reference period through the EU account. [Reported S161]
- EU equivalence for UK CCPs: extended on 31 January 2025 for three years to 30 June 2028, applying from 1 July 2025. Commissioner Albuquerque: the extension "will allow the recently agreed EMIR 3 measures to start taking effect, increasing clearing in the EU and reducing our exposure to UK CCPs." [Confirmed S160]
- UK side: FSMA 2023 gave the Bank of England rule-making powers over CCPs and CSDs; the Bank consulted in July 2025 on moving UK EMIR CCP requirements into its own FMI Rulebook, final rules no earlier than mid-2026. [Reported S197] The Bank is "consulting ... on ... permitting tokenised assets as eligible collateral for CCPs". [Confirmed S184]
- Why LCH cares: LCH SwapClear had record notional of $502tn in Q3 2025 [Reported S198]; any EU-forced shift of euro swaps is a direct threat; equivalence to 2028 buys time. LSEG's H1 2026 margin improved partly due to "the change in the SwapClear revenue share agreement in H2 2025". [Confirmed S195]

#### 4B.9 FX

- Market size: $9.6tn a day in April 2025, up 28% from $7.5tn in 2022; spot 31% of turnover; FX swaps 42%; US dollar on one side of 89.2% of trades; top four centres (UK, US, Singapore, Hong Kong) 75%. [Confirmed S163]
- UK: $4,745bn a day, 37.8% of global, down slightly from 38.0%; UK also 49.6% of OTC interest rate derivatives turnover. [Confirmed S162]
- FX Global Code: a voluntary set of 55 principles of good practice by the Global Foreign Exchange Committee (GFXC); first published 2017 [Reported S204]; three-year review completed December 2024 "to strengthen the Code's guidance on FX settlement risk and to increase transparency around certain types of FX transactions and the use of client-generated data"; updated Code published January 2025. [Confirmed S164; 55 principles and Principle 35 risk waterfall Reported S164 snippet]
- Settlement risk: the risk you pay your currency and do not receive the other one (also called Herstatt risk). CLS began operating in September 2002 to settle FX payment-versus-payment (PvP). [Reported S204] BIS (June 2026): "$5.2 trillion, was settled via PvP"; about 10%, or $1.4tn a day, settled with no protection. [Confirmed S205]
- LSEG FX: FXall (dealer-to-client) and FX Matching (dealer-to-dealer), plus LCH ForexClear; ForexClear clearing was up 45% in H1 2026. [Reported S198, S195 snippet]

#### 4B.10 Market abuse (UK MAR)

- UK MAR bans insider dealing, unlawful disclosure of inside information and market manipulation; issuers must disclose inside information promptly and keep insider lists. [Inferred, general knowledge; not re-verified this pass]
- FCA market cleanliness statistic (share of takeovers with abnormal pre-announcement price moves): 41.1% in 2025 under a revised method; 5-year average 33.74%. [Confirmed S166] Note: the FCA says the new method gives "systematically higher" figures than before. [Confirmed S166]

#### 4B.11 Operational resilience

- UK operational resilience: firms had until 31 March 2025 to be able to stay within impact tolerances for important business services. [Reported S172]
- EU DORA (Regulation (EU) 2022/2554): applies from 17 January 2025. [Reported S173]
- UK critical third parties regime: final rules PS24/16 on 12 November 2024, regime took effect 1 January 2025, first designations in force 13 July 2026. [Confirmed S170] Named: AWS, Google Cloud, Microsoft, Oracle. [Reported S171]

#### 4B.12 Debt capital markets at LSE

- The Eurobond market began with Autostrade in July 1963: $15m, 15 years, 5.5% coupon, lead manager S G Warburg. [Confirmed S174] Listed in Luxembourg. [Reported S175]
- Main Market: regulated market for debt listings (including gilts and sovereign bonds). [Inferred]
- International Securities Market (ISM): MTF for debt sold to professional investors; launched 8 May 2017, first admissions 15 May 2017; admission approved by LSE, not FCA Official List. [Reported S176]
- Sustainable Bond Market: launched 11 October 2019, building on the Green Bond Segment from 2015; LSE says it "was the first major exchange to launch a dedicated Green Bond Segment". [Confirmed S177]

#### 4B.13 Current issues and competitive map

- Listings drought: 88 companies left the LSE in 2024, the most since 2009. [Reported S200] 2025: 23 IPOs (9 Main Market, 14 AIM) raising GBP 2.1bn, up 170% on 2024's GBP 777.7m. [Confirmed S192] H1 2026: 7 listings raising GBP 577m. [Reported S193] Visma (around EUR 19bn valuation) chose London but postponed to 2027. [Reported S194]
- LSEG responses: LSE 24, announced 21 July 2026, a separate 24/5 venue, ETPs first in H1 2027 subject to approval. [Confirmed S196] H1 2026: income ex recoveries GBP 4,799m (+8.4% organic constant currency), Markets +11.9%, EBITDA margin 52.7%. [Confirmed S195]
- Competitive map (by segment) [Inferred unless marked]:
  - Listings: Nasdaq, NYSE, Euronext (Amsterdam), Hong Kong.
  - Equity trading in Europe: Cboe Europe, Euronext, Aquis, bank systematic internalisers.
  - Fixed income electronic trading: MarketAxess, Tradeweb, Trumid, Bloomberg [Reported S190].
  - FX: Bloomberg FXGO, 360T (Deutsche Boerse), Cboe FX, EBS (CME).
  - Clearing: CME, Eurex, ICE.
  - Data: Bloomberg, S&P Global, FactSet [Confirmed top three S188].
  - Indices: S&P DJI, MSCI.
- What customers value now [Inferred from S165, S186, S195]: lower total cost (data fees), resilience and uptime, deep liquidity, capital and margin efficiency, AI-ready data, longer trading hours, easier cross-border access.

#### 4B.14 Regulation timeline

| Date | Instrument | What it does | Relevance to LSEG | Source |
|---|---|---|---|---|
| Jul 1963 | Autostrade Eurobond | First Eurobond, lead managed from London | DCM heritage (but listed in Luxembourg) | S174, S175 |
| 27 Oct 1986 | Big Bang | Ended fixed commissions; screen trading | Modern LSE origins | S178 |
| 1 Nov 2007 | MiFID | Venue competition | Rise of MTFs like Turquoise | S203 |
| 3 Jan 2018 | MiFID II/MiFIR | Transparency, trading obligations | Reporting and data rules | S203 |
| Jan 2021 | Brexit, end of transition | EU share trading leaves London | Lost EU share volumes | S179 |
| 9 Dec 2022 | Edinburgh Reforms | Post-Brexit reform package | Started listings, WMR reforms | S199 |
| 29 Aug 2023 | FSMA 2023 commencement | Removes share trading obligation | Freer UK trading | S167 |
| 10 Jul 2023 | Mansion House Compact | DC pensions 5% unlisted by 2030 | Private markets flow | S181 |
| 8 Jan 2024 | DSS Regulations (SI 2023/1398) | Creates Digital Securities Sandbox | DLT trading and settlement test bed | S169 |
| 29 Feb 2024 | FCA wholesale data market study | Finds market power, no big intervention | Data pricing scrutiny | S165 |
| 29 Jul 2024 | UKLR via PS24/6 | Single commercial companies category | IPO competitiveness | S150 |
| 30 Sep 2024 | DSS opens | Applications accepted | Tokenisation | S168 |
| 5 Nov 2024 | PS24/14 | Bond and derivatives transparency | Tradeweb, bond data | S156 |
| 10 Dec 2024 | GFXC Code review complete | Stronger settlement risk guidance | LSEG FX clients | S164 |
| 24 Dec 2024 | EMIR 3 in force (EU) | Active account requirement etc. | Threat to LCH euro clearing | S161 |
| 1 Jan 2025 | CTP regime | Oversight of critical tech suppliers | LSEG cloud partners | S170 |
| 17 Jan 2025 | DORA applies (EU) | ICT resilience rules | LSEG EU entities (e.g. LCH SA) [Inferred] | S173 |
| 31 Jan 2025 | EU UK-CCP equivalence extension | To 30 Jun 2028, from 1 Jul 2025 | LCH EU access | S160 |
| 31 Mar 2025 | UK op resilience deadline | Within impact tolerances | All LSEG UK entities | S172 |
| 13 May 2025 | Mansion House Accord | 10% private markets by 2030 | PSM, private markets data | S181 |
| 5 Jun 2025 | PISCES Sandbox Regulations | Legal basis for PISCES to 5 Jun 2030 | LSE PSM | S152 |
| 10 Jun 2025 | PS25/6 rules in force | PISCES sourcebook | LSE PSM | S152 |
| 25 Jun 2025 | EMIR 3 active account applies | EU firms must clear some trades in EU | LCH SwapClear | S161 |
| 15 Jul 2025 | PS25/9, PS25/10; Leeds Reforms | New prospectus rules; reform package | Primary markets | S151, S180 |
| 14 Oct 2025 | EU Reg 2025/2075 published | EU T+1 from 11 Oct 2027 | Cross-border alignment | S159 |
| 20 Nov 2025 | UK draft T+1 SI | T+1 from 11 Oct 2027 | Post-trade operations | S158 |
| 27 Nov 2025 | UK Listing Relief (SDRT) | 3 years no stamp duty on new listings | IPO incentive | S182 |
| 1 Dec 2025 | PS24/14 rules in force | New bond transparency | Bond tape base | S156 |
| 19 Jan 2026 | POATRs in force | Replace UK Prospectus Regulation | Cheaper capital raising | S151 |
| 25 Mar 2026 | First LSE PSM auction | First PISCES trade | New LSE product | S154 |
| 22 Jun 2026 | UK bond consolidated tape live | One feed of bond trades | Data competition | S155 |
| 13 Jul 2026 | First CTP designations | AWS, Google, Microsoft, Oracle overseen | Cloud dependency | S170, S171 |
| 31 Jul 2026 | Equity CT policy (CP26/31) | Post-trade plus best bid/offer | Venue data income share | S157 |
| 6 Apr 2027 | Cash ISA limit GBP 12,000 | Nudges savers to shares | Retail demand for UK equities | S183 |
| H1 2027 | LSE 24 ETP launch (planned) | 24/5 venue | New trading hours | S196 |
| 11 Oct 2027 | UK and EU T+1 | Settlement next business day | Major ops change during your graduate year | S158, S159 |
| 30 Jun 2028 | EU equivalence for UK CCPs ends unless renewed | Cliff edge | LCH | S160 |
| 5 Jun 2030 | PISCES sandbox regulations expire | Must be made permanent or end | PSM future | S152 |

---

## 2) Key numbers table

| Number | What | Date | Tag | Source |
|---|---|---|---|---|
| $9.6tn per day | Global FX turnover | Apr 2025 | Confirmed | S163 |
| 28% | FX turnover growth vs 2022 | Apr 2025 | Confirmed | S163 |
| 37.8% | UK share of global FX | Apr 2025 | Confirmed | S162 |
| $4,745bn per day | UK FX turnover | Apr 2025 | Confirmed | S162 |
| 49.6% | UK share of OTC interest rate derivatives turnover | Apr 2025 | Confirmed | S162 |
| 89.2% | Share of FX trades with USD on one side | Apr 2025 | Confirmed | S163 |
| $5.2tn | Daily FX settlement via PvP | Apr 2025 | Confirmed | S205 |
| $1.4tn (10%) | Daily FX settlement with no risk protection | Apr 2025 | Confirmed | S205 |
| $49.2bn (+6.5%) | Global market data spend | 2025 | Confirmed | S188 |
| ~$200bn | FMI revenue pool by 2030 (base, 8% CAGR) | Forecast | Confirmed (OW view) | S185 |
| 30% | Data and tech share of FMI revenue | 2026 | Confirmed (OW) | S185 |
| $12bn / $9bn | AI revenue at risk / new AI revenue for FMIs | Forecast | Confirmed (OW) | S185 |
| 20% / 30% | Non-bank share of CIB revenue / trading volumes by 2030 | Forecast | Confirmed (BCG) | S186 |
| $2.3tn | Tokenised real-world assets by 2030 (base) | Forecast | Reported | S191 |
| 30% to 60%+ | Operating margins of key wholesale data providers 2017-22 | 2024 report | Reported | S165 snippet |
| 41.1% | FCA market cleanliness statistic | 2025 | Confirmed | S166 |
| 88 | Companies leaving LSE | 2024 | Reported | S200 |
| 23 / GBP 2.1bn | UK IPOs / proceeds | 2025 | Confirmed | S192 |
| 7 / GBP 577m | LSE listings / proceeds | H1 2026 | Reported | S193 |
| GBP 4,799m (+8.4%) | LSEG H1 2026 income ex recoveries | H1 2026 | Confirmed | S195 |
| +11.9% | LSEG Markets division organic growth | H1 2026 | Confirmed | S195 |
| 52.7% | LSEG adjusted EBITDA margin | H1 2026 | Confirmed | S195 |
| $530bn | LSEG FX average daily volume | H1 2025 | Reported | S198 |
| $502tn | SwapClear notional cleared in a quarter (record) | Q3 2025 | Reported | S198 |
| ~44% | US IG corporate bonds traded electronically | 2024 | Reported | S190 |
| 34% | Tradeweb share of US corporate bond e-trading | 2024 | Reported | S190 |
| EUR 9.2bn vs 8.6bn | Daily share trading Amsterdam vs London | Jan 2021 | Reported | S179 |
| $15m, 5.5% | Autostrade first Eurobond size and coupon | Jul 1963 | Confirmed | S174 |
| 0.5% | UK SDRT rate waived for 3 years on new listings | From 27 Nov 2025 | Reported | S182 |
| GBP 12,000 | Cash ISA limit | From 6 Apr 2027 | Reported | S183 |

---

## 3) Verbatim quotes actually read

1. FCA, PS24/6 page (S150): "The new rules aim to encourage prospective issuers to choose a UK listing by streamlining our rules and removing our 'premium' and 'standard' listing segments in favour of a new commercial companies category for equity shares."
2. FCA, PS25/6 (S152): "PISCES is a new type of share trading platform. It allows buyers and sellers of shares in private companies to trade those shares during intermittent trading periods."
3. FCA, PS25/6 (S152): "The Pisces sandbox regulations will cease to have effect on 5 June 2030."
4. FCA bond tape page (S155): "ETS Connect UK launched the UK bond CT service on 22 June 2026."
5. FCA equity tape page (S157): "We intend the tape to begin operating in 2027 or early 2028."
6. FCA T+1 statement (S158): "On 20 November 2025, the Government published a draft Statutory Instrument and related policy note, to make T+1 the standard settlement cycle in the UK from 11 October 2027."
7. FCA share trading obligation statement (S167): "On 29 August 2023, the Share Trading Obligation (STO) in Article 23 of UK MiFIR was revoked by the commencement of provisions in the Financial Services and Markets Act 2023."
8. European Commission (S160), Commissioner Maria Luis Albuquerque: "Central clearing is vital for well-functioning EU capital markets. With this extension of equivalence for UK CCPs we are safeguarding EU financial stability and avoiding short-term risks."
9. Bank of England (S162): "The UK remains the single largest centre of foreign exchange activity with share of 37.8% of global turnover, a slight decrease from the 38.0% recorded in April 2022."
10. FCA wholesale data press release (S165), Sheldon Mills: "We do not believe the case has been made for significant interventions. However, we will examine ways to help support wholesale data being provided on fair, reasonable and transparent terms."
11. FCA market cleanliness (S166): "The MC statistic for 2025 was 41.1%. The 5-year moving average was 33.74%."
12. Bank of England, Sasha Mills, October 2025 (S184): "Real-time payments, electronic securities settlement and central clearing were once novel concepts. Today, they are foundational to the functioning of the financial system."
13. Bank of England, Sasha Mills (S184): "In 2021 we introduced Omnibus Account, which supports the settlement of tokenised assets backed in central bank money."
14. Oliver Wyman (S185, via fetch summary): "AI offers a cost-reduction potential above 20%, which could lift sector EBITDA margins from 52-54% to more than 60%."
15. BCG (S186): "NBFIs are no longer peripheral players, they are central to how capital is being formed, intermediated, and traded." (original uses a dash after "players"; punctuation adjusted here)
16. Burton-Taylor via Mondo Visione (S188): "The financial market data industry posted another record year in 2025, with global spending climbing 6.5% to $49.2 billion".
17. ICMA (S174): "It is generally accepted that the Eurobond market began with the Autostrade issue for the Italian motorway network in July 1963."
18. LSEG (S177): "London Stock Exchange was the first major exchange to launch a dedicated Green Bond Segment and is now the first to introduce a green economy classification for equities."
19. LSEG H1 2026, David Schwimmer (S195): "Growth in our subscription businesses is accelerating."
20. LSEG H1 2026, David Schwimmer (S195): "With our plans for LSE 24 and growing momentum of transactions on the Private Securities Market, we are opening up significant new market opportunities."
21. LSEG LSE 24 release (S196): "LSE 24 will be available for client testing by the end of 2026, with Exchange Traded Products (ETPs) launching as the first asset class in H1 2027, subject to regulatory approval."
22. BIS Quarterly Review (S205): "Just over one third of the average daily settlement volume in April 2025, or $5.2 trillion, was settled via PvP, which eliminates settlement risk."
23. EY (S192): "There were 11 IPOs in the UK in Q4 2025 raising £1.9bn, according to data from EY-Parthenon."

---

## 4) Source table

[Sxx] | Outlet | Title | Pub date | URL | Accessed | Status | Confidence note
---|---|---|---|---|---|---|---
[S150] | FCA | PS24/6: Primary Markets Effectiveness Review: Feedback to CP23/31 and final UK Listing Rules | 11 Jul 2024 | https://www.fca.org.uk/publications/policy-statements/ps24-6-primary-markets-effectiveness-review-feedback-cp23-31-final-uk-listing-rules | Accessed 2026-10-05 | FETCHED | High; primary
[S151] | FCA | PS25/9: New rules for the public offers and admissions to trading regime | 15 Jul 2025 | https://www.fca.org.uk/publications/policy-statements/ps25-9-new-rules-public-offers-admissions-trading-regime | Accessed 2026-10-05 | FETCHED | High; primary
[S152] | FCA | PS25/6 Private Intermittent Securities and Capital Exchange System: sandbox arrangements (PDF) | Jun 2025 | https://www.fca.org.uk/publication/policy/ps25-6.pdf | Accessed 2026-10-05 | FETCHED | High; full PDF text extracted
[S153] | Debevoise & Plimpton / search snippets | FCA Sets Out Final Rules for PISCES and Launches PISCES Sandbox | Jun 2025 | https://www.debevoise.com/insights/publications/2025/06/fca-sets-out-final-rules-for-pisces-and-launches | Accessed 2026-10-05 | SNIPPET | Medium; LSE approval date 26 Aug 2025 from snippet, not verified on FCA site
[S154] | Burges Salmon | First PISCES auctions take place | 2026 | https://www.burges-salmon.com/articles/102mogc/first-pisces-auctions-take-place/ | Accessed 2026-10-05 | SNIPPET | Medium; page did not render via curl; dates from search summary
[S155] | FCA | Bond consolidated tape | Updated 2026 | https://www.fca.org.uk/markets/data-reporting-services-providers/bond-consolidated-tape | Accessed 2026-10-05 | FETCHED | High; GBP 4.8m and court case only in snippets
[S156] | FCA | PS24/14: Improving transparency for bond and derivatives markets | 5 Nov 2024 | https://www.fca.org.uk/publications/policy-statements/ps24-14-improving-transparency-bond-and-derivatives-markets | Accessed 2026-10-05 | FETCHED | High
[S157] | FCA | CP26/31: Policy Statement for the framework for a UK equity consolidated tape and next steps for delivery | First pub 19 Nov 2025; updated 31 Jul 2026 | https://www.fca.org.uk/publications/consultation-papers/cp26-31-policy-statement-framework-uk-equity-consolidated-tape-next-steps | Accessed 2026-10-05 | FETCHED | High
[S158] | FCA | Government publishes draft Statutory Instrument on T+1 settlement | 21 Nov 2025 | https://www.fca.org.uk/news/statements/government-publishes-draft-statutory-instrument-t-plus-1-settlement | Accessed 2026-10-05 | FETCHED | High; draft SI only
[S159] | EUR-Lex / Societe Generale SS snippets | Regulation (EU) 2025/2075 amending CSDR (shorter settlement cycle) | OJ 14 Oct 2025 | https://www.securities-services.societegenerale.com/en/insights/views/news/csdr-refit-or-regulatory-t-1/ | Accessed 2026-10-05 | SNIPPET | Medium-high; OJ not opened directly
[S160] | European Commission | Commission extends time-limited equivalence for UK central counterparties | 31 Jan 2025 | https://finance.ec.europa.eu/news/commission-extends-time-limited-equivalence-uk-central-counterparties-2025-01-31_en | Accessed 2026-10-05 | FETCHED | High; primary
[S161] | A&O Shearman | EMIR 3: the active account requirement | 2025 | https://www.aoshearman.com/en/insights/emir-3-the-active-account-requirement | Accessed 2026-10-05 | SNIPPET | Medium-high; dates consistent across several law firm snippets
[S162] | Bank of England | BIS Triennial Survey of FX and OTC IRD markets in April 2025: UK data | Sep 2025 | https://www.bankofengland.co.uk/news/2025/september/bis-triennial-survey-of-foreign-exchange-and-over-the-counter-interest-rate-derivatives-markets | Accessed 2026-10-05 | FETCHED | High; primary
[S163] | BIS | OTC foreign exchange turnover in April 2025 | Sep 2025 | https://www.bis.org/statistics/rpfx25_fx.htm | Accessed 2026-10-05 | FETCHED | High; primary
[S164] | GFXC | GFXC completes Three-Year Review of the FX Global Code | 10 Dec 2024 | https://www.globalfxc.org/press-releases/press-p241210/ | Accessed 2026-10-05 | FETCHED | High; principle numbers from snippets
[S165] | FCA | Financial regulator finds wholesale data market can be improved | 29 Feb 2024 | https://www.fca.org.uk/news/press-releases/financial-regulator-finds-wholesale-data-market-can-be-improved | Accessed 2026-10-05 | FETCHED | High; margin figures from MS23/1.5 snippet
[S166] | FCA | Market cleanliness statistics 2025/26 | 2026 | https://www.fca.org.uk/data/market-cleanliness-statistics-2025-26 | Accessed 2026-10-05 | FETCHED | High; methodology changed
[S167] | FCA | FCA statement on the share trading obligation | Updated 29 Aug 2023 | https://www.fca.org.uk/news/statements/fca-statement-share-trading-obligation | Accessed 2026-10-05 | FETCHED | High
[S168] | A&O Shearman | The UK Digital Securities Sandbox is officially open | 2024 (updated) | https://www.aoshearman.com/en/insights/the-uk-digital-securities-sandbox-is-officially-open | Accessed 2026-10-05 | FETCHED | Medium-high; says DSS runs to Dec 2028, may be extended
[S169] | FCA / BoE (snippets) | PS24/12 Digital Securities Sandbox joint Policy Statement; DSS Regulations SI 2023/1398 | 2024 | https://www.fca.org.uk/publications/policy-statements/ps24-12-digital-securities-sandbox-joint-policy-statement-final-guidance | Accessed 2026-10-05 | SNIPPET | Medium-high
[S170] | FCA | Critical Third Parties: Strengthening UK Financial Services | 10 Jul 2026 | https://www.fca.org.uk/firms/critical-third-parties-strengthening-uk-financial-services | Accessed 2026-10-05 | FETCHED | High; timeline read
[S171] | Herbert Smith Freehills Kramer | HM Treasury makes first designations under UK CTP regime | Jul 2026 | https://www.hsfkramer.com/notes/fsrandcorpcrime/2026-posts/hm-treasury-makes-first-designations-under-uk-ctp-regime | Accessed 2026-10-05 | SNIPPET | Medium-high; names consistent across many results
[S172] | Addleshaw Goddard / UK Finance | Operational Resilience deadline | 2025 | https://www.addleshawgoddard.com/en/insights/insights-briefings/2025/financial-regulation/operational-resilience-deadline/ | Accessed 2026-10-05 | SNIPPET | Medium-high
[S173] | EIOPA | Digital Operational Resilience Act (DORA) | n/a | https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en | Accessed 2026-10-05 | SNIPPET | High (EU agency), date widely consistent
[S174] | ICMA | History of the Eurobond market | n/a | https://www.icmagroup.org/About-ICMA/history/history-of-the-eurobond-market/ | Accessed 2026-10-05 | FETCHED | High
[S175] | Wikipedia | Eurobond (external bond) / Luxembourg Stock Exchange | n/a | https://en.wikipedia.org/wiki/Eurobond_(external_bond) | Accessed 2026-10-05 | SNIPPET | Medium; Luxembourg listing claim, verify
[S176] | Norton Rose Fulbright | Practical guide to London Stock Exchange's new International Securities Market | 2017 | https://www.nortonrosefulbright.com/en/knowledge/publications/94491974/practical-guide-to-london-stock-exchanges-new-international-securities-market | Accessed 2026-10-05 | SNIPPET | Medium-high
[S177] | LSEG | London Stock Exchange launches Green Economy Mark and Sustainable Bond Market | 11 Oct 2019 | https://lseg.com/en/media-centre/press-releases/2019/london-stock-exchange-launches-green-economy-mark-and-sustainable-bond-market | Accessed 2026-10-05 | FETCHED | High (company source)
[S178] | MoneyWeek | 27 October 1986: the City's Big Bang | n/a | https://moneyweek.com/353587/27-october-1986-the-citys-big-bang | Accessed 2026-10-05 | SNIPPET | High; well-established fact
[S179] | Crowdfund Insider (citing Cboe data) | Amsterdam Overtakes London As Europe's Largest Stock Trading Center | Feb 2021 | https://www.crowdfundinsider.com/2021/02/172245-amsterdam-overtakes-london-as-europes-largest-stock-trading-center-reports-e9-2-billion-in-trading-volume-in-jan-2021/ | Accessed 2026-10-05 | SNIPPET | Medium-high; original Bloomberg/FT likely PAYWALLED-NOT-READ
[S180] | Latham & Watkins / HSF Kramer | Leeds Reforms Set UK Government Agenda for Financial Services | Jul 2025 | https://www.lw.com/en/insights/leeds-reforms-set-uk-government-agenda-for-financial-services | Accessed 2026-10-05 | SNIPPET | Medium-high
[S181] | Pensions Age / Macfarlanes | Mansion House reforms; The Mansion House Accord | Jul 2023; May 2025 | https://www.macfarlanes.com/insights/102loh5/the-mansion-house-accord-and-its-impact-on-private-capital-markets/ | Accessed 2026-10-05 | SNIPPET | Medium-high
[S182] | Freshfields / AIC | Autumn Budget 2025: new SDRT UK listing relief | Nov 2025 | https://transactions.freshfields.com/post/102lwn7/autumn-budget-2025-new-stamp-duty-reserve-tax-uk-listing-relief | Accessed 2026-10-05 | SNIPPET | Medium-high
[S183] | Deloitte Taxscape / NatWest | ISA changes (Autumn Budget 2025) | Nov 2025 | https://taxscape.deloitte.com/measures-autumn-budget-2025/isa-changes.aspx | Accessed 2026-10-05 | SNIPPET | Medium-high; exact age carve-out wording varies by source
[S184] | Bank of England | From new ideas to new market structures, how innovation is reshaping the financial system, speech by Sasha Mills | Oct 2025 | https://www.bankofengland.co.uk/speech/2025/october/sasha-mills-keynote-speech-at-the-association-of-financial-markets-in-europes-annual-operations | Accessed 2026-10-05 | FETCHED | High; primary
[S185] | Oliver Wyman | How to win in financial market infrastructure through 2030 (Global Financial Infrastructure Report 2026: Back to the Future) | Jun 2026 | https://www.oliverwyman.com/our-expertise/insights/2026/jun/win-future-financial-market-infrastructure.html | Accessed 2026-10-05 | FETCHED | Medium-high; consultant forecast, read via summariser
[S186] | BCG | Non-Bank Players Set to Claim One-Fifth of CIB Revenues by 2030 | 14 Oct 2025 | https://www.bcg.com/press/14october2025-non-bank-players-set-to-claim-one-fifth-of-corporate-and-investment-banking-revenues-by-2030-reshaping-the-future-of-capital-markets | Accessed 2026-10-05 | FETCHED | Medium-high; consultant forecast
[S187] | McKinsey | Financial data and markets infrastructure: Positioning for the future | 2025 | https://www.mckinsey.com/industries/financial-services/our-insights/financial-data-and-markets-infrastructure-positioning-for-the-future | Accessed 2026-10-05 | SNIPPET | Medium; HTTP 503 on fetch, not read
[S188] | Mondo Visione (Burton-Taylor) | Real-Time Analytics Drive Record Growth Across The Financial Market Data Landscape | 26 Mar 2026 | https://mondovisione.com/media-and-resources/news/realtime-analytics-drive-record-growth-across-the-financial-market-data-landsca-2026326/ | Accessed 2026-10-05 | FETCHED | High for headline; full report is paid, PAYWALLED-NOT-READ
[S189] | Markets Media (Burton-Taylor) | Financial Market Data Spending Reaches Record $42bn | 29 Apr 2024 | https://www.marketsmedia.com/financial-market-data-spending-reaches-record-42bn/ | Accessed 2026-10-05 | FETCHED | High for headline
[S190] | Coalition Greenwich / The DESK | Electronic bond trading rises in US IG; e-trading boom to outpace market growth in 2025 | 2025 | https://www.fi-desk.com/coalition-greenwich-e-trading-boom-to-outpace-market-growth-in-2025/ | Accessed 2026-10-05 | SNIPPET | Medium; full Coalition Greenwich reports gated
[S191] | Morgan Stanley / Oliver Wyman (via press) | Tokenised real-world assets market to reach $2.3 trillion by 2030 | 2026 | https://www.morganstanley.com/insights/articles/digital-asset-investment-wholesale-banking-outlook | Accessed 2026-10-05 | SNIPPET | Medium
[S192] | EY | London IPO market rebounds in Q4 2025 (IPO Eye) | Jan 2026 | https://www.ey.com/en_uk/newsroom/2026/01/ipo-eye-q4-2025-london-stock-exchange | Accessed 2026-10-05 | FETCHED | High
[S193] | London Loves Business / IG (EY data) | London Stock Exchange IPOs surge as UK listings rebound in 2026 | Jul 2026 | https://londonlovesbusiness.com/london-stock-exchange-ipo-recovery-577-million-listings-2026/ | Accessed 2026-10-05 | SNIPPET | Medium
[S194] | Investing.com (Bloomberg report) | Visma delays IPO plans to 2027 | Mar 2026 | https://www.investing.com/news/stock-market-news/visma-delays-ipo-plans-to-2027-amid-market-uncertainty-93CH-4585387 | Accessed 2026-10-05 | SNIPPET | Medium; Bloomberg original PAYWALLED-NOT-READ
[S195] | LSEG | London Stock Exchange Group plc: H1 2026 Interim Results | 30 Jul 2026 | https://www.lseg.com/en/media-centre/press-releases/2026/london-stock-exchange-group-plc-h1-2026-interim-results | Accessed 2026-10-05 | FETCHED | High (company source)
[S196] | LSEG | London Stock Exchange to launch LSE 24 | 21 Jul 2026 | https://www.lseg.com/en/media-centre/press-releases/2026/london-stock-exchange-to-launch-lse-24 | Accessed 2026-10-05 | FETCHED | High (company source)
[S197] | Bank of England / law firm snippets | Ensuring the resilience of CCPs (consultation) | Jul 2025 | https://www.bankofengland.co.uk/paper/2025/cp/ensuring-the-resilience-of-ccps | Accessed 2026-10-05 | SNIPPET | Medium-high
[S198] | LSEG | LSEG 2025 H1 Interim Report; LCH ForexClear factsheets | Jul 2025 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/interim-report/lseg-interim-report-h1-2025-31july2025.pdf | Accessed 2026-10-05 | SNIPPET | Medium; figures from search summary
[S199] | McDonnell Ellis (and others) | Edinburgh Reforms announcement | 2022-23 | https://mcdonnellellis.com/whats-new-in-the-mansion-house-speech-and-where-are-we-with-the-edinburgh-reforms/ | Accessed 2026-10-05 | SNIPPET | Medium; GOV.UK original not opened
[S200] | Invezz / Investing.com (EY data) | London Stock Exchange sees the highest outflow of companies since the global financial crisis | Jan 2025 | https://invezz.com/news/2025/01/06/london-stock-exchange-sees-the-highest-outflow-of-companies-since-the-global-financial-crisis/ | Accessed 2026-10-05 | SNIPPET | Medium
[S201] | Cooley / Cleary Gottlieb | FCA Publishes Final UK Listing Rules | Jul 2024 | https://www.cooley.com/news/insight/2024/2024-07-16-fca-publishes-final-uk-listing-rules | Accessed 2026-10-05 | SNIPPET | Medium-high
[S202] | Norton Rose Fulbright | Listing regime | 2024 | https://www.nortonrosefulbright.com/en/knowledge/publications/e9a4e9e0/listing-regime | Accessed 2026-10-05 | SNIPPET | Medium; detail on votes/dual class not read
[S203] | William Fry / CSSF / SGCIB | MiFID II implementation date; MiFID | various | https://www.williamfry.com/knowledge/in-short-mifid-ii-implementation-date-extended-to-january-2018/ | Accessed 2026-10-05 | SNIPPET | High; well-established dates
[S204] | CLS Group / BIS 2002 paper | The FX Global Code; Settlement risk in FX markets and CLS Bank | various | https://www.cls-group.com/about/fx-global-code/ | Accessed 2026-10-05 | SNIPPET | Medium-high
[S205] | BIS Quarterly Review | Uncovering FX settlement risk: new measures from the 2025 BIS Triennial Survey | 15 Jun 2026 | https://www.bis.org/publ/qtrpdf/r_qt2606c.htm | Accessed 2026-10-05 | FETCHED | High; primary

Search and fetch count: 37 web searches; 15 WebFetch calls (14 returned content, 1 HTTP 503) plus 13 curl full-page fetches and 1 full PDF extraction.

---

## 5) Gaps (not verified, do not state as fact)

1. UK T+1: whether the final SI has been laid/made in 2026, and the Accelerated Settlement Taskforce/Technical Group implementation plan dates. Only the draft SI (Nov 2025) is confirmed.
2. EMIR 3 legal citation (believed to be Regulation (EU) 2024/2987 and Directive (EU) 2024/2994, OJ December 2024): not verified this pass.
3. POATRs SI number and key thresholds (for example the 75% further issuance threshold, protected forward-looking statements): not seen in fetched FCA page.
4. The FCA document that finalised the bond CT framework (as distinct from PS24/14): not identified.
5. LSE's PISCES approval date (26 Aug 2025) and PSM first auction details: from snippets only; check LSE press releases.
6. Equity trading share of Turquoise lit vs dark, and Tradeweb ownership percentage by LSEG: not sourced here (likely covered in another workstream).
7. Bank of England final CCP rules (after the July 2025 consultation): status in 2026 unknown.
8. Passive investing share figures (for example index fund share of US fund assets): no sourced number.
9. UK MAR detail (articles, insider list rules): from general knowledge only.
10. FX Global Code first publication date (May 2017) is widely known but not read in a primary source this pass.
11. McKinsey FDMI report: not read (HTTP 503). Coalition Greenwich and Burton-Taylor full reports: PAYWALLED-NOT-READ.
12. Whether the Autostrade bond was also admitted anywhere in London: Luxembourg listing is from a Wikipedia snippet; verify with Euroclear/Clearstream 60-year pieces before using.
13. Whether the DSS application window/end date (December 2028) has been extended in 2026.

---

## 6) Interview angles

1. "Walk me through a trade." Use the five-step lifecycle and name an LSEG business at each step: Workspace data (pre-trade), LSE/Turquoise/Tradeweb/FXall (execution), LCH (clearing), CSD and CLS (settlement), consolidated tape and UnaVista-type reporting (post-trade). Shows you "understand the full breadth of our organisation" (JD).
2. T+1 on 11 October 2027 lands while you would be a graduate. Have a view: less time to fix failed trades means more automation and same-day affirmation; risk teams will monitor fails. Good for the "Risk teams" placement.
3. Listings revival: be balanced. Reforms are real (UKLR 29 July 2024, POATRs 19 January 2026, SDRT relief from 27 November 2025) and 2025 proceeds rose 170%, but volumes remain low historically and Visma slipped to 2027. Suggest one idea, for example using PSM as a "pre-IPO" pipeline to the Main Market. [Inferred]
4. Debt listings (JD names "debt listings"): know ISM (2017, professional investors), Sustainable Bond Market (2019) and the 1963 Eurobond story, told correctly (London-arranged, Luxembourg-listed).
5. FX customers: London 37.8% of $9.6tn; about $1.4tn a day still settles unprotected (BIS 2026), so settlement risk and the 2024 FX Global Code update are live client topics.
6. Clearing politics: EU equivalence to 30 June 2028 and EMIR 3 active accounts. A "connect the dots" answer: LCH's value comes from netting (more trades in one place lowers margin), which is why the EU's policy carries costs for EU users too. [Inferred]
7. Data and AI: tie market data growth ($49.2bn in 2025) and the FCA's fee concerns to LSEG's subscription push and AI partnerships. Show you understand both the customer's cost worry and LSEG's strategy.
8. Three futures question ("Where will the industry be in five years?"): give the Oliver Wyman base case, the tokenisation/AI disruption case and the non-bank/regulation case, then say which signals you would watch (PvP adoption, DSS live entities, tape take-up, EMIR 3 shifts).
9. Strengths-based video interview: link "curiosity for data" to a personal habit (e.g. you tracked the BIS survey or the market cleanliness statistic and noticed the methodology change). Showing you read the footnote is a strength.
10. Values fit (Integrity, Partnership, Excellence, Change): market abuse rules and the market cleanliness statistic are good hooks for Integrity; LSE 24 and PSM for Change.

---

## Glossary (45 terms)

1. Exchange / regulated market (RM): the most heavily regulated type of trading venue, where securities are admitted to trading.
2. MTF (multilateral trading facility): a trading venue that matches many buyers and sellers under fixed rules, lighter regulation than an exchange.
3. OTF (organised trading facility): a venue for bonds and derivatives where the operator can use some discretion.
4. Systematic internaliser (SI): a bank or firm that trades against its own book with clients on an organised, frequent basis.
5. CCP (central counterparty): a clearing house that becomes buyer to every seller and seller to every buyer.
6. Clearing: the process between trade and settlement where obligations are confirmed, netted and risk-managed.
7. Margin: collateral posted to a CCP to cover potential losses. Initial margin covers possible future moves; variation margin settles daily gains and losses.
8. Default fund: a pool paid in by CCP members to cover losses if a member fails and its margin is not enough.
9. Netting: offsetting buys and sells so only the net amount is settled, reducing risk and cash needed.
10. Settlement: the actual exchange of cash and securities.
11. T+1: settlement one business day after the trade date.
12. CSD (central securities depository): the institution that records ownership of securities and settles transfers.
13. CSDR: the Central Securities Depositories Regulation (EU and UK versions).
14. Trade repository: a database collecting derivatives trade reports for regulators.
15. Index provider: a firm that creates and calculates indices like the FTSE 100 and licenses them.
16. Market data vendor (MDV): a firm that gathers and redistributes financial data.
17. Consolidated tape (CT): a single feed combining trade data from all venues for an asset class.
18. Pre-trade transparency: publishing bids and offers before trades happen.
19. Post-trade transparency: publishing the price and size of trades after they happen.
20. Deferral: permission to delay publishing a large trade so the dealer can hedge.
21. Primary market: where new securities are first sold to raise money.
22. Secondary market: where existing securities are traded between investors.
23. IPO (initial public offering): a company's first sale of shares to the public with admission to trading.
24. Prospectus: the legal document describing a security and issuer for investors.
25. POATRs: Public Offers and Admissions to Trading Regulations 2024, the UK's replacement for the Prospectus Regulation.
26. UKLR: the UK Listing Rules sourcebook in force from 29 July 2024.
27. ESCC: equity shares (commercial companies), the single main listing category under UKLR.
28. PISCES: Private Intermittent Securities and Capital Exchange System, for trading private company shares at set events.
29. PSM: London Stock Exchange's Private Securities Market, its PISCES platform.
30. AIM: LSE's growth market for smaller companies.
31. ISM: International Securities Market, LSE's MTF for debt sold to professional investors.
32. Eurobond: a bond issued in a currency other than that of the country where it is issued, sold internationally.
33. Lit venue: an order book where orders are visible before trading.
34. Dark pool: a venue where orders are hidden before execution.
35. CLOB (central limit order book): a continuous matching engine ordering bids and offers by price then time.
36. RFQ (request for quote): a protocol where a client asks selected dealers for prices.
37. OTC (over the counter): trades negotiated bilaterally, not on a venue.
38. Dealer-to-client (D2C) and dealer-to-dealer (D2D): platforms where banks trade with clients (FXall) or with each other (FX Matching).
39. Spot FX: currency exchange for near-immediate delivery (usually two days). FX swap: a spot trade plus a reverse forward trade.
40. Settlement risk (Herstatt risk): the risk of paying out one currency and not receiving the other.
41. PvP (payment versus payment): both currency legs settle at once, or neither does. CLS is the main PvP system.
42. FX Global Code: voluntary principles of good conduct in FX markets, maintained by the GFXC.
43. EMIR / UK EMIR / EMIR 3: EU (and retained UK) rules on derivatives clearing, reporting and CCPs; EMIR 3 is the 2024 EU revision.
44. Active account requirement: EMIR 3 rule that some EU firms must hold and use an account at an EU CCP.
45. Equivalence: an EU decision that a non-EU regime is good enough, letting EU firms use, for example, UK CCPs.
46. MiFID / MiFID II / MiFIR: EU rules on investment services and trading venues; UK keeps an amended "UK MiFIR".
47. Share trading obligation (STO): a former rule forcing certain shares to trade on venues; revoked in the UK on 29 August 2023.
48. UK MAR: UK Market Abuse Regulation covering insider dealing, unlawful disclosure and manipulation.
49. Inside information: precise, non-public, price-sensitive information about an issuer.
50. Insider list: a record issuers keep of people with access to inside information.
51. Market cleanliness statistic: FCA measure of takeovers preceded by abnormal share price moves.
52. Operational resilience: the ability to keep important services running through disruption.
53. DORA: EU Digital Operational Resilience Act, applies from 17 January 2025.
54. Critical third party (CTP): a supplier (for example a cloud provider) designated by HM Treasury for direct oversight.
55. DLT (distributed ledger technology): shared databases (like blockchains) used to record ownership.
56. Tokenisation: representing a security or asset as a digital token on a ledger.
57. Digital Securities Sandbox (DSS): a BoE and FCA regime for testing DLT-based trading and settlement.
58. Stablecoin: a crypto token designed to hold a stable value, often against a currency.
59. FSMA 2023: Financial Services and Markets Act 2023, the post-Brexit framework law.
60. SDRT (stamp duty reserve tax): 0.5% tax on buying UK shares electronically.
61. ETP (exchange-traded product): a fund or note traded on an exchange, such as an ETF.
62. ASV (annual subscription value): LSEG metric for the value of recurring subscription contracts.
63. Buy side / sell side: asset managers and investors (buy) vs banks and dealers (sell).
64. NBFI (non-bank financial institution): hedge funds, proprietary traders, asset managers and others outside banking.
