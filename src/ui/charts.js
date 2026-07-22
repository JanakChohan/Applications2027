// -----------------------------------------------------------------------------
// charts.js — hand-rolled, deliberately BORING SVG charts and tables.
//
// The real scales test uses plain corporate charts, so these are intentionally
// unstyled-looking: thin gridlines, muted greys, small sans-serif labels. Every
// chart is built from the same (entities × periods) matrix the dataset exposes,
// and every chart shows its unit as a footnote — because reading the unit first
// is the whole game (thousands vs millions traps).
//
// Each renderer returns an SVG STRING. No chart library, no runtime deps.
// -----------------------------------------------------------------------------

// Muted, print-like palette (colour-blind-safe-ish, low saturation).
const PALETTE = ['#4a6785', '#8a9a5b', '#a8734f', '#6b6b8a', '#5f8a8a', '#9a6a7a', '#7a8a4a'];
const AXIS = '#888';
const GRID = '#e2e2e2';
const INK = '#333';

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

/** Build a {entities, periods, val(e,p)} view of a tab in DISPLAY units. */
function matrix(tab, dataset) {
  const scale = (dataset.units[tab.metric] || { scale: 1 }).scale;
  const map = new Map();
  for (const c of tab.cells) map.set(`${c.e}|${c.p}`, c.base / scale);
  return {
    entities: tab.entities,
    periods: tab.periods,
    val: (e, p) => map.get(`${e}|${p}`),
  };
}

function niceMax(v) {
  if (v <= 0) return 1;
  const mag = Math.pow(10, Math.floor(Math.log10(v)));
  const n = v / mag;
  const step = n <= 1 ? 1 : n <= 2 ? 2 : n <= 5 ? 5 : 10;
  return step * mag;
}

function fmt(n, decimals) {
  if (n == null) return '';
  const d = decimals != null ? decimals : Math.abs(n) >= 100 ? 0 : 1;
  return Number(n).toLocaleString('en-US', { maximumFractionDigits: d, minimumFractionDigits: 0 });
}

function footnote(tab) {
  const u = tab.unit;
  const label = u.kind === 'currency' ? `Figures in ${u.label}`
    : u.kind === 'percent' ? `Figures in ${u.label}`
    : u.kind === 'index' ? 'Index, base 100 in first period'
    : `Figures: ${u.label}`;
  return `<div class="chart-foot">${esc(label)}</div>`;
}

// ---- dispatch ---------------------------------------------------------------
export function renderChart(tab, dataset) {
  const inner = (() => {
    switch (tab.chart) {
      case 'table': return renderTable(tab, dataset);
      case 'line': return renderLine(tab, dataset);
      case 'pie': return renderPie(tab, dataset);
      case 'stackedBar': return renderStacked(tab, dataset);
      case 'bar': return renderBar(tab, dataset);
      case 'groupedBar':
      default: return renderGrouped(tab, dataset);
    }
  })();
  const cap = tab.caption
    ? `<div class="chart-caption">${esc(tab.caption.text)}: <strong>${esc(captionValue(tab, dataset))}</strong></div>`
    : '';
  return `<div class="chart-wrap"><div class="chart-title">${esc(tab.title)}</div>${inner}${cap}${footnote(tab)}</div>`;
}

function captionValue(tab, dataset) {
  const u = tab.caption.unit;
  return `${u.symbol}${fmt(tab.caption.base / u.scale, u.decimals)}${u.scale >= 1e6 ? 'm' : u.scale >= 1e3 ? 'k' : ''}`;
}

// ---- table ------------------------------------------------------------------
function renderTable(tab, dataset) {
  const m = matrix(tab, dataset);
  const head = `<tr><th>${esc(dataset.meta.entityLabel)}</th>${m.periods.map((p) => `<th>${esc(p)}</th>`).join('')}</tr>`;
  const rows = m.entities.map((e) =>
    `<tr><td class="rowlab">${esc(e)}</td>${m.periods.map((p) => `<td>${fmt(m.val(e, p), tab.unit.decimals)}</td>`).join('')}</tr>`
  ).join('');
  let total = '';
  if (tab.hasTotal) {
    const cells = m.periods.map((p) => {
      let s = 0; for (const e of m.entities) s += m.val(e, p) || 0;
      return `<td>${fmt(s, tab.unit.decimals)}</td>`;
    }).join('');
    total = `<tr class="totalrow"><td class="rowlab">Total (shown)</td>${cells}</tr>`;
  }
  return `<div class="table-scroll"><table class="data-table">${head}${rows}${total}</table></div>`;
}

