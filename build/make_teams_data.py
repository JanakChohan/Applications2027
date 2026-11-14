import json, pathlib

V, SI, UA, NPE, CE = "Verified", "Supported inference", "Unverified account", "Not publicly established", "Conflicting evidence"


def rel(t, target, status, note="", sources=None):
    return {"type": t, "target": target, "status": status, "note": note, "sources": sources or []}


axes = {
    "geographies": [
        {"id": "geo-uk", "name": "UK & Ireland"},
        {"id": "geo-me", "name": "Middle East"},
        {"id": "geo-nordics", "name": "Nordics"},
        {"id": "geo-ch", "name": "Switzerland"},
        {"id": "geo-benelux", "name": "Benelux"},
        {"id": "geo-dach", "name": "Germany & Austria"},
        {"id": "geo-fr", "name": "France"},
        {"id": "geo-it", "name": "Italy"},
        {"id": "geo-iberia", "name": "Iberia"},
    ],
    "segments": [
        {"id": "seg-inst", "name": "Institutional"},
        {"id": "seg-tpw", "name": "Third Party Wealth"},
        {"id": "seg-ocio", "name": "OCIO / fiduciary"},
        {"id": "seg-ins", "name": "Insurance"},
        {"id": "seg-liq", "name": "Liquidity Solutions"},
    ],
    "functions": ["Sales (new business)", "Relationship management (existing clients)"],
}

teams = []


def team(**k):
    k.setdefault("group", None)
    k.setdefault("relations", [])
    k.setdefault("mandate_ids", [])
    k.setdefault("development_tags", [])
    k.setdefault("people_match", {})
    teams.append(k)


team(
    id="T-csg", name="Client Solutions Group (CSG)",
    name_basis="Goldman Sachs's own name. Campus and experienced-hire listings use 'Client Solutions Group', 'Global Client Solutions Group', 'Client Solutions Group / Sales' and 'Client Solutions Group (Sales)' [@R1-S10][@R1-S04][@R1-S09][@R1-S13].",
    name_status=V, kind="Umbrella client organisation of Goldman Sachs Asset Management (global)",
    summary="The part of Goldman Sachs Asset Management that develops client relationships and delivers investment solutions to institutional and third-party wealth clients worldwide, across public and private asset classes. Goldman's own listings gloss it as 'Sales' and call it 'the sales organization', but at least one London CSG team is also described as managing existing relationships, so it is not new-business-only.",
    intern_account="An umbrella term for everyone who speaks to clients, 'the equivalent of saying sales', covering sales, client relationship management and consultant relations, cut by coverage team, then client type, then sales versus relationship management. He also used 'CSG' for the sales side inside a team. {{UA}}",
    public_evidence="Goldman describes CSG as developing client relationships and delivering investment solutions 'for institutional and third-party wealth clients across the globe' [@R1-S10]. Listing titles equate it with sales [@R1-S04][@R1-S09][@R1-S14]. It has a named head (Matt Gibson) [@R6-S19] and its own management, strategy and finance team that runs sales budgeting, fundraising projections and Salesforce data governance [@R1-S13][@R1-S14]. A Goldman job advert lists the distribution channels as third party wealth, institutional, consultant, insurance and retirement [@R4-S09]. CSG roles are advertised in London, Frankfurt, Paris, Dubai, Doha, Stockholm, Milan and outside EMEA [@R1-S05][@R1-S06][@R1-S07][@R1-S08][@R5-S16][@R5-S17].",
    clients="Institutional investors (pension funds, endowments, foundations, sovereign wealth funds, insurers) and wealth intermediaries (private banks, wealth managers, advisers, platforms, multi-managers) [@R1-S20][@R1-S17].",
    decision_makers="Varies by client type: see each team.",
    needs="Varies by client type: see each team.",
    products="Goldman lists 'fixed income, equities, liquid alternatives, private equity, private credit, infrastructure and real estate' [@R1-S10].",
    channels="Direct institutional coverage, consultant relations, third-party wealth intermediaries, insurance and retirement channels [@R4-S09].",
    process="Not one process. Institutional business is usually won through consultant-led tenders and long due diligence; wealth business through approval by a gatekeeper and then adoption by advisers. {{SI}}",
    specialists="Portfolio management, product specialists, marketing, compliance, operations, legal, performance measurement and risk, accounting and billing [@R1-S10][@R1-S01].",
    business_model="CSG does not manage money. It is how the investment teams' strategies reach clients and how clients' needs reach the investment teams. Goldman does not disclose revenue, assets, flows or headcount for CSG or for any EMEA client team [@R2-S01].",
    languages="None at group level. Requirements are set team by team in job descriptions.",
    recruitment="The 2027 London Summer Analyst listing is filed under this group and contains no team-specific text [@R1-S02]. The 2026 cycle used sub-track titles such as 'Client Solutions Group, UK Institutional Sales' (search result only) [@R1-S31]. An applicant may apply to at most four business and location combinations a year [@R1-S02].",
    open_questions="How London applicants are allocated to a team. Whether the Client Coverage Group sits inside CSG or beside it. Whether London teams use 'CSG' to mean the sales side of a team.",
    sources=["R1-S10", "R1-S04", "R1-S09", "R1-S13", "R1-S14", "R1-S02", "R4-S09", "R6-S19", "R2-S01"],
    relations=[
        rel("Reports to", "Goldman Sachs Asset Management leadership within Asset & Wealth Management (exact line not published)", NPE, "A head of CSG is named publicly; the reporting line above that post is not stated in the sources read.", ["R6-S19"]),
        rel("Works with", "Portfolio management, trading, operations, performance measurement and risk, legal, compliance, accounting and billing", V, "", ["R1-S10"]),
        rel("Works with", "Client Coverage Group (CCG)", V, "CCG is described as 'partnering closely with the sales team'. No reporting line between the two is published.", ["R1-S11"]),
        rel("Distributes products for", "Goldman Sachs Asset Management investment teams across public and private markets", V, "", ["R1-S10"]),
    ],
    people_match={"segment": ["Multiple"], "coverage_contains": ["Global", "EMEA"]},
    mandate_ids=["M-R7-15", "M-R7-16"], development_tags=["All"],
)

team(
    id="T-ccg", name="Client Coverage Group (CCG)",
    name_basis="Goldman Sachs's own name, defined in a Hong Kong advert for 'the global CCG team' [@R1-S11]. London CCG titles were seen in search results only [@R1-S32]. A 'CCG Analyst' title is used for The Hague [@R5-S14].",
    name_status=V, kind="Function: service and retention of existing clients",
    summary="The group 'dedicated to retaining, expanding and supporting existing client relationships' through client service, operational support and risk management. It is the nearest public match to what the former intern called the relationship-management side.",
    intern_account="'CCG (Client Coverage Group)' is the label for the relationship-management side of each team: keeps existing clients, analyst base pay £48k against £52k for sales, more seats, sits opposite sales and does much the same work at analyst level. {{UA}}",
    public_evidence="The name and definition are confirmed [@R1-S11]. Official tasks: main point of contact for the client across portfolio management, trading, operations, legal and compliance; client queries; reporting; coordinating account openings, restructures and terminations; questionnaires and audit requests [@R1-S11]. Whether CCG sits inside CSG, and whether every London team has a CCG side, is not established. {{NPE}} The pay figures have no public support. {{UA}}",
    clients="Existing asset-management clients.",
    decision_makers="The client's investment staff, operations staff and, for reporting, trustees or committees. {{SI}}",
    needs="Accurate reporting, quick and correct answers, smooth account changes, early warning of problems. {{SI}}",
    products="'Equities, fixed income, and alternative - through various distribution vehicles' [@R1-S11].",
    channels="Existing mandates and fund holdings.",
    process="Onboarding, periodic reviews, query handling, account life-cycle events (openings, restructures, terminations), due-diligence questionnaires and audit requests [@R1-S11].",
    specialists="Strategic Client Services, Client Implementation, portfolio management, trading, operations, controllers, risk, legal, compliance, accounting and billing [@R1-S11].",
    business_model="Protects and grows revenue that already exists. Retained revenue is not new revenue, and the official wording itself includes 'expanding', so the sales and relationship-management split is not clean.",
    languages="None stated in the advert read.",
    recruitment="The Hong Kong Analyst/Associate advert asks for 3 to 5 or more years' experience, so it is not evidence of campus hiring into CCG [@R1-S11].",
    open_questions="Where CCG sits relative to CSG. Whether London campus hires are placed in CCG. Whether 'CCG' covers third-party wealth as well as institutional clients.",
    sources=["R1-S11", "R1-S32", "R5-S14"],
    relations=[
        rel("Works with", "Sales teams in the Client Solutions Group", V, "'Partnering closely with the sales team, keeping them abreast of recent interactions with clients.'", ["R1-S11"]),
        rel("Reports to", "Client Solutions Group", NPE, "No published reporting line. Do not draw one.", []),
    ],
)

