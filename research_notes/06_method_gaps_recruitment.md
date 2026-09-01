# Research Note 06 — Method, Recruitment Process, and Unclosed Gaps
Research conducted: 2026-08-31

## METHOD — how the primary data was actually obtained
1. **JPMorgan PDFs render as binary through the web-fetch tool.** Solution: downloaded each PDF with curl and extracted text locally with pypdf/PyMuPDF. This is why segment figures in this report are transcribed from the source tables rather than from a summary.
   - 10-K 2025: 410 pages, 1.55M chars extracted
   - 4Q25 earnings release: 8 pages
   - 4Q25 financial supplement: 29 pages
   - 2026 Company Update transcript: 31 pages
   - CRD IV governance disclosures: 10 pages
2. **Companies House filings are SCANNED IMAGES** with zero embedded text. Solution: installed tesseract and OCR'd page images rendered by PyMuPDF.
   - J.P. Morgan Securities plc FY2025 (114 pages): OCR succeeded for the strategic report. Figures cross-checked against the narrative text in the same document, which restates them in words — a good internal consistency check on the OCR.
   - J.P. Morgan Europe Limited FY2025 (80 pages): OCR did NOT complete — page rendering was pathologically slow on this particular file. **GAP LEFT OPEN AND DISCLOSED.**
3. **Careers site is a content shell.** careers.jpmorgan.com now 301-redirects to jpmorganchase.com/careers/explore-opportunities. Those pages render programme *categories* only. The live data is in Oracle Recruiting Cloud:
   - Search: `https://jpmc.fa.oraclecloud.com/hcmRestApi/resources/latest/recruitingCEJobRequisitions?onlyData=true&expand=requisitionList.secondaryLocations&finder=findReqs;siteNumber=CX_1001,limit=200,offset=0,keyword=<kw>`
   - Detail: `.../recruitingCEJobRequisitionDetails?expand=all&onlyData=true&finder=ById;Id="<Id>",siteNumber=CX_1001`
   - Candidate-facing: `https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/requisitions` and `.../job/<Id>`
   - 2,751 unique requisitions harvested across ~35 keyword queries; 43 UK early-careers requisitions pulled in full detail.

## RECRUITMENT PROCESS — evidence quality
PRIMARY (from requisition text/metadata):
- Posting start 2026-08-31, ExternalPostedEndDate 2026-11-01 23:55 (+00:00) on the 2027 programmes
- "Application deadline: 1st November 2026" stated in the description text of 17 of 43
- **"We will be filling our classes on a rolling basis. We strongly encourage you to submit your application as early as possible before job postings close."** — in 35 of 43
- "Help us learn about you by submitting a complete and thoughtful application, which includes your resume and location preference."
- Nine-week programme, five-day induction/training (15 of 43 mention nine/9-week)
- "June to August" (3 postings state it explicitly)
- "penultimate year or final year students" (7 postings)
- "2:1 Bachelor's degree (or equivalent)" (4 postings)
- Graduation windows seen: "August 2026 and July 2027" (full-time roles); "December 2027 and July 2028" (2027 summer internships)
- "Top performers may receive a 2028 full-time analyst offer at the end of the summer" (IB)
- **"We do not offer any type of employment-based immigration sponsorship for this program."** — Data & AI Summer Internship AND Data & AI Full Time Analyst ONLY (2 of 43). All other UK postings SILENT on sponsorship.
- NumberOfOpenings: NULL on every requisition.

SECONDARY / UNVERIFIED (recruitment aggregators, candidate reports — Extern, FE Training, IGotAnOffer, Leland, Glassdoor):
- Online assessment incl. numerical/situational judgement, and a timed maths test for some programmes
- HireVue asynchronous video interview: mostly behavioural + CV walk-through; described as the screening round before final rounds
- Final round = "superday" in the US, "assessment centre" in the UK; technicals on accounting/valuation/markets for IB and Markets
- Offers released in batches on a rolling basis
=> These are flagged as unverified in the report. JPMorgan does not publish its process.

## SPECIFIC PROGRAMME DETAIL WORTH QUOTING (all PRIMARY, from requisition text)
- **IB**: "Our nine-week program kicks off with five days of orientation and training... Top performers may receive a 2028 full-time analyst offer." Coverage sectors named: Consumer & Retail, Healthcare, Technology, Financial Institutions, Real Estate. Products: M&A, Corporate Finance Advisory, Infrastructure, Ratings Advisory, Sustainable Solutions, ECM, DCM.
- **Global Markets**: "nine-week program running from June to August, targeted at penultimate year or final year students and is a pipeline to the analyst programme the following year"; intern will "monitor markets, develop trade ideas, conduct portfolio reviews".
- **Sales** (separate requisition from Global Markets): "salespeople have a wide knowledge of multiple products, and proactively engage with clients and suggest trade ideas".
- **Payments**: "what it takes to 'make money move'"; "Global Payments business brings together Payments, Merchant Services and Commercial Card, delivering end-to-end capabilities across the full Pay In and Pay Out lifecycle".
- **Securities Services**: "Develop solutions and drive change in finance using project management, emerging technologies, data governance and analytics"; asks for "exceptional writing, verbal communication and client facing skills".
- **CIB Risk Management**: "Nine-weeks, with a five-day induction"; Credit Risk team "responsible for reviewing client credit strength and approving and managing retained credit risk (risk of default) within the CIB... including investment and non-investment grade syndicated loans, acquisition finance".
- **Data & AI**: "AWS, CoPilot, Snowflake, DataBricks, LLM"; "design scalable data platforms and pipelines, develop production-ready models".
- **Chase Digital Development Programme**: "revolutionising mobile banking"; "start your journey in becoming a Product Manager"; graduation Dec 2027–Jul 2028; "Interest in fintech; digital experiences".
- **CADP**: three disciplines — Analytics, Project Management, Process Improvement; full-time is "a two-year rotational experience across all three". **"This program is designed for students seeking broad, transferable business skills. It is not aligned to front-office, client-facing, or software engineering roles."** ← unusually candid, quoted in the report.

## GAPS LEFT OPEN (disclosed in report section 6.3)
1. JPMEL / Chase UK FY2025 P&L — OCR did not complete. Companies House 00938937.
2. UK Senior Country Officer — no primary source found.
3. JPMS plc employee headcount — note not reached in OCR.
4. J.P. Morgan International Bank Ltd — NOT in 10-K Exhibit 21; status unconfirmed.
5. Intake sizes — null in ATS; not published anywhere.
6. Return-offer conversion rates — no credible primary source.
7. Visa sponsorship for most UK programmes — postings silent.
8. Technology spend by line of business — in the Company Update slide deck, which I did not retrieve.
9. Whether a UK Spring Week will open later this autumn — unknowable today.

## THINGS I DELIBERATELY DID NOT DO
- Did not quote any forum or aggregator as fact.
- Did not present any group-level figure as a London figure.
- Did not invent a desk, a deadline, a headcount or an org-chart entry.
- Did not fill the JPMEL gap with a plausible-sounding estimate.
