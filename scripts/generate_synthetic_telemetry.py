#!/usr/bin/env python3
"""
Generate synthetic-but-realistic enterprise security telemetry for Task 5.

This dataset is intentionally synthetic. It represents the types of signals
collected across Lighthouse Technology Domains 1–4 without exposing real
credentials, production assets, personal data, or sensitive infrastructure.
"""

from __future__ import annotations

import csv
import random
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
OUTPUT_FILE = DATASETS_DIR / "synthetic_raw_telemetry.csv"

random.seed(2026)

ASSET_TYPES = [
    "domain_controller",
    "windows_server",
    "linux_server",
    "workstation",
    "firewall",
    "siem_server",
    "application_server",
]

BUSINESS_UNITS = [
    "identity_services",
    "security_operations",
    "network_services",
    "finance_operations",
    "business_applications",
]

FIELDNAMES = [
    "asset_id",
    "asset_type",
    "business_unit",
    "business_criticality",
    "failed_logons_24h",
    "privileged_changes_7d",
    "suspicious_powershell_7d",
    "suricata_high_alerts_7d",
    "firewall_policy_exposure",
    "attack_path_score",
    "vulnerability_score",
    "control_effectiveness",
    "residual_risk_score",
    "evidence_integrity_score",
    "risk_trend_30d",
    "generated_at",
]


def bounded(value: int, minimum: int = 0, maximum: int = 100) -> int:
    """Keep score values inside the documented range."""
    return max(minimum, min(maximum, value))


def generate_record(index: int, generated_at: str) -> dict[str, int | str]:
    """Create one synthetic enterprise telemetry record."""
    asset_type = random.choice(ASSET_TYPES)
    criticality = random.randint(1, 5)

    failed_logons = random.randint(0, 45)
    privileged_changes = random.randint(0, 10)
    suspicious_powershell = random.randint(0, 8)
    suricata_alerts = random.randint(0, 12)

    firewall_exposure = random.randint(5, 90)
    attack_path_score = random.randint(5, 95)
    vulnerability_score = random.randint(5, 100)
    control_effectiveness = random.randint(35, 98)
    evidence_integrity = random.randint(55, 100)
    risk_trend = random.randint(-25, 35)

    # Make a realistic minority of records materially riskier.
    if random.random() < 0.22:
        failed_logons += random.randint(20, 60)
        privileged_changes += random.randint(3, 10)
        suspicious_powershell += random.randint(2, 8)
        suricata_alerts += random.randint(3, 12)
        firewall_exposure += random.randint(10, 35)
        attack_path_score += random.randint(10, 35)
        vulnerability_score += random.randint(10, 30)
        control_effectiveness -= random.randint(10, 30)
        evidence_integrity -= random.randint(5, 25)
        risk_trend += random.randint(10, 35)

    residual_risk = bounded(
        round(
            (
                firewall_exposure * 0.16
                + attack_path_score * 0.20
                + vulnerability_score * 0.20
                + (100 - control_effectiveness) * 0.18
                + failed_logons * 0.18
                + suspicious_powershell * 3.5
                + suricata_alerts * 2.5
                + max(risk_trend, 0) * 0.8
            )
            / 1.8
        )
    )

    return {
        "asset_id": f"LHT-Asset-{index:03d}",
        "asset_type": asset_type,
        "business_unit": random.choice(BUSINESS_UNITS),
        "business_criticality": criticality,
        "failed_logons_24h": failed_logons,
        "privileged_changes_7d": privileged_changes,
        "suspicious_powershell_7d": suspicious_powershell,
        "suricata_high_alerts_7d": suricata_alerts,
        "firewall_policy_exposure": bounded(firewall_exposure),
        "attack_path_score": bounded(attack_path_score),
        "vulnerability_score": bounded(vulnerability_score),
        "control_effectiveness": bounded(control_effectiveness),
        "residual_risk_score": residual_risk,
        "evidence_integrity_score": bounded(evidence_integrity),
        "risk_trend_30d": risk_trend,
        "generated_at": generated_at,
    }


def main() -> None:
    DATASETS_DIR.mkdir(parents=True, exist_ok=True)
    generated_at = datetime.now(timezone.utc).isoformat()

    records = [generate_record(index, generated_at) for index in range(1, 251)]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(records)

    print(f"[+] Generated {len(records)} synthetic telemetry records")
    print(f"[+] Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
