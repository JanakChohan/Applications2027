# WS8 + WS9: Why LSEG (built from mechanism) and Scenario Playbook Inputs

Prepared 2026-10-05 for the LSEG Business Management Summer Internship 2027 (Req R0123386). Source IDs S300-S339 (WS8) and S340-S399 (WS9). Tags: [Confirmed] = read in a primary or official source; [Reported] = read in a secondary source or a search snippet; [Inferred] = my reasoning from confirmed facts, not stated by any source.

---

## 1) Findings

### WS8.1 Why LSEG is a group of distinct regulated businesses, not one integrated firm

**What the structure actually is (legal entities and ownership, FY2025 annual report)**

| Entity / business | What it is | LSEG ownership | Source |
|---|---|---|---|
| London Stock Exchange plc | Recognised Investment Exchange (RIE); operates Main Market, AIM, ISM (an MTF it runs as an RIE) | 100% | [Confirmed] S300, S346 |
| Turquoise Global Holdings Ltd | Equity MTF, "majority owned by LSEG in partnership with the user community since 2010" | 84.2% (non-controlling interest 15.8%) | [Confirmed] S300; history [Reported] S321 |
| LCH Group Holdings Ltd (parent of LCH Ltd, UK, and LCH SA, France) | CCPs: SwapClear, ForexClear, RepoClear, EquityClear, CDSClear | 94.4% (up 0.2pt in Oct 2025) | [Confirmed] S300 |
| Tradeweb Markets | Rates, credit, equities, money markets venues; separately listed on Nasdaq (TW) | 50.9% effective economic interest (45.6% economic interest in Tradeweb Markets Inc) | [Confirmed] S300, S303 |
| LSEG PTS Holdings (Post Trade Solutions) | Compression and optimisation for uncleared derivatives (ex-Quantile/TriOptima-type services) | 80% (11 banks bought 20% for £170m, Oct 2025) | [Confirmed] S300, S301 |
| LSEG FX (FXall, FX Matching) | Dealer-to-client and dealer-to-dealer FX venues; EU MTF in Ireland (Central Bank of Ireland) and UK MTF (FCA) | 100% (ex-Refinitiv) | [Confirmed] S341, S300 |
| Data & Analytics, FTSE Russell, Risk Intelligence | Subscription businesses | 100% | [Confirmed] S303 |

**Why separate entities: the mechanisms**

1. **Regulation forces separate legal entities with their own capital and boards.** A CCP "sits in the middle of trades as the buyer to every seller and the seller to every buyer. If either party defaults on the trade, the Company owns the defaulter's risk" (S304). That risk has to be ring-fenced: LCH Ltd is regulated by the Bank of England as a Recognised Clearing House and has its own Board, Audit, Remuneration, Risk and Operational Resilience committees (S304). An exchange (RIE) is FCA-supervised, the FX MTFs are licensed separately in Ireland and the UK (S341). A failure in one should not take capital from another. [Confirmed for the regulatory facts; the ring-fencing rationale is Inferred from them.]

2. **Open access is written into LCH's constitution, so LSEG cannot run it as a captive.** When LSEG bought control of LCH.Clearnet in 2012-13, the OFT recorded that an open-access provision, "considered a core operating principle", would be put into LCH's Articles: "LCH.Clearnet's services must be offered on terms that are fair, reasonable, open and non-discriminatory... No exchange will be favoured over any other and LSEG's trading services users will not be favoured over any other exchange's users" (S305). LCH Ltd still describes itself as "operating through an open access model that clears for major exchanges and platforms as well as a range of over-the-counter ('OTC') markets" (S304). LSEG's own AR 2025: "When other exchange groups focused on vertical integration of trading and clearing, we championed open access" (S300). [Confirmed]

3. **Horizontal vs vertical silo.** The OFT described CCPs as "stand-alone companies such as LCH.Clearnet or vertically integrated with a trading venue such as Deutsche Börse/Eurex Clearing" (S305). In a vertical silo the venue and its CCP are tied, so liquidity and clearing reinforce each other inside one group. LSEG's horizontal model means LCH competes for flow from any venue, and LSEG venues do not get a privileged CCP. [Confirmed for the description; the competitive logic is Inferred.]

4. **User governance keeps the banks in.** Before 2013 LCH was "owned 83 per cent by its clearing members and 17 per cent by trading venues" (OFT, S305). LSEG appointed only 4 of 17 directors at the start, with user and venue directors and iNEDs, and "push matters" required "60 per cent of votes cast, which must consist of at least 25 per cent of user shareholders" (S305). Today: "representatives of clearing members sit on the Company's Board" and the LCH Ltd Board Risk Committee includes clearing member and client representatives "with no one constituent of the Risk Committee having a majority" (S304). Product Advisory Groups and Risk Working Groups let participants comment on "risk policies, models and frameworks" (S304). [Confirmed]

5. **The bank-partnership model is repeated on purpose.** SwapClear was "founded in collaboration with clearing members 25 years ago" (S304). Founding members got about 30% of SwapClear's revenue surplus (€0.2bn in 2024); LSEG paid £1.2bn to cut this to 15% for 2025 and 10% from 2026 to 2045, while extending the arrangement (S301). In Oct 2025, 11 banks took 20% of Post Trade Solutions, "replicating the original LCH model that continues to prove so successful" (S301). Turquoise was founded by banks and kept a user minority (S321, S358). Tradeweb was dealer-owned before IPO: a group of dealer banks "collectively held a 46% ownership interest" (S320, snippet). [Confirmed for LCH/PTS; Reported for Tradeweb/Turquoise history.]

6. **Data feeds off venues: the flywheel.** LSEG's investor deck has a page titled "Our integrated offering creates more value" with four panels: "Creating our own data flywheel", "Fully integrated workflow", "End-to-end offering", "Integrated enterprise offering" (S303). Concrete: Turquoise discloses that "All data generated from the trading systems operated by Turquoise is collated and developed before being distributed via vendors or directly to end-users" (S358); FTSE Russell has updated "the price source for a number of our indices to Tradeweb" (S300); the deck lists fixed income indices "sourced from Tradeweb" (S303). The deck also says "~98% of group revenues derived from proprietary data, IP and market infrastructure" (S303). [Confirmed]

7. **The Refinitiv logic.** The 2021 Refinitiv deal brought FXall/Matching, the Workspace desktop, real-time data and the majority Tradeweb stake (S320 snippet on Refinitiv owning Tradeweb; S300). LSEG's stated pitch: "The combination of our trade lifecycle and data value chains is unmatched. We increasingly combine the two to develop differentiated products" (S303). [Confirmed]

**What the structure costs**

