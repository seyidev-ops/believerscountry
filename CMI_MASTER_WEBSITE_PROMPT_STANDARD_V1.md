# Standard V1 Update 01 — Resolved source artwork, daily podcast calendar & social sharing (17 October 2026)

This update **supersedes older placeholder artwork and undated podcast instructions** in this prompt. Continue calling the site Standard Version 1.0; this is a dated maintenance update, not a new standard version.

**Spiritual Intent — Money Under God:** Source the book-cover panels from the newer 11 October 2026 original four-book collection image, rather than synthesizing artwork or using generic placeholder numbers. `assets/books/money-under-god/` contains four unmodified cropped cover panels; read `SOURCE_MANIFEST.json` for exact image attribution and crop bounds. The source composite proposes a December 17, 2026 launch; keep that date provisional until the ministry authorizes publication. Replace low-resolution crops with standalone original cover assets only when source-identical verified masters are provided.

**2 Minutes Podcast:** Four real MP3 episodes should display in **daily descending website archive order**, beginning on Saturday **17 October 2026** (No Separation), Friday 16 Oct (Proof that you know God), Thursday 15 Oct (What is your advantage as a believer), Wednesday 14 Oct (Relationship With The Father). These are editorial website archive dates, not asserted recording dates. New episodes must be entered with an explicit Africa/Lagos issue date, appear latest-first on the archive and update the homepage feed. Do not add dates to audio claims or invent speakers and transcripts.

**Sharing and discoverability:** Each podcast card and episode page has a **Share episode** control, with native device share, X/Twitter, WhatsApp, Facebook, LinkedIn, Telegram, email and copy link. Homepage highlights the latest and links to the daily archive. Share targets must use the canonical absolute HTTPS episode URL at public launch (in local file preview no publicly valid share links exist). Generate unique SEO social metadata, verified schema.org PodcastEpisode/AudioObject metadata, RSS podcast feed, XML sitemap, actual canonical URLs, correct Open Graph/Twitter images and `robots` before site indexing. Keep `noindex` while staged. Do not invent a domain, public RSS or unsupported transcript.

---

# BELIEVERS COUNTRY — STANDARD WEBSITE V1.0 (CANONICAL BUILD PROMPT)

**Baseline status:** This is the first standard release of the *website specification*, derived from the approved V7 interactive website on 17 October 2026. The corpus remains **CMI Master Leadership Corpus V2.0** as an independently versioned doctrinal reference; never revert its edition number by renaming the website. The fully runnable website is in `website/`.

## Approved execution baseline — governing decisions

1. Exact public identity: **“A people belonging to the Father. A life received in the Son. A country expressed through His Spirit.”** No older variant is authoritative.
2. Foundational home passage: **Ephesians 2:18–22**; supporting **John 14:16–23**. All short display lines are marked or treated as **editorial paraphrases**, not verbatim quotations. Preserve other doctrinal uses of John 1:4.
3. Use official CMI original logo in mode-appropriate black/white variants. Wordmark in three vertically stacked lines: **Believers / Country / CMI** (CMI smaller).
4. A single top-centre **Choose your experience** button cycles Day → Night → System; never display a choice menu, option list, theme labels or icons. The upper-right hamburger belongs beside the top header, not beneath the experience button. Persist preference and announce changes accessibly.
5. Clean pages with breadcrumbs + unique headings. Remove redundant kicker/eyebrow/hero duplications and repetitive text. **Commonwealth** is the public stream name; **Country Vanguard** remains unchanged.
6. Encounters: Revi’i / Wednesday School of Scriptures 6:00 PM WAT; Chamishi / Thursday Ministering to the LORD 6:00 PM WAT; Shabbat / Saturday 8:00 AM WAT. Join URLs remain intentionally unpublished until supplied.
7. **2 Minutes Podcast has four authentic user-supplied original recordings, now converted to playable MP3**: **No Separation**; **Proof that you know God**; **What is your advantage as a believer**; **Relationship With The Father**. These are real media, not example cards. Use `content/site-content.json` as the media inventory; play from local `assets/audio/`, provide download and individual episode destinations. The editorial website archive dates (17–14 October 2026) are now assigned by instruction; these are **not original recording dates**. Do not invent the source recording dates, speakers, episode Scriptures, transcripts, subscriptions or quotations. The four recordings are approximately 82–89 seconds. No autoplay.
8. Remain a **noindex design/development preview** until domain, ministry/contact information, hosting, service links, privacy, episode rights, approved texts and media details are confirmed. Production SEO/GEO schema needs absolute URLs and real published metadata; do not fabricate those to satisfy validators.
9. The **CMI Master Leadership Corpus V2.0** is the full doctrinal reference; keep its rich Scripture investigation and guardrails intact. The website baseline number is independent of that corpus.

**Precedence:** This baseline governs anywhere the inherited V7 historical text below calls podcast media “not yet supplied,” says the foundation verse is pending, or calls this iteration V7. Historical text is maintained for architectural context; the canonical media and decisions above supersede outdated statements.

---

## Detailed architectural and editorial specification (inherited and harmonized)

# BELIEVERS COUNTRY — CMI MASTER WEBSITE PROMPT V7

## V7 — APPROVED CMI CORPUS ALIGNMENT & EDITORIAL DISCIPLINE

Across every page, remove duplicated page identities, headings, auxiliary upper labels and repeated descriptions. A breadcrumb identifies WHERE a visitor is, the primary heading communicates WHY that page matters, and introductory copy expands the message. Never repeat the breadcrumb text as the hero eyebrow and h1, or place the same slogan twice in the same page section.

