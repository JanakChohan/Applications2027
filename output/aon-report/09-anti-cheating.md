# Chapter 9 — The Anti-Cheating Architecture

This is the report's flagship chapter, built substantially from **Aon's own documents** — the cut-e design deck and the Virtual Proctoring flyer — rather than folklore. Aon's integrity model is unusual and worth understanding precisely, because it is **preventive by design rather than surveillant by default**: the system is built so that cheating barely pays, monitoring is a bolt-on the employer chooses, and verification (not accusation) is the endgame. For an honest candidate — especially one who has been falsely flagged elsewhere — this is one of the most benign integrity environments in the industry. Here is the whole machine, layer by layer.

## Layer 1 — Design security: tests that make cheating pointless

The vendor's own instrument-security principles, verbatim from its design deck `[VENDOR — primary]`:

- **"Item generation"** — test items are generated rule-based/parameterised, not drawn from a small static pool;
- **"Individual parallel versions (sample solutions do NOT exist!)"** — every candidate receives a psychometrically parallel but *different* test;
- **"Cheat-proof — our unique technology ensures that a different test is generated for each participant"** (the scales marketing line);
- **adalloc™** randomisation extends item-level variation even into the personality questionnaires.

The consequences are structural. **Leaked question banks and answer keys are worthless** — there is no fixed form to leak. **Collusion between candidates fails** — your friend's test was not your test. On the adaptive instruments (lst, the four games, shapes, ADEPT-15) the test's *path* additionally depends on your own answers, so no two sittings are even structurally identical. And the extreme time pressure does quiet integrity work too: with ~15 seconds per item, a helper on a second device or a lookup adds latency the format cannot absorb — though note honestly that the vendor sells short-timed tests as *efficiency*, and the anti-collusion effect is inference and prep-vendor commentary rather than a vendor claim. `[VENDOR + INFERRED/PREP-VENDOR]`

The exceptions matter: **chatAssess scenarios and squares items are fixed per employer build**, not per-candidate randomised — so within one employer's cycle, answer-sharing is *theoretically* possible there. The countermeasures are employer-specific keys (a shared "best answer" from another firm or year is simply wrong), content refresh, and latency telemetry. `[INFERRED + PREP-VENDOR; specifics UNKNOWN]`

## Layer 2 — Platform telemetry: what mapTQ logs on everyone

Two things are documented, one of them a finding this report can state with unusual confidence:

