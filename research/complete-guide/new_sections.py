# New sections for the complete SJP guide. Assembled by build.py.
S = {}

S['COVER'] = r'''
<section class="cover">
  <div class="step">COMPLETE GUIDE · FROM ZERO</div>
  <h1>St. James's Place:<br>the complete guide</h1>
  <div class="sub">How the firm works, who it serves, how it makes money, where it's going, and how to ace the HireVue</div>
  <svg viewBox="0 0 700 150">
    <defs><marker id="arc" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#2e6da4"/></marker></defs>
    <g font-size="13" font-weight="bold" text-anchor="middle">
      <rect x="5" y="30" width="150" height="80" rx="12" fill="#eaf6ee" stroke="#2f8f4e"/><text x="80" y="65" fill="#1f6b39">1. HireVue</text><text x="80" y="85" fill="#1f6b39" font-weight="normal" font-size="11.5">questions &amp; tips</text>
      <rect x="185" y="30" width="150" height="80" rx="12" fill="#eef3f8" stroke="#0b2d4f"/><text x="260" y="65" fill="#0b2d4f">2. The firm</text><text x="260" y="85" fill="#0b2d4f" font-weight="normal" font-size="11.5">from zero</text>
      <rect x="365" y="30" width="150" height="80" rx="12" fill="#fff7e8" stroke="#d9822b"/><text x="440" y="65" fill="#8a4b00">3. Your role</text><text x="440" y="85" fill="#8a4b00" font-weight="normal" font-size="11.5">what you'd do</text>
      <rect x="545" y="30" width="150" height="80" rx="12" fill="#0b2d4f"/><text x="620" y="65" fill="#fff">4. Revision</text><text x="620" y="85" fill="#cfe0f1" font-weight="normal" font-size="11.5">summary &amp; glossary</text>
    </g>
    <g stroke="#2e6da4" stroke-width="3"><path d="M155 70 H180" marker-end="url(#arc)"/><path d="M335 70 H360" marker-end="url(#arc)"/><path d="M515 70 H540" marker-end="url(#arc)"/></g>
  </svg>

  <h3>How to use this guide</h3>
  <ul>
    <li><b>No prior knowledge needed.</b> Every term is explained the first time it appears, and there's a glossary at the back.</li>
    <li><b>Short of time?</b> Read the HireVue pages, "What is SJP?", "How SJP makes money", "What makes SJP different" and the 60-second summary.</li>
    <li>Box colours: <span style="color:#2e6da4"><b>blue</b></span> = key idea · <span style="color:#d9822b"><b>orange</b></span> = interview tip · <span style="color:#c0392b"><b>red</b></span> = common mistake · <span style="color:#2f8f4e"><b>green</b></span> = a line you can say.</li>
    <li>Numbers come from SJP's own reports (2025 annual results, 2026 half-year results) unless marked <b>"press"</b> (news report) or <b>"≈"</b> (rounded or estimated).</li>
  </ul>

  <h3>Contents</h3>
  <div class="grid2" style="font-size:9pt">
    <div>
      <b style="color:#1f6b39">PART 1 · HIREVUE</b><br>
      What to expect &amp; how to answer · Question bank (motivation &amp; commercial) · Question bank (competency &amp; curveballs)<br><br>
      <b style="color:#0b2d4f">PART 2 · THE FIRM FROM ZERO</b><br>
      Why people pay for advice · Ten words you need · Types of money firm · What SJP is · History · How the group is structured · The Partnership · Who the clients are · Client types &amp; industries · What SJP sells · Every product explained · Why pensions matter · Why these products for these clients
    </div>
    <div>
      What clients pay · Fee-based <i>and</i> retention-based · How SJP makes profit · Which products make the most money · The leaky bucket · How the parts work together · A client's journey · What makes SJP different (4 pages) · Real examples, "mandates" &amp; news · What went wrong · What's happening now · Strategy &amp; the future · Competitors · Ten fascinating things<br><br>
      <b style="color:#8a4b00">PART 3 · YOUR ROLE</b><br>
      What wealth management means · Where you'd sit · What you'd do · How your work links to profit<br><br>
      <b>PART 4 · REVISION</b><br>
      60-second summary · Glossary
    </div>
  </div>
  <p class="small">Prepared 6 November 2026. Facts can change; check sjp.co.uk news and the share price the week of your interview.</p>
</section>
'''

S['HV1'] = r'''
<section>
  <div class="step" style="background:#2f8f4e">PART 1 · HIREVUE · 1 of 3</div>
  <h2>What to expect in the HireVue</h2>
  <p class="lead">A <b>HireVue</b> is a <b>one-way recorded video interview</b>. No person is on the call. A question appears on screen, you get some time to think, then you record your answer to the webcam. Recruiters watch the recordings later.</p>

  <svg viewBox="0 0 700 140">
    <defs><marker id="arh" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#2f8f4e"/></marker></defs>
    <g font-size="12" text-anchor="middle">
      <rect x="5" y="25" width="150" height="80" rx="10" fill="#eaf6ee" stroke="#2f8f4e"/><text x="80" y="55" font-weight="bold">1. Question</text><text x="80" y="73">appears on screen</text><text x="80" y="89">(text or video)</text>
      <rect x="185" y="25" width="150" height="80" rx="10" fill="#eaf6ee" stroke="#2f8f4e"/><text x="260" y="55" font-weight="bold">2. Think time</text><text x="260" y="73">usually ≈30 sec</text><text x="260" y="89">to 1 min</text>
      <rect x="365" y="25" width="150" height="80" rx="10" fill="#eaf6ee" stroke="#2f8f4e"/><text x="440" y="55" font-weight="bold">3. Record</text><text x="440" y="73">usually ≈1–3 min</text><text x="440" y="89">per answer</text>
      <rect x="545" y="25" width="150" height="80" rx="10" fill="#0b2d4f"/><text x="620" y="55" font-weight="bold" fill="#fff">4. Repeat</text><text x="620" y="73" fill="#fff">typically 4–8</text><text x="620" y="89" fill="#fff">questions</text>
    </g>
    <g stroke="#2f8f4e" stroke-width="3"><path d="M155 65 H180" marker-end="url(#arh)"/><path d="M335 65 H360" marker-end="url(#arh)"/><path d="M515 65 H540" marker-end="url(#arh)"/></g>
    <text x="350" y="130" text-anchor="middle" font-size="11" fill="#6b7280">Timings vary by employer. Your invite and the practice question will show SJP's exact settings.</text>
  </svg>

  <div class="box"><span class="label">What past SJP candidates report (Glassdoor, anonymous, mostly older)</span>
  • One described <b>four questions with one minute to prepare each</b>.<br>
  • Reported questions included: <i>"Why do you want to work in wealth management and at SJP?"</i>, <i>"What excites you about SJP?"</i>, <i>"How does SJP make money?"</i>, <i>"Tell us about a time you made a mistake and what you learned"</i>, <i>"How have you shown leadership?"</i> and <i>"What is your greatest weakness?"</i>.<br>
  • Candidate tip: <b>"Know the company and why you want to work there."</b></div>

  <h3>How to structure every answer</h3>
  <div class="grid2">
    <div class="card"><h4>For "Why…?" / business questions: 3-point answer</h4><p><b>1. Headline</b> (one sentence answer) → <b>2. Two or three reasons</b>, each with one specific SJP fact → <b>3. Link back to you</b> and the role.</p></div>
    <div class="card"><h4>For "Tell us about a time…": STAR</h4><p><b>S</b>ituation (1 line) → <b>T</b>ask (1 line) → <b>A</b>ction (most of your time: what <i>you</i> did) → <b>R</b>esult (a number if possible, plus what you learned).</p></div>
  </div>

  <h3>Practical checklist</h3>
  <div class="grid3">
    <div class="card"><p>✔ Do the <b>practice question</b> first to test camera and sound</p></div>
    <div class="card"><p>✔ Camera at <b>eye level</b>, light in front of you, plain background</p></div>
    <div class="card"><p>✔ Look at the <b>camera</b>, not the screen</p></div>
    <div class="card"><p>✔ Keep a <b>sticky note</b> of 3–4 SJP facts beside the camera</p></div>
    <div class="card"><p>✔ Aim for <b>≈60–90 seconds</b> unless told otherwise</p></div>
    <div class="card"><p>✔ Smile, slow down, and <b>finish on a clear last line</b></p></div>
  </div>
  <div class="warn"><span class="label">Don't</span>Read from a script (it shows), use jargon you can't explain, or run out the clock without reaching your point. Headline first.</div>
</section>
'''

