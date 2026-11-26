"""Write deep-dive.md (Phases 1-7), one-pager.md, qa-prep.md, cheat-sheet.md, checklist.md from data/derived/facts.json.
Number labels: (R) reported, (G) company guidance, (C) consensus, (B) broker, (E) my estimate."""
import json, os
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")); F = json.load(open(os.path.join(ROOT, "data", "derived", "facts.json")))
import pandas as pd
rt = pd.read_csv(os.path.join(ROOT, "data", "derived", "revenue_at_risk.csv")); json.dump(rt.to_dict(orient="records"), open(os.path.join(ROOT, "data", "derived", "rar_rows.json"), "w"))
MO = json.load(open(os.path.join(ROOT, "data", "derived", "model_outputs.json")))
V = F["valuation"]; K = F["key"]; RAR = F["rar"]; S = F["scen"]; B = S["Base"]; RK = F["risk"]; PEER = F["peers"]; Q = F["quarters"]; C = F["cons"]; SN = F["sens"]
def m(x, d=0): return f"${x:,.{d}f}m"
def bn(x, d=2): return f"${x/1000:,.{d}f}bn"
def p(x, d=1, sign=False): return f"{x:+.{d}f}%" if sign else f"{x:.{d}f}%"
def d(x, n=2): return f"${x:,.{n}f}"
def xx(x, n=1): return f"{x:.{n}f}x"
price = F["price"]; pt_bear, pt_base, pt_bull, pt_w = V["pt"]; r_bear, r_base, r_bull, r_w = [v * 100 for v in V["ret"]]; dcf_bear, dcf_base, dcf_bull, dcf_w = V["dcf"]
e27_bear, e27_base, e27_bull, _ = V["eps27"]; e28_bear, e28_base, e28_bull, _ = V["eps28"]
fy = lambda y: F[f"fy{y}"]
def yrow(label, key, fmt, years=(2021, 2022, 2023, 2024, 2025)):
    return "| " + label + " | " + " | ".join(("n/a" if fy(y)[key] is None else fmt(fy(y)[key])) for y in years) + " |"
def qrow(label, key, fmt):
    return "| " + label + " | " + " | ".join(("n/a" if Q[q][key] is None else fmt(Q[q][key])) for q in Q) + " |"
qh = "| | " + " | ".join(q[2:4] + q[4:] for q in Q) + " |\n|---|" + "---|" * len(Q)
sen = lambda k: f"{SN[k][0]:+.2f} ({SN[k][1]*100:+.1f}%)"
pk = lambda t, k: PEER[t][k]
T = {}

