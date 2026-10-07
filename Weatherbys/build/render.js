// Render HTML to PDF with Chromium. Usage: node render.js in.html out.pdf [title]
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const path = require('path');
(async () => {
  const [inp, out, title] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(inp), { waitUntil: 'load' });
  const t = title || 'Weatherbys Private Banking Internship 2027: Research Pack';
  await page.pdf({
    path: out, format: 'A4', printBackground: true, displayHeaderFooter: true,
    margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' },
    headerTemplate: `<div style="font-size:7px;width:100%;padding:0 16mm;color:#5b6475;font-family:Arial;display:flex;justify-content:space-between"><span>${t}</span><span>Prepared 7 Oct 2026 from public sources</span></div>`,
    footerTemplate: `<div style="font-size:7px;width:100%;padding:0 16mm;color:#5b6475;font-family:Arial;display:flex;justify-content:space-between"><span>Sources: Part 15. Confidence tags: Confirmed / Reported / Inferred</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
  });
  await browser.close();
})();
