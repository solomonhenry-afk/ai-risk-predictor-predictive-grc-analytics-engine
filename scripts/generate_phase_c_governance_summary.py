#!/usr/bin/env python3
"""
Generate a governance-ready Phase C summary from baseline forecast outputs.
"""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
REPORTS_DIR = BASE_DIR / "reports"

FORECAST_FILE = OUTPUT_DIR / "baseline_risk_forecasts.csv"
METRICS_FILE = OUTPUT_DIR / "baseline_model_metrics.json"
REPORT_FILE = REPORTS_DIR / "PHASE-C-BASELINE-RISK-FORECASTING-SUMMARY.md"


def main() -> None:
    if not FORECAST_FILE.exists() or not METRICS_FILE.exists():
        raise FileNotFoundError(
            "Missing Phase C outputs. Run train_baseline_risk_models.py first."
        )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    forecast = pd.read_csv(FORECAST_FILE)

    with METRICS_FILE.open("r", encoding="utf-8") as file:
        metrics = json.load(file)

    tier_counts = Counter(forecast["predicted_risk_tier"])
    confidence_counts = Counter(forecast["model_confidence"])
    anomaly_count = int((forecast["anomaly_flag"] == "Yes").sum())
    review_count = int((forecast["analyst_review_required"] == "Yes").sum())

    top_assets = forecast.sort_values(
        by=["high_risk_probability", "anomaly_score"],
        ascending=[False, True],
    ).head(10)

    lines = [
        "# Phase C — Baseline Risk Forecasting and Anomaly Detection Summary",
        "",
        f"**Generated:** {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Purpose",
        "",
        "This report summarizes advisory baseline risk forecasts and anomaly "
        "detection results. Outputs support analyst triage and governance review; "
        "they do not authorize autonomous remediation or enforcement.",
        "",
        "## Model Performance",
        "",
        f"- Accuracy: **{metrics['accuracy']:.2%}**",
        f"- Precision: **{metrics['precision']:.2%}**",
        f"- Recall: **{metrics['recall']:.2%}**",
        f"- ROC-AUC: **{metrics['roc_auc']:.4f}**",
        "",
        "## Forecast Distribution",
        "",
        f"- Critical: **{tier_counts.get('Critical', 0)}**",
        f"- High: **{tier_counts.get('High', 0)}**",
        f"- Medium: **{tier_counts.get('Medium', 0)}**",
        f"- Low: **{tier_counts.get('Low', 0)}**",
        f"- Anomalous telemetry profiles: **{anomaly_count}**",
        f"- Assets requiring analyst review: **{review_count}**",
        "",
        "## Highest-Priority Analyst Review Candidates",
        "",
        "| Asset | Type | Risk Probability | Tier | Anomaly | Residual Risk |",
        "|---|---|---:|---|---|---:|",
    ]

    for _, row in top_assets.iterrows():
        lines.append(
            f"| {row['asset_id']} | {row['asset_type']} | "
            f"{row['high_risk_probability']:.2%} | "
            f"{row['predicted_risk_tier']} | "
            f"{row['anomaly_flag']} | "
            f"{row['residual_risk_score']} |"
        )

    lines.extend(
        [
            "",
            "## Governance Interpretation",
            "",
            "The highest-priority records should be reviewed alongside their "
            "identity, network, detection, vulnerability, control-validation, "
            "and remediation evidence. A high probability or anomaly flag is a "
            "triage signal, not proof of compromise.",
            "",
            "## Required Analyst Actions",
            "",
            "1. Validate the supporting telemetry and evidence references.",
            "2. Confirm whether the predicted exposure is current.",
            "3. Check for control drift or incomplete remediation.",
            "4. Assign remediation ownership when residual risk is unacceptable.",
            "5. Record false positives and false negatives for future model review.",
        ]
    )

    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[+] Governance summary created: {REPORT_FILE}")


if __name__ == "__main__":
    main()