# =========================================================== deep-dive.md ===========================================================
T["deep-dive.md"] = f"""# Crocs, Inc. (NASDAQ: CROX) - deep-dive research report

Prepared 2026-11-26 for a fundamental long/short portfolio manager. Price {d(price)} (Nasdaq close {F['asof']}). Fundamentals through Q3 2026 (10-Q filed 2026-10-29).

**Labels on numbers:** (R) reported in company filings or by management, (G) company guidance, (C) consensus, (B) named broker, (E) my estimate. Source IDs [S1]-[S33] refer to `sources.md`.

**Inputs I had to choose because the brief left them blank**

| Input | Choice | Why |
|---|---|---|
| Peers | Deckers (DECK), Birkenstock (BIRK), On Holding (ONON) | The three listed, brand-led, 57-67% gross-margin footwear companies built around icon franchises. DECK (UGG/HOKA) is the closest: two brands, ~23% operating margin, US mid-cap. BIRK sells the competing clog (Boston). ONON is the growth reference. Skechers, the closest on price point, was taken private in 2025. |
| Direction | Decided from the evidence: **LONG**, moderate conviction | See Phase 7. The evidence does not support a short, and it supports a long only on a compounding argument, not a re-rating argument. |
| Holding period | 12-18 months, price target dated December 2027 | Covers the FY2027 guide (Feb 2027), the lapping of the North America accounting shift (Q3 2027) and five earnings reports. |
| Audience | Fundamental long/short PM with a value / cash-return tilt | Framing therefore leads with free cash flow, buybacks, downside and what is priced in. |
| Format | 15-minute pitch plus Q&A, 15 main slides plus appendix | As suggested in the brief. |

---

## Bottom line

- **Recommendation: LONG. Base-case price target {d(pt_base,0)} for December 2027 ({p(r_base,0,True)}). Probability-weighted value {d(pt_w,0)} ({p(r_w,0,True)}). Bear {d(pt_bear,0)} ({p(r_bear,0,True)}), bull {d(pt_bull,0)} ({p(r_bull,0,True)}).** (E)
- **Thesis in one sentence:** Crocs converts about 18% of revenue into free cash flow and is spending almost all of it retiring 8-10% of its shares a year, so EPS compounds in the mid-teens even with revenue growing 4%, yet the stock trades on {xx(F['pe_fy27_cons'])} consensus FY2027 EPS because the market still fears the clog is a fad.
- **Honest caveats.** The stock has doubled in twelve months and rose 34% in the last month. It trades at the sell-side's mean price target ($160.75 (C)). On forward P/E it is in the top quartile of its own five-year range and its 52% median discount to Deckers has closed. The CEO sold $14.1m of stock in the last six months with no 10b5-1 plan disclosed on the Form 4s. The re-rating is done. What is left is the compounding, and the left tail is fat: my full fad-unwind stress points to {d(RAR['val'],0)}.
- **Sizing implication.** A mid-sized long (not a top-five position), added to on pullbacks toward $135-140, with explicit kill criteria.

---

# PHASE 1 - THE DEEP DIVE

## 1. Business model: how Crocs makes money

**In plain English.** Crocs designs and markets cheap-to-make, easy-to-wear casual shoes and has other companies manufacture them. The core product is a moulded foam clog (the Classic Clog, about $50 at retail) made from a proprietary resin called Croslite. It also sells sandals, clip-on charms for the clogs (Jibbitz), and, since February 2022, a second brand of lightweight slip-on loafers (HEYDUDE). It owns no factories. It sells through its own stores and websites (direct-to-consumer, DTC) and to retailers and distributors (wholesale). [S1]

**Customers.** Mass-market consumers of all ages, with volume concentrated at $50-60 price points [S21]. Wholesale customers are family-footwear chains, sporting-goods stores, e-tailers and international distributors. **No customer accounted for 10% or more of revenue in 2023, 2024 or 2025** (R) [S1].

**Revenue split (FY2025 unless stated, all (R))**

| Cut | Split | Source |
|---|---|---|
| By type | 100% product sales recognised at a point in time. No subscription, licence or asset-linked revenue is disclosed. | [S1] |
| Recurring vs one-off | Nothing is contractually recurring. Repeat purchase is behavioural: 129m pairs of Crocs a year at a $25 average selling price. | [S1] |
| By segment | Crocs Brand {m(fy(2025)['crocs_rev'])} (82%); HEYDUDE Brand {m(fy(2025)['hd_rev'])} (18%) | [S1] |
| By product (Crocs Brand) | Clogs 74%, sandals 13% (about $450m), Jibbitz 8%, other 5% (residual, my arithmetic) | [S21] |
| By channel | DTC 52.1%, wholesale 47.9% (DTC was 48.0% in 2023). Digital (own sites, marketplaces, e-tailers) 37.8% | [S1] |
| By geography | United States {m(2260.656)} (55.9%), international {m(1779.518)} (44.0%). No single foreign country is 10%. China is about 8% of sales per management. | [S1] [S21] |
| Crocs Brand by region | North America {m(fy(2025)['crocs_na'])} (51.4%), international {m(fy(2025)['crocs_intl'])} (48.6%). On a trailing-twelve-month basis international is now {p(F['intl_share_ttm'])}. | [S1] [S3] |

**Cost structure.** Gross margin 58.3%. Cost of sales includes $488m of distribution cost. SG&A is 36% of revenue, of which marketing is {m(fy(2025)['marketing'],0)} ({p(fy(2025)['marketing_pct_rev'])}). Capex is about 1.5-2% of revenue. This is why free cash flow is high: {m(F['ttm_fcf'])} in the last twelve months, {p(F['ttm_fcf']/F['ttm_rev']*100)} of revenue. [S1] [S3]

## 2. Segment by segment

### 2a. Crocs Brand (82% of revenue, about 100% of profit)

**What it sells, to whom, how it is paid.** Clogs, sandals and Jibbitz to consumers in more than 85 countries, half through 439 company stores and 23 websites plus marketplaces (DTC 52% of the brand) and half through wholesale and distributors. Paid per pair: cash at the till in DTC, on trade terms in wholesale.

| Crocs Brand (R) | FY21 | FY22 | FY23 | FY24 | FY25 | FY26 (G) | FY27 (E, base) |
|---|---|---|---|---|---|---|---|
| Revenue, $m | {fy(2021)['crocs_rev']:,.0f} | {fy(2022)['crocs_rev']:,.0f} | {fy(2023)['crocs_rev']:,.0f} | {fy(2024)['crocs_rev']:,.0f} | {fy(2025)['crocs_rev']:,.0f} | ~{B['crocs']['FY2026E']:,.0f} (about +4%) | {B['crocs']['FY2027E']:,.0f} ({(B['crocs']['FY2027E']/B['crocs']['FY2026E']-1)*100:+.1f}%) |
| Growth | +66.9% | +14.9% | +13.3% | +8.8% | +1.5% | ~+4% | |
| North America, $m | {fy(2021)['crocs_na']:,.0f} | {fy(2022)['crocs_na']:,.0f} | {fy(2023)['crocs_na']:,.0f} | {fy(2024)['crocs_na']:,.0f} | {fy(2025)['crocs_na']:,.0f} | {B['na']['FY2026E']:,.0f} (E) | {B['na']['FY2027E']:,.0f} |
| International, $m | {fy(2021)['crocs_intl']:,.0f} | {fy(2022)['crocs_intl']:,.0f} | {fy(2023)['crocs_intl']:,.0f} | {fy(2024)['crocs_intl']:,.0f} | {fy(2025)['crocs_intl']:,.0f} | {B['intl']['FY2026E']:,.0f} (E) | {B['intl']['FY2027E']:,.0f} |
| Gross margin | n/a | 56.3% | 60.0% | 61.6% | 61.3% | 62.2% (9M, adjusted) | |
| Segment operating margin | {p(fy(2021)['crocs_op_margin_pct'])} | {p(fy(2022)['crocs_op_margin_pct'])} | {p(fy(2023)['crocs_op_margin_pct'])} | {p(fy(2024)['crocs_op_margin_pct'])} | {p(fy(2025)['crocs_op_margin_pct'])} | 33.8% (9M, ex tariff refunds, my calc) | |
| Pairs sold, m | 103.0 | 115.6 | 119.6 | 127.0 | 128.9 | | |
| Average selling price | $22.27 | $22.72 | $24.92 | $25.52 | $25.40 | | |

Consensus forecasts by segment: **not found** in any free source. FY26 is company guidance of 2026-10-29; FY27 is my base case. Management's 2027 colour is that Crocs will grow "roughly about what we grew at overall this year" [S21].

- **Growth drivers.** (1) International: +11% in 2025 on +19% in 2024; China +30% on +64%. Management says market share in China, India, Japan, Germany and France is about one-third of the share in established markets [S21]. International DTC grew 24% in Q3 2026 (R). (2) Sandals: 13% of mix, growing double digits, about $0.5bn in 2026 against a market management sizes at $30bn [S21]. (3) Social commerce: number one footwear brand on TikTok Shop in the US, UK, Japan and Malaysia (activity metric, [S21]).
- **Why margins moved.** Segment margin fell from 37.2% (FY21) to 33.4% (FY25). Gross margin is higher than in FY22-23, so the loss is all SG&A: segment SG&A rose from $728m (FY23) to $927m (FY25), +27%, while revenue rose 10%. That is DTC mix (stores and marketplace fees are opex), talent and marketing. In FY25 tariffs took 130 bps off group gross margin. In Q3 2026 lower duties added 130 bps, but "unfavourable product mix in the Crocs Brand" took off 130 bps (R) [S2]: the newer products carry lower margins than the Classic Clog. Roughly 65% of SG&A is fixed in my estimate, so operating leverage cuts both ways.
- **Competitive position.** Category creator and dominant brand in moulded clogs. No reliable share figure was found (a single unverified source says 70-80% of the clog category; I do not rely on it).
- **Segment-specific risks.** North America is shrinking (-6.8% in FY25, -2.1% in Q3 2026). Teen mindshare is falling (Piper Sandler rank No. 6 in 2023 to No. 10 in Fall 2026 [S25]). The silhouette has weak legal protection [S23]. Two contract manufacturers make 73% of the brand's volume and 45% of production is in Vietnam [S1].
- **Charts:** `charts/04_crocs_brand.png`, `charts/05_crocs_units_asp.png`.

### 2b. HEYDUDE Brand (18% of revenue, low-teens margin)

**What it sells, to whom, how it is paid.** Lightweight slip-on loafers (Wally for men, Wendy for women), at an average selling price near $32, almost all in the United States, to a heartland, value-oriented consumer. 55% DTC (including 75 outlet stores and a large Amazon business), 45% wholesale.

| HEYDUDE (R) | FY22 (from 17-Feb) | FY23 | FY24 | FY25 | FY26 (G) | FY27 (E, base) |
|---|---|---|---|---|---|---|
| Revenue, $m | {fy(2022)['hd_rev']:,.0f} | {fy(2023)['hd_rev']:,.0f} | {fy(2024)['hd_rev']:,.0f} | {fy(2025)['hd_rev']:,.0f} | ~{B['hd']['FY2026E']:,.0f} (about flat) | {B['hd']['FY2027E']:,.0f} (+4%) |
| Growth | n/a | +6.0% | -13.2% | -13.3% | ~0% | |
| Wholesale, $m | 574 | 567 | 456 | 336 | | |
| DTC, $m | 322 | 382 | 368 | 379 | | |
| Gross margin | 40.8% | 44.0% | 47.7% | 44.8% | 44.6% (9M, adjusted) | |
| Segment operating margin ex-impairment | {p(fy(2022)['hd_op_margin_ex_impair_pct'])} | {p(fy(2023)['hd_op_margin_ex_impair_pct'])} | {p(fy(2024)['hd_op_margin_ex_impair_pct'])} | {p(fy(2025)['hd_op_margin_ex_impair_pct'])} | 12.3% (9M, ex refunds and impairment, my calc) | |
| Pairs sold, m | 30.5 | 33.0 | 27.0 | 22.5 | | |

- **What happened.** Crocs paid $2.5bn in 2022. Revenue peaked at $949m in 2023 after wholesale accounts were loaded with inventory, then fell 25% in two years as the channel destocked and the brand lost heat. Wholesale revenue fell 41% from 2023 to 2025. Crocs wrote off $737m in Q2 2025. [S1] [S29] [S30]
- **Growth drivers now.** Wholesale returned to growth in Q3 2026 (+14.0%) against a quarter in which Crocs deliberately pulled product back the year before; management concedes "we are up against a weak compare" and puts the sustainable rate at low- to mid-single digits [S21]. Gross margin recovered 350 bps to 45.8% in Q3.
- **Why margins moved.** Fixed-cost deleverage on a 25% revenue fall, a jump in SG&A as Crocs built a retail fleet (75 stores) and a team, plus tariffs that hit HEYDUDE harder because production was still mostly in China until 2025.
- **Competitive position.** A niche it popularised, with weak barriers. It dropped off the Piper Sandler teen top-ten list in 2026 [S25].
- **Segment-specific risks.** Fourth brand leader in four years. Amazon dependence. A securities class action alleges the 2022-24 growth was channel stuffing [S22].
- **Chart:** `charts/06_heydude.png`.

### 2c. Enterprise corporate

Unallocated corporate cost was {m(293.309,0)} in FY25 (7.3% of revenue), up from $178m in FY21. [S1]

## 3. What drives the share price

**Company-specific drivers (in order of importance)**

1. Crocs Brand North America trend, because it is the read on whether the clog is a fad.
2. International growth rate.
3. Adjusted operating margin (the market trades this stock on EPS).
4. HEYDUDE revenue direction.
5. Buyback pace.
6. Guidance changes. Four of the last eight earnings days moved the stock 19% or more.

**Macro drivers:** US low- and middle-income consumer spending, US tariff rates on Asian footwear, the dollar (44% of revenue is international), oil (Croslite is a petroleum-derived resin and freight is oil-linked), and interest rates (about 47% of debt is floating).

**Quantified sensitivities on FY2027E EPS (base {d(e27_base)}; all (E), from `model.xlsx` sheet Sens)**

| Driver | Change | EPS impact | Assumption behind it |
|---|---|---|---|
| Group revenue | +1% | {sen('+1% group revenue')} | 50% incremental EBIT margin |
| Crocs North America revenue | +1% | {sen('+1% Crocs North America revenue')} | same |
| Crocs International revenue | +1% | {sen('+1% Crocs International revenue')} | same |
| Adjusted operating margin | +100 bps | {sen('+100 bps adjusted EBIT margin')} | mechanical |
| US tariff rate on imports | +1 point | {sen('+1 pt US tariff rate on imports')} | $80m annualised cost for the 19-20 point 2025 layer (R) [S21] |
| US dollar | +1% vs all currencies | {sen('+1% USD vs all currencies')} | 35% flow-through after local costs and hedges |
| Interest rates | +100 bps | {sen('+100 bps interest rates')} | $5.6m per 1% (R) [S1] |
| Share repurchases | +$100m | {sen('+$100m share repurchases (full-year effect)')} | at $175 |
| No buybacks at all in FY27 | | {sen('No buybacks at all in FY27 (cash retained)')} | |
| Oil / resin cost | | not found | company gives no sensitivity |

The stock's price sensitivity is larger than its earnings sensitivity because the multiple moves with the fad narrative: forward P/E has ranged from {xx(RK['CROX_pe_ntm_5y_stats']['min'])} to {xx(RK['CROX_pe_ntm_5y_stats']['max'])} in five years.

## 4. Moat

**Top three competitors.** Deckers (UGG Tasman slippers and clogs; HOKA recovery slides), Birkenstock (Boston clog, Arizona sandal), Skechers (Foamies moulded clogs; private since 2025). Below them sit unbranded lookalikes on Amazon, Temu and Shein.

**Market structure.** Casual footwear is fragmented. The moulded-clog niche is close to a branded monopoly surrounded by cheap copies. No audited share data was found.

**Does Crocs have a durable edge rivals cannot copy?**

| Source of edge | Verdict | Evidence |
|---|---|---|
| Patent | No | The original clog patents have expired (per litigants' filings; exact dates not found). In January 2026 the Federal Circuit left standing an ITC finding that Hobby Lobby, Orly and Amoji did not infringe the 3D clog trademarks [S23]. Crocs conceded in court that calling Croslite "patented" was false [S24]. |
| Switching cost | No | A $50 shoe. |
| Network effect | Weak | Jibbitz and collaborations create some collector behaviour (8% of brand revenue). |
| Cost structure | **Yes, this is the real moat** | A one-piece injection-moulded shoe has few parts and little labour. Crocs Brand gross margin is 61% at a $25 average wholesale-plus-retail price, which no stitched-shoe peer matches at that price. Scale of 129m pairs a year funds $394m of marketing. |
| Brand | Yes, but cyclical | 2008-09 showed the brand can lose a quarter of its sales in two years [S9]. |

**Pricing power.** Mixed evidence. Average selling price rose from $22.27 (FY21) to $25.52 (FY24) with units also rising, without heavy capex. But in FY25 price slipped 0.5% "driven mostly by increased discounting" (R) [S1], and when Crocs cut promotions from May 2025, North America revenue fell 7%. The price increase held outside the US. I read this as real pricing power internationally and limited pricing power in a saturated US.

**TAM and runway.** The US is saturated: Crocs Brand North America is $1.7bn and shrinking. The runway is international ($1.7bn, growing 9-12%), where share in the five largest growth markets is one-third of established-market levels. Closing half that gap in those markets would be worth several hundred million dollars of revenue; I cannot size it precisely because Crocs does not disclose revenue by country. Management's stated TAM grew from $160bn (2023 deck) to "$280bn+" (2025-26 decks) while revenue was flat, so I give the TAM claims no weight [S31].

## 5. Structural vs cyclical

| Tailwind | Structural or cyclical | Hard data | What happens when the cycle turns |
|---|---|---|---|
| International penetration | Structural | International share of the brand: 33% (FY21), 38%, 41%, 44%, 49% (FY25), {p(F['intl_share_ttm'],0)} TTM. Store count abroad 206 to 239 in 2025. Share one-third of mature markets. | Slows but does not reverse; base case fades growth from 9% to 5% by 2031. China (8% of sales, +30%) is the most cyclical piece. |
| Casualisation and comfort | Structural but mature | Units 103m (FY21) to 129m (FY25). | Already slowing: units +1.5% in FY25. |
| The clog fashion cycle | **Cyclical** | 2007-09 revenue -24%. North America -7% in FY25. Teen rank No. 6 to No. 10. | This is the bear case: North America falls another 8% a year for two years (base assumes flat). |
| Tariff relief | Cyclical / political | IEEPA layer of 18-20% replaced by 10-12.5% Section 301 duties in July 2026 (R) [S2] [S27]. Lower duties added 130 bps to Q3 gross margin. | Tariffs could be raised again. Each point is about $4m, {d(abs(SN['+1 pt US tariff rate on imports'][0]))} of EPS. |
| Easy comparisons | Cyclical, expires mid-2027 | Q4 2025 revenue -3.2%, HEYDUDE wholesale -40%. Q4 2026 guide +7-9%. | Growth rates fade through 2027; management has already said HEYDUDE settles at low- to mid-single digits. |
| Buybacks | Structural while free cash flow holds | $3bn repurchased and share count down 37% over a decade (R) [S21]. $1.7bn authorised. | Buybacks shrink with free cash flow in a downturn, as in 2022 when they stopped to pay down HEYDUDE debt. |

There is no backlog, pipeline or maturity schedule in this business. The closest thing to forward visibility is the wholesale order book, which the company does not disclose.

## 6. Catalysts (next 12 months)

See Phase 6 for the full table. The two that matter most: the first FY2027 guide around 11 February 2027, and Q3 2027 when the North America accounting distortion is lapped.

## 7. Asymmetry

- **Valuation floor.** Not low any more. At the 2025-26 lows the stock traded at 6.0-6.5x earnings. Today it is on {xx(F['pe_fy27_cons'])}. A return to the five-year 25th-percentile multiple of {xx(RK['CROX_pe_ntm_5y_stats']['p25'])} on flat earnings is about $100-110.
- **Growth ceiling.** Modest: revenue growth of 3-5%. The ceiling comes from capital return, not growth: free-cash-flow yield of {p(F['fcf_yield'])} against a cost of equity of 11%.
- **Verdict.** This is not a low-floor, high-ceiling set-up. It is a high-carry set-up: you are paid about 10% a year in buybacks to wait, with a fat left tail if the brand cracks. Base-case upside {p(r_base,0,True)} against bear-case downside {p(r_bear,0,True)} is a ratio of {K['Upside/downside ratio, base vs bear (x)']:.2f}x. Probability-weighted it is {K['Upside/downside ratio, probability-weighted (x)']:.1f}x.

## 8. Corporate actions in the last three years

| Date | Action | Value | Rationale | Effect |
|---|---|---|---|---|
| Nov 2023 - Nov 2026 | Acquisitions | **None** | | |
| Nov 2023 - Nov 2026 | Disposals / spin-offs | **None** | | |
| 2025 | Share repurchases | $577m, 6.5m shares at $88.68 (R) [S6] | Return of free cash flow | Share count -10% |
| 9M 2026 | Share repurchases | $501m, 4.4m shares (R) [S2] | Same | Diluted shares 48.0m in Q3-26 vs 54.0m a year earlier |
| Feb 2025; Jul 2026 | Authorisation increases | +$1.0bn; raised to about $2.0bn (R) [S2] | | $1.7bn remaining = {1700/F['mcap']*100:.0f}% of market cap |
| Q2 2025 | HEYDUDE impairment | $737m non-cash: $430m trademark, $307m goodwill (R) [S30] | Longer path to stabilisation, tariffs | GAAP loss in FY25; no cash effect |
| 2026 | Takeback of Malaysian distributor | $4.4m cost (R) [S3] | Convert distributor market to direct | Immaterial |
| For context: Dec 2021 / Feb 2022 | Acquisition of HEYDUDE | $2.5bn headline: $2.05bn cash + $450m stock (2,852,280 shares); recorded at about $2.3bn at close; funded by a $2.0bn Term Loan B (R) [S29] | Second brand, casual loafers | Revenue mix: 25% of group at peak, 17% now. Margin: dilutive (HEYDUDE 9.5% vs Crocs 33.4%). Rating: forward P/E fell from about 15x to 8x and has not recovered; net debt/EBITDA went 0.8x to 2.1x and is back to {xx(F['nd_ebitda'])}. Term loan now $500m. |

## 9. Management, capital allocation and shareholders

- **CEO Andrew Rees** (59): President since 2014, CEO since 2017. He led the 2017-21 turnaround (revenue $1.0bn to $2.3bn, operating margin 2% to 30%) and also the HEYDUDE deal. Beneficial ownership 1,016,929 shares, 2.0% (R) [S10].
- **CFO Patraic Reagan** since 22 September 2025 (ex-SharkNinja CFO, 14 years at Nike). He is the third CFO in 16 months: Anne Mehlman moved to run the Crocs Brand in June 2024, and Susan Healy resigned "effective immediately" on 28 August 2025, three weeks after the Q2 2025 guide-down. Reason not found. [S10]
- **HEYDUDE** is on its fourth leader since acquisition (Blackshaw, Reilly, Rees as interim, Rupert Campbell from November 2025).
- **Incentives.** Long-term awards are 67% performance units, tied to adjusted EBIT margin and to revenue with a relative-TSR modifier. The 2023-25 revenue PSU paid zero. Annual bonus is 40% on adjusted free cash flow. This is a reasonable design that rewards cash and margin. 22% of votes went against the 2026 equity plan. [S10]
- **Capital allocation record.** Good on buybacks: 6.5m shares in 2025 at $88.68 and about 4.4m in the first nine months of 2026 at about $115, both below today's price. Bad on M&A: one large deal, 30% written off.
- **Top holders** (13F at 30-Sep-2026 unless stated): BlackRock 4.52m shares; Vanguard entities about 4.2m (two filers); FMR 3.34m (13G: 3.51m, 7.1% at 30-Jun-2026); WIT Partners (the HEYDUDE founder's vehicle) 2.85m, 5.3%, unchanged since the deal; American Century 2.07m (+41% in the quarter); LSV 1.83m; State Street 1.61m. [S12] [S15]
- **Activists or concentrated funds.** No 13D and no activist found. Himalaya Capital (Li Lu) reportedly opened a position in Q4 2025 (secondary source, not verified against EDGAR) [S33].
- **Insiders** own 3.1% as a group (R) [S10]. In the last twelve months insiders sold ${F['insider']['sales_12m_usd']/1e6:.1f}m in the open market and bought ${F['insider']['buys_12m_usd']/1e6:.1f}m. **None of the {F['insider']['n_sales']} sale transactions is marked as made under a Rule 10b5-1 plan** on the Form 4 (checkbox blank, no footnote). The CEO sold {F['insider']['ceo_sales_sh']:,.0f} shares for ${F['insider']['ceo_sales_usd']/1e6:.1f}m between June and November 2026 and still holds {F['insider']['ceo_shares_after']:,} directly and in trust. [S11]

## 10. Financial quality

**Five years (R; ratios are my calculation)**

| | FY21 | FY22 | FY23 | FY24 | FY25 |
|---|---|---|---|---|---|
{yrow('Revenue, $m', 'revenue', lambda v: f'{v:,.0f}')}
{yrow('Growth', 'rev_growth_pct', lambda v: f'{v:+.1f}%')}
{yrow('Gross margin (GAAP)', 'gm_pct', lambda v: f'{v:.1f}%')}
{yrow('Adjusted operating margin', 'adj_op_margin_pct', lambda v: f'{v:.1f}%')}
{yrow('GAAP operating margin', 'op_margin_pct', lambda v: f'{v:.1f}%')}
{yrow('Adjusted EPS', 'adj_eps', lambda v: f'${v:.2f}')}
{yrow('GAAP EPS', 'eps_gaap', lambda v: f'${v:.2f}')}
{yrow('Free cash flow, $m', 'fcf', lambda v: f'{v:,.0f}')}
{yrow('FCF margin', 'fcf_margin_pct', lambda v: f'{v:.1f}%')}
{yrow('FCF / adjusted net income', 'fcf_conv_adj_ni_pct', lambda v: f'{v:.0f}%')}
{yrow('Net debt, $m', 'net_debt', lambda v: f'{v:,.0f}')}
{yrow('Net debt / adjusted EBITDA', 'net_debt_to_adj_ebitda', lambda v: f'{v:.1f}x')}
{yrow('Diluted shares, m', 'sh_diluted', lambda v: f'{v:.1f}')}
{yrow('Stock comp, $m', 'sbc', lambda v: f'{v:.0f}')}
{yrow('Stock comp % revenue', 'sbc_pct_rev', lambda v: f'{v:.1f}%')}
{yrow('ROIC (adj. EBIT after 18% tax / avg. invested capital)', 'roic_pct', lambda v: f'{v:.0f}%')}

**Last eight quarters (R)**

{qh}
{qrow('Revenue, $m', 'revenue', lambda v: f'{v:,.0f}')}
{qrow('Revenue growth y/y', 'revenue_yoy_pct', lambda v: f'{v:+.1f}%')}
{qrow('Adjusted gross margin', 'adj_gm_pct', lambda v: f'{v:.1f}%')}
{qrow('Adjusted operating margin', 'adj_op_margin_pct', lambda v: f'{v:.1f}%')}
{qrow('GAAP operating margin', 'op_margin_pct', lambda v: f'{v:.1f}%')}
{qrow('Adjusted EPS', 'adj_eps', lambda v: f'${v:.2f}')}
{qrow('GAAP EPS', 'eps_diluted', lambda v: f'${v:.2f}')}
{qrow('Free cash flow, $m', 'fcf_calc', lambda v: f'{v:,.0f}')}
{qrow('Net debt, $m', 'net_debt', lambda v: f'{v:,.0f}')}
{qrow('Diluted shares, m', 'sh_diluted_m', lambda v: f'{v:.1f}')}
{qrow('Stock comp, $m', 'sbc_q', lambda v: f'{v:.1f}')}

Trailing twelve months to September 2026: revenue {m(F['ttm_rev'])}, adjusted EBITDA {m(F['ttm_ebitda'])}, free cash flow {m(F['ttm_fcf'])} ({F['ttm_fcf_conv']:.0f}% of adjusted net income), stock comp {m(F['ttm_sbc'])} (1.1% of revenue), net debt/EBITDA {xx(F['nd_ebitda'])}.

**Quality observations**

- Cash conversion is genuine: free cash flow has exceeded adjusted net income in three of the last four years.
- Dilution is negative: stock comp is about 1% of revenue and the diluted share count has fallen about 24% since FY21.
- ROIC fell from 46% (FY22) to 27% (FY25) because HEYDUDE added $2.3bn of capital that earns little.
- The non-GAAP tax rate of 18% is five points below the GAAP rate because Crocs excludes the amortisation of deferred tax assets created by moving intellectual property between its own subsidiaries. That adds about ${F['ip_tax_eps_fy26e']:.2f} to FY2026 adjusted EPS (6%). Unrecognised tax benefits tied to those transfers stood at $637m at end-2025, up from $219m at the start of 2023 (R) [S1].

## 11. The compounding algorithm

**Revenue growth + margin expansion + buybacks = EPS growth.**

| | Revenue growth | Adj. operating margin change | Diluted share count change | Adjusted EPS growth |
|---|---|---|---|---|
| FY22 (R) | +53.7% (HEYDUDE) | -240 bps | -2.7% | +31.3% |
| FY23 (R) | +11.5% | 0 bps | -0.1% | +10.2% |
| FY24 (R) | +3.5% | -210 bps | -3.4% | +9.5% |
| FY25 (R) | -1.5% | -330 bps | -9.4% | -5.0% |
| FY26 (G/E) | about +3% | about +30 bps | about -10% | about +16% |
| FY27 (E, base) | {B['g']['FY2027E']*100:+.1f}% | +20 bps | {(B['sh_avg']['FY2027E']/B['sh_avg']['FY2026E']-1)*100:+.1f}% | {B['epsg']['FY2027E']*100:+.1f}% |
| FY28 (E, base) | {B['g']['FY2028E']*100:+.1f}% | +20 bps | {(B['sh_avg']['FY2028E']/B['sh_avg']['FY2027E']-1)*100:+.1f}% | {B['epsg']['FY2028E']*100:+.1f}% |

**Test against the record.** From FY23 to FY25 the algorithm failed: margin fell 540 bps and offset the buybacks, so EPS went sideways ($12.03 to $12.51). It works only when margin stops falling. In FY26 the margin stabilised and EPS growth is almost entirely share count: adjusted operating income grows about 5% ({m(B['ebit']['FY2026E'],0)} vs {m(fy(2025)['adj_op_income'],0)}) while EPS grows 16%. That is the honest description of the story: a levered equity shrink on a flat-to-slowly-growing earnings base.

**Every guidance change in the last four quarters (R) [S3]-[S6]**

| Line | 12-Feb-26 | 30-Apr-26 | 30-Jul-26 | 29-Oct-26 |
|---|---|---|---|---|
| Group revenue | -1% to slightly up | -1% to +1% | +1% to +2% | about +3% |
| Crocs Brand | flat to +2% | flat to +2% | +2% to +3% | about +4% |
| HEYDUDE | -9% to -7% | -7% to -5% | -4% to -2% | about flat |
| Adj. operating margin | modestly above 22.3% | same | same | modestly above 22.5% |
| Adjusted EPS | $12.88-13.35 | $13.20-13.75 | $13.70-14.00 | $14.45-14.65 |
| Capex | $70-80m | same | same | same |

Three raises in a row, on both brands. The last cut was 7 August 2025 (Q3 2025 revenue guided down 9-11%), and full-year 2025 guidance was withdrawn on 8 May 2025. Crocs International was guided at about +10% in February and trimmed to "high single digits to approaching 10%" in April because of Middle East distributors [S21].

---

# PHASE 2 - THE PEER COMPARISON

Vendor data: StockAnalysis.com at the 2026-11-25 close, one methodology for all four companies [S17]. Macrotrends was not accessible [S18]. BIRK and ONON figures are converted to US dollars by the vendor.

| | CROX | DECK | BIRK | ONON |
|---|---|---|---|---|
| Market cap, $bn | {pk('CROX','mkt_cap_usd_m')/1000:.1f} | {pk('DECK','mkt_cap_usd_m')/1000:.1f} | {pk('BIRK','mkt_cap_usd_m')/1000:.1f} | {pk('ONON','mkt_cap_usd_m')/1000:.1f} |
| P/S (TTM) | {pk('CROX','ps_ttm'):.2f} | {pk('DECK','ps_ttm'):.2f} | {pk('BIRK','ps_ttm'):.2f} | {pk('ONON','ps_ttm'):.2f} |
| P/S (forward) | {pk('CROX','ps_fwd'):.2f} | {pk('DECK','ps_fwd'):.2f} | {pk('BIRK','ps_fwd'):.2f} | {pk('ONON','ps_fwd'):.2f} |
| P/FCF | {pk('CROX','p_fcf'):.1f} | {pk('DECK','p_fcf'):.1f} | {pk('BIRK','p_fcf'):.1f} | {pk('ONON','p_fcf'):.1f} |
| EV/EBITDA | {pk('CROX','ev_ebitda'):.1f} | {pk('DECK','ev_ebitda'):.1f} | {pk('BIRK','ev_ebitda'):.1f} | {pk('ONON','ev_ebitda'):.1f} |
| EV/Sales | {pk('CROX','ev_sales'):.2f} | {pk('DECK','ev_sales'):.2f} | {pk('BIRK','ev_sales'):.2f} | {pk('ONON','ev_sales'):.2f} |
| Forward P/E | {pk('CROX','pe_fwd'):.1f} | {pk('DECK','pe_fwd'):.1f} | {pk('BIRK','pe_fwd'):.1f} | {pk('ONON','pe_fwd'):.1f} |
| Gross margin | {pk('CROX','gross_margin_pct'):.1f}% | {pk('DECK','gross_margin_pct'):.1f}% | {pk('BIRK','gross_margin_pct'):.1f}% | {pk('ONON','gross_margin_pct'):.1f}% |
| Operating margin | {pk('CROX','op_margin_pct'):.1f}% | {pk('DECK','op_margin_pct'):.1f}% | {pk('BIRK','op_margin_pct'):.1f}% | {pk('ONON','op_margin_pct'):.1f}% |
| FCF margin | {pk('CROX','fcf_margin_pct'):.1f}% | {pk('DECK','fcf_margin_pct'):.1f}% | {pk('BIRK','fcf_margin_pct'):.1f}% | {pk('ONON','fcf_margin_pct'):.1f}% |
| Revenue growth, TTM y/y | {pk('CROX','rev_growth_ttm_pct'):.1f}% | {pk('DECK','rev_growth_ttm_pct'):.1f}% | {pk('BIRK','rev_growth_ttm_pct'):.1f}% | {pk('ONON','rev_growth_ttm_pct'):.1f}% |
| **Value/Growth score** (P/S TTM / growth %) | **{pk('CROX','value_growth_score_ttm'):.2f}** | {pk('DECK','value_growth_score_ttm'):.2f} | {pk('BIRK','value_growth_score_ttm'):.2f} | **{pk('ONON','value_growth_score_ttm'):.2f}** |
| Same, on next-year consensus growth | {pk('CROX','value_growth_score_fwd'):.2f} | {pk('DECK','value_growth_score_fwd'):.2f} | {pk('BIRK','value_growth_score_fwd'):.2f} | {pk('ONON','value_growth_score_fwd'):.2f} |
| Net debt / EBITDA (incl. leases) | {pk('CROX','net_debt_to_ebitda'):.1f}x | net cash | {pk('BIRK','net_debt_to_ebitda'):.1f}x | net cash |
| ROIC | {pk('CROX','roic_pct'):.0f}% | {pk('DECK','roic_pct'):.0f}% | {pk('BIRK','roic_pct'):.0f}% | {pk('ONON','roic_pct'):.0f}% |
| Buyback yield | {pk('CROX','buyback_yield_pct'):.1f}% | {pk('DECK','buyback_yield_pct'):.1f}% | {pk('BIRK','buyback_yield_pct'):.1f}% | {pk('ONON','buyback_yield_pct'):.1f}% |
| 52-week share price change | {pk('CROX','chg_52w_pct'):+.0f}% | {pk('DECK','chg_52w_pct'):+.0f}% | {pk('BIRK','chg_52w_pct'):+.0f}% | {pk('ONON','chg_52w_pct'):+.0f}% |

**Reading the table**

- **On the Value/Growth score Crocs is the worst of the four, not the best.** It has the lowest P/S, but almost no growth: {pk('CROX','value_growth_score_ttm'):.2f} against {pk('ONON','value_growth_score_ttm'):.2f} for On. Even on next year's consensus growth it ranks last. Anyone pitching Crocs as "growth at a discount" is wrong. It is cash at a discount.
- **Against Deckers, the closest peer, Crocs is no longer cheap.** Forward P/E {pk('CROX','pe_fwd'):.1f}x vs {pk('DECK','pe_fwd'):.1f}x. EV/EBITDA {pk('CROX','ev_ebitda'):.1f}x vs {pk('DECK','ev_ebitda'):.1f}x, a 20% premium. Deckers grows faster ({pk('DECK','rev_growth_ttm_pct'):.1f}% vs {pk('CROX','rev_growth_ttm_pct'):.1f}%), has net cash and earns a far higher ROIC.
- **History of the gap.** On my forward P/E series (price over next-four-quarter EPS; `charts/08_pe_history.png`), Crocs traded at a median {abs(RK['CROX_vs_DECK_ntm_prem_pct_5y_stats']['median']):.0f}% discount to Deckers over five years and as wide as {abs(RK['CROX_vs_DECK_ntm_prem_pct_5y_stats']['min']):.0f}%. Today the discount is {abs((RK['crox_pe_ntm_now']/RK['deck_pe_ntm_now']-1)*100):.0f}%. It closed from both ends: Deckers de-rated from 32x to 11x as HOKA and UGG slowed, and Crocs re-rated from 6x to 10x.
- **Is the remaining parity justified by mix?** A small discount for Crocs would be. Deckers has two growing brands and no debt; Crocs has one growing region, one shrinking region and a damaged second brand. What Crocs has that Deckers lacks is a 10% free-cash-flow yield directed at buybacks.
- **How does the gap move from here?** The relative trade is finished. I would not pair long CROX / short DECK. If a gap reopens it is more likely by Crocs falling than Deckers rising, because Crocs is the more volatile, more narrative-driven stock. The long case rests on absolute value, not relative value.
- **Against its own history and the index.** Forward P/E {xx(RK['crox_pe_ntm_now'])} vs a five-year mean of {xx(RK['CROX_pe_ntm_5y_stats']['mean'])} and median of {xx(RK['CROX_pe_ntm_5y_stats']['median'])}: the {RK['CROX_pe_ntm_5y_stats']['pctile_now']:.0f}th percentile. Against the S&P 500 at 18.3x (10-year average 19.1x) [S20], Crocs is at a 45% discount (`charts/09_pe_vs_history_index.png`).

---

# PHASE 3 - THE BEAR CASE

Written as a short-seller would. Three red flags ranked by severity, then the checklist.

## Red flag 1 (most severe): the core franchise is still shrinking in its largest market and the lead indicators are getting worse

- Crocs Brand North America revenue: -6.8% in FY25, -6.1% in Q1 2026, +0.4% in Q2, -2.1% in Q3. North America wholesale -4.9% in Q3 2026, the quarter the stock rose 25%. (R) [S3] [S5]
- Piper Sandler's teen survey has Crocs falling from No. 6 (2023) to No. 10 with a 1% share (Fall 2026), and off the girls' top ten. Birkenstock is No. 4 with 5%. HEYDUDE is off the list. (B: Piper Sandler) [S25]
- Clogs are 74% of the brand. The 3D trademark on the clog shape failed against active importers at the ITC and on appeal in January 2026 [S23].
- When Crocs cut discounting in May 2025, the CEO said the pullback "has had the greatest impact on our Classic Clog business" (Q3 2025 call) [S21]. Demand at full price is lower than reported sales implied.
- For a year from Q3 2026 an accounting change (one marketplace partner moving from DTC to wholesale) will cut reported North America DTC growth by 700-800 bps a quarter, so nobody outside the company can see the clean trend until Q3 2027.
- The precedent: Crocs' revenue fell 24% from 2007 to 2009 and gross margin fell from 58.7% to 32.4% in 2008 [S9]. HEYDUDE fell 25% from 2023 to 2025.
- **Bull's rebuttal.** The decline was chosen: fewer promotions and tighter sell-in, which raised gross profit dollars in North America (CEO, Q3 2025). North America DTC excluding the shift grew about 2% in Q3 2026 and 5% in Q1 and Q2. The region is now less than half of the brand. Units are still growing (129m pairs in FY25, +1.5%). Circana listed clogs among the styles that grew in H1 2026 [S28].
- **Data that would settle it.** Crocs Brand North America DTC growth excluding the marketplace shift for Q4 2026 and Q1 2027 (management now discloses it); the Fall 2027 Piper survey; wholesale sell-through at Famous Footwear, DSW and Journeys.

## Red flag 2: earnings quality. EPS growth is share count and adjustments; the operating business earns less than it did in 2023

- Adjusted operating margin: 27.7% (FY23), 25.6%, 22.3% (FY25), about 22.6% (FY26 guide). Adjusted operating income is {m(B['ebit']['FY2026E'],0)} in FY26E against {m(fy(2023)['adj_op_income'],0)} in FY23, down {(1-B['ebit']['FY2026E']/fy(2023)['adj_op_income'])*100:.0f}%, while adjusted EPS is up {(B['eps']['FY2026E']/fy(2023)['adj_eps']-1)*100:.0f}% over the same period. All of the EPS growth since 2023 is buybacks and lower interest.
- Margin compression in three of the last four quarters: adjusted gross margin {F['gm_yoy_bps']['2025Q4']:+.0f} / {F['gm_yoy_bps']['2026Q1']:+.0f} / {F['gm_yoy_bps']['2026Q2']:+.0f} / {F['gm_yoy_bps']['2026Q3']:+.0f} bps y/y (Q4-25 to Q3-26); adjusted operating margin {F['opm_yoy_bps']['2025Q4']:+.0f} / {F['opm_yoy_bps']['2026Q1']:+.0f} / {F['opm_yoy_bps']['2026Q2']:+.0f} / {F['opm_yoy_bps']['2026Q3']:+.0f} bps. (R)
- The Q3 2026 improvement had help: lower duties +130 bps, while product mix was -130 bps. Q4's guided +7-9% growth laps a quarter in which Crocs cut shipments.
- Non-GAAP tax rate of 18% vs GAAP 23%. The gap is worth about ${F['ip_tax_eps_fy26e']:.2f} of FY26 EPS. Cash taxes paid in 2025 were $185m. Unrecognised tax benefits are $637m (R) [S1].
- GAAP vs non-GAAP: cumulative FY2025 gap of $14.01 per share (GAAP -$1.50 vs adjusted $12.51) because of the $737m impairment. In Q3 2026 the gap reversed: GAAP EPS $4.52 vs adjusted $3.69 because of $64m of tariff refunds. Screens using trailing GAAP P/E (11.8x) are flattered.
- **Bull's rebuttal.** The company excluded the tariff refund from adjusted EPS, which is conservative. Free cash flow ({m(F['ttm_fcf'])}) exceeds adjusted net income, so the earnings are cash. The margin fell because of tariffs (now easing), a deliberate promotion cut and DTC investment, and it turned up in Q3 2026. Buying back 10% of the company a year at 7-10x earnings is value creation, not engineering.
- **Data that would settle it.** Adjusted operating income in dollars (not EPS) growing in FY27; gross margin holding once duty comparisons normalise in H2 2027; the cash tax rate.

## Red flag 3: insiders are selling into the rally, and management turnover is high

- Open-market insider sales in the last twelve months: ${F['insider']['sales_12m_usd']/1e6:.1f}m. Purchases: ${F['insider']['buys_12m_usd']/1e6:.1f}m. None of the sales is flagged as a 10b5-1 trade. (R) [S11]
- CEO Andrew Rees sold {F['insider']['ceo_sales_sh']:,.0f} shares for ${F['insider']['ceo_sales_usd']/1e6:.1f}m in June, August and November 2026, at $117-154. In the eight trading days after the Q3 print insiders sold ${F['insider']['post_q3_sales_usd']/1e6:.1f}m.
- Three CFOs in 16 months; one resigned with immediate effect three weeks after a guide-down. Four HEYDUDE leaders in four years. The chief digital officer left in 2025.
- A securities class action (Carretta v. Crocs, D. Del.) alleges HEYDUDE's 2022-24 revenue was inflated by overstocking wholesalers; a motion to dismiss has been pending since February 2026. Four derivative suits. Only $0.6m is accrued for all legal matters. [S2] [S22]
- **Bull's rebuttal.** The CEO still holds about {F['insider']['ceo_shares_after']:,} shares (roughly ${F['insider']['ceo_shares_after']*price/1e6:.0f}m); he sold about 13% of his position after a stock that doubled. Directors Replogle, Smach and Kaplan bought at $75-112 between August 2025 and September 2026. The new CFO and HEYDUDE president are credible hires. Securities suits after a 19% one-day drop are routine.
- **Data that would settle it.** Whether the CEO keeps selling above $150; adoption of a 10b5-1 plan (disclosed in 10-Q Item 5); the motion-to-dismiss ruling.

## Checklist the brief asked for

| Check | Finding | Source |
|---|---|---|
| Customer over 25% of revenue | **No.** No customer is 10% or more. | [S1] |
| Margin compression, last 4 quarters | **Yes in 3 of 4.** Gross and operating margin both down y/y in Q4-25, Q1-26 and Q2-26; both up in Q3-26. | [S3]-[S6] |
| Unscheduled insider selling | **Yes.** $23.0m in 12 months, none marked 10b5-1. | [S11] |
| Widening GAAP vs non-GAAP gap | **Not widening on a clean basis.** One very large gap in Q2 2025 (impairment); a recurring ~6% tax adjustment. | [S3] [S7] |
| Guidance cuts in the last 12 months | **None.** Three raises. Last cut 7-Aug-2025; guidance withdrawn 8-May-2025. | [S7] |
| Accounting quality | Intra-group IP transfers created $905m of deferred tax assets and $637m of unrecognised tax benefits. Impairment testing of the remaining $404m goodwill and $1.3bn intangibles depends on HEYDUDE recovering. | [S1] [S2] |
| Debt maturities | Revolver ($113m drawn of $1.0bn) November 2027; $500m term loan February 2029; $350m 4.25% notes March 2029; $350m 4.125% notes August 2031. Nothing due inside 12 months. | [S2] |
| Dilution | Negative. Shares down 11% y/y; stock comp 1.1% of revenue. | [S3] |
| Litigation | Securities class action and four derivative suits (HEYDUDE inventory); Dawgs false-advertising counterclaim; Joybees cross-suits. Damages: not found. | [S2] [S22]-[S24] |
| Regulation / tariffs | 10-12.5% Section 301 duties on all sourcing countries, on top of normal footwear duties; under legal challenge; no sunset. | [S2] [S27] |
| Geopolitics | 45% of Crocs production in Vietnam; two manufacturers make 73%. Middle East conflict cut distributor revenue and raised oil-linked costs in 2026. | [S1] [S2] |
| Currency | 44% of revenue outside the US; $223m of hedges. FX added only 0.2% to FY25 revenue. | [S1] |
| Short interest | {F['short']['shares']/1e6:.2f}m shares, {F['short']['pct_shares']:.1f}% of shares outstanding, {F['short']['dtc']:.1f} days to cover ({F['short']['date']}); down from {F['short']['peak_12m']/1e6:.1f}m a year ago. Shorts have covered. | [S15] |
| Published short reports | None found. Hedgeye lists CROX as a "Best Idea Short" (paywalled, not read). Goldman Sachs (Brooke Roach) rates it Sell, PT $128. | [S26] |

---

# PHASE 4 - THE KEY DEBATE AND ORIGINAL ANALYSIS

## The five-year share price, annotated (`charts/07_price_5y.png`)

| # | Date | Move | Cause |
|---|---|---|---|
| 1 | 23-Dec-2021 | -11.6% | $2.5bn HEYDUDE acquisition announced, funded with $2.0bn of debt |
| 2 | 17-Jun-2022 | trough $47.21 (-74% from the Nov-2021 peak of $180.57) | Bear market, leverage at 2.1x, fear of a post-pandemic unwind |
| 3 | 3-Nov-2022 | +14.2% | Q3-22 beat; HEYDUDE guided to over $1.0bn for 2023 |
| 4 | 27-Apr-2023 | -15.9% | Q1-23 beat and raise, but Q2 EPS guide of $2.83-2.98 disappointed |
| 5 | 27-Jul-2023 | -14.6% | HEYDUDE 2023 growth guide cut from mid-20s% to 14-18% |
| 6 | 8-Jan-2024 | +20.3% | Pre-announced record 2023 revenue of about $3.95bn and higher margin |
| 7 | 29-Oct-2024 | -19.2% | Q3-24: HEYDUDE 2024 guide cut to about -14.5%; "excess inventories in the market" |
| 8 | 13-Feb-2025 | +23.9% | Q4-24 beat; 2025 EPS guide above consensus |
| 9 | 7-Aug-2025 | -29.2% | $737m HEYDUDE impairment; Q3 revenue guided down 9-11%; tariffs |
| 10 | 12-Feb-2026 | +19.0% | Q4-25 beat; 2026 EPS guide $12.88-13.35 vs about $11.9 consensus |
| 11 | 29-Oct-2026 | +25.5% | Q3-26 beat; third raise; HEYDUDE back to growth |

Every large move was an earnings or guidance event. Five of the six big falls were about HEYDUDE.

## The single debate

**Is the clog a fad that is now unwinding in its home market, or a durable franchise going through a deliberate reset while it grows abroad?**

- **Bears** say the 2020-24 boom was a fashion cycle; North America has shrunk for six of the last seven quarters; teens are moving on; copies are legal; and the EPS growth is financial engineering on a melting base. They point to 2008 and to HEYDUDE.
- **Bulls** say the North America decline was self-inflicted to protect price; international is over half the brand and under-penetrated; the product makes a 61% gross margin; and at a 10% free-cash-flow yield you do not need growth.

## Proprietary analysis: how much of Crocs is a fad?

**Method.** I split trailing-twelve-month revenue into nine lines, scored each 1-5 for exposure to a reversal of clog demand, mapped each score to a two-year revenue decline, and ran the lost revenue through the cost structure. Live in `model.xlsx` sheet RevAtRisk; Monte Carlo in `scripts/10_revenue_at_risk.py`.

| Revenue line | TTM revenue | % of group | Score | Haircut | Revenue at risk |
|---|---|---|---|---|---|
""" + "".join(f"| {r['line']} | {m(r['ttm_revenue_usd_m'])} | {r['pct_of_group']:.1f}% | {r['score']} | {r['haircut_pct']:.0f}% | {m(r['revenue_at_risk_usd_m'])} |\n" for r in json.load(open(os.path.join(ROOT, 'data', 'derived', 'rar_rows.json')))) + f"""| **Group** | **{m(RAR['at_risk']/RAR['at_risk_pct'])}** | 100% | | | **{m(RAR['at_risk'])} = {p(RAR['at_risk_pct']*100)}** |

**Sourced inputs:** revenue by brand, region and channel (R) [S3]-[S6]; FY2025 product mix 74/13/8 (R) [S21]; China about 8% of sales (R) [S21]; distribution cost $488m (R) [S1]; trailing adjusted P&L (R).
**My assumptions:** the nine scores; the haircut map (1 = 0%, 2 = 5%, 3 = 12%, 4 = 20%, 5 = 30%, with 5 calibrated to Crocs 2007-09 at -24% and HEYDUDE 2023-25 at -25%); applying the product mix uniformly across regions; applying the 8% China share to the Crocs Brand.

**Stress test**

| | TTM base | Stressed | Change |
|---|---|---|---|
| Revenue | {m(RAR['at_risk']/RAR['at_risk_pct'])} | {m(RAR['rev1'])} | -{p(RAR['at_risk_pct']*100)} |
| Adjusted EBITDA | {m(RAR['ebitda0'])} | {m(RAR['ebitda1'])} | {(RAR['ebitda1']/RAR['ebitda0']-1)*100:.0f}% |
| Adjusted EBIT | {m(F['ttm_adj_ebit'])} | {m(RAR['ebit1'])} | {(RAR['ebit1']/F['ttm_adj_ebit']-1)*100:.0f}% |
| EPS at today's share count | {d(RAR['eps0'])} | {d(RAR['eps1'])} | {(RAR['eps1']/RAR['eps0']-1)*100:.0f}% |

- **Fixed vs variable costs (my assumption):** 50% of distribution cost fixed; all other cost of sales variable; 65% of SG&A fixed; a further 150 bps of gross margin lost to markdowns. Decremental EBIT margin on the lost revenue: {p(RAR['decr']*100,0)}.
- **Tax rate:** 18% (company non-GAAP guidance). Net interest $75m. Shares 46.7m with no further buybacks.
- **Against consensus:** stressed EPS of {d(RAR['eps1'])} is {abs(RAR['vs_cons'])*100:.0f}% below consensus FY2027 EPS of $16.01 (C) [S16]. Consensus embeds none of this risk.
- **Value in the stress:** {d(RAR['eps1'])} x 7.0x trough multiple = {d(RAR['val'],0)}, {p(RAR['val_vs_px']*100,0,True)} from today.

**Sensitivity to my subjective scores**

| Case | Revenue at risk | Stressed EPS |
|---|---|---|
| Every score one notch lower | {p(RAR['minus1_pct']*100)} | {d(RAR['minus1_eps'])} |
| As scored | {p(RAR['at_risk_pct']*100)} | {d(RAR['eps1'])} |
| Every score one notch higher | {p(RAR['plus1_pct']*100)} | {d(RAR['plus1_eps'])} |
| Monte Carlo, each score independently -1/0/+1 (20,000 draws): 5th / 50th / 95th percentile | {F['rar_mc']['at_risk_pct_p5_p50_p95'][0]:.1f}% / {F['rar_mc']['at_risk_pct_p5_p50_p95'][1]:.1f}% / {F['rar_mc']['at_risk_pct_p5_p50_p95'][2]:.1f}% | {d(F['rar_mc']['eps_p5_p50_p95'][0])} / {d(F['rar_mc']['eps_p5_p50_p95'][1])} / {d(F['rar_mc']['eps_p5_p50_p95'][2])} |
| SG&A 50% fixed / 80% fixed (scores unchanged) | | {d(F['rar_cost']['SG&A fixed 50%'])} / {d(F['rar_cost']['SG&A fixed 80%'])} |
| Linear haircut map (0 / 7.5 / 15 / 22.5 / 30%) | {p(F['rar_linear']['at_risk_pct'])} | {d(F['rar_linear']['eps1'])} |

The conclusion is robust to the scores: across the Monte Carlo range a full fad unwind roughly halves EPS. The result is more sensitive to whether an unwind happens than to how I scored it.

## How management is responding

| Response | Hard revenue evidence (R) | Activity metrics only (R, management statements) |
|---|---|---|
| Diversify away from the Classic Clog | Sandals 13% of brand, about $450m in FY25, growing double digits; target about $0.5bn in 2026 | New franchises (Echo, Crafted, recovery clog, ballet flats); 2026 mix not disclosed |
| Grow outside North America | International +8.8% in 9M-26 ({m(1397.5)} vs {m(1284.1)}); international DTC +25.3% in 9M | Store openings (63 in 2025); China campaign "40 billion impressions" |
| Protect price | Adjusted gross margin +180 bps in Q3-26; North America gross profit dollars up after the promotion cut (management statement, not separately reported) | "Many more days that were non-promotional" |
| Social commerce | Piper Sandler estimates TikTok Shop at about 3% of Crocs Brand revenue in 2026 (B) | No. 1 footwear brand on TikTok Shop in four countries |
| Fix HEYDUDE | Revenue +6.1% in Q3-26; wholesale +14.0%; adjusted gross margin +350 bps | Eight collaborations in Q3, "each one selling out"; "we are outselling our inventory in the channel" |
| Cut cost | $150m of savings over 2025-26; adjusted SG&A +3.1% in 9M-26 vs revenue +2.0% | |
| Shrink the equity | 10.9m shares retired since January 2025 for $1.08bn | |

The hard evidence is strongest for international and capital return, moderate for HEYDUDE (one quarter against an easy comparison), and weakest for North America, where the only positive datapoint is DTC excluding an accounting change.

## Is the fear over-priced or under-priced at today's multiple?

- At the March 2026 low ($75.78 close on 20-Mar-2026) the stock was at 6.1x trailing adjusted EPS of $12.51. That price was only {(75.78/RAR['val']-1)*100:.0f}% above my full fad-unwind value of {d(RAR['val'],0)} and below my bear-case target. The fear was heavily over-priced.
- At {d(price)} the market-implied probability of my bear case is about {K['Market-implied probability of the bear case (base:bull 2:1)']*100:.0f}% (solving for the probability that makes my three targets, discounted at an 11% cost of equity, equal today's price). I put it at 25%.
- **Conclusion: the fear is still over-priced, but only modestly.** The gap between 40% and 25% is the entire margin of safety. A year ago the trade was a mispriced disaster scenario. Today it is a fairly priced carry trade with a favourable skew in probability terms and an unfavourable one in magnitude terms.

---

# PHASE 5 - VALUATION

All in `model.xlsx` (1,046 live formulas, zero errors after recalculation).

## Forecast (base case)

| $m | FY25 (R) | FY26E | FY27E | FY28E | FY29E |
|---|---|---|---|---|---|
| Revenue | {B['rev']['FY2025A']:,.0f} | {B['rev']['FY2026E']:,.0f} | {B['rev']['FY2027E']:,.0f} | {B['rev']['FY2028E']:,.0f} | {B['rev']['FY2029E']:,.0f} |
| Growth | -1.5% | {B['g']['FY2026E']*100:+.1f}% | {B['g']['FY2027E']*100:+.1f}% | {B['g']['FY2028E']*100:+.1f}% | {B['g']['FY2029E']*100:+.1f}% |
| Adjusted EBIT | {B['ebit']['FY2025A']:,.0f} | {B['ebit']['FY2026E']:,.0f} | {B['ebit']['FY2027E']:,.0f} | {B['ebit']['FY2028E']:,.0f} | {B['ebit']['FY2029E']:,.0f} |
| Margin | {B['margin']['FY2025A']*100:.1f}% | {B['margin']['FY2026E']*100:.1f}% | {B['margin']['FY2027E']*100:.1f}% | {B['margin']['FY2028E']*100:.1f}% | {B['margin']['FY2029E']*100:.1f}% |
| Adjusted net income | | {B['ni']['FY2026E']:,.0f} | {B['ni']['FY2027E']:,.0f} | {B['ni']['FY2028E']:,.0f} | {B['ni']['FY2029E']:,.0f} |
| Free cash flow | | | {B['fcf']['FY2027E']:,.0f} | {B['fcf']['FY2028E']:,.0f} | {B['fcf']['FY2029E']:,.0f} |
| Buybacks | | | {B['bb']['FY2027E']:,.0f} | {B['bb']['FY2028E']:,.0f} | {B['bb']['FY2029E']:,.0f} |
| Average diluted shares, m | {B['sh_avg']['FY2025A']:.1f} | {B['sh_avg']['FY2026E']:.1f} | {B['sh_avg']['FY2027E']:.1f} | {B['sh_avg']['FY2028E']:.1f} | {B['sh_avg']['FY2029E']:.1f} |
| **Adjusted EPS** | **{B['eps']['FY2025A']:.2f}** | **{B['eps']['FY2026E']:.2f}** | **{B['eps']['FY2027E']:.2f}** | **{B['eps']['FY2028E']:.2f}** | **{B['eps']['FY2029E']:.2f}** |
| Consensus EPS (C) | | 14.63 | 16.01 (Yahoo) / 15.85 (Nasdaq) | 16.69 (Nasdaq, 1 analyst) | |
| Net debt / EBITDA | {B['lev']['FY2025A']:.1f}x | {B['lev']['FY2026E']:.1f}x | {B['lev']['FY2027E']:.1f}x | {B['lev']['FY2028E']:.1f}x | {B['lev']['FY2029E']:.1f}x |

**Why I am {V['vs_cons'][1]*100:.0f}% above consensus for FY27.** Company guidance excludes future buybacks and the Street follows it. Consensus FY27 EPS of $16.01 on consensus revenue of $4.34bn implies a share count close to today's. My share count is {B['sh_avg']['FY2027E']:.1f}m against {B['sh_avg']['FY2026E']:.1f}m in FY26. Two-thirds of that reduction is already locked in by 2026 repurchases: with no buybacks at all in 2027 my EPS would still be {d(e27_base + SN['No buybacks at all in FY27 (cash retained)'][0])}.

## Scenarios

| | Bear | Base | Bull |
|---|---|---|---|
| Probability (E) | 25% | 50% | 25% |
| Story | Fad partly unwinds: North America -8% for two years, international stalls, HEYDUDE relapses | Management's 2027 colour: Crocs about +4%, HEYDUDE low- to mid-single digits, margin flat | North America grows, international low-teens, margin recovers a third of what it lost |
| Revenue CAGR FY26E-31E | {V['rcagr'][0]*100:+.1f}% | {V['rcagr'][1]*100:+.1f}% | {V['rcagr'][2]*100:+.1f}% |
| FY28E adjusted EBIT margin | {V['margin28'][0]*100:.1f}% | {V['margin28'][1]*100:.1f}% | {V['margin28'][2]*100:.1f}% |
| FY27E EPS | {d(e27_bear)} | {d(e27_base)} | {d(e27_bull)} |
| FY28E EPS | {d(e28_bear)} | {d(e28_base)} | {d(e28_bull)} |
| Exit P/E on FY28E, December 2027 | 7.0x | 10.5x | 13.0x |
| **Price target** | **{d(pt_bear,0)}** | **{d(pt_base,0)}** | **{d(pt_bull,0)}** |
| Return | {p(r_bear,0,True)} | {p(r_base,0,True)} | {p(r_bull,0,True)} |
| DCF value per share (cross-check) | {d(dcf_bear,0)} | {d(dcf_base,0)} | {d(dcf_bull,0)} |

- **Probability-weighted value {d(pt_w,0)}; expected return {p(r_w,0,True)}** over about 13 months.
- **Upside/downside ratio:** {K['Upside/downside ratio, base vs bear (x)']:.2f}x base vs bear; {K['Upside/downside ratio, probability-weighted (x)']:.1f}x probability-weighted.
- **Break-even:** the expected return is zero if the bear probability is {K['Break-even bear probability (EV = 0, base:bull kept 2:1)']*100:.0f}% rather than 25%.
- **How much of the base target is multiple?** Today's P/E on my FY27E EPS is {xx(F['pe_fy27_mine'])}. At that unchanged multiple the December 2027 value is {d(F['pe_fy27_mine']*e28_base,0)} ({(F['pe_fy27_mine']*e28_base/price-1)*100:+.0f}%). The step to 10.5x assumes consensus moves up to my numbers and the stock keeps today's {xx(F['pe_fy27_cons'])} consensus multiple.

## DCF (base)

WACC 10.0% (risk-free 5.0%, beta 1.2, equity premium 5.0%, cost of equity 11.0%, pre-tax debt 6.5%); terminal growth 2.0%; cash tax 22%; stock comp not added back. Enterprise value {m(B['dcf']['ev'],0)}, less net debt {m(B['dcf']['nd'],0)}, equity {m(B['dcf']['eq'],0)}, {d(dcf_base,0)} per share. Terminal value is {B['dcf']['tvpct']*100:.0f}% of enterprise value.

**DCF sensitivity, base case ($ per share)**

| WACC \\ terminal growth | 0% | 1% | 2% | 3% |
|---|---|---|---|---|
""" + "".join("| " + f"{r[0]*100:.1f}%" + " | " + " | ".join(f"{v:,.0f}" for v in r[1:]) + " |\n" for r in MO["sens_dcf_grid"][1:]) + f"""
## Reverse DCF: what does {d(price)} imply?

- Enterprise value {m(F['ev'],0)}. Trailing unlevered free cash flow after a 22% cash tax and 3% reinvestment: {m(F['reverse']['fcf'],0)}.
- **Implied perpetual growth in free cash flow: {F['reverse']['implied_g']*100:.1f}%** at a 10% WACC (single-stage).
- **Implied ten-year revenue growth at today's 22-23% margin: about {F['reverse']['implied_cagr']*100:.0f}% a year**, then 2%. My base case is {V['rcagr'][1]*100:.1f}%.
- Or, with zero growth forever, the price needs a {F['reverse']['implied_margin']*100:.0f}% margin, above anything Crocs has earned since 2023.
- **Read:** the market pays for a business that roughly stands still in real terms. It is not paying for decline, and not for growth.

## Cross-checks

- **Multiples and mean reversion.** Five-year mean forward P/E {xx(RK['CROX_pe_ntm_5y_stats']['mean'])}, median {xx(RK['CROX_pe_ntm_5y_stats']['median'])}. Mean reversion on my FY28E EPS gives {d(RK['CROX_pe_ntm_5y_stats']['mean']*e28_base,0)}; on consensus FY27 EPS it gives {d(RK['CROX_pe_ntm_5y_stats']['mean']*16.01,0)}. **Mean reversion of the multiple is a headwind, not a tailwind.** The long works only because EPS grows faster than the multiple can plausibly shrink.
- **Free-cash-flow yield.** {p(F['fcf_yield'])} on trailing free cash flow; {B['fcf']['FY2027E']/F['mcap']*100:.1f}% on my FY27E (which treats stock comp as a cash cost).
- **Sell-side.** Mean target $160.75, low $128 (Goldman Sachs), high $184; 5 Buy / 5 Hold / 1 Sell on Nasdaq (C) [S15].

## Expectations bar

- **Q4 2026 (about 11 February 2027):** guide is revenue +7-9% and EPS $3.25-3.45; consensus $3.40 (C). Crocs has beaten the top of its EPS guide in each of the last four quarters by 5-19%. The smallest of those beats applied to $3.45 is about $3.61; anything below that is a deceleration in beat size.
- **FY2027 guide:** consensus $16.01. A guide that excludes buybacks should still be about $16.0-16.8 on my numbers. Below $15.5 would break the thesis on margin.
- **Reaction to the last eight reports:** +23.9%, +9.8%, -29.2%, -2.5%, +19.0%, +1.8%, -7.4%, +25.5%. Average absolute move {F['earn_avg_abs_move']:.0f}%. The stock fell on two beats (October 2025, July 2026) when the next-quarter guide was soft. Guidance matters more than the quarter.

## Downside in a market sell-off

- Beta: 1.21 on five years of weekly returns (mine); 1.50 on Yahoo's five-year monthly; 0.67 over the last two years. One-year volatility 51% vs 15% for the S&P 500.
- In past S&P 500 drawdowns of 10% or more: 2020 -68% (index -34%); 2022 -42% (index -25%); February-April 2025 -19% (index -19%); October-November 2026 +29% (index -11%, because of the Q3 print).
- Own worst drawdown in five years: -74% (November 2021 to June 2022).
- **Planning number:** in a 20% market fall with no company news I would expect CROX down 25-30%, to about $112-120.

---

# PHASE 6 - CATALYSTS

| # | Date or window | Catalyst | Mechanism | Size in numbers | Probability (E) | Inside holding period? |
|---|---|---|---|---|---|---|
| 1 | 1-Dec-2026 | Morgan Stanley consumer conference | First read on Black Friday; any intra-quarter comment vs the +7-9% Q4 guide | Q4 revenue guide implies about $1,034m | 50% that it moves the stock either way | Yes |
| 2 | About 11-Feb-2027 (unconfirmed) | Q4 2026 results and first FY2027 guide | EPS guide vs $16.01 consensus; guide excludes buybacks | My FY27E {d(e27_base)}; ex-buyback {d(e27_base + SN['No buybacks at all in FY27 (cash retained)'][0])} | 60% that the guide midpoint is at or above $16.0 | Yes |
| 3 | Late April 2027 | Q1 2027 results | Worst optics on North America DTC (700-800 bps accounting headwind); HEYDUDE still on easy comps | North America DTC reported about -5% even if underlying +2% | 40% the market looks through it | Yes |
| 4 | Late July 2027 | Q2 2027 results | Seasonally largest quarter (EPS consensus $5.04) | 30% of annual EPS | n/a | Yes |
| 5 | Late October 2027 | Q3 2027 results | Marketplace shift lapped, clean North America number; but GAAP laps $64m of refunds | Adjusted figures unaffected | 55% North America DTC prints positive | Yes |
| 6 | Continuous | Buybacks | $1.7bn authorisation = {1700/F['mcap']*100:.0f}% of market cap; guidance excludes them | Base: {m(B['bb']['FY2027E'],0)} in FY27, 3.5m shares, about +{SN['+$100m share repurchases (full-year effect)'][1]*100*B['bb']['FY2027E']/100:.0f}% to run-rate EPS | 85% that 2027 buybacks exceed $500m | Yes |
| 7 | By November 2027 | Revolver refinancing | $1.0bn facility matures; $113m drawn | Extends maturity; cost about SOFR + 1.25-1.75% (E) | 90% done without issue | Yes |
| 8 | Open-ended | Section 301 tariff litigation or rate changes | 10-12.5% duties challenged at the Court of International Trade; Vietnam could move to the 10% tier | Each point about $4m, {d(abs(SN['+1 pt US tariff rate on imports'][0]))} EPS. Removal: about +$45m, +{45*0.82/B['sh_avg']['FY2027E']:.2f} EPS | 20% struck down within 12 months; 20% raised | Possibly |
| 9 | Q4 2026 - H1 2027 | Remaining IEEPA refunds | $8-13m still to come of $75-80m eligible | GAAP only; excluded from adjusted EPS | 90% | Yes |
| 10 | Open-ended | Ruling on motion to dismiss, Carretta v. Crocs | Dismissal removes an overhang; denial opens discovery | Damages not quantified; only $0.6m accrued | 50% dismissed | Possibly |
| 11 | About October 2027 | Piper Sandler teen survey | Crocs at No. 10 with 1% share; falling out of the top ten would feed the fad narrative | Stock fell over 3% on the Spring 2024 survey | 40% drops out | Yes |
| 12 | Open-ended | Supreme Court decision on cert, Crocs v. ITC | Procedural; does not restore the trademark claim | Small | 15% granted | Possibly |
| 13 | Not scheduled | Investor day / long-term targets | None announced; no multi-year financial targets were given on any of the last six earnings calls | Would anchor the margin debate | 20% within 12 months | Uncertain |
| 14 | Not a catalyst | S&P 500 inclusion | Market cap $7.3bn is far below the threshold | n/a | 0% | No |

---

# PHASE 7 - THE THESIS

**Recommendation: LONG CROX. Price target {d(pt_base,0)} (December 2027, base case). Probability-weighted value {d(pt_w,0)}, expected return {p(r_w,0,True)}. Holding period 12-18 months.**

**One sentence.** A 10% free-cash-flow yield pointed at a shrinking share count compounds EPS in the mid-teens on 4% revenue growth, and at {xx(F['pe_fy27_cons'])} earnings the market is still charging for a clog bust that the international numbers do not support.

## Variant perception

| | Consensus believes | I believe | Why the market is wrong |
|---|---|---|---|
| Earnings | FY27 EPS $16.01, +9% (C) | {d(e27_base)}, +{B['epsg']['FY2027E']*100:.0f}% (E) | Guidance and most models exclude buybacks. Crocs has retired about 10% of its shares in each of the last two years and has $1.7bn authorised. Two-thirds of the FY27 share-count benefit is already banked. |
| North America | Structural decline: teens leaving, six negative quarters in seven | Mostly self-inflicted and now distorted: promotion cuts from May 2025, tighter wholesale sell-in, and an accounting shift that hides DTC growth until Q3 2027 | The market reads reported growth; underlying DTC was +2% to +5% in each quarter of 2026. But I hold this view with low confidence: it is the part of the thesis with the least hard evidence. |
| What the company is | A one-product US fad | A majority-international brand: {p(F['intl_share_ttm'],0)} of Crocs Brand revenue, growing 9-12%, with share one-third of mature levels in its five biggest growth markets | The 2008 bust and the HEYDUDE write-off anchor perceptions. In 2008 Crocs had negative free cash flow and no international base of this size. |
| HEYDUDE | Worth nothing, a recurring source of negative surprises | Worth little, but no longer shrinking; it only has to stay flat | Five of the last six big falls in the stock were HEYDUDE guide-downs. That source of shocks is now much smaller: 17% of revenue, already written down. |

**What I am not claiming:** that the stock is cheap against peers (it is not), that the multiple should expand (history says it should not), or that the brand has a patent-like moat (it does not).

## Three pillars

| Pillar | Evidence | KPI to track |
|---|---|---|
| 1. Capital return does the work | Free cash flow {m(F['ttm_fcf'],0)} TTM ({p(F['fcf_yield'])} yield); ${F['ttm_buyback']:,.0f}m of buybacks in twelve months; diluted shares 54.0m to 48.0m in a year; leverage {xx(F['nd_ebitda'])} against a 1-1.5x target; $1.7bn authorised | Diluted share count down at least 7% y/y each quarter; free cash flow at least $700m a year; net debt/EBITDA at or below 1.5x |
| 2. International is a structural offset to North America | International 33% of the brand in FY21, {p(F['intl_share_ttm'],0)} now; +11.8% in Q3-26, DTC +24.1%; China +30% in 2025; share one-third of mature markets | Crocs International growth at or above 7% in constant currency; international DTC at or above 15% |
| 3. The earnings base has stopped shrinking | Adjusted operating margin troughed at 16.8% in Q4-25 and rose 150 bps y/y in Q3-26; duties down from 18-20% to 10-12.5%; $150m of cost savings; HEYDUDE +6% in Q3 and guided +10-12% in Q4 | Adjusted operating margin at or above 22.5% for FY27; HEYDUDE revenue flat or better; Crocs North America DTC excluding the shift at or above 0% |

## Key risks, mitigants and kill criteria

| Risk | Mitigant | Kill criterion (exit or cut) |
|---|---|---|
| The fad unwinds: North America falls again | International majority; DTC growing; price protected | North America DTC excluding the shift negative for two consecutive quarters |
| International slows | Low share; store roll-out; China only 8% | Crocs International growth below 5% for two consecutive quarters |
| Margin slips again (mix, oil, tariffs, promotions) | Cost programme; lower duties | Adjusted operating margin guided below 21.5% for FY27, or adjusted gross margin down more than 100 bps y/y for two quarters |
| Capital allocation error: another large acquisition | Leverage target; management says buybacks are the priority | Any acquisition above $500m, or net debt/EBITDA above 1.5x, or buybacks below $300m annualised |
| HEYDUDE relapses | Channel inventory clean | HEYDUDE revenue down more than 5% y/y in any quarter after Q1 2027 |
| Insiders keep selling; another CFO change | CEO retains about ${F['insider']['ceo_shares_after']*price/1e6:.0f}m of stock | CEO sells more than a further 10% of his holding, or the CFO leaves |
| Market sell-off | Low multiple, buyback support | None; this is a sizing question (plan for -25-30% in a -20% market) |
| Valuation: stock at consensus target after +99% | Estimates rising (FY27 EPS +7% in 30 days) | Price above $230 without a matching rise in my FY28 EPS: take profit |

## Does the evidence support a pitch?

Yes, but a qualified one. The honest position is:

1. **A long, not a strong buy.** Expected return {p(r_w,0,True)} with a {K['Upside/downside ratio, base vs bear (x)']:.2f}x base-to-bear ratio does not justify a top-weight position.
2. **Entry matters.** After +34% in a month, I would start at half size and add below $140 (8.1x my FY27E EPS), where the expected return rises to about 40%.
3. **It would have been a far better pitch at $80.** The largest part of the mispricing has been corrected.
"""

