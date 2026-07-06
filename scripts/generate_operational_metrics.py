#!/usr/bin/env python3
"""Generate executive operational metrics from Task 5 outputs."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"

FORECAST_FILE = OUTPUT_DIR / "baseline_risk_forecasts.csv"
THREAT_FILE = OUTPUT_DIR / "threat_priority_correlations.csv"
VALIDATION_FILE = OUTPUT_DIR / "prediction_validation_results.csv"
METRICS_FILE = OUTPUT_DIR / "executive_operational_metrics.json"


def count_where(data: pd.DataFrame, column: str, value: str) -> int:
    return int((data[column] == value).sum())


def main() -> None:
    required = [FORECAST_FILE, THREAT_FILE, VALIDATION_FILE]
    missing = [str(path) for path in required if not path.exists()]

    if missing:
        raise FileNotFoundError(
            "Missing required Task 5 output files:\n" + "\n".join(missing)
        )

    forecasts = pd.read_csv(FORECAST_FILE)
    threats = pd.read_csv(THREAT_FILE)
    validation = pd.read_csv(VALIDATION_FILE)

    metrics = {
        "project": "AI Risk Predictor — Predictive GRC Analytics Engine",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "telemetry_profiles_processed": int(len(forecasts)),
        "critical_predicted_risk_assets": count_where(
            forecasts, "predicted_risk_tier", "Critical"
        ),
        "high_predicted_risk_assets": count_where(
            forecasts, "predicted_risk_tier", "High"
        ),
        "anomalous_telemetry_profiles": count_where(
            forecasts, "anomaly_flag", "Yes"
        ),
        "analyst_review_required": count_where(
            forecasts, "analyst_review_required", "Yes"
        ),
        "critical_threat_priority_findings": count_where(
            threats, "threat_priority_tier", "Critical"
        ),
        "high_threat_priority_findings": count_where(
            threats, "threat_priority_tier", "High"
        ),
        "true_positive_count": count_where(
            validation, "validation_outcome", "True Positive"
        ),
        "false_positive_count": count_where(
            validation, "validation_outcome", "False Positive"
        ),
        "false_negative_count": count_where(
            validation, "validation_outcome", "False Negative"
        ),
        "governance_note": (
            "Metrics support executive prioritization and require human validation "
            "before escalation or remediation decisions."
        ),
    }

    METRICS_FILE.write_text(
        json.dumps(metrics, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"[+] Executive operational metrics created: {METRICS_FILE}")


if __name__ == "__main__":
    main()
