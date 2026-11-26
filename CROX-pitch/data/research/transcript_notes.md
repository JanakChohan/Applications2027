# Crocs, Inc. (CROX) — Earnings call transcript notes

Prepared 2026-11-26. Covers the six calls from Q2 2025 (Aug 7, 2025) to Q3 2026 (Oct 29, 2026).

**Rules followed.** Every passage inside double quotes below is verbatim from the transcript named at the top of that call's section, and was machine-checked against the saved text file (script result at the end). `[...]` marks an elision inside a quote. FactSet's own markers (`[ph]`, `[indiscernible]`) are left as printed. Numbers outside quotes are my paraphrase of the same transcript unless a different source is named. Where an item is marked not found, I searched all six transcripts and it is not there.

**Growth-rate convention.** Management says on every call that "All revenue growth rates will be cited on a constant currency basis unless otherwise stated." FY2026 guidance is on a reported basis.

## 0. Sources

| Call | Date | Primary source used for quotes | Saved file (in `data/transcripts/`) | Second copy |
|---|---|---|---|---|
| Q3 2026 | 2026-10-29 | Motley Fool: https://www.fool.com/earnings/call-transcripts/2026/10/29/crocs-crox-q3-2026-earnings-call-transcript/ | `2026-10-29_Q3-2026_fool.txt` | none (company PDF not posted at the expected URL; Webull/TradingKey pages did not return transcript text to a plain request) |
| Q2 2026 | 2026-07-30 | Company IR (FactSet corrected): https://s22.q4cdn.com/133460125/files/doc_financials/2026/q2/CORRECTED-TRANSCRIPT_-Crocs-Inc-CROX-US-Q2-2026-Earnings-Call-30-July-2026-8_30-AM-ET.pdf | `2026-07-30_Q2-2026_crocs-IR-factset.txt` | `2026-07-30_Q2-2026_fool.txt` (https://www.fool.com/earnings/call-transcripts/2026/08/07/crocs-crox-q2-2026-earnings-call-transcript/) |
| Q1 2026 | 2026-04-30 | Company IR (FactSet corrected): https://s22.q4cdn.com/133460125/files/doc_financials/2026/q1/CORRECTED-TRANSCRIPT_-Crocs-Inc-CROX-US-Q1-2026-Earnings-Call-30-April-2026-8_30-AM-ET.pdf | `2026-04-30_Q1-2026_crocs-IR-factset.txt` | `2026-04-30_Q1-2026_fool.txt` (https://www.fool.com/earnings/call-transcripts/2026/04/30/crocs-crox-q1-2026-earnings-transcript/) |
| Q4 2025 | 2026-02-12 | Company IR (FactSet corrected): https://s22.q4cdn.com/133460125/files/doc_financials/2025/q4/CORRECTED-TRANSCRIPT_-Crocs-Inc-CROX-US-Q4-2025-Earnings-Call-12-February-2026-8_30-AM-ET.pdf | `2026-02-12_Q4-2025_crocs-IR-factset.txt` | `2026-02-12_Q4-2025_fool.txt` (https://www.fool.com/earnings/call-transcripts/2026/02/12/crocs-crox-q4-2025-earnings-call-transcript/) |
| Q3 2025 | 2025-10-30 | Company IR (FactSet corrected): https://s22.q4cdn.com/133460125/files/doc_financials/2025/q3/Crocs-Inc-CROX-US-Q3-2025-Earnings-Call-30-October-2025-8-30-AM-ET.pdf | `2025-10-30_Q3-2025_crocs-IR-factset.txt` | none |
| Q2 2025 | 2025-08-07 | Company IR: https://s22.q4cdn.com/133460125/files/doc_financials/2025/q2/Crocs-Inc-Seconf-Quarter-2025-Earnings-Call-Transcript.pdf | `2025-08-07_Q2-2025_crocs-IR-factset.txt` (the PDF is a conference-service transcript, not FactSet; file name kept for consistency) | none |

All retrieved 2026-11-26 with plain `curl` and a simple script user agent. Nothing was paywalled or blocked on these URLs.

**Reliability.** Five of six calls are quoted from the transcript the company itself hosts. Q3 2026 is quoted from Motley Fool only, which is machine-transcribed and carries a disclaimer about possible errors; treat its wording as slightly less reliable (for example it spells the new IR head "Elizabeth Bouquard Pizzi", which I could not confirm elsewhere). The Takeaways, Risks and Summary blocks at the top of Fool pages are Fool's own summary and are not quoted here as management.

## 1. Management as stated on the calls

| Role | Name | Evidence |
|---|---|---|
| Chief Executive Officer (and Director) | Andrew Rees | All six calls. Q3 2026 intro: "With me today are Andrew Rees, Chief Executive Officer, and Patraic Reagan, Executive Vice President and Chief Financial Officer." |
| EVP and Chief Financial Officer | Patraic Reagan | First call was Q3 2025 (Oct 30, 2025). Rees on that call: "I would like to start by welcoming our Chief Financial Officer, Patraic Reagan, to his first Crocs, Inc. earnings call." |
| Prior CFO | Susan Healy | Presented the Q2 2025 call (Aug 7, 2025) as Chief Financial Officer. |
| Chief Brand Officer (both brands) | Terence Reilly | Q3 2025, Rees: "Terence Reilly, our Chief Brand Officer, did a amazing job live streaming from the store". Q2 2025, Rees: "Terence is getting settled as the Chief Brand Officer over both brands". |
| HEYDUDE brand president | Vacant as of Aug 2025; Rees acting | Q2 2025, Rees: "So the current leadership for HEYDUDE is myself." and "While we have not yet appointed a brand president of HEYDUDE, I would say that we have appointed some key team members". No later call names a HEYDUDE president. |
| Crocs brand president | Not found | No call in the set names one. |
| Investor relations | Elizabeth Bouquard Pizzi, "Vice President in Investor Relations" (Q3 2026, spelling per Fool); Abigail Ritter, Senior Manager IR & Strategic Finance (Q1 and Q2 2026); Erinn Murphy, SVP IR & Strategy (Q2 2025 to Q4 2025) | Q3 2026, Rees: "I'd like to welcome Elizabeth in her new role as Vice President of Investor Relations." |

Management changes during 2025-2026:

- **CFO change.** Healy on the Aug 7, 2025 call; Reagan on the Oct 30, 2025 call. Not discussed on a call beyond the welcome. Cross-check from the 8-K already in `data/sec_txt/2025-08-29_8-K_crox-20250828.txt` (not a transcript): Healy resigned Aug 28, 2025 effective immediately; Reagan (ex-SharkNinja CFO, ex-Nike) appointed effective Sept 22, 2025.
- **HEYDUDE leadership.** Q2 2025 analyst question refers to "changes at the organization, at the Chief Brand Officer level, Chief Strategy position". Rees: "we've strengthened our sort of growth and transformation with the addition of a strategy and growth officer" (not named on the call). Q3 2025, Rees on HEYDUDE: "We have retooled the management team and I'm very confident in the strength of our management team". Cross-check from `data/sec_txt/2025-05-21_8-K_crox-20250516.txt` (not a transcript): Reilly moved from Brand President for HEYDUDE to Chief Brand Officer on May 16, 2025, with Rees as interim HEYDUDE president.
- **IR.** Erinn Murphy last appears on the Feb 12, 2026 call; Abigail Ritter ran the Apr and Jul 2026 calls; new VP IR welcomed Oct 29, 2026. Murphy's departure is not explained on any call.
- **Chief Digital Officer.** Not mentioned on any call. The 8-K in `data/sec_txt/2025-03-07_8-K_crox-20250303.txt` records Adam Michaels' resignation effective May 1, 2025.

## 2. Guidance tracker

### 2a. FY2026 guidance: every change, by line (last four calls)

