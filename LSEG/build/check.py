import re,glob,os
parts=sorted(glob.glob('parts/*.html'))
src=open('parts/15_sources.html').read()
have=set(int(x) for x in re.findall(r'<td><b>S(\d+)</b>',src))
cited={}
for p in parts:
    if '15_sources' in p: continue
    t=open(p).read()
    for grp in re.findall(r'\[((?:S\d+[^\]]*))\]',t):
        for n in re.findall(r'S(\d+)',grp):
            cited.setdefault(int(n),set()).add(os.path.basename(p)[:2])
missing={k:v for k,v in cited.items() if k not in have}
print('sources in table',len(have),'cited',len(cited),'missing',sorted(missing.items()))
figs=[]
for p in parts:
    for f in re.findall(r'<div class="ft">Figure ([0-9]+[a-z]?)</div>',open(p).read()): figs.append((os.path.basename(p)[:2],f))
print(len(figs),'figures:',figs)
for p in parts:
    t=open(p).read()
    if '—' in t: print('EM DASH in',p,t.count('—'))
