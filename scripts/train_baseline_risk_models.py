#!/usr/bin/env python3
"""
Task 5 Phase C:
Train explainable baseline risk forecasting and anomaly detection models.

The models are advisory decision-support tools. They do not perform autonomous
security enforcement or remediation actions.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
MODELS_DIR = BASE_DIR / "models"
OUTPUT_DIR = BASE_DIR / "output"

INPUT_FILE = DATASETS_DIR / "model_ready_risk_features.csv"
FORECAST_FILE = OUTPUT_DIR / "baseline_risk_forecasts.csv"
METRICS_FILE = OUTPUT_DIR / "baseline_model_metrics.json"
IMPORTANCE_FILE = OUTPUT_DIR / "baseline_feature_importance.json"

RISK_MODEL_FILE = MODELS_DIR / "baseline_risk_forecast_model.joblib"
ANOMALY_MODEL_FILE = MODELS_DIR / "baseline_anomaly_detection_model.joblib"

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


def risk_tier(probability: float) -> str:
    """Convert probability into an analyst-friendly triage tier."""
    if probability >= 0.75:
        return "Critical"
    if probability >= 0.50:
        return "High"
    if probability >= 0.25:
        return "Medium"
    return "Low"


def confidence_label(probability: float) -> str:
    """Use distance from 0.50 as a simple baseline confidence indicator."""
    distance = abs(probability - 0.50) * 2

    if distance >= 0.75:
        return "High"
    if distance >= 0.40:
        return "Medium"
    return "Low"


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Missing dataset: {INPUT_FILE}. Run Phase B first."
        )

    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dataset = pd.read_csv(INPUT_FILE)

    missing_columns = [
        column
        for column in FEATURE_COLUMNS + [TARGET_COLUMN, "asset_id", "asset_type"]
        if column not in dataset.columns
    ]
    if missing_columns:
        raise ValueError(f"Dataset missing required columns: {missing_columns}")

    X = dataset[FEATURE_COLUMNS]
    y = dataset[TARGET_COLUMN]

    if y.nunique() < 2:
        raise ValueError(
            "The training label must contain both high-risk and non-high-risk records."
        )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=2026,
        stratify=y,
    )

    risk_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "classifier",
                LogisticRegression(
                    max_iter=2000,
                    class_weight="balanced",
                    random_state=2026,
                ),
            ),
        ]
    )

    risk_pipeline.fit(X_train, y_train)

    test_probabilities = risk_pipeline.predict_proba(X_test)[:, 1]
    test_predictions = (test_probabilities >= 0.50).astype(int)

    metrics = {
        "report_name": "Task 5 Phase C Baseline Model Metrics",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "dataset": str(INPUT_FILE),
        "model_type": "Logistic Regression",
        "training_record_count": int(len(X_train)),
        "test_record_count": int(len(X_test)),
        "accuracy": round(float(accuracy_score(y_test, test_predictions)), 4),
        "precision": round(
            float(precision_score(y_test, test_predictions, zero_division=0)),
            4,
        ),
        "recall": round(
            float(recall_score(y_test, test_predictions, zero_division=0)),
            4,
        ),
        "roc_auc": round(float(roc_auc_score(y_test, test_probabilities)), 4),
        "confusion_matrix": confusion_matrix(y_test, test_predictions).tolist(),
        "classification_report": classification_report(
            y_test,
            test_predictions,
            output_dict=True,
            zero_division=0,
        ),
        "governance_statement": (
            "This baseline model is advisory. Predictions require analyst review "
            "and must not be used as autonomous enforcement decisions."
        ),
    }

    classifier = risk_pipeline.named_steps["classifier"]
    importance = sorted(
        [
            {
                "feature": feature,
                "coefficient": round(float(coefficient), 6),
                "absolute_importance": round(float(abs(coefficient)), 6),
            }
            for feature, coefficient in zip(FEATURE_COLUMNS, classifier.coef_[0])
        ],
        key=lambda item: item["absolute_importance"],
        reverse=True,
    )

    anomaly_pipeline = Pipeline(
        steps=[
            ("scaler", StandardScaler()),
            (
                "detector",
                IsolationForest(
                    contamination=0.12,
                    random_state=2026,
                    n_estimators=250,
                ),
            ),
        ]
    )

    anomaly_pipeline.fit(X)

    probabilities = risk_pipeline.predict_proba(X)[:, 1]
    anomaly_predictions = anomaly_pipeline.predict(X)
    anomaly_scores = anomaly_pipeline.decision_function(X)

    forecast = dataset[
        [
            "asset_id",
            "asset_type",
            "business_unit",
            "business_criticality",
            "residual_risk_score",
            "identity_risk_score",
            "network_risk_score",
            "detection_gap_score",
            "governance_risk_score",
            "anomaly_signal_count",
        ]
    ].copy()

    forecast["high_risk_probability"] = probabilities.round(4)
    forecast["predicted_risk_tier"] = [
        risk_tier(probability) for probability in probabilities
    ]
    forecast["model_confidence"] = [
        confidence_label(probability) for probability in probabilities
    ]
    forecast["anomaly_score"] = anomaly_scores.round(4)
    forecast["anomaly_flag"] = [
        "Yes" if prediction == -1 else "No"
        for prediction in anomaly_predictions
    ]
    forecast["analyst_review_required"] = [
        "Yes"
        if probability >= 0.50 or anomaly_prediction == -1
        else "No"
        for probability, anomaly_prediction in zip(
            probabilities,
            anomaly_predictions,
        )
    ]
    forecast["generated_at"] = datetime.now(timezone.utc).isoformat()

    forecast.to_csv(FORECAST_FILE, index=False)

    with METRICS_FILE.open("w", encoding="utf-8") as file:
        json.dump(metrics, file, indent=2)

    with IMPORTANCE_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            {
                "report_name": "Task 5 Phase C Baseline Feature Importance",
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "model_type": "Logistic Regression",
                "features": importance,
            },
            file,
            indent=2,
        )

    joblib.dump(risk_pipeline, RISK_MODEL_FILE)
    joblib.dump(anomaly_pipeline, ANOMALY_MODEL_FILE)

    high_or_critical = forecast[
        forecast["predicted_risk_tier"].isin(["High", "Critical"])
    ].shape[0]
    anomalies = forecast[forecast["anomaly_flag"] == "Yes"].shape[0]

    print("[+] Baseline risk forecast model trained")
    print("[+] Baseline anomaly detection model trained")
    print(f"[+] High or Critical predicted assets: {high_or_critical}")
    print(f"[+] Anomalous telemetry profiles: {anomalies}")
    print(f"[+] Forecast output: {FORECAST_FILE}")
    print(f"[+] Metrics output: {METRICS_FILE}")
    print(f"[+] Feature importance output: {IMPORTANCE_FILE}")


if __name__ == "__main__":
    main()