team(
    id="T-uk", name="UK coverage (grouping)",
    name_basis="The former intern's label for the largest London coverage team. Public sources use 'UK and Ireland' for both the institutional and the third-party wealth businesses [@R6-S05][@R4-S08].",
    name_status=UA, kind="Regional grouping (explanatory)", group="T-csg",
    summary="A grouping used here to hold the UK-facing units together. Public evidence supports UK (and Ireland) institutional and third-party wealth businesses and a London-led UK fiduciary management business. It does not show a single 'UK team' with one head, and the OCIO business sits in an investment group, not in a regional sales team.",
    intern_account="The largest team by far, bringing in the most money, split into Institutional, Third Party Wealth and OCIO, each split again into sales and relationship management. {{UA}}",
    public_evidence="'Head of the UK and Ireland institutional business' was a public title until the holder became co-head of EMEA institutional client coverage [@R6-S05][@R6-S02]. A 'UK & Ireland Third Party Wealth team' is named in a Goldman advert seen through an aggregator [@R4-S08]. The UK fiduciary management business is led from London [@R3-S16]. Goldman publishes no UK assets, revenue or headcount, so 'largest' and 'most money' cannot be tested [@R2-S01]. {{NPE}}",
    clients="See UK Institutional, UK Third Party Wealth and OCIO.",
    decision_makers="See the three UK units.", needs="See the three UK units.", products="See the three UK units.",
    channels="Direct, consultant-led and intermediary.", process="See the three UK units.", specialists="See the three UK units.",
    business_model="Three different businesses that happen to share a geography: winning mandates from institutions, getting funds used by intermediaries, and taking delegated responsibility for whole portfolios.",
    languages="A UK Third Party Wealth sales-support advert required a native English speaker and no other language [@R1-S17].",
    recruitment="The former intern thinks the UK team is the most likely destination for an English-only London candidate. {{UA}} Every continental coverage advert read required a local language, which is consistent in direction [@R5-S05][@R5-S07].",
    open_questions="Whether a single UK head exists. Whether the three units recruit separately from the London summer programme.",
    sources=["R6-S05", "R6-S02", "R4-S08", "R3-S16", "R1-S17", "R2-S01"],
    relations=[rel("Covers clients in", "United Kingdom and Ireland", SI, "Ireland appears in the public names of both the institutional and third-party wealth businesses.", ["R6-S05", "R4-S08"])],
    people_match={"coverage_contains": ["UK"]},
    development_tags=["UK Institutional", "OCIO", "Third Party Wealth"],
)

team(
    id="T-uk-inst", name="UK Institutional",
    name_basis="The former intern's label. The 2026-cycle London listing was titled 'Client Solutions Group, UK Institutional Sales' (search result only; page expired) [@R1-S31]. Senior public titles: 'head of the UK and Ireland institutional business', then 'co-head of EMEA Institutional Client Coverage' [@R6-S05][@R6-S02].",
    name_status=SI, kind="Client segment within the UK grouping", group="T-uk",
    summary="Coverage of UK institutional investors. The former intern describes pension funds as dominant, with endowments and foundations and sovereign wealth funds also covered. Public evidence of named UK clients is almost entirely defined benefit pension schemes reached through OCIO or fiduciary mandates, plus older Local Government Pension Scheme mandates.",
    intern_account="His own team, on the sales side. 'The main team' and the one most likely to be hiring. Pension funds dominate; his project was client research on endowments and foundations. {{UA}}",
    public_evidence="Goldman's EMEA institutional marketing defines the institutional business as pension funds, endowments, foundations, sovereign wealth funds and insurers [@R1-S20]. The co-head of EMEA Institutional Client Coverage is quoted in the Shell OCIO announcement [@R3-S04][@R6-S02]. A head of EMEA defined contribution within CSG was reported appointed in June 2025 (search result only) [@R6-S26]. Public UK mandates outside OCIO are sparse: a Border to Coast emerging-markets equity sleeve (2023) and older local-authority mandates, some later terminated [@R7-S44][@R7-S46]. No public source names a current head of a 'UK Institutional sales' team. {{NPE}}",
    clients="Defined benefit pension schemes, defined contribution master trusts and providers, Local Government Pension Scheme funds and pools, endowments, foundations and charities, and official institutions. Which of these the London team actually covers beyond pension schemes is not publicly established.",
    decision_makers="Trustee boards and their investment sub-committees, the scheme's in-house investment staff or chief investment officer where one exists, the sponsoring employer on some decisions, and the investment consultant who advises the trustees and often runs the selection. For LGPS assets, increasingly the pool rather than the individual fund [@R3-S21].",
    needs="For closed defined benefit schemes: paying pensions as they fall due, hedging interest-rate and inflation risk, generating cash flow, and reaching an endgame (insurer buyout or run-on). Aggregate funding is strong: the PPF 7800 funding ratio was 133.7% at end October 2026 [@R3-S29]. For defined contribution: default-fund design under cost constraints and a push toward private markets [@R3-S20][@R3-S23].",
    products="Liability-driven and cashflow-driven investment, credit and fixed income, multi-asset, equity, private markets, and OCIO where the client wants to delegate. Goldman cited about $300bn globally in LDI and CDI in September 2025 [@R3-S04].",
    channels="Direct coverage of schemes and coverage of the consultants who advise them.",
    process="Typically: a consultant or trustee identifies a need, a shortlist is drawn, managers answer a request for proposal and due-diligence questionnaire, a final presentation is held, then legal negotiation, onboarding and transition. Cycles are long and the consultant's view of the manager matters throughout. {{SI}}",
    specialists="Consultant relations; the UK LDI and CDI pensions solutions team in fixed income [@R3-S13]; the OCIO and Multi-Asset Solutions teams; product specialists; request-for-proposal and marketing teams; legal and client implementation.",
    business_model="Few clients, large tickets, slow decisions, formal governance and published advisers. Revenue arrives as a management fee on a mandate or fund holding, at institutional rates. The structural trend (schemes maturing, buying out with insurers, or delegating to OCIO) means the same client may shrink, leave to an insurer, or hand everything to one provider.",
    languages="No UK institutional job description with a language requirement was read. {{NPE}}",
    recruitment="The 2026 London campus track carried the title 'UK Institutional Sales' (search result only) [@R1-S31]. The former intern says it is the team most likely to be hiring. {{UA}}",
    open_questions="Current head of UK institutional sales. Whether the team covers endowments, charities, LGPS, DC and sovereign institutions in practice. Whether it is split into sales and relationship management as described.",
    sources=["R1-S31", "R1-S20", "R6-S05", "R6-S02", "R6-S26", "R3-S04", "R3-S13", "R3-S29", "R3-S21", "R7-S44", "R7-S46"],
    relations=[
        rel("Covers clients in", "United Kingdom (public titles add Ireland)", SI, "", ["R6-S05", "R1-S31"]),
        rel("Reports to", "EMEA Institutional Client Coverage leadership", NPE, "The EMEA co-head title is public; the line from a UK team to it is not stated.", ["R6-S02"]),
        rel("Works with", "Consultant Relations", V, "Consultant relations 'creates a pipeline of business for the sales teams'.", ["R1-S21"]),
        rel("Works with", "OCIO / UK fiduciary management team", V, "The EMEA institutional co-head and the OCIO head are quoted together on UK OCIO announcements.", ["R3-S04", "R3-S07"]),
        rel("Works with", "UK LDI and CDI pensions solutions team (fixed income)", SI, "An investment and specialist team, not a coverage team.", ["R3-S13"]),
        rel("Distributes products for", "Goldman Sachs Asset Management public and private strategies", SI, "", ["R1-S10"]),
    ],
    people_match={"segment": ["Institutional"], "coverage_contains": ["UK", "EMEA institution", "EMEA defined contribution"]},
    mandate_ids=["M-R7-21", "M-R7-22", "M-R7-23", "M-R7-24", "M-R7-27", "M-R7-28"],
    development_tags=["UK Institutional"],
)

