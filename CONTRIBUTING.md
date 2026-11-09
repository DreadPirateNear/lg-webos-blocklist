# Contributing to LG WebOS Universal Blocklist

Thank you for your interest in contributing! This project is maintained to provide clean, safe, and effective DNS blocklists specifically tailored for LG Smart TVs running webOS.

---

## Guiding Principles

1. **Zero False Positives for Streaming Services**: Core streaming apps (Netflix, YouTube, Amazon Prime Video, Disney+, Apple TV) must NEVER be broken by standard rules.
2. **Never Block System Clock or Core Identity APIs**: Regional NTP endpoints (`*.lgtvsdp.com` and `*.lgeapi.com`) must remain strictly resolvable. Blocking them will desynchronize the TV clock, break SSL certificates, and cause boot loops on the home dashboard.
3. **Evidence-Based Additions**: Any new domain proposed must be backed by DNS query logs or packet captures from an actual LG webOS device.
4. **Synchronized Formats**: When submitting a pull request with new domains, ensure all three lists (`lg-webos-adguard`, `lg-webos-pihole`, and `lg-webos-hosts`) are updated simultaneously in their respective formats.

---

## How to Capture DNS Logs

To identify new ad or telemetry endpoints:
1. Note the TV's static IP address on your local network.
2. Filter the Query Log in **AdGuard Home** or **Pi-hole** by the TV's client IP.
3. Perform the action on the TV (e.g. boot the TV, launch the home dashboard, let screensaver kick in).
4. Identify outgoing domains requested during the event.
5. Search for the domain in the existing list to check if it is already present.

---

## Distribution Formats

When contributing domains, please follow the syntax for each file:

- **`lg-webos-adguard`**: Adblock Plus syntax: `||example.com^`
- **`lg-webos-pihole`**: Bare domain per line: `example.com`
- **`lg-webos-hosts`**: Standard hosts syntax: `0.0.0.0 example.com`

---

## Reporting False Positives

If a domain causes a streaming service or TV feature to stop working:
1. Check your resolver log for recently blocked queries originating from your TV.
2. Temporarily whitelist the suspected domain in your resolver.
3. If functionality is restored, please open an issue using the [Bug Report Template](https://github.com/DreadPirateNear/lg-webos-blocklist/issues/new?template=bug_report.md).

---

## Pull Request Guidelines

- Ensure your branch is up to date with `main`.
- Fill out the [Pull Request Template](.github/pull_request_template.md).
- Verify that system clock domains (`*.lgtvsdp.com`, `*.lgeapi.com`) remain completely untouched.
