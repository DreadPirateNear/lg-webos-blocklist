## Description of Changes
A concise summary of the domains added, removed, or modified.

## Category
- [ ] Advertising / Sponsored Tiles / Screensavers
- [ ] Telemetry & Usage Analytics
- [ ] ACR Fingerprinting / Tracking
- [ ] OTA Firmware Updates
- [ ] Allowlist / False Positive Fix
- [ ] Documentation / Metadata

## Pre-Submission Verification Checklist
Please verify each of the following before requesting review:
- [ ] **No NTP or Clock Domains**: Confirmed that NO `*.lgtvsdp.com` or `*.lgeapi.com` domains are blocked (blocking them causes clock desync and SSL handshake failures).
- [ ] **Multi-Format Parity**: All domain changes are synchronized across `lg-webos-adguard`, `lg-webos-pihole`, and `lg-webos-hosts`.
- [ ] **Syntax Verified**: Verified that AdGuard uses `||domain^`, Pi-hole uses bare domains, and Hosts uses `0.0.0.0 domain`.
- [ ] **Tested on Live Device**: Tested against an actual LG webOS TV (or verified with network capture) for at least 24 hours without breaking streaming apps (Netflix, Prime Video, YouTube).

## Observed Network Logs / References
Attach query log snippets or Wireshark logs supporting this submission:
```text
(Paste logs here)
```