S['HV2'] = r'''
<section style="font-size:8.7pt; line-height:1.3">
  <div class="step" style="background:#2f8f4e">PART 1 · HIREVUE · 2 of 3</div>
  <h2>Question bank: motivation and commercial awareness</h2>
  <p class="lead">These are the most likely questions. For each one: <b>what they're really testing</b>, and <b>the angle to take</b>. Page numbers point to where the facts are in this guide.</p>
  <table>
    <tr><th style="width:27%">Question</th><th style="width:22%">What they're testing</th><th>Your angle (fill in with your own story)</th></tr>
    <tr><td><b>Why St. James's Place?</b></td><td>Have you researched <i>us</i>, not just "finance"?</td><td>UK's largest advice business (≈£240bn, 1m+ clients, ≈5,000 Partners). Its unique Partnership life-cycle (Academy → BSP). Joining at the start of the "Amplify" growth phase in 2027. Pick one thing you genuinely find fascinating (see "Ten fascinating things").</td></tr>
    <tr><td><b>Why wealth management?</b></td><td>Do you understand what WM is, and do you care about clients?</td><td>It's about real people's life decisions: retirement, family, inheritance. Mention a personal link if you have one (family, part-time job). Advice gap: many people need help and don't get it.</td></tr>
    <tr><td><b>Why this graduate programme?</b></td><td>Do you know it's head office, not advising?</td><td>Rotations give a view of the whole advice system. The Level 4 Diploma gives technical depth. Data, projects and the CEO Office let you shape how ≈5,000 advisers work. <b>Don't</b> say "I want to be an adviser".</td></tr>
    <tr><td><b>What do you know about SJP? / How does SJP make money?</b></td><td>Commercial awareness</td><td>Vertically integrated: advice + products + funds. Earns yearly % fees on money looked after (≈1.6–1.7% all-in for clients; SJP keeps ≈0.45%). Pensions are 55% of the money. Profit = money × margin − costs. Retention ≈95% is what makes it work.</td></tr>
    <tr><td><b>What challenges does SJP / the industry face?</b></td><td>Balanced, mature thinking</td><td>(1) Turning strong gross inflows into stronger <i>net</i> inflows. (2) Fee pressure after the 2025 fee change, plus low-cost rivals. (3) AI and "targeted support" at the cheaper end. (4) Keeping and attracting top advisers. Close with an opportunity: pensions entering inheritance tax from 2027.</td></tr>
    <tr><td><b>Tell us about a recent news story about SJP or the industry.</b></td><td>Do you follow the market?</td><td>Q3 2026 update (net inflows slowed to £0.57bn, record £242bn). SJP's AI tools (Advice Assistant, SOFI). NatWest buying Evelyn Partners. Pensions entering IHT in April 2027. Give the fact, then <b>why it matters</b>.</td></tr>
    <tr><td><b>What do you think of SJP's fee change / the controversy?</b></td><td>Can you discuss a sensitive topic calmly?</td><td>What happened (exit fees, £426m refund provision) → what SJP changed (clear tiered fees, no exit fees on new money, refunds nearly done) → what's next (proving value under Consumer Duty). Fair and factual, about 20 seconds.</td></tr>
    <tr><td><b>Who are SJP's competitors, and what makes SJP different?</b></td><td>Market understanding</td><td>Quilter (closest), Rathbones/Evelyn (investment managers), AJ Bell/Hargreaves (DIY). SJP's edge: scale of the Partnership, the Academy, BSP succession market, advice guarantee, AI at scale.</td></tr>
    <tr><td><b>Where do you see yourself in 5 years?</b></td><td>Commitment to <i>this</i> path</td><td>Level 4 qualified, specialising in an area of the WM division (proposition, data, strategy), having delivered projects that helped Partners and clients.</td></tr>
  </table>
</section>
'''

S['HV3'] = r'''
<section style="font-size:9.3pt; line-height:1.36">
  <div class="step" style="background:#2f8f4e">PART 1 · HIREVUE · 3 of 3</div>
  <h2>Question bank: competency and curveballs</h2>
  <p class="lead">Each competency question maps to a line in the job description. Prepare <b>4–5 stories</b> from your life (uni, work, societies, sport) that you can reuse across these.</p>
  <table>
    <tr><th style="width:30%">Question</th><th style="width:22%">Job description link</th><th>What a strong answer shows</th></tr>
    <tr><td>Tell us about a time you used <b>data</b> to solve a problem or make a decision.</td><td>"Analyse data and produce insights"</td><td>A real dataset, the tool you used (Excel etc.), the insight, the recommendation, and the result in numbers.</td></tr>
    <tr><td>Describe a time you <b>explained something complex</b> to someone without your knowledge.</td><td>"Excellent communication"; reports for senior leaders</td><td>You adapted to your audience, used simple language or visuals, and checked they understood.</td></tr>
    <tr><td>Tell us about a time you <b>managed competing priorities</b>.</td><td>"Manage competing priorities… fast-paced"</td><td>How you ranked tasks (urgent vs important), communicated early, and delivered both.</td></tr>
    <tr><td>Tell us about a time you <b>took initiative</b> / showed leadership.</td><td>"Show initiative… take ownership"</td><td>You spotted something nobody asked you to fix, acted, and others followed.</td></tr>
    <tr><td>Describe a time you had to <b>adapt to change</b>.</td><td>"Adaptability"; rotating teams</td><td>A change you didn't choose, how you got up to speed fast, and what you'd do the same next time.</td></tr>
    <tr><td>Tell us about a time you <b>built a relationship</b> or worked in a team.</td><td>"Relationship-building"; working with Partners</td><td>Understanding the other person's needs, building trust, and a shared result.</td></tr>
    <tr><td>Tell us about a <b>mistake</b> and what you learned. / Your greatest <b>weakness</b>?</td><td>Self-awareness, "willingness to learn"</td><td>A real (not disastrous) mistake, ownership, and a concrete change you made since.</td></tr>
  </table>

  <h3>Possible curveballs (good to have a 30-second view on)</h3>
  <div class="grid2">
    <div class="card"><h4>"Will AI replace financial advisers?"</h4><p>Not the relationship. AI takes the admin. SJP's tools save ≈90 min per case (Advice Assistant), and SJP says pilot firms using SOFI grew new clients faster. Complex, emotional decisions still need people.</p></div>
    <div class="card"><h4>"How would you explain an ISA / pension to a client?"</h4><p>ISA = a box where up to £20k a year grows tax-free and you can take it out any time. Pension = a box for retirement: the government tops up your savings with tax relief, but you can't touch it until your late 50s.</p></div>
    <div class="card"><h4>"What does good client outcome mean?"</h4><p>Consumer Duty: the client gets a product that fits, at fair value, understands it, and gets support. And the firm can <b>prove</b> it.</p></div>
    <div class="card"><h4>"If you could change one thing at SJP…"</h4><p>Example: use data to spot clients likely to leave early and prompt a Partner review, which attacks the "leaky bucket" (net inflows).</p></div>
  </div>
  <div class="tip"><span class="label">Your story bank</span>Write 5 stories on a page: <b>data</b> · <b>teamwork</b> · <b>leadership/initiative</b> · <b>pressure/priorities</b> · <b>mistake/learning</b>. Most questions can be answered with one of these.</div>
</section>
'''