| Cost | Evidence | Tag |
|---|---|---|
| Paying partners for loyalty | £1.2bn (£921m 2025 + £250m 2026) to reduce the SwapClear revenue surplus share; banks still get 10% to 2045 | [Confirmed] S301 |
| Value leaking to minorities | Non-controlling interests: Tradeweb 49.1%, PTS 20%, Turquoise 15.8%, LCH 5.6% | [Confirmed] S300 |
| Integration cost and time | Refinitiv integration costs £121m in 2025 (£166m in 2024), four years after completion | [Confirmed] S300 |
| Transformation execution risk named as a principal risk | "platform and product upgrades, cloud migration, integration of acquisitions and the execution of the LSEG-Microsoft Partnership. These initiatives introduce execution risk" (Exec leads: CEO, COO) | [Confirmed] S302 |
| Reputation contagion grows with integration | "As our different businesses have continued to become more closely integrated, potential reputational exposure has increased" | [Confirmed] S302 |
| Open access cuts both ways | Securities & Reporting revenue fell 3.0% on "the final impact of the termination of the Euronext clearing agreement"; Net Treasury Income fell on "loss of business from Euronext" | [Confirmed] S301 |
| Governance overhead and slower decisions | LSEG cannot unilaterally impose decisions on LCH; consent and push matters, user directors, member-represented risk committee (2013 design) | [Confirmed] S305, S304; "slower" is [Inferred] |
| Conflicts and information barriers | OFT: "robust conflict of interest provisions and information barriers" so rival venues can talk to LCH "assured of the confidentiality of those discussions from LSEG" | [Confirmed] S305 |
| Regulatory capital and Microsoft lock-in | LCH capital injections from parent (S304); minimum Microsoft cloud spend of $2.8bn over 10 years, plus £250-300m incremental cash costs 2023-25 | [Confirmed] S304, S308 |

### WS8.2 How the businesses work together, and where collaboration actually lives

LSEG's own words: "Partnership: Our open model is integral to how we do business. We forge long-term relationships; we work together to solve evolving needs and deliver strategic outcomes" (Code of Conduct, S307). AR 2025 headline for the integrated business: "Monetising our integrated business" (S300).

Named, verifiable cross-business links:

| Link | What it is | Source |
|---|---|---|
| RepoAgent (Post Trade Solutions + Tradeweb) | Launched Nov 2025, "helps banks and clients reduce settlement fails in the repo market"; prelim calls it evidence of "the strength of collaboration within Markets" | [Confirmed] S301, S300 |
| FTSE Russell + Tradeweb | Index price source switched to Tradeweb for a number of indices | [Confirmed] S300 |
| FXall into Workspace | "We have now added a large proportion of FXAll's functionality" to Workspace (H1 2026) | [Confirmed] S302 |
| Tradeweb into Workspace | "in the process of making Tradeweb available on the platform", first permissioned Tradeweb dealer pricing streams, then dealing between Tradeweb Institutional Viewer and Workspace | [Confirmed] S302 |
| LCH data and FTSE Russell indices in Workspace | "customers can now access FXall, FTSE Russell indices and LCH data via Workspace" | [Confirmed] S300 |
| ForexClear + CLS | CLSClearedFX redesigned July 2025, puts members' cleared FX into the main CLS settlement session | [Confirmed] S304 |
| Microsoft as shared tech | 10-year partnership (Dec 2022): data platform to Azure, Workspace in Teams/Excel; DMI "powered by Microsoft Azure"; Autex replatformed onto Azure | [Confirmed] S308, S301 |
| LSEG Everywhere | "agreed trusted, AI-ready data partnerships with leading platforms including Anthropic, Databricks, Microsoft, Open AI, Rogo and Snowflake, based on MCP infrastructure" | [Confirmed] S301 |
| Single commercial contract | LSEG Data Access (LDA): long-term deals; £1.9bn of new agreements signed in Q4 2025 (Citi, Bank of America, Standard Chartered named) | [Confirmed] S300, S303 |
| Central sales | New exec role: Chris Coleman, Group Head of Sales and Account Management (joined Jan 2026) | [Confirmed] S306 |

Note on "SwapClear + Tradeweb swaps" and "ForexClear + FXall": I did not find an LSEG statement that ties these specific pairs commercially; under the open-access rule LCH must not favour LSEG venues (S305). Do not claim a preferential link. [Gap]

### WS8.3 What value LSEG gives customers, and the counter-case

**Who the customers are (numbers)**
- Group: "44,000+ customers in over 170 countries" (S303, May 2026). The 40,000 figure in the brief is out of date. [Confirmed]
- Revenue by customer community: Banking 72%, Buy-side & Wealth 14%, Corporates 14% (S303, 2025 total income £9.3bn; footnote warns some buy-side is tagged as banking). [Confirmed]
- FXall: "2,400+ institutional clients", "200+ liquidity providers", "500+ currency pairs" (S340); fact sheet says "more than 200 providers and 2,300 buy-side institutions" and Conversational Dealing "more than 4,000 organizations and 14,000 users in more than 120 countries" (S342). The intro deck says ">2,400 buy-side customers" in 130+ countries (S303). [Confirmed; the two counts differ by document date]
- FX Matching: "over 1,000 subscribers" (search snippet of LSEG page, not read in full). [Reported]
- ForexClear: 101 clients and 45 member entities (LCH Ltd, S304); prelim KPI shows "ForexClear Members 40" for 2025 and 41 at H1 2026 (S301, S302). Different counting bases. [Confirmed, flag the definitions]
- RepoClear: 86 live members incl. 16 Sponsored Members (S304). [Confirmed]
- Fixed Income Primary Markets: "1,300 global borrowers in over 60 countries that raise $500-600 billion annually" (LSEG job ad, S316). [Reported: job ad, not audited]

**What they buy, and why they accept the fees (mechanism)**
1. *Default protection that has been tested.* Lehman: SwapClear held a "$9 trillion OTC portfolio", "over 66,000 trades", "$2 billion" initial margin; "only 35% of its initial margin" used; all positions managed by week 3; five currency auctions (S354, CCP Global). LCH says it has "managed 9 member defaults and, in all cases, losses were within the initial margin held" (S351). [Confirmed]
2. *Netting and compression free up capital.* Revenue model includes fees for "compression"; OTC Derivatives revenue up 11.6% in 2025 "driven by growth in clearing and compression activity" (S301, S304). 2023: 7.8 million SwapClear trades compressed (S356). A 2025 compression figure was not found. [Confirmed/Gap]
3. *Margin efficiency.* Initial margin at "an enhanced 99.7% confidence interval" (S351); ForexClear uses "historical simulation expected shortfall... ten years of historical market data" (S352). Customers increasingly post non-cash collateral (avg €209.6bn non-cash vs €101.3bn cash, 2025) (S301). [Confirmed]
4. *Liquidity in one place.* SwapClear: ">90% share of cleared interest rate swap notional outstanding" (S303); $1,941trn notional cleared in 2025, record 13.4m trades (S301, S304). Tradeweb ADV $2.6trn in 2025, $3.2trn H1 2026 (S301, S302). [Confirmed]
5. *Data accuracy.* "data quality issues raised by customers have fallen 51% despite total content volumes rising 113%" over four years (S301). [Confirmed]

