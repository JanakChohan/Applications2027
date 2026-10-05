from lib import *

def fig_protocol():
    steps = [('1  STEADY','5-10 sec','"Let me make sure I have the situation right..." Restate the core in one line. Breathe.'),
             ('2  SORT','10-15 sec','"There are two things in tension here: X and Y." Name what matters and in what order.'),
             ('3  ACT','20-35 sec','"First I would... then... and I would tell [person] because..." Concrete steps, real people.'),
             ('4  CLOSE','5-10 sec','"The principle is: integrity and accuracy before speed." One sentence they can write down.')]
    b = ''
    for i,(t,tm,d) in enumerate(steps):
        x = 10 + i*175
        b += rect(x, 20, 160, 190, [TEALS,GRNS,ACCS,SIGS][i], [TEAL,GRN,ACC,SIG][i], 8, 1.5)
        b += text(x+80, 48, t, 14, NAVY, 'middle', 'bold')
        b += text(x+80, 68, tm, 10, MUT, 'middle')
        b += text(x+12, 92, d, 10, NAVY, 'start', width=27, lh=13)
        if i < 3: b += arrow(x+162, 115, x+173, 115)
    b += text(360, 236, 'Total: 45 to 75 seconds. Stop talking after the close. Let them come back to you.', 11, NAVY2, 'middle', 'bold')
    return svg(720, 250, b)

def fig_priority():
    tiers = [('1','Rules, confidentiality and Investec\'s name','Never traded. Cast-iron integrity is a stated value; a bank lives on trust and regulation.',RED),
             ('2','The client and the team\'s commitments','What the team has promised a client or a senior colleague comes before your own preferences.',ACC),
             ('3','Accuracy and the record','Check the numbers, keep the file tidy, say what you did and did not verify.',TEAL),
             ('4','Speed','Matters, but only inside the three lines above. Fast and wrong costs more than slow and right.',GRN)]
    b = ''
    for i,(n,t,d,c) in enumerate(tiers):
        w = 640 - i*70; x = (720-w)/2; y = 10 + i*58
        b += rect(x, y, w, 50, '#ffffff', c, 6, 2)
        b += f'<circle cx="{x+26}" cy="{y+25}" r="15" fill="{c}"/>' + text(x+26, y+30, n, 14, '#fff', 'middle', 'bold')
        b += text(x+50, y+21, t, 12, NAVY, 'start', 'bold')
        b += text(x+50, y+38, d, 9.5, MUT, 'start')
    b += text(360, 258, '"I would never trade integrity or accuracy for speed. Inside those lines I move as fast as the team needs, and I flag early."', 10.5, NAVY2, 'middle', 'bold', width=110)
    return svg(720, 285, b)

TACTICS = [
 ('Interruption','They cut in mid-answer.','Stop. "Of course." Answer their point in one line, then: "To finish the thought..." and land your close.'),
 ('Flat contradiction','"That\'s wrong."','"Help me see it. Which part?" If they are right, concede the fact, keep the principle. If not, restate calmly with the reason.'),
 ('Silence','They say nothing after you finish.','Do not fill it with a new answer. Wait three seconds, then: "Is there a part you would like me to go deeper on?"'),
 ('Escalation','"And now the MD is furious."','Same frame, higher stakes. Repeat the priority order out loud and add who you would tell, faster.'),
 ('Authority squeeze','"A senior person told you to. Do it."','"I would want to help them get the outcome, and I would check the one thing I am unsure about with them or my manager first."'),
 ('False choice','"Option A or B. Pick one."','"If those are truly the only options, A, because... But I would first check whether C exists, for example asking for ten minutes."'),
 ('Knowledge trap','A technical question you cannot answer.','"I do not know that precisely. Here is how I would reason about it... and I would check it with..." Never bluff a number.'),
 ('Invitation to badmouth','"What do you think of [rival / your old boss]?"','Stay generous and factual: "They are strong at X. What draws me to Investec is Y." Never criticise a person.')]

def fig_tactics():
    b = ''
    for i,(t,s,c) in enumerate(TACTICS):
        col = i % 2; row = i // 2
        x = 10 + col*355; y = 10 + row*92
        b += rect(x, y, 345, 84, '#fff', LINE, 6)
        b += rect(x, y, 8, 84, RED if col==0 else ACC, 'none', 0)
        b += text(x+18, y+18, f'{i+1}. {t}', 11.5, NAVY, 'start', 'bold')
        b += text(x+18, y+33, s, 9, MUT, 'start', italic=True)
        b += text(x+18, y+49, 'Counter: ' + c, 9, NAVY2, 'start', width=62, lh=11.5)
    return svg(720, 380, b)

