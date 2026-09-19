# PRIVATE CREDIT STRATEGIES AND DEAL MECHANICS — WORKSTREAM (Source IDs P50-P99)

Compiled 2026-09-19. Written for a beginner. Every non-obvious claim carries a [Pxx] marker and a
confidence tag. Figures from vendors are labelled as vendor estimates because different providers
define "private credit" differently (some include only direct lending, some include all of
distressed, mezzanine, real assets and structured credit), so headline market-size numbers are not
directly comparable across sources.

---

# 1. FINDINGS

## 1.1 THE STRATEGY MAP

Private credit is not one product. It is a ladder of strategies that differ by where they sit in a
company's capital structure, how much risk they take, and what kind of asset or cash flow actually
backs the loan. Below, each strategy is defined the way a beginner needs: what it is, where it sits,
what it targets, what can go wrong, and one concrete example of what it funds.

**Senior direct lending (first lien).** A loan made directly by a non-bank fund (not syndicated to
many buyers) to a company, secured by a first-priority claim ("first lien") on that company's assets.
"First lien" means this lender gets paid back before any other lender if the company is liquidated.
Cambridge Associates, a source used across the industry, defines direct lending senior debt as funds
that "lend money to performing companies on a first lien senior secured basis" [P56][Confirmed], and
estimates target returns roughly 100-200 basis points (bps; 1 bp = 0.01 percentage point) above what
the public leveraged-finance market pays for similar risk [P56][Reported]. Concrete example: a private
equity firm buys a business services company for $200m; a direct lending fund lends $120m secured
against the company's receivables, equipment and cash flow, priced at SOFR (the US reference floating
rate) plus a spread, to help fund the purchase.

**Unitranche.** A single, blended loan that stands in for what would otherwise be a separate senior
loan plus a separate junior/mezzanine loan (see section 3 for full mechanics) [P50][Confirmed].

**Second lien.** A loan secured on the same collateral as a first-lien loan, but with a claim that
only gets paid after the first-lien lender is repaid in full. "Second lien loans have the same
characteristics as senior loans except that they are second in lien priority," and in a default "the
first priority lien holder has first claim to the underlying collateral, leaving no collateral value
for the second priority lien holder" if that collateral is worth less than the first-lien debt
[P56-adjacent search synthesis; see also P98 for structural definition][Reported]. It sits below first
lien and unitranche, above mezzanine, in seniority. Example: on top of a $100m first-lien unitranche,
a second-lien lender puts in another $20m at a higher rate, betting the company is worth enough to
cover both.

**Mezzanine debt.** Subordinated debt (ranks below senior and second-lien debt, above equity) that
often carries an equity "kicker" — warrants or options that let the lender buy equity later. Cambridge
Associates: mezzanine/subordinated capital is "a loan or security that ranks lower than other loans
with regard to claims on assets or earnings" and typically carries "between 10% to 20% equity
exposure" bundled with the debt [P56][Confirmed]. It is "not repaid until after unsubordinated
(senior) debt holders have been repaid" [P56][Confirmed]. Example: a founder-owned manufacturer takes
a $15m mezzanine loan to buy out a retiring co-owner, paying a high cash coupon plus warrants worth a
small slice of the company if it is sold well.

**Payment-in-kind (PIK) structures.** Instead of paying interest in cash, some or all of the interest
is added to the loan's principal balance and paid at maturity. This can be a normal, pre-agreed
feature (mezzanine loans routinely PIK part of their coupon) or a "PIK toggle" exercised later under
stress (see section 5) [Reported, multiple sources below].

**Distressed debt.** Buying the existing debt of a company that is already in or near default,
usually at a steep discount to face value, in the hope of profiting from a restructuring or recovery.
Cambridge Associates groups this with "credit opportunities" strategies that are "opportunistic in
nature... investing in companies in stressed or distressed situations" and that can earn "higher
[returns] than direct lending during benign markets" precisely because they benefit "from market
stress and dislocations" [P56][Confirmed].

**Special situations.** A close cousin of distressed debt: financing built around an unusual corporate
event (spin-off, litigation, regulatory problem, rescue financing) rather than a routine loan.
Practitioner sources describe special situations as investing "with the intent of gaining control of a
company... generally one in financial distress" via secondary-market trading, direct origination, or
buying distressed debt where there is a price dislocation [Reported, from search synthesis of CAIA/
Cambridge material; treat as [Inferred] composite definition].

**Opportunistic credit.** A flexible, go-anywhere mandate that looks for situations "where traditional
sources of debt financing are unavailable for borrowers," creating pricing dislocations where a lender
can get "equity-like returns with strong downside protection" [Reported, same synthesis][Inferred
composite].

