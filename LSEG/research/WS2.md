# WS2: LSEG as a business, from the inside

Prepared 2026-10-05 for the LSEG Business Management Summer Internship 2027 (Markets side). Source IDs S70 to S119 only. Tags: [Confirmed] = primary source or two credible outlets; [Reported] = one credible secondary source; [Inferred] = my reasoning from the sources.

Quick glossary (used throughout)
- **Total income (excl. recoveries)**: LSEG's headline revenue figure. "Recoveries" are fees LSEG collects for third-party content (for example other exchanges' price data) and passes on, so they are stripped out.
- **Organic constant currency growth**: growth with acquisitions and disposals removed and exchange rates held fixed. This is the number management and analysts focus on.
- **Adjusted EBITDA margin**: earnings before interest, tax, depreciation and amortisation, as a share of income, excluding one-off items. A rough measure of how much of each pound of revenue is operating profit before investment costs.
- **AEPS**: adjusted earnings per share.
- **ASV (Annual Subscription Value)**: the annualised value of subscription contracts at a point in time. Its growth rate is a forward-looking signal for the data businesses. LSEG says it will retire ASV as a KPI at the end of 2026.
- **CCP (central counterparty)**: a clearing house that stands between buyer and seller of a trade, so that if one side defaults the other is still paid. LCH is LSEG's CCP group.
- **Net Treasury Income (NTI)**: the interest LSEG's clearing houses earn on cash margin posted by members, after paying members their share.
- **MCP (Model Context Protocol)**: an open standard for connecting AI applications to data sources. LSEG uses it to pipe licensed data into AI tools.
- **RIE (Recognised Investment Exchange)**: UK legal status for a regulated exchange, granted by the FCA. **MTF (Multilateral Trading Facility)**: a lighter-regulated trading venue run by an investment firm.

---

## 1) Findings

### A. Founding insight and history

**The founding insight.** The business started as a price list. In 1698, at Jonathan's Coffee House in London, John Castaing began issuing a list of stock and commodity prices called "The Course of the Exchange and other things" [Confirmed, S78]. That matters for an interview: the very first product of what became LSEG was *data*, not trading. Today the group describes itself as "a leading financial markets infrastructure and data provider" [Confirmed, S74], so in a sense it has come full circle [Inferred].

**Timeline (date stamped):**
| Date | Event | Tag / source |
|---|---|---|
| 1698 | Castaing's price list at Jonathan's Coffee House | [Confirmed, S78] |
| 1801 | "The first regulated exchange comes into existence in London and the modern Stock Exchange is born" | [Confirmed, S78] |
| 1986 | "Big Bang" deregulation of the UK market (abolition of fixed commissions, end of jobber/broker split, move from open outcry to screen trading) | [Confirmed, S78 for the date; detail from S100 snippet context, Reported] |
| 1995 | FTSE Group established; AIM founded | [Confirmed, S78] |
| July 2001 | LSE becomes a public company listed on its own market (demutualisation preceded this; exact 2000 date not verified this session) | [Confirmed for 2001 listing, S78] |
| 8 Sep 2008 | TradElect trading platform mostly unavailable for over 7 hours (see Skeletons) | [Reported, S100] |
| Oct 2007 | LSE and Borsa Italiana merge, creating London Stock Exchange Group | [Confirmed, S78] |
| 2010 | LSEG takes majority ownership of Turquoise (founded 2006 by nine banks) | [Reported, S95] |
| May 2013 | LSEG acquires majority stake in LCH Group | [Confirmed, S78] |
| Dec 2014 | LSEG completes acquisition of Frank Russell Company | [Confirmed, S78] |
| Mar 2016 to 29 Mar 2017 | £21bn "merger of equals" with Deutsche Börse agreed, then prohibited by the European Commission on 29 March 2017 over a "de facto monopoly" in fixed income clearing; LSEG said it "regrets the Commission's decision" | [Confirmed, S80, S81] |
| Sep 2019 | Board unanimously rejects Hong Kong Exchanges and Clearing's unsolicited ~£32bn proposal, citing concerns on "strategy, deliverability, form of consideration and value"; HKEX's bid was conditional on LSEG dropping Refinitiv | [Confirmed, S82, S107] |
| 2019 (announced) to 29 Jan 2021 (completed) | All-share acquisition of Refinitiv from a Blackstone-led consortium with Thomson Reuters, valued at about $27bn; Refinitiv owners got about 37% economic / 29% voting interest in LSEG | [Confirmed, S78 for completion; S84 for value and stakes, Reported] |
| 29 Apr 2021 | Borsa Italiana sold to Euronext (signed 9 Oct 2020) for about €4.4bn, to clear EU competition concerns on Refinitiv | [Reported, S83] |
| 12 Dec 2022 | 10-year strategic partnership with Microsoft; Microsoft buys ~4% stake from the Blackstone/Thomson Reuters consortium; LSEG commits to minimum cloud spend of $2.8bn (£2.3bn); incremental costs of £250-300m over 2023-25 | [Confirmed, S79] |
| May 2024 | Final sell-down: Thomson Reuters and Blackstone funds sell 17.3m shares at £91.50; Thomson Reuters exits completely | [Reported, S85] |
| 2022 to Feb 2027 | Buybacks: £4.6bn executed 2022-2025; £2.1bn in H1 2026; up to £1.35bn more by Feb 2027, taking cumulative buybacks since 2022 to over £8bn | [Confirmed, S74, S70] |

**Purpose wording (current).** "Our purpose is driving financial stability, empowering economies and enabling customers to create sustainable growth." [Confirmed, S74]. Values listed in the JD: Integrity, Partnership, Excellence and Change.

**Leadership.** David Schwimmer is CEO (appointed 2018, ex-Goldman Sachs; appointment date not re-verified this session), Michel-Alain Proch is CFO (appointed effective 1 March 2024), Don Robert is Chair [Confirmed, S70, S74]. Julia Hoggett is CEO of London Stock Exchange plc [Confirmed, S96]. **No CEO or Chair change found as of 5 Oct 2026.** The only 2026 board news found is that Amit Zavery (President, COO and Chief Product Officer of ServiceNow) joins as a non-executive director on 1 Dec 2026 [Reported, S92]. Searches found no announced Schwimmer succession [Inferred from absence; see Gaps].

### B. How LSEG makes money

**The 2026 segment structure (four divisions).** Since the FY2025 results, LSEG reports four divisions [Confirmed, S72, S70]:
1. **Data & Analytics (D&A)**: Workflows (Workspace desktop, the successor to Eikon), Data & Feeds (real-time and reference data), Analytics (Yield Book, Lipper, StarMine).
2. **FTSE Russell**: indices and benchmarks. Revenue is "Subscription" (licence fees for data) plus "Asset-based" (fees linked to assets in ETFs and funds tracking its indices).
3. **Risk Intelligence**: World-Check screening, Digital Identity & Fraud, Enhanced Due Diligence.
4. **Markets**: Equities (London Stock Exchange, Turquoise), Fixed Income Derivatives & Other (mostly Tradeweb), FX (FXall, Matching), OTC Derivatives (SwapClear, ForexClear, CDSClear, Post Trade Solutions), Securities & Reporting (EquityClear, RepoClear, regulatory reporting), Non-Cash Collateral, plus Net Treasury Income. Markets merged the old "Capital Markets" and "Post Trade" divisions [Confirmed, S72 vs S76].

**FY2025 (year to 31 Dec 2025, published 26 Feb 2026)** [Confirmed, S72]:
- Total income excl. recoveries **£8,986m**, +5.8% reported, **+7.1% organic**.
- Division income (organic growth): D&A £3,978m (+5.0%); FTSE Russell £954m (+7.3%); Risk Intelligence £579m (+11.7%); Markets £3,467m (+8.9%).
- Gross profit £8,233m. Adjusted EBITDA **£4,523m**, margin **50.3%** (2024: 48.8%). Adjusted operating profit £3,506m. AEPS **420.6p** (+15.7%). Reported EPS 238.4p.
- Dividend 150.0p (+15.4%), payout 35.7% of AEPS. Equity free cash flow £2.4bn. £2.1bn buybacks at average £93.44. Total returned £2.8bn.
- Division EBITDA margins: D&A 40.7%; FTSE Russell 66.6%; Risk Intelligence 57.5%; Markets 55.6%.

