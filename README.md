<div align="center">

# (https://github.com/tonytrawl/WatchTowarr/blob/main/icon.png?raw=true)🗼 WatchTowarr

**A lightweight Windows dashboard that keeps an eye on your whole media stack and pings your phone the moment something breaks.**

Monitors **Radarr · Sonarr · Prowlarr · Plex · qBittorrent · Ombi** in one place.

[![Platform](https://img.shields.io/badge/platform-Windows-blue)]()
[![Download](https://img.shields.io/badge/download-latest%20release-e5a00d)](../../releases/latest)

</div>

---

## Download

Grab the latest **`WatchTowarr.exe`** from the [**Releases**](../../releases/latest) page. That's it, no install, no dependencies, no Python required.

> **Heads up:** Because the `.exe` isn't code-signed, Windows SmartScreen may warn you on first launch. Click **More info → Run anyway**.

## Get started in under a minute

1. Download and run **`WatchTowarr.exe`**. It starts in the background with a tray icon (no console window).
2. Right-click the tray icon → **Open WatchTowarr**, or browse to **http://localhost:8787**.
3. A setup prompt walks you through your service addresses and API keys. Don't use one of the services? Just toggle it off and it won't bug you again.
4. Done. WatchTowarr keeps watching in the background.

## Where to run it

WatchTowarr was built to run on your **main PC, not your server**. The whole point is catching downtime, and a monitor running *on* the server goes down *with* the server. Running it on your everyday machine means it can actually tell you when the server or a service becomes unreachable.

You can run it on your server if that suits you better, it just works best off-box.

---

## What it does

### 🩺 Monitoring
- One clean view of every service: **healthy**, **warning**, or **error**
- Surfaces the *arr apps' own internal health warnings, not just whether they're online
- Checks on a timer (default 30s) with a manual refresh button anytime
- **Don't use a service?** Disable it and it disappears from the dashboard and stops being checked

### 📱 Phone alerts
- Push notifications via [**ntfy**](https://ntfy.sh) (free, no account needed) when something breaks, and again when it recovers
- Only alerts on real changes, so no spam every 30 seconds while something stays down
- Choose **errors only** or **warnings too**
- **Mute** specific services you don't want alerts for
- **Quiet hours** so it won't wake you at 3am, and anything overnight arrives as one tidy summary in the morning
- Send a **test notification** to confirm setup

### 🔎 Add movies & shows
- Built-in search with **poster previews**
- Pick something, confirm the **quality profile**, and it's sent to Radarr or Sonarr to grab
- Remembers your usual quality profile so you're not setting it every time
- No extra API keys needed, it reuses the apps you've already connected

### 📊 History & uptime
- Logs every time a service goes down and recovers, kept for **30 days**
- See real numbers like *"Radarr has gone down 4 times this week"* instead of guessing
- Great for catching a flaky service before it becomes a real headache

### 📈 Live stats
- When everything's healthy, the dashboard shows a calm **all-clear** screen with stats right below it
- **Library counts** (movies, episodes), **active torrents**, and **uptime %** at a glance
- **Now playing on Plex** — who's watching what, direct play vs transcode, with progress
- **Per-drive storage** bars that turn amber then red as a drive fills up
- A 24-hour **Plex streams** graph
- When there are issues, the cards take over and stats move to a one-click button in the header

### 🎨 Customization
- **Light and dark mode**, dark is a clean Plex-style grey, not harsh black (the logo even goes minimal monotone in dark)
- **Custom color palette**, set your own accent, background, and card colors with a live preview
- **Hide** services from view without fully disabling them
- Optional **summary bar** for a compact overview up top
- **Dismiss** issues you already know about so they stop nagging, and you can restore them anytime
- **Click any service** to jump straight to its web UI
- **Keyboard shortcuts**: `/` search · `r` refresh · `s` settings · `h` history
- Optional **sound + on-screen flash** when something newly breaks (bring your own sound if you like)

### 🌀 Active torrents (beta)
- Optional view of what's **downloading** and **seeding**, switchable between the two
- Full detail if you use **qBittorrent**
- No qBittorrent? It falls back to the **Radarr/Sonarr download queue**, so it still works with whatever client you use (Transmission, Deluge, etc.)

---

## Good to know

- **Runs quietly in the system tray.** Right-click the icon to open the dashboard or quit.
- **Update notices.** Checks GitHub about once a day and shows a quiet, dismissible card when a new release is available, with release notes and a link to download. Nothing downloads automatically. Turn it off in settings.
- **Check it from your phone or another device** on the same network, just browse to your PC's address on port `8787`.
- **Everything is configured in the app.** Settings are organized into tabs (General, Services, Alerts, Beta) and your choices are remembered across restarts.
- **Your data stays local.** WatchTowarr talks only to your own services and (if you enable it) the ntfy server you choose.

## What gets checked

| Service | What it watches |
|---|---|
| **Radarr / Sonarr / Prowlarr** | Reachability + the app's own internal health warnings |
| **Plex** | Server reachability and whether libraries respond |
| **qBittorrent** | Online status + torrents stuck in error/stalled/missing states |
| **Ombi** | Whether the service is reachable |

---

## Platform

**Windows only** for now. A Linux version may follow if there's interest, especially for folks who want to run it directly on a Linux server or who daily-drive Linux. If that's you, open an issue and let me know.

## Feedback

Found a bug or have an idea? [Open an issue](../../issues). Feature suggestions welcome.