// ---- shared plot frame ------------------------------------------------------
function frame(w, h, pad) {
  return { w, h, pad, x0: pad.l, x1: w - pad.r, y0: h - pad.b, y1: pad.t };
}
function yAxis(f, max, decimals) {
  const ticks = 4;
  let g = '';
  for (let i = 0; i <= ticks; i++) {
    const v = (max / ticks) * i;
    const y = f.y0 - (f.y0 - f.y1) * (i / ticks);
    g += `<line x1="${f.x0}" y1="${y}" x2="${f.x1}" y2="${y}" stroke="${GRID}"/>`;
    g += `<text x="${f.x0 - 6}" y="${y + 3}" text-anchor="end" class="axlab">${fmt(v, decimals)}</text>`;
  }
  return g;
}

// ---- grouped bar (entities within each period) ------------------------------
function renderGrouped(tab, dataset) {
  const m = matrix(tab, dataset);
  const w = 460, h = 260, f = frame(w, h, { l: 46, r: 12, t: 16, b: 34 });
  let max = 0;
  for (const e of m.entities) for (const p of m.periods) max = Math.max(max, m.val(e, p) || 0);
  max = niceMax(max);
  const groups = m.periods.length, gw = (f.x1 - f.x0) / groups;
  const bw = Math.min(26, (gw - 8) / m.entities.length);
  let bars = '';
  m.periods.forEach((p, gi) => {
    const gx = f.x0 + gi * gw;
    m.entities.forEach((e, ei) => {
      const v = m.val(e, p) || 0;
      const bh = (f.y0 - f.y1) * (v / max);
      const x = gx + (gw - bw * m.entities.length) / 2 + ei * bw;
      bars += `<rect x="${x}" y="${f.y0 - bh}" width="${bw - 2}" height="${bh}" fill="${PALETTE[ei % PALETTE.length]}"><title>${esc(e)} ${esc(p)}: ${fmt(v)}</title></rect>`;
    });
    bars += `<text x="${gx + gw / 2}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(p)}</text>`;
  });
  return svg(w, h, yAxis(f, max, tab.unit.decimals) + bars) + legend(m.entities);
}

// ---- single-series bar (latest period per entity) ---------------------------
function renderBar(tab, dataset) {
  const m = matrix(tab, dataset);
  const p = m.periods[m.periods.length - 1];
  const w = 460, h = 250, f = frame(w, h, { l: 46, r: 12, t: 16, b: 40 });
  let max = 0; for (const e of m.entities) max = Math.max(max, m.val(e, p) || 0);
  max = niceMax(max);
  const bw = (f.x1 - f.x0) / m.entities.length;
  let bars = '';
  m.entities.forEach((e, i) => {
    const v = m.val(e, p) || 0;
    const bh = (f.y0 - f.y1) * (v / max);
    const x = f.x0 + i * bw + bw * 0.2;
    bars += `<rect x="${x}" y="${f.y0 - bh}" width="${bw * 0.6}" height="${bh}" fill="${PALETTE[i % PALETTE.length]}"><title>${esc(e)}: ${fmt(v)}</title></rect>`;
    bars += `<text x="${x + bw * 0.3}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(e)}</text>`;
  });
  bars += `<text x="${(f.x0 + f.x1) / 2}" y="${h - 6}" text-anchor="middle" class="axsub">${esc(p)}</text>`;
  return svg(w, h, yAxis(f, max, tab.unit.decimals) + bars);
}

