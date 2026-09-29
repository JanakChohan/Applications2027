#!/usr/bin/env python3
"""Figures for Part 11 (scenario playbook)."""
import os
from svglib import *
from gen_playbook import LADDER

ROOT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(ROOT, "fragments")


def save(name, s):
    open(os.path.join(FR, f"fig_{name}.html"), "w").write(s)


def protocol():
    steps = [("1  STEADY", "0 to 5 s", "Breathe out. Repeat the core of the question.", "\"So the client is unhappy about the report, and wants an answer today.\"", S[0]),
             ("2  SORT", "5 to 20 s", "Name what collides and apply the priority order.", "\"Two things matter here: the rules on what I can send, and the client's deadline.\"", S[2]),
             ("3  ACT", "20 to 55 s", "Say what you would do, in order, and who you'd tell.", "\"First I'd tell my manager, then I'd chase approval, then I'd update the client with a time.\"", ACC),
             ("4  CLOSE", "55 to 75 s", "State the principle and the outcome. Stop talking.", "\"That way the client gets it fast and gets it right.\"", OPI)]
    out = [arrow_defs("p")]
    x = 6
    for i, (t, tm, what, ex, col) in enumerate(steps):
        out.append(f'<rect x="{x}" y="10" width="158" height="210" rx="5" fill="#fff" stroke="{col}" stroke-width="2"/>')
        out.append(f'<rect x="{x}" y="10" width="158" height="36" rx="5" fill="{col}"/>')
        out.append(f'<rect x="{x}" y="40" width="158" height="6" fill="{col}"/>')
        out.append(text(x + 10, 33, t, 13, "#fff", weight=700)[0])
        out.append(text(x + 10, 64, tm, 10, col, weight=700)[0])
        out.append(text(x + 10, 84, what, 10.5, INK, width=27)[0])
        out.append(text(x + 10, 146, ex, 9.5, INK2, width=29, italic=True)[0])
        if i < 3:
            out.append(line(x + 160, 115, x + 170, 115, "p"))
        x += 170
    out.append(text(340, 246, "Total: 45 to 75 seconds. Longer than 90 seconds and you lose the room; shorter than 30 and you skipped a step.", 10, INK2, "middle")[0])
    save("protocol", figure(svg(680, 256, "".join(out)),
        "The four-step answer protocol for any scenario. Timings are a coaching heuristic built for this pack [Inferred], not a Schroders rule."))


def priority():
    tiers = [("1. The rules and Schroders' name", "Regulation, approvals, confidentiality, inside information. Never traded for anything below.", HARD, 300),
             ("2. The client's real interest", "Good outcomes, fair treatment, honest answers. Consumer Duty makes this a rule for retail clients.", S[0], 380),
             ("3. Fair service to every colleague, the process and the record", "Nobody jumps the queue by volume or rank. Log it, tell people early.", S[2], 460),
             ("4. Speed", "As fast as possible inside 1 to 3. Speed is the variable you flex.", ACC, 540)]
    out = []
    y = 8
    for t, sub, col, w in tiers:
        x = (680 - w) / 2
        out.append(box(x, y, w, 50, t, col, col, "#fff", 12, 700, sub=sub, subsize=9.5, subcol="#fff"))
        y += 58
    out.append(text(340, y + 16, "The one sentence that holds every frame:", 10.5, INK2, "middle", 700)[0])
    out.append(text(340, y + 34, "\"I won't trade the rules or the client's interest for speed. Inside those, I'll be as fast and as helpful as I can, and I'll tell people early.\"", 11, OPI, "middle", 600, width=110)[0])
    save("priority", figure(svg(680, y + 60, "".join(out)),
        "Priority order when good things collide in a Client Group seat. Built by the author from the JD and the FCA rules in Part 6 [Inferred]."))


def tactics():
    items = [("Interruption", "They cut in mid-answer.", "Stop. \"Sure.\" Answer the new point in one line, then: \"To finish my first point...\""),
             ("Flat contradiction", "\"That's wrong.\"", "\"Tell me more.\" If they're right, update. If not: \"I see it differently, because...\""),
             ("Silence", "They say nothing after you finish.", "Don't fill it with a new answer. Wait three seconds, then: \"Would it help if I went deeper on any part?\""),
             ("Escalation", "\"And now the client threatens to leave.\"", "Same priority order, bigger stakes. Escalate to your manager sooner, not the rules later."),
             ("Authority squeeze", "\"The MD says just do it.\"", "\"I'll do it the moment it's approved, and I'll chase approval now.\" Rank doesn't change the rule."),
             ("False choice", "\"Break the rule or lose the client?\"", "Find the third door: \"Neither. I'd tell the client when they'll get it, and get it approved fast.\""),
             ("Knowledge trap", "A fact question you can't answer.", "\"I don't know that figure. Here's how I'd find it, and here's what I do know.\""),
             ("Invitation to badmouth", "\"Isn't [rival / old boss] a bit useless?\"", "Stay generous and specific: \"They do X well. What I'd do differently is...\"")]
    out = []
    for i, (t, how, counter) in enumerate(items):
        c, r = i % 2, i // 2
        x, y = 6 + c * 338, 6 + r * 92
        out.append(f'<rect x="{x}" y="{y}" width="330" height="84" rx="4" fill="#fff" stroke="{LINE}"/>')
        out.append(f'<rect x="{x}" y="{y}" width="6" height="84" rx="2" fill="{HARD}"/>')
        out.append(text(x + 14, y + 17, f"{i+1}. {t}", 11.5, NAVY, weight=700)[0])
        out.append(text(x + 14, y + 33, how, 9.5, HARD, italic=True, width=60)[0])
        out.append(text(x + 14, y + 50, counter, 9.5, INK, width=64)[0])
    save("tactics", figure(svg(680, 376, "".join(out)),
        "Eight ways assessors break a frame, with the counter to each. Author's synthesis of common interview practice [Inferred]."))


