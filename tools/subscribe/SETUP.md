# Connecting the 2 Minutes email list (one time, about 10 minutes)

The website's Subscribe form and the "new word" emails run on a small Google Apps Script
owned by the ministry's Google account. Subscribers are kept in a private Google Sheet, and
emails go out from the ministry's Gmail. Nothing to pay for.

## 1. Create the script (signed in as countryministriesinternational@gmail.com)
1. Go to https://script.google.com and click **New project**. Name it "2 Minutes email list".
2. Delete what is in `Code.gs`, paste the whole contents of `tools/subscribe/Code.gs` from this repository, and click **Save**.
3. In the function menu at the top choose **setup** and click **Run**. Approve the permissions
   (Google will warn that the app is unverified because it is your own; choose *Advanced → Go to project*).
4. Open **Execution log**. Copy the **NOTIFY_TOKEN** line. The log also links to the new private Sheet.

## 2. Publish it as a web app
1. Click **Deploy → New deployment**, type **Web app**.
2. *Execute as*: **Me**. *Who has access*: **Anyone**. Click **Deploy**.
3. Copy the **Web app URL** (it ends in `/exec`).

## 3. Connect it
- In GitHub: repository **seyidev-ops/cmi → Settings → Secrets and variables → Actions → New repository secret**
  - `NOTIFY_URL` = the web app URL
  - `NOTIFY_TOKEN` = the token from step 1
- In `tools/build_site.py`, set `SUBSCRIBE_URL` to the same web app URL and rebuild (or send the URL to Claude).

## Notes
- A personal Gmail account can email about 100 people a day from a script. If the list grows beyond that,
  the script sends to as many as the day allows and logs the rest; at that point move to a Google Workspace
  account or an email service.
- If you ever edit the script, use **Deploy → Manage deployments → Edit → New version** so the URL stays the same.
