# CROX — bear case, news flow and industry context (web research notes)

Compiled 2026-11-26. Stock reference: $159.93 close on 2026-11-25, 52-week range $75.13–$164.24.

**How to read this file**

- Every item carries a date, the numbers and a source URL.
- "SEC (local copy)" means the fact was read from the company filing already saved in `data/sec_txt/`; the URL given is the EDGAR original.
- "Snippet only" means the fact came from a search-result summary and the page itself was not opened (paywall, 403, or not fetched). Treat these as leads to verify before they go on a slide.
- "Not found" means I searched and did not find it. It does not mean it does not exist.
- Sites that refused automated access (403/Cloudflare): macrotrends.net, benzinga.com quote pages, marketbeat.com, securities.stanford.edu, courtlistener.com, qz.com, emarketer.com, chartmill.com, hedgeye.com, uk.fashionnetwork.com. No workaround was attempted.

---

## 1. Litigation

### 1a. Securities class action over HEYDUDE (the main one)

| Item | Detail | Source |
|---|---|---|
| Case | *Carretta v. Crocs, Inc., et al.*, No. 1:25-cv-00096 (C.A. No. 25-96-JLH-EGT), U.S. District Court, **District of Delaware**, Judge Jennifer L. Hall | SEC (local copy) Q3 2026 10-Q, Note 14: https://www.sec.gov/Archives/edgar/data/1334036/000133403626000060/crox-20260930.htm ; https://www.ktmc.com/new-cases/crocs-inc/ |
| Filed | 2025-01-22. Defendants: Crocs, CEO Andrew Rees, former CFO Anne Mehlman, then-CFO Susan Healy | Court memorandum order: https://www.ded.uscourts.gov/sites/ded/files/opinions/25-96.pdf |
| Class period | Original complaint: 2022-11-03 to 2024-10-28. **Amended complaint (filed 2025-12-15): 2022-08-04 to 2024-10-28** | Court order (original period); 10-Q Note 14 (amended period) |
| Claims | Sections 10(b) and 20(a) of the Exchange Act and Rule 10b-5; "allegedly false and misleading statements related to the Company's wholesaler inventory and its alleged impact on the Company's revenue". Unspecified damages | 10-Q Note 14 (URL above) |
| Allegations (plaintiff framing) | HEYDUDE's 2022 revenue (about 25% of group revenue) was driven by deliberately overstocking third-party wholesalers/retailers; defendants concealed that destocking plus waning demand would hit results | https://www.ktmc.com/new-cases/crocs-inc/ |
| Trigger event | 2024-10-29: Q3 2024 results, HEYDUDE revenue below expectations, "excess inventories in the market". Stock fell $26.47 (about 19.2%) from $138.05 to $111.58 | https://ksfcounsel.com/cases/nasdaqgs-crox-securities/ |
| Lead plaintiff | 2025-10-15: Teamsters Local 237 funds appointed lead plaintiff; three competing motions denied as moot. Related action *Shah v. Crocs* (C.A. 25-356) was voluntarily dismissed | https://www.ded.uscourts.gov/sites/ded/files/opinions/25-96.pdf |
| Motion to dismiss | 2026-02-27: defendants moved to dismiss the amended complaint. Kessler Topaz page still says "currently being briefed" | https://www.ktmc.com/new-cases/crocs-inc/ |
| **Status at 2026-11-26** | **No ruling found.** The Q3 2026 10-Q (filed 2026-10-29) describes the case as pending, states the company "is not in a position to assess the likelihood of any potential loss", and discloses no decision. One docket-aggregator snippet mentioned an "Oct 15, 2026 Order on Motion to Dismiss" but had no content and almost certainly confuses the 2025-10-15 lead-plaintiff order. Unverified; check PACER | 10-Q URL above |
| Accrual | $0.6 million accrued for all legal claims and disputes at 2026-09-30 (i.e. nothing material reserved for this case) | 10-Q Note 14 |

**No D. Colo. securities class action was found.** Colorado is where the derivative suits sit:

- *O'Connor v. Smach*, 1:25-cv-00576 (D. Colo.); *The Berger Trust v. Rees*, 1:25-cv-00597 (D. Colo.); *Sarabia v. Rees*, 2025CV30069 and *Lesanto v. Bickley*, 2025CV30071 (Dist. Ct., Broomfield County, Colo.). Four derivative actions alleging breach of fiduciary duty, unjust enrichment, insider trading, waste, etc., tied to the same wholesaler-inventory theory. Source: Q3 2026 10-Q Note 14 (URL above).

### 1b. IP / clog trademark fights

| Date | What happened | Source |
|---|---|---|
| 2024-10-03 | **Dawgs / Double Diamond false-advertising counterclaim revived.** Federal Circuit (No. 22-2160) reversed summary judgment for Crocs and held that calling Croslite "patented, proprietary, exclusive" can be actionable under Lanham Act §43(a)(1)(B). Crocs had conceded the "patented" claim was false | https://www.cafc.uscourts.gov/opinions-orders/22-2160.OPINION.10-3-2024_2395329.pdf ; https://ipwatchdog.com/2024/10/03/federal-circuit-says-lanham-act-applies-crocs-false-claims-croslite-patented/ |
| 2025-10-06 | **Supreme Court denied cert** (No. 25-75, *Crocs v. Double Diamond*). Federal Circuit ruling stands; case goes back to D. Colo. on the counterclaim. Remand outcome and damages exposure: not found | https://news.bloomberglaw.com/ip-law/high-court-spurns-case-over-crocs-false-use-of-word-patented ; https://natlawreview.com/article/patented-proprietary-or-problematic-supreme-court-declines-resolve-circuit-split |
| 2023-01 to 2026-01-08 | **ITC 3D-trademark case (Inv. 337-TA-1270) largely lost.** Marks: U.S. Reg. Nos. 5,149,328 and 5,273,875 (Classic Clog shape). ALJ (Jan 2023) and the Commission found no infringement or dilution by the active respondents (Orly Shoe, Hobby Lobby, Quanzhou ZhengDe/Amoji). On 2026-01-08 the Federal Circuit (No. 24-1300, precedential) dismissed Crocs' appeal of that finding as untimely and affirmed only a *limited* exclusion order against defaulting Chinese sellers, rejecting a general exclusion order | https://www.cafc.uscourts.gov/opinions-orders/24-1300.OPINION.1-8-2026_2629793.pdf ; https://www.thefashionlaw.com/crocs-itc-bid-to-block-lookalike-clogs-ends-in-mixed-result-on-appeal/ ; https://ipwatchdog.com/2026/01/08/crocs-delivered-blow-precedential-cafc-ruling-appeal-window-itc-decisions/ |
| 2026-04-27 / 2026-09-24 | Federal Circuit denied rehearing (2026-04-27). Crocs filed a cert petition on 2026-09-24 (No. 26-421, *Crocs v. ITC*); response was due 2026-10-28 and the Solicitor General asked for an extension on 2026-10-23. **Pending.** The petition is about appeal timing, not the trademark merits | https://www.supremecourt.gov/docket/docketfiles/html/public/26-421.html ; https://www.crowell.com/en/insights/client-alerts/when-the-clock-strikes-twice-crocs-takes-piecemeal-itc-appeals-to-the-supreme-court |
| 2021–2026 | **Crocs v. Joybees** (D. Colo., 1:21-cv-02859; trade secrets and trademark; Joybees is run by ex-Crocs staff). Jul 2025: Crocs agreed to drop trademark-dilution claims. Dec 2025: Joybees asked the court to find the clog designs lack the recognition needed for trademark protection. 2025-12-17: Joybees filed its own Lanham Act suit against Crocs (1:25-cv-04041); a 2026-05-08 hearing addressed Crocs' motion to stay. **No verdict or dispositive ruling found.** Snippet only for most of this | https://law360.com/articles/2371422 ; https://dockets.justia.com/docket/colorado/codce/1:2025cv04041/249949 ; https://www.law360.com/cases/617349d5437015a9e973c907/articles |
| Amicus argument worth quoting | Hobby Lobby and Orly told the Federal Circuit that Crocs' trademark claims were "a thinly veiled attempt to extend in perpetuity the monopoly it enjoyed through expired patents" | https://fedcircuitblog.com/wp-content/uploads/2025/10/CORRECTED-BRIEF-OF-AMICI-CURIAE-HOBBY-LOBBY-STORES-INC.-AND-ORLY-SHOE-CORP.-IN-SUPPORT-OF-APPELLEE-AND-AFFIRMANCE-.pdf |