S['HISTORY'] = r'''
<section>
  <div class="step">PART 2 · THE FIRM</div>
  <h2>A short history of SJP (1991 → today)</h2>
  <p class="lead">SJP is only about 35 years old. It grew from a start-up into a FTSE 100 company by building a huge network of advisers.</p>
  <svg viewBox="0 0 700 430">
    <line x1="80" y1="15" x2="80" y2="420" stroke="#9db7d3" stroke-width="5"/>
    <g font-size="11.5">
      <circle cx="80" cy="25" r="9" fill="#0b2d4f"/><text x="20" y="29" font-weight="bold">1991</text><text x="100" y="29"><tspan font-weight="bold">Founded</tspan> as J. Rothschild Assurance by Sir Mark Weinberg, Mike Wilson &amp; Lord (Jacob) Rothschild</text>
      <circle cx="80" cy="55" r="9" fill="#0b2d4f"/><text x="20" y="59" font-weight="bold">1992</text><text x="100" y="59">Starts trading. Business Sale &amp; Purchase (adviser succession) scheme begins</text>
      <circle cx="80" cy="85" r="9" fill="#0b2d4f"/><text x="20" y="89" font-weight="bold">1997</text><text x="100" y="89">Listed on the stock market via St. James's Place Capital; joins the FTSE 250</text>
      <circle cx="80" cy="115" r="9" fill="#2e6da4"/><text x="20" y="119" font-weight="bold">2000</text><text x="100" y="119">Halifax buys 60% (later HBOS, then Lloyds Banking Group)</text>
      <circle cx="80" cy="145" r="9" fill="#2e6da4"/><text x="20" y="149" font-weight="bold">2002</text><text x="100" y="149">Outsources administration to tech firm SS&amp;C (still its back office, on the Bluedoor platform)</text>
      <circle cx="80" cy="175" r="9" fill="#2e6da4"/><text x="20" y="179" font-weight="bold">2006</text><text x="100" y="179">Renamed simply "St. James's Place"</text>
      <circle cx="80" cy="205" r="9" fill="#2e6da4"/><text x="20" y="209" font-weight="bold">2012</text><text x="100" y="209">Launches the <tspan font-weight="bold">Financial Adviser Academy</tspan> to train its own advisers</text>
      <circle cx="80" cy="235" r="9" fill="#2e6da4"/><text x="20" y="239" font-weight="bold">2013</text><text x="100" y="239">Lloyds sells its last shares. SJP becomes fully independent. (Also: RDR bans commission across the industry)</text>
      <circle cx="80" cy="265" r="9" fill="#2f8f4e"/><text x="20" y="269" font-weight="bold">2014</text><text x="100" y="269">Joins the <tspan font-weight="bold">FTSE 100</tspan>; enters Asia by buying The Henley Group</text>
      <circle cx="80" cy="295" r="9" fill="#2f8f4e"/><text x="20" y="299" font-weight="bold">2016</text><text x="100" y="299">Buys <tspan font-weight="bold">Rowan Dartington</tspan>: adds bespoke portfolio management and stockbroking</text>
      <circle cx="80" cy="325" r="9" fill="#2f8f4e"/><text x="20" y="329" font-weight="bold">2022</text><text x="100" y="329">Launches <tspan font-weight="bold">Polaris</tspan>, which becomes the UK's largest multi-asset fund range by 2024 (press)</text>
      <circle cx="80" cy="355" r="9" fill="#c0392b"/><text x="20" y="359" font-weight="bold">2023–24</text><text x="100" y="359">Fee criticism; Dubai office opens; new CEO Mark FitzPatrick; £426m refund provision; shares fall</text>
      <circle cx="80" cy="385" r="9" fill="#d9822b"/><text x="20" y="389" font-weight="bold">2025</text><text x="100" y="389">New simple fee structure (Aug); Polaris Multi-Index launched; record £220bn</text>
      <circle cx="80" cy="415" r="9" fill="#d9822b"/><text x="20" y="419" font-weight="bold">2026–27</text><text x="100" y="419">Record £242bn; 20+ AI tools; 5,000th BSP deal; "Amplify" growth phase from 2027</text>
    </g>
  </svg>
  <div class="box"><span class="label">Why the founders matter</span>Sir Mark Weinberg had already built two big UK savings firms (Abbey Life and Allied Dunbar) using large teams of advisers. SJP was his third version of the idea, and the "Partnership" of self-employed advisers comes from that playbook. <span class="small">(Founders and dates: SJP's heritage page. Weinberg background: general knowledge, so verify if you quote it.)</span></div>
</section>
'''

S['STRUCTURE'] = r'''
<section style="font-size:9.5pt; line-height:1.38">
  <div class="step">PART 2 · THE FIRM</div>
  <h2>How the group is structured</h2>
  <p class="lead">SJP is one listed company that owns a set of smaller companies, each with a job. You don't need to memorise the legal names. Understand the <b>jobs</b>.</p>
  <svg viewBox="0 0 700 330">
    <g font-size="11" text-anchor="middle">
      <rect x="225" y="5" width="250" height="48" rx="10" fill="#0b2d4f"/><text x="350" y="25" fill="#fff" font-weight="bold" font-size="12.5">St. James's Place plc</text><text x="350" y="42" fill="#cfe0f1">listed parent company (LSE: STJ, FTSE 100)</text>
      <line x1="350" y1="53" x2="350" y2="75" stroke="#0b2d4f" stroke-width="2"/><line x1="70" y1="75" x2="630" y2="75" stroke="#0b2d4f" stroke-width="2"/>
      <g>
        <line x1="70" y1="75" x2="70" y2="92" stroke="#0b2d4f" stroke-width="2"/>
        <rect x="5" y="92" width="130" height="95" rx="8" fill="#d9822b"/><text x="70" y="112" fill="#fff" font-weight="bold">SJP Wealth</text><text x="70" y="127" fill="#fff" font-weight="bold">Management plc</text><text x="70" y="146" fill="#fff">ADVICE: legally</text><text x="70" y="160" fill="#fff">responsible for</text><text x="70" y="174" fill="#fff">Partners ★ you</text>
      </g>
      <g>
        <line x1="210" y1="75" x2="210" y2="92" stroke="#0b2d4f" stroke-width="2"/>
        <rect x="145" y="92" width="130" height="95" rx="8" fill="#eef3f8" stroke="#0b2d4f"/><text x="210" y="112" font-weight="bold">SJP UK plc</text><text x="210" y="127" font-weight="bold">(life company)</text><text x="210" y="146">PRODUCTS: pensions</text><text x="210" y="160">&amp; onshore bonds</text><text x="210" y="174">(insurance-based)</text>
      </g>
      <g>
        <line x1="350" y1="75" x2="350" y2="92" stroke="#0b2d4f" stroke-width="2"/>
        <rect x="285" y="92" width="130" height="95" rx="8" fill="#eef3f8" stroke="#0b2d4f"/><text x="350" y="112" font-weight="bold">SJP International</text><text x="350" y="127" font-weight="bold">plc (Dublin)</text><text x="350" y="146">PRODUCTS:</text><text x="350" y="160">offshore</text><text x="350" y="174">investment bonds</text>
      </g>
      <g>
        <line x1="490" y1="75" x2="490" y2="92" stroke="#0b2d4f" stroke-width="2"/>
        <rect x="425" y="92" width="130" height="95" rx="8" fill="#eef3f8" stroke="#0b2d4f"/><text x="490" y="112" font-weight="bold">SJP Unit Trust</text><text x="490" y="127" font-weight="bold">Group</text><text x="490" y="146">PRODUCTS: ISAs</text><text x="490" y="160">&amp; unit trusts;</text><text x="490" y="174">runs the funds</text>
      </g>
      <g>
        <line x1="630" y1="75" x2="630" y2="92" stroke="#0b2d4f" stroke-width="2"/>
        <rect x="565" y="92" width="130" height="95" rx="8" fill="#eef3f8" stroke="#0b2d4f"/><text x="630" y="112" font-weight="bold">Rowan</text><text x="630" y="127" font-weight="bold">Dartington</text><text x="630" y="146">Bespoke portfolios</text><text x="630" y="160">(DFM) &amp;</text><text x="630" y="174">stockbroking</text>
      </g>
      <rect x="5" y="205" width="340" height="50" rx="8" fill="#fff" stroke="#888" stroke-dasharray="4 3"/><text x="175" y="226" font-weight="bold">SJP Asia &amp; Middle East (AME)</text><text x="175" y="243">HK, Singapore, Dubai: expats &amp; local wealthy (£2.3bn)</text>
      <rect x="355" y="205" width="340" height="50" rx="8" fill="#fff" stroke="#888" stroke-dasharray="4 3"/><text x="525" y="226" font-weight="bold">Service companies</text><text x="525" y="243">employ staff, lend to Partners (treasury), admin</text>
      <rect x="5" y="270" width="690" height="55" rx="8" fill="#f3f3f3" stroke="#888"/><text x="350" y="292" font-weight="bold">Outside partners SJP relies on</text><text x="350" y="310">SS&amp;C (administration) · external fund managers (run the money) · Flagstone (cash accounts) · State Street (index funds)</text>
    </g>
  </svg>
  <p class="small">Legal entity names come from SJP filings and company directories. The exact ownership chain is simplified here.</p>

  <h3>Who runs it: the leadership teams</h3>
  <table>
    <tr><th>Area</th><th>Leader</th><th>Job, in one line</th></tr>
    <tr><td>Group</td><td>Mark FitzPatrick, CEO (since Dec 2023)</td><td>Runs the whole company; set the Strengthen → Amplify strategy</td></tr>
    <tr><td>Finance</td><td>Caroline Waddington, CFO</td><td>Money, results, shareholder returns, BSP scheme economics</td></tr>
    <tr><td><b>Wealth Management (your division)</b></td><td><b>James Rainbow, CEO</b> (joined 2025 from Schroders; press)</td><td>Supports and oversees the ≈5,000 Partners: advice, tools, proposition, client service</td></tr>
    <tr><td>Investments</td><td>Justin Onuekwusi, CEO Investments (confirmed 2026)</td><td>Chooses and monitors fund managers; Polaris; asset allocation</td></tr>
    <tr><td>Board</td><td>Paul Manduca, Chair</td><td>Oversees management on behalf of shareholders</td></tr>
  </table>
  <div class="box"><span class="label">Why a "life company"?</span>Pensions and investment bonds are legally <b>insurance products</b>, so SJP owns an insurance company (SJP UK plc) to issue them. That's also why it's regulated by both the <b>FCA</b> (conduct) and the <b>PRA</b> (the Bank of England arm that checks insurers have enough capital).</div>
</section>
'''

