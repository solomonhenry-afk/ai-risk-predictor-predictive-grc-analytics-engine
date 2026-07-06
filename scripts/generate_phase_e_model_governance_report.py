#!/usr/bin/env python3
"""Generate the Task 5 Phase E model validation and governance report."""

from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
REPORTS_DIR = BASE_DIR / "reports"

VALIDATION_FILE = OUTPUT_DIR / "prediction_validation_results.csv"
EXPLAINABILITY_FILE = OUTPUT_DIR / "asset_level_explainability.csv"
THRESHOLD_FILE = OUTPUT_DIR / "threshold_validation_summary.json"
REPORT_FILE = REPORTS_DIR / "PHASE-E-MODEL-VALIDATION-EXPLAINABILITY-AND-GOVERNANCE-REPORT.md"


def main() -> None:
    required_files = [
        VALIDATION_FILE,
        EXPLAINABILITY_FILE,
        THRESHOLD_FILE,
    ]

    missing_files = [str(path) for path in required_files if not path.exists()]

    if missing_files:
        raise FileNotFoundError(
            "Missing Phase E output files:\n" + "\n".join(missing_files)
        )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    validation = pd.read_csv(VALIDATION_FILE)
    explainability = pd.read_csv(EXPLAINABILITY_FILE)

    with THRESHOLD_FILE.open("r", encoding="utf-8") as file:
        threshold_summary = json.load(file)

    outcome_counts = Counter(validation["validation_outcome"])
    high_confidence_count = int(
        (validation["model_confidence"] == "High").sum()
    )

    false_positive_sample = validation[
        validation["validation_outcome"] == "False Positive"
    ].head(5)

    false_negative_sample = validation[
        validation["validation_outcome"] == "False Negative"
    ].head(5)

    top_explainability_sample = explainability.sort_values(
        by="high_risk_probability",
        ascending=False,
    ).head(5)

    lines = [
        "# Phase E — Prediction Validation, Explainability, and Governance Report",
        "",
        f"**Generated:** {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Executive Summary",
        "",
        "Phase E validates the baseline risk forecast against the known synthetic "
        "high-risk label, preserves asset-level explainability, and documents "
        "human oversight requirements. The model remains an advisory triage tool.",
        "",
        "## Threshold Governance",
        "",
        f"- Decision threshold: **{threshold_summary['decision_threshold']:.2f}**",
        "- Assets at or above the threshold are routed for analyst review.",
        "- Threshold changes require documented model-owner and GRC-lead review.",
        "",
        "## Validation Outcomes",
        "",
        f"- True positives: **{outcome_counts.get('True Positive', 0)}**",
        f"- True negatives: **{outcome_counts.get('True Negative', 0)}**",
        f"- False positives: **{outcome_counts.get('False Positive', 0)}**",
        f"- False negatives: **{outcome_counts.get('False Negative', 0)}**",
        f"- High-confidence forecasts: **{high_confidence_count}**",
        "",
        "## Explainability Evidence",
        "",
        f"- Asset-level explainability records generated: **{len(explainability)}**",
        "- Each record preserves the top feature contributions used by the baseline model.",
        "- Feature contributions explain model behavior; they do not establish causation.",
        "",
        "## False-Positive Review Queue",
        "",
        "| Asset | Probability | Tier | Required Analyst Action |",
        "|---|---:|---|---|",
    ]

    if false_positive_sample.empty:
        lines.append("| None | N/A | N/A | No false-positive records in this run |")
    else:
        for _, row in false_positive_sample.iterrows():
            lines.append(
                f"| {row['asset_id']} | {row['high_risk_probability']:.2%} | "
                f"{row['predicted_risk_tier']} | {row['analyst_action']} |"
            )

    lines.extend(
        [
            "",
            "## False-Negative Review Queue",
            "",
            "| Asset | Probability | Tier | Required Analyst Action |",
            "|---|---:|---|---|",
        ]
    )

    if false_negative_sample.empty:
        lines.append("| None | N/A | N/A | No false-negative records in this run |")
    else:
        for _, row in false_negative_sample.iterrows():
            lines.append(
                f"| {row['asset_id']} | {row['high_risk_probability']:.2%} | "
                f"{row['predicted_risk_tier']} | {row['analyst_action']} |"
            )

    lines.extend(
        [
            "",
            "## High-Risk Explainability Sample",
            "",
            "| Asset | Probability | Tier | Validation Outcome |",
            "|---|---:|---|---|",
        ]
    )

    for _, row in top_explainability_sample.iterrows():
        lines.append(
            f"| {row['asset_id']} | {row['high_risk_probability']:.2%} | "
            f"{row['predicted_risk_tier']} | {row['validation_outcome']} |"
        )

    lines.extend(
        [
            "",
            "## Governance Decision",
            "",
            "The baseline model may support risk prioritization when its output is "
            "reviewed with supporting telemetry, ATT&CK correlation, control "
            "validation, remediation evidence, and analyst judgment. It must not "
            "be used as an autonomous enforcement or incident-declaration mechanism.",
            "",
            "## Required Ongoing Controls",
            "",
            "1. Re-run data-quality checks before each model execution.",
            "2. Retain metrics, forecasts, explainability records, and review queues.",
            "3. Review false positives and false negatives after each run.",
            "4. Revalidate after changes to features, thresholds, source data, or models.",
            "5. Require human approval for escalation and remediation decisions.",
        ]
    )

    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"[+] Phase E governance report created: {REPORT_FILE}")


if __name__ == "__main__":
    main()
