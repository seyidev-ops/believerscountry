#!/usr/bin/env python3
"""Build the Believers Country / CMI static site.

Run from the repository root:   python3 tools/build_site.py
Every page shares one header, footer and design system. Content lives in this file
and in content/*.json, so a new episode or teaching is one entry, then one rebuild.
"""
import json, re, os, html, datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_URL = 'https://believerscountry.org/'
WAT = dt.timezone(dt.timedelta(hours=1))
NOW = dt.datetime.now(WAT)
# The day runs 6 PM to 6 PM: after 6 PM the next date's day has begun.
SACRED = (NOW + dt.timedelta(days=1)).date() if NOW.hour >= 18 else NOW.date()

EMAIL = 'countryministriesinternational@gmail.com'
LINKS = {
    'youtube': 'https://www.youtube.com/@believerscountry',
    'ministering': 'https://chat.whatsapp.com/B9DSqidV9SA0iyL6UemfM1',
    'school': 'https://chat.whatsapp.com/Hx8FnJWmFIw3mMwKjnOXoW',
    'shabbat': 'https://chat.whatsapp.com/GXjvYUmtqAtCYTa6vNcQmV',
}
GIVING = dict(name='Country Ministries International', bank='Guaranty Trust Bank (GTBank)',
              accounts=[('Naira', '₦', 'NGN', '3001282751'), ('US Dollar', '$', 'USD', '3001282775'),
                        ('British Pound', '£', 'GBP', '3001282816'), ('Euro', '€', 'EUR', '3001282799')])
LOGO = json.loads((ROOT / 'tools/logo_parts.json').read_text())
SERVICES = json.loads((ROOT / 'content/shabbat-services-5787-q1.json').read_text())
e = html.escape