**Counter-case (numbers from the other side)**
- FCA wholesale data market study (29 Feb 2024): "users may be paying higher prices for the data they buy than if competition was working more effectively"; markets "concentrated, usually with no more than three key providers"; but "we have not found evidence that firms cannot access the wholesale data they need"; no CMA referral (S309). [Confirmed]
- Market Structure Partners report (Feb 2025): some exchanges earned "an additional £4.93 billion in surplus revenue from market data fees since 2008"; cites Turquoise turnover down 61% (2020-22) while market data revenue rose 16.5%. LSEG replied the report "contains multiple errors" and retail data "has always been free" (S310, S311). [Confirmed as reported by The TRADE]
- Users organise against fee changes: IPUG members considered legal action over CME licensing changes in 2025 (snippet, S324). [Reported; not LSEG-specific]
- Banks build or co-own alternatives: historically Turquoise and Tradeweb were bank-founded (S320, S321); today banks co-own PTS (20%) and still sit in LCH (5.6%) (S300). The bargain is "use LSEG, but keep a seat and a share". [Confirmed facts; interpretation Inferred]
- Competitors on the desktop: Bloomberg Terminal reported at $31,980 a year from 2025 (S323 snippet); Workspace third-party estimates around $22,000 per user (snippet, low confidence). LSEG itself says it is "#2 financial desktops" (S303). [Reported/Confirmed]

### WS8.4 The "non-core" side: central functions

**Size and footprint** [Confirmed, S300 note 4]: 28,516 employees at 31 Dec 2025 (27,386 in 2024); average 27,695. By country at year end: India 8,541; UK 5,043; Europe ex-UK 3,388; US 3,218; Philippines 2,225; Other Asia 1,962; Sri Lanka 1,721; China 1,222; Africa & Middle East 540; Other 656. India is about 30% of staff [Inferred arithmetic]. Plus external contractors cut "from c. 11,000 to c. 9,200"; internal share of workforce 75% (S300). Total engineering headcount 15,101 to 14,244, insourced mix 49% to 60%, target 80% (S300). Job ads still say "25,000 people across 65 countries" (S317), the deck says "over 26,000 people in 65 countries" (S303): use the AR figure and note the ad copy is stale.

Operations hubs visible in live job ads (S319): Bangalore (RMZ Infinity, Divyasree Technopolis), Colombo, Gdynia, Manila (Taguig CitiPlaza), Bucharest, Cluj, Bangkok, Nottingham, Exeter, Paris (LCH SA), New York, Buffalo, St Louis. [Confirmed as job locations; not headcount]

**Executive team (lseg.com, read 2026-10-05, S306)** [Confirmed]
| Name | Role | Joined/appointed |
|---|---|---|
| David Schwimmer | Chief Executive Officer | not stated on page |
| Michel-Alain Proch | Chief Financial Officer | Feb 2024 (Board Mar 2024) |
| Balbir Bakhshi | Chief Risk Officer | Jan 2021 |
| Pascal Boillat | Chief Operating Officer | 1 Jul 2024 |
| Irfan Hussain | Chief Information Officer | Jan 2024 |
| Catherine Johnson | General Counsel | not stated |
| Erica Bourne | Chief People Officer | appointed Jan 2023 |
| Steve John | Chief Corporate Affairs & Marketing Officer | Apr 2025 |
| Chris Coleman | Group Head of Sales and Account Management | Jan 2026 |
| Gianluca Biagini | Co-Head of Data & Analytics | Aug 2025 |
| Ron Lefferts | Co-Head of Data & Analytics | Aug 2025 |
| Daniel Maguire | Group Head, LSEG Markets and CEO, LCH Group | ExCo since 2017 |

Daniel Maguire runs the division this internship sits in. No standalone Chief Strategy Officer is listed. [Confirmed absence on that page]

**How functions are wired to the front line**
- Risk ownership is set by principal risk, each with a named executive lead: e.g. Central counterparty risk: Head of Markets; Technology and cyber: CIO; Business continuity: COO, CRO, Divisional Group Heads; Third-party: COO, Divisional heads, CIO; Data: Divisional heads, COO; Regulatory change: General Counsel, CEO, Divisional heads (S302). [Confirmed]
- Three lines: "Accountability for risk management across the end-to-end product or service delivery sits within the first line of defence, independent oversight and challenge with the second line and objective, independent assurance with the third line" (S300). [Confirmed]
- Group Risk has central teams (Policy, Tooling, Cyber, Sustainability, TPRM) and "Coverage (Data and Analytics, Markets, Post Trade and Operations)"; it reports to a "Non-Financial Risk Committee, Executive Risk Committee, Audit Committee and Board" (job ad S314). [Confirmed as job ad text]
- First-line risk inside LCH: "First Line Business Continuity Management team at LCH Ltd" coordinating "EMIR switch testing, WAR site testing", TPRM MI for "senior management, committees and Board forums", and "Central Bank Attestation Support" (S318). [Confirmed]
- Business management / change: CDSClear Business Programme Manager coordinates "Risk, Operations, Product, Technology, Client Services, Legal, Compliance, Finance and Shared Services" and gives "decision support and recommendations to senior management, governance forums and steering committees" (S315). [Confirmed]
- Commercial: FX Senior Account Manager must "Identify upsell, cross-sell, and new business opportunities across FX trading, workflow, data, and related LSEG solutions" and lead "business reviews" (S313). DCM origination works with "Issuer Services, FTSE Russell, Admissions, Regulation, RNS, LSEG FX and Data & Analytics" and must "Execute market research and intelligence, competitive analysis and assist with internal reporting for LSEG management" (S316). [Confirmed]
- Search for "chief of staff" returned only 2 unrelated roles; "COO office" roles did not surface by title (S319). [Gap: COO-office structure for Markets not confirmed]

### WS8.5 "Why LSEG" drafts

**30 seconds**
"What draws me to LSEG is how it is built. It owns venues like the London Stock Exchange, Tradeweb and FXall, but its clearing house, LCH, has open access written into its constitution: it must clear on fair, non-discriminatory terms even for trades from rival venues, and banks still sit on its risk committee. That is why the market trusts it with over 90% of cleared interest rate swaps. Business management sits at the joins between those businesses, and that is where I want to learn."

**2 minutes**
"I want to work at LSEG because its advantage comes from a structure that is unusual, and the business management role is where you see that structure working.

First, the structure. LSEG is not one integrated exchange. LSE plc, Turquoise, LCH Ltd and LCH SA, the FX MTFs and Tradeweb are separate regulated entities, and LCH's articles say no exchange will be favoured and LSEG's users won't be favoured over anyone else's. Deutsche Börse went the other way, tying Eurex trading to Eurex clearing. LSEG chose open access and kept the banks inside: user directors, a risk committee where members and clients sit, and in 2025 it repeated the model by selling 20% of Post Trade Solutions to 11 banks.

Second, why customers pay. In 2008 SwapClear managed Lehman's $9 trillion swap book using about a third of Lehman's own initial margin, and LCH says all nine member defaults it has handled stayed within initial margin. That track record is why SwapClear cleared a record $1,941 trillion notional last year.

Third, where the businesses meet. The flywheel only works if trading turns into data and data into products, and LSEG is visibly doing that: FTSE Russell pricing some indices off Tradeweb, RepoAgent built by Post Trade Solutions and Tradeweb, FXall now largely inside Workspace.

I also see the tension. The FCA found users may be paying more for data than with stronger competition, and open access meant Euronext could take its clearing away. So the job is not just growth but keeping customers' trust while charging for value. That mix of numbers, customers and risk is what the four rotations offer, and it is what I want to spend the summer on."