S['CLIENTS_REQ'] = r'''
<section>
  <div class="step">PART 2 · CLIENTS</div>
  <h2>Who can be a client, and what's required?</h2>
  <div class="oneline">There is <b>no official firm-wide minimum</b> to become an SJP client. In practice, the business is built for people with <b>tens of thousands to millions</b> to invest. Each Partner sets their own threshold.</div>
  <table>
    <tr><th>What's required</th><th>The reality</th></tr>
    <tr><td><b>Official minimum</b></td><td>None published. Product minimums are low: an SJP ISA can start from <b>£1,500</b> lump sum or <b>£150 a month</b> (SJP FAQ).</td></tr>
    <tr><td><b>Adviser thresholds</b></td><td>Individual Partners often state minimums on adviser directories, e.g. <b>£50k+</b> or <b>£150k+</b> of investable wealth (press/directory listings; they vary).</td></tr>
    <tr><td><b>Special services</b></td><td>Cash savings service (via Flagstone): from <b>£50k</b>. SJP's Asia arm has targeted clients with <b>US$1m+</b> (press).</td></tr>
    <tr><td><b>How you join</b></td><td>Usually a <b>referral</b> or contact form → free first meeting → fact-find → advice → initial advice fee if you go ahead.</td></tr>
    <tr><td><b>The real "requirement"</b></td><td>Enough money and complexity that ≈1.6–1.7% a year buys real value. Average client ≈<b>£226k</b> with SJP.</td></tr>
  </table>

  <h3>Clients by life stage: the main way to think about it</h3>
  <svg viewBox="0 0 700 200">
    <g font-size="11.5" text-anchor="middle">
      <rect x="5" y="20" width="165" height="160" rx="10" fill="#eef3f8"/>
      <text x="87" y="45" font-weight="bold" fill="#0b2d4f" font-size="13">Builders</text><text x="87" y="62">≈30–50</text>
      <text x="87" y="88">Growing income,</text><text x="87" y="104">family, mortgage</text><text x="87" y="130" font-weight="bold">Needs:</text><text x="87" y="146">ISAs, pensions,</text><text x="87" y="162">protection</text>
      <rect x="180" y="20" width="165" height="160" rx="10" fill="#d9822b"/>
      <text x="262" y="45" font-weight="bold" fill="#fff" font-size="13">Pre-retirees ★</text><text x="262" y="62" fill="#fff">≈50–65</text>
      <text x="262" y="88" fill="#fff">Peak wealth, many</text><text x="262" y="104" fill="#fff">old pension pots</text><text x="262" y="130" font-weight="bold" fill="#fff">Needs:</text><text x="262" y="146" fill="#fff">consolidate, plan</text><text x="262" y="162" fill="#fff">retirement date</text>
      <rect x="355" y="20" width="165" height="160" rx="10" fill="#0b2d4f"/>
      <text x="437" y="45" font-weight="bold" fill="#fff" font-size="13">Retirees ★</text><text x="437" y="62" fill="#cfe0f1">≈65+</text>
      <text x="437" y="88" fill="#fff">Living off savings</text><text x="437" y="104" fill="#fff">(drawdown)</text><text x="437" y="130" font-weight="bold" fill="#ffd27a">Needs:</text><text x="437" y="146" fill="#fff">tax-efficient income,</text><text x="437" y="162" fill="#fff">care planning</text>
      <rect x="530" y="20" width="165" height="160" rx="10" fill="#eaf6ee"/>
      <text x="612" y="45" font-weight="bold" fill="#1f6b39" font-size="13">Passing it on</text><text x="612" y="62">older clients &amp; heirs</text>
      <text x="612" y="88">Family wealth</text><text x="612" y="104">moving generations</text><text x="612" y="130" font-weight="bold">Needs:</text><text x="612" y="146">inheritance tax,</text><text x="612" y="162">trusts, gifting</text>
    </g>
  </svg>
  <p>★ = SJP's core. Pensions are 55% of SJP's money, which tells you most clients are approaching or in retirement.</p>
</section>
'''

