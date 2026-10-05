const { chromium } = require('playwright');
(async () => { const b = await chromium.launch(); const p = await b.newPage();
 await p.goto('file:///home/user/Applications2027/investec/build/Cheat_Sheet.html');
 await p.pdf({ path: '/home/user/Applications2027/investec/Cheat_Sheet.pdf', format: 'A4', printBackground: true, margin: {top:'10mm',bottom:'10mm',left:'10mm',right:'10mm'} });
 await b.close(); })();
