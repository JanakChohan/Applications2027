# WS8.4 + WS1B: The "centre" of Investec UK and what the job postings show about its structure

Prepared for: Investec UK Summer Internship 2027 (req 14049), London, 30 Gresham Street. Department "People & Organisation", Division "IBP Business Enablement".
Research date: 2026-10-05. Source IDs: S260–S299, S340–S349.
Tags: [Confirmed] = read directly in a primary or fetched source. [Reported] = from a secondary source or search snippet. [Inferred] = my own deduction from the evidence.

---

## 1. Findings

### 1.1 How the jobs data was collected
- careers.investec.co.uk runs on the eArcu ATS. The search/results pages (`/jobs/vacancy/find/results/`) sit behind an AWS WAF JavaScript challenge, which returned HTTP 202 with an empty body (S276). Three other routes were open. The home page lists counts by category (S260). A public RSS feed at `/jobs/rss` returned 52 items, each with Department and Role Category (S261). `/jobs/sitemap.xml` lists 51 vacancy URLs (S262). Every individual vacancy page can be fetched, and each gives Location, Department, Division and Employment Type (S277). [Confirmed]
- The RSS and sitemap together gave 55 URLs. Two of them (Data Analyst 13313 and IPAM Engineer 13716, both Mumbai) are closed stubs with no fields. Two more URLs point to the same req 14115, which was renamed from "Head of Corporate Banking Technology" to "Head of Transactional Banking Technology". That leaves **52 live, unique vacancies**, which matches the RSS count. [Confirmed]
- The category tiles on the home page add up to 59 vacancies (Business Enablement 19, Technology & Digital 10, Compliance/Risk/Legal 9, CIB 8, Private Bank 4, Admin & Support 3, Change & Ops 3, HR & Marketing 2, Early Careers 1). This "Careersite Category" taxonomy is separate from the Role Category and Division fields. It probably counts some roles twice, or includes roles that are not in the feed. [Inferred]
- Aggregator snippets (Glassdoor Jobs, Indeed, Jooble) gave "22 open jobs overall across the UK… 9 in London". They also named roles that are **not** in the careers feed, such as "Organisation Development Consultant", "Employment Lawyer" and "Investment Banking Analyst/Associate – ECM and Corporate Broking". These may be closed, agency-posted, or posted only on LinkedIn. [Reported] (S342)

### 1.2 What the postings show about structure
1. **Postings use two different meanings of "Business Enablement".** [Confirmed]
   - **Role Category = "Business Enablement"** (plus "Offshore – Business Enablement" and "Operations") covers any non-client-facing role, wherever it sits. For example, a Corporate Banking "Proposition lead" and a Risk(IBP) "Operational Risk Manager" both carry it. 38 of the 52 live roles (73%) have a non-client-facing Role Category. 14 (27%) are "Client Facing – Revenue Generating" or "Non Revenue Generating".
   - **Division = "IBP Business Enablement"** is a narrower organisational unit. Its current postings come from these departments: People & Organisation (Summer Internship 14049, Senior Reward Manager), Company Secretarial(IBP), Operations(IBP) (Lending Operations / Credit Agency deal managers), Finance & Tax (Finance Business Partner, Mumbai), Enterprise & Shared Platforms (Marketing Transformation), the Credit Hub (Mumbai, IGSI), and Fund Solutions(IBP) credit support.
   - **Technology and Risk are posted as separate divisions:** "IBP Digital and Technology" and "IBP Risk & Compliance". Risk(IBP) and Compliance(IBP) roles fall under IBP Risk & Compliance. Technology is split into business-aligned departments (Corporate Banking Technology, Private Bank Technology) and offshore squads ("UK Offshore Tech: CBT", "UK Offshore Tech: SPT (Shared Platform Technology)"). [Confirmed]
   - So IBP Business Enablement looks like the IBP "COO/Finance/P&O/governance" family. Technology and the second-line Risk/Compliance functions sit beside it as their own divisions. [Inferred]
2. **"IBP" = Investec Bank plc.** The IBP 2026 Annual Financial Statements say: "Investec Bank plc (IBP) is the main banking subsidiary of Investec plc." Postings use "(IBP)" as a suffix on department names, e.g. Risk(IBP), Operations(IBP), Compliance(IBP), Company Secretarial(IBP). [Confirmed] (S278, S277)
3. **Other entity prefixes in the postings:**
   - IBCI = Investec Bank (Channel Islands) Limited, Guernsey. [Confirmed] (S275)
   - IGSI = Investec Global Services (India). [Confirmed as an acronym in the Credit Hub posting, "based in India (IGSI)"; full legal name from registry snippets, Reported] (S268, S341)
   - IBL = Investec Bank Limited (South Africa). [Inferred from "IBL Group" / "IBL Marketing"]
   - IBSAG = Investec Bank (Switzerland) AG. [Inferred]
4. **Mumbai (IGSI) is a large part of the centre.** 15 of 52 live roles (29%) are in Mumbai, and all but one of those are non-client-facing:
   - risk modelling, stress testing and model validation
   - payments and account-maintenance operations
   - engineering for Corporate Banking Technology and Shared Platform Technology
   - finance business partnering
   - a 25-FTE Credit Hub described as "Investec's credit centre of excellence".

   This is a hub-and-spoke model: London owns and leads, Mumbai delivers at scale. [Confirmed from postings; model label Inferred]
5. **Both embedded and central functions exist.** [Confirmed from postings; pattern Inferred]
   - Some functions sit inside the businesses. Examples are Corporate Banking Technology and Private Bank Technology, a first-line Operational Risk role in the Corporate Bank that reports to its COO, and Operations(IBP) roles listed under the IBP Corporate Banking division.
   - Other functions are central and serve the whole bank: Reward, Company Secretarial, Shared Platform Technology, Enterprise & Shared Platforms, and the Credit Hub.
   - The Head of Transactional Banking Technology posting describes the split clearly: a business-aligned squad that builds features "on the core banking platform only, while relying on specialist enterprise platforms and teams for payments processing, cards, digital channels, onboarding and other client enablement capabilities."