Bear read: the legal moat around the clog silhouette is weak. Utility/design patents have expired (per the amicus brief; specific expiry dates not found), the 3D marks failed against active respondents at the ITC, and the "patented Croslite" claim is now a live false-advertising liability.

### 1c. Other

- Consumer class action over "shrinking" Crocs (heat/sun shrinkage): a judge found the putative class failed to allege fraud; earlier ruling tossed all but one claim. Dates not captured. Snippet only. https://www.mealeys.com/mealeys/articles/2431303 ; https://courthousenews.com/judge-tosses-all-but-one-claim-in-case-over-shrinking-crocs/
- **Customs/tariff disputes: not found** (beyond the IEEPA refund process in section 5). The 10-Q legal note refers generally to "government tax audits".

---

## 2. Short reports, Sell ratings, upgrades and downgrades

### 2a. Activist short sellers

**Not found.** No published short report on CROX from Spruce Point, Hindenburg, Kerrisdale, Jehoshaphat or similar turned up. The only named institutional short call found is **Hedgeye, which has had CROX as a "Best Idea Short"** ("CROX | We'll Take It | Best Idea Short"); the page is paywalled/403 so date and thesis could not be read. https://app.hedgeye.com/insights/136987-crox-we-ll-take-it-best-idea-short

Short interest (Nasdaq data in local file `data/market/short_CROX.json`): 3,490,583 shares at 2026-11-13 settlement (2.8 days to cover), down from 6,057,886 at 2026-01-30. Shorts have been covering into the rally.

### 2b. Goldman Sachs Sell (Brooke Roach)

| Date | Action | Source |
|---|---|---|
| 2025-07-02 | Initiated at **Sell, PT $88** (about 18% downside) as part of a cautious mid-cap athleisure launch (Deckers also Sell, PT $90). Reasons reported: likes Crocs' marketing and product pipeline, but sees "normalizing demand" for the classic clog that "could temper and limit the pace of international expansion"; "limited upside due to the increasing competition and changing market dynamics"; HEYDUDE "growing pains" limiting sales and margins | https://ng.investing.com/news/stock-market-news/goldman-cautious-on-mid-cap-athleisure-starts-crocs-deckers-at-sell-1992071 ; https://stocktwits.com/news-articles/markets/equity/goldman-sachs-advises-sell-for-decker-crocs-stocks-retail-sentiment-divided/chFjKbpRcLx |
| 2025-07-22 | Sell maintained, PT $88 → $87 (lowest on the Street at the time; average was $123.74) | https://www.gurufocus.com/news/2994839/goldman-sachs-maintains-sell-rating-on-crox-adjusts-price-target-crox-stock-news |
| 2026-10-30 | **Sell maintained, PT $95 → $128** (about 20% below the current price) | https://stockanalysis.com/stocks/crox/ratings/ |

Goldman's full written thesis is behind the research paywall. Not found in more detail than above.

### 2c. Rating changes 2025–2026

| Date | Broker (analyst) | Action | PT | Stated reason | Source |
|---|---|---|---|---|---|
| 2025-01 | Williams Trading (Sam Poser) | Buy → Hold | $127 → $112 | Weakening trends in core brand and HEYDUDE (snippet only) | https://investing.com/news/stock-market-news/crocs-cut-to-hold-by-williams-trading-on-weakening-trends-3819229 |
| 2025-07-02 | Goldman Sachs (Brooke Roach) | Initiate Sell | $88 | See 2b | see 2b |
| 2025-08-08 | Stifel | Buy → Hold | $127 → $85 | Limited visibility on sales growth; muted revenue recovery through 2026; U.S. trends plus promotion pullback | https://www.tipranks.com/news/the-fly/crocs-downgraded-to-hold-from-buy-at-stifel-thefly |
| 2025-08 (post Q2) | Barclays | Overweight → Equal Weight | $81 | Snippet only, date not confirmed | https://www.tipranks.com/news/the-fly/crocs-downgraded-to-equal-weight-from-overweight-at-barclays-thefly |
| 2025-09-22 | Piper Sandler | Overweight → Neutral | $95 → $75 | U.S. demand headwinds "could be more prolonged than investors anticipate"; Crocs pulling back on discounting, HEYDUDE cutting performance marketing; shares "range-bound until the company's sales stabilize" | https://www.tipranks.com/news/the-fly/piper-downgrades-crocs-to-neutral-on-demand-headwinds-thefly |
| 2025-10-31 | Citigroup | Reported cut to a "negative" rating after Q3 2025 | not found | Reported by StockStory only; could not confirm rating label, analyst or PT | https://finviz.com/news/213617/why-crocs-crox-shares-are-trading-lower-today |
| 2026-01-30 | KeyBanc (Ashley Owens) | Overweight → Sector Weight | n/a | Planned promotion cuts, tighter N.A. wholesale receipts, choosy U.S. consumer, more competition under $100, few near-term catalysts | https://sgbonline.com/exec-keybanc-downgrades-crocs-lowers-price-targets-on-nike-and-on/ |
| 2026-02-18 | Williams Trading | Reported downgrade to Sell, PT $84 | $84 | **Unverified.** Appeared only in an investing.com consensus-table snippet; a targeted search could not confirm it | https://uk.investing.com/equities/crocs-consensus-estimates |
| 2026-04-14 | Seaport Global | Neutral → Buy | $135 | Reason not found | https://www.nasdaq.com/articles/seaport-global-upgrades-crocs-crox |
| ~2026-06-08 | Baird (Jonathan Komp) | Neutral → Outperform | $115 → $150 | HEYDUDE moving past inventory/marketplace reset; EPS est. $13.55 (2026), $14.90 (2027) | https://www.tikr.com/blog/baird-upgrades-crocs-nasdaq-crox-tock-and-sets-150-price-target-predicting-sustainable-growth |
| 2026-06-15 | Stifel | Hold maintained | $105 → $125 | Snippet only | https://www.benzinga.com/quote/CROX/analyst-ratings |
| 2026-06-26 | Piper Sandler | Neutral → Overweight | $95 → $150 | N.A. DTC back to mid-single-digit growth in Q1 2026 (best since Q2 2024); wholesale stabilising; valuation; TikTok Shop about 3% of Crocs brand revenue in 2026 vs 2% in 2025 | https://www.tikr.com/blog/piper-sandler-upgrades-crocs-nasdaq-stock-to-overweight-sees-65-upside |
| 2026-10-15 | Barclays (Adrienne Yih) | Equal Weight → Overweight | $118 → $139 (one source says $113 → $133) | Better visibility on recovery in Crocs N.A., international and HEYDUDE. Stock +6–7% on the day | https://finviz.com/news/403196/crocs-stock-steps-up-after-barclays-upgrade ; https://www.financialcontent.com/article/stockstory-2026-10-15-why-crocs-crox-stock-is-up-today |
| 2026-10-30 | Post-Q3 PT moves | Goldman Sell $95→$128; Piper Buy $150→$170; Stifel Hold $125→$148; UBS (Jay Sole) Hold $120→$145; Baird Buy $163→$173; Barclays Buy $139→$178; BTIG and KeyBanc Hold (no PT) | — | — | https://stockanalysis.com/stocks/crox/ratings/ |

