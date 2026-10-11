# WS10 Technical explainer: insurer capital, investor data templates, fund mechanics, pricing, latest Hayfin news

Prepared 2026-10-11 for a Hayfin Partner Solutions (PSG / IR) intern application. Source IDs S400-S449. Confidence tags: [Confirmed] = primary source or two credible outlets; [Reported] = one credible source; [Inferred] = my own reasoning from cited facts. Worked examples are arithmetic on cited factors and are tagged [Inferred].

---

## 1. Findings

### 1.0 Why this matters for PSG (the one-paragraph version)

Hayfin closed Direct Lending Fund V (DLF V) at more than EUR15bn in July 2026. The raise included a rated note feeder that "contributed approximately $600 million of total investable capital" and that "provides insurers with capital-efficient access" to the strategy [S402] [Confirmed: S402, S416]. Hayfin later wrote that DLF V's rated note feeder was "one of the first priced by a European direct lending manager" [S403] [Reported]. Hayfin also said a "European pension fund, a US institution and an Asian insurer may all want exposure to the same underlying senior-secured loans, but they may not want to access that exposure in the same form" [S403]. In 2026 Hayfin opened a Seoul distribution and IR office after Samsung Life became a strategic minority shareholder [S404] [Confirmed]. So a PSG intern will meet three technical regimes: Solvency II (EU insurers), NAIC RBC (US insurers) and K-ICS (Korean insurers). They will also meet the data templates those investors use (TPT, EET, ILPA) and the fund mechanics behind them.

### 1.1 Solvency II standard formula (EU insurers)

**Legal basis.** The capital factors sit in Commission Delegated Regulation (EU) 2015/35. I could not fetch EUR-Lex directly (it returned an empty bot-check page). I read the article texts from legislation.gov.uk's point-in-time copy of the EU regulation as at 31 Dec 2020 [S406-S413]. That copy includes the 2016, 2017 and 2019 EU amendments (2016/467, 2017/1542, 2019/981). The UK post-Brexit edits in that copy only swap words like "Union" for "United Kingdom". The factor values are the EU values. [Confirmed for factors; the "Union" wording in the EU text is Inferred from the UK edit notes.]

**(a) Fund units with no look-through: equity risk.**
- Art 168(3): type 2 equities include "commodities and other alternative investments". They also include the Art 84 fund exposures "where a look-through approach is not possible" and the insurer does not use the Art 84(3) fallback [S407] [Confirmed].
- Art 169(2)(c): the type 2 shock is "an instantaneous decrease equal to the sum of 49 % and the symmetric adjustment" [S408] [Confirmed]. Type 1 (listed, EEA/OECD) is 39% plus the symmetric adjustment (Art 169(1)(c)) [S408] [Confirmed].
- Art 172(4): today the symmetric adjustment "shall not be lower than -10 % or higher than 10 %" [S409] [Confirmed]. So a type 2 charge today runs from 39% to 59%. The current monthly EIOPA value was not checked (see Gaps).
- **Important nuance.** Art 168(6)(c) treats units in closed-ended AIFs as type 1 (39%), not type 2, when look-through is not possible. Two conditions apply. The fund must be established or marketed in the EU (marketed under AIFMD Art 35 or 40). It must also have "no leverage in accordance with the commitment method" [S407] [Confirmed]. ELTIFs get the same type 1 treatment (Art 168(6)(d)) [S407] [Confirmed].
- [Inferred] The 49% figure that commentators use is therefore the worst case. An unlevered, closed-ended EU direct lending fund could get 39% plus symmetric adjustment without look-through. A levered sleeve (Hayfin notes its levered commingled DLF V assets "more than doubling" from DLF IV [S403]) would not meet the no-leverage test. Its units would sit at 49% without look-through.
- **Long-term equity (LTEI).** Art 169(2)(b) allows 22% for equity that meets the Art 171a long-term equity criteria [S408, S413] [Confirmed]. Art 171a(2) lets the test run at fund level for the Art 168(6)(a)-(d) funds [S413] [Confirmed].

**(b) With look-through (Art 84): loans become spread-risk exposures.**
- Art 84(1): "The Solvency Capital Requirement shall be calculated on the basis of each of the underlying assets of collective investment undertakings and other investments packaged as funds (look-through approach)" [S406] [Confirmed].
- Art 84(3) gives a fallback. If full look-through is not possible, the insurer may use the fund's target allocation or last reported allocation. "Data groupings" are allowed for up to 20% of total assets [S406] [Confirmed].
- Under look-through, each loan is charged under Art 176 spread risk. Most mid-market direct lending borrowers have no ECAI rating. Art 176(4) then sets the unrated, uncollateralised stress at "3 % · dur" for duration up to 5 years [S410] [Confirmed].
- Art 176(2): "dur i shall never be lower than 1". For floating-rate loans, dur is the modified duration "of a fixed interest rate bond or loan of the same maturity and with coupon payments equal to the forward interest rate" [S410] [Confirmed]. So a floating-rate unitranche is not given near-zero duration for spread risk.
- Worked examples [Inferred]: an unrated loan with spread duration 3 gives 3% x 3 = 9%. Duration 4 gives 12%. Duration 5 gives 15%. All are well below 39-49%.
- **Internal assessment route (Art 176a).** Since the 2019 amendments, an unrated loan can be mapped to CQS 2 or CQS 3 if strict criteria are met [S411] [Confirmed]. They include: the borrower's head office is in the EU (UK in the UK copy); there has been no credit event for at least 10 years; "total debt ... no higher than 6,5 times the average of the company's annual free cash flows over the last five financial years"; and average EBITDA at least 6.5x interest expense [S411] [Confirmed].
- [Inferred] Sponsored European direct lending leverage averaged 6.12x EBITDA in 2025 YTD [S445]. Debt of 6.5x free cash flow is a much tighter test than 6.5x EBITDA, and the 6.5x interest cover test also bites. So most sponsor-backed unitranche loans will not qualify for Art 176a. In practice look-through usually means the unrated 3% x duration factor.
- Look-through needs data on every loan. That is why the TPT (section 1.4) exists.

**(c) Rated notes: spread risk by credit quality step (CQS) and duration (Art 176(3)).** For duration up to 5 years the stress is b x dur [S410] [Confirmed]:

| CQS | Typical rating | b (dur up to 5) | Stress at dur 3 [Inferred] | Stress at dur 5 [Inferred] | Band 5-10: a + b(dur-5) |
|---|---|---|---|---|---|
| 0 | AAA | 0.9% | 2.7% | 4.5% | 4.5% + 0.5% |
| 1 | AA | 1.1% | 3.3% | 5.5% | 5.5% + 0.6% |
| 2 | A | 1.4% | 4.2% | 7.0% | 7.0% + 0.7% |
| 3 | BBB | 2.5% | 7.5% | 12.5% | 12.5% + 1.5% |
| 4 | BB | 4.5% | 13.5% | 22.5% | 22.5% + 2.5% |
| 5-6 | B and below | 7.5% | 22.5% | 37.5% | 37.5% + 4.2% |

So, as the brief asks: an A-rated (CQS2) note at 5-year duration carries 7.0%, and a BBB (CQS3) note at 5-year duration carries 12.5% [Inferred from S410]. An unrated loan at the same duration carries 15% (Art 176(4)) [Inferred from S410].

