<p class="kick">Section 1</p>

# The Application Pipeline: Submit to First Round {#sec1}

<p class="sectionmeta">What actually happens between clicking "Submit" and a human deciding to interview you — with the numbers, and with the myths removed.</p>

Most CV advice assumes a recruiter reads your CV first. **For large UK graduate schemes, that assumption is often wrong** — the CV is frequently read *after* an automated assessment, not before. Understanding the real order of operations tells you where to spend effort. Here is the pipeline, stage by stage.

## 1.1 The first 60 seconds: parsing, not reading

When you submit, no human sees anything yet. Your file hits an **Applicant Tracking System (ATS)**, which *parses* it — extracts text and maps it into database fields. iCIMS (a vendor) describes parsing as technology that "*extracts data, usually from a Word or PDF document… automatically identifies important, relevant terms in a CV such as a candidate's contact details, language level, years of experience*" and self-populates a form. Its parsing partner Textkernel claims "*90% of CVs can be processed without any human intervention.*" *(Source: iCIMS blog, "What is CV/resume parsing" — Appendix §1.)*

The pipeline every parser runs is roughly: **text extraction → tokenisation → sectioning → named-entity recognition → structured output** *(Resume Optimizer Pro — Appendix §1)*. If any stage mis-fires, the wrong text lands in the wrong field, and the recruiter later searching the database never finds you. This is the single most important, most evidence-backed fact in this section: **your first reader is a parser, and you write for it by keeping the layout boringly simple** (Section 2).

## 1.2 What parses cleanly, and what breaks

<div class="box warning" markdown="1">
<span class="lbl">What consistently breaks parsing (every source agrees)</span>

- **Multi-column layouts, tables, text boxes.** These scramble reading order. A two-column contact table can parse as "*Email: New York, NY Phone: [email]*" *(ProfileOps, on Taleo — Appendix §1)*.
- **Contact details in the header/footer.** Many parsers ignore the header region — put your email and phone in the body.
- **Graphics, logos, icons, photos, and scanned/image PDFs.** "*Lever can't parse images… Lever will not be able to extract that*" *(Jobscan — Appendix §1)*. A scanned PDF is the one format everyone agrees is fatal.
- **Non-standard section headings.** Use "Work Experience", "Education", "Skills" — not "My Journey" or "Toolbox".
</div>

| ATS | Formats accepted | Practical note | Confidence |
|---|---|---|---|
| **Workday** | PDF, DOC/DOCX, RTF, TXT | Strips layout to plain text, maps to profile schema; single-column strongly advised | Vendor + secondary |
| **Greenhouse** | .doc, .docx, .pdf, .rtf, .txt (to 100 MB) | Lenient parser; **humans score, not a bot** (see 1.3) | **Vendor (official)** |
| **Taleo (Oracle)** | DOCX preferred | Older, stricter parser; complex layouts fail more often | Secondary |
| **iCIMS** | DOCX, PDF, RTF, TXT | Uses Textkernel + skills taxonomy; auto-fills 10–15 fields | Vendor + secondary |
| **SmartRecruiters** | DOCX, text PDF (rejects image PDFs) | Among the more lenient; has a public parse API | Vendor |
| **Lever** | DOCX, PDF, RTF, HTML | Single-column, no tables/images | Secondary |

## 1.3 Is "keyword scoring" real, or a myth?

This is the most contested question in the whole pipeline, and the honest answer is **both, depending on the vendor.**

<div class="box disagree" markdown="1">
<span class="lbl">The disagreement, laid out</span>

