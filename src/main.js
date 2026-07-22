// -----------------------------------------------------------------------------
// main.js — the app controller. A tiny screen state-machine that wires the
// generators, verifier-backed session, charts, calculator, scoring and coaching
// into the authentic scales-numerical flow. No framework, no backend.
// -----------------------------------------------------------------------------

import './ui/styles.css';
import guideMd from '../GUIDE.md?raw';

import { generateSession } from './generators/session.js';
import { renderChart } from './ui/charts.js';
import { createCalculator } from './ui/calculator.js';
import { scoreSession, requiredTabs } from './coaching/scoring.js';
import { recordSession, load, reset, typeAccuracy } from './coaching/store.js';
import { adaptiveWeights, weakestTypes } from './coaching/adaptive.js';
import { REASONS } from './coaching/diagnosis.js';

// ---- modes ------------------------------------------------------------------
const MODES = {
  full: { label: 'Full mock', count: 37, time: 720, timed: true, allowBack: true,
    desc: '37 tasks · 12:00 · the real long form (~20s/item)' },
  short: { label: 'Short mock', count: 18, time: 360, timed: true, allowBack: true,
    desc: '18 tasks · 6:00 · the real short form (~20s/item)' },
  remembered: { label: 'As remembered', count: 18, time: 720, timed: true, allowBack: true, nonstandard: true,
    desc: '18 tasks · 12:00 · gentler than the real test (your recollection)' },
  untimed: { label: 'Untimed drill', count: 15, time: 0, timed: false, allowBack: true,
    desc: 'No clock · learn the reasoning at your own pace' },
  adaptive: { label: 'Adaptive drill', count: 15, time: 0, timed: false, allowBack: true, adaptive: true,
    desc: 'No clock · serves more of your weakest categories' },
};
const TIERS = ['medium', 'intermediate', 'hard'];
const ANSWERS = [
  { v: 'TRUE', label: 'True', cls: 't' },
  { v: 'FALSE', label: 'False', cls: 'f' },
  { v: 'CANNOT_SAY', label: 'Cannot Say', cls: 'c' },
];

// ---- app state --------------------------------------------------------------
const app = document.getElementById('app');
let state = {
  screen: 'home',
  mode: 'full', tier: 'intermediate',
  options: { wrongTabPenalty: true, allowBack: true },
  session: null, answers: [], current: 0, activeTab: 0,
  timer: null, deadline: 0, enterTs: 0, expired: false,
  lastScore: null,
};
let calc = null;

// ---- helpers ----------------------------------------------------------------
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const fmtTime = (s) => `${Math.floor(s / 60)}:${String(Math.max(0, s % 60)).padStart(2, '0')}`;
const pct = (x) => `${Math.round(x * 100)}%`;

function topbar(right = '') {
  return `<div class="topbar">
    <div class="brand">Scales · <small>numerical reasoning trainer</small></div>
    <div class="meta">${right}</div>
  </div>`;
}

function render() {
  if (state.screen !== 'test' && calc) hideCalc();
  app.innerHTML = ({
    home: renderHome, test: renderTest, results: renderResults,
    progress: renderProgress, guide: renderGuide,
  }[state.screen])();
  wire();
}

// =============================================================================
// HOME
// =============================================================================
function renderHome() {
  const cards = Object.entries(MODES).map(([key, m]) => `
    <div class="mode-card">
      <h3>${esc(m.label)}${m.nonstandard ? ' <span class="pill">non-standard</span>' : ''}</h3>
      <div class="spec">${esc(m.desc)}</div>
      <div style="margin-top:10px"><button class="btn" data-start="${key}">Start</button></div>
    </div>`).join('');
  return `${topbar('')}
  <div class="panel">
    <h2 style="margin-top:0">Practise the Aon “scales numerical” assessment</h2>
    <p class="muted">Tabbed data displays, True / False / Cannot Say, a countdown, and negative marking —
    faithfully replicated for legitimate preparation. Questions are generated fresh every time and each
    one is independently verified, so the answer key is always provably correct.</p>
    <div class="controls" style="margin:12px 0">
      <label class="chk">Difficulty
        <select data-tier>${TIERS.map((t) => `<option value="${t}"${t === state.tier ? ' selected' : ''}>${t}</option>`).join('')}</select>
      </label>
      <label class="chk"><input type="checkbox" data-opt="wrongTabPenalty"${state.options.wrongTabPenalty ? ' checked' : ''}/> Wrong-tab penalty</label>
      <label class="chk"><input type="checkbox" data-opt="allowBack"${state.options.allowBack ? ' checked' : ''}/> Allow going back</label>
      <span class="btn ghost" data-nav="progress">View progress</span>
      <span class="btn ghost" data-nav="guide">Read the guide</span>
    </div>
    <div class="mode-grid">${cards}</div>
    <div class="banner">Preparation only. This is a practice simulator — not affiliated with Aon — and offers
    no live-test answer lookup. The Stanine/percentile shown after a session is a clearly-labelled synthetic
    estimate, since Aon’s real norms are confidential.</div>
  </div>`;
}