# JD "duty lines" for an internship, decoded as interview targets
DUTIES = [
 ('D1','Join a team within the Specialist Bank, aligned at your HR interview'),
 ('D2','Insight into culture; exposure to senior leaders'),
 ('D3','Real responsibilities: contribute and deliver to your team'),
 ('D4','A clear overview of the entire business, not just your team'),
 ('D5','Presentations, talks and networking'),
 ('D6','Absorb complex information from the FT; immerse yourself in financial analysis'),
 ('D7','Excel courses'),
 ('D8','Entrepreneurial thinker: fresh ideas'),
 ('D9','Self-starter: take a project and make it your own'),
 ('D10','Be you: passions and interests'),
 ('D11','Penultimate or final year, any degree'),
]

def fig_ladder():
    b = text(150, 16, 'JD line', 10, MUT, 'start', 'bold') + text(395, 16, 'Easy', 10, GRN, 'middle', 'bold') + text(520, 16, 'Medium', 10, ACC, 'middle', 'bold') + text(645, 16, 'Hard', 10, RED, 'middle', 'bold')
    short = ['Team allocation','Culture & seniors','Real work','Whole business','Talks & networking','FT & analysis','Excel','Fresh ideas','Own a project','Be you','Year & degree']
    for i,(d,_) in enumerate(DUTIES):
        y = 26 + i*29
        b += text(10, y+17, d, 10, ACC, 'start', 'bold') + text(48, y+17, short[i], 10, NAVY, 'start')
        for j,c in enumerate([GRN, ACC, RED]):
            x = 340 + j*125
            b += rect(x, y+2, 110, 22, ['#e7f4ec','#fbf1e2','#fbeaea'][j], c, 4)
            b += text(x+55, y+17, f'{d}.{j+1}', 9.5, NAVY, 'middle', 'bold')
    return svg(720, 26 + len(DUTIES)*29 + 6, b)

def tree(title, root, branches):
    """root question, branches = [(answer, [steps])]"""
    b = node(220, 8, 280, 50, root, fill=NAVY, stroke=NAVY, tc='#fff', size=11)
    n = len(branches); bw = 700/n
    for i,(ans, steps) in enumerate(branches):
        cx = 10 + bw*i + bw/2
        b += path(f'M360,58 L360,72 L{cx},72 L{cx},88', MUT)
        b += node(cx-bw/2+6, 90, bw-12, 30, ans, fill=ACCS, stroke=ACC, size=10)
        y = 128
        for s in steps:
            lines = wrap(s, int((bw-24)/5.2))
            hh = 10 + 12*len(lines)
            b += rect(cx-bw/2+6, y, bw-12, hh, '#fff', LINE, 4)
            for k,l in enumerate(lines): b += text(cx-bw/2+12, y+14+k*12, l, 9.2, NAVY)
            b += arrow(cx, y+hh, cx, y+hh+8) if s != steps[-1] else ''
            y += hh + 10
    return b

def fig_trees():
    t1 = tree('Senior asks you to skip a control', 'A senior person asks me to skip a check or bend a rule. Is it a rule or a preference?', [
        ('Clear rule (law, policy, client data)', ['Do not do it. Say so politely and at once.', '"I am not able to do that, but here is how I can get you the outcome fast."', 'Tell your manager the same day, factually.']),
        ('Grey area / not sure', ['Pause. Ask: "Can I check that with compliance or my manager first?"', 'Offer a compliant route that still meets the deadline.', 'Write down what was asked and what you did.']),
        ('Just a team habit', ['Ask why the check exists. Often it guards a real risk.', 'If it is genuinely optional, agree with your manager, not alone.', 'Suggest improving the process later, not on the day.'])])
    t2 = tree('Mistake you made', 'I find an error in work I have already sent. Has anyone acted on it yet?', [
        ('Not yet', ['Fix it. Send the corrected version with a one-line note of what changed.', 'Check whether the same error sits elsewhere.']),
        ('Yes, internally', ['Tell the person who acted on it now, in person or by phone.', 'Bring the fix and the impact: "Number X was Y, it should be Z."', 'Add a check so it cannot recur.']),
        ('Yes, a client saw it', ['Tell your manager immediately. Do not contact the client yourself.', 'Have the corrected version ready.', 'Let the senior person decide the client message.'])])
    return svg(720, 330, t1), svg(720, 330, t2)