team(
    id="T-uk-tpw", name="UK Third Party Wealth (TPW)",
    name_basis="Goldman Sachs's own name: a job advert refers to the 'UK Third Party Wealth (TPW) Sales Team' [@R1-S17]; another, seen through an aggregator, to the 'UK & Ireland Third Party Wealth team' [@R4-S08]. A press release names the 'EMEA Third Party Wealth Business' [@R4-S01].",
    name_status=V, kind="Client segment within the UK grouping", group="T-uk",
    summary="Sells Goldman Sachs Asset Management funds, exchange-traded funds and alternatives to other firms that then use them for their own clients: private banks, wealth managers, financial advisers and multi-managers. The client is an intermediary, not the end investor.",
    intern_account="Sells Goldman funds to other wealth managers and private banks, who offer them to their own private clients. A friend interned on the relationship side. {{UA}} His named example of a fund sold to another bank's private bank is not publicly established. {{NPE}}",
    public_evidence="The UK TPW Sales Team 'is responsible for new business development' with 'private banks, wealth managers, financial advisors and multi-managers' [@R1-S17]. The UK & Ireland team's stated clients are private banks, wealth managers, fund of funds and independent financial advisers, offered traditional and alternative strategies as funds, ETFs or separately managed accounts [@R4-S08]. A UK head of ETF distribution is named publicly [@R6-S31]. The EMEA head from 2021 left in spring 2026 and no successor had been named in the sources found [@R4-S02]. A formal split into sales and relationship management is not publicly established. {{NPE}}",
    clients="Private banks, wealth managers and discretionary fund managers, advice networks and independent financial advisers, multi-managers and funds of funds, and the platforms through which they deal.",
    decision_makers="The fund selector or research team (the gatekeeper), the investment committee that approves the buy list or model portfolio, then individual portfolio managers and advisers who decide whether to use an approved fund. The end investor rarely chooses the fund directly.",
    needs="Funds that fit a model portfolio or buy list, at a share-class price that passes value assessment, with reliable reporting and someone who can explain performance to advisers. Under the Consumer Duty the distributor must be able to show fair value for retail customers [@R4-S31].",
    products="UCITS funds, active and index UCITS ETFs (active equity range from April 2025, further fixed-income ETFs in April 2026) [@R4-S01][@R4-S17], and evergreen private-markets funds and ELTIFs for eligible investors [@R4-S19][@R4-S20]. No Goldman Sachs Long-Term Asset Fund or UK model portfolio service was identified. {{NPE}}",
    channels="Gatekeeper approval, buy lists and model portfolios, fund platforms, and adviser-facing sales support.",
    process="Research and gatekeeper meetings, due diligence, approval, making the share class available on the platforms the firm uses, then adviser-by-adviser adoption and ongoing monitoring. Approval is permission to buy; it does not produce assets by itself. {{SI}}",
    specialists="Product specialists and client portfolio managers, the ETF distribution team, the Third Party Wealth Alternatives team [@R4-S11], marketing, and compliance for financial promotions.",
    business_model="Many clients, smaller tickets, flows that build gradually and can reverse quickly. Revenue is the fund's management fee on assets that arrive only when advisers allocate. Buying power is concentrating in model portfolio services and consolidated wealth groups, so fewer decisions move more money.",
    languages="'Native English speaker is essential'; no other language required [@R1-S17].",
    recruitment="A UK TPW sales-support analyst advert (closed, undated) [@R1-S17] and an experienced-hire vice president advert seen through aggregators [@R4-S08]. No campus evidence specific to this team.",
    open_questions="Head of the UK & Ireland team. Successor to the EMEA head. Whether a separate relationship-management side exists.",
    sources=["R1-S17", "R4-S08", "R4-S01", "R4-S02", "R4-S11", "R4-S17", "R4-S19", "R4-S20", "R4-S31", "R6-S31"],
    relations=[
        rel("Covers clients in", "United Kingdom (the aggregator-sourced team name adds Ireland)", V, "", ["R1-S17", "R4-S08"]),
        rel("Reports to", "EMEA Third Party Wealth Business", SI, "Inferred from the team naming in a Goldman advert; the line is not stated in a primary source read directly.", ["R4-S08"]),
        rel("Works with", "Third Party Wealth Alternatives business in EMEA", SI, "A specialist overlay for private-markets products sold through wealth firms.", ["R4-S11"]),
        rel("Works with", "ETF distribution", SI, "", ["R4-S17"]),
        rel("Distributes products for", "Goldman Sachs Asset Management funds and ETFs; Goldman Sachs Alternatives G-Series", V, "", ["R4-S19", "R1-S17"]),
    ],
    people_match={"segment": ["Third Party Wealth"], "coverage_contains": ["UK", "EMEA wealth"]},
    mandate_ids=["M-R7-30", "M-R7-17", "M-R7-18", "M-R7-19", "M-R7-20"],
    development_tags=["Third Party Wealth"],
)