// =============================================================================
// TEST
// =============================================================================
function startSession(modeKey) {
  const m = MODES[modeKey];
  const seed = `${Date.now()}-${Math.floor(performance.now())}`;
  const opts = { seed, tier: state.tier, count: m.count };
  if (m.adaptive) opts.typeWeights = adaptiveWeights(load(), 2.2);
  const session = generateSession(opts);
  state.mode = modeKey;
  state.session = session;
  state.answers = session.items.map(() => ({ given: null, timeMs: 0, submittedTab: null }));
  state.current = 0; state.activeTab = 0; state.expired = false;
  state.options.allowBack = m.allowBack && state.options.allowBack;
  state.screen = 'test';
  state.enterTs = performance.now();
  if (m.timed) startTimer(m.time);
  render();
}

function startTimer(seconds) {
  clearInterval(state.timer);
  state.deadline = Date.now() + seconds * 1000;
  state.timer = setInterval(() => {
    const remaining = Math.round((state.deadline - Date.now()) / 1000);
    const el = document.querySelector('.timer');
    if (el) {
      el.textContent = fmtTime(remaining);
      el.classList.toggle('warn', remaining <= 60 && remaining > 20);
      el.classList.toggle('crit', remaining <= 20);
    }
    if (remaining <= 0) { state.expired = true; finish(); }
  }, 250);
}

function renderTest() {
  const { session, current } = state;
  const item = session.items[current];
  const m = MODES[state.mode];
  const right = m.timed ? `<span class="timer">${fmtTime(Math.round((state.deadline - Date.now()) / 1000))}</span>` : '<span class="muted">untimed</span>';

  const tabs = session.dataset.tabs.map((t, i) =>
    `<div class="tab${i === state.activeTab ? ' active' : ''}" data-tab="${i}">${esc(t.title)}</div>`).join('');
  const chart = renderChart(session.dataset.tabs[state.activeTab], session.dataset);

  const ans = state.answers[current];
  const answerBtns = ANSWERS.map((a) =>
    `<div class="ans ${a.cls}${ans.given === a.v ? ' sel' : ''}" data-ans="${a.v}">${a.label}</div>`).join('');

  const dots = session.items.map((_, i) => {
    const answered = state.answers[i].given != null;
    return `<div class="pdot${answered ? ' answered' : ''}${i === current ? ' current' : ''}" data-goto="${i}">${i + 1}</div>`;
  }).join('');

  return `${topbar(`<span class="muted">Question ${current + 1} / ${session.items.length}</span>${right}`)}
  <div class="panel">
    <div class="tabs">${tabs}</div>
    <div class="display-area">${chart}</div>
    <div class="statement">${esc(item.text)}</div>
    <div class="answers">${answerBtns}</div>
    <div class="navbar">
      <div>
        ${state.options.allowBack ? '<button class="btn secondary" data-prev>◀ Prev</button>' : ''}
        <button class="btn ghost" data-skip>Skip</button>
        <button class="btn secondary calc-toggle" data-calc>🖩 Calculator</button>
      </div>
      <div class="progress-dots">${dots}</div>
      <div>
        ${current < session.items.length - 1
          ? '<button class="btn" data-next>Next ▶</button>'
          : '<button class="btn" data-finish>Finish ▶</button>'}
      </div>
    </div>
  </div>
  <div class="panel small muted">
    Tip: confirm the correct tab is showing before you answer — on the real test, answering with the wrong
    tab up can cost points. Blanks score 0; wrong answers score −1, so skip rather than guess blindly.
  </div>`;
}

