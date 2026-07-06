#!/usr/bin/env python3
"""Generate a CI/CD-ready executive governance report for Task 5."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
REPORTS_DIR = BASE_DIR / "reports"

METRICS_FILE = OUTPUT_DIR / "executive_operational_metrics.json"
REPORT_FILE = REPORTS_DIR / "EXECUTIVE-AI-RISK-PREDICTOR-OPERATIONS-REPORT.md"


def main() -> None:
    if not METRICS_FILE.exists():
        raise FileNotFoundError(
            "Missing executive metrics. Run generate_operational_metrics.py first."
        )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    metrics = json.loads(METRICS_FILE.read_text(encoding="utf-8"))

    report = f"""# Executive AI Risk Predictor Operations Report

**Generated:** {datetime.now(timezone.utc).isoformat()}

## Purpose

This report summarizes the latest automated governance refresh for the Lighthouse Technology AI Risk Predictor. It combines validated telemetry-derived forecasting, anomaly detection, threat correlation, explainability, and model-governance evidence.

## Executive Risk Snapshot

| Metric | Current Value |
|---|---:|
| Telemetry profiles processed | {metrics["telemetry_profiles_processed"]} |
| Critical predicted-risk assets | {metrics["critical_predicted_risk_assets"]} |
| High predicted-risk assets | {metrics["high_predicted_risk_assets"]} |
| Anomalous telemetry profiles | {metrics["anomalous_telemetry_profiles"]} |
| Analyst reviews required | {metrics["analyst_review_required"]} |
| Critical threat-priority findings | {metrics["critical_threat_priority_findings"]} |
| High threat-priority findings | {metrics["high_threat_priority_findings"]} |

## Prediction Validation Snapshot

| Validation Metric | Current Value |
|---|---:|
| True positives | {metrics["true_positive_count"]} |
| False positives | {metrics["false_positive_count"]} |
| False negatives | {metrics["false_negative_count"]} |

## Governance Interpretation

The pipeline has refreshed model outputs and governance artifacts. High and Critical findings remain advisory until analysts validate supporting telemetry, ATT&CK context, control effectiveness, remediation status, and evidence integrity.

## CI/CD Control Evidence

- Scheduled workflow execution
- Dataset quality validation
- Baseline model retraining
- Threat-correlation refresh
- Explainability and validation refresh
- Evidence-manifest generation
- Executive report generation
- Retained GitHub Actions artifact package

## Decision Boundary

The AI Risk Predictor supports risk prioritization and executive communication. It does not autonomously declare incidents, change controls, modify access, or initiate remediation.
"""

    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"[+] Executive operations report created: {REPORT_FILE}")


if __name__ == "__main__":
    main()
