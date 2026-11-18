# Changelog

All notable changes to the **LG webOS Universal Blocklist** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-11-18

### Added
- **Expanded Modern Domain Coverage**:
  - LG Ad Solutions core CTV advertising and ACR platform: `lgads.tv`.
  - Smartclip Connected TV video ad delivery: `smartclip.tv`.
  - Direct webOS smart ad and regional endpoints: `ad.lgsmartad.com`, `aic.lgsmartad.com`, `eic.lgsmartad.com`, `kic.lgsmartad.com`.
  - Customer Data Platform and Recommendation services: `aic.cdpsvc.lgtvcommon.com`, `kic.cdpsvc.lgtvcommon.com`, `aic.rdl.lgtvcommon.com`, `kic.rdl.lgtvcommon.com`.
- **Automated Validation & CI**:
  - Introduced `tests/test_blocklists.py` unit test suite verifying rule syntax, 1:1 multi-format parity, duplicate elimination, and safety exclusion guarantees.
  - Added GitHub Actions workflow `.github/workflows/validate.yml` to automatically validate pull requests and pushes to `main`.

---

## [1.0.0] - 2026-11-01

### Added
- **Curated Multi-Format Distribution Lists**:
  - `lg-webos-adguard`: Adblock Plus syntax (`||domain^`) with subdomain matching for AdGuard Home and browser extensions.
  - `lg-webos-pihole`: Plain bare domain format (one per line) for Pi-hole and dnsmasq.
  - `lg-webos-hosts`: Standard Unix hosts syntax (`0.0.0.0 domain`) for pfSense, OPNsense, Unbound, and system hosts files.
- **Protection Scope**:
  - Home launcher promotions, sponsored tiles, and video screensaver ads (`lgsmartad.com`, `ad.lgappstv.com`, `ibis.lgappstv.com`, `initscr.lge.com`).
  - Automatic Content Recognition (ACR) audio/video fingerprint harvesting (`alphonso.tv`, `tvsquared.com`, `smartclip.com`).
  - LG ThinQ & IoT background telemetry beacons (`lgtviot.com`, `connect-client.lgthinq.com`).
  - OTA firmware upgrade interceptors (`snu.lge.com`, `su.lge.com`, `ota.lge.com`).
- **README SEO & Discoverability Overhaul**:
  - Shields.io platform badges (AdGuard Home, Pi-hole, NextDNS, Unbound, MIT).
  - Comprehensive hardware and webOS compatibility matrix (webOS 3.0 through 25, LG OLED C/G/B, QNED, NanoCell, UHD 4K).
  - Search-intent FAQ covering Netflix/streaming integrity and clock synchronization fixes.
  - Router firewall Port 53 / 853 NAT redirection rules to block hardcoded DNS bypass attempts.
- **GitHub Community Standards**:
  - Issue templates for bug reports / false positives and new domain suggestions (`.github/ISSUE_TEMPLATE/`).
  - Pull request template with domain safety checklist (`.github/pull_request_template.md`).
  - Contribution guidelines (`CONTRIBUTING.md`) and Security policy (`SECURITY.md`).

### Removed
- Removed legacy mirror `lg-webos-adguard-home` in favor of standard extension-free naming `lg-webos-adguard`.