**The "it's a myth" side (strong evidence).** Greenhouse "*does not use 'bot' scoring to summarily delete resumes based on keyword density. While Greenhouse does score candidates, human beings do the scoring, not an algorithm.*" Rejections are made by a person filling a **scorecard**, not an algorithm counting words *(FastApply / Jobscan summaries of Greenhouse's mechanism — Appendix §1)*.

**The "it's real, but misunderstood" side.** Workday *can* compute an internal "Match Score" using NLP, "*but does not automatically reject candidates just because they lack a keyword — that is a common myth.*" Recruiters mostly **search and filter** the database by keyword rather than trust a ranked list *(ApplyArc — Appendix §1)*. Note these blog sources are internally inconsistent — one line says "no universal score," the next says recruiters see a ranked list. Treat blog-level parsing specifics as **informed consensus, not vendor fact.**
</div>

**The reconciled takeaway you should act on:** automated *keyword scoring that auto-rejects* is largely a myth at the systems finance actually uses (Greenhouse, Lever, Workday in default config). But keyword *search by recruiters is real and ubiquitous* — so the right words still matter, not because a bot rejects you for missing them, but because a human searching "KYC" or "client onboarding" won't surface you if the phrase isn't there. This is the entire rationale for Section 4: put the real vocabulary of the job on the page so you are *findable*, then let a human make the call.

## 1.4 Where AI/LLM screening actually sits

AI screening is real, but it is **human-in-the-loop**, not an autonomous gatekeeper:

- **Eightfold** (a semantic layer on top of an ATS) ranks candidates by fit using embeddings built on "*1.6 billion career trajectories*," and is explicitly positioned as recommendation: it "*shows why each candidate is recommended so the recruiter and hiring manager can decide.*" *(Eightfold — Appendix §1.)*
- **HireVue** (used widely for finance video interviews) scores *transcribed answers* with NLP against job-related criteria. Critically, HireVue **discontinued facial/visual analysis in January 2021** after bias audits — its own scientist found visual data added "*only about 0.25% of predictive power.*" Current HireVue AI scores **what you say, not your face.** *(Secondary analysis + HireVue platform pages — Appendix §1.)*

## 1.5 The assessments — and the counter-intuitive order

<div class="box note" markdown="1">
<span class="lbl">At big grad schemes, the CV is often NOT the first gate</span>

**PwC** publishes its order as: *Apply online → Online assessment → Video interview → Assessment centre* — with **no CV-review step between apply and the online assessment**. The first real filter is a series of assessments on the SHL platform *(PwC early-careers page — Appendix §1)*. The general pattern: the aptitude/gamified test "*filters out a substantial percentage of applicants before human eyes ever review a CV.*"
</div>

Typical UK finance sequence and providers:

- **Aptitude / situational tests:** SHL, Korn Ferry, Cappfinity (numerical, logical, situational strengths).
- **Gamified tests:** Pymetrics, Arctic Shores — used by PwC, Deloitte, KPMG and financial firms.
- **Video interview:** HireVue (e.g. Barclays: 5–7 questions, ~90s prep, ~2 min answers), Sonru (UBS).

**What this means for you:** at a high-volume scheme, passing the online assessment can matter *before* your CV is ever read. Do not pour weeks into the CV and then fail the numerical test. Budget practice time for SHL/Cappfinity-style tests. Where your CV *is* the first gate — smaller asset managers, off-cycle roles, boutique desks, anything you reach by referral — it carries full weight.

## 1.6 The human screen: 6–7.4 seconds, and it's a rejection filter

When a human finally looks, the first pass is brutally short. The canonical evidence is the **Ladders eye-tracking studies**:

- **2012:** eye-tracking of 30 recruiters found an average initial gaze of **6 seconds**, with 80% of it spent on six data points: **name; current title & company; current dates; previous title & company; previous dates; education** *(Ladders 2012, via Forbes / The Interview Guys — Appendix §1)*.
- **2018:** the updated study found **7.4 seconds** (up from 6, attributed to a tighter labour market). Top CVs used **F- and E-pattern** reading paths with **bold job titles** over bulleted accomplishments; poor ones had "*long sentences, multiple columns, minimal white space*" and keyword stuffing *(Ladders 2018, via HR Dive / CNBC — Appendix §1)*.

<div class="box honest" markdown="1">
<span class="lbl">Reframe the 7-second number</span>

That 7.4 seconds "*was never a measure of how long a recruiter spends reading your qualifications. It's how long they spend deciding whether to keep reading at all*" *(The Interview Guys)*. The scan is a **go/no-go filter.** You design the top third of the page — name, most recent role and employer, and the First — to survive it, so the recruiter chooses to keep reading. (No newer large-scale replication has beaten the 2018 figure; 7.4s remains the cited number.)
</div>

## 1.7 Hard filters vs soft filters

The consensus: **posted grade minimums are mostly *soft* thresholds, enforced as a form question, not a hidden CV scan.** As one widely-cited (US-framed) source puts it: "*Posted minimums are soft thresholds used to discourage applications from candidates clearly below the bar… A candidate at 3.49 from a target school with two internships will not be automatically rejected. A candidate at 3.51 from an unknown school with no finance experience probably will*" *(mergersandinquisitions — Appendix §1)*. Where genuine hard knockouts exist, they are usually **application-form questions** — work authorisation, graduation year, minimum degree class you self-declare — not the parser reading your transcript. **Answer them honestly; your First passes the degree-class question outright.**

## 1.8 The funnel — realistic numbers

<div class="box note" markdown="1">
<span class="lbl">What the competition actually looks like</span>

- UK employers averaged **140 applications per graduate vacancy in 2024** — the highest since ISE records began in 1991. **Financial & professional services: 188 applications per job**, the second-most competitive sector *(ISE Student Recruitment Survey 2024/25 — primary; Appendix §1)*.
- Indicative offer rates (secondary, treat as ballpark): overall IB grad success "*1–2%*"; UBS Graduate Talent Program "*~2–3%*"; Barclays "*below 3%*." An illustrative stage funnel: ~15–20% pass initial screening; ~40–50% of first-round candidates reach the assessment centre *(GetSmartResume / Leon — Appendix §1)*.
</div>

The per-bank raw counts (e.g. "Goldman received X, hired Y") could not be verified — the primary eFinancialCareers article was inaccessible (HTTP 405). Flagged, not guessed.

## 1.9 How off-cycle roles and referrals bypass the funnel

The 188:1 ratio describes the **front door**. There are side doors:

- **Referrals.** A referred applicant's odds of passing the initial review are dramatically higher than a cold applicant's — the widely-repeated framing is "*recruiters spend seconds on a resume; networking gets you the minutes that matter*" *(CFAC/BYU — Appendix §1)*. Crucially, a referral that is a *push* (someone forwards your CV) is weaker than an *advocate* (someone speaks up for you internally) *(r/FinancialCareers "Networking and referrals" — Appendix §1)*.
- **Off-cycle / internships.** These run on smaller applicant pools, lighter automation, and are often read CV-first. For a non-target, an **off-cycle or boutique internship you then lateral from** is a repeatedly-cited route: "*Go to a small shop and cut your teeth. Then lateral up as fast as you can*" *(r/FinancialCareers — Appendix §1)*.
- **Target who reviews.** "*The point of networking is not to get in front of the most senior people — it is to get in front of the people who make recruiting decisions. In many cases that is more junior folks, since partners and MDs are not reviewing resumes*" *(r/FinancialCareers — Appendix §1)*.

**Bottom line for your applications:** treat the front door (online form + assessment) as a filter to *survive*, and the side door (referral, off-cycle, targeted outreach) as where you actually *win*. Section 8 operationalises the side door.
