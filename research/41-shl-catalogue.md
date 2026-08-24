# 41 — SHL: The Firm, Its Expertise, and the COMPLETE Product Catalogue

**Researched:** 2026-08-01 (deep-dive agent, slice 41). All access dates **2026-08-01** unless noted.
**Builds on:** `research/01-shl.md` (Verify item counts/timings, technical-manual figures r=0.77–0.84, T-scores/stens, verification test + Confidence Indicator + Monte Carlo validation, OPQ32r Thurstonian-IRT deep-dive, norm groups, cut-score estimates). **Deliberately not duplicated here.** This file covers the *firm*, the *full catalogue*, and *how the products interlock into a system*.

**Evidence tags:** `[VENDOR]` SHL marketing/site · `[VENDOR-PRIMARY]` SHL technical doc, manual or release note (primary but self-interested) · `[INDEPENDENT]` third party with no SHL commercial stake · `[PREP-VENDOR]` test-prep firm (biased toward "you need practice") · `[INFERRED]` my reasoning · `[UNKNOWN]` gap.

> **Standing caution.** SHL's product names churn constantly — renames, re-bundles, sunsets. A product name that appears only on a prep-vendor page and not on shl.com is *probably legacy*. Conversely a name in SHL release notes but not on the marketing site is *probably new*. Both directions flagged in §5.

---

## 1. THE FIRM

