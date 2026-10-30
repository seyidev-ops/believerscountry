/**
 * Believers Country · 2 Minutes email list
 *
 * Runs as a Google Apps Script web app owned by countryministriesinternational@gmail.com.
 *  - The website's Subscribe form posts here (action=subscribe). Addresses go into a private Google Sheet.
 *  - When a new 2 Minutes word goes live, GitHub posts here (action=notify) with a secret token,
 *    and this script emails every active subscriber from the ministry's Gmail.
 *  - Every email carries a one-click unsubscribe link (handled by doGet).
 *
 * Setup: see tools/subscribe/SETUP.md. Run `setup` once from the editor; it creates the Sheet and prints the token.
 */

const SITE = 'https://believerscountry.org/';
const FROM_NAME = 'Believers Country';
const REPLY_TO = 'countryministriesinternational@gmail.com';

function props_() { return PropertiesService.getScriptProperties(); }

function sheet_() {
  const p = props_();
  let id = p.getProperty('SHEET_ID'), ss;
  if (id) { ss = SpreadsheetApp.openById(id); }
  else {
    ss = SpreadsheetApp.create('2 Minutes · Subscribers (private)');
    p.setProperty('SHEET_ID', ss.getId());
    const sh = ss.getSheets()[0];
    sh.setName('Subscribers');
    sh.appendRow(['Email', 'Name', 'Status', 'Subscribed at', 'Source', 'Unsubscribed at']);
    sh.setFrozenRows(1);
    ss.insertSheet('Sent').appendRow(['Slug', 'Title', 'Sent at', 'Recipients']);
  }
  return ss;
}

/** Run once from the editor. Creates the Sheet, a secret token for GitHub, and an unsubscribe signing key. */
function setup() {
  const p = props_();
  if (!p.getProperty('NOTIFY_TOKEN')) p.setProperty('NOTIFY_TOKEN', Utilities.getUuid().replace(/-/g, ''));
  if (!p.getProperty('SIGNING_KEY')) p.setProperty('SIGNING_KEY', Utilities.getUuid() + Utilities.getUuid());
  const ss = sheet_();
  Logger.log('Subscriber sheet: ' + ss.getUrl());
  Logger.log('NOTIFY_TOKEN (paste into GitHub as a secret): ' + p.getProperty('NOTIFY_TOKEN'));
  Logger.log('Emails you can still send today: ' + MailApp.getRemainingDailyQuota());
}

function sig_(email) {
  const raw = Utilities.computeHmacSha256Signature(email.toLowerCase(), props_().getProperty('SIGNING_KEY'));
  return Utilities.base64EncodeWebSafe(raw).replace(/=+$/, '').slice(0, 22);
}
function unsubLink_(email) {
  return ScriptApp.getService().getUrl() + '?action=unsubscribe&email=' + encodeURIComponent(email) + '&sig=' + sig_(email);
}
function text_(s) { return ContentService.createTextOutput(s).setMimeType(ContentService.MimeType.TEXT); }
function esc_(s) { return String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c])); }

function doPost(e) {
  const p = (e && e.parameter) || {};
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);
  try {
    if (p.action === 'subscribe') return subscribe_(p);
    if (p.action === 'notify') return notify_(p);
    return text_('unknown action');
  } finally { lock.releaseLock(); }
}

function subscribe_(p) {
  const email = String(p.email || '').trim().toLowerCase();
  const name = String(p.name || '').trim().slice(0, 60);
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || email.length > 200) return text_('invalid');
  const sh = sheet_().getSheetByName('Subscribers');
  const rows = sh.getDataRange().getValues();
  for (let i = 1; i < rows.length; i++) {
    if (String(rows[i][0]).toLowerCase() === email) {
      if (rows[i][2] !== 'active') { sh.getRange(i + 1, 3).setValue('active'); sh.getRange(i + 1, 6).setValue(''); welcome_(email, name); }
      return text_('ok');
    }
  }
  sh.appendRow([email, name, 'active', new Date(), String(p.source || '').slice(0, 80), '']);
  welcome_(email, name);
  return text_('ok');
}

function welcome_(email, name) {
  if (MailApp.getRemainingDailyQuota() < 1) return;
  const hello = name ? 'Dear ' + esc_(name) + ',' : 'Welcome,';
  MailApp.sendEmail({
    to: email, name: FROM_NAME, replyTo: REPLY_TO,
    subject: 'You are subscribed to the 2 Minutes Podcast',
    htmlBody: shell_(`<p>${hello}</p><p>Thank you for subscribing. A new 2 Minutes word goes out every evening at 6:00 PM (West Africa Time), when the new day begins, and we will email you when it does.</p>
      <p><a href="${SITE}listen/2-minutes/" style="${btn_()}">Listen to today’s word</a></p>
      <p>You can also add the 2 Minutes app to your phone’s home screen from the listening room.</p>`, email)
  });
}