**(d) The securitisation trap.** If a rated note is a "securitisation position", Art 176 does not apply. Art 178 applies instead.
- For non-STS positions (Art 178(8)) the stress is min(b x dur; 1) with b = 12.5% (CQS0), 13.4% (CQS1), 16.6% (CQS2), 19.7% (CQS3), 82% (CQS4), 100% (CQS5-6) [S412] [Confirmed].
- [Inferred] A BBB non-STS tranche at duration 5 would carry 98.5%, against 12.5% for a BBB bond. Whether the feeder's notes count as a securitisation under the EU Securitisation Regulation is therefore the key structuring question for an EU insurer.
- Macfarlanes (Jan 2026): under the delegated act adopted 29 Oct 2025, senior investment-grade non-STS tranches at 5 years "are likely to see" charges "fall by roughly 60% to 80%". It also says a rated note feeder that works for Solvency II insurers, as opposed to NAIC-regulated peers, "remains a work in progress" [S448] [Reported].
- Macfarlanes (July 2026) says note classes in a securitisation structure "will be ranked and not pari passu". It also flags a possible 5% risk retention requirement and reporting and due diligence duties [S418] [Reported].
- Alter Domus also lists EU Securitisation Regulation compliance (risk retention, transparency, due diligence) as an RNF operating burden [S417] [Reported].

**Why a rated note feeder is called "capital-efficient" (summary).**
1. An insurer investing through the feeder holds debt securities, not a fund equity interest. With an ECAI rating the notes get Art 176 bond factors, for example 7-12.5% at 5-year duration for A/BBB. Without look-through, fund units get 39-49% plus the symmetric adjustment [Inferred from S408, S410].
2. A rated note also needs no line-by-line look-through, so the TPT burden is lighter [Inferred].
3. Industry framing: Alter Domus (Oct 2025) works through a EUR50m commitment. At 49% it needs "nearly EUR25 million" of capital. Through a BBB-rated RNF the charge is "9% to 15%", or EUR4.5-7.5m [S417] [Reported; vendor marketing, not a regulator].
4. The caveats are the securitisation classification risk above, rating agency cost and timing, and the equity tranche. Some agencies need equity alongside the notes for an investment-grade rating [S418] [Reported].
5. Rating agency activity: KBRA rated USD17bn of note feeder funds in 2025, against USD8bn in 2024 (per Macfarlanes) [S418] [Reported].

**Solvency II review (2024-2027).**
- Directive (EU) 2025/2 amends the Solvency II Directive. It was published in the Official Journal on 8 January 2025. Member States must transpose it by 29 January 2027, and it applies from 30 January 2027 [S415] [Reported from search snippets of KPMG / EU Monitor; EUR-Lex not fetched]. Debevoise also gives 30 January 2027 as the application date [S414] [Confirmed across S414, S415].
- Commission Delegated Regulation (EU) 2026/269 amends 2015/35. Per Debevoise (2 March 2026) it was published on 18 Feb 2026, entered into force on 10 March 2026, and applies from 30 Jan 2027 [S414] [Reported]. Macfarlanes dates its adoption to 29 Oct 2025 [S448] [Reported].
- Key changes per Debevoise [S414] [Reported]:
  - LTEI is reworked around an ability to "avoid forced sales" for five years under stress.
  - For funds, "the preferential 22% risk factor should generally apply to the equity exposures held within those funds" where fund-level conditions are met.
  - The symmetric adjustment corridor widens to -13% to +13%.
  - Senior STS securitisations are aligned with covered or corporate bonds of comparable rating, and senior non-STS factors are lowered.
  - The risk margin is reduced.
- [Inferred] For private credit specifically, the reform does not change the Art 176 bond and loan factors (no source says it does). The main gains are the securitisation recalibration, which helps RNF/CFO-type notes if classed as securitisation, and LTEI for equity-like fund units.

### 1.2 NAIC (US insurers): RBC, designations, Schedule D vs Schedule BA

**Factors.**
- Akin Gump (Law360, 9 July 2026): "the risk-based capital charge applicable to an insurer's holdings of investment grade debt is generally under 2%, and noninvestment grade debt (not including junk bonds) is generally under 10%, while the RBC for an equity interest in a private fund is 30%" [S419] [Reported; cites MetLife IM].
- MetLife IM's table of life RBC C-1 base factors (pretax, pre-covariance), approved for the 2021 bond factor change [S421] [Confirmed as NAIC-approved values per MetLife; the current NAIC instructions were not separately fetched]:

| NAIC designation | Approx. rating | Life RBC factor |
|---|---|---|
| 1.A | Aaa | 0.16% |
| 1.F | A2 | 0.82% |
| 1.G | A3 | 1.02% |
| 2.A | Baa1 | 1.26% |
| 2.B | Baa2 | 1.52% |
| 2.C | Baa3 | 2.17% |
| 3.B | Ba2 | 4.54% |
| 4.B | B2 | 9.54% |
| 5.C / 6 | Caa3 / Ca | 30.00% |

- Schedule BA "other" assets, including LP interests in private funds, carry a 30% pretax charge [S419, S421 context; S425 snippet of NAIC LR008] [Confirmed across two].
- [Inferred] For a US life insurer, BBB-rated (NAIC 2.B) feeder notes cost about 1.5% of capital against 30% for the LP interest. That is why US insurers drove the RNF market. Macfarlanes notes RNFs "were first designed for US insurers" (via search summary) [S418].

**Principles-based bond definition (PBBD), effective 1 January 2025.**
- The revised SSAP 26R and 43R took effect on 1 Jan 2025. Insurers must decide whether a holding is an issuer credit obligation, an asset-backed security, or neither, before it can go on Schedule D [S423] [Confirmed: Insurance Business Mag Apr 2026; KPMG snippet notes no grandfathering].
- Possible failure points include "debt lacking a substantive creditor relationship, instruments without meaningful credit enhancement, and securities with insufficient or highly uncertain cash flows" [S423] [Reported].
- Akin Gump: the NAIC "has been particularly concerned that rated note feeders and similar vehicles may be used to repackage equity-like exposure without providing meaningful risk mitigation". These concerns "were a driving consideration behind the NAIC's adoption of a principles-based bond definition" [S419] [Reported].
- Mayer Brown's Feb 2025 slides (snippet): a debt security that fails the bond test becomes a "non-bond debt security" under SSAP 21, reported on Schedule BA. Irregular cash flows that depend on manager discretion make bond treatment harder [S425] [SNIPPET].
- Chapman (Jan 2022) argued that rated-debt feeder notes repaid from loan pools differ from CFO debt repaid from PE fund cash flows [S420] [Reported; predates the final rules].

**SVO discretion over filing-exempt (private letter) ratings, from 1 January 2026.**
- The NAIC Financial Condition (E) Committee adopted the procedures on 29 Aug 2024, with an effective date of 1 Jan 2026 [S424] [SNIPPET; HSF Kramer page returned 403].
- Capstone (14 May 2026): the authority "took effect on January 1, 2026, but systems required to operationalize the process are still being developed" [S422] [Reported].
- Mechanics (search summaries of AIMA and HSF Kramer): the SVO can challenge a filing-exempt rating when its view differs by three or more notches. The security is marked "Under Review" and holders get an information request [S424] [SNIPPET].
- Scale: A.M. Best (via Capstone) puts life/annuity insurers' private credit at about USD1 trillion, of which "$419 billion carries private letter ratings" [S422] [Reported]. Akin Gump cites the same USD419bn [S419].
- CLO modelling: the NAIC is moving to direct modelling of CLO C-1 factors. The target has slipped from end-2025 to a proposed year-end 2026 [S423] [Reported].
- RBC review: the RBC Governance Task Force sought comments on Feb 10, 2026 and adopted "11 guiding principles", including "Equal Capital Equal Risk" [S422] [Reported].

### 1.3 Korea K-ICS (Korean insurers, including Samsung Life)

