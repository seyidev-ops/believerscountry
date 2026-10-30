/* Believers Country · CMI — site behaviour
   The day runs 6:00 PM to 6:00 PM (Africa/Lagos, WAT). Everything "today" resolves against that boundary. */
(() => {
  'use strict';
  const root = document.documentElement;
  root.classList.remove('no-js');
  const ROOT = root.dataset.root || '';
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  /* ---------------- experience: day / night / auto ---------------- */
  const modes = ['day', 'night', 'system'];
  const names = { day: 'Day', night: 'Night', system: 'Auto' };
  const media = matchMedia('(prefers-color-scheme: dark)');
  const toggle = $('[data-experience]');
  const label = $('[data-experience-label]');
  function applyMode(save) {
    let m = modes.includes(root.dataset.mode) ? root.dataset.mode : 'system';
    root.dataset.mode = m;
    const eff = m === 'system' ? (media.matches ? 'night' : 'day') : m;
    root.dataset.theme = eff;
    const next = modes[(modes.indexOf(m) + 1) % 3];
    if (toggle) toggle.setAttribute('aria-label', `Experience: ${names[m]}${m === 'system' ? ' (follows your device)' : ''}. Switch to ${names[next]}.`);
    if (label) label.textContent = names[m];
    // The tab icon follows the site's Day/Night choice: dark mark by day, light mark by night.
    const fav = $('[data-favicon]'), favPng = $('[data-favicon-png]');
    if (fav) fav.href = fav.dataset.favicon + (eff === 'night' ? 'night' : 'day') + '.svg';
    if (favPng) favPng.href = favPng.dataset.faviconPng + (eff === 'night' ? '-night' : '') + '.png';
    const meta = $('meta[name=theme-color]');
    if (meta) meta.content = eff === 'night' ? '#050913' : '#f7f2e6';
    if (save) { try { localStorage.setItem('bc-experience-v3', m); } catch (_) {} }
    window.dispatchEvent(new CustomEvent('themechange', { detail: eff }));
  }
  if (toggle) toggle.addEventListener('click', () => {
    const cur = modes.includes(root.dataset.mode) ? root.dataset.mode : 'system';
    root.dataset.mode = modes[(modes.indexOf(cur) + 1) % 3];
    applyMode(true);
    const live = $('[data-experience-live]');
    if (live) live.textContent = `Experience set to ${names[root.dataset.mode]}.`;
  });
  media.addEventListener && media.addEventListener('change', () => root.dataset.mode === 'system' && applyMode(false));
  applyMode(false);

  /* ---------------- living sky: stars by night, light motes by day ---------------- */
  const canvas = $('#sky-canvas');
  if (canvas && canvas.getContext) {
    const ctx = canvas.getContext('2d');
    let W, H, dpr, stars = [], motes = [], shooting = null, raf;
    function size() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = canvas.width = innerWidth * dpr; H = canvas.height = innerHeight * dpr;
      const n = Math.round(Math.min(220, (innerWidth * innerHeight) / 7000));
      stars = Array.from({ length: n }, () => ({ x: Math.random() * W, y: Math.random() * H * .85, r: (Math.random() * 1.2 + .25) * dpr, p: Math.random() * Math.PI * 2, s: .6 + Math.random() * 1.6 }));
      motes = Array.from({ length: Math.round(n / 4) }, () => ({ x: Math.random() * W, y: Math.random() * H, r: (Math.random() * 2 + .6) * dpr, v: (.08 + Math.random() * .25) * dpr, p: Math.random() * 6 }));
    }
    function frame(t) {
      ctx.clearRect(0, 0, W, H);
      const night = root.dataset.theme === 'night';
      if (night) {
        for (const s of stars) {
          const a = .35 + .65 * Math.abs(Math.sin(t / 1000 * s.s * .6 + s.p));
          ctx.globalAlpha = a; ctx.fillStyle = '#fff6dc';
          ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, 7); ctx.fill();
        }
        if (!shooting && Math.random() < .0025) shooting = { x: Math.random() * W * .7 + W * .2, y: Math.random() * H * .3, l: 0 };
        if (shooting) {
          shooting.l += 14 * dpr;
          const g = ctx.createLinearGradient(shooting.x, shooting.y, shooting.x - shooting.l, shooting.y + shooting.l * .45);
          g.addColorStop(0, 'rgba(255,240,200,.9)'); g.addColorStop(1, 'rgba(255,240,200,0)');
          ctx.globalAlpha = 1; ctx.strokeStyle = g; ctx.lineWidth = 1.4 * dpr;
          ctx.beginPath(); ctx.moveTo(shooting.x, shooting.y); ctx.lineTo(shooting.x - shooting.l, shooting.y + shooting.l * .45); ctx.stroke();
          shooting.x += 6 * dpr; shooting.y -= 2.7 * dpr;
          if (shooting.l > 260 * dpr) shooting = null;
        }
      } else {
        for (const m of motes) {
          m.y -= m.v; m.x += Math.sin(t / 2000 + m.p) * .25 * dpr;
          if (m.y < -10) { m.y = H + 10; m.x = Math.random() * W; }
          ctx.globalAlpha = .25 + .35 * Math.abs(Math.sin(t / 1500 + m.p));
          const g = ctx.createRadialGradient(m.x, m.y, 0, m.x, m.y, m.r * 3);
          g.addColorStop(0, 'rgba(214,171,79,.9)'); g.addColorStop(1, 'rgba(214,171,79,0)');
          ctx.fillStyle = g; ctx.beginPath(); ctx.arc(m.x, m.y, m.r * 3, 0, 7); ctx.fill();
        }
      }
      ctx.globalAlpha = 1;
      if (!reduce) raf = requestAnimationFrame(frame);
    }
    size(); frame(0);
    let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(() => { size(); if (reduce) frame(0); }, 150); });
    addEventListener('themechange', () => reduce && frame(0));
    document.addEventListener('visibilitychange', () => { if (document.hidden) cancelAnimationFrame(raf); else if (!reduce) raf = requestAnimationFrame(frame); });
  }

  /* ---------------- mobile drawer ---------------- */
  const menuBtn = $('#menu-button'), drawer = $('#drawer');
  if (menuBtn && drawer) {
    const set = open => {
      drawer.hidden = !open; menuBtn.setAttribute('aria-expanded', String(open));
      menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      document.body.classList.toggle('locked', open);
    };
    menuBtn.addEventListener('click', () => set(drawer.hidden));
    const dg = $$('details.d-group', drawer);
    dg.forEach(d => d.addEventListener('toggle', () => { if (d.open) dg.forEach(o => { if (o !== d) o.open = false; }); }));
    $$('a', drawer).forEach(a => a.addEventListener('click', () => set(false)));
    addEventListener('keydown', e => { if (e.key === 'Escape' && !drawer.hidden) { set(false); menuBtn.focus(); } });
    addEventListener('resize', () => innerWidth > 920 && !drawer.hidden && set(false));
  }

  /* ---------------- desktop menus ---------------- */
  const groups = $$('[data-nav-group]');
  const shut = except => groups.forEach(g => { if (g !== except) { g.classList.remove('open'); $('button', g).setAttribute('aria-expanded', 'false'); } });
  const hover = matchMedia('(hover: hover)').matches;
  groups.forEach(g => {
    const b = $('button', g);
    const set = o => { g.classList.toggle('open', o); b.setAttribute('aria-expanded', String(o)); };
    b.addEventListener('click', e => { e.stopPropagation(); const o = !g.classList.contains('open'); shut(g); set(o); });
    if (hover) { let t; g.addEventListener('mouseenter', () => { clearTimeout(t); shut(g); set(true); }); g.addEventListener('mouseleave', () => { t = setTimeout(() => set(false), 180); }); }
    g.addEventListener('keydown', e => { if (e.key === 'Escape') { set(false); b.focus(); } });
    g.addEventListener('focusout', e => { if (!g.contains(e.relatedTarget)) set(false); });
  });
  document.addEventListener('click', e => { if (!e.target.closest('[data-nav-group]')) shut(); });

  /* ---------------- reveal, glow, ripple ---------------- */
  const targets = $$('.reveal,.reveal-stagger');
  if ('IntersectionObserver' in window && !reduce) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px', threshold: .08 });
    targets.forEach(t => io.observe(t));
  } else targets.forEach(t => t.classList.add('in'));
  $$('.card').forEach(c => {
    if (!$('.glow', c)) { const g = document.createElement('span'); g.className = 'glow'; g.setAttribute('aria-hidden', 'true'); c.prepend(g); }
    c.addEventListener('pointermove', e => { const r = c.getBoundingClientRect(); c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px'); });
  });
  document.addEventListener('pointerdown', e => {
    const b = e.target.closest('.button,.chip,.play'); if (!b || reduce) return;
    const r = b.getBoundingClientRect(), s = Math.max(r.width, r.height), sp = document.createElement('span');
    sp.className = 'ripple'; sp.style.cssText = `width:${s}px;height:${s}px;left:${e.clientX - r.left - s / 2}px;top:${e.clientY - r.top - s / 2}px`;
    b.appendChild(sp); setTimeout(() => sp.remove(), 700);
  });

  /* ---------------- sacred time: 6 PM to 6 PM ---------------- */
  const WAT = 60 * 60 * 1000, DAY = 864e5;
  const YEAR_START = Date.UTC(2026, 8, 12); // 1 Tishrei 5787 (began at 6 PM, 11 Sep 2026)
  const MONTHS = [['Tishrei', 30], ['Cheshvan', 30], ['Kislev', 30], ['Tevet', 29], ['Shevat', 30], ['Adar I', 30], ['Adar II', 29], ['Nisan', 30], ['Iyyar', 29], ['Sivan', 30], ['Tammuz', 29], ['Av', 30], ['Elul', 29]];
  const DAYNAMES = ['Yom Rishon', 'Yom Sheni', 'Yom Shlishi', 'Yom Revi’i', 'Yom Chamishi', 'Yom Shishi', 'Shabbat'];
  const MOVEMENTS = [['Tav', 1, 90], ['Shin', 91, 208], ['Pe', 209, 297], ['Zayin', 298, 385]];
  function gematria(n) {
    const H = ['', 'ק', 'ר', 'ש', 'ת'], T = ['', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ'], U = ['', 'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט'];
    let s = ''; while (n >= 400) { s += 'ת'; n -= 400; }
    s += H[Math.floor(n / 100)]; n %= 100;
    if (n === 15) s += 'טו'; else if (n === 16) s += 'טז'; else s += T[Math.floor(n / 10)] + U[n % 10];
    return s.length > 1 ? s.slice(0, -1) + '״' + s.slice(-1) : s + '׳';
  }
  function sacredDay(now = Date.now()) {
    const w = new Date(now + WAT); // wall clock in Lagos, read through UTC getters
    const evening = w.getUTCHours() >= 18;
    const civil = Date.UTC(w.getUTCFullYear(), w.getUTCMonth(), w.getUTCDate());
    const day = civil + (evening ? DAY : 0); // the civil date whose daylight belongs to this sacred day
    const seq = Math.round((day - YEAR_START) / DAY) + 1;
    let month = null, dom = null;
    if (seq >= 1 && seq <= 385) { let r = seq; for (const [m, len] of MONTHS) { if (r <= len) { month = m; dom = r; break; } r -= len; } }
    const mv = MOVEMENTS.find(x => seq >= x[1] && seq <= x[2]);
    const nextBoundary = civil + 18 * 3600e3 - WAT + (evening ? DAY : 0);
    return { seq, month, dom, evening, day, weekday: new Date(day).getUTCDay(), movement: mv, nextBoundary, inYear: !!month };
  }
  const fmt = (ms, o) => new Intl.DateTimeFormat('en-GB', Object.assign({ timeZone: 'UTC' }, o)).format(new Date(ms));
  function paintToday() {
    const d = sacredDay();
    $$('[data-hdate]').forEach(el => { el.textContent = d.inYear ? `${d.dom} ${d.month} 5787` : fmt(d.day, { day: 'numeric', month: 'long', year: 'numeric' }); });
    $$('[data-hdate-heb]').forEach(el => { el.textContent = d.inYear ? gematria(d.seq) : ''; });
    $$('[data-hseq]').forEach(el => { el.textContent = d.inYear ? `Sequence ${d.seq} of 385` : ''; });
    $$('[data-hweekday]').forEach(el => { el.textContent = DAYNAMES[d.weekday]; });
    $$('[data-hcivil]').forEach(el => { el.textContent = fmt(d.day, { weekday: 'long', day: 'numeric', month: 'long' }); });
    $$('[data-hboundary]').forEach(el => { el.textContent = d.evening ? 'This day began at 6:00 PM' : 'This day began at 6:00 PM yesterday'; });
    $$('[data-hmovement]').forEach(el => { el.textContent = d.movement ? `${d.movement[0]} movement` : ''; });
    $$('.movement-bar [data-m]').forEach(el => {
      const mv = MOVEMENTS.find(x => x[0] === el.dataset.m);
      const on = d.movement && d.movement[0] === el.dataset.m;
      el.classList.toggle('now', !!on);
      if (on) el.style.setProperty('--p', ((d.seq - mv[1]) / (mv[2] - mv[1]) * 100).toFixed(1) + '%');
    });
    return d;
  }
  const today = paintToday();
  setInterval(paintToday, 60e3);

  /* ---------------- today's two minutes ---------------- */
  const epData = $('#episodes-data');
  const EPISODES = epData ? JSON.parse(epData.textContent) : [];
  function episodeFor(d) {
    if (!EPISODES.length) return null;
    const iso = new Date(d.day).toISOString().slice(0, 10);
    const exact = EPISODES.find(e => e.date === iso);
    if (exact) return exact;
    const asc = [...EPISODES].sort((a, b) => a.date.localeCompare(b.date));
    const first = Date.parse(asc[0].date + 'T00:00:00Z');
    const idx = ((Math.round((d.day - first) / DAY) % asc.length) + asc.length) % asc.length;
    return asc[idx];
  }
  const todayEp = episodeFor(today);
  $$('[data-today-player]').forEach(p => {
    if (!todayEp) return;
    p.dataset.src = ROOT + todayEp.audio.replace(/^\//, '');
    p.dataset.duration = todayEp.seconds;
    $('.player-title', p).textContent = todayEp.title;
    const link = $('[data-today-link]', p.closest('[data-today-wrap]') || document);
    if (link) link.href = ROOT + todayEp.path.replace(/^\//, '');
    const share = $('.share', p); if (share) { share.dataset.shareTitle = todayEp.title; share.dataset.shareUrl = ROOT + todayEp.path.replace(/^\//, ''); }
    const dl = $('[data-download]', p); if (dl) { dl.href = p.dataset.src; dl.setAttribute('download', todayEp.slug + '.mp3'); }
    const tt = $('.player-time .t-total', p); if (tt) tt.textContent = todayEp.label;
  });
  $$('[data-today-flag]').forEach(el => { if (todayEp) el.hidden = el.dataset.todayFlag !== todayEp.slug; });

  /* ---------------- players ---------------- */
  const tfmt = s => { if (!isFinite(s)) return '0:00'; s = Math.floor(s); const h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), ss = String(s % 60).padStart(2, '0'); return h ? `${h}:${String(m).padStart(2, '0')}:${ss}` : `${m}:${ss}`; };
  const players = $$('.player[data-src]');
  players.forEach(p => {
    const bars = $('.bars', p), btn = $('.play', p);
    const cur = $('.t-cur', p), tot = $('.t-total', p);
    let audio = null;
    if (bars && !bars.children.length) {
      let seed = [...(p.dataset.src || 'x')].reduce((a, c) => a + c.charCodeAt(0), 0);
      const n = innerWidth < 500 ? 30 : 44;
      for (let i = 0; i < n; i++) { seed = (seed * 9301 + 49297) % 233280; const h = 22 + (seed / 233280) * 78; const b = document.createElement('i'); b.style.height = h + '%'; b.style.animationDelay = (-(i * 97) % 1000) + 'ms'; bars.appendChild(b); }
    }
    const paint = () => {
      if (!audio) return; const pct = audio.duration ? audio.currentTime / audio.duration : 0;
      const kids = bars ? bars.children : [];
      for (let i = 0; i < kids.length; i++) kids[i].classList.toggle('on', i / kids.length <= pct);
      if (cur) cur.textContent = tfmt(audio.currentTime);
      if (tot && audio.duration) tot.textContent = tfmt(audio.duration);
    };
    const ensure = () => {
      if (audio) return audio;
      audio = new Audio(p.dataset.src); audio.preload = 'metadata';
      if (p.dataset.resume) { const at = Number(p.dataset.resume); audio.addEventListener('loadedmetadata', () => { if (at < audio.duration - 5) audio.currentTime = at; }, { once: true }); }
      audio.addEventListener('timeupdate', paint);
      audio.addEventListener('loadedmetadata', paint);
      audio.addEventListener('play', () => {
        if ('mediaSession' in navigator) {
          try {
            navigator.mediaSession.metadata = new MediaMetadata({ title: $('.player-title', p)?.textContent || 'Believers Country', artist: 'Believers Country', album: p.dataset.album || 'Believers Country', artwork: [{ src: ROOT + 'assets/favicon-512.png', sizes: '512x512', type: 'image/png' }] });
            navigator.mediaSession.setActionHandler('seekbackward', () => { audio.currentTime -= 15; });
            navigator.mediaSession.setActionHandler('seekforward', () => { audio.currentTime += 30; });
          } catch (_) {}
        }
        p.classList.add('playing'); btn.setAttribute('aria-label', 'Pause ' + ($('.player-title', p)?.textContent || '')); p.closest('.ep')?.classList.add('playing-card'); players.forEach(o => o !== p && o._audio && o._audio.pause()); });
      audio.addEventListener('pause', () => { p.classList.remove('playing'); btn.setAttribute('aria-label', 'Play ' + ($('.player-title', p)?.textContent || '')); p.closest('.ep')?.classList.remove('playing-card'); });
      audio.addEventListener('ended', () => { audio.currentTime = 0; paint(); });
      p._audio = audio; return audio;
    };
    btn && btn.addEventListener('click', () => { const a = ensure(); a.paused ? a.play().catch(() => {}) : a.pause(); });
    bars && bars.addEventListener('click', e => { const a = ensure(); const r = bars.getBoundingClientRect(); const go = () => { a.currentTime = (e.clientX - r.left) / r.width * a.duration; paint(); }; a.readyState >= 1 ? go() : a.addEventListener('loadedmetadata', go, { once: true }); });
    p.addEventListener('keydown', e => { if (!audio) return; if (e.key === 'ArrowRight') audio.currentTime += 10; if (e.key === 'ArrowLeft') audio.currentTime -= 10; });
    $$('[data-skip]', p).forEach(b => b.addEventListener('click', () => { const a = ensure(); a.currentTime = Math.max(0, a.currentTime + Number(b.dataset.skip)); paint(); }));
    // Long recordings remember where the listener stopped.
    const longForm = Number(p.dataset.duration) > 600, posKey = 'bc-pos:' + p.dataset.src;
    if (longForm) {
      let saved = 0; try { saved = Number(localStorage.getItem(posKey)) || 0; } catch (_) {}
      if (saved > 30) { p.dataset.resume = saved; const c = $('.t-cur', p); if (c) c.textContent = 'Resume at ' + tfmt(saved); }
      setInterval(() => { if (audio && !audio.paused) { try { localStorage.setItem(posKey, String(Math.floor(audio.currentTime))); } catch (_) {} } }, 5000);
    }
  });

  /* ---------------- encounters: next gathering & countdown ---------------- */
  const SESSIONS = {
    wed: { day: 3, h: 18, title: 'School of Scriptures', slug: 'school-of-scriptures', link: 'https://chat.whatsapp.com/Hx8FnJWmFIw3mMwKjnOXoW' },
    thu: { day: 4, h: 18, title: 'Ministering to the LORD', slug: 'ministering-to-the-lord', link: 'https://chat.whatsapp.com/B9DSqidV9SA0iyL6UemfM1' },
    sat: { day: 6, h: 8, title: 'Shabbat Service', slug: 'shabbat-service', link: 'https://chat.whatsapp.com/GXjvYUmtqAtCYTa6vNcQmV' }
  };
  const LENGTH = 2 * 3600e3;
  function nextOf(s, now = Date.now()) {
    const w = new Date(now + WAT);
    const base = Date.UTC(w.getUTCFullYear(), w.getUTCMonth(), w.getUTCDate());
    for (let k = -1; k < 8; k++) {
      const day = base + k * DAY; if (new Date(day).getUTCDay() !== s.day) continue;
      const start = day + s.h * 3600e3 - WAT;
      if (start + LENGTH > now) return start;
    }
  }
  $$('[data-next]').forEach(el => { const s = SESSIONS[el.dataset.next]; if (s) el.textContent = 'Next · ' + new Intl.DateTimeFormat('en-GB', { timeZone: 'Africa/Lagos', weekday: 'short', day: 'numeric', month: 'short' }).format(new Date(nextOf(s))); });
  function paintCountdown() {
    const now = Date.now();
    const list = Object.entries(SESSIONS).map(([k, s]) => ({ k, s, at: nextOf(s, now) })).sort((a, b) => a.at - b.at);
    const n = list[0];
    $$('[data-countdown]').forEach(el => {
      const title = $('[data-cd-title]', el), time = $('[data-cd-time]', el), when = $('[data-cd-when]', el), join = $('[data-cd-join]', el);
      if (title) title.textContent = n.s.title;
      const diff = n.at - now;
      if (time) {
        if (diff <= 0) time.textContent = 'Gathering now';
        else { const d = Math.floor(diff / DAY), h = Math.floor(diff % DAY / 3600e3), m = Math.floor(diff % 3600e3 / 60e3); time.textContent = (d ? d + 'd ' : '') + h + 'h ' + String(m).padStart(2, '0') + 'm'; }
      }
      if (when) when.textContent = new Intl.DateTimeFormat('en-GB', { timeZone: 'Africa/Lagos', weekday: 'long', hour: 'numeric', minute: '2-digit', hour12: true }).format(new Date(n.at)) + ' WAT';
      if (join) { join.href = n.s.link; }
    });
  }
  if ($('[data-countdown]')) { paintCountdown(); setInterval(paintCountdown, 30e3); }
  $$('[data-ics="daily"]').forEach(b => b.addEventListener('click', e => {
    e.stopImmediatePropagation();
    const now = new Date(), stamp = d => d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');
    const start = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate(), 17, 5));
    const appUrl = new URL(ROOT + 'listen/2-minutes/?source=reminder', location.href).href;
    const txt = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Believers Country//2 Minutes//EN', 'BEGIN:VEVENT', 'UID:bc-2min-daily@believerscountry', 'DTSTAMP:' + stamp(now),
      'DTSTART:' + stamp(start), 'DTEND:' + stamp(new Date(+start + 10 * 60e3)), 'RRULE:FREQ=DAILY', 'SUMMARY:Today’s 2 minutes · Believers Country',
      'DESCRIPTION:A new word is out. Listen: ' + appUrl, 'URL:' + appUrl, 'BEGIN:VALARM', 'ACTION:DISPLAY', 'DESCRIPTION:Today’s 2 minutes is out', 'TRIGGER:PT0M', 'END:VALARM', 'END:VEVENT', 'END:VCALENDAR'].join('\r\n');
    const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([txt], { type: 'text/calendar;charset=utf-8' })); a.download = '2-minutes-daily-reminder.ics';
    document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
    const m = $('[data-notify-msg]'); if (m) m.textContent = 'Open the downloaded file to add a reminder at 6:05 PM every evening.'; markDone('cal');
  }));
  $$('[data-ics]').forEach(b => b.addEventListener('click', () => {
    const s = SESSIONS[b.dataset.ics]; if (!s) return;
    const at = new Date(nextOf(s)), stamp = d => d.toISOString().replace(/[-:]/g, '').replace(/\.\d{3}/, '');
    const txt = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Believers Country//CMI//EN', 'BEGIN:VEVENT', 'UID:' + s.slug + '-' + stamp(at) + '@believerscountry', 'DTSTAMP:' + stamp(new Date()), 'DTSTART:' + stamp(at), 'DTEND:' + stamp(new Date(+at + LENGTH)), 'RRULE:FREQ=WEEKLY', 'SUMMARY:' + s.title + ' · Believers Country', 'DESCRIPTION:Join on WhatsApp: ' + s.link, 'URL:' + s.link, 'END:VEVENT', 'END:VCALENDAR'].join('\r\n');
    const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([txt], { type: 'text/calendar;charset=utf-8' })); a.download = s.slug + '.ics';
    document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }));

  /* ---------------- teachings: status & filters ---------------- */
  const svcCards = $$('[data-svc-date]');
  if (svcCards.length) {
    // A Shabbat service belongs to its Saturday; once Saturday's sacred day has begun it is "this Shabbat".
    const t = today.day;
    const past = svcCards.filter(c => Date.parse(c.dataset.svcDate + 'T00:00:00Z') <= t);
    const future = svcCards.filter(c => Date.parse(c.dataset.svcDate + 'T00:00:00Z') > t);
    svcCards.forEach(c => { const b = $('[data-status]', c); if (!b) return; b.className = 'badge'; b.textContent = 'Shared'; c.dataset.state = 'past'; });
    const latest = past[past.length - 1]; if (latest) { const b = $('[data-status]', latest); b.className = 'badge latest'; b.textContent = 'Latest teaching'; latest.dataset.state = 'latest'; }
    future.forEach((c, i) => { const b = $('[data-status]', c); b.className = 'badge' + (i ? '' : ' next'); b.textContent = i ? 'Coming' : 'This coming Shabbat'; c.dataset.state = 'upcoming'; });
  }
  const search = $('[data-teach-search]');
  if (search) {
    const items = $$('[data-teach]'), empty = $('[data-empty]'), chips = $$('[data-filter]');
    let mode = 'all';
    const run = () => {
      const q = search.value.toLowerCase().trim(); let shown = 0;
      items.forEach(i => { const ok = (!q || i.textContent.toLowerCase().includes(q)) && (mode === 'all' || (mode === 'shared' ? i.dataset.state !== 'upcoming' : i.dataset.state === 'upcoming')); i.hidden = !ok; if (ok) shown++; });
      if (empty) empty.hidden = !!shown;
    };
    search.addEventListener('input', run);
    chips.forEach(c => c.addEventListener('click', () => { mode = c.dataset.filter; chips.forEach(x => x.setAttribute('aria-pressed', String(x === c))); run(); }));
  }

  /* ---------------- listening room archive ---------------- */
  const arcList = $('[data-arc-list]');
  if (arcList) {
    const rows = $$('[data-arc]', arcList), q = $('[data-arc-search]'), sortSel = $('[data-arc-sort]'), kinds = $$('[data-arc-kind]'), count = $('[data-arc-count]'), empty = $('[data-arc-empty]');
    let kind = location.hash === '#shabbat' ? 'shabbat' : 'all';
    const run = () => {
      const term = q.value.toLowerCase().trim(), mode = sortSel.value;
      const sorted = [...rows].sort((a, b) => mode === 'az' ? a.dataset.title.localeCompare(b.dataset.title) : mode === 'old' ? a.dataset.date.localeCompare(b.dataset.date) : b.dataset.date.localeCompare(a.dataset.date));
      let shown = 0;
      sorted.forEach(r => { arcList.appendChild(r); const ok = (kind === 'all' || r.dataset.kind === kind) && (!term || r.textContent.toLowerCase().includes(term)); r.hidden = !ok; if (ok) shown++; });
      kinds.forEach(c => c.setAttribute('aria-pressed', String(c.dataset.arcKind === kind)));
      if (count) count.textContent = shown + (shown === 1 ? ' recording' : ' recordings');
      if (empty) empty.hidden = !!shown;
    };
    q.addEventListener('input', run); sortSel.addEventListener('change', run);
    kinds.forEach(c => c.addEventListener('click', () => { kind = c.dataset.arcKind; run(); }));
    addEventListener('hashchange', () => { if (location.hash === '#shabbat') { kind = 'shabbat'; run(); } });
    run();
  }

  /* ---------------- sharing ---------------- */
  const shares = $$('.share');
  const closeShares = except => shares.forEach(s => { if (s !== except) { const m = $('.share-menu', s); if (m) m.hidden = true; $('[data-share-toggle]', s)?.setAttribute('aria-expanded', 'false'); } });
  shares.forEach(box => {
    const tg = $('[data-share-toggle]', box), menu = $('.share-menu', box), msg = $('.share-msg', box);
    tg && tg.addEventListener('click', async e => {
      e.stopPropagation();
      if (box.hasAttribute('data-share-direct') && navigator.share) {
        const url = new URL(box.dataset.shareUrl || location.href, location.href).href;
        try { await navigator.share({ title: box.dataset.shareTitle || document.title, text: box.dataset.shareText || '', url }); return; } catch (err) { if (err && err.name === 'AbortError') return; }
      }
      const open = menu.hidden; closeShares(box); menu.hidden = !open; tg.setAttribute('aria-expanded', String(open));
    });
    $$('[data-share]', box).forEach(b => b.addEventListener('click', async () => {
      const url = new URL(box.dataset.shareUrl || location.href, location.href).href;
      const title = (box.dataset.shareTitle || document.title) + ' · Believers Country';
      const u = encodeURIComponent(url), t = encodeURIComponent(box.dataset.shareText || title), p = b.dataset.share;
      if (p === 'native') { if (navigator.share) { try { await navigator.share({ title, url }); } catch (_) {} } else msg.textContent = 'Choose a platform below.'; return; }
      if (p === 'copy') { try { await navigator.clipboard.writeText(url); msg.textContent = 'Link copied.'; } catch (_) { msg.textContent = url; } return; }
      const links = { whatsapp: 'https://api.whatsapp.com/send?text=' + t + '%20' + u, x: 'https://twitter.com/intent/tweet?text=' + t + '&url=' + u, facebook: 'https://www.facebook.com/sharer/sharer.php?u=' + u, telegram: 'https://t.me/share/url?url=' + u + '&text=' + t, email: 'mailto:?subject=' + t + '&body=' + u };
      if (p === 'email') location.href = links.email; else window.open(links[p], '_blank', 'noopener');
    }));
  });
  document.addEventListener('click', e => { if (!e.target.closest('.share')) closeShares(); });
  addEventListener('keydown', e => e.key === 'Escape' && closeShares());

  /* ---------------- copy account numbers ---------------- */
  $$('[data-copy]').forEach(b => b.addEventListener('click', async () => {
    const t = $('span', b); let ok = false;
    try { await navigator.clipboard.writeText(b.dataset.copy); ok = true; } catch (_) {
      const ta = document.createElement('textarea'); ta.value = b.dataset.copy; document.body.appendChild(ta); ta.select(); try { ok = document.execCommand('copy'); } catch (_) {} ta.remove();
    }
    if (t) t.textContent = ok ? 'Copied' : b.dataset.copy; b.classList.add('copied');
    setTimeout(() => { if (t) t.textContent = 'Copy'; b.classList.remove('copied'); }, 2000);
  }));

  /* ---------------- 2 Minutes app: install, notifications, email ---------------- */
  let swReg = null;
  if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === '127.0.0.1')) {
    navigator.serviceWorker.register(ROOT + 'sw.js', { scope: ROOT || './' }).then(r => { swReg = r; }).catch(() => {});
  }
  // Tell the app which word the visitor has already heard, so it does not notify about it again.
  if (todayEp && 'serviceWorker' in navigator) navigator.serviceWorker.ready.then(r => r.active && r.active.postMessage({ type: 'seen', slug: todayEp.slug })).catch(() => {});

  const standalone = matchMedia('(display-mode: standalone)').matches || navigator.standalone === true;
  const isIOS = /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  let deferredPrompt = null;
  const installBtn = $('[data-install]'), installMsg = $('[data-install-msg]');
  addEventListener('beforeinstallprompt', e => { e.preventDefault(); deferredPrompt = e; });
  addEventListener('appinstalled', () => { if (installMsg) installMsg.textContent = 'Installed. Look for “2 Minutes” on your home screen.'; });
  if (installBtn) {
    if (standalone) { installBtn.disabled = true; installBtn.textContent = 'Installed on this device'; }
    installBtn.addEventListener('click', async () => {
      if (deferredPrompt) { deferredPrompt.prompt(); const c = await deferredPrompt.userChoice; deferredPrompt = null; if (installMsg && c.outcome !== 'accepted') installMsg.textContent = 'No problem. You can install it any time from here.'; return; }
      if (!installMsg) return;
      installMsg.textContent = isIOS
        ? 'On iPhone or iPad: tap the Share button in Safari, then “Add to Home Screen”.'
        : 'Open your browser menu (⋮ or ⋯) and choose “Install app” or “Add to Home screen”.';
    });
    if (new URLSearchParams(location.search).get('install') === '1') {
      const card = installBtn.closest('.sub-card'); if (card) card.classList.add('pulse');
      setTimeout(() => installBtn.click(), 900);
    }
  }

  const notifyBtn = $('[data-notify]'), notifyMsg = $('[data-notify-msg]');
  const say = (el, t) => { if (el) el.textContent = t; };
  if (notifyBtn) {
    const canNotify = 'Notification' in window && 'serviceWorker' in navigator;
    if (canNotify && Notification.permission === 'granted') notifyBtn.textContent = 'Notifications are on';
    notifyBtn.addEventListener('click', async () => {
      if (!canNotify) { say(notifyMsg, 'This browser cannot show notifications. Use the daily calendar reminder instead.'); return; }
      if (isIOS && !standalone) { say(notifyMsg, 'On iPhone, install the app first (Share → Add to Home Screen), then turn on notifications from inside the app.'); return; }
      const perm = await Notification.requestPermission();
      if (perm !== 'granted') { say(notifyMsg, 'Notifications are off. You can use the daily calendar reminder instead.'); return; }
      const reg = await navigator.serviceWorker.ready;
      let periodic = false;
      if ('periodicSync' in reg) {
        try { const st = await navigator.permissions.query({ name: 'periodic-background-sync' }); if (st.state === 'granted') { await reg.periodicSync.register('new-episode', { minInterval: 6 * 3600e3 }); periodic = true; } } catch (_) {}
      }
      notifyBtn.textContent = 'Notifications are on'; markDone('push');
      reg.showNotification('Notifications are on', { body: 'We will let you know when the next 2 Minutes word is out.', icon: ROOT + 'assets/app-icon-192.png', tag: 'bc-welcome' });
      say(notifyMsg, periodic ? 'Done. The app will check for each new word and notify you.'
        : 'Done. You will be notified when you open the app and a new word is waiting. For a reminder every evening, add the daily calendar reminder too.');
    });
    // When the app opens with notifications on, check straight away for a word not yet heard.
    if (canNotify && Notification.permission === 'granted') navigator.serviceWorker.ready.then(r => r.active && r.active.postMessage({ type: 'check' })).catch(() => {});
  }

  const drop = $('[data-sub-drop]');
  const markDone = what => {
    try { const d = JSON.parse(localStorage.getItem('bc-notify') || '{}'); d[what] = 1; localStorage.setItem('bc-notify', JSON.stringify(d)); } catch (_) {}
    paintDrop();
  };
  function paintDrop() {
    if (!drop) return;
    let d = {}; try { d = JSON.parse(localStorage.getItem('bc-notify') || '{}'); } catch (_) {}
    if (standalone) d.app = 1;
    if ('Notification' in window && Notification.permission === 'granted') d.push = 1;
    const parts = [d.email && 'email', d.app && 'the app', d.push && 'notifications', d.cal && 'calendar'].filter(Boolean);
    drop.classList.toggle('done', parts.length > 0);
    if (parts.length) {
      $('[data-sub-title]', drop).textContent = 'You are set up for each new word';
      $('[data-sub-note]', drop).textContent = 'Through ' + parts.join(', ').replace(/, ([^,]*)$/, ' and $1');
      const pill = $('[data-sub-pill]', drop); if (pill) pill.textContent = 'Manage';
    }
  }
  paintDrop();
  if (drop && new URLSearchParams(location.search).get('install') === '1') drop.open = true;
  if (drop) drop.addEventListener('toggle', () => { const pill = $('[data-sub-pill]', drop); if (pill && !drop.classList.contains('done')) pill.textContent = drop.open ? 'Close' : 'Choose'; });
  addEventListener('appinstalled', () => markDone('app'));
  const subForm = $('[data-subscribe]');
  if (subForm) subForm.addEventListener('submit', async e => {
    e.preventDefault();
    const msg = $('.sub-msg', subForm), email = subForm.email.value.trim(), name = subForm.name.value.trim();
    if (subForm.website.value) return;                                     // spam trap
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { say(msg, 'Please enter a valid email address.'); subForm.email.focus(); return; }
    const endpoint = subForm.dataset.endpoint;
    const btn = $('button[type=submit]', subForm); btn.disabled = true;
    if (!endpoint) {                                                       // service not connected yet: send the request by email
      location.href = 'mailto:' + subForm.dataset.fallback + '?subject=' + encodeURIComponent('Subscribe me to the 2 Minutes Podcast') + '&body=' + encodeURIComponent('Please add me to the 2 Minutes email list.\n\nName: ' + name + '\nEmail: ' + email);
      say(msg, 'Your email app is opening with the request. Press send to finish.'); btn.disabled = false; return;
    }
    say(msg, 'Subscribing…');
    try {
      await fetch(endpoint, { method: 'POST', mode: 'no-cors', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams({ action: 'subscribe', email, name, source: location.pathname }) });
      subForm.reset(); say(msg, 'You are subscribed. Check your inbox for a welcome email (and your spam folder, just in case).'); markDone('email');
      try { localStorage.setItem('bc-subscribed', '1'); } catch (_) {}
    } catch (_) { say(msg, 'That did not go through. Please check your connection and try again.'); }
    btn.disabled = false;
  });

  /* ---------------- footer year ---------------- */
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
