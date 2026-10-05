# WS6 and WS7: Interview Intelligence and Interviewer Backgrounds

LSEG Business Management Summer Internship 2027, req R0123386, London (5 Canada Square). Research date 2026-10-05.

Tags: [Confirmed] = LSEG-owned page or official release, read in full. [Reported] = third party, test-prep vendor or forum; anecdotes are labelled ANECDOTE. [Inferred] = my reasoning from the evidence. Source IDs S260 to S299 (section 4).

Access notes: Glassdoor, TheStudentRoom, Reddit, Bright Network, Gradcracker and Tradeweb.com all returned HTTP 403 to both WebFetch and curl. Everything from those sites is search-result snippet only and is marked SNIPPET. The search tool's session budget ran out near the end, so a few planned searches (YouTube vlog titles, Bright Network salary, extra forum threads) were not run. See section 5.

---

## 1. Findings

### 1.1 The process: four stages, run the same way across business tracks

| Stage | What LSEG says | Confidence |
|---|---|---|
| 1. Application and CV | "The first stage of the recruitment process involves making an application and submitting your resume." Make one application only. If you make more than one, LSEG reviews only the first. | [Confirmed, S260] |
| 2. Immersive Online Assessment | "untimed Immersive Online Assessment. The assessment is designed to give you an insight into what it's like to work at LSEG." The hints page says it is "an interactive assessment designed to help us understand your strengths, potential and approach to solving real-world challenges", and points candidates to an "Assessment Preparation Hub". | [Confirmed, S260, S264] |
| 3. Video interview | "a video interview where you will answer a series of questions using a strength-based-interview style". Hints page: "we'll learn more about your experiences, motivations, strengths and what inspires you about a career at LSEG." | [Confirmed, S260, S264] |
| 4. Assessment centre | "a half day assessment centre which involves several different types of exercises - further information is provided at the point of invite." "all our assessment centres are held virtually." Hints page: "interactive activities, discussions and exercises ... a chance to get to know LSEG, meet our people". | [Confirmed, S260, S264] |
| 5. Offer | "If you're successful, you'll receive an offer to join LSEG". | [Confirmed, S264] |

The same four-stage wording appears in the FTSE Russell Business Graduate Programme and the Business Analyst Summer Internship postings, so this is a standard early careers process, not specific to this role. [Confirmed, S261, S262]

Rolling review: "Applications are reviewed on a first-come, first-served basis, so we strongly encourage you to complete all required assessments as early as possible." Assessment deadlines are given in the invitation email, and there is "no fixed timeframe" for results. [Confirmed, S266, S269]

### 1.2 Who runs the Immersive Online Assessment: strong evidence for Cappfinity

- LSEG's Business Programme hints page links the words "Assessment Preparation Hub" to `https://hub.preparationplus.com/dashboard/`. [Confirmed, S264, read in raw HTML]
- That hub page's HTML title is "Cappfinity Preparation Hub", its meta description is "Powered by Cappfinity", and its preview image is served from `apifiles.cappassessments.com`. [Confirmed, S265]
- Conclusion: LSEG's assessment partner for the immersive stage is very likely Cappfinity (formerly Capp). [Inferred, high confidence] LSEG does not name the vendor in text anywhere I read.
- Cappfinity's video interview product is described by Cappfinity as "fully asynchronous". [Confirmed for the product, S290] Whether LSEG uses Cappfinity for the video stage too is not stated. [Inferred, medium confidence, because the hub link sits on the same page as the video stage and Cappfinity sells both]

Conflicting claims, and why I give them less weight:
- GraduatesFirst (updated 21 Oct 2025) says "The LSEG assessment tests are provided by the test publisher SHL" and lists numerical, logical and verbal tests. [Reported, S286] PracticeAptitudeTests (updated 18 Nov 2025) says the numerical test is SHL and timed, and mentions a "telephone interview" stage. [Reported, S287] JobTestPrep sells "SHL-style" practice. [Reported, S288] These are test-prep sellers. Their descriptions (timed SHL tests, phone interview) do not match LSEG's own current wording (untimed, immersive, video). They may describe older cycles or other LSEG roles.
- One search snippet claimed a recent shift towards Aon and SHL and less Cappfinity use at LSEG. I could not identify or open the page behind it. [Reported, unverified, S299] The live LSEG link to a Cappfinity hub contradicts it for the 2027 cycle.