### 1.1 Origins
- Founded **1977** as **Saville & Holdsworth Ltd** (UK), by occupational psychologists Peter Saville and Roger Holdsworth. [VENDOR/INDEPENDENT — Exponent PE portfolio page, "Founded in 1977"; corroborated across SHL's own history messaging]
- Listed as **SHL Group plc** on the LSE before going private in the mid-2000s. [INDEPENDENT — general corporate record] [PARTIAL — exact delisting year not re-verified this pass]
- **Lineage note worth flagging:** Peter Saville subsequently left and founded **Saville Consulting** (Wave personality questionnaire, Swift aptitude range) — a *direct competitor* whose products are routinely confused with SHL's by candidates. Any candidate-facing analysis should keep SHL ≠ Saville Assessment distinct. [INFERRED from well-established industry record — exact departure date [UNKNOWN]]

### 1.2 Ownership chain — **RESOLVED (this was the flagged gap)**

| Period | Owner | Evidence |
|---|---|---|
| 1977 – mid-2000s | Founder-led; SHL Group plc, LSE-listed | [INDEPENDENT] |
| mid-2000s – 2012 | **HgCapital** (PE) — take-private of SHL Group | [INDEPENDENT — corporate record] [PARTIAL, not re-verified] |
| **2012** | **CEB** (Corporate Executive Board) acquires SHL | [INDEPENDENT] |
| **2017** | **Gartner** acquires CEB (~$2.6bn) — SHL transfers with it | [INDEPENDENT] |
| **6 Feb / Mar 2018 → PRESENT (Aug 2026)** | **Exponent Private Equity LLP (London), Fund III — bought SHL from Gartner for US$400m** | **[VENDOR + INDEPENDENT]** |

**→ CURRENT OWNER ANSWER: SHL is owned by Exponent Private Equity (UK mid-market PE firm, London), acquired from Gartner in Feb/Mar 2018 for ~$400m. As of access date 2026-08-01, Exponent's own portfolio page still lists SHL as a live holding with no exit stated — so Exponent remains the owner, ~8.5 years in.** [VENDOR — https://www.exponentpe.com/our-portfolio/shl] + [INDEPENDENT — https://mergr.com/transaction/exponent-private-equity-acquires-shl-group, deal $400m, 6 Feb 2018]

- *Analytical note:* 8+ years is a **long hold** for mid-market PE (typical 3–6 years). This means SHL has been under exit pressure for some time — consistent with the aggressive product-line expansion, AI features and platform migration seen 2023–2026. A sale/IPO is plausible in the near term. [INFERRED — no announced process found; do not state as fact]
- Leadership at acquisition: CEO **Andrew Bradshaw**, Chair **John Moore**. [VENDOR — exponentpe.com] — **current CEO as of 2026: [UNKNOWN]** (shl.com/about did not surface a name).
- Exponent's stated thesis: "the increasing importance of assessments across all areas of the employee lifecycle." [VENDOR]

### 1.3 Bolt-on M&A (shapes the catalogue)
- **SHL-Japan Ltd** taken private (P2P) — the separately-listed Japanese licensee brought in-house. [INDEPENDENT — privsource.com deal record; Nishimura & Asahi (law firm) work page listing "Exponent Private Equity LLP: Acquisition of stock in SHL-Japan Ltd."]
- **Aspiring Minds** acquired (Indian assessment firm; AMCAT battery, *Autoview* automated coding evaluation, SVAR spoken-English engine). [INDEPENDENT — hrkatha.com]
  → **This acquisition is the origin of much of SHL's coding/technical and language-evaluation range.** The presence of **SVAR** in 2025 SHL release notes (§2.7) confirms Aspiring Minds IP is now core SHL product. [INFERRED, well-supported]

### 1.4 Scale and reach
- **"Available in 40+ languages"**, **"Supporting 150 countries"**, **"NPS 95+"**. [VENDOR — https://www.shl.com/about/]
- **"80% of the FTSE 100 and over 50% of the Fortune Global 500"** are customers. [VENDOR — exponentpe.com, echoing SHL's standard line]
- Self-description: "**the largest provider of psychometric and cognitive talent assessment for business globally**." [VENDOR — marketing claim, unverified by any independent market-share study found]
- **Candidates assessed per year: [UNKNOWN]** — the commonly circulated figures (tens of millions/yr) were not confirmed on any SHL page fetched this pass. **Do not cite a number.**
- Employees, revenue, validation-database size in absolute terms: **[UNKNOWN]** (private company; no filings fetched).
- **Catalogue size:** "access to more than **1,000** aptitude, personality, skills, motivation and knowledge assessments" via Talent Central. [VENDOR — SHL Portugal site shl.pt, via search summary; treat the round number as marketing]

### 1.5 Scientific / IO-psychology credentials
- SHL publishes **technical manuals** per instrument (Verify Technical Manual v2.0, Oct 2007 — analysed in `01-shl.md`; OPQ32r Technical Manual lodged in academic repositories). [VENDOR-PRIMARY]
- **BPS (British Psychological Society) test reviews** exist for its flagship instruments — e.g. the OPQ32 BPS Review 2007. [INDEPENDENT-ish — BPS review is an external evaluation, though publisher-commissioned]. EFPA/BPS registration is a genuine differentiator vs. newer US-origin vendors that have no European review. [INFERRED]
- **~70 comparison/norm groups** in the Verify range alone (test type × job level × industry). [VENDOR-PRIMARY — Verify Technical Manual, per 01-shl.md]
- Peer-reviewed contribution: **Bartram (2005), "The Great Eight competencies"** (*Journal of Applied Psychology*) is SHL-authored research and is the empirical backbone of the UCF (§2.4). This is a genuinely cited, independently-reviewed paper — unusual among assessment vendors. [INDEPENDENT — it is a JAP publication, though by an SHL researcher]
- **Notable methodological honesty:** SHL publicly argues that **vendor validity claims (including corrected coefficients) are often exaggerated**, and states it has "historically taken a **conservative approach** to correcting validity coefficients — corrections for range restriction have typically **not** been conducted" because concurrent designs make correction estimates unreliable. [VENDOR-PRIMARY — https://www.shl.com/resources/by-type/blog/2022/talent-assessment-validity-claims-may-be-exaggerated/]
  → This is a real differentiator: most competitors quote *corrected* (inflated) validities. See §4.

---

## 2. THE COMPLETE PRODUCT CATALOGUE

SHL's own top-level taxonomy (from https://www.shl.com/products/ and /products/assessments/) is **six assessment categories**: Behavioral · Personality · Cognitive · Skills & Simulations · Job-Focused · Virtual Assessment & Development Centers — plus Video/Interview, Platform, and Services. [VENDOR]

SHL's **"Featured Products"** shortlist (i.e. what it actually sells hardest) is: **OPQ · Global Skills Assessment (GSA) · Job-Focused Assessments (JFA) · Motivational Questionnaire (MQ) · Situational Judgment Tests (SJT) · SHL Verify · SHL 360.** [VENDOR — /products/]

### 2.1 COGNITIVE — the "Verify" family
- **SHL Verify** — the umbrella cognitive brand, sold as "interactive cognitive assessment" measuring "potential to learn, adapt and perform." [VENDOR — /products/assessments/]
- **Verify G+ / "General Ability Test"** — general mental ability composite. Prep-vendor description: **36 minutes, 30 questions** split 10 numerical / 10 deductive / 10 inductive. [PREP-VENDOR — graduatesfirst.com/aptitude-tests-publishers/shl] ⚠️ **This matches the LEGACY Verify G+ figures in `01-shl.md`, not the Interactive G+ (24Q/36min).** Prep sites conflate the two. See §5.
- **Verify Interactive** — the current, gamified/drag-and-drop range. Confirmed live subtests include **Verify Interactive – Numerical Calculation** (named explicitly in SHL's 15 Oct 2025 release notes as receiving new German and Spanish language versions). [VENDOR-PRIMARY — SHL Release notes, 15 October 2025, v1.0 last updated 13 Nov 2025, https://support.shl.com/documents/1090/attachments/7226] Also **Inductive**, **Deductive**, **Verbal** reasoning. [VENDOR/PREP-VENDOR]
- **Verify Interactive G+** — adaptive composite of the Interactive subtests. [VENDOR — product-catalog view page]
- **SHL Verbal Reasoning Test** — standalone verbal comprehension. [PREP-VENDOR — graduatesfirst] (likely legacy/standalone rather than part of Interactive G+ — see §5)
- Checking / clerical / mechanical-technical tests: exist historically in SHL's range but **were not surfaced on current shl.com pages this pass** → likely folded into "Technical Skills" (§2.6) or legacy. **[UNKNOWN / probably legacy]**

### 2.2 PERSONALITY
- **OPQ — Occupational Personality Questionnaire** (OPQ32, current form **OPQ32r**; also OPQ32i legacy forced-choice-of-4 and OPQ32n normative). Described by SHL/Exponent as "one of the most used personality tests in the world today." Current SHL framing adds it "reveals individual preferences, motivations, and **remote-work capability**" — i.e. the RemoteWorkQ output is now derived from OPQ. [VENDOR — /products/assessments/] · Full mechanics in `01-shl.md`.
- **MQ — Motivational Questionnaire** — measures what energises/de-motivates someone at work (18 motivation dimensions in the classic form). Prep-vendor timing: **~20 minutes**. [VENDOR name confirmed on /products/; timing PREP-VENDOR — graduatesfirst] **Dimension count not re-verified this pass — [PARTIAL].**
- **RemoteWorkQ (RWQ)** — measures self-reported behavioural tendencies for remote-work effectiveness across **three competency areas: Work Relationships · Work Habits · Self-Development & Well-Being**. Prep-vendor timing **~10 minutes**. Has its own **RemoteWorkQ Manager Report** SKU. [VENDOR — shl.com/solutions/products/product-catalog/view/remoteworkq-manager-report/ and /assessments/personality-assessment/shl-remoteworkq-rwq; three-area structure via search summary of SHL/creativeorgdesign pages]
- **ADEPT-15** — 15-facet adaptive personality instrument. Named in `01-shl.md` as SHL-licensed. **It did NOT appear on any current shl.com page fetched this pass** (not in Featured Products, not in the Personality category listing). → **Flag as possibly retired / de-emphasised in SHL's line, or region-specific. [UNKNOWN — needs a direct product-catalog fetch to settle.]** ⚠️ Do not assert it is current.

### 2.3 BEHAVIOURAL / SITUATIONAL
- **SJT — Situational Judgment Tests** — a Featured Product; interactive work scenarios. Customisable and job-tailored; the competency weightings are configured per employer. [VENDOR + INFERRED from 01-shl.md §Role tailoring]
- **GSA — Global Skills Assessment** — a Featured Product under *Behavioral*. Has its own report line: **Global Skills Development Report (relative version)** and **(absolute version)** — confirmed live and receiving new German/Norwegian/US-English versions in the Oct 2025 release. [VENDOR-PRIMARY — SHL Release notes 15 Oct 2025]
  → **The "relative vs absolute" report split is analytically important**: SHL explicitly sells both a *norm-referenced* (relative-to-comparison-group) and a *criterion-referenced* (absolute) view of the same data. [VENDOR-PRIMARY]
- **Realistic Job Previews (RJP)** — scenario-based preview quizzes; a self-selection tool as much as a screen. [PREP-VENDOR — graduatesfirst]
- **JFA — Job-Focused Assessments** — a Featured Product: pre-packaged, role-specific batteries that "measure job-specific competencies" and "predict candidate readiness and fit." [VENDOR — /products/assessments/, /products/]

### 2.4 THE COMPETENCY MODEL — **Universal Competency Framework (UCF)**
*(SHL classifies the UCF as a Behavioral "product", which tells you it is sold, not just used internally.)*
- **Three-tier hierarchy: 8 general competency factors → 20 competency dimensions → 96 component skills.** [VENDOR — https://www.shl.com/products/assessments/behavioral-assessments/universal-competency-framework/]
- The 8 factors are SHL's **"Great Eight"**, derived from Bartram (2005). [INFERRED + INDEPENDENT — the JAP paper]
- Definition used: competencies are "**sets of behaviors that are instrumental in the delivery of desired results**" — deliberately *behavioural*, not knowledge/technical. [VENDOR]
- SHL states the structure "underwent statistical analysis to ensure competencies remain **discrete** across all levels." [VENDOR]
- **APTA™** — a customisable testing tool that maps the UCF to role-relevant competencies; SHL claims an innovation letting it **measure all 96 UCF components in 15 minutes**. [VENDOR — UCF page] ⚠️ 96 constructs in 15 min is an extraordinary claim; treat as marketing until a technical manual is seen.
- Supporting UCF materials shipped to clients: questionnaire items, **behavioural anchors**, **interview questions**, and **assessment-centre exercises** — i.e. the same framework instantiated in every modality. [VENDOR] ← **this is the key systems fact, see §3.**
- Validity framing: rests on "empirical evidence and extensive scientific research highlighting the most valid predictors of performance across roles"; cites **Aberdeen Strategy and Research** that orgs using a consistent competency model across acquisition/learning/performance/succession are "**five times as likely to achieve best-in-class performance**." [VENDOR quoting a third-party analyst firm — this is a *business* claim, not a psychometric one; do not present as validity evidence]

### 2.5 SKILLS & SIMULATIONS
- **Coding Simulations** — "AI-powered coding challenges." [VENDOR — /products/ Skills & Simulations; PREP-VENDOR corroborates]
- **Technical Skills assessments** — multiple-choice, prep-vendor timing ~15 min. [VENDOR name; timing PREP-VENDOR]
- **Business Skills assessments** — Microsoft Office / computer literacy. [VENDOR + PREP-VENDOR]
- **Call Center / Contact Centre Simulations** — customer-service environment simulation. [VENDOR]
- **Language Evaluation** — AI-scored language proficiency. Its engine is almost certainly **SVAR** (spoken-English automated evaluation, ex-Aspiring Minds), which is named as a live, *asynchronously scored* SHL assessment in the Oct 2025 release notes. [VENDOR + VENDOR-PRIMARY release notes; the SVAR↔Language-Evaluation link is INFERRED]

### 2.6 VIDEO & INTERVIEW
- **Smart Interview On Demand (SIOD)** — asynchronous/recorded video interview, optional AI scoring. Confirmed live in Oct 2025 release notes as one of three "asynchronously scored assessments." [VENDOR + VENDOR-PRIMARY]
- **Smart Interview Live** — real-time video interview. [VENDOR — product-catalog view page]
- **Smart Interview Live Coding** — live technical interview with an in-browser compiler; prep-vendor says **50+ programming languages**. [VENDOR + PREP-VENDOR]
- **Smart Interview Professional (SIP)** — **explicitly called "SHL's flagship interview product"** in the Oct 2025 release notes, and the focus of most 2025 development. [VENDOR-PRIMARY — release notes]
  Confirmed 2025 SIP features: **SSO authentication for interviewers**, interview-link-forwarding controls, **self-scheduling** with slot-selection statuses and bulk actions, **Interviewer Analytics dashboard** (PNG export), a **2-level vs 3-level Skill Framework toggle** (Category → Topic → Subtopic) applied across guides/scorecards/reports, **AI skill recommendations generated from an uploaded job description**, **O*NET job mapping** (or custom job family/role/level framework), and **candidate snapshot capture at 120-second intervals during interviews, shown on the report** (company-configurable). [VENDOR-PRIMARY — release notes 15 Oct 2025, availability 21 Jul 2025, TalentCentral+ only]
  ⚠️ **The 120-second snapshot capture is a first-party confirmation of image-based proctoring inside interviews** — a rare primary-source confirmation of the kind of monitoring `01-shl.md` could only source to prep-vendors. It is **opt-in per company**, which supports the caution flag in `01-shl.md` that monitoring is employer-configured, not universal.
- **AI Screener (SIA)** — a distinct, asynchronously-scored SHL assessment named alongside SVAR and SIOD. [VENDOR-PRIMARY — release notes] **Product details [UNKNOWN]** — appears to be an AI-scored screening interview/response product. **New-ish; not on the main marketing pages fetched.**
- **Video Feedback** — "personalized feedback to every candidate." [VENDOR — /products/]

### 2.7 ASSESSMENT CENTRES
- **Virtual Assessment and Development Centers (VADC)** — a full catalogue SKU and its own assessment category; integrates multiple exercise types virtually. Also offered as an **Outsourced Assessment** service. [VENDOR — /products/product-catalog/view/virtual-assessment-and-development-centers/ and /products/ Services list]

### 2.8 MULTI-RATER / DEVELOPMENT
- **SHL 360** — multi-rater/360 feedback; a Featured Product, and **"360/MFS" is a distinct platform** in SHL's own release-note platform matrix (alongside TalentCentral, TalentCentral+, SHL Apps, Insights). [VENDOR + VENDOR-PRIMARY]

### 2.9 PLATFORM
SHL's release notes tick-box matrix reveals the **actual live platform estate**: `TalentCentral™` · `TalentCentral+™` · `360/MFS` · `SHL Apps` · `Insights`. [VENDOR-PRIMARY — release notes 15 Oct 2025] This is the single best evidence of what SHL's platform line really is.
- **TalentCentral** — the legacy/incumbent delivery + reporting hub. Still receiving content updates (new language versions of Verify Interactive, GSA reports, OPQ reports) in Oct 2025 — i.e. **maintained, but new *features* go to TC+ only**. [VENDOR-PRIMARY — in the Oct 2025 notes, both new features were marked TalentCentral+ ☒ / TalentCentral ☐]
- **TalentCentral+ (TC+)** — the current-generation platform; **all 2025 feature work lands here**. Sign-in/SSO, candidate scores, reports, Excel data extracts. [VENDOR-PRIMARY]
  → **Strong inference: TalentCentral is being sunset in favour of TalentCentral+.** [INFERRED — well-supported by the release-note pattern; not stated by SHL]
- **Insights** — analytics platform. [VENDOR-PRIMARY, name only] **[UNKNOWN details]**
- **SHL Apps** — [VENDOR-PRIMARY, name only] **[UNKNOWN details]**
- Platform capability claim: access to "**more than 1,000** aptitude, personality, skills, motivation and knowledge assessments" through a single login; "integration with ATS, CRM, ERP and HR platforms." [VENDOR — shl.pt]
- **Mobilize** — named in the research brief; **NOT found on any SHL page this pass. [UNKNOWN — possibly retired or renamed.]** Do not assert.
- **shldirect.com / www2.shl.com/shldirect** — the candidate-facing practice portal (practice tests, assessment advice, accessibility support). [VENDOR — confirmed in `01-shl.md`]

### 2.10 ATS INTEGRATIONS
- **"SHL Integrates with Over 80 Applicant Tracking Systems."** [VENDOR — https://www.shl.com/solutions/services/ats-integrations/]
- Named partners with dedicated integration pages: **Workday · SmartRecruiters · Oracle (Gold Partner) · Cornerstone · iCIMS · ADP · Jobvite · Simplify.hr**. Logos additionally shown for **UKG · TeamTailor · SnapHire · PageUp · PeopleFluent · Oleeo · SAP**. [VENDOR]
- Integration promise: assessment delivery, results and candidate communications flow **directly into the ATS**, "eliminating manual handoffs and fragmented data." [VENDOR/INDEPENDENT-summary]

### 2.11 SERVICES (non-product revenue)
Managed Services · Training Services · **SHL Certification (OPQ / Verify)** · Outsourced Assessments (VADC) · Talent Management Consulting. [VENDOR — /products/]
→ **The OPQ/Verify certification business is strategically important**: it creates a population of client-side HR staff professionally credentialed *in SHL's instruments specifically*, which is a switching cost. [INFERRED]

---

## 3. HOW THE PRODUCTS LINK TOGETHER — SHL SELLS A SYSTEM, NOT TESTS

This is the analytical core. Five mechanisms:

**(a) The UCF is the connective tissue — one construct language across every modality.**
The UCF's 8 factors / 20 dimensions / 96 skills is not just a taxonomy SHL uses internally; SHL *ships* it as questionnaire items, **behavioural anchors**, **interview questions** and **assessment-centre exercises**. [VENDOR — UCF page] That means an OPQ scale, an SJT scenario, an interviewer's scorecard rating and an assessment-centre exercise observation can all be expressed on **the same competency axis**. The consequence: SHL can aggregate radically different measurement methods into one profile — which no single test could do, and which is the thing a client is actually buying.

**(b) Job-Focused Assessments are the packaged composite.**
JFAs are the retail form of the system: pre-built, role-specific bundles that "predict candidate **readiness and fit**." [VENDOR] SHL's own framing — "SHL defines the required skills for each specific role and assesses each candidate's ability and potential to perform at the highest level using objective data … with Job Focused Assessments to predict candidate readiness and fit" — is explicitly a **competency-profile-matching** model: define the role's competency requirement in UCF terms, measure the candidate on the same terms, score the *distance*. [VENDOR]

**(c) Scoring is relative, not absolute — and that is a design commitment.**
"The Talent Central Platform does not rank candidates based on absolute score but rather on **relative score** … graded according to how well they performed compared to past test-takers." [PREP-VENDOR — jobtestprep/talent-central-assessment; but consistent with the norm-group architecture and the ~70 comparison groups documented in `01-shl.md`] SHL nonetheless now sells **both** views for GSA: a *relative* and an *absolute* Development Report. [VENDOR-PRIMARY — Oct 2025 release notes] So the norm group choice — the employer's choice — is a load-bearing part of every score.

**(d) Multi-hurdle vs compensatory.**
- SHL's *architecture* is fundamentally **compensatory within an instrument** (Verify G+ combines sub-abilities into one composite; UCF rolls 96 skills up into 20 dimensions into 8 factors — each level a weighted aggregation). [INFERRED from the stated hierarchy]
- But **across the funnel it is multi-hurdle**, because the products are sequenced as gates in an ATS-integrated workflow: sift assessment → verification test → SJT/JFA → Smart Interview → VADC. The **verification test** is a pure hurdle (Verified / Not Verified, not a score) [VENDOR-PRIMARY, per `01-shl.md`], and the ATS integration exists precisely to automate stage advancement.
- **SHL does not publish which model any given employer uses — the employer configures it.** [INFERRED, consistent across sources] **Do not claim a universal SHL cut-score rule.**
- **The clearest primary evidence of "system" thinking: the Smart Assessment Workflow (response reuse).** From 14 Aug 2025, if a candidate has completed **SVAR, Smart Interview On Demand or AI Screener (SIA)** and is re-invited within a defined window (e.g. 30 days), the assessments show as already complete and **the prior scores are copied into the new attempt** for the recruiter. Synchronously-scored assessments have prior *responses* copied and re-scored in real time; asynchronously-scored ones have the *score* copied directly. Manual evaluation scores are never reused. Proctoring data and prior responses do not carry into the new report. [VENDOR-PRIMARY — release notes 15 Oct 2025, TalentCentral+ only]
  → **Analytical significance: a candidate's SHL result can follow them across applications within the same client.** This is a portable-score architecture, and it is a strong argument that SHL is building a *candidate record*, not a series of tests.

**(e) TalentCentral+ is the hub that makes it one product.**
Single login, 1,000+ assessments, reports, Excel data extracts, 80+ ATS integrations, and now SSO. [VENDOR + VENDOR-PRIMARY] The platform — not any individual test — is the moat and the renewal.

---

## 4. SHL'S OWN CLAIMED VALIDITY / SCIENCE

- **SHL's public position is unusually conservative and is itself a marketing weapon.** Its 2022 blog *"Talent Assessment Validity Claims May be Exaggerated"* states: SHL "has historically taken a conservative approach to correct validity coefficients. **Corrections for range restriction have typically not been conducted**" — because concurrent validation designs make accurate correction estimates difficult; and that its "technical manuals contain all information necessary to evaluate validity calculations and any statistical corrections." [VENDOR-PRIMARY — https://www.shl.com/resources/by-type/blog/2022/talent-assessment-validity-claims-may-be-exaggerated/]
- **Companion whitepaper:** *Guidance for the Interpretation of Validity Coefficients* — written to help buyers "evaluate vendor claims," noting "the level of the relationship between assessment scores and job performance is often **overestimated**." [VENDOR-PRIMARY — https://www.shl.com/resources/by-type/whitepapers-and-reports/guidance-for-the-interpretation-of-validity-coefficients/ ; PDF at https://www.shl.com/assets/premium-content/guidance-for-the-interpretation-of-validity-coefficients-en.pdf] **PDF not text-extracted this pass — [GAP, worth a follow-up fetch].**
- On the **2022 Sackett et al. re-analysis** (which revised corrected GMA validity down from ~0.51 toward ~0.31), SHL's stated position is that its conclusions "are **unlikely to impact our own validation study results or meta-analyses**" — precisely *because* SHL reports largely uncorrected figures. [VENDOR-PRIMARY] **This is a defensible position, and a genuine differentiator, but note it is also a convenient one.** [INFERRED]
- **Published coefficients:** SHL does **not** put headline validity numbers on its blog; it routes readers to per-instrument technical manuals. The only hard reliability figure secured across this project remains **Verify internal consistency 0.77–0.84** (per `01-shl.md`). **A specific published SHL criterion-validity coefficient was NOT obtained this pass — [GAP].**
- **CONFLICT TO NOTE BOTH WAYS:** a third-party comparison site (clarity-hire.com, "Criteria Corp vs SHL") asserts SHL and Criteria "land in roughly the same validity band — **0.50 corrected, somewhere in the 0.30s uncorrected**." [INDEPENDENT-ish, but a commercial comparison blog of unknown rigour] ⚠️ **This directly contradicts SHL's own claim not to correct for range restriction.** Treat the 0.50 as *not* SHL-sourced. Do not attribute it to SHL.
- **Validation database:** the same source describes "hundreds of studies, many large samples, deployed across dozens of countries," with SHL's largest studies concentrated in **financial services, consulting, and oil & gas**. [INDEPENDENT-ish, unverified — the finance concentration is highly relevant to this project but needs a better source before use]
- **Fairness / AI / NYC LL144:** **No SHL bias-audit publication, adverse-impact study, or LL144 AEDT posting was found this pass. [UNKNOWN — remains an open gap.]** Note the regulatory context is real: LL144 has been in force since July 2023, requires an **independent** bias audit of automated employment decision tools, and the practical benchmark is the EEOC four-fifths (0.80) impact-ratio rule. [INDEPENDENT — Deloitte, IAPP, DCI Consulting summaries] ⚠️ *SHL's absence from these results is not evidence of absence* — LL144 audits are typically posted by the **employer**, not the vendor. [INFERRED]
- **On facial/emotion analysis:** `01-shl.md` flags SHL marketing claiming Smart Interview On Demand could score "facial expressions, voice tonality, body language." **This pass found no current SHL page repeating that claim**, and the 2025 SIP feature set is built on **skill/topic frameworks, scorecards and O*NET job mapping** — i.e. *content*-based structured evaluation, not affect analysis. [VENDOR-PRIMARY — release notes] → **Weak-to-moderate evidence SHL has quietly moved away from facial/body-language scoring, consistent with the post-2021 industry retreat. NOT CONFIRMED — do not state as fact. [PARTIAL]**

---

## 5. CURRENT vs LEGACY / RETIRED

**Confirmed CURRENT (primary evidence, 2025–26):**
- TalentCentral+ (all new features land here) · Smart Interview Professional ("flagship") · Smart Interview On Demand · SVAR · AI Screener (SIA) · Verify Interactive (Numerical Calculation confirmed by name) · Global Skills Assessment + its relative/absolute Development Reports · OPQ reports incl. **HiPo Assessment Report** and **Unlocking Potential Report** · 360/MFS · Insights · SHL Apps. [VENDOR-PRIMARY — SHL Release notes 15 Oct 2025]
- Smart Assessment Workflow (response reuse) — live from **14 Aug 2025**. [VENDOR-PRIMARY]
- SIP feature wave — live from **21 Jul 2025**. [VENDOR-PRIMARY]

**Being wound down / de-emphasised:**
- **TalentCentral (classic)** — receives only content/localisation updates; **zero new features** in the Oct 2025 release, both of which were TC+-only. [INFERRED, well-supported by primary evidence]
- **Legacy Verify G+ (30 questions / 36 min, button-click)** vs **Verify Interactive G+ (24 questions / 36 min, adaptive, drag-and-drop)** — prep vendors (incl. graduatesfirst, accessed 2026-08-01) still describe the **30-question legacy form as if current**. This is the single most common candidate-facing error. [PREP-VENDOR error, identified by cross-check against `01-shl.md`]
- **Standalone SHL Verbal Reasoning** — still described by prep vendors; verbal is *not* among the confirmed Verify Interactive G+ sub-abilities (Numerical/Inductive/Deductive). Likely a separate legacy/standalone product. [INFERRED]
- **Checking / clerical / mechanical tests** — absent from current SHL pages. [UNKNOWN, probably legacy]

**Named in the brief but NOT FOUND on current SHL properties this pass — treat as unverified:**
- **ADEPT-15** — no current shl.com presence found. [UNKNOWN]
- **Mobilize** — no presence found. [UNKNOWN]
- "Smart Assessments" as a *product* — note the confirmed term is **"Smart Assessment Workflow"**, a *platform feature* (response reuse), **not a product family**. [VENDOR-PRIMARY] ⚠️ Correct this if the project has it as a product.

---

## 6. RESIDUAL GAPS
1. Current CEO of SHL (2026). [UNKNOWN]
2. Candidates assessed per year — **no number confirmed; do not cite one**.
3. ADEPT-15 and Mobilize: current, renamed, or retired? Needs a direct fetch of the full product-catalog index (which 301-redirects to /products/ and did not enumerate).
4. A specific **published SHL criterion-validity coefficient** — the *Guidance for the Interpretation of Validity Coefficients* PDF was located but not extracted.
5. Any SHL bias audit / adverse-impact publication / LL144 AEDT notice. Nothing found.
6. SHL's *current explicit* written stance on facial/emotion analysis in video interviews (only indirect evidence obtained).
7. MQ dimension count and current form; UCF "Great Eight" factor names not enumerated this pass.
8. HgCapital 2006 take-private year not re-verified.
9. Full text of the 15 Oct 2025 release-note product-availability tables beyond p.13–14 (Verify/GSA/OPQ report SKUs only partially captured).

---

## 7. KEY SOURCES (all accessed 2026-08-01)
**SHL primary / vendor**
- SHL Release notes, 15 October 2025 (v1.0, last updated 13 Nov 2025) — **best single primary source in this file** [VENDOR-PRIMARY]: https://support.shl.com/documents/1090/attachments/7226 *(PDF; text-extracted via pdftotext)*
- SHL products index [VENDOR]: https://www.shl.com/products/
- SHL assessments index [VENDOR]: https://www.shl.com/products/assessments/
- SHL Universal Competency Framework [VENDOR]: https://www.shl.com/products/assessments/behavioral-assessments/universal-competency-framework/
- SHL About [VENDOR]: https://www.shl.com/about/
- SHL ATS Integrations [VENDOR]: https://www.shl.com/solutions/services/ats-integrations/
- SHL blog — "Talent Assessment Validity Claims May be Exaggerated" (2022) [VENDOR-PRIMARY]: https://www.shl.com/resources/by-type/blog/2022/talent-assessment-validity-claims-may-be-exaggerated/
- SHL whitepaper — Guidance for the Interpretation of Validity Coefficients [VENDOR-PRIMARY, **not yet extracted**]: https://www.shl.com/assets/premium-content/guidance-for-the-interpretation-of-validity-coefficients-en.pdf
- SHL RemoteWorkQ Manager Report [VENDOR]: https://www.shl.com/solutions/products/product-catalog/view/remoteworkq-manager-report/
- SHL Smart Interview Live [VENDOR]: https://www.shl.com/solutions/products/product-catalog/view/smart-interview-live/
- SHL Smart Interview Live Coding [VENDOR]: https://www.shl.com/products/product-catalog/view/smart-interview-live-coding/
- SHL Virtual Assessment and Development Centers [VENDOR]: https://www.shl.com/products/product-catalog/view/virtual-assessment-and-development-centers/
- ⚠️ https://www.shl.com/products/product-catalog/ **301-redirects to /products/** — the enumerable catalogue index is gone from the public site.

**Ownership / corporate**
- Exponent Private Equity — SHL portfolio page (SHL still listed, no exit) [VENDOR]: https://www.exponentpe.com/our-portfolio/shl
- Mergr — Exponent Private Equity acquires SHL Group, $400m, 6 Feb 2018 [INDEPENDENT]: https://mergr.com/transaction/exponent-private-equity-acquires-shl-group
- PrivSource — SHL to acquire SHL Japan (P2P) [INDEPENDENT]: https://www.privsource.com/acquisitions/deal/shl-to-acquire-shl-japan-in-public-to-private-p2p-deal-gaSNm0
- Nishimura & Asahi — Exponent/SHL-Japan stock acquisition [INDEPENDENT]: https://www.nishimura.com/en/experience/work/92824
- HRKatha — SHL acquires Aspiring Minds [INDEPENDENT]: https://www.hrkatha.com/news/merger-acquisition/shl-acquires-aspiring-minds/
- PitchBook SHL Group profile [INDEPENDENT, paywalled]: https://pitchbook.com/profiles/company/11400-76

**Regulatory context**
- Deloitte — NYC Local Law 144-21 and Algorithmic Bias [INDEPENDENT]: https://www.deloitte.com/us/en/services/audit-assurance/articles/nyc-local-law-144-algorithmic-bias.html
- IAPP — Practical considerations for bias audits under NYC LL144 [INDEPENDENT]: https://iapp.org/news/a/practical-considerations-for-bias-audits-under-nyc-local-law-144
- DCI Consulting — NYC AEDT bill [INDEPENDENT]: https://www.dciconsult.com/nyc-automated-employment-decision-tools-bill
- arXiv — "Null Compliance: NYC Local Law 144 and the Challenges of Algorithm Accountability" [INDEPENDENT, academic]: https://arxiv.org/html/2406.01399v1

**Prep-vendor (biased — use only where corroborated)**
- GraduatesFirst — SHL publisher guide [PREP-VENDOR]: https://www.graduatesfirst.com/aptitude-tests-publishers/shl
- JobTestPrep — Talent Central Assessment [PREP-VENDOR]: https://www.jobtestprep.com/talent-central-assessment
- ClarityHire — Criteria Corp vs SHL validity [INDEPENDENT-ish, commercial, unverified]: https://clarity-hire.com/blog/criteria-corp-vs-shl-validity-research
