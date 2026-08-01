# 08 — HireVue — Raw Research Notes

**Researched:** 2026-08-01 (agent thread, WebSearch + WebFetch). All access dates = **2026-08-01**.
**Evidence tags:** `[VENDOR]` HireVue's own material · `[INDEPENDENT]` press/academic/regulator · `[CANDIDATE, n=X]` forum/first-hand (n = distinct corroborating accounts where countable; often approximate) · `[PREP-VENDOR]` commercially-biased prep sites · `[INFERRED]` my reasoning · `[UNKNOWN]` gap.
**Subsection coverage (5.1–5.13 mapped to task COVER list 1–11):** 5.1✅ 5.2✅ 5.3✅ 5.4✅ 5.5✅ 5.6✅ 5.7✅ 5.8✅ 5.9✅ 5.10✅ 5.11✅ (5.12/5.13 = prep + gaps below).

> **CRITICAL FRAMING — CURRENT vs LEGACY.** HireVue's single most important fact for this book is the **facial-analysis discontinuation**. Announced publicly **2021-01-12/19**; internally phased out ~March 2020. LEGACY (pre-2020/21) = video scored partly on **facial expressions / visual features / "nonverbal"** analysis. CURRENT (post-2021) = scoring is **language/content-based (NLP on the answer transcript) + game-based assessments**; facial/visual analysis **removed from the algorithms**. Every mechanic/critique below is tagged CURRENT or LEGACY. Do NOT let old (2018–2020) reporting describe the present product.

> **Analyst caution flag (throughout):** Two distinct source biases. (a) **Prep-vendors** (M&I, IGotAnOffer, WSO, CFI, JobTestPrep, GraduatesFirst, AceRound, Intervyo, thita.ai, gameassessmentprep) push "you need our practice" and routinely overstate/understate AI scoring and proctoring. (b) **HireVue's own PR** post-2021 is a deliberate "human-centric / audit-defensible" repositioning — treat "work as advertised on fairness" as a *vendor-commissioned* audit claim, not independent fact. Corroborate integrity/scoring claims across ≥2 source types.

---

## 5.1 — Ownership / corporate / what it is / UK-finance stage

- **Majority owner: The Carlyle Group** (PE). Growth investment / majority stake announced **2019-09-03**; deal closed shortly after. Prior/minority investors retained: **TCV, Granite Ventures, Sequoia** + management. [INDEPENDENT/VENDOR] Carlyle press release https://www.carlyle.com/media-room/news-release-archive/hirevue-receive-growth-investment-new-majority-investor-carlyle ; https://www.prnewswire.com/news-releases/hirevue-to-receive-growth-investment-from-new-majority-investor-the-carlyle-group-300910307.html ; Crunchbase https://www.crunchbase.com/acquisition/the-carlyle-group-acquires-hirevue--48c31cfb (all accessed 2026-08-01)
- Founded ~2004, Utah (South Jordan/Salt Lake City), US. [INFERRED from corporate history — verify founding year in gap audit]
- **Acquisition — game-based assessments: MindX**, a London-based psychometric-games company, acquired **~Nov 2018** (pre-Carlyle). MindX built "scientifically validated psychometric games and interactive quizzes." This is the origin of HireVue's game-based assessment line. [VENDOR] https://www.hirevue.com/blog/hiring/hirevue-and-mindx-are-teaming-up-to-build-the-industrys-most-powerful-hr-assessments-platform ; independent context https://diginomica.com/hirevue-video-interviews-game-based-assessment (dated Nov 2018)
- **What it is:** an end-to-end hiring/assessment platform. Product families [VENDOR, hirevue.com/platform/assessments]:
  1. **On-demand (async) video interview** — the "HireVue interview" candidates recognise; record answers to preset questions on their own time.
  2. **Game-based assessments** — psychometric games measuring cognitive abilities (mental agility, reasoning, numerical, visual/spatial) + emotional-intelligence/EQ (influence, collaboration, impulse control). [VENDOR blog]
  3. **Technical / coding assessments — "CodeVue"** — 200+ OnDemand coding assessments across Python, Java, Ruby, JavaScript, PHP, C++, Perl etc.; auto-scored; "built to … detect cheaters" and let non-technical recruiters screen. [VENDOR] https://www.hirevue.com/platform/coding-assessments
  4. **Virtual Job Tryout®** — scenario/SJT-style immersive assessments (40+ industries). [VENDOR]
  5. **Language proficiency tests** (customer-facing roles). [VENDOR]