| Line | Feb 12, 2026 (initial) | Apr 30, 2026 | Jul 30, 2026 | Oct 29, 2026 |
|---|---|---|---|---|
| Enterprise revenue (reported) | up slightly to down 1% | up 1% to down 1% (top raised) | up 1% to 2% (raised) | up approximately 3% (raised) |
| **Crocs Brand** revenue | flat to up 2% | flat to up 2% (unchanged) | up 2% to 3% (raised) | up approximately 4% (raised) |
| Crocs international | approximately 10% growth | "high single digits to approaching 10%" (trimmed; Middle East distributor) | not re-quantified ("led by international growth") | not re-quantified ("led by international growth") |
| Crocs North America | down; rate to "improve slightly from 2025's run rate" (2025 was down 7%); DTC to outperform wholesale | declines in North America (unchanged) | "down for the year with declines led by the wholesale channel"; DTC positive for the year excluding the marketplace revenue-recognition change | "continue to improve versus prior year"; Rees: growing for the year if normalized for the business model shift |
| **HEYDUDE** revenue | down 7% to 9%; return to growth in H2 | down 5% to 7% (raised) | down 2% to 4% (raised) | approximately flat (raised) |
| Adjusted gross margin | up slightly, despite ~80 bps incremental tariff pressure, all in H1 | slightly up (unchanged) | slightly up (unchanged) | up slightly (unchanged) |
| Adjusted SG&A dollars | roughly flat | roughly flat | roughly flat | slightly up (changed) |
| Adjusted operating margin | expand modestly from 22.3% | same | same | expand modestly from 22.5% (raised; the Q3 2026 press release in `data/sec_txt/` confirms "up from our previous guidance of expansion from 22.3%") |
| Items excluded from adjusted | ~$25M discrete costs for cost-savings implementation | ~$25M non-recurring costs | ~$25M non-recurring costs | non-GAAP **net benefit** of ~$40M (tariff refunds net of cost-reduction charges) |
| Adjusted diluted EPS | $12.88 to $13.35 | $13.20 to $13.75 | $13.70 to $14.00 | $14.45 to $14.65 |
| Buybacks in EPS guide | excluded; guide "reflects future debt repayment" | excluded | excluded | excluded |
| Tax rate | 18% non-GAAP, 23% GAAP | same | same | unchanged |
| Capex | $70M to $80M | same | same | unchanged |
| Tariff, annualized unmitigated | ~$80M (down from ~$90M given Aug 2025) | not updated; refunds not in guide | not updated | not updated; $64M refunds received in Q3 and excluded from adjusted results |
| Net leverage target | 1x to 1.5x | same | same | same |

Cumulative move Feb to Oct 2026: enterprise revenue midpoint roughly -0.5% to about +3%; Crocs midpoint +1% to +4%; HEYDUDE midpoint -8% to flat; EPS midpoint $13.12 to $14.55 (+$1.43, +11%). Three raises in three quarters.

### 2b. Next-quarter guidance versus what was then reported

| Guide given on | For quarter | Enterprise revenue | Crocs Brand | HEYDUDE | Adj. operating margin | Adj. EPS | Reported on the following call |
|---|---|---|---|---|---|---|---|
| Aug 7, 2025 | Q3 2025 | down 9% to 11% | down mid-single digits | not quantified (Rees confirmed a "leg down") | 18% to 19%, incl. ~170 bps tariff | not given | ~$1B, down 7%; Crocs $836M, down 3%; HEYDUDE $160M, down 22%; margin 20.8%; EPS $2.92; tariff hit 230 bps |
| Oct 30, 2025 | Q4 2025 | down ~8% | down ~3% (intl low-double-digit up; NA down low-double digits) | down mid-20s % | ~15.5%; gross margin down ~300 bps | $1.82 to $1.92 | ~$958M, down 4%; Crocs $768M, up slightly (reported); HEYDUDE $189M, down 18%; margin 16.8%; Q4 EPS not stated on the call ($2.29 per the press release in `data/sec_txt/`); tariff hit 300 bps |
| Feb 12, 2026 | Q1 2026 | down 3.5% to 5.5% | down low single digits | down 15% to 18% | ~21.5%; gross margin flat; tariff ~100 bps | $2.67 to $2.77 | $921M, down 2% reported / down 4% constant currency; Crocs $767M, down 2%; HEYDUDE $154M, down 13%; margin 22.3%; gross margin down 90 bps; EPS $2.99 |
| Apr 30, 2026 | Q2 2026 | down slightly | up 1% to 3% | down 12% to 14% | ~24.7%; gross margin down ~150 bps | $4.15 to $4.35 | $1.2B, up 2%; Crocs $1B, up 4%; HEYDUDE $179M, down 6%; margin 25.1%; gross margin down 170 bps (tariff 160 bps); EPS $4.55 |
| Jul 30, 2026 | Q3 2026 | approximately flat | up ~1% | flat to down 3% | ~21.5%; gross margin up ~170 bps | $3.20 to $3.30 | just over $1B, up 5%; Crocs $873M, up 4%; HEYDUDE $170M, up 6%; margin 22.3%; gross margin up 180 bps; EPS $3.69 |
| Oct 29, 2026 | Q4 2026 | up 7% to 9% | up 6% to 8% | up 10% to 12% | ~20.5%; gross margin up ~200 bps | $3.25 to $3.45 | not yet reported |

Every quarterly guide in the set was beaten on revenue, adjusted operating margin and (where guided) EPS. The misses were on gross margin and tariffs: Q3 2025 tariff hit 230 bps against 170 assumed; Q1 2026 gross margin down 90 bps against a flat guide; Q2 2026 down 170 bps against about 150.

Discrepancy to be aware of: on the Jul 30, 2026 call Reagan said Q2 EPS was "ahead of our guidance of $4.15 to $4.30 per share" (both the FactSet and Fool copies print $4.30). The Apr 30, 2026 call and press release gave $4.15 to $4.35.

### 2c. Tariff headwind as quantified call by call

| Call | Dollar figure | Basis points |
|---|---|---|
| Aug 7, 2025 | ~$40M in H2 2025; ~$90M annualized, "based on our current sourcing mix" | Q3 2025 guide embeds ~170 bps |
| Oct 30, 2025 | none | Q3 2025 actual 230 bps (60 bps worse than expected); Q4 2025 gross margin guided down ~300 bps "driven almost entirely by tariff headwinds" |
| Feb 12, 2026 | ~$80M annualized unmitigated (down from $90M) | FY2025 130 bps; Q4 2025 300 bps; FY2026 ~80 bps incremental, in H1; Q1 2026 ~100 bps; Q2 2026 close to 200 bps |
| Apr 30, 2026 | none; refunds not in guide | Q1 2026 actual 100 bps incremental |
| Jul 30, 2026 | none | Q2 2026 actual 160 bps incremental; reminder that Q4 2025 was 300 bps and Q3 2025 was 230 bps |
| Oct 29, 2026 | $64M tariff refunds received in Q3 2026, excluded from adjusted gross margin | "lower tariffs" cited as a gross-margin tailwind; no bps given |

### 2d. Cost savings programme as described

- Aug 7, 2025: $50M "already actioned"; $15M realized in Q2 2025, remaining $35M split evenly across Q3 and Q4, balanced between SG&A and gross margin.
- Oct 30, 2025: a further $100M of gross savings identified for 2026 (organizational simplification, non-critical spend, supply chain). How much drops to profit left open.
- Feb 12, 2026: $50M programme "effectively executed"; $100M for 2026, "relatively balanced" between cost of goods and SG&A; ~$25M of implementation costs excluded from adjusted results; Q4 2025 excluded ~$14M tied mostly to a reduction in force.
- Apr 30, 2026: Rees says both rounds "have all been completed".
- Oct 29, 2026: Reagan refers to "$150 million of cost savings that we put through our P&L over the last couple of years".

