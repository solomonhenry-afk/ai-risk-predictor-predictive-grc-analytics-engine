#!/usr/bin/env python3
"""
Transform synthetic raw telemetry into a model-ready risk feature dataset.
"""

from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"

INPUT_FILE = DATASETS_DIR / "synthetic_raw_telemetry.csv"
OUTPUT_FILE = DATASETS_DIR / "model_ready_risk_features.csv"

NUMERIC_FIELDS = [
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
]

FEATURE_FIELDS = [
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
    "identity_risk_score",
    "network_risk_score",
    "detection_gap_score",
    "governance_risk_score",
    "anomaly_signal_count",
    "high_risk_label",
    "feature_generated_at",
]


def to_int(record: dict[str, str], field: str) -> int:
    """Convert CSV values to integers with explicit validation."""
    try:
        return int(record[field])
    except (KeyError, ValueError) as error:
        raise ValueError(f"Invalid numeric field '{field}' for {record.get('asset_id')}") from error


def bounded(value: float, minimum: int = 0, maximum: int = 100) -> int:
    return max(minimum, min(maximum, round(value)))


def engineer_features(record: dict[str, str], generated_at: str) -> dict[str, int | str]:
    values = {field: to_int(record, field) for field in NUMERIC_FIELDS}

    identity_risk = bounded(
        values["failed_logons_24h"] * 1.0
        + values["privileged_changes_7d"] * 4.0
        + values["attack_path_score"] * 0.45
    )

    network_risk = bounded(
        values["firewall_policy_exposure"] * 0.55
        + values["suricata_high_alerts_7d"] * 4.0
        + values["vulnerability_score"] * 0.20
    )

    detection_gap = bounded(
        (100 - values["control_effectiveness"]) * 0.55
        + (100 - values["evidence_integrity_score"]) * 0.20
        + values["suspicious_powershell_7d"] * 5.0
    )

    governance_risk = bounded(
        values["residual_risk_score"] * 0.55
        + max(values["risk_trend_30d"], 0) * 1.2
        + (100 - values["evidence_integrity_score"]) * 0.25
    )

    anomaly_signals = sum(
        [
            values["failed_logons_24h"] >= 40,
            values["privileged_changes_7d"] >= 7,
            values["suspicious_powershell_7d"] >= 5,
            values["suricata_high_alerts_7d"] >= 8,
            values["firewall_policy_exposure"] >= 70,
            values["attack_path_score"] >= 70,
            values["vulnerability_score"] >= 75,
            values["control_effectiveness"] <= 55,
            values["residual_risk_score"] >= 70,
            values["risk_trend_30d"] >= 20,
        ]
    )

    high_risk_label = int(
        values["residual_risk_score"] >= 70
        or (
            anomaly_signals >= 4
            and values["business_criticality"] >= 4
        )
    )

    return {
        "asset_id": record["asset_id"],
        "asset_type": record["asset_type"],
        "business_unit": record["business_unit"],
        **values,
        "identity_risk_score": identity_risk,
        "network_risk_score": network_risk,
        "detection_gap_score": detection_gap,
        "governance_risk_score": governance_risk,
        "anomaly_signal_count": anomaly_signals,
        "high_risk_label": high_risk_label,
        "feature_generated_at": generated_at,
    }


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Missing input dataset: {INPUT_FILE}. "
            "Run generate_synthetic_telemetry.py first."
        )

    generated_at = datetime.now(timezone.utc).isoformat()

    with INPUT_FILE.open("r", newline="", encoding="utf-8") as source:
        reader = csv.DictReader(source)
        records = [engineer_features(record, generated_at) for record in reader]

    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as destination:
        writer = csv.DictWriter(destination, fieldnames=FEATURE_FIELDS)
        writer.writeheader()
        writer.writerows(records)

    high_risk_count = sum(record["high_risk_label"] for record in records)

    print(f"[+] Engineered {len(records)} model-ready feature records")
    print(f"[+] High-risk training labels: {high_risk_count}")
    print(f"[+] Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
