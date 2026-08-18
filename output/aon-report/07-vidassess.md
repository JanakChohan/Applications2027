# Chapter 7 — vidAssess-AI: The Video Interview

**What it is.** Aon's asynchronous ("one-way") video interview. The employer configures **up to 10 questions** — drawing on a bank of 600+ or writing their own — and, critically, sets **per question** the recording time and the **number of retries**. Questions are presented sequentially; you record your answers to camera in your own time before the deadline. `[VENDOR — product pages; PREP-VENDOR]` The classic "vidAssess" (without AI) also exists as plain competency-based video interviewing that humans review; "vidAssess-AI" adds the machine-scoring layer. `[VENDOR — cut-e deck lineage]`

## How it is marked — what the AI actually scores

The pipeline is documented, and its two most important facts cut in opposite directions:

1. **No facial analysis.** vidAssess-AI runs **speech-to-text transcription, then NLP scoring of the transcript** — it "scans the words spoken." Your face, expressions, eye movements and body language are **not** scored by the algorithm. `[VENDOR — explicit; consistent with the industry's post-2021 retreat from facial analysis, see the companion guide's HireVue chapter]`
2. **The NLP scores your words against personality constructs — specifically ADEPT-15's.** Per the ACLU's model cards, which cite Aon's own technical documentation: employers' questions are **mapped to specific ADEPT-15 constructs**, and the NLP **associates words and phrases in your transcript with those personality constructs**. In other words, the AI layer is not a generic "answer quality" grader — it is, in effect, **a language-based personality scorer**. `[INDEPENDENT — ACLU citing Aon technical documentation pp. 89–97; the strongest single finding in this chapter]`

Scores are reported to employers per competency/construct "in a variety of formats"; recruiters can also watch the recordings themselves, and whether a human reviews before decisions is an **employer configuration**, not a vendor guarantee. `[VENDOR; UNKNOWN per deployment]` Retakes: whatever the employer set per question — there is no universal retake right. `[VENDOR]`

## The fairness conflict — recorded both ways

Aon markets vidAssess-AI as fair and bias-minimising (and describes it as patented). The ACLU counters that **speech-to-text and NLP systems perform measurably worse for Black speakers, non-native English speakers, and speakers with speech or other disabilities** — so a transcript-scoring pipeline risks importing transcription error into personality inference, compounding the ADEPT-15 concerns of Chapter 6. Unadjudicated; both recorded. `[VENDOR vs INDEPENDENT]` The practical protections for an affected candidate: speak slightly slower and more clearly than feels natural (cleaner transcription is directly in your interest since *words are the only signal*), give full-length answers (thin transcripts are thin evidence), and request an adjustment or alternative format in advance where a speech difference or disability is in play.

## How to win

Everything from the companion guide's async-video method applies (Chapter 8 there: STAR/CARL structure, headline-first openings, ~100–125 words per minute, story bank, lens-eye-contact for the human reviewer). The vidAssess-specific edge comes from knowing what the machine reads:

- **Your words are the entire algorithmic signal.** Polish the *content*: concrete actions, first-person ownership ("I analysed… I decided…"), results with numbers, and vocabulary that reflects the competencies the question is transparently probing (a resilience question is looking for the language of persistence, learning and composure — say the substance, and the words follow).
- **Fill the allotted time with substance.** Transcript-based scoring cannot reward what you didn't say; a 30-second answer to a 2-minute window is self-sabotage.
- **Use your retries deliberately** where the employer allows them: first take for structure, second for delivery. Whether reviewers see the number of takes is undocumented `[UNKNOWN]` — assume they might and don't burn ten.
- **Don't script and read.** Flat, read-aloud delivery is obvious to human reviewers, and bullet-prompt speaking produces more natural, better-transcribed speech anyway.

## Anti-cheat notes

vidAssess **cannot be combined with Aon's virtual proctoring** — the flyer states proctoring "cannot be added to those assessments which already access the device's camera." The camera itself is the integrity layer: you are visibly you, on the record. `[VENDOR]` The realistic integrity checks are identity (the recording), response-similarity to coached scripts (undocumented for Aon, `[UNKNOWN]`), and simple human review. The honest-candidate rules: sit it alone, front-lit, on a stable connection; notes as bullet prompts beside the camera, not scripts in front of it.
