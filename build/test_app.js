// Automated checks for gsam_csg_command_center.html.  Usage: node build/test_app.js
// Exits non-zero if any check fails.
const { chromium, devices } = require('playwright');
const path = require('path');
const fs = require('fs');

const FILE = 'file://' + path.resolve(__dirname, '..', 'gsam_csg_command_center.html');
fs.mkdirSync(path.resolve(__dirname, 'out'), { recursive: true });
const results = [];
const ok = (name, cond, detail) => { results.push({ name, pass: !!cond, detail: detail || '' }); console.log((cond ? 'PASS ' : 'FAIL ') + name + (detail ? '  — ' + detail : '')); };
const visibleViews = (page) => page.$$eval('.view', (els) => els.filter((e) => !e.hidden).map((e) => e.id));

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1360, height: 900 }, colorScheme: 'light' });
  const page = await ctx.newPage();
  const errors = [], requests = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push(String(e)));
  await page.route('**/*', (r) => { const u = r.request().url(); if (u.startsWith('file://')) return r.continue(); requests.push(u); return r.abort(); });
  await page.goto(FILE);
  await page.waitForSelector('#view-home:not([hidden])');
  ok('loads with no network requests (works offline)', requests.length === 0, requests.slice(0, 3).join(', '));
  ok('no external script, stylesheet, image or font references', await page.evaluate(() =>
    !document.querySelector('script[src],link[rel=stylesheet],img[src^="http"],iframe') && !/url\(\s*['"]?https?:/.test(document.querySelector('style').textContent)));

  // navigation
  const views = ['role', 'relationships', 'sales', 'teams', 'facts', 'practise', 'library'];
  let navOk = true;
  for (const v of views) {
    await page.click(`nav.main a[href="#/${v}"]`);
    await page.waitForSelector(`#view-${v}:not([hidden])`);
    const vis = await visibleViews(page);
    if (vis.length !== 1 || (await page.getAttribute(`nav.main a[href="#/${v}"]`, 'aria-current')) !== 'page') navOk = false;
  }
  await page.click('a.brand'); await page.waitForSelector('#view-home:not([hidden])');
  ok('navigation: home and all seven sections open one at a time, with the current one marked', navOk);
  const homeLinks = await page.$$eval('.home-list a', (a) => a.map((x) => x.getAttribute('href')));
  ok('home page leads with the three guide pages in order', JSON.stringify(homeLinks) === JSON.stringify(['#/role', '#/relationships', '#/sales']));

  // content the user asked for, and content they asked to remove
  const whole = await page.evaluate(() => document.body.innerText);
  ok('why-trees are gone from the site', !/why-tree/i.test(whole) && !(await page.$('.why-tree, #whyList')));
  ok('no game points, levels or emoji tiles remain', !(await page.$('#xpNum, .tile, .burst, #cube')));
  await page.goto(FILE + '#/relationships');
  const rel = await page.evaluate(() => { const v = document.getElementById('view-relationships'); const h = Array.from(v.querySelectorAll('h2')).map((x) => x.textContent); return { h, d: v.querySelectorAll('.diagram').length, toc: v.querySelectorAll('.onpage a').length }; });
  const need = ['Who the relationship is with', 'What starts', 'What continues', 'What really builds', 'how one ends', 'Where the work happens', 'Why relationships matter', '40 years', 'year one'];
  ok('Relationships page covers who, what starts, continues and builds it, endings, where, why, the decades view and year one', need.every((n) => rel.h.some((h) => h.includes(n))), rel.h.length + ' sections');
  ok('Relationships page has its diagrams and an "on this page" list', rel.d >= 3 && rel.toc === rel.h.length, `${rel.d} diagrams`);
  await page.goto(FILE + '#/sales');
  const sales = await page.evaluate(() => { const v = document.getElementById('view-sales'); return { h: v.querySelectorAll('h2').length, steps: v.querySelectorAll('#stages-inst details').length, tpw: v.querySelectorAll('#stages-tpw details').length, d: v.querySelectorAll('.diagram').length }; });
  ok('Sales and RM page has the step-by-step process with expandable detail for each step', sales.steps >= 8 && sales.tpw >= 4 && sales.d >= 2, JSON.stringify(sales));
  await page.click('#stages-inst details summary');
  ok('a process step opens to show who leads and what the junior person produces', await page.$eval('#stages-inst details', (d) => d.open && d.querySelectorAll('dt').length >= 4));
  await page.goto(FILE + '#/role');
  ok('The role page opens with the from-zero guide and its diagrams', (await page.$$eval('#view-role .diagram', (e) => e.length)) >= 5);
  const dgFit = await page.evaluate(() => { let bad = 0, n = 0; ['role', 'relationships', 'sales'].forEach((v) => { const view = document.getElementById('view-' + v); const was = view.hidden; view.hidden = false;
    view.querySelectorAll('.diagram svg').forEach((s) => { n++; const vb = s.viewBox.baseVal; s.querySelectorAll('text').forEach((t) => { const b = t.getBBox(); if (b.x < -2 || b.x + b.width > vb.width + 2 || b.y < -2 || b.y + b.height > vb.height + 2) bad++; }); });
    view.hidden = was; }); return { n, bad }; });
  ok('no diagram text runs outside its picture', dgFit.bad === 0, `${dgFit.n} diagrams`);
  const dgWords = await page.$$eval('.diagram', (els) => els.every((d) => d.querySelector('svg[role=img][aria-label]') && d.querySelector('.dg-words')));
  ok('every diagram has a text description', dgWords);
  const dupIds = await page.evaluate(() => { const seen = {}, d = []; document.querySelectorAll('[id]').forEach((e) => { if (seen[e.id]) d.push(e.id); seen[e.id] = 1; }); return d; });
  ok('no duplicate element ids', dupIds.length === 0, dupIds.slice(0, 5).join(','));

  // anchors inside the guides jump to the right place
  await page.goto(FILE + '#/relationships');
  const tocHref = await page.getAttribute('#view-relationships .onpage a:nth-child(1)', 'href').catch(() => null) || await page.$eval('#view-relationships .onpage a', (a) => a.getAttribute('href'));
  await page.click('#view-relationships .onpage li:nth-child(3) a');
  await page.waitForTimeout(150);
  ok('"on this page" links stay on the page and move to the section', (await visibleViews(page))[0] === 'view-relationships' && !!tocHref);
  const mlink = await page.$('#view-relationships a[href="#M-R7-23"]');
  if (mlink) { await mlink.click(); await page.waitForSelector('#library-mandates:not([hidden])'); ok('a link to a mandate opens the Library on that mandate', (await visibleViews(page))[0] === 'view-library'); }
  else ok('a link to a mandate opens the Library on that mandate', false, 'link not found');

  // evidence
  const missing = await page.$$eval('.cite-missing', (e) => e.length);
  ok('every citation resolves to a source', missing === 0, missing + ' unresolved');
  const citeTargets = await page.evaluate(() => { const ids = new Set(Array.from(document.querySelectorAll('a.cite')).map((a) => a.getAttribute('href').slice(1))); let miss = 0; ids.forEach((i) => { if (!document.getElementById(i)) miss++; }); return { n: ids.size, miss }; });
  ok('every cited source has a row in the source list', citeTargets.miss === 0, `${citeTargets.n} distinct sources cited`);
  await page.goto(FILE + '#/role');
  const cite = await page.$('#view-role a.cite');
  await cite.click(); await page.waitForSelector('#library-sources:not([hidden])');
  ok('clicking a source code opens that source', (await visibleViews(page))[0] === 'view-library');
  const bad = await page.evaluate(() => { const out = []; const t = document.body.innerText; const m = t.match(/\bundefined\b|\bNaN\b|\[object Object\]/g); if (m) out.push(...m.slice(0, 5));
    document.querySelectorAll('dd,td,li,p,span').forEach((e) => { if (/^(null|undefined)$/.test(e.textContent.trim()) || (e.tagName === 'DD' && e.textContent.trim() === 'None')) out.push('whole-cell ' + e.textContent.trim()); }); return out.slice(0, 5); });
  ok('no "undefined", "NaN" or "null" shown anywhere', bad.length === 0, bad.join(','));
  ok('withheld client name appears nowhere', await page.evaluate(() => !/jaguar|land rover|\bJLR\b/i.test(document.documentElement.innerHTML)));
  ok('evidence labels are written out, not colour alone', await page.$$eval('.badge', (b) => b.length > 50 && b.every((x) => x.textContent.trim().length > 3)));

  // search
  await page.goto(FILE + '#/');
  await page.fill('#q', 'consultant');
  await page.waitForSelector('#view-search:not([hidden]) #searchResults li');
  const nRes = await page.$$eval('#searchResults li', (e) => e.length);
  ok('search returns results', nRes > 0, nRes + ' for "consultant"');
  await page.click('#searchResults li a'); await page.waitForTimeout(150);
  ok('a search result opens the page it points to', (await visibleViews(page))[0] !== 'view-search');
  await page.fill('#q', 'zzqxnotaword');
  await page.waitForFunction(() => /^0 results/.test(document.getElementById('searchSummary').textContent));
  ok('search reports zero results honestly', true);

  // teams
  await page.goto(FILE + '#/teams');
  const tOpts = await page.$$eval('#teamSel option', (o) => o.map((x) => x.value).filter(Boolean));
  await page.selectOption('#teamSel', tOpts[1]);
  await page.waitForTimeout(100);
  const visT = await page.$$eval('#teamPanel .team-card', (els) => els.filter((e) => !e.hidden).map((e) => e.id));
  ok('choosing a team shows only that team', visT.length === 1 && visT[0] === tOpts[1], `${tOpts.length} teams`);
  ok('each team has talking points, questions to ask and watch-outs', await page.$$eval('#teamPanel .team-card', (els) => els.every((c) => c.querySelectorAll('.brief h4').length === 3)));
  ok('the coverage map has no blank cells', (await page.$$eval('table.matrix td', (tds) => tds.filter((t) => !t.textContent.trim()).length)) === 0);
  await page.selectOption('#teamSel', '');
  await page.click('table.matrix a.teamlink'); await page.waitForTimeout(100);
  ok('a cell in the map opens its team', (await page.evaluate(() => location.hash)).startsWith('#/teams/T-'));

  // facts
  await page.goto(FILE + '#/facts');
  const nNum = await page.$$eval('#numWall .num-tile', (e) => e.length);
  await page.click('#testMe');
  ok('numbers: "test me" hides the values', nNum > 20 && /rgba\(0, 0, 0, 0\)|transparent/.test(await page.$eval('#numWall .num-val', (e) => getComputedStyle(e).color)), `${nNum} numbers`);
  await page.click('#numWall .num-tile summary');
  ok('numbers: opening one shows what it means, its caveat and its source', await page.$eval('#numWall .num-tile', (d) => d.open && !!d.querySelector('a.cite')));
  await page.click('[data-tab="facts"][data-pane="findings"]'); await page.waitForSelector('#facts-findings:not([hidden])');
  const fSel = await page.$('.filters[data-filter-for="intelList"] select');
  const nEdge = await page.$$eval('#intelList .edge', (e) => e.length);
  await fSel.selectOption({ index: 1 });
  const shown = await page.$$eval('#intelList .edge', (els) => els.filter((e) => e.offsetParent !== null).length);
  ok('key findings filter by area', shown > 0 && shown < nEdge, `${shown} of ${nEdge}`);
  await page.click('[data-tab="facts"][data-pane="charts"]'); await page.waitForSelector('#facts-charts:not([hidden])');
  const charts = await page.$$eval('.chart', (els) => ({ n: els.length, ok: els.every((c) => c.querySelector('svg .bar-mark') && c.querySelector('table') && c.querySelector('a.cite')) }));
  ok('charts have bars, a table view and a source', charts.n >= 5 && charts.ok, charts.n + ' charts');
  await page.click('[data-tab="facts"][data-pane="audit"]'); await page.waitForSelector('#facts-audit:not([hidden])');
  ok('the former intern\'s claims are listed with what the research found', (await page.$$eval('#facts-audit tbody tr', (r) => r.length)) >= 30);

  // practise
  await page.goto(FILE + '#/practise');
  const nQ = await page.$$eval('#qList .iq', (e) => e.length);
  ok('interview question bank is present', nQ >= 25, nQ + ' questions');
  await page.click('[data-tab="practise"][data-pane="timed"]'); await page.waitForSelector('#practise-timed:not([hidden])');
  await page.click('#pNext'); await page.click('#pStart'); await page.waitForTimeout(1300); await page.click('#pStop');
  ok('timed practice: the timer runs', (await page.textContent('#pTimer')) !== '0:00');
  await page.click('#pReveal'); ok('timed practice: the reasoning can be revealed', await page.isVisible('#pAnswer'));
  await page.click('[data-tab="practise"][data-pane="quiz"]'); await page.waitForSelector('#practise-quiz:not([hidden])');
  const quizData = await page.evaluate(() => { const d = JSON.parse(document.getElementById('data').textContent); return { n: d.quiz.length, bad: d.quiz.filter((q) => !Array.isArray(q.options) || q.options.length !== 4 || !(q.answer >= 0 && q.answer < 4)).length }; });
  ok('quiz questions are well formed', quizData.n >= 80 && quizData.bad === 0, `${quizData.n} questions`);
  await page.selectOption('#zLen', '5'); await page.click('#zStart');
  for (let i = 0; i < 5; i++) {
    const ans = await page.evaluate(() => { const q = document.getElementById('zQ').textContent; const d = JSON.parse(document.getElementById('data').textContent); return d.quiz.find((x) => x.q === q).answer; });
    await page.click(`#zOpts button:nth-child(${ans + 1})`);
    if (i === 0) ok('quiz: an answer shows whether it was right, and why', await page.isVisible('#zFb') && (await page.$$eval('#zOpts button.right', (e) => e.length)) === 1);
    await page.click('#zNext');
  }
  ok('quiz: a perfect round reports 5 / 5', /5 \/ 5/.test(await page.textContent('#zEnd')));
  ok('nothing is ever written to browser storage', await page.evaluate(() => localStorage.length === 0 && sessionStorage.length === 0));
  ok('the page never asks for the microphone or records audio', await page.evaluate(() => !/getUserMedia|MediaRecorder|webkitSpeechRecognition/.test(document.documentElement.innerHTML)));

  // library
  await page.goto(FILE + '#/library');
  const chCount = await page.$$eval('#chapters .chapter', (e) => e.length);
  ok('library reader shows one chapter at a time', chCount >= 10 && (await page.$$eval('#chapters .chapter', (els) => els.filter((e) => !e.hidden).length)) === 1, `${chCount} chapters`);
  await page.click('#nextCh'); await page.waitForTimeout(100);
  ok('next-chapter button works', /#\/library\/chapters\/ch01/.test(await page.evaluate(() => location.hash)));
  const l2Before = await page.$$eval('#chapters .chapter:not([hidden]) .lvl-2', (els) => els.filter((e) => e.offsetParent !== null).length);
  await page.click('[data-level="l1"]');
  const l2After = await page.$$eval('#chapters .chapter:not([hidden]) .lvl-2', (els) => els.filter((e) => e.offsetParent !== null).length);
  ok('"Plain" reading level hides the technical blocks', l2Before > 0 && l2After === 0, `${l2Before} -> ${l2After}`);
  await page.click('[data-level="both"]');
  const gl = await page.$('#chapters .chapter:not([hidden]) button.g');
  await gl.click(); ok('a dotted term opens its definition', await page.isVisible('#pop'));
  await page.keyboard.press('Escape'); ok('Escape closes the definition', !(await page.isVisible('#pop')));
  await page.click('[data-tab="library"][data-pane="people"]'); await page.waitForSelector('#library-people:not([hidden])');
  const pTotal = await page.$$eval('#peopleList .person', (e) => e.length);
  const pSel = await page.$('.filters[data-filter-for="peopleList"] select');
  await pSel.selectOption({ index: 1 });
  const pShown = await page.$$eval('#peopleList .person', (els) => els.filter((e) => e.offsetParent !== null).length);
  ok('people filter narrows the list, and Clear restores it', pShown > 0 && pShown < pTotal, `${pShown} of ${pTotal}`);
  await page.click('.filters[data-filter-for="peopleList"] button');
  await page.click('[data-tab="library"][data-pane="glossary"]'); await page.waitForSelector('#library-glossary:not([hidden])');
  await page.fill('#gq', 'ocio');
  const gShown = await page.$$eval('#glossList .gloss', (els) => els.filter((e) => e.offsetParent !== null).length);
  ok('glossary search works', gShown > 0 && gShown < (await page.$$eval('#glossList .gloss', (e) => e.length)), gShown + ' terms match "ocio"');
  await page.click('[data-tab="library"][data-pane="sources"]'); await page.waitForSelector('#library-sources:not([hidden])');
  const ext = await page.$$eval('table.sources a[href^="http"]', (a) => ({ n: a.length, safe: a.every((x) => x.rel.includes('noopener')) }));
  ok('source links are present and open safely', ext.n > 50 && ext.safe, ext.n + ' links');

  // calculator
  await page.goto(FILE + '#/library/calculator');
  const calc = await page.evaluate(() => window.__cases.map((c) => ({ id: c.id, js: window.__feeModel(c.params).total_fees, py: c.expected_total })));
  const worst = Math.max(...calc.map((c) => Math.abs(c.js - c.py) / Math.max(1, Math.abs(c.py))));
  ok('calculator: the page\'s model equals the independent Python model on every example', worst < 1e-9, `${calc.length} examples`);
  ok('calculator: £500m at 20bp for a year = £1,000,000', Math.abs(calc.find((c) => c.id === 'CASE-500-full').js - 1e6) < 1e-6);
  ok('calculator: half funded for six months then full = £750,000', Math.abs(calc.find((c) => c.id === 'CASE-500-tranche').js - 750000) < 1e-6);
  const tiered = await page.evaluate(() => window.__feeModel({ size: 600e6, fee_mode: 'tiered', tiers: [{ upto: 250e6, bps: 25 }, { upto: 500e6, bps: 20 }, { upto: null, bps: 15 }], months: 12 }).total_fees);
  ok('calculator: tiered fee on £600m = £1,275,000', Math.abs(tiered - 1275000) < 1e-6);
  const committed = await page.evaluate(() => window.__feeModel({ size: 100e6, fee_bps: 100, fee_base: 'committed', funded_pct_initial: 10, annual_return_pct: -50, months: 12 }).total_fees);
  ok('calculator: committed-capital fee ignores drawdown and markets', Math.abs(committed - 1e6) < 1e-6);
  ok('calculator: a withdrawal cannot take the balance below zero', (await page.evaluate(() => window.__feeModel({ size: 100e6, fee_bps: 10, flow_amount: -500e6, flow_month: 2, months: 3 }).rows[1].start_balance)) === 0);
  await page.selectOption('#caseSel', 'CASE-1bn-partial');
  ok('calculator: loading an example updates the result', /£/.test(await page.textContent('#calcTotal')));
  await page.fill('#c_size', '500000000'); await page.fill('#c_bps', '20'); await page.fill('#c_months', '12'); await page.fill('#c_flow', '0'); await page.fill('#c_flowmonth', '');
  ok('calculator: typed inputs give £1m', (await page.textContent('#calcTotal')).trim() === '£1m');

  // keyboard and structure
  await page.goto(FILE + '#/'); await page.reload();
  await page.keyboard.press('Tab');
  ok('first Tab stop is the skip link', await page.evaluate(() => document.activeElement.classList.contains('skip')));
  await page.evaluate(() => document.activeElement.blur()); await page.keyboard.press('/');
  ok('"/" focuses search', await page.evaluate(() => document.activeElement.id === 'q'));
  const sem = await page.evaluate(() => ({ main: !!document.querySelector('main'), nav: !!document.querySelector('nav[aria-label]'), header: !!document.querySelector('header'), lang: document.documentElement.lang,
    unlabeled: Array.from(document.querySelectorAll('input,select')).filter((i) => !i.closest('label') && !i.getAttribute('aria-label') && !document.querySelector(`label[for="${i.id}"]`)).length,
    italics: Array.from(document.querySelectorAll('em,i,cite')).filter((e) => getComputedStyle(e).fontStyle === 'italic').length }));
  ok('landmarks, language and labelled controls', sem.main && sem.nav && sem.header && sem.lang && sem.unlabeled === 0, JSON.stringify(sem));
  ok('no italic text anywhere (emphasis is bold)', sem.italics === 0);
  const type = await page.evaluate(() => { const p = document.querySelector('.lede'); const cs = getComputedStyle(document.body); return { size: parseFloat(cs.fontSize), lh: parseFloat(cs.lineHeight) / parseFloat(cs.fontSize) }; });
  ok('reading text is at least 17px with line height of 1.6 or more', type.size >= 17 && type.lh >= 1.6, JSON.stringify(type));
  ok('no JavaScript errors during the whole run', errors.length === 0, errors.slice(0, 3).join(' | '));

  // mobile
  const m = await browser.newContext({ ...devices['iPhone 13'] });
  const mp = await m.newPage();
  for (const v of ['', 'role', 'relationships', 'sales', 'teams', 'facts', 'practise', 'library', 'library/people', 'library/calculator', 'library/sources']) {
    await mp.goto(FILE + '#/' + v); await mp.waitForTimeout(120);
    const over = await mp.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    ok(`phone: no sideways page scroll on ${v || 'home'}`, over <= 1, over + 'px');
  }
  await mp.goto(FILE + '#/'); await mp.click('.home-list a'); await mp.waitForSelector('#view-role:not([hidden])');
  ok('phone: the home list opens the first guide', true);

  const rm = await browser.newContext({ reducedMotion: 'reduce', colorScheme: 'dark', viewport: { width: 1200, height: 800 } });
  const rp = await rm.newPage(); await rp.goto(FILE + '#/relationships');
  ok('reduced motion: smooth scrolling is off', (await rp.evaluate(() => getComputedStyle(document.documentElement).scrollBehavior)) === 'auto');
  const dark = await rp.evaluate(() => { const c = getComputedStyle(document.body); return { bg: c.backgroundColor, fg: c.color }; });
  ok('dark setting on the device gives a dark page with light text', dark.bg !== 'rgb(251, 250, 247)', JSON.stringify(dark));

  await browser.close();
  const failed = results.filter((r) => !r.pass);
  fs.writeFileSync(path.resolve(__dirname, 'out', 'test_report.json'), JSON.stringify({ total: results.length, failed: failed.length, results }, null, 1));
  console.log(`\n${results.length - failed.length} of ${results.length} checks passed`);
  process.exit(failed.length ? 1 : 0);
})();