6. **Most current central hiring supports the new UK Corporate (mid-market) Bank.** Of the London tech roles, four are tied to the Corporate Bank (Head of Transactional Banking Technology, Head of Channel Technology, two Technical Product Owners). A fifth is the Mumbai Head of Transactional Banking Technology. The Credit Hub Lead posting says Investec is "establishing a new Corporate Bank, launching in 2026", targeting "circa 1,000 clients over circa five years". City AM (Nov 2025) quotes Andy Hart, Head of Corporate Banking (IBP), on bringing "a private client banking experience to UK mid-market corporates", with a target of 1,000 mid-market clients by 2030. [Confirmed postings; City AM Reported]
7. **No openings in the UK regions.** Live roles are in London (23), Reading (2, both IBP Corporate Banking: Asset Finance and Private Companies), Guernsey (8), Dublin (1), Mumbai (15), New York (2) and Zurich (1). There are **zero** in Manchester, Birmingham, Leeds, Bristol, Glasgow, Edinburgh or Jersey. [Confirmed for this snapshot] Most of Investec's former UK regional branch network belonged to Investec Wealth & Investment, which combined with Rathbones in 2023. The investec.com "our offices" wealth pages now redirect to Rathbones. [Reported] (S345)
8. **Hybrid working policy, as stated in postings:** "our working week is 4 days in the office and one day remote". This appears in about 43 of 52 postings. [Confirmed]

### 1.3 Governance and executive organisation (Investec Bank plc)
- **IBP Board as at 12 June 2026** (IBP AFS 2026, Corporate information and director biographies) [Confirmed] (S278):
  - Executive Directors: Ruth Leas (IBP CEO); Kevin McKenna (IBP CRO); Fani Titi (Group CE); Marlé van der Walt (IBP Finance Director, "with overarching responsibility for Finance (including Capital) and Operations").
  - Non-Executive Directors: Vivek Ahuja (Chair since 20 March 2026; he succeeded John Reizenstein, who stepped down on 29 January 2026); Henrietta Baldock; David Germain (a former Group CIO at QBE and a technology and operations specialist); Paul Seward (former HSBC UK CRO); Lesley Watkins.
  - Company Secretary: David Miller.
  - Companies House shows the same 10 active directors, plus the secretary (S279).
- **Group leadership:** Henrietta Baldock "will be appointed Chair of Investec Group with effect from 6 August 2026, succeeding Philip Hourquebie". [Confirmed in IBP AFS 2026] Fani Titi is Group CE. Nishlan Samujh is Group Finance Director (Investec plc AFS 2025 directorate). [Confirmed] Mark Currie is Group CRO and Marc Kahn is Chief Strategy and Sustainability Officer (Investec plc AFS 2025). [Confirmed as of 2025]
- **Structure:**
  - **DLC structure.** Investec plc (LSE) holds the non-Southern African businesses and Investec Limited (JSE) the Southern African ones. Investec operates "as if it is a single unified economic enterprise". [Confirmed]
  - **Risk governance.** It "operates within an integrated but geographical and divisional structure". There are "specialist divisions in the UK and smaller risk divisions in other regions". The IBP Board and its committees report into the Group (DLC) Board committees, linked through cross-membership of the committee chairs. [Confirmed] (S281)
  - **Group committees.** The DLC Remuneration Committee, DLC Nomdac, DLC BRCC, DLC SEC, DLC Audit and DLC IT Risk & Governance committees serve the whole group. The IBP Board has its own BRCC, Nomination, Remuneration and Audit committees. [Confirmed]
  - **Implication for the centre.** Several central functions, including Reward and Company Secretarial, work at both levels. The Senior Reward Manager supports "several Remuneration Committees in partnership with the Global Head of Reward" and prepares proposals for "the Investec Group Remuneration Committee". The Company Secretarial team "supports the governance framework for the Investec Group, including Investec Bank plc". [Confirmed] (S264, S265)
- **UK executive committee membership** (beyond board executives) was **not** retrievable. investec.com is behind a Cloudflare challenge (S343). See Gaps.

### 1.4 Size of the centre
- **IBP headcount at 31 March 2026: 2,425.** This is 2,367 permanent plus 58 temporary, against 2,374 a year earlier. The split is 61.1% male, 36.5% female, 2.4% not reported. Average permanent employees were 2,365 (FY2025: 2,331), per note 7. The S1 table gives 2,362 for the same figure, a small internal inconsistency. [Confirmed] (S278)
- **IBP staff costs were £411.8m in FY2026** (FY2025: £419.1m). That is roughly £174k per average permanent employee, fully loaded. [Confirmed figures; per-head Inferred] Most staff costs (£388.2m) fall in the "Corporate, Investment Banking and Other" segment, so central-function costs are allocated into segments and not disclosed separately. [Confirmed table; interpretation Inferred]
- **Investec plc FY2025 SECR intensity ratios** imply about 1,970–1,985 people in "UK and offshore" (Channel Islands/IoM) and about 2,330–2,350 in total. This is consistent with the IBP figure. [Inferred from S281: 734 tCO2e ÷ 0.37 per head etc.]
- **Investec Group:** "currently has 8,000+ employees" (FY2026 results, 21 May 2026). [Confirmed] (S282) Wikipedia gives 7,400 (2026) [Reported] (S297). Revelio Labs models about 7,000, of which 26% are UK and 6.6% India [Reported, modelled data] (S340).
- **Front office vs support split:** **not disclosed** in the IBP AFS 2026 or the Investec plc AFS 2025. The only proxy is the open-roles mix (73% non-client-facing), which is a flow measure, not a stock. [Inferred]
- **Cost pressure:** In FY2026, "Fixed operating costs grew 9.4% driven by higher headcount to support our strategic growth initiatives and enhance business resilience". The UK & Other cost-to-income ratio was 54.0% (FY2025: 53.5%). [Confirmed] (S282)
- **Peer comparison:** Close Brothers has about 3,000 employees (Wikipedia, 2026) [Reported] (S299). This makes IBP (about 2.4k) a mid-sized specialist bank, much smaller than the high-street banks. A like-for-like front/back split for peers was not found.

