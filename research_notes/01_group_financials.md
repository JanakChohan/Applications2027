# Research Note 01 — JPMorganChase Group Financials
Research conducted: 2026-08-31 (all web access this date unless stated)

## Primary sources used
- FY2025 Form 10-K (filed 2026-02-13): https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/quarterly-earnings/2025/4th-quarter/corp-10k-2025.pdf — downloaded and text-extracted locally (410 pages)
- 4Q25 Earnings Press Release (2026-01-13): .../2025/4th-quarter/d868c7ef-1670-465d-ba75-c2b36ddbcc6b.pdf
- 4Q25 Earnings Release Financial Supplement: .../2025/4th-quarter/ff69a4a4-ab52-4a38-b82a-f153ba695e41.pdf
- 2Q26 Earnings Release narrative (SEC 8-K Ex-99.1): https://www.sec.gov/Archives/edgar/data/0000019617/000162828026048078/a2q26erfexhibit991narrative.htm

METHOD NOTE: JPM PDFs render as binary through WebFetch. I curl'd them and extracted text with pypdf locally. All figures below are transcribed from those extractions = PRIMARY, not recalled.

## Firmwide three-year summary (10-K p.46), $m
| Metric | 2025 | 2024 | 2023 |
|---|---|---|---|
| Total net revenue (reported) | 182,447 | 177,556 | 158,104 |
| Total noninterest expense | 95,640 | 91,797 | 87,172 |
| Pre-provision profit | 86,807 | 85,759 | 70,932 |
| Provision for credit losses | 14,212 | 10,678 | 9,320 |
| Net income | 57,048 | 58,471 | 49,552 |
| Diluted EPS ($) | 20.02 | 19.75 | 16.23 |
| ROE | 17% | 18% | 17% |
| ROTCE | 20% | 22% | 21% |
| ROA | 1.29 | 1.43 | 1.30 |
| Overhead ratio | 52% | 52% | 55% |
| Loans-to-deposits | 58% | 56% | 55% |
| CET1 (Standardized) | 14.6% | 15.7% | 15.0% |
| SLR | 5.8 | 6.1 | 6.1 |
| LCR (avg) | 111% | 113% | 113% |
| Market cap | 868,793 | 670,618 | 489,320 |
| Book value/share ($) | 126.99 | 116.07 | 104.45 |
| TBVPS ($) | 107.56 | 97.30 | 86.08 |
| Total assets | 4,424,900 | 4,002,814 | 3,875,393 |
| Deposits | 2,559,320 | 2,406,032 | 2,400,688 |
| Loans | 1,493,429 | 1,347,988 | 1,323,706 |
| Common stockholders' equity | 342,393 | 324,708 | 300,474 |
| Employees | 318,512 | 317,233 | 309,926 |
| Net charge-offs | 9,849 | 8,638 | 6,209 |
| NCO rate | 0.74% | 0.68% | 0.52% |
| Allowance for credit losses | 31,230 | 26,866 | 24,765 |

NOTE 2024 distortion: 2024 revenue included a $7.9bn net gain on Visa shares and expense included $1.0bn Visa-share donation. So 2025 net income falling 2% vs 2024 is NOT underlying deterioration.
NOTE 2025 distortion: provision includes $2.2bn reserve build for the Apple Card forward purchase commitment; also cut CET1 ~25bp (Standardized).

## FY2025 revenue composition (managed basis, supplement p.7)
- Net interest income – reported 95,443 / managed 95,868
- Noninterest revenue – reported 87,004 / managed 89,713
- Total net revenue – reported 182,447 / **managed 185,581**
=> FY2025 mix ≈ 51.7% NII / 48.3% fee & other. Roughly half-and-half. THIS IS THE KEY STRUCTURAL FACT.

FY2025 reported noninterest revenue lines ($m):
Investment banking fees 9,615 | Principal transactions 27,212 | Lending- & deposit-related fees 9,093 | Asset management fees 20,327 | Commissions & other fees 8,539 | Investment securities losses (57) | Mortgage fees 1,381 | Card income 4,720 | Other income 6,174

FY2025 expense lines ($m): Compensation 54,487 | Occupancy 5,461 | Technology, comms & equipment 11,029 | Professional & outside services 12,356 | Marketing 5,531 | Other 6,776. Total 95,640.
- Compensation = 57% of total expense. Firmwide legal expense only $361m FY25 (vs $740m FY24).
- CAUTION: "Technology, communications and equipment" $11.0bn is NOT the full tech budget — much tech spend sits in compensation (engineers) and professional/outside services. Firm's stated total tech spend is a separate disclosed number; see note 05.