SC = {}  # duty -> 3 cards
SC['D1'] = [
 card('easy','"Which part of the business would you like to join?"','The HR interviewer asks where you want to be placed.','Naming one team only, or saying "anywhere" with no reason.','"My first choice is [Private Banking / a CIB team], because [mechanism, e.g. it serves both entrepreneurs and the businesses they own]. I would be equally keen on [second], because [reason]. What I want most is a team where I own a piece of work."','The JD says the team is chosen with you at the HR interview, so a ranked, reasoned answer helps them place you. [S1]','"And if we place you in Operations?" Hold: "Then I would learn how the bank actually works, which most front-office interns never see. I would ask to sit in on a credit committee too."'),
 card('med','"Why not apply to a bulge-bracket bank?"','They test whether you chose Investec or just applied everywhere.','Badmouthing big banks or saying "smaller is easier".','"Big banks run interns through a fixed rotation. Investec places you in one team with real work, in a bank small enough that you see senior people. I also like that the private bank and the corporate bank serve the same entrepreneurs."','Mechanism, not adjectives: team placement, scale, the combined client. [S1] [I]','"But big banks pay more and have bigger names." Hold: "True. I am choosing where I will learn fastest in eight weeks."'),
 card('hard','"You have no finance background. Why should a credit team take you?"','A non-finance candidate is pushed on fit.','Apologising, or pretending to know more than you do.','"The JD says any degree, and I take that at face value. I bring [skill from degree, e.g. structured argument / data handling]. I have already [specific learning step]. In week one I would learn the team\'s credit template before touching anything else."','Shows self-awareness and a concrete learning plan, which is what "self-starter" means. [S1]','"Explain what a credit committee is." Use the definition in Part 5; if unsure, say what you know and how you would find out.')]
SC['D2'] = [
 card('easy','"What do you know about our culture?"','Opening question on culture.','Reciting "out of the ordinary" with nothing behind it.','"The phrase is out of the ordinary, but what makes it real to me is [one structural fact from Part 2, e.g. the founders built it as an entrepreneurial bank in Johannesburg in 1974]. The values I would test myself against are [named values]."','Ties a slogan to a fact and to behaviour. [S70+]','"Which value matters most to you?" Pick one and give a two-line story.'),
 card('med','"You get ten minutes with a senior leader. What do you ask?"','Tests curiosity and judgement around seniority.','Asking something you could Google, or asking about pay or a job offer.','"I would ask how they decide which niches the bank lends into and which it stays out of, and what made them change their mind on one in the last few years."','A real business question shows you understand niche lending as a strategic choice. [I]','"They answer in jargon." Hold: "I would ask them to give me one example, then write it up and check my understanding with my manager."'),
 card('hard','"A senior leader says something you think is wrong in a Q&A. What do you do?"','Culture says challenge; hierarchy says careful.','Silent nodding, or a public "gotcha".','"If it is a factual point, I would ask a curious question: \'I read X, how does that fit with Y?\' If it is a judgement call, I would note it and ask my manager later."','Respectful challenge fits an entrepreneurial culture and protects relationships. [I]','"And if your manager says drop it?" Hold: "I would drop it, and learn why."')]
SC['D3'] = [
 card('easy','"You are given your first task. How do you start?"','Basic work habits.','"I would just get on with it."','"I would repeat back the ask, the deadline and the format, ask what good looks like, check if there is a previous example, then send a quick draft early."','Clarity before speed matches the priority order. [I]','"Your manager is too busy to answer." Hold: ask an analyst on the team, then confirm with the manager by short email.'),
 card('med','"You finish your task early. What next?"','Self-starter test.','"I would wait to be given something."','"I tell my manager it is done, offer one improvement, and ask if anyone else on the team needs a hand. If not, I use the time to learn the deal or client file."','Shows initiative without overstepping. [S1]','"Nobody needs anything." Hold: "Then I build my overview of the wider business, which the programme says is a goal."'),
 card('hard','"Two people on the team give you urgent work due at the same time."','Scarce-resource collision.','Choosing silently, or doing both badly.','"I would tell both of them straight away, give each the other\'s deadline, and ask the more senior person or my manager to set the order. Then I would deliver in that order and keep both updated."','Transparency and a clear owner of priority is how teams resolve this. [I]','"Both say theirs is client-facing." Hold: client commitments first, the earlier client deadline wins, and the manager decides ties.')]