### 1.5 People & Organisation (P&O)
- Investec calls HR **"People & Organisation" (P&O)**. Postings also use "People and Organisation Leads" and "People Consultants", which suggests HR business partners embedded with business leaders. [Confirmed terms; model Inferred] (S264)
- **Leaders:**
  - UK: "Jason Spivey has joined Investec as Head of People and Organisation for the UK" (Feb 2026; previously Group CHRO at UBP). [Reported, from search snippet only; the HRToday page returned 403] (S290)
  - Global: Lesley-Anne Gatter (previously Head of P&O, South Africa) replaced Marc Kahn as Global Head of P&O on the Group Executive Team. [Reported via search snippet of an Investec press release; date not seen] (S291)
  - Also a "Global Head of Reward" (named only by title). [Confirmed role]
- **EVP and culture as stated in the IBP AFS 2026** [Confirmed] (S278):
  - "Our employee value proposition positions our culture at the core of the organisation."
  - The culture is "defined by material ownership, freedom to operate with accountability and open and honest dialogue."
  - FY2026 actions: UK paid paternity leave rose from 2 to 16 weeks; two new UK diversity networks were launched (Working Parents, Ability); Investec was "Featured in the Financial Times Best Employers 2026 list"; a designated NED represents the workforce on the board.
  - Targets: 35% women in senior leadership by 2027 (Women in Finance Charter), with 40% achieved; 40% female representation on the board, with 44% achieved; a female CEO and a female Finance Director.
- **Early careers:**
  - The 2027 Summer Internship is an "eight-week programme", "open to any degree subject", for penultimate and final-year students. Interns are placed "within our Specialist Bank" after an "HR interview".
  - The posting's "About you" includes "Be you – bring your whole self to work."
  - Applications opened "09:00am on 5th October for 24 hours (subject to volume of applications)".
  - [All Confirmed] (S263)
  - The investec.com graduates page states that Investec "has paused its rotational graduate programmes in the UK while redefining its early career offerings". [Reported, snippet] (S294)
- **Social mobility:**
  - Investec supports the 10,000 Black Interns and 10,000 Able Interns programmes [Reported, snippet] (S294).
  - Its education programmes work with Morpeth School and Arrival Education, and it runs "Invest for Success" for London and Liverpool students [Reported, VERCIDA] (S293).
- **Sponsorships:**
  - Investec is title partner of the Investec Champions Cup (European rugby) under a five-year deal announced on 31 August 2023, replacing Heineken (sponsor since 1995). Ruth Leas: "This is a very significant partnership for our business." [Confirmed City AM] (S285)
  - Cricket: Investec was England's home Test sponsor under a 10-year deal (about £5m a year) agreed in November 2011. It ended early, and Specsavers took over from the 2018 India series. [Reported, snippet] Wikipedia gives 2011–2017. [Reported] (S298, S297)
  - England Rugby is **not** a current Investec sponsorship. Wikipedia lists past rugby ties and the Epsom Derby (2009–2020). [Reported]
- **Glassdoor:** 4.2/5 from 887 reviews; 87% would recommend; culture and values 4.4; career opportunities 3.8; London 4.1 from 279 reviews. [Reported, search snippet; Glassdoor returned 403] (S292)

### 1.6 Offices and 30 Gresham Street
- **HQ:** 30 Gresham Street, London EC2V 7QP is the registered office of both Investec plc and IBP [Confirmed] (S278, S281). The internship posting gives EC2V 7QN [Confirmed] (S263).
- **The building:** 386,000 sq ft, developed by Land Securities in 2002–03 on the former Blossom's Inn site. Occupants are Commerzbank, Investec and Rathbones. [Reported, Wikipedia] (S288)
- **Lease:** In August 2025 Investec Bank plc and Rathbones Group plc completed "a long-term lease regear" covering "in excess of 350,000 sq. ft. NIA", creating a shared London HQ with "significant renovation works" to follow [Confirmed, Macfarlanes] (S287). A search snippet says Investec signed reversionary leases to September 2038 on 150,000 sq ft [Reported, snippet] (S289).
- **Other footprint (IBP AFS 2026)** [Confirmed] (S278, S281):
  - IBP operates in the UK, Channel Islands, Ireland (Treasury Risk Solutions and Institutional Equities), Continental Europe and the USA.
  - The Reading International Business Park registered office houses the asset finance and leasing subsidiaries.
  - Guernsey hosts Investec Bank (Channel Islands) Ltd. Mumbai hosts IGSI. Dublin hosts the Irish entities.
- **Manchester:** a 2008 article shows the Private Bank had a Manchester treasury team serving the North [Confirmed, but dated] (S347). Current bank-only regional offices could not be confirmed.

---

## 2. Key numbers table

