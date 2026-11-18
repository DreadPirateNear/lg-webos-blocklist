"""
Automated validation and regression test suite for LG webOS blocklists.
Validates syntax, multi-format parity, safety exclusions, and domain integrity.
"""

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

ADGUARD_PATH = REPO_ROOT / "lg-webos-adguard"
PIHOLE_PATH = REPO_ROOT / "lg-webos-pihole"
HOSTS_PATH = REPO_ROOT / "lg-webos-hosts"

SAFETY_EXCLUDED_DOMAINS = [
    "lgtvsdp.com",
    "lgeapi.com",
    "netflix.lge.com",
    "eic.common.lgthinq.com",
]

DOMAIN_REGEX = re.compile(r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)+$")


def parse_adguard(path: Path):
    domains = []
    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("!"):
                continue
            match = re.match(r"^\|\|([a-zA-Z0-9.-]+)\^$", line)
            if not match:
                raise ValueError(f"Invalid AdGuard rule at line {line_num}: {line}")
            domain = match.group(1).lower()
            if not DOMAIN_REGEX.match(domain):
                raise ValueError(f"Invalid domain format at line {line_num}: {domain}")
            domains.append(domain)
    return domains


def parse_pihole(path: Path):
    domains = []
    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            domain = line.lower()
            if not DOMAIN_REGEX.match(domain):
                raise ValueError(f"Invalid domain format at line {line_num}: {domain}")
            domains.append(domain)
    return domains


def parse_hosts(path: Path):
    domains = []
    with open(path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 2 or parts[0] != "0.0.0.0":
                raise ValueError(f"Invalid hosts entry at line {line_num}: {line}")
            domain = parts[1].lower()
            if not DOMAIN_REGEX.match(domain):
                raise ValueError(f"Invalid domain format at line {line_num}: {domain}")
            domains.append(domain)
    return domains


class TestBlocklists(unittest.TestCase):
    def setUp(self):
        self.adguard_domains = parse_adguard(ADGUARD_PATH)
        self.pihole_domains = parse_pihole(PIHOLE_PATH)
        self.hosts_domains = parse_hosts(HOSTS_PATH)

    def test_files_exist(self):
        self.assertTrue(ADGUARD_PATH.exists(), "lg-webos-adguard must exist")
        self.assertTrue(PIHOLE_PATH.exists(), "lg-webos-pihole must exist")
        self.assertTrue(HOSTS_PATH.exists(), "lg-webos-hosts must exist")

    def test_no_duplicates_within_file(self):
        self.assertEqual(
            len(self.adguard_domains),
            len(set(self.adguard_domains)),
            "Duplicate domains found in lg-webos-adguard",
        )
        self.assertEqual(
            len(self.pihole_domains),
            len(set(self.pihole_domains)),
            "Duplicate domains found in lg-webos-pihole",
        )
        self.assertEqual(
            len(self.hosts_domains),
            len(set(self.hosts_domains)),
            "Duplicate domains found in lg-webos-hosts",
        )

    def test_multi_format_parity(self):
        adguard_set = set(self.adguard_domains)
        pihole_set = set(self.pihole_domains)
        hosts_set = set(self.hosts_domains)

        self.assertEqual(
            adguard_set,
            pihole_set,
            f"Parity mismatch between AdGuard and Pi-hole: {adguard_set ^ pihole_set}",
        )
        self.assertEqual(
            pihole_set,
            hosts_set,
            f"Parity mismatch between Pi-hole and Hosts: {pihole_set ^ hosts_set}",
        )

    def test_safety_exclusions(self):
        all_domains = set(self.pihole_domains)
        for domain in all_domains:
            for safe_root in SAFETY_EXCLUDED_DOMAINS:
                if domain == safe_root or domain.endswith("." + safe_root):
                    self.fail(f"Safety violation: critical domain '{domain}' matches exclusion '{safe_root}'")

    def test_domain_count(self):
        self.assertEqual(
            len(self.pihole_domains),
            118,
            f"Expected exactly 118 domains, got {len(self.pihole_domains)}",
        )


if __name__ == "__main__":
    unittest.main()