function selectAnswer(v) {
  const a = state.answers[state.current];
  a.given = v;
  a.submittedTab = state.session.dataset.tabs[state.activeTab].id;
  // reflect selection without a full re-render
  document.querySelectorAll('.ans').forEach((el) => el.classList.toggle('sel', el.dataset.ans === v));
  const dot = document.querySelector(`.pdot[data-goto="${state.current}"]`);
  if (dot) dot.classList.add('answered');
}

function accrueTime() {
  const now = performance.now();
  state.answers[state.current].timeMs += now - state.enterTs;
  state.enterTs = now;
}

function goTo(i) {
  accrueTime();
  state.current = Math.max(0, Math.min(state.session.items.length - 1, i));
  state.enterTs = performance.now();
  render();
}

// =============================================================================
// FINISH + SCORE
// =============================================================================
function finish() {
  clearInterval(state.timer);
  accrueTime();
  // mark blanks as timed-out if the clock expired
  const m = MODES[state.mode];
  state.answers.forEach((a) => { a.ranOutOfTime = !!(m.timed && state.expired && a.given == null); });
  const score = scoreSession(state.session, state.answers, { wrongTabPenalty: state.options.wrongTabPenalty });
  recordSession(score, { mode: state.mode, tier: state.tier, dateISO: new Date().toISOString() });
  state.lastScore = score;
  state.screen = 'results';
  render();
}