| Metric | Value | Date | Tag | Source |
|---|---|---|---|---|
| Live Investec UK-site vacancies (unique) | 52 | 2026-10-05 | Confirmed | S261, S277 |
| Home-page category tile total | 59 (BE 19; Tech 10; CRL 9; CIB 8; PB 4; Admin 3; Change & Ops 3; HR & Mktg 2; Early Careers 1) | 2026-10-05 | Confirmed | S260 |
| Non-client-facing share of live roles (Role Category BE / Offshore-BE / Operations) | 38 / 52 = 73% | 2026-10-05 | Confirmed count | S261 |
| Roles in Division "IBP Business Enablement" | 9 (6 London, 3 Mumbai) | 2026-10-05 | Confirmed | S277 |
| Mumbai share of live roles | 15 / 52 = 29% | 2026-10-05 | Confirmed | S277 |
| IBP employees (total / permanent / temp) | 2,425 / 2,367 / 58 | 31 Mar 2026 | Confirmed | S278 |
| IBP employees prior year | 2,374 | 31 Mar 2025 | Confirmed | S278 |
| IBP average permanent employees | 2,365 (note 7) / 2,362 (S1 table) | FY2026 | Confirmed | S278 |
| IBP gender split | 61.1% M / 36.5% F / 2.4% not reported | 31 Mar 2026 | Confirmed | S278 |
| IBP staff costs | £411.8m (FY25 £419.1m) | FY2026 | Confirmed | S278 |
| IBP total operating costs | £607.3m (FY25 £597.7m) | FY2026 | Confirmed | S278 |
| Staff cost per average permanent employee | ~£174k | FY2026 | Inferred | S278 |
| Women in senior leadership (target 35% by 2027) | 40% | FY2026 | Confirmed | S278 |
| Women on IBP Board | 44% | FY2026 | Confirmed | S278 |
| UK paid paternity leave | 2 → 16 weeks | FY2026 | Confirmed | S278 |
| Investec Group employees | "8,000+" | 21 May 2026 | Confirmed | S282 |
| Group employees (alt.) | 7,400 (Wikipedia); ~7,000 (Revelio, 26% UK) | 2026 / Dec 2025 | Reported | S297, S340 |
| UK & Other cost-to-income | 54.0% (FY25 53.5%) | FY2026 | Confirmed | S282 |
| Group fixed opex growth | +9.4%, "driven by higher headcount" | FY2026 | Confirmed | S282 |
| Investec plc implied headcount (SECR) | ~1,980 UK & offshore; ~2,340 total | FY2025 | Inferred | S281 |
| Credit Hub team size | "circa 25 FTE" | 2026 | Confirmed | S268 |
| UK Corporate Bank target | ~1,000 clients over ~5 years / by 2030 | 2025–26 | Confirmed (posting) / Reported (City AM) | S268, S286 |
| 30 Gresham Street size | 386,000 sq ft; regear >350,000 sq ft NIA (Aug 2025) | 2025 | Reported / Confirmed | S288, S287 |
| Glassdoor | 4.2/5 (887 reviews), 87% recommend | snippet, undated | Reported | S292 |
| Close Brothers employees (peer) | ~3,000 | 2026 | Reported | S299 |

### 2a. Open roles by Division (as posted) × city
Method: the RSS feed (`/jobs/rss`) and the sitemap were merged, and each vacancy page was fetched with curl on 2026-10-05 (about 10:50 UTC). The Location and Division fields were parsed. Closed stubs (2) and the duplicate renamed req (1) were removed. n = 52.

| Division (as posted) | London (30 Gresham St) | Reading | Guernsey | Dublin | Mumbai | New York | Zurich | Total |
|---|---|---|---|---|---|---|---|---|
| IBP Business Enablement | 6 | 0 | 0 | 0 | 3 | 0 | 0 | 9 |
| IBP Corporate Banking | 3 | 2 | 0 | 0 | 3 | 0 | 0 | 8 |
| Guernsey (IBCI) | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 8 |
| IBP Digital and Technology | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 7 |
| IBP Risk & Compliance | 1 | 0 | 0 | 0 | 3 | 1 | 0 | 5 |
| Corporate and Investment Banking | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| IBP Bank Funding Group | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| IBP Private Client | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| IBP Funds | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| IBP Private Equity Group | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Ireland | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| Investec India | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Aviation | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Corporate Banking Technology | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| IBSAG Switzerland | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| **Total** | **23** | **2** | **8** | **1** | **15** | **2** | **1** | **52** |

Manchester, Birmingham, Leeds, Bristol, Glasgow, Edinburgh and Jersey all had **0** live roles at the snapshot.

### 2b. Open roles by Role Category × city (same method)
| Role Category (RSS) | London | Reading | Guernsey | Dublin | Mumbai | New York | Zurich | Total |
|---|---|---|---|---|---|---|---|---|
| Business Enablement | 13 | 0 | 5 | 1 | 9 | 1 | 0 | 29 |
| Offshore – Business Enablement | 0 | 0 | 1 | 0 | 4 | 0 | 0 | 5 |
| Operations | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 4 |
| Client Facing – Revenue Generating | 6 | 1 | 1 | 0 | 0 | 0 | 1 | 9 |
| Client Facing – Non Revenue Generating | 2 | 1 | 1 | 0 | 0 | 1 | 0 | 5 |

### 2c. Department-level detail for the "centre" (IBP Business Enablement division + adjacent central units)
| Role (req) | City | Department | Division |
|---|---|---|---|
| Summer Internship 2027 (14049) | London | People & Organisation | IBP Business Enablement |
| Senior Reward Manager (13645) | London | People and Organisation | IBP Business Enablement |
| Assistant Company Secretary (13933) | London | Company Secretarial(IBP) | IBP Business Enablement |
| Marketing Transformation Lead (14077) | London | Enterprise & Shared Platforms | IBP Business Enablement |
| Deal Manager (14084) | London | Operations(IBP) | IBP Business Enablement |
| Deal Manager – Credit Agency (14023) | London | Operations(IBP) | IBP Business Enablement |
| Finance Business Partner (13925) | Mumbai | Finance & Tax | IBP Business Enablement |
| Credit Hub Lead (13691) | Mumbai | Business Enablement | IBP Business Enablement |
| Credit Analyst (13553) | Mumbai | Fund Solutions(IBP) | IBP Business Enablement |
| Operational Risk Manager (13783) | London | Risk(IBP) | IBP Risk & Compliance |
| Model Validation / IRB Credit Modeller / Stress Testing Quant (12271, 12586, 13954) | Mumbai | Risk(IBP) | IBP Risk & Compliance |
| Senior Compliance Officer (13578) | New York | Compliance(IBP) | IBP Risk & Compliance |
| Payments Analyst / Account Maintenance Analyst (13445, 13446) | Mumbai | Operations(IBP) | IBP Corporate Banking |
| Quality Engineer (13767) | Mumbai | UK Offshore Tech: SPT (Shared Platform Technology) | IBP Digital and Technology |
| Travel desk (13502) | Mumbai | Corporate Services and Workspace | Investec India |
| Head of Workplace Experience and Facilities (13076) | Guernsey | IBCI Group Resources | Guernsey |