// ---- line (periods on x, one line per entity) -------------------------------
function renderLine(tab, dataset) {
  const m = matrix(tab, dataset);
  const w = 460, h = 260, f = frame(w, h, { l: 46, r: 12, t: 16, b: 34 });
  let max = 0, min = Infinity;
  for (const e of m.entities) for (const p of m.periods) { const v = m.val(e, p); if (v != null) { max = Math.max(max, v); min = Math.min(min, v); } }
  const base0 = tab.unit.kind === 'index' ? Math.max(0, min * 0.9) : 0;
  const span = niceMax(max - base0) || 1;
  const X = (i) => f.x0 + (f.x1 - f.x0) * (m.periods.length === 1 ? 0.5 : i / (m.periods.length - 1));
  const Y = (v) => f.y0 - (f.y0 - f.y1) * ((v - base0) / span);
  let g = '';
  for (let i = 0; i <= 4; i++) {
    const y = f.y0 - (f.y0 - f.y1) * (i / 4);
    g += `<line x1="${f.x0}" y1="${y}" x2="${f.x1}" y2="${y}" stroke="${GRID}"/>`;
    g += `<text x="${f.x0 - 6}" y="${y + 3}" text-anchor="end" class="axlab">${fmt(base0 + span * (i / 4), tab.unit.decimals)}</text>`;
  }
  m.entities.forEach((e, ei) => {
    const pts = m.periods.map((p, i) => `${X(i)},${Y(m.val(e, p))}`).join(' ');
    g += `<polyline points="${pts}" fill="none" stroke="${PALETTE[ei % PALETTE.length]}" stroke-width="2"/>`;
    m.periods.forEach((p, i) => { g += `<circle cx="${X(i)}" cy="${Y(m.val(e, p))}" r="2.5" fill="${PALETTE[ei % PALETTE.length]}"><title>${esc(e)} ${esc(p)}: ${fmt(m.val(e, p))}</title></circle>`; });
  });
  m.periods.forEach((p, i) => { g += `<text x="${X(i)}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(p)}</text>`; });
  const leg = m.entities.length > 1 || m.entities[0] !== '__ALL__' ? legend(m.entities.map((e) => e === '__ALL__' ? tab.title : e)) : '';
  return svg(w, h, g) + leg;
}

// ---- stacked bar (periods on x, entities stacked) ---------------------------
function renderStacked(tab, dataset) {
  const m = matrix(tab, dataset);
  const w = 460, h = 260, f = frame(w, h, { l: 46, r: 12, t: 16, b: 34 });
  let max = 0;
  for (const p of m.periods) { let s = 0; for (const e of m.entities) s += m.val(e, p) || 0; max = Math.max(max, s); }
  max = niceMax(max);
  const bw = Math.min(46, (f.x1 - f.x0) / m.periods.length * 0.6);
  let g = yAxis(f, max, tab.unit.decimals);
  m.periods.forEach((p, gi) => {
    const cx = f.x0 + (f.x1 - f.x0) * ((gi + 0.5) / m.periods.length);
    let acc = 0;
    m.entities.forEach((e, ei) => {
      const v = m.val(e, p) || 0;
      const bh = (f.y0 - f.y1) * (v / max);
      const y = f.y0 - (f.y0 - f.y1) * (acc / max) - bh;
      g += `<rect x="${cx - bw / 2}" y="${y}" width="${bw}" height="${bh}" fill="${PALETTE[ei % PALETTE.length]}"><title>${esc(e)} ${esc(p)}: ${fmt(v)}</title></rect>`;
      acc += v;
    });
    g += `<text x="${cx}" y="${f.y0 + 16}" text-anchor="middle" class="axlab">${esc(p)}</text>`;
  });
  return svg(w, h, g) + legend(m.entities);
}

// ---- pie (shares for the latest period) -------------------------------------
function renderPie(tab, dataset) {
  const m = matrix(tab, dataset);
  const p = m.periods[m.periods.length - 1];
  const vals = m.entities.map((e) => Math.max(0, m.val(e, p) || 0));
  const total = vals.reduce((s, v) => s + v, 0) || 1;
  const cx = 130, cy = 130, r = 100;
  let a0 = -Math.PI / 2, g = '';
  m.entities.forEach((e, i) => {
    const frac = vals[i] / total;
    const a1 = a0 + frac * Math.PI * 2;
    const large = a1 - a0 > Math.PI ? 1 : 0;
    const x0 = cx + r * Math.cos(a0), y0 = cy + r * Math.sin(a0);
    const x1 = cx + r * Math.cos(a1), y1 = cy + r * Math.sin(a1);
    g += `<path d="M${cx},${cy} L${x0},${y0} A${r},${r} 0 ${large} 1 ${x1},${y1} Z" fill="${PALETTE[i % PALETTE.length]}" stroke="#fff"><title>${esc(e)}: ${fmt(vals[i])}%</title></path>`;
    a0 = a1;
  });
  return svg(260, 260, g) + legend(m.entities.map((e, i) => `${e} (${fmt(vals[i])}%)`));
}

// ---- helpers ----------------------------------------------------------------
function svg(w, h, body) {
  return `<svg viewBox="0 0 ${w} ${h}" class="chart-svg" role="img" preserveAspectRatio="xMidYMid meet">${body}</svg>`;
}
function legend(labels) {
  return `<div class="legend">${labels.map((l, i) =>
    `<span class="leg"><span class="swatch" style="background:${PALETTE[i % PALETTE.length]}"></span>${esc(l)}</span>`
  ).join('')}</div>`;
}
