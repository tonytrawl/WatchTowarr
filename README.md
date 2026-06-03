<div align="center">

# ![image](https://github.com/tonytrawl/GuardTowarr/blob/main/icon-4.png?raw=true) GuardTowarr

**A lightweight dashboard that keeps an eye on your whole media stack and pings your phone the moment something breaks.**

Monitors **Radarr · Sonarr · Prowlarr · Readarr · Lidarr · Plex · Jellyfin · qBittorrent · Ombi · Overseerr · Jellyseerr** in one place.

[![Docker Link](https://img.shields.io/badge/Docker-repo-blue?logo=docker)](https://hub.docker.com/r/tonytrawl/guardtowarr)
[![Download](https://img.shields.io/badge/download-latest%20release-e5a00d)](../../releases/latest)
[![Buy me a Coffee](https://img.shields.io/badge/Support%20My%20Work-Buy%20me%20a%20coffee%20%E2%98%95-chocolate?style=plastic)](https://buymeacoffee.com/tonytrawl)

<table>
  <!-- First Row of Images -->
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/tonytrawl/GuardTowarr/blob/main/Dashboard%20clear.png?raw=true" alt="" width="100%">
    </td>
     <td align="center" width="50%">
      <img src="https://github.com/tonytrawl/GuardTowarr/blob/main/dashboard%20error.png?raw=true" alt="" width="100%">
    </td>
  </tr>
  
  <!-- Second Row of Images -->
  <tr>
     <td align="center" width="35%">
      <img src="https://github.com/tonytrawl/GuardTowarr/blob/main/Mobile%20All%20clear%20view.png?raw=true" alt="" width="35%">
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/tonytrawl/GuardTowarr/blob/main/movie%20search.png?raw=true" alt="" width="100%">
    </td>
  </tr>
</table>

---
<div align="left">
  
## Windows Download

Grab the latest **`GuardTowarr.exe`** from the [**Releases**](../../releases/latest) page. That's it, no install, no dependencies, no Python required.

> **Heads up:** Because the `.exe` isn't code-signed, Windows SmartScreen may warn you on first launch. Click **More info → Run anyway**.

## Docker

Prefer containers? GuardTowarr is on Docker Hub as **`tonytrawl/guardtowarr`**.

The Docker image is the cross-platform way to run GuardTowarr — it runs anywhere Docker does, **including Linux servers, NAS devices (Synology/unRAID/etc.), and Windows/macOS**. You do **not** need Windows to run the container; the "Windows only" note further down applies only to the standalone `.exe` desktop build.

```yaml
services:
  guardtowarr:
    image: tonytrawl/guardtowarr:latest
    container_name: guardtowarr
    ports:
      - "9595:9595"
    volumes:
      - ./config:/config
    restart: unless-stopped
```

Then `docker compose up -d` and open `http://<host>:9595`.

**Important networking note:** if your Radarr/Sonarr/Plex/etc. run on the same machine, the container **cannot** reach them at `localhost` (inside a container that means the container itself). Use one of these:

- Put your host's LAN IP in each service URL, e.g. `http://192.168.1.50:7878`, or
- Run with `network_mode: host` (uncomment it in the compose file and drop the `ports` block).

Settings, dismissed issues, and history persist in the mounted `./config` volume. The system-tray feature is desktop-only and isn't part of the Docker image; the container just runs in the background like any other service.

---

## What it does
 
### 🩺 Monitoring
- One clean view of every service: **healthy**, **warning**, or **error**
- Surfaces the *arr apps' own internal health warnings, not just whether they're online
- Checks on a timer (default 60s) with a manual refresh button anytime
- **Don't use a service?** Disable it and it disappears from the dashboard and stops being checked
### 📱 Phone alerts
- Push notifications via [**ntfy**](https://ntfy.sh) (free, no account needed) when something breaks, and again when it recovers
- Only alerts on real changes, so no spam every 30 seconds while something stays down
- Choose **errors only** or **warnings too**
- **Mute** specific services you don't want alerts for
- **Quiet hours** so it won't wake you at 3am, and anything overnight arrives as one tidy summary in the morning
- **Torrent finished alerts** (beta), get a ping like "Dune: Part Two finished downloading" when a download completes, using the clean title from Radarr/Sonarr
- Send a **test notification** to confirm setup
### 🔎 Add movies, shows, books & music
- Built-in search with **poster previews**
- Search **movies** (Radarr), **shows** (Sonarr), **books** (Readarr), and **music** (Lidarr)
- Pick something, confirm the **quality profile**, and it's sent to the right app to grab
- Search options only appear for the apps you've set up and enabled
- Remembers your usual quality profile so you're not setting it every time
- No extra API keys needed, it reuses the apps you've already connected
### 📊 History & uptime
- Logs every time a service goes down and recovers, kept for **30 days**
- See real numbers like *"Radarr has gone down 4 times this week"* instead of guessing
- Great for catching a flaky service before it becomes a real headache
### 📈 Live stats
- When everything's healthy, the dashboard shows a calm **all-clear** screen with stats right below it
- **Library counts** (movies, episodes), **active torrents**, and **uptime %** at a glance
- **Now playing on Plex and/or Jellyfin** — who's watching what, direct play vs transcode, with progress and a tag showing which server it's on
- **Transcode vs. direct-play breakdown**, and **per-server library counts** when both media servers are running
- **Per-drive storage** bars that turn amber then red as a drive fills up
- A 24-hour **streams** graph
- When there are issues, the cards take over and stats move to a one-click button in the header
### 🎨 Customization
- **Light and dark mode**, dark is a clean Plex-style grey, not harsh black (the logo even goes minimal monotone in dark)
- **Custom color palette**, set your own accent, background, and card colors with a live preview
- **Hide** services from view without fully disabling them
- **Dismiss** issues you already know about so they stop nagging, and you can restore them anytime
- **Click any service** to jump straight to its web UI
- **Keyboard shortcuts**: `/` search · `r` refresh · `s` settings · `h` history
- Optional **sound + on-screen flash** when something newly breaks (bring your own sound if you like)
### 🌀 Active torrents
- View of what's **downloading** and **seeding**, switchable between the two
- Full detail if you use **qBittorrent**
- No qBittorrent? It falls back to the **Radarr/Sonarr download queue**, so it still works with whatever client you use (Transmission, Deluge, etc.)
---
 
## Good to know
 
- **Runs quietly in the system tray.** Right-click the icon to open the dashboard or quit.
- **Update notices.** Checks GitHub about once a day and shows a quiet, dismissible card when a new release is available, with release notes and a link to download. Nothing downloads automatically. Turn it off in settings.
- **Check it from your phone or another device** on the same network, just browse to your PC's address on port `9595`.
- **Everything is configured in the app.** Settings are organized into tabs (General, Services, Alerts, Beta) and your choices are remembered across restarts.
- **Your data stays local.** GuardTowarr talks only to your own services and (if you enable it) the ntfy server you choose.
## What gets checked
 
GuardTowarr doesn't just ping a port. For each service it logs in with your credentials and reads that app's own status and health endpoints, so it catches things that are technically "up" but quietly broken.
 
| Service | What it watches |
|---|---|
| **Radarr / Sonarr / Prowlarr / Readarr / Lidarr** | Reachability + the app's own internal health checks (missing root folders, no indexers, download client problems, update issues, etc.), each linked to the relevant wiki fix |
| **Plex** | Server reachability, token validity, and whether libraries respond (distinguishes "down" from "up but libraries not responding") |
| **Jellyfin** _(beta)_ | Server reachability + API key validity; also feeds the live now-playing view |
| **qBittorrent** | Online status, bad-credential detection, and torrents stuck in error / missing-files / stalled states |
| **Ombi / Overseerr / Jellyseerr** | Reachability + API key validity via the status endpoint |
 
Every service reports one of three states — healthy, warning, or error — with real outages kept separate from minor warnings. Any issue can be dismissed and stays hidden until it recurs.
 
---

## Platform

- **Docker image** — runs anywhere Docker does: **Linux, NAS (Synology/unRAID), Windows, macOS.** This is the recommended way to run it on a server. See the [Docker](#docker) section above.
- **Standalone `.exe`** — **Windows only.** This is the desktop build with the system-tray icon, for running on your everyday Windows PC.

So: if you're on Linux or a NAS, use Docker — it's fully supported. The native desktop app is Windows-only for now; a native Linux build may follow if there's interest. Either way, open an issue and let me know what you're running.

## Feedback

Found a bug or have an idea? [Open an issue](../../issues). Feature suggestions welcome.
