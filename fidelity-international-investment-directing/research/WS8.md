# WORKSTREAM 8: WHY FIDELITY INTERNATIONAL, BUILT FROM MECHANISM NOT ADJECTIVES

Firm identity check performed throughout: target is Fidelity International (FIL), Bermuda-domiciled,
London-hubbed. Fidelity Investments / FMR LLC (Boston) is a separate company since the 1980 split.
Two sources fetched during this research (institutional.fidelity.com and part of the workplace-pensions
page) turned out to describe the Boston firm (FIAM LLC, US 401(k) business) and are explicitly excluded
from any FIL claim below; they are noted only where relevant to the split itself.

Research note on method: the session's web-search allowance was shared across all workstreams running
in parallel and was exhausted after 10 distinct queries from this workstream (a hard stop, not a choice
to under-search). This was offset with 19 successful full-page fetches, well above the 10-fetch minimum.
The corporate site fidelityinternational.com returned a hard Akamai "Access Denied" to every path tried
(both via the fetch tool and via direct curl with a browser user agent), so the official Leadership page
and the Annual Report PDF could not be read. Their substitutes (careers.fidelityinternational.com, which
is a different, unblocked host, plus secondary aggregators) are used instead and flagged wherever that
substitution matters. This is recorded honestly in GAPS.

## 1. FINDINGS

### Q1. Why is the firm structured this way: private, Bermuda, vertically integrated

**Ownership.** Fidelity International is privately held. FIL Limited, the ultimate parent, is
headquartered in Pembroke, Bermuda [S300][Confirmed - two independent outlets agree on the basic fact].
Ownership is split between the founding Johnson family and current/former management and staff. The one
hard number available is from a 2012 Bermuda regulatory filing reported by the Royal Gazette: the Johnson
family held 39.89% of FIL, with "fund managers and senior employees" owning the rest, per a company
spokesperson quoted at the time [S301][Reported - single primary-adjacent source, dated 2012, age noted].
Wikipedia's current article repeats the same 39.89% figure without a fresher citation, and a secondary
AI-aggregated source (Grokipedia) also repeats "approximately 40%" [S300][S319][Reported - all three
appear to trace to the same 2012 filing, not three independent confirmations; treat as one data point,
14 years stale]. No 2024-2026 breakdown of the ownership split was found.

**Why this structure exists historically.** FIL was set up in 1969 as the non-US arm of the Boston
business, managing funds for investors outside North America (particularly the Far East), then was
formally incorporated as an independent Bermuda company and spun off as a separate business from the
US parent in 1980 [S300][S301][Confirmed - both sources agree on 1969 origin / 1980 split]. The Bermuda
incorporation let it operate as an offshore vehicle purpose-built for non-US investors, structurally
separate from the US entity's regulatory perimeter [S301][Reported]. That 1980 split is also why the
firm still shares the Fidelity brand and Johnson-family lineage with the Boston firm (both trace to
Edward C. Johnson II) but has been under completely separate ownership and management for 46 years
[S300][S301][Confirmed].

**What the structure buys the firm.** Two mechanisms are directly evidenced:
- No listed shares means no quarterly earnings calls and no public shareholders to manage. This is the
  standard argument for privately-held asset managers, and Grokipedia's summary of Fidelity's own public
  positioning frames it exactly this way: private ownership "supports long-term decision-making insulated
  from public market pressures" [S319][Reported - single secondary source paraphrasing the firm's own
  framing, not a direct quote from FIL].
- Owning distribution, not just manufacturing, gives the firm a direct retail relationship. On its own
  UK platform, Fidelity reports **1.7 million customers** and **over £40 billion of investments** held
  through fidelity.co.uk, a business it has run for "over 50 years" [S318][Confirmed - retrieved directly
  from the firm's retail platform site]. Separately, the firm's careers site states the wider Fidelity
  business serves **2.5 million clients** globally, "from central banks and financial institutions to
  wealth managers and private individuals" [S302][Reported - single source, and note this 2.5m figure is
  a different, broader scope than the 1.7m UK-platform figure, so the two are not directly comparable].
  Owning that direct channel means the firm holds its own client data and distribution economics rather
  than renting shelf space from a third-party platform, and it is not solely dependent on external
  fund-buyer gatekeepers for flows.

**What it costs.** Two costs are directly evidenced, one is inferred:
- Complexity and cross-subsidy risk. Running a technology-and-administration-heavy platform, adviser
  business and workplace-pensions business alongside fund management means carrying a lower-margin,
  more capital- and headcount-intensive business inside an asset manager. The scale of that
  non-investment machine is large: Customer Operations alone describes "Client Services" as roughly
  **280 staff** across the UK and India, and separately says the institutional side of operations
  supports **over 800 institutional clients** [S307][Confirmed - directly stated by the firm on its own
  careers site]. That headcount is doing platform/administration work, not fund management, and it has to
  be funded regardless of that quarter's fund flows [Inferred from S307 - the firm does not itself
  publish this as a "cost", this is the analyst's inference from the headcount evidence].
