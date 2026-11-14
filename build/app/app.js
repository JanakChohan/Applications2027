(function(){
'use strict';
document.documentElement.classList.add('js');
var DATA=JSON.parse(document.getElementById('data').textContent);
var $=function(s,r){return (r||document).querySelector(s)};
var $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var esc=function(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})};
var VIEWS=['home','read','teams','people','mandates','awareness','roles','lifecycle','calculator','why','practice','glossary','sources','search'];
var reduceMotion=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ---------- optional local progress ---------- */
var KEY='gsamcsg.v1',store={save:false,steps:{},history:[]};
function lsGet(){try{var v=localStorage.getItem(KEY);return v?JSON.parse(v):null}catch(e){return null}}
function lsSet(){if(!store.save)return;try{localStorage.setItem(KEY,JSON.stringify(store))}catch(e){}}
function lsClear(){try{localStorage.removeItem(KEY)}catch(e){}}
(function(){var s=lsGet();if(s&&s.save){store=s;store.steps=store.steps||{};store.history=store.history||[]}})();
function toast(msg){var t=document.createElement('div');t.className='toast';t.setAttribute('role','status');t.textContent=msg;document.body.appendChild(t);setTimeout(function(){t.remove()},2600)}

/* ---------- fee model (mirror of build/calc.py) ---------- */
var CDEF={currency:'£',size:500000000,funded_pct_initial:100,remaining_funded_month:null,annual_return_pct:0,flow_amount:0,flow_month:null,monthly_flow:0,monthly_flow_start:null,fee_mode:'flat',fee_bps:20,tiers:[],fee_change_month:null,new_fee_bps:null,months:12,fee_base:'market_value'};
function annualFee(base,p,month){
  if(p.fee_mode==='tiered'&&p.tiers&&p.tiers.length){var fee=0,lower=0;for(var i=0;i<p.tiers.length;i++){var t=p.tiers[i];var upper=(t.upto==null)?Infinity:t.upto;var slice=Math.max(0,Math.min(base,upper)-lower);fee+=slice*t.bps/10000;lower=upper;if(base<=upper)break}return fee}
  var bps=p.fee_bps;if(p.fee_change_month&&p.new_fee_bps!=null&&month>=p.fee_change_month)bps=p.new_fee_bps;return base*bps/10000}
function feeModel(params){
  var p={},k;for(k in CDEF)p[k]=CDEF[k];for(k in params)if(k in CDEF)p[k]=params[k];
  var months=Math.max(1,Math.floor(p.months)),rm=Math.pow(1+p.annual_return_pct/100,1/12)-1,bal=0,rows=[];
  for(var m=1;m<=months;m++){var flow=0;
    if(m===1)flow+=p.size*p.funded_pct_initial/100;
    if(p.remaining_funded_month&&m===p.remaining_funded_month)flow+=p.size*(100-p.funded_pct_initial)/100;
    if(p.flow_month&&m===p.flow_month)flow+=p.flow_amount;
    if(p.monthly_flow&&p.monthly_flow_start&&m>=p.monthly_flow_start)flow+=p.monthly_flow;
    bal=Math.max(0,bal+flow);var base=p.fee_base==='committed'?p.size:bal;var fee=annualFee(base,p,m)/12;
    var row={month:m,flow:flow,start_balance:bal,fee_base:base,fee:fee};bal=bal*(1+rm);row.end_balance=bal;rows.push(row)}
  var years=[],total=0;
  for(var y=0;y<Math.ceil(months/12);y++){var ch=rows.slice(y*12,(y+1)*12),avg=0,fees=0;ch.forEach(function(r){avg+=r.fee_base;fees+=r.fee});avg/=ch.length;
    years.push({year:y+1,months:ch.length,avg_fee_base:avg,fees:fees,effective_bps_annualised:avg?fees/avg*10000*12/ch.length:null,end_balance:ch[ch.length-1].end_balance})}
  rows.forEach(function(r){total+=r.fee});
  return {params:p,rows:rows,years:years,total_fees:total}}
function trimNum(x,d){return x.toLocaleString('en-GB',{minimumFractionDigits:0,maximumFractionDigits:d})}
function money(x,cur){if(x==null)return 'n/a';cur=cur||'£';var neg=x<0;x=Math.abs(x);var s;
  if(x>=1e9)s=trimNum(x/1e9,3)+'bn';else if(x>=1e6)s=trimNum(x/1e6,3)+'m';else if(x>=1e3)s=trimNum(x/1e3,1)+'k';else s=trimNum(x,0);return (neg?'-':'')+cur+s}
window.__feeModel=feeModel;window.__cases=DATA.cases;

