---
name: New Domain Submission
about: Suggest a new advertising, telemetry, or ACR tracking domain observed on LG webOS
title: "[DOMAIN]: <domain.com>"
labels: ["enhancement", "domain-candidate"]
assignees: []
---

## Proposed Domain(s)
List the exact fully-qualified domain name(s) (FQDN) to block:
- `example-telemetry.lge.com`

## Category
Select the appropriate category:
- [ ] **Ads & Promotions**: Sponsored launcher tiles, promotion banners, screensaver promos
- [ ] **Telemetry & Analytics**: Usage beacons, user tracking, customer data platforms
- [ ] **ACR (Automatic Content Recognition)**: Viewing habit tracking (e.g. Alphonso, Smartclip)
- [ ] **OTA Firmware Updates**: Software update servers and notification endpoints

## Evidence & Query Logs
Please paste DNS query logs or Wireshark packet captures demonstrating that the TV queries this domain and what behavior corresponds to it:
```text
(Paste query log lines here with timestamps)
```

## Verification & Side Effects
Have you tested blocking this domain locally for at least 24-48 hours?
- [ ] Yes, blocked in local resolver without breaking streaming services or system clock.
- [ ] No, needs verification by maintainers.

## Additional Context
Any additional details (TV model, webOS version, observed UI changes).

