# Acceptance test, open questions and limits

This chapter holds the project to its own standard. It answers the nine acceptance questions from the brief, lists what is still unresolved, and shows topic by topic what was investigated and what was not.

## The nine acceptance questions

Each answer says where the evidence is and where the project falls short. "Yes" is only claimed where you can check it yourself by doing the test described.

| Question | Honest answer | How to check it yourself |
|---|---|---|
| Can a beginner explain the business without memorising jargon? | The material is there: chapter 1 teaches each idea from first principles before any acronym is used, and the glossary defines every term in plain English. Whether you can explain it is a test only you can run | Close the file and explain to someone outside finance how a pension scheme's money reaches an asset manager and how the manager is paid |
| Can the reader distinguish sales, relationship management and adjacent roles without oversimplifying? | Yes for the general industry picture (chapters 2 and 6, role comparison). For Goldman specifically, the published evidence shows the labels overlap, and the internal split is not public | Compare any two roles in the Role comparison view and say what each can decide alone |
| Can the reader connect a junior task to a client outcome and a commercial consequence? | Yes. Every lifecycle stage lists what the junior person produces and what good execution changes, and the sample work products show the documents | Pick the meeting preparation note in chapter 7 and trace it to the mandate's fee in the calculator |
| Are the organisational claims, people and mandates supported, not invented? | Supported where sources exist, and marked where they do not. Several posts have no publicly established holder, and no mandate is attributed to a London team because no source does so | Open any team, person or mandate and follow its source link |
| Can every statement about trust, relationships, value or passion be translated into an action, a difficult choice or a concrete preference? | Chapter 7 ends with a translation table that does this word by word. Passion is deliberately not asserted anywhere | Take any sentence containing "trust" in your own draft answers and replace it using the table |
| Can the motivation arguments withstand repeated questioning without becoming circular? | The nine why-trees are built so that each question challenges the previous answer and each tree ends in a stated preference, assumption or uncertainty. Your own answers are untested until you give them | Answer each level aloud before opening it. Note where you repeat yourself |
| Does the material distinguish a strong business argument from evidence of personal fit? | Yes, structurally. Layer B and Layer C are labelled apart, and the personal ledger is empty by design | Check that nothing in your answers uses "the role is valuable" as proof that you would enjoy it |
| Does it explain when a client should not buy, when a mandate should shrink and when a different career might fit better? | Yes: chapter 7 on when a relationship should end, the withdrawal cases in chapter 5, and the "different role" signal at the end of each why-tree | Find the three passages and summarise each in two sentences |
| Do the dossier, website and PDF agree, and are their limits explicit? | They are generated from the same files by one script, so they cannot drift apart. Limits are stated in chapter 0 and below | Run `python3 build/build.py --pdf` and compare any entity ID across the three outputs |

## What was verified, and what stayed open

The audit of the former intern's account, claim by claim:

<!-- DATA:intern-claims -->

## Research coverage register

Each row is a topic from the brief. "Complete" means the planned sources were read. "Partial" means some evidence was found and more exists. "Searched, not established" means it was looked for and not found in public sources. "Not investigated" means nobody has looked yet.

<!-- DATA:coverage-register -->

## Open questions worth resolving before an interview

These are the gaps most likely to matter in conversation, with the fastest way to close each.

1. **The current London listing.** The exact 2027 London listing carried only programme-wide wording when it was read on a mirror, and it was no longer among the live campus listings on 14 November 2026 [@R1-S03]. Check your own application portal for the wording and any team information it shows you.
2. **How Client Solutions Group and Client Coverage Group relate in London.** Both names are real. Their reporting relationship is not published. A neutral question to ask an interviewer: "How do the sales and client coverage roles divide the work on your team?"
3. **Who leads UK institutional coverage and UK & Ireland third-party wealth today.** Neither post has a publicly established current holder. A departure from the EMEA third-party wealth leadership was reported in April 2026, with no successor found in public sources.
4. **Which OCIO award the former intern saw.** Two 2026 awards fit. Do not name one as fact.
5. **Analyst pay.** The two figures in the starting account have no public support. Do not build any argument on them.
6. **The interview format this cycle.** Goldman publishes the general shape of its process. Whether this team's final round is in person, and what it asks about AI, is not established. Prepare for both.

## Limits of this project

- **It is not exhaustive.** The people directory is a sample of publicly visible professionals. The mandates register holds what was found in the time and search allowance available. Neither should be described as complete.
- **It is dated.** Every figure is correct to the date beside it. The rates backdrop changed in the week before the cutoff, which shows how quickly a commercial-awareness point can go stale.
- **It contains interpretation.** Layer B passages are arguments. A well-informed interviewer may disagree with some of them, and a reasoned disagreement is a good conversation to have.
- **It cannot assess you.** Practice scores are self-assessed against a proposed framework. Goldman Sachs has not published scoring criteria, and nobody outside the firm knows the questions.
- **It was partly written by automated research and drafting.** Every claim carries a source or a label so that you can check it. Open the source for anything you intend to say aloud.

## What was tested

The application and PDF were checked by an automated script and by inspecting rendered pages. The README lists every check and its result. In brief: navigation, search, filters, expandable sections, the fee calculator's arithmetic against an independent implementation, keyboard access, mobile layout, reduced-motion behaviour, and that the file makes no network requests. The PDF was rendered and its pages inspected for clipped text and broken tables.

No part of this project has been published or hosted. The HTML file is a local file. If you choose to share it, check the source register and the people directory first and decide what you are comfortable circulating.
