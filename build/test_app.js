// Automated checks for gsam_csg_command_center.html.  Usage: node build/test_app.js
// Exits non-zero if any check fails. Writes screenshots to build/out/shots/.
const { chromium, devices } = require('playwright');
const path = require('path');
const fs = require('fs');

const FILE = 'file://' + path.resolve(__dirname, '..', 'gsam_csg_command_center.html');
const SHOTS = path.resolve(__dirname, 'out', 'shots');
fs.mkdirSync(SHOTS, { recursive: true });
const results = [];
const ok = (name, cond, detail) => { results.push({ name, pass: !!cond, detail: detail || '' }); console.log((cond ? 'PASS ' : 'FAIL ') + name + (detail ? '  — ' + detail : '')); };

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: 1360, height: 900 } });
  const page = await ctx.newPage();
  const errors = [], requests = [];
  page.on('console', (m) => { if (m.type() === 'error') errors.push(m.text()); });
  page.on('pageerror', (e) => errors.push(String(e)));
  // Offline behaviour: record and block every request that is not the file itself.
  await page.route('**/*', (r) => { const u = r.request().url(); if (u.startsWith('file://')) return r.continue(); requests.push(u); return r.abort(); });
  await page.goto(FILE);
  await page.waitForSelector('#view-home:not([hidden])');
  ok('loads with no network requests (works offline)', requests.length === 0, requests.slice(0, 3).join(', '));
  ok('no external script, stylesheet, image or font references', await page.evaluate(() =>
    !document.querySelector('script[src],link[rel=stylesheet],img[src^="http"],iframe') && !/url\(\s*['"]?https?:/.test(document.querySelector('style').textContent)));

  // navigation: every view opens and exactly one is visible
  const views = ['home', 'read', 'teams', 'people', 'mandates', 'awareness', 'roles', 'lifecycle', 'calculator', 'why', 'practice', 'glossary', 'sources'];
  let navOk = true;
  for (const v of views) {
    await page.click(`nav.side a[href="#/${v}"]`);
    await page.waitForSelector(`#view-${v}:not([hidden])`);
    const vis = await page.$$eval('.view', (els) => els.filter((e) => !e.hidden).map((e) => e.id));
    if (vis.length !== 1 || vis[0] !== 'view-' + v) { navOk = false; console.log('   nav problem', v, vis); }
    const cur = await page.getAttribute(`nav.side a[href="#/${v}"]`, 'aria-current');
    if (cur !== 'page') navOk = false;
  }
  ok('navigation: all 13 views open, one at a time, with aria-current', navOk);

  // unavailable values never rendered as zero / undefined / NaN
  const bad = await page.evaluate(() => { const out = []; const t = document.body.innerText; const m = t.match(/\bundefined\b|\bNaN\b|\[object Object\]/g); if (m) out.push(...m.slice(0, 5));
    document.querySelectorAll('dd,td,li,p,span').forEach((e) => { if (/^(null|undefined)$/.test(e.textContent.trim()) || (e.tagName === 'DD' && e.textContent.trim() === 'None')) out.push('whole-cell ' + e.textContent.trim()); }); return out.slice(0, 5); });
  ok('no "undefined", "NaN", "null" or "[object Object]" in visible text', bad.length === 0, bad.join(','));
  const zeroes = await page.evaluate(() => Array.from(document.querySelectorAll('dl.kv dd, td')).filter((e) => /^(0|£0|\$0|0%)$/.test(e.textContent.trim()) && !e.closest('#calcOut,#pHistory,.case')).length);
  ok('no unavailable value shown as a bare zero in data cards and tables', zeroes === 0, String(zeroes));
  const missing = await page.$$eval('.cite-missing', (e) => e.length);
  ok('every citation resolves to a source in the register', missing === 0, missing + ' unresolved');
  const citeTargets = await page.evaluate(() => { const ids = new Set(Array.from(document.querySelectorAll('a.cite')).map((a) => a.getAttribute('href').slice(1))); let miss = 0; ids.forEach((i) => { if (!document.getElementById(i)) miss++; }); return { n: ids.size, miss }; });
  ok('every cited source has a row in the source register', citeTargets.miss === 0, `${citeTargets.n} distinct sources cited`);

  // reader + level toggle
  await page.goto(FILE + '#/read');
  const chCount = await page.$$eval('#chapters .chapter', (e) => e.length);
  const visCh = await page.$$eval('#chapters .chapter', (els) => els.filter((e) => !e.hidden).length);
  ok('reader shows one chapter at a time', chCount > 0 && visCh === 1, `${chCount} chapters`);
  await page.click('#nextCh');
  await page.waitForTimeout(100);
  ok('next-chapter button changes chapter', (await page.evaluate(() => location.hash)).includes('/read/ch'));
  const l2Before = await page.$$eval('#chapters .chapter:not([hidden]) .lvl-2', (els) => els.filter((e) => e.offsetParent !== null).length);
  await page.click('[data-level="l1"]');
  const l2After = await page.$$eval('#chapters .chapter:not([hidden]) .lvl-2', (els) => els.filter((e) => e.offsetParent !== null).length);
  const warnVisible = await page.$$eval('#chapters .chapter:not([hidden]) .box-warn', (els) => els.every((e) => e.offsetParent !== null || e.closest('.lvl-2')));
  ok('beginner view hides Level 2 blocks', l2Before > 0 ? l2After === 0 : true, `${l2Before} -> ${l2After}`);
  ok('beginner view keeps caveat boxes that sit outside Level 2', warnVisible);
  await page.click('[data-level="both"]');
  const gl = await page.$('#chapters .chapter:not([hidden]) button.g');
  if (gl) { await gl.click(); ok('glossary popover opens from a term in the text', await page.isVisible('#pop')); await page.keyboard.press('Escape'); ok('Escape closes the glossary popover', !(await page.isVisible('#pop'))); }
  else ok('glossary popover opens from a term in the text', false, 'no linked term found');

  // search
  await page.fill('#q', 'basis point');
  await page.waitForSelector('#view-search:not([hidden]) #searchResults li');
  const nRes = await page.$$eval('#searchResults li', (e) => e.length);
  ok('full-text search returns results', nRes > 0, nRes + ' results for "basis point"');
  await page.click('#searchResults li a');
  ok('search result link navigates away from results', !(await page.evaluate(() => location.hash)).startsWith('#/search'));
  await page.fill('#q', 'zzqxnotaword');
  await page.waitForFunction(() => /0 results/.test(document.getElementById('searchSummary').textContent));
  ok('search reports zero results honestly', true);

  // filters
  await page.goto(FILE + '#/people');
  const pTotal = await page.$$eval('#peopleList .person', (e) => e.length);
  const sel = await page.$('.filters[data-filter-for="peopleList"] select');
  if (sel && pTotal) {
    const opt = await sel.$$eval('option', (o) => o.map((x) => x.value).filter(Boolean)[0]);
    await sel.selectOption(opt);
    const shown = await page.$$eval('#peopleList .person', (els) => els.filter((e) => e.offsetParent !== null).length);
    ok('people filter narrows the list', shown > 0 && shown <= pTotal, `${shown} of ${pTotal} for "${opt}"`);
    await page.click('.filters[data-filter-for="peopleList"] button');
    ok('clear filters restores the list', (await page.$$eval('#peopleList .person', (els) => els.filter((e) => e.offsetParent !== null).length)) === pTotal);
  } else ok('people filter narrows the list', false, 'no people or no filter');
  await page.goto(FILE + '#/mandates');
  const mSel = await page.$('.filters[data-filter-for="mandateList"] select');
  ok('mandate filters are built from the data', !!mSel);

  // teams
  await page.goto(FILE + '#/teams');
  const tOpts = await page.$$eval('#teamSel option', (o) => o.map((x) => x.value).filter(Boolean));
  if (tOpts.length) {
    await page.selectOption('#teamSel', tOpts[0]);
    const vis = await page.$$eval('#teamPanel .team-card', (els) => els.filter((e) => !e.hidden).map((e) => e.id));
    ok('choosing a team shows only that team profile', vis.length === 1 && vis[0] === tOpts[0], `${tOpts.length} teams`);
    const parts = await page.$eval('#' + tOpts[0], (c) => ({ people: !!c.querySelector('.rel-block'), src: c.querySelectorAll('a.cite').length, fields: c.querySelectorAll('dl.kv dt').length }));
    ok('team profile carries clients, people, mandates, issues and sources', parts.people && parts.fields >= 6, JSON.stringify(parts));
    const link = await page.$('#pane-matrix a.teamlink');
    if (link) { await link.click(); ok('clicking a matrix cell opens its team', (await page.evaluate(() => location.hash)).startsWith('#/teams/T-')); }
    await page.click('#tab-org'); ok('organisational map tab shows', await page.isVisible('#pane-org'));
    await page.click('#tab-cube'); ok('optional 3D explorer draws without error', await page.isVisible('#cube'));
    await page.focus('#cube'); await page.keyboard.press('ArrowRight'); await page.keyboard.press('ArrowUp');
    await page.focus('#tab-cube'); await page.keyboard.press('ArrowLeft');
    ok('tabs respond to arrow keys', (await page.getAttribute('#tab-org', 'aria-selected')) === 'true');
  } else ok('choosing a team shows only that team profile', false, 'no teams');
  const emptyCells = await page.$$eval('table.matrix td', (tds) => tds.filter((t) => !t.textContent.trim()).length);
  ok('matrix has no blank cells (every cell states its evidence)', emptyCells === 0);

  // roles
  await page.goto(FILE + '#/roles');
  const cols = await page.$$eval('#roleCompare thead th', (e) => e.length);
  ok('role comparison renders two roles side by side', cols >= 3, cols + ' columns');

  // lifecycle
  await page.goto(FILE + '#/lifecycle');
  const nSt = await page.$$eval('#stepper button', (e) => e.length);
  await page.click('#nextStage');
  const visSt = await page.$$eval('#stages-inst .stage', (els) => els.filter((e) => !e.hidden).length);
  ok('lifecycle steps one stage at a time', nSt > 5 && visSt === 1, nSt + ' stages');
  await page.click('#allStages');
  ok('lifecycle "show all" reveals every stage', (await page.$$eval('#stages-inst .stage', (els) => els.filter((e) => !e.hidden).length)) === nSt);
  await page.click('[data-path="tpw"]');
  ok('wealth-intermediary lifecycle variant loads', (await page.$$eval('#stepper button', (e) => e.length)) > 3);

  // calculator arithmetic
  await page.goto(FILE + '#/calculator');
  const calc = await page.evaluate(() => {
    const out = []; for (const c of window.__cases) { const r = window.__feeModel(c.params); out.push({ id: c.id, js: r.total_fees, py: c.expected_total }); } return out; });
  const worst = Math.max(...calc.map((c) => Math.abs(c.js - c.py) / Math.max(1, Math.abs(c.py))));
  ok('calculator: JavaScript model equals the Python model on every worked case', worst < 1e-9, `${calc.length} cases, worst relative difference ${worst.toExponential(2)}`);
  const base = calc.find((c) => c.id === 'CASE-500-full');
  ok('calculator: £500m at 20bp for a year = £1,000,000', base && Math.abs(base.js - 1e6) < 1e-6, base ? String(base.js) : 'case missing');
  const tr = calc.find((c) => c.id === 'CASE-500-tranche');
  ok('calculator: half funded for six months then full = £750,000', tr && Math.abs(tr.js - 750000) < 1e-6, tr ? String(tr.js) : '');
  const tiered = await page.evaluate(() => window.__feeModel({ size: 600e6, fee_mode: 'tiered', tiers: [{ upto: 250e6, bps: 25 }, { upto: 500e6, bps: 20 }, { upto: null, bps: 15 }], months: 12 }).total_fees);
  ok('calculator: tiered fee on £600m = 250×25bp + 250×20bp + 100×15bp = £1,275,000', Math.abs(tiered - 1275000) < 1e-6, String(tiered));
  const committed = await page.evaluate(() => window.__feeModel({ size: 100e6, fee_bps: 100, fee_base: 'committed', funded_pct_initial: 10, annual_return_pct: -50, months: 12 }).total_fees);
  ok('calculator: committed-capital fee ignores drawdown and markets (£100m × 1% = £1m)', Math.abs(committed - 1e6) < 1e-6, String(committed));
  const wd = await page.evaluate(() => window.__feeModel({ size: 100e6, fee_bps: 10, flow_amount: -500e6, flow_month: 2, months: 3 }).rows[1].start_balance);
  ok('calculator: a withdrawal cannot take the balance below zero', wd === 0);
  await page.selectOption('#caseSel', 'CASE-1bn-partial');
  const shownTotal = await page.textContent('#calcTotal');
  ok('calculator UI: loading a case updates the displayed total', /£/.test(shownTotal), shownTotal);
  await page.fill('#c_size', '500000000'); await page.fill('#c_bps', '20'); await page.fill('#c_months', '12'); await page.fill('#c_flow', '0'); await page.fill('#c_flowmonth', '');
  ok('calculator UI: typed inputs give £1m', (await page.textContent('#calcTotal')).trim() === '£1m', await page.textContent('#calcTotal'));

  // why-trees
  await page.goto(FILE + '#/why');
  const closed = await page.$$eval('#whyList details.why-node', (d) => d.filter((x) => x.open).length);
  await page.click('#whyOpen');
  const opened = await page.$$eval('#whyList details.why-node', (d) => d.filter((x) => x.open).length);
  ok('why-trees start collapsed and expand', closed === 0 && opened > 10, `${opened} nodes`);
  await page.click('#whyClose');
  await page.focus('#whyList details.why-node > summary'); await page.keyboard.press('Enter');
  ok('why-tree nodes open from the keyboard', await page.$eval('#whyList details.why-node', (d) => d.open));

  // practice mode: no microphone, timer, scoring, optional storage
  await page.goto(FILE + '#/practice');
  const nQ = await page.$$eval('#qList .iq', (e) => e.length);
  if (nQ) {
    await page.click('#pNext'); await page.click('#pStart'); await page.waitForTimeout(1300); await page.click('#pStop');
    ok('practice timer runs', (await page.textContent('#pTimer')) !== '0:00');
    await page.click('#pReveal'); ok('practice reveal shows the reasoning', await page.isVisible('#pAnswer'));
    await page.selectOption('#pScores select', '2'); await page.click('#pSave');
    ok('practice attempt is recorded in the history table', (await page.$$eval('#pHistory tbody tr', (e) => e.length)) === 1);
    ok('nothing stored locally unless the user opts in', (await page.evaluate(() => localStorage.getItem('gsamcsg.v1'))) === null);
  } else ok('practice question bank present', false, 'no questions');
  ok('page never asks for the microphone or records audio', await page.evaluate(() => !/getUserMedia|MediaRecorder|webkitSpeechRecognition/.test(document.documentElement.innerHTML)));
  await page.goto(FILE + '#/home');
  await page.check('#saveToggle');
  const step = await page.$('.route-step'); if (step) await step.check();
  ok('opt-in progress saving writes to this browser only', (await page.evaluate(() => { const v = localStorage.getItem('gsamcsg.v1'); return v && JSON.parse(v).save; })) === true);
  await page.click('#resetBtn');
  ok('reset clears saved progress', await page.evaluate(() => { const v = JSON.parse(localStorage.getItem('gsamcsg.v1') || '{}'); return Object.keys(v.steps || {}).length === 0 && (v.history || []).length === 0; }));
  await page.uncheck('#saveToggle');
  ok('turning saving off removes the stored data', (await page.evaluate(() => localStorage.getItem('gsamcsg.v1'))) === null);

  // glossary + sources
  await page.goto(FILE + '#/glossary');
  await page.fill('#gq', 'ocio');
  const gShown = await page.$$eval('#glossList .gloss', (els) => els.filter((e) => e.offsetParent !== null).length);
  ok('glossary filter works', gShown > 0 && gShown < (await page.$$eval('#glossList .gloss', (e) => e.length)), gShown + ' terms match "ocio"');
  await page.goto(FILE + '#/read');
  const cite = await page.$('#chapters .chapter a.cite');
  if (cite) { const href = await cite.getAttribute('href'); await page.evaluate((h) => { location.hash = h; }, href); await page.waitForSelector('#view-sources:not([hidden])'); ok('a citation opens its row in the source register', true, href); }
  const extLinks = await page.$$eval('table.sources a[href^="http"]', (a) => ({ n: a.length, safe: a.every((x) => x.rel.includes('noopener')) }));
  ok('source links are present and open safely', extLinks.n > 50 && extLinks.safe, extLinks.n + ' links');

  // keyboard + semantics
  await page.goto(FILE + '#/home'); await page.reload();
  await page.keyboard.press('Tab');
  ok('first Tab stop is the skip link', await page.evaluate(() => document.activeElement.classList.contains('skip')));
  await page.keyboard.press('Escape'); await page.evaluate(() => document.activeElement.blur()); await page.keyboard.press('/');
  ok('"/" focuses the search box', await page.evaluate(() => document.activeElement.id === 'q'));
  const sem = await page.evaluate(() => ({ main: !!document.querySelector('main'), nav: !!document.querySelector('nav[aria-label]'), header: !!document.querySelector('header'), lang: document.documentElement.lang,
    h1PerView: Array.from(document.querySelectorAll('.view')).every((v) => v.querySelector('h1')), unlabeled: Array.from(document.querySelectorAll('input,select')).filter((i) => !i.closest('label') && !i.getAttribute('aria-label') && !document.querySelector(`label[for="${i.id}"]`)).length,
    badgesHaveText: Array.from(document.querySelectorAll('.badge')).every((b) => b.textContent.trim().length > 3) }));
  ok('semantic landmarks, language, one h1 per view, labelled controls', sem.main && sem.nav && sem.header && sem.lang && sem.h1PerView && sem.unlabeled === 0, JSON.stringify(sem));
  ok('evidence badges carry a written label and symbol, not colour alone', sem.badgesHaveText);
  ok('withheld client name appears nowhere in the application', await page.evaluate(() => !/jaguar|land rover|\bJLR\b/i.test(document.documentElement.innerHTML)));
  ok('no JavaScript errors during the whole run', errors.length === 0, errors.slice(0, 3).join(' | '));
  await page.screenshot({ path: path.join(SHOTS, 'desktop-home.png') });
  await page.goto(FILE + '#/teams'); await page.screenshot({ path: path.join(SHOTS, 'desktop-teams.png') });
  await page.goto(FILE + '#/read/ch07'); await page.screenshot({ path: path.join(SHOTS, 'desktop-read.png') });
  await page.goto(FILE + '#/calculator'); await page.screenshot({ path: path.join(SHOTS, 'desktop-calculator.png') });

  // mobile layout
  const m = await browser.newContext({ ...devices['iPhone 13'] });
  const mp = await m.newPage();
  for (const v of ['home', 'read', 'teams', 'people', 'calculator', 'practice', 'sources']) {
    await mp.goto(FILE + '#/' + v); await mp.waitForTimeout(120);
    const over = await mp.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    ok(`mobile: no horizontal page scroll on ${v}`, over <= 1, over + 'px overflow');
  }
  await mp.goto(FILE + '#/home'); await mp.click('#menuBtn');
  ok('mobile: menu button opens navigation', await mp.isVisible('nav.side'));
  await mp.click('nav.side a[href="#/teams"]');
  await mp.waitForSelector('#view-teams:not([hidden])');
  ok('mobile: choosing a section closes the menu', !(await mp.isVisible('nav.side')));
  await mp.screenshot({ path: path.join(SHOTS, 'mobile-teams.png') });

  // reduced motion + dark theme
  const rm = await browser.newContext({ reducedMotion: 'reduce', colorScheme: 'dark', viewport: { width: 1200, height: 800 } });
  const rp = await rm.newPage(); await rp.goto(FILE + '#/teams');
  ok('reduced-motion: smooth scrolling is off', (await rp.evaluate(() => getComputedStyle(document.documentElement).scrollBehavior)) === 'auto');
  await rp.screenshot({ path: path.join(SHOTS, 'dark-teams.png') });

  await browser.close();
  const failed = results.filter((r) => !r.pass);
  fs.writeFileSync(path.resolve(__dirname, 'out', 'test_report.json'), JSON.stringify({ date: '2026-11-14', total: results.length, failed: failed.length, results }, null, 1));
  console.log(`\n${results.length - failed.length} of ${results.length} checks passed`);
  process.exit(failed.length ? 1 : 0);
})();
