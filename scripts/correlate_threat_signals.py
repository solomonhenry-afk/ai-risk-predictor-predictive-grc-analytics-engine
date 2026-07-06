#!/usr/bin/env python3
"""
Task 5 Phase D:
Correlate risk forecasts with ATT&CK-aligned identity, endpoint, network,
vulnerability, control, and remediation signals.

Outputs are advisory triage intelligence. They are not incident declarations
and do not perform autonomous response actions.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATASETS_DIR = BASE_DIR / "datasets"
OUTPUT_DIR = BASE_DIR / "output"

FEATURE_FILE = DATASETS_DIR / "model_ready_risk_features.csv"
FORECAST_FILE = OUTPUT_DIR / "baseline_risk_forecasts.csv"
OUTPUT_FILE = OUTPUT_DIR / "threat_priority_correlations.csv"


def bounded(value: float, minimum: int = 0, maximum: int = 100) -> int:
    return max(minimum, min(maximum, round(value)))


def add_attack_context(row: pd.Series) -> tuple[list[str], list[str], list[str]]:
    """Return ATT&CK techniques, observed signals, and analyst actions."""
    techniques: list[str] = []
    signals: list[str] = []
    actions: list[str] = []

    if row["failed_logons_24h"] >= 40:
        techniques.append("T1110 Brute Force")
        signals.append("Elevated failed logons")
        actions.append("Review authentication pattern and MFA evidence")

    if row["privileged_changes_7d"] >= 7:
        techniques.append("T1098 Account Manipulation")
        signals.append("Elevated privileged-group changes")
        actions.append("Validate authorization and privilege blast radius")

    if row["suspicious_powershell_7d"] >= 5:
        techniques.append("T1059.001 PowerShell")
        signals.append("Elevated suspicious PowerShell activity")
        actions.append("Review endpoint command and parent-process telemetry")

    if row["attack_path_score"] >= 70:
        techniques.append("T1021 Remote Services")
        signals.append("High attack-path exposure")
        actions.append("Review reachable administrative paths and segmentation")

    if row["suricata_high_alerts_7d"] >= 8:
        techniques.append("T1046 Network Service Discovery")
        signals.append("High-severity network alert volume")
        actions.append("Validate alert source, destination, and firewall evidence")

    if row["firewall_policy_exposure"] >= 70:
        techniques.append("T1190 Exploit Public-Facing Application")
        signals.append("Elevated firewall-policy exposure")
        actions.append("Review exposed services and firewall-rule justification")

    if row["vulnerability_score"] >= 75:
        techniques.append("T1210 Exploitation of Remote Services")
        signals.append("High vulnerability exposure")
        actions.append("Validate patch status, exploitability, and reachability")

    if row["control_effectiveness"] <= 55:
        signals.append("Reduced control effectiveness")
        actions.append("Review control-validation failures and remediation owner")

    if row["residual_risk_score"] >= 70:
        signals.append("Elevated residual risk")
        actions.append("Prioritize risk-treatment decision")

    return techniques, signals, actions


def priority_tier(score: int) -> str:
    if score >= 80:
        return "Critical"
    if score >= 60:
        return "High"
    if score >= 35:
        return "Medium"
    return "Low"


def main() -> None:
    if not FEATURE_FILE.exists() or not FORECAST_FILE.exists():
        raise FileNotFoundError(
            "Missing Phase B or Phase C output. Run those phases first."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    features = pd.read_csv(FEATURE_FILE)
    forecasts = pd.read_csv(FORECAST_FILE)

    merged = features.merge(
        forecasts[
            [
                "asset_id",
                "high_risk_probability",
                "predicted_risk_tier",
                "model_confidence",
                "anomaly_score",
                "anomaly_flag",
                "analyst_review_required",
            ]
        ],
        on="asset_id",
        how="inner",
        validate="one_to_one",
    )

    correlations = []

    for _, row in merged.iterrows():
        techniques, signals, actions = add_attack_context(row)

        signal_convergence = len(signals)
        anomaly_bonus = 15 if row["anomaly_flag"] == "Yes" else 0
        review_bonus = 8 if row["analyst_review_required"] == "Yes" else 0

        threat_priority_score = bounded(
            row["high_risk_probability"] * 40
            + row["business_criticality"] * 6
            + row["attack_path_score"] * 0.14
            + row["network_risk_score"] * 0.10
            + row["identity_risk_score"] * 0.10
            + row["governance_risk_score"] * 0.08
            + signal_convergence * 4
            + anomaly_bonus
            + review_bonus
        )

        correlations.append(
            {
                "asset_id": row["asset_id"],
                "asset_type": row["asset_type"],
                "business_unit": row["business_unit"],
                "business_criticality": row["business_criticality"],
                "high_risk_probability": round(row["high_risk_probability"], 4),
                "predicted_risk_tier": row["predicted_risk_tier"],
                "model_confidence": row["model_confidence"],
                "anomaly_flag": row["anomaly_flag"],
                "anomaly_score": round(row["anomaly_score"], 4),
                "attack_techniques": "; ".join(techniques) if techniques else "No elevated ATT&CK mapping",
                "correlated_signals": "; ".join(signals) if signals else "No elevated correlation signals",
                "signal_convergence_count": signal_convergence,
                "threat_priority_score": threat_priority_score,
                "threat_priority_tier": priority_tier(threat_priority_score),
                "analyst_actions": "; ".join(dict.fromkeys(actions))
                if actions
                else "Continue normal monitoring",
                "evidence_context": (
                    "Identity telemetry; endpoint telemetry; network telemetry; "
                    "attack-path analysis; control validation; remediation scoring"
                ),
                "generated_at": datetime.now(timezone.utc).isoformat(),
            }
        )

    output = pd.DataFrame(correlations).sort_values(
        by=["threat_priority_score", "high_risk_probability"],
        ascending=[False, False],
    )

    output.to_csv(OUTPUT_FILE, index=False)

    print(f"[+] Correlated {len(output)} asset telemetry profiles")
    print(
        "[+] Critical/High threat-priority findings: "
        f"{len(output[output['threat_priority_tier'].isin(['Critical', 'High'])])}"
    )
    print(f"[+] Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