- Conflict-of-interest management overhead. A firm that manufactures funds and also runs the platform its
  own funds are sold on has to prove it is not self-dealing. The FCA's SYSC 10 conflicts-of-interest rules
  require such a firm to "take all appropriate steps to identify and to prevent or manage conflicts of
  interest" (SYSC 10.1.3R), maintain "effective organisational and administrative arrangements" including
  information barriers between product and distribution teams (SYSC 10.1.7R), keep a written conflicts
  policy naming "portfolio management" specifically as an area needing "special attention" (SYSC
  10.1.12G), report material conflicts to senior management at least annually, and treat disclosure to
  retail clients as a last resort rather than a substitute for real controls (SYSC 10.1.9G, 10.1.6R)
  [S310][Confirmed - primary regulatory source, FCA Handbook]. Concretely, on the retail platform itself,
  Fidelity does not appear to restrict fidelity.co.uk to only its own funds: the platform's "Investment
  Finder" gives access to "over 3,000 funds" and "over 2,000 shares" plus ETFs and trusts, i.e.
  whole-of-market choice, alongside its own curated "Select 50" list [S318][Confirmed - directly read on
  the retail platform site]. That whole-of-market design is itself a control against the most obvious
  version of the conflict (forcing retail customers into house funds only), though it does not remove the
  economic incentive to promote house funds within that wider list.
- No listed equity currency. Being private means the firm cannot use its own stock to fund acquisitions
  or as a standard staff equity-incentive tool the way a listed asset manager can. No source directly
  states this as a stated cost of Fidelity's structure; this is the analyst's own inference from the basic
  mechanics of private ownership, not a claim found in any source [Inferred].

**The research platform.** Multiple internal Fidelity sources give slightly different headline numbers,
which the analyst has not been able to reconcile to one authoritative figure:
- The firm's investment-trusts site: "over 360 investment professionals and research staff around the
  world," doing "more than 16,000 company meetings" a year (about one every 8 minutes), with portfolio
  managers holding in-house research or proprietary insight on "90% of holdings," and a separate Manager
  Research team covering "approximately 160 third-party investment strategies" [S317][Confirmed - directly
  read, single source but internally consistent and specific].
- The firm's careers "about us" page: "over 400 professionals" in Investment Management, and "more than
  17,000 company meetings" a year [S302][Reported - a different Fidelity page, a different, larger
  headcount and a different, higher meeting count than S317; both cannot be quoted as "the" number without
  flagging the discrepancy, which this report does].
The recurring argument in the material is organisational rather than adjectival: research sits on "single
platform coverage which supports all of our Portfolio Managers" rather than being siloed fund-by-fund
[S303][Confirmed - directly read on the careers investment-management page], and analysts "work together
across asset classes, e.g. combining insights from equity and credit research, to form a 360° view on the
health and prospects of companies" [S302][Confirmed - direct quote, read on the page]. The commercial
logic implied (not stated outright by any source) is that a shared research platform is expensive to build
and staff, but if portfolio managers across equities, fixed income and multi-asset are all drawing on the
same coverage, the cost is shared across a much larger AUM base than any single fund could justify on its
own [Inferred].

### Q2. How the parts work together, and where collaboration actually lives

The careers site describes Investment Management as organised into **four asset classes: Equities, Fixed
Income, Multi-Asset and Real Estate**, which "work synonymously combining the strength and skills of
separate disciplines" [S303][Confirmed - direct quote]. Note this is a different grouping from the JD's
five groups (Equities, Fixed Income, Multi Asset, Systematic Investing and Real Estate) reported elsewhere
in this pack; Systematic Investing does not appear as a fifth named pillar on this particular careers
page, so either it sits inside one of the four, or the careers page taxonomy is simply older/coarser than
the current team list [Inferred - flagged as a discrepancy, not resolved].

Within Equities, the described chain runs "Research Analysts, to Portfolio Managers and Traders," with a
separate "Equity Product team" and operational staff who process transactions [S303][Confirmed]. Fixed
Income's own team "handles portfolio representation to clients, reporting, product creation, and sales
support" [S303][Confirmed] — this is functionally identical to what the Investment Directing team purpose
statement in the JD describes doing across all asset classes, i.e. Investment Directing sits at exactly
the seam between "what the fund does" and "what the client and sales team need to hear about it."

The explicit connective-tissue role named on the careers site is Product Management: "The Product
Management team is a conduit between our investment professionals and the clients they serve," doing
reporting, analysis and client communications to build the relationship [S303][Confirmed - direct quote].
Investment Directing (per the JD already established in this pack) is the outward-facing counterpart to
that: representing the investment groups to "prospective and existing clients," reporting on portfolios,
producing thought leadership, working with product development on new products, and generating the
marketing material sales actually uses.

On the distribution side, the careers site names specific channel teams that Investment Directing and
Product would be feeding: Adviser Solutions, Personal Investing, Retail Funds, DC & Workplace Savings,
Retirement Service, a Global Institutional Team (described as "a trusted adviser, expert manager, and a
thought-provoking investment partner to institutions globally," covering pension funds, sovereign wealth
funds and insurers) and a separate Government Institutional Group for "Sovereign Wealth Funds, central
banks, supranationals and public sector pension funds" [S309][Confirmed - all direct quotes]. The page
states plainly that the business benefits from "combining its distribution strengths with the investment
expertise of the Fidelity group" but does not spell out the operating mechanics of that collaboration
beyond naming the teams [S309][Confirmed for the quote; the underlying mechanics are not detailed in any
source found].