S['CLIENTS_TYPES'] = r'''
<section style="font-size:9.5pt; line-height:1.38">
  <div class="step">PART 2 · CLIENTS</div>
  <h2>Client types and industries SJP targets</h2>
  <p class="lead">Partners often <b>specialise</b> in a profession or industry. That makes them experts in its specific money problems and lets them win referrals inside that community.</p>
  <table>
    <tr><th style="width:24%">Client type</th><th style="width:38%">Their specific money problem</th><th>How SJP helps</th></tr>
    <tr><td><b>Business owners &amp; company directors</b></td><td>Wealth is locked in the company; how to take money out tax-efficiently; selling the business</td><td>Profit extraction, company pension contributions, exit planning, protecting key people</td></tr>
    <tr><td><b>Doctors, GPs, dentists (NHS)</b></td><td>Complex NHS pension rules, tax charges on large pensions, high incomes</td><td>Specialist NHS pension planning (several Partner practices advertise this)</td></tr>
    <tr><td><b>Lawyers, accountants, professional partnerships</b></td><td>High, uneven incomes; partnership capital; retirement from the partnership</td><td>Tax planning, pensions, and these firms are also <b>referral sources</b> for SJP</td></tr>
    <tr><td><b>Senior corporate employees</b></td><td>Share schemes, bonuses, many workplace pensions</td><td>Consolidation, using allowances, planning for share options</td></tr>
    <tr><td><b>Farmers &amp; rural families</b></td><td>Land-rich, cash-poor; passing on the farm; inheritance tax changes</td><td>Succession and inheritance planning (SJP has produced farm-business material)</td></tr>
    <tr><td><b>Women investors</b></td><td>Career breaks, divorce, widowhood, often under-advised</td><td>SJP and Partners run "advice for women" propositions</td></tr>
    <tr><td><b>Sports professionals</b></td><td>Big income over a short career</td><td>Making peak earnings last a lifetime</td></tr>
    <tr><td><b>Private clients (wealthier)</b></td><td>Larger, more complex wealth</td><td>Bespoke portfolios via Rowan Dartington; a bigger HNW push planned under "Amplify"</td></tr>
    <tr><td><b>Expats &amp; international</b></td><td>Living abroad with UK ties</td><td>SJP Asia &amp; Middle East (Hong Kong, Singapore, Dubai), offshore bonds</td></tr>
    <tr><td><b>Businesses (as employers)</b></td><td>Want to help staff with money</td><td>Workplace financial education and group schemes (opens doors to future individual clients)</td></tr>
  </table>
  <p class="small">Segments drawn from SJP and Partner practice websites. Not every Partner offers every specialism.</p>

  <svg viewBox="0 0 700 120">
    <defs><marker id="arcl" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#2e6da4"/></marker></defs>
    <g font-size="11.5" text-anchor="middle">
      <rect x="5" y="25" width="155" height="70" rx="10" fill="#eef3f8"/><text x="82" y="52" font-weight="bold">Partner specialises</text><text x="82" y="70">e.g. "dentists"</text>
      <rect x="185" y="25" width="155" height="70" rx="10" fill="#eef3f8"/><text x="262" y="52" font-weight="bold">Becomes the expert</text><text x="262" y="70">in that community</text>
      <rect x="365" y="25" width="155" height="70" rx="10" fill="#eef3f8"/><text x="442" y="52" font-weight="bold">Happy clients</text><text x="442" y="70">refer colleagues</text>
      <rect x="545" y="25" width="150" height="70" rx="10" fill="#0b2d4f"/><text x="620" y="52" font-weight="bold" fill="#fff">Cheap, trusted</text><text x="620" y="70" fill="#fff">new clients</text>
    </g>
    <g stroke="#2e6da4" stroke-width="3"><path d="M160 60 H181" marker-end="url(#arcl)"/><path d="M340 60 H361" marker-end="url(#arcl)"/><path d="M520 60 H541" marker-end="url(#arcl)"/></g>
  </svg>
  <div class="box"><span class="label">Why it works</span>Advice is a <b>trust</b> purchase. People trust a recommendation from a colleague in their own profession more than any advert. Specialising turns each Partner into a referral engine.</div>
</section>
'''

S['PRODUCTS_DEEP'] = r'''
<section style="font-size:8.5pt; line-height:1.28">
  <div class="step">PART 2 · PRODUCTS</div>
  <h2 style="font-size:15pt">Every product: why it exists, who it's for, SJP vs rivals</h2>
  <table>
    <tr><th style="width:15%">Product</th><th style="width:25%">Why it exists (the problem it solves)</th><th style="width:18%">Typical SJP client</th><th style="width:20%">SJP's version</th><th>How it differs from competitors</th></tr>
    <tr><td><b>Pension</b><br>(personal pension, SIPP, drawdown)</td><td>The government gives tax relief to encourage retirement saving. Since 2015 retirees can keep it invested and draw income.</td><td>50–70 year olds with several old pots</td><td>SJP pension (Retirement Account) invested in SJP funds, e.g. Polaris. £120bn</td><td>Rivals: DIY SIPPs (AJ Bell ≈0.25% platform fee) or IFA + platform. SJP bundles advice + wrapper + funds in one place, at ≈1.67% a year all-in.</td></tr>
    <tr><td><b>ISA</b></td><td>£20k a year can grow tax-free; flexible access</td><td>Almost everyone with savings</td><td>SJP ISA, from £1,500 lump sum</td><td>The same ISA is available almost anywhere; SJP's difference is the advice and fund range. Total ≈1.59% a year in Polaris.</td></tr>
    <tr><td><b>Unit trust</b><br>(general account)</td><td>Investing beyond ISA and pension limits</td><td>Wealthier clients who've used their allowances</td><td>SJP unit trusts (the funds themselves)</td><td>Similar to any fund account; taxable.</td></tr>
    <tr><td><b>Investment bond</b><br>(onshore &amp; offshore)</td><td>An insurance-based wrapper: tax is <b>deferred</b>, 5% a year can be withdrawn without immediate tax, and it works well in <b>trusts</b> for inheritance planning</td><td>Wealthy clients, retirees, inheritance planners</td><td>Issued by SJP's own life companies (UK &amp; Dublin). £44bn</td><td><b>Less common at DIY platforms</b>, so this is a genuine advice-led product. Owning a life company lets SJP offer it in-house.</td></tr>
    <tr><td><b>Discretionary portfolios</b> (DFM)</td><td>A manager makes buy/sell decisions on a bespoke portfolio</td><td>Wealthier private clients</td><td>Rowan Dartington. ≈£3.7bn</td><td>Competes with Rathbones, Evelyn, Quilter Cheviot; small for SJP.</td></tr>
    <tr><td><b>Cash savings</b></td><td>Earning interest on cash awaiting investment, or as an emergency pot</td><td>Clients holding large cash</td><td>Via partner Flagstone, from £50k; cash ISAs too</td><td>Keeps the client's cash "inside" the SJP relationship.</td></tr>
    <tr><td><b>Protection</b></td><td>Pays out if you die, fall ill or can't work</td><td>Families, business owners</td><td>Life cover, critical illness, income protection</td><td>Standard market products; an add-on to holistic advice.</td></tr>
    <tr><td><b>Mortgages &amp; wills</b></td><td>Buying property; who inherits what</td><td>Families</td><td>Through <b>separate firms</b>, not SJP itself</td><td>Rounds out the "whole of life" service.</td></tr>
  </table>

  <h3>The funds inside the products</h3>
  <p><b>Polaris (2022):</b> four ready-made portfolios from cautious (1) to adventurous (4), ≈£94bn. In 2024 it overtook Vanguard LifeStrategy as the UK's largest multi-asset range (City AM). <b>Polaris Multi-Index (2025):</b> a cheaper index-based version (≈0.2% fund charge, press), built with State Street, &gt;£1bn. <b>Single-strategy funds</b>, e.g. Global Smaller Companies (£1.9bn), are run by outside managers SJP hires and replaces.</p>
  <p style="color:#c0392b"><b>Fair comparison:</b> critics compare SJP's ≈1.6–1.7% with Vanguard LifeStrategy's ≈0.22%, but that compares advice + wrapper + fund with a fund alone. The real question is whether the advice is worth the difference to that client.</p>
</section>
'''

