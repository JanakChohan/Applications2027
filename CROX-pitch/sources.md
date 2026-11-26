# sources.md - Crocs, Inc. (CROX) pitch

Compiled 2026-11-26. Market data as of the 2026-11-25 close unless stated. Labels: **reported** (company filings or statements), **consensus**, **broker** (named), **my estimate**.

Raw files are in `data/` (SEC filings in `data/sec/` and as text in `data/sec_txt/`; market data in `data/market/`; peers in `data/sa/`; transcripts in `data/transcripts/`; web-research notes with per-item URLs in `data/research/`).
All calculations are in `scripts/` and can be re-run in numeric order (01 to 17).

| ID | Source | URL | Used for | Label | As-of |
|---|---|---|---|---|---|
| S1 | Crocs 10-K FY2025 (filed 2026-02-12) | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/crox-20251231.htm | Business description, segments, FY2023-25 segment P&L, units/ASP, geography, customer concentration (none >10%), sourcing mix, debt terms, tax note (unrecognized tax benefits $637.0m), legal note, marketing expense, store counts, interest-rate sensitivity | reported | FY ended 2025-12-31 |
| S2 | Crocs 10-Q Q3 2026 (filed 2026-10-29) | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000060/crox-20260930.htm | Balance sheet 30-Sep-2026, borrowings by instrument and maturity, IEEPA refund disclosure ($67m received, $75-80m eligible), tariff rates 10-12.5%, legal proceedings, buyback authorization ($1.7bn left), segment P&L | reported | Quarter ended 2026-09-30 |
| S3 | Crocs Q3 2026 earnings release (8-K EX-99.1, 2026-10-29) | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000058/croxq32026-pressrelease.htm | Q3-26 results, non-GAAP reconciliations, revenue by brand/channel/geography, FY2026 and Q4-26 guidance | reported / guidance | 2026-10-29 |
| S4 | Crocs Q2 2026 earnings release (2026-07-30) | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000050/croxq22026-pressrelease.htm | Q2-26 results, guidance raise #2, Q3 guide | reported / guidance | 2026-07-30 |
| S5 | Crocs Q1 2026 earnings release (2026-04-30) | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000029/croxq12026-pressrelease.htm | Q1-26 results, guidance raise #1 | reported / guidance | 2026-04-30 |
| S6 | Crocs Q4 2025 earnings release (2026-02-12) | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000004/croxq42025-pressrelease.htm | FY2025 results, initial FY2026 guidance, buybacks $577m in 2025 | reported / guidance | 2026-02-12 |
| S7 | Crocs earnings releases Q2 2020 - Q3 2025 (8-K EX-99.1) | see auto-generated list below | Quarterly adjusted EPS history (P/E history), guidance history (withdrawal May-2025, Q3-25 guide-down Aug-2025), HEYDUDE guidance cuts 2023-24 | reported | various |
| S8 | Crocs 10-K FY2024, FY2023, FY2022, FY2021 | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000009/crox-20241231.htm | FY2021-24 segment revenue and income, units/ASP, brand gross margins, Crocs Brand NA/International split | reported | FY2021-FY2024 |
| S9 | Crocs 10-K FY2009 (filed 2010-02-25) | https://www.sec.gov/Archives/edgar/data/1334036/000104746910001357/a2196634z10-k.htm | Fad-bust precedent: revenue $847.4m (2007), $721.6m (2008), $645.8m (2009); gross profit $497.6m (2007), $234.0m (2008) | reported | FY2007-FY2009 |
| S10 | Crocs DEF 14A 2026 proxy (filed 2026-04-23) | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000020/crox-20260423.htm | Beneficial ownership (5% holders, insiders 3.1%), executive team, incentive design (67% PSUs; adj. EBIT margin and revenue/rTSR metrics), STIP payouts, CFO change | reported | as of 2026-03-31 |
| S11 | SEC Form 4 filings, issuer CIK 1334036, 2024-07 to 2026-11 (XML) | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001334036&type=4 | Insider open-market sales/purchases, Rule 10b5-1 checkbox; parsed in data/derived/form4_transactions.csv (each row has its EDGAR URL) | reported | through 2026-11-06 filings |
| S12 | Schedule 13G filings (FMR 2026-08-06; WIT Partners 2026-05-06; Vanguard Capital Mgmt 2026-04-29) | https://www.sec.gov/Archives/edgar/data/1334036/000031506626001989/primary_doc.xml | Large holders: FMR 3.51m sh (7.1%), WIT Partners 2.85m (5.3%), Vanguard Capital Management 2.57m (5.1%) | reported | various 2026 |
| S13 | SEC XBRL company facts, Crocs (CIK 1334036) and Deckers (CIK 910521) | https://data.sec.gov/api/xbrl/companyfacts/CIK0001334036.json | Annual financial history FY2009-FY2025 (CROX); DECK quarterly net income and diluted shares for P/E history | reported | retrieved 2026-11-26 |
| S14 | Nasdaq.com public API - CROX, DECK, BIRK, ONON, SPY, XRT daily prices | https://api.nasdaq.com/api/quote/CROX/historical?assetclass=stocks | Share prices (10 years), 52-week range, market cap; used INSTEAD of Yahoo Finance price API, which refused automated requests (HTTP 429) | market data | close of 2026-11-25 |
| S15 | Nasdaq.com public API - short interest, earnings surprise, analyst forecasts (Zacks), price targets, institutional holdings (13F) | https://api.nasdaq.com/api/quote/CROX/short-interest?assetClass=stocks | Short interest 3.49m sh (2026-11-13); consensus EPS FY26 $14.62 / FY27 $15.85 / FY28 $16.69 (5 analysts); mean PT $160.75 (low $128, high $184); 13F holders at 2026-09-30 | consensus / market data | retrieved 2026-11-26 |
| S16 | Yahoo Finance - CROX key statistics and analysis pages | https://finance.yahoo.com/quote/CROX/analysis/ | Consensus FY26 revenue $4.18bn / EPS $14.63 (14 analysts); FY27 revenue $4.34bn / EPS $16.01 (15 analysts, range $15.24-17.12); forward P/E 10.03; beta (5y monthly) 1.50; 1y target $164.67; next earnings date estimate 2027-02-11 | consensus | read 2026-11-26 |
| S17 | StockAnalysis.com - statistics, financials, forecast pages for CROX, DECK, BIRK, ONON | https://stockanalysis.com/stocks/crox/statistics/ | Peer multiples (P/S, P/FCF, EV/EBITDA, forward P/E, margins, ROIC), analyst rating changes and price targets by broker, year-end forward P/E points | market data / broker | close of 2026-11-25 |
| S18 | Macrotrends P/E pages (CROX, DECK) | https://www.macrotrends.net/stocks/charts/CROX/crocs/pe-ratio | NOT ACCESSIBLE (HTTP 403 Cloudflare). Historical P/E was instead computed from price / reported EPS (scripts/08) and cross-checked with companiesmarketcap.com year-end P/E | not found | attempted 2026-11-26 |
| S19 | companiesmarketcap.com year-end P/E (CROX, DECK) | https://companiesmarketcap.com/crocs/pe-ratio/ | Cross-check of trailing GAAP P/E 2016-2026 (CROX 7.2x end-2023, 6.8x end-2024; DECK 23.9x, 32.8x) | market data | read 2026-11-26 |
| S20 | FactSet Earnings Insight, 13-Nov-2026 | https://advantage.factset.com/hubfs/Website/Resources%20Section/Research%20Desk/Earnings%20Insight/EarningsInsight_111326.pdf | S&P 500 forward 12m P/E 18.3x; 5-year average 19.8x; 10-year average 19.1x (via web search summary - verify against the PDF) | market data | 2026-11-13 |
| S21 | Earnings call transcripts Q2 2025 - Q3 2026 (company-hosted FactSet PDFs; Motley Fool for Q3 2026) | https://www.fool.com/earnings/call-transcripts/2026/10/29/crocs-crox-q3-2026-earnings-call-transcript/ | All management quotes; product mix (clogs 74%, sandals 13%, Jibbitz 8%); China ~8% of sales, +30%; share one-third of established markets; marketplace accounting shift (270 bps Q3, 700-800 bps/qtr to Q3-27); tariff $80m annualized; leverage target 1-1.5x; 2027 colour. Raw text in data/transcripts/, notes in data/research/transcript_notes.md | reported (management statements) | 2025-08-07 to 2026-10-29 |
| S22 | Carretta v. Crocs, D. Del. No. 1:25-cv-00096 - court order and plaintiff-firm summary | https://www.ded.uscourts.gov/sites/ded/files/opinions/25-96.pdf | Securities class action: class period 2022-08-04 to 2024-10-28; motion to dismiss filed 2026-02-27, no ruling found | reported | status per 10-Q of 2026-10-29 |
| S23 | Federal Circuit, Crocs v. ITC, No. 24-1300 (2026-01-08) and coverage | https://www.cafc.uscourts.gov/opinions-orders/24-1300.OPINION.1-8-2026_2629793.pdf | 3D clog trademark case: non-infringement finding against active respondents left standing; limited exclusion order only | reported | 2026-01-08 |
| S24 | Federal Circuit, Crocs v. Effervescent/Double Diamond (Dawgs), No. 22-2160 (2024-10-03); cert denied 2025-10-06 | https://www.cafc.uscourts.gov/opinions-orders/22-2160.OPINION.10-3-2024_2395329.pdf | 'Patented Croslite' false-advertising counterclaim proceeds | reported | 2024-10-03 / 2025-10-06 |
| S25 | Piper Sandler Taking Stock With Teens (via SGB Media coverage), Fall 2026 | https://sgbonline.com/exec-who-were-the-big-brand-winners-and-losers-in-piper-sandlers-teen-survey/ | Crocs No. 10 favourite footwear brand (1% share), off the girls' top 10; Birkenstock No. 4 (5%); history No. 6 (2023) to No. 10 (2026) | broker (Piper Sandler survey), secondary source | 2026-10 |
| S26 | Broker rating actions (Goldman Sachs, Piper Sandler, Stifel, Barclays, Baird, KeyBanc, UBS) via StockAnalysis, TheFly/TipRanks, Investing.com | https://stockanalysis.com/stocks/crox/ratings/ | Goldman Sell PT $95 to $128 (2026-10-30), initiated Sell PT $88 on 2025-07-02 citing 'normalizing demand'; downgrades Aug-2025 to Jan-2026; upgrades Apr-Oct 2026 | broker (named) | 2025-07 to 2026-10 |
| S27 | USTR fact sheet, Section 301 action on ~60 economies (2026-07) | https://www.ustr.gov/about/policy-offices/press-office/fact-sheets/2026/july/fact-sheet-ustr-section-301-action-response-failure-60-economies-ban-imports-produced-forced-labor | Replacement tariffs of 10% / 12.5% after IEEPA tariffs were struck down (Supreme Court 2026-02-20) and Section 122 expired (2026-07-24) | reported | 2026-07 |
| S28 | Circana US footwear H1 2026; FDRA footwear CPI 2026 (via SGB Media / World Footwear) | https://www.circana.com/post/performance-shoe-sales-pick-up-the-pace-amid-selective-us-consumer-spending-in-the-footwear-market | US footwear dollars +1% in H1 2026 (units down), clogs among styles that grew; footwear CPI +5.2% y/y in May 2026 | industry data | 2026 |
| S29 | HEYDUDE acquisition press releases (2021-12-23 announcement; 2022-02-17 close) and 10-K FY2022 Note 3 | https://www.sec.gov/Archives/edgar/data/1334036/000133403621000204/exhibit991pressrelease1223.htm | Deal value $2.5bn ($2.05bn cash + $450m stock, 2,852,280 shares); $2.0bn Term Loan B; purchase price recorded at close ~$2.3bn | reported | 2021-12-23 / 2022-02-17 |
| S30 | Crocs 10-Q Q2 2025 (filed 2025-08-07) | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000085/crox-20250630.htm | $737m HEYDUDE impairment ($430m trademark + $307m goodwill) and valuation assumptions | reported | Quarter ended 2025-06-30 |
| S31 | Crocs investor presentations (2023 UBS deck; Q1 2026 earnings deck) | https://s22.q4cdn.com/133460125/files/doc_financials/2026/q1/Q1-2026-Earnings-Presentation-vF.pdf | Management TAM claims: $160bn casual footwear (2023 deck), $280bn+ (2025-26 decks), sandals $30bn (Q3-26 call) | reported (management claim), partly snippet only | 2023-2026 |
| S32 | News coverage of the November 2026 market sell-off and Treasury yields (AP via local outlets; TheStreet) | https://www.fox19.com/2026/11/05/brutal-sell-off-ai-stocks-sends-wall-street-reeling-sp-500-sees-worst-day-since-2025-liberation-day-tariffs/ | S&P 500 -4.4% on 2026-11-05 (AI-led); 10-year yield quoted between 4.84% and 5.13% in Nov-2026 (sources disagree) - model uses 5.0% | market data (secondary) | 2026-11 |
| S34 | Coverage of Q2 2025 results (Nasdaq/Zacks, Reuters via TradingView, Motley Fool) | https://www.nasdaq.com/articles/crocs-q2-earnings-surpass-estimates-revenues-increase-34 | Q2 2025 adjusted EPS $4.23 vs consensus $4.00-4.02 (supports 'all eight recent quarters beat EPS forecasts') | consensus (secondary) | 2025-08-07 |
| S33 | Himalaya Capital 13F coverage; No Street GP exit (Motley Fool) | https://www.fool.com/coverage/filings/2025/11/15/fund-exits-usd50-million-crocs-stake-as-guidance-weakens-and-operating-trends-cool | Himalaya Capital new position Q4 2025 (628,159 sh); No Street sold 495,000 sh in Q3 2025. Not verified against EDGAR | secondary | 2025-11 / 2026-02 |