**H1 2026 (six months to 30 June 2026, published 30 July 2026)** [Confirmed, S70]:
- Total income excl. recoveries **£4,799m**, +6.9% reported, **+8.4% organic**. Q1 alone was +9.8%, described by LSEG as a record [Confirmed, S75].
- Division (organic): D&A £2,061m (+5.1%); FTSE Russell £504m (+9.1%); Risk Intelligence £310m (+9.7%); Markets £1,920m (+11.9%).
- Adjusted EBITDA £2,527m, margin **52.7%** (+320bps). Of this, 140bps came from the SwapClear revenue-share change and LSEG says this year-on-year uplift "will largely reverse in Q4 2026". Underlying constant currency margin improvement: 120bps.
- AEPS 244.9p (+17.2%). Interim dividend 55.0p (+17.0%). Equity free cash flow £1.2bn.
- Division EBITDA margins: D&A 42.3%; FTSE Russell 68.1%; Risk Intelligence 59.4%; Markets 58.6%.
- Subscription KPIs: ASV growth 6.1%; rolling 12-month gross sales £482m; revenue retention 92.8%; New Product Vitality Index 25%.

**Markets line by line, H1 2026 (organic growth)** [Confirmed, S70]: Equities £230m (+12.2%); Fixed Income, Derivatives & Other £864m (+13.0%); FX £145m (+7.6%); OTC Derivatives £355m (+13.6%); Securities & Reporting £124m (+8.2%); Non-Cash Collateral £59m (+3.5%); Net Treasury Income £143m (+12.6%). Same lines for FY2025: Equities £412m; FIDO £1,539m; FX £272m; OTC Derivatives £641m; Securities & Reporting £229m; Non-Cash Collateral £117m; NTI £257m [Confirmed, S72].

Schwimmer, H1 2026 call: "Remember that Markets is 40% of LSEG revenue." [Confirmed, S71]. Check: £1,920m / £4,799m = 40.0% [Inferred arithmetic].

**Recurring share.** "Over 70% of our income is recurring in nature"; recurring revenue was 73% of total income including recoveries in 2025 [Confirmed, S74]. LSEG also says "~98% of group revenues derived from proprietary data, IP and market infrastructure" [Confirmed, S73] and "90% of our data revenues come from real-time or data that is proprietary" [Confirmed, S71]. This last point is LSEG's main defence against the AI-disruption bear case.

**Tradeweb.** LSEG's 2025 annual report lists Tradeweb Markets LLC as a 50.9%-owned subsidiary [Confirmed, S74]. Because LSEG controls it, 100% of Tradeweb revenue is consolidated into "Fixed Income, Derivatives & Other", and the minority's share shows up as "non-controlling interests" (adjusted £334m in 2025, £194m in H1 2026, growth "mainly reflecting strong performance of the Tradeweb business") [Confirmed, S72, S70]. Tradeweb ADV: $2.62trn in 2025 (+16.9%) and $3.18trn in H1 2026 (+24.8%) [Confirmed, S72, S70].

**LCH ownership and SwapClear economics.** In Oct 2025 LSEG paid £1.2bn (instalments £921m in 2025, £250m in 2026) to change the SwapClear revenue-share deal with founding bank members: their share of the "revenue surplus" fell from c.30% to 15% for 2025 and 10% from 2026 to 2045 [Confirmed, S72, S70]. LSEG said this immediately improved group EBITDA margin by 100bps and was 2-3% accretive to AEPS in 2025 [Confirmed, S72]. In July 2026 LSEG agreed to buy up to 1.05% more of LCH Group for €70m, taking ownership to over 95% [Confirmed, S70]. SwapClear IRS notional cleared: $1,941trn in 2025 (+21.2%); $1,165trn in H1 2026 (+29.4%) [Confirmed, S72, S70].

**Geography.** 2025 revenue by location of service provider (£m, total revenue £9,081m): UK 2,918; US 3,418; Europe excl. UK 1,253; Asia 1,035; Other 457 [Confirmed, S74]. So the US is the single biggest market (about 38%) and the UK about 32% [Inferred arithmetic]. Note this is where the LSEG entity providing the service sits, not where the customer is.

**The money trail (customer to shareholder), simplified** [Inferred, built from S70, S72, S74]:
1. A customer pays: a bank pays for Workspace seats and data feeds (D&A); an ETF issuer pays FTSE Russell a fee linked to the fund's assets; a bank pays a World-Check subscription; a trader pays per-trade fees on LSE, Turquoise, FXall or Tradeweb; a clearing member pays clearing fees to LCH and posts margin, on which LCH earns Net Treasury Income.
2. Cost of sales (£1,113m in 2025) mostly pays for third-party content in D&A and revenue shares (for example the SwapClear surplus share). Gross profit £8,233m.
3. Operating costs (£3,711m adjusted in 2025, 71% of which is people) leave adjusted EBITDA of £4,523m (50.3% margin).
4. Depreciation and amortisation of investment (capex £919m in 2025, 10.2% of income) and interest, tax (about 24%), and the Tradeweb/LCH minority share come out.
5. What is left becomes equity free cash flow (£2.4bn in 2025, guided at least £2.7bn in 2026), which funds dividends (£718m cash in 2025) and buybacks (£2.1bn in 2025), within a leverage target of 1.5-2.5x net debt to EBITDA (1.8x at Dec 2025, 2.1x at June 2026).
The highest-margin pound is an index licence (FTSE Russell, 68% EBITDA margin in H1 2026); the lowest is a Workspace desktop seat inside D&A (division margin 42%), which needs heavy content costs and engineering.

### C. The stakeholder "contracts"
| Stakeholder | What they give LSEG | What they get | Evidence |
|---|---|---|---|
| **Issuers** (companies listing on LSE or AIM, private companies on the Private Securities Market) | Admission and annual fees; disclosure obligations | Access to capital, a public price, liquidity for shareholders (including employees, via PSM) | PSM approval [Confirmed, S96]; Equities line [S70] |
| **Trading members** (brokers, banks, asset managers on LSE, Turquoise, FXall, Tradeweb) | Per-trade fees, connectivity fees, order flow (which itself creates data) | Liquidity, price discovery, best-execution evidence | Volumes up: UK ADV +33.5%, FX +5.8%, Tradeweb +24.8% in H1 2026 [Confirmed, S70] |
| **Clearing members** (banks at LCH) | Clearing fees; initial and variation margin; default fund contributions; in SwapClear and Post Trade Solutions, equity investment and governance input | Counterparty risk removed, capital and margin efficiency, a share of revenue (SwapClear founding members) or equity upside (11 banks bought 20% of Post Trade Solutions for £170m, Oct 2025) | [Confirmed, S72]; total CCP collateral £277bn at end 2025 [Confirmed, S74] |
| **Data customers** (banks, asset managers, wealth managers, corporates) | Multi-year subscriptions; in Q4 2025 customers signed long-term contracts worth £1.9bn, up to 7 years; about 16% of run-rate D&A revenue on such contracts | Trusted, licensed data and a workflow tool; increasingly delivery into their own AI tools via MCP | [Confirmed, S72, S73] |
| **Index licensees** (ETF issuers like BlackRock, fund managers) | Subscription fees plus asset-based fees on ETF AUM; FTSE Russell-linked ETF AUM $2.19trn at June 2026 | The right to market a product tracking a recognised benchmark | BlackRock partnership extended in 2025 [Confirmed, S72, S70] |
| **Microsoft** | Equity holder (4.1% at Dec 2025), Azure cloud, co-developed products (Workspace in Teams, Excel/PowerPoint add-ins, Open Directory, data in Fabric) | Minimum $2.8bn cloud spend from LSEG over 10 years; Microsoft estimated about $5bn extra revenue to Microsoft over the decade | [Confirmed, S79, S74]; $5bn figure [Reported, S104] |
| **Shareholders** | Capital; tolerance of investment spend | Progressive dividend (17% CAGR over 20 years), buybacks over £8bn since 2022 incl. planned | [Confirmed, S70, S74]. Top holders at Dec 2025: Qatar Investment Authority 6.2%, BlackRock 5.7%, Capital Group 5.1%, Microsoft 4.1%, Lindsell Train 4.1% [Confirmed, S74]. Elliott built a stake in Feb 2026 (size not disclosed) [Confirmed, S86, S87 headline] |
| **Regulators and the state** | Licences (RIE, MTF, CCP) | Stable market infrastructure; UK growth policy (PISCES, digital gilts) | [Confirmed, S96, S70] |

