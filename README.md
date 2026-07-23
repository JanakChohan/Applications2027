# Applications2027

A Claude Code prompt pack for writing truthful, specimen-grade cover letters.

The engine works on one principle: a letter can only be as specific as what is
genuinely true about you and about the firm. It researches the firm hard, finds
the strongest **real** overlap with your own history, and refuses to paper over an
absent connection with filler. When you have nothing true and specific to say, it
tells you to go get it — a fifteen-minute call with an analyst — rather than write
around the gap.

## What's here

```
.
├── .claude/commands/coverletter.md   # the /coverletter slash command (the engine)
├── profile.md                        # your fact base — the ONLY source of claims about you
└── examples/                         # gold-standard specimen letters (add optiver.md)
    └── README.md
```

## Setup (once)

1. Fill in `profile.md` — contact block, current role, experience bank, technical
   and academic background, your personal thesis, network log, and constraints.
   The command reads this every time and will not claim anything about you that it
   cannot trace back to this file. Richer input, better letters.
2. (Optional) Drop your best real cover letter into `examples/optiver.md`. It
   becomes the register the engine writes toward. See `examples/README.md`.

## Usage

From this directory, run `claude` and invoke the command with the firm details
inline:

```
/coverletter Firm: Cinven. Role: Investment Analyst, London. JD pasted below...
```

The engine then works in four phases and will not skip ahead to drafting:

1. **Research** — 8–20 web searches to build a firm dossier that goes well past
   the homepage, then a short briefing back to you.
2. **Connect, then interrogate** — it ranks the truest possible spine for the
   letter (Tier 1 worked there → Tier 5 no connection), then asks you up to six
   questions and **waits for your answers**.
3. **Draft** — bespoke narrative for a strong connection, upgraded three-paragraph
   for a weaker one, always inside the voice-and-form rules.
4. **Self-critique** — find-and-replace test, invention audit, "so what" pass,
   register check, and a one-page word count — fixed before you ever see it.

It delivers the finished letter plus **Sources**, **Unverified**, and
**Weakest link** notes so you can verify every claim before sending.

## Two honest caveats

- **Tier 5 is common** and the engine is deliberately unhelpful about it. For most
  firms you'll have no internship, no conversation, no alumnus — and it will tell
  you to go get one rather than fake it.
- **Research quality is the ceiling.** The letter can only be as specific as the
  dossier. If a briefing comes back thin, push it: name the trade publications,
  point it at founder letters or engineering blogs, ask for the division's real
  mandate rather than the group's marketing copy.