**The close (one specific thing to work on)**
"If I could pick one thing, it would be the FXall move into Workspace. LSEG says a large share of FXall's functionality is now in Workspace. I'd like to help measure whether FX clients are actually moving their workflow: which client segments have switched, where post-trade or permissioning issues come up in onboarding, and whether it changes retention or cross-sell. It touches the FX customer team, the data side and operational improvement at the same time."
Alternates by rotation: Primary Markets: ISM admissions turnaround against the stated 3-day/2-day comment windows (S347); Risk: tracking the BCM and third-party risk MI that LCH first line produces (S318); BI: Tradeweb ADV vs revenue capture (S301).

### WS8.6 What most candidates say vs what this candidate can say

| Most candidates say | This candidate can say (with source) |
|---|---|
| "LSEG is a global leader" | "It is #1 in rates trading venues by volume via Tradeweb and has over 90% of cleared IRS notional outstanding at SwapClear" (S303) |
| "I'm interested in data" | "~98% of revenue comes from proprietary data, IP and infrastructure, and Turquoise's own trading data is packaged and sold through vendors" (S303, S358) |
| "LSEG has diverse businesses" | "They are separate regulated entities by design: LCH must clear on open, non-discriminatory terms; LSEG owns 94.4% of LCH, 50.9% of Tradeweb, 84.2% of Turquoise, 80% of PTS" (S300, S305) |
| "I like your values" | "Partnership is defined as 'Our open model is integral to how we do business', which is literally the LCH open-access clause" (S307, S305) |
| "Risk management is important" | "Initial margin is set at 99.7% confidence; nine defaults all within initial margin; Lehman used about 35% of IM" (S351, S354) |
| "LSEG is innovative" | "RepoAgent (PTS + Tradeweb), CLSClearedFX for ForexClear, LSE 24 planned for H1 2027" (S301, S304, S302) |
| "I want exposure across the business" | "The graduate ad says the Markets programme 'brings together our Capital Markets and Post Trade businesses'; I want the joins, e.g. FXall in Workspace" (S312, S302) |
| "Customers trust LSEG" | "Banks keep a stake to keep a say: 10% of the SwapClear surplus to 2045, 20% of PTS, user seats on the LCH risk committee" (S301, S304) |

### WS8.7 Honest counter-case list (be ready to hear or raise these)
1. Data pricing: FCA says users may overpay; MSP says £4.93bn surplus across some exchanges; LSEG disputes errors (S309-S311).
2. Open access means customers and venues can leave: the Euronext clearing loss hit 2025 revenue (S301).
3. Minority leakage: half of Tradeweb's economics belong to other shareholders (S300).
4. Paying for partnership: £1.2bn to banks to cut the SwapClear surplus share, which they still keep at 10% to 2045 (S301).
5. Integration is long and costly: Refinitiv integration costs still £121m in 2025 (S300); transformation and Microsoft execution are principal risks (S302).
6. Tighter integration raises reputational contagion (S302).
7. Heavy offshoring and contractor reduction: 30% of staff in India, contractors down ~1,800 in a year (S300). For an intern this means much operations work sits in hubs, and London roles are coordinating ones [Inferred].
8. Concentration of systemic risk: LCH is a single point of failure for swaps; cyber "could... pose systemic risks" (S302).

---

### WS9 Scenario playbook fact base

#### (a) FX customer account management and post-sale

**Product facts** [Confirmed unless noted]
- FXall (dealer-to-client): RFQ (QuickTrade), PriceStream (disclosed bank streams), Orderbook (anonymous ECN using prime brokers), Advanced Execution (aggregates the two), resting and algo orders (TWAP, Peg, Iceberg, Hidden) (S342).
- FX Matching: anonymous dealer-to-dealer central limit order book (S303; "over 1,000 subscribers" [Reported]).
- Regulated venues: EU MTF in Ireland "authorised and supervised by the Central Bank of Ireland" (FXall RFQ and Forwards Matching); UK MTF "authorised and supervised by the Financial Conduct Authority" (S341). The platform supports "best execution with pre-trade checks for price, size and volatility" (S341).
- Post-trade on FXall: "confirmations, settlement instructions, and Trade Performance Reporting", STP via "Trade Notification", booking of off-platform trades with "full STP", FIX API, OMS/TMS integration (S340).
- TCA: Trade Performance Reporting lets clients "evaluate the cost and effectiveness of your execution strategies" (S340).
- Onboarding: done in "FXall Admin", the "reference data and permissioning tool"; tasks include onboarding buy-side and sell-side clients, NDF Matching participant data and "Price Stream Entitlement requests" (S317).
- Volumes: FX ADV $525bn in 2025 (+9.6%), $561bn in H1 2026 (+5.8%); FX revenue £272m (2025), £145m (H1 2026) (S301, S302). Revenue mix ~75% transactional, ~25% recurring (membership and data fees) (S303). Forward First Fixing: "over $330 billion of volume executed" in Q2 2026 (S302).
- Settlement: CLSSettlement settles "over USD8.0 trillion of payments" a day in "18 of the most actively traded currencies", PvP, "over 75" members (S345). ForexClear's CLSClearedFX (July 2025) moved cleared FX into the main CLS session (S304).

**FX Global Code (updated Dec 2024, S343)** principles to quote in scenarios [Confirmed]
- P17 Last look: "Market Participants employing last look should be transparent regarding its use and provide appropriate disclosures to Clients." Defined as "a final opportunity to accept or reject the request against its quoted price."
- P19: "clearly and effectively identify and appropriately limit access to Confidential Information."
- P20: "should not disclose Confidential Information to external parties, except under specific circumstances."
- P45: novations, amendments, cancellations "in a carefully controlled manner."
- P46: "confirm trades as soon as practicable, and in a secure and efficient manner"; automated matching "strongly recommended"; confirmation segregated from trading.
- P48: "identify and resolve confirmation and settlement discrepancies as soon as practicable."
- P50: measure settlement risk like credit exposure where PvP is not practicable.
- P51: use Standard Settlement Instructions, maintained by staff segregated from sales and trading.
- GFXC guidance (snippet, S344): last look "should not be used for purposes of information gathering". [Reported]

**Realistic client issues and the fact you would reach for**
| Issue | Fact to anchor the answer |
|---|---|
| Trade break / mismatched confirm | P46, P48; FXall provides confirmations and STP (S340, S343) |
| Rejected trades / last look complaint | P17 disclosure duty sits with the liquidity provider; venue can supply Trade Performance Reporting data (S340, S343). [Inferred split of duties] |
| Best execution / TCA request | Trade Performance Reporting; MTF pre-trade checks (S340, S341) |
| Connectivity outage | Technology risk: "system outages... could impact customer access" (S302); escalate per incident process; BCM testing exists (S318) |
| Permissioning / new stream not showing | Price Stream Entitlement requests in FXall Admin (S317) |
| Another client asks what a big bank is doing | Code P19/P20 and Code of Conduct "must never disclose confidential information... unless there is a legitimate need to know" (S343, S307) |
| Fee query | Revenue model mixes membership/data fees and transaction fees (S303); "fee schedule" detail not found [Gap] |

#### (b) Primary Markets and debt listings

