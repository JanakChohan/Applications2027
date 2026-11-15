"""Small hand-laid SVG diagrams for the beginner primer.

Each diagram is boxes, arrows and plain words. Colours come from CSS variables, so the same
SVG reads correctly in the dark app, the light app and the printed PDF. Meaning never depends
on colour: every box is labelled and every diagram has an "In words" caption underneath.
"""
import html
import textwrap

W = 760
FS = 15.5      # body text size inside diagrams (viewBox units)
LH = 20        # line height


def esc(s):
    return html.escape(str(s), quote=True)


class Dia:
    def __init__(self, key, height, title, in_words):
        self.key, self.h, self.title, self.words, self.parts = key, height, title, in_words, []

    def box(self, x, y, w, h, head, body="", kind="a", align="middle"):
        """kind: a = plain, b = tinted, c = dashed outline (an adviser or outside party)."""
        cx = x + w / 2 if align == "middle" else x + 12
        chars = max(8, int((w - 18) / (FS * 0.56)))
        head_lines = textwrap.wrap(head, chars) if head else []
        body_lines = [ln for para in str(body).split("\n") for ln in (textwrap.wrap(para, chars) or [""])] if body else []
        total = len(head_lines) + len(body_lines)
        need = total * LH + 18
        if need > h:                       # grow evenly up and down so arrows aimed at the middle still meet it
            y -= (need - h) / 2
            h = need
        self.parts.append(f'<rect x="{x}" y="{y:.1f}" width="{w}" height="{h:.1f}" rx="10" class="dg-box dg-{kind}"/>')
        ty = y + (h - total * LH) / 2 + LH * 0.75
        for ln in head_lines:
            self.parts.append(f'<text x="{cx}" y="{ty:.1f}" text-anchor="{align}" class="dg-h">{esc(ln)}</text>')
            ty += LH
        for ln in body_lines:
            self.parts.append(f'<text x="{cx}" y="{ty:.1f}" text-anchor="{align}" class="dg-t">{esc(ln)}</text>')
            ty += LH
        return self

    def arrow(self, x1, y1, x2, y2, label="", dashed=False, lx=None, ly=None, anchor="middle"):
        cls = "dg-arrow dg-dash" if dashed else "dg-arrow"
        self.parts.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" marker-end="url(#ah-{self.key})"/>')
        if label:
            lx = (x1 + x2) / 2 if lx is None else lx
            ly = (y1 + y2) / 2 - 7 if ly is None else ly
            for i, ln in enumerate(label.split("\n")):
                self.parts.append(f'<text x="{lx}" y="{ly + i * (LH - 2):.1f}" text-anchor="{anchor}" class="dg-s">{esc(ln)}</text>')
        return self

    def path(self, d, dashed=False):
        cls = "dg-arrow dg-dash" if dashed else "dg-arrow"
        self.parts.append(f'<path d="{d}" class="{cls}" fill="none" marker-end="url(#ah-{self.key})"/>')
        return self

    def text(self, x, y, s, cls="dg-t", anchor="middle"):
        for i, ln in enumerate(str(s).split("\n")):
            self.parts.append(f'<text x="{x}" y="{y + i * LH}" text-anchor="{anchor}" class="{cls}">{esc(ln)}</text>')
        return self

    def html(self):
        return (f'<figure class="diagram" id="dg-{self.key}"><figcaption class="dg-title">{esc(self.title)}</figcaption>'
                f'<svg viewBox="0 0 {W} {self.h}" role="img" aria-label="{esc(self.title)}. {esc(self.words)}" preserveAspectRatio="xMidYMin meet">'
                f'<defs><marker id="ah-{self.key}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
                f'<path d="M0,0 L10,5 L0,10 z" class="dg-head"/></marker></defs>{"".join(self.parts)}</svg>'
                f'<p class="dg-words"><strong>In words:</strong> {esc(self.words)}</p></figure>')


def money_chain():
    d = Dia("money", 370, "Whose money is it, and where does it go?",
            "People need money in the future. An institution such as a pension scheme holds it for them. The institution hires an asset manager "
            "to invest it, often on the advice of an investment consultant. The manager is paid a small yearly percentage. Any gains belong to the people, not the manager.")
    xs = [10, 200, 390, 580]
    d.box(xs[0], 40, 170, 130, "1. The people", "Workers saving for a pension, a charity, a country's citizens")
    d.box(xs[1], 40, 170, 130, "2. The client", "A pension scheme, charity, insurer or state fund holds the money", "b")
    d.box(xs[2], 40, 170, 130, "3. The asset manager", "Invests the money, following the client's rules", "b")
    d.box(xs[3], 40, 170, 130, "4. The markets", "Shares, bonds, property, loans, private companies")
    for i in range(3):
        d.arrow(xs[i] + 170, 105, xs[i + 1], 105)
    d.box(250, 245, 260, 76, "Investment consultant", "Advises the client on which manager to choose", "c")
    d.arrow(380, 245, 380, 204, dashed=True)
    d.text(380, 26, "Money to invest moves this way  →", "dg-s")
    d.path("M665,170 V202 H95 V172", dashed=False)
    d.text(745, 224, "Gains and income return to the people", "dg-s", "end")
    d.text(380, 350, "The manager's pay: a small percentage of the assets each year", "dg-s")
    return d.html()


def where_csg_sits():
    d = Dia("where", 490, "Where the team sits inside Goldman Sachs",
            "Goldman Sachs reports three business segments. Asset and Wealth Management is one of them. Inside it, asset management has people who choose "
            "investments and people who look after clients. The Client Solutions Group is the client side. Wealth management, a separate business, serves rich individuals directly.")
    d.box(10, 10, 740, 54, "Goldman Sachs (the whole firm)", "", "a")
    d.box(10, 90, 230, 78, "Global Banking & Markets", "Advises companies, trades for clients")
    d.box(265, 90, 230, 78, "Asset & Wealth Management", "28.6% of 2025 net revenues", "b")
    d.box(520, 90, 230, 78, "Platform Solutions", "A smaller third segment")
    for x in (125, 380, 635):
        d.arrow(x, 64, x, 90)
    d.box(140, 200, 230, 78, "Asset management", "Manages money for institutions and funds", "b")
    d.box(400, 200, 230, 78, "Wealth management", "Advises wealthy individuals directly")
    d.arrow(340, 168, 270, 200)
    d.arrow(420, 168, 500, 200)
    d.box(10, 320, 230, 96, "Investment teams", "Decide what to buy and sell. Portfolio managers and analysts")
    d.box(265, 320, 230, 96, "Client Solutions Group", "Finds clients, wins mandates, looks after existing clients", "b")
    d.box(520, 320, 230, 96, "Clients", "Pension schemes, insurers, state funds, banks and wealth managers", "c")
    d.arrow(200, 278, 140, 320)
    d.arrow(300, 278, 370, 320)
    d.arrow(495, 368, 520, 368)
    d.arrow(240, 368, 265, 368)
    d.text(380, 446, "You are applying to the tinted path:\nAsset & Wealth Management → asset management → Client Solutions Group", "dg-s")
    return d.html()


def two_routes():
    d = Dia("routes", 350, "Two routes to the people whose money it is",
            "On the institutional route the team deals with the organisation that owns the money, such as a pension scheme, usually with a consultant advising it. "
            "On the wealth route the team deals with another firm, such as a private bank, whose advisers then offer the fund to their own customers.")
    d.text(15, 30, "Route 1: Institutional", "dg-h", "start")
    d.box(10, 45, 160, 80, "Client Solutions Group", "institutional team", "b")
    d.box(215, 45, 160, 80, "Trustees or investment staff", "decide")
    d.box(420, 45, 160, 80, "The scheme's money", "one large mandate")
    d.box(610, 45, 140, 80, "Members", "get pensions")
    d.arrow(170, 85, 215, 85); d.arrow(375, 85, 420, 85); d.arrow(580, 85, 610, 85)
    d.box(215, 138, 160, 34, "Consultant advises", "", "c")
    d.text(15, 212, "Route 2: Third Party Wealth", "dg-h", "start")
    d.box(10, 240, 160, 80, "Client Solutions Group", "wealth team", "b")
    d.box(200, 240, 150, 80, "Fund selector", "at a bank or wealth manager approves the fund")
    d.box(380, 240, 150, 80, "Advisers", "choose whether to use it")
    d.box(560, 240, 190, 80, "Individual investors", "many small amounts")
    d.arrow(170, 280, 200, 280); d.arrow(350, 280, 380, 280); d.arrow(530, 280, 560, 280)
    return d.html()


def fee_arithmetic():
    d = Dia("fee", 250, "How a mandate becomes income",
            "The yearly fee is the client's assets multiplied by the fee rate. Five hundred million pounds at one fifth of one per cent is one million pounds a year. "
            "The fee changes when the client adds or withdraws money, when markets move, or when the rate is renegotiated.")
    d.box(10, 30, 200, 90, "£500 million", "of the client's money", "b")
    d.text(238, 84, "×", "dg-big")
    d.box(265, 30, 210, 90, "0.20% a year", "also written as 20 basis points")
    d.text(503, 84, "=", "dg-big")
    d.box(530, 30, 220, 90, "£1 million a year", "gross management fee", "b")
    d.text(380, 160, "What makes the £1 million go up or down", "dg-h")
    d.box(10, 178, 235, 56, "The client adds or withdraws", "", "c")
    d.box(262, 178, 235, 56, "Markets rise or fall", "", "c")
    d.box(515, 178, 235, 56, "The fee rate is renegotiated", "", "c")
    return d.html()


def lifecycle():
    d = Dia("life", 350, "The life of one client relationship",
            "A relationship moves through eight steps: research, first conversations, a proposal, formal checks, appointment, setting up, regular reviews, "
            "and then a decision to grow, shrink or end it. The first five steps are mostly about winning the client. The rest are about keeping the promise.")
    top = ["1. Research: who might need this?", "2. First talks: what is their problem?", "3. Proposal: a specific answer", "4. Checks: questionnaires and due diligence"]
    bot = ["8. Decision: grow, shrink or leave", "7. Reviews: report, explain, listen", "6. Set-up: contract, accounts, funding", "5. Appointment: the client says yes"]
    xs = [10, 198, 386, 574]
    for i, t in enumerate(top):
        d.box(xs[i], 40, 176, 86, t, "", "b" if i < 4 else "a")
        if i < 3:
            d.arrow(xs[i] + 176, 83, xs[i + 1], 83)
    for i, t in enumerate(bot):
        d.box(xs[i], 200, 176, 86, t, "", "a" if i else "c")
        if i < 3:
            d.arrow(xs[i + 1], 243, xs[i] + 176, 243)
    d.arrow(662, 126, 662, 200)
    d.text(380, 25, "Winning the client (often months, sometimes years)", "dg-s")
    d.text(380, 312, "Keeping the promise (ideally many years)", "dg-s")
    d.text(380, 336, "Step 8 leads back to step 7, or to a goodbye handled well", "dg-s")
    return d.html()


def trust_steps():
    d = Dia("trust", 460, "How trust is built, one step at a time",
            "Trust rises in steps, and each step is earned by a behaviour the client can see. First you do what you said. Then your numbers are always right. "
            "Then you explain a bad result plainly. Then you tell the client when something is not right for them. After many years the client trusts the firm, "
            "not only one person. One broken promise can drop you back several steps.")
    steps = [("First meetings", "You do what you said, on time"),
             ("First year", "Every number you send is right"),
             ("First bad result", "You explain it plainly, no excuses"),
             ("Years 3 to 10", "You say 'not right for you' when it is not"),
             ("10 years and more", "They trust the firm, so it survives people changing")]
    for k, (a, b) in enumerate(steps):
        d.box(10 + k * 150, 300 - k * 46, 142, 124, a, b, "b" if k % 2 == 0 else "a")
    d.text(15, 26, "More trust ↑", "dg-s", "start")
    d.text(745, 448, "Time →", "dg-s", "end")
    d.box(10, 44, 290, 92, "The slide back down", "A missed promise, a hidden problem or a wrong number costs several steps at once", "c")
    return d.html()


def career_path():
    d = Dia("career", 410, "The long view: how the job changes over a career",
            "Titles move from summer analyst to analyst, associate, vice president (called executive director in Europe), managing director and, for a few, partner. "
            "What you are responsible for grows from getting documents right, to running client work, to owning relationships, to owning a business. "
            "Many people leave this ladder for other good paths along the way. The timings are a general industry pattern, not Goldman policy.")
    stages = [("Summer analyst", "9 to 10 weeks. Learn, help, be accurate"),
              ("Analyst", "Prepare meetings, check numbers, follow up"),
              ("Associate", "Run parts of client work day to day"),
              ("Vice president", "(Executive director in Europe.) Own relationships and targets"),
              ("Managing director", "Own a region or client group")]
    for i, (a, b) in enumerate(stages):
        d.box(10 + i * 150, 56, 140, 132, a, b, "b" if i < 2 else "a")
        if i:
            d.arrow(10 + i * 150 - 10, 122, 10 + i * 150, 122)
    d.text(380, 22, "Responsibility grows from left to right", "dg-s")
    d.text(380, 216, "What you own at each stage", "dg-h")
    owns = ["Your own work", "Documents and details", "A process", "A relationship", "A business"]
    for i, o in enumerate(owns):
        d.box(10 + i * 150, 228, 140, 52, o, "", "c")
    d.box(10, 304, 740, 84, "Paths people take along the way",
          "Investment specialist · investment consultant · the client side (a pension scheme or state fund) · another asset manager · private wealth · something else entirely", "c")
    return d.html()


def sales_rm():
    d = Dia("salesrm", 240, "Two jobs on one client",
            "Before the client appoints the manager, the sales person leads and the relationship manager supports. After appointment the relationship manager leads "
            "and the sales person stays involved when the client might add more. In real teams the two overlap, and at junior level the work is much the same.")
    d.text(380, 28, "The client appoints the manager here", "dg-s")
    d.arrow(380, 36, 380, 62)
    d.box(10, 70, 420, 60, "Sales leads", "Find the client, understand the need, win the mandate", "b")
    d.box(440, 70, 310, 60, "Sales supports", "Returns for new or larger mandates", "c")
    d.box(10, 145, 320, 60, "Relationship management supports", "Helps with checks and set-up", "c")
    d.box(340, 145, 410, 60, "Relationship management leads", "Reviews, reporting, problems, renewals", "b")
    d.text(15, 228, "Before appointment", "dg-s", "start")
    d.text(745, 228, "After appointment, for as long as the client stays", "dg-s", "end")
    return d.html()


def why_funnel():
    d = Dia("why", 300, "From understanding the job to a reason you can defend",
            "Start with what the job is. Pick out the parts that might suit you. Test each one against something that has happened in your own life. "
            "What survives the test is a reason you can defend. What does not survive is a question to keep exploring, and saying so is an honest answer.")
    d.box(10, 40, 170, 110, "1. What the job is", "Facts from this guide")
    d.box(200, 40, 170, 110, "2. What might suit me", "A guess, not yet a reason", "c")
    d.box(390, 40, 170, 110, "3. Evidence from my life", "A time I did something like it, and how it felt", "c")
    d.box(580, 40, 170, 110, "4. A reason I can defend", "Specific, honest, tested", "b")
    for x in (180, 370, 560):
        d.arrow(x, 95, x + 20, 95)
    d.box(200, 200, 360, 70, "No evidence yet?", "Say what you want to find out, and how the internship would test it", "c")
    d.arrow(475, 150, 430, 200, dashed=True)
    return d.html()


DIAGRAMS = {
    "money-chain": money_chain, "where-csg-sits": where_csg_sits, "two-routes": two_routes, "fee-arithmetic": fee_arithmetic,
    "lifecycle": lifecycle, "trust-steps": trust_steps, "career-path": career_path, "sales-rm": sales_rm, "why-funnel": why_funnel,
}


def diagram(name):
    fn = DIAGRAMS.get(name)
    return fn() if fn else f'<p class="na">Diagram "{esc(name)}" not found.</p>'