### D. Risk and control architecture

**LCH default waterfall.** Order of loss absorption if a clearing member defaults, per LCH: "The collateral and default fund contributions of the defaulting Clearing Member are utilised first, followed by the CCP's own funds and then by the default fund contributions of non-defaulting Clearing Members." LCH sets aside 25% of its minimum regulatory capital as "skin-in-the-game", applies a "defaulter-pays" principle, and calculates initial margin to 99.7% confidence (99% for Listed Rates), above regulatory minimums of 99% (listed) and 99.5% (OTC) [Confirmed, S93]. LSEG's annual report adds: members are selected on capital and operational strength; margins must include a minimum amount of cash; default funds cover "multiple defaults in extreme market circumstances"; stress tests size both; CCP risk committees review them; each CCP holds regulatory capital plus extra own capital [Confirmed, S74].

Scale: total clearing member margin and default fund collateral across group CCPs was **£277bn at 31 Dec 2025** (cash £91bn, non-cash £186bn), peaking at £303bn during 2025 (£334bn in 2024). The cash portfolio (£90bn) was 99.95% invested securely, weighted average maturity 82 days [Confirmed, S74]. This is where Net Treasury Income comes from [Inferred].

**Who supervises what.**
- **LCH Ltd** (UK): supervised by the Bank of England, which supervises UK CCPs, central securities depositories and payment systems. The Bank's FMI Annual Report 2025-26 (published 25 June 2026) names operational resilience, including meeting "Impact Tolerances under cyber and extreme scenarios", and the critical third party regime as priorities [Confirmed, S94].
- **LCH SA** (Paris): regulated by the ACPR (French prudential regulator) and registered in the US with the CFTC (for CDS clearing) and SEC [Reported, S105 snippet of SEC/CFTC filings]. The BoE has an MoU allowing reliance on French authorities for LCH SA [Reported, S94 search snippet]. The AMF role was not verified this session (Gap).
- **London Stock Exchange plc**: a UK Recognised Investment Exchange under Part XVIII of FSMA 2000, supervised by the FCA [Reported, S95 snippet].
- **Turquoise**: Turquoise Global Holdings Ltd is an FCA-authorised investment firm operating an MTF; Turquoise Europe B.V. in Amsterdam is regulated by the Dutch AFM; LSEG has majority-owned TGHL "in partnership with the user community since 2010" [Reported, S95].

**Group risk framework.** LSEG runs a "three lines of defence" model: the business (first line) owns risk, Risk and Compliance (second line) provide independent oversight and challenge, Internal Audit (third line) provides independent assurance. An Enterprise Risk Management Framework (ERMF) and a Group Risk Taxonomy feed Group Risk Appetite Statements approved by the Board annually. Committees include a Board Risk Committee, a Board Audit Committee and an executive-level Group Executive Risk Committee with sub-committees covering financial, model, and technology/cyber risk [Confirmed, S74].

**How this produces stability** [Inferred]: the waterfall puts the defaulter's own money first, so members have incentives to manage risk; LCH's own capital comes second so management has "skin in the game"; mutualised default funds are a last resort sized by stress tests. LSEG's stability is also commercial: high retention (92.8%), multi-year data contracts, and diversification across data and transactions are the "all-weather" story in the annual report [Confirmed for the phrase "all-weather growth", S74].

### E. Strategy and business mix

**What has grown** [Confirmed, S73, S72, S70]:
- Organic growth (constant currency, excl. recoveries) 2021-2025: 5.8%, 6.3%, 7.1%, 7.7%, 7.1%. H1 2026: 8.4%.
- EBITDA margin (excl. FX) 2021-2025: 47.8%, 47.8%, 47.2%, 48.8%, 50.3%. H1 2026: 52.7%.
- AEPS 2021-2025: 272.4p, 317.8p, 323.9p, 363.5p, 420.6p.
- Markets: Schwimmer says annual growth "has averaged almost 10%" over five years with "no weak years" [Confirmed, S71].
- FTSE Russell: ETF AUM linked to its indices $1.43trn (end 2024) to $1.83trn (end 2025) to $2.19trn (June 2026) [Confirmed, S72, S70]. 44 new equity ETFs in 2025, a record [Confirmed, S72].
- Workspace: Eikon sunset completed; AI Search 17,000 active users, Deep Research 7,000 users at H1 2026 [Confirmed, S70, S72].
- Post Trade Solutions: 11 banks took 20% for £170m (Oct 2025), "replicating the original LCH model" [Confirmed, S72].

**Guidance** [Confirmed, S72, S70]:
- 2026: organic growth 7.0-7.5% (raised from 6.5-7.5%); constant currency EBITDA margin up about 100bps (raised from 80-100bps); capex c.9.5% of income; equity FCF at least £2.7bn; tax 24-25%.
- **Medium term 2027-2029** (new framework set Feb 2026): mid to high single-digit organic growth annually including acceleration in subscription businesses; underlying EBITDA margin up a cumulative c.150bps 2027-2029; capex down to c.8% of income by 2029; double-digit CAGR in equity FCF per share. LSEG says it "consistently met or exceeded" the 2023 framework [Confirmed, S72].

**AI monetisation framework** (new in H1 2026): recurring subscription to licence LSEG datasets for use with AI models; a recurring charge for MCP access, with usage bands to come; AI Search priced into the Workspace annual price review up to a usage cap, with Deep Research as a premium add-on [Confirmed, S70].

### F. Public company and share price
- Listed on the London Stock Exchange, ticker LSEG, FTSE 100 constituent; ISIN GB00B0SWJX34 [Confirmed, S70].
- Share price story (Yahoo Finance daily closes, S90) [Confirmed for price data; causes per cited news]:
  - Peak close **12,095p on 5 Feb 2025**.
  - **31 Jul 2025** (H1 2025 results): close down 7.9% day on day; Bloomberg headline "LSEG Shares Plunge on Slowing Growth in Subscription Value" [Reported, S102 headline only, S103]. The driver was slower ASV growth.
  - **3 Feb 2026**: close down 12.8% in a day (8,234p to 7,180p). Reuters: shares "tumbled nearly 13% in one day in February" as worries about large language models "like Anthropic's Claude" triggered a software selloff [Confirmed, S90 + S88]. Low close **7,170p on 4 Feb 2026**; 52-week intraday low 6,684p [Confirmed, S90]. Peak to trough close about -41% [Inferred arithmetic].
  - **11 Feb 2026**: reports that Elliott had built a stake; shares jumped as much as 7% then settled +2.3%; stock had "fallen by more than 35% in the past 12 months" [Confirmed, S86, S87 headline].
  - **26 Feb 2026** (FY2025 results plus £3bn buyback plan): close up 9.1% [Confirmed, S90].
  - **11 Jun 2026**: Reuters analysis says shares up 27% since Elliott news but 23% below the 2025 peak; trading about 18x forward earnings, about 30% discount to Moody's and 40% to MSCI; 90% of 20 analysts rate buy or strong buy [Reported, S88].
  - **18 Jun 2026**: Rothschild & Co Redburn downgrades to neutral, target cut from £120 to £104, saying about 30% of EBITDA faces downside in a "realistic base case"; close down 7.0% [Reported, S89; price move Confirmed, S90].
  - **30 Jul 2026** (record H1 2026 results, guidance raised): close down 6.4% (9,198p to 8,606p). Coverage said investors were weighing the timing of AI monetisation [Confirmed price, S90; reason Reported, S108 snippet].
  - **5 Oct 2026**: about 8,216p intraday [Confirmed, S90].
