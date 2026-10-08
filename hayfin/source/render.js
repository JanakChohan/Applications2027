// usage: node render.js in.html out.pdf [--toc]
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path'); const { execSync } = require('child_process');
const [,, inHtml, outPdf, flag] = process.argv;
const header = `<div style="font-family:Helvetica,Arial,sans-serif;font-size:7.5px;color:#6b7280;width:100%;padding:0 14mm;display:flex;justify-content:space-between"><span>Hayfin · Partner Solutions Group · Summer 2027 · Interview Research Pack</span><span>Public sources only · built 8 Oct 2026</span></div>`;
const footer = `<div style="font-family:Helvetica,Arial,sans-serif;font-size:7.5px;color:#6b7280;width:100%;padding:0 14mm;display:flex;justify-content:space-between"><span>[Sxx] = source in Part 15 · [Confirmed] [Reported] [Inferred]</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`;
async function render(html, out) {
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(html), { waitUntil: 'load' });
  await p.pdf({ path: out, format: 'A4', printBackground: true, displayHeaderFooter: flag !== '--nohf',
    headerTemplate: header, footerTemplate: footer,
    margin: { top: '16mm', bottom: '15mm', left: '0mm', right: '0mm' } });
  await b.close();
}
(async () => {
  await render(inHtml, outPdf);
  if (flag === '--toc') {
    const src = fs.readFileSync(inHtml, 'utf8');
    const ids = [...src.matchAll(/data-toc="([A-Za-z0-9_]+)"/g)].map(m => m[1]);
    const n = parseInt(execSync(`pdfinfo "${outPdf}" | grep Pages | awk '{print $2}'`).toString());
    const map = {};
    for (let i = 1; i <= n; i++) {
      const t = execSync(`pdftotext -f ${i} -l ${i} "${outPdf}" -`).toString();
      for (const m of t.matchAll(/QQ([A-Za-z0-9_]+?)QQ/g)) if (!(m[1] in map)) map[m[1]] = i;
    }
    let s2 = src.replace(/<span class="tocpg" data-for="([A-Za-z0-9_]+)">[^<]*<\/span>/g, (a, id) => `<span class="tocpg" data-for="${id}">${map[id] ?? '?'}</span>`);
    const missing = ids.filter(i => !(i in map));
    if (missing.length) console.error('MISSING markers:', missing.join(','));
    fs.writeFileSync(inHtml, s2);
    await render(inHtml, outPdf);
    console.log('pages', n, 'toc', JSON.stringify(map));
  }
})();
