#!/usr/bin/env python3
"""Validate the Task 5 model-ready Lighthouse telemetry feature dataset."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "datasets" / "model_ready_risk_features.csv"

REQUIRED_COLUMNS = {
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
}


def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

    data = pd.read_csv(DATA_FILE)

    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        raise ValueError(
            "Missing required columns: " + ", ".join(sorted(missing_columns))
        )

    if data.empty:
        raise ValueError("Dataset is empty.")

    if data["asset_id"].isna().any():
        raise ValueError("asset_id contains null values.")

    if data["asset_id"].duplicated().any():
        raise ValueError("asset_id contains duplicate values.")

    numeric_columns = REQUIRED_COLUMNS.difference(
        {"asset_id", "asset_type", "business_unit"}
    )

    null_numeric_columns = [
        column
        for column in numeric_columns
        if data[column].isna().any()
    ]

    if null_numeric_columns:
        raise ValueError(
            "Null values found in required numeric columns: "
            + ", ".join(sorted(null_numeric_columns))
        )

    print("[+] Task 5 data quality validation passed")
    print(f"[+] Dataset: {DATA_FILE}")
    print(f"[+] Telemetry profiles: {len(data)}")
    print(f"[+] Required columns validated: {len(REQUIRED_COLUMNS)}")


if __name__ == "__main__":
    main()