---

## 3. Verbatim quotes actually read

Postings (careers.investec.co.uk, fetched 2026-10-05):
1. Summer Internship 2027 (14049), S263: "Location: London - 30 Gresham Street … Department: People & Organisation … Division: IBP Business Enablement". Also: "Successful applicants will become part of a team within our Specialist Bank (we will discuss the best aligned team for you during your HR interview from the range of business areas hosting an Internship position)." And: "Although embedded into one team we aim to provide you with a clear overview of our entire business." And: "Be you – bring your whole self to work."
2. Senior Reward Manager (13645), S264: "The team partners closely with senior business leaders, People & Organisation colleagues, Finance and governance forums to provide expert, commercially grounded advice on remuneration…" And: "Coordinate communication with People and Organisation Leads, People Consultants and business leaders…" And: "Co-ordinate the EVA bonus pool and Long-Term Share Awards overall pool determination and divisional or team allocation, working closely with the CEO and CFO."
3. Assistant Company Secretary (13933), S265: "At Investec, Company Secretariat is not simply an administrative function." And: "…supports the governance framework for the Investec Group, including Investec Bank plc, its Board, Board Committees, management forums and principal subsidiaries."
4. Marketing Transformation Lead (14077), S266: "Marketing Operations is responsible for the operating model and infrastructure that enable the IBP Marketing department to deliver effectively. The team works across Marketing, Technology, Risk, Compliance and Operations, with strong links to IBL Marketing and offshore delivery hubs." And: "Build trusted relationships across IBL Group, UK Marketing, Operations, Technology and the offshore hub…"
5. Finance Business Partner (13925), S267: "…building strong relationships across the leadership within the Support Division."
6. Credit Hub Lead (13691), S268: "The Credit Hub is Investec's credit centre of excellence, based in India (IGSI), providing independent credit support to Private Markets, Private Clients, TRS and Credit across the Group." And: "Investec is also establishing a new Corporate Bank, launching in 2026, which the Hub will support." And: "…leading, coaching and developing a team of circa 25 FTE across multiple desks."
7. Deal Manager (14084), S269: "Acting as a key partner to the lending businesses, you will be the primary point of contact for Global Lending Operations activity. You will work closely with Relationship Managers and stakeholders across Treasury, Client Services, Legal Risk, Group Risk, Financial Control, Settlements, Credit Services, and Financial Crime and Fraud."
8. Head of Transactional Banking Technology (13815/14115), S270: "At Investec, we are building a differentiated Corporate Banking proposition in the UK, and transactional banking sits right at the heart of it." And (14115): "It will own the delivery of transactional banking features on the core banking platform only, while relying on specialist enterprise platforms and teams for payments processing, cards, digital channels, onboarding and other client enablement capabilities." And: "Act as the senior technology partner to Transactional Banking and Corporate Banking leaders…"
9. First-Line Operational Risk (14015), S271: "Reporting to the Chief Operating Officer, this role will partner closely with business and functional leaders to strengthen the operational risk and control environment across our corporate banking activities."
10. Funding Associate (13988), S272: "The Bank Funding Group is responsible for raising, managing and optimising the funding required to support Investec Bank plc's balance sheet and lending activities."
11. Model Validation Specialist (12271), S273: "Model Risk & Validation is responsible for the independent review and challenge of the models used within Investec Bank plc…"
12. Credit Analyst, Fund Solutions (13553), S274: "The Fund Solutions team within the IGSI Credit Hub supports the wider Fund Solutions franchise of Investec Bank Plc, working in close partnership with the London and New York teams."
13. IBCI Technical Business Analyst (13805), S275: "We are the Digital and Technology team at Investec Bank (Channel Islands) Limited—a dynamic and diverse group of analysts and engineers who thrive on variety and close collaboration with our business partners."
14. Older posting boilerplate, S277: "We combine a flat structure with a focus on internal mobility." Newer boilerplate: "At Investec, we do things differently. We're a leading international bank and wealth manager built on a culture of curiosity, entrepreneurial spirit and human connection."
15. Postings, S277: "As part of our collaborative & agile culture, our working week is 4 days in the office and one day remote."
16. Careers home page, S260: "Our culture is what sets us apart … We work in a collaborative environment and offer freedom and flexibility, as well as opportunities for growth."

Annual reports and filings:
17. IBP AFS 2026, p8, S278: "Investec Bank plc (IBP) is the main banking subsidiary of Investec plc."
18. IBP AFS 2026, p65, S278: Marlé van der Walt "was appointed as Finance Director in September 2022 with overarching responsibility for Finance (including Capital) and Operations."
19. IBP AFS 2026, p324, S278: "Our employee value proposition positions our culture at the core of the organisation." And: "…our culture is defined by material ownership, freedom to operate with accountability and open and honest dialogue."
20. IBP AFS 2026, p18, S278: "Increased our paid paternity leave entitlement in the UK from two weeks to a total of 16 weeks paid leave". And: "Featured in the Financial Times Best Employers 2026 list". And: "Board-level representation of workforce perspectives through a designated Non-Executive Director".
21. IBP AFS 2026, p62, S278: "Following receipt of regulatory approval, I assumed the role of Chair on 20 March 2026." (Vivek Ahuja)
22. Investec plc AFS 2025, S281: "Group risk management operates within an integrated but geographical and divisional structure…" And: "The Board and Board committees of IBP report to the Board and the Board committees of the Group…"
23. FY2026 results, S282: "The Group was established in 1974 and currently has 8,000+ employees." And: "Fixed operating costs grew 9.4% driven by higher headcount to support our strategic growth initiatives and enhance business resilience, as well as annual salary increases."

Press:
24. City AM, 31 Aug 2023, S285 (Ruth Leas): "This is a very significant partnership for our business. It is one of the world's biggest rugby competitions."
25. City AM, Nov 2025, S286 (Andy Hart, Head of Corporate Banking, IBP): "We see a clear strategic growth opportunity to extend our offering and bring a private client banking experience to UK mid-market corporates."
26. Macfarlanes, 20 Aug 2025, S287: "…in excess of 350,000 sq. ft. NIA of office space"; "The building will now undergo significant renovation works…"

