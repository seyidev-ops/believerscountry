**Standard V1 status:** Four source recordings have been converted to MP3 and integrated into the episode library. The site stays noindex pending official public domain and launch verification.

# BELIEVERS COUNTRY — SEO, AEO & GEO LAUNCH GATE

**Status:** Ready for technical implementation, **not** claiming current public crawlability. The concept uses `robots=noindex,nofollow` deliberately. The public domain has not been supplied; do not invent canonical URLs or a production sitemap.

## Site architecture and findability

- Preserve direct routes and descriptive breadcrumbs: `/`, `/about/`, `/ministries/[stream]/`, `/encounters/[series]/`, `/listen/2-minutes/`, `/spiritual-intent/`, `/spiritual-intent/books/`, `/teachings/`.
- Server-render genuine titles, descriptions, H1, H2, accessible navigation, dates and page content. Avoid requiring JavaScript to reveal essential copy.
- Generate real absolute canonical tags for each indexable route once the correct domain is confirmed; do not canonicalize all pages to the homepage.
- Generate `sitemap.xml` from published canonical URLs and `robots.txt` from the final production staging policy; only remove `noindex` after authorization.
- Create Open Graph and social share graphics with the **exact supplied logo**, verified artwork and matching page description; provide alt text and minimum image metadata.

## Structured data templates (publish only when facts exist)

| Page | Eligible types | Data needed |
|---|---|---|
| CMI landing | `Organization`, `WebSite`, `WebPage` | Valid legal/display name, exact domain, real public links/contact |
| Ministry stream | `AboutPage` / `WebPage` + `BreadcrumbList` | Verified programme and identity text |
| Weekly encounter | `Event` for specific dated occurrences; `EventSeries` if appropriate | Actual dates, time zone, real attendance mode, status, join/location when public |
| 2 Minutes Podcast | `PodcastSeries`, `PodcastEpisode`, `AudioObject` | Four real MP3 recordings and verified titles/durations now present; public domain, speaker, dates, transcripts and RSS pending |
| Spiritual Intent and books | `Book`, `CreativeWorkSeries`, `BreadcrumbList` | Original official covers, titles, authors, ISBN, formats and verified dates |
| Published teaching | `Article` / `CreativeWork` as appropriate | Actual text, author, date, citations, related Scripture |

Avoid using `Offer`, `AggregateRating`, `Review`, `FAQPage` or `LocalBusiness` markup without genuinely corresponding source facts and valid eligibility.

## Content designed for search and AI-assisted discovery

1. Give each ministry its own precise explanatory identity, linked from the CMI overview and homepage.
2. Give each encounter its own practical answer to "what happens, when, how to attend?", and maintain status for changes or cancellations.
3. Four genuine MP3 recordings are already integrated. Add accurate transcripts, approved speaker credits, episode dates, Scriptures and related teaching only after verification; do not invent them.
4. Make full approved teachings searchable by title, Scripture reference, topic, date and series; keep their complete reasoning instead of excerpt-only pages.
5. Give each actual book a canonical page with consistent author/title, edition, availability and approved excerpt; preserve original imagery.
6. Provide editorial ownership, accurate updated dates, intentional cross-links and verifiable claims, without inventing statistics or testimony.
7. Use clear, semantically marked, visible HTML text and normal crawlable links. `llms.txt` may be explored as an optional document, but does not replace existing SEO controls or guarantee inclusion in AI tools.

## Delivery quality gates

- WCAG 2.2 AA review, labelled controls, keyboard navigation, visible focus, contrast and reduced-motion testing.
- Mobile navigation, all relative links, appearance persistence, no layout overflow and real event calendar files.
- Appropriate Core Web Vitals target monitoring: LCP <= 2.5 seconds, INP <= 200 ms, CLS <= 0.1 at the 75th percentile. These are **targets**, not measured performance claims for this offline preview.
- HTTPS, CSP, secure editorial access, backups, anti-spam if public forms are introduced, consent and Nigeria-relevant privacy review.
- Confirm `Organization`, events, podcasts and books with structured-data validators *after* public metadata exists.
- Regenerate assets and XML from the real production domain, remove concept/status labels only on approved pages.

## Specific content awaiting CMI approval

Approved logo; exact corporate spelling; source corpus/master theological review; working public domain; per-encounter join links, venue and operational time overrides; podcast MP3 audio attached (4 episodes); remaining metadata, artwork and transcripts; original book covers, full metadata, sales and release status; official contact and privacy/consent information.


## Approved visual identity asset integration (17 October 2026)
- Logo source: owner-supplied `CMI_Logo_All_Variants_v2(1).zip` with original black/white vectors and transparent 4096-pixel versions.
- Website header, footer, favicon: working preview now uses the attached source logo; Day black / Night white.
- Brand supporting identity (verbatim): “A people belonging to the Father. A life received in the Son. A country expressed through His Spirit.”
- In production, use these verified logo files for `Organization.logo` only after owner approves the production origin and absolute accessible media URL. Avoid claiming that structured data, canonical URLs or Open Graph deployment are already live.


## V7: Scripture and organization identity provenance

- Canonical editorial identity reference: CMI Master Leadership Corpus V2, section 2.3; the homepage foundation is Ephesians 2:18–22 (not the earlier John 1:4 panel).
- The sentences “Through the Son. By one Spirit. To the Father.” and “No longer strangers; together, members of God's household.” are editorial summaries, NOT verbatim Bible quotations or structured-data `quotation` values.
- Match About page copy, publisher metadata, HTML descriptions and structured data to the approved public identity without duplicating the identical slogan in titles, headings and footers unnecessarily.
- Distinguish historical `Country Ministry International` in V1 from configurable current visitor-facing `Country Ministries International`; do not assert legal identity without verification.


## Standard V1 update 01 — Daily podcast, social sharing and book-cover indexing
- Archive dates assigned editorially: Oct 17 / Oct 16 / Oct 15 / Oct 14 2026, newest first; original recording dates not inferred. Future episodes sort descending automatically by `archiveDate`.
- Four original book cover **crops** extracted from the latest identifiable 11 October 2026 Library image. Corrected second-book subtitle remains intact. Source and bounding boxes are recorded in `assets/books/money-under-god/SOURCE_MANIFEST.json`. The original collage includes pre-order text; use only the four cover crops without claiming a confirmed release or price.
- Episode pages contain unique titles/meta descriptions, PodcastEpisode and AudioObject schema without fabricated speakers/transcripts. `PodcastSeries` on archive. Do not claim transcript markup where no transcript is supplied.
- Share panel: native device sharing, X/Twitter, WhatsApp, Facebook, LinkedIn, Telegram, email and copy link. It forms real URLs from the user's visited page; file/localhost previews cannot be shared to external users.
- **Before indexing:** set actual HTTPS primary domain; issue absolute canonical, og:url, og:image and episode URLs, WebSite/Organization IDs and AudioObject contentUrls; generate sitemap.xml and public RSS 2.0 feed with absolute enclosure URLs; enable public site meta (remove `noindex,nofollow`) only after content, rights, legal identity and links are approved. Avoid relative URLs in any external feed.
- Use honest episode archive dates for `datePublished` only after these become the actual public publish dates. If initial publication happens after the backdated archive, distinguish that in CMS `firstPublishedAt` versus `archiveDate`.
- Optimize cover images with width/height, alt text, lazy loading and cache headers. Higher-resolution originals should replace crops only if the **same exact approved artwork** is supplied.