function notify_(p) {
  const P = props_();
  if (!p.token || p.token !== P.getProperty('NOTIFY_TOKEN')) return text_('forbidden');
  const slug = String(p.slug || ''), title = String(p.title || ''), url = String(p.url || '');
  if (!slug || !title || url.indexOf(SITE) !== 0) return text_('missing');
  const ss = sheet_(), sent = ss.getSheetByName('Sent');
  if (sent.getDataRange().getValues().some(r => r[0] === slug)) return text_('already sent');
  const subs = ss.getSheetByName('Subscribers').getDataRange().getValues().slice(1).filter(r => r[2] === 'active');
  const quota = MailApp.getRemainingDailyQuota();
  let n = 0;
  for (const r of subs) {
    if (n >= quota) break;
    const email = String(r[0]), name = String(r[1] || '');
    try {
      MailApp.sendEmail({
        to: email, name: FROM_NAME, replyTo: REPLY_TO,
        subject: 'Today’s 2 minutes · ' + title,
        htmlBody: shell_(`<p>${name ? 'Dear ' + esc_(name) + ',' : 'Good evening,'}</p>
          <p>A new 2 Minutes word is out.</p>
          <p style="font:600 22px/1.3 Georgia,serif;margin:18px 0 6px">${esc_(title)}</p>
          <p style="color:#55615c;margin:0 0 18px">${esc_(p.blurb || '')}${p.label ? ' · ' + esc_(p.label) : ''}</p>
          <p><a href="${esc_(url)}" style="${btn_()}">Listen now</a></p>`, email)
      });
      n++;
    } catch (err) { console.warn('send failed', email, err); }
  }
  sent.appendRow([slug, title, new Date(), n]);
  if (n < subs.length) console.warn('Daily email limit reached: sent ' + n + ' of ' + subs.length);
  return text_('sent ' + n);
}

function btn_() { return 'display:inline-block;padding:12px 22px;border-radius:999px;background:#c99a3b;color:#160f03;font:700 15px Arial,sans-serif;text-decoration:none'; }
function shell_(inner, email) {
  return `<div style="background:#f7f2e6;padding:28px 12px"><div style="max-width:520px;margin:0 auto;background:#fffcf4;border:1px solid #e6dcc4;border-radius:18px;padding:28px;font:16px/1.6 Arial,sans-serif;color:#17201e">
    <p style="font:800 11px Arial,sans-serif;letter-spacing:.2em;color:#9d711c;margin:0 0 18px">BELIEVERS COUNTRY · 2 MINUTES</p>${inner}
    <hr style="border:0;border-top:1px solid #e6dcc4;margin:24px 0 14px">
    <p style="font-size:12px;color:#8a938e;margin:0">Country Ministries International · <a href="${SITE}" style="color:#9d711c">believerscountry.org</a><br>
    You receive this because you subscribed to the 2 Minutes Podcast. <a href="${unsubLink_(email)}" style="color:#9d711c">Unsubscribe</a></p></div></div>`;
}

function doGet(e) {
  const p = (e && e.parameter) || {};
  if (p.action === 'unsubscribe' && p.email && p.sig === sig_(p.email)) {
    const sh = sheet_().getSheetByName('Subscribers');
    const rows = sh.getDataRange().getValues();
    for (let i = 1; i < rows.length; i++) {
      if (String(rows[i][0]).toLowerCase() === String(p.email).toLowerCase()) { sh.getRange(i + 1, 3).setValue('unsubscribed'); sh.getRange(i + 1, 6).setValue(new Date()); }
    }
    return HtmlService.createHtmlOutput(`<div style="font:17px/1.6 Georgia,serif;max-width:480px;margin:60px auto;padding:0 20px;color:#17201e">
      <h2>You have been unsubscribed.</h2><p>You will not receive any more 2 Minutes emails. You can still listen any time at
      <a href="${SITE}listen/2-minutes/">believerscountry.org</a>, and you are welcome to subscribe again.</p></div>`).setTitle('Unsubscribed · Believers Country');
  }
  return HtmlService.createHtmlOutput('<p style="font:16px sans-serif;margin:40px">Believers Country · 2 Minutes email list.</p>');
}
