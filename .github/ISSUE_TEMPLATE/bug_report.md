---
name: Bug Report / False Positive
about: Report a broken streaming app, service malfunction, or clock desync caused by blocked domains
title: "[BUG]: <Brief description of the broken app or service>"
labels: ["bug", "triage"]
assignees: []
---

## Description of the Problem
A clear and concise description of what is broken on your LG Smart TV when using this blocklist.

## Device & Environment Information
- **LG TV Model**: (e.g., LG OLED C2 55", LG QNED80, LG NanoCell 50")
- **webOS Version**: (e.g., webOS 22, webOS 23, webOS 6.0, webOS 4.5)
- **DNS Blocking System**: (AdGuard Home / Pi-hole / NextDNS / pfSense Unbound / other)
- **Blocklist Flavor Used**: (Standard / Full Shield / Legacy URL)

## Broken Service / App
- **Affected App**: (e.g., Netflix, YouTube, Amazon Prime Video, LG Channels, LG Content Store, Time Sync)
- **Observed Behavior**: (e.g., app fails to load, SSL certificate handshake error, TV clock desyncs)

## Relevant DNS Query Logs
Please paste the exact domain queries from your AdGuard Home or Pi-hole query log showing blocked domains during the incident:
```text
(Paste query log lines here)
```

## Temporary Whitelist Test
Did whitelisting a specific domain restore functionality? If so, which domain?
- [ ] Yes: `domain-name.com`
- [ ] No / Untested