def ladder():
    out = []
    cols = [("Easy", EASY), ("Medium", MED), ("Hard", HARD)]
    out.append(text(8, 16, "JD line", 10, INK2, weight=700)[0])
    for j, (c, col) in enumerate(cols):
        out.append(text(214 + j * 156 + 74, 16, c.upper(), 10, col, "middle", 700)[0])
    y = 24
    for i, (label, jd, scen) in enumerate(LADDER):
        out.append(f'<rect x="4" y="{y}" width="672" height="34" fill="{WASH if i%2==0 else "#fff"}"/>')
        out.append(text(10, y + 21, f"{i+1}. {label}", 10.5, NAVY, weight=600)[0])
        for j, (c, col) in enumerate(cols):
            x = 214 + j * 156
            out.append(box(x, y + 3, 148, 28, scen[j][0], "#fff", col, INK, 8.6, sw=1.4))
        y += 36
    save("ladder", figure(svg(680, y + 6, "".join(out)),
        "The scenario ladder: every JD line in this role, three rungs from easy to hard. Full cards follow. Scenarios are the author's constructions from the JD [Inferred]."))


TREES = {
 "shout": ("Two senior salespeople both demand the one fund-manager slot",
  dict(t="Two seniors want the same scarce slot", kids=[
    dict(edge="step 1", t="Is there a written rule for allocation?", kids=[
      dict(edge="yes", kind="go", t="Apply it. Tell both what the rule says and when."),
      dict(edge="no", t="Can you split or add a slot?", kids=[
        dict(edge="yes", kind="go", t="Offer both options in writing within the hour."),
        dict(edge="no", kind="a", t="Put both cases to the diary owner or your manager. They decide.")])])])),
 "skip": ("A senior person asks you to skip a control",
  dict(t="Senior asks you to send, book or change something without the usual approval", kids=[
    dict(edge="check", t="Is the step a rule or approval (compliance, data, sign-off)?", kids=[
      dict(edge="yes", t="Can approval be sped up today?", kids=[
        dict(edge="yes", kind="go", t="Chase it now. Tell the senior the time."),
        dict(edge="no", kind="stop", t="Do not skip. Tell your manager. Offer an interim message to the client.")]),
      dict(edge="no", kind="go", t="It's a habit, not a rule. Do it faster; mention it to your manager after.")])])),
 "mnpi": ("You hear something that might be confidential or inside information",
  dict(t="You overhear possible price-sensitive or confidential information", kids=[
    dict(edge="step 1", t="Could it be non-public and affect a price, or is it client-confidential?", kids=[
      dict(edge="maybe", kind="stop", t="Do not repeat, trade or forward it. Write down what, when, who. Tell Compliance or your manager today."),
      dict(edge="clearly no", kind="go", t="Treat it as normal business information, still need-to-know only.")])])),
 "mistake": ("You made a mistake",
  dict(t="You find an error in your own work", kids=[
    dict(edge="step 1", t="Has it reached a client or a decision-maker?", kids=[
      dict(edge="yes", kind="stop", t="Tell your manager now with the fix. They decide client contact. Log it."),
      dict(edge="no", t="Does anyone else rely on it?", kids=[
        dict(edge="yes", kind="a", t="Fix it, then tell them what changed."),
        dict(edge="no", kind="go", t="Fix it and note the lesson.")])])])),
 "deadline": ("Incomplete information against a deadline",
  dict(t="Deadline in 1 hour, key data missing", kids=[
    dict(edge="step 1", t="Is the output going to a client or regulator?", kids=[
      dict(edge="yes", kind="stop", t="Only verified, approved figures. Ask for more time or send with the gap stated."),
      dict(edge="no, internal", t="Can you get 80% right on time?", kids=[
        dict(edge="yes", kind="go", t="Send on time, flag assumptions in line one."),
        dict(edge="no", kind="a", t="Tell the requester now, agree a new time or scope.")])])])),
}


def trees():
    for k, (cap, root) in TREES.items():
        save(f"tree_{k}", figure(tree(root, uid=k, size=9.5),
            f"Decision tree: {cap}. Draw it from memory: the question at each node is what matters. Author's construction from FCA principles cited in the text [Inferred]."))


def calm():
    pass


if __name__ == "__main__":
    protocol(); priority(); tactics(); ladder(); trees()
    print("playbook figs done")