Consensus snapshot (Nasdaq, local `data/market/target_CROX.json`, fetched 2026-11-26): 5 Buy / 5 Hold / 1 Sell; mean PT $160.75, low $128, high $184. Yahoo 1-year target estimate: $164.67. **The stock ($159.93) is already at the consensus target.**

Pattern worth noting for the pitch: the Street downgraded near the lows (Aug 2025–Jan 2026, stock $75–$85) and upgraded after the stock had already rallied (Apr–Oct 2026).

---

## 3. Activists and notable holders

- **Activist involvement / 13D filings 2024–2026: not found.** No 13D, proxy contest, or strategic-review announcement turned up. Commentary that "the market values HEYDUDE at zero" exists but is opinion, not a campaign.
- **5%+ holders at 2026-03-31** (DEF 14A, SEC local copy; 50,444,107 shares outstanding): BlackRock 5,566,035 (11.0%); Vanguard 5,496,183 (10.9%); FMR 4,233,829 (8.4%); **WIT Partners Advisory Pte. Ltd. 2,852,280 (5.7%)**. That last block is exactly the 2,852,280 shares issued to the HEYDUDE seller in 2022, i.e. the HEYDUDE founder's vehicle still holds its full consideration stake. CEO Andrew Rees: 1,016,929 (2.0%). https://www.sec.gov/Archives/edgar/data/1334036/000133403626000020/crox-20260423.htm
- **Himalaya Capital (Li Lu):** new position in Q4 2025, 628,159 shares (about $53.7M, about 1.5% of its 13F book; 13F filed 2026-02-17). Third-party trackers show it raised to 887,093 shares (+41%) in Q1 2026. Not verified against EDGAR. https://www.aol.com/articles/crocs-stock-draws-54-million-144157095.html ; https://valuesider.com/guru/li-lu-himalaya-capital-management/history/CROX
- **No Street GP** exited in Q3 2025: sold all 495,000 shares (about $50.1M). https://www.fool.com/coverage/filings/2025/11/15/fund-exits-usd50-million-crocs-stake-as-guidance-weakens-and-operating-trends-cool
- Largest 13F holders at 2026-09-30 (Nasdaq, local `data/market/inst_CROX.json`): BlackRock 4.52M; FMR 3.34M; American Century 2.07M (+41% QoQ); LSV 1.83M; Franklin Templeton 1.36M (+31%); Fuller & Thaler 1.26M; Citadel 1.17M; D. E. Shaw 1.12M (+29%); UBS 1.10M (+71%).
- Insider selling: Yahoo shows 3 recent insider transactions totalling $3.10M, including a $2.30M sale by director Ronald Frasch (date not shown). https://finance.yahoo.com/quote/CROX/holders/

---

## 4. Management changes 2024–2026

All from SEC filings (local copies) unless noted.

| Date | Event | Source |
|---|---|---|
| 2024-04-16 | **Rick Blackshaw (HEYDUDE president) left "effective immediately".** Terence Reilly (ex-Stanley president, former Crocs CMO) named EVP and President, HEYDUDE; joined 2024-04-29 | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000076/exhibit991pressrelease41624.htm |
| 2024-05-07 | **Susan Healy named CFO effective 2024-06-03**, succeeding Anne Mehlman, who became Brand President, Crocs | https://www.sec.gov/Archives/edgar/data/1334036/000133403624000092/exhibit991pressrelease5724.htm |
| 2025-03-03 (8-K item 5.02, filed 03-07) | **Adam Michaels, EVP Chief Digital Officer, resigned** effective 2025-05-01. $320,000 lump sum for 24-month non-compete; no severance | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000026/crox-20250303.htm |
| 2025-05-16 (8-K item 5.02, filed 05-21) | **Terence Reilly moved from HEYDUDE Brand President to EVP Chief Brand Officer** (marketing for both brands). **CEO Rees became interim HEYDUDE president.** So HEYDUDE had three leaders in about 13 months | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000060/crox-20250516.htm |
| 2025-08-28 (8-K item 5.02, filed 08-29) | **CFO Susan Healy resigned "effective immediately" on 2025-08-28**, three weeks after the Q2 2025 guide-down and about 15 months into the job. **Patraic Reagan** (ex-SharkNinja CFO, 14 years at Nike) named CFO effective 2025-09-22: salary $750,000, $800,000 sign-on bonus, $3.5M RSU grant. Q3 guidance reaffirmed the same day | https://www.sec.gov/Archives/edgar/data/1334036/000133403625000094/crox-20250828.htm ; https://www.sec.gov/Archives/edgar/data/1334036/000133403625000094/exhibit991pressrelease82925.htm |
| 2025-11-17 | **Rupert Campbell** (ex-President adidas North America, Nov 2021–Dec 2023) appointed EVP, Brand President HEYDUDE. No 8-K was filed for this | DEF 14A: https://www.sec.gov/Archives/edgar/data/1334036/000133403626000020/crox-20260423.htm |
| 2026-06-09 (8-K item 5.02, filed 06-10) | **Not a departure.** Item 5.02 reports stockholder approval of the 2026 Equity Incentive Plan at the annual meeting. Note the plan passed with 27.4M for vs 7.8M against (about 22% opposition), and chairman Thomas Smach had 3.7M votes withheld | https://www.sec.gov/Archives/edgar/data/1334036/000133403626000046/crox-20260609.htm |
| CEO | **Andrew Rees**, age 59: joined as President June 2014, CEO since June 2017 (about 9.5 years), director since June 2017, Class I director (term to 2027 annual meeting). Contract term/expiry: not found | DEF 14A (URL above) |

Bear read: three CFOs in about 16 months (Mehlman to June 2024, Healy June 2024–Aug 2025, Reagan from Sept 2025); Healy left abruptly three weeks after the Q2 2025 guide-down; the chief digital officer left; HEYDUDE is on its fourth leader since acquisition (Blackshaw, Reilly, Rees as interim, Campbell).

---

## 5. Tariffs

### 5a. Crocs' stated exposure

| Date | Statement | Source |
|---|---|---|
| 2025-05-08 (Q1 2025 call) | 2025 guidance withdrawn. Scenario: if 145% China tariff plus 10% elsewhere persisted, about **$130M annualized** cash cost | https://ng.investing.com/news/stock-market-news/crocs-pulls-guidance-amid-tariff-uncertainty-q1-earnings-beat-1907969 (snippet only for the $130M) |
| 2025-08-07 (Q2 2025 call) | Incremental tariff cost about **$40M in H2 2025**, about **$90M annualized** on then-current sourcing mix. Q3 2025 adjusted operating margin guide of 18–19% included about 170 bps of tariff drag | Press release (SEC local copy): https://www.sec.gov/Archives/edgar/data/1334036/000133403625000083/croxq22025-pressrelease.htm ; $40M/$90M via https://finviz.com/news/136353/crox-q2-deep-dive-margin-pressures-and-cautious-guidance-amid-us-consumer-pullback (snippet only) |
| 2025-10-30 (Q3 2025) | Tariffs cut gross margin by about 230 bps in Q3 2025 (snippet only) | https://sgbonline.com/crocs-q3-earnings-decline-27-percent-tops-guidance/ |
| 2026-02-12 (Q4 2025 call) | FY2025 adjusted gross margin 58.3% with about 130 bps tariff drag; Q4 2025 gross margin down 320 bps, about 300 bps from tariffs. 2026 guide embeds an incremental about 80 bps tariff headwind; unmitigated annualized hit trimmed to about **$80M** (from $90M). **$100M of 2026 cost savings** "identified and actioned" | Press release (SEC local copy): https://www.sec.gov/Archives/edgar/data/1334036/000133403626000004/croxq42025-pressrelease.htm ; bps and $80M via https://www.zacks.com/stock/news/2880318/crocs-margins-under-pressure-temporary-dip-or-structural-shift and https://www.fool.com/earnings/call-transcripts/2026/02/12/crocs-crox-q4-2025-earnings-call-transcript/ (snippet only) |
| 2026-07-30 (Q2 2026) | Tariff costs contributed to a 170 bps decline in adjusted gross margin to 60%. Guidance explicitly excluded IEEPA refunds | https://www.proactiveinvestors.com/companies/news/1096311/crocs-shares-slide-as-weak-outlook-draws-focus-from-earnings-beat-1096311.html |
| 2026-10-29 (Q3 2026 10-Q) | **Received about $67M of IEEPA refunds incl. interest in Q3 2026: $64M credited to cost of sales, $3M to interest income.** Total eligible refunds estimated at **$75–80M**. "These refunds are non-recurring. The tariffs that remain in effect continue to increase our product costs." Remaining tariffs "ranging from 10% to 12.5%" on Vietnam, China, Indonesia, India, Cambodia | SEC (local copy): https://www.sec.gov/Archives/edgar/data/1334036/000133403626000060/crox-20260930.htm |