team(
    id="T-ocio", name="OCIO / fiduciary management",
    name_basis="Goldman Sachs's own names: 'UK fiduciary management business', 'International OCIO and UK Fiduciary Management Team', 'Outsourced Chief Investment Officer business', 'EMEA OCIO Institutional Business' [@R3-S16][@R3-S01][@R3-S10][@R3-S11].",
    name_status=V, kind="Delegated-portfolio business within Multi-Asset Solutions (an investing group); global",
    summary="The business that takes delegated responsibility for running all or part of an institution's portfolio. It is global, not UK-only, and it sits in Multi-Asset Solutions, an investment group, not in a regional sales team. Client coverage works alongside it.",
    intern_account="One of three UK sub-teams. 'Pretty sure' it exists only in the UK team. Goldman can bring the client's in-house investment team into the firm. Recently won an award. 'Already over-hired'. {{UA}}",
    public_evidence="Not UK-only: Goldman reported $480bn of OCIO assets under supervision at 31 March 2026 and '$540+ billion' at 30 June 2026, with large US mandates and stated growth in the Netherlands, Germany and Switzerland [@R3-S09][@R8-S22][@R3-S10]. {{CE}} The fiduciary and OCIO teams sit within Multi-Asset Solutions [@R6-S18][@R1-S15], supported by a team of more than 300 people that was still growing in November 2025 [@R3-S07]. UK history: a leader hired from a consultant in late 2021 [@R3-S16], Short Brothers (£1.6bn, 2022) [@R3-S15], BAE Systems (about £23bn, 2023, in-house team transferred) [@R3-S01], Shell entities (about $40bn across countries, 2025) [@R3-S04]. Team transfer is reported only in some of the largest deals [@R7-S04]. Fee rates are not disclosed. {{NPE}} 'Over-hired' has no public support. {{NPE}}",
    clients="Corporate defined benefit pension schemes of all sizes; also a captive insurer and, in the United States, defined contribution plan advisory. Public UK names include the BAE Systems schemes, Shell UK pension entities, the Short Brothers Common Investment Fund, the Calor plan and the Northern Foods scheme (see the mandates register).",
    decision_makers="Trustee boards, advised by an independent consultant or evaluator who runs the tender; the sponsoring employer where it bears the cost or its in-house team is affected. In the public UK cases the advisers were Redington, Isio, PwC and Barnett Waddingham [@R3-S02][@R3-S04][@R3-S15].",
    needs="Governance capacity the trustees do not have in house, faster implementation, access to managers and private markets, integrated liability hedging, and a credible path to the scheme's endgame. Goldman's stated view is that sponsors increasingly ask whether running a pension scheme is core business [@R3-S07].",
    products="Delegated management: strategy advice (in full fiduciary management), asset allocation, manager selection using internal and external managers, liability hedging and reporting [@R3-S15][@R3-S08].",
    channels="Competitive tender. UK trust-based schemes must invite bids from at least three unconnected providers before fiduciary managers run 20% or more of assets [@R3-S24].",
    process="Tender run by a third-party evaluator, scored proposals and standardised performance data, trustee decision, then a long transition of assets and, in a few very large cases, of people.",
    specialists="Multi-Asset Solutions portfolio managers, the External Investing Group for manager selection, LDI and CDI specialists, transition management, legal and operations.",
    business_model="The fee is for running the whole portfolio, usually a low rate on a large base, with underlying managers' fees charged separately. A public UK scheme report (scheme name withheld) shows an asset-based fiduciary fee on the return-seeking and cashflow-driven portfolios with the LDI manager invoicing separately [@R3-S17]. In Goldman's filings, advisory and OCIO alternative accounts averaged 17 basis points in 2025, a firm-wide blend and not a mandate price [@R2-S01]. One appointment can be very large, but each is rare, slow and re-tendered.",
    languages="None found for UK roles. The OCIO Insurance advert in The Hague states none in the text read [@R1-S15].",
    recruitment="Senior hiring continued in September 2025 [@R3-S07]. A 'Client Relationship Manager (OCIO)' London title was seen in search results only [@R1-S33]. No analyst-level campus evidence.",
    open_questions="Goldman's UK-only OCIO assets and market rank. Its OCIO fee rates. Whether CSG summer analysts are placed with OCIO client coverage. Which of two 2026 awards the former intern saw.",
    sources=["R3-S01", "R3-S04", "R3-S07", "R3-S08", "R3-S09", "R3-S10", "R3-S11", "R3-S15", "R3-S16", "R3-S17", "R3-S24", "R6-S18", "R1-S15", "R8-S22", "R2-S01", "R7-S04"],
    relations=[
        rel("Reports to", "Multi-Asset Solutions (investment group)", V, "Public sources place the fiduciary and OCIO teams within Multi-Asset Solutions. This is 'sits within', as stated publicly; individual reporting lines are not published.", ["R6-S18", "R1-S15"]),
        rel("Works with", "EMEA Institutional Client Coverage and UK institutional coverage", V, "", ["R3-S04", "R3-S07"]),
        rel("Works with", "Trustees' independent advisers and tender evaluators", V, "Redington, Isio, PwC and Barnett Waddingham in the public UK cases.", ["R3-S02", "R3-S04", "R3-S15"]),
        rel("Covers clients in", "United Kingdom, Ireland, Netherlands, Germany, Switzerland, United States and Canada", V, "Mandates or stated activity in each; the business is global.", ["R3-S09", "R3-S10", "R3-S04"]),
        rel("Distributes products for", "Goldman Sachs internal strategies and external managers selected for client portfolios", V, "", ["R3-S15"]),
    ],
    people_match={"segment": ["OCIO"]},
    mandate_ids=["M-R7-01", "M-R7-02", "M-R7-03", "M-R7-04", "M-R7-05", "M-R7-06", "M-R7-07", "M-R7-08", "M-R7-09", "M-R7-10", "M-R7-25", "M-R7-26"],
    development_tags=["OCIO"],
)

team(
    id="T-consultant", name="Consultant Relations",
    name_basis="Goldman Sachs's own name: 'Consultant Relations' and 'Global Consultant Relations' [@R1-S21][@R6-S25].",
    name_status=V, kind="Function: coverage of investment consultants", group="T-csg",
    summary="Covers the investment consulting firms that advise institutional investors, rate managers and run selections. It does not win mandates directly; it builds the consultants' understanding of the firm so that sales teams are considered.",
    intern_account="One of the three functions inside CSG: 'covering the investment consultants who steer clients toward managers'. {{UA}}",
    public_evidence="An older London advert describes the team as working with the regional institutional sales teams and creating 'a pipeline of business for the sales teams', with UK and continental European travel [@R1-S21]. A managing director was reported as joining in September 2024 as head of international, global consultant relations, based in London [@R6-S25]. A Goldman advert lists 'institutional, third-party wealth, insurance and consultant relations teams' side by side [@R5-S42]. Whether the function formally sits inside CSG today is not established from a primary source read directly.",
    clients="Investment consulting firms: for UK pensions, firms such as WTW, Mercer, Aon, LCP, Hymans Robertson, Isio, XPS, Redington and Barnett Waddingham.",
    decision_makers="Consultants' manager-research teams (who rate strategies) and field consultants (who advise specific clients).",
    needs="Deep, consistent information on strategies, people and process; early notice of changes; access to portfolio managers.",
    products="No product of its own. It supports ratings across the firm's strategies.",
    channels="Research meetings, data submissions to consultant databases, strategy reviews.",
    process="Maintain ratings, respond to research requests, brief consultants on changes, and pass intelligence on searches to the sales teams.",
    specialists="Portfolio managers and product specialists for research meetings; the request-for-proposal team for data.",
    business_model="No direct revenue. Its value shows up as shortlists and ratings that make a sale possible. The consulting sector is consolidating, which concentrates this influence in fewer firms [@R3-S34].",
    languages="'A second European language' was listed as an advantage in the older advert [@R1-S21].",
    recruitment="Older associate advert (undated); vice president and analyst titles seen in search results only [@R1-S34].",
    open_questions="Current structure and exact place within CSG. Size of the London team.",
    sources=["R1-S21", "R1-S34", "R6-S25", "R5-S42", "R3-S34"],
    relations=[
        rel("Works with", "Regional institutional sales teams", V, "", ["R1-S21"]),
        rel("Covers clients in", "UK, continental Europe, Middle East, Africa and Asia (international head's remit as reported)", SI, "", ["R6-S25"]),
        rel("Reports to", "Client Solutions Group", NPE, "Listed alongside CSG channels in an advert summary; no reporting line is published.", ["R5-S42"]),
    ],
    people_match={"segment": ["Consultant Relations"]},
    development_tags=["UK Institutional"],
)

team(
    id="T-me", name="Middle East",
    name_basis="The former intern's label. No public team name was found. A former head's public title was 'head of MENA client business and new markets' [@R6-S14]. Listings: 'Client Solutions Group - Third Party Wealth' (Dubai) and 'Alternatives Capital Formation, Client Solutions Group' (Doha) [@R1-S07][@R1-S08].",
    name_status=SI, kind="Regional coverage", group="T-csg",
    summary="Coverage of Gulf and wider Middle East clients. Public evidence shows CSG hiring in Dubai and Doha, a growing set of local offices, and that the former regional head's team was spread across London, Riyadh, Dubai, Abu Dhabi and Doha. The split the former intern described is not established.",
    intern_account="Arabic is not required. He thinks it is split into Third Party Wealth and Institutional. His own assessment centre was for this team. {{UA}}",
    public_evidence="A former head of MENA client business left in September 2025; his team was based in London, Riyadh, Dubai, Abu Dhabi and Doha [@R6-S14]. The current head is not publicly established. {{NPE}} 2027 off-cycle roles are listed in Dubai (CSG Third Party Wealth) and Doha (Alternatives Capital Formation, CSG), with no language requirement stated [@R1-S07][@R1-S08]. Goldman has offices in Dubai, Doha and Riyadh, announced an Abu Dhabi office in 2023 [@R5-S29], opened Kuwait in October 2025 [@R5-S30] and officially opened a Riyadh regional headquarters in December 2025 [@R5-S28]. Whether Arabic is required and whether an 'Institutional' sub-team exists by name are not established. {{NPE}}",
    clients="Sovereign wealth funds and other official institutions, public pension funds, family offices, and local banks and wealth distributors. {{SI}}",
    decision_makers="Small senior investment teams and investment committees at state investors; family principals and their offices; product heads at local banks. {{SI}}",
    needs="Partnership-style relationships: separately managed accounts, co-investment, private markets access, knowledge transfer and local presence. {{SI}}",
    products="Publicly documented examples are alternatives: a $1bn private-credit separately managed account with Mubadala (2024) [@R5-S04] and other sovereign partnerships in the mandates register.",
    channels="Direct senior coverage; alternatives capital formation; third-party wealth distribution through regional banks.",
    process="Long, relationship-led and senior. Deals are often structured as partnerships with the alternatives business, not won through a consultant-run tender. {{SI}}",
    specialists="Goldman Sachs Alternatives (private credit, private equity), alternatives capital formation, and the firm's wider regional franchise.",
    business_model="Very few clients, each potentially enormous, with bespoke terms. A commitment or partnership announcement is not the same as funded, fee-paying assets, and a fundraising target is not a commitment.",
    languages="No language requirement stated in the Dubai or Doha listings [@R1-S07][@R1-S08]. Arabic: not publicly established either way.",
    recruitment="2027 off-cycle internships in Dubai and Doha [@R1-S07][@R1-S08]. That London assessment centres are run for a Middle East team is the former intern's account only. {{UA}}",
    open_questions="Current head. Whether London still houses Middle East coverage staff after the 2025 departures. The internal split.",
    sources=["R6-S14", "R1-S07", "R1-S08", "R5-S04", "R5-S28", "R5-S29", "R5-S30", "R5-S18"],
    relations=[
        rel("Covers clients in", "Middle East and North Africa", V, "From the former head's public title and team locations.", ["R6-S14"]),
        rel("Works with", "Goldman Sachs Alternatives on sovereign partnerships", SI, "", ["R5-S04"]),
        rel("Reports to", "Client Solutions Group", SI, "Dubai and Doha roles are listed under CSG; the regional reporting line is not published.", ["R1-S07", "R1-S08"]),
    ],
    people_match={"segment": ["Multiple"], "coverage_contains": ["Middle East", "MENA"]},
    mandate_ids=["M-R7-12", "M-R7-13", "M-R7-14"], development_tags=["Middle East"],
)

