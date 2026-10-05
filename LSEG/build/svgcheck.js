const fs=require('fs');const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:794,height:1123}});
const h=fs.readFileSync(process.argv[2],'utf8');await p.setContent(h);await p.evaluate(()=>document.fonts.ready);
const res=await p.evaluate(()=>{const out=[];
document.querySelectorAll('figure.fig').forEach(fig=>{const ft=(fig.querySelector('.ft')||{}).textContent;const svg=fig.querySelector('svg');if(!svg)return;
const vb=svg.viewBox.baseVal;const texts=[...svg.querySelectorAll('text')].filter(t=>!t.closest('defs'));
const boxes=[];
texts.forEach(t=>{let bb;try{bb=t.getBBox()}catch(e){return}
 // transform to svg user space
 const m=t.getCTM(),sm=svg.getCTM();if(!m||!sm)return;const r=sm.inverse().multiply(m);
 const pts=[[bb.x,bb.y],[bb.x+bb.width,bb.y],[bb.x,bb.y+bb.height],[bb.x+bb.width,bb.y+bb.height]].map(([x,y])=>[r.a*x+r.c*y+r.e,r.b*x+r.d*y+r.f]);
 const x1=Math.min(...pts.map(p=>p[0])),x2=Math.max(...pts.map(p=>p[0])),y1=Math.min(...pts.map(p=>p[1])),y2=Math.max(...pts.map(p=>p[1]));
 const fs_=parseFloat(getComputedStyle(t).fontSize);
 if(x1<vb.x-1||x2>vb.x+vb.width+1||y1<vb.y-1||y2>vb.y+vb.height+1) out.push(`${ft}: OUTSIDE viewBox "${t.textContent.slice(0,40)}" x[${x1|0},${x2|0}] y[${y1|0},${y2|0}] vb ${vb.width}x${vb.height}`);
 if(fs_<9.5 && !t.closest('[aria-hidden]')) out.push(`${ft}: small font ${fs_} "${t.textContent.slice(0,30)}"`);
 boxes.push({x1,x2,y1:y1+bb.height*0.2,y2:y2-bb.height*0.2,s:t.textContent.slice(0,30),t});});
for(let i=0;i<boxes.length;i++)for(let j=i+1;j<boxes.length;j++){const a=boxes[i],c=boxes[j];
 if(a.t.contains(c.t)||c.t.contains(a.t))continue;
 const ox=Math.min(a.x2,c.x2)-Math.max(a.x1,c.x1),oy=Math.min(a.y2,c.y2)-Math.max(a.y1,c.y1);
 if(ox>2&&oy>1.5) out.push(`${ft}: OVERLAP "${a.s}" / "${c.s}" (${ox|0}x${oy|0})`);}
});return out;});
console.log(res.join('\n')||'clean');await b.close();})();