---

## 3. Q3 2026 call — October 29, 2026

Source: https://www.fool.com/earnings/call-transcripts/2026/10/29/crocs-crox-q3-2026-earnings-call-transcript/ (retrieved 2026-11-26). Speakers: Andrew Rees, Chief Executive Officer; Patraic Reagan, Executive Vice President and Chief Financial Officer.

### Guidance and change versus July

- FY2026 enterprise revenue: up approximately 3% (was up 1% to 2%).
- Crocs Brand: up approximately 4% (was up 2% to 3%), led by international. North America to keep improving.
- HEYDUDE: approximately flat (was down 2% to 4%).
- Adjusted EPS: $14.45 to $14.65 (was $13.70 to $14.00); no future buybacks assumed.
- Adjusted operating margin: expand modestly from 22.5% (was from 22.3%). Excludes a non-GAAP net benefit of about $40M tied to tariff refunds and cost-reduction initiatives.
- Adjusted gross margin up slightly (unchanged). Adjusted SG&A dollars now slightly up (was roughly flat). Tax and capex ($70M to $80M) unchanged.
- Q4 2026: enterprise revenue up 7% to 9%; Crocs up 6% to 8%; HEYDUDE up 10% to 12%; adjusted operating margin about 20.5% with gross margin up about 200 bps; adjusted EPS $3.25 to $3.45.
- North America DTC "business model shift" (one large marketplace partner moved from DTC to wholesale accounting): 270 bps headwind to North America DTC in Q3 (about one month); 700 to 800 bps per quarter until it is lapped in Q3 2027; about half the DTC dollars reappear in wholesale.
- 2027 colour (not formal guidance): HEYDUDE low- to mid-single-digit growth; Crocs a growth year at roughly 2026's rate.
- Capital return in Q3: about 2M shares for $250M; $21M debt repaid; net leverage at the low end of 1x to 1.5x.

### Management quotes

1. **(a) Crocs North America.** "North America revenue declined approximately 2%, in part driven by the previously communicated impact of our business model shift from the direct-to-consumer to wholesale segment. This shift represents a 270 basis point headwind to the North America DTC channel, reflecting approximately one month of impact to the quarter as we began implementing." — Patraic Reagan, EVP and CFO (prepared remarks)
2. **(a) Underlying North America DTC.** "To be clear, D2C would have been up roughly about 2% in North America excluding this shift." [...] "What it roughly means from a modeling standpoint is that you can think of in the neighborhood of 700-800 basis points of headwinds for the D2C channel as we make our way through the next several quarters." — Patraic Reagan, EVP and CFO (Q&A)
3. **(b) Sandals and diversification.** "The sandals market represents an estimated $30 billion global addressable market, where we have gained substantial market share, and to date, represent a leading player in this category. Our sandals business continues to grow double digits led by our Miami and Saturday franchises, where we attract new consumers, increase purchase frequency, and gain market share." — Andrew Rees, CEO (prepared remarks)
4. **(c) International.** "The biggest drivers of that growth are actually the big markets. Number one, China, number two, India, and also Japan." — Andrew Rees, CEO (Q&A). Also: "Although I would highlight our international business is actually bigger than our North American business today." — Andrew Rees, CEO (Q&A)
5. **(d) HEYDUDE sustainable growth rate.** "I would say, as we kind of think about Q3 and Q4 together, and we remove the cleanup that we did last year, we are looking at about a low single to mid-single sustainable growth rate for the brand, and we think that is where it will be in the short term." — Andrew Rees, CEO (Q&A)
6. **(d) HEYDUDE channel and margin.** "From a wholesale channel perspective, as we look at our inventories in the channel, we look at the performance of those inventories, we are outselling our inventory in the channel." — Andrew Rees, CEO (Q&A). And: "Compared to last year, gross margin increased 350 basis points while SG&A decreased 9%." — Andrew Rees, CEO (prepared remarks)
7. **(e) Tariff refunds.** "Notably, adjusted gross margin excludes $64 million of tariff refunds, which we received during the quarter." — Patraic Reagan, EVP and CFO (prepared remarks). On rates: "How we would contextualize both Q3 and Q4 is tariff rates were slightly favorable to us on a year-over-year comparison standpoint versus 2025, slightly." — Patraic Reagan, EVP and CFO (Q&A)
8. **(f) Cost savings.** "We've got plenty of levers that are available to us in terms of how we keep our profitability, whether that's through pricing, whether that's through efficiencies in our supply chain, whether it's through the $150 million of cost savings that we put through our P&L over the last couple of years." — Patraic Reagan, EVP and CFO (Q&A)
9. **(g) Capital allocation.** "Importantly, over the last decade, we have taken our powerful value creation engine and returned meaningful cash to shareholders with approximately $3 billion of share repurchases and 37% reduction in share count." — Andrew Rees, CEO (prepared remarks). And: "During the quarter, we paid down an additional $21 million of debt and ended the quarter with net leverage at the low end of our target range of 1x-1.5x." — Patraic Reagan, EVP and CFO (prepared remarks)
10. **(h) Social commerce.** "Notably, this quarter, we maintained our number 1 footwear brand ranking on TikTok Shop in the U.S., U.K., Japan, and most recently, Malaysia." — Andrew Rees, CEO (prepared remarks)
11. **(i) Consumer.** "But we see weakness at the low-end consumer, and we see strength at the high-end consumer." [...] "I think we do benefit from selling in the $50 $60 range, really across both of our brands." — Andrew Rees, CEO (Q&A)
12. **(j) 2027.** "From a Crocs brand standpoint, again, we're confident in the growth, and as we go into 2027, we feel confident that it's going to be a growth year for Crocs, likely roughly about what we grew at overall this year." — Patraic Reagan, EVP and CFO (Q&A)

### Three toughest analyst questions

1. **Jonathan Komp (Baird): what is the underlying health of Crocs North America DTC once the marketplace shift is stripped out, and what is the path to North America growth?** Reagan quantified the shift for the first time (270 bps in Q3, 700 to 800 bps for the next three quarters, no change to units or share). Rees gave three supports: product pipeline, social selling, wholesale relationships. Verbatim: "I do think it is exceptionally important to underline that there is no change to units in the market or market share." — Patraic Reagan
2. **Jonathan Komp (Baird): HEYDUDE once made over $900M of revenue and over $200M of profit; where is it in that journey?** Rees conceded the wholesale growth was against a weak comparison and put the near-term rate at low- to mid-single digits; longer term he pointed to under-penetrated US regions and international, with no number. Verbatim: "I think the critical thing to kind of bear in mind from a wholesale channel perspective is we are up against a weak compare." — Andrew Rees
3. **Brooke Roach (Goldman Sachs): how much of the implied Q4 acceleration is easy comparisons, and is 200 bps of gross margin expansion sustainable into 2027 with raw material and oil costs rising?** Rees accepted that easier wholesale sell-in comparisons are one of three drivers and that they run into early 2027. Reagan declined to size the gross margin pieces or guide 2027. Verbatim: "I think we can all recognize that we're in an elevated inflationary environment, right?" — Patraic Reagan

### Activity metrics (not revenue)

- Shares repurchased: about 2 million for $250M. Fool's summary block gives an average price of $123.32; that figure is not in the spoken transcript.
- Ten-year capital return: about $3B of repurchases, 37% reduction in share count.
- Inventory turns "above our goal of four times" annualized. Inventory $413M, up 4%.
- Crocs Brand DTC up 8%; Crocs international DTC up 24%; North America DTC about +2% excluding the shift.
- HEYDUDE: eight collaborations launched in Q3, "each one selling out"; Buc-ee's collaboration "sold out in just 24 hours"; wholesale up 14%, DTC "up slightly"; SG&A down 9%.
- China Echo 2.0 campaign with Fan Zhendong: "40 billion impressions" (as transcribed).
- TikTok Shop: number 1 footwear brand in the US, UK, Japan and Malaysia.
- Price points: bulk of volume in the "$50 $60 range".
- HEYDUDE store plan: no significant additions over the next 12 to 24 months.
- Not given on this call: units or pairs, ASP figures, store counts, Jibbitz mix, brand awareness.

