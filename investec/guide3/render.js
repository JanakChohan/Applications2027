// Two-pass render: HTML -> PDF with real contents-page numbers.
// Usage: node render.js in.html out.pdf [--toc]
const { chromium } = require('playwright');
const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

const [,, inHtml, outPdf, flag] = process.argv;

async function render(htmlPath, pdfPath, title) {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(htmlPath), { waitUntil: 'load' });
  await page.pdf({
    path: pdfPath, format: 'A4', printBackground: true,
    margin: { top: '16mm', bottom: '16mm', left: '14mm', right: '14mm' },
    displayHeaderFooter: true,
    headerTemplate: `<div style="font-size:7px;width:100%;padding:0 14mm;color:#5b6b82;font-family:Helvetica,Arial;display:flex;justify-content:space-between"><span>${title}</span><span>Public sources only · prepared 7 Oct 2026</span></div>`,
    footerTemplate: `<div style="font-size:7px;width:100%;padding:0 14mm;color:#5b6b82;font-family:Helvetica,Arial;display:flex;justify-content:space-between"><span>Client-Facing at Investec · Ideal Work Environment</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
  });
  await browser.close();
}

(async () => {
  const title = 'CLIENT-FACING AT INVESTEC';
  if (flag !== '--toc') { await render(inHtml, outPdf, title); return; }
  await render(inHtml, outPdf, title);
  // map anchor markers to pages
  const n = parseInt(execSync(`pdfinfo "${outPdf}" | grep Pages | awk '{print $2}'`).toString());
  const map = {};
  for (let p = 1; p <= n; p++) {
    const t = execSync(`pdftotext -f ${p} -l ${p} -layout "${outPdf}" -`).toString();
    const re = /QQA([a-z0-9-]+)QQ/g; let m;
    while ((m = re.exec(t))) if (!(m[1] in map)) map[m[1]] = p;
  }
  let html = fs.readFileSync(inHtml, 'utf8');
  html = html.replace(/<span class="tocpg" data-a="([a-z0-9-]+)">[^<]*<\/span>/g,
    (s, a) => `<span class="tocpg" data-a="${a}">${map[a] ?? '?'}</span>`);
  fs.writeFileSync(inHtml, html);
  await render(inHtml, outPdf, title);
  console.log(JSON.stringify(map));
})();
