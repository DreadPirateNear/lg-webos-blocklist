# LG webOS Universal Blocklist

[![Blocked Domains](https://img.shields.io/badge/domains-108%20blocked-blue.svg?style=flat-square)](#protection-scope--blocked-categories)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Platform: AdGuard Home](https://img.shields.io/badge/AdGuard%20Home-Compatible-brightgreen?style=flat-square&logo=adguard)](https://adguard.com/)
[![Platform: Pi-hole](https://img.shields.io/badge/Pi--hole-Compatible-red?style=flat-square&logo=pi-hole)](https://pi-hole.net/)
[![Platform: NextDNS](https://img.shields.io/badge/NextDNS-Compatible-blue?style=flat-square&logo=nextdns)](https://nextdns.io/)
[![Platform: Unbound / pfSense](https://img.shields.io/badge/Unbound%20%2F%20pfSense-Compatible-orange?style=flat-square)](https://www.pfsense.org/)

### The Definitive DNS Adblock & Anti-Telemetry Blocklist for LG Smart TVs

A comprehensive, evidence-based, and zero-breakage DNS blocklist engineered specifically for **LG webOS Smart TVs**. It neutralizes home launcher advertisements, screensaver sponsored promotions, Automatic Content Recognition (ACR) tracking, forced OTA firmware updates, and IoT analytics—while strictly preserving system clock sync, streaming service integrity (Netflix, Prime Video, YouTube, Disney+), and device stability.

---

## Table of Contents

- [Blocklist Formats & Direct Links](#blocklist-formats--direct-links)
- [Hardware & webOS Compatibility Matrix](#hardware--webos-compatibility-matrix)
- [Protection Scope & Blocked Categories](#protection-scope--blocked-categories)
- [Installation & Setup](#installation--setup)
  - [1. AdGuard Home](#1-adguard-home)
  - [2. Pi-hole (v5 / v6)](#2-pi-hole-v5--v6)
  - [3. NextDNS](#3-nextdns)
  - [4. pfSense / OPNsense / Unbound / Hosts](#4-pfsense--opnsense--unbound--hosts)
- [Important Safety Exclusions (System Clock & Core APIs)](#important-safety-exclusions-system-clock--core-apis)
- [Advanced: Router Firewall & NAT Redirect (Prevent DNS Bypass)](#advanced-router-firewall--nat-redirect-prevent-dns-bypass)
- [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
- [Contributing & Reporting Issues](#contributing--reporting-issues)
- [License](#license)

---

## Blocklist Formats & Direct Links

Subscribe to the format matching your DNS resolver:

| Resolver / System | Syntax Format | Raw Subscription URL |
| :--- | :--- | :--- |
| **AdGuard Home / ABP** | Adblock Plus syntax (`\|\|domain^`) with full subdomain matching | `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-adguard` |
| **Pi-hole / dnsmasq** | Bare plain domains (one domain per line) | `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-pihole` |
| **Hosts / Unbound** | Standard Unix hosts syntax (`0.0.0.0 domain`) | `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-hosts` |

---

## Hardware & webOS Compatibility Matrix

This blocklist is continuously verified across the following LG TV generations and software versions:

| Platform / Lineup | Supported Versions | Validated TV Models |
| :--- | :--- | :--- |
| **webOS 24 / 25** | `v9.x` / `v10.x` | LG OLED G4, C4, B4, QNED90T, QNED85T, UT8000 |
| **webOS 23** | `v8.x` | LG OLED G3, C3, B3, QNED80, UR9000, UR8000 |
| **webOS 22** | `v7.x` | LG OLED G2, C2, B2, A2, QNED85, UQ9000 |
| **webOS 6.0** | `v6.x` (2021) | LG OLED G1, C1, B1, A1, NANO90, UP8000 |
| **webOS 5.0** | `v5.x` (2020) | LG OLED GX, CX, BX, NANO85, UN7300 |
| **webOS 4.0 / 4.5** | `v4.x` (2018-2019) | LG OLED C9, B9, C8, B8, SK9000, UK6300 |
| **webOS 3.0 / 3.5** | `v3.x` (2016-2017) | LG OLED C7, B7, UH8500 |

---

## Protection Scope & Blocked Categories

- **LG Ads, Sponsored Tiles & Screensavers**: Blocks banner promotions, home launcher recommendation tiles, and sponsored screensaver videos (`lgsmartad.com`, `ad.lgappstv.com`, `ibis.lgappstv.com`, `initscr.lge.com`, `lgunifiedsmart.com`).
- **ACR & Viewing Analytics**: Blocks Automatic Content Recognition audio/video fingerprint harvesting engines that monitor what you watch over HDMI and broadcast TV (`alphonso.tv`, `cr-alphonso.tv`, `tvsquared.com`, `smartclip.com`, `smartclip.net`).
- **LG ThinQ & IoT Telemetry**: Silences background tracking beacons, customer data platforms (CDP), and device telemetry (`lgtviot.com`, `connect-client.lgthinq.com`, `eic.cdpbeacon.lgtvcommon.com`, `ngda.lge.com`).
- **OTA Firmware Update Shield**: Intercepts software update servers (`snu.lge.com`, `su.lge.com`, `ota.lge.com`, `lss.lgthinq.com`) to prevent unwanted background firmware upgrades that might restrict sideloading or alter home screen settings.

---

## Installation & Setup

### 1. AdGuard Home
1. Open your **AdGuard Home** dashboard.
2. Go to **Filters** → **DNS blocklists**.
3. Click **Add blocklist** → **Add a custom list**.
4. Configure:
   * **Name**: `LG webOS Blocklist`
   * **URL**:
     ```text
     https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-adguard
     ```
5. Click **Save**.

### 2. Pi-hole (v5 / v6)
1. Open your **Pi-hole Admin Console**.
2. Navigate to **Adlists** (under *Domains/Lists*).
3. In the **Address** field, paste:
   ```text
   https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-pihole
   ```
4. Add a comment (e.g. `LG webOS Telemetry & Ads`) and click **Add**.
5. Update your Gravity database via **Tools** → **Update Gravity** (or run `pihole -g` in your terminal).

### 3. NextDNS
1. In your **NextDNS** dashboard, navigate to the **Privacy** tab.
2. Under **Blocklists**, click **Add a blocklist**.
3. Alternatively, copy domains into your **Denylist** or link the raw plain list URL via NextDNS CLI.

### 4. pfSense / OPNsense / Unbound / Hosts
* Download or curl `lg-webos-hosts` and append it to your system `/etc/hosts` or configure your Unbound DNSBL module to ingest it as an external host override source.

---

## Important Safety Exclusions (System Clock & Core APIs)

> [!IMPORTANT]
> **Never block LG regional clock and identity root services.**
> Regional subdomains (`*.lgtvsdp.com` and `*.lgeapi.com`, such as `it.lgtvsdp.com` or `us.lgtvsdp.com`) are required for NTP network time synchronization, user account login, and Home Dashboard boot. Blocking them will cause system time desynchronization and break SSL certificate handshakes across Netflix, Amazon Prime Video, and YouTube.

If you ever encounter clock desynchronization or a boot loop, ensure these exceptions are allowlisted in your DNS resolver:
```adblock
@@||lgtvsdp.com^
@@||lgeapi.com^
@@||netflix.lge.com^
@@||eic.common.lgthinq.com^
```

---

## Advanced: Router Firewall & NAT Redirect (Prevent DNS Bypass)

LG webOS daemons frequently hardcode fallback public DNS servers (such as Google DNS `8.8.8.8` or Cloudflare DNS `1.1.1.1`) to bypass your DHCP-assigned local DNS resolver when queries fail. To enforce complete protection:

### Port Forwarding / NAT Redirect Rule (Port 53 & Port 853)
In your router firewall (pfSense, OPNsense, OpenWrt, UniFi, MikroTik):
1. Create a Port Forwarding / NAT rule:
   * **Source**: LG TV Static IP address.
   * **Destination**: Any IP (not equal to local DNS server IP).
   * **Port**: `53` (DNS UDP/TCP) and `853` (DNS-over-TLS).
   * **Redirect Target**: Local AdGuard Home or Pi-hole IP address.
2. **Drop Fallbacks**: Alternatively, create an outbound firewall rule dropping all external DNS queries originating from the TV's IP.

---

## Frequently Asked Questions (FAQ)

<details>
<summary><strong>Will this blocklist break streaming apps like Netflix, YouTube, or Prime Video?</strong></summary>

**No.** Streaming content delivery networks (CDNs) and core application APIs are strictly excluded from this list. All rules are tested to ensure flawless playback on Netflix, YouTube, Prime Video, Disney+, Apple TV, and Plex.
</details>

<details>
<summary><strong>Why did my TV clock become incorrect or display the wrong date?</strong></summary>

If your TV shows an incorrect year or time desynchronization, your DNS resolver is likely blocking `*.lgtvsdp.com` or `*.lgeapi.com`. LG webOS uses these regional endpoints for its internal network time protocol (NTP). Whitelist `@@||lgtvsdp.com^` to immediately resolve this.
</details>

<details>
<summary><strong>How often is the blocklist updated?</strong></summary>

The list is updated continuously as new telemetry beacons and ad endpoints are discovered and verified by the community.
</details>

---

## Contributing & Reporting Issues

Contributions, domain submissions, and false positive reports are warmly welcomed!
- To submit new domains or report a broken application, please read [CONTRIBUTING.md](CONTRIBUTING.md).
- Security disclosures should follow [SECURITY.md](SECURITY.md).

---

## License

Distributed under the [MIT License](LICENSE).