---

## 4. Q2 2026 call — July 30, 2026

Source: https://s22.q4cdn.com/133460125/files/doc_financials/2026/q2/CORRECTED-TRANSCRIPT_-Crocs-Inc-CROX-US-Q2-2026-Earnings-Call-30-July-2026-8_30-AM-ET.pdf (retrieved 2026-11-26). Speakers: Andrew Rees, Chief Executive Officer & Director; Patraic Reagan, Chief Financial Officer & Executive Vice President.

### Guidance and change versus April

- FY2026 enterprise revenue: up 1% to 2% (was up 1% to down 1%).
- Crocs Brand: up 2% to 3% (was flat to up 2%). North America still expected down for the year, wholesale-led.
- HEYDUDE: down approximately 2% to 4% (was down 5% to 7%).
- Adjusted EPS: $13.70 to $14.00 (was $13.20 to $13.75).
- Unchanged: gross margin slightly up; SG&A dollars roughly flat; operating margin to expand modestly from 22.3%; ~$25M non-recurring costs excluded; tax 18% / 23%; capex $70M to $80M.
- New: revenue-recognition change with "one of our largest marketplace partners" in Crocs North America from Q3 (lower DTC revenue, higher wholesale revenue, lower total revenue, neutral units, higher operating profit). Not quantified on this call.
- New: additional $1.5B buyback authorization, total available about $2B.
- Q3 2026: revenue about flat; Crocs up about 1%; HEYDUDE flat to down 3%; adjusted operating margin about 21.5% with gross margin up about 170 bps; adjusted EPS $3.20 to $3.30.
- Capital return in Q2: about 2.3M shares for $251M; $31M debt repaid.

### Management quotes

1. **(a) North America back to growth, with less promotion.** "North America returned to growth, up slightly to prior year. Within North America, the direct-to-consumer channel was up 5% to prior year, led by marketplace outperformance and despite our continued year-over-year reduction in promotional activity." — Patraic Reagan, CFO (prepared remarks)
2. **(a) But not for the full year.** "And from a Crocs perspective, we will not be returning to growth here in 2026, but we will meaningfully reduce the rate of decline that we saw in 2025." — Andrew Rees, CEO (Q&A, speaking of North America)
3. **(a) The marketplace accounting change.** "One, we will recognize lower revenue in our DTC channel. Two, conversely, we will recognize higher revenue in our wholesale channel. Three, the net of these revenue shifts will be lower overall revenue. Four, this will be neutral from a units sold and market share perspective. And five, we will see an improvement to operating profit." — Patraic Reagan, CFO (prepared remarks)
4. **(b) Sandals size.** "With the sandal business this year will be $0.5 billion dollars on a global basis. So, that is a meaningful business." [...] "We estimate it's in excess of $30 billion on a global basis, it's an annual refresh category, particularly for women." — Andrew Rees, CEO (Q&A)
5. **(b) Clog diversification and the Classic.** "As for our Classic franchise with a North American Wholesale, we are on plan with our strategy to tighten inventory and channel and further segment our business across key partners." — Andrew Rees, CEO (prepared remarks)
6. **(c) International.** "We saw double-digit growth in high priority markets, China, India and Japan, followed by key markets in Western Europe." — Andrew Rees, CEO (prepared remarks). On profitability: "the flow through of that growth to profitability from our international business is as strong as our North American business." — Andrew Rees, CEO (Q&A)
7. **(d) HEYDUDE wholesale.** "Wholesale was better than anticipated, down 17%, supported by higher at-once demand and thoughtful management of in-channel inventory." — Andrew Rees, CEO (prepared remarks)
8. **(e) Tariffs.** "Enterprise adjusted gross margin of 60% was down 170 basis points to prior year, driven by 160 basis points of incremental tariff impact." — Patraic Reagan, CFO (prepared remarks). And: "And for margins, the fourth quarter of 2025 had a larger tariff headwind of 300 basis points versus Q3 at 230 basis points." — Patraic Reagan, CFO (prepared remarks)
9. **(g) Buyback.** "Reflecting our confidence in the business and future cash flow generation, earlier this week, our board approved an additional $1.5 billion share repurchase authorization, bringing our total available authorization to approximately $2 billion." — Patraic Reagan, CFO (prepared remarks)
10. **(h) Social and AI commerce.** "As we continue to push the boundaries of digital commerce, we've also become the first brand to launch a shoppable series within TikTok Shop." — Andrew Rees, CEO (prepared remarks). And: "In addition, we began testing AI-enabled shopping experiences across platforms, such as ChatGPT and Copilot during the quarter." — Andrew Rees, CEO (prepared remarks)
11. **(i) Wholesale partners' caution.** "And then, I think, the third thing I'd say, as we look at the consumer landscape that our wholesale partners are dealing with, I think they're planning their business relatively conservatively." — Andrew Rees, CEO (Q&A)

### Three toughest analyst questions

1. **Adrienne Yih (Barclays): is the slowdown in the Q3 Crocs guide (about 1% against 3.7% constant currency) all due to the revenue-recognition change, and what share of sales does it touch?** Reagan would not size it, saying only that it is one strategically significant partner, Crocs North America only, with no effect on units or share. Verbatim: "You know what I'd say in terms of percentage of marketplace shift, we're not going to get into the quantification exactly of those numbers." — Patraic Reagan
2. **Kendall Toscano (BofA): what would Q2 North America DTC have been under the new accounting; would it still be positive? And why did gross margin miss (down 170 bps against a 150 bps guide)?** Rees gave one data point and nothing more; Reagan attributed the margin to tariffs plus product and channel mix from diversification. Verbatim: "What I would say to your specific question, if this had been in place for the first half of 2026, we would still have been positive in DTC in the Crocs Brand in North America." — Andrew Rees
3. **Tom Nikic (Needham): the HEYDUDE guide implies mid- to high-single-digit growth in Q4; how real is that?** Rees agreed the step-up is steep and said part of it is the weak comparison created by last year's reset. Verbatim: "And you are right, there is a steep increase in Q4, and that is relative to two things. One is confidence. We have been growing in both channels. And two is the reset actions that we took last year that created a very weak compare." — Andrew Rees

### Activity metrics (not revenue)

- First quarter in which Crocs Brand revenue exceeded $1B.
- Crocs Brand DTC up 12%; North America DTC up 5%; HEYDUDE DTC up 7%; HEYDUDE wholesale down 17%.
- Stores: "approximately 160 mono-brand stores and kiosks" opened in the quarter, "including 34 owned and operated stores internationally".
- Inventory $389M, down 4%; "Inventory footwear units were down high-single digits"; turns above 4x.
- Shares: about 2.3M repurchased for $251M.
- Sandals: on track for about $0.5B in 2026; market put at over $30B.
- Media: two ReelShorts microdramas "nearly 20 million views"; BAPE collaboration "sold out within minutes globally"; HEYDUDE Burlebo collaboration "sold out in less than 24 hours".
- China: record revenue quarter.
- Not given: pairs, ASP figures, total store count, Jibbitz mix.

---

## 5. Q1 2026 call — April 30, 2026

Source: https://s22.q4cdn.com/133460125/files/doc_financials/2026/q1/CORRECTED-TRANSCRIPT_-Crocs-Inc-CROX-US-Q1-2026-Earnings-Call-30-April-2026-8_30-AM-ET.pdf (retrieved 2026-11-26). Speakers: Andrew Rees, Chief Executive Officer & Director; Patraic Reagan, Chief Financial Officer & Executive Vice President.

