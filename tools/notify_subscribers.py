#!/usr/bin/env python3
"""Tell the email list that today's 2 Minutes word is live.

Reads episodes.json, finds the episode for the current day (the day runs 6 PM to 6 PM,
West Africa Time) and posts it to the Apps Script web app. The script ignores an episode
it has already sent, so running this more than once is safe.
Needs NOTIFY_URL and NOTIFY_TOKEN in the environment; does nothing without them.
"""
import json, os, sys, urllib.parse, urllib.request, datetime as dt

url, token = os.environ.get('NOTIFY_URL', '').strip(), os.environ.get('NOTIFY_TOKEN', '').strip()
if not url or not token:
    print('Email notifications are not connected yet (NOTIFY_URL / NOTIFY_TOKEN missing). Skipping.')
    sys.exit(0)
now = dt.datetime.now(dt.timezone(dt.timedelta(hours=1)))
today = (now + dt.timedelta(days=1)).date() if now.hour >= 18 else now.date()
eps = json.load(open(os.path.join(os.path.dirname(__file__), '..', 'episodes.json')))
ep = next((e for e in eps if e['date'] == today.isoformat()), None)
if not ep:
    print(f'No episode dated {today}. Nothing to send.')
    sys.exit(0)
data = urllib.parse.urlencode({'action': 'notify', 'token': token, 'slug': ep['slug'], 'title': ep['title'],
                               'url': ep['url'], 'blurb': ep.get('blurb', ''), 'label': ep.get('label', '')}).encode()
with urllib.request.urlopen(urllib.request.Request(url, data=data, method='POST'), timeout=120) as r:
    print(f"{ep['title']} ({today}): {r.read().decode()[:200]}")