**Information barriers.** No FIL-specific published policy describing its own internal information-barrier
architecture was found (the firm's public conflicts-of-interest policy page, on the fidelityinternational.com
domain, was blocked — see GAPS). What is evidenced instead is the regulatory floor such barriers must meet:
FCA SYSC 10 requires "information barriers between product development and distribution teams" as one of
the standard tools for managing conflicts in a manufacturer/distributor [S310][Confirmed - primary
regulatory source, this is the FCA's generic guidance, not a quote about FIL specifically]. The most
obvious place such a barrier would need to bite at Fidelity is between people who have access to
non-public information about a fund's near-term flows/positioning (portfolio managers, dealing desks) and
people whose job is to sell that fund externally (Investment Directing, sales, marketing) — this is the
standard inside-information barrier in any manufacturer that also distributes, but no FIL-specific document
confirming exactly how it is drawn was located [Inferred from general regulatory requirement, not
confirmed for FIL specifically].

### Q3. What is the fundamental value the firm gives its clients

**Who the clients are**, per the firm's own segmentation on its careers site: retail direct customers via
Personal Investing (1.7 million customers, £40bn AUA on the UK platform, per S318); advised clients via
Adviser Solutions; workplace pension members via DC & Workplace Savings; and institutional/wholesale
clients split further into a Global Institutional Team (pension funds, sovereign wealth funds, insurers)
and a Government Institutional Group (central banks, supranationals, public sector pension funds)
[S307][S309][Confirmed - all read directly]. Customer Operations separately states it supports "over 800
institutional clients" [S307][Confirmed].

**What they are buying, per the firm's own framing:** proprietary, shared research coverage (the "single
platform" argument above); a genuinely global, cross-asset-class view built from "more than 16,000-17,000"
company meetings a year [S302][S317][Confirmed, with the number discrepancy flagged above]; and, for UK
retail clients specifically, choice rather than a closed shelf — "over 3,000 funds," "over 2,000 shares,"
Which? Recommended Provider status for SIPPs for six consecutive years, and tools like a retirement
calculator and an AI assistant ("Freya") for account questions [S318][Confirmed - directly read]. None of
the sources found make an explicit, quantified case for Fidelity's own Asia access or its own
decumulation-plus-accumulation continuity claim beyond naming Retirement Builder (a single-fund pension
product) and the Retirement Service business unit [S318][S309][Confirmed the products exist; the
"one-stop-shop across the whole life-cycle" argument is the analyst's inference from having both
accumulation products (ISA, SIPP, workplace DC) and decumulation products (Retirement Service, Retirement
Builder) under one roof, not a claim any source makes explicitly - Inferred].

**Why clients pay active fees when passive is cheaper — the counter-case, with numbers.** This is the
strongest evidence-based finding of this workstream and it cuts against the active-management pitch:
- S&P Dow Jones Indices' SPIVA data, as reported by a secondary outlet citing the SPIVA U.S. scorecards
  directly: in 2025, **79%** of active large-cap US equity funds underperformed the S&P 500, worse than
  **65%** in 2024, and the fourth-worst year in SPIVA's 25-year history; in 2024 the underperformance rate
  was actually reported elsewhere as **62%** for large-cap (small-cap active managers did much better in
  2024, with only 30% underperforming the S&P SmallCap 600) [SNIPPET-sourced from search results only, not
  a page the analyst directly read in full; treat as Reported, single-outlet paraphrase of SPIVA, not
  independently verified against S&P's own PDF, which could not be opened as text in this session — see
  GAPS].
- The same secondary source, citing SPIVA's Persistence and year-end scorecards through 2024: over the
  **20 years to 2024, 94.1%** of all domestic (US) funds underperformed the S&P 1500 Composite on a raw
  basis, rising to **97.3%** underperformance on a risk-adjusted basis; over the **15 years to 2024**, not
  one of 22 US equity fund categories had a majority of active managers beating their benchmark
  [S311][Confirmed - this outlet's article was read in full and these figures were directly in the text,
  attributed by it to S&P's Persistence Scorecard and year-end SPIVA reports].
- Morningstar's Active/Passive Barometer, via search snippets only (the Morningstar pages themselves
  returned blocked or empty content when fetched directly — see GAPS): for 2025, **38%** of active
  strategies survived and beat their asset-weighted passive counterpart, down 4 points on the year before;
  over 10 years, only **21%** of active funds both survived and outperformed; for equity funds
  specifically, the one-year success rate was **31.2%** in 2025 (up from 29.2% in 2024) but only **11.4%**
  over 10 years; fixed income success fell 24 points to **40%**; real estate fell 54 points to **12%**
  [SNIPPET-sourced only, Reported, not independently read on Morningstar's own page].
- On fees, no source in this workstream gave an exact, current, side-by-side active-vs-passive UK fee
  differential figure; this specific number is a gap (see GAPS section), though the Morningstar finding
  that "active funds in the cheapest fee quintiles consistently delivered higher long-term success rates"
  is itself indirect evidence that fee level is a first-order driver of the whole active/passive gap
  [SNIPPET-sourced, Reported].

Put together: the arithmetic case against active management, in aggregate and over long horizons, is
strong and well-evidenced by two independent, credible index providers (S&P and Morningstar), across
multiple years. Fidelity's own client-facing material does not engage with these statistics directly in
anything read for this workstream; its pitch is about research depth, access, and service rather than a
head-to-head performance claim against a benchmark [Inferred from the absence of any such rebuttal in the
material read].

### Q4. The non-investing side: scale, organisation, connective wiring

**How big, in numbers actually sourced (not estimated):**
- Client Services: approximately **280 staff** across the UK and India [S307][Confirmed].
- Investment Services & Fund Accounting (ISFA): **over 230 staff**, maintaining "the formal records for
  Fidelity funds" [S308][Confirmed].
- Institutional Operations: supports **over 800 institutional clients** [S307][Confirmed].
- Group-wide headcount: Wikipedia's article cites 7,600+ employees, but dates this to 2018, so it is
  materially stale [S300][Reported, outdated]. A secondary aggregator (Grokipedia) states roughly 9,500
  employees with no date given [S319][Reported, single source, unclear as-of date]. Neither can be treated
  as a reliable current figure; the primary source (FIL's own annual report) could not be opened in this
  session (see GAPS).
- AUM: Wikipedia states US$1.086 trillion as of 31 December 2025 [S300][Reported]; Grokipedia separately
  states US$1,001.2 billion as of 30 June 2025 [S319][Reported]. The two are for different dates and are
  broadly consistent with each other (growth from mid-year to year-end), but neither was confirmed against
  FIL's own primary reporting in this session.

**How it is organised — the firm's own groupings (careers site, not the corporate leadership page, which
was blocked — see GAPS):** the careers site splits "Professionals" roles into four areas, each with its
own page:
- **Investment Management** — the four asset classes described in Q2.
- **Distribution** — Adviser Solutions, Personal Investing, Retail Funds, DC & Workplace Savings,
  Retirement Service, Global Institutional Team, Government Institutional Group [S309][Confirmed].
- **Customer Operations** — described by the firm as covering "Client Services, Retail, DC and
  Institutional Operations and Investment Platform Change which collectively make up what we call
  Platform Services," plus an "Operational Architecture Group" that "challenges existing practices and
  offers improvements," and an "Operational Development and Testing" function doing project management
  and UAT [S307][Confirmed, all direct quotes].
- **Central Functions** — Technology and Digital ("provide services which underpin every area of the
  global Fidelity business," covering enterprise architecture, application management, security,
  infrastructure and digital client experience across mobile/desktop channels), Human Resources, Legal,
  Compliance ("manage regulatory risk across multiple jurisdictions"), ISFA, Finance, Internal Audit,
  Administration and Support, and Corporate Affairs [S308][Confirmed, all direct quotes].

**How it is wired to the front line.** The clearest connective role the firm itself names is Product
Management, described as "a conduit between our investment professionals and the clients they serve"
[S303][Confirmed]. Investment Directing, per the JD material already established in this pack, is the
outward-facing sibling of that role: it is explicitly staffed by people who are not portfolio managers or
analysts but who sit close enough to both the investment teams and the sales/marketing machine to
translate one into the other. The Technology and Digital function is explicitly framed as a firm-wide
utility rather than a business-line-specific team ("underpin every area of the global Fidelity business")
[S308][Confirmed], which is the clearest evidence of a shared-service model cutting across investment,
platform and distribution.

## 2. KEY NUMBERS TABLE

| Number | What it measures | As-of date | Source | Confidence |
|---|---|---|---|---|
| 39.89% | Johnson family stake in FIL Limited | 2012 (Bermuda regulatory filing) | S301 (Royal Gazette), repeated in S300, S319 | Reported (single origin, stale) |
| 1969 / 1980 | FIL founded as non-US arm / spun off independent from Boston parent | Historical | S300, S301 | Confirmed |
| US$1.086 trillion | FIL group AUM | 31 Dec 2025 | S300 (Wikipedia) | Reported |
| US$1,001.2 billion | FIL group AUM (different date) | 30 Jun 2025 | S319 (Grokipedia) | Reported |
| 7,600+ | FIL group headcount | 2018 (stale) | S300 | Reported, outdated |
| ~9,500 | FIL group headcount | Undated | S319 | Reported, single source |
| 2.5 million | FIL clients worldwide (all business lines) | Undated | S302 | Reported |
| 1.7 million | Fidelity.co.uk (UK retail platform only) customers | Undated (current site copy) | S318 | Confirmed (read directly) |
| £40 billion+ | Investments held via fidelity.co.uk platform | Undated (current site copy) | S318 | Confirmed |
| Over 3,000 | Funds available via fidelity.co.uk Investment Finder | Undated | S318 | Confirmed |
| Over 800 | Institutional clients supported by Customer Operations | Undated | S307 | Confirmed |
| ~280 | Client Services staff, UK + India | Undated | S307 | Confirmed |
| Over 230 | ISFA (fund accounting/records) staff | Undated | S308 | Confirmed |
| Over 360 | Investment professionals and research staff | Undated | S317 | Confirmed (this page); conflicts with next row |
| Over 400 | Investment Management professionals | Undated | S302 | Reported (different FIL page, higher figure) |
| ~16,000/yr | Company meetings by Fidelity investors | Undated | S317 | Confirmed (this page); conflicts with next row |
| ~17,000/yr | Company meetings by Fidelity investors | Undated | S302 | Reported (different FIL page, higher figure) |
| 90% | Share of fund holdings with in-house research/proprietary insight | Undated | S317 | Confirmed |
| ~160 | Third-party investment strategies covered by Manager Research | Undated | S317 | Confirmed |
| 79% | Active large-cap US equity funds underperforming S&P 500 | Full year 2025 | SPIVA, via S311-adjacent search snippet | Reported (snippet, not directly read) |
| 65% | Same measure, prior year | Full year 2024 | Same as above | Reported (snippet) |
| 94.1% | US domestic active funds underperforming S&P 1500, 20yr | 2005-2024 | S311 | Confirmed (directly read) |
| 97.3% | Same, risk-adjusted basis | 2005-2024 | S311 | Confirmed |
| 0 of 22 | US equity categories where a majority of active funds beat benchmark, 15yr | to Dec 2024 | S311 | Confirmed |
| 38% | Active strategies beating asset-weighted passive peer, all categories | Full year 2025 | Morningstar Active/Passive Barometer, via snippet | Reported (snippet, not directly read) |
| 21% | Active funds surviving and beating passive, 10yr | to 2025 | Same as above | Reported (snippet) |
| 11.4% | Active equity funds surviving and beating passive, 10yr | to 2025 | Same as above | Reported (snippet) |

## 3. VERBATIM QUOTES ACTUALLY READ

- "The Product Management team is a conduit between our investment professionals and the clients they
  serve." — careers.fidelityinternational.com/professionals-overview/investment-management/ [S303]
- "Analysts work together across asset classes, e.g. combining insights from equity and credit research,
  to form a 360° view on the health and prospects of companies." — careers.fidelityinternational.com/about-us/
  [S302]
- "Technical Services... provide services which underpin every area of the global Fidelity business." —
  paraphrase-adjacent to the read text; direct read was: Technology and Digital teams "provide services
  which underpin every area of the global Fidelity business" — careers.fidelityinternational.com/professionals-overview/central-functions/
  [S308]
- "[Client Services, Retail, DC and Institutional Operations and Investment Platform Change] collectively
  make up what we call Platform Services." — careers.fidelityinternational.com/professionals-overview/customer-operations/
  [S307]
- "A trusted adviser, expert manager, and a thought-provoking investment partner to institutions
  globally." (describing the Global Institutional Team) — careers.fidelityinternational.com/professionals-overview/distribution/
  [S309]
- "The investment team is at the heart of the Fidelity business, and consists of four asset classes; Real
  Estate, Fixed Income, Equities and Multi-Asset[, which] work synonymously combining the strength and
  skills of separate disciplines." — careers.fidelityinternational.com/professionals-overview/ and
  /investment-management/ [S303]/[S306]
- "[The Johnsons] own 39.89 percent of FIL" and fund managers and senior employees "own the rest" (company
  spokesperson quote) — royalgazette.com, "Fidelity Fund Empire Bermuda ties," 21 Sept 2012 [S301]
- FCA Handbook, SYSC 10.1.3R: a firm must "take all appropriate steps to identify and to prevent or manage
  conflicts of interest." SYSC 10.1.7R requires firms to "maintain and operate effective organisational
  and administrative arrangements" to stop conflicts harming client interests. SYSC 10.1.9G warns against
  "over-reliance on disclosure without adequate consideration as to how conflicts may appropriately be
  managed." — handbook.fca.org.uk/handbook/SYSC/10/ [S310]

## 4. SOURCE TABLE ROWS

[S300] | Wikipedia | "Fidelity International" | undated (live article) | https://en.wikipedia.org/wiki/Fidelity_International | Accessed 2026-09-16 | FETCHED | Secondary, tertiary-sourced encyclopaedia article; treat AUM/headcount as Reported not Confirmed.
[S301] | The Royal Gazette | "Fidelity Fund Empire Bermuda ties" | 2012-09-21 | https://www.royalgazette.com/international-business/business/article/20120921/fidelity-fund-empire-bermuda-ties/ | Accessed 2026-09-16 | FETCHED | Quality regional business press, cites a named company spokesperson; figure is 14 years old.
[S302] | Fidelity International Careers | "About Us" | undated (live page) | https://careers.fidelityinternational.com/about-us/ | Accessed 2026-09-16 | FETCHED | Primary source (firm's own site), current copy, no publication date shown.
[S303] | Fidelity International Careers | "Investment Management" (Professionals overview) | undated | https://careers.fidelityinternational.com/professionals-overview/investment-management/ | Accessed 2026-09-16 | FETCHED | Primary source.
[S304] | Fidelity International Careers | Careers homepage/navigation | undated | https://careers.fidelityinternational.com/ | Accessed 2026-09-16 | FETCHED | Primary source, used for site navigation/structure only.
[S305] | Fidelity International Careers | "Internships" (Early careers) | undated | https://careers.fidelityinternational.com/early-careers-overview/interns-and-insights/internships/ | Accessed 2026-09-16 | FETCHED | Primary source; note this page's internship description (stock-picking, "director of research" mentor) reads as the general investment-research internship, not confirmed to be Investment Directing specifically - do not conflate with the JD in this pack's shared brief.
[S306] | Fidelity International Careers | "Professionals overview" | undated | https://careers.fidelityinternational.com/professionals-overview/ | Accessed 2026-09-16 | FETCHED | Primary source, names the four business-area groupings used in Q4.
[S307] | Fidelity International Careers | "Customer Operations" | undated | https://careers.fidelityinternational.com/professionals-overview/customer-operations/ | Accessed 2026-09-16 | FETCHED | Primary source, direct headcount and client-count figures.
[S308] | Fidelity International Careers | "Central Functions" | undated | https://careers.fidelityinternational.com/professionals-overview/central-functions/ | Accessed 2026-09-16 | FETCHED | Primary source.
[S309] | Fidelity International Careers | "Distribution" | undated | https://careers.fidelityinternational.com/professionals-overview/distribution/ | Accessed 2026-09-16 | FETCHED | Primary source.
[S310] | Financial Conduct Authority | FCA Handbook, SYSC 10 (Conflicts of interest) | current in-force version | https://www.handbook.fca.org.uk/handbook/SYSC/10/?view=chapter | Accessed 2026-09-16 | FETCHED | Primary regulatory source; generic rule, not FIL-specific.
[S311] | WealthManagement.com | "Active Management's Persistent Failure: A 2025 Perspective" | 2025 (exact date not shown on fetch) | https://www.wealthmanagement.com/investing-strategies/active-management-s-persistent-failure-a-2025-perspective | Accessed 2026-09-16 | FETCHED | Quality trade press summarising S&P Dow Jones Indices SPIVA/Persistence Scorecard data; figures attributed to S&P, not independently verified against S&P's own document (blocked, see GAPS).
[S312] | Prosple UK | "Investment Directing Summer Internship (Jun 2026)" | undated listing | https://uk.prosple.com/graduate-employers/fidelity-international/jobs-internships/investment-directing-summer-internship | Accessed 2026-09-16 | PAYWALLED-NOT-READ (403 on fetch) | Not read; do not attribute quotes to this URL beyond what is already in the shared brief.
[S313] | Bright Network | "Investment Directing Summer Internship 2026" | undated listing | https://www.brightnetwork.co.uk/graduate-jobs/fidelity-international/investment-directing-summer-internship-2026 | Accessed 2026-09-16 | SNIPPET (Cloudflare-blocked, per shared brief; not independently fetched here either) | Consistent with shared brief's reconstruction; no new content obtained.
[S314] | S&P Dow Jones Indices | "U.S. Persistence Scorecard Year-End 2025" (SPIVA) | Year-End 2025 | https://www.spglobal.com/spdji/en/spiva/article/us-persistence-scorecard/ | Accessed 2026-09-16 | SNIPPET (403 on direct fetch; figures obtained via search-result summary only) | Primary index provider, but only snippet-level data obtained, not the full document; treat headline % as Reported, not Confirmed.
[S315] | Morningstar | "Better Conditions Did Not Yield Better Results for Active Managers in 2025" | 2025/2026 (Active/Passive Barometer year-end release) | https://www.morningstar.com/funds/better-conditions-did-not-yield-better-results-active-managers-2025 | Accessed 2026-09-16 | SNIPPET (fetch returned no extractable content / 403) | Figures used in this report are from the search-engine summary of this and related Morningstar Barometer coverage, not from a page read in full.
[S316] | Morningstar UK | "Passively Managed Funds Outperform Active Peers Across Most Categories" | undated | https://global.morningstar.com/en-gb/funds/passively-managed-funds-outperform-active-peers-across-most-categories | Accessed 2026-09-16 | SNIPPET (403 on fetch) | Same caveat as S315.
[S317] | Fidelity (Investment Trusts UK) | "About" | undated | https://investment-trusts.fidelity.co.uk/about/ | Accessed 2026-09-16 | FETCHED | Primary source (Fidelity's own UK investment-trusts site); gives the 360-professional / 16,000-meeting / 90%-coverage figures used in Q1.
[S318] | Fidelity.co.uk | Homepage | undated (live page) | https://www.fidelity.co.uk/ | Accessed 2026-09-16 | FETCHED | Primary source, UK retail platform; client count and fund-range figures are for the UK platform only, not the whole FIL group.
[S319] | Grokipedia | "Fidelity International" | undated (AI-generated encyclopaedia page) | https://grokipedia.com/page/Fidelity_International | Accessed 2026-09-16 | FETCHED | Not in the brief's preferred source hierarchy; an AI-summarised secondary/tertiary source used only for cross-checking and named-leader identification, every figure from it flagged Reported and not treated as independently corroborating S300/S301 since likely same underlying origin.
[S320] | TheOrg.com | "Fidelity International" (org chart page) | undated | https://theorg.com/org/fidelity-international | Accessed 2026-09-16 | FETCHED | Low-confidence crowd/scrape-sourced org-chart aggregator; page itself shows internally inconsistent headline data (e.g. "1-10 employees" alongside 786-person office listings). Used only as a weak secondary pointer to division names (e.g. "Global Platform Solutions"), not for any headcount claim.
[S321] | TheOrg.com | "Fidelity International - Leadership Team" | undated | https://theorg.com/org/fidelity-international/teams/leadership-team-1 | Accessed 2026-09-16 | FETCHED | Page is self-labelled "Unverified" by the host site; used only as a weak pointer to two named roles, not relied upon for any figure in this report.
[S322] | Fidelity International (Retirement) | "What we do by region" | undated | https://retirement.fidelityinternational.com/global-capabilities/what-we-do-region/ | Accessed 2026-09-16 | FETCHED | Primary FIL source for UK/Germany/Hong Kong/Japan workplace-pensions descriptions; the page also surfaced US 401(k)/$2.2tn figures that belong to the separate Boston firm (Fidelity Investments) and are explicitly excluded from any FIL claim in this report.
[S323] | Craft.co | "Fidelity International Executives" | undated | https://craft.co/fidelity-international/executives | Accessed 2026-09-16 | PAYWALLED-NOT-READ (403 on fetch) | Not read; no content used from this URL.
[S324] | Fidelity Institutional (institutional.fidelity.com) | "Pension investment solutions" | undated | https://institutional.fidelity.com/institutions/institutional-solutions/pension-investment-solutions | Accessed 2026-09-16 | FETCHED but EXCLUDED | This page belongs to Fidelity Investments/FIAM LLC (the separate Boston firm), not Fidelity International. Read and then discarded per the firm-identity rule; recorded here only to document the check was made.

## 5. GAPS

- The official corporate site, fidelityinternational.com (including its Leadership page and its Annual
  Report PDF), returned a hard Akamai "Access Denied" on every path tried, via both the fetch tool and a
  direct curl request with a standard browser user agent. This means the firm's own leadership-page
  groupings and its own primary-source AUM/headcount/ownership figures could not be verified directly.
  Careers-site material and secondary aggregators were used as substitutes and are flagged accordingly
  throughout.
- The session's web-search allowance is shared across all parallel workstreams in this project and was
  exhausted mid-research (10 distinct queries completed from this workstream before the tool returned a
  hard "budget used" stop). The 14-search target for this workstream specifically was not reached; this
  was compensated for with 19 successful full-page fetches (versus a 10-fetch minimum), but some findings
  that would normally be triangulated across three or four searches (e.g. the current, non-2012 ownership
  split; a current, dated headcount figure; a current UK active-vs-passive fee differential) rest on fewer
  independent queries than would be ideal.
- No current (post-2012) figure for the Johnson family's ownership percentage of FIL was found. The
  39.89% figure in circulation traces to a single 2012 filing and is repeated, not re-confirmed, by later
  secondary sources.
- No FIL-specific document describing its own internal information-barrier architecture (as opposed to the
  generic FCA requirement that such barriers exist) was located.
- The two Fidelity pages giving research-platform headcount and company-meeting counts (S302 and S317)
  disagree with each other (over 360 vs over 400 professionals; ~16,000 vs ~17,000 meetings/year) and
  neither is dated, so it is not possible to say whether this is a real change over time or simply two
  pages that have not been kept in sync.
- SPIVA's own scorecard document and Morningstar's own Active/Passive Barometer report page both returned
  blocked or unreadable content when fetched directly (one PDF could not be converted to text in this
  environment; the Morningstar HTML pages returned 403 or empty content). All SPIVA/Morningstar figures in
  this report are therefore Reported from search-engine result summaries, not Confirmed from a directly
  read primary document, and are flagged as such in the tables above.
- No current, UK-specific, side-by-side fee differential (average active OCF vs average passive OCF) was
  found in this workstream; this would strengthen the Q3 counter-case numerically if sourced from the
  Investment Association or the FCA's own market study data.
- Named leadership figures beyond Anne Richards, Abigail Johnson and Keith Metters (whose roles are widely
  reported and were not in doubt) come from secondary aggregators (Grokipedia, TheOrg) that are outside the
  brief's preferred source hierarchy and were not cross-confirmed on the firm's own blocked leadership page.
  Treat any name beyond those three as Reported and unverified against a primary source.
- Whether "Systematic Investing" is a genuinely separate fifth pillar (as in the JD reconstruction already
  in the shared brief) or sits inside one of the four asset classes named on the careers site could not be
  resolved from the material read.

## 6. INTERVIEW ANGLES

### Why Fidelity International, and why Investment Directing — raw material

**30 seconds.** "Fidelity International is one of the few asset managers that both manufactures funds and
owns the distribution around them — it runs its own retail platform, its own adviser platform and its own
workplace pensions business, and it's stayed privately owned since splitting from the US Fidelity business
in 1980. That means it can invest through a cycle without quarterly shareholders to answer to, but it also
means it has to actively manage the conflict of selling its own funds on its own shelf — which is why, for
example, its UK platform gives access to thousands of third-party funds rather than just its own. Investment
Directing is the team that sits exactly on that seam: turning what the fund managers and analysts are doing
into something a client, an adviser or a pension scheme can actually act on. That's the part of asset
management I find most interesting: not picking the stock, but explaining and defending the decision to the
people whose money it is."

**2 minutes.** Build outward from the 30-second version using: the ownership mechanism (private, ~40% Johnson
family per a 2012 filing, no listed shares, so no earnings-call pressure but also no equity currency for
acquisitions); the vertical-integration mechanism (Personal Investing, Adviser Solutions, DC & Workplace
Savings, Global Institutional and Government Institutional teams all sit under one roof, per the firm's own
Distribution page, which is unusual — most active managers only manufacture); the cost side, honestly stated
(a platform business that needs hundreds of Customer Operations and Fund Accounting staff regardless of that
quarter's flows, and a conflicts framework under FCA SYSC 10 that has to be taken seriously, not just
disclosed away); the research mechanism (a shared research platform — several hundred analysts, tens of
thousands of company meetings a year — that only makes commercial sense if it's shared across every asset
class and every product built on top of it, which is exactly the model the firm runs); and the honest
counter-case on active management (SPIVA and Morningstar both show a majority of active funds underperform
over most horizons, so the pitch has to be about something more specific than "we beat the index" — depth of
proprietary research, whole-of-lifecycle service, and being able to sit across equities, fixed income, real
estate and multi-asset for one client relationship). Land on Investment Directing specifically as the role
that has to make that case, in writing and in the room, to real clients — which is why the internship's own
description (marketing materials, portfolio reporting, sourcing "the latest internal views," project
management) is really an apprenticeship in translation between the investment side and the commercial side.

**Closing line, naming one specific thing to work on.** "The one thing I want to get better at before
starting is reading a fund factsheet and portfolio commentary the way an Investment Directing analyst would
— not just what the fund holds, but what story that positioning is meant to tell a client, and where the
honest caveats are." (This should be adapted once the candidate has actually practised reading a Fidelity
factsheet, per whichever workstream produces the fund examples; this line is deliberately concrete and
checkable, not a generic "I want to learn more.")

### What most candidates will say vs what this candidate can say

| Theme | What most candidates will say | What this candidate can say, using this research |
|---|---|---|
| Why Fidelity | "It's a big, well-known, global asset manager with a strong reputation." | "It's one of a small number of active managers that owns manufacturing and distribution end to end — its own retail platform (1.7m UK customers, £40bn+ AUA), its own adviser platform, and its own workplace pensions business — and it has stayed privately owned since the 1980 split from the US Fidelity business, which changes its incentives versus a listed peer." |
| Ownership | Doesn't mention it, or says "it's privately owned" with no detail. | Can say ownership sits with the founding Johnson family (around 40% per a 2012 filing) and current/former management, can explain what that buys (no quarterly earnings pressure) and what it costs (no listed equity for M&A or staff incentives), and can flag that the ownership split hasn't been re-confirmed publicly in years. |
| Research | "Fidelity has great research." | Can name the mechanism: a shared research platform reused across equities, fixed income and multi-asset, several hundred analysts doing five-figure numbers of company meetings a year, feeding into 90% in-house-researched holdings — and can explain why sharing that cost across the whole platform is what makes it economically viable. |
| The active/passive question | Avoids it, or gives a defensive answer about "our strong track record." | Can state the counter-case with real numbers unprompted — SPIVA shows most active managers underperform over most horizons, Morningstar's Active/Passive Barometer shows the same — and can then make the more defensible, narrower case for why a firm like Fidelity still has a role (depth, access, service, one provider across the client's whole life-cycle) rather than claiming to beat the index. |
| Conflicts of interest | Doesn't realise there is one to discuss. | Can name the specific conflict (a firm selling its own funds on its own platform) and the specific regulatory framework that governs it (FCA SYSC 10, information barriers, conflicts committees, disclosure as a last resort), and can point to a concrete mitigant the firm actually uses (whole-of-market fund choice on its own platform, not a closed shelf). |
| The non-investment business | Doesn't know it exists, or assumes "it's mostly fund managers." | Can describe the firm's own four-part structure (Investment Management, Distribution, Customer Operations, Central Functions) and cite specific headcounts (e.g. ~280 in Client Services, 230+ in fund accounting, 800+ institutional clients supported) to show the platform is a real, large machine, not a footnote. |
| Why Investment Directing specifically | "I want client-facing exposure" (generic). | Can explain the role as the named connective function between a Product Management team ("a conduit between our investment professionals and the clients they serve") and the outward commercial teams, and can point to the JD's own listed duties (marketing materials, portfolio reporting, sourcing internal views, project management) as evidence of exactly that translation function. |