S['WHY_PRODUCTS'] = r'''
<section>
  <div class="step">PART 2 · PRODUCTS</div>
  <h2>Why these products, for these clients?</h2>
  <p class="lead">Each SJP product answers a specific life need. The adviser's job is to match the need to the box.</p>
  <svg viewBox="0 0 700 330">
    <defs><marker id="arw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#2e6da4"/></marker></defs>
    <text x="150" y="18" text-anchor="middle" font-size="13" font-weight="bold">Client says…</text>
    <text x="550" y="18" text-anchor="middle" font-size="13" font-weight="bold">SJP recommends…</text>
    <g font-size="11.5">
      <rect x="10" y="30" width="280" height="40" rx="8" fill="#eef3f8"/><text x="22" y="55">"I want to retire comfortably at 62"</text>
      <rect x="410" y="30" width="280" height="40" rx="8" fill="#0b2d4f"/><text x="422" y="55" fill="#fff">Pension (consolidate pots) + Polaris</text>
      <rect x="10" y="80" width="280" height="40" rx="8" fill="#eef3f8"/><text x="22" y="105">"I'm retired and need a steady income"</text>
      <rect x="410" y="80" width="280" height="40" rx="8" fill="#0b2d4f"/><text x="422" y="105" fill="#fff">Pension drawdown + ISA withdrawals</text>
      <rect x="10" y="130" width="280" height="40" rx="8" fill="#eef3f8"/><text x="22" y="155">"I want my children to inherit, not the taxman"</text>
      <rect x="410" y="130" width="280" height="40" rx="8" fill="#0b2d4f"/><text x="422" y="155" fill="#fff">Investment bond in a trust + gifting plan</text>
      <rect x="10" y="180" width="280" height="40" rx="8" fill="#eef3f8"/><text x="22" y="205">"I want my savings to grow tax-free"</text>
      <rect x="410" y="180" width="280" height="40" rx="8" fill="#0b2d4f"/><text x="422" y="205" fill="#fff">ISA (£20k a year) in Polaris</text>
      <rect x="10" y="230" width="280" height="40" rx="8" fill="#eef3f8"/><text x="22" y="255">"What if I die or get ill?"</text>
      <rect x="410" y="230" width="280" height="40" rx="8" fill="#0b2d4f"/><text x="422" y="255" fill="#fff">Protection (life / illness cover)</text>
      <rect x="10" y="280" width="280" height="40" rx="8" fill="#eef3f8"/><text x="22" y="305">"I'm selling my business next year"</text>
      <rect x="410" y="280" width="280" height="40" rx="8" fill="#0b2d4f"/><text x="422" y="305" fill="#fff">Exit plan + pension + bond + ISA mix</text>
    </g>
    <g stroke="#2e6da4" stroke-width="2.5"><path d="M290 50 H405" marker-end="url(#arw)"/><path d="M290 100 H405" marker-end="url(#arw)"/><path d="M290 150 H405" marker-end="url(#arw)"/><path d="M290 200 H405" marker-end="url(#arw)"/><path d="M290 250 H405" marker-end="url(#arw)"/><path d="M290 300 H405" marker-end="url(#arw)"/></g>
  </svg>
  <h3>Why SJP sells <i>its own</i> products (the business logic)</h3>
  <div class="grid2">
    <div class="card"><h4>For SJP</h4><p>Owning the box and the fund means SJP earns a fee at <b>every layer</b>, not just for the advice. Money in its own products is also easier to keep.</p></div>
    <div class="card"><h4>For the adviser</h4><p>One joined-up system: paperwork, research, fund choice and compliance are done for them, so they can spend more time with clients.</p></div>
    <div class="card"><h4>For the client</h4><p>One relationship, one statement, one place for everything, and a FTSE 100 firm standing behind the advice.</p></div>
    <div class="card"><h4>The trade-off</h4><p>"Restricted" advice: the client isn't shown the whole market. This is why fees and value are scrutinised so closely under Consumer Duty.</p></div>
  </div>
</section>
'''

S['MONEY_MODEL'] = r'''
<section style="font-size:9pt; line-height:1.33">
  <div class="step">PART 2 · THE MONEY</div>
  <h2>Is it fee-based or retention-based? Both, and here's why</h2>
  <div class="oneline">SJP charges <b>fees</b> (a yearly % of the client's money). Because the fee repeats every year the money stays, <b>retention</b> is what turns those fees into a big profit. Fees are the price; retention is the multiplier.</div>

  <h3>How one £100,000 client is worth more the longer they stay</h3>
  <svg viewBox="0 0 700 230" style="max-height:52mm">
    <line x1="60" y1="190" x2="680" y2="190" stroke="#333" stroke-width="2"/>
    <line x1="60" y1="190" x2="60" y2="20" stroke="#333" stroke-width="2"/>
    <text x="370" y="222" text-anchor="middle" font-size="12">Years the client stays</text>
    <text x="22" y="105" font-size="12" transform="rotate(-90 22 105)" text-anchor="middle">Total fees (≈ to SJP)</text>
    <g font-size="11" text-anchor="middle">
      <rect x="100" y="184" width="80" height="6" fill="#9db7d3"/><text x="140" y="177">≈£450</text><text x="140" y="205">1 year</text>
      <rect x="240" y="161" width="80" height="29" fill="#6f98c4"/><text x="280" y="154">≈£2,400</text><text x="280" y="205">5 years</text>
      <rect x="380" y="126" width="80" height="64" fill="#2e6da4"/><text x="420" y="119">≈£5,400</text><text x="420" y="205">10 years</text>
      <rect x="520" y="30" width="80" height="160" fill="#0b2d4f"/><text x="560" y="23">≈£13,400</text><text x="560" y="205">20 years</text>
    </g>
  </svg>
  <p class="small">Illustration only: assumes SJP keeps ≈0.45% a year and the pot grows ≈4% a year after charges. Not SJP figures.</p>

  <div class="grid2">
    <div class="card"><h4>Why SJP charges this way</h4><p>
      • <b>The law pushed it:</b> since 2013 (the RDR) advisers can't take commissions from product providers; they charge clients directly.<br>
      • <b>It's aligned:</b> if the client's money grows, SJP earns more. If it falls, SJP earns less.<br>
      • <b>It's predictable:</b> recurring income, like a subscription.<br>
      • <b>It scales:</b> one adviser can look after ≈£49m.</p></div>
    <div class="card"><h4>Why retention matters so much</h4><p>
      • Winning a client costs time and money (initial advice, admin).<br>
      • The profit comes from the <b>years after</b>.<br>
      • SJP keeps ≈<b>95%</b> of money each year, so the average pound stays a long time.<br>
      • Pensions are the stickiest (≈4% leave a year), which is why they matter most.</p></div>
  </div>

  <h3>Old model vs new model</h3>
  <table>
    <tr><th></th><th>Before Aug 2025</th><th>After Aug 2025</th></tr>
    <tr><td>Upfront cost</td><td>Hidden. SJP paid the adviser up front and recovered it over 6 years</td><td>Clear initial advice fee (3/2/1%, max £30k)</td></tr>
    <tr><td>Leaving early</td><td>Exit fee up to 6% (bonds &amp; pensions)</td><td>No exit fee on new money</td></tr>
    <tr><td>When SJP earns</td><td>Mainly after year 6 ("gestation")</td><td>From day one, at a lower rate</td></tr>
    <tr><td>Retention</td><td>Partly enforced by exit fees</td><td>Must be <b>earned</b> through good service</td></tr>
  </table>
  <div class="box"><span class="label">The big shift</span>The old model partly <b>locked</b> clients in. The new model has to <b>earn</b> retention through service and value. That's why the Wealth Management division (advice quality, client experience, Partner tools) is now so central.</div>
</section>
'''