# =========================================================== one-pager.md ===========================================================
T["one-pager.md"] = f"""# CROX - one-pager

**Crocs, Inc. (NASDAQ: CROX) | LONG | Price {d(price)} ({F['asof']}) | Base target {d(pt_base,0)} (Dec-2027, {p(r_base,0,True)}) | Probability-weighted {d(pt_w,0)} ({p(r_w,0,True)}) | Bear {d(pt_bear,0)} / Bull {d(pt_bull,0)} | Holding period 12-18 months**

Labels: (R) reported, (G) guidance, (C) consensus, (B) broker, (E) my estimate. Sources in `sources.md`.

## Thesis

A 10% free-cash-flow yield pointed at a shrinking share count compounds EPS in the mid-teens on 4% revenue growth. At {xx(F['pe_fy27_cons'])} consensus FY27 earnings the market still prices a roughly 40% chance of a clog bust; I put it at 25%.

## Snapshot

| | |
|---|---|
| Market cap / EV | {bn(F['mcap'],1)} / {bn(F['ev'],1)} (net debt {m(F['net_debt'],0)}, {xx(F['nd_ebitda'])} EBITDA) |
| TTM revenue / adj. EBITDA / FCF (R) | {m(F['ttm_rev'],0)} / {m(F['ttm_ebitda'],0)} / {m(F['ttm_fcf'],0)} |
| P/E FY26 guide / FY27 consensus / FY27 mine | {xx(F['pe_fy26_guide'])} / {xx(F['pe_fy27_cons'])} / {xx(F['pe_fy27_mine'])} |
| EV/EBITDA TTM; FCF yield; buyback yield | {xx(F['ev_ebitda'])}; {p(F['fcf_yield'])}; {p(F['buyback_yield'])} |
| FY27E EPS: mine vs consensus | {d(e27_base)} (E) vs $16.01 (C), {V['vs_cons'][1]*100:+.0f}% |
| Key holders | BlackRock, Vanguard, FMR (7.1%), WIT Partners (HEYDUDE founder, 5.3%); insiders 3.1% |
| 52-week range; 1-year return | $75.13-164.24; +99% |
| Short interest | {F['short']['pct_shares']:.1f}% of shares, {F['short']['dtc']:.1f} days to cover |

## Why the market is wrong (variant perception)

1. **Street EPS ignores buybacks.** Guidance excludes them and consensus follows. Crocs retired about 10% of its shares in each of 2025 and 2026 and has $1.7bn authorised ({1700/F['mcap']*100:.0f}% of market cap).
2. **North America is distorted, not collapsing.** Promotions were cut on purpose in May 2025; an accounting shift hides DTC growth until Q3 2027. Underlying DTC grew 2-5% in each quarter of 2026. (Lowest-confidence leg of the thesis.)
3. **This is a majority-international brand.** {p(F['intl_share_ttm'],0)} of Crocs Brand revenue, growing 9-12%, with share one-third of mature levels in China, India, Japan, Germany and France.

## Proprietary analysis

Scoring nine revenue lines for fad exposure puts **{p(RAR['at_risk_pct']*100)} of revenue ({m(RAR['at_risk'],0)}) at risk**. Run through the cost structure that cuts EPS to {d(RAR['eps1'])} ({(RAR['eps1']/RAR['eps0']-1)*100:.0f}%), worth about {d(RAR['val'],0)} at 7x. The March 2026 low of $76 priced nearly all of that. Today's price embeds about a 40% chance of my milder bear case.

## Three pillars and KPIs

| Pillar | KPI |
|---|---|
| Capital return: FCF {m(F['ttm_fcf'],0)}, shares -11% y/y | Share count down at least 7% y/y; leverage at or below 1.5x |
| International: +11.8% in Q3-26, DTC +24% | International growth at or above 7% |
| Earnings base stabilised: margin +150 bps y/y in Q3-26, HEYDUDE +6% | Adj. operating margin at or above 22.5%; HEYDUDE flat or better |

## Catalysts

FY2027 guide about 11-Feb-2027 (my ex-buyback EPS {d(e27_base + SN['No buybacks at all in FY27 (cash retained)'][0])} vs $16.01 consensus); Q3 2027 lapping of the North America accounting shift; continuous buybacks; tariff litigation.

## Top risks

1. Clog fad unwinds in North America (still -2% in Q3-26; teen rank No. 10).
2. Earnings quality: operating income 14% below FY23; EPS growth is share count; non-GAAP tax rate 18% vs 23% GAAP.
3. CEO sold ${F['insider']['ceo_sales_usd']/1e6:.1f}m in six months, no 10b5-1 plan disclosed; three CFOs in 16 months.

**Kill criteria:** North America DTC ex-shift negative two quarters running; international growth below 5% two quarters running; FY27 margin guide below 21.5%; acquisition above $500m; leverage above 1.5x.

## What I would not say

The stock is not cheap against Deckers ({pk('CROX','pe_fwd'):.1f}x vs {pk('DECK','pe_fwd'):.1f}x forward P/E), it is in the top quartile of its own five-year P/E range, and it has no patent moat. The long is about carry and compounding. After +34% in a month, start at half size and add below $140.
"""

