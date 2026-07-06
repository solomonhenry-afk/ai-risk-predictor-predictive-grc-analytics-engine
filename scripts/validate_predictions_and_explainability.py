#!/usr/bin/env python3
"""
Task 5 Phase E:
Validate baseline predictions, generate review queues, and preserve
asset-level explainability for governance use.

This script supports analyst review. It does not make autonomous security,
employment, access-control, or remediation decisions.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
MODELS_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "output"

FEATURE_FILE = DATASETS_DIR / "model_ready_risk_features.csv"
FORECAST_FILE = OUTPUT_DIR / "baseline_risk_forecasts.csv"
MODEL_FILE = MODELS_DIR / "baseline_risk_forecast_model.joblib"

VALIDATION_FILE = OUTPUT_DIR / "prediction_validation_results.csv"
EXPLAINABILITY_FILE = OUTPUT_DIR / "asset_level_explainability.csv"
FALSE_POSITIVE_FILE = OUTPUT_DIR / "false_positive_review_queue.csv"
FALSE_NEGATIVE_FILE = OUTPUT_DIR / "false_negative_review_queue.csv"
THRESHOLD_FILE = OUTPUT_DIR / "threshold_validation_summary.json"

FEATURE_COLUMNS = [
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
]

TARGET_COLUMN = "high_risk_label"


def classify_outcome(actual: int, predicted: int) -> str:
    if actual == 1 and predicted == 1:
        return "True Positive"
    if actual == 0 and predicted == 0:
        return "True Negative"
    if actual == 0 and predicted == 1:
        return "False Positive"
    return "False Negative"


def analyst_action(outcome: str, probability: float) -> str:
    if outcome == "False Positive":
        return (
            "Validate contributing telemetry, document benign explanation if confirmed, "
            "and retain as model-improvement evidence."
        )
    if outcome == "False Negative":
        return (
            "Review missed risk signals, validate feature coverage, and consider "
            "threshold or feature-engineering improvement."
        )
    if probability >= 0.75:
        return "Validate evidence immediately and assign analyst review."
    if probability >= 0.50:
        return "Validate evidence during priority risk triage."
    return "Continue monitoring and retain forecast evidence."


def main() -> None:
    required_files = [FEATURE_FILE, FORECAST_FILE, MODEL_FILE]
    missing_files = [str(path) for path in required_files if not path.exists()]

    if missing_files:
        raise FileNotFoundError(
            "Missing required Phase B or Phase C artifacts:\n"
            + "\n".join(missing_files)
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    features = pd.read_csv(FEATURE_FILE)
    forecasts = pd.read_csv(FORECAST_FILE)
    model = joblib.load(MODEL_FILE)

    merged = features.merge(
        forecasts[
            [
                "asset_id",
                "high_risk_probability",
                "predicted_risk_tier",
                "model_confidence",
                "anomaly_flag",
                "analyst_review_required",
            ]
        ],
        on="asset_id",
        how="inner",
        validate="one_to_one",
    )

    merged["predicted_high_risk_label"] = (
        merged["high_risk_probability"] >= 0.50
    ).astype(int)

    merged["validation_outcome"] = merged.apply(
        lambda row: classify_outcome(
            int(row[TARGET_COLUMN]),
            int(row["predicted_high_risk_label"]),
        ),
        axis=1,
    )

    merged["analyst_action"] = merged.apply(
        lambda row: analyst_action(
            row["validation_outcome"],
            float(row["high_risk_probability"]),
        ),
        axis=1,
    )

    validation_columns = [
        "asset_id",
        "asset_type",
        "business_unit",
        TARGET_COLUMN,
        "predicted_high_risk_label",
        "high_risk_probability",
        "predicted_risk_tier",
        "model_confidence",
        "anomaly_flag",
        "validation_outcome",
        "analyst_action",
    ]

    validation = merged[validation_columns].copy()
    validation["generated_at"] = datetime.now(timezone.utc).isoformat()
    validation.to_csv(VALIDATION_FILE, index=False)

    false_positives = validation[
        validation["validation_outcome"] == "False Positive"
    ].copy()
    false_negatives = validation[
        validation["validation_outcome"] == "False Negative"
    ].copy()

    false_positives.to_csv(FALSE_POSITIVE_FILE, index=False)
    false_negatives.to_csv(FALSE_NEGATIVE_FILE, index=False)

    classifier = model.named_steps["classifier"]
    coefficients = classifier.coef_[0]

    scaled_values = model.named_steps["scaler"].transform(
        merged[FEATURE_COLUMNS]
    )

    explainability_rows = []

    for row_index, (_, row) in enumerate(merged.iterrows()):
        contributions = []

        for feature_index, feature_name in enumerate(FEATURE_COLUMNS):
            contribution = (
                scaled_values[row_index][feature_index]
                * coefficients[feature_index]
            )

            contributions.append(
                {
                    "feature": feature_name,
                    "feature_value": round(
                        float(row[feature_name]),
                        4,
                    ),
                    "contribution": round(float(contribution), 6),
                    "direction": (
                        "Increases predicted risk"
                        if contribution > 0
                        else "Reduces predicted risk"
                    ),
                }
            )

        contributions.sort(
            key=lambda item: abs(item["contribution"]),
            reverse=True,
        )

        top_contributors = contributions[:5]

        explainability_rows.append(
            {
                "asset_id": row["asset_id"],
                "asset_type": row["asset_type"],
                "high_risk_probability": round(
                    float(row["high_risk_probability"]),
                    4,
                ),
                "predicted_risk_tier": row["predicted_risk_tier"],
                "validation_outcome": row["validation_outcome"],
                "top_risk_contributors": json.dumps(top_contributors),
                "explainability_statement": (
                    "Contributions are derived from the baseline logistic-regression "
                    "model and support analyst interpretation. They do not establish "
                    "causation or incident attribution."
                ),
                "generated_at": datetime.now(timezone.utc).isoformat(),
            }
        )

    explainability = pd.DataFrame(explainability_rows)
    explainability.to_csv(EXPLAINABILITY_FILE, index=False)

    threshold_summary = {
        "report_name": "Task 5 Phase E Threshold Validation Summary",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "decision_threshold": 0.50,
        "decision_rule": (
            "Assets at or above the threshold are classified as predicted high risk "
            "and routed for analyst review."
        ),
        "record_count": int(len(validation)),
        "true_positive_count": int(
            (validation["validation_outcome"] == "True Positive").sum()
        ),
        "true_negative_count": int(
            (validation["validation_outcome"] == "True Negative").sum()
        ),
        "false_positive_count": int(
            (validation["validation_outcome"] == "False Positive").sum()
        ),
        "false_negative_count": int(
            (validation["validation_outcome"] == "False Negative").sum()
        ),
        "governance_note": (
            "Threshold changes require documented review by the model owner and "
            "GRC lead, including assessment of false-positive and false-negative impact."
        ),
    }

    with THRESHOLD_FILE.open("w", encoding="utf-8") as file:
        json.dump(threshold_summary, file, indent=2)

    print("[+] Prediction validation complete")
    print(
        "[+] False positives: "
        f"{threshold_summary['false_positive_count']}"
    )
    print(
        "[+] False negatives: "
        f"{threshold_summary['false_negative_count']}"
    )
    print(f"[+] Validation output: {VALIDATION_FILE}")
    print(f"[+] Explainability output: {EXPLAINABILITY_FILE}")
    print(f"[+] Threshold summary: {THRESHOLD_FILE}")


if __name__ == "__main__":
    main()