team(
    id="T-nordics", name="Nordics",
    name_basis="Job-advert names: 'Nordics Institutional Sales Support' (London) and 'TPW Nordic Client Coverage' (Copenhagen), both from search summaries [@R5-S08][@R5-S46]. A 2020 report describes one integrated Nordic team [@R5-S26].",
    name_status=SI, kind="Regional coverage", group="T-csg",
    summary="Coverage of Sweden, Denmark, Norway and Finland from Stockholm, Copenhagen and London. In 2020 institutional sales and third-party distribution were merged into one Nordic organisation, which shows a region need not be split the way the UK is described.",
    intern_account="A coverage team that needs a local language. {{UA}}",
    public_evidence="In May 2020 Goldman Sachs Asset Management merged third-party distribution and institutional sales into one Nordic organisation selling all asset classes to all client types, with staff in Stockholm, Copenhagen and London [@R5-S26]. A London Nordics Institutional Sales Support Analyst advert requires native Swedish and describes work with pension funds and sovereign wealth funds (search summary) [@R5-S08]. A 2027 Stockholm CSG off-cycle role is listed [@R5-S17]. Whether the 2020 structure still holds is not confirmed.",
    clients="Pension institutions and sovereign funds [@R5-S08]; insurers, described as part of 'the core' in older press [@R5-S47]; discretionary and advisory wealth managers, private banks and fund platforms on the wealth side [@R5-S46].",
    decision_makers="Large professional in-house investment teams with their own manager-research staff. {{SI}}",
    needs="Specialist strategies that in-house teams do not run themselves, at institutional fees, with strong sustainability standards. {{SI}}",
    products="All asset classes [@R5-S26].",
    channels="Direct to institutions; intermediaries for wealth.",
    process="Direct selection by professional buyers; formal public procurement for some state funds. {{SI}}",
    specialists="Product specialists; sustainable-investing capability inherited through NN Investment Partners.",
    business_model="Sophisticated, fee-sensitive buyers who can manage assets internally, so the manager is hired for what the client cannot do itself.",
    languages="Native Swedish for the London institutional sales-support seat (search summary) [@R5-S08].",
    recruitment="2027 Stockholm off-cycle CSG analyst [@R5-S17].",
    open_questions="Current head and whether the integrated 2020 structure persists. No Nordic mandate after 2001 was found in public sources.",
    sources=["R5-S08", "R5-S17", "R5-S26", "R5-S46", "R5-S47"],
    relations=[rel("Covers clients in", "Nordic countries", V, "", ["R5-S26"])],
    people_match={"coverage_contains": ["Nordic", "Sweden", "Finland"]},
    mandate_ids=["M-R7-29"], development_tags=["Nordics"],
)

team(
    id="T-ch", name="Switzerland",
    name_basis="Job-advert name 'TPW Switzerland team' [@R1-S18]; press name 'Swiss Third Party Wealth business' [@R4-S07].",
    name_status=V, kind="Regional coverage (publicly evidenced for Third Party Wealth)", group="T-csg",
    summary="Publicly evidenced as a third-party wealth business with its own head since early 2025, with a sales-support seat in London and a role in Zurich. Swiss institutional coverage was searched for and not found.",
    intern_account="A coverage team that needs a local language. {{UA}}",
    public_evidence="A London-based sales-support analyst was hired for the 'TPW Switzerland team' serving 'the Swiss client base' [@R1-S18]. The Swiss Third Party Wealth business has had a dedicated head since the start of 2025 [@R4-S07]. A Zurich third-party wealth alternatives role requires German, with other European languages preferred [@R5-S11], while the London advert mirror listed no language requirement. {{CE}}",
    clients="Private banks and wealth managers whose private clients are the end investors [@R4-S07].",
    decision_makers="Fund selection teams and chief investment offices at private banks; then relationship managers and discretionary portfolio managers who decide whether to use an approved fund. {{SI}}",
    needs="Funds and private-markets vehicles suitable for international private clients, available in the right share classes and jurisdictions. {{SI}}",
    products="Public and private asset offerings; alternatives for wealth through intermediaries [@R5-S11].",
    channels="Private-bank gatekeepers and their advisory and discretionary desks.",
    process="As for third-party wealth generally: approval first, usage second.",
    specialists="Third Party Wealth Alternatives; product specialists.",
    business_model="A concentrated set of very large private banks, so a single approval can open a large adviser base, and a single removal can close it.",
    languages="Mixed evidence: German required for a Zurich role [@R5-S11]; none listed on the London advert mirror [@R5-S06].",
    recruitment="Closed London sales-support posting [@R5-S06].",
    open_questions="Whether a Swiss institutional team exists and where it sits.",
    sources=["R1-S18", "R4-S07", "R5-S06", "R5-S11"],
    relations=[
        rel("Covers clients in", "Switzerland", V, "", ["R1-S18"]),
        rel("Reports to", "EMEA Third Party Wealth Business", NPE, "A Swiss head is named; the line above is not stated in the sources read.", ["R4-S07"]),
    ],
    people_match={"coverage_contains": ["Switzerland", "Swiss"]},
    development_tags=["Switzerland"],
)

team(
    id="T-benelux", name="Benelux",
    name_basis="Goldman Sachs's own names: 'BeNeLux Client Solutions Group' and, earlier, 'BeNeLux Institutional Sales Team' for the same London role [@R1-S01][@R1-S19].",
    name_status=V, kind="Regional coverage", group="T-csg",
    summary="Coverage of Belgium, the Netherlands and Luxembourg. The best-documented continental team: a live London advert describes one team doing both new business and existing relationships, and local offices in The Hague, Amsterdam and Brussels carry third-party wealth and client-coverage seats.",
    intern_account="A coverage team (Belgium, Luxembourg, Netherlands) that needs a local language. {{UA}}",
    public_evidence="The London-based BeNeLux Client Solutions Group 'is responsible for new business development and managing existing institutional client relationships' [@R1-S01]. Official junior tasks: prepare and follow up client and prospect meetings, answer day-to-day client queries, work with product specialists, marketing, compliance and operations, and support the Country Head [@R1-S01]. Third-party wealth sales roles are advertised in The Hague or Amsterdam and Brussels, and a 'CCG Analyst' title is used for The Hague (search summaries) [@R5-S12][@R5-S13][@R5-S14]. Goldman acquired NN Investment Partners in April 2022 [@R5-S23].",
    clients="Institutional clients in the three countries, notably Dutch pension funds and insurers; wealth intermediaries.",
    decision_makers="Pension fund boards and their fiduciary managers, who often select underlying managers on the fund's behalf. {{SI}}",
    needs="Dutch pension funds are moving to the new contribution-based system, with entitlements to transfer by 1 January 2028, which is rewriting hedging and return portfolios [@R5-S35].",
    products="'Traditional Public Markets to Private Assets' [@R1-S01]; former NN Investment Partners capabilities.",
    channels="Direct institutional coverage; fiduciary managers; wealth intermediaries.",
    process="For Dutch pensions, often through a fiduciary manager acting as the fund's gatekeeper. {{SI}}",
    specialists="Product specialists, marketing, compliance, operations [@R1-S01].",
    business_model="A market where Goldman is both a seller to fiduciary managers and, through the former NN business, a fiduciary manager itself.",
    languages="London institutional role: 'Native Dutch speaker is essential (written and oral fluency) with French an advantage' [@R1-S01].",
    recruitment="London Analyst/Associate advert posted October 2026 and live on 14 November 2026 [@R1-S01].",
    open_questions="Whether the team is formally split by channel. Where the 'external sales team' named in the advert sits.",
    sources=["R1-S01", "R1-S19", "R5-S12", "R5-S13", "R5-S14", "R5-S23", "R5-S35"],
    relations=[
        rel("Covers clients in", "Belgium, Netherlands, Luxembourg", V, "", ["R1-S01"]),
        rel("Works with", "Product specialists; marketing, compliance and operations; the Country Head", V, "", ["R1-S01"]),
    ],
    people_match={"coverage_contains": ["Benelux"]},
    mandate_ids=["M-R7-11", "M-R7-25", "M-R7-26"], development_tags=["Benelux"],
)

