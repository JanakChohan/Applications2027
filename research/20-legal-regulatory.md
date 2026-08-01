# 20 — Legal & Regulatory Framework (UK candidate) — Raw Research Notes

**Researched:** 2026-08-01 (main thread, direct). **Feeds:** cross-cutting §6.7 + per-provider §5.11.
**Evidence tags:** `[REGULATORY]` official/statutory · `[INDEPENDENT]` reputable legal analysis · `[INFERRED]` reasoning shown · `[UNKNOWN]` say why.
**Access date for ALL URLs below:** 2026-08-01.

> **ANALYST HEADLINE / MISCONCEPTION WARNINGS (read first):**
> 1. **UK Article 22 is NO LONGER the live provision.** The Data (Use and Access) Act 2025 ("DUAA") **replaced** Art. 22 with new **Arts 22A–22D**, in force **5 February 2026**. The framework flipped from *general prohibition* to *permitted-with-safeguards*. Any guide text citing "Article 22 bans automated hiring decisions" is now **out of date**. See §2.
> 2. **The EU AI Act's high-risk recruitment rules are NOT yet in force.** The original 2 Aug 2026 date for Annex III high-risk systems was **pushed to 2 December 2027** by the "Digital Omnibus" (Council final approval 29 June 2026). So as of the 2026 application window this book targets, EU-side hiring-AI obligations are still **pending**. See §4.
> 3. **The UK has NO "four-fifths / 80% rule."** That is a *US* (EEOC/UGESP) construct. UK adverse-impact challenges run through **indirect discrimination (Equality Act s.19)** with a **proportionate-means-of-a-legitimate-aim** justification defence — no fixed numerical trigger. Do not import the 80% rule into UK advice. See §3 + §7.
> 4. **"Solely automated" is a high bar and rarely met in real graduate sifts.** Most banks keep a human in the funnel somewhere, which is often enough to take a decision *out* of the strict solely-automated regime — but DUAA now also regulates *partly* automated significant decisions less strictly. Precision matters. See §2.

---

## 1. UK GDPR ARTICLE 15 — RIGHT OF ACCESS / DSAR (§6.7, §5.11 template core)