- **UK-finance stage & duration:** HireVue's async video interview is one of the **most common early-stage video-interview steps** in UK graduate/intern finance pipelines. Typically sits **after online application + aptitude tests, before assessment centre/final**. [CANDIDATE/PREP-VENDOR, many] Duration cited **~10–30 min total** (varies by Q count). [PREP-VENDOR/CANDIDATE consistent]

## 5.2 — Why it exists (structured async interview at volume)

- Core value prop: run a **structured interview at scale** without scheduling live interviewers — every candidate gets identical questions, recorded, reviewable asynchronously. Enables high-volume grad/intern sifts. [VENDOR/INFERRED]
- HireVue's stated design logic: IO psychologists define **critical competencies per role**, questions map to them, responses scored against a rubric — i.e. *structured* interviewing, which the IO-psych literature holds is markedly more predictive of job performance than *unstructured* interviews. [VENDOR framing] hirevue.com/platform/assessments — vendor quote: "Rely on our team of expert IO Psychologists to identify the critical competencies for each role."
- **Predictive-validity backdrop (independent, for the book's cross-cutting chapter):** meta-analytic consensus (Schmidt & Hunter and successors) = structured interviews substantially out-predict unstructured; note the 2022 Sackett et al. re-analysis that revised several operational validities downward — cross-reference the SHL/§6.3 note. [INDEPENDENT — general literature, not HireVue-specific; verify exact figures in legal/psychometrics chapter] `[UNKNOWN]` HireVue-specific independent criterion-validity study.

## 5.3 — Why a firm picks HireVue (differentiators)

- **Scale + async** — thousands of candidates, no interviewer scheduling. [INFERRED/VENDOR]
- **ATS integration** — integrates with major applicant-tracking systems (Workday etc.). [VENDOR — specific integrations not captured this pass] `[UNKNOWN — list of named ATS integrations]`
- **Post-2021 "human-centric / audit-defensible" repositioning** — after the facial-analysis controversy HireVue rebuilt its pitch around: facial analysis removed, NLP/content scoring, **published external bias audits**, IO-psych rubrics, human-in-the-loop. This is explicitly a **compliance/defensibility** selling point to risk-averse buyers (banks). [VENDOR PR — see 5.6/5.9]
- **Reference clients (finance):** multiple bulge brackets + UK banks use HireVue video (see 5.11). Named across prep/candidate sources: **Goldman Sachs, J.P. Morgan, Morgan Stanley, Bank of America, Barclays, HSBC** (+ Deloitte, others). [PREP-VENDOR/CANDIDATE — see 5.11 for per-bank sourcing]

## 5.4 — FULL MECHANICS (async video)

**Question types:** predominantly **behavioural/competency** ("tell me about a time…", "why [firm]/why IB?", "walk me through your CV", "tell me about a team you worked in"); some **commercial-awareness/markets** ("tell us about a recent M&A deal / market that interests you"); occasionally **light technical** depending on division. [CANDIDATE/PREP-VENDOR, many: M&I, CFI, WSO, IGotAnOffer]

**Number of questions:** typically **3–5** (IB grad/intern). [PREP-VENDOR/CANDIDATE consistent — M&I "3–5"; WSO "3–5"]. UK banks skew higher: **Barclays ~5–8** (~1 min each, ~20 min total); **BofA reported ~5**. [PREP-VENDOR: graduatesfirst/jobtestprep; CANDIDATE: WSO BofA thread]

**Thinking / prep time:** **~20–30 seconds** per question. [PREP-VENDOR/CANDIDATE consistent — CFI "20–30s"; M&I "30s"; WSO "30s"]. Employer-configurable.

**Recording / answer time:** commonly **60–180 s** (i.e. 1–3 min); frequently **90 s** or **up to 2 min** or **up to 3 min** depending on employer config. Recording **auto-stops** at the limit. [PREP-VENDOR/CANDIDATE consistent — M&I "90s"; CFI "up to 3 min"; WSO "up to 2 min, stops at 2"; BofA "3 min"]. Summer-analyst windows sometimes shorter. [PREP-VENDOR]

**Number of takes / re-records — EMPLOYER-CONFIGURED, KEY NUANCE:**
- Default / common config: **ONE take per question, no re-record** ("once you begin recording you cannot pause or re-record"; CFI "only one chance"). [PREP-VENDOR/CANDIDATE, many]
- BUT **some employers enable limited re-records** ("some firms let you re-record a few times"). [PREP-VENDOR: M&I]
- **Whether re-record count is visible to reviewer:** `[UNKNOWN — not confirmed by any source this pass]`. Prep sources say re-record availability is set per employer; none confirm reviewers see how many takes you used. Flag as gap.

**Practice questions:** **YES.** Unlimited **practice/tutorial questions** before the real interview; HireVue's help center indicates practice responses are **not uploaded, not scored, not visible to employer** (up to ~3 practice prompts, unlimited attempts). [PREP-VENDOR summarising HireVue help: Intervyo, AceRound] — corroborates VENDOR help-center existence, though the primary Zendesk page (hirevuesupport.zendesk.com) returned 403 this pass. `[Re-verify against primary help center.]`

**Human-reviewed vs AI-transcribed vs AI-scored (CURRENT):** all three configurations exist depending on employer:
- Responses are **transcribed** (speech-to-text) and can be **AI-scored via NLP** against competencies; and/or
- **Human-reviewed** by the employer's recruiters (many banks use HireVue purely as a *recording/delivery* tool with humans watching, NOT AI scoring). [INDEPENDENT/INFERRED] — important: **"uses HireVue" ≠ "AI-scored."** Many UK bank deployments are human-reviewed one-way video. Flag this distinction hard for the book. [INFERRED from vendor config flexibility + candidate reports of human next-round invites]

**Competency rubric:** IO-psych-defined competencies per role; scoring maps transcript content to those competencies (see 5.6). [VENDOR]

**Game-based assessments (mechanics):** separate module; a battery of short **psychometric games** measuring cognitive + EQ traits; "new games added regularly" so **no fixed count**. [VENDOR blog] `[UNKNOWN — canonical game list/count/timing; game-prep sites claim "~13 simulations" but that's PREP-VENDOR (gameassessmentprep.com), unverified.]`

**Coding assessments (CodeVue) mechanics:** 200+ OnDemand auto-scored coding challenges; completed on candidate's own time, any device; measures language proficiency + problem-solving; anti-cheat features. [VENDOR] hirevue.com/platform/coding-assessments

**Device:** desktop/laptop with **webcam + mic + internet** (video); coding/games "any device." [PREP-VENDOR/VENDOR]

**Retake (whole assessment):** employer-set; generally no self-serve retake once submitted (see 5.6). [PREP-VENDOR: Intervyo retake page]

## 5.5 — Tailoring (per-employer configuration)

- **Same core engine, employer-configured surface.** Questions, competencies, number of Qs, prep/answer times, re-record on/off, and whether integrity flags are on are all **set per employer**. [PREP-VENDOR/CANDIDATE consistent — StudentRoom users note "depends completely on the company"; format can even include MCQ/essay + video in one HireVue link]
- Rubric/competencies **customisable per role** via HireVue's IO-psych team (or off-the-shelf competency libraries). [VENDOR]
- Practical consequence: candidate experience of "a HireVue" varies widely between banks; do not generalise timings across employers. [INFERRED]

## 5.6 — SCORING (how video is scored NOW) + IO rubric + retake

- **CURRENT scoring = content/language-based.** After 2021, primary signal is **what the candidate says** — the answer **transcript analysed by NLP/ML** mapped to competencies; facial/visual analysis **removed**. [INDEPENDENT] SHRM: "Natural language processing now serves as the primary analytical method … the company shifted focus to analyzing applicants' actual responses and speech content rather than facial expressions." https://www.shrm.org/topics-tools/news/talent-acquisition/hirevue-discontinues-facial-analysis-screening ; EU-analysis corroboration: "analyzes what candidates say (language, content) rather than how they look." https://www.upnorth.ai/en/insights/ai-act-hirevue
- **IO-psychologist-built rubric:** HireVue IO psychologists define competencies + scoring; models validated against those. [VENDOR]
- **The 0.25% fact (why facial was dropped):** HireVue Chief Data Scientist **Lindsey Zuloaga** said nonverbal/visual data contributed **~0.25%** of predictive power vs answer content (up to ~4% for some customer-facing roles). CEO **Kevin Parker**: *"When you put that in the context of the concerns people were having … it wasn't worth the incremental value."* [INDEPENDENT] Fortune 2021-01-19 https://fortune.com/2021/01/19/hirevue-drops-facial-monitoring-amid-a-i-algorithm-audit/
- **What recruiter sees / output:** competency **scores + candidate ranking**; recorded video for human review; integrity flags if enabled. [VENDOR/PREP-VENDOR] — exact score scale/report format `[UNKNOWN — not captured; verify]`.
- **Human review is central now** and (per EU AI Act analysis) legally required as meaningful oversight — recruiters can override AI; "rubber-stamping the AI score doesn't count." [INDEPENDENT] upnorth.ai (Art. 14 / 26(1))
- **Ranking:** candidates ranked/scored to prioritise reviewer attention; not necessarily auto-reject (see 5.8). [INFERRED/PREP-VENDOR]
- **Retake policy:** employer-set; typically **no candidate-initiated retake** after submission; re-invites at employer discretion. [PREP-VENDOR: Intervyo https://www.intervyo.co.uk/answers/hirevue/can-you-retake-hirevue]

## 5.7 — How to prepare LEGITIMATELY

- **Structure under time pressure: STAR / CARL.** With ~30 s think + ~60–90 s answer, use STAR (Situation, Task, Action, Result) or CARL (Context, Action, Result, Learning) to stay focused. [PREP-VENDOR consensus: M&I, Leland]
- **Pacing:** aim ~**100–125 words/min**; practise 5 questions at 30 s prep / 90 s answer with a stopwatch. [PREP-VENDOR: M&I]
- **First ~10 seconds:** open with a crisp headline/thesis sentence (answer the question directly) before the story — reviewers skim; the transcript's early content is weighted by attention. [PREP-VENDOR/INFERRED]
- **Framing / lighting / eye-line (still matters for HUMAN reviewers even though the algorithm no longer scores your face):** face a window/soft light, camera at eye level, look **into the lens** (not the screen), neutral background, test mic. [PREP-VENDOR consensus]
- **Recovering from a fumble:** if no re-record, keep going — reviewers/NLP score the substance; a restart phrase ("let me put that more clearly") is fine. Don't burn silence. [INFERRED/PREP-VENDOR]
- **What reviewers score against:** the **competencies** (teamwork, drive, commercial awareness, motivation for firm/role) — tailor concrete examples to the firm's stated values. [VENDOR/PREP-VENDOR]
- **Worked strong-vs-weak (illustrative, INFERRED — mark as author example, not sourced data):**
  - *Weak:* "Umm, I guess I work well in teams, like at uni we did a group project and it went fine and everyone was happy." (no structure, no result, vague, no competency evidence)
  - *Strong (STAR):* "In my final-year consulting project (S) I was made team lead for a 5-person deliverable to a real SME client (T). I split workstreams by strength, ran twice-weekly stand-ups, and personally rebuilt the financial model when our numbers didn't tie (A). We delivered two days early and the client adopted two of our three recommendations; I learned to delegate analysis but own the client-facing narrative (R)." [INFERRED — author-constructed]

## 5.8 — INTEGRITY / PROCTORING

- **What HireVue can monitor (CURRENT, employer-configurable):**
  - **Browser focus / tab-switch tracking** — logs *when* focus leaves the HireVue tab and returns; **does NOT screen-record or see other tabs' contents**. [PREP-VENDOR, corroborated across AceRound articles] https://www.aceround.app/blog/can-hirevue-detect-tab-switching/
  - **Candidate image capture / ID snapshot** — periodic webcam snapshots to confirm a face is present / identity. [PREP-VENDOR]
  - **Webcam-presence check** — flags if no face in frame. [PREP-VENDOR]
  - **Camera + audio only** (per prep sources) — **not** full screen recording. [PREP-VENDOR: AceRound "Camera & Audio Only"]
  - **Similarity/plagiarism scoring** across responses (flagging answers very similar to other candidates', e.g. read/coached). [PREP-VENDOR: AceRound — single-source, treat cautiously]
  - **NOT eye-tracking / facial-expression analysis** — discontinued Jan 2021. [INDEPENDENT] Any claim HireVue "tracks your eyes/emotions" is LEGACY or myth.
- **How flags are actioned:** flags go into the **assessment record**; a **human reviewer at the employer decides** — HireVue does **not auto-reject** on a tab-switch. [PREP-VENDOR: AceRound, consistent]
- **What employer receives:** recording + transcript + competency scores + any integrity flags (if enabled). [INFERRED/PREP-VENDOR]
- **Whether candidate is told:** integrity monitoring is often disclosed in T&Cs/instructions but candidates frequently under-notice it; disclosure obligations vary by jurisdiction (see 5.10). [INFERRED] `[UNKNOWN — HireVue's standard candidate-facing disclosure text not captured this pass.]`

## 5.9 — FALSE-POSITIVE risks + documented bias critiques

- **Accent / ESL under NLP scoring (CURRENT risk):** the ORCAA audit itself **recommended investigating bias in candidates with different accents**, and flagged that **minority candidates giving brief responses were disproportionately routed to human reviewers**. [INDEPENDENT] Fortune 2021-01-19. This is the live fairness risk now that scoring is language/transcript-based. Speech-to-text error rates are known to be higher for some accents/dialects → transcription errors → competency-scoring errors. [INDEPENDENT/INFERRED]
- **Lighting / skin-tone face-detection (LEGACY + residual):** legacy facial analysis raised racial-bias concerns (facial-recognition/emotion tech documented to underperform on darker skin). EPIC alleged facial recognition "could be racially biased." [INDEPENDENT] Nat Law Review https://natlawreview.com/article/epic-files-complaint-ftc-regarding-ai-based-facial-scanning-software . Residual: webcam **presence/ID snapshots** can still fail in poor lighting/low contrast on darker skin → false "no face" integrity flags. [INFERRED]
- **Disability / neurodivergence in video:** atypical eye-contact, affect, stutter, motor differences historically risked misscoring by facial/nonverbal analysis (now removed) but can still affect **human** reviewers and speech-fluency-sensitive NLP. Expert **Merve Hickok** (AI ethics): *"Facial expressions are not universal — they can change due to culture, context and disabilities — and they can also be gamed."* [INDEPENDENT] SHRM. **Julia Stoyanovich** (NYU): *"We should not be relying on signal features … that have nothing to do with job performance."* [INDEPENDENT] SHRM.
- **Stutter / disfluency:** timed, no-re-record recording + speech-to-text penalises disfluency and non-native pacing. [INFERRED — flag for accessibility]
- **Eye-line misread:** looking away to think can read as evasive to human reviewers (algorithm no longer scores it). [INFERRED/PREP-VENDOR]
- **The EPIC FTC complaint (documented, central):** EPIC filed with the FTC **2019-11-06** (some coverage bylined Jan 2020) alleging **unfair & deceptive practices under §5 FTC Act** — that HireVue's AI (claimed to measure "cognitive ability, psychological traits, emotional intelligence, social aptitudes") was **"biased, unprovable, and not replicable,"** that eye-tracking could disparately impact visually-impaired applicants, and that HireVue **deceptively denied using facial recognition**. [INDEPENDENT] https://epic.org/documents/in-re-hirevue/ ; https://natlawreview.com/article/epic-files-complaint-ftc-regarding-ai-based-facial-scanning-software ; EPIC's own summary of the Jan-2021 outcome https://archive.epic.org/2021/01/hirevue-facing-ftc-complaint-f.html
- **Academic/press critique:** Washington Post (Drew Harwell) reporting quoted AI researchers calling face-scanning hiring **"digital snake oil … an unfounded blend of superficial measurements and arbitrary number-crunching."** [INDEPENDENT] via NCRC repost https://ncrc.org/the-washington-post-a-face-scanning-algorithm-increasingly-decides-whether-you-deserve-the-job/ (Harwell, WaPo, 2019).

## 5.10 — Adjustments / accessibility + regulatory (feeds legal chapter)

- **Accessibility/adjustments:** candidates can request adjustments (extra time, alternative format) via the employer; specifics employer-mediated. `[UNKNOWN — HireVue's documented accommodation process not captured; verify.]`
- **GDPR Art. 22 (EU/UK):** prohibits decisions based **solely** on automated processing with legal/significant effect, absent consent/contract/law + safeguards (right to human intervention, to express views, to contest). Automated hiring/video-interview analysis is squarely in scope; regulators (2026 coverage) reasserting Art. 22 applies to video-interview platforms. [INDEPENDENT] https://www.techtimes.com/articles/320141/20260711/... ; upnorth.ai — this is exactly why HireVue emphasises **human-in-the-loop** (avoids "solely automated").
- **EU AI Act:** HireVue = textbook **high-risk** system, **Annex III point 4** (employment/worker management — recruitment & candidate evaluation). Requires meaningful human oversight (Arts. 14, 26(1)), candidate transparency **before** assessment (Art. 26(11)). Note: **Digital Omnibus** pushed the stand-alone Annex-III high-risk compliance deadline from **2026-08-02 → 2027-12-02**. [INDEPENDENT] https://www.upnorth.ai/en/insights/ai-act-hirevue ; https://regumatrix.eu/compliance/hr-recruitment
- **Illinois Artificial Intelligence Video Interview Act (effective 2020):** requires employers using AI to analyse video interviews to **notify** candidates, **explain** how the AI works/what it evaluates, obtain **consent**, limit sharing, and delete on request. First-in-US AI-video law; **no bias-audit mandate** in the original act. [INDEPENDENT] https://introl.com/blog/illinois-ai-video-interview-law-employer-notification-2026 ; teamfill.net comparison
- **NYC Local Law 144 (AEDT, enforced 2023-07-05):** any **automated employment decision tool** used to screen NYC candidates must have an **independent third-party bias audit** (disparate impact by race/ethnicity/sex, incl. intersectional) published, plus candidate notice. Broader than IL (covers CV screeners + video). [INDEPENDENT] hraizon / employsome guides
- **HireVue's audit posture (they publish audits — audit-defensible strategy):**
  - **ORCAA** (O'Neil Risk Consulting & Algorithmic Auditing, founded by **Cathy O'Neil**, *Weapons of Math Destruction*) audited HireVue's early-career assessments; concluded they **"work as advertised with regard to fairness and bias issues"** — BUT audit scope was **limited to representative early-career use cases, not all algorithms**, and recommended accent-bias investigation. [INDEPENDENT/vendor-commissioned] Fortune/SHRM (2021).
  - **DCI Consulting Group** (DC-based HR compliance firm) engaged **Jan 2023** for external bias audit of **competency-based AND game-based algorithms** (race, gender, intersectional, multiple job levels/use cases), aligned to **NYC LL144**. [VENDOR] https://www.hirevue.com/press-release/hirevue-leads-industry-in-fair-and-ethical-hiring-practice-engaging-external-auditor-dci-consulting-group-for-external-bias-audit-of-algorithms

## 5.11 — UK FINANCE EMPLOYER USAGE (which banks / stage / source) — FLAG VOLATILITY

> **Volatility warning:** vendor choice and stage change year to year and by division/region. Every row below is a *point-in-time* candidate/prep claim, not a standing contract. **HireVue being used ≠ AI-scored** (many are human-reviewed one-way video). Verify per intake before print.

- **Goldman Sachs** — HireVue async video for programme applicants (IB summer analyst etc.), post-application. [CANDIDATE, WSO threads (Goldman HireVue overview/process); PREP-VENDOR: CFI names GS]. WSO forum pages 403'd this pass (title/snippet-level only).
- **J.P. Morgan** — HireVue video interview stage. [PREP-VENDOR: CFI names JPM; WSO "JP Morgan HireVue Interview Questions" thread]
- **Morgan Stanley** — HireVue questions guide exists; used for programmes. [PREP-VENDOR: Leland "Morgan Stanley HireVue Questions"]
- **Bank of America** — HireVue, reported **~5 questions, ~3 min each, one try**. [CANDIDATE: WSO "BofA HireVue" thread (403 this pass, snippet); PREP-VENDOR: jobtestprep BofA summer internship]
- **Barclays** — pre-recorded one-way HireVue; **~5–8 questions, ~1 min each, ~20 min**; used for operations/grad schemes. [PREP-VENDOR: graduatesfirst/jobtestprep; CANDIDATE: StudentRoom "Barclays HireVue Video Interview – Operations" t=6733974 (403 this pass)]
- **HSBC** — HireVue pre-recorded video across most grad + many experienced pipelines; sits after SHL online tests, before assessment centre (HSBC process = SHL tests → HireVue → AC → final). [PREP-VENDOR: graduatesfirst HSBC interviews, ophyai HSBC guide; CANDIDATE: StudentRoom/Glassdoor]
- **Santander** (internship, Risk & Compliance), **BlackRock** (analyst programme), **Dyson**, **WTW/Willis Towers Watson** — HireVue video referenced by UK candidates. [CANDIDATE: StudentRoom threads t=6750446, t=7610366, t=7350734, t=7445727 — snippet-level; pages 403'd]
- **Deloitte** (accounting, adjacent) — named HireVue client. [PREP-VENDOR: CFI]

---

## Strongest / primary sources (for citations)
- **[INDEPENDENT] Fortune, 2021-01-19** — facial drop, ORCAA audit, 0.25% figure, Zuloaga & Parker quotes, accent-bias recommendation: https://fortune.com/2021/01/19/hirevue-drops-facial-monitoring-amid-a-i-algorithm-audit/
- **[INDEPENDENT] SHRM** — NLP-primary scoring, expert critiques (Hickok, Stoyanovich), audit scope limits: https://www.shrm.org/topics-tools/news/talent-acquisition/hirevue-discontinues-facial-analysis-screening
- **[INDEPENDENT] EPIC** — FTC complaint + outcome: https://epic.org/documents/in-re-hirevue/ · https://archive.epic.org/2021/01/hirevue-facing-ftc-complaint-f.html
- **[INDEPENDENT] Nat Law Review** — EPIC complaint substance: https://natlawreview.com/article/epic-files-complaint-ftc-regarding-ai-based-facial-scanning-software
- **[INDEPENDENT] upnorth.ai** — EU AI Act high-risk + Art. 22 + current NLP operation: https://www.upnorth.ai/en/insights/ai-act-hirevue
- **[VENDOR] Carlyle / PRNewswire** — ownership: https://www.carlyle.com/media-room/news-release-archive/hirevue-receive-growth-investment-new-majority-investor-carlyle
- **[VENDOR] HireVue** — DCI audit press release; platform/assessments; CodeVue coding; MindX blog (URLs above).
- **[PREP-VENDOR, mechanics]** M&I https://mergersandinquisitions.com/hirevue-interview/ · CFI https://corporatefinanceinstitute.com/resources/careers/interviews/about-hirevue-interview/ · IGotAnOffer (403) · AceRound proctoring series.

## Residual gaps (for gap audit)
- **Re-record visibility to reviewer** — unconfirmed whether reviewers see how many takes a candidate used. `[UNKNOWN]`
- **Primary HireVue candidate help-center text** (practice/re-record/retake rules) — Zendesk 403'd; re-verify from primary.
- **Named ATS integrations** — not captured. `[UNKNOWN]`
- **Game-based assessment canonical list/count/timings** — only PREP-VENDOR ("~13") figures; no VENDOR count. `[UNKNOWN]`
- **Score-report format / scale** the recruiter sees — not captured. `[UNKNOWN]`
- **WSO forum + StudentRoom threads all returned 403** this pass — bank-specific candidate timings are snippet-level only; re-fetch (or archive.org) needed for verbatim first-hand n-counts.
- **HireVue founding year** and full acquisition timeline — verify.
- **HireVue-specific independent criterion-validity study** — none found; only vendor validity claims. `[UNKNOWN]`
- **Standard candidate-facing integrity/monitoring disclosure text** — not captured. `[UNKNOWN]`
- **Post-2021 additional FTC action / IL/NYC enforcement against HireVue specifically** — LegalClarity "every legal challenge" page noted but not fetched; check for BIPA/Illinois suits. `[UNKNOWN — follow up]`
