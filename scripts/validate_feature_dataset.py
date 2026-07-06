#!/usr/bin/env python3
"""
Validate Task 5 model-ready risk features and produce a governance-ready report.
"""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_FILE = DATASETS_DIR / "model_ready_risk_features.csv"
REPORT_FILE = OUTPUT_DIR / "phase_b_data_quality_report.json"

REQUIRED_FIELDS = [
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

SCORE_FIELDS = [
    "firewall_policy_exposure",
    "attack_path_score",
    "vulnerability_score",
    "control_effectiveness",
    "residual_risk_score",
    "evidence_integrity_score",
    "identity_risk_score",
    "network_risk_score",
    "detection_gap_score",
    "governance_risk_score",
]


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Missing feature dataset: {INPUT_FILE}. "
            "Run engineer_risk_features.py first."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    issues: list[str] = []
    seen_assets: set[str] = set()
    row_count = 0
    high_risk_count = 0

    with INPUT_FILE.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        missing_columns = [field for field in REQUIRED_FIELDS if field not in reader.fieldnames]
        if missing_columns:
            issues.append(f"Missing required columns: {', '.join(missing_columns)}")

        for row_number, row in enumerate(reader, start=2):
            row_count += 1
            asset_id = row.get("asset_id", "").strip()

            if not asset_id:
                issues.append(f"Row {row_number}: missing asset_id")
                continue

            if asset_id in seen_assets:
                issues.append(f"Row {row_number}: duplicate asset_id {asset_id}")
            seen_assets.add(asset_id)

            for field in REQUIRED_FIELDS:
                if not row.get(field, "").strip():
                    issues.append(f"Row {row_number}: missing value for {field}")

            for field in SCORE_FIELDS:
                try:
                    value = int(row[field])
                    if not 0 <= value <= 100:
                        issues.append(
                            f"Row {row_number}: {field} outside expected range 0-100"
                        )
                except ValueError:
                    issues.append(f"Row {row_number}: invalid numeric value for {field}")

            try:
                label = int(row["high_risk_label"])
                if label not in (0, 1):
                    issues.append(f"Row {row_number}: high_risk_label must be 0 or 1")
                high_risk_count += label
            except ValueError:
                issues.append(f"Row {row_number}: invalid high_risk_label")

    report = {
        "report_name": "Task 5 Phase B Data Quality Report",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dataset": str(INPUT_FILE),
        "record_count": row_count,
        "unique_asset_count": len(seen_assets),
        "high_risk_label_count": high_risk_count,
        "high_risk_label_rate_percent": round(
            (high_risk_count / row_count * 100) if row_count else 0,
            2,
        ),
        "quality_status": "PASS" if not issues else "FAIL",
        "issue_count": len(issues),
        "issues": issues,
        "governance_statement": (
            "The dataset is synthetic and contains no production credentials, "
            "private IP addresses, personal data, or real enterprise identifiers."
        ),
    }

    with REPORT_FILE.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    print(f"[+] Data-quality status: {report['quality_status']}")
    print(f"[+] Records validated: {row_count}")
    print(f"[+] Issues found: {len(issues)}")
    print(f"[+] Report: {REPORT_FILE}")

    if issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
