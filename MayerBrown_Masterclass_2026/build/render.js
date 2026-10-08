// usage: node render.js in.html out.pdf [hf=1] [title]
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [inp, out, hf = '1', title = ''] = process.argv.slice(2);
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(async () => chromium.launch());
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(inp), { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  const header = `<div style="font-family:Inter,sans-serif;font-size:7px;color:#5B6475;width:100%;padding:0 16mm;display:flex;justify-content:space-between;"><span style="font-weight:700;color:#14213D">${title}</span><span>Public sources only. Confidence-tagged. Built 8 Oct 2026</span></div>`;
  const footer = `<div style="font-family:Inter,sans-serif;font-size:7px;color:#5B6475;width:100%;padding:0 16mm;display:flex;justify-content:space-between;"><span>Mayer Brown Masterclass 2026 · SEO London · prep pack</span><span style="font-weight:700;color:#14213D">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`;
  const opts = { path: out, format: 'A4', printBackground: true, preferCSSPageSize: true };
  if (hf === '1') Object.assign(opts, { displayHeaderFooter: true, headerTemplate: header, footerTemplate: footer });
  await page.pdf(opts);
  await browser.close();
})();