- **ISM**: "a specialist market designated for qualified investors... prescribed by Regulation 16 of the POATR"; "a UK MTF and is operated by the Exchange as a Recognised Investment Exchange"; admission "determined by the Exchange"; approval "is not an approval or verification by the Exchange of the Admission particulars"; ISM securities "are not admitted to the Official List maintained by the FCA"; "Admission particulars are not required for exempt issuers"; an "express route" exists (ISM Rulebook, January 2026, S346). [Confirmed]
- **ISM timetable** (info pack, S347): comments "within three days of your first submission"; "within two days of your subsequent submissions"; final particulars and signed ISM Form 1 "by 9:00 am (UK local time) one business day before" admission; pricing supplements under a programme "before 2:00 pm... one business day prior"; decision announced "via a Dealing Notice... on RNS"; branded "COMPETITIVE TURNAROUND TIMES (3+2)"; direct submission, "no listing agents are required". [Confirmed; pack is older than the 2026 rulebook, so check current timings]
- **Main Market vs ISM vs PSM** (info pack table, S347): reviewer LSEG vs UKLA (now FCA); admission particulars vs full prospectus vs listing particulars; ISM and PSM professional only. The pack cites the Prospectus Directive and UKLA, which are out of date: the 2026 rulebook refers to POATR and "PRMs" (Prospectus Rules: Admission to Trading on a Regulated Market) (S346). [Confirmed; use the rulebook terms]
- **Continuing obligations**: ISM rulebook Section 4; issuer "must Publish without delay" listed details; annual report "without delay"; disclosure of future inside information "as required to be made public under the UK Market Abuse Regulation" (S346). [Confirmed]
- **MAR**: inside information is "information of a precise nature, which has not been made public... likely to have a significant effect on the prices" (Art 7(1)(a)); reasonable investor test (Art 7(4)) (S349). Insider lists: issuers must "draw up a list of all persons who have access to inside information", including advisers; contents include identity, reason, "date and time" of access; retain "at least five years" (Art 18, S348). Art 17: disclose as soon as possible, delay allowed only under 17(4), and FCA must be told after (S350 snippet). [Confirmed / Reported]
- **Pipeline confidentiality at LSEG**: Code of Conduct prohibits trading "on confidential, proprietary, inside and/or material non-public information" and requires need-to-know (S307). [Confirmed]
- **Scale**: 1,300 borrowers, 60+ countries, $500-600bn a year; ISM and Sustainable Bond Market "key engines of growth" (S316). [Reported]

#### (c) Business intelligence, strategy and operational improvement

**KPIs LSEG Markets publishes** (prelim KPI table, S301; H1 2026, S302) [Confirmed]
| KPI | 2025 | H1 2026 |
|---|---|---|
| UK value traded, average daily | £4.8bn (+14.3%) | £6.67bn (+33.5%) |
| Tradeweb ADV, all asset classes | $2.62trn (+16.9%) | $3.2trn (+24.8%) |
| FX average daily total volume | $525bn (+9.6%) | $561bn (+5.8%) |
| SwapClear IRS notional cleared | $1,941trn (+21.2%) | $1,165trn (+29.4%) |
| SwapClear client trades | 5.31m (+33%) | 3.28m (+23.8%) |
| ForexClear notional | $48.1trn (+31.4%) | $33.3trn (+45.2%) |
| ForexClear members | 40 | 41 |
| EquityClear trades | 1,077m | n/a read |
| RepoClear nominal | €334.2trn (+7.8%) | n/a read |
| Avg non-cash / cash collateral | €209.6bn / €101.3bn | n/a read |
| Markets adjusted EBITDA margin | 55.6% | 58.6% |

Revenue capture [Inferred method]: revenue / volume, e.g. FX £272m on $525bn ADV; useful as a BI exercise, but LSEG does not publish a capture rate in these documents.

**Operational improvement methods LSEG names** [Confirmed, S300, S301]: Zero-Based Budgeting; insourcing engineers (49% to 60%, target 80%); single coding platform (95% of code); AI coding tools; "increased our velocity by 25%, while reducing major incidents by 50%"; AI Q&A cut query resolution time by 40% across 22,000 queries a month; customer AI search resolving ~70% without an agent; webcast transcripts from 8 hours to 10 minutes; "unified revenue and billing platform" in progress.

#### (d) Risk