SC['D4'] = [
 card('easy','"Describe Investec in one sentence."','Basic firm knowledge.','A brochure line.','Use the 30-second line in Part 12: a specialist bank and wealth manager serving entrepreneurs, high-income professionals and mid-market businesses, listed in London and Johannesburg.','Precise and sourced. [S70+]','"What is a specialist bank?" Define it from Part 5.'),
 card('med','"How do the private bank and the corporate bank work together?"','Do you understand One Investec?','Inventing collaboration figures.','"The idea is that the same people appear on both sides: a founder banks privately and their company borrows from the corporate bank. Referrals between them are the point. I would want to see how that works in practice."','Uses the firm\'s own framing, flagged as their claim. [S120+]','"Isn\'t that a conflict of interest?" Hold: information barriers and client consent; explain in Part 3.'),
 card('hard','"If you ran the UK bank, what would you cut?"','Strategic judgement under pressure.','Pretending to know the internal numbers.','"I cannot judge that from outside. I would ask which niches earn above their cost of capital through a full cycle, and look at the ones that rely on one or two people. From public results I would look first at [segment with weak return if reported]."','Honest about limits, shows the right test (return over cost of capital). [I]','"Just pick one." Hold: pick with a reason, labelled as an outside view.')]
SC['D5'] = [
 card('easy','"How would you make the most of the speaker series?"','Learning habits.','"I would attend all of them."','"I would read up on each speaker\'s business beforehand, prepare one question, and write a five-line note afterwards on what I learned and who I want to follow up with."','Shows a system, not enthusiasm. [S1]','"And the networking drinks?" Hold: set a target of two real conversations, not twenty business cards.'),
 card('med','"How do you approach networking with people more senior?"','Social confidence.','Transactional networking ("I want a job").','"I ask about their work, not about jobs. I follow up within a day with a thank-you and one thing I took away."','Respectful and memorable. [I]','"Give an example from your past." Have one ready.'),
 card('hard','"A senior person you met says \'Come and see me any time\'. Do you?"','Boundaries and judgement.','Turning up uninvited or never following up.','"Yes, but on their terms. I would email to ask for fifteen minutes, keep it short, and mention it to my manager so nothing happens behind their back."','Balances initiative with respect for line management. [I]','"Your manager is annoyed." Hold: apologise, explain intent, agree how to handle it next time.')]
SC['D6'] = [
 card('easy','"What did you read in the FT this week?"','Commercial awareness, the classic.','Naming a headline without a view.','Pick a story from Part 7. Structure: what happened, why it matters to a bank like Investec, your view, what would change your mind.','The JD itself names the FT. [S1]','"Why does that matter to us specifically?" Link to a segment.'),
 card('med','"Explain how a rise in interest rates affects Investec."','Basic bank economics.','Saying "banks make more money" and stopping.','"Higher rates raise the margin on loans funded by cheaper deposits, up to a point. But depositors demand more, borrowers struggle, and credit losses can rise. Investec\'s results show [NIM / impairment point from Part 2]."','Two-sided, mechanism-based, sourced. [S70+]','"So are falling rates good or bad?" Hold: margin squeeze vs. lower credit losses and more deal activity.'),
 card('hard','"Here are three numbers from our results. What do they tell you?"','Live financial analysis.','Freezing, or guessing.','"Let me take them one at a time... The cost-to-income ratio tells me how efficient... ROE against CET1 tells me how hard capital works..." Think aloud.','Thinking aloud is what they want to see. [I]','"Which is the most worrying?" Pick one and say why, labelled as a view.')]
SC['D7'] = [
 card('easy','"How good is your Excel?"','Honesty about skills.','Overclaiming.','"Solid on [functions you can use: XLOOKUP, pivot tables, SUMIFS]. Less confident on [macros / financial modelling]; I am working on it via [course]."','Honest and specific. [I]','"Explain a pivot table." One sentence: summarises a big table by groups.'),
 card('med','"Your model gives a strange result an hour before it is due."','Accuracy vs speed.','Sending it anyway.','"I would check the inputs and the formula chain, and if I cannot find it in thirty minutes I would send it with a clear flag on the number I do not trust, and tell my manager."','Accuracy and the record outrank speed. [I]','"The MD needs it now." Hold: send with the flag; never hide a known problem.'),
 card('hard','"Someone asks you to hard-code a number to make the output match."','Integrity in small things.','Doing it silently.','"I would ask where the number comes from. If it is a real override, I would label it as an input with its source. I would not hide it in a formula."','Transparent models protect the bank and the client. [I]','"It\'s just a draft." Hold: drafts get forwarded; label it anyway.')]
