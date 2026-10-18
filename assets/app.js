(() => {
  const root=document.documentElement;
  const modes=['day','night','system'];
  const media=window.matchMedia('(prefers-color-scheme: dark)');
  const cycleButton=document.querySelector('[data-experience-cycle]');
  const announcement=document.querySelector('[data-experience-announcement]');
  // Visual copy never changes: the entire sky and palette communicate the new mode.
  // The accessible name/live message communicates the active setting to screen readers.
  const displayName=m=>m.charAt(0).toUpperCase()+m.slice(1);
  function updateTheme(shouldSave){
    let m=root.dataset.mode||'system';
    if(!modes.includes(m))m='system';
    root.dataset.mode=m;
    const effective=m==='system'?(media.matches?'night':'day'):m;
    root.dataset.theme=effective;
    const next=modes[(modes.indexOf(m)+1)%modes.length];
    if(cycleButton)cycleButton.setAttribute('aria-label',`Choose your experience. Current: ${displayName(m)}. Activate to switch to ${displayName(next)}.`);
    const meta=document.querySelector('meta[name=theme-color]');
    if(meta)meta.content=effective==='night'?'#08151d':'#f8f7f2';
    if(shouldSave){try{localStorage.setItem('bc-experience-v2',m)}catch(_){}}
  }
  if(cycleButton)cycleButton.addEventListener('click',()=>{
    const current=modes.includes(root.dataset.mode)?root.dataset.mode:'system';
    root.dataset.mode=modes[(modes.indexOf(current)+1)%modes.length];
    updateTheme(true);
    if(announcement)announcement.textContent=`Experience changed to ${displayName(root.dataset.mode)}.`;
  });
  if(media.addEventListener)media.addEventListener('change',()=>{if(root.dataset.mode==='system')updateTheme(false)});
  updateTheme(false);
  const menu=document.getElementById('mobile-nav'), menuButton=document.getElementById('menu-button');
  if(menu&&menuButton){
    const closeMenu=(restoreFocus=false)=>{menu.hidden=true;menuButton.setAttribute('aria-expanded','false');menuButton.setAttribute('aria-label','Open site menu');if(restoreFocus)menuButton.focus()};
    menuButton.addEventListener('click',()=>{const opening=menu.hidden;menu.hidden=!opening;menuButton.setAttribute('aria-expanded',String(opening));menuButton.setAttribute('aria-label',opening?'Close site menu':'Open site menu')});
    menu.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>closeMenu(false)));
    document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!menu.hidden)closeMenu(true)});
    document.addEventListener('click',e=>{if(!menu.hidden&&!menu.contains(e.target)&&!menuButton.contains(e.target))closeMenu(false)});
  }
  const sessions={wed:{day:3,hour:18,minute:0,title:'School of Scriptures',slug:'school-of-scriptures'},thu:{day:4,hour:18,minute:0,title:'Ministering to the LORD',slug:'ministering-to-the-lord'},sat:{day:6,hour:8,minute:0,title:'Shabbat Service',slug:'shabbat-service'}};
  function nextOccurrence(s){const now=new Date();const nigeria=new Date(now.getTime()+60*60*1000);const weekday=nigeria.getUTCDay();let delta=(s.day-weekday+7)%7;const mins=nigeria.getUTCHours()*60+nigeria.getUTCMinutes();if(delta===0&&mins>=s.hour*60+s.minute)delta=7;return new Date(Date.UTC(nigeria.getUTCFullYear(),nigeria.getUTCMonth(),nigeria.getUTCDate()+delta,s.hour-1,s.minute))}
  document.querySelectorAll('[data-next]').forEach(el=>{const s=sessions[el.dataset.next];if(!s)return;el.textContent='Next · '+new Intl.DateTimeFormat('en-GB',{timeZone:'Africa/Lagos',weekday:'short',day:'numeric',month:'short'}).format(nextOccurrence(s))});
  document.querySelectorAll('[data-ics]').forEach(button=>button.addEventListener('click',()=>{const s=sessions[button.dataset.ics];if(!s)return;const at=nextOccurrence(s),stamp=d=>d.toISOString().replace(/[-:]/g,'').replace(/\.\d{3}/,'');const txt=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Believers Country//Website Preview//EN','BEGIN:VEVENT','UID:'+s.slug+'-'+stamp(at)+'@believers-country-preview','DTSTAMP:'+stamp(new Date()),'DTSTART:'+stamp(at),'SUMMARY:'+s.title,'DESCRIPTION:Believers Country weekly gathering.  All times are Africa/Lagos (WAT). Online link to be announced.','END:VEVENT','END:VCALENDAR'].join('\r\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([txt],{type:'text/calendar;charset=utf-8'}));a.download=s.slug+'-next.ics';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500)}));
  const search=document.querySelector('[data-teachings-search]');if(search){const rows=[...document.querySelectorAll('[data-teaching]')];const empty=document.querySelector('[data-no-results]');search.addEventListener('input',()=>{const q=search.value.toLocaleLowerCase().trim();let visible=0;rows.forEach(r=>{const show=r.textContent.toLocaleLowerCase().includes(q);r.hidden=!show;if(show)visible++});if(empty)empty.hidden=visible!==0})}
})();


// Share live episode URLs without assuming a domain for the offline review.
(function(){
 const menus=[...document.querySelectorAll('.episode-share')];
 if(!menus.length)return;
 function closeAll(except){for(const box of menus){if(box===except)continue;box.querySelector('.episode-share-menu').hidden=true;box.querySelector('.podcast-share-toggle').setAttribute('aria-expanded','false');}}
 for(const box of menus){
  const toggle=box.querySelector('.podcast-share-toggle'),menu=box.querySelector('.episode-share-menu'),msg=box.querySelector('.share-message');
  toggle.addEventListener('click',()=>{const opening=menu.hidden;closeAll(box);menu.hidden=!opening;toggle.setAttribute('aria-expanded',String(opening));});
  box.querySelectorAll('[data-share-platform]').forEach(button=>button.addEventListener('click',async()=>{
   const platform=button.dataset.sharePlatform,title=box.dataset.shareTitle||'2 Minutes Podcast';
   const url=new URL(box.dataset.shareUrl,window.location.href);
   if(document.querySelector('meta[name="site-public"]')?.content!=='true'||!['https:','http:'].includes(url.protocol)||['localhost','127.0.0.1','0.0.0.0'].includes(url.hostname)){msg.textContent='This website preview has no public address yet. Shareable links will work after publication.';return;}
   const u=encodeURIComponent(url.href),t=encodeURIComponent(title+' · Believers Country — 2 Minutes Podcast');
   if(platform==='native'){if(navigator.share){try{await navigator.share({title,url:url.href});msg.textContent='Shared using your device.';}catch(e){if(e.name!=='AbortError')msg.textContent='Choose a social platform instead.';}}else msg.textContent='Your device does not support native sharing. Choose a platform below.';return;}
   if(platform==='copy'){try{await navigator.clipboard.writeText(url.href);msg.textContent='Episode link copied.';}catch(e){msg.textContent='Copy this link: '+url.href;}return;}
   if(platform==='email'){window.location.href='mailto:?subject='+t+'&body='+u;return;}
   const links={x:'https://twitter.com/intent/tweet?text='+t+'&url='+u,whatsapp:'https://api.whatsapp.com/send?text='+t+'%20'+u,facebook:'https://www.facebook.com/sharer/sharer.php?u='+u,linkedin:'https://www.linkedin.com/sharing/share-offsite/?url='+u,telegram:'https://t.me/share/url?url='+u+'&text='+t};
   if(links[platform])window.open(links[platform],'_blank','noopener,noreferrer');
  }));
 }
 document.addEventListener('click',e=>{if(!e.target.closest('.episode-share'))closeAll();});
 document.addEventListener('keydown',e=>{if(e.key==='Escape')closeAll();});
})();
