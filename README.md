# LG WebOS Universal Blocklist

A comprehensive, curated, and evidence-based DNS blocklist designed specifically for **LG webOS Smart TVs**. It neutralizes home launcher advertisements, screensaver banners, Automatic Content Recognition (ACR) audio/video tracking, forced OTA firmware updates, and background IoT telemetry—while strictly preserving system clock sync, streaming app integrity (Netflix, Prime Video, YouTube), and device stability.

Compatible with **AdGuard Home**, **Pi-hole**, **dnsmasq**, **NextDNS**, **pfSense/OPNsense (Unbound)**, and standard Unix hosts files.

---

## Blocklist Formats & Direct Links

Subscribe to the format matching your DNS resolver:

| Format / System | Description | Raw Subscription URL |
| :--- | :--- | :--- |
| **AdGuard Home / ABP** | Adblock Plus syntax (`\|\|domain^`) with full subdomain matching | `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-adguard` |
| **Pi-hole / dnsmasq** | Bare plain domains (one domain per line) | `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-pihole` |
| **Hosts / Unbound** | Standard Unix hosts syntax (`0.0.0.0 domain`) | `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-hosts` |
| **Legacy AGH URL** | Preserved for backward compatibility with older setups | `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-adguard-home` |

---

## Blocked Categories & Protection Scope

* **LG Ads, Promotions & Screensavers**: Blocks sponsored tiles, launcher recommendations, and promotion banners (`lgsmartad.com`, `ad.lgappstv.com`, `ibis.lgappstv.com`, `initscr.lge.com`, `lgunifiedsmart.com`).
* **ACR & Viewing Analytics**: Blocks Automatic Content Recognition fingerprinting and viewing habit reporting engines (`alphonso.tv`, `tvsquared.com`, `smartclip.com`, `smartclip.net`).
* **OTA Firmware Update Shield**: Intercepts background update checks (`snu.lge.com`, `su.lge.com`, `ota.lge.com`, `lss.lgthinq.com`) to prevent unwanted firmware upgrades that might restrict sideloading or modify UI behaviors.
* **LG ThinQ & IoT Telemetry**: Silences background telemetry and device monitoring calls (`lgtviot.com`, `connect-client.lgthinq.com`, `lgthinqhome.com`).

---

## Installation & Setup

### 1. AdGuard Home
1. Log in to your **AdGuard Home** dashboard.
2. Navigate to **Filters** → **DNS blocklists**.
3. Click **Add blocklist** → **Add a custom list**.
4. Enter:
   * **Name**: `LG WebOS Blocklist`
   * **URL**: `https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-adguard`
5. Click **Save**.

### 2. Pi-hole (v5 / v6)
1. Open the **Pi-hole Admin Console**.
2. Go to **Adlists** (under *Domains/Lists*).
3. In the **Address** field, paste:
   ```text
   https://raw.githubusercontent.com/DreadPirateNear/lg-webos-blocklist/main/lg-webos-pihole
   ```
4. Add a comment (e.g. `LG webOS Telemetry & Ads`) and click **Add**.
5. Update your Gravity database via **Tools** → **Update Gravity** (or run `pihole -g` in the terminal).

### 3. dnsmasq / pfSense / OPNsense / Generic Hosts
* Download or fetch `lg-webos-hosts` and append it to `/etc/hosts` or configure your Unbound / dnsmasq resolver to ingest it as an external host override source.

---

## Important Safety Exclusions (System Clock & Core APIs)

> [!IMPORTANT]
> **Do not block root domains for LG clock and identity services.**
> Regional subdomains (`*.lgtvsdp.com` and `*.lgeapi.com`, e.g. `it.lgtvsdp.com`, `us.lgtvsdp.com`) are required for NTP network time synchronization, user account login, and Home Dashboard boot. Blocking them will cause system time desync and break SSL handshakes across streaming applications.

If you ever experience clock desynchronization or a boot loop on the home dashboard, ensure these whitelists or exceptions are active in your DNS sinkhole:
```adblock
@@||lgtvsdp.com^
@@||lgeapi.com^
@@||netflix.lge.com^
@@||eic.common.lgthinq.com^
```

---

## Advanced: Prevent TV Fallback / DNS Bypass

LG webOS daemons frequently hardcode fallback public resolvers (such as `8.8.8.8`, `8.8.4.4`, or `1.1.1.1`) to bypass local DHCP DNS servers. To enforce complete protection:

1. **Firewall / NAT Redirect (Port 53 & Port 853)**:
   In your router firewall (pfSense, OPNsense, OpenWrt, UniFi, Mikrotik), create a Port Forwarding / NAT rule:
   * Any outbound UDP/TCP query destined for **Port 53 (DNS)** or **Port 853 (DNS-over-TLS)** originating from the TV's static IP must be redirected to your local AdGuard Home or Pi-hole IP.
2. **Block Fallback**:
   Alternatively, drop all outbound DNS queries from the TV's IP that are not destined for your local DNS server.

---

## Contributions

Contributions and issue reports are welcome! If you notice new telemetry endpoints or an app breakage, please open an issue or pull request on [GitHub](https://github.com/DreadPirateNear/lg-webos-blocklist/issues).

## License

Distributed under the [GNU General Public License v3.0](LICENSE).
