import re, sys
sys.path.insert(0, '.')
from new_sections import S
base = open('../beginner-guide/sjp-beginners-guide.html').read()
head, rest = base.split('<!-- ============ COVER ============ -->', 1)
# split into named blocks
parts = re.split(r'<!-- ============ (.*?) ============ -->', '<!-- ============ COVER ============ -->' + rest)
blocks = {}
for i in range(1, len(parts), 2):
    blocks[parts[i]] = parts[i+1]
tail = ''
# glossary block contains closing body/html
g = blocks['21 GLOSSARY']
g, tail = g.split('</body>', 1)
blocks['21 GLOSSARY'] = g
tail = '</body>' + tail
def old(k): return blocks[k]
order = [
 S['COVER'], S['HV1'], S['HV2'], S['HV3'],
 old('1 BASIC IDEA'), old('2 TEN WORDS'), old('3 KINDS OF FIRM'), old('4 WHAT IS SJP'),
 S['HISTORY'], S['STRUCTURE'], old('5 PARTNERSHIP'),
 old('8 CLIENTS'), S['CLIENTS_REQ'], S['CLIENTS_TYPES'],
 old('6 WHAT SJP SELLS'), S['PRODUCTS_DEEP'], old('7 PENSIONS'), S['WHY_PRODUCTS'],
 old('9 WHAT A CLIENT PAYS'), S['MONEY_MODEL'], old('10 PROFIT'), S['WHICH_PRODUCTS'], old('11 LEAKY BUCKET'),
 old('12 HOW PARTS WORK TOGETHER'), old('13 CLIENT JOURNEY'),
 old('DIFFERENT 1'), old('DIFFERENT 2'), old('DIFFERENT 3'), old('DIFFERENT 4'),
 S['EXAMPLES'], old('14 WHAT WENT WRONG'), old('15 NOW'), S['STRATEGY'], S['COMPETITORS'], S['FASCINATING'],
 old('16 WHAT WM MEANS'), old('17 YOUR JOB WHERE'), old('18 YOUR JOB WHAT'), old('19 CONNECT'),
 old('20 SUMMARY'), old('21 GLOSSARY'),
]
body = '\n'.join(order)
# relabel old "PAGE n · X" steps to part labels
P3={'THE INDUSTRY','YOUR JOB','THE BIG PICTURE'}; P4={'REVISION','GLOSSARY'}
def relabel(m):
    lab = m.group(1)
    part = 'PART 3' if lab in P3 else ('PART 4' if lab in P4 else 'PART 2')
    style = ' style="background:#d9822b"' if part=='PART 3' else ''
    return f'<div class="step"{style}>{part} · {lab}</div>'
body = re.sub(r'<div class="step">PAGE \d+ · (.*?)</div>', relabel, body)
body = body.replace('<div class="step" style="background:#d9822b">WHAT MAKES SJP DIFFERENT', '<div class="step" style="background:#d9822b">PART 2 · WHAT MAKES SJP DIFFERENT')
# fix cross references in old text
body = body.replace('Section 17 explains this.', 'Part 3 explains this.').replace('(see page 14)', '(see "What went wrong")').replace('Page 14 explains why it changed.', '"What went wrong" explains why.').replace('Remember the four profit levers from page 10?', 'Remember the four profit levers from "How SJP makes its profit"?')
head = head.replace('<title>SJP Beginner\'s Guide</title>', '<title>SJP Complete Guide</title>')
open('sjp-complete-guide.html', 'w').write(head + body + '\n' + tail)
print('ok', body.count('<section'))