# =========================================================== qa-prep.md ===========================================================
qa = [
("Growth runway: North America is saturated and shrinking. Where does growth come from?",
 f"From outside the US. International is {p(F['intl_share_ttm'],0)} of Crocs Brand revenue and grew 11.8% in Q3. Management says share in China, India, Japan, Germany and France is one-third of established-market levels. My base case needs only {B['g']['FY2027E']*100:.1f}% group growth, with North America flat."),
("What happens when the cyclical driver, the clog fashion cycle, slows?",
 f"It already has in North America, down 6.8% in FY25. If it gets worse my bear case has North America falling 8% a year for two years, EPS of {d(e28_bear)} in FY28 and a {d(pt_bear,0)} stock. The full fad unwind in my stress test is {d(RAR['eps1'])} of EPS."),
("Why a 12-18 month holding period?",
 f"Because it spans the two events that settle the debate: the FY27 guide in February and Q3 2027, when the 700-800 basis point North America accounting distortion is lapped. It is also long enough for two more years of buybacks to show: my share count falls {abs((B['sh_avg']['FY2028E']/B['sh_avg']['FY2026E']-1)*100):.0f}% by FY28."),
("The stock has doubled. Is it not already priced in?",
 f"The re-rating is, the compounding is not. On a reverse DCF the price implies about {F['reverse']['implied_cagr']*100:.0f}% revenue growth for a decade. On my numbers it is {xx(F['pe_fy27_mine'])} FY27 earnings. My base target is {d(pt_base,0)}. But I agree the easy money was made between $76 and $160."),
("What if results beat but the stock falls?",
 f"It has happened twice in eight quarters: October 2025 (-2.5%) and July 2026 (-7.4%), both on a soft next-quarter guide. The average absolute move on results is {F['earn_avg_abs_move']:.0f}%. That is why I would start at half size and treat a guide-driven dip below $140 as the entry, provided the kill criteria are intact."),
("The discount to Deckers has closed. Could the gap reopen the wrong way?",
 f"Yes. The five-year median discount was {abs(RK['CROX_vs_DECK_ntm_prem_pct_5y_stats']['median']):.0f}% and today it is about {abs((RK['crox_pe_ntm_now']/RK['deck_pe_ntm_now']-1)*100):.0f}%. Deckers has net cash and grows faster. I do not rely on relative value; my base target uses 10.5x, roughly today's multiple, not a peer multiple."),
("How exposed is this to interest rates?",
 f"Modestly. About 47% of the $1.3bn of debt is floating; 100 basis points costs $5.6m, or {abs(SN['+100 bps interest rates'][1])*100:.1f}% of EPS. The bigger rate effect is on the multiple: every 50 basis points on WACC moves my DCF by about $14 a share."),
("Regulation: what is the tariff exposure now?",
 f"US imports from Vietnam, China, Indonesia, India and Cambodia carry a 10-12.5% Section 301 duty, down from the 18-20% IEEPA layer that the Supreme Court struck down in February 2026. Each point is about $4m, or {d(abs(SN['+1 pt US tariff rate on imports'][0]))} of EPS. The $64m of refunds is excluded from adjusted earnings."),
("Elections and politics: does the November 2026 midterm result matter?",
 f"Indirectly. Trade policy is the channel, and tariffs now rest on Section 301 with no sunset, so Congress matters less than the courts and USTR. A 5-point tariff swing either way is about {d(abs(SN['+1 pt US tariff rate on imports'][0])*5)} of EPS, roughly 2%. The consumer effect of any fiscal change is larger and I cannot quantify it."),
("War and geopolitics?",
 f"Two exposures. Sourcing: 45% of Crocs production is in Vietnam and two manufacturers make 73% of it. Demand and cost: the Middle East conflict cut distributor revenue and raised oil-linked resin and freight costs in 2026; that is why the international guide was trimmed from about 10% to high single digits in April."),
("Currency?",
 f"44% of revenue is outside the US. A 1% stronger dollar costs about {abs(SN['+1% USD vs all currencies'][1])*100:.1f}% of EPS on my 35% flow-through assumption. FX added only 0.2% to FY25 revenue, and Crocs hedges $223m notional."),
("What is the downside in a market sell-off?",
 f"Plan for 25-30% down in a 20% market fall, to about $112-120. Beta is 1.2 on five years of weekly data and 1.5 on Yahoo's monthly measure. In 2022 the stock fell 42% against 25% for the index, and 74% peak to trough."),
("How subjective are your assumptions in the revenue-at-risk work?",
 f"The nine scores and the haircut map are mine. Moving every score one notch changes revenue at risk from {p(RAR['at_risk_pct']*100,0)} to {p(RAR['minus1_pct']*100,0)} or {p(RAR['plus1_pct']*100,0)}. A Monte Carlo of independent one-notch moves gives a 5th-95th percentile EPS range of {d(F['rar_mc']['eps_p5_p50_p95'][0])} to {d(F['rar_mc']['eps_p5_p50_p95'][2])}. The conclusion that a full unwind halves EPS survives."),
("What are the numbers behind the main catalyst?",
 f"The FY27 guide, expected around 11 February. Consensus EPS is $16.01. My base is {d(e27_base)}; excluding all 2027 buybacks, as guidance does, it is {d(e27_base + SN['No buybacks at all in FY27 (cash retained)'][0])}. I put 60% on a guide midpoint at or above $16."),
("And the numbers behind the HEYDUDE acquisition?",
 f"$2.5bn headline in February 2022: $2.05bn cash and $450m in stock, funded by a $2.0bn term loan. Revenue peaked at $949m in 2023 and was $715m in 2025. Crocs wrote off $737m, about 30% of the price. The term loan is down to $500m. It was a poor deal; it is also now only 17% of revenue."),
("Operating income is below 2023. Is this not just financial engineering?",
 f"Largely, yes, and I say so. Adjusted operating income is {m(B['ebit']['FY2026E'],0)} against {m(fy(2023)['adj_op_income'],0)} in FY23. But the buybacks are funded by {m(F['ttm_fcf'],0)} of real free cash flow, not debt: leverage is {xx(F['nd_ebitda'])}. Retiring 8% of the company a year at 10x earnings is a legitimate source of per-share value."),
("The CEO has been selling. Why should we buy?",
 f"He sold {F['insider']['ceo_sales_sh']:,.0f} shares for ${F['insider']['ceo_sales_usd']/1e6:.1f}m since June with no 10b5-1 plan disclosed on the forms, which I flag as a red flag. He retains about {F['insider']['ceo_shares_after']:,} shares, so he sold roughly 13%. A further 10% sale is one of my kill criteria."),
("Why is your EPS above consensus? What do you know that the Street does not?",
 f"Nothing secret: it is arithmetic. I am {V['vs_cons'][1]*100:.0f}% above consensus for FY27 because I model {m(B['bb']['FY2027E'],0)} of buybacks and the Street models few or none. Consensus FY27 EPS has already risen 7% in 30 days, from $14.95 to $16.01."),
("What would make you wrong fastest?",
 f"A second leg down in North America. If DTC excluding the accounting shift turns negative for two quarters, the 'self-inflicted' explanation fails and my bear case, 25% probability and {d(pt_bear,0)}, becomes the base case. That number is disclosed quarterly, so I will know by April."),
("Why not wait for a better entry, or just own Deckers?",
 f"Waiting is reasonable: I would buy half now and half below $140, where expected return rises from {p(r_w,0)} to about {(pt_w/140-1)*100:.0f}%. Deckers is the higher-quality company at a similar {pk('DECK','pe_fwd'):.1f}x, but it returns {pk('DECK','buyback_yield_pct'):.0f}% of its market cap a year in buybacks against {pk('CROX','buyback_yield_pct'):.0f}% for Crocs."),
]
T["qa-prep.md"] = "# CROX - Q&A prep: the 20 toughest questions\n\nEach answer is about 30 seconds spoken (60-80 words) and contains at least one number. Figures as of " + F['asof'] + "; (E) estimates from `model.xlsx`.\n\n" + \
    "\n".join(f"### {i}. {q}\n\n{a}\n" for i, (q, a) in enumerate(qa, 1))

