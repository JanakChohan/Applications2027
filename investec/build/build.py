import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import lib, sources, parts_end as E, parts_firm as F, parts_role as R, parts_market as M
OUT = '/home/user/Applications2027/investec'

def glossary():
    g = []
    for line in open(f'{OUT}/research/WS4_industry_regulation.md', encoding='utf8'):
        m = re.match(r'^\d+\.\s+\*\*(.+?)\*\*:\s*(.+)$', line.strip())
        if m: g.append((m.group(1), m.group(2)))
    seen = {t.lower() for t,_ in g}
    g += [x for x in E.GLOSS_EXTRA if x[0].lower() not in seen]
    return sorted(g, key=lambda x: x[0].lower())

def cover():
    return ('<div class="cover"><div class="k">Complete interview pack</div>'
            '<h1>Investec<br>Summer Internship 2027</h1>'
            '<div class="sub">Specialist Bank, London, 30 Gresham Street. Requisition 14049. The role decoded, the firm from the inside, the industry from zero, live news, the interview, a scenario playbook and a cheat sheet.</div>'
            '<div class="meta">Prepared 5 October 2026, application day (window opened 09:00 for 24 hours).<br>'
            'Built only from public sources. Every non-obvious claim carries a confidence tag and a source marker resolving in Part 15.<br>'
            'Investec Bank plc, 30 Gresham Street, London EC2V 7QP · Companies House 00489604 · FCA/PRA FRN 172330 (reported).</div></div>')

def toc(body):
    rows = ''
    for m in re.finditer(r'<div class="band" id="(p\d+)"><div class="num">([^<]+)</div><h1>([^<]+)</h1>|<h2 id="([a-z0-9]+)">([^<]+)</h2>', body):
        if m.group(1):
            rows += f'<tr class="pt"><td>{m.group(2)}: {m.group(3)}<span class="tocpg" data-a="{m.group(1)}">0</span></td></tr>'
        else:
            rows += f'<tr><td style="padding-left:14px">{m.group(5)}<span class="tocpg" data-a="{m.group(4)}">0</span></td></tr>'
    return f'<section class="part"><h1 style="margin-top:0">Contents</h1><table class="toc">{rows}</table></section>'

def figlist():
    rows = ''.join(f'<tr><td style="padding:1px 2px">Figure {n}. {lib.esc(t)}<span class="tocpg" data-a="fig{n}">0</span></td></tr>' for n,t in lib.FIGS)
    return f'<section class="part"><h1 style="margin-top:0">List of figures</h1><table class="toc" style="font-size:8.6pt">{rows}</table></section>'

def markers(body):
    body = re.sub(r'(<div class="band" id="(p\d+)">)', r'\1<span class="mk">QQA\2QQ</span>', body)
    body = re.sub(r'(<h2 id="([a-z0-9]+)">)', r'<span class="mk">QQA\2QQ</span>\1', body)
    body = re.sub(r'(<div class="fig(?: fullpage)?" id="(fig\d+)">)', r'\1<span class="mk">QQA\2QQ</span>', body)
    return body

def main():
    lib.FIGS.clear()
    parts = [E.build0(), R.build(), F.build(), F.build3(), M.build4(), M.build5(), M.build6(), M.build7(), M.build8(),
             E.build9(), E.build10(), E.build11(), E.build12(), E.build13(), E.build14(glossary()), E.build15(sources.load()), E.build16()]
    body = ''.join(parts)
    body = body.replace('—', ', ')  # house style: no em dashes
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Investec Internship Pack</title>'
            f'<style>{open(os.path.join(os.path.dirname(__file__),"style.css")).read()}</style></head><body>'
            f'{cover()}{toc(body)}{figlist()}{markers(body)}</body></html>')
    path = f'{OUT}/Investec_Summer_Internship_2027_Complete_Interview_Pack.html'
    open(path, 'w', encoding='utf8').write(page)
    print('figures', len(lib.FIGS), 'bytes', len(page))

if __name__ == '__main__': main()
