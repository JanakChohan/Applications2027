// Assemble parts/*.html into one self-contained HTML, render to PDF in two passes
// so the contents page carries real page numbers.
// Usage: node build.js
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');
const { chromium } = require('/opt/node-tools/node_modules/playwright');

const ROOT = __dirname;
const OUT = path.resolve(ROOT, '..');
const NAME = 'LSEG_Business_Management_Summer_Internship_Complete_Interview_Pack';
const fonts = fs.readFileSync(path.join(ROOT, 'fonts/fonts_embed.css'), 'utf8');
const css = fs.readFileSync(path.join(ROOT, 'style.css'), 'utf8');
const cover = fs.readFileSync(path.join(ROOT, 'cover.html'), 'utf8');
const partFiles = fs.readdirSync(path.join(ROOT, 'parts')).filter(f => f.endsWith('.html')).sort();
let body = partFiles.map(f => fs.readFileSync(path.join(ROOT, 'parts', f), 'utf8')).join('\n');

// Renumber figures sequentially in document order and update every "Figure X" reference.
const figMap = {};
let figN = 0;
for (const m of body.matchAll(/<div class="ft">Figure ([0-9]+[a-z]?)<\/div>/g)) { if (!(m[1] in figMap)) figMap[m[1]] = String(++figN); }
const remap = t => t.replace(/\b(Figures?) ([0-9]+[a-z]?)((?:(?:,| and|,? and| to| or) [0-9]+[a-z]?\b)*)/g, (m, w, k, tail) =>
  `${w} ${figMap[k] || k}` + tail.replace(/[0-9]+[a-z]?/g, x => figMap[x] || x));
body = remap(body);
console.log('figures renumbered:', figN);
fs.writeFileSync(path.join(ROOT, 'figmap.json'), JSON.stringify(figMap, null, 1));

// Collect TOC entries: part bands (data-toc on section) and h2 with id.
const entries = [];
let n = 0;
const mk = id => { const i = entries.findIndex(e => e.id === id); return `<span class="pm">MK${1000 + i}KM</span>`; };
body = body.replace(/<section class="part([^"]*)" id="([^"]+)" data-toc="([^"]+)">/g, (m, cls, id, title) => {
  entries.push({ id, title, level: 1 });
  return `${m}${mk(id)}`;
});
body = body.replace(/<h2 id="([^"]+)"([^>]*)>([\s\S]*?)<\/h2>/g, (m, id, rest, title) => {
  entries.push({ id, title: title.replace(/<[^>]+>/g, ''), level: 2 });
  return `<h2 id="${id}"${rest}>${mk(id)}${title}</h2>`;
});
// keep entries in document order
entries.forEach((e, i) => { e.key = String(1000 + i); e.pos = body.indexOf(`MK${e.key}KM`); });
entries.sort((a, b) => a.pos - b.pos);

function tocHtml(pages) {
  const rows = entries.map(e => {
    const pg = pages && pages[e.id] ? pages[e.id] : '00';
    return `<div class="row ${e.level === 1 ? 'part-row' : 'sub'}"><span class="t"><a href="#${e.id}">${e.title}</a></span><span class="pg">${pg}</span></div>`;
  }).join('\n');
  return `<section class="tocpage" id="contents"><div class="band"><div class="num">Contents</div><h1>What is in this pack</h1><p class="lede">Page numbers count from the first page after the cover.</p></div><div class="toc">${rows}</div></section>`;
}

function html(pages) {
  return `<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>LSEG Interview Pack</title><style>${fonts}\n${css}</style></head><body>${tocHtml(pages)}\n${body}</body></html>`;
}

const headerT = `<div style="font-family:Arial,sans-serif;font-size:7px;color:#5B6577;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>LSEG &middot; Business Management Summer Internship 2027 &middot; Interview research pack</span><span>Built 5 Oct 2026 from public sources</span></div>`;
const footerT = `<div style="font-family:Arial,sans-serif;font-size:7px;color:#5B6577;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>[Sxx] = source table, Part 15 &middot; Confirmed / Reported / Inferred = confidence</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`;

async function render(page, htmlStr, file, withHF) {
  await page.setContent(htmlStr, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: file, format: 'A4', printBackground: true,
    displayHeaderFooter: withHF, headerTemplate: headerT, footerTemplate: footerT,
    margin: withHF ? { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' } : { top: '0', bottom: '0', left: '0', right: '0' },
  });
}

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const tmp1 = path.join(ROOT, 'pass1.pdf');
  await render(page, html(null), tmp1, true);
  const txt = execSync(`pdftotext -layout "${tmp1}" -`, { maxBuffer: 1 << 28 }).toString();
  const pagesTxt = txt.split('\f');
  const pages = {};
  pagesTxt.forEach((t, i) => { for (const m of t.replace(/\s+/g, "").matchAll(/MK(\d{4})KM/g)) { const e = entries.find(x => x.key === m[1]); if (e && !pages[e.id]) pages[e.id] = i + 1; } });
  const missing = entries.filter(e => !pages[e.id]).map(e => e.id);
  if (missing.length) console.log('WARN markers not found:', missing.join(', '));
  const final = html(pages);
  fs.writeFileSync(path.join(OUT, `${NAME}.html`), `<!-- cover -->\n` + final.replace('<body>', `<body>${cover}<div style="break-after:page"></div>`));
  const bodyPdf = path.join(ROOT, 'body.pdf');
  await render(page, final, bodyPdf, true);
  // cover without header/footer
  const coverPdf = path.join(ROOT, 'cover.pdf');
  await page.setViewportSize({ width: 794, height: 1123 });
  await render(page, `<!doctype html><html><head><meta charset="utf-8"><style>${fonts}\n${css}\n@page{margin:0}.cover{height:297mm;padding:30mm 20mm}</style></head><body>${cover}</body></html>`, coverPdf, false);
  await browser.close();
  execSync(`python3 -c "
from pypdf import PdfWriter
w=PdfWriter()
for f in ['${coverPdf}','${bodyPdf}']: w.append(f)
w.write('${path.join(OUT, NAME + '.pdf')}')
"`);
  const total = pagesTxt.length - 1;
  console.log('pages(body):', total, 'toc entries:', entries.length);
  // render cheat sheet standalone if present
  const cs = path.join(ROOT, 'parts');
  const csFile = partFiles.find(f => /cheat/i.test(f));
  if (csFile) {
    const b2 = await chromium.launch(); const p2 = await b2.newPage();
    const csHtml = remap(fs.readFileSync(path.join(cs, csFile), 'utf8')).replace(/class="part([^"]*)"/, 'class="cs$1"');
    await render(p2, `<!doctype html><html><head><meta charset="utf-8"><style>${fonts}\n${css}</style></head><body>${csHtml}</body></html>`, path.join(OUT, 'Cheat_Sheet.pdf'), true);
    await b2.close();
  }
})();
