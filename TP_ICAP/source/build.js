const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const out = process.argv[2]; const src = process.argv[3] || 'guide.html'; const ft = process.argv[4] || "TP ICAP: the complete beginner's firm guide";
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + path.resolve(src));
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-family:Verdana,sans-serif;font-size:8.5pt;color:#4f5b69;padding:0 17mm;display:flex;justify-content:space-between"><span>' + ft.replace(/'/g,'&#39;') + '</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>' });
  const bg = await b.newPage();
  await bg.setContent('<html><body style="margin:0;background:#FBF6EA"></body></html>');
  await bg.pdf({ path: 'bg.pdf', format: 'A4', printBackground: true, margin:{top:0,bottom:0,left:0,right:0} });
  await b.close();
})();
