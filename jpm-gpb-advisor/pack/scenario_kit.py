import re, subprocess, pymupdf, diagrams4 as d4
n=[0]
def F(svg,cap):
    n[0]+=1; return f'<div class="fig">{svg}<div class="cap"><b>Figure {n[0]}.</b> {cap}</div></div>'
css=open("pack_style.css").read()+"""
body{font-size:10.3pt} .big{font-size:11.8pt;line-height:1.5;color:#0b2545}
.case{border:1px solid #d6dbe3;border-left:5px solid #0b2545;border-radius:4pt;padding:8pt 11pt;margin:8pt 0}
.case .h{font-weight:700;color:#0b2545;font-size:11.5pt;margin-bottom:4pt}
.phr{background:#eaf5ef;border-left:4px solid #2e7d5b;padding:4pt 9pt;margin:4pt 0;font-size:9.6pt}
.phr b{color:#2e7d5b}
table.plan td:first-child{white-space:nowrap;font-weight:700;color:#0b2545;width:16%}
.keep{break-inside:avoid}
"""
body=f"""
<div class="cover" style="height:250mm">
<div class="band"><div class="kicker">Practice kit · the interactive client scenario</div>
<h1>How to Prepare for the Group Exercise</h1>
<div class="sub">What the assessors score, a five-step method with the exact phrases, three practice cases with model answers, how to handle the group, and a four-day rehearsal plan. Built for the Inside Private Banking day on Monday 19 October 2026.</div></div>
<div class="meta"><p><strong>Prepared:</strong> 15 October 2026. Companion to the event brief, whose Part 2 has the full background on the five seats, the bank's vocabulary and the UK tax facts.</p>
<p><strong>What is known and what is inferred:</strong> the invitation promises "an interactive client scenario designed to give you insight into the work of the Private Bank". No account of a previous London event is public. The format below is inferred from the bank's Asia Private Bank Challenge (teams of four, a hypothetical client, a presentation to judges), from peer firms' internship simulations, and from how assessment-centre group exercises are scored. Prepare for the hardest version: a team of four to six, a one-page client profile, twenty to thirty minutes to discuss, a short presentation to a banker, questions back.</p></div></div>

<h2>1. What they are actually scoring</h2>
<p class="big">A group exercise at a private bank is not a test of whether you know the right product. It is a test of whether you behave like someone a wealthy family would trust in a room: you listen, you ask, you structure, you bring in others, and you are honest about what you do not know. The answer matters less than the way you reach it.</p>
<table>
<tr><th style="width:22%">What is scored</th><th>What it looks like when done well</th><th style="width:30%">What loses marks</th></tr>
<tr><td><strong>Listening and questioning</strong></td><td>You ask what the money is for before you say what to do with it. You notice the detail in the brief that others skipped (the second home abroad, the child who does not want the business, the loan that matures next year).</td><td>Opening with "I think they should invest in..." Repeating the brief back without a question.</td></tr>
<tr><td><strong>Structure</strong></td><td>You propose a frame in the first two minutes: "Shall we do balance sheet, then goals, then who we bring in, then two next steps?" and you keep the group to it.</td><td>A list of ideas with no order. Running out of time before next steps.</td></tr>
<tr><td><strong>Teamwork</strong></td><td>You build on others by name ("Taking Priya's point about the tax bill, that means..."). You bring in the quiet person. You give up your own idea when a better one appears.</td><td>Talking most. Interrupting. Arguing to win. Silence.</td></tr>
<tr><td><strong>Commercial judgement</strong></td><td>You see where the bank earns and where the risk sits: lending against the portfolio keeps the assets invested; a concentrated stock is both the client's risk and the bank's collateral problem.</td><td>Giving everything away. Ignoring that this is a business.</td></tr>
<tr><td><strong>Client empathy</strong></td><td>You name the human issue: the founder has lost a job as well as gained a fortune; the widow is being advised by three people who all want her money.</td><td>Treating the client as a spreadsheet.</td></tr>
<tr><td><strong>Honesty about limits</strong></td><td>"That is a Wealth Advisor question; what I would want them to check is..." You give ranges, not invented precision.</td><td>Tax advice from memory. Made-up numbers.</td></tr>
</table>
{{FIG:flow}}

<h2>2. The five-step method, with the phrases</h2>
<div class="case"><div class="h">Step 1. Frame the time (first ninety seconds)</div>
<p>Someone has to propose a structure. If nobody does in the first minute, it is you. Offer it as a question so it is the group's, not yours.</p>
<div class="phr"><b>Say:</b> "We have twenty minutes. Can I suggest five minutes on what the client has and owes, five on what they want and when, five on what we would bring in, and five to agree two next steps and who presents? Does anyone want to change that?"</div>
<div class="phr"><b>Then:</b> "Who is happy to keep time, and who will note the points on the flipchart?" Take one of those roles yourself if nobody moves; the scribe is a good role for a listener because it forces you to synthesise.</div></div>
<div class="case"><div class="h">Step 2. Both sides of the balance sheet (what they have, what they owe, what is coming)</div>
<p>Read the brief for the numbers and sort them into liquid and illiquid, now and later. Say the three things most briefs hide: a tax bill, a loan, a locked asset.</p>
<div class="phr"><b>Say:</b> "Before we talk about what to do: the liquid pot is about X, the illiquid pot is about Y, and there are three things that will take cash out in the next two years: the tax, the mortgage and the children's purchases. Have I missed anything that costs money?"</div></div>
<div class="case"><div class="h">Step 3. Goals and horizons (what is the money for, and when)</div>
<p>The bank's own question is "What's the purpose of your wealth?" Sort the money into lifestyle (next five years), growth (ten years plus), legacy and giving. Tie each pot to a horizon; the horizon decides the risk.</p>
<div class="phr"><b>Say:</b> "If this were a real first meeting I would ask the client what the money is for before any of this. From the brief, I read three goals: a secure income of about £1m a year for life, something for each child, and keeping the Italian house in the family. Does anyone read it differently?"</div>
<div class="phr"><b>Say, if the brief is silent on the person:</b> "The thing the brief does not say is how the founder feels about having sold. In my experience from the Pictet onboarding desk, the first six months after a sale are when people make the decisions they regret, so I would want the plan to be reversible for a year."</div></div>
<div class="case"><div class="h">Step 4. Name the seats (who we bring in, and for what)</div>
<p>This is where you show you understand the bank. Do not solve the tax, the loan or the portfolio yourself; say which specialist owns each, and what you would ask them.</p>
<div class="phr"><b>Say:</b> "Three of the five seats are needed straight away. Wealth Advisor: the will, the Italian succession, the children's gifts, and whether the family's UK residence is changing. Capital Advisor: can we refinance the mortgage against the portfolio and lend against the locked shares rather than wait? Investor: a staged plan, cash and gilts for the first two years, the long-term portfolio in tranches, alternatives sized to a liquidity budget. The banker, which is us, owns the sequence."</div></div>
<div class="case"><div class="h">Step 5. Two next steps and the presentation (last five minutes)</div>
<p>End with actions, not a product list. Agree who presents what; a two-person presentation with one person handling questions reads as a team.</p>
<div class="phr"><b>Say:</b> "So our two next steps: one, ring-fence the tax and two years of spending this week so nothing is forced; two, a second meeting with the Wealth Advisor and Capital Advisor in the room, before any investing. Shall Sam open with the balance sheet, I take the goals and seats, and Priya take questions?"</div>
<div class="phr"><b>When the banker asks "what would you invest in?":</b> "Honestly, not yet. The first ninety days are about making sure nothing has to be sold at the wrong time. Once the tax and the spending are covered, a diversified core with alternatives sized to what the client will not need for five years. The exact mix is the Investor's conversation with the client, and it depends on what they told us the money is for."</div></div>

<h2>3. Three practice cases</h2>
<p>Work each one alone against the clock (twenty minutes), then once aloud with a friend playing the banker who asks questions back. The model answer is a shape, not a script.</p>
<div class="case"><div class="h">Case A. The founder who has just sold</div>
<p><strong>Brief.</strong> Amira, 52, sold her logistics-software company to a listed US buyer three weeks ago. £42m cash received; £9m of the buyer's shares locked for twelve months; a £8m house in Hampstead with a £2m mortgage; a £3m house in Tuscany; two children, 19 and 23; spends about £1m a year; no will since the sale; capital gains tax of about £9m due in January; a UK resident since birth; her husband is Italian. She says she wants "to never think about money again" and to "do something useful" with part of it.</p>
{{FIG:family}}
<p><strong>The trap.</strong> Investing the £42m. <strong>The things to notice.</strong> £9m of tax and £2m of spending must stay liquid; the locked shares are both a concentration risk and collateral; the Italian husband and house mean two legal systems for succession; "do something useful" is a philanthropy conversation. <strong>Seats.</strong> Wealth Advisor first (will, cross-border succession, gifts to children, Philanthropy Centre), Capital Advisor (refinance the mortgage against the portfolio; a facility against the locked shares), Investor (staged core, alternatives later). <strong>Two next steps.</strong> Ring-fence £11m plus a buffer in cash and short gilts this week; a second meeting with the Wealth Advisor and Capital Advisor before any investment. <strong>The human line.</strong> "She sold her life's work three weeks ago; the plan should be reversible for a year."</p></div>
<div class="case"><div class="h">Case B. The family with a reluctant heir and a move in mind</div>
<p><strong>Brief.</strong> The Okafors: Daniel, 68, owns a private engineering group worth about £80m that pays him £3m a year; his wife Grace, 66; three children, of whom one works in the business and wants to run it, one is a doctor who wants nothing to do with it, and one is 30 and "finding herself". Family investments of £15m with another bank, mostly in UK equities; a £6m house; £4m of pensions. Daniel is thinking of selling to private equity in two years, or passing the business to his son. Grace's parents are in Lagos and she wants to spend more time there. Daniel asks whether the family should "leave the UK before the Budget".</p>
<p><strong>The trap.</strong> Answering the tax question. <strong>The things to notice.</strong> This is a pre-liquidity case, so the 18-to-24-month planning window is open now; the three children want different things, which is a family-governance conversation before a tax one; "leave the UK" involves the ten-year IHT tail and should go straight to the Wealth Advisor; the existing £15m is concentrated in one market; the pensions enter IHT in April 2027. <strong>Seats.</strong> Wealth Advisor and the Advice Lab (family governance, succession, Private Business Advisory, residence), Capital Advisor later (liquidity for the two children not taking the business), Investor (diversify the £15m), and the investment bank's coverage if a sale is real. <strong>Two next steps.</strong> A family meeting with the Wealth Advisor to agree what each child wants and what "fair" means; a pre-sale planning review with Private Business Advisory before any decision on selling or moving. <strong>The human line.</strong> "The question is not whether to leave the UK; it is what the family wants the business and the money to do for three very different children."</p></div>
<div class="case"><div class="h">Case C. The fund partner with a loan request</div>
<p><strong>Brief.</strong> Tom, 44, is a partner at a London private-equity firm. Income £2m a year, lumpy: most of it is carried interest paid every two or three years. £10m of liquid investments, £12m of fund interests and co-investments that he cannot sell, £5m of capital commitments still to be called over the next four years, a £5m mortgage, and a divorce in progress. He wants a £4m loan to buy a house for his children's mother, and asks whether the bank can also "fund my next GP commitment".</p>
<p><strong>The trap.</strong> Saying yes to the loan. <strong>The things to notice.</strong> His liquid assets are £10m but £5m of them are already promised to capital calls; his wealth is in illiquid fund interests, which the bank may lend against only at low advance rates; the divorce changes who owns what, so no structure until it is settled; carried interest timing is the real cash-flow question. <strong>Seats.</strong> Capital Advisor (specialty lending against fund interests and GP commitments, with a cash-flow model of calls and distributions), Wealth Advisor (the divorce, the house ownership, the children), Investor (keep the liquid £10m liquid until the calls are covered). <strong>Two next steps.</strong> A cash-flow map of the next four years of calls, distributions and carry before sizing any loan; the Wealth Advisor to be in the room with his divorce lawyer's letter before any new structure. <strong>The commercial line.</strong> "The bank wants two ways out of every loan. Here the second way out is carried interest we cannot see yet, so the first conversation is about timing, not amount."</p></div>

<h2>4. Handling the group</h2>
<table>
<tr><th style="width:28%">Situation</th><th>What to do</th></tr>
<tr><td>Nobody speaks in the first minute</td><td>Propose the structure (Step 1). Ask a named person to start on the balance sheet.</td></tr>
<tr><td>One person dominates</td><td>Do not fight them. Use them: "That is useful; can we capture it and hear from the two people who have not spoken yet?" Then turn to the quiet one by name.</td></tr>
<tr><td>Someone jumps to products</td><td>"Before we pick investments, do we agree what the money is for? If the tax is due in January, the first £9m decides itself."</td></tr>
<tr><td>You disagree</td><td>Say what you would do differently and why in one sentence, then let the group decide. Losing an argument gracefully scores higher than winning it loudly.</td></tr>
<tr><td>You do not know a fact</td><td>"I am not certain; I think it is roughly X, and it is a Wealth Advisor question anyway." Never bluff a tax rate.</td></tr>
<tr><td>Time is running out</td><td>Call it: "Three minutes left. Can we agree two next steps and who says what?"</td></tr>
<tr><td>The banker challenges your plan in the presentation</td><td>Agree with the part that is right, then explain the trade-off: "You are right that cash earns less than equities; we chose it for the first two years because a forced sale in a bad year costs more than the yield."</td></tr>
<tr><td>Another team member answers a question wrongly</td><td>Add, do not correct: "And one more thing on that point: ..." The assessors notice who protects the team.</td></tr>
</table>
<div class="box key"><div class="t">The three sentences to have ready</div>"Can I suggest a structure?" "What is this money for, and when is it needed?" "That is a question for the Wealth Advisor; here is what I would want them to look at." A candidate who says those three things at the right moments has shown structure, discovery and judgement about limits, which is most of the mark.</div>

<h2>5. The four-day plan</h2>
<table class="plan">
<tr><th>Day</th><th>Do this</th></tr>
<tr><td>Thursday</td><td>Read Part 2 of the event brief (the seats, the vocabulary, the UK tax facts, the scenario section). Learn the five steps until you can say them without the page. Work Case A alone, twenty minutes on a timer, writing on one sheet: balance sheet, goals, seats, two next steps.</td></tr>
<tr><td>Friday</td><td>Work Cases B and C the same way. Then record yourself giving the Case A presentation in three minutes, as if to a banker. Watch it once. Cut every sentence that starts with a product.</td></tr>
<tr><td>Saturday</td><td>Find one friend (anyone who will read a brief). Give them Case B and play it as a group of two for twenty minutes, then have them ask you three hostile questions ("why not just put it in an index fund?", "should they leave the UK?", "how does the bank make money on this?"). Practise bringing them in by name.</td></tr>
<tr><td>Sunday</td><td>Re-read the five steps and the three sentences. Read the cheat sheet. Decide your opening line for the table on Monday. Stop by 20:00; sleep matters more than a fourth case.</td></tr>
<tr><td>Monday, in the room</td><td>Learn the names at your table before the exercise starts and use them. Take the scribe or timekeeper role if nobody else does. Ask one question before you propose anything. Bring in the quiet person once. End with two next steps.</td></tr>
</table>
<div class="box say"><div class="t">If the format turns out to be different</div>If it is a role play with a banker acting as the client: the same five steps apply, and the first ten minutes are questions only. If it is a written case with a presentation: write the structure on the page first, then fill it. If it is a debate or a markets discussion: use the three market views from Part 3 of the event brief and tie each to a client, not to a trade. Nothing about the method changes with the format.</div>
"""
figs={"flow":F(d4.scenario_flow(),"The five steps and what the assessors watch. Same figure as the event brief, Part 2."),
      "family":F(d4.family_balance_sheet(),"Case A on one page. The sheet you should be able to produce from the brief in five minutes.")}
for k,v in figs.items(): body=body.replace("{FIG:"+k+"}",v)
open("Scenario_Practice_Kit.html","w").write(f"<!doctype html><html><head><meta charset='utf-8'><title>Group Exercise Practice Kit</title><style>{css}</style></head><body>{body}</body></html>")
subprocess.run(["node","topdf_short.js","Scenario_Practice_Kit.html","Scenario_Practice_Kit.pdf","Inside Private Banking London · scenario practice kit","Prepared 15 October 2026"],check=True,capture_output=True)
print("pages",pymupdf.open("Scenario_Practice_Kit.pdf").page_count)