team(
    id="T-dach", name="Germany & Austria",
    name_basis="Listing and advert names: 'Client Solutions Group - Institutional Sales' (Frankfurt) [@R1-S05]; 'Institutional Sales Team for Germany & Austria' and 'German TPW team' (search summaries) [@R5-S15][@R5-S07].",
    name_status=V, kind="Regional coverage (Frankfurt)", group="T-csg",
    summary="Not mentioned by the former intern. Covered from Frankfurt, which is why it would not appear in a London team list. Institutional sales, third-party wealth and insurance seats are all evidenced there.",
    intern_account="Never came up. He said his list was 'everyone'. {{UA}}",
    public_evidence="The 2027 Frankfurt off-cycle listing is 'Client Solutions Group - Institutional Sales' for a German speaker [@R1-S05]; the 2026 Frankfurt new-analyst listing was 'Client Solutions Group / Sales' [@R1-S04]. A head of Third-Party Wealth for Germany and Austria took up the post on 1 July 2026 [@R6-S08]. An Insurance Client Solutions Group associate seat was advertised in Frankfurt (search summary) [@R5-S21].",
    clients="Institutional clients; private banks, wealth managers, financial advisers and multi-managers; insurers [@R5-S07][@R5-S21].",
    decision_makers="In-house investment teams at insurers and pension institutions; fund selectors at banks. {{SI}}",
    needs="Not researched to source.",
    products="The Goldman Sachs Asset Management range; no team-specific list.",
    channels="Direct institutional; bank and wealth intermediaries; insurance.",
    process="Not researched to source.", specialists="Insurance Asset Management; product specialists.",
    business_model="A local-language market served locally.",
    languages="German speaker (in the Frankfurt listing title) [@R1-S05]; native German and English for the German TPW team (search summary) [@R5-S07].",
    recruitment="2027 Frankfurt off-cycle internship; 2026 Frankfurt new analyst [@R1-S05][@R1-S04].",
    open_questions="Named head of institutional coverage for Germany and Austria.",
    sources=["R1-S05", "R1-S04", "R5-S07", "R5-S15", "R5-S21", "R6-S08"],
    relations=[rel("Covers clients in", "Germany and Austria", SI, "", ["R5-S15", "R6-S08"])],
    people_match={"coverage_contains": ["Germany"]},
    mandate_ids=["M-R7-02"],
)

team(
    id="T-fr", name="France",
    name_basis="Listing name 'Client Solutions Group - Third Party Wealth' (Paris) [@R1-S06]; 'EMEA French Sales Team' in an advert summary [@R5-S10].",
    name_status=V, kind="Regional coverage (Paris, with a London support seat)", group="T-csg",
    summary="Not mentioned by the former intern. A 2027 Paris listing places French third-party wealth coverage in Paris; a London sales-support seat for the French region has also been advertised.",
    intern_account="Never came up. {{UA}}",
    public_evidence="The 2027 Paris off-cycle listing is 'Client Solutions Group - Third Party Wealth' for a French speaker [@R1-S06]. A London sales-support role in the 'EMEA French Sales Team' required fluent French and English (search summary) [@R5-S10]. Institutional coverage of France was not established. {{NPE}}",
    clients="Third-party wealth clients (per the advert summary).", decision_makers="Not researched to source.", needs="Not researched to source.",
    products="Not specified; ETFs are sold from Paris [@R5-S45].", channels="Bank, insurer and private-bank distribution. {{SI}}",
    process="Not researched to source.", specialists="ETF distribution.",
    business_model="A local-language intermediary market.",
    languages="French speaker (Paris listing title) [@R1-S06]; French and English fluency for the London support seat (search summary) [@R5-S10].",
    recruitment="2027 Paris off-cycle internship [@R1-S06].",
    open_questions="Institutional coverage; named head.",
    sources=["R1-S06", "R5-S10", "R5-S45"],
    relations=[rel("Covers clients in", "France", SI, "", ["R5-S10", "R1-S06"])],
    people_match={"coverage_contains": ["France"]},
)

team(
    id="T-it", name="Italy",
    name_basis="No public team name found. A 'country head for Italy' title is public [@R6-S11]; Milan CSG and third-party wealth roles are listed (search summaries) [@R5-S16][@R5-S44].",
    name_status=SI, kind="Regional coverage (Milan)", group="T-csg",
    summary="Not mentioned by the former intern. Covered from Milan under a long-standing country head.",
    intern_account="Never came up. {{UA}}",
    public_evidence="A country head for Italy is named publicly and based in Milan [@R6-S11]. A 2027 Milan CSG off-cycle analyst role and a Milan third-party wealth sales associate role are listed (search summaries) [@R5-S16][@R5-S44]. 2025 reporting describes third-party wealth relationships with private banks, asset managers and insurers [@R5-S43].",
    clients="Private banks, asset managers and insurance companies as distributors [@R5-S43].", decision_makers="Not researched to source.",
    needs="Not researched to source.", products="Not specified.", channels="Bank and insurer distribution networks. {{SI}}",
    process="Not researched to source.", specialists="Not researched.",
    business_model="Distribution through large bank and insurance networks.",
    languages="No advert text read. {{NPE}}", recruitment="2027 Milan off-cycle CSG analyst (search summary) [@R5-S16].",
    open_questions="Institutional coverage; language requirement.",
    sources=["R6-S11", "R5-S16", "R5-S43", "R5-S44"],
    relations=[rel("Covers clients in", "Italy", SI, "", ["R6-S11", "R5-S16"])],
    people_match={"coverage_contains": ["Italy"]},
)

team(
    id="T-iberia", name="Iberia",
    name_basis="Public titles: 'Managing Director for Iberia' and, earlier, 'head of Distribution for Iberia' [@R6-S12][@R6-S13].",
    name_status=SI, kind="Regional coverage (Madrid)", group="T-csg",
    summary="Not mentioned by the former intern. The Iberia distribution head and her London team moved to Madrid in June 2021, which explains why Iberia is absent from a London team list.",
    intern_account="Never came up. {{UA}}",
    public_evidence="Goldman Sachs Asset Management moved its Iberia distribution head and her London team to Madrid in June 2021 [@R6-S13]. A managing director for Iberia is named publicly [@R6-S12]. Team structure and client segments are not established. {{NPE}}",
    clients="Not established.", decision_makers="Not established.", needs="Not established.", products="Not established.",
    channels="Private banks and bank networks. {{SI}}", process="Not established.", specialists="An alternatives specialist for Spain is named publicly [@R6-S12].",
    business_model="Not researched to source.",
    languages="No job advert found. {{NPE}}", recruitment="No 2027 Madrid CSG listing was seen.",
    open_questions="Structure, segments and languages. Iberia-specific searches were cut short when the search allowance ran out.",
    sources=["R6-S12", "R6-S13"],
    relations=[rel("Covers clients in", "Spain and Portugal", V, "From the public title and the 2021 relocation report.", ["R6-S13", "R6-S12"])],
    people_match={"coverage_contains": ["Iberia"]},
)