SC['D8'] = [
 card('easy','"Give us a fresh idea for Investec."','Entrepreneurial thinker.','A vague idea ("use AI more").','Use the idea structure: who it helps, the problem, the smallest test, how you would measure it. For example, a student-run content series on the FT summaries the JD mentions.','Specific, testable, small. [S1]','"Why hasn\'t it been done?" Hold: "Maybe it has; I would ask first."'),
 card('med','"Tell us about something you started."','Evidence of entrepreneurship.','A team project where you did little.','STAR with the numbers: what you started, what you risked, what happened, what you learned.','The JD asks for fresh ideas and owning projects. [S1]','"What would you do differently?" Have one real answer.'),
 card('hard','"Your idea would cost money and the team says no."','Handling rejection.','Arguing on.','"I would ask what would make it worth trying, test a smaller version for free if possible, and drop it gracefully if not."','Entrepreneurs test small. [I]','"Would you go above their heads?" No, unless it is a conduct issue.')]
SC['D9'] = [
 card('easy','"Tell us about a project you made your own."','Self-starter.','Describing a group effort as solo.','Pick one; show ownership: you defined it, you chased people, you delivered. Give the result.','Matches the JD wording. [S1]','"Who helped you?" Credit others.'),
 card('med','"Your project is going nowhere after two weeks."','Persistence vs. judgement.','Pretending it is fine.','"I would tell my manager early, show what I tried, and propose either a narrower scope or a different route."','Early honesty beats late surprise. [I]','"Your manager is away." Ask the next senior person on the team.'),
 card('hard','"You are given a vague task: \'look into fund finance for us\'."','Ambiguity.','Starting without a scope.','"I would ask what decision it informs and by when, then send a one-page plan before spending a day on it."','Saves everyone time. [I]','"They say: just figure it out." Hold: draft the scope yourself and confirm by email.')]
SC['D10'] = [
 card('easy','"What do you do outside your studies?"','Be you.','A list with no story.','One passion, one detail, one link to how you work. Keep it honest.','The JD explicitly asks for passions. [S1]','"How does that help you here?" One sentence link.'),
 card('med','"What would surprise us about you?"','Authenticity.','A humblebrag.','Something true and specific that shows character.','[I]','"Why does that matter?" Link to resilience or curiosity.'),
 card('hard','"Isn\'t that hobby a distraction from the job?"','Pressure on a personal answer.','Getting defensive or dropping it.','"It is what keeps me sharp. During exams I scaled it down to [x], and I would do the same during the internship."','Shows self-management. [I]','"Prove it." Give the example.')]
SC['D11'] = [
 card('easy','"Why an internship now?"','Timing and motivation.','"Because everyone does one."','"I want to test whether banking is right for me before I commit to a graduate role, and eight weeks inside a real team is the best test."','[S1]','"And if it isn\'t?" Hold: then you learned it cheaply.'),
 card('med','"How does your degree help in a bank?"','Any-degree candidates.','Saying it does not.','Name two transferable skills with evidence.','[S1]','"Name a weakness of your degree for this job." Have one and your fix.'),
 card('hard','"Where do you see yourself in five years?"','Ambition and realism.','Naming a title you do not understand.','"Ideally on Investec\'s graduate programme then in [area], having learned [skill]. I would expect that to change as I learn what I am good at."','[I]','"Would you leave for a hedge fund?" Hold: honest, not disloyal.')]

COMPOSURE = [
 ('Two seniors, one intern, both urgent','Two people each say their task is the priority and both are due by 5pm.',
  'Tell both at once, share the clash, ask the more senior person or your manager to set the order. Deliver in order. Keep both updated.'),
 ('Asked to skip a control','A senior colleague asks you to email a client file to your personal address so you can finish it at home.',
  'Say no politely: "I\'m not able to send client data outside the bank, but I can finish it in the office tonight or on a bank laptop." Tell your manager. See the decision tree.'),
 ('Overheard something possibly inside information','In the lift you hear a deal team discuss a listed company being bought.',
  'Do not trade, do not repeat, do not write it down. Tell compliance or your manager that you may have heard something. Assume it is inside information until told otherwise.'),
 ('Your mistake','You find an error in a spreadsheet already sent to a director.',
  'Tell the director now with the fix and the impact. Do not wait. See the decision tree.'),
 ('Incomplete information, hard deadline','You have to brief your team on a company by 9am, and half the data is missing.',
  'Deliver what you have on time, mark clearly what is missing and what you assumed, and say how you would fill the gap.')]