**Quality-of-earnings point:** Q3 2026 GAAP gross margin was 66.2% vs adjusted 60.3%; GAAP EPS $4.52 vs adjusted $3.69. The company excluded the refund from adjusted EPS, and FY2026 guidance now shows a "non-GAAP net *benefit* of $40 million primarily associated with tariff refunds and our cost reduction initiatives". Adjusted numbers are clean; GAAP numbers and any screen using trailing GAAP P/E are flattered. Sources: Q3 2026 press release https://www.sec.gov/Archives/edgar/data/1334036/000133403626000058/croxq32026-pressrelease.htm ; https://finviz.com/news/411760/crocs-beats-and-raises-again-as-heydude-turns-positive-but-buybacks-and-a-shrinking-north-america-temper-the-story

### 5b. Sourcing mix (FY2025 10-K, SEC local copy)

- Crocs brand: about **45% of production in Vietnam** in 2025 (51% in 2024, 56% in 2023); also China, Indonesia, India, Mexico. Largest manufacturer (mostly Vietnam) made about 45% of Crocs brand production; second largest (Vietnam and China) about 28%. Two vendors = about 73%.
- HEYDUDE: about **44% Vietnam in 2025** (20% in 2024, 5% in 2023); "prior to 2025, the majority of our HEYDUDE Brand production was in China". Also Cambodia, Indonesia, India.
- Source: https://www.sec.gov/Archives/edgar/data/1334036/000133403626000006/crox-20251231.htm

### 5c. Legal and policy timeline

| Date | Event | Source |
|---|---|---|
| 2026-02-20 | **Supreme Court (6–3) held IEEPA does not authorize tariffs.** Did not address refunds; remanded to the Court of International Trade | https://ropesgray.com/en/insights/alerts/2026/02/supreme-court-strikes-down-ieepa-tariffs-key-takeaways-and-implications-for-importers ; https://www.dlapiper.com/en/insights/publications/2026/02/us-supreme-court-holds-ieepa-does-not-authorize-tariffs |
| 2026-02-20 / 02-24 | President imposed a **10% global tariff under Section 122** (Trade Act of 1974), effective 2026-02-24, 150-day statutory limit | https://www.cozen.com/news-resources/publications/2026/supreme-court-rules-president-lacks-ieepa-tariff-authority-president-imposes-section-122-tariffs |
| 2026-03-04 | CIT (Judge Eaton) ordered CBP to process unliquidated entries without IEEPA duties and reliquidate non-final entries | https://www.bakertilly.com/insights/ieepa-refunds |
| 2026-04-20 | CBP launched Phase 1 of the **CAPE** refund tool (about 63% of IEEPA-paid entries); about 45-day review-to-refund cycle. Finally liquidated entries deferred to later phases, no timeline | https://www.hklaw.com/en/insights/publications/2026/04/cape-has-arrived-navigating-the-next-phase-of-ieepa-duty-refunds ; https://www.troutman.com/insights/cbps-cape-crusade-a-new-45-day-path-to-ieepa-duty-refunds.html |
| 2026-05-07 | CIT ruled Section 122 tariffs unlawful, but relief limited to the three named plaintiffs; on appeal | https://www.americanbar.org/groups/public_contract_law/resources/procurement-lawyer/2026-fall/ieepa-tariffs-struck-down-replacement-tariffs-expired/ |
| 2026-07-24 | **Section 122 surcharge expired** (Congress did not extend). Same moment, USTR imposed **"forced labor" Section 301 tariffs on about 60 economies: 10% (countries with a forced-labor import ban) or 12.5% (those without, including China and Vietnam)**, stacking on MFN duties. No statutory cap or expiry. Already being challenged at the CIT | https://www.ustr.gov/about/policy-offices/press-office/fact-sheets/2026/july/fact-sheet-ustr-section-301-action-response-failure-60-economies-ban-imports-produced-forced-labor ; https://www.hklaw.com/en/insights/publications/2026/07/and-the-tariff-beat-goes-on ; https://www.wiley.law/alert-New-Forced-Labor-Tariffs-Imposed-on-60-US-Trading-Partners |
| 2026-07-22 | Vietnam announced a forced-labor import prohibition, apparently too late for the 07-23 action; could later move Vietnam to the 10% tier. Unconfirmed | https://www.kelleydrye.com/viewpoints/blogs/trade-and-manufacturing-monitor/ustr-announces-final-tariff-rates-exclusions-and-tariff-rate-quotas |
| 2026-07-31 | CBP: CAPE declarations covering 25.1M entries accepted. Total dollars refunded industry-wide: not found | https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/august-12th/ieepa-duty-refund-processing-update |

What footwear importers face now: normal MFN footwear duties (FDRA says footwear tariffs average more than 12% vs just over 2% for consumer goods overall) plus 10–12.5% Section 301 on essentially every sourcing country, plus pre-existing China Section 301. Net: the incremental tariff layer is now 10–12.5% per the company's own 10-Q, lower than the 2025 IEEPA rates (the 2025 country rates were not re-sourced here), which helps 2027 comparisons, but it is not zero and now sits on a legal basis with no sunset. **Section 232 action specific to footwear: not found.**

---

## 6. The key debate: is the clog a fad / has Crocs peaked in North America?

### 6a. Piper Sandler "Taking Stock With Teens" — favourite footwear brand, all teens

| Survey | Crocs rank (share) | HEYDUDE rank (share) | Notes | Source |
|---|---|---|---|---|
| Spring 2023 | No. 6 (2%) | No. 8 (1%) | Both gained about 25 bps YoY | https://pipersandler.com/sites/default/files/document/TSWTSpring2023.pdf |
| Fall 2023 | No. 6 | No. 7 | Crocs +30 bps YoY, HEYDUDE +50 bps YoY. Nike at 61% | https://mms.businesswire.com/media/20231010273091/en/1910930/1/TSWT_Fall23_Infographic.pdf |
| Spring 2024 | No. 7 | No. 8 | Crocs was No. 3 "on the way out" trend among male teens. Piper: weakness among upper-income teens "could signal that we are close to the top of the Crocs trend cycle". Stock fell more than 3% (2024-04-09) | https://uk.investing.com/news/stock-market-news/crocs-stock-drops-as-piper-sandlers-survey-shows-brand-is-losing-favor-with-teens-432SI-3425233 |
| Fall 2024 | No. 8 (2%) | No. 10 (1%) | UGG No. 5, On No. 7 | https://sgbonline.com/exec-piper-sandlers-fall-survey-finds-continued-shifts-in-brands-winning-with-teens |
| Spring 2025 | No. 9 (inferred: Fall 2025 article says rank "maintained ... compared to Spring") | not found | UGG biggest gainer | https://sgbonline.com/piper-sandler-survey-reveals-nike-lululemon-and-stanley-losing-teen-mindshare/ ; https://sgbonline.com/exec-athletic-brands-still-scoring-with-teens/ |
| Fall 2025 | No. 9 | not in article (not found) | Birkenstock share doubled to 4%; Crocs "continues to erode" with upper-income males | https://sgbonline.com/exec-athletic-brands-still-scoring-with-teens/ |
| Spring 2026 | **No survey.** Piper moved to one survey a year | — | Announced 2026-04-22 | https://sgbonline.com/piper-sandlers-taking-stock-with-teens-becomes-an-annual-event/ |
| **Fall 2026** (26th annual; 8,934 teens; published about 2026-10-15) | **No. 10 (1%)** | **Off the top 10** (fell off the list among boys) | All teens: Nike 45%, Adidas 10%, New Balance 7%, **Birkenstock 5% (No. 4, up from No. 6)**, UGG 4%, Converse 4%, On 3%, Asics 2%, Vans 1%, Crocs 1%. Crocs **dropped off the girls' top 10**; boys' share fell from 2% to 1% (still No. 8). Teen footwear spend −1% YoY | https://sgbonline.com/exec-piper-sandler-annual-teen-survey-sees-athletic-brands-losing-appeal/ ; https://sgbonline.com/exec-who-were-the-big-brand-winners-and-losers-in-piper-sandlers-teen-survey/ |

