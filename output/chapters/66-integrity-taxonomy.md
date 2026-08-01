# Chapter 6.6 — Integrity Monitoring: The Cross-Provider Taxonomy

This chapter is the one to read if you have been screened out on integrity or proctoring grounds, or fear you might be. It consolidates the per-provider integrity sections (§x.8–x.10) into a single reference: a matrix of **what is monitored, by whom, and with what consequence**; the evidence on **false positives and demographic disparities**; and a **universal pre-flight checklist** that removes every avoidable ambiguity before you start. The governing principle throughout: the systems in UK finance early-careers assessment are **far less surveillant, and far less trigger-happy, than their reputation** — most flags are reviewed by a human, and the loudest online horror stories describe either high-stakes remote *exam* proctoring (a different, heavier product) or the legacy facial-analysis era that the main video vendor abandoned in 2021.

## The first thing to understand: most of these tests barely watch you

A recurring myth is that every online assessment films you through a locked-down browser and auto-rejects you for looking away. In the UK finance early-careers stack that is simply not how most of it works. The providers fall into three very different surveillance tiers, and knowing which tier you are in tells you almost everything about your real risk.

- **Tier A — statistical / design-based integrity, little or no live watching.** SHL's Verify range and Aon/cut-e rely primarily on **randomised per-candidate item banks** (your test differs from everyone else's, so shared answers are useless) and, for SHL, a **verification re-test** that catches a proxy statistically rather than by webcam. Game-based and behavioural tools — **pymetrics, Arctic Shores, Plum, Cappfinity** — are typically **unproctored** and are hard to fake *by design* rather than by monitoring. For these, there is often **no webcam layer at all**.
- **Tier B — lightweight behavioural telemetry, human-reviewed.** **HireVue** (async video) and **TestGorilla** (skills library) can log tab-switching, capture periodic webcam snapshots, and flag anomalies — but these are **optional, employer-enabled**, camera-and-audio only (not screen recording), and the flags go to a **human who decides**, not to an auto-reject.
- **Tier C — heavy live/AI proctoring.** Continuous webcam+screen recording, lockdown browsers, AI "suspicion" scoring. This is the tier the frightening research is about — but it is characteristic of **university exams and professional-certification testing**, and is **uncommon** in graduate finance OAs. If a finance employer uses it, they must tell you and obtain consent, which is itself the signal it is on.

The practical upshot: for the great majority of assessments you will sit in a UK finance process, the honest false-positive risk is **low** — and this chapter is about making it lower still, not about managing a hostile surveillance system.

## The signal × provider × consequence matrix

The table below consolidates what each provider is documented (or reasonably inferred) to monitor, and — the column that matters most — **how a flag is actioned.** "Consequence" is the difference between a note a recruiter may never read and an automatic rejection. Confidence tags carry over from the provider chapters; where a cell is `[UNKNOWN]` the provider does not document it and no reliable report established it.