### Guidance and change versus February

- FY2026 enterprise revenue: up 1% to down 1% reported (was up slightly to down 1%). Now includes the Middle East distributor impact and higher distribution and logistics costs.
- Crocs Brand: flat to up 2% (unchanged). International now "high single digits to approaching 10%" (was about 10%).
- HEYDUDE: down approximately 5% to 7% (was down 7% to 9%); both channels expected to return to growth in H2.
- Adjusted EPS: $13.20 to $13.75 (was $12.88 to $13.35).
- Unchanged: gross margin slightly up; SG&A dollars roughly flat; operating margin to expand modestly from 22.3%; ~$25M non-recurring costs excluded; tax 18% / 23%; capex $70M to $80M.
- Tariff refunds from the February Supreme Court rulings: expected, but not in guidance.
- Q2 2026: revenue down slightly; Crocs up 1% to 3%; HEYDUDE down 12% to 14%; adjusted operating margin about 24.7% with gross margin down about 150 bps on tariffs; adjusted EPS $4.15 to $4.35.
- Capital return: $747M left on the authorization at quarter end; 800,000 shares for $74M bought quarter-to-date in Q2; net leverage at the low end of 1x to 1.5x. (No Q1 repurchase amount is stated on the call.)

### Management quotes

1. **(a) North America and promotions.** "North America was down 6%, including DTC up 5%, despite a meaningful reduction in promotional activity, offset in part by wholesale declines." — Patraic Reagan, CFO (prepared remarks)
2. **(a) What was done in H2 2025.** "And if you recall during the second half of last year, the team took several strategic actions, but very painful in the moment, to pull back on promotions, pull back on paid search, pull back on inventory going into the marketplace for both Crocs, particularly in North America and HEYDUDE more broadly." — Patraic Reagan, CFO (Q&A)
3. **(b) Sandals.** "Our sandal business started the year off strong and we expect this pillar to approach $500 million in revenue this year up double-digits from 2025." — Andrew Rees, CEO (prepared remarks)
4. **(b) New product is margin-dilutive.** "As a reminder, select new products come with slightly lower product margins." — Patraic Reagan, CFO (prepared remarks)
5. **(c) International mix.** "It's a key growth area for us and within 2026, it'll be the first year that Crocs, Inc. is predominantly a international-driven company." — Patraic Reagan, CFO (Q&A). And: "As it relates to guidance, I think roughly about a quarter ago, we guided to 10% and I would say that we're still very much in the high single digits to approaching 10% within international." — Patraic Reagan, CFO (Q&A)
6. **(d) HEYDUDE wholesale.** "The wholesale channel was down 26%, as we continue to carefully manage our inventory to sell-through levels, consistent with our return-to-growth plan." — Patraic Reagan, CFO (prepared remarks). And: "Wholesale sellouts, while still below our aspirations, improved sequentially versus the fourth quarter." — Andrew Rees, CEO (prepared remarks)
7. **(e) Tariff refunds.** "While we believe we are well-positioned to collect refunds on the incremental tariffs we paid in 2025 and into this year, we have not currently embedded any upside from this within our guidance." — Patraic Reagan, CFO (prepared remarks)
8. **(e) Tariffs after the ruling.** "Then we had the Supreme Court ruling, then we had a response." [...] "But what we do feel better about is that tariffs now become part of our base." — Patraic Reagan, CFO (Q&A)
9. **(f) Cost savings done.** "So, what I'd say – so I think the most important thing from an SG&A perspective is the couple of different rounds of cost-saving initiatives that we've talked to you about have all been completed. So we have attained those cost-saving goals." — Andrew Rees, CEO (Q&A)
10. **(g) Capital allocation.** "Quarter-to-date, we have repurchased 800,000 shares for $74 million and we continue to deliver against our commitment to return meaningful cash to shareholders. Net leverage ended the quarter at the low end of our target range of 1 to 1.5 times." — Patraic Reagan, CFO (prepared remarks)
11. **(h) Social commerce.** "In fact, Crocs was recently awarded Top Seller of the Year on TikTok Shop for 2025, underscoring our ability to continue to reach consumers on their preferred social channels." — Andrew Rees, CEO (prepared remarks)
12. **(i) Consumer and macro.** "As we look closely at our consumer behavior here in North America, in Europe, and in Asia, we're not seeing a discernible trend relative to, I think, what is reported as weak consumer confidence." — Andrew Rees, CEO (Q&A). And: "what we're seeing in maybe more broadly in the marketplace is we're still seeing that the consumer is stressed and that retailers are leaning into promotions as a way to drive both traffic and sales." — Patraic Reagan, CFO (Q&A)

### Three toughest analyst questions

1. **Kendall Toscano (BofA): gross margin fell 90 bps against a flat guide although tariffs came in as expected; what went wrong and does it persist?** Reagan named two drivers: new products carrying lower margin, and HEYDUDE outperforming (lower-margin brand). No sizing for the rest of the year. Verbatim: "And so that turned out to be a little bit more headwind than we thought it was going to be when we planned the quarter, but not necessarily a bad thing." — Patraic Reagan
2. **Tom Nikic (Needham): North America wholesale has been negative for many quarters and will be about 30% below peak by year end; is there line of sight to stabilization?** Rees said yes, without a date or number: inventory right-sized, newness, at-once capacity. Verbatim: "I think the short answer is yes, right. So we feel like the North American wholesale business is exactly where we expected it to be at this point in time." — Andrew Rees
3. **Brooke Roach (Goldman Sachs), following Rick Patel (Raymond James): size the input-cost headwind if oil stays high, the timing, and the role of price.** Rees declined to quantify, called transportation a bigger pressure than resin, and said guidance captures what is known. Verbatim: "I actually probably might point you to transportation as a bigger cost pressure to be quite honest." — Andrew Rees

Also notable: Rees remarked near the end, "I think our entire conversation this morning has been on Crocs, nobody's asked a single question about HEYDUDE."

### Activity metrics (not revenue)

- Crocs Brand DTC up 11%; North America DTC up 5%; HEYDUDE DTC up 8%; HEYDUDE wholesale down 26%.
- Inventory $398M, up 2%; "Inventory footwear units were down high-single-digits"; turns above 4x.
- Stores: "approximately 40 mono-brand stores and kiosks" opened, "including 6 owned and operated stores internationally"; Malaysia distributor converted to owned on April 1, adding "21 highly productive retail stores".
- Shares: 800,000 bought quarter-to-date for $74M; $747M authorization remaining at quarter end.
- Media: ReelShorts micro-drama "over 10 million views". TikTok Shop: Crocs "Top Seller of the Year" 2025; HEYDUDE "Top Growth Seller of the Year"; launching in Japan.
- Oil reference point used by Rees: $120.
- Not given: pairs, ASP, total store count, Jibbitz mix.

---

## 6. Q4 2025 call — February 12, 2026

Source: https://s22.q4cdn.com/133460125/files/doc_financials/2025/q4/CORRECTED-TRANSCRIPT_-Crocs-Inc-CROX-US-Q4-2025-Earnings-Call-12-February-2026-8_30-AM-ET.pdf (retrieved 2026-11-26). Speakers: Andrew Rees, Chief Executive Officer & Director; Patraic Reagan, Chief Financial Officer & Executive Vice President.

### Guidance (first FY2026 guide; the Aug and Oct 2025 calls gave next-quarter guidance only)