**Trajectory: Crocs No. 6 → 6 → 7 → 8 → 9 → 9 → 10 over three and a half years; HEYDUDE No. 7 at peak to unranked.** Birkenstock and UGG have taken the casual-comfort slots. Counterpoint for the bulls: the Fall 2026 survey also shows teens rotating *away* from athletic brands toward non-athletic styles, which is the reverse of the 2025 "athletic is back" headwind.

### 6b. Evidence the North America franchise has peaked

- Crocs brand North America revenue fell **6.8% in FY2025** (snippet only: https://uk.fashionnetwork.com/news/Crocs-2025-revenue-dips-1-5-,1807309.html). Q2 2025: −6.5% to $457M, which Rees attributed mainly to pulling back DTC discounting "most notably on clog" (https://sgbonline.com/crocs-inc-to-sacrifice-sales-in-short-term-to-focus-on-expenses-and-inventories/, snippet only).
- 2026-02-12 call: Crocs brand N.A. "will not be returning to growth here in 2026" (snippet only: https://www.fool.com/earnings/call-transcripts/2026/02/12/crocs-crox-q4-2025-earnings-call-transcript/).
- Q1 2026: Crocs brand N.A. −6.1% to $345.9M; N.A. wholesale −18.9%, DTC +5% (https://sgbonline.com/crocs-raises-fy-outlook-as-q1-far-exceeds-expectations/, snippet only).
- **Q3 2026: Crocs brand N.A. still −2.1%, N.A. wholesale −4.9%**, in the quarter the stock rose 25%. International +11.8% (international DTC +24.1%) is doing the work. A shift to a marketplace model in N.A. DTC cost about 270 bps of N.A. DTC growth and management expects a **700–800 bps headwind until it laps in Q3 2027**, which will obscure the true N.A. trend for a year. Earnings Whispers: "Bears have legitimate ammunition in the fact that the brand's largest market is still shrinking"; roughly half of headline EPS growth came from buybacks (diluted shares about 48.0M vs 54.0M). https://finviz.com/news/411760/crocs-beats-and-raises-again-as-heydude-turns-positive-but-buybacks-and-a-shrinking-north-america-temper-the-story ; https://www.tradingkey.com/news/transcripts/262253894-tradingkey
- Clogs are about three-quarters of Crocs brand mix (snippet only: https://finance.yahoo.com/markets/stocks/articles/crocs-shoes-making-surprising-comeback-161700199.html).
- 2025-08-07: Rees said the shift toward athletic footwear was cyclical but "will persist for a while" given the 2026 World Cup and 2028 L.A. Olympics, and that some consumers were "super cautious". Stock −29%. https://www.arise.tv/crocs-shares-plunge-30-amid-falling-us-sales-economic-pressures-consumer-shift-to-athletic-footwear ; https://news.bloomberglaw.com/international-trade/crocs-sinks-after-third-quarter-forecast-for-sharp-sales-decline
- "With Crocs shares down 30 percent, is the ugly shoe trend over?" (FashionUnited, about 2025-08-08): calls the drop "a market verdict on aesthetic overexposure". https://fashionunited.com/news/fashion/with-crocs-shares-down-30-percent-is-the-ugly-shoe-trend-over/2025080867623
- KeyBanc (2026-01-30): "intensified competition in the sub-$100 category". Goldman (2025-07-02): "normalizing demand" for the classic clog.
- Search interest: a third-party tracker shows a Crocs search index of 65.3 in Aug 2026 (2024 = 100), down 26.1% YoY. Low-authority source, not a raw Google Trends export. https://closo.co/tools/closo/research/brands/crocs
- Fashion cycle: ballet flats were the double-digit growth style in H1 2026; Crocs and Birkenstock are both launching flats (MarketWatch, 2026-08-15). https://www.morningstar.com/news/marketwatch/20260815126/ballet-flats-are-so-popular-that-even-brands-like-birkenstock-and-crocs-are-cashing-in-on-the-trend

### 6c. Evidence against the fad thesis

- **Circana H1 2026:** U.S. footwear dollars +1% (price-led, units down); fashion footwear flat; **clogs listed among styles that grew** (no % given), alongside mules and pumps; ballerinas double-digit; running +13%. Circana expects 2026 flat. https://www.circana.com/post/performance-shoe-sales-pick-up-the-pace-amid-selective-us-consumer-spending-in-the-footwear-market ; https://www.worldfootwear.com/news/us-footwear-sales-rise-slightly-in-the-first-half/11731.html
- Crocs brand revenue passed $1B in a quarter for the first time in Q2 2026; DTC +12%. https://fashionunited.com/news/business/crocs-brand-surpasses-one-billion-dollars-in-quarterly-revenue/2026073073825
- Q3 2026 Crocs brand record Q3 (+4.4% to $873M); HEYDUDE +6.1% to $170M (wholesale +14%) after −18%, −13%, −6% in the prior three quarters. https://www.fool.com/investing/2026/10/29/why-crocs-stock-skyrocketed-today/
- Discounting was pulled back deliberately: adjusted gross margin 60.3% in Q3 2026 (+180 bps); HEYDUDE adjusted gross margin 45.8% (+350 bps).
- Diversification away from the Classic Clog: sandals, Echo 2.0, Crafted, recovery clog, first ballet flats (LoveShackFancy collab, March 2026).
- Piper (2026-06-26): N.A. DTC back to mid-single-digit growth.

### 6d. Competition

- **Birkenstock** (Boston clog): No. 4 teen footwear brand in Fall 2026 with 5% share, five times Crocs' 1%. Positioned at $150+.
- **UGG** (Tasman and slippers): 4% all-teen share; No. 3 among girls at 10%.
- **Skechers Foamies, On, Hoka recovery slides:** named as competitors in general coverage; no share data found.
- **Dupes on Amazon/Temu/Shein:** "dozens of generic foam clog manufacturers on Amazon" (low-authority source); Chinese-language coverage attributes eroded pricing power to knock-offs (https://longbridge.com/en/news/252461752). Hard data on dupe share: **not found**. The ITC loss (section 1b) is the concrete evidence that Crocs cannot block lookalikes from active importers such as Hobby Lobby.
- An unverified single-source estimate puts Crocs at 70–80% of the global clog category. Do not use without corroboration.
- Global clogs market size per Fortune Business Insights: $10.65B in 2025. https://www.fortunebusinessinsights.com/clogs-market-116920

### 6e. Retailer commentary 2025–2026

**Largely not found.** Searches for Crocs/HEYDUDE mentions on Foot Locker, DSW/Designer Brands, Famous Footwear/Caleres, Academy, Dick's, Shoe Carnival and Genesco/Journeys calls returned nothing brand-specific. What was found:

- Shoe Carnival fiscal Q1 2026 (May 2026): revenue $277.7M, −7.5% YoY; adult athletic, men's and women's non-athletic and kids all down low single digits; closing 12–14 stores in FY2026. General softness at a family-channel retailer that carries both brands. https://www.nasdaq.com/articles/shoe-carnival-q1-earnings-call-highlights
- Genesco/Journeys: Journeys sales +7% in fiscal 2026 and +5% in Q1 fiscal 2027, driven by athletic (Hoka added, Saucony back). HEYDUDE is still listed among Journeys' larger assortments. No Crocs commentary. https://sgbonline.com/exec-journeys-gets-q1-boost-from-athletics-momentum-sauconys-return-and-hokas-arrival/
- Resale data (StockX etc.): **not found.**

---

## 7. HEYDUDE acquisition facts

| Item | Fact | Source |
|---|---|---|
| Agreement / announcement | SPA signed **2021-12-22**; announced **2021-12-23** | 10-K FY2021 (SEC local copy): https://www.sec.gov/Archives/edgar/data/1334036/000133403622000011/crox-20211231.htm ; press release https://www.sec.gov/Archives/edgar/data/1334036/000133403621000204/exhibit991pressrelease1223.htm |
| Headline price | **$2.5B = $2.05B cash + $450M in Crocs shares** issued to founder Alessandro Rosano (20-day VWAP before signing); 2,852,280 shares | https://investors.crocs.com/news-and-events/press-releases/press-release-details/2021/Crocs-Inc.-to-Acquire-Casual-Footwear-Brand-HEYDUDE/default.aspx |
| Closing | **2022-02-17**. Aggregate purchase price at closing recorded as **$2.3B** (the stock leg was worth less by closing) | 10-K FY2022 Note 3 (SEC local copy): https://www.sec.gov/Archives/edgar/data/1334036/000133403623000015/crox-20221231.htm ; https://www.sec.gov/Archives/edgar/data/1334036/000133403622000014/exhibit991pressrelease21722.htm |
| Financing | **$2.0B Term Loan B** (matures 2029-02-17) plus revolver draw; revolver upsized by $100M to $600M at closing | Closing press release (URL above); 10-K FY2025 |
| Revenue at deal | HEYDUDE expected about **$570M** revenue in 2021 (snippet only) | https://www.rte.ie/news/business/2021/1223/1268422-crocs-shoe-deal |
| Revenue since | 2022 (partial, from 02-17): **$895.9M**. 2023: **$949.4M** (+6.0%). 2024: −13.2% (about $824M). 2025: −13.3% (about $715M, derived). 2026 guide: about flat. Q3 2026: $170M (+6.1%). So HEYDUDE today is about 25% below its 2023 peak | 10-K FY2023: https://www.sec.gov/Archives/edgar/data/1334036/000133403624000025/crox-20231231.htm ; 10-K FY2024 and FY2025 (URLs above); Q3 2026 press release |
| Q2 2025 impairment | **$737M non-cash: $430M HEYDUDE trademark + $307M goodwill.** Assumptions at the time: revenue growth averaging about 8%, EBITDA margin about 20%, 15.0% discount rate. Goodwill fell from $710M to $403M. Cited causes: longer path to stabilisation, weak U.S. consumer, "disproportionate impact of tariffs on HEYDUDE Brand products" | 10-Q Q2 2025 (SEC local copy): https://www.sec.gov/Archives/edgar/data/1334036/000133403625000085/crox-20250630.htm |
| Debt paid down | Term Loan B down from $2.0B to **$500M** at 2026-09-30 | Q3 2026 10-Q |
| Did it destroy value? | Commentary: the write-down is "the accountants formally admitting the price paid was too high" (https://eightx.co/blog/us-teardown-crocs); Schwab Network segment titled "HEYDUDE deal disappointment" (https://schwabnetwork.com/video/ca-htag-crocs-crox-heydude-deal-disappointment-generational-fashion-shift); Seeking Alpha "Crocs: HEYDUDE Struggles Continue" (https://seekingalpha.com/article/4855178-crocs-heydude-struggles-continue). It is also the subject of the securities class action (section 1a). A rigorous independent post-mortem: not found | as linked |

Simple arithmetic for the pitch: paid about $2.3–2.5B for a brand that now does about $715M of revenue at a mid-40s gross margin, and has written off $737M (about 30–32% of the price).

---

## 8. Macro, consumer and TAM

- **Circana:** U.S. footwear Q1 2026 up modestly on price; H1 2026 dollars +1%, units down; 2026 expected "relatively flat". Performance +6%, running +13%, fashion flat. https://www.circana.com/post/us-footwear-industry-delivers-modest-first-quarter-growth-driven-by-price-increases-and-strength-in ; https://www.shoeintelligence.com/market-statistics-and-analysis/us-footwear-sales-up-1-in-h1-thanks-to-higher-prices/122849.article
- **FDRA footwear CPI:** flat for 2025 as a whole; 2026 rose from +1.5% YoY (Feb) to **+5.2% in May (fastest in nearly four years)**, +4.1% June, +3.4% July; H1 2026 +3.2%. FDRA's chief economist said 2026 is "on pace to see one of the fastest increases in footwear prices in more than three decades" and attributes it to tariffs. https://sgbonline.com/fdra-footwear-inflation-expands-at-fastest-pace-in-nearly-four-years/ ; https://sgbonline.com/fdra-footwear-inflation-shows-slight-deceleration-in-june-after-mays-peak-levels/ ; https://www.worldfootwear.com/news/us-retail-footwear-remains-under-pressure-as-consumers-turn-to-value/11747.html
- **Imports and confidence (World Footwear, 2026-09-08):** footwear import volumes −13.0% Jan, −10.1% Feb, −1.5% Mar, −12.1% Apr, +20.7% May, +3.4% Jun; average import price about $13.30 a pair Mar–Jun 2026; consumer confidence −18.5% YoY in June 2026. Same URL as above.
- FDRA also flagged higher oil prices pressuring footwear margins (relevant: Croslite is a petroleum-derived resin, and Crocs' own 10-Q cites "elevated oil prices" raising raw material and transport costs). https://sgbonline.com/exec-fdra-sees-higher-oil-prices-pressuring-footwear-margins/
- AlixPartners 2026 back-to-school survey: shoppers buying earlier, "fewer, pricier pairs". https://www.alixpartners.com/newsroom/2026-back-to-school-footwear-survey-press-release/
- **Low-income consumer:** Walmart CFO: gap between low- and upper-income cohorts "has grown a little bit in more recent months"; lower-income consumer "more budget conscious and perhaps navigating financial distress". NRF (2026-11-18): the K-shape is "considerably more" visible in discretionary categories than staples. Crocs' own Q3 2026 commentary cited a K-shaped consumer with weakness at the low end and cautious wholesale partners. https://finance.yahoo.com/news/americas-biggest-retailers-see-uneven-results-with-low-income-consumers-feeling-the-squeeze-of-high-prices-140010734.html ; https://nrf.com/blog/reframing-the-debate-on-the-k-shaped-economy
- **TAM figures cited by Crocs management:**
  - Feb/Mar 2023 UBS conference deck: **$160B** casual footwear TAM, with a separate **$30B** category figure (which category the $30B refers to was not confirmed; snippet only). https://s22.q4cdn.com/133460125/files/doc_presentations/2023/03/2023-Crocs-UBS-Presentation-v05.pdf
  - Q2 2025 through Q2 2026 earnings decks: "Global leader in casual footwear with two iconic brands and a **$280B+ TAM**". The definition changed between 2023 and 2025; the footnote explaining it was not read. https://s22.q4cdn.com/133460125/files/doc_financials/2026/q1/Q1-2026-Earnings-Presentation-vF.pdf
  - An older (about 2021) deck referred to a "fragmented $30bn casual market". https://static.seekingalpha.com/uploads/sa_presentations/41/91041/original.pdf
  - Worth flagging on a slide: management's stated TAM went from $160B (2023 deck) to $280B+ (2025–2026 decks) while company revenue went from $3.96B (FY2023) to about $4.04B (FY2025).

---

## 9. Market reaction on the last eight earnings dates

Close-to-close moves computed from Nasdaq prices in local `data/market/px_CROX.json`.

| Date | Move | Reason per news | Source |
|---|---|---|---|
| 2025-02-13 | **+23.9%** ($88.83 → $110.05) | Q4 2024 beat (adj. EPS $2.52 vs $2.26; revenue about $990M vs $962M); HEYDUDE flat vs feared decline; 2025 EPS guide $12.70–$13.15 above $12.58 consensus | https://benzinga.com/25/02/43691979/crocs-smashes-q4-earnings-expectations-amid-strong-china-growth-stock-jumps |
| 2025-05-08 | **+9.8%** ($100.76 → $110.65) | Q1 2025 beat (adj. EPS $3.00 vs $2.49; revenue $937M vs $908M); investors looked past withdrawal of 2025 guidance on tariff uncertainty | https://ng.investing.com/news/stock-market-news/crocs-pulls-guidance-amid-tariff-uncertainty-q1-earnings-beat-1907969 |
| 2025-08-07 | **−29.2%** ($105.13 → $74.39) | Q3 2025 revenue guided −9% to −11% (Street expected slight growth); tariffs; "super cautious" consumer; athletic shift; $737M HEYDUDE impairment. Biggest drop since March 2020 | https://news.bloomberglaw.com/international-trade/crocs-sinks-after-third-quarter-forecast-for-sharp-sales-decline |
| 2025-10-30 | **−2.5%** ($84.69 → $82.54) | Q3 2025 EPS beat ($2.92) but revenue −6.2%, HEYDUDE −21.6%, Q4 guided −8% with HEYDUDE down mid-20s%; Citi cut reported | https://finviz.com/news/213617/why-crocs-crox-shares-are-trading-lower-today |
| 2026-02-12 | **+19.0%** ($82.73 → $98.46) | Q4 2025 beat (adj. EPS $2.29 vs about $1.91; revenue $957.6M vs about $917M); 2026 EPS guide $12.88–$13.35 vs $11.89 consensus; 10% of shares bought back in 2025; $100M cost savings | https://www.fool.com/investing/2026/02/12/why-crocs-stock-jumped-20-thursday-morning |
| 2026-04-30 | **+1.8%** ($100.14 → $101.98) | Q1 2026 beat (adj. EPS $2.99 vs $2.77) and first FY raise, offset by revenue −1.7% and Crocs N.A. −6.1%; stock was down about 3% pre-market before recovering. No article explaining the close was found | https://www.worldfootwear.com/news/crocs-posts-soft-first-quarter-but-raises-full-year-outlook/11450.html ; https://www.chartmill.com/news/CROX/Chartmill-46549-Crocs-NASDAQCROX-Beats-Q1-Estimates-Yet-Stock-Slips-3-Pre-Market (403, snippet only) |
| 2026-07-30 | **−7.4%** ($133.52 → $123.66; about −10% intraday) | Q2 2026 beat and second FY raise, but Q3 guide missed: adj. EPS $3.20–$3.30 vs about $3.53 consensus, revenue about flat; tariffs and mix; HEYDUDE −5.7% | https://www.proactiveinvestors.com/companies/news/1096311/crocs-shares-slide-as-weak-outlook-draws-focus-from-earnings-beat-1096311.html |
| 2026-10-29 | **+25.5%** ($119.69 → $150.26) | Q3 2026 beat (adj. EPS $3.69 vs $3.31; revenue $1.04B, +4.6%); HEYDUDE back to growth (+6.1%); third FY raise to $14.45–$14.65; Q4 guide +7–9% revenue, EPS midpoint $3.35 vs $3.11 consensus | https://www.fool.com/investing/2026/10/29/why-crocs-stock-skyrocketed-today/ |

Observation: four of the eight earnings days moved the stock by 19% or more (three up, one down). This is a guidance-driven, high-volatility name; the average absolute move is about 15%.

---

## 10. Yahoo Finance and Macrotrends data

### Yahoo Finance — Key Statistics (read via web fetch 2026-11-26; "current" column tied to the 2026-11-25 close)

| Metric | Current | 9/30/2026 | 6/30/2026 | 3/31/2026 | 12/31/2025 | 9/30/2025 |
|---|---|---|---|---|---|---|
| Market cap | $7.28B | 5.62B | 5.99B | 4.17B | 4.44B | 4.56B |
| Enterprise value | $8.81B | 7.14B | 7.59B | 5.65B | 5.99B | 6.14B |
| Trailing P/E | 11.95 | 10.28 | -- | -- | 29.69 | 22.70 |
| Forward P/E | 10.03 | 7.73 | 8.77 | 6.58 | 7.67 | 9.18 |
| PEG (5-yr expected) | 4.17 | 3.65 | -- | -- | 5.10 | 1.45 |
| Price/Sales | 1.92 | 1.48 | 1.58 | 1.11 | 1.17 | 1.16 |
| Price/Book | 5.42 | 4.08 | 4.26 | 3.22 | 3.29 | 3.22 |
| EV/Revenue | 2.14 | 1.76 | 1.89 | 1.40 | 1.47 | 1.48 |
| EV/EBITDA | 8.74 | 7.75 | 35.80 | 23.69 | 20.96 | 17.90 |

Source: https://finance.yahoo.com/quote/CROX/key-statistics/ . Trailing multiples for late 2025 to mid 2026 are distorted by the $737M impairment; the "current" trailing P/E and EV/EBITDA are flattered by the $64M tariff refund.

From the Yahoo quote page (https://finance.yahoo.com/quote/CROX/): **Beta (5Y monthly) 1.50**; P/E (TTM) 12.12; EPS (TTM) $13.20; 1-year target $164.67; **next earnings date shown: 2027-02-11** (Yahoo estimate, not company-confirmed).

**Not returned by Yahoo** (fields rendered blank to the fetch tool): short % of float, shares short, % held by institutions/insiders, float, top-holder tables. Substitutes from local Nasdaq files: short interest 3,490,583 shares (2026-11-13), which is about 7–8% of the roughly 46M shares outstanding that Nasdaq shows (derived; the Yahoo "% of float" figure itself was not obtained); institutional ownership shown by Nasdaq as 118.2% (stale share-count artefact).

### Yahoo Finance — Analysis (consensus), read 2026-11-26

| | Q4 2026 | Q1 2027 | **FY2026** | **FY2027** |
|---|---|---|---|---|
| Revenue: analysts | 12 | 7 | 13 | 13 |
| Revenue: average | $1.03B | $956.8M | **$4.18B** | **$4.34B** |
| Revenue: low / high | 1.01B / 1.04B | 950.2M / 967.7M | 4.15B / 4.18B | 4.28B / 4.37B |
| Revenue growth | +7.9% | +3.8% | +3.4% | +3.8% |
| EPS: analysts | 13 | 9 | 14 | 15 |
| EPS: average | $3.40 | $3.43 | **$14.63** | **$16.01** |
| EPS: low / high | 3.32 / 3.45 | 3.20 / 3.68 | 14.55 / 14.82 | 15.24 / 17.12 |
| Year-ago EPS | 2.29 | 2.99 | 12.51 | 14.63 |

EPS trend for FY2027: $16.01 now vs $14.95 thirty days ago and $14.92 ninety days ago (about +7% revision). Source: https://finance.yahoo.com/quote/CROX/analysis/ . Caveat: Yahoo's "7 days ago" column shows the pre-earnings numbers even though results were four weeks ago, so its revision timestamps look lagged.

Implied: at $159.93 the stock is on about 10.9x FY2026 and about 10.0x FY2027 consensus EPS. Consensus FY2026 EPS ($14.63) sits at the top of the guided range ($14.45–$14.65).

### Macrotrends — BLOCKED

https://www.macrotrends.net/stocks/charts/CROX/crocs/pe-ratio and the DECK equivalent both returned **HTTP 403 with a Cloudflare "Just a moment..." challenge**, to the web fetch tool and to plain curl with a simple user agent. Not bypassed. No Macrotrends data captured.

Substitute (different methodology, GAAP year-end P/E) from companiesmarketcap.com, read 2026-11-26:

| Year-end | CROX P/E | DECK P/E |
|---|---|---|
| 2016 | −14.6 | −923 |
| 2017 | −84.3 | 32.8 |
| 2018 | −23.2 | 14.4 |
| 2019 | 24.6 | 16.7 |
| 2020 | 13.4 | 22.1 |
| 2021 | 11.0 | 24.3 |
| 2022 | 12.3 | 21.5 |
| 2023 | 7.22 | 23.9 |
| 2024 | 6.81 | 32.8 |
| 2025 | −71.3 (impairment) | 14.6 |
| Nov 2026 (TTM) | 11.8 | 11.3 |

Sources: https://companiesmarketcap.com/crocs/pe-ratio/ ; https://companiesmarketcap.com/deckers-brands/pe-ratio/ . Note the convergence: CROX traded at a 16–26 point P/E discount to DECK in 2023–2024 and now trades at a slight premium on trailing GAAP. The local StockAnalysis ratio files in `data/sa/` are a better source for a clean series.

---

## 11. Catalysts over the next 12 months

| Date | Catalyst | Source / status |
|---|---|---|
| 2026-11-19 | BNP Paribas Outdoor & Sports Conference (attended; no coverage of remarks found) | https://finviz.com/news/423641/crocs-inc-to-attend-bnp-paribas-outdoor-sports-conference-and-present-at-the-morgan-stanley-global-consumer-retail-conference |
| **2026-12-01, 11:45 ET** | Presentation at Morgan Stanley Global Consumer & Retail Conference (webcast). First read on Black Friday/Cyber Week | same URL |
| Holiday 2026 | Q4 guide is the most demanding of the year: revenue +7–9%, HEYDUDE +10–12%, adj. EPS $3.25–$3.45, against easy comps from 2025 cleanup and a "promotional Q4" | Q3 2026 press release |
| **2027-01-11 to 01-13** | ICR Conference, Orlando. **Correction to the brief:** Crocs pre-announced at ICR in Jan 2023 (8-K 2023-01-10) and Jan 2024 (8-K 2024-01-08), but EDGAR shows **no January pre-announcement 8-K in 2025 or 2026**. The practice appears to have stopped. Whether Crocs attends ICR 2027: not found | https://icrinc.com/conference/ ; EDGAR 8-K list in local `data/sec_submissions_CROX.json` |
| **~2027-02-11** | Q4 2026 results and first FY2027 guidance. Date is Yahoo's estimate; company has not announced (last year the call notice came on 2026-01-22). Early 2027 commentary on the Q3 call: Crocs brand roughly +4%, HEYDUDE low-to-mid single digits | https://finance.yahoo.com/quote/CROX/ |
| Through Q3 2027 | 700–800 bps N.A. DTC growth headwind from the marketplace-model change until lapped | https://www.tradingkey.com/news/transcripts/262253894-tradingkey |
| Q4 2026 – H1 2027 | Remaining IEEPA refunds: about $8–13M still to come ($75–80M eligible less $67M received). Then the GAAP tailwind disappears and Q3 2027 faces a $64M cost-of-sales comp | Q3 2026 10-Q |
| Open-ended | Section 301 "forced labor" tariffs (10–12.5%): CIT challenge pending; Vietnam may qualify for the 10% tier. Section 122 appeal. Any ruling cuts both ways | section 5c |
| Open-ended | Securities class action: motion-to-dismiss ruling (filed 2026-02-27, pending about 9 months) | section 1a |
| Open-ended | Supreme Court decision on cert in *Crocs v. ITC* (No. 26-421) | section 1b |
| **2027-11** | **Revolving credit facility ($1.0B, $113M drawn) matures November 2027**, so it should need extending or refinancing within the next 12 months (my inference from the maturity date; no refinancing announcement found). Other debt: $500M Term Loan B due 2029-02-17; $350M 4.25% notes due 2029-03-15; $350M 4.125% notes due 2031-08-15. Total borrowings $1.29B | Q3 2026 10-Q |
| Ongoing | Buyback: authorization raised by $1.5B to about $2.0B on 2026-07-27; about $1.7B left at 2026-09-30; $500.6M repurchased in 9M 2026 (4.4M shares). Guidance excludes buybacks | Q3 2026 10-Q |
| Product / collabs | LEGO multi-year partnership (announced 2026-01-23; Brick Clog $149.99; "multiple product drops planned for 2026 and beyond"); Umbro football capsule (2026-05-08, the nearest thing to a World Cup tie-in found); Yu-Gi-Oh! (2026-09-09); DOE (Fall 2026); Kiko Kostadinov (Paris FW F/W 2026); LoveShackFancy ballet flats (2026-03-05); NFL team collection; HEYDUDE x Sydney Sweeney campaign; "Wonderfully Unordinary" global brand narrative (2026) | https://www.lego.com/en-au/aboutus/news/2026/january/the-lego-group-and-crocs-enter-multi-year-global-partnership ; https://www.theindustry.fashion/crocs-teams-up-with-umbro-for-exclusive-football-inspired-clogs/ ; https://investors.crocs.com/news-and-events/press-releases/press-release-details/2026/Crocs-Unveils-Wonderfully-Unordinary-a-New-Global-Brand-Narrative-Ushering-in-the-Next-Era-of-Self-Expression/default.aspx |
| Official FIFA World Cup 2026 tie-in | **Not found** | — |
| Investor day | **Not found** (none announced) | — |
| Index inclusion | CROX has been in the **S&P MidCap 400 since 2021-06-02**. S&P 500 addition threshold was $22.7B (set 2025-07-01; later updates not found); CROX market cap is about $7.3B, **below even the MidCap 400 addition floor of $8.0B**. S&P 500 inclusion is not a realistic catalyst. Not in the Nasdaq-100 | https://press.spglobal.com/2021-05-26-Crocs-Set-to-Join-S-P-MidCap-400-and-Organogenesis-to-Join-S-P-SmallCap-600 ; https://press.spglobal.com/2025-07-01-S-P-Dow-Jones-Indices-Announces-Update-to-S-P-Composite-1500-Market-Cap-Guidelines |

---

## Not found (consolidated)

1. Ruling on the motion to dismiss in *Carretta v. Crocs* (none appears to exist as of the 2026-10-29 10-Q).
2. Any securities class action in D. Colo. (only derivative suits there).
3. Any activist short report (Spruce Point, Hindenburg, Kerrisdale, Jehoshaphat). Hedgeye "Best Idea Short" exists but could not be read.
4. Goldman's full written Sell thesis; confirmation of the Citi (Oct 2025) and Williams Trading (Feb 2026) Sell-type ratings.
5. Any 13D or activist campaign 2024–2026.
6. CEO Rees' contract term; reason for Susan Healy's resignation.
7. Customs disputes other than IEEPA refunds; footwear-specific Section 232 action; industry-wide IEEPA dollars refunded.
8. Piper Sandler HEYDUDE rank for Spring 2025 and Fall 2025; Crocs' Spring 2025 rank is inferred.
9. Raw Google Trends data; StockX/resale data; clog category growth % from Circana; dupe market share.
10. Brand-specific commentary on Crocs/HEYDUDE from Foot Locker, Dick's, DSW, Famous Footwear, Academy, Shoe Carnival or Journeys.
11. Macrotrends P/E history (blocked, 403). Yahoo short % of float and holder tables (blank).
12. Explanation for the 2026-04-30 closing move; Crocs' ICR 2027 participation; confirmed Q4 2026 earnings date; investor day; official World Cup partnership.
13. Remand outcome/damages in the Dawgs false-advertising case; verdict in Crocs v. Joybees; specific clog patent expiry dates.
