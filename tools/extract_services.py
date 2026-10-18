"""Extract the 13 Q1 5787 Shabbat services from the manuscript PDF text into JSON."""
import re, json, sys
raw = open(sys.argv[1], encoding='utf-8').read()
raw = raw.replace('­', '').replace('of er', 'offer').replace('of ice', 'office')
parts = re.split(r'SHABBAT SERVICE (\d+) OF 13', raw)
def clean(t):
    t = re.sub(r'\s*\n\s*', ' ', t).strip()
    t = re.sub(r'\s{2,}', ' ', t)
    return t
def between(t, a, b):
    m = re.search(a + r'(.*?)' + b, t, re.S)
    return m.group(1) if m else ''
out = []
for i in range(1, len(parts), 2):
    n = int(parts[i]); t = parts[i + 1]
    title = re.search(r'“([^”]+)”', t).group(1)
    sub = re.search(r'Sequence:\s*(\d+)\s*\n\s*(\w+day), (\d+ \w+ \d{4})\s*\n+\s*(.+?)\n', t)
    seq, weekday, date, kicker = int(sub.group(1)), sub.group(2), sub.group(3), sub.group(4).strip()
    heb = re.search(r'(\d+ \w+) 5787 \| Sequence', t).group(1)
    implication = clean(between(t, r'IMPLICATION FOR THIS SABBATH', r'✦ II\. THE THEME ✦'))
    theme = [clean(p) for p in re.split(r'\n\s*\n', between(t, r'✦ II\. THE THEME ✦', r'✦ III\.').strip()) if clean(p)]
    focus = clean(between(t, r'✦ WORD IN GOLD ✦', r'\(NASB\)'))
    supporting = clean(between(t, r'SUPPORTING TEXTS', r'✦ IV\.'))
    school_t = between(t, r'✦ IV\. THE SCHOOL OF SCRIPTURES ✦', r'✦ V\.')
    items = re.split(r'\n\s*(I{1,3}|IV)\. ', '\n' + school_t)
    school = []
    for j in range(1, len(items), 2):
        body = items[j + 1].strip()
        head, _, rest = body.partition('\n')
        school.append({'n': items[j], 'title': clean(head), 'text': clean(rest)})
    comm = between(t, r'✦ V\. THE COMMUNION SEGMENT ✦', r'AT THE BREAKING OF THE BREAD')
    bread = clean(between(t, r'AT THE BREAKING OF THE BREAD', r'AT THE CUP'))
    cup = clean(between(t, r'AT THE CUP', r'THE SUMMONS FOR THE NEW WEEK'))
    summons = clean(between(t + '\nSHABBAT', r'THE SUMMONS FOR THE NEW WEEK', r'(?:\nSHABBAT|$)'))
    letters = re.search(r'✦ I\. THE SEQUENCE BLUEPRINT ✦\s*\n(.+?)\n', t).group(1)
    out.append(dict(n=n, title=title, seq=seq, weekday=weekday, date=date, hebrew=heb, kicker=kicker,
                    focus=focus, supporting=supporting, implication=implication, theme=theme,
                    school=school, communion=clean(comm), bread=bread, cup=cup, summons=summons))
json.dump(out, open(sys.argv[2], 'w'), ensure_ascii=False, indent=1)
for s in out: print(s['n'], s['title'], s['date'], s['hebrew'], s['seq'], len(s['school']), s['focus'][:30], '|', s['summons'][:60])