- Market cap: roughly **£40bn** at 8,216p [Inferred: share count near 490m, from 497m weighted average in H1 2026 (S70) less continuing buybacks; not a sourced figure].

### G. Leadership's stated view of the future
- **"More valuable in an AI world"** is the title of both the FY2025 results and Q1 2026 presentations [Confirmed, S73, S75 title]. Core claim: data, compute and models are the ingredients of AI; compute is an arms race, models are commoditising, and trusted licensed data becomes more valuable [Confirmed, S71].
- **LSEG Everywhere**: deliver AI-ready data wherever customers work. Partnerships with Anthropic, Databricks, Microsoft Copilot Studio, OpenAI, Rogo, Snowflake (2025), then Amazon Quick and Google Gemini (H1 2026). MCP customers: over 60 trialling (Feb 2026), over 150 connected or onboarding (Apr 2026), over 200 engaged (Jul 2026) [Confirmed, S72, S75, S70].
- **Microsoft**: Workspace in Teams, Excel/PowerPoint add-ins, Open Directory (20+ customers onboarded), Autex on Azure, DMI on Azure [Confirmed, S72, S70]. Reuters reports some investors see the rollout as disappointing and "less pivotal" than when announced [Reported, S88].
- **Digital markets infrastructure**: Digital Markets Infrastructure (DMI) launched Sept 2025 for private funds, six fund providers onboarded by H1 2026; Digital Settlement House (DiSH) launched H1 2026; Digital Securities Depository planned H2 2026; MoU with HSBC to support the UK's first digital gilt (DIGIT) by Q1 2027 [Confirmed, S72, S73, S70].
- **Private markets**: Private Securities Market under PISCES (first operator approved, 26 Aug 2025; first transactions in H1 2026, "including two high-profile UK unicorns" in July); Preqin and eVestment data partnerships; FTSE StepStone private markets indices [Confirmed, S96, S71, S72].
- **24-hour trading**: LSE 24, a 24/5 venue (initially ETPs, running 5pm to 7:50am London time) announced 21 July 2026 for launch in H1 2027 [Confirmed, S70; detail Reported, S97].
- **Internal AI**: AI coding platform with nearly 50% daily use; headcount figure "reduced from 15,100 to around 14,200" in 2025 in the engineering transformation context, in-house engineers up from 49% to 60%; major incidents down 50% [Confirmed, S72].
- **Hiring inference** [Inferred]: the emphasis on forward-deployed engineers, AI monetisation, Post Trade Solutions customers (80+ added in H1 2026), and new venues (PSM, LSE 24, DiSH) suggests Markets interns are likely to meet projects in onboarding, product launch support, customer analysis for FX, and risk reporting. The JD's four tracks (FX customers, market research on debt listings and shareholder analysis, business intelligence, risk) map onto these.

### H. Recent moves, Oct 2024 to Oct 2026 (date stamped)
| Date | Move | Source |
|---|---|---|
| 19 Jul 2024 | Global Workspace outage blamed on a "third party global technical issue" (the CrowdStrike day; that link is my inference); RNS publication disrupted | [Reported, S98] |
| 27 Feb 2025 | FY2024 results: income £8,494m, +7.7% organic | [Confirmed, S76] |
| 30 Jun 2025 | Eikon access ended for existing customers; migration to Workspace completed | [Confirmed, S72] |
| 31 Jul 2025 | H1 2025 results; shares fall on ASV slowdown | [Reported, S102, S103] |
| 26 Aug 2025 | LSE first operator to get a PISCES Approval Notice for the Private Securities Market | [Confirmed, S96] |
| Sep 2025 | DMI launched, first transaction | [Confirmed, S72] |
| Oct 2025 | 11 banks buy 20% of Post Trade Solutions for £170m; £1.2bn SwapClear revenue-share restructuring, extended to 2045 | [Confirmed, S72] |
| Nov 2025 | RepoAgent launched (Post Trade Solutions with Tradeweb) | [Confirmed, S72] |
| Dec 2025 | MCP server launch; AI Enhanced Search | [Confirmed, S70, S72] |
| 3-4 Feb 2026 | Shares fall ~13% on AI disruption fears | [Confirmed, S88, S90] |
| 11 Feb 2026 | Elliott stake reported | [Confirmed, S86, S87] |
| 26 Feb 2026 | FY2025 results; £3bn buyback plan by Feb 2027; new 2027-29 guidance | [Confirmed, S72] |
| Mar 2026 | Lindsell Train adds to its holding | [Reported, S88] |
| 23 Apr 2026 | Q1 2026 update: +9.8% organic, "record" quarter; £1.1bn bought back in Q1 | [Confirmed, S75] |
| H1 2026 | Amazon Quick and Google Gemini partnerships; TradeAgent; DiSH; Model-as-a-Service with Societe Generale; Russell 9000 announced; Tradeweb strategic partnership and minority investment in Kalshi | [Confirmed, S70] |
| 18 Jun 2026 | Redburn downgrade on AI risk | [Reported, S89] |
| Jul 2026 | LSE 24 announced (21 Jul); HSBC DIGIT MoU; agreement to raise LCH ownership to over 95% | [Confirmed, S70] |
| 30 Jul 2026 | H1 2026 results; guidance raised; £1.35bn further buyback | [Confirmed, S70] |
| 1 Dec 2026 (future) | Amit Zavery joins board | [Reported, S92] |
| 22 Oct 2026 (future) | Q3 2026 trading statement (revenues only), **not yet published** as of 5 Oct 2026 | [Confirmed, S91] |

### I. Skeletons, told straight
1. **The 2025-26 derating.** From a 12,095p peak (Feb 2025) the shares fell about 41% to a 7,170p close (Feb 2026), on (a) slowing subscription growth (ASV) in mid-2025 and (b) fear that AI tools would let customers bypass terminals and aggregated data. Redburn's June 2026 note put about 30% of group EBITDA at risk, concentrated in "workflow and aggregation-driven revenues", and called the shift to API and AI consumption "structurally deflationary for parts of the model" [Confirmed price S90; Reported S88, S89]. Even after record H1 2026 results the shares fell 6.4% [Confirmed, S90]. UBS analyst Michael Werner: "There is still a 'show me' story for AI. It's one thing to have usage, it's another to start charging people." [Reported, S88].
2. **Workspace (D&A) is the slow-growth part.** Workflows grew only 3.1% in 2025 and 2.8% in H1 2026, against 7.5% for Data & Feeds [Confirmed, S72, S70]. D&A margin (about 41-42%) is far below the rest of the group [Confirmed, S72, S70]. Users have reported inconsistencies between legacy Eikon features and Workspace [Reported, low-quality source; treat with caution, S109 snippet]. I did not find (and so do not claim) a specific FT exposé on Workspace complaints (Gap).
3. **Refinitiv integration is still costing money five years on.** Non-underlying amortisation of £568m in H1 2026 "mainly arose from the Refinitiv acquisition"; integration, separation and restructuring costs were £19m in H1 2026, down from £53m [Confirmed, S70]. LSEG itself says cost and revenue synergies were delivered "significantly ahead of initial Refinitiv acquisition targets" [Confirmed, S73]. So the story is less "overrun" than "long and expensive"; I could not verify any specific cost overrun claim (Gap). The Microsoft deal itself carried a £250-300m incremental cost and a 50-100bps margin hit over 2023-25 [Confirmed, S79].
4. **Outages.**
   - 8 Sep 2008: TradElect largely unavailable for over 7 hours on a heavy trading day; an analyst linked several outages to volume spikes [Reported, S100]. (The brief said 2009; there was also a further crash reported in Nov 2009, per a Register headline, snippet only.)
   - Aug 2020: LSE opening delayed by more than an hour and a half, which LSEG attributed to "a technical software configuration issue following an upgrade of functionality"; it denied a cyber attack [Reported, S101].
   - 19 Jul 2024: global Workspace outage; RNS disrupted; a trader called it "the mother of all global market outages"; LSE trading itself unaffected [Reported, S98].
   - 2023 Eikon platform outage reported by Reuters (headline snippet only, date not verified) [Reported, low detail].