- **Session logging** — time in assessment, connectivity, actions; a started test cannot be paused or resumed, and closing/refreshing/back-navigating can **block you from the test**. `[VENDOR-VIA-CLIENT — mapTQ candidate instructions]`
- **Window-switch telemetry exists platform-wide — including on unproctored sittings.** The proof is in Aon's own proctoring flyer, which reports the percentage of candidates who "switched away from the active test window" in **both** proctored **and unproctored** settings (12.3% vs 19.4% — see Layer 3). You cannot report a number you did not measure: **mapTQ logs tab/window focus regardless of whether proctoring is on.** `[VENDOR — deduced directly from Aon's own published statistics]`

What is *not* documented: clipboard monitoring, IP/device fingerprinting, or post-hoc statistical data-forensics beyond the photo-comparison ratings below — all `[UNKNOWN]`. The honest reading is that Aon's telemetry is real but narrow, and nothing suggests a hair-trigger.

## Layer 3 — Optional monitoring: Aon "Virtual Proctoring", fully documented

Where an employer switches it on, Aon's virtual proctoring runs a four-step, consent-first workflow `[VENDOR — the proctoring flyer, full text]`:

1. **Consent** — you are asked to agree to proctoring before anything is captured;
2. **Reference photo** — one identity snapshot;
3. **"Protecting"** — further webcam **photos periodically throughout the assessment** (snapshots, *not* continuous video);
4. **Rating** — the "Eye in the Sky" system compares photos and **flags inconsistencies** — is it the same person throughout, is a second face or a phone visible — producing an algorithmic *likelihood* rating, not a verdict.

It also watches navigation ("spots those who may be accessing other sites"). Critically, **the employer — not Aon — decides everything consequential**: whether proctoring is mandatory or opt-out-able, and what happens on a flag. It cannot run on vidAssess (the camera is already in use). Refusal-consequences are therefore employer policy; if you have privacy concerns, the flyer's own framing gives you standing to ask the recruiter what the opt-out means in practice. `[VENDOR]`

**Aon's own numbers (internal study, n > 30,000, self-reported)** `[VENDOR study]`:

| Signal | Unproctored | Proctored |
|---|---|---|
| "Moderate cheating likelihood" rating | **6.52%** | 2.25% |
| "High cheating likelihood" rating | 0.07% | 0.02% |
| Switched away from test window ≥ once | **19.4%** | 12.3% |

Read these carefully, because they contain the false-positive story the vendor doesn't spell out. First, base rates are tiny — genuine high-likelihood flags are seven in ten thousand. Second, **"likelihood of cheating" is an algorithmic photo-comparison rating, not confirmed cheating** — the gap between 6.52% flagged and any plausible real cheating rate *is* an unquantified false-positive surface. Third, one in five honest unproctored candidates switched windows at least once — notifications, accidental keystrokes, connection hiccups — which is exactly why a single focus-loss cannot be, and per all available evidence is not, treated as guilt. `[INFERRED from the vendor's own figures]`

## Layer 4 — Verification: the endgame is a re-test, not an accusation

The design deck states it in five words: **"onsite re-test for verification is possible."** `[VENDOR — verbatim]` Because every sitting generates a fresh parallel form, an employer who doubts an online score can simply re-test the candidate under supervision — at the assessment centre, on a new form the candidate has never seen — and compare. Whether Aon currently productises this as a formal statistical verification service (à la SHL's Confidence Indicator) is `[UNKNOWN]`; the capability is inherent in the parallel-forms design, and prep sources echo it at the behavioural level too: distorted questionnaire answers "might get further questions at a later stage for verification." For you this is the single most useful fact in the chapter: **an honest candidate's best insurance is that they can always reproduce their score.** If you are ever doubted, *ask for the supervised re-sit* — it is the system working as designed, in your favour.

## What happens on a flag — and what you're told

Undocumented, honestly: `[UNKNOWN]`. The employer receives the proctoring ratings and evidence; no documentation describes automatic rejection, and Aon's structural posture (prevent, then verify) argues against it — but consequences are employer policy, and **no source documents candidates being told they were flagged.** No false-positive cases specific to Aon's proctoring are documented anywhere `[UNKNOWN — absence]`. The adjacent, well-documented dispute is different in kind: the **ACLU's 2024 FTC complaint and EEOC charges** concern alleged *construct* unfairness (disability, race) in gridChallenge, ADEPT-15 and vidAssess-AI — assessment fairness, not cheat-flagging — and is recorded both ways in Chapters 4, 6 and 7.

## The honest candidate's checklist (Aon-specific)

The environment is low-surveillance; the risks are technical and behavioural, not paranoid:

- **One protected sitting per test** — no pause, no resume; stable connection, ideally wired; close everything else *before* launching (window-switch is logged even unproctored — give it nothing to log).
- **Never close, refresh or back-navigate** — mapTQ can block you.
- **Calculator and rough paper are officially fine** for the numerical test — no need to hide ordinary working; where a calculator isn't allowed, you'll be told.
- **If proctoring is on**: consent screens tell you; front-light your face, clear the frame of other people and phones, and don't leave frame without need.
- **Answer questionnaires as one consistent, authentic persona** — cross-instrument consistency is the behavioural integrity check, and your interviewers will hold your profile.
- **If flagged or doubted, request the supervised re-test** — the architecture's own remedy, and the honest candidate's friend.
- **Adjustments in advance, in writing, via the employer** — extra time for dyslexia and screen magnifiers are documented accommodations, case-by-case `[VENDOR-adjacent]`; the request also creates the paper trail that protects you if anything downstream is ever misread.