**Asset-based finance / specialty finance.** This is explicitly the fastest-growing part of private
credit. Rather than lending against a company's overall enterprise cash flow (as direct lending does),
ABF lends against a specific, granular pool of assets or contracted cash flows: equipment leases,
trade receivables, royalty streams, consumer loans, aircraft, litigation claims, or music rights
[P52][Confirmed]. A June 2026 survey of more than 380 private-credit professionals globally (the
"Compass 2026" survey by Oxane Partners) found 66% of respondents cite "ABF and specialty finance" as
the leading driver of AUM growth over the next 12-18 months, ahead of fund finance (60%) and corporate
direct lending (56%); 83% expect AUM to grow at all [P52][Confirmed, FETCHED]. In the first three
quarters of 2025, specialty finance was reportedly the most popular strategy for new private-credit
fund launches (84 launches) ahead of direct lending (71) [Reported, search synthesis][Reported].
Sub-sectors, with examples:
  - *Equipment leasing and receivables*: lending against a pool of leased trucks, medical equipment or
    invoices a business is owed; cash flow is diversified across many obligors rather than one company.
  - *Royalties*: lending against a music catalogue's or patent's future royalty income. Banks now
    extend "senior secured facilities collateralized directly by copyrights," and a rated
    catalogue-backed bond market has also emerged [Reported, search synthesis of Neuberger Berman/EY
    coverage][Reported].
  - *Consumer loans*: buying or financing pools of consumer instalment or auto loans originated by
    fintech lenders.
  - *Fund finance*: lending to private equity/credit funds themselves rather than to operating
    companies (subscription lines against unfunded investor commitments, and NAV facilities against
    the fund's asset base). The fund finance market (subscription lines plus NAV) is estimated by more
    than half of respondents to a 2026 Haynes Boone survey at $1.25-$1.75 trillion, with 16% putting it
    even higher [P54][Reported, vendor survey — respondents' own estimate, not an audited figure].
    Subscription-line facilities represent more than two-thirds of the market per 82% of respondents,
    and 94% of surveyed lenders closed a subscription financing in 2025 [P54][Reported].
  - *Aviation*: financing aircraft purchases or leases using the aircraft as collateral. More than
    19,000-21,000 new aircraft globally are expected to need new financing over the next decade, with
    an estimated $300bn+ of aviation assets requiring capital solutions, and private credit has become
    a bigger source of that financing alongside banks and the ABS (asset-backed securities) market
    [Reported, search synthesis of Maples Group/Ogier coverage][Reported].
  - *Litigation finance*: funding a law firm's or claimant's legal costs in exchange for a share of any
    settlement or award. Market-research vendor ResearchNester sizes global litigation funding
    investment at about $23.48bn in 2026, projected to reach $51.09bn by 2036 (8.08% CAGR)
    [Reported, vendor market-sizing][Reported] — for scale, this is roughly 100x smaller than the
    private credit market as a whole [Reported].
  - *Music rights*: lending against, or buying, catalogues of song royalties, treated increasingly as
    an institutional asset class with "long-duration, inflation-resistant cash flows uncorrelated to
    traditional markets" [Reported, industry commentary][Reported].

**NAV lending.** A loan made not to an operating company but to a private equity fund itself, secured
against the fund's entire portfolio of investments (its net asset value, or NAV) rather than any single
company's cash flow. "A NAV loan is a credit facility extended to a private equity fund, with the
collateral being the fund's portfolio of investments, where the lender advances money based on a
percentage of the fund's estimated net asset value" [Reported, search synthesis][Reported]. Pricing
typically runs SOFR plus 300-600 bps depending on portfolio quality [Reported][Reported]. In March
2026, NAV lender 17Capital closed its Credit Fund 2 at $7.5bn, described as the largest NAV loan
fundraise ever recorded, taking the firm's total capital raised across strategies to $24bn
[Reported][Reported]; the wider NAV loan market is estimated around $150bn today with vendor
projections of $600-700bn by 2030 [Reported, vendor projection — wide range across sources, treat as
directional][Reported]. **Why it is controversial**: the loan is serviced and often used to fund cash
distributions back to the fund's own investors (LPs) before the fund has actually sold anything, which
critics say can mask weak underlying performance; interest costs on the NAV loan "come out of fund
returns before LPs see a dollar," and if a distribution funded by a NAV loan later needs to be clawed
back because the fund underperforms, LPs may have already spent cash they thought was a real
realisation rather than borrowed money [Reported][Reported]. The added leverage sits on top of the
leverage already inside each portfolio company, which is "a growing worry for investors in PE funds
and for regulators," and the SEC reportedly wants assurance that general partners are not inflating
portfolio valuations to preserve NAV-loan borrowing capacity, and that NAV-funded distributions are
clearly disclosed as debt-funded rather than realisation-funded [Reported][Reported].

**Venture debt.** A loan to a venture-capital-backed company that is not yet profitable, sized against
its cash runway and existing VC backing rather than positive cash flow or hard collateral
[Reported][Reported]. In 2026, "a Series B startup... should expect SOFR plus 600 to 900 basis points
— call it 10% to 13% all-in — plus an upfront fee of 1% to 2%, an end-of-term fee of 3% to 6%, and
warrant coverage of 0.5% to 1.5% of the loan amount," with most lenders in 2026 tightening terms to
2-3 year maturities [Reported][Reported]. Warrants (the lender's right to buy equity later at a fixed
price, usually the most recent funding round's valuation) typically give coverage of 5%-30% of the
loan depending on deal risk [Reported][Reported] — compensation for lending to a company with no
proven cash flow.

**Real estate debt.** Loans secured against commercial or residential property, ranging from senior
mortgages to higher-risk bridge and mezzanine loans on transitional (under-renovation) buildings.
Non-bank/private lenders (debt funds and mortgage REITs) accounted for 40% of non-agency commercial
real estate loan closings in Q4 2025, filling a gap left by banks that pulled back under Basel III and
Dodd-Frank capital rules, especially in higher-risk bridge and development lending [P61][Reported].
About $875bn of US commercial and multifamily mortgage debt is scheduled to mature in 2026 (roughly
17.5% of the ~$5.0 trillion outstanding market), much of it originated in 2019-2021 at far lower rates
[Reported, search synthesis][Reported]; CBRE separately puts the 2026 US CRE maturity wall at "over
$800 billion" [P61][Reported] — the two figures are close but not identical, a reminder that even
maturity-wall estimates vary by data provider and definition. Real estate credit is underwritten on
LTV (loan-to-value: loan size as a percentage of the property's appraised value), debt yield and debt
service coverage ratio, not EBITDA multiples like corporate lending [P61][Confirmed]. Falling property
values (commercial values down roughly 20% from early 2022 per one estimate) have let lenders extend
credit at lower LTVs (about 60-65% versus 70%+ in the last cycle), which the same source frames as
"less risk at higher returns" [Reported][Reported].

**Infrastructure debt.** Loans to long-life physical infrastructure assets (toll roads, power
generation, digital infrastructure/data centres, fibre networks) with typically long, contracted or
regulated cash flows. As of 2026, private high-yield "BB" infrastructure credit spreads were reported
starting in the "high-200-to-low-300 bp range," implying yields around 7.0% or higher, which compares
to the BB US High Yield Index option-adjusted spread averaging about 176 bps over the twelve months to
April 2026 [Reported][Reported] — i.e., private infrastructure debt was pricing wider (paying more) than
public high-yield bonds of similar rating, one reason investors have been rotating into it. Dedicated
infrastructure debt funds hold a small share of total infrastructure AUM (about 8.1% as of Q1 2025),
which vendors argue leaves room for growth [Reported][Reported]; total global infrastructure debt
volumes reached about $1.05 trillion in 2025, split roughly 80% bank loans / 20% capital markets
issuance [Reported][Reported].

**Significant risk transfer (SRT) / synthetic risk transfer.** Not a loan a private credit fund makes
to a company at all — instead, a bank keeps a pool of loans (say, a book of corporate loans) on its own
balance sheet, but pays a group of investors (increasingly private credit funds) a fee to insure it
against losses on a slice ("tranche") of that pool, usually via a credit-linked note or a
credit-default-swap-like guarantee [P60][Confirmed]. This frees up the bank's regulatory capital
without it having to sell the underlying loans. The Bank for International Settlements reports that
annual SRT issuance grew from less than €5bn in 2016 to €21bn in 2024, and that by end-2024 SRTs
provided credit protection on roughly €800bn of loans across the EU, US, UK and Canada — about 2% or
less of those banks' total loans [P60][Confirmed, FETCHED]. The average capital relief for issuing
banks was about 43 bps of CET1 (core regulatory capital), exceeding 100 bps for some banks
[P60][Confirmed]. A worked example from the same source: a bank keeps the senior 92% of a loan
portfolio at a much-reduced 15% risk weight, transfers a 7% mezzanine slice to investors (whose risk
weight on that piece then drops toward 0% for the bank), and retains the bottom 1% first-loss "junior"
tranche, which carries an extremely punitive 1,250% risk weight if kept on balance sheet
[P60][Confirmed]. Since 2016, default risk on more than €1.3 trillion of loans has been transferred via
SRTs, with roughly a third of that transferred in just the last two years — a sign of rapid recent
growth [P62][Reported]. Before 2020, specialised credit funds and pension funds made up about
three-quarters of SRT investors; since then the investor base has broadened to include private credit
funds, hedge funds and other asset managers [P60][Confirmed]. Regulators (BIS, and separately the Basel
Committee) flag a risk: the SRT investor base is still concentrated, so "changes in risk appetite or
funding conditions among a small group of investors can have outsized effects on issuance volumes and
pricing," creating potential procyclicality [Reported][Reported].

## 1.2 THE CAPITAL STRUCTURE — THE LADDER, IN PLAIN ENGLISH

Picture a company's financing as a ladder from safest (top, gets paid first) to riskiest (bottom, gets
paid last, but keeps the upside if things go well):

1. **Senior secured debt (first lien).** Paid first. Has a formal legal claim ("lien") on specific
   assets. If the company is sold or liquidated, this lender is repaid from the proceeds of its
   collateral before anyone else touches that money.
2. **Second lien debt.** Same collateral as the first-lien lender, but that lender's claim is
   satisfied first; the second-lien lender only gets what is left over.
3. **Senior unsecured / subordinated debt (including mezzanine).** No specific collateral claim, or a
   claim explicitly ranked below the secured lenders. Compensated with a higher interest rate and
   sometimes warrants for the extra risk.
4. **Preferred equity.** Technically an ownership stake, not debt, but usually has a fixed dividend
   and gets paid out before common equity in a sale or liquidation.
5. **Common equity.** The owners (often the private equity sponsor and management). Paid last, but
   keeps all the upside if the company grows in value.

Plain-English glossary:
- **First lien / second lien**: the *order* in which secured lenders get paid from specific collateral
  if it is sold. First lien is paid in full before second lien gets anything.
- **Subordinated**: ranked below other debt in payment priority; "sub debt" gets paid only after
  senior debt is satisfied.
- **Security**: the legal right a lender has been granted over specific assets (a mortgage on a
  building, a lien on receivables, a pledge of shares) that lets it seize and sell those assets if the
  borrower defaults.
- **Collateral**: the actual assets pledged as security — equipment, receivables, real estate, IP, a
  fund's portfolio, etc.
- **Recovery**: the percentage of the original loan amount a lender actually gets back after a default
  and any workout or liquidation. A first-lien loan with good collateral might recover 70-90 cents on
  the dollar; a subordinated loan behind it might recover little or nothing if the collateral's value
  does not stretch that far.

## 1.3 UNITRANCHE IN DETAIL

**What it is.** A unitranche facility replaces what used to be two separate loans — a senior tranche
and a junior/mezzanine tranche, each with its own lender group, pricing and intercreditor terms — with
"a single secured credit facility in which two or more groups of lenders share in the same security
interest" [P50][Confirmed, FETCHED]. Crucially, "unlike traditional first lien/second lien deals with
separate liens, unitranche arrangements feature only one lien" [P50][Confirmed]. From the borrower's
point of view, it behaves like one loan: one lender group (or a small club), one credit agreement, one
set of collateral documents, one blended interest rate [P50][Confirmed].

**Why borrowers like it.** Speed and simplicity. Negotiating with one lender (or one arranger who
syndicates a small club afterwards) instead of separately negotiating senior debt with a bank and
junior debt with a mezzanine fund cuts the number of parties, the number of documents, and the
execution risk in a competitive M&A auction where speed and certainty of funding win deals
[P50][Confirmed].

**The agreement among lenders (AAL).** Behind that single blended loan, the actual economic risk is
usually still split between two informal groups of lenders — "first-out" and "last-out" — through a
private side contract, the Agreement Among Lenders, that the *borrower typically never sees or signs*
[P50][Confirmed]. The AAL sets out, at minimum: (i) payment priority (in the events set out in the
AAL, all principal and interest collected first goes to pay the first-out lender in full before
last-out lenders see a cent) [P50][Confirmed]; (ii) waterfall/trigger events that switch the facility
from "normal" blended payments into strict first-out-first priority — these "nearly always include
payment and insolvency defaults," and often financial covenant defaults too [P51][Confirmed]; (iii)
who controls enforcement action (foreclosing on collateral, driving a restructuring) — this can sit
with the first-out or last-out group depending on the deal and can shift after a trigger event
[P50][Confirmed]; and (iv) voting thresholds for amendments, often something like "50% of first-out
lenders and 50% of last-out lenders" [P50][Confirmed]. A worked pricing example from the same source:
the credit agreement quotes the borrower a single blended rate of SOFR + 800 bps; the AAL then
reallocates ("skims") that margin so the last-out lenders actually receive SOFR + 500 bps of spread
(they are taking most of the credit risk) while the first-out lenders receive SOFR + 300 bps (they get
paid first and take much less risk) [P50][Confirmed]. Proskauer's own deal data shows first
lien/unitranche structures made up 86% of the loans it worked on in 2022 [P51][Confirmed], and reports
that the market has been moving away from the classic separate senior-term-loan-plus-AAL model toward
unitranche facilities built from "a single senior term loan combined with a 'super-priority' cash
flow-based revolver," sometimes *without* a formal AAL at all — which creates open legal questions
about how payment priority will actually be enforced if the deal goes bankrupt [P51][Confirmed].

**Typical pricing (2026).** Coupon spreads on new unitranche issuance were reported "generally ranging
from 4.75% to 5.50%" in 2026 reporting, "nearly 25 basis points higher than year-end levels"
[Reported][Reported] — note this is the all-in blended spread quoted to the borrower, not the
first-out/last-out split described above.

## 1.4 DEAL ECONOMICS AND PRICING

**Reference rates.** US direct lending prices off SOFR (Secured Overnight Financing Rate); the UK/
Europe use SONIA and EURIBOR respectively as the equivalent floating reference rates. SOFR averaged
approximately 4.30% in Q1 2025 and Q2 2025, falling to approximately 3.70% in Q1 2026 and 3.60% in Q2
2026 [Reported][Reported] — consistent with the Fed at 3.75-4.00% as at mid-September 2026 noted in
prior project research.

**Spreads and compression.** Senior direct lending spreads have compressed since a 2022-2023 peak:
"Relative to the peaks in 2022 and 2023, spreads for new leveraged buyouts financed in the private and
syndicated credit markets have compressed over the course of 2024 and 2025" [Reported][Reported]. For
2026 specifically: asset yields on directly originated first-lien loans are projected to trough "in the
8.0% to 8.5% vicinity... even after factoring in a slight compression in spreads" [Reported][Reported];
spreads in the "traditional middle market remained modestly compressed" in both Q1 and Q2 2026
[Reported][Reported]. One direct market-update source states plainly that new loans were pricing about
25 bps *higher* in Q1 2026 than in Q4 2025, and that broadly syndicated loan spreads widened about
15-30 bps over the same window [P63][Reported, FETCHED] — i.e. within 2026 itself, spreads have wobbled
both up and down quarter to quarter even as the multi-year trend since 2023 is compression. This is a
useful nuance: "spread compression" is a multi-year story (2023 to 2025), not a straight line every
single quarter of 2026. One real-estate-adjacent source quotes corporate direct lending spreads at
S+450-500 bps producing 8.5%-9.5% all-in yields, with total leverage "typically 5-6x EBITDA, with senior
debt at 4-5x" [P61][Confirmed, FETCHED].

**Original issue discount (OID).** When a lender funds a loan below its face (par) value — e.g.
advancing $97m against a $100m commitment — the $3m gap is OID, effectively extra interest paid up
front to the lender rather than over the life of the loan [Reported][Reported]. Upfront/arrangement
fees are often structured the same way, as a reduction to the amount actually funded rather than a
separate invoice, so "upfront closing fees often function similarly to OID and are documented as OID"
[Reported][Reported]. Around 67-69% of BDCs and credit funds surveyed treat OID as incremental yield,
amortising it over the loan's life using the effective interest method, while funds using fair-value
accounting tend to recognise it immediately — a difference that makes reported yields hard to compare
across managers [Reported][Reported].

**Call protection / prepayment penalties.** Typical step-downs: 2% penalty if the borrower prepays in
year one, 1% in year two; "soft call" protection of 1-2% often applies only if the borrower repriced
purely to cut its interest rate within 6-12 months of closing; "make-whole" provisions require paying
the present value of interest that would have been earned through a set date; some loans simply
prohibit prepayment for an initial no-call period [Reported][Reported].

**Leverage multiples (debt/EBITDA).** These vary sharply by deal size. Upper-middle-market sponsor
buyouts were reported securing financing around 5.0x-5.5x EBITDA total leverage; lower-middle-market
deals cluster around 3.5x-4.5x, with one data set putting the average lower-middle-market deal at 4.0x
[Reported][Reported]; a separate 2026 dataset (GF Data, cited via a market-data aggregator) reported 80
completed lower-middle-market transactions in Q1 2026 at an average 7.3x total *enterprise value*/EBITDA
multiple (a purchase-price multiple, not the same as a leverage multiple) [Reported][Reported]. For
larger corporate direct lending, total leverage of 5-6x EBITDA (senior debt 4-5x) was cited above
[P61][Confirmed].

**Largest deals / moving upmarket.** Direct lending has grown large enough to compete directly with the
broadly syndicated loan (BSL) market for the biggest buyouts. One 2026 source states direct lending "now
match[es] the broadly syndicated loan market at $1.5-2 trillion in size" with a forecast to reach $3
trillion by 2028 [Reported][Reported], though as the brief notes, market-size figures vary hugely by
provider and by what counts as "private credit." At the largest deal end: reporting from 2023 (still
one of the largest deals cited by industry sources as a record) describes a $5.3bn private-credit loan
package to Finastra Group Holdings (a Vista Equity Partners portfolio company), comprising a $4.8bn
unitranche and a $500m revolver, provided by Oak Hill Advisors, Blue Owl Capital and HPS Investment
Partners among others [Reported, search-snippet only, original Bloomberg article returned 403 on
fetch — PAYWALLED-NOT-READ, so treat the exact split as reported-not-verified][Reported]. Europe's
largest direct-lending deal on record was separately reported at €4.5bn unitranche [Reported][Reported].
More broadly, "mega-unitranche" deals above $2bn became common from 2023-2024 as clubs of direct
lenders and BDCs combined firepower [Reported][Reported]. In competitive terms, 63% of US leveraged
buyouts larger than $1bn were financed in the broadly syndicated loan market in 2025 (versus 51% in
2024 and 39% in 2023) [P62][Confirmed, FETCHED] — showing the BSL market clawing *some* large-cap share
back from private credit in 2025, a useful counter-data-point to the "private credit takes everything
upmarket" narrative. In Europe, 1Q26 direct lending volumes were €31.7bn across 264 deals, up 55%
year-on-year, with large-cap deals reported to be compensating for a slowdown in overall M&A activity
[Reported][Reported].

## 1.5 COVENANTS AND DOCUMENTATION

**Maintenance vs incurrence covenants (cov-lite).** A maintenance covenant requires the borrower to
prove, on an ongoing basis — "typically quarterly" — that it is meeting agreed financial tests (e.g.
leverage below X times EBITDA), whether or not it takes any new action [P55][Confirmed, FETCHED]. An
incurrence covenant (the basis of "cov-lite" loans) is only tested if the borrower takes a specific
action, like issuing more debt or paying a dividend; absent that trigger, no test ever happens, so
performance can deteriorate quietly with no formal breach [Reported][Reported]. A cov-lite variant
sometimes seen even within nominally "covenanted" deals: the maintenance test only "benefits" revolving
lenders and is triggered only once revolver usage crosses a set threshold, meaning term lenders get no
real ongoing test, only a cross-default right if the revolver covenant is breached [P55][Confirmed].

**Is it still true that private credit kept covenants while the syndicated market lost them, in
2026?** Broadly yes, but with real erosion at the top of the market. Sidley Austin's March 2026 note
states maintenance covenants "remain the market standard" in private credit and that private credit
lenders "rely on contractual protections to monitor performance, manage risk and preserve value"
precisely because of their different lending model (concentrated club lending vs syndicated, dispersed
holders) [P55][Confirmed]. It also notes explicitly that cov-lite terms seen in private credit today
are "derived from the syndicated markets" — i.e., private credit has begun importing some syndicated-
market flexibility, not inventing its own, and has not fully replicated it [P55][Confirmed]. Separately,
one 2026 source reports the percentage of cov-lite loan packages reaching "as high as 93 percent" in
*larger* loans, while stating that "leverage-based maintenance testing continues to anchor the vast
majority of private credit structures" and that lower-middle-market lenders (Ares, Apollo, Blackstone
cited as examples) maintain a covenant retention rate around 98% [Reported][Reported]. Read together:
the claim "private credit retained covenants, syndicated lost them" still mostly holds at the
core/lower-middle-market end of private credit in 2026, but at the large-cap end — where private credit
increasingly competes head-to-head with syndicated loans for the same borrowers — private credit deals
increasingly look and price like cov-lite syndicated loans, eroding the historic covenant advantage
[Inferred, synthesis of P55 plus the cov-lite percentage reporting above].

Moody's research on *outcomes* (not just presence of a covenant) finds that lenders who can act early,
"armed with a maintenance covenant," recover more in a default than lenders who only discover trouble at
payment default, with an average recovery gap of about 10 percentage points across multiple default
cycles [Reported][Reported] — a concrete reason covenants matter beyond documentation prestige.

**EBITDA add-backs and "adjusted EBITDA."** Loan covenants are almost always written against "adjusted
EBITDA," not GAAP net income. EBITDA itself starts from consolidated net income (a GAAP figure) and
adds back interest, taxes, depreciation and amortisation [P55][Confirmed]. "Adjusted" EBITDA then adds
back further items management argues are one-off or non-recurring: restructuring costs, transaction
expenses, projected cost synergies, and other "extraordinary, unusual, or nonrecurring" items
[P55][Confirmed]. The controversy: there is no single, standardised definition of adjusted EBITDA — "in
practice it is and has always been a negotiated definition, varying from agreement to agreement"
[Reported][Reported], and research shows these add-backs are large and often do not pan out. Studies
covering different vintage years found that add-backs represented over 29% of management-projected
EBITDA and almost 55% of trailing-twelve-month reported EBITDA for a sample of large M&A/LBO deals
originated in 2022 [Reported, S&P Global study, PAYWALLED-NOT-READ on direct fetch, reported via search
snippet only][Reported]; for deals originated 2015-2020, 95% of companies failed to hit their first-year
EBITDA projections, and 2020-vintage deals ran with median leverage 2.1 turns higher than forecast for
2021 (three turns higher by 2022) [Reported, same study family, PAYWALLED-NOT-READ][Reported]. Direct
lenders have responded by capping the size of allowable EBITDA add-backs in middle-market deal
documents — one source cites caps around 25% of EBITDA [Reported][Reported]. The practical upshot for a
beginner: a covenant that looks comfortable (e.g. "leverage must stay below 6.0x adjusted EBITDA") can
mask real leverage that is meaningfully higher once the add-backs are stripped out.

**Amend-and-extend.** A negotiated modification where lender and borrower agree to push out a loan's
maturity (and often adjust pricing or covenants) rather than have the borrower refinance elsewhere or
default. Reporting frames 2026 as "a liability-management year," with refinancings making up 28% of
total direct lending activity in 2025 and dominating deal flow into 2026; "amend-to-extend" sits
alongside more aggressive tools — uptiering, drop-downs, double-dips — as a technique lenders and
borrowers are using to manage a wave of loan maturities [Reported][Reported]. One source frames the
market split starkly: "weaker credits are being pushed into amend-and-extend arrangements, while
stronger credits tap syndicated markets when opportunities arise" [Reported][Reported] — i.e.
amend-and-extend is itself a soft signal that a credit could not refinance cleanly at market terms.

**PIK toggles as a stress indicator.** A PIK toggle lets a borrower elect, usually under stress, to pay
some or all of its interest by adding it to principal instead of paying cash — deferring the cash
burden but growing the debt balance. Multiple 2026 sources treat rising PIK usage as an early-warning
signal of portfolio stress rather than a neutral financing feature. One dataset: the share of BDC
(business development company) loans structured with PIK rose from about 5.4% in Q1 2022 to 9.8% in Q1
2026, peaking near 9.85% in Q4 2025 — roughly a 67% relative increase over three years
[Reported][Reported], and PIK income specifically was reported at 8.1% of total BDC interest and
dividend income in 2025, up from 7.7% [Reported][Reported] (this sits close to, and roughly corroborates
in direction, the previously-established figures of "5.9% in 2023 to about 8% in 2026" from earlier
project research). A Federal Reserve Bank of Boston co-author is on record describing rising PIK usage
as "a sign of stress" [Reported][Reported]. Academically, PIK added *by amendment after a loan has
already been originated* (as opposed to PIK built into a deal from day one) is associated with a
1-2 percentage-point increase in the probability that the loan becomes delinquent the following quarter,
against an unconditional base delinquency probability of about 3% — i.e. amendment-driven PIK roughly
doubles near-term delinquency odds [Reported][Reported].

## 1.6 THE BORROWER

**Sponsor-backed vs non-sponsored.** A sponsor-backed borrower is owned by a private equity firm,
which typically runs the process of choosing the lender and negotiating terms, and which can inject
more equity if the company needs it — giving lenders extra comfort [Reported][Reported]. A
non-sponsored borrower (often family-owned, founder-owned, or an independent operating company with no
PE owner) borrows directly, with all terms bilaterally negotiated, no sponsor intermediary, and
typically no ready pool of additional equity to call on if things go wrong — which is why most private
credit funds have historically avoided this segment, seeing it as "more risky, complex and
labor-intensive" to underwrite [Reported][Reported]. Roughly 70%+ of direct lending activity is reported
to be sponsor-backed [Reported][Reported], though a number of managers (cited in coverage: Kennedy
Lewis, PennantPark, PGIM, among others) are explicitly building non-sponsored strategies to diversify
away from crowded sponsor-backed competition [Reported][Reported].

**Deal sourcing and company size.** Deals reach lenders mainly through relationships rather than cold
outreach: private equity sponsors are the largest single source of deal flow (since sponsors already
have relationships with a roster of lenders they use repeatedly), followed by investment banks running
formal sale processes, corporate advisors introducing family/founder-owned businesses, and referrals
from lawyers, accountants and consultants [P59][Confirmed, FETCHED]. "Good opportunities rarely appear
out of nowhere. They're introduced by people who already know the borrower, the sponsor, or the lender"
[P59][Confirmed]. Lenders screen very quickly on stable, predictable, recurring cash flow, experienced
management, reasonable leverage and a defensible market position; "funds often screen out deals within
days" if a business does not fit, and early-stage or speculative companies typically do not qualify for
conventional direct lending because "debt requires a predictable cash flow" [P59][Confirmed].

**Loan sizes.** Middle-market direct lending transactions range from roughly $5m at the smallest end to
well over $100m, scaling with borrower size, leverage and structure [Reported][Reported]. At the very
top, "mega-unitranche" deals now regularly exceed $2bn (see 1.4 above).

**Move upmarket.** As covered in 1.4, direct lending has expanded from its original middle-market home
into deals that would previously have gone exclusively to the broadly syndicated loan market — although
2025 data shows the BSL market clawing back some large (>$1bn) LBO share, so this is a genuine
back-and-forth competition rather than a one-way migration [P62][Confirmed].

## 1.7 THE LIFECYCLE OF A DEAL

1. **Sourcing.** A company needs capital (an acquisition, a refinancing, growth capital, a dividend
   recapitalisation). The introduction usually comes through a private equity sponsor's existing lender
   relationships, an investment bank running a formal process, or a referral network of advisors
   [P59][Confirmed].
2. **Sponsor relationship / screening.** For sponsor-backed deals, the sponsor typically pre-selects a
   shortlist of lenders it already trusts and controls much of the negotiation on the borrower's behalf
   [Reported][Reported]. Lenders run a fast initial screen against mandate criteria (sector, cash flow
   quality, leverage) and reject unsuitable deals within days [P59][Confirmed].
3. **Indicative terms / competing bids.** Lenders that pass the screen submit an indicative proposal —
   loan size, pricing, maturity, leverage, security package — not a binding commitment; multiple lenders
   may compete, and the borrower/sponsor picks finalists [P59][Confirmed].
4. **Due diligence.** The lender digs into the borrower's industry, financial history, business model,
   management team and growth prospects; this typically takes about 3-6 weeks [Reported][Reported]. The
   most common failure points are incomplete borrower diligence, underappreciated collateral/structural
   risk at underwriting, and inadequate ongoing monitoring set up from the start [Reported][Reported].
5. **Credit committee.** Findings are written up in a formal credit memo and presented to an internal
   credit committee, whose approval is required before the fund can commit capital [Reported][Reported].
6. **Term sheet.** Once commercial terms are agreed (loan size, pricing, maturity, covenants), they are
   set out in a term sheet that becomes "the blueprint for the financing" — in many direct lending deals
   this is taken seriously enough that separate commitment papers are skipped and full legal
   documentation follows directly from the term sheet [P58][Confirmed, FETCHED].
7. **Documentation.** Legal counsel drafts the credit agreement, security documents, guarantee
   agreements, fee letters and (where more than one class of lender exists) an intercreditor agreement
   or AAL; commercial and technical points (how a covenant is defined, what counts as a default) are
   negotiated in detail at this stage [P58][Confirmed].
8. **Conditions precedent and closing checklist.** Before any money moves, a checklist must be
   satisfied: signed legal agreements, corporate approvals, security perfected, legal opinions,
   know-your-customer (KYC) checks, and evidence that any existing debt being refinanced has actually
   been repaid [P58][Confirmed].
9. **Funding.** Documents are signed, conditions precedent are confirmed complete, funds are
   transferred, and the lender begins earning interest from that point [P58][Confirmed].
10. **Monitoring.** Ongoing surveillance through financial reporting, covenant testing, compliance
    certificates and regular contact with management; for asset-based deals this can include
    third-party collateral verification and quarterly (or per-deal) re-underwriting
    [Reported][Reported].
11. **Amendment.** If the borrower needs flexibility (a covenant waiver, a maturity extension, extra
    capacity to make an add-on acquisition), the parties negotiate an amendment; under stress this can
    include amend-and-extend or a PIK toggle election (see 1.5) [Reported][Reported].
12. **Exit or refinancing.** Most loans do not run to full contractual maturity; direct lending loans
    typically carry 5-7 year stated maturities but are refinanced or repaid earlier on average, with
    actual average time outstanding often only 3-4 years once refinancing activity is accounted for
    [Reported][Reported].
13. **Default and restructuring.** If the borrower cannot pay or breaches covenants, the lender (often
    now a private credit fund rather than a bank syndicate) leads a workout: this can mean an amendment,
    a liability management exercise (LME), a debt-for-equity swap, or — increasingly cited in 2026
    reporting — the sponsor simply handing the keys (equity) to the lenders without a fight rather than
    fighting for control, because private credit lenders in the middle market are often unwilling to
    wait out a long restructuring and instead push for a faster sale to a better-capitalised owner
    [P57][Confirmed, FETCHED]. Fitch Ratings reported a private credit default rate of 6.0% as of April
    2026 [Reported][Reported], and Proskauer's own default index (cited in prior established project
    research) moved from 1.84% to 2.73% across recent quarters. 2026 commentary frames private credit
    lenders as increasingly needing in-house workout/restructuring expertise, since "most direct lending
    teams scaled origination over the past five years, but almost none scaled workouts"
    [Reported][Reported]. Sectors flagged for elevated distress risk in 2026 outlooks include AI-exposed
    software/technology, education, consumer products, healthcare, chemicals, paper, packaging and
    building products [P57][Confirmed].

---

# 2. KEY NUMBERS TABLE

| Number | What it measures | As-of date | Source | Confidence |
|---|---|---|---|---|
| SOFR ~4.30% (Q1/Q2 2025) → ~3.70% (Q1 2026) → ~3.60% (Q2 2026) | US reference floating rate used to price direct loans | Q1-Q2 2026 | Search synthesis of market commentary | Reported |
| Direct-lending first-lien asset yields trough ~8.0%-8.5% | 2026 projected yield on senior direct loans | 2026 | Market commentary | Reported |
| Unitranche coupon spreads 4.75%-5.50% (~25 bps above year-end) | 2026 unitranche pricing | 2026 | Market commentary | Reported |
| S+450-500 bps, 8.5%-9.5% all-in yield; leverage 5-6x EBITDA (senior 4-5x) | Corporate direct lending spread/leverage | 2026 | [P61] CBRE | Confirmed (fetched) |
| Upper-mid-market leverage 5.0x-5.5x EBITDA; lower-mid-market 3.5x-4.5x (avg ~4.0x) | Sponsor buyout leverage by segment | 2026 | Market commentary/data aggregators | Reported |
| GF Data: 80 completed LMM deals, avg 7.3x EV/EBITDA | Purchase price multiple, not leverage | Q1 2026 | Market data aggregator | Reported |
| Unitranche AAL example: blended SOFR+800bps split into first-out SOFR+300bps / last-out SOFR+500bps | How AAL reallocates blended coupon | Illustrative, 2026 commentary | [P50] Mayer Brown | Confirmed (fetched) |
| 86% of Proskauer-documented 2022 loans were first lien/unitranche | Structural mix of private credit deals | 2022, cited 2026 | [P51] Proskauer | Confirmed (fetched) |
| Fund finance market $1.25-$1.75tn (>50% of respondents); >2/3 is subscription lines (82%); 94% closed a sub-line in 2025 | Fund finance market size/survey | April 2026 | [P54] Haynes Boone | Reported (vendor survey, fetched) |
| NAV loan market ~$150bn now, vendor projection $600-700bn by 2030 | NAV lending market size | 2026 | Market commentary | Reported (wide range across sources) |
| 17Capital Credit Fund 2 closed at $7.5bn, largest NAV loan fundraise on record; firm total $24bn raised | Single-fund NAV lending fundraise | March 2026 | Market commentary | Reported |
| NAV loan pricing SOFR + 300-600 bps | NAV loan cost | 2026 | Market commentary | Reported |
| SRT protection ~€800bn of loans outstanding end-2024 (~2% or less of covered banks' total loans); annual issuance grew <€5bn (2016) → €21bn (2024); avg. capital relief ~43 bps CET1 | Synthetic/significant risk transfer market | End-2024, published 2026 | [P60] BIS | Confirmed (fetched) |
| >€1.3tn of loan default risk transferred via SRT since 2016; ~1/3 of that in the last 2 years | Cumulative SRT volume | 2026 | [P62] Man Group | Confirmed (fetched) |
| 63% of US LBOs >$1bn financed in BSL market in 2025 (vs 51% in 2024, 39% in 2023) | Large-cap LBO financing venue share | 2025 | [P62] Man Group | Confirmed (fetched) |
| Cov-lite packages up to 93% in larger loans; LMM covenant retention ~98% (Ares/Apollo/Blackstone-type lenders cited) | Covenant erosion vs retention | 2026 | Market commentary | Reported |
| Maintenance covenant holders recover ~10 percentage points more than payment-default-only lenders on average | Value of maintenance covenants | Multi-cycle, cited 2026 | Moody's-sourced commentary | Reported |
| 2022-vintage EBITDA add-backs = 29%+ of projected EBITDA, ~55% of LTM reported EBITDA; 95% of 2015-2020 deals missed year-1 EBITDA projections | Scale of add-back inflation | Study covering 2015-2022 vintages, cited 2026 | S&P Global (PAYWALLED-NOT-READ) | Reported |
| Direct lender EBITDA add-back caps ~25% of EBITDA | Lender pushback on add-backs | 2026 | Market commentary | Reported |
| BDC PIK share of loans: ~5.4% (Q1 2022) → 9.8% (Q1 2026), peak 9.85% (Q4 2025); PIK = 8.1% of BDC interest/dividend income in 2025 (up from 7.7%) | PIK growth as stress signal | 2022-2026 | Fed Boston / market commentary | Reported |
| Amendment-driven PIK linked to +1-2 pp increase in next-quarter delinquency probability (vs ~3% base rate) | PIK as leading stress indicator | Academic/cited 2026 | Market commentary | Reported |
| Refinancings = 28% of total direct lending activity in 2025 | Amend/refinance activity | 2025 | Market commentary | Reported |
| Fitch private credit default rate 6.0% | Default rate | April 2026 | Fitch, cited via Forbes/market commentary | Reported |
| ≥70% of direct lending is sponsor-backed | Sponsor vs non-sponsor mix | 2026 | Market commentary | Reported |
| Direct lending loan sizes ~$5m to $100m+ in middle market; mega-unitranche >$2bn common since 2023-24; $5.3bn Finastra package ($4.8bn unitranche + $500m revolver) cited as a US record; €4.5bn cited as Europe's largest | Deal size range and records | 2023-2026 | Market commentary; Bloomberg (PAYWALLED-NOT-READ) | Reported |
| Direct loan maturities typically 5-7 years; average actual time outstanding ~3-4 years after refinancing | Loan tenor | 2026 | Market commentary | Reported |
| Due diligence typically takes 3-6 weeks | Deal timeline | 2026 | Market commentary | Reported |
| Litigation funding market ~$23.48bn (2026), projected $51.09bn by 2036 | ABF sub-sector sizing | 2026 | ResearchNester (vendor) | Reported |
| Infrastructure debt funds hold only ~8.1% of total infrastructure AUM; global infra debt volumes ~$1.05tn in 2025 (80% bank/20% capital markets) | Infrastructure debt market structure | Q1 2025 / 2025 | Market commentary | Reported |
| Private BB infra credit spreads ~high-200s-to-low-300s bps (yields ~7.0%+) vs public BB HY OAS ~176 bps (12m to April 2026) | Infra debt pricing premium over public HY | To April 2026 | Market commentary | Reported |
| US CRE 2026 maturity wall: ~$875bn (17.5% of ~$5.0tn outstanding) per one estimate; "over $800bn" per CBRE | Real estate refinancing pressure | 2026 | [P61] CBRE + market commentary | Reported/Confirmed (fetched for CBRE figure) |
| Non-bank lenders = 40% of non-agency CRE closings, Q4 2025 | Bank retrenchment in CRE | Q4 2025 | [P61] CBRE | Confirmed (fetched) |
| Compass 2026 survey (Oxane Partners, 380+ professionals): 83% expect AUM growth; 66% cite ABF/specialty finance as top growth driver, 60% fund finance, 56% direct lending | Where growth is concentrated | June 2026 | [P52] Alternative Credit Investor | Confirmed (fetched) |

---

# 3. VERBATIM QUOTES ACTUALLY READ (fetched pages only)

- [P50] Mayer Brown, "Understanding the Mechanics of an Unitranche Lending Structure" (2026-07):
  "a single secured credit facility in which two or more groups of lenders share in the same security
  interest"; "unlike traditional first lien/second lien deals with separate liens, unitranche
  arrangements feature only one lien, and the priority of payment is governed by an agreement among the
  lenders"; example split "SOFR + 800 basis points on all obligations," with the AAL directing "the
  margin is then split...such that the last out lenders receive 500 basis points...with the first out
  lenders receiving 300 basis points."
  URL: https://www.mayerbrown.com/en/insights/publications/2026/07/understanding-the-mechanics-of-an-unitranche-lending-structure

- [P51] Proskauer, "Private Credit Restructuring Trends: No AAL, No Problem?": "first lien/unitranche
  structures account for 86% of Proskauer originated loans in 2022"; "These senior secured unitranche
  deals commonly are comprised of a single senior term loan" combined with "a 'super-priority' cash
  flow-based revolver" without separate AALs.
  URL: https://www.proskauer.com/alert/private-credit-restructuring-trends-no-aal-no-problem

- [P52] Alternative Credit Investor, "ABF and specialty finance to lead private credit growth"
  (2026-06-04): "83 per cent of respondents expecting assets under management to increase over the next
  12 to 18 months"; ABF and specialty finance cited by "66%"; "ABF and specialty finance are leading
  growth because the market has moved beyond a simple direct lending story" (Kanav Kalia, Oxane
  Partners).
  URL: https://alternativecreditinvestor.com/2026/06/04/abf-and-specialty-finance-to-lead-private-credit-growth/

- [P54] Haynes Boone, 2026 Fund Finance Annual Report press release: "more than half of respondents
  estimating it at between $1.25-$1.75 trillion"; "More than 82 percent of respondents indicated that
  subscription facilities represent greater than two-thirds of the market"; "94 percent of survey
  participants reporting they closed subscription financings in 2025"; "72 percent of respondents expect
  moderate to significant growth in institutional NAV activity in 2026."
  URL: https://www.haynesboone.com/news/press-releases/2026-fund-finance-annual-report

- [P55] Sidley Austin, "Financial Covenants in Private Credit Transactions" (2026-03): maintenance
  covenants require "periodic — typically quarterly — compliance with specified financial metrics";
  "financial maintenance covenants benefit only revolving lenders, with term lenders receiving only
  cross-acceleration rights"; "private credit lenders rely on contractual protections to monitor
  performance, manage risk and preserve value"; adjusted EBITDA "begins with consolidated net income (a
  GAAP measure) and adds back interest, taxes, depreciation, and amortization," plus "extraordinary,
  unusual, or nonrecurring losses."
  URL: https://www.sidley.com/en/insights/newsupdates/2026/03/financial-covenants-in-private-credit-transactions

- [P56] Cambridge Associates, "Private Credit Strategies: An Introduction": senior debt funds "lend
  money to performing companies on a first lien senior secured basis"; subordinated capital "a loan or
  security that ranks lower than other loans with regard to claims on assets or earnings," "not repaid
  until after unsubordinated (senior) debt holders have been repaid," typically "between 10% to 20%
  equity exposure"; credit opportunities is "a broad range of strategies that are typically
  opportunistic... investing in companies in stressed or distressed situations"; specialty finance
  "pursue[s] a very broad array of niche strategies" with returns "rang[ing] from the high single digits
  to the high teens."
  URL: https://www.cambridgeassociates.com/insight/private-credit-strategies-introduction/

- [P57] Octus, "2026 Distressed Outlook": "We are going to see a lot of handing-over-the-keys
  transactions resulting from both the expiration of the extended runway created by LMEs as well as
  private credit workouts"; "Many private credit lenders are also unwilling to wait it out and instead
  push for a sale to a better-positioned owner"; "As many LMEs come back for a second-step conversation,
  there is a lot of focus on prebaking and prewiring a subsequent out-of-court restructuring."
  URL: https://octus.com/resources/articles/2026-distressed-outlook/

- [P58] Inside Private Credit (Substack), "From Term Sheet to Closing — How a Private Credit Deal Comes
  Together": "The loan size. Pricing. Maturity. Covenants" documented in a term sheet that is "the
  blueprint for the financing"; conditions precedent include "signed legal agreements, corporate
  approvals, security documents, legal opinions, know-your-customer (KYC) requirements, evidence that
  existing debt has been refinanced."
  URL: https://insideprivatecredit.substack.com/p/from-term-sheet-to-closing-how-a

- [P59] Inside Private Credit (Substack), "How a Private Credit Deal Is Sourced": "Funds often screen
  out deals within days"; qualifying businesses have "stable and predictable cash flows, recurring
  revenue, experienced management teams, reasonable leverage, strong market positions"; "debt requires a
  predictable cash flow"; "Good opportunities rarely appear out of nowhere. They're introduced by people
  who already know the borrower, the sponsor, or the lender."
  URL: https://insideprivatecredit.substack.com/p/how-a-private-credit-deal-is-sourced

- [P60] BIS, "The rise and risks of synthetic risk transfers" (r_qt2603c): "annual issuance of SRT
  tranches grew from less than €5 billion in 2016 to €21 billion in 2024"; as of end-2024 SRTs "provided
  protection to loan portfolios totaling approximately €800 billion," roughly "2% or less of total bank
  loans" across the EU, US, UK and Canada; average capital relief "approximately 43 basis points of
  Common Equity Tier 1 (CET1) capital... though this exceeded 100 basis points for some institutions."
  URL: https://www.bis.org/publ/qtrpdf/r_qt2603c.pdf

- [P61] CBRE, "Private Credit Stress: Contained or Contagious?" (dated 2026-05-11 per page metadata):
  "Credit enhancement sized to LTV, DY, and DSCR rather than EBITDA multiples"; "the 2026 maturity wall
  totaling over $800 billion"; "Total leverage typically runs 5-6x EBITDA, with senior debt at 4-5x";
  "Spreads are quoted over SOFR, typically S+450-500bps... with 8.5% to 9.5% yields"; alternative lenders
  held "40% of non-agency closings in Q4 2025."
  URL: https://www.cbre.com/insights/briefs/private-credit-stress-contained-or-contagious

- [P62] Man Group, "2026 Credit Outlook: Divergence Meets Opportunity": "Since 2016, default risk on
  more than €1.3 trillion of loans has been transferred using significant risk transfers (SRTs), with
  approximately one-third transferred in the past two years"; "63% of LBOs larger than $1 billion have
  been financed in the BSL market in 2025, compared to 51% in 2024 and 39% in 2023"; global high yield
  spreads "304 basis points over government bonds" as of 2025-11-30, "virtually unchanged from 305 bps
  on January 1, 2025."
  URL: https://www.man.com/insights/2026-credit-outlook

- [P63] Northleaf Capital, "Private Credit Market Update: Q1-2026": "new loans price ~25 basis points
  higher" in Q1 2026 vs Q4 2025; broadly syndicated loan spreads widened "~15-30 basis points on new
  issues from Q4-2025 to Q1-2026"; "direct lending continues to generate high single-digit unlevered
  asset returns, an attractive premium relative to public credit markets."
  URL: https://www.northleafcapital.com/news/private-credit-market-update-q1-2026

---

# 4. SOURCE TABLE ROWS

[P50] | Mayer Brown | Understanding the Mechanics of an Unitranche Lending Structure | 2026-07 | https://www.mayerbrown.com/en/insights/publications/2026/07/understanding-the-mechanics-of-an-unitranche-lending-structure | Accessed 2026-09-19 | FETCHED | Law firm client alert; mechanics and worked pricing example read in full — Confirmed
[P51] | Proskauer Rose LLP | Private Credit Restructuring Trends: No AAL, No Problem? | undated (2026 alert) | https://www.proskauer.com/alert/private-credit-restructuring-trends-no-aal-no-problem | Accessed 2026-09-19 | FETCHED | Law firm alert citing Proskauer's own deal database (86% stat) — Confirmed
[P52] | Alternative Credit Investor | ABF and specialty finance to lead private credit growth | 2026-06-04 | https://alternativecreditinvestor.com/2026/06/04/abf-and-specialty-finance-to-lead-private-credit-growth/ | Accessed 2026-09-19 | FETCHED | Reports on Oxane Partners' Compass 2026 survey (n=380+) — Confirmed as reported, vendor survey caveat applies to underlying numbers
[P53] | Alternative Credit Investor | The top private credit M&A deals of 2025 | 2025-12-31 | https://alternativecreditinvestor.com/2025/12/31/the-top-private-credit-ma-deals-of-2025/ | Accessed 2026-09-19 | FETCHED | Manager M&A deals (not loan deals); used for context on industry consolidation, not cited in main text numbers above — Reported
[P54] | Haynes Boone | 2026 Fund Finance Annual Report (press release) | 2026-04-27 | https://www.haynesboone.com/news/press-releases/2026-fund-finance-annual-report | Accessed 2026-09-19 | FETCHED | Vendor/law-firm annual survey; figures are respondent estimates, not audited market data — Reported
[P55] | Sidley Austin LLP | Financial Covenants in Private Credit Transactions | 2026-03 | https://www.sidley.com/en/insights/newsupdates/2026/03/financial-covenants-in-private-credit-transactions | Accessed 2026-09-19 | FETCHED | Law firm practitioner note — Confirmed
[P56] | Cambridge Associates | Private Credit Strategies: An Introduction | undated (current as of 2026 access) | https://www.cambridgeassociates.com/insight/private-credit-strategies-introduction/ | Accessed 2026-09-19 | FETCHED | Established institutional investment consultant taxonomy — Confirmed
[P57] | Octus | 2026 Distressed Outlook | undated (2026) | https://octus.com/resources/articles/2026-distressed-outlook/ | Accessed 2026-09-19 | FETCHED | Restructuring-industry trade outlet with named practitioner quotes — Confirmed
[P58] | Inside Private Credit (Substack) | From Term Sheet to Closing — How a Private Credit Deal Comes Together | undated (2026) | https://insideprivatecredit.substack.com/p/from-term-sheet-to-closing-how-a | Accessed 2026-09-19 | FETCHED | Independent trade-focused newsletter, not a primary source; used for process description only — Reported
[P59] | Inside Private Credit (Substack) | How a Private Credit Deal Is Sourced | undated (2026) | https://insideprivatecredit.substack.com/p/how-a-private-credit-deal-is-sourced | Accessed 2026-09-19 | FETCHED | Same caveat as P58 — Reported
[P60] | Bank for International Settlements | The rise and risks of synthetic risk transfers | BIS Quarterly Review, 2026 (r_qt2603c) | https://www.bis.org/publ/qtrpdf/r_qt2603c.pdf | Accessed 2026-09-19 | FETCHED | Primary regulator source, per brief's source hierarchy — Confirmed
[P61] | CBRE | Private Credit Stress: Contained or Contagious? | 2026-05-11 | https://www.cbre.com/insights/briefs/private-credit-stress-contained-or-contagious | Accessed 2026-09-19 | FETCHED | Major CRE brokerage/research house — Confirmed
[P62] | Man Group | 2026 Credit Outlook: Divergence Meets Opportunity | 2026 | https://www.man.com/insights/2026-credit-outlook | Accessed 2026-09-19 | FETCHED | Asset manager house view, citing BSL/SRT market data — Confirmed
[P63] | Northleaf Capital | Private Credit Market Update: Q1-2026 | 2026 (Q1 update) | https://www.northleafcapital.com/news/private-credit-market-update-q1-2026 | Accessed 2026-09-19 | FETCHED | Asset manager house view; limited detail retrievable from fetch — Reported
[P64] | Federal Reserve Bank of Boston | Early Warning Signals in Private Credit? What BDC Portfolios Reveal about Emerging Risks | 2026 | https://www.bostonfed.org/publications/current-policy-perspectives/2026/early-warnings-private-credit-bdc-portfolios.aspx | Accessed 2026-09-19 | SNIPPET | Central bank research source (per brief hierarchy) but only search-result snippet read, not full fetch — Reported
[P65] | (multiple, synthesized) | BDC PIK share and PIK income growth figures (5.4%→9.8%/9.85%; 8.1% of income) | 2022-2026 | search synthesis, no single fetchable URL | Accessed 2026-09-19 | SNIPPET | Numbers appeared consistently across several outlets' search snippets (PrivateEquityWire, Morningstar, InvestmentNews) but no single page was fully fetched — Reported
[P66] | PitchBook | EBITDA adjustments are getting ridiculous | undated | https://pitchbook.com/news/articles/ebitda-adjustments-are-getting-ridiculous | Accessed 2026-09-19 | PAYWALLED-NOT-READ | 403 on fetch; used only as corroboration that this is an established controversy, no numbers taken from it directly — Reported
[P67] | S&P Global Ratings | EBITDA Addback Study Shows Increased Debt Projection and Leverage Misses | 2026 (regulatory article series, prior years 2023-2024 also cited) | https://www.spglobal.com/ratings/en/regulatory/article/ebitda-addback-study-shows-increased-debt-projection-and-leverage-misses-s101670186 | Accessed 2026-09-19 | PAYWALLED-NOT-READ | 403 on fetch; add-back percentages (29%/55%, 95% miss rate) taken from search-result snippet of this study family only, not independently verified against full text — Reported
[P68] | Axios | Signs of distress are showing up in private credit | 2026-08-07 | https://www.axios.com/2026/08/07/private-credit-pik-distress | Accessed 2026-09-19 | PAYWALLED-NOT-READ | 403 on fetch; PIK/distress framing corroborated via other outlets' snippets — Reported
[P69] | Wikipedia | NAV lending | undated (2026 revision) | https://en.wikipedia.org/wiki/NAV_lending | Accessed 2026-09-19 | SNIPPET | Tertiary source, used only for the basic NAV-loan definition, corroborated elsewhere — Reported
[P70] | Clifford Chance | NAV Financing briefing | 2026-01 | https://www.cliffordchance.com/content/dam/cliffordchance/briefings/2026/01/nav-financing.pdf | Accessed 2026-09-19 | SNIPPET | Identified via search, not fetched in full; flagged as a gap below — Reported
[P71] | re-cap.com | Venture Debt Guide [2026]: Costs, Terms & Eligibility for Startups | 2026 | https://www.re-cap.com/financing-instruments/venture-debt | Accessed 2026-09-19 | SNIPPET | Non-bank lender's own marketing/guide content; pricing figures plausible and consistent with market commentary but vendor-authored — Reported
[P72] | PIMCO | Asset-Based Finance: Redefining the Private Credit Landscape | undated (2026) | https://www.pimco.com/us/en/investment-strategies/asset-based-finance | Accessed 2026-09-19 | SNIPPET | Major asset manager, used for general ABF framing only — Reported
[P73] | TPG | Asset-Based Finance: A Growing Frontier for Private Credit | undated (2026) | https://www.tpg.com/news-and-insights/asset-based-finance-a-growing-frontier-for-private-credit | Accessed 2026-09-19 | SNIPPET | Asset manager house view — Reported
[P74] | Financial Stability Board | Report on Vulnerabilities in Private Credit | 2026-05-06 | https://www.fsb.org/uploads/P060526.pdf | Accessed 2026-09-19 | SNIPPET | Primary regulator source per brief hierarchy; identified but not fully fetched in this workstream — Reported, flagged as gap
[P75] | Northleaf Capital | Asset-Based Specialty Finance Spotlight: Lending Against Music Royalty Assets | undated (2026) | https://www.northleafcapital.com/news/asset-based-specialty-finance-spotlight-lending-against-music-royalty-assets | Accessed 2026-09-19 | SNIPPET | Asset manager thought-piece — Reported
[P76] | Neuberger Berman | Music Royalties Explained: From Niche Market Segment to Institutional Asset Class | undated (2026) | https://www.nb.com/en/insights/article-music-royalties-explained-from-niche-market-segment-to-institutional-asset-class | Accessed 2026-09-19 | SNIPPET | Asset manager thought-piece — Reported
[P77] | Research Nester | Litigation Funding Investment Market Size, Growth Trends 2026-2036 | 2026 | https://www.researchnester.com/reports/litigation-funding-investment-market/2800 | Accessed 2026-09-19 | SNIPPET | Commercial market-research vendor; figures are vendor estimates — Reported
[P78] | PennantPark | Sponsor Vs. Non-Sponsor Backed Lending, What You Need to Know | undated (2026) | https://www.pennantpark.com/sponsor-vs-non-sponsor-backed-lending-what-you-need-to-know/ | Accessed 2026-09-19 | SNIPPET | Direct lender's own educational content — Reported
[P79] | Invesco | Direct Lending's Evolution: A Look Into Sponsored Versus Non-Sponsored | undated (2026) | https://www.invesco.com/us/en/insights/direct-lendings-evolution-a-look-into-sponsored-versus-non-sponsored.html | Accessed 2026-09-19 | SNIPPET | Asset manager educational content — Reported
[P80] | Maples Group | Aviation Financing and Leasing Trends 2026: Key Developments | 2026 | https://maples.com/knowledge/aviation-financing-leasing-trends-2026 | Accessed 2026-09-19 | SNIPPET | Law firm market note — Reported
[P81] | Ogier | Private credit's growing role in aviation finance | undated (2026) | https://www.ogier.com/news-and-insights/insights/private-credits-growing-role-in-aviation-finance/ | Accessed 2026-09-19 | SNIPPET | Law firm market note — Reported
[P82] | Oaktree Capital | Direct Lending: Benefits, Risks and Opportunities | undated | https://www.oaktreecapital.com/insights/insight-commentary/education/direct-lending | Accessed 2026-09-19 | SNIPPET | Asset manager educational content; used for maturity/hold-size figures — Reported
[P83] | Bloomberg | Private Credit Loans Are Growing Bigger and Breaking Records | 2023-08-17 | https://www.bloomberg.com/news/articles/2023-08-17/private-credit-loans-are-growing-bigger-and-breaking-records | Accessed 2026-09-19 | PAYWALLED-NOT-READ | 403 on fetch; Finastra $5.3bn deal figures taken from search-result snippet only, not independently confirmed against the article text — Reported
[P84] | Fitch Ratings (via secondary coverage) | Private credit default rate 6.0% | 2026-04 (reported) | (accessed via Forbes coverage, see P85) | Accessed 2026-09-19 | SNIPPET | Rating agency figure, but only seen quoted in secondary press, not on Fitch's own site — Reported
[P85] | Forbes | Rising Private Credit Defaults Are Testing Banks And Insurers | 2026-05-24 | https://www.forbes.com/sites/mayrarodriguezvalladares/2026/05/24/rising-private-credit-defaults-are-testing-banks-and-insurers/ | Accessed 2026-09-19 | SNIPPET | Contributor column citing Fitch data — Reported
[P86] | Moody's | Lend, extend, and then... | undated (2026) | https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html | Accessed 2026-09-19 | SNIPPET | Rating agency commentary; source of the maintenance-covenant recovery-gap statistic — Reported
[P87] | CapitalPad (aggregator, citing GF Data) | Lower Middle Market EBITDA Multiples: Data by Deal Size and Industry | 2026 | https://capitalpad.com/lower-middle-market-ebitda-multiples/ | Accessed 2026-09-19 | SNIPPET | Third-party aggregator citing GF Data; not the primary GF Data release itself — Reported
[P88] | Capstone Partners | Middle Market Leveraged Finance Update – Q1 2026 | Q1 2026 | https://www.capstonepartners.com/insights/middle-market-leveraged-finance-report/ | Accessed 2026-09-19 | SNIPPET | Investment bank market report — Reported
[P89] | CT Acquisitions | The Private Credit Market in 2026: $1.7 Trillion AUM, Top Firms, Growth Trends | 2026 | https://ctacquisitions.com/private-credit-market-2026/ | Accessed 2026-09-19 | SNIPPET | Secondary aggregator site; used only for general market-size framing, not relied on for a specific number in the findings above — Reported, low weight
[P90] | Origin Investments (citing MBA/Trepp-type data) | How Private Lenders are Reshaping Commercial Real Estate Financing | 2026 | https://origininvestments.com/how-private-lenders-are-reshaping-commercial-real-estate-financing/ | Accessed 2026-09-19 | SNIPPET | Real estate manager's own content citing third-party maturity data ($875bn/17.5%) — Reported
[P91] | Withintelligence | Private Credit Outlook 2026: Market Faces First Big Test | 2026 | https://www.withintelligence.com/insights/private-credit-outlook-2026/ | Accessed 2026-09-19 | SNIPPET | Trade-data provider outlook piece — Reported
[P92] | Alternative Credit Investor | Rise in distressed restructurings may have 'deferred' private credit stress | 2026-05-20 | https://alternativecreditinvestor.com/2026/05/20/rise-in-distressed-restructurings-may-have-deferred-private-credit-stress/ | Accessed 2026-09-19 | SNIPPET | Trade press; identified via search, not fully fetched — Reported
[P93] | ION Analytics / Debtwire | Private credit sidesteps LME fights as sponsors quietly cede control of struggling companies | 2026 | https://ionanalytics.com/insights/debtwire/private-credit-sidesteps-lme-fights-as-sponsors-quietly-cede-control-of-struggling-companies/ | Accessed 2026-09-19 | SNIPPET | Trade press; corroborates the Octus "handing over the keys" finding (P57) — Reported
[P94] | ION Analytics | European direct lending activity remains stable as large cap deals compensate for M&A slowdown – 1Q26 European Direct Lender Rankings | 2026 | https://ionanalytics.com/insights/debtwire/european-direct-lending-activity-remains-stable-as-large-cap-deals-compensate-for-ma-slowdown-1q26-european-direct-lender-rankings/ | Accessed 2026-09-19 | SNIPPET | Source of the €31.7bn/264 deals/+55% YoY figure — Reported
[P95] | PGIM | Enhancing Diversification Through Non-Sponsored Direct Lending | 2025-2026 | https://www.pgim.com/us/en/institutional/insights/annual-best-ideas/2025/enhancing-diversification-through-non-sponsored-direct-lending | Accessed 2026-09-19 | SNIPPET | Asset manager house view on non-sponsored lending — Reported
[P96] | MetLife Investment Management | Infrastructure Debt: A Compelling Private Credit Portfolio Addition | 2026 | https://investments.metlife.com/insights/private-capital/infrastructure-debt-a-compelling-private-credit-portfolio-addition/ | Accessed 2026-09-19 | SNIPPET | Insurer-affiliated asset manager house view; source of the infra spread-vs-public-HY comparison — Reported
[P97] | Golub Capital | The Bigger PIK-ture: Bringing Clarity to Payment-in-Kind Structures in Private Credit | undated (2026) | https://education.golubcapital.com/resource/the-bigger-pik-ture-bringing-clarity-to-payment-in-kind-structures-in-private-credit/ | Accessed 2026-09-19 | SNIPPET | Direct lender's own educational white paper on PIK — Reported
[P98] | Wikipedia | Unitranche debt | undated (2026 revision) | https://en.wikipedia.org/wiki/Unitranche_debt | Accessed 2026-09-19 | SNIPPET | Tertiary source, used only to corroborate structural/second-lien definitional language — Reported
[P99] | WallStreetPrep | Covenant-Lite Loans (Cov-Lite) | Debt Structure + Characteristics | undated | https://www.wallstreetprep.com/knowledge/covenant-lite-loans/ | Accessed 2026-09-19 | SNIPPET | Training-provider reference material, used only for baseline cov-lite definition, corroborated by P55 — Reported

---

# 5. GAPS

- **FSB Report on Vulnerabilities in Private Credit (2026-05-06, [P74])** and the **Federal Reserve
  Bank of Boston BDC study ([P64])** were identified as primary/near-primary sources but were only
  captured via search snippets in this workstream, not fully fetched and read. A future pass should
  fetch these directly (FSB PDF, Boston Fed page) for exact figures rather than relying on secondary
  paraphrase.
- **S&P Global's EBITDA add-back study series ([P67])**, **PitchBook's "EBITDA adjustments are getting
  ridiculous" ([P66])**, **Axios's PIK distress piece ([P68])**, and **Bloomberg's Finastra deal report
  ([P83])** all returned HTTP 403 on direct fetch. The specific percentages attributed to them (29%/55%
  add-back shares, 95% miss rate, the $5.3bn/$4.8bn Finastra unitranche breakdown) come only from
  search-engine snippets of those pages, not verified full text. Treat these numbers as Reported, not
  Confirmed, until re-fetched through an authenticated or alternate route.
- **Clifford Chance's NAV Financing briefing ([P70])** was found but not fetched; it likely contains the
  most detailed legal/structural explanation of NAV lending mechanics and would sharpen the "why
  controversial" section with primary legal-practitioner language.
- No SEC EDGAR filing (10-K, N-2, 8-K) was directly pulled in this workstream for a specific private
  credit BDC's actual realized spread, OID or leverage terms on a named deal; the pricing and leverage
  figures above are all market-commentary aggregates, not one company's disclosed loan terms. A future
  pass should pull a specific BDC 10-Q's schedule of investments to show one real, named loan's actual
  spread, OID and maturity as a worked example.
- Exact 2026 sector breakdown (software/healthcare/business services percentage of direct lending
  origination) was not confirmed with a specific numeric source in this pass; the qualitative claim that
  these sectors dominate borrowing is widely repeated in the searched material but a single quantified,
  attributable breakdown (e.g. from Lincoln International, Cliffwater or PitchBook LCD, as suggested by
  the brief) was not retrieved before the session's web-search quota was exhausted.
- A single authoritative bps-by-quarter spread series from Lincoln International or Cliffwater (the
  brief specifically flagged these as good sources) was not obtained; the spread-compression narrative
  above is stitched together from several asset managers' qualitative 2026 commentary rather than one
  clean index series.
- Music rights and litigation finance figures rely on vendor/asset-manager commentary rather than a
  named, sourced market-size study; treat the ABF sub-sector sizing as directional only.

---

# 6. WHAT A BEGINNER MUST UNDERSTAND FROM THIS

1. **Private credit is a ladder, not a monolith — where a lender sits changes everything.** The single
   most useful mental model is the capital structure ladder (senior secured → second lien →
   subordinated/mezzanine → equity). Best worked example: on one $140m buyout, a first-lien lender might
   put in $100m at SOFR+500 and expect to recover 80-90 cents on the dollar even in a bad outcome, while
   a mezzanine lender putting in $20m at a much higher rate plus warrants might recover little if the
   company is worth less than expected. Same company, same default, wildly different outcomes, purely
   because of where each lender sits on the ladder.

2. **Unitranche hides a real split behind a friendly single number.** The blended rate a borrower is
   quoted (say SOFR+800) is not what any one lender actually earns; a private Agreement Among Lenders
   splits that into a safer "first-out" slice (e.g. SOFR+300) and a riskier "last-out" slice (e.g.
   SOFR+500) that the borrower never sees. Best analogy: it's like two friends splitting a taxi fare
   evenly on the receipt, while privately agreeing that whoever gets dropped off first pays less because
   they're taking less of the risk that the meter keeps running. The receipt (credit agreement) looks
   simple; the real deal (the AAL) is not.

3. **Adjusted EBITDA is a negotiated fiction, and that matters for every covenant built on top of it.**
   Because there is no single legal definition of "adjusted EBITDA," and because add-backs have
   historically run to 30-55% of the reported number in some studies, a covenant that says "leverage
   must stay under 6.0x EBITDA" can be true on paper while real leverage is meaningfully higher. Best
   worked example: if a company's raw EBITDA is $20m but management adds back $8m of "one-off" costs to
   get to $28m of "adjusted EBITDA," a $140m loan looks like 5.0x leverage on the adjusted number but is
   actually 7.0x on the real number — the covenant cushion is an illusion until those add-backs are
   tested against reality.

4. **PIK is the canary in the coal mine.** Payment-in-kind, where interest gets added to the loan
   balance instead of paid in cash, is not inherently bad (it is built into many mezzanine deals from
   day one), but a rising share of loans switching to PIK *after* origination, under stress, is one of
   the clearest, most-cited real-time signals that a private credit portfolio is under pressure — more
   useful to watch than headline default rates, because it shows up before an outright default does.
   The 2022-to-2026 rise in BDC PIK share is the concrete, memorable data point to cite.

5. **Asset-based finance is where the growth is because it diversifies away from single-company risk.**
   Direct lending's whole risk is "will this one company's cash flow hold up." Asset-based finance
   spreads risk across a pool: hundreds of leases, thousands of consumer loans, or one royalty stream
   with decades of predictable history. Best worked example: a music royalty loan is backed by a
   catalogue's decades of steady, largely recession-resistant streaming and licensing income, which
   behaves nothing like a single mid-market manufacturer's cash flow — that difference in the underlying
   risk driver is exactly why ABF is being cited by two-thirds of surveyed practitioners as the sector's
   biggest growth engine, and it is the single best "why does this matter" line for an internship
   interview answer about private credit's future.
