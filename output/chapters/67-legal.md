# Chapter 6.7 — Your Legal Rights and the Regulatory Picture

> *This chapter states the law as it stood on 1 August 2026. One area — UK automated-decision rules — changed materially in February 2026, and another — the EU AI Act — is mid-deferral. Both are flagged inline. Where a detailed regulator standard was still pending, the chapter says so rather than inventing certainty. Confidence tags: `[REGULATORY]` = statute/official source; `[INDEPENDENT]` = reputable legal analysis; `[INFERRED]` = reasoning shown; `[UNKNOWN]` = not settled.*

If you have been screened out at an online assessment — especially on integrity grounds — the single most useful thing to understand is that you have **more enforceable rights *before* you sit the test than after you are rejected.** The law gives you a strong, reliably-granted right to adjustments up front, a solid right to see your data afterwards, and a weaker, slower right to challenge the decision itself. This chapter tells you exactly what each one is, and — importantly — corrects two things a candidate who read about this even a year ago would now get wrong.

## The headline corrections

**1. UK "Article 22" is no longer the live provision.** For years, UK data-protection law (via Article 22 of the UK GDPR) said you had the right *not to be subject to a decision based solely on automated processing* that significantly affected you — a general *prohibition*. That is **out of date.** The **Data (Use and Access) Act 2025 ("DUAA")**, section 80, **replaced Article 22 with new Articles 22A–22D, in force from 5 February 2026.** The framework **flipped from prohibition to permission-with-safeguards**: a fully-automated significant decision is now *lawful* provided the organisation gives you four specific safeguards. `[REGULATORY — DUAA 2025 s.80; INDEPENDENT — Travers Smith, Handley Gill, Bratby analyses]` This changes your lever from "you weren't allowed to do that" to "you must now give me the safeguards — including human review" (see below).

**2. The EU AI Act's recruitment rules are not yet enforceable.** AI used to filter and evaluate job applicants is classed as **high-risk** under the EU AI Act (Annex III, point 4(a)). But the obligations that would matter to you as a candidate were **deferred**: the "Digital Omnibus" package (Council approval 29 June 2026) pushed the high-risk Annex III duties to **2 December 2027.** `[INDEPENDENT — Gibson Dunn, Cooley, DLA Piper]` So for the 2026–2027 application cycles this guide targets, the EU-side protections are largely **not yet in force** — useful to know about, not yet a tool you can wield.

**3. There is no UK "four-fifths / 80% rule."** That is a *US* construct (see the end of this chapter). UK challenges to a biased test run through **indirect discrimination** under the Equality Act 2010, which has **no fixed numerical trigger** — do not import the 80% rule into UK thinking. `[REGULATORY]`

## Your right of access: the DSAR (UK GDPR Article 15)

This is your workhorse right, and it survived the 2025 reforms intact. Under **Article 15**, you can require any organisation holding your personal data to give you (a) confirmation they are processing it, (b) a **copy** of that data, and (c) supplementary information — including the existence of any automated decision-making and *meaningful information about the logic* involved. `[REGULATORY]` A request is called a **Data Subject Access Request (DSAR)**.

- **Deadline: one month**, extendable by up to two further months for genuinely complex requests, but only if they tell you (with reasons) within the first month. `[REGULATORY — ICO]` DUAA added a **"stop-the-clock"** rule: the month pauses if the organisation reasonably needs to verify your identity or clarify the request, resuming when you reply. `[REGULATORY — gov.uk DUAA factsheet]`
- **Cost: free**, in the ordinary case. They can only charge or refuse if the request is "manifestly unfounded or excessive," and the burden is on them to prove that. `[REGULATORY]`
- **Who to send it to.** The **employer** (the bank or firm) is almost always the **data controller** and the right first recipient — send it to their DPO or privacy team (often `privacy@` or `dataprotection@`). The **assessment vendor** (SHL, Aon, HireVue and so on) is usually a **processor** acting on the employer's instructions, though vendors often become controllers for their own norming and model-training. Send it to the employer first; if they point you to the vendor, send a second request there. `[INFERRED — controller/processor test; exact split is contract-specific and usually undisclosed]`