What the immersive assessment probably looks like (Cappfinity's general format, not LSEG-specific):
- A single storyline set in a realistic role. Situational "strengths" questions with numerical and verbal tasks built in, and sometimes a written or video task. Sections are "often generously timed or untimed". You may be asked both what you would do and how much you would enjoy it. [Reported, S289; this guide does not mention LSEG]
- Candidate ANECDOTE (Glassdoor, graduate programme): "Behavior Assessment with personality, behavior and logic tests without time limit"; the questions are mainly behavioural and "very well-crafted". [Reported, SNIPPET, S291]
- Practical implication: answer consistently and honestly. Read every email and attachment in the simulation, because the numerical items sit inside the story. [Inferred]

### 1.3 The strengths-based video interview

- LSEG confirms the strengths style and the themes: experiences, motivations, strengths, and what inspires you about a career at LSEG. [Confirmed, S260, S264]
- ANECDOTE (Glassdoor, graduate programme, SNIPPET): a video assessment "composed of 8 questions" with no time limit; "unlimited time to prepare" but "only one attempt to record an answer of 1-2 minutes". [Reported, S291] The question count is anecdotal and may differ by year or track.
- ANECDOTE (TheStudentRoom, 2026 graduate threads, SNIPPET): candidates said the video interview invite tended to arrive about a day after the online assessment, and that waiting 2 to 3 days with no invite might not be a good sign. [Reported, S293, low confidence]
- Typical Cappfinity-style strengths prompts include "How do you feel when you are looking at data?", "How do you deal with setbacks?", "How do you stay motivated?". These are third-party examples, not LSEG's own questions. [Reported, S289]
- LSEG has not published its exact questions. The question bank (Question_Bank_draft.md) uses the themes LSEG names plus common strengths-style prompts. [Inferred]

### 1.4 The half-day virtual assessment centre

- Confirmed: half day, virtual, several exercise types, details sent with the invite, includes a chance to meet LSEG people. [Confirmed, S260, S264]
- Reported by a test-prep site: group exercise ("small teams to solve a business case or scenario"), case study ("analyse a business scenario, review data, and propose solutions"), and a final interview with "senior managers or team leaders". [Reported, S286]
- ANECDOTE (Glassdoor, technology graduate scheme, SNIPPET): group exercise with 3 other candidates; about 30 minutes of individual reading of an information pack, then about 30 minutes of group discussion while 2 assessors listen; each candidate given a factor (for example ESG, economic, political, technological) to argue which has the biggest impact; assessors focused on group behaviour more than content. A case study with 30 minutes to review a long pack about a fictional website. Described as "Fast and Easy". [Reported, S292] This is the tech track and may differ for business.
- Business Analyst or Engineering tracks may add technical elements; Business Management does not list a technical assessment. [Confirmed by absence in S260]

### 1.5 Programme facts, intake, conversion, pay

- Internship: 9 weeks, starting June 2027, London, hybrid with 3 days a week in the office. Eligibility: penultimate-year undergraduate finishing summer 2028. Closes 30 October 2026 but may close early. [Confirmed, S260; JD.md]
- Placement: interns join LSE, LSEG FX, Tradeweb, Turquoise or LCH. LSEG uses the process to "get to know your skills and interest and how they align with the needs of the business". [Confirmed, S260]
- Posting date: the Workday API shows a start date of 2026-09-21 ("Posted 14 Days Ago" on 2026-10-05). JD.md says about 29 Sep. Small discrepancy, not material. [Confirmed, S260, S263]
- Wording discrepancy: JD.md says "review all the graduate programme opportunities"; the live posting text says "internship programme opportunities". [Confirmed, S260]
- On 2026-10-05 the Graduate_Careers Workday board listed 19 postings. The London Business Management and Sales Graduate Programme (R0123406) was not among them; New York's version (R0123419-2) was. [Confirmed, S263] It may have closed or be paused. [Inferred]
- Business Graduate Programme (what interns aim to convert into): 12 months, starts September 2027, Commercial and Business Analyst pathways, 8-week group project, offsite skills training, AI upskilling. [Confirmed, S268] FTSE Russell posting: "12-month development journey", global induction, "Ignite" mid-point offsite, 5 study days, graduates join permanently. [Confirmed, S261]
- Intake size: not published. The ISE case study (1 Aug 2024) reports an "8-fold increase in programme participants in one year" and "4.5x growth in programme locations in one year" but gives no absolute numbers. [Confirmed as ISE publication of LSEG's own figures, S270]
- Conversion: ISE reports a "42% increase in intern conversions in one year" and a "35% increase in offer acceptance rate". These are relative changes, not conversion rates. [Confirmed, S270] The actual intern-to-graduate conversion rate is unknown. [Gap]
- Award: LSEG won ISE's Best Graduate Development Programme Award 2024. [Confirmed, S270]
- Intern pay: no official figure. Glassdoor snippets show London "Summer Intern" pay of about £37K to £38K a year pro rata, and general intern pay of £36K to £40K. Glassdoor also shows a model "estimate" of £69K to £100K for Business Management Summer Internship, which is very unlikely to be real pay and should be ignored. [Reported, SNIPPET, S295, low confidence] Bright Network listings may show pay but were blocked. [S296, not read]

### 1.6 Question bank and questions to ask

The full bank is in `/home/user/Applications2027/LSEG/research/Question_Bank_draft.md`: 58 questions in 10 groups (motivation 6, why Markets 5, strengths 10, behavioural 6, commercial awareness 7, markets basics 8, data 4, case and AC 4, values 4, ethics 4). Each has what is being tested, an answer structure, sourced LSEG facts and traps.

Summary list:
- Motivation: Why LSEG; why not a bank; what you know about the five businesses; what inspires you about LSEG; where you see yourself; tell us about yourself.
- Why Markets: which business and why; FX client goals; debt listings research; what risk teams do; venue vs clearing house.
- Strengths: what energises you; what drains you; staying organised; learning quickly; starting vs finishing; looking at data; best in a team; plans changing; what friends say; many things vs one thing.
- Behavioural: solving a customer problem; using data to persuade; difficult colleague; failure; improving a process; tight deadline.
- Commercial: a recent LSEG development; how Markets makes money; why H1 2026 revenue grew; LSE challenges; AI in infrastructure; competitors; tokenisation.
- Markets basics: CCP; spot vs forward FX; bond listing; exchange vs MTF; interest rate swaps and clearing; Tradeweb; ETPs and LSE 24; trade lifecycle.
- Data: read a volume table; measure a product launch; your tools; estimation.
- Case and AC: group ranking exercise; case pack recommendation; client outage; three urgent requests.
- Values: Integrity, Partnership, Excellence, Change, using LSEG's own definitions (S271).
- Ethics: inside information; colleague's error; operational resilience; client gift.

Ten smart questions to ask (each relies on a recent source):
1. LSE 24 goes to client testing by end 2026, with ETPs first in H1 2027 and trading 17:00 to 07:50. What has early client feedback been, and would an intern see that work? [S278]
2. FXall is being integrated into Workspace, with straight-through execution into ForexClear. How does the team decide when to sell venue and clearing together? [S284]
3. Turquoise Europe in Amsterdam got new leaders in March 2026. What does success for Turquoise look like over the next year? [S277]
4. The Private Securities Market had its first transactions in H1 2026. Does the primary markets team see it as a route to a later public listing? [S285]
5. With the HSBC DSD link for the DIGIT digital gilt pilot due by Q1 2027, which skills will Markets graduates need in 2028 that they do not need today? [S285]
6. Q2 2026 volumes moderated after an exceptional Q1. How does your team plan for quieter markets? [S285]
7. The JD says LSEG places interns based on what it learns during recruitment. How is that decided, and can preferences change? [S260]
8. ISE reported a 42% rise in intern conversions in one year. What do interns who convert tend to do differently? [S270]
9. TradeAgent had 11 customers live after launch. How do commercial and risk teams work together on launches like that? [S285]
10. LSEG's "About" text now says "LSEG. Make more possible." How has that changed how client-facing teams describe LSEG? [S278]

### 1.7 Leaders an intern in Markets might hear from or read about (WS7)

No interviewers are named. These are public, professional facts only. "Tenure" is from the source date. Check titles again close to the AC, because LSEG has changed several Markets roles in 2025 and 2026.

| Person | Role (as of source date) | Tenure and career path | Public voice | Confidence |
|---|---|---|---|---|
| David Schwimmer | CEO, LSEG; member of LSEG plc Board | Joined 2018. Before that 20 years at Goldman Sachs (Global Head of Market Structure; Global Head of Metals & Mining); lawyer at Davis Polk. Yale BA; Harvard JD; Fletcher MALD. | Leads results calls; on Q1 2026 call discussed FXall investment and integration. | [Confirmed, S273, S284] |
| Daniel Maguire | Group Head, LSEG Markets and CEO, LCH Group | Joined LCH 1999; Global Head of SwapClear, ForexClear, LCH Group COO; J.P. Morgan 2005 to 2008; back at LCH 1 Sep 2008 and led the trading and unwinding of Lehman's LCH-cleared bond and repo portfolio; New York 2010 to 2014 building LCH US; CEO LCH Group and LSEG ExCo since 2017. Board Director, Tradeweb Markets Inc.; ISDA Board. | Quoted in LCH releases on leadership (Jan 2025, May 2026). Known for work on CCP regulation, LIBOR transition and Brexit. | [Confirmed, S273, S274, S275, S276] |
| Julia Hoggett | CEO, London Stock Exchange plc and Head of Digital and Securities Markets, LSEG | Appointed Dec 2020 (start 2021) from the FCA (Director of Market Oversight; Head of Wholesale Banking Supervision); before that BAML, DEPFA (CEO DEPFA ACS Bank), JP Morgan debt capital markets from 1997. Cambridge BA, Social and Political Sciences. Not listed on the Group Executive Team page as read on 2026-10-05. | Quoted on LSE 24 (July 2026): "an important step in the evolution of our markets". | [Confirmed, S278, S279, S273] |
| Charlie Walker | Deputy CEO, London Stock Exchange plc; oversees primary markets | Joined LSEG 2018 from J.P. Morgan Cazenove ECM; Deputy CEO from Sept 2023. Still Deputy CEO in March 2026 release. | Quoted on European equities appointments (Mar 2026). | [Confirmed, S280, S277] |
| Tom Stenhouse | CEO, Turquoise (subject to regulatory approval) and Head of Product | Appointed March 2026. Previous co-head of equities trading reported by trade press; the LSEG release does not give his start year. | Not found. | [Confirmed role, S277] |
| Simon McQuoid-Mason | Leads New Product Development, Market Structure and Business Development for LSE and Turquoise | Appointed Dec 2025; Business Development added Mar 2026. | Not found. | [Confirmed, S277] |
| James Pearson | Head of FX, LSEG | Joined LCH as Head of ForexClear 1 June 2021. Previously Global Head of FX Trading at RBS; Nomura and Lehman (G10 spot, EM FX); Citi and HSBC trading desks. Took over as group head of FX in May 2024 after Neill Penney left (trade press). No LSEG release on the FX head appointment was found. | Extended interview with The Full FX (May 2026) on FX swaps technology and workflow. | [Confirmed for 2021 history, S281; Reported for current title, S282, S283] |
| Simon Jones | Head of FX Product and Liquidity, Markets, LSEG | Not researched. | In the same Full FX interview (May 2026). | [Reported, S283] |
| Andrew Batchelor | Head of ForexClear | Joined LCH 2021 as ForexClear COO and Head of Product; 20 years at Barclays (Global FX COO and others). Chartered Accountant. | In the Full FX interview (May 2026). | [Confirmed, S274] |
| Susi de Verdelon | CEO, LCH Ltd | Joined LCH 2017; Group Head of SwapClear and Listed Rates; CEO from Feb 2025; ex-Goldman Sachs MD. Oxford MA. ISDA board; Co-Head of Europe, WIFM. | Quoted Jan 2025 on "a culture of excellence". | [Confirmed, S275, S274] |
| Corentine Poilvet-Clédière | CEO, LCH SA (Paris) | With LSEG since 2012; Head of Repo clearing, Collateral and Liquidity management at LCH SA; Global Head of Regulatory Strategy. | Not researched. | [Confirmed, S274] |
| John Horkan | COO, Markets and LCH Group; Head of Americas | Joined LCH 2012; SwapClear COO; 19 years at BofA Merrill Lynch and J.P. Morgan before. CFTC Global Markets Advisory Committee since 2019. | Not researched. | [Confirmed, S274] |
| Nick Rustad | Head of LCH SwapClear and Listed Rates | Ex-JPMorgan (Global Head of Futures and Derivatives Clearing), ex-Taula Capital; former FIA Chair. Nottingham Trent BA. | Not researched. | [Confirmed, S274] |
| Billy Hult | CEO, Tradeweb | CEO since January 2023 after about 15 years as President. | Interviews on bond trading and prediction markets in 2026 (snippet). | [Reported, SNIPPET, S298] |
| Patricia (Trish) Cuddy | Group Head of People, Markets and Americas (LCH leadership page) | With LSEG over 10 years; before that ICE and NYSE HR. Quoted in the ISE graduate programme case study as "Group Head of HR, Post Trade and Capital Markets". | Quoted on graduate programme design (ISE 2024). | [Confirmed, S274, S270]. Same person in both sources is [Inferred, high confidence]: same surname, "Trish" is a common short form of Patricia, both are HR heads for Post Trade/Markets. |
| Erica Bourne | Group Chief People Officer | Appointed Jan 2023; ex-Burberry CPO; 12 years at American Express. Chairs the LSEG Foundation. | Not researched. | [Confirmed, S273] |
| Chris Coleman | Group Head of Sales and Account Management | Joined Jan 2026 from State Street (Global Head of Sales and Client Coverage). | Not researched. | [Confirmed, S273] |
| Head of Early Careers | Not publicly named on any LSEG page read. A "Global Early Careers Lead" job ad appeared in search results but was not opened, and no person is attributed here. | | | [Gap] |

### 1.8 Interviewer types by stage and how to adapt live

| Stage | Likely assessor | Evidence | How to adapt |
|---|---|---|---|
| Immersive assessment | No live person; automated scoring against a strengths model. | [Inferred from S264, S265, S289] | Be consistent. Answer as yourself, not as an ideal candidate. Read every item in the scenario. |
| Video interview | Recorded; reviewed later by trained reviewers, probably early careers recruiters or trained business reviewers. | Asynchronous format [Confirmed for Cappfinity product, S290]; reviewer identity not published [Gap] | You get no live feedback, so put the answer first, give one example, and end on a clear link to LSEG. Show energy through detail and pace. |
| AC group exercise | Two observers per group (anecdote). | [Reported, S292] | Show listening by naming others' points. Keep time. Help the group reach a decision. |
| AC case or interview | Business practitioners ("senior managers or team leaders", per test-prep source). LSEG says the AC is a chance to "meet our people". | [Reported, S286; Confirmed, S264] | With a practitioner: go deeper on one business, ask a smart question. With a recruiter: stress motivation, values and fit. With a recent graduate or intern assessor (common at many firms, not confirmed at LSEG): be warm and specific about the programme. |

Live adaptation tips (all [Inferred]):
- If the interviewer asks follow-ups about detail, they are probably a practitioner. Give numbers and the "why".
- If they ask about motivation and values, they are probably scoring fit. Use LSEG's own value wording (S271).
- If you do not know a fact, say so and reason it out. Do not invent figures.
- No manipulation tactics. Mirroring, flattery or name-dropping senior leaders you have never met will look false.

---

## 2. Key numbers

| Item | Value | Source | Confidence |
|---|---|---|---|
| Internship length | 9 weeks | S260 | Confirmed |
| Start | June 2027 | S260, S267 | Confirmed |
| Application close | 30 Oct 2026 (rolling; may close early) | S260 | Confirmed |
| Posting start date (Workday) | 2026-09-21 | S260 | Confirmed |
| Office pattern | Hybrid, 3 days in office | JD.md | Confirmed (JD) |
| Stages | 4 (application, immersive OA, strengths video, half-day virtual AC) | S260, S264 | Confirmed |
| Video interview questions | about 8; 1 to 2 min each; one take; untimed prep | S291 | Reported, ANECDOTE |
| AC group exercise | 4 candidates, about 30 min reading + 30 min discussion, 2 assessors (tech track) | S292 | Reported, ANECDOTE |
| Graduate programme length | 12 months (start Sept 2027) | S261, S268 | Confirmed |
| Grad group project | 8 weeks | S268 | Confirmed |
| Study days on grad programme | 5 | S261 | Confirmed |
| Graduate participants growth | 8-fold in one year | S270 | Confirmed (ISE, 2024) |
| Intern conversions | up 42% in one year (relative) | S270 | Confirmed (ISE, 2024) |
| Offer acceptance rate | up 35% in one year (relative) | S270 | Confirmed (ISE, 2024) |
| Intern pay (London) | about £37K to £38K a year pro rata | S295 | Reported, SNIPPET, low |
| LSEG employees | over 26,000 in 65 countries | S272, S276 | Confirmed |
| Markets total income H1 2026 | £1,920m, +11.9% constant currency | S285 | Confirmed |
| Equities revenue H1 2026 | £230m, +12.2% | S285 | Confirmed |
| Fixed Income, Derivatives & Other H1 2026 | £864m, +13.0% | S285 | Confirmed |
| FX revenue H1 2026 | £145m, +7.6% | S285 | Confirmed |
| OTC Derivatives revenue H1 2026 | £355m, +13.6% | S285 | Confirmed |
| Securities & Reporting H1 2026 | £124m, +8.2% | S285 | Confirmed |
| Tradeweb ADV H1 2026 | $3.2trn, +24.8% | S285 | Confirmed |
| LSEG FX average daily volume H1 2026 | $561bn, +5.8% | S285 | Confirmed |
| UK equities average daily value traded H1 2026 | £6,671m, +33.5% | S285 | Confirmed |
| SwapClear IRS notional cleared H1 2026 | $1,165trn, +29.4% | S285 | Confirmed |
| ForexClear notional cleared H1 2026 | $33,311bn, +45.2%; 41 members | S285 | Confirmed |
| RepoClear nominal H1 2026 | €182.8trn, +8.9% | S285 | Confirmed |
| Forward First Fixing Q2 2026 | over $330bn, a record | S285 | Confirmed |
| LSE 24 hours | 17:00 to 07:50 (pause 18:30 to 19:00); ETPs first, H1 2027 | S278 | Confirmed |
| Graduate_Careers postings live | 19 on 2026-10-05 | S263 | Confirmed |

---

## 3. Verbatim quotes actually read

All quotes below were read in full page text (curl or Workday API) unless marked "via WebFetch extraction".

1. "The next stage of the application process is an untimed Immersive Online Assessment. The assessment is designed to give you an insight into what it's like to work at LSEG." (S260)
2. "The second stage is a video interview where you will answer a series of questions using a strength-based-interview style" (S260)
3. "The final stage is a half day assessment centre which involves several different types of exercises - further information is provided at the point of invite." (S260) [original uses a dash between clauses]
4. "To allow us to place you in the right area, during the recruitment process we will get to know your skills and interest and how they align with the needs of the business." (S260)
5. "Before you begin, visit our Assessment Preparation Hub for guidance, tips and technical support to help you feel confident and prepared. You'll then complete an interactive assessment designed to help us understand your strengths, potential and approach to solving real-world challenges." (S264)
6. "Through a series of questions, we'll learn more about your experiences, motivations, strengths and what inspires you about a career at LSEG." (S264)
7. "Take part in interactive activities, discussions and exercises designed to showcase your skills, ideas and potential. It's also a chance to get to know LSEG, meet our people and discover more about the opportunity." (S264)
8. `<title>Cappfinity Preparation Hub</title>` and `<meta name="description" content="Powered by Cappfinity" />` (S265, page source)
9. "Progress through a 12-month development journey aiming to build foundational skills that are key for your future success" (S261)
10. "Meet in person with your cohort at 'Ignite', the programme mid-point skills offsite." (S261)
11. "42% increase in intern conversions in one year" (S270)
12. Trish Cuddy: "Critical to Post Trade's future success is maintaining our position as a leader in the external environment." (S270)
13. "At LSEG, our values are Integrity, Partnership, Excellence, and Change." and "Integrity: We stand by our principles and deliver on our promises. We earn trust by acting responsibly." (S271)
14. "LSEG's Markets Division combines the Group's flagship trading and clearing businesses - the London Stock Exchange, Turquoise, LSEG FX, Tradeweb and LCH Group - with its risk management, capital optimisation, collateral management, and regulatory reporting capabilities, including Acadia and Quantile." (S273) [original uses dashes]
15. Julia Hoggett: "The launch of LSE 24 marks an important step in the evolution of our markets, providing clients with greater flexibility beyond traditional trading hours and supporting more digital, connected global markets." (S278)
16. Daniel Maguire: "Her deep expertise in governance, risk and operational resilience will provide a distinct perspective as we continue to grow our global offering." (S276)
17. Susi de Verdelon: "I am committed to driving forward our strategic vision, fostering a culture of excellence, and strengthening our position as a market leader in risk management." (S275)
18. David Schwimmer: "We've got FXall also plugged in as of a year or two ago into Tradeweb. We have straight through FXall execution capabilities into ForexClear, so the kind of end-to-end processing." (S284)
19. "Heightened market volatility and geopolitical uncertainty drove exceptional clearing activity across interest rate swap, foreign exchange and credit derivatives in the first quarter." (S285)
20. "Applications are reviewed on a first-come, first-served basis, so we strongly encourage you to complete all required assessments as early as possible." (S266, via WebFetch extraction)
21. "The LSEG assessment tests are provided by the test publisher SHL" (S286, via WebFetch extraction; test-prep claim, disputed)
22. "Cappfinity's video interview platform is fully asynchronous and brand-aligned" (S290, via WebFetch extraction)
23. Charlie Walker: "We remain committed to operating high quality markets that support our customers' evolving capital raising and trading needs." (S277)

---

## 4. Source table

[Sxx] | Outlet | Title | Pub date | URL | Accessed | Status | Confidence note

[S260] | LSEG Workday (JSON API) | Business Management Summer Internship (R0123386) | 2026-09-21 (posting start) | https://lseg.wd3.myworkdayjobs.com/en-US/Graduate_Careers/details/Business-Management-and-Sales-Summer-Internship_R0123386 (read via /wday/cxs/lseg/Graduate_Careers/job/... API) | Accessed 2026-10-05 | FETCHED | Primary, official. High.
[S261] | LSEG Workday (JSON API) | Business Graduate Programme (FTSE Russell) R0123708 | 2026-09-23 | https://lseg.wd3.myworkdayjobs.com/en-US/Graduate_Careers/job/London-United-Kingdom/Business-Graduate-Programme--FTSE-Russell-_R0123708 | Accessed 2026-10-05 | FETCHED | Official; grad programme structure. High.
[S262] | LSEG Workday (JSON API) | Business Analyst Summer Internship R0123387 | 2026-09-21 | https://lseg.wd3.myworkdayjobs.com/en-US/Graduate_Careers/job/London-United-Kingdom/Business-Analyst-Summer-Internship_R0123387 | Accessed 2026-10-05 | FETCHED | Official; same process text. High.
[S263] | LSEG Workday (JSON API) | Graduate_Careers job list (19 postings) | live list | https://lseg.wd3.myworkdayjobs.com/Graduate_Careers | Accessed 2026-10-05 | FETCHED | Snapshot on access date. High.
[S264] | LSEG | Business Programme (hints and tips modal) | undated | https://www.lseg.com/en/modal/careers/business-programme | Accessed 2026-10-05 | FETCHED | Official; raw HTML read, includes hub link. High.
[S265] | Cappfinity | Cappfinity Preparation Hub (page source) | undated | https://hub.preparationplus.com/dashboard/ | Accessed 2026-10-05 | FETCHED | HTML head only (JS app). Vendor identification high.
[S266] | LSEG | Early careers programmes (FAQ) | undated | https://www.lseg.com/en/careers/graduate-internship-programmes | Accessed 2026-10-05 | FETCHED | Via WebFetch extraction. High.
[S267] | LSEG | Internship Programmes | undated | https://www.lseg.com/en/careers/graduate-internship-programmes/internship-programmes | Accessed 2026-10-05 | FETCHED | Via WebFetch extraction. High.
[S268] | LSEG | Graduate Programmes | undated | https://www.lseg.com/en/careers/graduate-internship-programmes/graduate-programmes | Accessed 2026-10-05 | FETCHED | Via WebFetch extraction. High.
[S269] | LSEG | graduates and students (FAQ) | undated | https://www.lseg.com/careers/graduates-and-students | Accessed 2026-10-05 | FETCHED | Via WebFetch extraction. High.
[S270] | Institute of Student Employers (ISE) | How LSEG's graduate programme is meeting future skills needs | 2024-08-01 | https://ise.org.uk/knowledge/insights/206/how_lsegs_graduate_programme_is_meeting_future_skills_needs/ | Accessed 2026-10-05 | FETCHED | LSEG-supplied case study; figures are relative, 2024. Medium-high.
[S271] | LSEG | Our purpose and values | undated | https://www.lseg.com/en/about-us/purpose-values | Accessed 2026-10-05 | FETCHED | Official. High.
[S272] | LSEG | Careers | undated | https://www.lseg.com/en/careers | Accessed 2026-10-05 | FETCHED | Official; 26,000 people, 65 countries. High.
[S273] | LSEG | Executive Team | undated (live) | https://www.lseg.com/en/about-us/executive-team | Accessed 2026-10-05 | FETCHED | Official; current as of access. High.
[S274] | LSEG | Meet Our Leaders: LCH Executive Team | undated (live) | https://lseg.com/en/post-trade/clearing/about-lch/structure-and-governance/leadership | Accessed 2026-10-05 | FETCHED | Official. High.
[S275] | LSEG press release | Susi de Verdelon appointed CEO of LCH Limited | 2025-01-21 | https://www.lseg.com/en/media-centre/press-releases/lch/2025/susi-de-verdelon-appointed-ceo-of-lch-limited | Accessed 2026-10-05 | FETCHED | Official. High.
[S276] | LSEG press release | LCH Limited appoints Carole Machell as Chair | 2026-05-05 | https://www.lseg.com/en/media-centre/press-releases/lch/2026/lch-limited-appoints-carole-machell-as-chair | Accessed 2026-10-05 | FETCHED | Official. High.
[S277] | LSEG press release | LSEG strengthens presence in European equities trading | 2026-03-19 | https://www.lseg.com/en/media-centre/press-releases/2026/lseg-strengthens-presence-european-equities-trading | Accessed 2026-10-05 | FETCHED | Official. High.
[S278] | LSEG press release | London Stock Exchange to launch LSE 24 | 2026-07-21 | https://www.lseg.com/en/media-centre/press-releases/2026/london-stock-exchange-to-launch-lse-24 | Accessed 2026-10-05 | FETCHED | Official. High.
[S279] | LSEG press release | LSEG announces new CEO of London Stock Exchange plc | 2020-12-07 | https://www.lseg.com/en/media-centre/press-releases/2020/lseg-announces-new-ceo-london-stock-exchange-plc | Accessed 2026-10-05 | FETCHED | Official; career history. High.
[S280] | LSEG press release | Charlie Walker appointed Deputy CEO of London Stock Exchange | 2023-09-11 | https://lseg.com/en/media-centre/press-releases/2023/charlie-walker-appointed-deputy-ceo-london-stock-exchange | Accessed 2026-10-05 | FETCHED | Official. High.
[S281] | LSEG press release | LCH appoints James Pearson as Head of ForexClear | 2021-05-24 | https://www.lseg.com/en/media-centre/press-releases/lch/2021/lch-appoints-james-pearson-head-forexclear | Accessed 2026-10-05 | FETCHED | Official; 2021 role only. High.
[S282] | The Full FX | Change at the Top of LSEG FX with Two Senior Exits | 2024-05-27 | https://thefullfx.com/change-at-the-top-of-lseg-fx-with-two-senior-exits/ | Accessed 2026-10-05 | FETCHED | Trade press, via WebFetch extraction. Medium-high.
[S283] | The Full FX | The Full FX Talks to LSEG FX - Part One | 2026-05-11 | https://thefullfx.com/the-full-fx-talks-to-lseg-fx-part-one/ | Accessed 2026-10-05 | FETCHED | Trade press; confirms current titles as of May 2026. Medium-high.
[S284] | LSEG investor relations | LSEG Q1 2026 Trading Update transcript | 2026-04-23 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/trading-statement/transcripts/lseg-q1-2026-trading-update-transcript-23apr2026.pdf | Accessed 2026-10-05 | FETCHED | Official PDF. High.
[S285] | LSEG investor relations | LSEG H1 2026 Interim Report | 2026-07-30 | https://www.lseg.com/content/dam/lseg/en_us/documents/investor-relations/financial-results/interim-report/lseg-interim-report-h1-2026-30july2026.pdf | Accessed 2026-10-05 | FETCHED | Official PDF. High.
[S286] | GraduatesFirst (test-prep vendor) | LSEG Recruitment Process, Graduate Programmes Practice Guide | updated 2025-10-21 | https://www.graduatesfirst.com/lseg-aptitude-tests | Accessed 2026-10-05 | FETCHED | Commercial; SHL claim conflicts with LSEG wording. Low-medium.
[S287] | PracticeAptitudeTests (test-prep vendor) | London Stock Exchange Group (LSEG) Assessments | published 2020-10-02, updated 2025-11-18 | https://www.practiceaptitudetests.com/top-employer-profiles/london-stock-exchange-assessments/ | Accessed 2026-10-05 | FETCHED | Commercial; mentions phone interview, likely dated. Low.
[S288] | JobTestPrep (test-prep vendor) | London Stock Exchange Group (LSEG) Hiring Tests | undated (2026 course) | https://www.jobtestprep.co.uk/london-stock-exchange-group-tests | Accessed 2026-10-05 | FETCHED | Commercial; "SHL-style". Low.
[S289] | Intervyo | Cappfinity Immersive Assessment Guide: Strengths and SJT | 2026 (footer) | https://www.intervyo.co.uk/assessments/cappfinity | Accessed 2026-10-05 | FETCHED | Third-party guide; does not mention LSEG. Medium for Cappfinity format.
[S290] | Cappfinity | Video Interview (product page) | undated | https://cappfinity.com/solutions/for-talent-leaders/assessments/video-interview/ | Accessed 2026-10-05 | FETCHED | Vendor marketing; not LSEG-specific. Medium.
[S291] | Glassdoor | LSEG Graduate Program Interview Questions | various | https://www.glassdoor.co.uk/Interview/LSEG-London-Stock-Exchange-Group-Graduate-Program-Interview-Questions-EI_IE11860.0,32_KO33,49.htm | Accessed 2026-10-05 | SNIPPET (403 on fetch) | ANECDOTE; review dates unknown. Low-medium.
[S292] | Glassdoor | LSEG Technology Graduate Scheme Interview Questions | various | https://www.glassdoor.co.in/Interview/LSEG-London-Stock-Exchange-Group-Technology-Graduate-Scheme-Interview-Questions-EI_IE11860.0,32_KO33,59.htm | Accessed 2026-10-05 | SNIPPET (403 on fetch) | ANECDOTE; tech track; AC detail. Low-medium.
[S293] | TheStudentRoom | LSEG Graduate Programme 2026 / London stock exchange group grad schemes 2026 | 2025 to 2026 | https://www.thestudentroom.co.uk/showthread.php?t=7638848 and https://www.thestudentroom.co.uk/showthread.php?t=7629839 | Accessed 2026-10-05 | SNIPPET (403 on fetch) | ANECDOTE; timing claim. Low.
[S294] | TheStudentRoom | LSEG Summer Internship Programme 2025 | 2024 to 2025 | https://www.thestudentroom.co.uk/showthread.php?t=7543818 | Accessed 2026-10-05 | NOT READ (403) | Exists; content unknown. Not used for claims.
[S295] | Glassdoor | LSEG Intern Salaries in London | various | https://www.glassdoor.com/Intern-Salary/LSEG-London-Stock-Exchange-Group-London-Internship-Salary-EI_IE11860.0,32_IL.33,39_IM1035.htm | Accessed 2026-10-05 | SNIPPET | Self-reported plus model estimates; the £69K to £100K figure is an estimate and unreliable. Low.
[S296] | Bright Network | Business Summer Internship Programme 2025 - LSEG | 2024 to 2025 | https://www.brightnetwork.co.uk/graduate-jobs/london-stock-exchange-group/business-summer-internship-2025 | Accessed 2026-10-05 | NOT READ (403) | Possible pay and deadline data; not used.
[S297] | Gradcracker | London Stock Exchange Group hub | undated | https://www.gradcracker.com/hub/300/london-stock-exchange-group | Accessed 2026-10-05 | NOT READ (403) | Not used.
[S298] | Tradeweb / Business Wire | Tradeweb Elevates Billy Hult to Chief Executive Officer | 2023-01-03 | https://www.businesswire.com/news/home/20230103005226/en/Tradeweb-Elevates-Billy-Hult-to-Chief-Executive-Officer | Accessed 2026-10-05 | SNIPPET (403 on fetch) | Official release exists; only snippet read. Medium.
[S299] | Search-result snippet (originating page not identified; possibly getsmartresume.com) | Claim of a shift to Aon and SHL tests at LSEG | unknown | https://www.getsmartresume.com/article/refinitiv-lseg-graduate-program (candidate page) | Accessed 2026-10-05 | SNIPPET | Unverified; contradicted by S264 and S265. Very low.

---

## 5. Gaps

1. LSEG never names its assessment vendor in text. The Cappfinity link is strong evidence but still an inference. The video interview platform is not confirmed.
2. No first-hand forum thread could be read (TSR, Reddit, Glassdoor, WSO all blocked). All candidate anecdotes are snippets with unknown dates and tracks. Reddit and WallStreetOasis returned nothing usable.
3. Exact number of video questions, prep and answer time for the 2027 cycle: only one anecdote (8 questions, 1 to 2 minutes).
4. AC content for the Business track specifically: the detailed anecdote is from the tech track.
5. Intern pay: no official figure; Bright Network blocked; Glassdoor numbers are weak.
6. Intake size and actual conversion rate: only relative changes from 2024.
7. Head of Early Careers: not publicly named on any page read. Not attempted via LinkedIn (identity risk).
8. Tradeweb: CEO confirmed only by snippet; LSEG's ownership stake in Tradeweb not verified here.
9. Head of FX: no LSEG release found; title rests on trade press (May 2024 and May 2026).
10. YouTube intern vlog titles: not searched (search budget ran out).
11. Competitor facts (market shares, rival venues): not researched.
12. Offer timing for summer interns: no reliable source.

---

## 6. Interview angles

1. **Use the Cappfinity lens.** The immersive test and the video both probe what you do well and also what energises you [Inferred, S264, S265, S289]. Prepare 6 to 8 true stories and, for each, be ready to say why you enjoyed it. Consistency across stages matters.
2. **Show you understand "the full breadth".** The JD asks for people who want to understand "how it fits together" [S260]. Practise a 60-second explanation of the trade lifecycle using LSEG's own businesses: LSE or Turquoise or Tradeweb or FXall to trade, LCH to clear, regulatory reporting after [S273, S284].
3. **Use one recent number per answer, not five.** Strong options: Markets income £1,920m up 11.9% in H1 2026; ForexClear notional up 45.2%; LSE 24 coming in H1 2027 [S278, S285].
4. **Match your interest to the four exposure areas in the JD.** FX customers, debt listings research, business intelligence and operational improvements, risk [S260]. Have one story for each.
5. **Values are scored.** Use LSEG's definitions (S271). "How you achieve it" matters as much as results (JD) [S260]. Pick stories where you behaved well under pressure.
6. **Resilience and change are live themes.** Q1 2026 volatility, then moderation in Q2 [S285]; leadership changes in equities and LCH in 2025 and 2026 [S275, S276, S277]. Show calm adaptability.
7. **Ask a question only a researcher could ask.** Use section 1.6. Check the leader titles again in the week of the AC.
8. **Apply early.** Rolling, first-come first-served review; may close before 30 October [S260, S266].
9. **Do not over-prepare SHL numerical tests.** Test-prep sites say SHL, but LSEG's own wording points to an untimed immersive simulation [S260, S264, S286]. A little numerical practice is still useful because numerical items are built into immersive tests [S289].
10. **Plain explanations win.** Expect "explain a CCP to a friend" style probes. Practise the eight market basics in the bank (section F).