/* ---------- routing ---------- */
var chapters=$$('#chapters .chapter'),curCh=0,glossDone={};
function showView(name){
  VIEWS.forEach(function(v){var el=$('#view-'+v);if(el)el.hidden=(v!==name)});
  $$('nav.side a').forEach(function(a){if(a.getAttribute('href')==='#/'+name)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
  $('#sidenav').classList.remove('open');$('#menuBtn').setAttribute('aria-expanded','false')}
function showChapter(id,sec){
  var idx=0;chapters.forEach(function(c,i){if(c.dataset.chapter===id)idx=i});curCh=idx;
  chapters.forEach(function(c,i){c.hidden=(i!==idx)});
  $$('#chapterNav > li').forEach(function(li,i){li.classList.toggle('current',i===idx)});
  $('#prevCh').disabled=idx===0;$('#nextCh').disabled=idx===chapters.length-1;
  linkGlossary(chapters[idx]);
  var target=sec?document.getElementById(sec):null;
  if(target){target.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'})}else{window.scrollTo(0,0)}}
function focusCard(view,id){var el=document.getElementById(id);if(!el)return;
  var list=el.parentElement;$$('[data-filtered]',list).forEach(function(x){x.removeAttribute('data-filtered')});
  $$('.filters[data-filter-for="'+list.id+'"] select').forEach(function(s){s.value=''});
  el.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});el.setAttribute('tabindex','-1');el.focus({preventScroll:true})}
var firstRoute=true;
function route(){
  var initial=firstRoute;firstRoute=false;
  var h=location.hash||'#/home';
  if(h.indexOf('#/')!==0){ // plain anchor: source rows, headings
    var el=document.getElementById(decodeURIComponent(h.slice(1)));
    if(el){var v=el.closest('.view');if(v){showView(v.id.replace('view-',''));var ch=el.closest('.chapter');if(ch){showChapter(ch.dataset.chapter,el.id)}
      else{el.scrollIntoView({block:'center'});if(el.tagName==='TR'){el.style.outline='3px solid var(--focus)';setTimeout(function(){el.style.outline=''},2500)}}}}
    return}
  var parts=h.slice(2).split('/').map(decodeURIComponent),name=VIEWS.indexOf(parts[0])>=0?parts[0]:'home';
  showView(name);
  if(name==='read'){showChapter(parts[1]||(chapters[0]&&chapters[0].dataset.chapter),parts[2])}
  else if(name==='teams'){selectTeam(parts[1]||'')}
  else if(name==='search'){runSearch(parts.slice(1).join('/'))}
  else if(parts[1]){setTimeout(function(){focusCard(name,parts[1])},0)}
  else{window.scrollTo(0,0)}
  if(!initial&&!parts[1]&&name!=='search'){var m=$('#main');m.focus({preventScroll:true})}}
window.addEventListener('hashchange',route);
$('#prevCh').addEventListener('click',function(){if(curCh>0)location.hash='#/read/'+chapters[curCh-1].dataset.chapter});
$('#nextCh').addEventListener('click',function(){if(curCh<chapters.length-1)location.hash='#/read/'+chapters[curCh+1].dataset.chapter});
$('#menuBtn').addEventListener('click',function(){var n=$('#sidenav');var o=n.classList.toggle('open');this.setAttribute('aria-expanded',o?'true':'false')});

/* ---------- level + theme ---------- */
$$('[data-level]').forEach(function(b){b.addEventListener('click',function(){document.body.classList.remove('view-l1','view-l2','view-both');document.body.classList.add('view-'+b.dataset.level);
  $$('[data-level]').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')})})});
$('#themeBtn').addEventListener('click',function(){var r=document.documentElement,cur=r.getAttribute('data-theme');
  var dark=cur?cur==='dark':(window.matchMedia&&window.matchMedia('(prefers-color-scheme: dark)').matches);r.setAttribute('data-theme',dark?'light':'dark');drawCube()});

/* ---------- glossary popovers ---------- */
var G=DATA.glossary.filter(function(g){return g.term&&g.term.length>1}),gByKey={};
G.forEach(function(g){gByKey[g.term.toLowerCase()]=g});
var gRe=null;
function buildGRe(){var terms=G.map(function(g){return g.term}).sort(function(a,b){return b.length-a.length}).map(function(t){return t.replace(/[.*+?^${}()|[\]\\\/]/g,'\\$&')});
  if(!terms.length)return null;return new RegExp('(^|[^A-Za-z0-9])('+terms.join('|')+')(?![A-Za-z0-9])','g')}
function linkGlossary(ch){if(!ch||glossDone[ch.id]||!G.length)return;glossDone[ch.id]=true;if(!gRe)gRe=buildGRe();if(!gRe)return;
  var secs=$$('.sec',ch);if(!secs.length)secs=[ch];
  secs.forEach(function(sec){var seen={},w=document.createTreeWalker(sec,NodeFilter.SHOW_TEXT,{acceptNode:function(n){var p=n.parentElement;
      if(!p||p.closest('h1,h2,h3,h4,a,button,code,pre,summary,.badge,.layer,.cite,.box-title,th,caption'))return NodeFilter.FILTER_REJECT;return n.nodeValue.length>2?NodeFilter.FILTER_ACCEPT:NodeFilter.FILTER_REJECT}}),nodes=[],n;
    while((n=w.nextNode()))nodes.push(n);
    nodes.forEach(function(node){var text=node.nodeValue,m,last=0,frag=null;gRe.lastIndex=0;
      while((m=gRe.exec(text))){var term=m[2],key=term.toLowerCase(),g=gByKey[key];
        if(!g||seen[key]||(g.term===g.term.toUpperCase()&&term!==g.term)){gRe.lastIndex=m.index+m[0].length;continue}
        seen[key]=1;frag=frag||document.createDocumentFragment();var start=m.index+m[1].length;
        frag.appendChild(document.createTextNode(text.slice(last,start)));
        var b=document.createElement('button');b.type='button';b.className='g';b.dataset.g=g.id;b.textContent=term;b.setAttribute('aria-label',term+': show definition');frag.appendChild(b);last=start+term.length}
      if(frag){frag.appendChild(document.createTextNode(text.slice(last)));node.parentNode.replaceChild(frag,node)}})})}
var pop=$('#pop'),popFrom=null;
function closePop(){if(!pop.hidden){pop.hidden=true;if(popFrom)popFrom.focus();popFrom=null}}
document.addEventListener('click',function(e){var b=e.target.closest&&e.target.closest('button.g');
  if(b){var g=G.filter(function(x){return x.id===b.dataset.g})[0];if(!g)return;popFrom=b;
    pop.innerHTML='<strong>'+esc(g.term)+'</strong>'+(g.expansion&&g.expansion!==g.term?' · '+esc(g.expansion):'')+'<p>'+esc(g.plain||'')+'</p><p><a href="#/glossary/'+esc(g.id)+'">Open in glossary</a> <button type="button" id="popClose">Close</button></p>';
    pop.hidden=false;var r=b.getBoundingClientRect();pop.style.top=(window.scrollY+r.bottom+6)+'px';pop.style.left=Math.max(8,Math.min(window.scrollX+r.left,window.scrollX+document.documentElement.clientWidth-360))+'px';
    $('#popClose').focus();e.stopPropagation();return}
  if(e.target.id==='popClose'||(!pop.hidden&&!pop.contains(e.target))){var keep=e.target.id==='popClose';if(keep)closePop();else{pop.hidden=true;popFrom=null}}
  var a=e.target.closest&&e.target.closest('#pop a');if(a){pop.hidden=true;popFrom=null}});
document.addEventListener('keydown',function(e){
  if(e.key==='Escape'){closePop();$('#sidenav').classList.remove('open')}
  if(e.key==='/'&&!/INPUT|TEXTAREA|SELECT/.test(document.activeElement.tagName)){e.preventDefault();$('#q').focus()}});
$('#gq').addEventListener('input',function(){var q=this.value.trim().toLowerCase(),n=0;$$('#glossList .gloss').forEach(function(c){var hit=!q||c.textContent.toLowerCase().indexOf(q)>=0;if(hit){c.removeAttribute('data-filtered');n++}else c.setAttribute('data-filtered','out')});
  $('#gCount').textContent=n+' terms shown'});
$('#gCount').textContent=$$('#glossList .gloss').length+' terms';

/* ---------- search ---------- */
var index=null;
function buildIndex(){index=[];$$('[data-search]').forEach(function(el){var view=el.closest('.view');if(!view)return;var v=view.id.replace('view-','');
  var t=$('h2,h3,h4,.card-title',el),title=t?t.textContent.trim():(el.cells?el.cells[0].textContent.trim().slice(0,90):''),href;
  if(el.dataset.kind==='chapter'){var ch=el.closest('.chapter');href='#/read/'+ch.dataset.chapter+'/'+el.dataset.sec;title=($('h1',ch)?$('h1',ch).textContent+' › ':'')+title}
  else if(el.id&&el.id.indexOf('src-')===0){href='#'+el.id;title=el.cells[1].textContent.trim().slice(0,110)}
  else if(el.id){href=(v==='sources'||el.closest('.chapter'))?'#'+el.id:'#/'+v+'/'+el.id}
  else href='#/'+v;
  if(el.dataset.kind==='team-card'||el.classList.contains('team-card'))href='#/teams/'+el.id;
  var text=el.textContent.replace(/\s+/g,' ');index.push({kind:el.dataset.kind||v,title:title,text:text,low:text.toLowerCase(),tlow:title.toLowerCase(),href:href})})}
var KIND={chapter:'Dossier',person:'Person','card person':'Person',glossary:'Glossary',source:'Source',claim:'Claim','claim-audit':'Intern-claim audit',interview:'Interview question','practice-case':'Practice case','why-tree':'Why-tree','fee-case':'Fee case',coverage:'Coverage register',personal:'Personal ledger'};
function kindLabel(k){if(KIND[k])return KIND[k];if(/team/.test(k))return 'Team';if(/person/.test(k))return 'Person';if(/mandate/.test(k))return 'Mandate';if(/dev/.test(k))return 'Awareness card';if(/comp/.test(k))return 'Competitor';if(/role/.test(k))return 'Role';if(/stage/.test(k))return 'Lifecycle stage';if(/gloss/.test(k))return 'Glossary';return 'Item'}
function runSearch(q){if(!index)buildIndex();q=(q||'').trim();$('#q').value=q;var out=$('#searchResults');out.innerHTML='';
  var toks=q.toLowerCase().split(/\s+/).filter(Boolean);if(!toks.length){$('#searchSummary').textContent='Type in the search box to search every chapter, team, person, mandate, glossary entry, claim and source.';return}
  var hits=[];index.forEach(function(it){var score=0;for(var i=0;i<toks.length;i++){var t=toks[i],c=it.low.split(t).length-1;if(!c)return;score+=Math.min(c,8)+(it.tlow.indexOf(t)>=0?12:0)}
    if(it.kind==='glossary'&&it.tlow.indexOf(toks[0])===0)score+=20;hits.push({it:it,score:score})});
  hits.sort(function(a,b){return b.score-a.score});
  $('#searchSummary').textContent=hits.length+' result'+(hits.length===1?'':'s')+' for "'+q+'"'+(hits.length>80?' (showing the first 80)':'');
  hits.slice(0,80).forEach(function(h){var it=h.it,pos=it.low.indexOf(toks[0]),s=Math.max(0,pos-70),snip=esc(it.text.slice(s,s+230));
    toks.forEach(function(t){snip=snip.replace(new RegExp('('+t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+')','ig'),'<mark>$1</mark>')});
    var li=document.createElement('li');li.innerHTML='<a href="'+esc(it.href)+'"><strong>'+esc(it.title||'(untitled)')+'</strong></a> <span class="badge badge-x">'+esc(kindLabel(it.kind))+'</span><div class="muted">'+(s>0?'… ':'')+snip+' …</div>';out.appendChild(li)})}
var qTimer;$('#q').addEventListener('input',function(){var v=this.value;clearTimeout(qTimer);qTimer=setTimeout(function(){if(v.trim().length>1){var nh='#/search/'+encodeURIComponent(v.trim());if(location.hash.indexOf('#/search')===0)history.replaceState(null,'',nh),route();else location.hash=nh}},220)});
$('#q').addEventListener('keydown',function(e){if(e.key==='Enter'){clearTimeout(qTimer);location.hash='#/search/'+encodeURIComponent(this.value.trim())}});

/* ---------- generic filters ---------- */
$$('.filters[data-filter-for]').forEach(function(bar){var list=document.getElementById(bar.dataset.filterFor);if(!list)return;
  var rowsSel=bar.dataset.filterRows,items=rowsSel?$$(rowsSel,list):$$(':scope > .card',list),keys=bar.dataset.filterKeys.split(','),sels=[];
  var count=document.createElement('span');count.className='count';count.setAttribute('role','status');
  keys.forEach(function(k){var vals={};items.forEach(function(it){(it.getAttribute('data-'+k)||'').split('|').forEach(function(v){v=v.trim();if(v)vals[v]=(vals[v]||0)+1})});
    var names=Object.keys(vals).sort();if(names.length<2)return;var lab=document.createElement('label'),sel=document.createElement('select');
    lab.textContent=k.replace(/-/g,' ').replace(/^./,function(c){return c.toUpperCase()})+' ';sel.dataset.key=k;sel.innerHTML='<option value="">All</option>'+names.map(function(n){return '<option value="'+esc(n)+'">'+esc(n)+' ('+vals[n]+')</option>'}).join('');
    lab.appendChild(sel);bar.appendChild(lab);sels.push(sel);sel.addEventListener('change',apply)});
  var reset=document.createElement('button');reset.type='button';reset.textContent='Clear filters';reset.addEventListener('click',function(){sels.forEach(function(s){s.value=''});apply()});
  if(sels.length)bar.appendChild(reset);bar.appendChild(count);
  function apply(){var n=0;items.forEach(function(it){var ok=sels.every(function(s){if(!s.value)return true;return (it.getAttribute('data-'+s.dataset.key)||'').split('|').map(function(x){return x.trim()}).indexOf(s.value)>=0});
    if(ok){it.removeAttribute('data-filtered');n++}else it.setAttribute('data-filtered','out')});count.textContent=n+' of '+items.length+' shown'}
  apply()});

/* ---------- teams ---------- */
var teamSel=$('#teamSel');DATA.teams.forEach(function(t){var o=document.createElement('option');o.value=t.id;o.textContent=t.name;teamSel.appendChild(o)});
function selectTeam(id){teamSel.value=id||'';var found=false;$$('#teamPanel .team-card').forEach(function(c){var show=!id||c.id===id;c.hidden=!show;if(show&&id)found=c});
  if(found){$('#team-detail-h').scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});found.setAttribute('tabindex','-1');found.focus({preventScroll:true})}}
teamSel.addEventListener('change',function(){location.hash='#/teams'+(this.value?'/'+this.value:'')});
var tabs=$$('[role=tab]');
function selTab(t){tabs.forEach(function(x){var on=x===t;x.setAttribute('aria-selected',on?'true':'false');x.tabIndex=on?0:-1;$('#pane-'+x.dataset.pane).hidden=!on});if(t.dataset.pane==='cube')drawCube()}
tabs.forEach(function(t,i){t.addEventListener('click',function(){selTab(t)});t.addEventListener('keydown',function(e){var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(d){var n=tabs[(i+d+tabs.length)%tabs.length];selTab(n);n.focus()}})});

/* ---------- optional 3D explorer: the matrix as a cube ---------- */
var cube=$('#cube'),ang={x:-0.45,y:0.6},pts=[];
(function(){var geos=DATA.axes.geographies||[],segs=DATA.axes.segments||[],fns=DATA.axes.functions||[];if(!fns.length)fns=['All functions'];
  var tn={};DATA.teams.forEach(function(t){tn[t.id]=t.name});var list=$('#cubeList');
  (DATA.matrix||[]).forEach(function(c){var gi=geos.map(function(g){return g.id}).indexOf(c.geo),si=segs.map(function(s){return s.id}).indexOf(c.segment);if(gi<0||si<0)return;
    fns.forEach(function(f,fi){pts.push({x:gi,y:si,z:fi,status:c.status,team:c.team,label:geos[gi].name+' · '+segs[si].name+' · '+f})});
    var li=document.createElement('li');li.innerHTML=(c.team?'<a href="#/teams/'+esc(c.team)+'">'+esc(geos[gi].name+' · '+segs[si].name)+'</a>':esc(geos[gi].name+' · '+segs[si].name))+' — '+esc(c.status||'');list.appendChild(li)});
  cube._dims=[Math.max(1,geos.length-1),Math.max(1,segs.length-1),Math.max(1,fns.length-1)];cube._axes=[geos.map(function(g){return g.name}),segs.map(function(s){return s.name}),fns]})();
function proj(x,y,z,W,H){var d=cube._dims,px=(x/d[0]-.5)*2,py=(y/d[1]-.5)*-1.5,pz=(z/d[2]-.5)*1.1;
  var cy=Math.cos(ang.y),sy=Math.sin(ang.y),cx=Math.cos(ang.x),sx=Math.sin(ang.x);var x1=px*cy+pz*sy,z1=-px*sy+pz*cy,y1=py*cx-z1*sx,z2=py*sx+z1*cx;var s=3.2/(4+z2);
  return {x:W/2+x1*s*W*.3,y:H/2+y1*s*H*.42,z:z2,s:s}}
function drawCube(){if(!cube||$('#pane-cube').hidden)return;var dpr=window.devicePixelRatio||1,W=cube.clientWidth,H=cube.clientHeight;cube.width=W*dpr;cube.height=H*dpr;var c=cube.getContext('2d');c.scale(dpr,dpr);
  var cs=getComputedStyle(document.documentElement),ink=cs.getPropertyValue('--ink').trim(),muted=cs.getPropertyValue('--muted').trim(),line=cs.getPropertyValue('--line').trim(),acc=cs.getPropertyValue('--accent').trim();
  c.clearRect(0,0,W,H);c.font='12px sans-serif';if(!pts.length){c.fillStyle=muted;c.fillText('No matrix cells to show.',20,30);return}
  var d=cube._dims,ax=cube._axes;c.strokeStyle=line;c.lineWidth=1;
  [[0,0,0,d[0],0,0],[0,0,0,0,d[1],0],[0,0,0,0,0,d[2]],[d[0],0,0,d[0],d[1],0],[0,d[1],0,d[0],d[1],0],[0,0,d[2],d[0],0,d[2]],[0,0,d[2],0,d[1],d[2]],[d[0],0,d[2],d[0],d[1],d[2]],[0,d[1],d[2],d[0],d[1],d[2]],[d[0],0,0,d[0],0,d[2]],[0,d[1],0,0,d[1],d[2]],[d[0],d[1],0,d[0],d[1],d[2]]].forEach(function(e){var a=proj(e[0],e[1],e[2],W,H),b=proj(e[3],e[4],e[5],W,H);c.beginPath();c.moveTo(a.x,a.y);c.lineTo(b.x,b.y);c.stroke()});
  c.fillStyle=muted;ax[0].forEach(function(n,i){var p=proj(i,-0.35,0,W,H);c.fillText(n,p.x-14,p.y+14)});ax[1].forEach(function(n,i){var p=proj(-0.5,i,0,W,H);c.fillText(n,Math.max(2,p.x-70),p.y+4)});ax[2].forEach(function(n,i){var p=proj(d[0]+.25,0,i,W,H);c.fillText(n,p.x+6,p.y+4)});
  pts.map(function(p){var q=proj(p.x,p.y,p.z,W,H);q.p=p;return q}).sort(function(a,b){return b.z-a.z}).forEach(function(q){var r=6*q.s+2,st=q.p.status||'';p_draw(c,q.x,q.y,r,st,ink,acc,muted);q.p._sx=q.x;q.p._sy=q.y});
  c.fillStyle=muted;c.fillText('Filled circle = Verified · ring = Unverified account · square = Supported inference · cross = Not publicly established · diamond = Conflicting',10,H-10)}
function p_draw(c,x,y,r,st,ink,acc,muted){c.lineWidth=2;c.strokeStyle=ink;c.fillStyle=acc;c.beginPath();
  if(st==='Verified'){c.arc(x,y,r,0,7);c.fill();c.stroke()}
  else if(st==='Supported inference'){c.rect(x-r,y-r,2*r,2*r);c.fill();c.stroke()}
  else if(st==='Conflicting evidence'){c.moveTo(x,y-r*1.3);c.lineTo(x+r*1.3,y);c.lineTo(x,y+r*1.3);c.lineTo(x-r*1.3,y);c.closePath();c.stroke()}
  else if(st==='Not publicly established'){c.strokeStyle=muted;c.moveTo(x-r,y-r);c.lineTo(x+r,y+r);c.moveTo(x+r,y-r);c.lineTo(x-r,y+r);c.stroke()}
  else{c.arc(x,y,r,0,7);c.stroke()}}
if(cube){var drag=null;cube.addEventListener('pointerdown',function(e){drag={x:e.clientX,y:e.clientY,ax:ang.x,ay:ang.y,moved:false};cube.setPointerCapture(e.pointerId)});
  cube.addEventListener('pointermove',function(e){if(!drag)return;var dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>3)drag.moved=true;ang.y=drag.ay+dx*.008;ang.x=Math.max(-1.4,Math.min(1.4,drag.ax+dy*.008));drawCube()});
  cube.addEventListener('pointerup',function(e){if(drag&&!drag.moved){var r=cube.getBoundingClientRect(),mx=e.clientX-r.left,my=e.clientY-r.top,best=null,bd=18;pts.forEach(function(p){var dd=Math.hypot(p._sx-mx,p._sy-my);if(dd<bd){bd=dd;best=p}});if(best&&best.team)location.hash='#/teams/'+best.team}drag=null});
  cube.addEventListener('keydown',function(e){var k={ArrowLeft:[0,-.12],ArrowRight:[0,.12],ArrowUp:[-.12,0],ArrowDown:[.12,0]}[e.key];if(k){e.preventDefault();ang.x=Math.max(-1.4,Math.min(1.4,ang.x+k[0]));ang.y+=k[1];drawCube()}});
  window.addEventListener('resize',drawCube)}

/* ---------- role comparison ---------- */
var roles=$$('#roleList .role').map(function(c){var rows={};$$(':scope > dl.kv > dt',c).forEach(function(dt){rows[dt.textContent]=dt.nextElementSibling.innerHTML});return {id:c.id,name:$('.card-title',c).textContent,rows:rows}});
function renderRoles(){var pick=['roleA','roleB','roleC'].map(function(i){return roles.filter(function(r){return r.id===$('#'+i).value})[0]}).filter(Boolean),box=$('#roleCompare');
  if(pick.length<2){box.innerHTML='<p class="na">Choose at least two roles.</p>';return}var keys=[];pick.forEach(function(r){Object.keys(r.rows).forEach(function(k){if(keys.indexOf(k)<0)keys.push(k)})});
  box.innerHTML='<table><caption>Side-by-side comparison (general industry practice; real teams overlap)</caption><thead><tr><th scope="col">Dimension</th>'+pick.map(function(r){return '<th scope="col">'+esc(r.name)+'</th>'}).join('')+'</tr></thead><tbody>'+
    keys.map(function(k){return '<tr><th scope="row">'+esc(k)+'</th>'+pick.map(function(r){return '<td>'+(r.rows[k]||'<span class="na">Not described</span>')+'</td>'}).join('')+'</tr>'}).join('')+'</tbody></table>'}
$$('.roleSel').forEach(function(s,i){s.innerHTML=(i===2?'<option value="">None</option>':'')+roles.map(function(r){return '<option value="'+esc(r.id)+'">'+esc(r.name)+'</option>'}).join('');s.addEventListener('change',renderRoles)});
(function(){var f=function(re){var r=roles.filter(function(x){return re.test(x.name)})[0];return r?r.id:''};var a=f(/institutional sales/i)||(roles[0]&&roles[0].id),b=f(/institutional (rm|relationship)/i)||(roles[1]&&roles[1].id);
  if(roles.length){$('#roleA').value=a;$('#roleB').value=b;renderRoles()}else $('#roleCompare').innerHTML='<p class="na">No role cards loaded.</p>'})();

/* ---------- lifecycle ---------- */
var path='inst',stageIdx=0,showAll=false;
function stages(){return $$('#stages-'+path+' .stage')}
function renderStages(){var st=stages(),sp=$('#stepper');sp.innerHTML='';$('#stages-inst').hidden=path!=='inst';$('#stages-tpw').hidden=path!=='tpw';if(stageIdx>=st.length)stageIdx=0;
  st.forEach(function(s,i){s.hidden=!showAll&&i!==stageIdx;var li=document.createElement('li'),b=document.createElement('button');b.type='button';b.textContent=$('.card-title',s).textContent;b.setAttribute('aria-pressed',(!showAll&&i===stageIdx)?'true':'false');
    b.addEventListener('click',function(){showAll=false;$('#allStages').setAttribute('aria-pressed','false');stageIdx=i;renderStages()});li.appendChild(b);sp.appendChild(li)});
  $('#prevStage').disabled=showAll||stageIdx===0;$('#nextStage').disabled=showAll||stageIdx>=st.length-1}
$$('[data-path]').forEach(function(b){b.addEventListener('click',function(){path=b.dataset.path;stageIdx=0;$$('[data-path]').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});renderStages()})});
$('#prevStage').addEventListener('click',function(){if(stageIdx>0){stageIdx--;renderStages()}});
$('#nextStage').addEventListener('click',function(){if(stageIdx<stages().length-1){stageIdx++;renderStages()}});
$('#allStages').addEventListener('click',function(){showAll=!showAll;this.setAttribute('aria-pressed',showAll?'true':'false');renderStages()});
renderStages();

/* ---------- calculator ---------- */
var num=function(id){var v=$('#'+id).value;return v===''?null:Number(v)};
function readCalc(){var p={size:num('c_size')||0,funded_pct_initial:num('c_funded')==null?100:num('c_funded'),remaining_funded_month:num('c_remmonth'),annual_return_pct:num('c_ret')||0,months:Math.min(120,Math.max(1,num('c_months')||12)),
  flow_amount:num('c_flow')||0,flow_month:num('c_flowmonth'),monthly_flow:num('c_mflow')||0,monthly_flow_start:num('c_mflowstart'),fee_base:$('#c_base').value,fee_mode:$('#c_mode').value,fee_bps:num('c_bps')||0,fee_change_month:num('c_chgmonth'),new_fee_bps:num('c_newbps'),tiers:[]};
  if(p.fee_mode==='tiered'){[['t1u','t1b'],['t2u','t2b'],['t3u','t3b']].forEach(function(t){var b=num(t[1]);if(b!=null)p.tiers.push({upto:num(t[0]),bps:b})});
    for(var i=0;i<p.tiers.length;i++)if(p.tiers[i].upto==null){p.tiers=p.tiers.slice(0,i+1);break}}
  return p}
function writeCalc(p){var q={},k;for(k in CDEF)q[k]=CDEF[k];for(k in p)q[k]=p[k];var set=function(id,v){$('#'+id).value=(v==null?'':v)};
  set('c_size',q.size);set('c_funded',q.funded_pct_initial);set('c_remmonth',q.remaining_funded_month);set('c_ret',q.annual_return_pct);set('c_months',q.months);set('c_flow',q.flow_amount);set('c_flowmonth',q.flow_month);set('c_mflow',q.monthly_flow);set('c_mflowstart',q.monthly_flow_start);
  $('#c_base').value=q.fee_base;$('#c_mode').value=q.fee_mode;set('c_bps',q.fee_bps);set('c_chgmonth',q.fee_change_month);set('c_newbps',q.new_fee_bps);
  var t=q.tiers||[];[['t1u','t1b'],['t2u','t2b'],['t3u','t3b']].forEach(function(ids,i){set(ids[0],t[i]?t[i].upto:null);set(ids[1],t[i]?t[i].bps:null)})}
function runCalc(){var p=readCalc(),r=feeModel(p);$('#tierBox').hidden=p.fee_mode!=='tiered';$('#calcTotal').textContent=money(r.total_fees);
  var y1=r.years[0],f='';
  if(p.fee_mode==='flat'){f+='Fee for a month = fee base × rate ÷ 12\nRate = '+p.fee_bps+'bp = '+(p.fee_bps/100).toFixed(4).replace(/0+$/,'').replace(/\.$/,'')+'% a year'+(p.fee_change_month&&p.new_fee_bps!=null?' (then '+p.new_fee_bps+'bp from month '+p.fee_change_month+')':'')+'\n'}
  else{f+='Annual fee = sum over tiers of (slice of fee base × tier rate)\n'+p.tiers.map(function(t,i){return '  Tier '+(i+1)+': '+(t.upto==null?'everything above':'up to '+money(t.upto))+' at '+t.bps+'bp'}).join('\n')+'\n'}
  f+='Fee base = '+(p.fee_base==='committed'?'committed capital of '+money(p.size)+' (does not move with markets or drawdowns)':'market value of the assets each month')+'\n';
  f+='Year 1: average fee base '+money(y1.avg_fee_base)+' → fee '+money(y1.fees)+(y1.effective_bps_annualised==null?'':' (effective '+y1.effective_bps_annualised.toFixed(1)+'bp a year)')+'\n';
  f+='Month 1 check: '+money(r.rows[0].fee_base)+' fee base → '+money(r.rows[0].fee)+' for the month';
  $('#calcFormula').textContent=f;
  $('#calcYears tbody').innerHTML=r.years.map(function(y){return '<tr><td>Year '+y.year+(y.months===12?'':' ('+y.months+' months)')+'</td><td>'+money(y.avg_fee_base)+'</td><td>'+money(y.fees)+'</td><td>'+(y.effective_bps_annualised==null?'n/a (no fee-bearing assets)':y.effective_bps_annualised.toFixed(1)+'bp')+'</td><td>'+money(y.end_balance)+'</td></tr>'}).join('');
  $('#calcMonths tbody').innerHTML=r.rows.map(function(m){return '<tr><td>'+m.month+'</td><td>'+(m.flow?money(m.flow):'none')+'</td><td>'+money(m.start_balance)+'</td><td>'+money(m.fee_base)+'</td><td>'+money(m.fee)+'</td><td>'+money(m.end_balance)+'</td></tr>'}).join('');
  return r}
var caseSel=$('#caseSel'),lastGroup='',og=null;DATA.cases.forEach(function(c){if(c.group!==lastGroup){og=document.createElement('optgroup');og.label=c.group;caseSel.appendChild(og);lastGroup=c.group}var o=document.createElement('option');o.value=c.id;o.textContent=c.title;og.appendChild(o)});
caseSel.addEventListener('change',function(){var c=DATA.cases.filter(function(x){return x.id===caseSel.value})[0];if(c){writeCalc(c.params);$('#caseTeach').textContent=c.teaches}else $('#caseTeach').textContent='';runCalc()});
$$('#calcForm input,#calcForm select').forEach(function(i){i.addEventListener('input',function(){if(caseSel.value){caseSel.value='';$('#caseTeach').textContent=''}runCalc()})});
runCalc();

/* ---------- why-trees ---------- */
$('#whyOpen').addEventListener('click',function(){$$('#whyList details').forEach(function(d){d.open=true})});
$('#whyClose').addEventListener('click',function(){$$('#whyList details').forEach(function(d){d.open=false})});
$$('.why-node').forEach(function(n){n.style.setProperty('--d',n.dataset.depth)});

/* ---------- practice ---------- */
var QS=$$('#qList .iq').map(function(c){return {id:c.id,cat:c.dataset.category,q:$('.card-title',c).textContent,el:c}}),used=[],curQ=null,tStart=0,tInt=null,elapsed=0;
var CRIT=(DATA.criteria&&DATA.criteria.length)?DATA.criteria.map(function(c){return c.name}):['Accuracy','Specificity','Logic','Judgement','Clarity','Supported personal evidence'];
(function(){var cats={};QS.forEach(function(q){cats[q.cat]=1});Object.keys(cats).sort().forEach(function(c){var o=document.createElement('option');o.value=c;o.textContent=c;$('#pCat').appendChild(o)});
  $('#pScores').innerHTML=CRIT.map(function(c,i){return '<label>'+esc(c)+' <select data-crit="'+i+'" aria-label="'+esc(c)+' score"><option value="">–</option><option>0</option><option>1</option><option>2</option><option>3</option></select></label>'}).join('')})();
function fmt(s){return Math.floor(s/60)+':'+('0'+(s%60)).slice(-2)}
function stopTimer(){if(tInt){clearInterval(tInt);tInt=null}}
$('#pNext').addEventListener('click',function(){var cat=$('#pCat').value,pool=QS.filter(function(q){return (!cat||q.cat===cat)&&used.indexOf(q.id)<0});
  if(!pool.length){used=[];pool=QS.filter(function(q){return !cat||q.cat===cat})}if(!pool.length){toast('No questions in this set yet.');return}
  curQ=pool[Math.floor(Math.random()*pool.length)];used.push(curQ.id);stopTimer();elapsed=0;$('#pTimer').textContent='0:00';$('#pTimeMsg').textContent='';$('#pSaved').textContent='';
  $('#pCard').hidden=false;$('#pMeta').textContent=curQ.cat+' · '+curQ.id;$('#pQ').textContent=curQ.q;$('#pAnswer').hidden=true;$('#pAnswer').innerHTML='';$$('#pScores select').forEach(function(s){s.value=''});$('#pQ').focus()});
$('#pStart').addEventListener('click',function(){stopTimer();var target=Number($('#pLen').value);tStart=Date.now()-elapsed*1000;$('#pTimeMsg').textContent='Timing. Target '+fmt(target)+'.';
  tInt=setInterval(function(){elapsed=Math.floor((Date.now()-tStart)/1000);$('#pTimer').textContent=fmt(elapsed);if(elapsed===target)$('#pTimeMsg').textContent='Target time reached. Finish your sentence.';if(elapsed>=target+60){stopTimer();$('#pTimeMsg').textContent='Stopped a minute past the target.'}},250)});
$('#pStop').addEventListener('click',function(){stopTimer();$('#pTimeMsg').textContent='Stopped at '+fmt(elapsed)+'.'});
$('#pReveal').addEventListener('click',function(){if(!curQ)return;var box=$('#pAnswer');box.innerHTML='';$$(':scope > details',curQ.el).forEach(function(d){var c=d.cloneNode(true);c.open=true;box.appendChild(c)});box.hidden=false});
function renderHistory(){var h=store.history,box=$('#pHistory');if(!h.length){box.innerHTML='';return}
  box.innerHTML='<h3>Attempts this '+(store.save?'device':'session')+'</h3><div class="table-wrap"><table><thead><tr><th>Question</th><th>Time</th>'+CRIT.map(function(c){return '<th>'+esc(c)+'</th>'}).join('')+'<th>Total</th></tr></thead><tbody>'+
  h.slice().reverse().map(function(a){return '<tr><td>'+esc(a.q)+'</td><td>'+fmt(a.t)+'</td>'+a.s.map(function(v){return '<td>'+(v==null?'–':v)+'</td>'}).join('')+'<td>'+a.s.reduce(function(x,y){return x+(y||0)},0)+' / '+(CRIT.length*3)+'</td></tr>'}).join('')+'</tbody></table></div>'}
$('#pSave').addEventListener('click',function(){if(!curQ)return;stopTimer();var s=$$('#pScores select').map(function(x){return x.value===''?null:Number(x.value)});
  store.history.push({id:curQ.id,q:curQ.q,t:elapsed,s:s});lsSet();renderHistory();$('#pSaved').textContent=store.save?'Recorded and saved on this device.':'Recorded for this session only.'});
renderHistory();

/* ---------- progress controls ---------- */
var saveToggle=$('#saveToggle');saveToggle.checked=!!store.save;
function syncSteps(){$$('.route-step').forEach(function(c){c.checked=!!store.steps[c.dataset.step]})}
syncSteps();
$$('.route-step').forEach(function(c){c.addEventListener('change',function(){store.steps[c.dataset.step]=c.checked;lsSet()})});
saveToggle.addEventListener('change',function(){store.save=saveToggle.checked;if(store.save){lsSet();$('#saveState').textContent='Saving in this browser only. Untick or reset to remove it.'}else{lsClear();$('#saveState').textContent='Saving is off. Saved data has been removed from this browser.'}renderHistory()});
$('#resetBtn').addEventListener('click',function(){store={save:saveToggle.checked,steps:{},history:[]};lsClear();lsSet();syncSteps();renderHistory();toast('Progress reset.')});
if(store.save)$('#saveState').textContent='Saving in this browser only. Untick or reset to remove it.';

route();
})();