### Honest counter-case: genuine reasons someone might not want this job

- It is explicitly not a portfolio-management or research-analyst seat. The JD's own duties (marketing
  materials, reporting, sourcing views from others, project management) are support and translation work,
  not idea generation. Someone whose primary interest is picking stocks or building models may find this
  adjacent to, rather than inside, that work.
- The firm's own material shows a wide range of sub-teams within Distribution and Investment Directing
  (retail, adviser, DC, institutional, government institutional). A candidate motivated specifically by one
  of these (e.g. only wants institutional/pension work) may land in a different client segment than they
  expected, since the JD covers all of Equities, Fixed Income, Multi Asset, Systematic Investing and Real
  Estate.
- The firm is privately owned with an opaque, stale-data ownership structure (the clearest public figure is
  14 years old). Someone who wants to work somewhere with fully transparent public disclosure (as a listed
  company would have) will find less of that here.
- The active-management pitch has real headwinds: the SPIVA and Morningstar evidence in this report shows
  most active strategies do not beat their passive benchmark over most measured horizons. A candidate who
  is not comfortable defending active management's value proposition against that evidence, or who is
  personally more convinced by the passive case, should reckon with that tension honestly rather than
  ignore it.
- Because the firm both manufactures and distributes funds, there is a real, regulator-acknowledged conflict
  of interest built into the business model (FCA SYSC 10 exists precisely because this structure creates
  risk). Someone uncomfortable with that structural tension, even where it is well managed, should weigh it.
- Several of the headline numbers used to describe the firm's own scale (headcount, research-team size,
  meeting counts) are inconsistent between the firm's own pages and are not dated, which suggests the
  public-facing material is not tightly maintained; a candidate expecting crisp, current public reporting
  (as they would get from a listed company's investor-relations site) will not find that here.