| Provider | Proctoring flavour | Signals collected (where enabled) | How a flag is actioned | Told? |
|---|---|---|---|---|
| **SHL** (Verify) | Unsupervised + optional **verification re-test**; webcam proctoring a separate opt-in layer | Randomised item bank; **Confidence Indicator** (unsupervised vs supervised score gap); *if webcam enabled:* focus-loss/tab-switch, copy-paste, screen captures, face presence | "Not Verified" → **employer review** (vendor position) though top firms often reject on a large gap; single focus-loss treated holistically | Rarely told of a flag; consent to any webcam layer |
| **Aon / cut-e** | Mostly **unproctored**; webcam offered, not default | Unique per-candidate item bank; extreme time limits; tab-switch/clipboard telemetry `[UNKNOWN]` | Human review; no documented auto-reject | Usually not |
| **Arctic Shores** | **Unproctored / low-surveillance** by design | Behavioural telemetry (reaction time, learning rate) — *for measurement, not policing*; integrity mechanics `[UNKNOWN]` | n/a — little to flag | n/a |
| **pymetrics (Harver)** | **Unproctored**; hard-to-fake by design | Game telemetry; anti-cheat signals `[UNKNOWN]` | Fit-model match; no pass/fail to game | No |
| **Cappfinity** | **Largely unproctored** | Response-time capture, cross-response **consistency checks** | Soft — inconsistency weakens score; no webcam flag | No |
| **Plum** | **Unproctored** | Consistency/social-desirability inference `[INFERRED]`; explicit proctoring `[UNKNOWN]` | n/a | No |
| **HireVue** (video) | **Optional**, employer-enabled; camera+audio only | Browser focus / **tab-switch** logging; **webcam ID snapshots**; face-presence; possible response-similarity | Flag → **human at employer decides**; **no auto-reject** on a tab-switch; **no** eye-tracking/emotion analysis (dropped 2021) | Usually disclosed in T&Cs |
| **Willo** (video) | **Minimal** by design | Time-taken metadata incl. retakes; marketing claims of tab/gaze checks unverified `[UNKNOWN]` | Human-reviewed; small surface | Employer-configured |
| **TestGorilla** | **Anti-cheating suite** (a selling point) | **30-sec webcam snapshots**, full-screen/tab-switch, IP/location, copy-paste/screenshot/dev-tools, randomised retiring pools, timestamped behaviour log/tiers | Behaviour log + tiers → **employer decides**; vendor is candid that flags aren't proof | Candidate-facing notice `[UNKNOWN exact wording]` |
| **Amberjack** | Light; virtual-AC + one-shot human-scored video | `[UNKNOWN]` — not documented | Human-scored video component | `[UNKNOWN]` |
| **Morgan Stanley (firm-built stack)** | Inherits vendor postures (Aon/cut-e unproctored + HireVue optional) | As per Aon and HireVue rows | As per those vendors | As per those vendors |

Two patterns jump out. First, **the majority of the stack is unproctored or lightly monitored**, and **almost nothing auto-rejects** — the near-universal design is flag-then-human-review. Second, the one genuinely distinctive integrity mechanism is **SHL's verification re-test**, which is statistical, not surveillant: it is the only common mechanism where an *honest* candidate can be caught out (by under-performing on the supervised re-sit relative to the unsupervised one), which is why SHL's own manual insists a "Not Verified" be *investigated*, not treated as guilt.

## Genuine cheating that is reliably detected

Stated as risk, not instruction. Item randomisation defeats **shared answers**. SHL's verification re-test and Confidence Indicator defeat a **proxy sitting the unsupervised test**. ID snapshots defeat **someone else answering a video**. Focus/tab-switch logging plus response-similarity defeat **looking answers up or reading a script**. pymetrics-style games are defeated less by monitoring than by the fact that a **faked behavioural profile mismatches the model** it is aimed at. None of this is worth the risk; the entire value of this guide is legitimate preparation.

## The false-positive catalogue — how an honest candidate gets flagged

This is the section written specifically for you. Each item is a real, documented, or well-reasoned way that honest behaviour can be misread — concentrated in the Tier B/C settings, since Tier A rarely watches you at all.