- FY2026 enterprise revenue: up slightly to down 1% reported; H2 growth to outpace H1.
- Crocs Brand: flat to up 2%; international about +10%; North America down, improving slightly on 2025's rate.
- HEYDUDE: down approximately 7% to 9%; return to growth in H2 2026.
- Adjusted gross margin up slightly despite about 80 bps incremental tariff pressure (in H1). Unmitigated annualized tariff headwind about $80M (was $90M).
- Adjusted SG&A dollars roughly flat. Adjusted operating margin to expand modestly from 22.3%; ~$25M discrete costs excluded.
- Adjusted EPS $12.88 to $13.35, reflecting debt repayment but no buybacks. Tax 18% / 23%. Capex $70M to $80M. Net leverage 1x to 1.5x.
- Q1 2026: revenue down 3.5% to 5.5%; Crocs down low single digits; HEYDUDE down 15% to 18%; adjusted operating margin about 21.5%; gross margin flat; tariff headwind about 100 bps in Q1 and close to 200 bps in Q2; adjusted EPS $2.67 to $2.77.
- Stores: 200 to 250 Crocs openings planned for 2026.
- 2025 capital return: free cash flow $659M; 6.5M shares for $577M; $128M debt repaid; $747M authorization remaining.

### Management quotes

1. **(a) North America and promotions.** "North America was down 7% to prior year at $1.7 billion. This was tied to both the decision to pull back on promotional activity in our DTC channels earlier in the year, as well as carefully managing our sell-in to the North American market." — Patraic Reagan, CFO (prepared remarks)
2. **(a) Classic Clog discounting.** "We've pulled back on discounting, particularly on the Classic Clog on our digital channels, which is creating some of the headwind, but we are introducing a significant number of new innovative products into the marketplace that are clog-based, right?" — Andrew Rees, CEO (Q&A)
3. **(b) Product mix.** "During the year, clogs represented 74% of our mix, with sales up slightly to last year, led by strong consumer response to our diversified clog franchises." — Andrew Rees, CEO (prepared remarks)
4. **(b) Sandals and Jibbitz.** "Sandals had a very good year and represented 13% of our mix, closing in on the $450 million mark." [...] "Jibbitz, our unique vehicle for self-expression, represented 8% of sales." — Andrew Rees, CEO (prepared remarks)
5. **(c) China and whitespace.** "In China, our second largest market, we grew 30% on top of 64% last year, and the country now represents approximately 8% of sales." [...] "Our average market share in China, India, Japan, Germany and France represented approximately one-third of the market share we have in our established markets." — Andrew Rees, CEO (prepared remarks)
6. **(d) HEYDUDE clean-up cost.** "While these two actions constrained our revenue growth by approximately $45 million in the second half of 2025, they have been effective in cleaning up the channel and establish a more profitable foundation for future growth." — Andrew Rees, CEO (prepared remarks)
7. **(d) HEYDUDE sell-out versus inventory.** "We look at sell-out relative to our inventories on hand and they are at parity at this point." — Andrew Rees, CEO (Q&A)
8. **(e) Tariff dollars.** "Based on current tariff rates and sourcing mix, we now see an unmitigated tariff headwind of approximately $80 million on an annualized basis, which is down from our previously provided figure of $90 million." — Patraic Reagan, CFO (prepared remarks)
9. **(f) Cost savings.** "In addition, we effectively executed our $50 million cost savings program and actioned $100 million of additional cost savings for 2026, as we previously communicated." [...] "We expect these savings to be relatively balanced between our cost of goods sold and SG&A." — Patraic Reagan, CFO (prepared remarks)
10. **(g) Capital allocation.** "We are committed to maintaining net leverage in the range of 1 to 1.5 times, while deploying excess cash flow towards opportunistically buying back shares." — Patraic Reagan, CFO (prepared remarks)
11. **(h) Social commerce.** "In 2025, we launched seven new markets globally with TikTok Shop and have more on our roadmap for 2026." — Andrew Rees, CEO (prepared remarks)
12. **(i) Consumer.** "So the higher-end consumer I think has plenty of disposable income and is shopping. The lower-end consumer I think is still a bit tentative, so – and we think that likely continues through 2026." — Andrew Rees, CEO (Q&A)
13. **(j) Long-run record (no forward target given).** "In the last 20 years, we have relentlessly served our consumers, selling approximately 1.5 billion pairs of shoes, while delivering 14% sales growth on a compound annual growth basis." [...] "In fact, our digital, international and non-clog product categories each represent a revenue stream in excess of $1.5 billion, which we see as compelling drivers for future growth." — Andrew Rees, CEO (prepared remarks)

### Three toughest analyst questions

1. **Mitch Kummetz (Seaport): how much of HEYDUDE's promised H2 growth is simply lapping the $45M clean-up, and is the fall order book positive?** Reagan said part of it is the lap, part is newness and awareness; Rees refused the order-book question. Verbatim: "We don't comment on our order book, Mitch. We haven't done that for many years now, so." — Andrew Rees
2. **Aubrey Tianello (BNP Paribas): how much of the $100M of savings drops to the bottom line and what is in the guide?** Reagan gave no split: savings fund flat SG&A, tariff offset in gross margin, and reinvestment flexibility. Verbatim: "So we're reserving a little bit of flexibility into what we're doing as well as flowing dollars to the bottom line." — Patraic Reagan
3. **Jonathan Komp (Baird): can Crocs North America get back to growth later in 2026?** Reagan guided only to a slight improvement on 2025; Rees called the guide prudent and pointed to international being larger than the US in 2026. Verbatim: "But for the full year, what we're really thinking is slight improvement from what we saw in 2025." — Patraic Reagan

### Activity metrics (not revenue)

- Crocs Brand 2025: "units up 2% to prior year to a total of 129 million pairs sold, while brand ASPs were roughly flat".
- HEYDUDE 2025: "ASPs were up 4% to just under $32, while unit volume was 22 million pairs, down 17%"; Q4 was "the 10th consecutive quarter of positive ASP growth".
- Mix (Crocs Brand, 2025): clogs 74%; sandals 13% (about $450M); Jibbitz 8%. International "almost half" of Crocs Brand sales; China about 8% of sales.
- Market share in China, India, Japan, Germany and France about one-third of that in established markets.
- Stores: "approximately 2,600 Crocs mono-branded stores and kiosks" at year end; 200 to 250 openings planned for 2026. HEYDUDE: 23 opened in 2025, "a total of 75 at year-end", nearly all outlets.
- Awareness: HEYDUDE 39%, up 9 points in a year (Reagan: "from 30% to 39% just in the last six months or so"; the two descriptions of the period differ). Sandal awareness "roughly half that of clogs", up mid-single digits.
- Inventory $369M, up 4% in dollars; units down high single digits; turns above 4x.
- Shares: 6.5M for $577M in 2025, "approximately 10% of our shares outstanding"; Q4 2.2M for $180M at about $84.
- International DTC up 23% in 2025; international growth 11% on top of 19%.
- Since IPO: about 1.5 billion pairs; distribution in over 85 countries.
- TikTok Shop: number one footwear brand in the US; HEYDUDE number two; seven new markets in 2025.

---

## 7. Q3 2025 call — October 30, 2025

Source: https://s22.q4cdn.com/133460125/files/doc_financials/2025/q3/Crocs-Inc-CROX-US-Q3-2025-Earnings-Call-30-October-2025-8-30-AM-ET.pdf (retrieved 2026-11-26). Speakers: Andrew Rees, Chief Executive Officer & Director; Patraic Reagan, Chief Financial Officer & Executive Vice President (first call).

### Guidance and change versus August