team(
    id="T-liq", name="Liquidity Solutions",
    name_basis="Goldman Sachs's own name: 'Liquidity Solutions', with a 'Global Head, Liquidity Solutions Client Business' [@R5-S01]; a London advert refers to an 'EMEA Liquidity Solutions' sales channel (search summary) [@R5-S09].",
    name_status=V, kind="Product-line client business (global)", group="T-csg",
    summary="A client business organised around a product, not a region: money market funds and short-duration strategies for clients with operating or strategic cash. It has global leadership shared with Insurance Asset Management and an EMEA sales seat in London.",
    intern_account="A product line with its own team 'because the product is strong'. He did not know how it is split. He said an English-only candidate could go there, then said everyone in it speaks French. {{UA}}",
    public_evidence="'Our Liquidity Solutions team oversees $1.2+ trillion in money market and short-term assets' as at 30 September 2026 (global) [@R5-S01]; firm-wide liquidity assets under supervision were $1,051bn at the same date [@R2-S02]. Clients: 'financial institution, hedge fund, institutional, corporate, and wealth management clients' [@R5-S01]. A London 'EMEA Liquidity Solutions Sales (UK Corporates)' seat covers UK corporate and insurance clients (search summary) [@R5-S09]. No evidence that French is required: the one French-speaker advert found belongs to the French sales team. {{NPE}} Its placement inside CSG is the former intern's account; public sources show its own global client-business head.",
    clients="Corporate treasurers, financial institutions, hedge funds, private equity and venture firms, public institutions, insurers, pension schemes holding collateral, and wealth clients.",
    decision_makers="Treasurers and treasury committees working to a board-approved investment policy; chief financial officers; collateral and operations managers at funds and schemes. {{SI}}",
    needs="Safety of capital first, same-day or next-day access second, yield third. Counterparty diversification, credit ratings and operational ease (portals, cut-off times) often decide the choice. {{SI}}",
    products="Money market funds: GS US$ Liquid Reserves and GS Euro Liquid Reserves (low-volatility net asset value), GS US$ Treasury Liquid Reserves (public debt constant net asset value); short-duration accounts and funds; fixed income ETFs; the Mosaic portal [@R5-S01].",
    channels="Direct treasury coverage and dealing portals.",
    process="Onboarding and counterparty approval, then daily subscriptions and redemptions with no sales event attached. The 'mandate' is permission to place cash; the balance moves every day.",
    specialists="Money market portfolio managers and credit analysts; operations and portal support.",
    business_model="Thin fee on a very large, very mobile balance. The investor earns the portfolio yield net of the fund charge; the manager earns that charge on average balances. Firm-wide, liquidity products earned an average 14 basis points in 2025 [@R2-S01]. Balances can leave in a day for reasons unrelated to service.",
    languages="None seen in the UK Corporates advert summary [@R5-S09]. French requirement: not publicly established.",
    recruitment="Experienced-hire London postings only; no student-programme evidence specific to liquidity.",
    open_questions="Internal split; whether CSG summer analysts are placed here; EMEA head.",
    sources=["R5-S01", "R5-S02", "R5-S09", "R2-S01", "R2-S02", "R5-S32"],
    relations=[
        rel("Distributes products for", "Fixed Income and Liquidity Solutions (money market and short-duration portfolio management)", V, "", ["R5-S01"]),
        rel("Works with", "Insurance Asset Management (shared global head)", V, "", ["R5-S01", "R5-S02"]),
        rel("Covers clients in", "EMEA from London, including UK corporates", SI, "", ["R5-S09"]),
        rel("Reports to", "Client Solutions Group", UA, "Placement inside CSG is the former intern's account. Public sources show a global head of the liquidity client business.", ["R5-S01"]),
    ],
    people_match={"segment": ["Liquidity"]},
    development_tags=["Liquidity Solutions"],
)

team(
    id="T-ins", name="Insurance",
    name_basis="Goldman Sachs's own names: 'Insurance Asset Management' and, in advert titles, 'Insurance Client Solutions Group' [@R5-S02][@R5-S21].",
    name_status=V, kind="Client vertical (global)", group="T-csg",
    summary="A global client vertical for insurance companies' own balance-sheet assets. It has named global heads and seats in London and Frankfurt, and was extended in Europe by the NN Investment Partners acquisition.",
    intern_account="Its own client base, mentioned as an afterthought. Where it sits is unclear. {{UA}}",
    public_evidence="Goldman Sachs Asset Management states it manages '$651 billion in general account assets on behalf of insurance clients' as at 31 December 2025 [@R5-S02]. Its offer is partial to full outsourcing across fixed income, alternatives and equities, plus advice on asset-liability management, strategic asset allocation and capital-efficient strategies [@R5-S02]. 'Insurance Client Solutions Group' roles have been advertised in London and Frankfurt (search summaries) [@R5-S21][@R5-S22]. A CSG advert lists insurance beside institutional and third-party wealth as a peer channel (search summary) [@R5-S42]. Whether EMEA insurance staff report regionally or to the global vertical is not established. {{NPE}}",
    clients="Life, health, property and casualty, and reinsurance companies [@R5-S21].",
    decision_makers="The insurer's chief investment officer and chief financial officer, with actuarial, risk and capital-management teams involved in every decision.",
    needs="Assets that match liabilities, earn spread, and use regulatory capital efficiently. The rulebook is changing: amended EU Solvency II rules apply from 30 January 2027 [@R5-S39]; the UK regulator has consulted on faster access to matching-adjustment benefits [@R5-S38]. In Goldman's 2026 survey of 434 insurance investment and finance chiefs, 62% planned to increase private-asset allocations [@R5-S03].",
    products="Investment-grade fixed income, private credit and asset-backed finance, and full or partial outsourcing of the general account [@R5-S02].",
    channels="Direct coverage by insurance specialists.",
    process="Solution design around the insurer's balance sheet, with constraints on capital charges, accounting treatment, book yield and realised gains written into guidelines.",
    specialists="Insurance strategists, the OCIO Insurance team within Multi-Asset Solutions [@R1-S15], fixed income and private credit teams.",
    business_model="Large, sticky, low-fee fixed-income mandates where the manager is judged on yield, capital use and accounting outcomes as much as on return against an index.",
    languages="Not read in a job description. {{NPE}}",
    recruitment="Experienced-hire postings in London and Frankfurt (search summaries) [@R5-S21][@R5-S22].",
    open_questions="Reporting structure in EMEA; EMEA head; whether CSG summer analysts are placed here.",
    sources=["R5-S02", "R5-S03", "R5-S21", "R5-S22", "R5-S23", "R5-S38", "R5-S39", "R5-S42", "R1-S15"],
    relations=[
        rel("Works with", "Liquidity Solutions (shared global head)", V, "", ["R5-S01", "R5-S02"]),
        rel("Works with", "OCIO Insurance team within Multi-Asset Solutions", V, "", ["R1-S15"]),
        rel("Works with", "Institutional, third-party wealth and consultant relations teams", SI, "", ["R5-S42"]),
        rel("Reports to", "Global Insurance Asset Management leadership or regional CSG leadership", NPE, "Which applies in EMEA is not published.", []),
    ],
    people_match={"segment": ["Insurance"]},
    mandate_ids=["M-R7-11"], development_tags=["Insurance"],
)

M = []


def cell(geo, seg, team_id, status, note, sources=None):
    M.append({"geo": geo, "segment": seg, "team": team_id, "status": status, "note": note, "sources": sources or []})