# =========================================================== cheat-sheet.md ===========================================================
cs = [("Share price", d(price), f"Nasdaq close {F['asof']}"), ("Market cap / enterprise value", f"{bn(F['mcap'],1)} / {bn(F['ev'],1)}", "45.7m shares; net debt $1.15bn"),
      ("Base price target (Dec-2027)", f"{d(pt_base,0)} ({p(r_base,0,True)})", "10.5x FY28E EPS of " + d(e28_base) + " (E)"), ("Probability-weighted value / expected return", f"{d(pt_w,0)} / {p(r_w,0,True)}", "25% bear, 50% base, 25% bull (E)"),
      ("Bear / bull targets", f"{d(pt_bear,0)} ({p(r_bear,0,True)}) / {d(pt_bull,0)} ({p(r_bull,0,True)})", "7.0x and 13.0x (E)"), ("FY2026 adjusted EPS guidance", "$14.45-14.65", "raised three times from $12.88-13.35 (G)"),
      ("FY2027 EPS: consensus vs mine", f"$16.01 vs {d(e27_base)}", "Yahoo, 15 analysts (C); mine includes buybacks (E)"), ("Forward P/E on consensus FY27", xx(F['pe_fy27_cons']), f"5-year median {xx(RK['CROX_pe_ntm_5y_stats']['median'])}; S&P 500 18.3x"),
      ("EV / TTM adjusted EBITDA", xx(F['ev_ebitda']), f"Deckers {pk('DECK','ev_ebitda'):.1f}x (vendor basis: CROX {pk('CROX','ev_ebitda'):.1f}x)"), ("TTM free cash flow / yield", f"{m(F['ttm_fcf'],0)} / {p(F['fcf_yield'])}", "CFO less capex, to Sep-2026 (R)"),
      ("TTM revenue", m(F['ttm_rev'],0), f"{p(F['ttm_rev_g'],1,True)} y/y; FY26 guide about +3% (R/G)"), ("Adjusted operating margin", "22.3% FY25; about 22.6% FY26E", "27.7% in FY23 (R/G)"),
      ("Crocs Brand / HEYDUDE revenue, FY25", f"{m(fy(2025)['crocs_rev'],0)} / {m(fy(2025)['hd_rev'],0)}", "82% / 18% (R)"), ("International share of Crocs Brand", f"{p(F['intl_share_ttm'],0)} TTM", "33% in FY21 (R)"),
      ("Q3-26 growth: Crocs NA / International / HEYDUDE", "-2.1% / +11.8% / +6.1%", "(R)"), ("Product mix, Crocs Brand FY25", "clogs 74%, sandals 13%, Jibbitz 8%", "management, Q4-25 call (R)"),
      ("Revenue at risk if the fad unwinds", f"{p(RAR['at_risk_pct']*100)} = {m(RAR['at_risk'],0)}", "my scoring (E)"), ("Stressed EPS / value", f"{d(RAR['eps1'])} / {d(RAR['val'],0)}", f"EPS {(RAR['eps1']/RAR['eps0']-1)*100:.0f}%; 7x trough multiple (E)"),
      ("Buybacks", f"${F['ttm_buyback']:,.0f}m TTM; $1.7bn authorised", f"shares -11% y/y; authorisation = {1700/F['mcap']*100:.0f}% of market cap (R)"), ("Net debt / EBITDA", xx(F['nd_ebitda']), "target 1-1.5x; revolver matures Nov-2027 (R)"),
      ("HEYDUDE deal", "$2.5bn paid (2022); $737m written off (2025)", "revenue $949m peak to $715m (R)"), ("Tariffs", "10-12.5% now vs 18-20% in 2025", f"about $4m, {d(abs(SN['+1 pt US tariff rate on imports'][0]))} EPS per point; $64m refund excluded (R/E)"),
      ("Insider selling, 12 months", f"${F['insider']['sales_12m_usd']/1e6:.1f}m sold vs ${F['insider']['buys_12m_usd']/1e6:.1f}m bought", f"CEO ${F['insider']['ceo_sales_usd']/1e6:.1f}m; none marked 10b5-1 (R)"),
      ("Reverse DCF", f"about {F['reverse']['implied_cagr']*100:.0f}% revenue growth for 10 years", f"implied perpetual FCF growth {F['reverse']['implied_g']*100:.1f}% at 10% WACC (E)"),
      ("Earnings-day volatility", f"{F['earn_avg_abs_move']:.0f}% average absolute move", "last eight: +24, +10, -29, -3, +19, +2, -7, +26 (R)")]