- Still no full-year guide.
- Q4 2025: revenue down about 8%; Crocs down about 3% (international accelerating from mid-single-digit to low-double-digit growth; North America down low-double digits); HEYDUDE down mid-20s %; adjusted operating margin about 15.5% (excluding about $10M of cost-reduction charges); gross margin down about 300 bps, almost all tariffs; adjusted SG&A dollars below prior year; adjusted EPS $1.82 to $1.92.
- FY2025 capex $70M to $75M.
- New: $100M of incremental gross cost savings for 2026, on top of the $50M in 2025. Commitment to operating leverage in 2026.
- Versus the August guide for Q3: revenue down 7% (guide down 9% to 11%); adjusted operating margin 20.8% (guide 18% to 19%); tariff hit 230 bps (60 bps worse than assumed).
- Capital return in Q3: 2.4M shares for $203M at about $83; $63M debt repaid; $927M authorization remaining; total borrowings $1.3B; net leverage at the low end of 1x to 1.5x.

### Management quotes

1. **(a) The two deliberate actions.** "First, we pulled back on the breadth and depth of promotional activity across our digital channels in North America. This promotional pullback has had the greatest impact on our Classic Clog business as we work harder to protect our icon. Second, we continue to reduce receipts into the wholesale channel to better match supply to demand and ultimately drive a demand-led model." — Andrew Rees, CEO (prepared remarks)
2. **(a) Effect on gross profit.** "Further, we have seen a net positive benefit to our gross profit dollars in North America as a result of our pullback on promotions." — Andrew Rees, CEO (prepared remarks)
3. **(a) How deep the pullback was.** "It didn't go to zero, obviously, but we did both have many more days that were non-promotional and also the depth of the promotions that we run were typically substantially less than we had run previously." — Andrew Rees, CEO (Q&A)
4. **(c) China.** "China delivered revenue growth across all channels and was up mid 20% to prior year, outperforming the overall market [ph] handily (00:19:25)." — Andrew Rees, CEO (prepared remarks)
5. **(d) HEYDUDE wholesale reset.** "Wholesale was down 39%, reflecting the previously communicated wholesale clean-up actions we took in the quarter. As a result of these actions, we started to see an improvement in wholesale sell-outs, which are now in line with our inventory levels." — Patraic Reagan, CFO (prepared remarks)
6. **(d) No sale of HEYDUDE.** "And so, I think, we're not contemplating any portfolio changes at this time." — Andrew Rees, CEO (Q&A)
7. **(e) Tariff hit.** "The tariff impact in the quarter was 60 basis points higher than we previously anticipated, based on higher receipts and country mix." — Patraic Reagan, CFO (prepared remarks)
8. **(e) Pricing as mitigation.** "So pricing, from a conceptual perspective, we don't price the cost. We price to market, right?" [...] "At this point, though, we are not planning to initiate price increases, for example, on our core Classic Clog here in North America." — Andrew Rees, CEO (Q&A)
9. **(f) Cost savings.** "As we shared on our last call, we've already taken action on $50 million of gross cost savings this year and have since identified another $100 million of gross cost savings across the business to simplify the organization." — Andrew Rees, CEO (prepared remarks)
10. **(g) Buyback.** "During the quarter, we repurchased 2.4 million shares of our common stock for a total of $203 million, at an average cost of approximately $83 per share. This represented approximately 4% of our float." — Patraic Reagan, CFO (prepared remarks)
11. **(h) Social commerce.** "In fact, Crocs was the first fashion brand to live stream 24/7 for an entire month across TikTok [ph] and .com (00:18:52)." — Andrew Rees, CEO (prepared remarks)
12. **(i) Low-income consumer.** "But there is a large portion of consumers who are nervous, they are in less good financial shape, and they're being super cautious about their spending and certainly spending closer to need." — Andrew Rees, CEO (Q&A). And: "We definitely see it in our mid to lower channels. There is less traffic to stores, right?" — Andrew Rees, CEO (Q&A)
13. **Competition.** "We do see the athletic brands, particularly the big ones, leaning back into these price points and increasing distribution" — Andrew Rees, CEO (Q&A)

### Three toughest analyst questions

1. **Jonathan Komp (Baird): nearly four years after buying HEYDUDE and with challenges persisting, is portfolio management on the table?** Rees said no and defended the brand and the retooled team. Verbatim: "We absolutely acknowledge the challenges that we have had in running and operating this brand over the last several years." — Andrew Rees
2. **Christopher Nardone (BofA): what is the risk of losing core customers by pulling promotions in Crocs North America?** Rees did not address customer loss directly; he reframed the decline as chosen, described a bifurcated consumer, and listed product and social initiatives. Verbatim: "As a reminder, some of the lack of growth or the decline in sales are based on some strategic decisions we've made." — Andrew Rees
3. **Rick Patel (Raymond James) then Anna Andreeva (Piper Sandler): is North America DTC accelerating?** Reagan first told Patel "That's right. Yes."; when Andreeva followed up, Rees narrowed it to a Q4-versus-Q3 expectation. Verbatim: "We did not say the DTC accelerated during Q3, right? So, we actually don't comment on trajectory within the quarter. But what we did say is we believe that DTC in North America will be stronger in Q4 than it was in Q3." — Andrew Rees

### Activity metrics (not revenue)