# UK & Ireland
cell("geo-uk", "seg-inst", "T-uk-inst", SI, "2026 London listing titled 'UK Institutional Sales' (search result only); 'UK and Ireland institutional business' was a senior public title.", ["R1-S31", "R6-S05"])
cell("geo-uk", "seg-tpw", "T-uk-tpw", V, "Goldman advert names the 'UK Third Party Wealth (TPW) Sales Team'.", ["R1-S17"])
cell("geo-uk", "seg-ocio", "T-ocio", V, "UK fiduciary management business led from London; BAE Systems, Shell and other public mandates.", ["R3-S16", "R3-S01", "R3-S04"])
cell("geo-uk", "seg-ins", "T-ins", SI, "'Insurance Client Solutions Group' role advertised in London (search summary).", ["R5-S22"])
cell("geo-uk", "seg-liq", "T-liq", SI, "London 'EMEA Liquidity Solutions Sales (UK Corporates)' seat (search summary).", ["R5-S09"])
# Middle East
cell("geo-me", "seg-inst", "T-me", SI, "A MENA client business with London and Gulf staff is public; an 'Institutional' sub-team by name is the former intern's account only.", ["R6-S14", "R1-S08"])
cell("geo-me", "seg-tpw", "T-me", V, "2027 Dubai listing: 'Client Solutions Group - Third Party Wealth'.", ["R1-S07"])
cell("geo-me", "seg-ocio", None, NPE, "No Middle East OCIO client or seat found in the sources read; not searched for specifically.")
cell("geo-me", "seg-ins", None, NPE, "No Middle East insurance seat found. Insurance is run as a global vertical.")
cell("geo-me", "seg-liq", None, NPE, "No Middle East liquidity seat found. Liquidity is run as a global product line.")
# Nordics
cell("geo-nordics", "seg-inst", "T-nordics", SI, "London 'Nordics Institutional Sales Support' advert, native Swedish (search summary); integrated Nordic team reported in 2020.", ["R5-S08", "R5-S26"])
cell("geo-nordics", "seg-tpw", "T-nordics", SI, "Copenhagen 'TPW Nordic Client Coverage' roles (search summary).", ["R5-S46"])
cell("geo-nordics", "seg-ocio", None, NPE, "No Nordic OCIO mandate or seat found.")
cell("geo-nordics", "seg-ins", "T-nordics", SI, "Older press calls pension and insurance companies 'the core' Nordic client base; no dedicated Nordic insurance seat found.", ["R5-S47"])
cell("geo-nordics", "seg-liq", None, NPE, "No Nordic liquidity seat found.")
# Switzerland
cell("geo-ch", "seg-inst", None, NPE, "Searched for; no Swiss institutional coverage team or head found.")
cell("geo-ch", "seg-tpw", "T-ch", V, "'TPW Switzerland team' in a Goldman advert; dedicated head since early 2025.", ["R1-S18", "R4-S07"])
cell("geo-ch", "seg-ocio", "T-ocio", SI, "Goldman cites Switzerland among markets where its OCIO business is growing; no Swiss mandate is named.", ["R3-S10"])
cell("geo-ch", "seg-ins", None, NPE, "No Swiss insurance seat found.")
cell("geo-ch", "seg-liq", None, NPE, "No Swiss liquidity seat found.")
# Benelux
cell("geo-benelux", "seg-inst", "T-benelux", V, "London 'BeNeLux Client Solutions Group': new business and existing institutional relationships; native Dutch.", ["R1-S01"])
cell("geo-benelux", "seg-tpw", "T-benelux", SI, "Third-party wealth sales roles in The Hague, Amsterdam and Brussels (search summaries); a Benelux TPW head reported.", ["R5-S12", "R5-S13", "R6-S10"])
cell("geo-benelux", "seg-ocio", "T-ocio", V, "OCIO Insurance team in The Hague within Multi-Asset Solutions; Dutch fiduciary heritage.", ["R1-S15", "R6-S18"])
cell("geo-benelux", "seg-ins", "T-ins", SI, "NN Group strategic partnership after the NN Investment Partners acquisition (partnership terms from secondary reporting).", ["R5-S23", "R5-S24"])
cell("geo-benelux", "seg-liq", None, NPE, "No Benelux liquidity seat found.")
# Germany & Austria
cell("geo-dach", "seg-inst", "T-dach", V, "2027 Frankfurt listing: 'Client Solutions Group - Institutional Sales', German speaker.", ["R1-S05"])
cell("geo-dach", "seg-tpw", "T-dach", V, "Head of Third-Party Wealth for Germany and Austria named from 1 July 2026.", ["R6-S08"])
cell("geo-dach", "seg-ocio", "T-ocio", V, "The Shell OCIO mandate includes about $2.8bn in Germany.", ["R3-S04"])
cell("geo-dach", "seg-ins", "T-ins", SI, "Frankfurt 'Insurance Client Solutions Group' associate advert (search summary).", ["R5-S21"])
cell("geo-dach", "seg-liq", None, NPE, "No German or Austrian liquidity seat found.")
# France
cell("geo-fr", "seg-inst", None, NPE, "Searched for; no French institutional coverage team or head found.")
cell("geo-fr", "seg-tpw", "T-fr", V, "2027 Paris listing: 'Client Solutions Group - Third Party Wealth', French speaker.", ["R1-S06"])
cell("geo-fr", "seg-ocio", None, NPE, "No French OCIO mandate or seat found.")
cell("geo-fr", "seg-ins", None, NPE, "No French insurance seat found.")
cell("geo-fr", "seg-liq", None, NPE, "No French liquidity seat found. The former intern's remark that liquidity staff speak French has no public support.")
# Italy
cell("geo-it", "seg-inst", None, NPE, "A country head for Italy is public; institutional coverage is not separately evidenced.", ["R6-S11"])
cell("geo-it", "seg-tpw", "T-it", SI, "Milan third-party wealth sales role (search summary); 2025 reporting on Italian wealth distribution.", ["R5-S44", "R5-S43"])
cell("geo-it", "seg-ocio", None, NPE, "No Italian OCIO mandate or seat found.")
cell("geo-it", "seg-ins", None, NPE, "Insurers appear as distributors in Italy; no general-account insurance seat found.", ["R5-S43"])
cell("geo-it", "seg-liq", None, NPE, "No Italian liquidity seat found.")
# Iberia
cell("geo-iberia", "seg-inst", None, NPE, "Not established. Iberia-specific searches were cut short.")
cell("geo-iberia", "seg-tpw", "T-iberia", SI, "An Iberia 'distribution' head and team moved from London to Madrid in 2021; the channel split is not stated.", ["R6-S13", "R6-S12"])
cell("geo-iberia", "seg-ocio", None, NPE, "No Iberian OCIO mandate or seat found.")
cell("geo-iberia", "seg-ins", None, NPE, "No Iberian insurance seat found.")
cell("geo-iberia", "seg-liq", None, NPE, "No Iberian liquidity seat found.")

out = {"axes": axes, "teams": teams, "matrix": M}
p = pathlib.Path("/home/user/Applications2027/data/teams.json")
p.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")

# ---- validation
import glob, re
root = pathlib.Path("/home/user/Applications2027")
src = set()
for f in glob.glob(str(root / "data/sources/*.json")):
    src |= {s["id"] for s in json.load(open(f))}
mids = {m["id"] for m in json.load(open(root / "data/fragments/mandates.R7.json"))}
bad = set()
txt = json.dumps(out)
for sid in re.findall(r"\[@([A-Za-z0-9\-]+)\]", txt):
    if sid not in src:
        bad.add(sid)
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == "sources":
                for s in v:
                    if s not in src: bad.add(s)
            else: walk(v)
    elif isinstance(o, list):
        for x in o: walk(x)
walk(out)
print("unknown sources:", sorted(bad))
for t in teams:
    for m in t["mandate_ids"]:
        if m not in mids: print("bad mandate", t["id"], m)
pairs = {(c["geo"], c["segment"]) for c in M}
print("cells", len(M), "expected", len(axes["geographies"]) * len(axes["segments"]), "unique", len(pairs))
ids = {t["id"] for t in teams}
for t in teams:
    if t["group"] and t["group"] not in ids: print("bad group", t["id"])
for c in M:
    if c["team"] and c["team"] not in ids: print("bad team", c)
# people matches
P = json.load(open(root / "data/fragments/people.R6.json"))
for t in teams:
    pm = t["people_match"]
    hit = []
    for p_ in P:
        seg_ok = (not pm.get("segment")) or any(s.lower() in (p_.get("segment") or "").lower() for s in pm["segment"])
        cov_ok = (not pm.get("coverage_contains")) or any(c.lower() in ((p_.get("coverage") or "") + " " + (p_.get("title_public") or "")).lower() for c in pm["coverage_contains"])
        if pm and seg_ok and cov_ok: hit.append(p_["name"])
    print(t["id"], len(hit), hit)
