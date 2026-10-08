"""Small inline-SVG helper library for the interview pack."""
import html as _h

NAVY="#14213D"; NAVY2="#22335A"; ACC="#D9822B"; ACCS="#FBEBDD"; SIG="#7A3FB0"; SIGS="#F1E8FA"
GRN="#2E8B57"; GRNS="#E3F3EA"; AMB="#C99A06"; AMBS="#FBF3D6"; RED="#C0392B"; REDS="#FBE4E1"
BLU="#2F6DB5"; BLUS="#E4EEF9"; GREY="#5B6475"; LINE="#D9DDE5"; TINT="#F5F6F9"; WHITE="#FFFFFF"

def esc(s): return _h.escape(str(s), quote=True)

def wrap(text, maxw, fs):
    cw = fs*0.54
    maxc = max(4, int(maxw/cw))
    out=[]
    for para in str(text).split("\n"):
        words=para.split(" "); line=""
        for w in words:
            t=(line+" "+w).strip()
            if len(t)<=maxc: line=t
            else:
                if line: out.append(line)
                line=w
        out.append(line)
    return out

def text(x,y,s,fs=11,fill=NAVY,anchor="start",weight=400,maxw=None,lh=1.22,italic=False):
    lines = wrap(s,maxw,fs) if maxw else str(s).split("\n")
    st=' font-style="italic"' if italic else ''
    r=[]
    for i,l in enumerate(lines):
        r.append(f'<text x="{x}" y="{y+i*fs*lh:.1f}" font-size="{fs}" fill="{fill}" text-anchor="{anchor}" font-weight="{weight}"{st}>{esc(l)}</text>')
    return "".join(r)

def box(x,y,w,h,label="",fill=BLUS,stroke=NAVY,tc=NAVY,fs=11,weight=600,rx=6,sub=None,subfs=None,dash=False,sw=1.2,align="middle"):
    d=' stroke-dasharray="5 3"' if dash else ''
    s=f'<g class="bx"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    pad=8
    lines=wrap(label,w-2*pad,fs) if label else []
    sl=wrap(sub,w-2*pad,subfs or fs*0.82) if sub else []
    sfs=subfs or fs*0.82
    total=len(lines)*fs*1.2+len(sl)*sfs*1.22+(3 if sl and lines else 0)
    yy=y+h/2-total/2+fs*0.92
    ax = x+w/2 if align=="middle" else x+pad
    anchor = "middle" if align=="middle" else "start"
    for l in lines:
        s+=f'<text x="{ax}" y="{yy:.1f}" font-size="{fs}" fill="{tc}" text-anchor="{anchor}" font-weight="{weight}">{esc(l)}</text>'; yy+=fs*1.2
    if sl: yy+=3-fs*1.2+sfs*1.0+ (fs*1.2-sfs*1.0 if lines else 0)
    for l in sl:
        s+=f'<text x="{ax}" y="{yy:.1f}" font-size="{sfs:.1f}" fill="{tc}" text-anchor="{anchor}" font-weight="400" opacity="0.9">{esc(l)}</text>'; yy+=sfs*1.22
    return s+'</g>'

def arrow(x1,y1,x2,y2,color=GREY,sw=1.6,label=None,fs=9.5,dash=False,lc=None,loff=(0,-5),head=True,both=False):
    d=' stroke-dasharray="5 3"' if dash else ''
    mid=color.replace("#","")
    me=f' marker-end="url(#ah{mid})"' if head else ''
    ms=f' marker-start="url(#as{mid})"' if both else ''
    s=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"{d}{me}{ms}/>'
    if label:
        mx=(x1+x2)/2+loff[0]; my=(y1+y2)/2+loff[1]
        s+=f'<text x="{mx}" y="{my}" font-size="{fs}" fill="{lc or color}" text-anchor="middle" font-weight="600">{esc(label)}</text>'
    return s

def path_arrow(d,color=GREY,sw=1.6,dash=False):
    mid=color.replace("#","")
    da=' stroke-dasharray="5 3"' if dash else ''
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{da} marker-end="url(#ah{mid})"/>'

def defs():
    cols=[NAVY,GREY,ACC,SIG,GRN,RED,BLU,AMB,WHITE,NAVY2]
    m=""
    for c in cols:
        i=c.replace("#","")
        m+=f'<marker id="ah{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        m+=f'<marker id="as{i}" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
    return f'<defs>{m}</defs>'

def svg(w,h,body,title=None):
    t=f'<title>{esc(title)}</title>' if title else ''
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" role="img">{t}{defs()}{body}</svg>'