T["cheat-sheet.md"] = "# CROX - cheat sheet: 25 numbers to know cold\n\nAs of " + F['asof'] + ". (R) reported, (G) guidance, (C) consensus, (E) my estimate.\n\n| # | Number | Value | Context |\n|---|---|---|---|\n" + \
    "\n".join(f"| {i} | {a} | **{b}** | {c} |" for i, (a, b, c) in enumerate(cs, 1)) + "\n"
assert len(cs) == 25 and len(qa) == 20

# =========================================================== checklist.md ===========================================================
T["checklist.md"] = f"""# CROX pitch - task checklist

| Phase | Task | Status | Output |
|---|---|---|---|
| 0 | Set up folder, data and scripts directories | [x] | `CROX-pitch/` |
| 0 | Download SEC filings (10-K x6, 10-Q x9, earnings releases x26, proxy, Form 4s, 13Gs) | [x] | `data/sec/`, `data/sec_txt/` |
| 0 | Market data, consensus, short interest, holders | [x] | `data/market/` (Nasdaq API; Yahoo price API and Macrotrends refused automated access, see sources.md) |
| 0 | Peer fundamentals and multiples | [x] | `data/sa/` |
| 0 | Earnings call transcripts (six calls) and web research | [x] | `data/transcripts/`, `data/research/` |
| 1 | Deep dive (11 sections) | [x] | `deep-dive.md` |
| 2 | Peer comparison, P/E history, premium/discount | [x] | `deep-dive.md`, `charts/08-10`, `model.xlsx` Peers |
| 3 | Bear case: 3 ranked red flags and checklist | [x] | `deep-dive.md` Phase 3 |
| 4 | Key debate, annotated price chart, revenue-at-risk analysis, stress test, sensitivity | [x] | `deep-dive.md` Phase 4, `charts/07, 12, 13`, `model.xlsx` RevAtRisk |
| 5 | Forecast, DCF, reverse DCF, scenarios, sensitivities | [x] | `model.xlsx` |
| 6 | Catalyst table | [x] | `deep-dive.md` Phase 6 |
| 7 | Thesis, variant perception, pillars, risks, kill criteria | [x] | `deep-dive.md` Phase 7 |
| 8 | deck.pptx (15 main slides plus appendix, speaker notes) | [x] | `deck.pptx` |
| 8 | pitch-memo.docx | [x] | `pitch-memo.docx` |
| 8 | model.xlsx, one-pager.md, qa-prep.md, cheat-sheet.md, sources.md | [x] | as named |
| 9 | Re-run scripts, formula-error scan, cross-document number check | [x] | `verification.md` |
"""
for name, text in T.items():
    open(os.path.join(ROOT, name), "w").write(text)
    print(name, len(text.split()), "words")