**What it is.** Art. 15 UK GDPR + Data Protection Act 2018 give any individual the right to (a) confirmation you are processing their data, (b) a **copy** of that personal data, and (c) supplementary info (purposes, recipients, retention, source, existence of automated decision-making + meaningful info about the logic). `[REGULATORY]` ICO, *Right of access* (summarised via search of ico.org.uk right-of-access hub — direct fetch 403'd on 2026-08-01). https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/right-of-access/

**Deadline — ONE MONTH.** Controller must respond "without undue delay and **at the latest within one month**" of receipt. Extendable by **up to two further months** for complex/numerous requests, but the controller must **tell the applicant of the extension + reasons within the first month**. `[REGULATORY]` ICO, *Time limits for responding to data protection rights requests*. https://ico.org.uk/for-the-public/time-limits-for-responding-to-data-protection-rights-requests/
- **DUAA 2025 "stop the clock":** the response clock now **pauses** where the controller has reasonably asked the applicant for ID verification or clarification, resuming when they reply. `[REGULATORY/INDEPENDENT]` gov.uk DUAA factsheet (UK GDPR & DPA). https://www.gov.uk/government/publications/data-use-and-access-act-2025-factsheets/data-use-and-access-act-factsheet-uk-gdpr-and-dpa
- DUAA also **codifies** that the controller's search need only be **"reasonable and proportionate"** (reflecting existing case law) — a mild narrowing of scope, not a new refusal ground. `[REGULATORY]` same gov.uk factsheet.

**Cost — FREE.** No fee for a DSAR in the ordinary case. A controller may charge a "reasonable fee" or refuse **only** where the request is **manifestly unfounded or excessive** (e.g., repetitive). `[REGULATORY]` ICO right-of-access hub (search summary, 2026-08-01). Burden is on the controller to show it is excessive.

**Who is the CONTROLLER (candidate vs employer vs vendor)?** `[INFERRED — legally reasoned]`
- The **employer** (the bank/firm) is almost always the **data controller** for the hiring decision — they decide purposes/means.
- The **assessment vendor** (SHL, Aon, HireVue, Arctic Shores, etc.) is typically a **processor** acting on the employer's instructions — BUT vendors often become **joint/independent controllers** for their own norming, validation, model-training and product-improvement uses. `[INFERRED]` from the controller/processor test; exact status is contract-specific and usually undisclosed → **template should send the DSAR to the employer first**, and separately to the vendor if the employer points there. `[UNKNOWN — per-deal]`.
- Practical: send the DSAR to the **employer's DPO / privacy team** (privacy@firm). They must either answer or route to the processor.

**WHAT A CANDIDATE CAN / SHOULD SPECIFICALLY REQUEST (put in the §5.11 template):** `[INFERRED from Art.15 scope + [INDEPENDENT] recruitment-SAR analysis]`
- Raw and scaled **scores** for each test/section; the **percentile / sten / band**;
- The **norm group** the score was compared against (e.g., "UK Graduate Finance");
- Any **cut-score / threshold** applied and whether you were above/below it;
- **Proctoring / integrity flag logs**: flag events, similarity/plagiarism scores, "suspicious behaviour" markers, IP/device logs;
- **Video/footage & audio** of any webcam-proctored or async video interview, plus any **AI-derived analysis** (competency ratings, keyword/transcript scoring);
- **Automated decision-making disclosure**: whether an automated decision/sift was applied, **meaningful information about the logic**, and the **significance/consequences** (Art. 15(1)(h));
- **Human involvement**: whether a human reviewed the decision and at what stage;
- Recipients (who inside the firm / which vendor saw it) and **retention period**.
- **Redaction caveat:** controller may redact **third-party** personal data (e.g., other candidates' scores, assessor identities where their rights outweigh yours) and must **explain what was withheld and why**. `[INDEPENDENT]` recruitment-SAR analysis (Clyde & Co / ICO employer Q&A, via search 2026-08-01). https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/subject-access-request-q-and-as-for-employers/ (direct fetch 403'd; content from ICO/Clyde&Co search summaries).
- **Trade-secret caveat:** vendors resist disclosing the *underlying algorithm/item bank*. Art. 15 requires **meaningful info about the logic**, NOT the source code or proprietary scoring formula. Expect a high-level description, not the model. `[INFERRED]`.

---

## 2. AUTOMATED DECISION-MAKING — OLD ART. 22 → NEW ARTS 22A–22D (DUAA 2025) (§6.7 flagship, §5.11)

### 2a. The OLD regime (pre-5 Feb 2026) — for historical framing only
- Old **Art. 22(1)**: individuals had the right **not to be subject to a decision based *solely* on automated processing** (incl. profiling) producing **legal effects or similarly significantly affecting** them. Default = **prohibition** unless (a) necessary for a contract, (b) authorised by law, or (c) explicit consent; plus safeguards. `[REGULATORY/INDEPENDENT]` ICO ADM page + LegalVision. https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/individual-rights/individual-rights/rights-related-to-automated-decision-making-including-profiling/ ; https://legalvision.co.uk/data-privacy-it/article-22-uk-gdpr/
- ICO's own worked example of a "similarly significant effect": **"e-recruiting practices without any human intervention."** `[REGULATORY]` ICO ADM page (search summary 2026-08-01). → This is the hook that made a **fully-automated CV/OA sift** potentially engage Art. 22.
- "**Solely**" = "totally automated with **no meaningful human influence** on the outcome." A human who merely rubber-stamps or only feeds in data does **not** make it non-solely. `[REGULATORY]` ICO ADM guidance (via Handley Gill summary of ICO position). https://www.handleygill.co.uk/handley-gill-blog/section-80-data-use-and-access-act-2025-article-22a-uk-gdpr-automated-decision-making-automated-processing-meaningful-human-involvement

### 2b. The CURRENT regime — DUAA 2025 s.80 inserts Arts 22A–22D, **in force 5 February 2026** `[REGULATORY]`
Source: Data (Use and Access) Act 2025 c.18 s.80 (legislation.gov.uk direct fetch 503'd on 2026-08-01; provisions below corroborated across gov.uk factsheet + Travers Smith + Bratby + Handley Gill).
- **legislation.gov.uk:** https://www.legislation.gov.uk/ukpga/2025/18/section/80 (503 on fetch — retry recommended in gap audit) and Part 5 Ch.1 ADM crossheading https://www.legislation.gov.uk/ukpga/2025/18/part/5/chapter/1/crossheading/automated-decisionmaking
- **PHILOSOPHICAL FLIP:** default moves from **prohibition** → **permission with safeguards**. Solely automated **significant decisions** are now **allowed for ordinary personal data**, provided the required safeguards are in place. `[REGULATORY]` gov.uk factsheet; `[INDEPENDENT]` Travers Smith, *UK's data protection reforms take effect — a new era for automated decision-making*. https://www.traverssmith.com/knowledge/knowledge-container/uks-data-protection-reforms-take-effect-a-new-era-for-automated-decision-making/
- **"Significant decision"** = a decision that produces a **legal effect** or **similarly significant effect** for the data subject (concept carried over; recruitment sift plausibly qualifies). `[REGULATORY/INDEPENDENT]`.
- **"Based solely on automated processing"** = **no meaningful human involvement**. Art. 22A defines by reference to meaningful human involvement; the Secretary of State may make regulations on what counts. `[REGULATORY]` s.80/Art.22A; `[INDEPENDENT]` Handley Gill.
- **REQUIRED SAFEGUARDS (Art. 22C) — the four the candidate can invoke:** the controller must provide measures that (1) give the data subject **information** about significant automated decisions taken about them; (2) enable them to **make representations**; (3) enable them to **obtain human intervention** from the controller; (4) enable them to **contest** the decision. `[REGULATORY]` gov.uk factsheet + s.80. → **These four map directly onto the §5.11 "I was auto-rejected" escalation template.**
- **SPECIAL CATEGORY DATA (Art. 22B) — stricter:** solely automated significant decisions based **wholly or partly on special-category data** (Art. 9 — e.g., health, disability inferences, race, biometric) remain **prohibited** unless an Art. 9 condition applies **AND** the safeguards are met **AND** (broadly) consent or substantial-public-interest basis. `[REGULATORY/INDEPENDENT]` Travers Smith + Handley Gill. → Relevant where **video/biometric or personality inference could touch health/disability**.
- **"Meaningful human involvement"** — pre-DUAA ICO benchmarks (still the working standard pending new ICO guidance): reviewer must have **authority + competence to override**, actually **weigh/interpret** the recommendation before implementation, have access to **all relevant data**, and not be **disincentivised from disagreeing**; decisions should be **logged/monitored**. `[REGULATORY]` ICO (via Handley Gill).

### 2c. STATUS / UNCERTAINTY FLAGS
- `[UNKNOWN — live]` The **ICO has not yet finalised** updated ADM guidance reflecting DUAA. ICO launched a **consultation on draft ADM & profiling guidance in early 2026**; final guidance + any Secretary-of-State regulations on "meaningful human involvement" **were still pending as of 2026-08-01**. `[INDEPENDENT]` Bird & Bird, *ICO launches consultation on draft guidance on ADM and profiling* (2026). https://www.twobirds.com/en/insights/2026/ico-launches-consultation-on-draft-guidance-on-automated-decision-making-and-profiling → **State the current position but flag that the detailed standard may shift.**
- `[INFERRED]` **How a fully-automated grad sift engages the regime NOW:** if a bank auto-scores an OA and **auto-rejects below a cut-score with no human looking**, that is a *solely automated significant decision* → it is **lawful under the new regime IF** the firm provides the four safeguards (notice + representations + human intervention + contest). The candidate's practical lever is therefore **"invoke the Art. 22C safeguards: I want human review of my auto-rejection."** If special-category data was involved, add the Art. 22B argument (likely unlawful without an Art. 9 basis).

---

## 3. EQUALITY ACT 2010 — REASONABLE ADJUSTMENTS + INDIRECT DISCRIMINATION (§6.7, §5.11) `[REGULATORY]`

### 3a. Duty to make reasonable adjustments (ss. 20–21, Sch. 8)
- Employer duty to make **reasonable adjustments** for **disabled** applicants/employees. Triggered where a **PCP** (provision, criterion or practice), a **physical feature**, or **lack of an auxiliary aid** puts a disabled person at a **substantial disadvantage** vs non-disabled people. `[REGULATORY/INDEPENDENT]` Equality Act 2010 ss.20–21; Michelmores, *What are 'reasonable adjustments' in the recruitment process?*. https://www.michelmores.com/commercial-litigation-insight/what-are-reasonable-adjustments-recruitment-process/
- **An online timed test IS a PCP.** Worked example: "a policy requiring all applicants to complete an online test within 30 minutes" is a PCP capable of disadvantaging disabled candidates. `[INDEPENDENT]` Michelmores.
- **Typical assessment adjustments:** **extra time** (commonly +25%, but no statutory figure — reasonableness is fact-specific `[INFERRED]`); alternative format (e.g., short written answers instead of MCQ, or vice-versa); screen-reader-compatible / dyslexia-friendly format; rest breaks; removing/replacing a gamified element; assessor briefing for autistic candidates; skip webcam proctoring where it disadvantages. `[INDEPENDENT]` Michelmores (dyslexia extra-time + Asperger's alternative-format examples).
- **KNOWLEDGE trigger:** duty bites once the employer **knows or ought reasonably to know** the person is disabled and likely disadvantaged. → **candidate should disclose + request early** to fix knowledge. `[REGULATORY]`.
- **s.60 pre-offer health questions:** employers generally **must NOT ask about health/disability before a job offer**, **EXCEPT** (among narrow exceptions) **to establish whether a reasonable adjustment is needed for an assessment**. So the recruiter's "do you need adjustments for the test?" question is the lawful channel. `[REGULATORY/INDEPENDENT]` s.60; Michelmores.
- **COST/who pays:** employer bears the cost of the adjustment (cannot pass to candidate). `[REGULATORY]`.

### 3b. Anticipatory vs reactive — an important nuance to get right `[INDEPENDENT]`
- In the **employment field** the reasonable-adjustment duty is generally **reactive** — it arises in relation to a particular disabled applicant, NOT a blanket anticipatory duty to pre-equip for every possible disability. `[INDEPENDENT]` Michelmores; ico/gov guidance.
- BUT **service providers** (Part 3 EqA) owe an **anticipatory** duty (must design accessible services *before* being asked). **Recruitment agencies / assessment providers** can fall to be treated as **employment service-providers** — so in practice **vendors should design accessible tests from the outset**, and a candidate can push the *firm* to require its vendor to do so. `[INDEPENDENT/INFERRED]` Michelmores + EqA s.55 framing. → Good persuasive point in a §5.11 letter even if the strict employment duty is reactive.

### 3c. Indirect discrimination (s.19) — the route to challenge adverse-impact in a TEST
- **s.19:** a PCP that is applied to everyone but puts people **sharing a protected characteristic** (sex, race, disability, age, religion, etc.) at a **particular (group) disadvantage**, and puts the claimant at that disadvantage, is unlawful **unless** the employer shows it is a **proportionate means of achieving a legitimate aim** (objective justification). `[REGULATORY]` Equality Act 2010 s.19, https://www.legislation.gov.uk/ukpga/2010/15/section/19 ; `[INDEPENDENT]` Foot Anstey; Acas, *Indirect discrimination*, https://www.acas.org.uk/discrimination-and-the-law/indirect-discrimination
- **NO numerical threshold** in UK law (contrast US 80% rule). Claimant shows **group disadvantage** (statistics help but aren't a fixed cut); employer defends with **legitimate aim** (e.g., valid predictor of job performance / genuine business need) that is **appropriate + necessary + proportionate**. `[INDEPENDENT]` DavidsonMorris, *Objective Justification*. https://www.davidsonmorris.com/objective-justification/
- → **This is how a candidate/claimant attacks a biased cognitive or gamified test in the UK:** show the test disadvantages e.g. a racial group or disabled people, then force the employer to prove the test is job-related + proportionate and that no less-discriminatory alternative exists. `[INFERRED]` from s.19 structure.

### 3d. Difference from US frameworks (feed §7 too) `[INDEPENDENT/INFERRED]`
- **UK:** disability-specific **positive duty to adjust** (proactive individual accommodation) + indirect discrimination with **open-ended proportionality** defence + **no fixed 80% trigger**. Disability discrimination also includes **s.15 "discrimination arising from disability"** and the adjustments duty — broader/more claimant-friendly than the US "reasonable accommodation + undue hardship" model in some respects. `[INFERRED]`.
- **US:** ADA "reasonable accommodation / undue hardship" for disability; **Title VII disparate impact** with the **EEOC four-fifths rule** as a rule-of-thumb trigger (see §7). Numerical, litigation-driven, class-action culture.

---

## 4. EU AI ACT — AI IN RECRUITMENT AS "HIGH-RISK" (§6.7; relevant to UK candidates at EU-operating firms)

- **Classification:** AI used in employment/recruitment is **HIGH-RISK** under **Art. 6(2) + Annex III point 4(a)**. Exact Annex III wording: *"AI systems intended to be used for the recruitment or selection of natural persons, in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates."* `[REGULATORY]` artificialintelligenceact.eu, Annex III. https://artificialintelligenceact.eu/annex/3/
- **Provider obligations (the vendor):** risk-management system across lifecycle, high-quality/representative training data + bias mitigation, technical documentation, logging, transparency & human-oversight design, conformity assessment + CE-style marking, post-market monitoring. `[REGULATORY/INDEPENDENT]` Hunton, *The Impact of the EU AI Act on HR Activities*. https://www.hunton.com/insights/legal/the-impact-of-the-eu-ai-act-on-human-resources-activities
- **Deployer obligations (the employer):** use per instructions, ensure **human oversight**, monitor, keep **logs ≥ 6 months**, run a **DPIA / fundamental-rights impact assessment** where required, ensure staff **AI literacy**, **inform workers' representatives** before deployment, and **inform candidates** they are subject to a high-risk AI system. `[REGULATORY/INDEPENDENT]` Hunton.
- **Candidate transparency / right to explanation:** individuals subject to a high-risk decision have the right to a **clear explanation of the AI system's role in the decision-making procedure and the main elements of the decision taken** (Art. 86 right to explanation of individual decision-making). `[REGULATORY/INDEPENDENT]` Hunton. → Stronger explicit "explain the decision" hook than UK GDPR gives.
- **TIMELINE — critical current-status flag:** `[REGULATORY/INDEPENDENT]`
  - Feb 2 2025: prohibited-use + AI-literacy rules live.
  - Aug 2 2025: GPAI rules live.
  - **Original** Aug 2 2026: high-risk (Annex III) + transparency → **DEFERRED**.
  - **DIGITAL OMNIBUS (proposed 19 Nov 2025; Council final approval 29 June 2026):** standalone **Annex III high-risk obligations pushed to 2 December 2027** (Annex I embedded to 2 Aug 2028). `[INDEPENDENT — multiple law firms]` Gibson Dunn, https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ ; Cooley, https://www.cooley.com/news/insight/2025/2025-11-24-eu-ai-act-proposed-digital-omnibus-on-ai-will-impact-businesses-ai-compliance-roadmaps ; DLA Piper. → **So for candidates applying in the 2026–2027 cycles, the EU recruitment-AI protections are largely NOT YET ENFORCEABLE.** Flag prominently.
- **Extraterritorial reach / why UK candidates care:** the Act binds providers/deployers whose AI **output is used in the EU**, regardless of location. A UK candidate applying to a bank's **EU/EMEA-run** grad programme (Frankfurt/Dublin/Paris hiring) can fall within scope even while sitting in London — but only once the high-risk rules bite (Dec 2027). `[REGULATORY/INDEPENDENT]` Hunton. `[INFERRED]` for the London-applicant-to-EU-desk scenario.

---

## 5. NYC LOCAL LAW 144 — AEDT BIAS AUDITS + NOTICE (§6.7; §5.11 evidence tool)
`[REGULATORY/INDEPENDENT]` — enacted 2021 (LL144-21); effective **1 Jan 2023**; **enforcement from 5 July 2023**.

- **Scope:** an **Automated Employment Decision Tool (AEDT)** = computational tool (ML/statistical/AI) that produces a **score/classification/recommendation** that **substantially assists or replaces** discretionary hiring/promotion decisions, for jobs **in NYC**. `[REGULATORY/INDEPENDENT]` Deloitte, *NYC Local Law 144 and Algorithmic Bias*. https://www.deloitte.com/us/en/services/audit-assurance/articles/nyc-local-law-144-algorithmic-bias.html ; NYC DCWP AEDT page https://www.nyc.gov/site/dca/about/automated-employment-decision-tools.page
- **Bias audit:** must be done by an **independent auditor**, **within one year** before use (i.e., **annually**), computing **selection rates** and **impact ratios** by **sex, race/ethnicity** (and intersectional categories); a **summary of results** + audit date + tool-distribution date must be **published publicly** on the employer's site. Auditors may exclude a category <2% of data. `[REGULATORY/INDEPENDENT]` Deloitte; DCWP FAQ https://www.nyc.gov/assets/dca/downloads/pdf/about/DCWP-AEDT-FAQ.pdf (PDF did not text-extract on 2026-08-01 — content from Deloitte + search of DCWP).
- **Notice to candidates:** must notify NYC candidates **at least 10 business days before** using the AEDT, stating the **job qualifications/characteristics** the tool assesses, and (on written request within 30 days) the **data collected**. `[REGULATORY]` NYC statute/DCWP (search summary 2026-08-01). *(Note: Deloitte's page did not restate the 10-business-day figure; the 10-business-day advance-notice requirement is in the statute itself — verify exact wording in gap audit.)* `[UNKNOWN — needs primary-text confirm]`.
- **Alternative process / accommodation:** LL144 requires **notice of the opportunity to request an alternative selection process or an accommodation** — but the law does **NOT actually compel the employer to grant one**. Common misconception. `[INDEPENDENT]` DCWP/critique literature (arxiv *Null Compliance*, https://arxiv.org/html/2406.01399v1). → useful to cite candidate-side.
- **Penalties:** civil, **$500 first violation**, up to **$1,500 per subsequent**, **each day = separate violation**. `[REGULATORY/INDEPENDENT]` Deloitte.
- **Why UK candidates care:** global banks (GS, JPM, MS, Citi, BofA) run **NYC hiring** and therefore **publish AEDT bias audits** — a UK candidate can **read a bank's published bias-audit summary for the very SHL/HireVue/etc. tool** they'll face and cite it. Low compliance/quality in practice (2024–2026 critiques). `[INDEPENDENT]` DLA Piper, *Critical audit of NYC's AI hiring law signals increased risk* (Jan 2026). https://www.dlapiper.com/en-us/insights/publications/2026/01/critical-audit-of-nyc-ai-hiring-law-signals-increased-risk-for-employers

---

## 6. ILLINOIS AI VIDEO INTERVIEW ACT (AIVIA, 820 ILCS 42) (§6.7; §5.11 for video providers) `[REGULATORY]`
Enacted **9 Aug 2019** (PA 101-0260); amended since. Primary text: Justia, https://law.justia.com/codes/illinois/chapter-820/act-820-ilcs-42/

- **Trigger:** employer uses **AI analysis of an applicant's video interview** for **Illinois-based** applicant positions. `[REGULATORY/INDEPENDENT]` Littler. https://www.littler.com/news-analysis/asap/implementing-illinois-ai-video-interview-act-five-steps-employers-can-take
- **Three core duties (before the interview / on use):**
  1. **Notice + explanation** — tell the applicant AI may be used, **how the AI works**, and the **general types of characteristics** it evaluates. `[REGULATORY]`.
  2. **Consent** — obtain the applicant's **consent** to be evaluated by AI before the interview. `[REGULATORY]`.
  3. **Sharing limits** — share the video **only with persons whose expertise/technology is necessary** to evaluate the applicant. `[REGULATORY]`.
- **Deletion on request:** on the applicant's request, **destroy all copies (incl. backups, incl. third parties') within 30 days**. `[REGULATORY]` Littler.
- **Demographic-data reporting (s.20):** an employer that **relies SOLELY on AI analysis** of the video to decide **who gets an in-person interview** must **collect + report race/ethnicity** of (i) those given/not given an in-person interview and (ii) those hired — reported to the **Illinois Dept of Commerce & Economic Opportunity annually by 31 Dec** (12-month period ending 30 Nov); Department reports on racial bias to Governor/General Assembly by 1 July. `[REGULATORY/INDEPENDENT]` 820 ILCS 42/20 (Justia); Aronberg Goldgehn. https://www.agdglaw.com/the-artificial-intelligence-video-interview-act-mandates-reporting-for-employers-electing-to-use-videorecorded-interviews
- **Note:** AIVIA does **not** define "AI," lacks a private right of action clarity, and enforcement is light — its practical value to a UK candidate is as **precedent/leverage language** (banks with US ops standardise HireVue notices around it). `[INDEPENDENT]` Littler/Holistic AI.

---

## 7. US EEOC / UGESP — FOUR-FIFTHS (80%) RULE (context for how vendors DEFEND tests) `[REGULATORY]`
- Source: **Uniform Guidelines on Employee Selection Procedures 1978**, 29 CFR Part 1607, adopted by EEOC/DOL/DOJ/CSC. https://www.ecfr.gov/current/title-29/subtitle-B/chapter-XIV/part-1607
- **Four-fifths rule:** a selection rate for any race/sex/ethnic group that is **< 80% (4/5) of the rate for the highest group** is **generally regarded as evidence of adverse impact**. Above 80% generally not. Smaller gaps can still count if statistically + practically significant. `[REGULATORY]` UGESP §1607.4(D); uniformguidelines.com Q&A https://www.uniformguidelines.com/uniform-guidelines-qa.html
- **The vendor's defence path (Title VII):** even with adverse impact, a test is lawful if **job-related and consistent with business necessity** (i.e., **validated** — content/criterion/construct validity per UGESP §1607.5) **and** no equally-valid **less-discriminatory alternative** exists. `[REGULATORY]` UGESP.
- **Why this matters for the book:** SHL/Aon/etc. **validation & adverse-impact studies are built around UGESP + the 80% rule** — when a vendor says "our test is fair / validated," they usually mean *US* four-fifths + validity evidence, which is **NOT the UK legal test**. A UK candidate should not assume "passed the 80% rule" = "lawful in the UK." `[INFERRED]`. EEOC's 2023 Title VII AI guidance confirms the four-fifths rule applies to algorithmic tools too. `[INDEPENDENT]` Hinckley Allen, https://www.hinckleyallen.com/publications/eeoc-releases-new-guidance-for-employers-on-title-vii-compliance-when-using-ai/

---

## 8. PRACTICAL — HOW & WHEN A UK CANDIDATE REQUESTS ADJUSTMENTS / ESCALATES (§5.11, §6.7)

### 8a. Reasonable adjustments — exact HOW/WHEN `[INFERRED from EqA + [INDEPENDENT] guidance]`
- **WHEN:** as **early as possible** — at the application stage or immediately on invitation to the OA/video, **before** taking it. Disclosing early fixes the employer's **"knowledge"** (see §3a) and is far stronger than complaining after a fail.
- **HOW:** reply to the recruiter / graduate-recruitment or `earlycareers@`/`reasonableadjustments@` inbox; state (a) you are disabled within EqA (no need to over-share diagnosis), (b) the **barrier** the specific test creates, (c) the **specific adjustment** requested (extra time %, format, no webcam, rest breaks). Keep it in writing (evidence).
- **Evidence:** employer can ask for reasonable evidence (e.g., diagnostic/educational-psychologist report for extra time) but must not use the request to discriminate.

### 8b. If the adjustment is REFUSED / you're auto-rejected `[INFERRED / [INDEPENDENT]]`
1. **Internal escalation:** ask for the decision + reasons in writing; ask for **human review** (invoke DUAA **Art. 22C** safeguards if the rejection was solely automated — §2b); ask them to reconsider the adjustment.
2. **DSAR (Art. 15):** submit the DSAR (§1) to get scores, flags, footage, decision-logic, human-involvement record — builds the evidence base. Free; **one month**.
3. **ICO complaint:** if the firm mishandles the DSAR or the automated-decision safeguards, complain to the **ICO** (ico.org.uk/make-a-complaint). ICO can investigate; fines up to **£17.5m / 4% global turnover** (but ICO rarely fines over an individual sift — realistically it nudges the controller, not overturns your rejection). `[INDEPENDENT]`.
4. **Equality route:** a **disability discrimination / failure-to-adjust** or **indirect-discrimination** claim goes to the **Employment Tribunal** (job applicants ARE covered even though never employed). **Time limit: 3 months less one day** from the act complained of; **Acas Early Conciliation** is a mandatory pre-step. `[REGULATORY/INDEPENDENT]` Acas. → This is the only route that can actually *remedy* (compensation; injury to feelings), not reverse the specific hire.

### 8c. REALISTIC expectations (be honest in the book) `[INFERRED]`
- **What almost never happens:** a regulator or court *forcing a firm to re-run your assessment or hire you*. There is **no "appeal my OA score" statutory right** that overturns the result.
- **What CAN realistically be won:** (a) **human review** of a solely-automated rejection (DUAA Art. 22C) — sometimes reverses; (b) **the adjustment itself** if requested *before* the test (routinely granted — extra time is standard); (c) **disclosure** of your data via DSAR; (d) **ET compensation** for a genuine failure-to-adjust or discrimination, months later. (e) NYC/EU material = **leverage + transparency**, not a UK remedy.
- **Highest-yield candidate move:** request the adjustment **up front** — that is the single most reliably enforceable right in the whole chapter.

---

## 9. WHAT AN EMPLOYER/VENDOR MUST DISCLOSE UNDER UK LAW (§6.7 checklist)
`[REGULATORY]` unless noted.
- **Privacy information (Arts 13–14 UK GDPR)** at/near data collection: identity of controller + DPO contact, **purposes + lawful basis**, recipients, retention, data-subject rights, right to complain to ICO, **and — where solely automated decisions with significant effect are made — the existence of ADM, meaningful info about the logic, and the significance/consequences.** → the recruitment **privacy notice** must flag automated sifting.
- **On DSAR (Art. 15):** must supply the personal data + the supplementary info in §1 within one month, free.
- **DUAA Arts 22A–22D:** where a solely-automated significant decision is taken, must proactively enable the **four safeguards** (information, representations, human intervention, contest) — §2b.
- **Equality Act s.60:** may only ask about health/disability pre-offer within the narrow exceptions (incl. arranging assessment adjustments).
- **NOT required to disclose:** proprietary algorithm/source code, item bank, other candidates' data, or exact cut-scores (no explicit UK duty to reveal the threshold — `[INFERRED]`, though the *fact* of a threshold + your data are within Art. 15).
- **EU AI Act (from Dec 2027, EU-scope roles):** deployer must inform candidates a high-risk AI system is used + provide Art. 86 explanation of the AI's role in the decision. `[REGULATORY]`.

---

## RESIDUAL GAPS / TO VERIFY IN GAP AUDIT
- `[UNKNOWN]` **Primary text of DUAA s.80 / Arts 22A–22D** — legislation.gov.uk returned **503** on 2026-08-01; ico.org.uk returned **403** on all ADM + right-of-access + employer-SAR pages. Provisions here are corroborated across gov.uk factsheet + 3 law-firm analyses, but re-fetch the **legislation.gov.uk** primary text and the **final ICO ADM guidance** (consultation was open early 2026 — check if finalised).
- `[UNKNOWN]` **NYC LL144 "10 business days"** advance-notice figure — confirm against DCWP rule text (Deloitte omitted it; search asserted it).
- `[UNKNOWN]` **Exact controller/processor split** per vendor (SHL/Aon/HireVue/Arctic Shores) — contract-specific; check each vendor's candidate privacy notice for whether they self-declare controller vs processor (feeds per-provider §5.11).
- `[UNKNOWN]` Whether the ICO has, post-DUAA, issued a **fixed standard for "meaningful human involvement"** via Secretary-of-State regulations — pending as of 2026-08-01.
- To add: **Baroness/EHRC guidance** and the **EHRC Employment Statutory Code of Practice** for authoritative reasonable-adjustment/indirect-discrimination detail (primary UK regulator guidance, not yet fetched).