- Shares: 2.4M for $203M at about $83, about 4% of float; year-to-date 4.3M shares for about $400M.
- Inventory $397M, up 8% in dollars; "inventory units were down low-single digits"; turns above 4x.
- HEYDUDE: "the ninth consecutive quarter of ASP increases"; DTC down 1%; wholesale down 39%.
- Crocs: North America DTC down 8%, wholesale down 11%; international DTC up 23%, international wholesale down 7%.
- Price points: "the Classic Clog essentially MSRP $50 and the majority of our HEYDUDE product is between $60 and $70"; Crafted Clog "starting at $60".
- Media: pan-Asian monsoon campaign video "approximately 575 million views across Instagram and YouTube"; TikTok Shop launched in the UK, Germany and Brazil; Crocband has "something like 200,000 four and five-star reviews" on Amazon (Rees's estimate).
- Stores: openings concentrated in European outlets (UK, France); SoHo flagship opened; no counts given.

---

## 8. Q2 2025 call — August 7, 2025 (HEYDUDE impairment; the roughly 29% share-price fall is from the brief, not the transcript)

Source: https://s22.q4cdn.com/133460125/files/doc_financials/2025/q2/Crocs-Inc-Seconf-Quarter-2025-Earnings-Call-Transcript.pdf (retrieved 2026-11-26). Speakers: Andrew Rees, Chief Executive Officer; Susan Healy, Chief Financial Officer.

### Guidance

- Full-year guidance not reinstated.
- Q3 2025: revenue down 9% to 11%; Crocs Brand down mid-single digits (North America down, international up); adjusted operating margin 18% to 19%, including about 170 bps from tariffs. No EPS guide.
- Tariffs: about $40M in H2 2025 and about $90M annualized at then-current rates.
- $50M of cost savings actioned, more being identified. Receipts cut for both brands in H2.
- Q2 capital return: 1.3M shares for $133M at about $102; $105M debt repaid; $1.1B authorization remaining; borrowings $1.4B.

### Management quotes

1. **The impairment.** "This excludes the non-cash impairment charge of $737 million on HEYDUDE's intangible assets. This impairment comes as a result of a longer than expected timeline to stabilize the HEYDUDE brand and return it to growth, due in part to a weaker U.S. consumer and the disproportionate impact of tariffs on HEYDUDE products." — Susan Healy, CFO (prepared remarks)
2. **Outlook tone.** "The current environment in the second half is concerning, and we see that clearly reflected in retail order books." — Andrew Rees, CEO (prepared remarks)
3. **(a) Start of the promotion pullback.** "For the Crocs brand, in addition to adjusting our forward receipts, we pulled back on promotional activity across the direct channels starting in May." — Andrew Rees, CEO (prepared remarks)
4. **(a) Size of the pullback.** "But what I could say is, if you look at Q2, which is down essentially almost 6%, right, for North America for Crocs, if we had, I think, not made that decision, it would have been down slightly." — Andrew Rees, CEO (Q&A)
5. **(a) Shelf space.** "I think in some channels of wholesale distribution, we are losing shelf space relative to other brands, relative to the athletic brands." — Andrew Rees, CEO (Q&A)
6. **(c) International mix.** "Three, we've accelerated our international growth business, which has grown from 38% of Crocs brand sales in 2022 to 52% in the second quarter." — Andrew Rees, CEO (prepared remarks)
7. **(d) HEYDUDE reset.** "This has resulted in us choosing to take back additional aged inventory and ensure more of our partners are reset with our current product lines." — Andrew Rees, CEO (prepared remarks)
8. **(e) Tariff cost.** "The impact from these incremental rates equates to approximately $40 million in the second half of 2025 and approximately $90 million on an annual basis based on our current sourcing mix." — Susan Healy, CFO (prepared remarks)
9. **(e) India sourcing.** "India is a meaningful but not the largest country from which we source exports to the U.S." — Susan Healy, CFO (Q&A)
10. **(g) Buyback record.** "To remind everyone, over the last decade, we have deployed $2.4 billion to buy back approximately 30% of our total shares outstanding." — Andrew Rees, CEO (prepared remarks)
11. **(i) Low-income consumer.** "The low-end consumer is a consumer that we believe is most sensitive to price increases, is most nervous, and in some cases, is not leaving the house." — Andrew Rees, CEO (Q&A)
12. **No full-year guide.** "Therefore, we are not reinstating full year guidance at this time." — Susan Healy, CFO (prepared remarks)

### Three toughest analyst questions

1. **Jonathan Komp (Baird): are you losing order-book share in family channels, and with this much deleverage in Q3 where is profitability being protected?** Rees conceded an athletic-led squeeze on open-to-buy and called Q3 a low point for margin. Verbatim: "I think I'm anticipating that Q3 is a bit of a low spot in our in our EBIT potential." — Andrew Rees
2. **Sam Poser (Williams Trading): is this macro, or is the product simply not innovative enough for a broad consumer?** Rees rejected the product critique and blamed macro plus self-inflicted but deliberate actions. Verbatim: "So I think the macro is a very important factor for our business." — Andrew Rees
3. **Adrienne Yih (Barclays): how much of the down 9% to 11% is proactive, and what about the risk of losing shelf space?** Rees said the guide reflects the order book as it stands with conservative return and cancellation assumptions, and admitted shelf-space loss to athletic brands. Verbatim: "It embeds the order book where it sits today." — Andrew Rees

### Activity metrics (not revenue)

- International was 52% of Crocs Brand sales in Q2 2025 (38% in 2022).
- Aided awareness: HEYDUDE 35%, against "60% plus" for Crocs.
- Sandals: 13% of Crocs Brand mix "last year"; up double digits in H1 2025.
- Shares: 1.3M in Q2 at about $102; 1.9M in H1, "3% of our outstanding shares"; $2.4B over a decade for about 30% of shares.
- Inventory $405M, up 7%; turns above 4x.
- India: brand ambassador's first Instagram post "over 400 million views".
- TikTok Shop: Crocs number one footwear brand in the US; HEYDUDE number two.

---

## 9. Not found in any of the six transcripts

- **Sourcing mix by country** (Vietnam, China, Indonesia, India, Mexico, Cambodia percentages). Only qualitative references: "current sourcing mix", "country mix", India "meaningful but not the largest", and China "slightly more favorable" on tariffs in 2026.
- **The term "IEEPA" spoken by management**, and **the date February 20, 2026**. Management says "the February Supreme Court rulings" (Apr 2026) and "$64 million of tariff refunds" (Oct 2026). The IEEPA label and the Feb 20 date are in the Q3 2026 press release (`data/sec_txt/2026-10-29_8-K_EX_croxq32026-pressrelease.txt`), not on the call.
- **Total IEEPA tariffs paid, and refunds still outstanding.** Only the $64M received in Q3 2026 is stated.
- **Long-term financial targets** (operating margin target, multi-year growth algorithm, revenue target). None given on any call. Nearest items: 2027 colour on the Oct 2026 call and "operating leverage in 2026" on the Oct 2025 call.
- **Jibbitz attach rate; social follower counts; DTC comparable-store sales.** Jibbitz is given only as 8% of 2025 Crocs Brand sales.
- **Clog / sandal / Jibbitz mix for 2026.** Only 2025 mix (74% / 13% / 8%) and the 2026 sandal aim of about $500M.
- **India, Japan and Western Europe growth rates as numbers.** Described as "double-digit" (and Japan "returned to growth" in 2025); only China is quantified (above 30% in Q2 2025, mid-20s % in Q3 2025, 30% for 2025, record quarter in Q2 2026).
- **Definition or list of "tier 1 markets".** Used repeatedly; the closest to a list is China, India, Japan and Western Europe (UK, France, Germany).
- **HEYDUDE operating margin or segment profit.** Only gross margin by brand.
- **Wally / Wendy sales or share of HEYDUDE.**
- **Brand presidents' names** (Crocs brand; HEYDUDE after Aug 2025).
- **Q1 2026 share repurchase amount** and **Q4 2025 adjusted EPS** as spoken figures.
- **TikTok Shop revenue or share of sales.**
- **Name of the marketplace partner** in the North America revenue-recognition change.
- **A company-hosted transcript for Q3 2026** (the q4cdn URL pattern used for earlier quarters returned 404 on 2026-11-26).

## 10. Inconsistencies and cautions spotted while reading

1. **Q2 2026 EPS guide.** Apr 30, 2026 call and press release: $4.15 to $4.35. Jul 30, 2026 call (Reagan, both transcript copies): "$4.15 to $4.30". Use $4.15 to $4.35.
2. **Crocs North America in 2026.** Jul 30, 2026, Rees: "we will not be returning to growth here in 2026". Oct 29, 2026, Rees: "So if you normalize for this business model shift, as Patraic said, we do see North America Crocs growing for the year." Reagan's own wording on both calls is narrower (North America DTC positive for the year excluding the shift). It is unclear whether Rees meant total North America or DTC.
3. **When the marketplace shift was announced.** Oct 29, 2026, Reagan: "we announced this in Q3 on our last call". The announcement was on the Q2 call held Jul 30, 2026 (during Q3).
4. **North America DTC "accelerating" (Oct 30, 2025).** The CFO agreed with an analyst that it was accelerating; the CEO then restricted the claim to a Q4-versus-Q3 expectation.
5. **HEYDUDE awareness.** Feb 12, 2026: Rees says 39%, up 9 points "from one year ago"; Reagan says 30% to 39% "just in the last six months or so". The Aug 7, 2025 call gave 35%.
6. **Tariff refund amount.** The call says $64M. A third-party summary seen in search results (Quartr) says $67M including interest; I did not verify that figure against a transcript.
7. **Operating-margin base.** Earlier 2026 calls guide to expansion from 22.3% (FY2025 actual). The Oct 2026 call says from 22.5%. This is a raise, confirmed by the press release, not a transcription slip.
8. **Q3 2026 wording** rests on a single machine-generated transcript (Motley Fool). Figures in it match the company press release held in `data/sec_txt/` where I checked (revenue growth, $64M refund, EPS ranges, 22.5%).

## 11. Quote verification

A script extracted every double-quoted string in this file and searched for it in the saved transcript for that call, after normalizing whitespace, line-break hyphens and curly quotes. All 202 transcript quotes matched (final run, 2026-11-26). The only quoted string not taken from a transcript is the press-release sentence in table 2a ("up from our previous guidance of expansion from 22.3%"), which is verbatim from `data/sec_txt/2026-10-29_8-K_EX_croxq32026-pressrelease.txt`. Speaker attribution was checked by reading, not by script.