**What to specifically request** (put all of this in the letter — the template is at the end):

| Ask for | Why |
|---|---|
| Raw and scaled **scores** per test/section; your **percentile / sten / band** | The actual result |
| The **norm group** you were compared against | Determines what your percentile means (Chapter 6.3) |
| Any **cut-score / threshold** applied and whether you cleared it | Tells you *how* you fell |
| **Proctoring / integrity flag logs** — flag events, similarity/plagiarism scores, "suspicious behaviour" markers, IP/device logs | The heart of a false-flag case |
| Any **webcam/screen footage or audio**, plus any **AI-derived analysis** (competency ratings, transcript scoring) | What the machine "saw" |
| **Automated-decision disclosure**: whether an automated sift was applied, meaningful information about the logic, and the consequences (Art. 15(1)(h)) | Engages the new Art. 22A–22D safeguards |
| Whether a **human reviewed** the decision, and at what stage | Determines if it was "solely automated" |
| Recipients and **retention period** | Completeness |

**Two limits to expect.** They may **redact third-party data** (other candidates' scores, assessor identities) but must tell you what was withheld and why. And Article 15 entitles you to *meaningful information about the logic* — **not** the proprietary algorithm, item bank or source code. Expect a plain-English description of how the decision was made, not the model itself. `[INFERRED / INDEPENDENT]`

## Automated decisions: the new Articles 22A–22D (DUAA 2025)

Here is the current UK position, in force since 5 February 2026. `[REGULATORY — DUAA 2025 s.80; INDEPENDENT — Travers Smith, Handley Gill]`

A **"significant decision"** is one producing a legal or *similarly significant* effect on you — an automated graduate sift that rejects you plausibly qualifies. A decision is **"based solely on automated processing"** when there is **no meaningful human involvement.** Under the old law, such a decision was presumptively banned. Under the new law it is **permitted for ordinary personal data — but only if the organisation provides the four safeguards in Article 22C:**

1. give you **information** about the automated significant decisions taken about you;
2. enable you to **make representations**;
3. enable you to **obtain human intervention** from the controller;
4. enable you to **contest** the decision.

**These four are your escalation script.** If you were auto-rejected below a cut-score with no human looking, that is a solely-automated significant decision, and you can write: *"Please provide the Article 22C safeguards: I am making representations and requesting human intervention in, and contesting, this automated decision."* `[INFERRED from the statute — this is the practical lever]`

**A stricter rule protects sensitive data (Article 22B).** A solely-automated significant decision based *wholly or partly on special-category data* — health, disability, race, biometric data — **remains prohibited** unless a narrow Article 9 condition is met *and* the safeguards are in place. `[REGULATORY / INDEPENDENT]` This matters where a **video or personality inference could touch health or disability** — for example, if a proctoring or video-analysis system effectively processed data about a disability. In that scenario you have a materially stronger argument that the decision was unlawful.

**What "meaningful human involvement" means.** Pending updated ICO guidance, the working standard is the pre-DUAA one: the human reviewer must have the **authority and competence to override** the machine, must actually **weigh and interpret** the recommendation (not rubber-stamp it), must have access to all relevant data, and must not be discouraged from disagreeing. A recruiter who merely clicks "confirm" on a ranked list has *not* provided meaningful human involvement. `[REGULATORY — ICO benchmarks via Handley Gill]`

**A live uncertainty, stated honestly.** The **ICO had not finalised** its updated automated-decision-making and profiling guidance as of 1 August 2026 (a consultation ran in early 2026), and any Secretary-of-State regulations defining "meaningful human involvement" were still pending. `[UNKNOWN — live]` The framework above is correct, but the fine detail of the standard may shift; check the ICO site before relying on the precise threshold.

## The Equality Act 2010: adjustments and adverse impact

This is, in practice, your most valuable law — because the right it gives you *before* the test is the one that is most reliably granted.

**The duty to make reasonable adjustments (ss. 20–21).** An employer must make reasonable adjustments for a **disabled** applicant where a *provision, criterion or practice* (a "PCP") puts them at a **substantial disadvantage** compared with non-disabled people. **A timed online test is a PCP** — a worked legal example is literally "a policy requiring all applicants to complete an online test within 30 minutes." `[REGULATORY / INDEPENDENT — Michelmores]` Typical adjustments include:

- **Extra time** (commonly +25%, but there is *no statutory figure* — reasonableness is fact-specific); `[INDEPENDENT/INFERRED]`
- an **alternative format** (e.g. a dyslexia-friendly or screen-reader-compatible version);
- **rest breaks**; removing or replacing a **gamified** element that disadvantages you;
- **skipping webcam proctoring** where it disadvantages you (directly relevant to the false-flag problem);
- an assessor **briefing** for autistic candidates.

Two features make this powerful. First, the duty bites once the employer **knows or ought reasonably to know** you are disabled and likely disadvantaged — which is exactly why you should **disclose and request early**, before you sit, to fix that knowledge. `[REGULATORY]` Second, although employers generally **must not ask about health or disability before a job offer** (s. 60), there is a specific exception: they *may* ask **to establish whether an assessment adjustment is needed.** `[REGULATORY]` So the recruiter's "do you need any adjustments for the test?" is the lawful channel — use it. The **employer pays** for the adjustment; it can never be passed to you. `[REGULATORY]`

**Challenging a biased test — indirect discrimination (s. 19).** If a test disadvantages a group sharing a protected characteristic (race, sex, disability, age, religion), it is unlawful **unless** the employer proves it is a *proportionate means of achieving a legitimate aim* — i.e. that the test is genuinely job-related and that no equally-valid, less-discriminatory alternative exists. `[REGULATORY]` There is **no numerical threshold** in UK law; you show group disadvantage (statistics help), and the burden shifts to the employer to justify. `[INDEPENDENT]` This is the mechanism by which a candidate could, in principle, attack a cognitive or gamified test that adversely affects their group — though it is a tribunal claim, not a quick fix.

## The other regimes — leverage, not UK remedies

Three foreign or partial regimes are worth knowing because global banks comply with them and thereby generate information you can use.

**NYC Local Law 144.** Since July 2023, any employer using an *automated employment decision tool* for NYC jobs must commission an **independent bias audit annually** and **publish a summary** — selection rates and impact ratios by sex and race/ethnicity — on its website, and give candidates advance notice. `[REGULATORY / INDEPENDENT — Deloitte, NYC DCWP]` Because the bulge-bracket banks all hire in New York, **they publish bias audits for the very tools (SHL, HireVue and so on) you will face in London.** You can read a bank's published audit summary for the exact tool. Two honest caveats: the law only requires *notice* of the opportunity to request an alternative process — it does **not compel** the employer to grant one — and independent reviews (2024–2026) found real-world compliance patchy. `[INDEPENDENT — DLA Piper; arXiv "Null Compliance"]`

**Illinois AI Video Interview Act.** For Illinois roles, an employer using **AI to analyse a video interview** must (1) notify the applicant and explain how the AI works and what it evaluates, (2) obtain **consent**, and (3) limit who sees the video, plus **delete all copies within 30 days on request.** `[REGULATORY]` Its value to a UK candidate is as **precedent language** — banks with US operations tend to standardise their HireVue notices around it, so the transparency you're entitled to elsewhere is often already documented.

**US EEOC four-fifths rule.** Under the US Uniform Guidelines, a selection rate for any group below **80%** of the highest group's rate is treated as evidence of adverse impact. `[REGULATORY]` This matters only because it is **how vendors defend their tests**: when SHL or Aon says a test is "fair" or "validated," they usually mean it passes the US four-fifths rule plus US validity standards — which is **not** the UK legal test. Do not assume "passed the 80% rule" means "lawful in the UK." `[INFERRED]`

## What an employer or vendor must actually tell you (UK)

- **Privacy information (Arts 13–14):** at collection, the recruitment privacy notice must state the controller and DPO, the purposes and lawful basis, recipients, retention, your rights, your right to complain to the ICO, and — where solely-automated significant decisions are made — the existence of that automated decision-making, meaningful information about the logic, and its consequences. If a firm auto-sifts, its privacy notice should say so; read it. `[REGULATORY]`
- **On a DSAR:** your data plus the supplementary information above, within one month, free.
- **They need *not* disclose:** the proprietary algorithm, the item bank, other candidates' data, or (there is no explicit UK duty here) the exact cut-score — although the *fact* of a threshold and your own data fall within Article 15. `[INFERRED]`

## The realistic bottom line

Be honest with yourself about outcomes, because it changes where you spend effort:

- **What almost never happens:** a regulator or court forcing a firm to re-run your assessment or hire you. There is no statutory "appeal my score and overturn it" right.
- **What you can realistically win:** (a) **the adjustment itself**, if you request it *before* the test — this is routinely granted and is by far the most reliably enforceable right in this chapter; (b) **human review** of a solely-automated rejection under Article 22C — which sometimes reverses; (c) **disclosure** of your data and flag logs via a DSAR; (d) months later, **tribunal compensation** for a genuine failure to adjust or for discrimination (job applicants are covered even though never employed; the time limit is **three months less one day**, and **Acas Early Conciliation** is a mandatory first step). `[REGULATORY / INDEPENDENT — Acas]`
- **Highest-yield move, full stop:** request any adjustment **up front, in writing, before you sit.**

## Template letters

**(A) Pre-assessment reasonable-adjustment request — send *before* you sit:**
> Subject: Reasonable adjustment request — [name], [role/ref]
> Dear [Early Careers team],
> I have been invited to complete [SHL/Aon/HireVue/etc.] online assessment(s) for [role]. I am a disabled person within the meaning of the Equality Act 2010. The [timed format / webcam proctoring / gamified element] places me at a substantial disadvantage because [brief, factual barrier — e.g. "my dyslexia materially slows timed reading"]. Under the Act's duty to make reasonable adjustments, I request [specific adjustment — e.g. 25% additional time / a non-webcam-proctored version / an alternative format]. I can provide supporting documentation. Please confirm what can be arranged and any revised deadline. Thank you.

**(B) Auto-rejection: invoking the Article 22C safeguards:**
> Subject: Request for human review of an automated decision — [name], [ref]
> Dear [team],
> I understand my application was declined following an online assessment. If that decision was based solely on automated processing, I invoke my rights under Articles 22A–22C of the UK GDPR (as amended by the Data (Use and Access) Act 2025): I wish to make representations, to obtain human intervention in the decision, and to contest it. Please confirm whether a human with authority to overturn the outcome has reviewed my result, and arrange such a review. Thank you.

**(C) Data Subject Access Request (Article 15):**
> Subject: Data Subject Access Request — [name], [ref]
> Dear [Data Protection Officer],
> Under Article 15 of the UK GDPR I request access to the personal data you hold about my application, and specifically: my raw and scaled assessment scores and percentile/band; the norm group used; any cut-score applied and whether I met it; all proctoring and integrity flag logs (flag events, similarity scores, behavioural markers, IP/device logs); any webcam or screen recording and any AI-derived analysis of my responses; disclosure of any automated decision-making, meaningful information about the logic, and its consequences (Art. 15(1)(h)); and confirmation of whether and at what stage a human was involved. Please respond within one month. Thank you.

---

*Sources (accessed 2026-08-01): DUAA 2025 c.18 s.80 and Arts 22A–22D (legislation.gov.uk; gov.uk DUAA factsheet); ICO guidance on right of access, time limits, and automated decision-making; Equality Act 2010 ss. 19, 20–21, 60 (legislation.gov.uk); Acas indirect-discrimination and early-conciliation guidance; EU AI Act Annex III and the Digital Omnibus deferral (artificialintelligenceact.eu; Gibson Dunn, Cooley, DLA Piper); NYC Local Law 144 (NYC DCWP; Deloitte); Illinois AI Video Interview Act, 820 ILCS 42 (Justia; Littler); US UGESP 29 CFR Part 1607 (eCFR). Analyst notes and residual gaps — including that legislation.gov.uk and ico.org.uk pages were intermittently blocking automated fetches on the access date, and that final ICO ADM guidance was pending — are logged in research/20-legal-regulatory.md.*