---

## 4. Source table

| ID | Outlet | Title | Pub date | URL | Accessed | Status | Confidence note |
|---|---|---|---|---|---|---|---|
| [S260] | Investec Careers (eArcu) | Working at Investec: a different kind of opportunity (home, category counts) | live | https://careers.investec.co.uk/jobs/home/ | Accessed 2026-10-05 | FETCHED | High. Category taxonomy differs from feed |
| [S261] | Investec Careers | Current vacancies (RSS, 52 items) | live | https://careers.investec.co.uk/jobs/rss | Accessed 2026-10-05 | FETCHED | High. Primary dataset |
| [S262] | Investec Careers | sitemap.xml (51 vacancy URLs) | live | https://careers.investec.co.uk/jobs/sitemap.xml | Accessed 2026-10-05 | FETCHED | High |
| [S263] | Investec Careers | Summer Internship 2027 (14049) | live | https://careers.investec.co.uk/jobs/vacancy/summer-internship-2027-14049-london---30-gresham-street/14067/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S264] | Investec Careers | Senior Reward Manager (13645) | live | https://careers.investec.co.uk/jobs/vacancy/senior-reward-manager-13645-london---30-gresham-street/13663/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S265] | Investec Careers | Assistant Company Secretary (13933) | live | https://careers.investec.co.uk/jobs/vacancy/assistant-company-secretary-13933-london---30-gresham-street/13951/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S266] | Investec Careers | Marketing Transformation Lead (14077) | live | https://careers.investec.co.uk/jobs/vacancy/marketing-transformation-lead-14077-london---30-gresham-street/14095/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S267] | Investec Careers | Finance Business Partner (13925) | live | https://careers.investec.co.uk/jobs/vacancy/finance-business-partner-13925-mumbai/13943/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S268] | Investec Careers | Credit Hub Lead (13691) | live | https://careers.investec.co.uk/jobs/vacancy/credit-hub-lead-13691-mumbai/13709/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S269] | Investec Careers | Deal Manager (14084) | live | https://careers.investec.co.uk/jobs/vacancy/deal-manager-14084-london---30-gresham-street/14102/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S270] | Investec Careers | Head of Transactional Banking Technology (Corporate Banking) (13815) and (14115) | live | https://careers.investec.co.uk/jobs/vacancy/head-of-transactional-banking-technology-corporate-banking-13815-london---30-gresham-street/13833/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S271] | Investec Careers | First-Line Operational Risk, Controls & Resilience (14015) | live | https://careers.investec.co.uk/jobs/vacancy/first-line-operational-risk-controls--resilience--14015-london---30-gresham-street/14033/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S272] | Investec Careers | Funding Associate (13988) | live | https://careers.investec.co.uk/jobs/vacancy/funding-associate-13988-london---30-gresham-street/14006/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S273] | Investec Careers | Model Validation Specialist (12271) | live | https://careers.investec.co.uk/jobs/vacancy/model-validation-specialist-12271-mumbai/12289/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S274] | Investec Careers | Credit Analyst, Fund Solutions (13553) | live | https://careers.investec.co.uk/jobs/vacancy/credit-analyst-13553-mumbai/13571/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S275] | Investec Careers | Technical Business Analyst, IBCI (13805) | live | https://careers.investec.co.uk/jobs/vacancy/technical-business-analyst-13805-guernsey/13823/description/ | Accessed 2026-10-05 | FETCHED | High |
| [S276] | Investec Careers | Job search results page | live | https://careers.investec.co.uk/jobs/vacancy/find/results/ | Accessed 2026-10-05 | BLOCKED (AWS WAF challenge, HTTP 202) | n/a |
| [S277] | Investec Careers | All 52 live vacancy detail pages (bulk crawl via RSS + sitemap URLs) | live | https://careers.investec.co.uk/jobs/vacancy/… | Accessed 2026-10-05 | FETCHED | High. Snapshot at ~10:50 UTC |
| [S278] | Investec Bank plc via Companies House | Investec Bank plc Annual Financial Statements 2026 (AA filing, 361pp; pp 4, 6, 8, 17–18, 62–66, 152, 324–325, 359 read as rendered images) | filed 12 Jul 2026 (dated 12 Jun 2026) | https://find-and-update.company-information.service.gov.uk/company/00489604/filing-history/MzUzMDk3ODM1OWFkaXF6a2N4/document?format=pdf&download=0 | Accessed 2026-10-05 | FETCHED | Very high. Primary statutory filing |
| [S279] | Companies House | INVESTEC BANK PLC officers | live | https://find-and-update.company-information.service.gov.uk/company/00489604/officers | Accessed 2026-10-05 | FETCHED | Very high |
| [S280] | Companies House | INVESTEC BANK PLC filing history (accounts) | live | https://find-and-update.company-information.service.gov.uk/company/00489604/filing-history | Accessed 2026-10-05 | FETCHED | Very high. Shows Reizenstein TM01 29 Jan 2026 |
| [S281] | Investec plc via financialreports.eu | Investec Annual Report 2025, Investec plc silo annual financial statements | Jul 2025 | https://cdn.financialreports.eu/financialreports/media/filings/5231/2025/RNS/5231_rns_2025-07-07_0a25ff56-e486-4971-a197-67f8cb22f9b4.pdf | Accessed 2026-10-05 | FETCHED | High. Prior-year governance |
| [S282] | Investegate (RNS) | Investec: Final Results 31/03/2026 | 21 May 2026 | https://www.investegate.co.uk/announcement/rns/investec--invp/final-results-31-03-2026/9578809 | Accessed 2026-10-05 | FETCHED | High (via summariser) |
| [S283] | Investegate (RNS) | Investec: Half-year Financial Report 30 Sep 2025 | Nov 2025 | https://www.investegate.co.uk/announcement/rns/investec--invp/half-year-financial-report-30-sep-2025/9245448 | Accessed 2026-10-05 | FETCHED | High. "approximately 8,000 employees"; UK C:I 53.3% |
| [S284] | Investegate (RNS) | Investec Bank plc: Annual Financial Report | 23 Jun 2026 | https://www.investegate.co.uk/announcement/rns/investec-bank-plc--im88/annual-financial-report/9632763 | Accessed 2026-10-05 | FETCHED | High. Company Secretary David Miller |
| [S285] | City AM | Investec hands rugby vote of confidence with Champions Cup sponsorship | 31 Aug 2023 | https://www.cityam.com/investec-hand-rugby-vote-of-confidence-with-champions-cup-sponsorship/ | Accessed 2026-10-05 | FETCHED | High |
| [S286] | City AM | Investec looks to mid-market businesses in growth push | 20 Nov 2025 | https://www.cityam.com/investec-looks-to-mid-market-businesses-in-growth-push/ | Accessed 2026-10-05 | FETCHED | Medium-high |
| [S287] | Macfarlanes | Macfarlanes advises Investec Bank PLC and Rathbones Group PLC on a long-term lease regear of 30 Gresham Street | 20 Aug 2025 | https://www.macfarlanes.com/what-we-think/102eli5/macfarlanes-advises-investec-bank-plc-and-rathbones-group-plc-on-a-long-term-lease-regear-of-30-gresham-street-london-102l0dw/ | Accessed 2026-10-05 | FETCHED | High |
| [S288] | Wikipedia | 30 Gresham Street | n/a | https://en.wikipedia.org/wiki/30_Gresham_Street | Accessed 2026-10-05 | FETCHED | Medium |
| [S289] | Property Week / CoStar (search result) | Landlords regear leases on 350,000 sq ft…; reversionary leases to Sept 2038 on 150,000 sq ft | 2025 | https://www.propertyweek.com/news/landlords-regear-leases-on-350000-sq-ft-of-city-offices-at-30-gresham-street | Accessed 2026-10-05 | SNIPPET | Medium-low. Exact outlet of the 2038 figure not verified |
| [S290] | HR Today (India) | Jason Spivey Joins Investec as Head of People and Organisation for the UK | ~Feb 2026 | https://hrtoday.in/jason-spivey-joins-investec-as-head-of-people-and-organisation-for-the-uk/ | Accessed 2026-10-05 | SNIPPET (403 on fetch) | Medium-low. Verify on LinkedIn before naming |
| [S291] | Investec press release | Investec boosts executive team in line with strategic journey (Lesley-Anne Gatter, Global Head of P&O) | date not seen | https://www.investec.com/en_us/welcome-to-investec/press/investec-boosts-executive-team-in-line-with-strategic-journey.html | Accessed 2026-10-05 | SNIPPET (Cloudflare 403) | Medium. Currency unknown |
| [S292] | Glassdoor UK | Investec Reviews | live | https://www.glassdoor.co.uk/Reviews/Investec-Reviews-E7373.htm | Accessed 2026-10-05 | SNIPPET (403) | Medium. Figures drift |
| [S293] | VERCIDA | Social Mobility Programmes at Investec | undated | https://www.vercida.com/uk/features/social-mobility-programmes-at-investec | Accessed 2026-10-05 | FETCHED | Medium. Undated |
| [S294] | Investec | UK graduate opportunities / FAQ | live | https://www.investec.com/en_gb/welcome-to-investec/Careers/graduates.html | Accessed 2026-10-05 | SNIPPET | Medium. Grad scheme "paused" |
| [S295] | CFO South Africa | Marlé van der Walt steps in as Investec Bank FD | 9 Apr 2021 | https://cfo.co.za/articles/marle-van-der-walt-steps-in-as-investec-bank-fd/ | Accessed 2026-10-05 | FETCHED | High (refers to IBL, SA) |
| [S296] | CFO South Africa | Marlé van der Walt appointed Specialist Bank CFO at Investec | 8 Mar 2019 | https://cfo.co.za/articles/marle-van-der-walt-appointed-specialist-bank-cfo-at-investec/ | Accessed 2026-10-05 | FETCHED | High (historical) |
| [S297] | Wikipedia | Investec | n/a | https://en.wikipedia.org/wiki/Investec | Accessed 2026-10-05 | FETCHED | Medium |
| [S298] | ESPNcricinfo / SportBusiness (search results) | Specsavers took over from Investec as England home Test sponsor; Investec 10-year deal from Nov 2011 | 2018–2020 | https://www.espncricinfo.com/story/specsavers-leave-door-open-after-confirming-end-to-ecb-sponsorship-1220433 | Accessed 2026-10-05 | SNIPPET (403) | Medium |
| [S299] | Wikipedia | Close Brothers Group | n/a | https://en.wikipedia.org/wiki/Close_Brothers_Group | Accessed 2026-10-05 | FETCHED | Medium. Peer headcount ~3,000 |
| [S340] | Revelio Labs | Investec Number of Employees 2026 | Dec 2025 data | https://www.reveliolabs.com/companies/investec/employees/ | Accessed 2026-10-05 | SNIPPET | Low-medium. Modelled data |
| [S341] | Tracxn / InstaFinancials (registry aggregators) | Investec Global Services (India) Pvt Ltd | 2025 | https://www.instafinancials.com/company/investec-global-services-india-privatelimited-U74999MH2020FTC350908 | Accessed 2026-10-05 | SNIPPET | Low. Incorporated 28 Nov 2020; "225 employees" figure unreliable |
| [S342] | Glassdoor Jobs / Indeed / Jooble | Investec jobs in London / UK | Sep–Oct 2026 | https://uk.jooble.org/jobs-investec/London | Accessed 2026-10-05 | SNIPPET | Low. "22 UK / 9 London"; extra roles not in feed |
| [S343] | Investec | Corporate Governance page | live | https://www.investec.com/en_gb/welcome-to-investec/about-us/corporate-governance.html | Accessed 2026-10-05 | BLOCKED (Cloudflare 403) | n/a |
| [S344] | Investec | Our People – Cultivating Out of the Ordinary | live | https://www.investec.com/en_gb/welcome-to-investec/sustainability/our-people.html | Accessed 2026-10-05 | BLOCKED (Cloudflare 403) | n/a |
| [S345] | Investec / Rathbones (search results) | Wealth "our offices" pages now Rathbones | live | https://www.investec.com/en_gb/wealth/our-offices.html | Accessed 2026-10-05 | SNIPPET | Medium |
| [S346] | MarketScreener (search result) | Investec Bank Limited governance (IBL exco: Cumesh Moodliar CEO, Stuart Spencer COO) | 2025 | https://www.marketscreener.com/quote/stock/INVESTEC-BANK-LIMITED-119080194/company-governance/ | Accessed 2026-10-05 | SNIPPET | Medium. SA entity only |
| [S347] | PAM Insight / TheWealthNet | Investec Private Bank expands Manchester office with two new appointments | 13 Aug 2008 | https://www.paminsight.com/twn/article/investec-private-bank-expands-manchester-office-with-two-new-appointments | Accessed 2026-10-05 | FETCHED | High but dated (2008) |