## Net interest margin detail (supplement p.6, FY2025)
- Total interest-earning assets (avg) $3,834,359m; yield 5.05%
- Total interest-bearing liabilities (avg) $3,163,933m; rate 3.09%
- Interest rate spread 1.96%; **Net yield on interest-earning assets (NIM) 2.50%** (2024: 2.63%)
- NIM excluding Markets 3.75% (2024: 3.84%) — the "real" banking margin; Markets assets are low-margin/high-volume and dilute headline NIM.
- Avg loan yield 6.72%; avg interest-bearing deposit rate 2.37%; avg noninterest-bearing deposits $604,183m (free funding).

## FY2025 segment results (managed, $m) — supplement pp.12,16,20,23
| | CCB | CIB | AWM | Corporate | Firm |
|---|---|---|---|---|---|
| Net revenue | 76,029 | 78,454 | 24,073 | 7,025 | 185,581 |
| Noninterest expense | 40,267 | 38,216 | 15,332 | 1,825 | 95,640 |
| Provision | 11,493 | 2,615 | 97 | 7 | 14,212 |
| Net income | 18,245 | 27,761 | 6,522 | 4,520 | 57,048 |
| ROE | 32% | 18% | 40% | n/a | 17% |
| Overhead ratio | 53% | 49% | 64% | n/a | 52% |
| Allocated equity (avg) | 56,000 | 149,500 | 16,000 | ~111,254 (resid.) | 332,754 |
| Employees (YE25) | 144,196 | 94,563 | 29,722 | 50,031 | 318,512 |

Share of firm: revenue CCB 41.0% / CIB 42.3% / AWM 13.0% / Corp 3.8%.
Share of net income: CCB 32.0% / CIB 48.7% / AWM 11.4% / Corp 7.9%.
=> CIB earns a *larger* share of profit than revenue; CCB *smaller* (heavy credit provision + big cost base). AWM tiny capital, outsized return.

Capital intensity (revenue per $ of allocated equity, FY25): CCB 1.36x, CIB 0.52x, AWM 1.50x.
Profit per $ allocated equity: CCB 0.326, CIB 0.186, AWM 0.408.
Revenue per employee (FY25): CCB $527k, CIB $830k, AWM $810k. Net income per employee: CCB $127k, CIB $294k, AWM $219k. [INFERENCE — my calculation from disclosed figures, not a JPM disclosure]

## CCB detail FY2025 ($m)
Revenue by business: Banking & Wealth Management 42,862 | Home Lending 4,966 | Card Services & Auto 28,201
NII 58,234 (77% of CCB revenue) vs noninterest revenue 17,795 → CCB is overwhelmingly a SPREAD business.
Noninterest revenue lines: lending/deposit fees 3,669; asset mgmt fees 4,669; mortgage fees 1,326; card income 2,230; all other 5,901 (incl. operating lease income $3.8bn).
Provision 11,493 (incl. $2.2bn Apple Card build). Card Services NCO rate 3.14% (4Q25).
Deposits (period-end) $1,072,792m; loans $592,067m; equity $56,000m.
4Q25: revenue 19,396; NI 3,642; ROE 25% (depressed by Apple Card build).

## CIB detail FY2025 ($m)
Total net revenue 78,454; NI 27,761; ROE 18%; overhead 49%; comp/revenue 25%.
NII 24,688 vs noninterest revenue 53,766 → CIB is mostly FEE/TRADING, but NII is a fast-growing chunk (+13% YoY).
Revenue by business:
- Investment Banking 10,198 (of which IB fees 9,735)
- Payments 19,331
- Lending 7,601
- **Total Banking & Payments 37,136**
- Fixed Income Markets 22,532
- Equity Markets 13,250
- Securities Services 5,599
- Credit adjustments & other (63)
- **Total Markets & Securities Services 41,318**
Banking & Payments by client coverage segment: Global Corporate Banking & Global Investment Banking 25,285 | Commercial Banking 11,851 (of which Commercial & Specialized Industries 8,306; Commercial Real Estate Banking 3,545).
NOTE: "Middle Market Banking" was RENAMED "Commercial & Specialized Industries" in 2Q25.
Balance sheet: total assets $2,142,534m period-end; deposits $1,226,155m; equity $149,500m (up 13% YoY from $132bn — capital being pushed into CIB).
4Q25: IB fees down 5% YoY; **#1 global IB fees, 8.4% wallet share FY2025**. Markets +17% (FI +7%, Equities +40%).

