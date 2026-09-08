// Renders guide_source.html to PDF with headless Chromium via Playwright.
// Usage: node build_pdf.js
const path = require('path');
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');

(async () => {
  const name = process.argv[2] || 'guide_source.html';
const outName = process.argv[3] || 'JPMorgan_Private_Bank_2027_London_Internship_Guide.pdf';
const src = 'file://' + path.resolve(__dirname, name);
  const out = path.resolve(__dirname, outName);
const footerTitle = process.argv[4] || 'J.P. Morgan Global Private Bank 2027 London Internship Guide';
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(src, { waitUntil: 'load' });
  await page.pdf({
    path: out,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<div></div>',
    footerTemplate: `<div style="width:100%;font-size:8px;color:#666;padding:0 16mm;display:flex;justify-content:space-between;font-family:Helvetica,Arial,sans-serif;">
      <span>${footerTitle}</span>
      <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
    margin: { top: '18mm', right: '16mm', bottom: '20mm', left: '16mm' },
  });
  await browser.close();
  console.log('Wrote', out);
})().catch((e) => { console.error(e); process.exit(1); });
