# Security Policy

## Supported Versions

Because this repository distributes static DNS blocklist definitions, security and stability updates are applied continuously on the `main` branch and tagged releases.

| Version / Branch | Supported |
| :--- | :--- |
| `main` (Latest) | :white_check_mark: Yes |
| Tagged Releases (`v1.x`) | :white_check_mark: Yes |
| Historical branches | :x: No |

---

## Scope & Vulnerability Definition

This project maintains DNS filter rules. Security considerations in this context primarily involve:
- **Service Disruption / False Positives**: Accidental sinkholing of critical system endpoints (such as regional time sync `*.lgtvsdp.com`) causing device clock drift or security certificate validation failures.
- **Supply Chain / Integrity**: Unauthorized tampering with distributed blocklist files or GitHub Actions workflows.

Standard requests to add or remove domains are treated as community enhancements or bug reports, not security vulnerabilities. Please use the [Issue Tracker](https://github.com/DreadPirateNear/lg-webos-blocklist/issues) for regular domain suggestions.

---

## Reporting a Security Concern

If you discover a security vulnerability or critical supply-chain defect:
1. **Do not open a public issue.**
2. Send an email with reproduction steps and impact analysis to:
   `security@dreadpiratenear.org` (or open a [GitHub Private Vulnerability Report](https://github.com/DreadPirateNear/lg-webos-blocklist/security/advisories/new)).
3. Maintainers will review the report and respond within 48 hours.