---

## 5. Gaps
- **UK executive committee (IBP Exco) membership** is not in the IBP AFS pages read, and investec.com (the leadership pages) is behind a Cloudflare challenge. Names of the UK COO, CTO/CIO, Head of Operations, General Counsel, Head of Compliance and Head of Marketing are therefore **not verified**. Only board executives are confirmed: CEO Ruth Leas, CRO Kevin McKenna, FD Marlé van der Walt (who also covers Operations), and Group CE Fani Titi.
- **The UK Head of P&O (Jason Spivey) and the Global Head of P&O (Lesley-Anne Gatter)** come from search snippets only. Check on LinkedIn or the Investec press page before naming them in interview. Use role titles if unsure.
- **Front-office vs support headcount split** is not disclosed. IBP gives only a total (2,425) and a gender split. The IBP Pillar 3 document was not fetched (investec.com blocked). Pillar 3 normally covers board directorships and the remuneration code staff count, not the functional split.
- **Search results page blocked** (WAF), so the counts rely on the RSS feed and sitemap. They may under-count roles posted only to LinkedIn or by agencies (S342 lists extra roles). The home-page tile total of 59 against 52 in the feed is unexplained.
- **The LinkedIn jobs page** was not fetched separately, because the session's web-search budget ran out. eFinancialCareers was not checked.
- **Current UK regional offices of the bank** (Manchester, Birmingham, Leeds, Bristol, Glasgow, Edinburgh) are not confirmed for 2026. The evidence only shows Reading (asset finance) and the Leeds registered office of an associate (CF Capital Holdings).
- **Peer comparison** is thin: only Close Brothers, about 3,000 (Wikipedia).
- **The 30 Gresham Street lease term to 2038 / 150k sq ft** is snippet-only.
- **The Glassdoor figures** are a snippet and undated.