- **Three lines and ERMF** (S300): Enterprise Risk Management Framework, Group Risk Taxonomy, Board Audit and Board Risk committees plus executive committees; three lines definition quoted above. [Confirmed]
- **LCH default waterfall** (S351): defaulter's collateral and default fund first, then "the CCP's own funds ('skin-in-the-game')", then non-defaulters' default fund. IM at 99.7% (Listed Rates 99%); "multiple intraday margin calls"; annual group-wide fire drill testing "All layers in the default waterfall". [Confirmed]
- **Default Management Group**: LCH staff plus senior member representatives; may hedge or go to close-out (LCH SA DMP, S353). Lehman steps: traders from six SwapClear banks on a rota, macro hedges, client porting, five currency auctions (S354). [Confirmed]
- **Lehman figures to quote**: $9trn notional, 66,000+ trades (66,390 in LCH's 2008 release per snippet S355), 5 currencies, about 35% of IM used, no default fund used, resolved within three weeks (S354, S355). [Confirmed S354; Reported S355]
- **Supervision**: LCH Ltd "Recognised Clearing House" supervised by the Bank of England; BoE non-objection for LCH Ltd board appointments (S304); BoE supervises CCPs to "protect and enhance financial stability in the UK" (S357). Board meets regulators during the year (S304). [Confirmed]
- **Principal risks with owners** (S302): Global economic and geopolitical; Sustainability; Reputation/brand/IP; Transformation; Central counterparty; Model risk (margining, market abuse detection, stress testing, AI models); Technology; Information and cyber; Business continuity; Third-party; Data; People and talent; Regulatory change and compliance. [Confirmed]
- **Operational resilience in practice**: LCH first-line BCM, BIAs, BCPs, EMIR switch testing, work-area recovery site testing, TPRM, central bank attestations (S318). Group control framework: material control assessments and attestations, risk event and issue management standards (S314). [Confirmed]
- **Incidents**: "reducing major incidents by 50%" (S301). Specific named LSE/LCH outage incidents not sourced in this pass [Gap].
- **Speak Up**: "confidential and if preferred, anonymous, channels", "independent, 24-hour Speak Up hotline", Audit Committee briefed; "In 2025, 192 reports were received" (S300). Code: "you must follow the Speak Up Policy and not look the other way"; "LSEG does not tolerate retaliation"; channel lseg.ethicspoint.com (S307). [Confirmed]

**Values (verbatim, Code of Conduct S307)** [Confirmed]
- Integrity: "We stand by our principles and deliver on our promises. We earn trust by acting responsibly."
- Partnership: "Our open model is integral to how we do business. We forge long-term relationships; we work together to solve evolving needs and deliver strategic outcomes."
- Excellence: "Our breadth of capabilities sets us apart, globally. We achieve industry-leading outcomes by combining unique, diverse perspectives and knowledge across markets."
- Change: "We embrace change. We combine human ingenuity, technology, risk management, and insight to create the products and services that lead and shape the industry."
A separate "Our behaviours" framework was not found (lseg.com/our-culture returned 404) [Gap].

---

## 2) Key numbers table

| Number | Value | Date | Source | Tag |
|---|---|---|---|---|
| Customers / countries | 44,000+ / 170+ | May 2026 deck | S303 | Confirmed |
| Employees at year end | 28,516 | 31 Dec 2025 | S300 | Confirmed |
| Employees in India | 8,541 | 31 Dec 2025 | S300 | Confirmed |
| External contractors | c. 11,000 to c. 9,200 | 2025 | S300 | Confirmed |
| Engineering headcount | 15,101 to 14,244; insourced 60% | 2025 | S300 | Confirmed |
| Group total income | £9.3bn | 2025 | S303 | Confirmed |
| Markets share of revenue | 39% | 2025 | S303 | Confirmed |
| Markets total income | £3,467m; EBITDA margin 55.6% | 2025 | S301 | Confirmed |
| LSEG stake in LCH Group | 94.4% | FY2025 | S300 | Confirmed |
| LSEG stake in Tradeweb | 50.9% effective | FY2025 | S300 | Confirmed |
| LSEG stake in Turquoise | 84.2% | FY2025 | S300 | Confirmed |
| LSEG stake in PTS | 80% (banks 20%, £170m) | Oct 2025 | S300, S301 | Confirmed |
| SwapClear surplus share | 30% to 15% (2025) to 10% (2026-2045); £1.2bn paid | Oct 2025 | S301 | Confirmed |
| SwapClear notional cleared | $1,941trn; 13.4m trades | 2025 | S301, S304 | Confirmed |
| Cleared IRS share | >90% of notional outstanding | 2026 deck | S303 | Confirmed |
| Lehman SwapClear book | $9trn, 66,000+ trades, ~35% IM used | Sep-Oct 2008 | S354 | Confirmed |
| LCH defaults managed | 9, all within IM | current page | S351 | Confirmed |
| IM confidence | 99.7% (Listed Rates 99%) | current page | S351 | Confirmed |
| FXall clients / LPs / pairs | 2,400+ / 200+ / 500+ | current page | S340 | Confirmed |
| FX ADV | $525bn (2025); $561bn (H1 2026) | | S301, S302 | Confirmed |
| Tradeweb ADV | $2.6trn (2025); $3.2trn (H1 2026) | | S301, S302 | Confirmed |
| ForexClear ADV | $188bn | 2025 | S304 | Confirmed |
| CLS daily settlement | >$8.0trn, 18 currencies | current page | S345 | Confirmed |
| Refinitiv integration costs | £121m (2025), £166m (2024) | | S300 | Confirmed |
| Microsoft deal | 10 years; ~4% stake; $2.8bn min cloud spend | 12 Dec 2022 | S308 | Confirmed |
| LDA deals signed | £1.9bn | Q4 2025 | S303 | Confirmed |
| Speak Up reports | 192 | 2025 | S300 | Confirmed |
| ISM review | 3 days first, 2 days subsequent | info pack | S347 | Confirmed |
| Debt primary markets | 1,300 borrowers, $500-600bn/yr | job ad 2026 | S316 | Reported |
| FCA data study | published 29 Feb 2024 | | S309 | Confirmed |
| MSP data "surplus" claim | £4.93bn since 2008 | Feb 2025 | S310 | Reported |

---

## 3) Verbatim quotes actually read

1. "When other exchange groups focused on vertical integration of trading and clearing, we championed open access – and stay true to this philosophy today with our market infrastructure and our data." (LSEG AR 2025, S300)
2. "LCH.Clearnet's services must be offered on terms that are fair, reasonable, open and non-discriminatory, and on a basis such that LCH.Clearnet's risk is adequately controlled. No exchange will be favoured over any other and LSEG's trading services users will not be favoured over any other exchange's users." (OFT decision, S305)
3. "operating through an open access model that clears for major exchanges and platforms as well as a range of over-the-counter ('OTC') markets." (LCH Ltd 2025 accounts, S304)
4. "The composition of the Risk Committee is governed by UK EMIR and EMIR (as amended) and includes representatives of Clearing Members and Clients, with no one constituent of the Risk Committee having a majority." (S304)
5. "This initiative continues the strong history of strategic partnership between LSEG and market participants, replicating the original LCH model that continues to prove so successful for LCH and its customers." (Prelims 2025, S301)
6. "Reflecting the strength of collaboration within Markets, in November we launched RepoAgent, a collaboration between Post Trade Solutions and Tradeweb." (S301)
7. "We have now added a large proportion of FXAll's functionality and are in the process of making Tradeweb available on the platform." (H1 2026, S302)
8. "As our different businesses have continued to become more closely integrated, potential reputational exposure has increased." (H1 2026 principal risks, S302)
9. "The combination of our trade lifecycle and data value chains is unmatched. We increasingly combine the two to develop differentiated products" (Intro to LSEG, S303)
10. "Accountability for risk management across the end-to-end product or service delivery sits within the first line of defence, independent oversight and challenge with the second line and objective, independent assurance with the third line." (AR 2025, S300)
11. "users may be paying higher prices for the data they buy than if competition was working more effectively" (FCA MS23/1, S309)
12. "managed 9 member defaults and, in all cases, losses were within the initial margin held" (LCH Group risk page, S351)
13. "The Group Risk team... should be seen as a strategic partner with deep relationships that proactively identifies, escalates and supports management of risks." (Job ad R0122830, S314)
14. "Identify upsell, cross-sell, and new business opportunities across FX trading, workflow, data, and related LSEG solutions." (Job ad R0122999, S313)
15. "This graduate programme brings together our Capital Markets and Post Trade businesses to offer a comprehensive suite of solutions." (Graduate ad R0123406, S312)
16. "Admission of Securities to trading on ISM is determined by the Exchange. Approval of an application for admission of Securities to trading on ISM is not an approval or verification by the Exchange of the Admission particulars" (ISM Rulebook Jan 2026, S346)
17. "Market Participants employing last look should be transparent regarding its use and provide appropriate disclosures to Clients." (FX Global Code P17, S343)
18. "If you witness or learn about inappropriate conduct in the workplace or which relates to LSEG, you must follow the Speak Up Policy and not look the other way." (Code of Conduct, S307)

---

## 4) Source table

[S300] | LSEG | Annual Report 2025 | 2026 (FY2025; exact date not captured) | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/annual-reports/lseg-annual-report-2025.pdf | Accessed 2026-10-05 | FETCHED | Primary; full PDF text read for ownership note 19, employee note 4, risk, Speak Up, CFO review
[S301] | LSEG | 2025 Preliminary Results RNS | 26 Feb 2026 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/preliminary-results/rns/lseg-2025-preliminary-results-rns-26feb2026.pdf | Accessed 2026-10-05 | FETCHED | Primary; KPI table and Markets section read
[S302] | LSEG | Interim Report H1 2026 | 30 Jul 2026 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/interim-report/lseg-interim-report-h1-2026-30july2026.pdf | Accessed 2026-10-05 | FETCHED | Primary; most recent; principal risks read in full
[S303] | LSEG | An introduction to LSEG (investor deck) | May 2026 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/introduction-to-lseg.pdf | Accessed 2026-10-05 | FETCHED | Primary; marketing claims (e.g. #1, >90%) are LSEG's own
[S304] | LCH Limited | Report and Financial Statements 31 Dec 2025 | 2026 | https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/annual-reports/2025-lch-limited-financial-statements.pdf | Accessed 2026-10-05 | FETCHED | Primary; governance and business review read
[S305] | OFT (UK) | Anticipated acquisition by LSEG of control of LCH.Clearnet Group (ME/5464-12) | Decision 14 Dec 2012, published 25 Jan 2013 | https://assets.publishing.service.gov.uk/media/555de2f740f0b669c4000047/LSEG.pdf | Accessed 2026-10-05 | FETCHED | Primary regulator; 2012 governance may have changed since
[S306] | LSEG | Executive Team | live page | https://www.lseg.com/en/about-us/executive-team | Accessed 2026-10-05 | FETCHED | Primary; read via summarising fetch, names and titles reliable
[S307] | LSEG | Code of Conduct (Group CEO's message page) | live page | https://www.lseg.com/en/policies/code-of-conduct | Accessed 2026-10-05 | FETCHED | Primary; values quoted via fetch tool, verify wording on page before quoting aloud
[S308] | LSEG | LSEG and Microsoft launch 10-year strategic partnership | 12 Dec 2022 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/press-releases/lseg-and-microsoft-launch-strategic-partnership-12dec2022.pdf | Accessed 2026-10-05 | FETCHED | Primary
[S309] | FCA | MS23/1 Wholesale data market study | 29 Feb 2024 | https://www.fca.org.uk/publications/market-studies/ms23-1-wholesale-data-market-study | Accessed 2026-10-05 | FETCHED | Primary regulator; summary page only, annexes not read
[S310] | The TRADE | Some exchanges pocketing nearly £5 billion from 'inexplicable' market data price rises, finds report | 4 Feb 2025 | https://www.thetradenews.com/some-exchanges-pocketing-nearly-5-billion-from-inexplicable-market-data-price-rises-finds-report/ | Accessed 2026-10-05 | FETCHED | Secondary; report commissioned by an advocacy firm (MSP)
[S311] | The TRADE | Exchanges hit back at 'inaccurate' and 'misleading' accusations around market data costs | 4 Feb 2025 | https://www.thetradenews.com/exchanges-hit-back-at-inaccurate-and-misleading-accusations-around-market-data-costs/ | Accessed 2026-10-05 | FETCHED | Secondary; contains LSEG rebuttal
[S312] | LSEG Workday | Business Management and Sales Graduate Programme (R0123406) | posted c. 1 Oct 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/job/GBR-London-5-Canada-Square/Business-Management-and-Sales-Graduate-Programme_R0123406-2 | Accessed 2026-10-05 | FETCHED | Primary job ad via CXS API
[S313] | LSEG Workday | Senior Account Manager, FX Sales, Singapore (R0122999) | 15 Sep 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/job/SGP-Singapore-1-Raffles-Quay/Senior-Account-Manager--FX-Sales_R0122999 | Accessed 2026-10-05 | FETCHED | Primary job ad
[S314] | LSEG Workday | Director, Non-Financial Risk, Bangalore (R0122830) | 24 Sep 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/job/IND-Bangalore-TowerERMZ-Infin/Director--Non-Financial-Risk_R0122830 | Accessed 2026-10-05 | FETCHED | Primary job ad
[S315] | LSEG Workday | Business Programme Manager, CDSClear, London (R0119909) | 15 Sep 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/job/London-United-Kingdom/Business-Programme-Manager--CDSClear_R0119909 | Accessed 2026-10-05 | FETCHED | Primary job ad
[S316] | LSEG Workday | Debt Capital Markets - Business Development, New York (R0120076) | 22 Sep 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/job/New-York-United-States/Senior-Associate-Americas-Fixed-Income-Origination_R0120076-1 | Accessed 2026-10-05 | FETCHED | Primary job ad; market-size figures unaudited
[S317] | LSEG Workday | Senior Analyst, FX Venue Onboarding, Manila (R0122593) | 25 Aug 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/job/PHL-Taguig-City-CitiPlaza/Senior-Analyst--FX-Venue-Onboarding_R0122593 | Accessed 2026-10-05 | FETCHED | Primary job ad
[S318] | LSEG Workday | Senior Associate, First Line Business Continuity Management, LCH Ltd (R0123614) | 23 Sep 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/job/PHL-Taguig-City-CitiPlaza/Senior-Associate--First-Line-Business-Continuity-Management_R0123614 | Accessed 2026-10-05 | FETCHED | Primary job ad
[S319] | LSEG Workday | CXS job search results ("business management", "COO", "LCH risk", "chief of staff", "primary markets", "FX account") | 5 Oct 2026 | https://lseg.wd3.myworkdayjobs.com/wday/cxs/lseg/Careers/jobs | Accessed 2026-10-05 | FETCHED | Titles/locations only; keyword search is loose
[S320] | Tradeweb / SEC | Tradeweb Form S-1 and 10-K FY2019 (search result text) | 2019 | https://www.sec.gov/Archives/edgar/data/1758730/000110465919054160/tv529956-s1.htm | Accessed 2026-10-05 | SNIPPET | Dealer 46% pre-IPO stake from search summary; not opened
[S321] | The TRADE | LSE cuts Turquoise stake to 51% as three banks invest | c. 2010 | https://www.thetradenews.com/lse-cuts-turquoise-stake-to-51-as-three-banks-invest/ | Accessed 2026-10-05 | SNIPPET | Historical; current stake 84.2% per S300
[S322] | LSEG | LSEG has increased its majority shareholding in LCH Group | 14 Dec 2018 | https://www.lseg.com/en/media-centre/press-releases/2018/lseg-has-increased-its-majority-shareholding-lch-group | Accessed 2026-10-05 | SNIPPET | Historical context only
[S323] | NeuGroup | Bloomberg Terminals: How Much More You'll Pay Next Year | c. 2024 | https://connect.neugroup.com/public/blogs/bloomberg-terminals-how-much-more-youll-pay-next-year | Accessed 2026-10-05 | SNIPPET | $31,980 figure from search summary only; low confidence
[S324] | WatersTechnology | CME rankles market data users with licensing changes | 2025 | https://www.waterstechnology.com/data-management/7952957/cme-rankles-market-data-users-with-licensing-changes | Accessed 2026-10-05 | SNIPPET | Possibly PAYWALLED-NOT-READ; not LSEG-specific
[S340] | LSEG FX | Why choose FXall? (FXall electronic trading platform) | live page | https://lseg.com/en/fx/venues/fxall-electronic-trading-platform | Accessed 2026-10-05 | FETCHED | Primary product page
[S341] | LSEG FX | Multilateral Trading Facility (MTF) | live page | https://www.lseg.com/en/fx/venues/mtf-multilateral-trading-facility | Accessed 2026-10-05 | FETCHED | Primary; rulebooks linked not read
[S342] | LSEG FX | Active Trading on FXall fact sheet | undated | https://www.lseg.com/content/dam/fx/en_us/documents/fact-sheets/active-trading-on-fxall-fact-sheet.pdf | Accessed 2026-10-05 | FETCHED | Primary; counts may be older than S340
[S343] | Global Foreign Exchange Committee | FX Global Code (updated December 2024) | Dec 2024 | https://www.globalfxc.org/docs/fx_global.pdf | Accessed 2026-10-05 | FETCHED | Primary; principles 17, 19, 20, 45-51 read
[S344] | GFXC | Report on Last Look / revised last look guidance (search result text) | Dec 2017 onward | https://www.globalfxc.org/press/p171219.htm | Accessed 2026-10-05 | SNIPPET | Context only
[S345] | CLS Group | CLSSettlement | live page | https://www.cls-group.com/products/settlement/clssettlement/ | Accessed 2026-10-05 | FETCHED | Primary
[S346] | London Stock Exchange | International Securities Market Rulebook (effective January 2026) | Jan 2026 | https://docs.londonstockexchange.com/sites/default/files/documents/lse-ism-rulebook-jan-2026-03.pdf | Accessed 2026-10-05 | FETCHED | Primary, current
[S347] | London Stock Exchange | International Securities Market information pack | undated (pre-2021 terms) | https://docs.londonstockexchange.com/sites/default/files/documents/international-securities-market-information-pack.pdf | Accessed 2026-10-05 | FETCHED | Primary but dated: cites UKLA and Prospectus Directive
[S348] | legislation.gov.uk | UK MAR Article 18 (Insider lists) | as amended | https://www.legislation.gov.uk/eur/2014/596/article/18 | Accessed 2026-10-05 | FETCHED | Primary law
[S349] | legislation.gov.uk | UK MAR Article 7 (Inside information) | as amended | https://www.legislation.gov.uk/eur/2014/596/article/7 | Accessed 2026-10-05 | FETCHED | Primary law
[S350] | Hill Dickinson / FCA (search result text) | FCA's spotlight on delayed disclosure of inside information | c. 2024-25 | https://www.hilldickinson.com/our-view/articles/fca-s-spotlight-on-delayed-disclosure-of-inside-information-when-can-and-should-issuers-delay/ | Accessed 2026-10-05 | SNIPPET | Art 17 summary; verify on FCA site
[S351] | LCH (LSEG) | Group Risk Management | live page | https://www.lseg.com/en/post-trade/clearing/risk-management/group-risk-management | Accessed 2026-10-05 | FETCHED | Primary
[S352] | LCH (LSEG) | ForexClear: Our Risk Management Philosophy | live page | https://www.lseg.com/en/post-trade/clearing/lch-services/forexclear/risk-management | Accessed 2026-10-05 | FETCHED | Primary
[S353] | LCH SA | LCH SA Default Management Process (presentation) | undated | https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/lch-sa-default-management-process.pdf | Accessed 2026-10-05 | FETCHED | Primary; slide text fragmentary
[S354] | CCP Global | The Lehman Case | undated | https://ccp-global.org/the-lehman-case | Accessed 2026-10-05 | FETCHED | Industry association; consistent with LCH 2008 release
[S355] | LCH.Clearnet | $9 trillion Lehman OTC interest rate swap default successfully resolved | 8 Oct 2008 | https://secure-area.lchclearnet.com/media_centre/press_releases/2008-10-08.asp | Accessed 2026-10-05 | SNIPPET | Domain unreachable (DNS); 66,390 trades from search text
[S356] | Markets Media | LCH's SwapClear Has Record Year for Total Notional Cleared | c. Jan 2024 | https://www.marketsmedia.com/lchs-swapclear-has-record-year-for-total-notional-cleared/ | Accessed 2026-10-05 | FETCHED | Secondary; 2023 data
[S357] | Bank of England | Financial market infrastructure supervision | live page | https://www.bankofengland.co.uk/financial-stability/financial-market-infrastructure-supervision | Accessed 2026-10-05 | FETCHED | Primary regulator
[S358] | Turquoise Global Holdings | Market data transparency obligation disclosures 2025 | 2025 | https://docs.londonstockexchange.com/sites/default/files/documents/turquoise-tghl-rcb-disclosure-document-2025.pdf | Accessed 2026-10-05 | FETCHED | Primary regulatory disclosure

---

## 5) Gaps

1. 2025 SwapClear compression volume (trades or notional compressed): not found; latest read is 7.8m trades compressed in 2023 (S356).
2. No LSEG statement found tying SwapClear to Tradeweb swaps, or ForexClear to FXall, as a commercial bundle. Open access forbids favouring LSEG venues (S305).
3. FX Matching "over 1,000 subscribers" seen only in a search snippet.
4. LSEG FX's own last-look disclosure and FX Global Code Statement of Commitment not read (search budget ran out).
5. No named LSE/LCH outage or BoE enforcement case sourced in this pass. Do not cite one from memory.
6. "Our behaviours" framework not found; lseg.com/en/about-us/our-culture returned 404.
7. No published headcount for Finance, Risk, Legal, HR etc. Only total, country split and engineering headcount exist (S300).
8. COO-office or business-management team structure inside Markets/LCH not confirmed from postings; "chief of staff" search returned nothing relevant.
9. Current Main Market debt admission process under POATR/PRM (from 19 Jan 2026) not read in FCA source; the ISM info pack is outdated on this.
10. LSEG FX fee schedules and how FX billing queries are handled: not found.
11. Tradeweb pre-IPO dealer ownership read only as a search summary (S320).
12. FCA wholesale data study annexes (MDV annex names firms' practices) not read.

---

## 6) Interview angles

1. **Lead with the open-access clause.** It explains structure, values (Partnership is defined as "our open model") and why banks trust LCH. One sentence, then a number (>90% of cleared IRS).
2. **Show you know the price of partnership.** £1.2bn paid to SwapClear founders, 10% surplus share until 2045, 20% of PTS sold to banks. Ask: "How does the Markets team decide when user ownership is worth the cost?"
3. **Use the H1 2026 integration facts.** FXall functionality largely in Workspace; Tradeweb next. Ask the interviewer what success metrics they use for that migration.
4. **FX scenario playbook.** For a client complaint: listen, check data (Trade Performance Reporting, confirmations), apply FX Global Code P17/P19/P46/P48, escalate outages under technology risk process, never share other clients' information.
5. **Primary Markets scenario.** Anchor on ISM 3+2 review windows, Dealing Notice on RNS, MAR Art 18 insider lists, need-to-know. If asked about a pipeline issuer by a friend: refuse, cite Code of Conduct.
6. **BI scenario.** Use the published KPI set (ADV, notional cleared, client trades, members, collateral) and compute revenue per unit of volume; say clearly it is your own metric.
7. **Risk scenario.** Waterfall order, 99.7% IM, nine defaults within IM, fire drills, three lines, principal risks with named executive owners. Lehman: $9trn, about 35% of IM used, three weeks.
8. **Counter-case maturity.** Volunteer the FCA data finding and the Euronext clearing loss, then explain what LSEG does about each (long-term LDA contracts and transparent rights management; open access as a deliberate trade-off).
9. **Strength-based video interview.** Map stories to the four values using LSEG's own definitions (S307); "what you achieve is equally important as how" in the JD matches Integrity's "deliver on our promises" and "acting responsibly".
10. **Know the boss's boss.** Daniel Maguire: Group Head, LSEG Markets and CEO, LCH Group (S306). Chris Coleman's new Group Sales and Account Management role (Jan 2026) signals centralised account management, relevant to the FX customer rotation.