## Figure and table source map

| Deliverable item | Sources | Script |
|---|---|---|
| Chart 01 revenue mix, 02 margins, 03 EPS/FCF/shares | S1, S3, S6, S7, S8, S13; FY26E-27E my estimates (model.xlsx) | 06, 13 |
| Chart 04-05 Crocs Brand; 06 HEYDUDE | S1, S2, S3-S8 | 06, 13 |
| Chart 07 price history; 11 earnings reactions | S14; event descriptions S3-S7, S29 | 08, 13 |
| Chart 08-09 P/E history, premium to DECK, vs index | S14, S7, S13, S15, S20 (my calculation; S18 not accessible) | 08, 13 |
| Chart 10 peers; peer table | S17 (cross-checked with S16, S15) | 09, 13 |
| Chart 12-13 revenue at risk and stress test | S3-S6 (TTM revenue), S21 (mix), S1 (distribution cost), S9 (precedent), S16 (consensus); scores are my assumptions | 10, 11, 13 |
| Chart 14 valuation range; 16 EPS bridge; all price targets | model.xlsx (my estimates) on S1-S6 inputs; S15 for sell-side targets | 11, 12, 13 |
| Chart 15 quarterly margins and GAAP gap | S3-S7 | 06, 13 |
| Insider table | S11 | 07 |
| Holder table | S10, S12, S15 | - |
| Guidance tracker | S3-S7, S21 | - |