def hbar(data,w=760,barh=22,gap=10,labw=210,unit="",title=None,maxv=None,color=NAVY,hl=None,hlcolor=ACC,valfmt="{:,.0f}",note_w=0):
    """data: list of (label, value, est_flag, note)"""
    top=30 if title else 8
    h=top+len(data)*(barh+gap)+16
    maxv=maxv or max(d[1] for d in data if d[1] is not None)*1.1
    plotw=w-labw-90-note_w
    s=""
    if title: s+=text(0,18,title,13,NAVY,weight=700)
    for i,d in enumerate(data):
        lab,v=d[0],d[1]; est=d[2] if len(d)>2 else False; note=d[3] if len(d)>3 else ""
        y=top+i*(barh+gap)
        c=hlcolor if (hl and lab in hl) else color
        s+=text(labw-8,y+barh*0.68,lab,10.5,NAVY,"end",600 if (hl and lab in hl) else 400)
        if v is None:
            s+=text(labw+4,y+barh*0.68,"not disclosed",9.5,GREY,italic=True)
            continue
        bw=max(2,plotw*v/maxv)
        s+=f'<rect x="{labw}" y="{y}" width="{bw:.1f}" height="{barh}" rx="3" fill="{c}" {"fill-opacity=\"0.55\" stroke=\""+c+"\" stroke-dasharray=\"4 2\"" if est else ""}/>'
        vs=valfmt.format(v)+unit+(" (est.)" if est else "")
        s+=text(labw+bw+5,y+barh*0.68,vs,10,NAVY,weight=700)
        if note: s+=text(w-note_w,y+barh*0.68,note,8.5,GREY)
    return svg(w,h,s)

def timeline(events,w=760,title=None,color=NAVY,rowh=None,label_w=150):
    """events: list of (date_label, text, highlight_bool). vertical timeline"""
    top=30 if title else 10
    s=text(0,18,title,13,NAVY,weight=700) if title else ""
    y=top; x0=label_w
    rows=[]
    for e in events:
        lines=wrap(e[1],w-x0-30,10)
        hh=max(24,len(lines)*12.5+10)
        rows.append((e,lines,hh))
    total=sum(r[2] for r in rows)
    s+=f'<line x1="{x0}" y1="{top}" x2="{x0}" y2="{top+total}" stroke="{LINE}" stroke-width="3"/>'
    for e,lines,hh in rows:
        hl=e[2] if len(e)>2 else False
        c=ACC if hl else color
        s+=f'<circle cx="{x0}" cy="{y+10}" r="6" fill="{c}" stroke="#fff" stroke-width="2"/>'
        s+=text(x0-14,y+14,e[0],10,c,"end",700)
        for i,l in enumerate(lines):
            s+=f'<text x="{x0+16}" y="{y+14+i*12.5}" font-size="10" fill="{NAVY}" font-weight="{600 if hl else 400}">{esc(l)}</text>'
        y+=hh
    return svg(w,top+total+6,s)

def spectrum(axes,w=760,title=None,firms_hl=("Mayer Brown",)):
    """axes: list of (left_label,right_label,[(name,pos0to1)])"""
    top=30 if title else 6
    rowh=70
    s=text(0,18,title,13,NAVY,weight=700) if title else ""
    x0,x1=150,w-150
    for i,(l,r,pts) in enumerate(axes):
        y=top+i*rowh+34
        s+=text(x0-12,y+4,l,9.5,GREY,"end",600,maxw=140)
        s+=text(x1+12,y+4,r,9.5,GREY,"start",600,maxw=138)
        s+=f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="4" stroke-linecap="round"/>'
        placed=[]
        for j,(n,p) in enumerate(sorted(pts,key=lambda t:t[1])):
            x=x0+(x1-x0)*p
            hl=n in firms_hl
            lvl=0
            while any(abs(x-px)<62 and pl==lvl for px,pl in placed): lvl+=1
            placed.append((x,lvl))
            ly=y-10-lvl*11 if lvl%2==0 else y+18+(lvl//2)*11
            ly = y-10-(lvl//2)*11 if lvl%2==0 else y+19+(lvl//2)*11
            s+=f'<circle cx="{x:.1f}" cy="{y}" r="{7 if hl else 5}" fill="{ACC if hl else NAVY}" stroke="#fff" stroke-width="1.5"/>'
            s+=text(x,ly,n,8.6 if not hl else 9.6,ACC if hl else NAVY,"middle",800 if hl else 500)
    return svg(w,top+len(axes)*rowh+10,s)

def legend(items,x,y,fs=9.5,gap=150):
    s=""
    for i,(lab,col) in enumerate(items):
        xx=x+i*gap
        s+=f'<rect x="{xx}" y="{y-9}" width="12" height="12" rx="2" fill="{col}"/>'+text(xx+17,y+1,lab,fs,NAVY)
    return s