**What was established.**
- K-ICS replaced the old RBC regime in 2023. It is market-consistent and based on the IAIS Insurance Capital Standard with local calibration. It measures risk at a "99.5% confidence level" and covers interest rate, market, credit, operational and insurance risk [S429] [Reported, Skadden Apr 2026].
- The legal minimum is 100%. In practice the FSS encourages 130% or more [S429] [Reported].
- **2025 easing.** In March 2025 the FSS announced a cut in the recommended ratio from 150% to a 130-140% range, plus a new core capital requirement (Fitch via Insurance Business, 1 Apr 2025) [S426] [Reported].
- **Core capital rule from 2027.** The core capital K-ICS ratio counts only paid-in capital and retained earnings. Below 50% triggers prompt corrective action, and 80% is the recommended level. A transition runs to 2035 [S427] [Reported, Seoul Economic Daily 31 Dec 2025, AI-translated].
- **Latest ratios.** At end-June 2026 the industry ratio after transitional measures was 215.2% (life 206.8%). Samsung Life was 208.2%, down 1.8 points. The equity risk charge "increased by 35.2 trillion won" in the quarter [S428] [Reported, Herald 17 Sep 2026].
- **Rated wrappers.** An industry comment (WTW via AsianInvestor) says some Korean insurers have structured alternatives "into a form of structured notes that are 'rated'" to get better risk charging [S430] [SNIPPET; underlying article PAYWALLED-NOT-READ].

**What I could not establish.** I could not find primary or credible secondary text giving the K-ICS shock for fund units without look-through, or credit factors by rating. The 49% "other assets" stress appears in the IAIS ICS (per a BIS summary snippet), but I could not confirm that K-ICS uses the same number. [Gap; do not quote a K-ICS percentage.]

[Inferred] The logic is the same as under Solvency II. Rated debt gets a credit-spread charge. Opaque fund equity gets a high equity charge. Korean insurers are also facing a new core capital ratio and an equity charge that rose with the stock market. Both push them toward capital-light, rated or look-through-friendly forms of European private credit. KRW hedging cost is a further driver (see 1.6).

### 1.4 Tripartite Template (TPT) and European ESG Template (EET)

**What the TPT is.**
- FinDatEx calls the TPT "a widely used European data exchange template designed to support the provision of asset data from asset managers to insurers for Solvency II reporting purposes" [S431] [Confirmed].
- It standardises data for the Solvency II QRTs. It is "not compulsory" and is free of charge and IP rights [S435] [Confirmed].
- **Who maintains it.** FinDatEx (Financial Data Exchange Templates). Its members include EFAMA, Insurance Europe, EBF, EACB, EAPB, ESBG and EUSIPA, and PensionsEurope joined later [S435, S400 site list] [Confirmed]. Club Ampère, a French industry group, originated the template [Inferred from general knowledge; not verified in a fetched source this session].

**Versions.**
- TPT V7 was released on 17 Dec 2024. It could be used from April 2025 with an effective date of 31 March 2025. V6 and V7 ran in parallel in Q2 2025, and FinDatEx recommended full adoption by July 2025 [S432] [Confirmed].
- V7 adds SCR support for callable bonds, "Improved handling of bonds or loans with payment-in-kind features", infrastructure items and dual NACE codes [S432] [Confirmed].
- **TPT V8.** Consultation ran 7 July to 4 Sept 2026. The aim was to validate the final version "by the end of September 2026". Implementation is encouraged from early January 2027 and expected to be mandatory in Q1 2027 [S431] [Confirmed]. V8 adds 2 datapoints for the new Solvency II regime, strengthens issuer identification for concentration risk, and deletes 20 datapoints [S431] [Confirmed]. Whether V8 was finalised in late September 2026 was not verified (Gap).

**What the fund manager supplies (from the V7 workbook, "Version 7 dated 2024/11/25") [S433] [Confirmed].** About 150 numbered fields, in these groups:
- **Portfolio level:** fund ID and name, currency, NAV, valuation and reporting dates, share price, cash ratio, portfolio modified duration, "Complete SCR delivery" flag.
- **Instrument codification:** CIC code, identifier, name.
- **Valuations and exposures:** quantity, nominal, market value in quotation and portfolio currency, valuation weight, market exposure.
- **Interest rate features:** rate type, coupon, reference index (e.g. Euribor), "Interest_rate_margin", frequency, maturity, redemption, call/put dates.
- **Issuer data:** name, LEI-type ID, group, country, NACE sector, securitisation flag, subordination, "Nature of the tranche", "Credit_quality_step".
- **Analytics:** modified duration to maturity and to next option date, credit sensitivity.
- **Optional indicative SCR contributions:** interest rate up/down, equity type 1/2, property, spread on bonds, spread on structured, FX up/down.
- **Other fields:** "Credit_rating", "Rating_agency", valuation method, acquisition value, yield and z-spread, infrastructure flag, type 1 private equity eligibility fields from the 2019 amendments, collateral fields.
- **V7 additions:** custodian ID, bail-in, expected maturity, expected duration, expected credit sensitivity, "PIK", NACE 2.1.

[Inferred] For a direct lending fund, a PSG or reporting team would supply each loan's margin over Euribor, maturity, spread duration, sector, country, rating or internal CQS, and whether it is PIK. Insurers then rebuild Art 176 spread risk from these fields.

**EET (European ESG Template).**
- The EET is FinDatEx's SFDR, MiFID and IDD ESG data template.
- V1.1.3 was published on 18 Dec 2024. FinDatEx recommends using it "as of 1 January 2025" and retiring V1.1.2 "as of 1 July 2025". It implements the ESMA fund naming guidelines and PAB/CTB compliance [S434] [Confirmed].
- An editorial update file dated 10 April 2026 is on the FinDatEx site [S400] [Confirmed that the file exists; contents not opened].

### 1.5 ILPA reporting standards

**ILPA Reporting Template (v2.0) and Performance Templates, released January 2025** (FAQ v1.1 posted April 2025) [S436] [Confirmed].

- **Timing.** ILPA's FAQ says, verbatim in substance [S436] [Confirmed]:
  - Updated Reporting Template: "provided for the first time after Q1 2026 (i.e., ... QTD data as of March 31, 2026)".
  - Performance Template: "provided for the first time after Q1 2027", "with the required data capture beginning in Q1 2026".
  - The new granular breakouts apply going forward to funds starting operations in Q1 2026 or later. Older funds may use an "Other: 2016 ILPA Reporting Template" row.
  - The original target was 1Q 2025, linked to the SEC Private Fund Adviser rule. That rule was vacated, which led to the later dates.
- **Reporting Template changes by section** [S436] [Confirmed]:
  - Cash/Non-Cash Flows: adds offering and syndication costs, placement fees, partner transfers.
  - Management Fees: "Added gross-to-net reconciliation of management fees. Step-by-step netting of rebates, waivers and offsets."
  - Partnership Expenses: internal chargebacks (GP staff and related persons) are split out from external expenses. New external lines include third-party valuations, investigation and examination costs, and "Subscription Facility Fees/Interest".
  - Offsets / Portfolio Company Fees: arrangement, origination and consulting fees are captured. [Inferred] This matters for direct lenders, whose arrangement fees are a key economic term.
  - Carried Interest: the accrued, earned and paid carry reconciliation is merged into the Capital Account Statement.
  - Structure: the Level 1 / Level 2 tiers are removed, and GPs and LPs can no longer modify the template.
- **Performance Templates** [S436] [Confirmed]:
  - Three tables: "Fund Performance", "Gross Portfolio Performance", "Net Portfolio Performance".
  - Net fund-level metrics are required. Gross fund-level metrics are optional.
  - Fund-level metrics are calculated "both with and without the impact of fund-level subscription facilities".
- **Granular vs Gross Up** [S436] [Confirmed]:
  - Granular is for GPs that itemise capital calls. It "excludes calls for fees/expenses, as well as paid/accrued carry, interest, fees, etc. from the gross calculation". The gross multiple is called "Gross Fund-Level MOIC".
  - Gross Up is for GPs that do not itemise calls. It "includes the total amount of capital called" and adds back fees and carry. The result is "a slightly lower gross IRR and TVPI", but "the gross/net spread will be smaller". The gross multiple is called "Gross TVPI".