## Where sources disagree (flagged)

- **Consensus FY2027 EPS:** Yahoo $16.01 (15 analysts) vs Nasdaq/Zacks $15.85 (5 analysts). The pitch uses Yahoo and shows both.
- **Beta:** Yahoo 1.50 (5y monthly) vs my 1.21 (5y weekly vs SPY) vs 0.67 (2y weekly). The model uses 1.20.
- **10-year Treasury yield, Nov 2026:** press reports range from 4.84% to 5.13%. The model uses 5.0%.
- **Net debt:** $1,150m on borrowings at face value less cash (mine) vs $1,500m on StockAnalysis (includes $374m of operating leases). Peer table uses the vendor definition for all four companies; my leverage figures exclude leases.
- **Share count:** 46.2m at 30-Sep-2026 (10-Q balance sheet) vs 45.73m implied by Nasdaq/StockAnalysis market cap on 25-Nov-2026. Market cap uses 45.73m.
- **DECK Sep-2026 quarter EPS:** $2.31 from XBRL net income / diluted shares vs $2.03 on Nasdaq/Zacks. Trailing DECK P/E is therefore approximate; forward P/E (consensus) is unaffected.
- **China '8% of sales':** management did not say whether this is of the Crocs Brand or the enterprise. I apply it to the Crocs Brand.
- **Barclays price target on 2026-10-15:** $139 in one source, $133 in another.
- **North America 2026:** CEO said in July 2026 the region would not return to growth in 2026, then in October that it is growing for the year excluding the marketplace shift.

