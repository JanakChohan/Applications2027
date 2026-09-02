const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path=require('path'), fs=require('fs');
(async()=>{
  const dir=__dirname; fs.mkdirSync(path.join(dir,'shots'),{recursive:true});
  const b=await chromium.launch();
  const p=await b.newPage({viewport:{width:681,height:1400},deviceScaleFactor:2});
  await p.emulateMedia({media:'print'});
  await p.goto('file://'+path.join(dir,'blackstone-briefing.html'),{waitUntil:'load'});
  await p.evaluate(()=>document.fonts.ready); await p.waitForTimeout(1000);
  const figs=await p.$$('figure');
  for(let i=0;i<figs.length;i++){
    await figs[i].screenshot({path:path.join(dir,'shots',`fig${String(i+1).padStart(2,'0')}.png`)});
  }
  console.log('figures:',figs.length);
  await b.close();
})();