## AWM detail FY2025 ($m)
Revenue 24,073 (Asset Management 11,700 / Global Private Bank 12,373); NI 6,522; ROE 40%; overhead 64%.
Pretax margin FY25: AM 35%, GPB 37%, AWM total 36%.
Asset management fees 15,494 of 17,241 noninterest revenue → dominant. NII only 6,832 (28%) — mostly GPB lending/deposits.
AUM $4.8tn (+18% YoY); client assets $7.1tn (+20%) at 31-Dec-2025.
Loans $266,385m; deposits $257,316m; equity only $16,000m.
Employees 29,722; Global Private Bank client advisors 4,101 (+9% YoY).

## Corporate FY2025 ($m)
Revenue 7,025 (Treasury & CIO 6,501; Other Corporate 524); NI 4,520.
NII 6,114 (down 38% YoY as rates fell). Investment securities portfolio avg $734,850m.
FY24 comparison heavily distorted by Visa ($7.9bn gain).
Employees 50,031 — note this is where centralised functions (tech, ops, finance, risk, HR) sit.

## Latest quarter: 2Q26 (source: SEC 8-K Ex 99.1, filed July 2026)
Firmwide: net revenue reported $57.3bn / managed $58.0bn; net income $21.2bn (incl. $4.6bn Visa share-exchange gain + $1.0bn equity investment gains); net income ex-significant items $16.9bn; EPS $7.70 (ex-items $6.14); ROE 24% / ROTCE 29% (ex-items 23%). CET1 Std 14.1% / Adv 14.2%. Total assets $5.0tn. Stockholders' equity $375bn. BVPS $133.01; TBVPS $113.35. Std RWA $2.1tn. TLAC $590bn.
NII $25.6bn managed; noninterest revenue $32.4bn.
- CCB: revenue $20.3bn (B&WM 11.2 / Home Lending 1.3 / Card & Auto 7.8); expense 11.1; provision 2.2; NI $5.3bn; ROE 34%. Card NCO 3.34%.
- CIB: revenue $24.9bn; expense 11.4; provision 0.356; NI $9.7bn; ROE 22%. Banking & Payments $11.2bn (IB fees $3.3bn +30%; Payments $5.3bn; Lending $2.0bn). Markets & Sec Svcs $13.7bn (FI $6.1bn +6%; Equities $6.0bn +86%; Sec Svcs $1.7bn +17%). **#1 global IB, 9.3% wallet share YTD.**
- AWM: revenue $6.9bn; expense 4.2; NI $2.0bn; ROE 48%. AUM $5.1tn (+18%); client assets $7.7tn (+19%). LT net inflows $50bn in quarter.
- Corporate: revenue $6.0bn; NI $4.2bn (Visa gain).
CAUTION: 2Q26 is a record, flattered by the Visa gain and an 86% jump in Equity Markets. Do not treat as run-rate.

## Total assets jumped $4.42tn (Dec-25) -> $5.0tn (Jun-26)
Driven by Markets balance-sheet growth (trading assets, repo/securities borrowed). [INFERENCE from 4Q25 trend: trading assets rose from $637.8bn to $802.9bn during 2025 and fed funds sold/repo from $295bn to $336bn.]

## Workforce (10-K p.9, as of 31-Dec-2025)
318,512 employees, 66 countries, 58% in US.
By region: North America 185,208 | Asia-Pacific 96,499 | **EMEA 31,030** | LatAm/Caribbean 5,775.
By LOB: CCB 144,196 | CIB 94,563 | AWM 29,722 | Corporate 50,031.
IMPORTANT: EMEA 31,030 is the ONLY regional figure in the 10-K. There is NO UK or London headcount in the 10-K. UK headcount must come from UK entity accounts / press. See note 03.

## UK subsidiaries named in 10-K Exhibit 21 (significant subsidiaries list)
- J.P. Morgan Capital Holdings Limited (UK) → J.P. Morgan Securities plc (UK)
- JPMorgan Asset Management International Limited (UK) → JPMorgan Asset Management (UK) Limited (UK)
- (also J.P. Morgan SE — Germany; JPMorgan Asset Management (Europe) S.à r.l. — Luxembourg)
NOTE: Exhibit 21 lists only *significant* subsidiaries, so absence of e.g. J.P. Morgan Europe Limited / Chase UK entity does not mean it doesn't exist.

## Country exposure
10-K line: "United Kingdom 987 / 1,254 / 1,254" (context: country exposure table, $m) — need to re-check units/context before using. FLAGGED as unverified.

## Open items
- Segment RWA (not allocated equity) by LOB — check 10-K Business Segment Results section
- Total technology spend figure — Investor Day
- League tables by product/region — Dealogic/LSEG via press