---

## 6. Interview angles
1. **Know what your division is.** "IBP Business Enablement" is the Investec Bank plc unit that holds non-client-facing teams: P&O, Company Secretarial, Lending Operations, Finance & Tax, Marketing operations ("Enterprise & Shared Platforms") and the IGSI Credit Hub. Technology and Risk & Compliance are posted as their own IBP divisions. A sharp line to use: *"I noticed the internship sits in IBP Business Enablement under P&O. I'd love to understand how the internship teams are allocated across the Specialist Bank."* The posting says this is decided in the HR interview.
2. **The Corporate Bank build is where most of the action is.** About 5 of 52 open roles are Corporate Banking technology leadership. A Credit Hub posting says the new Corporate Bank is "launching in 2026" and aims for about 1,000 clients. Asking how central teams (Ops, Tech, Risk, P&O hiring) are scaling for it shows you have joined up the strategy and the org chart.
3. **The hub model: London owns, Mumbai delivers at scale.** 29% of open roles are in Mumbai (IGSI), including the "credit centre of excellence". A good question: "How do London teams work day-to-day with the IGSI hub?" It shows you understand modern bank operating models.
4. **Governance literacy.** IBP is "the main banking subsidiary of Investec plc", inside a DLC structure with Investec Limited. IBP has its own board, including a new Chair, Vivek Ahuja, since March 2026. Henrietta Baldock becomes Group Chair from August 2026. Mentioning Company Secretarial's line that it is "not simply an administrative function" lands well if you are placed in a governance team.
5. **P&O-specific hooks:**
   - FY2026 people actions: UK paternity leave raised to 16 weeks, Working Parents and Ability networks, FT Best Employers 2026, and a designated workforce NED.
   - The Women in Finance target of 35% by 2027 has already been beaten (40% achieved).
   - The internship's own "Be you – bring your whole self to work" line.
   - Ask how P&O measures the culture of "material ownership" and "freedom to operate with accountability".
6. **Culture vocabulary to reuse:**
   - "Out of the Ordinary"
   - "create enduring worth" (the purpose)
   - "entrepreneurial spirit", "flat/accessible structure with a focus on internal mobility"
   - the four-days-in-office "collaborative & agile culture".
7. **Cost-discipline awareness.** UK & Other cost-to-income was 54.0% in FY2026, and fixed costs grew 9.4% "driven by higher headcount". A thoughtful question for a Business Enablement intern: "How does the centre balance investment in the Corporate Bank with keeping the cost-to-income ratio in check?"
8. **Sponsorship small talk.** Investec Champions Cup (title partner since the 2023/24 season, five-year deal). Investec previously sponsored England home Tests (2011 to about 2017) and the Epsom Derby. Don't claim a current England Rugby sponsorship.
9. **Avoid pitfalls.** Investec Wealth & Investment UK is now part of Rathbones (Investec holds about 41%). The regional wealth offices are Rathbones', not the bank's. The UK rotational graduate scheme is reported as "paused", so ask about conversion routes from the internship carefully.