def slugify(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

def hms(sec):
    sec = int(round(sec)); h, m = divmod(sec // 60, 60)
    return f'{h}:{m:02d}:{sec % 60:02d}' if h else f'{m}:{sec % 60:02d}'

def probe(path):
    import subprocess
    try:
        return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=nw=1:nk=1', str(path)]).decode().strip())
    except Exception:
        return None

for s in SERVICES:
    s['slug'] = slugify(s['title'])
    f = ROOT / 'assets/audio/shabbat' / (s['slug'] + '.mp3')
    d = probe(f) if f.exists() else None
    if d:
        s['audio'] = f"assets/audio/shabbat/{s['slug']}.mp3"
        s['seconds'] = int(round(d)); s['label'] = hms(d)
        s['path'] = f"teachings/{s['slug']}/"; s['word'] = s['title']
    s['iso'] = dt.datetime.strptime(s['date'], '%d %B %Y').date().isoformat()

EPISODES = [
    dict(slug='son-talk-part-2', title='Son Talk (Part 2)', date='2026-10-25', seconds=88, label='1:28',
         word='Son talk', blurb='The second word in the series on the Son: continuing to look at who He is and what He has accomplished.'),
    dict(slug='son-talk-part-1', title='Son Talk (Part 1)', date='2026-10-24', seconds=86, label='1:26',
         word='Son talk', blurb='The first of a short series on the Son: a brief word on who He is and what He has accomplished.'),
    dict(slug='who-are-believers', title='Who Are Believers', date='2026-10-23', seconds=87, label='1:27',
         word='Who are believers', blurb='Who the believer is in the Son: a short word on the identity of those who believe on Him.'),
    dict(slug='believe-on-him-part-3', title='Believe On Him (Part 3)', date='2026-10-22', seconds=86, label='1:26',
         word='Believe on Him', blurb='The third word in the series on believing on the Son: resting the whole weight of your life on Him.'),
    dict(slug='how-believe-comes', title='How Believe Comes', date='2026-10-21', seconds=92, label='1:32',
         word='How believe comes', blurb='Where believing comes from, and how it grows: a short word continuing the series on believing on the Son.'),
    dict(slug='believing-on-him-part-2', title='Believing On Him (Part 2)', date='2026-10-20', seconds=97, label='1:37',
         word='Believing on Him', blurb='The second word in the series on believing on the Son: continuing to rest your whole weight on Him, day by day.'),
    dict(slug='believe-on-him-part-1', title='Believe On Him (Part 1)', date='2026-10-19', seconds=87, label='1:27',
         word='Believe on Him', blurb='The first of a short series on believing on the Son: what it means to rest your whole weight on Him.'),
    dict(slug='the-measuring-line', title='The Measuring Line', date='2026-10-18', seconds=90, label='1:30',
         word='The measuring line', blurb='A short word from Believers Country on the measuring line. Press play, then carry it with you through the day.'),
    dict(slug='no-separation', title='No Separation', date='2026-10-17', seconds=82, label='1:22',
         word='Nothing stands between', blurb='Nothing created stands between the believer and the love of God in Christ. A short word on union that cannot be broken.'),
    dict(slug='proof-that-you-know-god', title='Proof that you know God', date='2026-10-16', seconds=85, label='1:25',
         word='Known and knowing', blurb='What does it look like to truly know God? A brief, searching word on the evidence of relationship.'),
    dict(slug='what-is-your-advantage-as-a-believer', title='What is your advantage as a believer', date='2026-10-15', seconds=89, label='1:29',
         word='The believer’s edge', blurb='The life received in the Son is not ordinary life. Two minutes on the advantage every believer carries.'),
    dict(slug='relationship-with-the-father', title='Relationship With The Father', date='2026-10-14', seconds=89, label='1:29',
         word='Abba, Father', blurb='Through the Son, by one Spirit, to the Father. A short word on the relationship at the centre of the faith.'),
]
for ep in EPISODES:
    ep['audio'] = f"assets/audio/{ep['slug']}.mp3"
    ep['path'] = f"listen/2-minutes/{ep['slug']}/"
    d = dt.date.fromisoformat(ep['date'])
    ep['pretty'] = d.strftime('%A · %-d %B %Y')
    ep['short'] = d.strftime('%-d %b')

def episode_for(day):
    asc = sorted(EPISODES, key=lambda x: x['date'])
    for ep in asc:
        if ep['date'] == day.isoformat():
            return ep
    first = dt.date.fromisoformat(asc[0]['date'])
    return asc[(day - first).days % len(asc)]

# ------------------------------------------------------------------ icons
I = {
 'copy': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="12" height="12" rx="2.5"/><path d="M5 15V5.5A2.5 2.5 0 0 1 7.5 3H15"/></svg>',
 'gift': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="13" rx="2"/><path d="M12 8v13M3 12h18M12 8S9.5 3 7 4.5 8.5 8 12 8Zm0 0s2.5-5 5-3.5S15.5 8 12 8Z"/></svg>',
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'up': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>',
 'play': '<svg class="i-play" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5v13a1 1 0 0 0 1.5.86l10.5-6.5a1 1 0 0 0 0-1.72L9.5 4.64A1 1 0 0 0 8 5.5Z"/></svg>',
 'pause': '<svg class="i-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="5" width="4" height="14" rx="1.2"/><rect x="14" y="5" width="4" height="14" rx="1.2"/></svg>',
 'download': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>',
 'share': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18" cy="5" r="2.5"/><circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="19" r="2.5"/><path d="m8.2 10.8 7.6-4.6M8.2 13.2l7.6 4.6"/></svg>',
 'cal': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3.5" y="5" width="17" height="15" rx="2.5"/><path d="M3.5 10h17M8 3v4M16 3v4"/></svg>',
 'whatsapp': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2a9.9 9.9 0 0 0-8.5 15l-1.4 5 5.2-1.36A9.9 9.9 0 1 0 12.04 2Zm0 18.1a8.2 8.2 0 0 1-4.2-1.15l-.3-.18-3.08.8.82-3-.2-.31a8.2 8.2 0 1 1 6.96 3.84Zm4.5-6.14c-.25-.12-1.46-.72-1.69-.8-.23-.08-.39-.12-.55.12-.17.25-.64.8-.78.97-.14.16-.29.18-.53.06a6.7 6.7 0 0 1-3.37-2.94c-.25-.44.25-.41.72-1.36.08-.16.04-.3-.02-.42-.06-.12-.55-1.33-.76-1.82-.2-.48-.4-.41-.55-.42h-.47a.9.9 0 0 0-.65.3 2.74 2.74 0 0 0-.86 2.04 4.76 4.76 0 0 0 1 2.53 10.9 10.9 0 0 0 4.17 3.68c1.55.67 2.16.73 2.94.61.47-.07 1.46-.6 1.66-1.17.2-.58.2-1.07.15-1.17-.06-.11-.22-.17-.47-.29Z"/></svg>',
 'youtube': '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12 31 31 0 0 0 1 16.8a3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8ZM9.8 15V9l5.2 3-5.2 3Z"/></svg>',
 'book': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5v-15Z"/><path d="M4 20.5A2.5 2.5 0 0 0 6.5 23H20v-5"/></svg>',
 'headphones': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1v-6h3v4ZM3 19a2 2 0 0 0 2 2h1v-6H3v4Z"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="m4 7 8 6 8-6"/></svg>',
}

# ------------------------------------------------------------------ the mark
DEFS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>
<linearGradient id="flameGold" x1="0" y1="1" x2="0" y2="0">
 <stop offset="0" stop-color="#b9781a"><animate attributeName="stop-color" values="#b9781a;#d8901f;#b9781a" dur="3.2s" repeatCount="indefinite"/></stop>
 <stop offset=".45" stop-color="#f2b73c"><animate attributeName="stop-color" values="#f2b73c;#ffd25e;#f0ad35;#f2b73c" dur="2.4s" repeatCount="indefinite"/></stop>
 <stop offset=".8" stop-color="#ffe08a"><animate attributeName="stop-color" values="#ffe08a;#fff3c4;#ffe08a" dur="1.8s" repeatCount="indefinite"/></stop>
 <stop offset="1" stop-color="#fff6d6"/>
</linearGradient>
<radialGradient id="flameHalo"><stop offset="0" stop-color="#ffd970" stop-opacity=".55"/><stop offset=".55" stop-color="#f3b84a" stop-opacity=".16"/><stop offset="1" stop-color="#f3b84a" stop-opacity="0"/></radialGradient>
<linearGradient id="riverGrad" x1="0" x2="1"><stop offset="0" stop-color="#7cc4c2" stop-opacity="0"/><stop offset=".4" stop-color="#e8c46f"/><stop offset=".7" stop-color="#7cd8dc"/><stop offset="1" stop-color="#7cc4c2" stop-opacity="0"/></linearGradient>
<linearGradient id="cityGlow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffe7a6" stop-opacity=".95"/><stop offset=".5" stop-color="#e8c46f" stop-opacity=".55"/><stop offset="1" stop-color="#7cd8dc" stop-opacity=".1"/></linearGradient>
</defs></svg>'''

def mark(cls='', label=None, still=False):
    aria = f'role="img" aria-label="{e(label)}"' if label else 'aria-hidden="true"'
    if still:
        return (f'<svg class="mark still {cls}" viewBox="{LOGO["viewBox"]}" {aria} focusable="false">'
                f'<path class="ring" d="{LOGO["ring"]}"/><path class="body" d="{LOGO["body"]}"/><path class="flame" d="{LOGO["flame"]}"/></svg>')
    return (f'<span class="mark-float {cls}"><span class="mark-spin"><svg class="mark" viewBox="{LOGO["viewBox"]}" {aria} focusable="false">'
            f'<ellipse class="flame-halo" cx="768" cy="430" rx="190" ry="250" fill="url(#flameHalo)"/>'
            f'<path class="ring" d="{LOGO["ring"]}"/><path class="body" d="{LOGO["body"]}"/><path class="flame" d="{LOGO["flame"]}"/>'
            f'</svg></span></span>')

# ------------------------------------------------------------------ chrome
# Four top-level items. Two of them open a short menu.
NAV = [
    ('about/', 'About', ['about'], None),
    (None, 'Ministries', ['ministries', 'encounters', 'spiritual-intent', 'year'], [
        ('ministries/', 'CMI ministry expressions', 'Four streams, one river'),
        ('encounters/', 'Weekly encounters', 'Wednesday, Thursday, Shabbat'),
        ('spiritual-intent/', 'Spiritual Intent', 'Books and study'),
        ('year-5787/', 'The Year 5787', 'Tav, Shin, Pe, Zayin')]),
    (None, 'Listen & Learn', ['listen', 'teachings'], [
        ('listen/2-minutes/', 'The listening room', '2 Minutes Podcast and Shabbat audio'),
        ('teachings/', 'Shabbat teachings', 'Thirteen Sabbaths celebrating the Son')]),
    ('contact/', 'Contact', ['contact'], None),
]

def toggle():
    return ('<button class="horizon" type="button" data-experience aria-label="Experience: Auto. Switch to Day.">'
            '<span class="horizon-track" aria-hidden="true"><span class="horizon-stars"><i></i><i></i><i></i><i></i></span><span class="horizon-orb"></span><span class="ground"></span></span>'
            '<span class="horizon-label" data-experience-label aria-hidden="true">Auto</span></button>'
            '<span class="sr-only" aria-live="polite" data-experience-live></span>')

def header(r, section):
    chev = '<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>'
    top, drawer = [], [f'<a class="d-link" href="{r or "./"}">Home</a>']
    for i, (href, label, keys, items) in enumerate(NAV):
        cur = ' aria-current="page"' if section in keys else ''
        if not items:
            top.append(f'<a class="nav-item" href="{r}{href}"{cur}>{label}</a>')
            drawer.append(f'<a class="d-link" href="{r}{href}"{cur}>{label}</a>')
            continue
        menu = ''.join(f'<a href="{r}{h}"><b>{t}</b><small>{d}</small></a>' for h, t, d in items)
        top.append(f'<div class="nav-group" data-nav-group><button class="nav-item" type="button" aria-expanded="false" aria-controls="nav-m{i}"{" data-current" if cur else ""}>{label}{chev}</button>'
                   f'<div class="nav-menu" id="nav-m{i}">{menu}</div></div>')
        sub = ''.join(f'<a href="{r}{h}">{t}<small>{d}</small></a>' for h, t, d in items)
        drawer.append(f'<details class="d-group" name="d-nav"{" open" if cur else ""}><summary>{label}{chev}</summary><div class="d-sub">{sub}</div></details>')
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="container"><div class="bar">
<a class="brand" href="{r or './'}" aria-label="Believers Country — home">{mark(still=True)}<span class="brand-words"><strong><span>Believers</span><span>Country</span></strong><small>CMI</small></span></a>
<nav class="primary-nav" aria-label="Main">{''.join(top)}</nav>
<div class="header-actions">{toggle()}<a class="button gold join" href="{r}encounters/">Join us {I['arrow']}</a>
<button class="menu-button" id="menu-button" type="button" aria-expanded="false" aria-controls="drawer" aria-label="Open menu"><i></i><i></i></button></div>
</div></div></header>
<div class="drawer" id="drawer" hidden><nav aria-label="Menu">{''.join(drawer)}</nav></div>'''

def footer(r):
    return f'''<footer class="footer"><div class="container">
<div class="footer-grid">
<div><a class="footer-brand" href="{r or './'}">{mark()}<span class="brand-words"><strong><span>Believers</span><span>Country</span></strong><small>CMI</small></span></a>
<p>A people belonging to the Father. A life received in the Son. A country expressed through His Spirit.</p>
<div class="socials"><a href="{LINKS['youtube']}" target="_blank" rel="noopener" aria-label="Believers Country on YouTube">{I['youtube']}</a><a href="{LINKS['shabbat']}" target="_blank" rel="noopener" aria-label="Join the Shabbat Service WhatsApp group">{I['whatsapp']}</a><a href="mailto:{EMAIL}" aria-label="Email Country Ministries International">{I['mail']}</a></div></div>
<div class="footer-col"><h4>Discover</h4><a href="{r}about/">Who we are</a><a href="{r}ministries/">Four ministry streams</a><a href="{r}year-5787/">The Year 5787</a><a href="{r}contact/">Contact</a><a href="{r}contact/#give">Give · Partner</a></div>
<div class="footer-col"><h4>Gather</h4><a href="{r}encounters/school-of-scriptures/">School of Scriptures · Wed</a><a href="{r}encounters/ministering-to-the-lord/">Ministering to the LORD · Thu</a><a href="{r}encounters/shabbat-service/">Shabbat Service · Sat</a></div>
<div class="footer-col"><h4>Listen &amp; read</h4><a href="{r}listen/2-minutes/">2 Minutes Podcast</a><a href="{r}teachings/">Shabbat teachings</a><a href="{r}spiritual-intent/">Spiritual Intent</a><a href="{LINKS['youtube']}" target="_blank" rel="noopener">YouTube channel</a></div>
</div>
<div class="legal"><span>© <span data-year>2026</span> Country Ministries International · Believers Country. All rights reserved.</span><nav aria-label="Legal"><a href="{r}privacy/">Privacy Policy</a><a href="{r}terms/">Terms of Use</a><span>Times in WAT (Africa/Lagos)</span></nav></div>
</div></footer>'''

ORG = {'@type': ['Organization', 'Church'], '@id': SITE_URL + '#org', 'name': 'Country Ministries International', 'alternateName': ['Believers Country', 'CMI'],
       'url': SITE_URL, 'logo': SITE_URL + 'assets/favicon-512.png', 'image': SITE_URL + 'assets/og-image.png', 'slogan': 'Living Eternal Life Abundantly.',
       'description': 'Believers Country is the communal expression of Country Ministries International: a people belonging to the Father, a life received in the Son, a country expressed through His Spirit.',
       'address': {'@type': 'PostalAddress', 'addressCountry': 'NG'}, 'email': EMAIL, 'sameAs': [LINKS['youtube']]}
CRUMB_NAMES = {'about': 'About', 'ministries': 'CMI ministry expressions', 'encounters': 'Weekly encounters', 'listen': 'Listen', '2-minutes': 'The listening room',
               'teachings': 'Shabbat teachings', 'spiritual-intent': 'Spiritual Intent', 'books': 'Money Under God', 'year-5787': 'The Year 5787',
               'contact': 'Contact', 'privacy': 'Privacy Policy', 'terms': 'Terms of Use'}
OG_TYPE = {'teachings': 'article', 'listen': 'article'}

def page(path, title, desc, body, section='', jsonld=None, extra_head='', out_file=None):
    depth = path.count('/') if path else 0
    r = '../' * depth
    full_title = f'{title} | Believers Country' if title != 'Believers Country' else 'Believers Country — Living Eternal Life Abundantly'
    url = SITE_URL + path
    graph = []
    if path == '':
        graph += [ORG, {'@type': 'WebSite', '@id': SITE_URL + '#site', 'name': 'Believers Country', 'alternateName': 'Country Ministries International',
                        'url': SITE_URL, 'inLanguage': 'en', 'publisher': {'@id': SITE_URL + '#org'}}]
    elif not out_file:
        parts = [x for x in path.strip('/').split('/') if x]
        items = [{'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE_URL}]
        for i in range(len(parts)):
            sub = '/'.join(parts[:i + 1]) + '/'
            if sub == 'listen/':
                continue
            name = title if i == len(parts) - 1 else CRUMB_NAMES.get(parts[i], parts[i])
            items.append({'@type': 'ListItem', 'position': len(items) + 1, 'name': name, 'item': SITE_URL + sub})
        graph.append({'@type': 'BreadcrumbList', 'itemListElement': items})
        graph.append({'@type': 'WebPage', '@id': url, 'url': url, 'name': full_title, 'description': desc, 'inLanguage': 'en',
                      'isPartOf': {'@type': 'WebSite', '@id': SITE_URL + '#site', 'name': 'Believers Country', 'url': SITE_URL}, 'publisher': {'@type': 'Organization', '@id': SITE_URL + '#org', 'name': 'Country Ministries International'}})
    if jsonld:
        graph += jsonld if isinstance(jsonld, list) else [jsonld]
    for g in graph: g.pop('@context', None)
    ld = f'<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>' if graph else ''
    og_type = OG_TYPE.get(path.split('/')[0], 'website') if path.count('/') > 1 else 'website'
    eps = json.dumps([{k: ep[k] for k in ('slug', 'title', 'date', 'audio', 'path', 'seconds', 'label')} for ep in EPISODES])
    doc = f'''<!DOCTYPE html>
<html lang="en" class="no-js" data-mode="system" data-theme="day" data-root="{r}">
<head>
<meta charset="utf-8">{extra_head}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#f7f2e6">
<link rel="canonical" href="{url}">
<meta name="robots" content="{'noindex' if out_file else 'index, follow, max-image-preview:large, max-snippet:-1'}">
<meta name="author" content="Country Ministries International">
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="Believers Country"><meta property="og:locale" content="en_NG"><meta property="og:title" content="{e(full_title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}assets/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Believers Country — Country Ministries International">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(full_title)}"><meta name="twitter:description" content="{e(desc)}"><meta name="twitter:image" content="{SITE_URL}assets/og-image.png">
<link rel="sitemap" type="application/xml" href="{SITE_URL}sitemap.xml">
<script>(function(){{var d=document.documentElement,m='system';try{{m=localStorage.getItem('bc-experience-v3')||localStorage.getItem('bc-experience-v2')||'system'}}catch(e){{}}if(['day','night','system'].indexOf(m)<0)m='system';d.dataset.mode=m;d.dataset.theme=m==='system'?(matchMedia('(prefers-color-scheme: dark)').matches?'night':'day'):m}})()</script>
<link rel="icon" href="{r}assets/favicon-day.svg" type="image/svg+xml" data-favicon="{r}assets/favicon-">
<link rel="icon" href="{r}assets/favicon-cmi.png" type="image/png" sizes="192x192" data-favicon-png="{r}assets/favicon-cmi">
<script>(function(){{var n=document.documentElement.dataset.theme==='night',a=document.querySelector('[data-favicon]'),b=document.querySelector('[data-favicon-png]');if(a)a.href=a.dataset.favicon+(n?'night':'day')+'.svg';if(b)b.href=b.dataset.faviconPng+(n?'-night':'')+'.png'}})()</script>
<link rel="apple-touch-icon" href="{r}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{r}assets/styles.css">
{ld}
</head>
<body>
{DEFS}
<div class="sky" aria-hidden="true"></div><div class="aurora" aria-hidden="true"></div><canvas id="sky-canvas" aria-hidden="true"></canvas>
{header(r, section)}
<main id="main">
{body(r) if callable(body) else body}
</main>
{footer(r)}
<script type="application/json" id="episodes-data">{eps}</script>
<script src="{r}assets/app.js" defer></script>
</body>
</html>
'''
    out = ROOT / (out_file or (path + 'index.html'))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    if not out_file: PAGES.append(path)

PAGES = []

# ------------------------------------------------------------------ components
def btn(href, text, kind='ghost', icon='arrow', ext=False):
    t = ' target="_blank" rel="noopener"' if ext else ''
    ic = I.get(icon, '') if icon else ''
    return f'<a class="button {kind}" href="{href}"{t}>{text} {ic}</a>' if icon != 'whatsapp' and icon != 'youtube' else f'<a class="button {kind}" href="{href}"{t}>{ic} {text}</a>'

def crumbs(r, trail):
    items = f'<a href="{r or "./"}">Home</a>' + ''.join(f'<span><a href="{r}{h}">{t}</a></span>' if h else f'<span aria-current="page">{t}</span>' for h, t in trail)
    return f'<nav class="crumbs" aria-label="Breadcrumb">{items}</nav>'

# Breadcrumb names for parent pages — the same label each page carries as its own crumb.
CRUMB = {'ministries/': 'CMI ministry expressions', 'encounters/': 'Weekly encounters', 'listen/2-minutes/': 'The listening room',
         'teachings/': 'Shabbat teachings', 'spiritual-intent/': 'Spiritual Intent'}

def page_hero(r, trail, eyebrow, h1, lead, chips=None, side=True, aside=''):
    # The page's label lives in the breadcrumb (Home / Weekly encounters), not repeated as a dashed line above the title.
    trail = [(h, CRUMB.get(h, t)) for h, t in trail[:-1]] + [(None, eyebrow)]
    c = ''
    if chips:
        c = '<div class="on-page">' + ''.join(f'<a class="chip" href="{h}">{t}</a>' for h, t in chips) + '</div>'
    if aside:
        return f'''<section class="page-hero with-aside"><div class="container hero-split"><div class="reveal">{crumbs(r, trail)}<h1>{h1}</h1><p class="lead">{lead}</p>{c}</div>{aside}</div></section>'''
    sm = f'<div class="side-mark" aria-hidden="true">{mark()}</div>' if side else ''
    return f'''<section class="page-hero"><div class="container reveal">{crumbs(r, trail)}<h1>{h1}</h1><p class="lead">{lead}</p>{c}</div>{sm}</section>'''

def portrait(r):
    # The photograph is shown whole and unaltered; only the frame around it is designed.
    return (f'<figure class="portrait reveal"><div class="portrait-float"><div class="portrait-frame"><div class="portrait-mat">'
            f'<picture><source srcset="{r}assets/people/seyi-and-shirley-ashiru.webp" type="image/webp">'
            f'<img src="{r}assets/people/seyi-and-shirley-ashiru.png" width="1086" height="1448" alt="Seyi and Shirley Ashiru" decoding="async" fetchpriority="high"></picture>'
            f'</div><span class="corner tl"></span><span class="corner tr"></span><span class="corner bl"></span><span class="corner br"></span></div></div>'
            f'<figcaption><b>Seyi &amp; Shirley Ashiru</b></figcaption></figure>')

def share_box(title, url):
    return (f'<div class="share" data-share-title="{e(title)}" data-share-url="{url}"><button class="chip" type="button" data-share-toggle aria-expanded="false">{I["share"]} Share</button>'
            '<div class="share-menu" hidden><button type="button" data-share="whatsapp">WhatsApp</button><button type="button" data-share="native">Device share</button>'
            '<button type="button" data-share="x">X / Twitter</button><button type="button" data-share="facebook">Facebook</button><button type="button" data-share="telegram">Telegram</button>'
            '<button type="button" data-share="email">Email</button><button type="button" data-share="copy">Copy link</button><p class="share-msg" role="status"></p></div></div>')

def player(r, ep, today=False, feature=False, tools=True):
    attrs = 'data-today-player ' if today else ''
    t = ''
    if tools:
        skip = ('<button class="chip" type="button" data-skip="-15" aria-label="Back 15 seconds">↺ 15s</button><button class="chip" type="button" data-skip="30" aria-label="Forward 30 seconds">30s ↻</button>'
                if ep['seconds'] > 600 else '')
        t = (f'<div class="player-tools">{skip}<a class="chip" data-download href="{r}{ep["audio"]}" download="{ep["slug"]}.mp3">{I["download"]} MP3</a>'
             f'{share_box(ep["title"], r + ep["path"])}</div>')
    return (f'<div class="player{" feature" if feature else ""}" {attrs}data-src="{r}{ep["audio"]}" data-duration="{ep["seconds"]}" data-album="{'Shabbat Services 5787' if ep['seconds'] > 600 else '2 Minutes Podcast'}">'
            f'<button class="play" type="button" aria-label="Play {e(ep["title"])}">{I["play"]}{I["pause"]}</button>'
            f'<div class="player-body"><div class="player-title">{e(ep["title"])}</div><div class="bars" aria-hidden="true"></div>'
            f'<div class="player-time"><span class="t-cur">0:00</span><span class="t-total">{ep["label"]}</span></div>{t}</div></div>')

def ep_card(r, ep):
    ax = {'son-talk-part-2': '30%', 'son-talk-part-1': '65%', 'who-are-believers': '40%', 'believe-on-him-part-3': '75%', 'how-believe-comes': '20%', 'believing-on-him-part-2': '55%', 'believe-on-him-part-1': '35%', 'the-measuring-line': '60%', 'no-separation': '25%', 'proof-that-you-know-god': '70%', 'what-is-your-advantage-as-a-believer': '45%', 'relationship-with-the-father': '80%'}[ep['slug']]
    return f'''<article class="card ep" style="--ax:{ax}"><div class="art" aria-hidden="true"><span class="rings"></span><span class="art-dur">{ep['label']}</span><span class="art-word">{e(ep['word'])}</span></div>
<div class="kicker">{ep['pretty']} <span class="badge latest" data-today-flag="{ep['slug']}" hidden>Today</span></div>
<h3><a class="card-link" href="{r}{ep['path']}">{e(ep['title'])}</a></h3><p>{e(ep['blurb'])}</p>{player(r, ep)}</article>'''

def svc_card(r, s, featured=False):
    letters = gem(s['seq'])
    return f'''<article class="card teach{' featured' if featured else ''}" data-teach data-svc-date="{s['iso']}"><span class="glyph hebrew" aria-hidden="true">{letters}</span>
<div class="meta"><span class="badge" data-status>Shabbat {s['n']} of 13</span><span class="badge">{s['hebrew']} · Seq {s['seq']}</span>{f'<span class="badge audio">{I["headphones"]} Listen · {s["label"]}</span>' if s.get('audio') else ''}</div>
<div class="kicker">{dt.date.fromisoformat(s['iso']).strftime('%-d %B %Y')}</div>
<h3><a class="card-link" href="{r}teachings/{s['slug']}/">{e(s['title'])}</a></h3><div class="focus">{e(s['focus'])}</div>
<div class="open"><span>{'Listen or read' if s.get('audio') else 'Open the teaching'}</span><span class="circle">{I['arrow']}</span></div></article>'''

def svc_player(r, s):
    if not s.get('audio'):
        return ''
    return (f'<div class="panel feature-player svc-listen" id="listen" style="margin-bottom:34px"><div class="today-label">{I["headphones"].replace("<svg", "<svg width=14 height=14")} Listen to this Shabbat service · {s["label"]}</div>'
            f'{player(r, s, feature=True)}<p class="muted small" style="margin:12px 0 0">Keep listening with your screen locked, or download the MP3 for the road.</p></div>')

def gem(n):
    H = ['', 'ק', 'ר', 'ש', 'ת']; T = ['', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ']; U = ['', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט']
    s = ''
    while n >= 400: s += 'ת'; n -= 400
    s += H[n // 100]; n %= 100
    s += 'טו' if n == 15 else 'טז' if n == 16 else T[n // 10] + U[n % 10]
    return s

ENCOUNTERS = [
    dict(key='wed', slug='school-of-scriptures', title='School of Scriptures', letter='ל', day='Wednesday', time='6:00 PM', link=LINKS['school'],
         heb='Wednesday evening, as Yom Chamishi begins', short='Scripture studied deeply in the light of the Son.',
         intro='A weekly time of patient, Christ-centred study. Scripture is opened with its context, its confirmation passages and its consequences for the believer’s life — so that we learn how conclusions are reached, not only what they are.',
         expect=[('Open with the Son', 'Every passage is read with Christ as its interpretive centre (Luke 24:27).'),
                 ('Reason from the text', 'Context, word studies and confirming passages are laid out so the reasoning is visible.'),
                 ('Test what we hear', 'Like the Bereans, we examine the Scriptures to see whether these things are so (Acts 17:11).'),
                 ('Carry it into the week', 'Each study closes with what changes in thought, speech and conduct.')],
         bring='Your Bible, a notebook, and a question you have been carrying.'),
    dict(key='thu', slug='ministering-to-the-lord', title='Ministering to the LORD', letter='ה', day='Thursday', time='6:00 PM', link=LINKS['ministering'],
         heb='Thursday evening, as Yom Shishi begins', short='Corporate prayer, ministry before the LORD and summons.',
         intro='Following the pattern of Antioch, where prophets and teachers were ministering to the Lord and fasting when the Holy Spirit spoke (Acts 13:1–3), this gathering turns Godward first — worship, thanksgiving, prayer in the Spirit, Scripture and attentive silence — before it turns to requests.',
         expect=[('Worship and thanksgiving', 'We come to minister to Him, not to extract an answer.'),
                 ('Prayer in the Spirit and with the mind', 'Room for tongues as Godward prayer, with order in the gathering (1 Corinthians 14:15, 40).'),
                 ('Summons', 'Instruction received is recorded, weighed and tested by Scripture, Christ, fruit and community.'),
                 ('Intercession', 'We pray by name for one another, for the household of faith and for the nations.')],
         bring='A quiet place to join from, and room in your evening to linger.'),
    dict(key='sat', slug='shabbat-service', title='Shabbat Service', letter='ש', day='Saturday', time='8:00 AM', link=LINKS['shabbat'],
         heb='Shabbat morning', short='Gathering around the Son, His Word, rest and fellowship.',
         intro='Our Saturday gathering of rest, Christ-centred teaching and communion. Shabbat is received as a discipline of rest and weekly completion in the finished work of the Son — never as a ladder into righteousness (Hebrews 4; Colossians 2:16–17).',
         expect=[('Convocation', 'The people are called to order and the week is consciously closed.'),
                 ('Ministering to the Lord', 'Worship, thanksgiving and attentive Godward prayer.'),
                 ('School of Scriptures', 'Christ-centred exposition with the reasoning made visible.'),
                 ('Communion', 'Bread and cup received through the finished work of the Son.'),
                 ('Commonwealth', 'Needs, testimonies, giving and practical care are surfaced.'),
                 ('Summons and sending', 'We enter the new week with tested instruction and leave as representatives.')],
         bring='Your Bible, and bread and cup if you are joining from home.'),
]

STREAMS = [
    dict(slug='believers-country', name='Believers Country', river='Perat · Euphrates', tag='Community', letter='ב',
         line='The communal expression of CMI: a country of believers, fellowship, citizenship and shared life.',
         burden='Fruitfulness, settlement and citizenship culture.', output='Embassies, domestic strata, assemblies and citizen formation.',
         body=['Believers Country is where doctrine becomes peoplehood. Its task is not merely to host weekly meetings but to form a recognisable culture of citizenship: worship, teaching, communion, common responsibility, households, welfare, work and public witness.',
               'In Ephesians 2:18–22, belonging is not created by institutional membership. Through the Son and by the Spirit, believers have access to the Father and are joined as fellow citizens and members of His household. Believers Country recognises, trains and organises what the Gospel has already created.'],
         structure=[('Regional strata', 'Coordinate several local embassies within a territory.'), ('Local embassies', 'A governed local expression of one message, one life and one civic order — not a franchise outlet.'), ('Domestic strata', 'Households and home hubs, where citizenship culture becomes daily life.')],
         verses='Colossians 1:13 · Philippians 3:20 · Ephesians 2:19 · 1 Peter 2:9–12'),
    dict(slug='school-of-scriptures', name='School of Scriptures', river='Gihon', tag='Scripture', letter='ל',
         line='The ministry’s teaching, study, formation and publishing expression, with Christ as interpretive centre.',
         burden='Breaking forth in understanding and scriptural formation.', output='Curriculum, teaching, publishing and leadership formation.',
         body=['The School exists because a movement that cannot reproduce its reasoning will eventually reproduce only its slogans. Its mandate is to teach how conclusions are reached, not merely which conclusions to repeat.',
               'Luke 24, Acts 17:11 and 2 Timothy 2:15 set the culture: Scripture opened around Christ, claims examined, and workers trained to handle the word accurately. The Wednesday study is one regular gathering of this ministry; its wider work includes teaching, study and publishing.'],
         structure=[('Christology', 'The person and finished work of the Son.'), ('New creation identity', 'What is true of the one who is in Christ.'), ('The Holy Spirit', 'His person, mission, gifts, fruit and the testing of what we hear.'), ('Languages and sacred time', 'Word studies, the Hebrew calendar and their responsible use.')],
         verses='Luke 24:27, 44–47 · Acts 17:11 · 2 Timothy 2:15'),
    dict(slug='commonwealth', name='Commonwealth', river='Pishon', tag='Welfare', letter='ס',
         line='Material welfare, responsible stewardship, economic support and practical care within the community.',
         burden='Shared resources, welfare and productive abundance.', output='Welfare, enterprise networks, skills exchange and mutual support.',
         body=['Acts 2:44–47 and 4:32–35 describe a community in which possessions never become indifference to need. 2 Corinthians 8–9 adds voluntary generosity, proportion, equality of burden and cheerful giving.',
               'Commonwealth makes belonging economically visible. Its aim is not dependency: it is that no citizen is abandoned, and that receiving help becomes a route back to productive contribution wherever possible. It is a ministry of care, never a promise of financial return.'],
         structure=[('Welfare and emergency support', 'Practical help when a member is in need.'), ('Productive empowerment', 'Skills, work and enterprise that restore contribution.'), ('Stewardship', 'Shared resources held and used faithfully.')],
         verses='Acts 2:44–47 · Acts 4:32–35 · 2 Corinthians 8–9'),
    dict(slug='country-vanguard', name='Country Vanguard', river='Hiddekel · Tigris', tag='Outreach', letter='ג',
         line='Missionary mobilisation, outreach and strategic deployment of service beyond the gathering.',
         burden='Swift deployment, pioneering and reach.', output='Envoys, embassy planting, mission teams and strategic response.',
         body=['The Vanguard carries the sending logic of Acts. The church at Antioch released Barnabas and Saul; apostolic teams entered cities, preached Christ, formed communities, appointed leaders and moved on.',
               'Hiddekel is a swift river, not an uncontrolled flood. Deployment follows doctrine, character, confirmation and accountable sending — so that what goes out carries the same life as what was received.'],
         structure=[('Pioneer envoys', 'People sent ahead to open new ground.'), ('Embassy launches', 'Planting new local expressions of Believers Country.'), ('Mission and response teams', 'Outreach and service where it is needed most.')],
         verses='Acts 13:1–4 · Acts 16:6–10 · Revelation 22:1–2'),
]

LAND = '''<div class="land" aria-hidden="true"><svg viewBox="0 0 1440 220" preserveAspectRatio="none">
<ellipse class="city" cx="700" cy="150" rx="260" ry="70"/>
<path class="h1" d="M0 150 C200 110 360 120 520 140 C680 160 820 120 980 118 C1140 116 1300 140 1440 128 L1440 220 L0 220Z"/>
<path class="h2" d="M0 176 C180 150 380 168 560 172 C760 176 900 150 1080 156 C1240 162 1360 176 1440 168 L1440 220 L0 220Z"/>
<path class="river" d="M700 150 C690 170 620 180 560 192 C480 206 300 206 0 214"/>
<path class="river" d="M700 150 C720 172 820 184 920 194 C1060 206 1240 208 1440 214" style="animation-duration:7s"/>
<path class="h3" d="M0 204 C240 192 520 206 720 210 C940 214 1180 198 1440 204 L1440 220 L0 220Z"/>
</svg></div>'''

# ------------------------------------------------------------------ HOME
def home(r):
    ep = episode_for(SACRED)
    latest = [s for s in SERVICES if s['iso'] <= SACRED.isoformat()]
    upcoming = [s for s in SERVICES if s['iso'] > SACRED.isoformat()]
    feat = (latest[-1:] + upcoming[:4]) if latest else upcoming[:5]
    if len(feat) < 5: feat = SERVICES[-5:]
    enc = ''.join(f'''<article class="card enc"><div class="icon-letter hebrew" aria-hidden="true">{x['letter']}</div>
<div class="kicker" style="margin-top:18px">{x['day']} · {x['heb'].split(',')[-1].strip().capitalize() if ',' in x['heb'] else x['heb']}</div><h3><a class="card-link" href="{r}encounters/{x['slug']}/">{x['title']}</a></h3><p>{x['short']}</p>
<div class="when"><b>{x['time']}</b><span>WAT · weekly</span></div><div class="next" data-next="{x['key']}">Every {x['day']}</div>
<div class="actions"><a class="button wa" href="{x['link']}" target="_blank" rel="noopener">{I['whatsapp']} Join on WhatsApp</a><button class="chip" type="button" data-ics="{x['key']}">{I['cal']} Add to calendar</button></div></article>''' for x in ENCOUNTERS)
    streams = ''.join(f'''<article class="card stream"><div class="kicker">0{i+1} · {s['tag']}</div><svg class="wave" viewBox="0 0 200 46" preserveAspectRatio="none" aria-hidden="true"><path d="M0 23 C25 5 50 41 75 23 S125 5 150 23 S175 41 200 23"/><path d="M0 30 C25 14 50 46 75 30 S125 14 150 30 S175 46 200 30"/></svg>
<div class="river-name">{s['river']}</div><h3><a class="card-link" href="{r}ministries/{s['slug']}/">{s['name']}</a></h3><p>{s['line']}</p><span class="more textlink">Explore <span class="arr">→</span></span></article>''' for i, s in enumerate(STREAMS))
    return f'''
<section class="hero"><div class="clouds" aria-hidden="true"><span class="cloud"></span><span class="cloud"></span><span class="cloud"></span></div>
<div class="container hero-grid">
<div class="reveal">
<h1><span class="h1-pre">Welcome to</span><em>Believers</em><br>Country.</h1>
<div class="tagline">Living Eternal Life Abundantly.</div>
<p class="lead">A people belonging to the Father. A life received in the Son. A country expressed through His Spirit.</p>
<div class="hero-actions"><a class="button primary" href="{r}encounters/">Join a weekly encounter {I['arrow']}</a><a class="button ghost" href="#today">{I['headphones']} Today’s 2 minutes</a></div>
<div class="foundation"><strong>Our foundation · Ephesians 2:18–22</strong><span>Through the Son. By one Spirit. To the Father. No longer strangers — together, members of God’s household.</span></div>
</div>
<div class="hero-mark" aria-hidden="true"><span class="halo-rays"></span><span class="orbit-ring two"></span><span class="orbit-ring"></span>{mark()}</div>
</div>{LAND}</section>

<section class="today" id="today"><div class="container"><div class="panel today-inner reveal">
<div class="today-cell"><div class="today-label"><span class="live-dot"></span> Today</div>
<div class="hdate"><span data-hdate>{SACRED.strftime('%-d %B %Y')}</span><span class="hebrew" data-hdate-heb></span></div>
<div class="today-meta"><span data-hweekday></span> · <span data-hcivil></span><br><span data-hseq></span> · <span data-hmovement></span><br><span data-hboundary>The day begins at 6:00 PM</span></div></div>
<div class="today-cell" data-today-wrap><div class="today-label">{I['headphones'].replace('<svg', '<svg width="14" height="14"')} Today’s 2 minutes</div>{player(r, ep, today=True)}
<a class="textlink" style="margin-top:12px" href="{r}listen/2-minutes/" data-today-link>All episodes <span class="arr">→</span></a></div>
<div class="today-cell" data-countdown><div class="today-label">Next encounter</div><div class="countdown"><span data-cd-title>Shabbat Service</span><small><span data-cd-when></span></small></div>
<div class="today-meta">Begins in <b data-cd-time>—</b></div><a class="button wa" style="margin-top:14px;min-height:42px" data-cd-join href="{LINKS['shabbat']}" target="_blank" rel="noopener">{I['whatsapp']} Join on WhatsApp</a></div>
</div></div></section>

<section class="section"><div class="container grid g2" style="align-items:center;gap:clamp(30px,6vw,80px)">
<div class="reveal"><div class="eyebrow">More than a gathering</div><h2>A shared life, <em>centred on the Son.</em></h2></div>
<div class="reveal"><p class="lead">Believers Country is the communal expression of CMI. Our understanding of Scripture, our fellowship and our service begin with Christ Jesus — who He is, what He has accomplished and the life we have received in Him.</p>
<p class="muted">We are learning to express that life together: in the Word, in prayer, in practical care and beyond our own community. We announce Yeshua Himself — salvation is not first a process; salvation is a Person.</p>
<a class="textlink" href="{r}about/">Discover who we are <span class="arr">→</span></a></div>
</div></section>

<section class="section tight" id="encounters"><div class="container">
<div class="section-head reveal"><div><div class="eyebrow">Weekly encounters</div><h2>Three moments <em>each week.</em></h2><p class="lead">Study the Scriptures, minister before the LORD and gather on Shabbat. Each encounter has its own WhatsApp community — tap to join.</p></div><a class="textlink" href="{r}encounters/">The weekly rhythm <span class="arr">→</span></a></div>
<div class="grid g3 reveal-stagger">{enc}</div></div></section>

<section class="section"><div class="container">
<div class="section-head reveal"><div><div class="eyebrow">Shabbat teachings · First quarter 5787</div><h2>Celebrating <em>the Son.</em></h2><p class="lead">Thirteen Sabbaths moving through the person and work of Christ — from His place before all things to the promise of His return. Read them, or listen to the full services on the go.</p></div><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="button ghost" href="{r}listen/2-minutes/#shabbat">{I['headphones']} Listen to the services</a><a class="textlink" href="{r}teachings/">The full library <span class="arr">→</span></a></div></div>
<div class="teach-grid reveal-stagger">{''.join(svc_card(r, s, i == 0) for i, s in enumerate(feat))}</div></div></section>

<section class="section tight"><div class="container grid g2">
<article class="card reveal" style="padding:clamp(26px,3vw,42px)"><div class="kicker">The listening room</div><h2 style="margin:10px 0 14px">2 Minutes <em>Podcast.</em></h2><p>Short, original words from Believers Country. Press play, then sit with it for the rest of your day.</p>
<div style="display:grid;gap:10px;margin:16px 0">{''.join(f'<a class="chip" style="justify-content:space-between;padding:12px 16px;position:relative;z-index:2" href="{r}{x["path"]}"><span>{e(x["title"])}</span><span class="muted">{x["label"]}</span></a>' for x in EPISODES)}</div>
<a class="button primary" style="position:relative;z-index:2;align-self:flex-start" href="{r}listen/2-minutes/">{I['headphones']} Enter the listening room</a></article>
<article class="card reveal" style="padding:clamp(26px,3vw,42px)"><div class="kicker">Books · Spiritual Intent</div><h2 style="margin:10px 0 14px">Money <em>Under God.</em></h2><p>Scripture read in the light of Christ — four books on wealth, receiving, debt, investment and enjoyment.</p>
<div class="books" style="margin:22px 0;grid-template-columns:repeat(4,1fr)">{''.join(f'<span class="book"><img src="{r}assets/books/money-under-god/{b}.png" alt="" width="256" height="405" loading="lazy" decoding="async"></span>' for b in ['scriptural-wealth', 'how-to-receive-from-god', 'scriptural-pattern-of-debt', 'investment-and-enjoyment'])}</div>
<a class="button ghost" style="position:relative;z-index:2;align-self:flex-start" href="{r}spiritual-intent/books/">{I['book']} See the collection</a></article>
</div></section>

<section class="section"><div class="container">
<div class="section-head reveal"><div><div class="eyebrow">CMI ministry expressions</div><h2>One river, <em>four streams.</em></h2><p class="lead">A river went out of Eden and parted into four heads (Genesis 2:10). Our ministries are distinct in function and one in source.</p></div><a class="textlink" href="{r}ministries/">All ministries <span class="arr">→</span></a></div>
<div class="grid g4 reveal-stagger">{streams}</div></div></section>

{year_teaser(r)}

<section class="section tight"><div class="container"><div class="callband reveal"><div><h2>Come into the <em>conversation.</em></h2><p>Start with a gathering. Listen, learn, pray, and discover the shared life of believers centred on the Son.</p></div>
<div class="cta"><a class="button gold" href="{LINKS['shabbat']}" target="_blank" rel="noopener">{I['whatsapp']} Join this Shabbat</a><a class="button ghost" href="{r}contact/#give">{I['gift']} Give · Partner</a><a class="button ghost" href="{LINKS['youtube']}" target="_blank" rel="noopener">{I['youtube']} Watch on YouTube</a></div></div></div></section>
'''

YEAR_LETTERS = [('ת', 'Tav', 400, 'The mark', 'Sign, seal and ownership — whose you are, settled before anything is said.'),
                ('ש', 'Shin', 300, 'The fire', 'Refining and transformation — the polishing that makes an arrow select.'),
                ('פ', 'Pe', 80, 'The mouth', 'Speech and declaration — the word that is made, not invented.'),
                ('ז', 'Zayin', 7, 'The sword', 'Edge, crown and Sabbath completion — authority that waits to be released.')]
MOVES = [('Tav', 'Tishrei – Kislev', 'Seq 1–90'), ('Shin', 'Tevet – Adar II', 'Seq 91–208'), ('Pe', 'Nisan – Sivan', 'Seq 209–297'), ('Zayin', 'Tammuz – Elul', 'Seq 298–385')]

def year_teaser(r):
    cards = ''.join(f'<article class="card letter-card"><div class="heb hebrew" aria-hidden="true">{h}</div><div class="val">{n} · {v}</div><h3>{t}</h3><p>{d}</p></article>' for h, n, v, t, d in YEAR_LETTERS)
    mv = ''.join(f'<div data-m="{m}">{m}<small>{a} · {b}</small></div>' for m, a, b in MOVES)
    return f'''<section class="section tight"><div class="container"><div class="section-head reveal"><div><div class="eyebrow">The year 5787 · <span class="hebrew">ה׳תשפ״ז</span></div><h2>The year of the <em>crowned mouth.</em></h2><p class="lead">Mark, fire, mouth, sword. Ownership precedes formation; formation precedes speech; speech precedes authority (Isaiah 49:2).</p></div><a class="textlink" href="{r}year-5787/">Walk through the year <span class="arr">→</span></a></div>
<div class="letters reveal-stagger">{cards}</div><div class="movement-bar reveal" aria-label="The four movements of 5787">{mv}</div></div></section>'''

# ------------------------------------------------------------------ ABOUT
def about(r):
    return page_hero(r, [(None, 'About')], 'Who we are', 'The country we call <em>home.</em>',
                     'Believers Country welcomes you into the shared life and ministry of Country Ministries International.',
                     [('#centre', 'Our centre'), ('#identity', 'Our identity'), ('#life', 'Eternal life in abundance'), ('#language', 'Why “Country”'), ('#declaration', 'Our declaration')]) + f'''
<section class="section tight" id="centre"><div class="container grid g2" style="gap:clamp(30px,6vw,80px)">
<div class="reveal"><div class="eyebrow">Our centre</div><h2>Yeshua is <em>Salvation.</em></h2></div>
<div class="reveal"><p class="lead">Salvation is not first a process; salvation is a Person. Simeon took the child in his arms and said, “my eyes have seen Your salvation.” When Yeshua entered Zacchaeus’ house, salvation came to that house.</p>
<p class="muted">Forgiveness, life, reconciliation, righteousness and deliverance are not separate commodities handed out apart from Christ. They are received in union with Him. So we do not preach a mechanism with Jesus added as the password — we announce the crucified, risen and enthroned Son. To receive Him is to receive the life that is in Him (1 John 5:11–12).</p>
<ul class="clean ticks small"><li>Luke 2:25–32 · Luke 19:9–10 · John 1:4</li><li>John 14:6 · Acts 4:10–12 · Hebrews 5:9</li></ul></div></div></section>

<section class="section tight" id="identity"><div class="container">
<div class="section-head reveal"><div><div class="eyebrow">Our identity</div><h2>Father. Son. <em>Spirit.</em></h2><p class="lead">Ephesians 2:18–22 places our belonging in the work of the Son and the fellowship of the Spirit: we have access to the Father and are joined as fellow citizens and members of His household. John 14:16–23 shows how that life is personally received.</p></div></div>
<div class="grid g3 reveal-stagger">
<article class="card"><div class="icon-letter hebrew">א</div><h3 style="margin-top:20px">A people belonging to the Father</h3><p>Transferred out of darkness into the domain of the Son, we are no longer strangers but members of God’s household (Colossians 1:13; Ephesians 2:19).</p></article>
<article class="card"><div class="icon-letter hebrew">ב</div><h3 style="margin-top:20px">A life received in the Son</h3><p>“In Him was life.” Eternal life is located in the Son, and those who have the Son have life (John 1:4; 1 John 5:12).</p></article>
<article class="card"><div class="icon-letter hebrew">ר</div><h3 style="margin-top:20px">A country expressed through His Spirit</h3><p>The Spirit regenerates, indwells, seals, teaches and empowers — and always glorifies the Son (John 16:13–15).</p></article>
</div></div></section>

<section class="section tight" id="life"><div class="container"><div class="panel reveal" style="padding:clamp(28px,4vw,56px)">
<div class="grid g2" style="gap:clamp(24px,5vw,60px)"><div><div class="eyebrow">Our motto</div><h2>Living Eternal Life <em>in Abundance.</em></h2><p class="lead" style="margin-top:16px">Living Zoe unto Perisson.</p></div>
<div class="facts"><div><span>Zoe — the life received</span><b>The divine life shared through union with Christ (John 5:26; 10:28)</b></div><div><span>Perisson — the life overflowing</span><b>Beyond the ordinary measure, across the whole person and community (John 10:10)</b></div><div><span>The order</span><b>Accomplished reality first; trained expression second</b></div><div><span>Not a prosperity doctrine</span><b>Provision matters, but money is not the measure of divine life</b></div></div></div></div></div></section>

<section class="section tight" id="language"><div class="container grid g3 reveal-stagger">
<article class="card"><div class="kicker">Why “Country”</div><h3>Citizenship you can inhabit</h3><p>Country speaks of belonging, shared life, citizenship and ordered community under Christ. It recovers the civic force of politeuma, sympolitai, ethnos and patris. It is not a claim to political sovereignty, nor a literal translation of basileia.</p></article>
<article class="card"><div class="kicker">Why “Believer”</div><h3>The believing one</h3><p>John organises the response to Yeshua around believing (John 3:16; 20:31). “Christian” is a biblical word (Acts 11:26; 1 Peter 4:16); we simply keep the defining act and posture visible.</p></article>
<article class="card"><div class="kicker">Continuous believing</div><h3>Neither terror nor presumption</h3><p>Assurance rests in the eternal Son, His finished work and keeping power. We do not wake trying to be saved again; we remain where life is — in the Son (John 10:27–30; 15:4).</p></article>
</div></section>

<section class="section tight" id="declaration"><div class="container"><div class="summons reveal"><div class="kicker">The CMI core declaration</div>
<p>Yeshua is Salvation. His life is our life, His finished work is our standing, His Spirit is our indwelling witness and power, and His present Lordship is the government under which we live. We are marked before we are armed, formed before we speak, and restrained before we wield an edge. Christ is the centre. Scripture is the witness. The Spirit glorifies the Son. The Son honours the Father. The Country belongs to the Father.</p></div></div></section>
{next_steps(r, [('ministries/', 'The four streams', 'See how one river becomes four ministries.'), ('encounters/', 'Weekly encounters', 'Wednesday, Thursday and Shabbat.'), ('teachings/', 'Shabbat teachings', 'Thirteen Sabbaths celebrating the Son.')])}'''

def next_steps(r, items, title='Where to <em>next.</em>'):
    cards = ''.join(f'<article class="card"><div class="kicker">Next</div><h3><a class="card-link" href="{r}{h}">{t}</a></h3><p>{d}</p><span class="more textlink">Continue <span class="arr">→</span></span></article>' for h, t, d in items)
    return f'<section class="section tight"><div class="container"><div class="section-head reveal"><h2>{title}</h2></div><div class="grid g3 reveal-stagger">{cards}</div></div></section>'

# ------------------------------------------------------------------ MINISTRIES
def ministries(r):
    rows = ''.join(f'''<article class="card stream"><div class="icon-letter hebrew" aria-hidden="true">{s['letter']}</div><div class="kicker" style="margin-top:18px">0{i+1} · {s['tag']} · {s['river']}</div>
<h3><a class="card-link" href="{r}ministries/{s['slug']}/">{s['name']}</a></h3><p>{s['line']}</p><div class="facts small"><div><span>Burden</span><b>{s['burden']}</b></div><div><span>Fruit</span><b>{s['output']}</b></div></div><span class="more textlink">Explore {s['name']} <span class="arr">→</span></span></article>''' for i, s in enumerate(STREAMS))
    return page_hero(r, [(None, 'Ministries')], 'CMI ministry expressions', 'One river, <em>four streams.</em>',
                     'Distinct expressions of life and service, built on one foundation in Christ.', [(f'#{s["slug"]}', s['name']) for s in STREAMS]) + f'''
<section class="section tight"><div class="container"><div class="grid g2 reveal-stagger">{rows}</div></div></section>
<section class="section tight"><div class="container"><div class="panel reveal" style="padding:clamp(28px,4vw,56px)"><div class="grid g2" style="gap:clamp(24px,5vw,60px)">
<div><div class="eyebrow">Why four</div><h2>From Eden <em>to the throne.</em></h2></div>
<div><p class="lead">Genesis 2:10 describes one river leaving Eden and dividing into four heads. Revelation 22:1–2 closes the canon with the river of the water of life flowing from the throne of God and of the Lamb, for the healing of the nations.</p>
<p class="muted">Believers Country without the School becomes culture without depth. The School without the Country becomes knowledge without peoplehood. Commonwealth without formation becomes welfare administration. Vanguard without all three becomes expansion without substance. The four correct one another by remaining one river.</p></div></div></div></div></section>
{next_steps(r, [('encounters/', 'Gather with us', 'Three weekly encounters, each with its own community.'), ('about/', 'Our centre', 'Why we begin with the Son.'), ('contact/', 'Get in touch', 'Join a WhatsApp community or watch on YouTube.')])}'''

def stream_page(s, idx):
    def body(r):
        others = [x for x in STREAMS if x is not s]
        struct = ''.join(f'<li><span><b>{a}</b><span>{b}</span></span></li>' for a, b in s['structure'])
        return page_hero(r, [('ministries/', 'Ministries'), (None, s['name'])], f"0{idx+1} · {s['tag']} · {s['river']}", s['name'], s['line'],
                         [('#about', 'About this stream'), ('#shape', 'How it works'), ('#gather', 'Take part')]) + f'''
<section class="section tight" id="about"><div class="container article"><div class="prose reveal">{''.join(f'<p>{p}</p>' for p in s['body'])}
<h2 id="shape">How it <em>works.</em></h2><ol class="steps clean">{struct}</ol></div>
<aside class="aside reveal"><div class="panel"><div class="letter-big hebrew" aria-hidden="true">{s['letter']}</div><div class="facts small" style="margin-top:14px"><div><span>River</span><b>{s['river']}</b></div><div><span>Burden</span><b>{s['burden']}</b></div><div><span>Fruit</span><b>{s['output']}</b></div><div><span>Scripture</span><b>{s['verses']}</b></div></div></div>
<a class="button wa" href="{LINKS['shabbat']}" target="_blank" rel="noopener">{I['whatsapp']} Join the community</a></aside></div></section>
<section class="section tight" id="gather"><div class="container"><div class="section-head reveal"><h2>The other <em>streams.</em></h2></div><div class="grid g3 reveal-stagger">{''.join(f'<article class="card stream"><div class="kicker">{o["tag"]} · {o["river"]}</div><h3><a class="card-link" href="{r}ministries/{o["slug"]}/">{o["name"]}</a></h3><p>{o["line"]}</p><span class="more textlink">Explore <span class="arr">→</span></span></article>' for o in others)}</div></div></section>'''
    page(f"ministries/{s['slug']}/", s['name'], s['line'], body, 'ministries')

# ------------------------------------------------------------------ ENCOUNTERS
def encounters(r):
    cards = ''.join(f'''<article class="card enc" id="{x['slug']}"><div class="icon-letter hebrew" aria-hidden="true">{x['letter']}</div><div class="kicker" style="margin-top:18px">0{i+1} · Every {x['day']}</div>
<h3><a class="card-link" href="{r}encounters/{x['slug']}/">{x['title']}</a></h3><p>{x['short']}</p><div class="when"><b>{x['time']}</b><span>WAT</span></div><div class="heb-note">{x['heb']}</div><div class="next" data-next="{x['key']}">Every {x['day']}</div>
<div class="actions"><a class="button wa" href="{x['link']}" target="_blank" rel="noopener">{I['whatsapp']} Join on WhatsApp</a><button class="chip" type="button" data-ics="{x['key']}">{I['cal']} Calendar</button></div></article>''' for i, x in enumerate(ENCOUNTERS))
    return page_hero(r, [(None, 'Encounters')], 'Weekly encounters', 'Scripture, prayer <em>and rest.</em>',
                     'Meet with us through the week. Each encounter gathers in its own WhatsApp community, where joining details and notices are shared.') + f'''
<section class="section tight"><div class="container"><div class="grid g3 reveal-stagger">{cards}</div></div></section>
<section class="section tight"><div class="container"><div class="panel reveal" style="padding:clamp(28px,4vw,56px)"><div class="grid g2" style="gap:clamp(24px,5vw,60px)">
<div><div class="eyebrow">Sacred time</div><h2>Evening <em>and morning.</em></h2></div>
<div><p class="lead">Genesis counts each day from evening to morning, and Leviticus 23:32 orders the appointed day from evening to evening. So our day begins at 6:00 PM.</p>
<p class="muted">That is why our Wednesday and Thursday encounters open a new day rather than close an old one: rest is received before work is performed. All times are West Africa Time (Africa/Lagos, UTC+1).</p></div></div></div></div></section>
<section class="section tight"><div class="container"><div class="panel reveal" data-countdown style="padding:clamp(24px,3vw,40px);display:flex;flex-wrap:wrap;gap:24px;align-items:center;justify-content:space-between">
<div><div class="today-label"><span class="live-dot"></span> Next encounter</div><div class="countdown"><span data-cd-title>—</span><small><span data-cd-when></span> · begins in <b data-cd-time>—</b></small></div></div>
<a class="button wa" data-cd-join href="{LINKS['shabbat']}" target="_blank" rel="noopener">{I['whatsapp']} Join on WhatsApp</a></div></div></section>'''

def encounter_page(x, idx):
    def body(r):
        exp = ''.join(f'<li><span><b>{a}</b><span>{b}</span></span></li>' for a, b in x['expect'])
        extra = ''
        if x['key'] == 'sat':
            nxt = [s for s in SERVICES if s['iso'] >= SACRED.isoformat()][:1] or SERVICES[-1:]
            extra = f'<div class="section-head reveal" style="margin-top:60px"><h2>This <em>Shabbat.</em></h2></div><div class="teach-grid reveal-stagger" style="grid-template-columns:1fr">{svc_card(r, nxt[0], True)}</div>'
        return page_hero(r, [('encounters/', 'Encounters'), (None, x['title'])], f"Every {x['day']} · {x['time']} WAT", x['title'], x['intro'],
                         [('#expect', 'What to expect'), ('#join', 'How to join')]) + f'''
<section class="section tight" id="expect"><div class="container article"><div class="reveal"><h2 style="margin-bottom:24px">What to <em>expect.</em></h2><ol class="steps clean">{exp}</ol>{extra}</div>
<aside class="aside reveal" id="join"><div class="panel"><div class="letter-big hebrew" aria-hidden="true">{x['letter']}</div><div class="facts small" style="margin-top:14px"><div><span>When</span><b>Every {x['day']} · {x['time']}</b></div><div><span>Sacred time</span><b>{x['heb']}</b></div><div><span>Next</span><b data-next="{x['key']}">Every {x['day']}</b></div><div><span>Bring</span><b>{x['bring']}</b></div></div></div>
<a class="button wa" href="{x['link']}" target="_blank" rel="noopener">{I['whatsapp']} Join the {x['title']} group</a><button class="button ghost" type="button" data-ics="{x['key']}">{I['cal']} Add to calendar</button></aside></div></section>
{next_steps(r, [(f"encounters/{o['slug']}/", o['title'], f"Every {o['day']} · {o['time']} WAT") for o in ENCOUNTERS if o is not x] + [('teachings/', 'Shabbat teachings', 'Revisit the Sabbaths of this quarter.')], 'Other <em>encounters.</em>')}'''
    nxt = SACRED + dt.timedelta(days=(({'wed': 2, 'thu': 3, 'sat': 5}[x['key']] - SACRED.weekday()) % 7))
    hh = 18 if x['key'] != 'sat' else 8
    ev = {'@type': 'Event', 'name': f"{x['title']} · Believers Country", 'description': x['intro'], 'url': SITE_URL + f"encounters/{x['slug']}/",
          'startDate': f"{nxt.isoformat()}T{hh:02d}:00:00+01:00", 'endDate': f"{nxt.isoformat()}T{hh + 2:02d}:00:00+01:00",
          'eventAttendanceMode': 'https://schema.org/OnlineEventAttendanceMode', 'eventStatus': 'https://schema.org/EventScheduled',
          'eventSchedule': {'@type': 'Schedule', 'repeatFrequency': 'P1W', 'byDay': f"https://schema.org/{x['day']}", 'startTime': f'{hh:02d}:00', 'endTime': f'{hh + 2:02d}:00', 'scheduleTimezone': 'Africa/Lagos'},
          'location': {'@type': 'VirtualLocation', 'url': x['link']}, 'isAccessibleForFree': True,
          'organizer': {'@type': 'Organization', 'name': 'Country Ministries International', 'url': SITE_URL}, 'image': SITE_URL + 'assets/og-image.png'}
    page(f"encounters/{x['slug']}/", x['title'], f"{x['title']} — every {x['day']} at {x['time']} WAT. {x['short']}", body, 'encounters', ev)

# ------------------------------------------------------------------ LISTEN
def archive_row(r, x, kind):
    d = dt.date.fromisoformat(x['iso'] if kind == 'shabbat' else x['date'])
    if kind == 'shabbat':
        label, sub, href = f"Shabbat service {x['n']}", x['focus'], f"teachings/{x['slug']}/"
    else:
        label, sub, href = '2 Minutes', x['blurb'], x['path']
    return (f'<article class="arc-row" data-arc data-kind="{kind}" data-date="{d.isoformat()}" data-title="{e(x["title"].lower())}">'
            f'<div class="arc-date"><b>{d.day}</b><span>{d.strftime("%b %Y")}</span><small>{d.strftime("%A")}</small></div>'
            f'<div class="arc-info"><span class="badge{" audio" if kind == "shabbat" else ""}">{label} · {x["label"]}</span>'
            f'<h3><a href="{r}{href}">{e(x["title"])}</a></h3><p>{e(sub)}</p></div>{player(r, x)}</article>')

def listen(r):
    ep = episode_for(SACRED)
    rows = [archive_row(r, x, 'podcast') for x in EPISODES] + [archive_row(r, x, 'shabbat') for x in SERVICES if x.get('audio')]
    n_pod, n_sab = len(EPISODES), len([x for x in SERVICES if x.get('audio')])
    return page_hero(r, [(None, 'Listen')], 'The listening room', '2 Minutes <em>Podcast.</em>',
                     'A brief word, with room to reflect — and the full Shabbat services for the road. Play here, download for later, or share with someone who needs it today.', side=False) + f'''
<section class="section tight" style="padding-top:0"><div class="container"><div class="panel feature-player reveal" data-today-wrap>
<div class="today-label"><span class="live-dot"></span> Today’s 2 minutes · <span data-hcivil></span></div>{player(r, ep, today=True, feature=True)}
<p class="muted small" style="margin:14px 0 0">A new day begins at 6:00 PM, and so does the day’s word. <a class="textlink" data-today-link href="{r}{ep['path']}">Episode page <span class="arr">→</span></a></p></div></div></section>
<section class="section tight" id="archive"><span id="shabbat"></span><div class="container"><div class="section-head reveal"><div><h2>The <em>archive.</em></h2><p class="lead">Every recording in one place. Search by title or topic, filter by kind, and sort by date.</p></div>
<a class="button ghost" href="{LINKS['youtube']}" target="_blank" rel="noopener">{I['youtube']} More on YouTube</a></div>
<div class="filters reveal" data-arc-tools><label class="sr-only" for="arc-q">Search recordings</label><input id="arc-q" type="search" placeholder="Search a title, topic or scripture…" data-arc-search>
<button class="chip" type="button" data-arc-kind="all" aria-pressed="true">All {n_pod + n_sab}</button><button class="chip" type="button" data-arc-kind="podcast" aria-pressed="false">2 Minutes · {n_pod}</button><button class="chip" type="button" data-arc-kind="shabbat" aria-pressed="false">Shabbat services · {n_sab}</button>
<label class="sr-only" for="arc-sort">Sort recordings</label><select id="arc-sort" class="chip sort" data-arc-sort><option value="new">Newest first</option><option value="old">Oldest first</option><option value="az">Title A–Z</option></select></div>
<p class="muted small" data-arc-count aria-live="polite"></p>
<div class="arc-list" data-arc-list>{''.join(rows)}</div><p class="empty" data-arc-empty hidden>No recording matches that search.</p></div></section>
{next_steps(r, [('teachings/', 'Shabbat teachings', 'Read the services Sabbath by Sabbath.'), ('spiritual-intent/', 'Spiritual Intent', 'Books for careful, Christ-centred study.'), ('encounters/', 'Gather with us', 'Three weekly encounters.')])}'''

def shabbat_audio(r):
    rec = [x for x in reversed(SERVICES) if x.get('audio')]
    if not rec:
        return ''
    rows = ''.join(f'''<article class="card svc-row"><div class="svc-meta"><div class="kicker">Shabbat {x['n']} · {dt.date.fromisoformat(x['iso']).strftime('%-d %B %Y')}</div>
<h3><a class="card-link" href="{r}teachings/{x['slug']}/">{e(x['title'])}</a></h3><div class="focus">{e(x['focus'])}</div></div>{player(r, x)}</article>''' for x in rec)
    return f'''<section class="section tight" id="shabbat"><div class="container"><div class="section-head reveal"><div><div class="eyebrow">Shabbat services · audio</div><h2>Take the Sabbath <em>with you.</em></h2>
<p class="lead">Full Shabbat services celebrating the Son. Listen on the way, at work or at rest — each one also opens as a written teaching.</p></div><a class="textlink" href="{r}teachings/">The teaching library <span class="arr">→</span></a></div>
<div class="grid reveal-stagger">{rows}</div></div></section>'''

def episode_page(ep, idx):
    def body(r):
        prev = EPISODES[idx + 1] if idx + 1 < len(EPISODES) else None
        nxt = EPISODES[idx - 1] if idx > 0 else None
        pager = '<div class="pager">' + (f'<a class="card" href="{r}{prev["path"]}"><div class="kicker">← Earlier</div><h3>{e(prev["title"])}</h3></a>' if prev else '<span></span>') + (f'<a class="card next" href="{r}{nxt["path"]}"><div class="kicker">Later →</div><h3>{e(nxt["title"])}</h3></a>' if nxt else '<span></span>') + '</div>'
        return page_hero(r, [('listen/2-minutes/', 'Listen'), (None, ep['title'])], f"2 Minutes Podcast · {ep['pretty']}", e(ep['title']), e(ep['blurb']), side=False) + f'''
<section class="section tight" style="padding-top:0"><div class="container"><article class="card ep feature-player reveal" style="--ax:30%"><div class="art" aria-hidden="true" style="height:200px"><span class="rings"></span><span class="art-dur">{ep['label']}</span><span class="art-word">{e(ep['word'])}</span></div>{player(r, ep, feature=True)}</article>
{pager}</div></section>
{next_steps(r, [('listen/2-minutes/', 'All episodes', 'The full listening room.'), ('teachings/', 'Shabbat teachings', 'Thirteen Sabbaths celebrating the Son.'), ('encounters/', 'Gather with us', 'Join a weekly encounter.')])}'''
    page(ep['path'], f"{ep['title']} · 2 Minutes Podcast", ep['blurb'], body, 'listen',
         {'@type': 'PodcastEpisode', 'name': ep['title'], 'description': ep['blurb'], 'datePublished': ep['date'], 'timeRequired': f"PT{ep['seconds']}S", 'url': SITE_URL + ep['path'], 'inLanguage': 'en',
          'associatedMedia': {'@type': 'AudioObject', 'contentUrl': SITE_URL + ep['audio'], 'encodingFormat': 'audio/mpeg', 'duration': f"PT{ep['seconds']}S"},
          'partOfSeries': {'@type': 'PodcastSeries', 'name': '2 Minutes Podcast', 'url': SITE_URL + 'listen/2-minutes/'},
          'publisher': {'@type': 'Organization', 'name': 'Country Ministries International'}})

# ------------------------------------------------------------------ TEACHINGS
def teachings(r):
    latest = [s for s in SERVICES if s['iso'] <= SACRED.isoformat()]
    feat = latest[-1]['n'] if latest else 1
    cards = ''.join(svc_card(r, s, s['n'] == feat) for s in SERVICES)
    arc = [('1–3', 'Who the Son is', 'Before all things, made flesh, declared by the Father.'), ('4–7', 'His life among us', 'Testing, teaching, service and shepherding.'),
           ('8–9', 'Cross and empty tomb', 'The Lamb slain, the firstborn from the dead.'), ('10–12', 'His present ministry', 'Enthroned, interceding, joined to His body.'), ('13', 'His appearing', 'Closing the quarter in expectation.')]
    return page_hero(r, [(None, 'Teachings')], 'Shabbat teachings · First quarter of 5787', 'Celebrating <em>the Son.</em>',
                     'Thirteen Sabbaths moving in a single arc through the person and work of Christ Jesus. The quarter stands under the Tav — the sign, the seal and the mark of ownership — and its one question is whose you are. Every service answers it in the Son.') + f'''
<section class="section tight" style="padding-top:0"><div class="container"><div class="movement-bar reveal" style="grid-template-columns:repeat(5,1fr)">{''.join(f'<div>Shabbat {a}<small>{b} — {c}</small></div>' for a, b, c in arc)}</div></div></section>
<section class="section tight"><div class="container">
<div class="filters reveal"><label class="sr-only" for="teach-q">Search teachings</label><input id="teach-q" type="search" placeholder="Search a title, theme or scripture…" data-teach-search>
<button class="chip" type="button" data-filter="all" aria-pressed="true">All 13</button><button class="chip" type="button" data-filter="shared" aria-pressed="false">Shared</button><button class="chip" type="button" data-filter="upcoming" aria-pressed="false">Coming</button></div>
<div class="teach-grid reveal-stagger">{cards}</div><p class="empty" data-empty hidden>No teaching matches that search.</p></div></section>
{next_steps(r, [('encounters/shabbat-service/', 'Join Shabbat', 'Saturdays at 8:00 AM WAT.'), ('listen/2-minutes/', '2 Minutes Podcast', 'A short word for every day.'), ('year-5787/', 'The Year 5787', 'Tav, Shin, Pe, Zayin.')])}'''

def teaching_page(s, idx):
    def body(r):
        prev = SERVICES[idx - 1] if idx > 0 else None
        nxt = SERVICES[idx + 1] if idx + 1 < len(SERVICES) else None
        school = ''.join(f'<h3><span class="rn">{x["n"]}.</span>{e(x["title"])}</h3><p>{e(x["text"])}</p>' for x in s['school'])
        theme = ''.join(f'<p>{e(p)}</p>' for p in s['theme'])
        pager = '<div class="pager">' + (f'<a class="card" href="{r}teachings/{prev["slug"]}/"><div class="kicker">← Shabbat {prev["n"]}</div><h3>{e(prev["title"])}</h3></a>' if prev else '<span></span>') + (f'<a class="card next" href="{r}teachings/{nxt["slug"]}/"><div class="kicker">Shabbat {nxt["n"]} →</div><h3>{e(nxt["title"])}</h3></a>' if nxt else '<span></span>') + '</div>'
        date = dt.date.fromisoformat(s['iso']).strftime('%A, %-d %B %Y')
        return page_hero(r, [('teachings/', 'Teachings'), (None, f"Shabbat {s['n']}")], f"Shabbat service {s['n']} of 13 · {s['hebrew']} 5787 · Sequence {s['seq']}", e(s['title']), e(s['kicker']),
                         ([('#listen', 'Listen')] if s.get('audio') else []) + [('#theme', 'The theme'), ('#school', 'School of Scriptures'), ('#table', 'The Table'), ('#summons', 'The summons')], side=False) + f'''
<section class="section tight" style="padding-top:0"><div class="container article">
<div class="prose reveal">
{svc_player(r, s)}
<p class="pull">{e(s['implication'])}</p>
<h2 id="theme">The <em>theme.</em></h2>{theme}
<h2 id="school">The School of <em>Scriptures.</em></h2>{school}
<h2 id="table">The <em>Table.</em></h2><div class="table-elements"><div><b>At the breaking of the bread</b>{e(s['bread'])}</div><div><b>At the cup</b>{e(s['cup'])}</div></div>
<div class="summons" id="summons" style="margin-top:40px"><div class="kicker">The summons for the new week</div><p>{e(s['summons'])}</p></div>
{pager}</div>
<aside class="aside reveal"><div class="panel"><div class="letter-big hebrew" aria-hidden="true">{gem(s['seq'])}</div><div class="facts small" style="margin-top:14px"><div><span>Date</span><b>{date}</b></div><div><span>Hebrew date</span><b>{s['hebrew']} 5787</b></div><div><span>Sequence</span><b>{s['seq']} of 385</b></div><div><span>Word in Gold</span><b>{e(s['focus'])}</b></div><div><span>Supporting texts</span><b>{e(s['supporting'])}</b></div></div></div>
{share_box(s['title'], r + 'teachings/' + s['slug'] + '/')}
<a class="button wa" href="{LINKS['shabbat']}" target="_blank" rel="noopener">{I['whatsapp']} Join Shabbat Service</a></aside></div></section>'''
    page(f"teachings/{s['slug']}/", f"{s['title']} · Shabbat {s['n']}", f"{s['title']} — Shabbat service {s['n']} of 13, {s['date']}. {s['focus']}.", body, 'teachings',
         dict({'@type': 'Article', 'headline': s['title'], 'description': f"{s['kicker']}. {s['focus']}.", 'datePublished': s['iso'], 'inLanguage': 'en',
               'image': SITE_URL + 'assets/og-image.png', 'about': 'Jesus Christ', 'keywords': f"Shabbat, {s['title']}, {s['focus']}, Believers Country, CMI",
               'author': {'@type': 'Organization', 'name': 'Country Ministries International', 'url': SITE_URL},
               'publisher': {'@type': 'Organization', 'name': 'Country Ministries International', 'logo': {'@type': 'ImageObject', 'url': SITE_URL + 'assets/favicon-512.png'}},
               'mainEntityOfPage': SITE_URL + f"teachings/{s['slug']}/"},
              **({'audio': {'@type': 'AudioObject', 'name': s['title'], 'contentUrl': SITE_URL + s['audio'], 'encodingFormat': 'audio/mpeg', 'duration': f"PT{s['seconds']}S", 'uploadDate': s['iso']}} if s.get('audio') else {})))

# ------------------------------------------------------------------ SPIRITUAL INTENT
BOOKS = [('scriptural-wealth', 'Scriptural Wealth', 'Wealth and faithful stewardship under Christ.'), ('how-to-receive-from-god', 'How to Receive From God', 'Receiving from God and understanding the Source.'),
         ('scriptural-pattern-of-debt', 'The Scriptural Pattern of Debt and the Way Out', 'A scriptural examination of debt and the way out.'), ('investment-and-enjoyment', 'Investment & Enjoyment', 'Seed for sowing, bread for eating, and wise stewardship.')]

def spiritual(r):
    return page_hero(r, [(None, 'Spiritual Intent')], 'Books · Formation · Study', 'Scripture, read in <em>the light of Christ.</em>',
                     'Spiritual Intent examines the whole counsel of Scripture in the light of the Son, the new creation and His finished work.', [('#approach', 'The approach'), ('#collections', 'The collections')]) + f'''
<section class="section tight" id="approach"><div class="container grid g2" style="gap:clamp(30px,6vw,80px)"><div class="reveal"><div class="eyebrow">The approach</div><h2>Christ the foundation. <em>Scripture the witness.</em></h2></div>
<div class="reveal"><p class="lead">A literary and teaching identity attentive to context, fulfilment, the finished work of Christ and the life of the believer as a new creation.</p><p class="muted">Connected to CMI’s doctrinal framework, its written works make room for extended argument, confirmation passages and practical application — far beyond a caption or an isolated quotation.</p></div></div></section>
<section class="section tight" id="collections"><div class="container grid g2 reveal-stagger">
<article class="card" style="padding:clamp(26px,3vw,42px)"><div class="kicker">Collection · Four books</div><h2 style="margin:10px 0 14px">Money <em>Under God.</em></h2><p>Studies on provision, receiving, debt, investment and enjoyment.</p><div class="books" style="margin:20px 0">{''.join(f'<span class="book"><img src="{r}assets/books/money-under-god/{b}.png" alt="{e(t)} cover" width="256" height="405" loading="lazy" decoding="async"></span>' for b, t, _ in BOOKS)}</div><a class="button primary" style="position:relative;z-index:2;align-self:flex-start" href="{r}spiritual-intent/books/">{I['book']} Explore the books</a></article>
<article class="card" style="padding:clamp(26px,3vw,42px)"><div class="kicker">Series in development</div><h2 style="margin:10px 0 14px">The Business of <em>the Believer.</em></h2><p>Practical scriptural wisdom about work and business, drawn through the created order — the seven days of Genesis as a pattern for light, structure, fruit, seasons, reach, stewardship and rest.</p>
<ul class="clean ticks"><li>Yom Rishon — name what must become visible</li><li>Yom Sheni — build structure and boundaries</li><li>Yom Shlishi — plant, produce and measure fruit</li><li>Shabbat — cease, review and receive</li></ul></article>
</div></section>
{next_steps(r, [('spiritual-intent/books/', 'Money Under God', 'The four-book collection.'), ('teachings/', 'Shabbat teachings', 'Christ-centred studies, Sabbath by Sabbath.'), ('listen/2-minutes/', '2 Minutes Podcast', 'A short word for today.')])}'''

def books(r):
    cards = ''.join(f'<article class="card"><span class="book" style="transform:none;margin:-6px -6px 20px">{""}<img src="{r}assets/books/money-under-god/{b}.png" alt="{e(t)} cover" width="256" height="405" loading="lazy" decoding="async"></span><div class="kicker">Book 0{i+1}</div><h3>{e(t)}</h3><p>{d}</p></article>' for i, (b, t, d) in enumerate(BOOKS))
    return page_hero(r, [('spiritual-intent/', 'Spiritual Intent'), (None, 'Money Under God')], 'Spiritual Intent · Collection', 'Money <em>Under God.</em>',
                     'Four distinct books on wealth, receiving, debt, and investment and enjoyment — examined through Scripture, in the light of Christ.') + f'''
<section class="section tight"><div class="container"><div class="grid g4 reveal-stagger">{cards}</div></div></section>
<section class="section tight"><div class="container"><div class="callband reveal"><div><h2>Be first to <em>read them.</em></h2><p>Join the Believers Country community to hear when the collection is released.</p></div><div class="cta"><a class="button gold" href="{LINKS['school']}" target="_blank" rel="noopener">{I['whatsapp']} Join School of Scriptures</a></div></div></div></section>'''

# ------------------------------------------------------------------ YEAR 5787
def year(r):
    cards = ''.join(f'<article class="card letter-card"><div class="heb hebrew" aria-hidden="true">{h}</div><div class="val">{n} · {v}</div><h3>{t}</h3><p>{d}</p></article>' for h, n, v, t, d in YEAR_LETTERS)
    mv = ''.join(f'<div data-m="{m}">{m}<small>{a} · {b}</small></div>' for m, a, b in MOVES)
    months = [('Tishrei', 30, 'Sep 12 – Oct 11', 'Beginnings, kingship and covenant'), ('Cheshvan', 30, 'Oct 12 – Nov 10', 'Quiet building and consistency'), ('Kislev', 30, 'Nov 11 – Dec 10', 'Light in darkness; guard the vision'),
              ('Tevet', 29, 'Dec 11 – Jan 8', 'Guarding the eyes and the inner life'), ('Shevat', 30, 'Jan 9 – Feb 7', 'Renewal; the rising of sap'), ('Adar I', 30, 'Feb 8 – Mar 9', 'The added month: extension'),
              ('Adar II', 29, 'Mar 10 – Apr 7', 'Joy, reversal, hidden providence'), ('Nisan', 30, 'Apr 8 – May 7', 'Redemption and new beginnings'), ('Iyyar', 29, 'May 8 – Jun 5', 'Healing and steady counting'),
              ('Sivan', 30, 'Jun 6 – Jul 5', 'Revelation; the giving of the word'), ('Tammuz', 29, 'Jul 6 – Aug 3', 'Guard the covenant'), ('Av', 30, 'Aug 4 – Sep 2', 'Comfort; mourning turned to gladness'), ('Elul', 29, 'Sep 3 – Oct 1', 'Return and preparation for 5788')]
    mrows = ''.join(f'<article class="card"><div class="kicker">{d} · {n} days</div><h3>{m}</h3><p>{t}</p></article>' for m, n, d, t in months)
    disc = [('Sealed ownership', 'Tav · first quarter', 'Once a week, name aloud what has first claim on you — measured by what receives your attention on waking.'),
            ('The polished arrow', 'Shin · winter', 'Submit one area of competence to correction by someone qualified to give it. Polishing is friction from another hand.'),
            ('The told story', 'Pe · spring', 'Tell someone younger, in specific terms, what God has done for you — at least once a month.'),
            ('The sheathed edge', 'Zayin · summer', 'No correction delivered in the first hour of wanting to — and none to a person you have not recently blessed by name.')]
    return page_hero(r, [(None, 'The Year 5787')], 'The Hebrew year 5787 · <span class="hebrew">ה׳תשפ״ז</span>', 'The year of the <em>crowned mouth.</em>',
                     'A leap year of 385 days — exactly 55 weeks, thirteen months with Adar I and Adar II. It opened on Shabbat, 12 September 2026, and closes on 1 October 2027.',
                     [('#letters', 'The letters'), ('#movements', 'Four movements'), ('#months', 'Thirteen months'), ('#disciplines', 'Disciplines')]) + f'''
<section class="section tight"><div class="container"><div class="panel reveal" style="padding:clamp(24px,3vw,40px);display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:24px">
<div><div class="today-label"><span class="live-dot"></span> Today in 5787</div><div class="hdate"><span data-hdate></span><span class="hebrew" data-hdate-heb></span></div></div>
<div class="today-meta"><b data-hweekday></b><br><span data-hcivil></span><br><span data-hseq></span></div><div class="today-meta"><b data-hmovement></b><br><span data-hboundary></span></div></div></div></section>
<section class="section tight" id="letters"><div class="container"><div class="section-head reveal"><div><div class="eyebrow">787 = 400 + 300 + 80 + 7</div><h2>Mark, fire, <em>mouth, sword.</em></h2><p class="lead">What distinguishes 5787 within its century is Pe and Zayin — the mouth and the sword. 5786 was the mouth nailed; 5787 is the same mouth given an edge and a crown.</p></div></div>
<div class="letters reveal-stagger">{cards}</div></div></section>
<section class="section tight"><div class="container"><div class="summons reveal"><div class="kicker">Isaiah 49:2 · the governing word</div><p>The servant’s mouth is made like a sharp sword and hidden in the shadow of His hand. A year of the mouth is not a year of volume: the arrow is polished, then hidden, and released only by the hand that owns it.</p></div></div></section>
<section class="section tight" id="movements"><div class="container"><div class="section-head reveal"><div><div class="eyebrow">The year in four movements</div><h2>Where we <em>stand now.</em></h2></div></div><div class="movement-bar reveal">{mv}</div></div></section>
<section class="section tight" id="months"><div class="container"><div class="section-head reveal"><div><div class="eyebrow">Thirteen months</div><h2>Move with <em>the seasons.</em></h2></div></div><div class="grid g4 reveal-stagger">{mrows}</div></div></section>
<section class="section tight" id="disciplines"><div class="container"><div class="section-head reveal"><div><div class="eyebrow">The year’s four disciplines</div><h2>One discipline <em>per letter.</em></h2></div></div>
<div class="grid g4 reveal-stagger">{''.join(f'<article class="card"><div class="kicker">{b}</div><h3>{a}</h3><p>{c}</p></article>' for a, b, c in disc)}</div>
<p class="muted small reveal" style="margin-top:24px">Hebrew letters and calendar patterns are a devotional and interpretive lens for prayer and intention. They do not outrank explicit Scripture and are not used to predict events.</p></div></section>'''

# ------------------------------------------------------------------ CONTACT / LEGAL
def contact(r):
    order = sorted(ENCOUNTERS, key=lambda x: {'sat': 0, 'wed': 1, 'thu': 2}[x['key']])
    cards = ''.join(f'''<article class="card join-card"><div class="join-top"><div class="icon-letter hebrew" aria-hidden="true">{x['letter']}</div>
<div class="join-when"><b>{x['day']}</b><span>{x['time']} WAT</span></div></div>
<h3>{x['title']}</h3><p>{x['short']}</p><div class="next" data-next="{x['key']}">Every {x['day']}</div>
<div class="join-actions"><a class="button wa" href="{x['link']}" target="_blank" rel="noopener">{I['whatsapp']} Join the group</a><button class="chip" type="button" data-ics="{x['key']}">{I['cal']} Add to calendar</button></div>
{'<span class="badge latest join-flag">Best place to begin</span>' if x['key'] == 'sat' else ''}</article>''' for x in order)
    steps = [('Choose a community', 'Shabbat Service is the best place to begin. The Wednesday and Thursday groups are for study and prayer.'),
             ('Say hello', 'Introduce yourself in the group. Questions about faith, prayer requests and visiting are all welcome there.'),
             ('Join a gathering', 'Joining details for each encounter are shared in its group before it begins.'),
             ('Keep listening', 'Return each day for the 2 Minutes Podcast, and watch past gatherings on YouTube.')]
    st = ''.join(f'<article class="card step-card"><span class="num">0{i+1}</span><h3>{a}</h3><p>{b}</p></article>' for i, (a, b) in enumerate(steps))
    return page_hero(r, [(None, 'Contact')], 'Connect with us', 'We would love to <em>welcome you.</em>',
                     'The quickest way to reach Believers Country is through our WhatsApp communities. Join the one that fits your week, introduce yourself, and someone will respond.',
                     [('#gather', 'Join a gathering'), ('#give', 'Give · Partner · Support'), ('#steps', 'First steps')], aside=portrait(r)) + f'''
<section class="section tight" id="gather" style="padding-top:0"><div class="container"><div class="section-head reveal"><div><h2>Join a <em>gathering.</em></h2><p class="lead">Each weekly encounter has its own WhatsApp community, where joining details and notices are shared.</p></div></div>
<div class="grid g3 reveal-stagger">{cards}</div>
<div class="grid g2 bands"><a class="card yt-band reveal" href="{LINKS['youtube']}" target="_blank" rel="noopener"><span class="ico">{I['youtube']}</span><span><b>Watch on YouTube</b><small>Past gatherings and teachings · @believerscountry</small></span><span class="circle">{I['up']}</span></a>
<a class="card yt-band mail-band reveal" href="mailto:{EMAIL}"><span class="ico">{I['mail']}</span><span><b>Email us</b><small>{EMAIL.replace('@', '<wbr>@')}</small></span><span class="circle">{I['up']}</span></a></div></div></section>
{give_section()}
<section class="section tight" id="steps"><div class="container"><div class="section-head reveal"><h2>Your first <em>steps.</em></h2></div><div class="grid g4 reveal-stagger">{st}</div></div></section>'''

def give_section():
    ways = [('Offerings', 'Your regular giving and thanksgiving, offered as worship to the Lord (2 Corinthians 9:7).', 'Offering'),
            ('Venue projects', 'Helping to secure and prepare places where believers gather, learn and are sent.', 'Venue'),
            ('Country projects', 'Commonwealth care, Country Vanguard outreach and the work of the four streams.', 'Project')]
    w = ''.join(f'<article class="card give-way"><div class="icon-letter" aria-hidden="true">{I["gift"]}</div><h3>{a}</h3><p>{b}</p><span class="badge">Narration: {c}</span></article>' for a, b, c in ways)
    rows = ''.join(f'''<div class="acct"><span class="cur" aria-hidden="true">{sym}</span><span class="acct-l"><b>{name}</b><small>{code} account</small></span>
<span class="acct-n">{num}</span><button class="chip" type="button" data-copy="{num}" aria-label="Copy {name} account number">{I['copy']} <span>Copy</span></button></div>''' for name, sym, code, num in GIVING['accounts'])
    return f'''<section class="section tight" id="give"><div class="container"><div class="section-head reveal"><div><h2>Give, partner, <em>support.</em></h2>
<p class="lead">Every gift is received as worship and stewarded for the life and mission of Believers Country. Choose what you are giving towards, then use the account for your currency.</p></div></div>
<div class="give-grid"><div class="grid reveal-stagger">{w}</div>
<div class="panel give-panel reveal"><div class="kicker">Bank transfer</div><h3>{GIVING['name']}</h3><p class="muted small" style="margin:4px 0 16px">{GIVING['bank']}</p>
<div class="accts">{rows}</div><p class="muted small give-note">Add a narration such as <b>Offering</b>, <b>Venue</b> or <b>Project</b> so your gift goes where you intend. To partner regularly or share a testimony, message us in the Shabbat Service group.</p>
<a class="button wa" href="{LINKS['shabbat']}" target="_blank" rel="noopener">{I['whatsapp']} Tell us about your gift</a></div></div></div></section>'''

def legal(kind):
    def body(r):
        if kind == 'privacy':
            secs = [('What we collect', 'This website does not ask you to create an account and has no sign-up, payment or contact forms. We do not run advertising or tracking cookies.'),
                    ('Your preferences', 'Your Day, Night or Auto choice is saved in your own browser’s local storage so the site remembers it. It never leaves your device, and you can clear it at any time through your browser settings.'),
                    ('Audio and downloads', 'Podcast audio is served from this website when you press play or download. Your browser makes the request in the ordinary way; we do not build listening profiles.'),
                    ('Third-party services', 'Fonts are loaded from Google Fonts, and the site is hosted on GitHub Pages; both may receive standard technical information such as your IP address and browser type. When you follow a link to WhatsApp, YouTube or a social network to share, that service’s own privacy policy applies.'),
                    ('Children', 'This website is suitable for all ages and does not knowingly collect personal information from anyone.'),
                    ('Changes and contact', 'We may update this policy as the website grows; the date below shows the latest revision. For any privacy question, reach us through one of our WhatsApp communities on the Contact page.')]
            title, h1, lead = 'Privacy Policy', 'Privacy <em>Policy.</em>', 'How Believers Country handles information when you visit this website.'
        else:
            secs = [('Using this website', 'Believers Country provides this website to share the life, teaching and gatherings of Country Ministries International. By using it you agree to these terms.'),
                    ('Our content', 'Unless otherwise stated, the text, teachings, audio recordings, book covers, logo and design are © Country Ministries International. All rights reserved.'),
                    ('Personal and ministry use', 'You are welcome to listen, download podcast episodes for personal listening, and share links to any page. Please do not republish, sell, alter or present our recordings, teachings or artwork as your own without written permission.'),
                    ('Scripture', 'Scripture references and short quotations remain the property of their respective translation publishers and are used for teaching and comment.'),
                    ('External links', 'Links to WhatsApp, YouTube and other services are provided for convenience. Those services are governed by their own terms.'),
                    ('No guarantees', 'Teaching on this site is offered for spiritual formation. It is not legal, medical or financial advice, and Commonwealth is a ministry of care, not an offer of financial return. We work to keep information accurate, and gathering times may occasionally change.'),
                    ('Changes', 'We may revise these terms from time to time. Continued use of the site means you accept the current version.')]
            title, h1, lead = 'Terms of Use', 'Terms of <em>Use.</em>', 'The simple terms for using the Believers Country website and its content.'
        s = ''.join(f'<h2 style="font-size:clamp(26px,3vw,34px);margin:40px 0 12px">{a}</h2><p>{b}</p>' for a, b in secs)
        other = ('terms/', 'Terms of Use') if kind == 'privacy' else ('privacy/', 'Privacy Policy')
        return page_hero(r, [(None, title)], title, h1, lead, side=False) + f'''
<section class="section tight" style="padding-top:0"><div class="container article"><div class="prose reveal">{s}<p class="muted small" style="margin-top:40px">Last updated {NOW.strftime('%-d %B %Y')}.</p></div>
<aside class="aside reveal"><div class="panel"><div class="kicker">Also read</div><p style="margin:10px 0 0"><a class="textlink" href="{r}{other[0]}">{other[1]} <span class="arr">→</span></a></p></div></aside></div></section>'''
    title = 'Privacy Policy' if kind == 'privacy' else 'Terms of Use'
    page(f'{kind}/', title, f'Believers Country {title}.', body)

# ------------------------------------------------------------------ build
def main():
    page('', 'Believers Country', 'Believers Country — Country Ministries International. Weekly encounters, Shabbat teachings celebrating the Son, the 2 Minutes Podcast and the Spiritual Intent books.', home, 'home',
         None)
    page('about/', 'About', 'Who we are: a people belonging to the Father, a life received in the Son, a country expressed through His Spirit.', about, 'about')
    page('ministries/', 'Ministries', 'The four streams of CMI: Believers Country, School of Scriptures, Commonwealth and Country Vanguard.', ministries, 'ministries')
    for i, s in enumerate(STREAMS): stream_page(s, i)
    page('encounters/', 'Weekly encounters', 'School of Scriptures on Wednesday, Ministering to the LORD on Thursday and Shabbat Service on Saturday — join on WhatsApp.', encounters, 'encounters')
    for i, x in enumerate(ENCOUNTERS): encounter_page(x, i)
    page('listen/2-minutes/', '2 Minutes Podcast', 'Short original messages from Believers Country. Listen today, download or share.', listen, 'listen',
         {'@type': 'PodcastSeries', 'name': '2 Minutes Podcast', 'description': 'Short original messages from Believers Country, one for each day.', 'url': SITE_URL + 'listen/2-minutes/', 'inLanguage': 'en',
          'image': SITE_URL + 'assets/og-image.png', 'author': {'@type': 'Organization', 'name': 'Country Ministries International'}})
    for i, ep in enumerate(EPISODES): episode_page(ep, i)
    page('teachings/', 'Shabbat teachings', 'Celebrating the Son — thirteen Shabbat teachings for the first quarter of 5787.', teachings, 'teachings')
    for i, s in enumerate(SERVICES): teaching_page(s, i)
    page('spiritual-intent/', 'Spiritual Intent', 'Scripture read in the light of Christ: the Money Under God collection and The Business of the Believer.', spiritual, 'spiritual-intent')
    page('spiritual-intent/books/', 'Money Under God', 'Four books on wealth, receiving, debt, investment and enjoyment, examined through Scripture.', books, 'spiritual-intent')
    page('year-5787/', 'The Year 5787', 'The Hebrew year 5787 — Tav, Shin, Pe, Zayin: the year of the crowned mouth. Four movements, thirteen months, today’s sequence.', year, 'year')
    page('contact/', 'Contact', 'Connect with Believers Country through our WhatsApp communities and YouTube channel.', contact)
    legal('privacy'); legal('terms')
    # legacy route kept as a redirect
    (ROOT / 'ministries/country-commonwealth/index.html').write_text('<!DOCTYPE html><meta charset="utf-8"><title>Commonwealth | Believers Country</title><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=../commonwealth/"><link rel="canonical" href="https://believerscountry.org/ministries/commonwealth/"><p>Moved to <a href="../commonwealth/">Commonwealth</a>.</p>')
    def prio(p):
        if p == '': return '1.0', 'daily'
        if p in ('listen/2-minutes/', 'encounters/', 'teachings/'): return '0.9', 'daily' if p.startswith('listen') else 'weekly'
        if p.count('/') == 1: return '0.8', 'monthly'
        if p.startswith('privacy') or p.startswith('terms'): return '0.3', 'yearly'
        return '0.7', 'monthly'
    today = NOW.date().isoformat()
    sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        f'<url><loc>{SITE_URL}{p}</loc><lastmod>{today}</lastmod><changefreq>{prio(p)[1]}</changefreq><priority>{prio(p)[0]}</priority></url>\n' for p in PAGES) + '</urlset>\n'
    (ROOT / 'sitemap.xml').write_text(sitemap)
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}sitemap.xml\n')
    page('', 'Page not found', 'This page could not be found.', lambda r: page_hero(r, [(None, 'Not found')], 'Page not found', 'This path has <em>no road yet.</em>', 'The page you were looking for has moved or does not exist. Start again from home, or step into one of the gatherings.') + next_steps(r, [('', 'Home', 'Return to the beginning.'), ('encounters/', 'Weekly encounters', 'Join us this week.'), ('listen/2-minutes/', 'Listen', 'Today’s 2 minutes.')]), extra_head='<base href="/">', out_file='404.html')
    print(f'Built {len(PAGES)} pages · sacred day {SACRED} · today’s episode: {episode_for(SACRED)["title"]}')

if __name__ == '__main__':
    main()
