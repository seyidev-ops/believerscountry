# Believers Country — CMI website

Live at https://believerscountry.org/ (GitHub Pages, `main` branch, repository root; custom domain set in `CNAME`).

## Design
"A new heaven and a new earth": **Day** is the new earth at first light (pearl sky, living gold, the river of life); **Night** is the new heaven (sapphire sky, stars, gold that does not go out). The horizon toggle in the header cycles Day → Night → Auto; Auto follows the device setting. The CMI mark levitates, turns at intervals, and its flame burns in animated gold. All motion respects *reduce motion*.

## Sacred time
The day runs **6:00 PM to 6:00 PM (WAT)**. The "Today" panel, the Hebrew date and sequence, the day's 2 Minutes episode and the teaching status all resolve against that boundary in the browser, so they change at 6 PM without a rebuild.

## Editing content
All pages are generated. Edit, then run:

```
python3 tools/build_site.py
```

- Podcast episodes: `EPISODES` in `tools/build_site.py` (MP3s in `assets/audio/`). Clean every new recording first: `python3 tools/clean_audio.py INPUT assets/audio/SLUG.mp3 "Title"` (removes background noise, evens loudness); for a Shabbat service add `--service` and save to `assets/audio/shabbat/SLUG.mp3`.
- Shabbat teachings: `content/shabbat-services-5787-q1.json` (extracted from the Q1 manuscript with `tools/extract_services.py`).
- Encounter times and WhatsApp links: `ENCOUNTERS` and `LINKS` in `tools/build_site.py`, and `SESSIONS` in `assets/app.js`.
- Styles: `assets/styles.css`; behaviour: `assets/app.js`.