- **"With" vs "without" subscription line.** The "without" calculation "de-levers the returns by bumping up the start of the IRR calculation to the date capital was first drawn down from the subscription facility". It includes cash flows with the lender [S436] [Confirmed].
- The Net Portfolio Performance table is needed when the template is used for marketing. This supports SEC Marketing Rule compliance [S436] [Confirmed].
- **ILPA Principles 3.0.** The official PDF is dated 2019 and was uploaded in the ilpa.org June 2019 folder [S439] [Confirmed year; the month comes from the URL path].
  - It recommends that "back-first, i.e., whole of fund" waterfalls are "best practice" [S439] [Confirmed].
  - It covers subscription line disclosure [S439] [Confirmed].

### 1.6 Fund mechanics

**Subscription lines and IRR (ILPA 2017 and June 2020).**
- The 2017 parameters were a maximum of 15-25% of uncalled capital and a maximum of 180 days outstanding [S437] [Confirmed].
- The June 2020 guidance asks GPs to show net performance "with and without the use of subscription lines" [S437] [Confirmed].
- ILPA's notional example: the same deal returns IRR 6.62% / TVPI 1.45x with no line, 7.14% / 1.40x with a 1-year line, and 7.98% / 1.35x with a 2-year line [S437] [Confirmed]. The line raises IRR while lowering the multiple, because of interest cost.
- LPs reported actual PE exposure "as much as 2-4 percentage points higher" once their share of sub-line balances is counted [S437] [Confirmed].

**NAV facilities.**
- ILPA published NAV-based facility guidance in July 2024. It notes NAV facilities "have been commonly used in secondaries, private credit, and real estate for some time" [S438] [Confirmed]. Proskauer, via search summary, says the guidance itself is aimed at PE funds [Reported].
- [Inferred] In direct lending, fund-level leverage (asset-backed or NAV facilities) is how "levered" sleeves are built. This is the leverage that would block Art 168(6)(c) type 1 treatment.

**Currency-hedged share classes and feeders.**
- Record (Sept 2025): hedged share classes widen access, and hedging suits "relatively predictable cash flows, such as private credit". Longer-dated forwards "may require the fund to post collateral", and "some liquidity will be required to settle the hedge each time it is rolled" [S447] [Reported].
- [Inferred, labelled]
  - A USD investor in a EUR fund that hedges EUR to USD earns roughly the rate gap as positive carry. VRC shows June 2026 3M Euribor at 2.32% against Fed funds at 3.50-3.75% [S443]. That is a 1.2-1.4% pick-up, before costs.
  - For KRW, the sign and size depend on Bank of Korea rates, which I did not check (Gap).
  - Hayfin's RNF was described in USD ("approximately $600 million") [S402]. This suggests at least part of the feeder was USD-denominated. Which currencies the RNF notes were issued in is not disclosed (Gap).

**Fees, hurdle and carry in direct lending.**
- **Macfarlanes (28 Nov 2024) base case.** An unlevered closed-ended DL fund with "a management fee on net invested capital, a performance fee subject to a preferred return with catch-up" and a 1% headline fee [S440] [Reported].
  - The model gives 10.88% gross IRR. Manager income is roughly 50/50 management and performance fee, and "over half of the manager's income (and all of the performance fee) is received in the last two years".
  - Cutting the fee to 0.75% lifts net IRR to 9.05%.
  - "A 2% management fee would be seen as commercially unviable within direct lending." The average DL fee is "likely slightly under 1%" after discounts.
  - It does not state a hurdle or carry percentage.
