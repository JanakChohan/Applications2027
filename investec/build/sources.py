"""Parse source-table rows from every research findings file."""
import re, glob
def load():
    rows = {}
    for f in sorted(glob.glob('/home/user/Applications2027/investec/research/*.md')):
        ws = f.split('/')[-1].split('_')[0]
        for line in open(f, encoding='utf8'):
            line = line.strip().strip('`')
            m = re.match(r'^\|?\s*\[S(\d+)\]\s*\|(.*)$', line)
            if not m: continue
            n = int(m.group(1)); parts = [p.strip() for p in m.group(2).strip().strip('|').split('|')]
            if len(parts) < 5: continue
            outlet, title, pub, url = parts[0], parts[1], parts[2], parts[3]
            rest = parts[4:]
            status = next((p for p in rest if re.search(r'FETCHED|SNIPPET|PAYWALL', p)), '')
            note = rest[-1] if rest and rest[-1] != status else ''
            if n not in rows: rows[n] = (ws, outlet, title, pub, url, status, note)
    return rows
if __name__ == '__main__':
    r = load(); print(len(r), sorted(r)[:5], sorted(r)[-5:])