S['WHICH_PRODUCTS'] = r'''
<section>
  <div class="step">PART 2 · THE MONEY</div>
  <h2>Which products make the most money?</h2>
  <p class="lead">SJP doesn't publish profit by product. But we can work it out from where the money sits, where new money goes, and how long it stays.</p>
  <svg viewBox="0 0 700 260">
    <text x="20" y="20" font-size="13" font-weight="bold">Share of money looked after vs share of new money (2025)</text>
    <g font-size="12">
      <text x="20" y="55" font-weight="bold">Pensions</text>
      <rect x="160" y="40" width="303" height="20" fill="#0b2d4f"/><text x="470" y="55">55% of money</text>
      <rect x="160" y="62" width="347" height="14" fill="#d9822b"/><text x="514" y="74">63% of new money</text>
      <text x="20" y="115" font-weight="bold">ISA / unit trust / DFM</text>
      <rect x="160" y="100" width="138" height="20" fill="#0b2d4f"/><text x="305" y="115">25%</text>
      <rect x="160" y="122" width="127" height="14" fill="#d9822b"/><text x="294" y="134">23%</text>
      <text x="20" y="175" font-weight="bold">Investment bonds</text>
      <rect x="160" y="160" width="110" height="20" fill="#0b2d4f"/><text x="277" y="175">20%</text>
      <rect x="160" y="182" width="77" height="14" fill="#d9822b"/><text x="244" y="194">14%</text>
      <rect x="160" y="222" width="18" height="12" fill="#0b2d4f"/><text x="184" y="233">money looked after</text>
      <rect x="340" y="222" width="18" height="12" fill="#d9822b"/><text x="364" y="233">new money in 2025</text>
    </g>
  </svg>

  <table>
    <tr><th>Rank (≈)</th><th>Product</th><th>Why</th></tr>
    <tr><td><b>1</b></td><td><b>Pensions</b></td><td>Biggest pile (£120bn), most new money, and the <b>stickiest</b> (≈4% leaves a year). Most of the ≈£53bn "gestation" money moving onto full fees by ≈2031 is pensions and bonds, so profits from it should <b>rise</b>.</td></tr>
    <tr><td><b>2</b></td><td><b>Investment bonds</b></td><td>£44bn, long-term, often in trusts (very sticky). Wealthier clients.</td></tr>
    <tr><td><b>3</b></td><td><b>ISAs / unit trusts</b></td><td>£56bn, but the most likely to be withdrawn (≈7% a year), and a slightly lower product fee (0.27% vs 0.35%).</td></tr>
    <tr><td>Small</td><td>DFM (Rowan Dartington) &amp; Asia/Middle East</td><td>Still in "investment" mode: in 2025 both were small net <b>costs</b> in SJP's profit table (−£4.1m and −£7.6m).</td></tr>
  </table>

  <h3>And across the layers: who earns what</h3>
  <svg viewBox="0 0 700 110">
    <rect x="20" y="20" width="335" height="45" fill="#d9822b"/><rect x="355" y="20" width="113" height="45" fill="#2e6da4"/><rect x="468" y="20" width="218" height="45" fill="#1a8a7a"/>
    <g font-size="12" fill="#fff" font-weight="bold" text-anchor="middle"><text x="187" y="48">Advice 0.80% → mostly Partner</text><text x="411" y="48">Product 0.27–0.35%</text><text x="577" y="48">Fund ≈0.52% → SJP + managers</text></g>
    <text x="350" y="92" text-anchor="middle" font-size="12">SJP's own net keep across product + fund layers: ≈<tspan font-weight="bold">0.43–0.45%</tspan> of mature money a year (SJP guidance)</text>
  </svg>
  <div class="good"><span class="label">Something you can say</span>"Pensions are SJP's profit engine. They're over half the money, most of the new money, and the stickiest, and much of the older pension money is only now moving onto full charges."</div>
</section>
'''

S['EXAMPLES'] = r'''
<section style="font-size:9.4pt; line-height:1.37">
  <div class="step">PART 2 · REAL EXAMPLES</div>
  <h2>Real examples, "mandates" and news you can quote</h2>
  <div class="box"><span class="label">What's a "mandate"?</span>A <b>mandate</b> is a formal instruction to a fund manager: "manage £X of our money, in this style, against this target". SJP's investment team <b>hands out mandates</b> to outside managers and takes them away if they disappoint. That's how its "hire and fire" model works.</div>
  <table>
    <tr><th style="width:15%">When</th><th style="width:33%">What happened</th><th>Why it's interesting</th></tr>
    <tr><td>2024 (press)</td><td><b>Polaris overtakes Vanguard LifeStrategy</b> as the UK's largest multi-asset fund range</td><td>Shows the distribution power of 5,000 advisers. Critics noted it costs far more, and much of the money came from existing clients switching in.</td></tr>
    <tr><td>2025</td><td><b>Global Smaller Companies fund (£1.9bn)</b>: moved from one manager to <b>seven</b> (six new mandates alongside Northern Trust)</td><td>A textbook "hire and fire" decision: spreading the money across complementary styles.</td></tr>
    <tr><td>2025</td><td><b>Polaris Multi-Index</b> launched with State Street (14 index building blocks; ≈0.2% fund charge, press); &gt;£1bn quickly</td><td>SJP responding to low-cost competition: a cheaper option inside its own system.</td></tr>
    <tr><td>Aug 2025</td><td><b>New fee structure</b> live after ≈2 years' work, costing £119m to implement</td><td>Biggest change in SJP's history; ended exit fees on new money.</td></tr>
    <tr><td>2024–26</td><td><b>Cash service with Flagstone</b>: minimum cut from £250k to £50k; cash ISAs added</td><td>Keeps clients' cash inside the relationship.</td></tr>
    <tr><td>Mar 2026 (press)</td><td><b>5,000th BSP deal</b>; ≈250–300 a year, ≈£200m a year</td><td>A 34-year-old internal market for adviser businesses.</td></tr>
    <tr><td>H1 2026</td><td><b>Largest BSP deal ever</b>; nearly 200 advisers buying</td><td>Succession is accelerating as older advisers retire.</td></tr>
    <tr><td>H1 2026</td><td><b>SOFI</b> AI meeting tool: pilot firms grew new clients faster than a control group; now rolling out</td><td>Evidence that AI helps advisers rather than replaces them.</td></tr>
    <tr><td>H1 2026</td><td><b>Brand:</b> net promoter score and awareness each up 14 points since end-2023</td><td>Reputation recovering after the 2024 crisis.</td></tr>
    <tr><td>Oct 2026</td><td><b>200 new advisers</b> graduate from the Academy</td><td>SJP says it trains ≈half of all new UK advisers.</td></tr>
    <tr><td>29 Oct 2026</td><td><b>Q3 update:</b> record £242bn, but net inflows only £0.57bn</td><td>The "leaky bucket" challenge in one number.</td></tr>
  </table>
  <div class="tip"><span class="label">How to use a news item in the HireVue</span><b>Fact</b> (one line) → <b>so what</b> for SJP → <b>link to the role</b>. Example: "SJP's SOFI pilot showed AI tools helping advisers win more clients. That's the kind of Partner-tool project the Wealth Management team runs, and I'd love to measure impact like that."</div>
</section>
'''

S['STRATEGY'] = r'''
<section>
  <div class="step">PART 2 · THE FUTURE</div>
  <h2>SJP's strategy: where it's going, and why</h2>
  <svg viewBox="0 0 700 170">
    <defs><marker id="ars" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10z" fill="#d9822b"/></marker></defs>
    <rect x="5" y="15" width="330" height="140" rx="12" fill="#eef3f8" stroke="#0b2d4f" stroke-width="2"/>
    <text x="170" y="42" text-anchor="middle" font-size="15" font-weight="bold" fill="#0b2d4f">STRENGTHEN · 2024–2026</text>
    <g font-size="12"><text x="20" y="68">✔ New simple fees (Aug 2025)</text><text x="20" y="88">✔ Refund review (finishing 2026)</text><text x="20" y="108">✔ ≈£100m cost cut (by 2027)</text><text x="20" y="128">✔ Polaris Multi-Index, cash, AI tools</text><text x="20" y="148">✔ Shareholder payout raised to 70%</text></g>
    <path d="M340 85 H362" stroke="#d9822b" stroke-width="6" marker-end="url(#ars)"/>
    <rect x="365" y="15" width="330" height="140" rx="12" fill="#0b2d4f"/>
    <text x="530" y="42" text-anchor="middle" font-size="15" font-weight="bold" fill="#ffd27a">AMPLIFY · 2027 →</text>
    <g font-size="12" fill="#fff"><text x="380" y="68">→ Grow faster: more clients, more advisers</text><text x="380" y="88">→ More for wealthier (HNW) clients</text><text x="380" y="108">→ Data &amp; AI to boost adviser productivity</text><text x="380" y="128">→ Stronger brand &amp; Partnership community</text><text x="380" y="148">→ Details due at Feb 2027 results</text></g>
  </svg>

  <h3>The targets SJP has set</h3>
  <div class="grid3">
    <div class="stat"><div class="n">2×</div><div class="t">Double profit (Underlying cash result) from 2023 to 2030</div></div>
    <div class="stat"><div class="n">£100m</div><div class="t">a year of costs removed by 2027</div></div>
    <div class="stat"><div class="n">70%</div><div class="t">of profit returned to shareholders each year from 2026</div></div>
  </div>

  <h3>Why SJP is doing this: the forces behind the strategy</h3>
  <div class="grid2">
    <div class="card"><h4>1. Regulation (Consumer Duty)</h4><p>Firms must prove fair value. Opaque fees and exit charges weren't sustainable, so SJP had to simplify first.</p></div>
    <div class="card"><h4>2. Competition</h4><p>Cheap DIY platforms growing at ≈9% a year; banks buying wealth managers (NatWest–Evelyn). SJP needs to grow, not just stay big.</p></div>
    <div class="card"><h4>3. AI and technology</h4><p>A threat (cheaper digital advice; Feb 2026 share sell-off) and an opportunity (20+ tools across 5,000 advisers). Scale lets SJP invest.</p></div>
    <div class="card"><h4>4. The advice gap and demographics</h4><p>An ageing population, pension freedoms, and pensions entering inheritance tax in 2027 all increase demand for advice.</p></div>
    <div class="card"><h4>5. The adviser shortage</h4><p>Advisers are getting older and rivals compete for them, so the Academy, BSP and new Partner pay become strategic weapons.</p></div>
    <div class="card"><h4>6. Profit maths</h4><p>Lower margins after the fee change mean growth must come from volume, maturing older money, and cost discipline.</p></div>
  </div>
  <div class="good"><span class="label">Something you can say</span>"SJP spent 2024–26 fixing its foundations, with transparent fees, refunds and lower costs. From 2027 it's moving to growth. Joining in September 2027 means arriving right at the start of that."</div>
</section>
'''

