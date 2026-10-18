# 2 Minutes Podcast — Daily Publishing Standard

This page sets the editorial arrangement beginning 17 October 2026 and applies to later podcast files added to the Believers Country website.

## Current daily archive
| Website archive date (Africa/Lagos, WAT) | Episode |
|---|---|
| 2026-10-17 | No Separation |
| 2026-10-16 | Proof that you know God |
| 2026-10-15 | What is your advantage as a believer |
| 2026-10-14 | Relationship With The Father |

These dates were assigned by instruction for the website archive. They are **not verified recording timestamps**. If exact first-publication dates become available, record those as a separate CMS field. Do not backdate a factual claim about recording/publication merely because an archive slot exists.

## Adding a future recording
1. Verify the audio file and permission to publish; convert a source OGG to MP3 with a consistent encoder (no added speech or altered spoken content).
2. Choose its **Africa/Lagos** website archive day and a canonical lowercase hyphenated slug; preserve the real title.
3. Store audio under `website/assets/audio/`, create its own `/listen/2-minutes/<slug>/` page, and add the entry to `website/content/site-content.json` with `archiveDate`, audio path, actual duration, download file, and source provenance.
4. Sort episodes descending by archive date; update the listening-room entries, latest homepage player, homepage chronological links, episode description, JSON-LD, sharing components and meta information.
5. When a real HTTPS origin is configured, regenerate RSS, sitemap, canonicals, OG and Twitter metadata by running `python tools/configure_public_site.py --site-url https://ACTUAL-DOMAIN` from the package root. Use `--publish` only after all launch reviews are complete.
6. Test every MP3 source, cover/image asset, time label, HTML route and social share link. If the original speaker/transcript is unknown, leave it unasserted.

**Important:** Standard V1 is a static HTML preview, not a connected publishing CMS. New episodes do **not** appear merely by copying an MP3 file. A future CMS implementation should automate steps 3–5 from a single episode publish operation, with the archive sorted by date descending.

## Public sharing
The **Share episode ↗** menu exposes device share, X/Twitter, WhatsApp, Facebook, LinkedIn, Telegram, email and copy URL. The preview deliberately disables outward sharing until a public HTTPS site origin has been configured and the site-public flag is enabled. This prevents distributing sandbox/file links that guests cannot access.