5. **World-Check data leak (2024).** Hacking group GhostR claimed to have stolen 5.3m records of World-Check (LSEG's sanctions and PEP screening database). LSEG said: "This was not a security breach of LSEG/our systems... The incident involves a third party's data set, which includes a copy of the World-Check data file." [Reported, S99]. This is a reputational issue for Risk Intelligence, which sells trust.
6. **Fines.** I searched for Bank of England, ACPR and CFTC penalties against LCH and found none in this session. The Bank of England's July 2025 fine of Vocalink (£11.9m) was described as the first time it had fined an FMI, which suggests (but does not prove) that LCH Ltd has not been fined by the Bank [Reported, S106; Inferred]. Do not claim an LCH fine in interview without a source (Gap).
7. **FTSE Russell index errors.** Not found in this session; no claim made (Gap).
8. **Failed mega-deals.** Two blocked or rejected combinations (Deutsche Börse 2017, HKEX 2019) show that LSEG's clearing assets are strategically sensitive to regulators [Confirmed, S80, S82; Inferred interpretation].
9. **Reliance on volatility and a one-off margin boost.** H1 2026 Markets strength was helped by "elevated market volatility", and the 140bps SwapClear margin benefit will "largely reverse in Q4 2026" [Confirmed, S70]. Redburn flags Markets cyclicality as a risk [Reported, S89].
10. **Activist pressure.** Elliott's involvement (Feb 2026) followed the share fall; reported asks were a fresh buyback and closing the gap with rivals, and Elliott reportedly does not want a sale or spin-off of the exchange [Reported, S86]. LSEG then announced the £3bn buyback programme on 26 Feb 2026 [Confirmed, S72]; I do not claim causation.

**Headcount note.** Annual report: total employees 28,516 at 31 Dec 2025 (27,386 at end 2024); average 27,695 (2025) and 27,038 (2024); India is the largest single country with 8,541 at end 2025, UK 5,043, US 3,218 [Confirmed, S74]. The JD says "25,000 people across 65 countries", which is lower than the annual report figure; the "15,100 to 14,200" figure in the FY2025 results sits in the engineering section and appears not to be group headcount [Inferred].

---

## 2) Key numbers table

| Number | What | Source | Date | Confidence |
|---|---|---|---|---|
| £8,986m | FY2025 total income excl. recoveries | S72 | 26 Feb 2026 | Confirmed |
| 7.1% | FY2025 organic constant currency growth | S72 | 26 Feb 2026 | Confirmed |
| £4,523m / 50.3% | FY2025 adjusted EBITDA / margin | S72 | 26 Feb 2026 | Confirmed |
| 420.6p | FY2025 AEPS | S72 | 26 Feb 2026 | Confirmed |
| 150.0p | FY2025 dividend per share | S72 | 26 Feb 2026 | Confirmed |
| £2.4bn | FY2025 equity free cash flow | S72 | 26 Feb 2026 | Confirmed |
| £2.1bn / £93.44 | FY2025 buybacks / average price | S72 | 26 Feb 2026 | Confirmed |
| £4,799m | H1 2026 total income excl. recoveries | S70 | 30 Jul 2026 | Confirmed |
| 8.4% | H1 2026 organic growth | S70 | 30 Jul 2026 | Confirmed |
| 9.8% | Q1 2026 organic growth | S75 | 23 Apr 2026 | Confirmed |
| 52.7% | H1 2026 adjusted EBITDA margin | S70 | 30 Jul 2026 | Confirmed |
| 244.9p | H1 2026 AEPS | S70 | 30 Jul 2026 | Confirmed |
| 55.0p | 2026 interim dividend | S70 | 30 Jul 2026 | Confirmed |
| 73% | Recurring revenue share of total income incl. recoveries, 2025 | S74 | Feb/Mar 2026 | Confirmed |
| 40% | Markets share of group revenue (CEO) | S71 | 30 Jul 2026 | Confirmed |
| 50.9% | LSEG ownership of Tradeweb Markets LLC | S74 | at 31 Dec 2025 | Confirmed |
| >95% | LSEG ownership of LCH Group after July 2026 deal | S70 | 30 Jul 2026 | Confirmed (on completion) |
| £1.2bn | Cost of SwapClear revenue-share change (surplus share to 10% from 2026 to 2045) | S72, S70 | Oct 2025 | Confirmed |
| £170m / 20% | 11 banks' investment in Post Trade Solutions | S72 | Oct 2025 | Confirmed |
| £277bn | Total CCP margin and default fund collateral | S74 | 31 Dec 2025 | Confirmed |
| 99.7% | LCH initial margin confidence level (most services) | S93 | accessed 5 Oct 2026 | Confirmed |
| 25% | Share of LCH minimum regulatory capital as skin in the game | S93 | accessed 5 Oct 2026 | Confirmed |
| $1,941trn / $1,165trn | SwapClear IRS notional cleared FY2025 / H1 2026 | S72, S70 | 2026 | Confirmed |
| $2.62trn / $3.18trn | Tradeweb ADV FY2025 / H1 2026 | S72, S70 | 2026 | Confirmed |
| $525bn / $561bn | FX average daily volume FY2025 / H1 2026 | S72, S70 | 2026 | Confirmed |
| £4.8bn / £6.67bn | UK equities average daily value traded FY2025 / H1 2026 | S72, S70 | 2026 | Confirmed |
| £257m / £143m | Net Treasury Income FY2025 / H1 2026 | S72, S70 | 2026 | Confirmed |
| $2.19trn | ETF AUM linked to FTSE Russell indices (period end) | S70 | 30 Jun 2026 | Confirmed |
| 92.8% | Subscription revenue retention rate | S70 | 30 Jun 2026 | Confirmed |
| 6.1% | ASV growth | S70 | 30 Jun 2026 | Confirmed |
| 17,000 | Workspace AI Search active users | S70 | 30 Jul 2026 | Confirmed |
| >200 | Customers engaged on MCP server | S70 | 30 Jul 2026 | Confirmed |
| 7.0-7.5% | 2026 organic growth guidance (raised) | S70 | 30 Jul 2026 | Confirmed |
| c.150bps | Cumulative EBITDA margin gain target 2027-29 | S72 | 26 Feb 2026 | Confirmed |
| >£8bn | Cumulative buybacks since 2022 incl. planned to Feb 2027 | S70 | 30 Jul 2026 | Confirmed |
| 4.1% | Microsoft's shareholding | S74 | 31 Dec 2025 | Confirmed |
| $2.8bn | LSEG minimum cloud commitment to Microsoft over 10 years | S79 | 12 Dec 2022 | Confirmed |
| ~$27bn | Refinitiv deal value | S84 | Jan 2021 | Reported |
| 28,516 | Total employees at year end | S74 | 31 Dec 2025 | Confirmed |
| 12,095p | Peak daily close | S90 | 5 Feb 2025 | Confirmed |
| 7,170p | Low daily close | S90 | 4 Feb 2026 | Confirmed |
| -12.8% | One-day fall (AI fears) | S90, S88 | 3 Feb 2026 | Confirmed |
| ~8,216p | Share price | S90 | 5 Oct 2026 | Confirmed |
| ~£40bn | Market cap | Inferred from S90, S70 | 5 Oct 2026 | Inferred |
| ~18x | Forward P/E (vs 24x post-Refinitiv average) | S88, S89 | Jun 2026 | Reported |

**Time series for charts**

*Group total income excl. recoveries (£m, as reported each year)* [Confirmed]: 2022: 7,428 (S77); 2023: 8,009 (S77, S76); 2024: 8,494 (S76, S72); 2025: 8,986 (S72); H1 2025: 4,489; H1 2026: 4,799 (S70). 2021: not retrieved (Gap).

*Organic constant currency growth* [Confirmed, S73]: 2021 5.8%; 2022 6.3%; 2023 7.1%; 2024 7.7%; 2025 7.1%; H1 2026 8.4% (S70).

*Adjusted EBITDA margin excl. FX* [Confirmed, S73]: 2021 47.8%; 2022 47.8%; 2023 47.2%; 2024 48.8%; 2025 50.3%; H1 2026 52.7% (S70, reported basis).

*AEPS (p)* [Confirmed, S73, S70]: 2021 272.4; 2022 317.8; 2023 323.9; 2024 363.5; 2025 420.6.

*Dividend per share (p)* [Confirmed, S77, S76, S72]: 2022 107.0; 2023 115.0; 2024 130.0; 2025 150.0.

*Revenue by division, current four-division basis (£m)* [Confirmed, S72, S70]:
| Division | FY2024 (restated) | FY2025 | H1 2025 | H1 2026 |
|---|---|---|---|---|
| Data & Analytics | 3,859 | 3,978 | 1,991 | 2,061 |
| FTSE Russell | 911 | 954 | 472 | 504 |
| Risk Intelligence | 531 | 579 | 287 | 310 |
| Markets (incl. NTI) | 3,180 | 3,467 | 1,735 | 1,920 |
| Other | 13 | 8 | 4 | 4 |

*Revenue by division, old five-division basis (£m)* [Confirmed, S76]: FY2023: D&A 3,931; FTSE Russell 844; Risk Intelligence 492; Capital Markets 1,546; Post Trade 1,167. FY2024: D&A 4,010; FTSE Russell 918; Risk Intelligence 531; Capital Markets 1,828; Post Trade 1,194. (Do not splice these with the new basis without a note: cost and revenue items were reallocated.)

*Revenue by geography of service provider (£m)* [Confirmed, S74]: 2024: UK 2,717; US 3,224; Europe excl. UK 1,205; Asia 991; Other 442 (total 8,579). 2025: UK 2,918; US 3,418; Europe excl. UK 1,253; Asia 1,035; Other 457 (total 9,081).

*Employees* [Confirmed, S74]: year end 2024 27,386; year end 2025 28,516. Earlier years not retrieved (Gap).

*Share price, daily close (p)* [Confirmed, S90]: 5 Feb 2025 12,095 (peak); 27 Feb 2025 11,775; 3 Oct 2025 8,606; 2 Jan 2026 8,804; 4 Feb 2026 7,170 (low); 26 Feb 2026 8,500; 30 Jul 2026 8,606; 2 Oct 2026 8,090; 5 Oct 2026 ~8,216 (intraday).

---

## 3) Verbatim quotes actually read

1. "Our purpose is driving financial stability, empowering economies and enabling customers to create sustainable growth." (S74, Annual Report 2025)
2. "Over 70% of our income is recurring in nature and benefits from long-term customer relationships." (S74)
3. "Our customers believe our solutions are more valuable in an AI world, not less." (S70 and S72)
4. "Remember that Markets is 40% of LSEG revenue." (David Schwimmer, S71, 30 Jul 2026)
5. "Annual growth has averaged almost 10% over this period, and it's also been consistent. There have been strong years and really strong years, but no weak years." (Schwimmer on Markets, S71)
6. "90% of our data revenues come from real-time or data that is proprietary." (Schwimmer, S71)
7. "As we've said before, our sector moves slowly. Given the range and complexity of issues to address, this is a marathon, not a sprint, and LSEG is the best running partner." (Schwimmer, S71)
8. "Our Markets businesses had an exceptional first half, achieving double-digit growth through sustained investment. With our plans for LSE 24 and growing momentum of transactions on the Private Securities Market, we are opening up significant new market opportunities." (Schwimmer, S70)
9. "In Post Trade Solutions, we have aligned ourselves strategically with key customers through their investment in the business." (Schwimmer, S72)
10. "This initiative continues the strong history of strategic partnership between LSEG and market participants, replicating the original LCH model that continues to prove so successful for LCH and its customers." (S72, on the Post Trade Solutions stake sale)
11. "Due to the timing of recognition of the benefit, this year-on-year uplift will largely reverse in Q4 2026." (S70, on the SwapClear margin benefit)
12. "In H1, we significantly increased our buyback commitment to reflect the Board's view on the dislocation between the intrinsic value of the business and the prevailing share price." (S70)
13. "The collateral and default fund contributions of the defaulting Clearing Member are utilised first, followed by the CCP's own funds and then by the default fund contributions of non-defaulting Clearing Members." (S93)
14. "LSEG operates a three lines of defence model, providing appropriate segregation of duties and clear roles and responsibilities, including Risk, Compliance and Internal Audit." (S74)
15. "This strategic partnership is a significant milestone on LSEG's journey towards becoming the leading global financial markets infrastructure and data business, and will transform the experience for our customers." (Schwimmer, S79, 12 Dec 2022)
16. "LSEG regrets the Commission's decision to prohibit the proposed Merger." (S80, 29 Mar 2017)
17. "There is still a 'show me' story for AI. It's one thing to have usage, it's another to start charging people." (Michael Werner, UBS, via Reuters, S88)
18. "I don't believe the risk of disruption from AI is minimal." (Stephen Yiu, Blue Whale, via Reuters, S88)
19. A shift toward "modular, API- and AI-driven data consumption may prove structurally deflationary for parts of the model." (Redburn, via Investing.com, S89)
20. "We are delighted to be the first venue operator to have been granted a PISCES Approval Notice by the FCA." (Julia Hoggett, S96)
21. "This was not a security breach of LSEG/our systems." (LSEG spokesperson on World-Check, S99; read in search snippet only)
22. "We are having the mother of all global market outages." (unnamed London trader, 19 Jul 2024, S98)

---

## 4) Source table

| ID | Outlet | Title | Pub date | URL | Accessed | Status | Confidence note |
|---|---|---|---|---|---|---|---|
| [S70] | LSEG (primary) | Interim results for six months ended 30 June 2026 (Interim Report H1 2026) | 2026-07-30 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/interim-report/lseg-interim-report-h1-2026-30july2026.pdf | Accessed 2026-10-05 | FETCHED | Primary; full PDF read via pdftotext |
| [S71] | LSEG (primary) | H1 2026 Interim Results Presentation Transcript | 2026-07-30 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/interim-results/transcripts/lseg-h1-2026-interim-results-analyst-investor-call-transcript.pdf | Accessed 2026-10-05 | FETCHED | Primary; CEO remarks read |
| [S72] | LSEG (primary) | Preliminary results for the year ended 31 December 2025 (RNS) | 2026-02-26 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/preliminary-results/rns/lseg-2025-preliminary-results-rns-26feb2026.pdf | Accessed 2026-10-05 | FETCHED | Primary |
| [S73] | LSEG (primary) | 2025 preliminary results: More valuable in an AI world (presentation) | 2026-02-26 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/preliminary-results/presentation/lseg-2025-preliminary-results-presentation-26feb2026.pdf | Accessed 2026-10-05 | FETCHED | Primary; chart values read from text extraction |
| [S74] | LSEG (primary) | Annual Report 2025 | 2026 (Feb/Mar) | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/annual-reports/lseg-annual-report-2025.pdf | Accessed 2026-10-05 | FETCHED | Primary; exact publication date not checked |
| [S75] | LSEG (primary) | Q1 2026 Trading Update (RNS) | 2026-04-23 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/trading-statement/rns/lseg-trading-update-q1-2026-rns-23apr2026.pdf | Accessed 2026-10-05 | FETCHED | Primary |
| [S76] | LSEG (primary) | Preliminary results for year ended 31 December 2024 (RNS) | 2025-02-27 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/preliminary-results/rns/lseg-2024-preliminary-results-rns-27feb2025.pdf | Accessed 2026-10-05 | FETCHED | Primary; old five-division basis |
| [S77] | LSEG (primary) | Preliminary results for year ended 31 December 2023 (RNS) | 2024-02-29 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/preliminary-results/rns/lseg-2023-preliminary-results-rns-29feb2024.pdf | Accessed 2026-10-05 | FETCHED | Primary |
| [S78] | LSEG (primary) | History | n/d | https://www.lseg.com/en/about-us/history | Accessed 2026-10-05 | FETCHED | Primary; omits 2011 FTSE and 2021 Borsa sale |
| [S79] | LSEG (primary) | LSEG and Microsoft launch 10-year strategic partnership... | 2022-12-12 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/press-releases/lseg-and-microsoft-launch-strategic-partnership-12dec2022.pdf | Accessed 2026-10-05 | FETCHED | Primary |
| [S80] | LSEG (primary) | Recommended all-share merger between LSEG and Deutsche Börse: Termination following EC decision | 2017-03-29 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/mergers-and-acquisitions/deutsche-boerse/lseg-termination-deutsche-borse-merger-ec-decision-29mar2017.pdf | Accessed 2026-10-05 | FETCHED | Primary |
| [S81] | Concurrences | The EU Commission prohibits a merger in the financial markets (Deutsche Börse / London Stock Exchange) | 2017-03 | https://www.concurrences.com/en/bulletin/news-issues/march-2017/the-eu-commission-prohibits-a-merger-in-the-financial-markets-deutsche-borse | Accessed 2026-10-05 | SNIPPET | Corroborates S80; £21bn figure from search summary |
| [S82] | LSEG (primary) | Rejection of conditional proposal from HKEX | 2019-09-13 | https://www.lseg.com/en/media-centre/press-releases/2019/rejection-conditional-proposal-hkex | Accessed 2026-10-05 | SNIPPET | Primary but read via search summary only |
| [S83] | CNBC | Euronext acquires Borsa Italiana in a deal worth over $5 billion | 2021-04-29 | https://www.cnbc.com/2021/04/29/ma-deal-euronext-buys-borsa-italiana-from-london-stock-exchange-group.html | Accessed 2026-10-05 | SNIPPET | Price stated as about €4.4bn in snippet; exact figure unverified |
| [S84] | Finadium | LSEG completes $27bn Refinitiv acquisition | 2021-01 | https://finadium.com/lseg-completes-27bn-refinitiv-acquisition/ | Accessed 2026-10-05 | SNIPPET | 37%/29% interest detail from search summary |
| [S85] | Thomson Reuters (primary for TR) | Thomson Reuters Announces Sale of Remaining Stake in London Stock Exchange Group | 2024-05 | https://www.thomsonreuters.com/en/press-releases/2024/may/thomson-reuters-announces-sale-of-remaining-stake-in-london-stock-exchange-group | Accessed 2026-10-05 | SNIPPET | 17.3m shares at £91.50 per snippet |
| [S86] | RTÉ (Reuters/FT report) | Activist investor Elliott builds stake in LSEG | 2026-02-11 | https://www.rte.ie/news/business/2026/0211/1557838-activist-investor-elliott-builds-stake-in-lseg-ft/ | Accessed 2026-10-05 | FETCHED | Secondary, cites Reuters and FT |
| [S87] | Bloomberg | Elliott Builds Stake in London Stock Exchange Group | 2026-02-11 | https://www.bloomberg.com/news/articles/2026-02-11/activist-investor-elliott-builds-stake-in-lse-group-ft-reports | Accessed 2026-10-05 | PAYWALLED-NOT-READ | Headline only; corroborates existence of report |
| [S88] | Reuters via Yahoo Finance UK (Samuel Indyk) | Analysis: LSEG slowly sheds 'AI risk' tag with drive to show growth | 2026-06-11 | https://uk.finance.yahoo.com/news/analysis-lseg-slowly-sheds-ai-050520115.html | Accessed 2026-10-05 | FETCHED | Credible; read via summariser so quotes may be lightly trimmed |
| [S89] | Investing.com | LSEG shares drop 4% after Rothschild & Co Redburn warns on AI disruption risks | 2026-06-18 | https://www.investing.com/news/stock-market-news/lseg-shares-drop-4-after-rothschild--co-redburn-warns-on-ai-disruption-risks-4749129 | Accessed 2026-10-05 | FETCHED | Single outlet for broker note |
| [S90] | Yahoo Finance | LSEG.L chart data API (daily and monthly) | live | https://query1.finance.yahoo.com/v8/finance/chart/LSEG.L?range=2y&interval=1d | Accessed 2026-10-05 | FETCHED | Market data; monthly series has date-label quirks, daily used for key points |
| [S91] | LSEG (primary) | Financial Calendar | n/d | https://www.lseg.com/en/investor-relations/financial-calendar | Accessed 2026-10-05 | FETCHED | Q3 statement 22 Oct 2026 |
| [S92] | Investing.com | LSEG appoints ServiceNow executive to board | 2026 | https://www.investing.com/news/company-news/lseg-appoints-servicenow-executive-to-board-93CH-4926400 | Accessed 2026-10-05 | SNIPPET | Zavery start date 1 Dec 2026 per snippet |
| [S93] | LSEG / LCH (primary) | LCH Group Risk Management | n/d | https://www.lseg.com/en/post-trade/clearing/risk-management/group-risk-management | Accessed 2026-10-05 | FETCHED | Primary |
| [S94] | Bank of England (primary) | FMI Annual Report 2025-26 | 2026-06-25 | https://www.bankofengland.co.uk/financial-stability/financial-market-infrastructure-supervision/report/fmi-annual-report-2025-26 | Accessed 2026-10-05 | FETCHED | Partial; CCP list in annex not retrieved |
| [S95] | London Stock Exchange (primary) | TGHL Annual MiFIDPRU Disclosure / Turquoise documents | n/d | https://docs.londonstockexchange.com/sites/default/files/documents/tghl-annual-mifidpru-disclosure_0.pdf | Accessed 2026-10-05 | SNIPPET | RIE and MTF status from search summary; FCA register not directly checked |
| [S96] | LSEG (primary) | London Stock Exchange's new Private Securities Market receives PISCES Approval Notice by the FCA | 2025-08-26 | https://www.lseg.com/en/media-centre/press-releases/2025/london-stock-exchange-receives-pisces-approval-notice-by-fca | Accessed 2026-10-05 | FETCHED | Primary |
| [S97] | ETF Express | London Stock Exchange to launch LSE 24 | 2026-07-21 | https://etfexpress.com/2026/07/21/london-stock-exchange-to-launch-lse-24/ | Accessed 2026-10-05 | SNIPPET | Hours detail from search summary; launch confirmed in S70 |
| [S98] | Global Banking & Finance Review (Reuters) | LSEG's Workspace platform suffers widespread outage, trading hit | 2024-07-19 | https://www.globalbankingandfinance.com/lsegs-workspace-platform-suffers-widespread-outage-trading-hit | Accessed 2026-10-05 | FETCHED | Reuters syndication |
| [S99] | Bank Info Security | Hacker Threatens to Expose Sensitive World-Check Database | 2024 | https://www.bankinfosecurity.com/hacker-threatens-to-expose-sensitive-world-check-database-a-24909 | Accessed 2026-10-05 | SNIPPET | LSEG quote via snippet; multiple outlets carried the story |
| [S100] | Boston Globe | London exchange has 7-hour outage | 2008-09-09 | http://archive.boston.com/business/markets/articles/2008/09/09/london_exchange_has_7_hour_outage/ | Accessed 2026-10-05 | SNIPPET | Detail partly from Wikipedia TradElect snippet |
| [S101] | Computer Weekly | London Stock Exchange glitch delays trading | 2020-08 | https://www.computerweekly.com/news/252468724/London-Stock-Exchange-glitch-delays-trading | Accessed 2026-10-05 | SNIPPET | Quote via search summary |
| [S102] | Bloomberg | LSEG Shares Plunge on Slowing Growth in Subscription Value | 2025-07-31 | https://www.bloomberg.com/news/articles/2025-07-31/lseg-raises-margin-guidance-announces-1-billion-buyback | Accessed 2026-10-05 | PAYWALLED-NOT-READ | Headline only |
| [S103] | Proactive Investors | LSEG shares hit by growth fears but brokers see value after sharp sell-off | 2025-07/08 | https://www.proactiveinvestors.com/companies/news/1076025/lseg-shares-hit-by-growth-fears-but-brokers-see-value-after-sharp-sell-off-1076025.html | Accessed 2026-10-05 | SNIPPET | Search summary mixed in 2026 figures; only the "ASV slowdown" point is used |
| [S104] | CIO.com / TechCrunch | Microsoft signs $2.8B cloud deal with LSEG; Microsoft to acquire 4% stake | 2022-12-12 | https://www.cio.com/article/415862/microsoft-signs-2-8b-cloud-deal-with-london-stock-exchange-group.html | Accessed 2026-10-05 | SNIPPET | $5bn Microsoft revenue estimate |
| [S105] | SEC / CFTC filings | LCH SA comprehensive disclosure and rule filings | various | https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/ccp-disclosures/lch-sa-comprehensive-disclosure-as-required-by-sec-rule-17ad-22-e-23-q3-2024.pdf | Accessed 2026-10-05 | SNIPPET | ACPR, CFTC, SEC status via search summary |
| [S106] | Bank of England (primary) | BoE fines Vocalink Limited | 2025-07 | https://www.bankofengland.co.uk/news/2025/july/boe-fines-vocalink-limited | Accessed 2026-10-05 | SNIPPET | Used only to infer absence of prior FMI fines |
| [S107] | South China Morning Post | London Exchange rejects Hong Kong's surprise US$36.6 billion bid | 2019-09 | https://www.scmp.com/business/companies/article/3027187/london-stock-exchange-unanimously-rejects-hong-kongs-us366 | Accessed 2026-10-05 | SNIPPET | Corroborates S82 |
| [S108] | Investing.com | LSEG H1 2026 slides: 8.4% growth, raised guidance amid AI buildup | 2026-07-30 | https://www.investing.com/news/company-news/lseg-h1-2026-slides-84-growth-raised-guidance-amid-ai-buildup-93CH-4823305 | Accessed 2026-10-05 | SNIPPET | "AI monetisation timing" reason for results-day fall |
| [S109] | Globaldatabase.com | Bloomberg vs Refinitiv vs S&P Capital IQ | n/d | https://www.globaldatabase.com/bloomberg-vs-refinitiv-vs-sp-capital-iq-which-financial-terminal-is-worth-it | Accessed 2026-10-05 | SNIPPET | Low quality; do not rely on in interview |

---

## 5) Gaps
- **Q3 2026 trading statement** is due 22 Oct 2026 and was not out on 5 Oct 2026. Re-check before interviews.
- **FY2021 total income** and pre-2024 headcount were not retrieved; time series for income starts at 2022, headcount at 2024.
- **Dates not re-verified this session**: Schwimmer's start date (2018) and Goldman background; demutualisation year (2000); FTSE full ownership (Dec 2011); Refinitiv announcement date (Aug 2019); Tradeweb's arrival with Refinitiv. All are widely reported, but I did not fetch a source.
- **Exact Borsa Italiana price** (€4.325bn vs €4.4bn) unresolved.
- **LCH fines**: none found by Bank of England, ACPR or CFTC; absence of evidence is not proof. AMF role for LCH SA not checked.
- **FTSE Russell index errors**: none found.
- **Workspace complaints**: no credible outlet piece retrieved (FT/Bloomberg pieces likely exist but were not found or are paywalled).
- **Refinitiv cost overruns**: no evidence found; LSEG claims synergies ahead of target.
- **Elliott stake size** and any later Elliott statements (one HL headline suggests Elliott later said there was "still an opportunity for further value enhancing actions"; not read).
- **Market cap**: inferred, not sourced. Exact share count at end Sept 2026 not retrieved.
- **Revenue by customer geography** (as opposed to service-provider location) not found.
- **Analyst consensus** now (Oct 2026) not retrieved; June 2026 Reuters figures may be stale.
- Search budget for this session was exhausted before the Refinitiv integration and FTSE index-error checks could be repeated with different terms.

---

## 6) Interview angles
1. **"Markets is 40% of LSEG."** The public debate is about AI and data, but the role you are applying for sits in the division that grew 11.9% in H1 2026 and has "no weak years" in five. Show you know the Markets line items (Equities, Tradeweb-driven FIDO, FX, OTC Derivatives, NTI) and that Markets margins (58.6%) now beat D&A's (42.3%).
2. **The LCH partnership model.** LSEG keeps doing deals where customers co-own infrastructure: SwapClear founding members, 11 banks buying 20% of Post Trade Solutions, Turquoise "in partnership with the user community". A good question: "How do you balance giving members economics, like the SwapClear surplus share, against LSEG's own margin, given you paid £1.2bn to cut that share to 10%?"
3. **Explain the waterfall in 30 seconds.** Defaulter's margin and default fund first, then LCH's own skin in the game (25% of minimum regulatory capital), then other members' default fund. Margin at 99.7% confidence. This fits the JD's risk-team track.
4. **FX track.** FX revenue £145m in H1 2026 (+7.6%), volumes $561bn a day; Forward First Fixing above $330bn in Q2; Streaming FX Spot on AWS Outposts with about 70% lower latency; FXall functionality going into Workspace. Customer problem-solving in the JD maps to helping asset managers with fixing and workflow.
5. **Debt listings and shareholder analysis track.** Talk about the Private Securities Market (first PISCES operator), LSE 24, and the digital gilt (DIGIT) with HSBC as ways London is trying to win back issuers and investors.
6. **The AI debate, balanced.** Bull: 90% of data revenue is real-time or proprietary, MCP customers rising from 60 to 200+, Q1 2026 the best quarter in five years. Bear: Redburn's 30% of EBITDA at risk, Workflows growth under 3%, UBS's "show me" point on charging. A thoughtful line: "The test is whether the new AI licence and MCP charges show up in ASV and gross sales by the 2026 full-year results."
7. **Resilience as a product.** Outages (2008 TradElect, 2020 delayed open, 2024 Workspace) show that for infrastructure, reliability is the brand. Mention LSEG's own claim of 50% fewer major incidents after its engineering programme.
8. **Capital allocation and the activist.** Buybacks over £8bn since 2022, driven by the Board's view of a "dislocation" between value and share price; Elliott arrived in Feb 2026. A fair question to ask an interviewer: how do Markets teams compete for investment when so much cash goes to buybacks?
9. **Founding insight link.** The 1698 price list was data. LSEG's strategy today is joining the trade lifecycle and the data value chain. Use this as a memorable opener for "Why LSEG?".
10. **Watch list before the interview**: Q3 trading statement on 22 Oct 2026; whether the SwapClear margin uplift reverses in Q4 as guided; LSE 24 client testing by year end; Amit Zavery joining the board 1 Dec 2026.