- Preferred breadcrumb convention: `Home / Discover CMI`, `Home / Our ministries`, `Home / Spiritual Intent`, `Home / The Listening Room`, `Home / Weekly encounters`. For inner pages, show an accessible linked parent trail and one distinct page heading.
- The Discover CMI page must begin `Home / Discover CMI`, then a meaningful introduction; retire the duplicated “One foundation. A life expressed together.” as breadcrumb and heading.
- The ministries overview h1 is **CMI Ministry Expressions**, not “One country. Four streams.” Do not repeat these phrases as decorative eyebrow text.
- On the Spiritual Intent landing page, show `Home / Spiritual Intent` and follow with a substantive heading and copy. Remove upper kicker lines such as “Spiritual Intent · Books · Studies · Life” which re-say the existing identity.
- The podcast page uses `Home / The Listening Room` followed by `2 Minutes Podcast` and then the distinct sub-sections **Listen with attention** and **Episode library**. Do not repeat the podcast title as an extra kicker.
- On encounter pages, don't repeat the same short hook in the hero paragraph and first content heading. On ministry pages, replace identical templated asides with stream-specific context or remove them.
- Remove redundant decorated uppercase eyebrow/kicker labels above headings throughout interior pages and homepage content sections. Exceptions requiring a true content role: the Listening Room subsection labels **Listen with attention** and **Episode library**. Breadcrumbs, descriptive headings, and supporting copy must be sufficient without extra filler. Do not use editorial dashes, bullets or lines to restate an existing heading or navigation label.
- Preserve the approved brand statement, official logo, single cyclic Choose your experience control, four named ministry expressions, weekly schedules and access-link verification.
- **Approved homepage foundation: Ephesians 2:18–22**, replacing the previous *homepage-panel use* of John 1:4 (which remains valid in the Corpus's teaching on life in the Son). Display **Our foundation · Ephesians 2:18–22**, followed by the original editorial synthesis **“Through the Son. By one Spirit. To the Father.”** and **“No longer strangers; together, members of God's household.”** Make clear these are editorial paraphrases, not a verbatim Bible translation.
- The approved theological companion texts are **John 14:16–23**, **Galatians 4:4–7**, **Romans 8:14–17**, **1 John 5:11–12**, and **1 Corinthians 12:4–13**; cite them only when relevant and with contextual reasoning, not as ornamental decorations.
- Source priority is now **CMI_Compendium_Master_Leadership_Corpus_v2.docx**, which includes section 2.3 (received Father–Son–Spirit identity), updated publication designation **Commonwealth**, section 20.1, and a provenance register. The original V1 remains an archived foundation, not discarded.
- Avoid editorial repetition across pages: one breadcrumb, one non-duplicative page heading, and a substantive introduction. Never multiply abstract slogans, upper dashes or repeated page labels.


**Version:** Integrated Website V7, 17 October 2026  
**Deliverable requested:** Public-facing ministry website with a memorable, interactive day/night/system experience; complete information architecture, content/CMS system, technical SEO, generative-search discoverability (GEO/AEO), accessibility, privacy, security, and operational acceptance tests.  
**Status:** Website prototype and approved theological identity revision. Unverified live links, dates of publication, content assets and final publication permissions remain pending; content marked *proposed* elsewhere still requires editorial approval.

---

## 1. YOUR ROLE AND REQUIRED OUTPUT

Act simultaneously as senior brand experience architect, Christ-centred theological content editor, information architect, UX/UI director, accessibility lead, frontend engineer, SEO/GEO technical specialist, CMS architect, and QA engineer.

**Do not respond with vague advice or a pretty but nonfunctional single-page mock-up.** Produce a production-minded, responsive, maintainable website with real page routes, navigation, reusable components, typed content models, and a working content-management path. Separate the **design preview** from the **publishable site**. Never fabricate ministry assets, doctrinal claims, podcast episodes, book covers, contact details, service links, donations, testimonials, staff profiles, public addresses, or launch status.

Mandatory staged outputs:
1. Grounded content inventory and unresolved-source register.
2. Sitemap, navigation architecture, journeys, wireframes, and homepage visual preview.
3. Design tokens, accessible light/dark/system theme implementation and responsive components.
4. Implemented multi-page web app, CMS/content types, service-scheduling and media workflow.
5. Technical SEO/GEO plan and real generated artifacts, including valid sitemap and robots directives.
6. QA/audit matrix, deployment notes, content handover, and final publication checklist.

Never treat incomplete source material as permission to invent facts. Use clearly labeled private `NEEDS_CONTENT` entries or public graceful fallbacks. Before launch, refuse to render broken join/buy/listen buttons.

---

## 2. IDENTITY: WHO WE ARE

### Umbrella and positioning

**Visitor-facing brand:** **Believers Country**.  
**Ministry umbrella:** **CMI**. Recent approved public logo use spells this **Country Ministries International**, while older foundational documents use **Country Ministry International**. Keep the displayed full legal/organizational spelling configurable and **resolve with the source owner before launch**; do not silently alternate names.  
**Approved public line:** **Living Eternal Life Abundantly.**  
**Christological centre:** Christ Jesus, the Son of God; who He is, His finished work, and the believer's life in Him illuminate CMI's Scripture, community, ministry, leadership and spiritual practice. **Approved identity argument:** belonging to the Father (Galatians 4:4–7; Romans 8:14–17), life received in the Son (John 14:19–23; 1 John 5:11–12), and a people expressed by the Spirit (Ephesians 2:18–22; 1 Corinthians 12). Local participation must not be equated with salvation.

**Doctrinal/brand guardrails:**
- CMI's use of **Country** conveys belonging, citizenship, government, culture, communal obedience and shared life under Christ. Do not characterize it as a political sovereign nation or imply that the Greek *basileia* literally translates as “country.”
- CMI foregrounds **Believer** to convey faith, allegiance, belonging, trust and active participation. Do not claim that the biblical word *Christianos* is invalid or Christianity is inherently illegitimate.
- “No doctrine of God should require us to ignore the Son” is the interpretive principle. Present Jesus Christ as the basis of the new creation rather than Hebrew chronology, symbolism, or speculative numerology.
- Hebrew days and the 5787 framework can appear as explanatory organizational terminology, not as a condition of salvation or obligation to adopt Judaism, rabbinic custom or extra-biblical practice. Scripture establishes doctrine; numerical and letter motifs, if used, are *secondary reflective lenses*, not proof texts.
- Sacred time, Shabbat and the weekly rhythm serve remembrance, rest, worship, teaching, fellowship and shared life, not legalism or mechanical guarantees.
- Do not copy the entire leadership-training corpus onto a welcome page; create accessible introductory content with links to deep teaching and the underlying Scripture/reasoning rather than flattening the doctrine.
- Scripture quotations: store reference, translation and rights/licensing information; avoid lengthy unlicensed reproduction. Use accurate links to authoritative Scripture views when rights are unknown.

### Website mood and proposed opening

**Primary welcome headline (proposed):** `Welcome to Believers Country.`  
**Subhead (approved expression):** `Living Eternal Life Abundantly.`  
**Approved supporting statement (apply verbatim on the homepage and identity destinations; avoid mechanical repetition in every page heading):** `A people belonging to the Father. A life received in the Son. A country expressed through His Spirit.`  
**Core invitations:** `Discover the Country` • `Join an Encounter` • `Explore the Scriptures`.

The visitor should feel warmly welcomed to a real community of believers, not intimidated by an institutional cathedral-like hero or overwhelmed by sales language.

---

## 3. FOUR STREAMS — FUNCTIONAL ARCHITECTURE

CMI's four streams are not interchangeable programme cards. They form one coherent ministry identity:

| Stream | Source mapping | Public purpose | Proposed visitor action |
|---|---|---|---|
| **Believers Country** | Perat | The community / national-domain expression: citizenship, fellowship, embassies and hubs, culture of the believer, grounded communal life | `Find Your Place` |
| **School of Scriptures** | Gihon | Teaching and educational engine: Scripture study, re-education, theological formation, teaching archives and publishing | `Enter the School` |
| **Commonwealth** | Pishon | Practical welfare, stewardship, community empowerment, economic support and resources | `Explore the Commonwealth` |
| **Country Vanguard** | Hiddekel | Mission, mobilization, deployment, outreach and strategic ministry expansion | `Discover the Vanguard` |

The river associations are an internal source-derived taxonomy, **not a homepage doctrinal proof or replacement for Christ**. Offer an optional secondary 'The four streams' explainer on the CMI overview page. Every stream has its own page, mission, Scripture-based foundation, activities, contact/join CTA, and editorial status (live, in development, forthcoming). Do not imply any programme exists where it has not been launched.

Important taxonomy: **School of Scriptures** is a CMI stream and also names the Wednesday weekly encounter. The architecture must distinguish `/ministries/school-of-scriptures` (ministry) from `/encounters/school-of-scriptures` (weekly gathering), with unambiguous link labels and breadcrumbs.

---

## 4. NON-NEGOTIABLE HOMEPAGE ORDER

1. **Minimal top bar:** accurate official logo, two-line “Believers” / “Country” wordmark, small “CMI” third line, navigation, `Join an Encounter` CTA. Position **one discrete, clickable button**, centred in the top bar and labelled exactly **`Choose your experience`**. No separate label, options, icon or visible state name may appear beside or below it. Each activation immediately cycles the entire page through Day → Night → System → Day.
2. **Hero — New Creation visual language:** horizon, sky, light, restrained stars or abstract terrain; no literal image of God/Jesus/heavenly throne; no false claim that the visual is a photograph of heaven. Headline, motto, orientation, two meaningful CTAs.
3. **A place to belong:** 75–120 words explaining CMI and Believers Country through Christ, belonging and life in Him; a clear `About CMI` link.
4. **This week's encounters:** three substantial session cards with correct schedule, timezone, brief purpose, `Join Online` only when approved link exists, plus `View Details`, `Add to Calendar`, and optional in-person info only when verified.
5. **The four streams of CMI:** concise identifiable cards and a thoughtful summary of the umbrella.
6. **2 Minutes Podcast:** most recent verified episode only, genuine cover art, audio player when audio exists, episode title, length, date, series page and RSS/provider subscriptions where real.
7. **Spiritual Intent:** editorial books-and-formation area, with `Explore Spiritual Intent` (series home), `Browse the Books`, and spotlight/availability cards reflecting actual confirmed assets.
8. **Teaching/Word library:** searchable Scriptures-based messages, notes and session recordings/transcripts, with topic/scripture tags and clear source provenance.
9. **Welcome/participation:** what happens at a gathering, how online participation works, how to contact; optional send a welcome inquiry with privacy consent.
10. **Footer:** verified legal/ministry full name, four streams, encounter schedules, podcast, Spiritual Intent, policies, contact, social profiles, copyright, useful links.

Editorial discipline: no duplicate CTAs in adjacent blocks, no fabricated metrics, no fake event countdowns, no intrusive pop-ups, no generalized stock church crowd photography, no crowded masonry layout. Prioritize sessions and orientation above purchases.

---

## 5. WEBSITE SITEMAP AND USER JOURNEYS

### Primary navigation (desktop)

Top-right **`Menu`** control (accessible dropdown containing `Home`, `Discover CMI`, `Our Ministries`, `Weekly Encounters`, `Listen`, `Spiritual Intent`, `Teachings`); adjacent **`Join an Encounter`** CTA on wide screens. The menu control remains on the right in mobile view, not below the experience button.

For mobile use a compact drawer with accessible focus management and a separate high-visibility upcoming session CTA.

### Routes

```text
/
/welcome
/about
/about/what-we-believe
/about/our-story
/about/leadership               [only with verified biographies/photos]
/ministries
/ministries/believers-country
/ministries/school-of-scriptures
/ministries/commonwealth
/ministries/country-vanguard
/encounters
/encounters/school-of-scriptures
/encounters/ministering-to-the-lord
/encounters/shabbat-service
/encounters/calendar
/encounters/[session-slug]       [dated occurrences if meaningful]
/listen
/listen/2-minutes
/listen/2-minutes/[episode-slug]
/spiritual-intent                [series home]
/spiritual-intent/books
/spiritual-intent/books/[book-slug]
/spiritual-intent/series/[collection-slug]
/teachings
/teachings/[teaching-slug]
/scripture-index
/contact
/privacy
/terms                         [if applicable]
/accessibility
/search
/sitemap.xml
/robots.txt
```

Optional later: verified location/hub/embassy pages, newsletter, account/library, donations/payments only if genuinely operational, studies/courses (do not promise a full academy before launch). No SEO doorway pages.

### User flows

- **First-time visitor:** Home → Welcome/About → What We Believe → Upcoming Encounter → Join.
- **Online attendee:** Home/Encounters → specific session → confirmed platform link → add to calendar / access instructions.
- **Audio listener:** Podcast card → episode → listen/play transcript/subscribe.
- **Reader:** Spiritual Intent → topic/collection → individual book → read description/excerpt → preorder/buy only if confirmed.
- **Scripture student:** Search → teaching archive → structured study page with Scriptures and linked sessions → follow next study.
- **CMI collaborator:** Ministry stream → activities → contact/participation when available.

---

## 6. WEEKLY ENCOUNTERS — AUTHORITATIVE INPUTS

Use **Africa/Lagos (WAT, UTC+01:00)** as the canonical schedule timezone, regardless of the visitor's device clock. Add optional *Your local time* conversion and clearly label both.

| Encounter | Day terminology | Weekly time | Positioning |
|---|---|---|---|
| **School of Scriptures** | **Revi'i — Wednesday** | **6:00 PM WAT** | Scripture study in the light of the Son, depth rather than slogan |
| **Ministering to the LORD** | **Chamishi — Thursday** | **6:00 PM WAT** | Corporate prayer, ministering and summons before the LORD |
| **Shabbat Service** | **Shabbat — Saturday** | **8:00 AM WAT** | Gathering centred on the Son, the Word, remembrance, rest and fellowship |

Wednesday and Thursday times are newly specified by the owner in this request. Shabbat 8:00 AM is based on CMI's established service announcements and **must remain editor-configurable** in case location/season changes. Display the established WAT weekly rhythm but use actual data for session title, details, delivery mode and current meeting links.

Each event card needs:
- name, Hebrew day identifier as supporting text (never confusing to international visitors), weekday, local time, timezone, next occurrence, status, venue when valid;
- session-specific join URL, platform, publish window, help text, organizer contact (only approved), brief spiritual description and optional sermon/study theme;
- `Join Online` button when link and permission are verified; otherwise `Online link to be announced` (inert text, not button) and `View Encounter`;
- unique occurrence override for special sessions, postponement/cancellation and holiday changes; no misleading `LIVE NOW` unless actually live;
- `Add to Calendar` downloadable ICS with `UID`, timezone, dynamic future recurrence and canonical page URL, plus Google/Outlook links where supported;
- direct, accessible external link to verified actual meeting location (Zoom, WhatsApp, Meet or others), secure `noopener noreferrer`, and publish controls to avoid accidental exposure of private invite credentials.

If the ministry uses sunset-to-sunset liturgical day markers elsewhere, keep these separate from the displayed Wednesday/Thursday/Saturday **civil-clock schedule** to avoid confusing visitors. Do not convert Wednesday 6pm into a different weekday simply because sacred days begin at sunset.

### Example encounter CMS object

```json
{
  "id": "school-of-scriptures-weekly",
  "title": "School of Scriptures",
  "weekday": "Wednesday",
  "hebrewDayLabel": "Revi'i",
  "startTimeLocal": "18:00",
  "timezone": "Africa/Lagos",
  "platform": null,
  "onlineJoinUrl": null,
  "joinLinkVisibility": "not-published",
  "durationMinutes": null,
  "venue": null,
  "description": "Scripture studied in the light of Christ Jesus.",
  "upcomingOccurrenceOverrides": []
}
```

NOTE: null fields are deliberate pending confirmation; **do not invent meeting URLs, duration, or place**.

---

## 7. THE 2 MINUTES PODCAST

Use the user-specified name **2 Minutes Podcast**. Four source-verified titles and converted MP3 files exist in this Standard V1 baseline. Do not invent host names, external channels, episode chronology, ratings, transcripts, speaker names, Scripture references or listening destinations beyond these genuine recordings.

Page features:
- short introduction, four genuinely supplied playable recordings, and a newest-first dated website archive, with 17 October 2026 as its current editorial latest issue;
- accessible audio controls with play/pause, progress and speed, duration, optional download based on rights;
- transcript, episode key scriptures, publication date and named speaker/author **only after those fields have been verified from the source**; currently pending;
- verified Apple Podcasts / Spotify / YouTube / RSS subscriptions if actually present; proper RSS feed metadata if site owns the feed;
- `PodcastSeries`/`PodcastEpisode` schema and `AudioObject` when real episodes exist; crawlable transcripts and share previews;
- do not autoplay audio; honor reduced-motion/data-saver preferences.

---

## 8. SPIRITUAL INTENT — SERIES HOME AND BOOK LIBRARY

**Spiritual Intent** is the literature, Scripture-interpretation and discipleship-formation identity grounded in CMI's Christ-centred interpretive framework, the new creation and the finished work of the Son. The website should have **a dedicated Spiritual Intent home (`/spiritual-intent`) and a book library/store (`/spiritual-intent/books`)**, rather than inventing a separate formal ‘Home Ministry.’ If 'Home' is later confirmed to be a distinct product/programme, add its own content model after approval.

Verified-in-project collection directions to model:
- **Spiritual Intent: Money Under God** — four-book collection; preserve **exact approved original covers** and correct individual title/subtitle/edition details from book assets.
- **Spiritual Intent: The Business of the Believer** — established future series title; display its development/publication status truthfully.
- Editions can include standard, pocket, ePub, flashcard or e-pocketbook **only for editions actually produced**.
- Earlier project planning identified a revised **17 December 2026** launch for Money Under God; place the date in content staging as `pending editorial confirmation`, not as an irreversible live countdown or confirmed sale.

Book page: verified title, cover, synopsis, series, author, ISBN (only if supplied), format, release status, book excerpt if approved, price/currency/payment details only when supplied, shipping/digital fulfillment and refund policies where relevant. Schema.org `Book`, `CreativeWorkSeries`, `Offer` only when a true buyable offer exists. **No invented bestseller badges, testimonials or fake scarcity.**

The Spiritual Intent home needs an introduction explaining its method (whole Scripture read in light of the Son, fulfillment, finished work, new creation), series collections, readings or essays, and links back to CMI's teaching foundation. Separate the intellectual home from the commercial book library; avoid letting buying displace the welcome or weekly encounter actions.

---

## 9. DISTINCTIVE DAY / NIGHT / SYSTEM EXPERIENCE

This is a **single-button experience cycle**, not a three-way selector, dropdown, toggle rail or segmented control. Place **one small button** centred in the top header. Its **only visible text is `Choose your experience`**, at all times. There is **no separate caption**, no displayed `Day`/`Night`/`System` labels, no icons, no options list, and no visible current-mode badge. The visitor clicks the very same button repeatedly; **each click immediately switches the visual experience in the fixed order Day → Night → System → Day**. This transition is expressed by the entire site's atmosphere, not by changing the button label.

**First-load interaction:** when no saved choice exists, start in **System** (honour OS preference). The first click selects **Day**, the second **Night**, the third **System**, then repeat. If a visitor already has a saved preference, resume from their saved state and advance to its next mode on click. The chosen state follows them through all internal pages.

### Aesthetic position

Interpret *new heaven and new earth* through poetic abstract visual grammar, not a literal or doctrinally prescriptive scene:
- **Day:** luminous ivory/white, soft mineral blue near the horizon, restrained warm gold, clean white space, calm light; a sense of renewal and clarity.
- **Night:** deep midnight/navy-black, extremely restrained constellational/starlight grain, gentle gold edge lighting, quiet depth and shelter; not neon, sci-fi, purple fantasy, or gothic imagery.
- **System:** reflect `prefers-color-scheme` in real time while the user has selected System.
- Both views have identical structure, editorial hierarchy, full content, links and accessibility; neither hides Scripture, menus or content.
- Use approved CMI gold as the **only signature accent** alongside black/white/neutral lights/darks, with minimal atmospheric colour as background rather than competing brand accents.
- Gold typography/background must meet contrast targets; do not use gold for small text unless contrast is sufficient.
- **Logo:** the owner has supplied `CMI_Logo_All_Variants_v2(1).zip`. Implement the authentic Country Ministries International mark exactly as supplied, without recolouring, redrawing, squeezing or deformation. The supplied master files now reside in `assets/logos/`: `cmi-original-day.svg` (black transparent) and `cmi-original-night.svg` (white transparent), plus source 4096px PNGs. `cmi-display-day.svg` and `cmi-display-night.svg` preserve precisely the original paths, changing **only the viewBox** so the elongated emblem can be seen clearly at header size without losing most width to transparent margins. Pair the small mark on the **left** with a live-text Believers Country wordmark on its right, and the CMI name below. Use black mark on Day mode and white mark on Night mode, including when System tracks the user's OS. Apply the same placement to the footer on all routes. Do not generate a replacement logo or add shadows/glows to the mark. Make the name clear and responsive; respect optical spacing and aspect ratio.

### Interaction spec

- Three mutually exclusive states: `day`, `night`, `system`.
- On first visit default **System**; `prefers-color-scheme` picks effective style.
- Save an explicit user choice to localStorage when available; never store a choice merely because a visitor has loaded the page.
- Listen for OS theme changes while System is active; users manually selecting Day/Night should not be overridden.
- Use a single semantic `<button type="button">Choose your experience</button>` with a large (at least 44px) tap target, visible keyboard focus, and an accessible name describing the current and next modes through `aria-label`; announce mode changes in an offscreen `aria-live="polite"` region. These accessible messages must **not** create visible Day/Night/System labels. Both mouse clicks and keyboard Enter/Space must cycle identically.
- Prevent unwanted light-mode flashing on dark first paint; initialize theme before UI paints where practical.
- Crossfade subtle color variables ≤250ms, but **no animation** when `prefers-reduced-motion: reduce`.
- Avoid render-blocking full-screen video and huge particle effects. Use primarily CSS gradients/textures and optional optimized media.
- Consider a slow abstract horizon animation only when motion preference permits and actual performance remains healthy.

### Proposed token system (adjust after approved logo is evaluated)

```css
:root[data-theme="day"] {
  --page: #F8F7F2;
  --surface: #FFFFFF;
  --ink: #1B201F;
  --muted: #58615F;
  --gold: #8E6A29;
  --outline: #D9D2C4;
}
:root[data-theme="night"] {
  --page: #071018;
  --surface: #111D27;
  --ink: #F4F4EF;
  --muted: #B6C0C3;
  --gold: #DBBB74;
  --outline: #35404A;
}
```

Typography: elegant and contemporary with a display serif reserved for meaningful lead lines, and readable sans-serif body; prefer self-hosted performant fonts with fallback. Avoid ornamental script, excessively large quotes, stock photos, icon clutter and unnecessary glow. Header/logo is always small and sharp. Responsive hero: two-column on desktop and structured single-column on mobile. Make it feel inhabitable, not merely cinematic.

---

## 10. CONTENT MODELS AND CMS OPERATIONS

Build a CMS that nontechnical ministry administrators can operate (a mature headless CMS with previews, roles and versioning; select the least complex durable stack). Avoid every-content-change requiring a developer edit.

Content entities:
- **OrganizationSettings** (exact full name, display branding, contact, social, logos, legal/permission fields, geography).
- **MinistryStream** (four authoritative streams, parent, icon/artwork, summary, core scriptures, scope, status, contact).
- **EncounterSeries** (schedule, timezone, Hebrew term, venue, platform, default join URL, publication policy).
- **EncounterOccurrence** (next date, special theme, join override, cancellation, notes, physical address, recording).
- **Teaching** (title, Scripture references, study body, doctrinal status, teacher, recording, session and topic crosslinks, publication date, canonical slug, revisions).
- **PodcastSeries** and **PodcastEpisode** (provider/feed/audio URL, captions/transcript, metadata, duration, publication/rights).
- **BookCollection**, **Book**, **BookEdition** (original artwork, ISBN, formats, status, store/ordering links, price when verified).
- **SitePage** (SEO metadata, canonical URL, OG image, visibility, primary CTA).
- **FAQItem**, **Announcement**, **Location/Embassy** only if supported.

CMS controls: schema validation, roles (`admin`, `editor`, `publisher`), saved drafts, editorial review, publish and unpublish, canonical slug and redirect management, media alt text, transcript publication, accurate preview URLs, backups, change history, audit logs and approved asset library. Publishing a new podcast, encounter or teaching should update navigation-related modules, homepage feeds, feeds/sitemap and structured data automatically where applicable.

Refrain from publishing private phone numbers or email addresses until explicitly designated public. Any welcome/contact or prayer forms must minimize collection, prevent spam, display consent, route submissions securely and define retention/deletion and sensitive-content protection.

---

## 11. COMPREHENSIVE TECHNICAL SEO

SEO is a foundation, not a hidden metadata checklist. Implement:

**Discovery, crawling, rendering**
- Crawlable human-readable pages using SSR or SSG; preserve important text in HTML, not client-only canvases or inaccessible tabs.
- Correct 200/301/404/410, clean slugs, logical redirects, one canonical per indexable route, no trailing-slash conflicts, robots.txt referencing XML sitemap, automatic valid sitemap index if necessary, sensible `lastmod` reflecting real material changes.
- Use `noindex` for preview, admin, thin search results and duplicate pages; never `Disallow` a page to force deindexing. Keep private meeting credentials out of public indexable pages until intended to publish.
- Noindex placeholder book pages with no substantive verified content when appropriate; no generated mass template pages merely to target keywords.
- Use accurate `hreflang` only if distinct language equivalents truly exist; do not automatically infer language variants from Hebrew names.

**On-page content**
- Unique descriptive `title`, meta description (written for users, not guarantees), single semantically meaningful H1, meaningful H2/H3 nesting, accessible anchor navigation and breadcrumbs, descriptive internal links and image alt text.
- Canonical topic hubs for Christ/new creation/the finished work/Scripture studies, meaningful transcript archives, encounters and podcast episode pages, not repeated blocks of thin generic Christian SEO prose.
- Topic and Scripture indexes linking exact book/chapter/verse references to original CMI studies, and back from each study to source Scriptures and related encounters. Preserve author/presenter and dates on authentic material.
- Optimized share previews: Open Graph, Twitter/X cards, real social imagery when approved; page-specific share title/image and canonical URL.

**Structured data**
- Use JSON-LD `Organization` and more specific `Church` **where appropriate**, with stable `@id`; no invented founding date, phone, location, address or congregation size.
- `WebSite` (+ `SearchAction` only if the onsite search genuinely works), `WebPage`, `BreadcrumbList`.
- Event instance markup `Event`, `eventAttendanceMode`, `VirtualLocation` for online or `Place` when verified, `eventStatus`, accurate ISO times. For recurring events use `Event` with `Schedule` / `eventSchedule` where supported, but also expose crawlable dated upcoming event instances as appropriate; don't claim Google rich-result eligibility automatically.
- `PodcastSeries`, `PodcastEpisode`, `AudioObject` on actual podcast pages; `Book`, `CreativeWorkSeries`, `Offer` on verified catalogue items; `Article`/`BlogPosting` on authentic teaching essays, `VideoObject` on actual recordings. `FAQPage` only when justified by real visible FAQs; don't promise a FAQ rich result.
- Validate schema and ensure properties accurately match visible content; use stable IDs linking organization, person, podcast, book, and events. Do not misapply `Course`, `LocalBusiness`, `Review` or product markup solely for visibility.

**Analytics and operations**
- Set up Google Search Console and Bing Webmaster Tools, appropriate XML sitemap submission, verified domain where available, consent-aware privacy-respecting analytics, event tracking for encounter clicks, real audio plays, teaching downloads, relevant book interactions, and form successes; separate data from advertising retargeting unless consent exists.
- Track indexed pages, genuine search queries, site search, CTR, schema validity, missing alt text, 404s, inbound session links and landing-page engagement without inventing results.
- Use `robots.txt`, canonical headers, OG tags, social images, asset MIME, compression, caching, immutable fingerprinted static assets.

**Core Web Vitals targets (75th percentile field data):** LCP ≤2.5s, INP ≤200ms, CLS ≤0.1. Budget JS, optimize images (responsive WebP/AVIF), limit font shifts and preload, use reasonable caching, lazy-load below fold, avoid giant hero video/background, test slow mobile devices and variable networks.

---

## 12. GEO / AEO / GENERATIVE SEARCH DISCOVERABILITY

GEO means making trustworthy ministry content **discoverable, legible and attributable** in answer and AI-supported search experiences; it is not a secret trick to make a model recommend CMI.

- Publish a source-backed `What We Believe` page, ministry ownership/identity, named authors where approved, full canonical transcripts with timestamps for actual podcast/media, genuine publication/update dates, topic/subtopic headings and clear primary-source Scripture citations.
- Create useful first-party content answering legitimate visitor questions: `What is Believers Country?`, `What happens in the School of Scriptures?`, `When does Ministering to the LORD meet?`, `How do I join CMI online?`, `What is Spiritual Intent?`, `What is the distinction between CMI's four ministries?` — answer accurately, clearly, and with source links; no doorway spam.
- Put short helpful answers before expansive study sections, preserving theological nuance and explicit source/confirmation text links. Use metadata author, `about`, `isPartOf`, transcript and relationship links when schema supports them.
- Ensure text remains accessible to crawlers under ordinary public rules. Decide crawler policies explicitly after privacy/legal review; never expose privileged information to improve indexing.
- Optional lightweight `/llms.txt` or machine-readable site summary may be considered as a navigational experiment **but is neither required by Google nor proven to confer ranking or AI inclusion**. It cannot replace HTML, sitemap, correct schema or quality material.
- Do **not** claim guaranteed appearance in AI Overviews, AI Mode, ChatGPT, Perplexity or Bing AI, and do not generate fake third-party citations or trust marks.
- Keep source attributions credible (when a teaching comes from CMI, identify it as CMI’s interpretation, not universal consensus on debated scriptural matters).
- Make the site a meaningful reference others would actually link to: thoughtful teachings, original studies, primary material and accurate calendars. Build coherent entity presence with consistent verified profiles and publisher identities.

---

## 13. ACCESSIBILITY, SAFETY, TRUST AND PERFORMANCE

Meet **WCAG 2.2 AA** best effort: keyboard-only navigation, focus indicators, semantic landmarks, accessible dialogs/menu and toggles, sufficient text contrast, no critical content conveyed only by stars or gold, audio transcripts, image alt text, touch targets, descriptive buttons, skip link, reduced-motion support, readable line length, scalable text, no keyboard traps. Screen-reader test the single experience-cycle button and session links.

Security/reliability: managed SSL/TLS, dependency monitoring, least-privilege CMS user roles, MFA if available, secure headers/CSP when compatible, input validation/server-side sanitation, CSRF protection where appropriate, anti-bot controls, privacy-respecting logs, secret management, safe media handling, backups, rollbacks, content approval workflow, graceful load failures, broken link checks and uptime alerts.

Transparency: accessible privacy page, clear contact pathways, cookie notice only when necessary and compliant, no unverified institutional claims, no unauthorized public meeting credentials, accurate physical address only if public and approved, accessible disclaimer that the visual experience is symbolic/artistic, not a literal scriptural rendering.

---

## 14. CONTENT TEMPLATES AND PROPOSED COPY

**Homepage hero:**

> Welcome to Believers Country.  
> Living Eternal Life Abundantly.  
> A people belonging to the Father. A life received in the Son. A country expressed through His Spirit.

**About excerpt (draft requiring approval):**

> Believers Country is the welcoming, communal expression of CMI — a people whose belonging is defined by Christ Jesus. Our common life is shaped by Scripture understood in the light of the Son, by fellowship and worship, by spiritual formation, and by service that takes the life of Christ into the world. The Country is not a political border: it is a shared life and witness.

**Weekly session card summaries (proposed):**
- `School of Scriptures` — `Go beyond reading. Examine the Scriptures in the light of the Son.`
- `Ministering to the LORD` — `A gathering devoted to prayer, ministry before the LORD, and summons.`
- `Shabbat Service` — `We gather around the Son, His Word, remembrance, rest, and the life we share in Him.`

**Podcast intro (proposed):** `A brief moment in the Word. A life directed toward the Son.`

**Spiritual Intent intro (proposed):** `Scripture considered in the light of Christ — His person, His fulfillment, His finished work, and the life of the believer in the New Creation.`

*Do not claim these proposed passages are verbatim quotations from the CMI Master Corpus. Have the content owner approve them.*

---

## 15. RECOMMENDED TECHNICAL STACK AND DELIVERABLES

**Preferred:** Astro (modern supported release) with TypeScript, accessible components, static prerendering for durable content and selective interactive islands, CMS integration with preview/publish; or an equivalent supported framework only if a strong practical reason is documented. A smaller, faster site is preferable to a heavyweight animated app. Use documented deployment suitable for the final domain/host (do not assume a domain exists). Keep a simple backup solution for changing schedule/link entries.

**Deliver files:** source code, `.env.example`, CMS config/schema, approved-asset manifests and safe TODO fields, README and editors' guide, responsive preview, design tokens, routes, structured data generators, content templates, reusable event/podcast/book components, working theme state, robots and sitemap generation, podcast RSS where it exists, safe redirect logic, test scripts, accessibility audit, SEO validation and deployment checklist.

**Never publish** until the integrated official SVG logo has been visually approved, all live online links, podcast feed/media, approved book artworks/copy/status, final CMI name, contact details and legal pages have been checked.

---

## 16. ACCEPTANCE TESTS — DEFINITION OF DONE

1. User opens in OS dark mode with no saved preference: site enters the Night visual experience and shows only the button text `Choose your experience`; its screen-reader accessible name identifies the internal System mode; no light flash.
2. From the first-load System setting: first click = Day, second = Night, third = System, then repeat. The visible button label never changes. A chosen mode survives refresh and navigation; when System is active current and future OS preferences are honoured.
3. All main pages render without JavaScript for critical SEO text and links; usable with keyboard/screen reader on mobile.
4. Three encounter cards always display correct weekday and time **in WAT**, with correct `Africa/Lagos` metadata; next occurrence accounts for local calendar dates.
5. Each occurrence connects to its independently editable approved live joining link; if missing, join CTA is disabled/replaced by explanatory non-button text; no fake URL.
6. A legitimate episode has an operational player, duration, transcript and schema; where no episode exists, the site does not simulate it.
7. Original book artwork is preserved exactly; offers appear only when approved; Spiritual Intent series home and books page are distinct.
8. Four stream pages exist with correct source-derived roles; School of Scriptures as ministry and as encounter have separate clear paths.
9. Unique metadata, canonical URLs, clean indexability, sitemap, robots, semantic H structure and accurate JSON-LD validated across representative page types.
10. Current public links, images, privacy settings, redirects, forms, mobile navigation, reduced motion and error states pass manual/automated QA.
11. Main public content is Christ-centred; site does not import Judaism/rabbinic customs as CMI requirements, treat numbers as scriptural proof, or present new-earth art as an actual biblical image.
12. Editors can change weekly links, times, teachings, podcast episodes, books and content independently without code deployment if the CMS is configured to support publication.

---

## 17. APPROVAL DEPENDENCIES / SOURCE REGISTER

**Grounded in source materials or established project decisions:** four ministry names/functions and river taxonomy; CMI Christ-centred theology; Country/Believer distinctions; motto; approved black/white/gold CMI design; Wednesday/Thursday 6 PM; prior Saturday 8 AM notices; 5787 year framing; Shabbat messages under the Son; Spiritual Intent themes and series direction.

**Proposal requiring content approval:** hero supporting copy, descriptions, ambient visual treatments, naming of 2 Minutes Podcast until a verified title/graphic/feed is supplied, page-by-page CTA wording, exact donation/contact model, final book inventory, SEO snippet copy.

**Not supplied as verified live production data:** website domain and hosting; external podcast distribution URLs, speaker credits, original recording dates and transcripts (four MP3 episodes are supplied, with editorial website archive dates assigned); session online join URLs; official legal/organizational spelling; final public address and email; authorized Spiritual Intent sale/payment URLs; official headshots and approved programme descriptions.

**Source caution:** `CMI Compendium.txt` available here is a note *about* the Master Leadership Corpus v1, not the actual full text of that corpus. The provided archive contains primary 5787 materials, including `CMI_Shabbat_Services_Q1_New_Testament.docx`, `CMI_Shabbat_Services_5787_Q1_NT_Calendar.docx`, `CMI_The_Holy_Spirit_Manual.docx`, and `5787_Year_Blueprint.docx`. The full Master Leadership Corpus should be attached to the implementation project for line-by-line doctrinal copy validation. Preserve the source hierarchy: approved leadership corpus / later explicit decisions → Christ-centred Shabbat/teaching materials → contextual 5787 material → new proposed copy, which is never automatically doctrinal authority.

---

**Now create the complete website from this brief. Begin with an accessible homepage prototype whose single 'Choose your experience' cycling button works, and with an accurate three-encounter schedule and the four CMI stream cards; then implement the CMS-backed multi-page system and verify the acceptance tests.**


---
## 18. INTEGRATED CONCEPT 02 — IMPLEMENTATION STATUS (16 OCTOBER 2026)

The `Believers_Country_Integrated_Preview` package implements the proposal as a **working, responsive multi-page static preview**. It includes 17 connected local page routes, the single-button Day → Night → System experience cycle with persistent user choice, visible WAT schedules, automatic next occurrence labels, calendar `.ics` downloads, live teaching title search, accessible mobile navigation, ministry destinations, the real MP3 listening-room episodes, the four sourced Money Under God artworks and the Spiritual Intent catalogue, a preview privacy disclosure and a source-driven content JSON. All navigation is relative to support file-based review without deployment.

This is not yet a publishable ministry site or CMS backend. The source data file is a starting inventory, not a live editor. The `noindex,nofollow` robots setting is intentional for the preview. The approved source logo is now integrated into the header and footer with both theme variants. Before publication verify CMI umbrella wording and original ministry corpus, verify podcast rights and source cover details, verify meeting links, confirm the public contact details and site domain, establish a suitable CMS, add accurate structured data and deployment-generated canonical/sitemap files, self-host fonts, audit accessibility and obtain owner approval. Do not strip the preview's warnings until each dependency is resolved.

**Design note:** The abstract gold horizon and atmospheric sky are conceptual graphic language inspired by restoration and new creation, not a literal scriptural visualization of heaven.


## APPROVED IDENTITY UPDATE — 17 OCTOBER 2026

**Governing public statement, exact copy:**

> A people belonging to the Father. A life received in the Son. A country expressed through His Spirit.

This replaces the earlier wording about belonging to Christ, receiving in Him, and being expressed through His people in the public hero and all future prompts or content seeds. Preserve the explicit **Father / Son / His Spirit** language and the three-sentence structure. Do not silently paraphrase. This is a governing copy decision, not a substitute for Scripture or corpus-based theological explanation.

**Logo supplied and incorporated:** `CMI_Logo_All_Variants_v2(1).zip` — use original logo vectors. Keep the mark fully intact, choose the high-contrast mode-specific variant, and preserve sharp rendering. The live wordmark beside the mark is a separate textual brand label, not part of the original logo artwork. Update Open Graph/favicon usage to use approved assets, subject to final production social-image approval.


---
## 19. APPROVED INTERACTION REVISION — SINGLE-BUTTON EXPERIENCE (17 OCTOBER 2026)

**Supersedes all earlier visible three-choice selector designs, screenshots, descriptions and menu specifications in this file.** The visitor sees only **one button** at the top-centre reading **`Choose your experience`**. Never display Day, Night or System as choices, icons, tabs, an open list, a label underneath, an adjacent caption, or text that replaces the button title.

**Click behaviour** (starting with the first-load default, System):

1. First click → **Day**: immediately render Day palette, sky, and black official CMI logo.
2. Second click → **Night**: immediately render Night palette, starlight, and white official CMI logo.
3. Third click → **System**: immediately follow OS preference, with the correct logo for the resulting effective scheme.
4. Subsequent clicks repeat Day → Night → System → Day.

Persist mode choice between pages/reloads with the existing `bc-experience-v2` browser storage key. Respect live operating-system changes **only** while mode=System. Keep button text unchanged after every click. Expose the selected and next modes only in its screen-reader accessible name and a visually hidden polite live announcement. Give the single button keyboard access, visible focus, 44px minimum touch height, and identical functionality on desktop and mobile. No JavaScript-dependent selector menu is needed. All 17 preview pages and production templates must share this same component. Do not print a list of modes elsewhere in public navigation or footer. The source of truth for this implementation is `assets/app.js`, `.experience-button` styles and page-header markup in this V4 prototype.


---
## 20. APPROVED HEADER & MINISTRY NAMING REVISION — WEBSITE V5 (17 OCTOBER 2026)

This section **supersedes earlier brand header, menu placement, hero eyebrow, and naming instructions** in this master prompt.

1. **Brand lock-up on every page, header and footer:** place the **original approved CMI logo mark** to the left, never stretched, squeezed, or redrawn. Beside it, write **“Believers” on the first line**, **“Country” on the second**, and **“CMI” on a noticeably smaller third line, directly beneath “Country”**. Do not put “Believers Country” on one horizontal line; do not spell out “Country Ministries International” in this compact lock-up. The full institutional name may remain elsewhere in the website’s About/legal/footer descriptive copy for clarity and SEO.
2. **Desktop/tablet/mobile navigation:** one refined upper header with the official mark and stacked wordmark on the **left**, the *single* **`Choose your experience`** cycle button **visually centred**, and an elegant **Menu / hamburger control anchored on the far right on the same level**. Never place the hamburger beneath the centre experience button. On desktop an approved **`Join an Encounter`** link may sit adjacent to the right menu. Open the full accessible site navigation from that upper-right control; avoid a duplicate navigation bar underneath the top row. On extremely narrow screens when three columns cannot fit, keep **brand + menu in the first row** and move *only the experience button* into a centred second row.
3. **Experience-button typography:** set exactly **`Choose your experience`** in a distinctive, elegant **editorial serif** (e.g. Newsreader, with a Georgia fallback), medium weight, approximately 18px on desktop, with a fine gold border and subtle depth. Prioritize legibility and presence over decorative icons or generic system-button text. There is no visible mode label, option list, icon or second button. All three states still cycle Day → Night → System with retained preference and accessible announcements.
4. **Homepage hero cleanup:** **delete** the decorative eyebrow copy **“Christ at the centre · Life in Him”** (and spelling variants) from the hero; do not replace it with a synonym. Keep the foundation in the actual welcome message, the Father–Son–Spirit three-sentence identity statement, and scripture, not a redundant eyebrow. This removes a display label only; it does not dilute the ministry's Christ-centred theological foundation.
5. **Ministry display-name correction:** **`Commonwealth`** replaces **`Country Commonwealth`** as the stream’s public-facing name **throughout** the homepage, ministries page, its detail page, breadcrumbs, menus, content model, page title, cards, and relevant page copy. **`Country Vanguard` remains unchanged**. Canonical route is `/ministries/commonwealth/`; previous `/ministries/country-commonwealth/` should be a redirect, not a duplicate indexed page. Distinguish terminology used in quoted historical source files from *current public branding*.
6. **Scope & verification:** propagate the revised header to all 17 canonical preview pages, both Day and Night modes, mobile widths, structured content seeds and SEO metadata. Keep all weekly encounter sessions, the original approved mark, Spiritual Intent, 2 Minutes Podcast, and the exact Father / Son / Spirit welcome statement untouched. QA keyboard navigation, menu positioning and cycle-button interactions at 320px, 390px, 768px, 1024px and 1440px.


## V7 SOURCE HARMONIZATION AND PUBLICATION DECISION REGISTER

**Approved on 17 October 2026:** Identity statement; Ephesians 2:18–22 homepage foundation; companion John 14:16–23; ministry name Commonwealth; webpage anti-repetition rule; original stacked CMI logo; single cyclic experience control.

**Website execution:** The homepage foundation panel uses a concise editorial summary of Ephesians 2:18–22, not a quotation. The About and Believers Country ministry pages explain the scriptural reasoning once within their distinct contexts. All other pages retain their own functional identity and do not repeat the exact foundation panel. Do not create additional generic banners under headings.

**Corpus execution:** Apply section 2.3, section 20.1, updated Scripture index, and appendix D of the versioned Master Corpus V2. Source text is the complete Library V1 extraction, not the earlier short project summary; formatting is reconstructed and V1 is preserved as the archival baseline.

**Outstanding before launch:** Verify public legal ministry name (legacy source uses Country Ministry International; current public identity often uses Country Ministries International), publish confirmed session links only, and confirm podcast/publication rights, individual cover-master resolution and availability, and final contact details.


---

## STANDARD V1.0 PODCAST HANDOFF — IMPLEMENTED, NOT PLACEHOLDER

- `website/listen/2-minutes/index.html`: four genuine playable embedded recordings.
- `website/listen/2-minutes/<episode-slug>/index.html`: one standalone episode page per recording.
- `website/assets/audio/*.mp3`: converted source audio, HTML5-compatible, each source title written to MP3 ID3 tags.
- `website/index.html`: playable highlighted sample for **No Separation**, without claiming recency.
- `website/content/site-content.json`: titles, routes, durations, filepaths and source provenance.
- `source-audio-originals/*.ogg`: preserved original uploads in the distribution package for provenance, outside site root.
- `PODCAST_MEDIA_MANIFEST.json`: checksums and format info for the four transcoded files.
- Avoid auto-generated summaries, transcripts or episode quotations without listening/verification. Keep native controls keyboard-operable; no autoplay; use metadata preload only.
- The public domain is unknown, so prepare but do not emit false canonical, public `PodcastEpisode` URLs or a bogus external RSS feed. When going live, build genuine podcasts structured data and RSS from the approved media metadata and public URLs.
