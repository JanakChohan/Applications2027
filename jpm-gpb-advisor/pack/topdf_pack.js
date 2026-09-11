const { chromium } = require('/opt/node22/lib/node_modules/playwright');
(async () => {
  const [input, output, header] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + require('path').resolve(input), { waitUntil: 'networkidle' });
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: output, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: `<div style="font-size:7.5px;color:#8a93a3;width:100%;padding:0 17mm;font-family:Arial;display:flex;justify-content:space-between;"><span>${header}</span><span>Prepared 11 September 2026 · public sources only</span></div>`,
    footerTemplate: '<div style="font-size:7.5px;color:#8a93a3;width:100%;padding:0 17mm;font-family:Arial;display:flex;justify-content:space-between;"><span>J.P. Morgan Global Private Bank · Advisor Summer Internship 2027 · London</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>',
    margin: { top: '22mm', bottom: '20mm', left: '17mm', right: '17mm' } });
  await browser.close();
  console.log('ok', output);
})().catch(e => { console.error(e); process.exit(1); });