// =============================================================================
// RESULTS + REVIEW
// =============================================================================
function renderResults() {
  const s = state.lastScore;
  const items = state.session.items;

  const stat = (n, l, cls = '') => `<div class="stat ${cls}"><div class="n">${n}</div><div class="l">${l}</div></div>`;
  const scorebar = `<div class="scorebar">
    ${stat(s.correct, 'correct', 'good')}
    ${stat(s.wrong, 'wrong (−1 each)', 'bad')}
    ${stat(s.blank, 'blank (0)')}
    ${stat(s.adjustedScore, 'net score')}
    ${stat(pct(s.accuracyAttempted), 'accuracy (attempted)')}
    ${stat(pct(s.coverage), 'coverage')}
  </div>`;

  const naiveGap = s.naiveScore - s.adjustedScore;
  const penaltyNote = `<div class="banner">
    Naive “count correct” score would be <strong>${s.naiveScore}</strong>. With negative marking${s.tabPenalty ? ' and the wrong-tab penalty' : ''},
    your net score is <strong>${s.adjustedScore}</strong> — a <strong>${naiveGap}</strong>-point gap.
    ${s.wrong ? `${s.wrong} wrong answer${s.wrong > 1 ? 's' : ''} cost you ${s.wrong} point${s.wrong > 1 ? 's' : ''}; a blank would have cost 0.` : ''}
    ${s.wrongTabEvents ? ` ${s.wrongTabEvents} answer(s) submitted on the wrong tab cost ${s.tabPenalty} more.` : ''}
  </div>`;

  const norm = `<div class="row" style="align-items:center;margin-top:12px">
    <div class="stat" style="flex:0 0 160px">
      <div class="stanine-badge">${s.stanine}</div>
      <div class="l">Stanine (1–9) · ${esc(s.stanineLabel)}</div>
    </div>
    <div class="col">
      <div><strong>≈ ${s.percentile}th percentile</strong> <span class="muted small">(illustrative synthetic norm — not an official Aon result)</span></div>
      <div class="muted small" style="margin-top:6px">Avg time / attempted item: ${(s.avgTimeMs / 1000).toFixed(1)}s (target ~20s).
      Remember: on the real test you are <em>not</em> expected to finish — accuracy beats coverage.</div>
    </div>
  </div>`;

  // reason tally
  const reasons = Object.entries(s.reasonTally)
    .filter(([k]) => k !== 'correct_fast')
    .sort((a, b) => b[1] - a[1]);
  const reasonList = reasons.length
    ? `<h3>Where the points went</h3><div>${reasons.map(([k, n]) =>
        `<div class="bar-row"><div class="bar-label">${esc(REASONS[k]?.label || k)}</div>
         <div class="bar-track"><div class="bar-fill" style="width:${Math.min(100, n / s.count * 100)}%"></div></div>
         <div class="bar-num">${n}</div></div>`).join('')}</div>`
    : '';

  const review = s.perItem.map((p) => renderReviewItem(p, items[p.index])).join('');

  return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}
  <div class="panel">
    <h2 style="margin-top:0">Session review — ${esc(MODES[state.mode].label)} · ${esc(state.tier)}</h2>
    ${scorebar}
    ${penaltyNote}
    ${norm}
    ${reasonList}
    <div class="controls" style="margin-top:14px">
      <button class="btn" data-drill>Drill my weakest areas ▶</button>
      <button class="btn secondary" data-nav="progress">See progress over time</button>
      <button class="btn ghost" data-nav="home">Back to home</button>
    </div>
  </div>
  <div class="panel">
    <h3 style="margin-top:0">Per-question worked solutions</h3>
    <p class="muted small">Click any question to expand the step-by-step solution, the figures used, and the diagnosis.</p>
    ${review}
  </div>`;
}

function renderReviewItem(p, item) {
  const correct = item.label;
  const cls = p.isBlank ? 'blankh' : p.isCorrect ? 'correct' : 'wrong';
  const yourAns = p.isBlank ? '—' : ANSWERS.find((a) => a.v === p.given)?.label;
  const rightAns = ANSWERS.find((a) => a.v === correct)?.label;
  const pillCls = { TRUE: 't', FALSE: 'f', CANNOT_SAY: 'c' }[correct];
  const reqTabs = [...requiredTabs(item)];
  const tabNote = item.label === 'CANNOT_SAY'
    ? 'No single tab holds the answer — a required figure is missing.'
    : `Needed tab(s): <strong>${reqTabs.map((t) => esc(tabTitle(t))).join(', ') || '—'}</strong>`;

  const steps = item.solution.steps.map((s) => `<li>${esc(s)}</li>`).join('');
  const timeStr = p.timeMs != null ? `${(p.timeMs / 1000).toFixed(1)}s` : '';
  const diag = p.diagnosis.category === 'correct_fast' ? '' :
    `<div class="diag"><strong>${esc(p.diagnosis.label)}.</strong> ${esc(p.diagnosis.advice)}</div>`;

  return `<div class="review-item">
    <div class="review-head ${cls}" data-toggle>
      <div><span class="pill ${pillCls}">${rightAns}</span> &nbsp;${esc(item.text)}</div>
      <div class="small muted" style="white-space:nowrap">
        you: <strong>${esc(yourAns)}</strong> ${p.wrongTab ? '· ⚠ wrong tab' : ''} ${timeStr ? '· ' + timeStr : ''}
      </div>
    </div>
    <div class="review-body">
      <div class="small muted">${tabNote} · type: ${esc(item.type)}${(item.traps || []).length ? ' · traps: ' + item.traps.map(esc).join(', ') : ''}</div>
      <div class="solution"><ol>${steps}</ol></div>
      <div class="rationale">${esc(item.solution.rationale)}</div>
      ${diag}
    </div>
  </div>`;
}
function tabTitle(id) {
  const t = state.session.dataset.tabs.find((x) => x.id === id);
  return t ? t.title : id;
}

// =============================================================================
// PROGRESS
// =============================================================================
function renderProgress() {
  const data = load();
  const acc = typeAccuracy(data);
  const totalSeen = Object.values(data.byType).reduce((s, b) => s + b.seen, 0);

  if (!totalSeen) {
    return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}
      <div class="panel"><h2>Progress</h2><p class="muted">No sessions yet — complete a drill and your stats will appear here.</p>
      <button class="btn" data-nav="home">Start practising</button></div>`;
  }

  const typeBars = Object.entries(acc).sort((a, b) => a[1].accuracy - b[1].accuracy).map(([t, s]) =>
    `<div class="bar-row"><div class="bar-label">${esc(t)}</div>
     <div class="bar-track"><div class="bar-fill" style="width:${s.accuracy * 100}%;background:${s.accuracy < .5 ? 'var(--bad)' : s.accuracy < .75 ? 'var(--warn)' : 'var(--ok)'}"></div></div>
     <div class="bar-num">${pct(s.accuracy)} · ${s.seen}</div></div>`).join('');

  const tierBars = Object.entries(data.byTier).map(([t, b]) =>
    `<div class="bar-row"><div class="bar-label">${esc(t)}</div>
     <div class="bar-track"><div class="bar-fill" style="width:${b.seen ? b.correct / b.seen * 100 : 0}%"></div></div>
     <div class="bar-num">${b.seen ? pct(b.correct / b.seen) : '—'} · ${b.seen}</div></div>`).join('');

  const reasons = Object.entries(data.byReason).filter(([k]) => !['correct_fast'].includes(k))
    .sort((a, b) => b[1] - a[1]).slice(0, 8);
  const reasonBars = reasons.map(([k, n]) =>
    `<div class="bar-row"><div class="bar-label">${esc(REASONS[k]?.label || k)}</div>
     <div class="bar-track"><div class="bar-fill" style="width:${Math.min(100, n / totalSeen * 100 * 3)}%"></div></div>
     <div class="bar-num">${n}</div></div>`).join('');

  const hist = data.history.slice(-24);
  const maxH = Math.max(...hist.map((h) => h.accuracy), 1);
  const spark = hist.map((h) =>
    `<div class="b" style="height:${Math.max(3, h.accuracy / maxH * 60)}px" title="${new Date(h.date).toLocaleDateString()}: ${pct(h.accuracy)} · Stanine ${h.stanine}"></div>`).join('');

  const weak = weakestTypes(data, 3);
  const weakNote = weak.length ? `Weakest right now: ${weak.map((w) => `${w.type} (${pct(w.accuracy)})`).join(', ')}.` : '';

  return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}
  <div class="panel">
    <h2 style="margin-top:0">Progress</h2>
    <p class="muted">${data.sessions.length} sessions · ${totalSeen} items practised. ${esc(weakNote)}</p>
    <div class="row">
      <div class="col"><h3>Accuracy by item type</h3>${typeBars}</div>
      <div class="col"><h3>Accuracy by difficulty</h3>${tierBars}
        <h3 style="margin-top:16px">Accuracy trend (recent sessions)</h3>
        <div class="spark">${spark}</div>
      </div>
    </div>
    <h3>Most common “why wrong”</h3>${reasonBars}
    <div class="controls" style="margin-top:14px">
      <button class="btn" data-drill>Adaptive drill on weak areas ▶</button>
      <button class="btn ghost" data-reset>Reset all progress</button>
    </div>
  </div>`;
}

// =============================================================================
// GUIDE (renders GUIDE.md)
// =============================================================================
function renderGuide() {
  return `${topbar(`<span class="btn ghost" data-nav="home">Home</span>`)}
  <div class="panel guide">${mdToHtml(guideMd)}</div>
  <div class="panel"><button class="btn" data-nav="home">Back to home</button></div>`;
}

// Minimal, safe-enough Markdown → HTML for our own trusted guide file.
function mdToHtml(md) {
  const lines = md.replace(/\r/g, '').split('\n');
  let html = '', inList = false, inTable = false;
  const inline = (s) => esc(s)
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
    .replace(/\*([^*]+)\*/g, '<em>$1</em>')
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  const closeList = () => { if (inList) { html += '</ul>'; inList = false; } };
  const closeTable = () => { if (inTable) { html += '</tbody></table>'; inTable = false; } };

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (/^\|/.test(line)) {
      const cells = line.split('|').slice(1, -1).map((c) => c.trim());
      if (/^[-:\s|]+$/.test(line.replace(/\|/g, ''))) continue; // separator row
      if (!inTable) { closeList(); html += '<table><tbody>'; inTable = true; }
      const tag = html.endsWith('<tbody>') || /<\/tr>$/.test(html) && !html.includes('<td') ? 'th' : 'td';
      html += `<tr>${cells.map((c) => `<td>${inline(c)}</td>`).join('')}</tr>`;
      continue;
    } else closeTable();

    if (/^### /.test(line)) { closeList(); html += `<h3>${inline(line.slice(4))}</h3>`; }
    else if (/^## /.test(line)) { closeList(); html += `<h2>${inline(line.slice(3))}</h2>`; }
    else if (/^# /.test(line)) { closeList(); html += `<h1>${inline(line.slice(2))}</h1>`; }
    else if (/^> /.test(line)) { closeList(); html += `<blockquote>${inline(line.slice(2))}</blockquote>`; }
    else if (/^(---|___)\s*$/.test(line)) { closeList(); html += '<hr/>'; }
    else if (/^\s*[-*] /.test(line)) { if (!inList) { html += '<ul>'; inList = true; } html += `<li>${inline(line.replace(/^\s*[-*] /, ''))}</li>`; }
    else if (/^\s*\d+\. /.test(line)) { if (!inList) { html += '<ul>'; inList = true; } html += `<li>${inline(line.replace(/^\s*\d+\. /, ''))}</li>`; }
    else if (line.trim() === '') { closeList(); }
    else { closeList(); html += `<p>${inline(line)}</p>`; }
  }
  closeList(); closeTable();
  return html;
}

// =============================================================================
// CALCULATOR show/hide
// =============================================================================
function showCalc() {
  if (!calc) calc = createCalculator();
  document.body.appendChild(calc);
  document.addEventListener('keydown', calc._onKey);
}
function hideCalc() {
  if (calc && calc.parentNode) { calc.parentNode.removeChild(calc); document.removeEventListener('keydown', calc._onKey); }
}

// =============================================================================
// EVENT WIRING (delegation)
// =============================================================================
function wire() {
  // generic nav
  app.querySelectorAll('[data-nav]').forEach((el) => el.onclick = () => { state.screen = el.dataset.nav; render(); });
  app.querySelectorAll('[data-start]').forEach((el) => el.onclick = () => startSession(el.dataset.start));

  if (state.screen === 'home') {
    const tierSel = app.querySelector('[data-tier]');
    if (tierSel) tierSel.onchange = () => { state.tier = tierSel.value; };
    app.querySelectorAll('[data-opt]').forEach((el) => el.onchange = () => { state.options[el.dataset.opt] = el.checked; });
  }

  if (state.screen === 'test') {
    app.querySelectorAll('[data-tab]').forEach((el) => el.onclick = () => { state.activeTab = +el.dataset.tab; render(); });
    app.querySelectorAll('[data-ans]').forEach((el) => el.onclick = () => selectAnswer(el.dataset.ans));
    const next = app.querySelector('[data-next]'); if (next) next.onclick = () => goTo(state.current + 1);
    const prev = app.querySelector('[data-prev]'); if (prev) prev.onclick = () => goTo(state.current - 1);
    const skip = app.querySelector('[data-skip]'); if (skip) skip.onclick = () => goTo(state.current + 1);
    const fin = app.querySelector('[data-finish]'); if (fin) fin.onclick = () => finish();
    app.querySelectorAll('[data-goto]').forEach((el) => el.onclick = () => { if (state.options.allowBack || +el.dataset.goto >= state.current) goTo(+el.dataset.goto); });
    const calcBtn = app.querySelector('[data-calc]'); if (calcBtn) calcBtn.onclick = () => (calc && calc.parentNode ? hideCalc() : showCalc());
  }

  if (state.screen === 'results' || state.screen === 'progress') {
    app.querySelectorAll('[data-toggle]').forEach((el) => el.onclick = () => el.nextElementSibling.classList.toggle('open'));
    const drill = app.querySelector('[data-drill]'); if (drill) drill.onclick = () => startSession('adaptive');
    const rst = app.querySelector('[data-reset]'); if (rst) rst.onclick = () => { if (confirm('Erase all saved progress?')) { reset(); render(); } };
  }
}

// warn before leaving an in-progress timed test
window.addEventListener('beforeunload', (e) => {
  if (state.screen === 'test') { e.preventDefault(); e.returnValue = ''; }
});

render();