## Not found

- Macrotrends historical P/E (blocked). Yahoo price history API (blocked, HTTP 429); Yahoo short % of float and holder tables (blank). Substitutes are listed above.
- Consensus forecasts by segment (brand); consensus FY2028 revenue. Segment forecasts shown are company guidance (FY26) and my estimates.
- Any published activist short report; Goldman Sachs' full Sell note; Hedgeye's short thesis (paywalled).
- Ruling on the motion to dismiss in the securities class action; damages estimate.
- Sell-through / market-share data by retailer; raw Google Trends; resale data; clog category growth rate; share of dupes.
- Long-term financial targets (none given on the last six earnings calls); investor day date; confirmed Q4 2026 earnings date.
- Oil / resin cost sensitivity; total tariffs paid in dollars.
- 2026 product mix (only FY2025: clogs 74%, sandals 13%, Jibbitz 8%).

## SEC documents downloaded (auto-generated from data/sec_filing_index.json)

| Filed | Form | URL |
|---|---|---|
| 2026-10-29 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000060/crox-20260930.htm |
| 2026-10-29 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000058/croxq32026-pressrelease.htm |
| 2026-07-30 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000052/crox-20260630.htm |
| 2026-07-30 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000050/croxq22026-pressrelease.htm |
| 2026-04-30 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000032/crox-20260331.htm |
| 2026-04-30 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000029/croxq12026-pressrelease.htm |
| 2026-04-23 | DEF 14A | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000020/crox-20260423.htm |
| 2026-02-12 | 10-K | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/crox-20251231.htm |
| 2026-02-12 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000004/croxq42025-pressrelease.htm |
| 2025-10-30 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000101/crox-20250930.htm |
| 2025-10-30 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000099/croxq32025-pressrelease.htm |
| 2025-08-29 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000094/exhibit991pressrelease82925.htm |
| 2025-08-07 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000085/crox-20250630.htm |
| 2025-08-07 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000083/croxq22025-pressrelease.htm |
| 2025-05-21 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000060/exhibit991pressrelease52125.htm |
| 2025-05-08 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000054/crox-20250331.htm |
| 2025-05-08 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000052/croxq12025-pressrelease.htm |
| 2025-02-13 | 10-K | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000009/crox-20241231.htm |
| 2025-02-13 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000007/croxq42024-pressrelease.htm |
| 2024-10-29 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000159/crox-20240930.htm |
| 2024-10-29 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000156/croxq32024-pressrelease.htm |
| 2024-08-01 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000140/crox-20240630.htm |
| 2024-08-01 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000138/croxq22024-pressrelease.htm |
| 2024-05-07 | 10-Q | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000096/crox-20240331.htm |
| 2024-05-07 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000092/exhibit991pressrelease5724.htm |
| 2024-05-07 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000090/croxq12024-pressrelease.htm |
| 2024-04-16 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000076/exhibit991pressrelease41624.htm |
| 2024-02-15 | 10-K | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000025/crox-20231231.htm |
| 2024-02-15 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000022/crox123123earningsreleasea.htm |
| 2024-02-01 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000015/exhibit991pressrelease2124.htm |
| 2024-01-08 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000012/exhibit991pressrelease1824.htm |
| 2023-12-18 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000190/exhibit991pressrelease1218.htm |
| 2023-11-02 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000166/croxq32023-pressrelease.htm |
| 2023-08-08 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000146/exhibit991pressrelease8823.htm |
| 2023-07-27 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000123/croxq22023-pressrelease.htm |
| 2023-04-27 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000053/croxq12023-pressrelease.htm |
| 2023-02-16 | 10-K | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000015/crox-20221231.htm |
| 2023-02-16 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000012/crox123122earningsreleasea.htm |
| 2023-01-10 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403623000005/exhibit991pressrelease11023.htm |
| 2022-11-03 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403622000165/croxq32022-pressrelease.htm |
| 2022-08-04 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403622000115/croxq22022-pressrelease.htm |
| 2022-05-05 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403622000050/croxq12022-pressrelease.htm |
| 2022-02-16 | 10-K | https://www.sec.gov/Archives/edgar/data/1334036/000133403622000011/crox-20211231.htm |
| 2022-02-16 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403622000007/crox123121earningsreleasea.htm |
| 2021-10-21 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403621000180/croxq32021-pressrelease.htm |
| 2021-07-22 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403621000122/croxq22021-pressrelease.htm |
| 2021-04-27 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403621000069/croxq12021-pressrelease.htm |
| 2021-02-23 | 10-K | https://www.sec.gov/Archives/edgar/data/1334036/000133403621000035/crox-20201231.htm |
| 2021-02-23 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403621000033/crox123120earningsreleasea.htm |
| 2020-10-27 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403620000110/croxq32020-pressrelease.htm |
| 2020-07-30 | 8-K EX-99 | https://www.sec.gov/Archives/edgar/data/1334036/000133403620000064/croxq22020-pressrelease.htm |
| 2010-02-25 | 10-K | https://www.sec.gov/Archives/edgar/data/1334036/000104746910001357/a2196634z10-k.htm |
