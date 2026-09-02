const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path');

(async () => {
  const dir = __dirname;
  const url = 'file://' + path.join(dir, 'blackstone-briefing.html');
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(1200);

  // ---- pass 1: cover, full bleed ----
  const coverStyle = await page.addStyleTag({ content:
    `section{display:none !important} @page{size:A4;margin:0 !important}` });
  await page.pdf({ path: path.join(dir,'_cover.pdf'), format:'A4', printBackground:true,
                   margin:{top:'0',bottom:'0',left:'0',right:'0'} });
  await page.evaluate(el => el.remove(), coverStyle);

  // ---- pass 2: body, with margins + footer ----
  await page.addStyleTag({ content:
    `.cover{display:none !important} @page{size:A4;margin:0}
     section:first-of-type{break-before:auto !important}` });
  await page.pdf({ path: path.join(dir,'_body.pdf'), format:'A4', printBackground:true,
    margin:{ top:'16mm', bottom:'15mm', left:'15mm', right:'15mm' },
    displayHeaderFooter:true,
    headerTemplate:'<div></div>',
    footerTemplate:`<div style="width:100%;font-size:7.5px;font-family:Helvetica,Arial,sans-serif;color:#9aa0a6;padding:0 15mm;display:flex;justify-content:space-between;align-items:center;">
      <span style="letter-spacing:.06em;">BLACKSTONE &mdash; DEEP DIVE BRIEFING &nbsp;·&nbsp; PREPARED 2 SEPTEMBER 2026</span>
      <span class="pageNumber" style="font-weight:600;color:#5c6470;"></span></div>`
  });

  await browser.close();
  console.log('rendered');
})();
