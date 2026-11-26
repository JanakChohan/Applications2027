
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://' + process.argv[2], { waitUntil: 'networkidle' });
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="font-family:Inter,Arial,sans-serif;font-size:7.5pt;color:#5f6368;width:100%;padding:0 16mm;display:flex;justify-content:space-between;"><span>Crocs (CROX): risks and catalysts. Study guide. Data as of 25 Nov 2026. Not investment advice.</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>',
    margin: { top: '17mm', bottom: '18mm', left: '16mm', right: '16mm' } });
  await b.close();
})();