- **Cliffwater 2025 survey** (via Swedroe blog, 24 Mar 2025, mostly US lenders) [S441] [Reported, secondary; the blog's totals do not reconcile, so verify]:
  - Unlevered funds: management fee 1.04% average, carry 11.2% average (10% median), hurdle 5.12% average (5.00% median).
  - Levered funds: carry 12.1% with a 6.2% hurdle on GAV-fee funds, and 14.5% with a 6.5% hurdle on NAV-fee funds.
  - Management fees averaged 1.02% on GAV and 1.23% on NAV.
- [Inferred] Senior DL norms are therefore about 1% on invested capital, a 5-6% hurdle with catch-up, and 10-15% carry. PE buyout norms are around 2% and 20% (Proskauer 2026 buyout report via search notes 2% is still most common for small and mid funds). The lower carry reflects a lower target return.

### 1.7 European direct lending pricing, 2025-2026

- **Rothschild (Sept 2025)** [S445] [Confirmed, primary PDF]:
  - "direct lending median spreads at 500bps YTD vs 550bps in 2024 and 613bps in 2023".
  - "YTD sponsored leverage averages 6.12x vs 4.83x syndicated" (FY24: 6.24x and 4.93x).
  - 2Q25 DL volume was EUR12.23bn.
  - Adevinta's EUR6.5bn refinancing of a EUR4.5bn unitranche, "Europe's largest direct lending deal on record".
- **Baird (22 June 2026)** [S442] [Reported]:
  - Q1 2026 unitranche at E+525-625bps (traditional mid-market) and E+500-600bps (upper mid-market).
  - Private-over-public premium about 77bps at end-2025.
  - "storied, cyclical or AI-exposed credits now carry a 50-100bps premium, if they clear at all".
- **VRC (Q2 2026, posted 7 Aug 2026)** [S443] [Reported]:
  - Traditional mid-market (up to about EUR75m EBITDA): issue price about 97.5-98.5, coupon margin about 5.00-6.00%, all-in spread incl. OID about 5.25-6.25%.
  - Upper mid-market: price about 97.5-98.5, margin about 4.75-5.75%, all-in about 5.00-6.00%.
  - Broadly syndicated interest coverage was 2.71x in Q2 2026, against a pre-2022 average of 4.0x.
  - 3M Euribor 2.32% (June). The ECB deposit rate was raised to 2.25% in June 2026, "the first hike in almost three years".
  - DL H1 2026 volume was EUR15.2bn against EUR23.5bn in H1 2025.
- **KBRA DLD (30 Apr 2026)** [S444] [Reported]:
  - Q1 2026 European DL issuance was EUR16.7bn, up 16% YoY.
  - "Euro loans are flirting with sub-8% yields for the first time amid compression across spreads and OIDs".
  - The KBRA DLD Europe default rate was 1% at end-2025.
  - [Note] KBRA's EUR16.7bn and VRC's H1 figure use different datasets, so they do not reconcile.
- **Call protection (Proskauer, May 2023, on 2022 data)** [S446] [Reported, dated]:
  - Make-wholes apply "on a little over 60% of European private credit deals in year one".
  - About 65% of deals have a 2% or 1% premium in year two.
  - "over 80% of deals having no call protection from year three onwards".
  - Large-cap European syndicated deals typically get 101 soft call for six months only.
  - Baird (2026) lists "waived call protection" as a borrower tool [S442].
- **Hayfin's own targeting.** Hayfin targets "middle- and upper-middle-market transactions between EUR100 million and EUR400 million" [S405]. It deployed a record EUR7.1bn in DL over the twelve months to July 2026 and has more than EUR38bn deployed in the strategy since inception [S402] [Confirmed, primary].
- [Inferred synthesis for interview use] 2025-26 European unitranche is roughly E+475-625bps, depending on size and quality, with about 1.5-2.5 points of OID. Sponsored leverage is about 6x, and interest cover is thin at around 2-3x on BSL. Call protection is weak after year two.

### 1.8 Hayfin news, 8-11 October 2026, and fundraising pipeline

- **9 Oct 2026.** Hayfin posted "Opportunities in European Real Estate: Enhancing Opportunistic Credit Portfolios by Adapting to Evolving Markets", a gated report [S401] [Confirmed].
  - It cites "more than EUR4bn invested across European real estate over 15 years".
  - It describes opportunities "from acquiring quality stabilised assets at rebased entry points, to bank capital replacement, to illiquid secondary situations".
  - The Real Estate strategy page was updated the same day [S400] [Confirmed].
- No other Hayfin press release dated 8-11 Oct 2026 was found in the WordPress feed. The previous posts are dated 1 Oct (Seoul office) and 30 Sep (Mergermarket award) [S400] [Confirmed].
- **Special Opportunities Fund IV.** No announcement was found. SOF III closed above its EUR2bn target in December 2021 (Hayfin site, Alternatives Watch, via search) [S449] [SNIPPET].
  - [Inferred] On a typical 4-5 year cycle a successor could be raising in 2026. This is unverified, so do not assert it.
  - Hayfin's 9 Oct real estate piece is framed around "opportunistic credit portfolios" [S401]. This may hint at Special Opportunities marketing [Inferred].
- **Firm metrics.** As of Q2 2026, Hayfin manages about EUR40bn and has invested more than EUR59bn since inception [S405] [Confirmed]. Hayfin named Marc Chowrimootoo as Co-Head of Direct Lending in the award release [S405].

---

## 2. Key numbers table

| Figure | Value | Date | Source | Confidence |
|---|---|---|---|---|
| SII type 2 equity shock | 49% + symmetric adjustment | Reg 2015/35 as amended 2019 | S408 | Confirmed |
| SII type 1 equity shock | 39% + symmetric adjustment | same | S408 | Confirmed |
| SII LTEI / strategic shock | 22% | same | S408 | Confirmed |
| Symmetric adjustment corridor | -10% to +10% now; -13% to +13% from 30 Jan 2027 | 2020 text; Debevoise Mar 2026 | S409, S414 | Confirmed / Reported |
| Closed-ended unleveraged EU AIF units w/o look-through | Type 1 (39%) | Art 168(6)(c) | S407 | Confirmed |
| Unrated loan spread stress | 3% x duration (up to 5y) | Art 176(4) | S410 | Confirmed |
| CQS2 (A) spread stress, dur 5 | 7.0% | Art 176(3) | S410 | Inferred arithmetic |
| CQS3 (BBB) spread stress, dur 5 | 12.5% | Art 176(3) | S410 | Inferred arithmetic |
| Non-STS securitisation b, CQS3 | 19.7% per year of duration | Art 178(8) | S412 | Confirmed |
| Art 176a debt test | total debt no more than 6.5x avg 5y FCF | Art 176a | S411 | Confirmed |
| Data grouping cap (Art 84(3)) | 20% of total assets | Art 84 | S406 | Confirmed |
| Directive 2025/2 application | 30 Jan 2027 | publ. 8 Jan 2025 | S414, S415 | Confirmed |
| Delegated Reg 2026/269 | publ. 18 Feb 2026; in force 10 Mar 2026; applies 30 Jan 2027 | Mar 2026 | S414 | Reported |
| NAIC RBC, private fund LP interest | 30% | 2026 article | S419 | Confirmed (S419 + S425) |
| NAIC 2.B (Baa2) life RBC | 1.52% | 2021 factors | S421 | Confirmed |
| NAIC 1.F (A2) life RBC | 0.82% | 2021 factors | S421 | Confirmed |
| PBBD effective | 1 Jan 2025 | Apr 2026 article | S423 | Confirmed |
| SVO discretion effective | 1 Jan 2026 | May 2026 | S422 | Reported |
| US insurer private credit with PLRs | USD419bn | 2026 | S419, S422 | Confirmed |
| KBRA note feeder ratings | USD17bn (2025) vs USD8bn (2024) | Jul 2026 | S418 | Reported |
| Hayfin DLF V | more than EUR15bn | 2 Jul 2026 | S402 | Confirmed |
| Hayfin DLF V rated note feeder | about USD600m | 2 Jul 2026 | S402, S416 | Confirmed |
| DLF V capital from EMEA | more than half; 10% Middle East | 22 Sep 2026 | S403 | Reported |
| Hayfin DL deployment LTM | EUR7.1bn | Jul 2026 | S402 | Confirmed |
| Hayfin AUM | about EUR40bn; more than EUR59bn invested | Q2 2026 | S405 | Confirmed |
| K-ICS industry ratio | 215.2% (Samsung Life 208.2%) | end-Jun 2026 | S428 | Reported |
| K-ICS recommended ratio | 150% cut to 130-140% | Mar 2025 | S426 | Reported |
| K-ICS core capital minimum | 50% (rec. 80%) from 2027 | Dec 2025 | S427 | Reported |
| TPT V7 release | 17 Dec 2024; use from 31 Mar 2025 | 2024 | S432 | Confirmed |
| TPT V8 | consultation 7 Jul-4 Sep 2026; mandatory Q1 2027 expected | 7 Jul 2026 | S431 | Confirmed |
| TPT V8 deletions | 20 datapoints removed, 2 added | 7 Jul 2026 | S431 | Confirmed |
| EET V1.1.3 | use from 1 Jan 2025 | 18 Dec 2024 | S434 | Confirmed |
| ILPA Reporting Template first use | after Q1 2026 | FAQ v1.1 2025 | S436 | Confirmed |
| ILPA Performance Template first use | after Q1 2027 (data capture from Q1 2026) | FAQ v1.1 2025 | S436 | Confirmed |
| ILPA 2017 sub line parameters | 15-25% of uncalled; 180 days | Jun 2020 doc | S437 | Confirmed |
| ILPA sub line IRR example | 6.62% / 7.14% / 7.98% | Jun 2020 | S437 | Confirmed |
| DL base-case mgmt fee | 1% on net invested capital | Nov 2024 | S440 | Reported |
| Unlevered DL carry / hurdle (Cliffwater) | 11.2% / 5.12% avg | 2025 | S441 | Reported (secondary) |
| Levered DL carry / hurdle (GAV fee) | 12.1% / 6.2% | 2025 | S441 | Reported (secondary) |
| European DL median spread | 500bps YTD 2025 (550 in 2024; 613 in 2023) | Sep 2025 | S445 | Confirmed |
| Sponsored DL leverage | 6.12x (vs 4.83x BSL) | 2025 YTD | S445 | Confirmed |
| Unitranche margin, traditional MM | E+525-625bps | Q1 2026 | S442 | Reported |
| Unitranche margin, upper MM | E+500-600bps | Q1 2026 | S442 | Reported |
| Unitranche issue price (OID) | about 97.5-98.5 | Q2 2026 | S443 | Reported |
| BSL interest coverage | 2.71x | Q2 2026 | S443 | Reported |
| 3M Euribor | 2.32% | Jun 2026 | S443 | Reported |
| European DL Q1 2026 volume | EUR16.7bn, +16% YoY | Apr 2026 | S444 | Reported |
| Year 3+ no call protection | more than 80% of European deals | 2022 data | S446 | Reported |

---

## 3. Verbatim quotes actually read

- "The Solvency Capital Requirement shall be calculated on the basis of each of the underlying assets of collective investment undertakings and other investments packaged as funds (look-through approach)." [S406]
- "an instantaneous decrease equal to the sum of 49 % and the symmetric adjustment as referred to in Article 172 of this Regulation, in the value of type 2 equities" [S408]
- "The symmetric adjustment shall not be lower than - 10 % or higher than 10 %." [S409]
- "For variable interest rate bonds or loans, dur i shall be equivalent to the modified duration of a fixed interest rate bond or loan of the same maturity and with coupon payments equal to the forward interest rate." [S410]
- "the total debt of the company at the end of the most recent financial year for which figures are available is no higher than 6,5 times the average of the company's annual free cash flows over the last five financial years" [S411]
- "The DLF V fundraise also includes the successful close of a rated note feeder which contributed approximately $600 million of total investable capital. The structure, advised on by Proskauer as Legal Counsel, provides insurers with capital-efficient access to Hayfin's European Direct Lending strategy" [S402]
- "DLF V's rated note feeder, one of the first priced by a European direct lending manager, was designed with exactly that in mind: giving insurers a more capital-efficient route into the strategy without changing the underlying investment." [S403]
- "A European pension fund, a US institution and an Asian insurer may all want exposure to the same underlying senior-secured loans, but they may not want to access that exposure in the same form." [S403]
- "Investment consultant involvement in DLF V was also greater than in any prior Hayfin fundraise." [S403]
- "the risk-based capital charge applicable to an insurer's holdings of investment grade debt is generally under 2%, and noninvestment grade debt (not including junk bonds) is generally under 10%, while the RBC for an equity interest in a private fund is 30%." [S419]
- "the NAIC has been particularly concerned that rated note feeders and similar vehicles may be used to repackage equity-like exposure without providing meaningful risk mitigation." [S419]
- "took effect on January 1, 2026, but systems required to operationalize the process are still being developed." [S422]
- "remains a work in progress" (on RNFs for Solvency II insurers) [S448]
- "The TPT is a widely used European data exchange template designed to support the provision of asset data from asset managers to insurers for Solvency II reporting purposes." [S431]
- "Management Fees: Added gross-to-net reconciliation of management fees. Step-by-step netting of rebates, waivers and offsets." [S436]
- "The 'without' calculation de-levers the returns by bumping up the start of the IRR calculation to the date capital was first drawn down from the subscription facility" [S436]
- "the parameters prescribed in 2017 guidance with respect to maximum percentage of uncalled capital (15-25%) and maximum days outstanding on the subscription line (180 days) were most relevant to private equity" [S437]
- "a management fee on net invested capital, a performance fee subject to a preferred return with catch-up" [S440]
- "A 2% management fee would be seen as commercially unviable within direct lending." [S440]
- "Pricing compressed, with direct lending median spreads at 500bps YTD vs 550bps in 2024 and 613bps in 2023" [S445]
- "YTD sponsored leverage averages 6.12x vs 4.83x syndicated" [S445]
- "Euro loans are flirting with sub-8% yields for the first time amid compression across spreads and OIDs." [S444]
- "make-wholes only now apply on a little over 60% of European private credit deals in year one" [S446]
- "Drawing on more than EUR4bn invested across European real estate over 15 years, Hayfin applies a credit-oriented discipline" (original uses the euro symbol) [S401]

---

## 4. Source table

[S400] | Hayfin (WordPress JSON API: posts and pages; FinDatEx site index also read) | Hayfin posts feed per_page=8; pages modified after 2026-10-07 | 2026-10-09 (latest item) | https://www.hayfin.com/wp-json/wp/v2/posts?per_page=5 | Accessed 2026-10-11 | FETCHED | Primary, firm-controlled; also FinDatEx homepage https://findatex.eu/ read for file list and members
[S401] | Hayfin | Opportunities in European Real Estate: Enhancing Opportunistic Credit Portfolios by Adapting to Evolving Markets | 2026-10-09 | https://www.hayfin.com/opportunities-in-european-real-estate-enhancing-opportunistic-credit-portfolios-by-adapting-to-evolving-markets/ | Accessed 2026-10-11 | FETCHED | Primary; full report gated, only landing text read
[S402] | Hayfin | Hayfin announces record close of Direct Lending Fund V in excess of EUR15bn | 2026-07-02 | https://www.hayfin.com/hayfin-announces-record-close-of-direct-lending-fund-v-in-excess-of-e15bn/ | Accessed 2026-10-11 | FETCHED | Primary
[S403] | Hayfin | What a EUR15bn Fundraise Tells Us About the Evolution of European Private Credit | 2026-09-22 | https://www.hayfin.com/what-a-e15bn-fundraise-tells-us-about-the-evolution-of-european-private-credit/ | Accessed 2026-10-11 | FETCHED | Primary, firm opinion piece
[S404] | Hayfin | Hayfin deepens Korean market presence with Seoul office opening | 2026-10-01 | https://www.hayfin.com/hayfin-deepens-korean-market-presence-with-seoul-office-opening/ | Accessed 2026-10-11 | FETCHED | Primary; corroborated by Alternatives Watch and Korea Herald headlines in search
[S405] | Hayfin | Hayfin named Private Credit Lender of the Year at ION Analytics Mergermarket Private Equity Awards 2026 | 2026-09-30 | https://www.hayfin.com/hayfin-named-private-credit-lender-of-the-year-at-ion-analytics-mergermarket-private-equity-awards-2026/ | Accessed 2026-10-11 | FETCHED | Primary
[S406] | legislation.gov.uk (copy of EU text) | Delegated Regulation (EU) 2015/35, Article 84 (point in time 2020-12-31) | 2014-10-10 as amended | https://www.legislation.gov.uk/eur/2015/35/article/84/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official text copy; EUR-Lex blocked by bot check
[S407] | legislation.gov.uk | Delegated Regulation (EU) 2015/35, Article 168 | as amended to 2020 | https://www.legislation.gov.uk/eur/2015/35/article/168/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official copy; UK wording edits noted
[S408] | legislation.gov.uk | Delegated Regulation (EU) 2015/35, Article 169 (as substituted by 2019/981) | as amended to 2020 | https://www.legislation.gov.uk/eur/2015/35/article/169/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official copy
[S409] | legislation.gov.uk | Delegated Regulation (EU) 2015/35, Article 172 | as amended to 2020 | https://www.legislation.gov.uk/eur/2015/35/article/172/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official copy; corridor changes from 2027 per S414
[S410] | legislation.gov.uk | Delegated Regulation (EU) 2015/35, Article 176 | as amended to 2020 | https://www.legislation.gov.uk/eur/2015/35/article/176/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official copy; factor table read in full
[S411] | legislation.gov.uk | Delegated Regulation (EU) 2015/35, Article 176a | as inserted by 2019/981 | https://www.legislation.gov.uk/eur/2015/35/article/176a/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official copy
[S412] | legislation.gov.uk | Delegated Regulation (EU) 2015/35, Article 178 | as amended to 2020 | https://www.legislation.gov.uk/eur/2015/35/article/178/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official copy; pre-2027 calibration
[S413] | legislation.gov.uk | Delegated Regulation (EU) 2015/35, Article 171a | as inserted by 2019/981 | https://www.legislation.gov.uk/eur/2015/35/article/171a/2020-12-31 | Accessed 2026-10-11 | FETCHED | Official copy; criteria replaced from 2027 per S414
[S414] | Debevoise & Plimpton | European Commission Adopts Amendments to the Solvency II Delegated Regulation | 2026-03-02 | https://www.debevoise.com/insights/publications/2026/03/european-commission-adopts-amendments-to-the-solve | Accessed 2026-10-11 | FETCHED | Law firm; OJ text of 2026/269 not read
[S415] | KPMG Klardenker / EU Monitor (search results) | Revised Solvency II Directive published in OJ (Directive (EU) 2025/2) | 2025-01 | https://klardenker.kpmg.de/financialservices-hub/regulatory-update/ueberarbeitete-solvency-ii-richtlinie-im-eu-amtsblatt-veroeffentlicht/ | Accessed 2026-10-11 | SNIPPET | Dates consistent with S414
[S416] | Proskauer | Proskauer Advises Hayfin Capital Management on Close of Rated Note Feeder for DLF V Fundraise | 2026-07-07 | https://www.proskauer.com/release/proskauer-advises-hayfin-capital-management-on-close-of-rated-note-feeder-for-dlf-v-fundraise | Accessed 2026-10-11 | FETCHED | Law firm release; rating agency not named
[S417] | Alter Domus | Unlocking Capital Efficiency: Why Insurers Are Turning to Rated Note Feeders | 2025-10-15 | https://alterdomus.com/insight/rated-note-feeders-capital-relief/ | Accessed 2026-10-11 | FETCHED | Fund administrator marketing; numbers illustrative
[S418] | Macfarlanes (via Mondaq) | Rated Note Feeders: Structuring Access To Private Capital | 2026-07-12 | https://www.mondaq.com/uk/fund-finance/1815512/rated-note-feeders-structuring-access-to-private-capital | Accessed 2026-10-11 | FETCHED | Law firm; KBRA volume figure second-hand
[S419] | Akin Gump (Law360 reprint) | How Rated Note Feeders Help Insurers Tap Private Credit | 2026-07-09 | https://www.akingump.com/a/web/oe1DTVT3a6bPV1LACkQiEe/law360-how-rated-note-feeders-help-insurers-tap-private-credit.pdf | Accessed 2026-10-11 | FETCHED | Law firm; PDF read via pdftotext
[S420] | Chapman and Cutler | Rated Debt Feeder Structure: NAIC regulatory accounting treatment | 2022-01-13 | https://chapman.com/publication-rated-debt-feeder-structure-naic-regulatory-accounting-treatment | Accessed 2026-10-11 | FETCHED | Law firm; predates final PBBD
[S421] | MetLife Investment Management (InsuranceAUM Journal reprint) | A Very Long Engagement: Asset Allocation Implications of U.S. Life Insurance RBC Changes | 2021 (Q3) | https://insuranceaum.com/sites/default/files/pdf/InAUMJournal-Q3-2021-mim-a-very-long-engagement.pdf | Accessed 2026-10-11 | FETCHED | Asset manager research; NAIC factor table
[S422] | Capstone DC | Insurers' Increasing Exposure to Private Credit Attracts Regulators' Scrutiny | 2026-05-14 | https://capstonedc.com/?p=54390 | Accessed 2026-10-11 | FETCHED | Policy research firm; cites A.M. Best
[S423] | Insurance Business Magazine | NAIC tightens grip on insurers' investment risk with bond and CLO overhaul | 2026-04-20 | https://www.insurancebusinessmag.com/us/news/claims/naic-tightens-grip-on-insurers-investment-risk-with-bond-and-clo-overhaul-572390.aspx | Accessed 2026-10-11 | FETCHED | Trade press
[S424] | HSF Kramer / AIMA (search results) | NAIC committee adopts new procedures allowing discretion on rated securities | 2024-08 | https://www.hsfkramer.com/insights/2024-08/naic-committee-adopts-new-procedures-allowing-discretion-on-rated-securities | Accessed 2026-10-11 | SNIPPET | Page returned 403; adoption date 29 Aug 2024 from snippet
[S425] | Mayer Brown; NAIC LR008 (search results) | Insurance company investment slides (Feb 2025); LR008 instruction change | 2025 | https://mayerbrown.com/-/media/files/perspectives-events/events/2025/02/insurance-company-investment-slides.pdf | Accessed 2026-10-11 | SNIPPET | NBDS/Schedule BA and 30% factor from snippets
[S426] | Insurance Business Asia (Fitch) | New Korean capital rules ease insurers' burden | 2025-04-01 | https://insurancebusinessmag.com/asia/news/breaking-news/new-korean-capital-rules-ease-insurers-burden--fitch-ratings-530437.aspx | Accessed 2026-10-11 | FETCHED | Trade press citing Fitch
[S427] | Seoul Economic Daily | Korea to Introduce Core Capital Rules for Insurers From 2027 | 2025-12-31 | https://en.sedaily.com/finance/2025/12/31/korea-to-introduce-core-capital-rules-for-insurers-from-2027 | Accessed 2026-10-11 | FETCHED | Korean press, AI-translated per outlet
[S428] | Herald Corp (Herald Business) | Post-transitional-measure ratio as of end-June falls 0.8 percentage points | 2026-09-17 | https://biz.heraldcorp.com/article/10876878 | Accessed 2026-10-11 | FETCHED | Korean press citing FSS data
[S429] | Skadden | The Standard Formula: Encyclopaedia of Prudential Solvency, Ch. 13 Korea | 2026-04 | https://www.skadden.com/insights/publications/2026/04/chapter-13-the-prudential-solvency-regime-in-korea | Accessed 2026-10-11 | FETCHED | Law firm; no factor detail
[S430] | AsianInvestor (WTW comment) | Korean insurers looking to get their K-ICS from more alts | 2019-02-26 | https://asianinvestor.net/article/korean-insurers-looking-to-get-their-k-ics-from-more-alts/450100 | Accessed 2026-10-11 | PAYWALLED | PAYWALLED-NOT-READ beyond intro; WTW quote from search snippet only
[S431] | FinDatEx | FinDatEx launches public consultation on TPT V8 | 2026-07-07 | https://findatex.eu/news/91/findatex-launches-public-consultation-on-tpt-v8 | Accessed 2026-10-11 | FETCHED | Primary standard-setter
[S432] | FinDatEx | FinDatEx Releases Updated TPT V7 Template | 2024-12-17 | https://findatex.eu/news/82/findatex-releases-updated-tpt-v7-template | Accessed 2026-10-11 | FETCHED | Primary
[S433] | FinDatEx | TPT_V7 20241125_updated.xlsx (template workbook) | 2024-11-25 | https://findatex.eu/mediaitem/ac6fc8a5-67b0-4f4b-ad74-1487b5a4ceaa/TPT_V7++20241125_updated.xlsx | Accessed 2026-10-11 | FETCHED | Primary; field list parsed
[S434] | FinDatEx | FinDatEx publishes EET V1.1.3 | 2024-12-18 | https://findatex.eu/news/84/findatex-publishes-eet-v1-1-3 | Accessed 2026-10-11 | FETCHED | Primary
[S435] | FinDatEx | FinDatEx platform publishes fifth version of Solvency II template | 2020-01-16 | https://findatex.eu/news/37/findatex-platform-publishes-fifth-version-of-solvency-ii-template | Accessed 2026-10-11 | FETCHED | Primary; membership list
[S436] | ILPA | Frequently Asked Questions: ILPA Reporting Template and ILPA Performance Templates (v1.1) | 2025-04 (released Jan 2025) | https://ilpa.org/wp-content/uploads/2025/04/ILPA-Templates-FAQs-v1.1.pdf | Accessed 2026-10-11 | FETCHED | Primary
[S437] | ILPA | Enhancing Transparency Around Subscription Lines of Credit | 2020-06 | https://ilpa.org/wp-content/uploads/2020/06/ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf | Accessed 2026-10-11 | FETCHED | Primary
[S438] | ILPA | NAV-Based Facilities: Guidance for Limited Partners and General Partners | 2024-07 | https://ilpa.org/wp-content/uploads/2024/07/ILPA-Guidance-on-NAV-Facilities-2024.pdf | Accessed 2026-10-11 | FETCHED | Primary; first pages read
[S439] | ILPA | ILPA Principles 3.0: Fostering Transparency, Governance and Alignment of Interests | 2019 (June upload folder) | https://ilpa.org/wp-content/uploads/2019/06/ILPA-Principles-3.0_2019.pdf | Accessed 2026-10-11 | FETCHED | Primary; month inferred from URL
[S440] | Macfarlanes | The evolution of direct lending fund fee structures | 2024-11-28 | https://www.macfarlanes.com/insights/102loh7/the-evolution-of-direct-lending-fund-fee-structures/ | Accessed 2026-10-11 | FETCHED | Law firm; modelled scenarios
[S441] | Larry Swedroe Substack (summarising Cliffwater) | 2025 Private Credit Fund Expenses | 2025-03-24 | https://larryswedroe.substack.com/p/2025-private-credit-fund-expenses | Accessed 2026-10-11 | FETCHED | Secondary; mostly US; internal totals inconsistent
[S442] | Baird | European Debt Markets Q2 2026: Looking Through the Noise | 2026-06-22 | https://www.rwbaird.com/corporations-and-institutions/investment-banking/insights/2026/06/looking-through-the-noise/ | Accessed 2026-10-11 | FETCHED | Investment bank commentary
[S443] | VRC via EACCNY | European Private Market Trends: Q2 2026 Direct Lending and Private Equity Update | 2026-08-07 | https://eaccny.com/news/vrc-european-private-market-trends-q2-2026-direct-lending-private-equity-update/ | Accessed 2026-10-11 | FETCHED | Valuation firm; page has typos
[S444] | KBRA DLD | Europe Insights and Outlook Report: 1Q26 volume rises 16% YoY to EUR16.7B | 2026-04-30 | https://www.kbra.com/analytics/products/dld/insights/europe-insights-outlook-report-1q26-volume-rises-16-yoy-to-16-7b | Accessed 2026-10-11 | FETCHED | Rating agency data; full report login-gated
[S445] | Rothschild & Co | European Leveraged Finance Market: September Update | 2025-09 | https://www.rothschildandco.com/siteassets/publications/rothschildandco/global_advisory/2025/growth_equity_update/09/european-leveraged-finance-market---september-update.pdf | Accessed 2026-10-11 | FETCHED | Adviser; sources Debtwire, LCD, PitchBook
[S446] | Proskauer | Private Credit Deep Dives: Call Protection (Europe) | 2023-05-22 | https://proskauer.com/alert/private-credit-deep-dives-call-protection | Accessed 2026-10-11 | FETCHED | Law firm; 2022 deal data, dated
[S447] | Record Financial Group | Private Wealth and the Increasing Importance of Share Class Hedging for Private Fund Managers | 2025-09-15 | https://recordfg.com/private-wealth-and-the-increasing-importance-of-share-class-hedging-for-private-fund-managers/ | Accessed 2026-10-11 | FETCHED | Currency manager; qualitative
[S448] | Macfarlanes | Insurers and the EU securitisation reforms: an asset class finally unlocked? | 2026-01-15 | https://www.macfarlanes.com/insights/102m1xa/insurers-and-the-eu-securitisation-reforms-an-asset-class-finally-unlocked/ | Accessed 2026-10-11 | FETCHED | Law firm
[S449] | Hayfin / Alternatives Watch / 9fin (search results) | Hayfin exceeds EUR2bn target for Special Opportunities Fund III; Hayfin to exceed EUR10bn target for fifth direct lending fund | 2021-12 / 2026-03-05 | http://www.hayfin.com/hayfin-exceeds-e2-2bn-target-special-opportunities-fund-iii/ | Accessed 2026-10-11 | SNIPPET | No SOF IV found

Search log (more than 20 WebSearch queries run): Solvency II delegated act 2025-26; rated note feeder Solvency II; NAIC RNF PBBD; SVO discretion (x2); NAIC RBC factors; K-ICS (x5 incl. Korean language); TPT V7; ILPA template; ILPA guidance; Macfarlanes fees; DL fee survey; unitranche pricing 2026; leverage and call protection (x2); Hayfin SOF IV (x2); ILPA Principles 3.0; FX hedged share classes; RNF securitisation; Directive 2025/2; Hayfin October 2026.

---

## 5. Gaps

1. **EUR-Lex not readable.** The factor values come from the legislation.gov.uk copy of the EU text as at end-2020. I did not read the OJ text of Delegated Regulation 2026/269, so the post-2027 LTEI wording and securitisation factors come from law firms only (S414, S448).
2. **Current symmetric adjustment.** I did not retrieve EIOPA's monthly published value for September 2026, so the live type 2 charge (49% plus SA) is not stated.
3. **Classification of Hayfin's RNF.** No source says how Hayfin's RNF is structured: which rating agency, ratings, tranches, currency, or whether EU insurers or only US insurers bought it. The USD figure suggests US insurers, but that is Inferred.
4. **K-ICS factors.** The equity shock for fund units, the look-through rules, and credit factors by rating were not found in any primary or credible secondary source. Do not quote 49% for K-ICS.
5. **NAIC.** The current life RBC instructions (LR008 / LR002) were not fetched directly, and the 30% BA factor rests on Akin and a snippet. The SVO discretion adoption (29 Aug 2024) is snippet-only. Whether the SVO has actually challenged any RNF notes is unknown.
6. **TPT V8 final.** I did not verify whether V8 was validated at end-September 2026. Club Ampère's origin role was not confirmed in a fetched source this session.
7. **European fee and terms survey.** I found no Europe-specific survey of DL hurdle and carry. The Cliffwater data is US-heavy and comes via a blog with arithmetic inconsistencies. No 2025-26 European call protection dataset was found; Proskauer's is 2022 data. No current European DL leverage figure for 2026 was found; Rothschild's 6.12x is 2025 YTD.
8. **FX hedging.** Bank of Korea and RBA policy rates and KRW/AUD hedge costs were not checked. Whether DLF V offers hedged share classes is not disclosed.
9. **Hayfin SOF IV.** No evidence either way of a 2026 raise. Do not claim it is in market.
10. **Directive 2025/2 publication date (8 Jan 2025)** is from search snippets, not a fetched OJ page.

---

## 6. Interview angles (PSG / IR intern)

1. **Know the RNF story cold.** "DLF V raised more than EUR15bn, including about USD600m through a rated note feeder, which Hayfin calls one of the first priced by a European direct lending manager. The point is the same loans in a different wrapper. A BBB note costs an EU insurer about 12.5% of capital at 5-year duration, against 39-49% for fund units without look-through. For a US life insurer it is about 1.5% against 30%." Then add the caveat: if the notes count as a securitisation, EU charges can be far higher. That is why Macfarlanes calls Solvency II RNFs "a work in progress". (S402, S403, S408, S410, S412, S419, S448)
2. **Show you understand look-through and data.** Insurers can avoid the equity charge by looking through to the loans, but only if the manager sends clean loan-level data in the TPT. TPT V8 becomes mandatory around Q1 2027 alongside the Solvency II review. A PSG intern who can explain why the "Interest_rate_margin", "Credit_quality_step" and "PIK" fields matter is useful on day one. (S406, S431, S433)
3. **Korea angle.** Samsung Life is a shareholder, and Hayfin opened Seoul on 1 Oct 2026. Korean insurers face a new 50% core capital minimum from 2027, and their equity risk charges jumped in 2026. Capital-light, rated or look-through-friendly products and KRW hedging are likely to come up. Be honest that you do not know the exact K-ICS fund factors. (S404, S427, S428)
4. **ILPA reporting.** Mention that the updated ILPA Reporting Template applies from Q1 2026 data, with gross-to-net management fee reconciliation and arrangement fee offsets. The Performance Template follows from Q1 2027 in Granular or Gross Up form, with and without subscription lines. This links directly to the JD task of "assisting with quarterly LP reporting". (S436)
5. **DDQ-ready numbers.** European unitranche is roughly E+500-625bps, with OID about 1.5-2.5 points. Sponsored leverage is about 6x. Most European deals have little call protection after year two. Hayfin targets EUR100-400m tickets. These numbers help when proofreading pitch books or answering RFP questions on market context. (S442, S443, S445, S446, S405)
6. **Fees conversation.** DL economics are about 1% on invested capital, a 5-6% hurdle with catch-up, and 10-15% carry, against 2/20 in buyout. Macfarlanes shows fee cuts mostly happen through side letters and size or early-bird discounts. This is useful for understanding MFN and side letter work in PSG. (S440, S441)
7. **Latest-news hook.** On 9 Oct 2026 Hayfin published a European real estate opportunistic credit report citing more than EUR4bn invested over 15 years. A good question for an interviewer: "How do insurers' capital rules shape demand for your opportunistic and real estate credit products versus direct lending?" (S401)
8. **Question to ask.** "With the Solvency II review applying from 30 January 2027, do you expect European insurers to use the RNF route too, or mainly look-through into the commingled fund?" This shows you read beyond the press release. (S414, S448)
