/* Believers Country · 2 Minutes web app — service worker
   - keeps the site usable offline (pages: network first; styles, scripts, images: cache first)
   - on supported phones (installed app, Chrome/Edge on Android and desktop), checks once or twice a day
     for a new 2 Minutes word and shows a notification when the new day's episode is out.
   The day runs 6:00 PM to 6:00 PM, West Africa Time. */
const VERSION = 'd55f2638af';
const CACHE = 'bc-' + VERSION;
const CORE = ['./', 'listen/2-minutes/', 'assets/styles.css', 'assets/app.js', 'assets/app-icon-192.png', 'assets/favicon-day.svg', 'manifest.webmanifest'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(keys => Promise.all(keys.filter(k => k.startsWith('bc-') && k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  if (url.pathname.endsWith('.mp3') || req.headers.has('range')) return;          // audio streams straight from the network
  if (url.pathname.endsWith('episodes.json')) return;                               // always fresh
  if (req.mode === 'navigate' || req.headers.get('accept')?.includes('text/html')) {
    e.respondWith(fetch(req).then(res => { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); return res; })
      .catch(() => caches.match(req).then(r => r || caches.match('listen/2-minutes/'))));
    return;
  }
  e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(res => {
    if (res.ok) { const copy = res.clone(); caches.open(CACHE).then(c => c.put(req, copy)); }
    return res;
  })));
});

/* ---- new-episode check ---- */
const META = 'bc-meta';
async function lastSeen() { const r = await (await caches.open(META)).match('last-seen'); return r ? r.text() : ''; }
async function setSeen(slug) { await (await caches.open(META)).put('last-seen', new Response(slug)); }
function sacredToday() {
  const w = new Date(Date.now() + 3600e3);                     // wall clock in Lagos (UTC+1)
  const d = new Date(Date.UTC(w.getUTCFullYear(), w.getUTCMonth(), w.getUTCDate() + (w.getUTCHours() >= 18 ? 1 : 0)));
  return d.toISOString().slice(0, 10);
}
async function checkForNew() {
  const res = await fetch('episodes.json', { cache: 'no-store' });
  if (!res.ok) return;
  const eps = await res.json();
  const today = sacredToday();
  const ep = eps.find(x => x.date === today);
  if (!ep) return;
  if ((await lastSeen()) === ep.slug) return;
  await setSeen(ep.slug);
  await self.registration.showNotification('Today’s 2 minutes · ' + ep.title, {
    body: ep.blurb || 'A new word from Believers Country is ready to play.',
    icon: 'assets/app-icon-192.png', badge: 'assets/app-icon-192.png', tag: 'bc-2min', data: { url: ep.path }
  });
}
self.addEventListener('periodicsync', e => { if (e.tag === 'new-episode') e.waitUntil(checkForNew()); });
self.addEventListener('message', e => {
  if (e.data?.type === 'seen' && e.data.slug) e.waitUntil(setSeen(e.data.slug));
  if (e.data?.type === 'check') e.waitUntil(checkForNew());
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  const target = new URL(e.notification.data?.url || 'listen/2-minutes/', self.registration.scope).href;
  e.waitUntil(clients.matchAll({ type: 'window', includeUncontrolled: true }).then(list => {
    for (const c of list) if ('focus' in c) { c.navigate(target); return c.focus(); }
    return clients.openWindow(target);
  }));
});