S['COMPETITORS'] = r'''
<section>
  <div class="step">PART 2 · THE MARKET</div>
  <h2>Competitors: who SJP is up against</h2>
  <svg viewBox="0 0 700 250">
    <g font-size="11.5" text-anchor="middle">
      <rect x="250" y="95" width="200" height="60" rx="12" fill="#0b2d4f"/><text x="350" y="120" fill="#fff" font-weight="bold" font-size="13">SJP</text><text x="350" y="138" fill="#cfe0f1">advice-led, integrated</text>
      <rect x="10" y="10" width="200" height="70" rx="10" fill="#eef3f8" stroke="#2e6da4"/><text x="110" y="33" font-weight="bold">Quilter</text><text x="110" y="50">closest rival: own advisers +</text><text x="110" y="66">platform + funds · £157bn</text>
      <rect x="490" y="10" width="200" height="70" rx="10" fill="#eef3f8" stroke="#2e6da4"/><text x="590" y="33" font-weight="bold">Rathbones</text><text x="590" y="50">investment manager for</text><text x="590" y="66">wealthier clients · £121bn</text>
      <rect x="10" y="170" width="200" height="70" rx="10" fill="#eef3f8" stroke="#2e6da4"/><text x="110" y="193" font-weight="bold">AJ Bell / Hargreaves</text><text x="110" y="210">DIY platforms, cheap,</text><text x="110" y="226">fast-growing · AJ Bell £126bn</text>
      <rect x="490" y="170" width="200" height="70" rx="10" fill="#eef3f8" stroke="#2e6da4"/><text x="590" y="193" font-weight="bold">Evelyn (NatWest)</text><text x="590" y="210">advice + investment; bought</text><text x="590" y="226">by NatWest in 2026 (£2.7bn)</text>
      <rect x="265" y="5" width="170" height="55" rx="10" fill="#fff7e8" stroke="#d9822b"/><text x="350" y="28" font-weight="bold">Independent advisers</text><text x="350" y="45">thousands of small firms</text>
      <rect x="265" y="190" width="170" height="55" rx="10" fill="#fff7e8" stroke="#d9822b"/><text x="350" y="213" font-weight="bold">Robo / AI / banks</text><text x="350" y="230">low-cost digital help</text>
    </g>
    <g stroke="#9db7d3" stroke-width="2"><line x1="210" y1="60" x2="255" y2="100"/><line x1="490" y1="60" x2="445" y2="100"/><line x1="210" y1="195" x2="255" y2="150"/><line x1="490" y1="195" x2="445" y2="150"/><line x1="350" y1="60" x2="350" y2="95"/><line x1="350" y1="155" x2="350" y2="190"/></g>
  </svg>
  <table>
    <tr><th>Firm</th><th>Model</th><th>New-money growth</th><th>Versus SJP</th></tr>
    <tr><td><b>SJP</b></td><td>Restricted advice + own products + funds</td><td>≈2.5% a year (H1 2026)</td><td>Biggest adviser force; strongest retention system</td></tr>
    <tr><td><b>Quilter</b></td><td>Own advisers + platform used by independent advisers + DFM</td><td>≈9% a year (H1 2026)</td><td>Wins money from independent advisers too; growing faster</td></tr>
    <tr><td><b>Rathbones</b></td><td>Discretionary investment management</td><td>Outflows in H1 2026</td><td>Richer clients; investment-led rather than advice-led</td></tr>
    <tr><td><b>AJ Bell</b></td><td>DIY / adviser platform</td><td>≈9% a year</td><td>Much cheaper, no personal advice; younger clients</td></tr>
    <tr><td><b>Hargreaves Lansdown</b></td><td>DIY platform (private since 2025)</td><td>n/a (private)</td><td>Self-directed investors</td></tr>
    <tr><td><b>Evelyn / NatWest</b></td><td>Bank-owned advice + investment</td><td>n/a</td><td>Can feed bank customers into advice</td></tr>
  </table>
  <div class="box"><span class="label">SJP's edge in one line</span><b>Distribution and loyalty</b>: ≈5,000 advisers, an adviser "factory" (Academy), a succession market (BSP), and ≈95% retention. Its weak spot is <b>growth rate and price</b> against cheaper, faster-growing rivals.</div>
</section>
'''

S['FASCINATING'] = r'''
<section>
  <div class="step" style="background:#d9822b">PART 2 · PICK YOUR "HOOK"</div>
  <h2>Ten genuinely fascinating things about SJP</h2>
  <p class="lead">Recruiters hear "it's a great firm" all day. Pick <b>one</b> of these that you honestly find interesting and use it in "Why SJP?".</p>
  <div class="grid2">
    <div class="card"><h4>1. It builds its own advisers</h4><p>SJP says its Academy trains ≈half of all new UK advisers. 200 graduated in Oct 2026.</p></div>
    <div class="card"><h4>2. It runs a marketplace for advice businesses</h4><p>BSP: 5,000 deals since 1992, ≈£200m a year. Advisers can buy and sell client books, financed by SJP.</p></div>
    <div class="card"><h4>3. It's a fund giant without being a stock-picker</h4><p>Polaris became the UK's biggest multi-asset range, but SJP mainly <b>hires and fires</b> outside managers.</p></div>
    <div class="card"><h4>4. It owns an insurance company</h4><p>That's how it can issue pensions and investment bonds itself, products most advisers must buy from others.</p></div>
    <div class="card"><h4>5. It rebuilt its pricing from scratch</h4><p>A ≈2-year, £119m project ended exit fees and made every charge visible, while keeping ≈95% retention.</p></div>
    <div class="card"><h4>6. AI as a helper, not a replacement</h4><p>Advice Assistant saves ≈90 min per case; SOFI pilot firms won more new clients.</p></div>
    <div class="card"><h4>7. The money stays when advisers retire</h4><p>Clients pass to another SJP Partner via BSP, so the firm keeps the relationship.</p></div>
    <div class="card"><h4>8. A charity built into the culture</h4><p>£130m+ raised; SJP matches every £1; 70%+ of Partners and staff give monthly.</p></div>
    <div class="card"><h4>9. Profits are still to come from the past</h4><p>≈£53bn of older money only reaches full charges over the next ~6 years, so earnings are "baked in".</p></div>
    <div class="card"><h4>10. A turnaround story</h4><p>From a 30% share crash and £426m provision (2024) to record £242bn and a 70% payout (2026), now pivoting to growth.</p></div>
  </div>
  <div class="good"><span class="label">Example "Why SJP?" opener</span>"What fascinates me about SJP is that it isn't just an advice firm. It's built a complete system around its advisers, from training them in the Academy to letting them buy and sell businesses through BSP, so clients stay even when advisers retire. I'd love to work in the division that runs that system."</div>
</section>
'''