- **Looking away to think or use scratch paper.** On any webcam-proctored deployment, sustained gaze-off-screen can register as a gaze/absence anomaly. Universal honest behaviour; naive detectors read it as evasion. (Note: HireVue's *algorithm* no longer scores gaze at all, but a human reviewer or a proctoring layer might.)
- **A second monitor connected but unused** — some proctoring/lockdown configs flag multiple displays.
- **Another person entering the room, or audible nearby** — a housemate, parent, or flatmate on a call trips second-face or audio flags.
- **Poor or backlit lighting** causing intermittent loss of your face — compounded by the documented reality that **face detection is less reliable for darker skin tones** (evidence below).
- **Glasses glare, a headscarf, or a face covering** confusing face-presence detection.
- **Disability-related movement** — tics, stimming, ADHD restlessness, or an autistic gaze pattern — misread as "suspicious."
- **A stutter or speech difference** on video — timed, no-re-record recording plus fluency-sensitive speech-to-text can under-score honest answers.
- **An unstable connection** producing focus-loss/disconnection events that look like tab-switching.
- **Browser notifications, an auto-updating OS, or work-laptop security software** stealing focus or being flagged as unauthorised software.
- **VPNs or corporate/university networks** producing IP/geolocation anomalies.
- **Answering unusually fast because you are genuinely good** — extremely fast, accurate responses can look "impossibly fast" to an anomaly detector.
- **A large score jump between an unproctored test and a supervised verification** (SHL) — which can happen honestly through nerves, illness or under-sleep, yet is exactly the pattern the Confidence Indicator flags.
- **Sitting in a library or shared space**, where other faces and movement are unavoidable.
- **Screen readers or assistive technology** read as unauthorised software.

## The evidence on demographic disparities in remote proctoring

This is not folklore, and it is a legitimate basis for requesting an alternative or adjustment in advance. Independent research and journalism have documented that facial-detection and face-matching systems perform **worse for darker-skinned users and for some disabled users**. The foundational study, **Buolamwini and Gebru's "Gender Shades" (2018)**, found commercial face-classification error rates of up to ~35% for darker-skinned women versus under 1% for lighter-skinned men; **NIST's Face Recognition Vendor Test** demographic evaluations subsequently confirmed accuracy gaps across skin tone, sex and age across many algorithms. `[INDEPENDENT]` Carried into proctoring, these gaps mean a darker-skinned candidate is more likely to trigger a "no face detected" flag or a failed identity check through no fault of their own. In the specific video-hiring context, **HireVue's own ORCAA audit** recommended investigating accent bias and noted that minority candidates giving brief answers were disproportionately routed to human review — a live fairness issue now that scoring is transcript-based (higher speech-to-text error rates for some accents). `[INDEPENDENT]` And HireVue's abandonment of facial analysis, after the **EPIC FTC complaint** argued the technology was "biased, unprovable, and not replicable," is itself the industry's clearest admission that face-based inference in hiring was not sound. `[INDEPENDENT]`

If you are in an affected group, the risk of a false flag is real and documented — which is not a counsel of despair but a concrete argument you can put in writing, in advance, to secure a non-webcam alternative or an adjustment (below, and Chapter 6.7).

## The universal pre-flight checklist

Print this. It applies to *any* proctored or webcam-enabled assessment; for unproctored tests most of it is simply good practice.

**Before the day**
- **Confirm the format in writing.** Ask the recruiter whether the test is **webcam-proctored**, whether **calculator and scratch paper** are permitted, and whether a **supervised verification test** will follow (SHL). Their answer tells you which risks apply and creates a record.
- **Request adjustments in advance** (Equality Act 2010) if you have any condition affecting movement, gaze, speech, reading speed, or that a webcam would disadvantage — before you sit, using the template in Chapter 6.7. This is the single most protective action in this chapter.

**The environment**
- A quiet room you can close, **door shut, a note on it**; no other person within earshot or camera range.
- **Lighting in front of you, not behind** — no window at your back. If webcam-enabled, check your face is evenly lit and fully in frame before starting.

**The device and network**
- Full-size laptop/desktop; **disconnect any second monitor**. Close every other application and browser tab. Enable Do Not Disturb / Focus mode. **Pause OS and antivirus auto-updates** for the window.
- The most **stable connection** you have — wired if possible; avoid a VPN and, where you can, a locked-down corporate network. Have a phone hotspot as backup but don't switch mid-test without noting it.

**On the desk and during the test**
- Keep only what the recruiter confirmed is permitted. If unsure, **ask rather than assume.**
- **Don't tab-switch.** If you must look away or leave frame on a proctored test, and the interface allows, **say aloud to the camera what you're doing** ("using scratch paper," "the doorbell rang") — it hands a human reviewer the innocent explanation up front.

## If a flag happens anyway

The consequence column of the matrix is your friend here: because almost nothing auto-rejects, a flag is usually a **human decision you can influence.** Ask the employer whether an integrity flag contributed; request **human review** and, where a rejection may have been solely automated, invoke the **Article 22A–22C safeguards** (UK GDPR as amended by the Data (Use and Access) Act 2025); and submit a **DSAR** for your flag logs, footage and decision logic. Full mechanics, templates and the realistic odds are in Chapter 6.7. The recurring lesson of this whole chapter: the systems are more forgiving than they look, the flags are mostly human-reviewed, and your rights and preparation together make a wrongful rejection genuinely contestable.

---

*Sources: consolidated from the per-provider chapters (2–11) and their research files; demographic-disparity evidence from Buolamwini & Gebru, "Gender Shades" (2018), NIST FRVT demographic evaluations, the HireVue ORCAA audit and EPIC FTC complaint (see Chapter 8), and the remote-proctoring critique literature. Full citations in the bibliography.*
