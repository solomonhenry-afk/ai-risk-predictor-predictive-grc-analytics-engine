#!/usr/bin/env python3
"""Generate Task 5 Phase D attack-trend and analyst-triage reporting."""

from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
REPORTS_DIR = BASE_DIR / "reports"

INPUT_FILE = OUTPUT_DIR / "threat_priority_correlations.csv"
REPORT_FILE = REPORTS_DIR / "PHASE-D-THREAT-ANALYTICS-AND-ATTACK-TREND-REPORT.md"


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Missing threat correlations. Run correlate_threat_signals.py first."
        )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(INPUT_FILE)

    tier_counts = Counter(data["threat_priority_tier"])
    anomaly_count = int((data["anomaly_flag"] == "Yes").sum())

    technique_counter: Counter[str] = Counter()
    for value in data["attack_techniques"]:
        if value != "No elevated ATT&CK mapping":
            for technique in value.split("; "):
                technique_counter[technique] += 1

    top_findings = data.head(12)

    lines = [
        "# Phase D — Threat Analytics and Attack-Trend Correlation Report",
        "",
        f"**Generated:** {datetime.now(timezone.utc).isoformat()}",
        "",
        "## Executive Summary",
        "",
        "This report correlates predictive risk outputs with ATT&CK-aligned "
        "identity, endpoint, network, vulnerability, control, and remediation "
        "signals. Findings are analyst-review candidates, not incident declarations.",
        "",
        "## Threat-Priority Distribution",
        "",
        f"- Critical: **{tier_counts.get('Critical', 0)}**",
        f"- High: **{tier_counts.get('High', 0)}**",
        f"- Medium: **{tier_counts.get('Medium', 0)}**",
        f"- Low: **{tier_counts.get('Low', 0)}**",
        f"- Anomalous telemetry profiles: **{anomaly_count}**",
        "",
        "## Most Frequent ATT&CK-Aligned Correlations",
        "",
    ]

    if technique_counter:
        for technique, count in technique_counter.most_common():
            lines.append(f"- **{technique}:** {count} correlated asset profiles")
    else:
        lines.append("- No elevated ATT&CK-aligned correlations were generated.")

    lines.extend(
        [
            "",
            "## Highest-Priority Analyst Triage Candidates",
            "",
            "| Asset | Tier | Score | Probability | Anomaly | ATT&CK Context |",
            "|---|---|---:|---:|---|---|",
        ]
    )

    for _, row in top_findings.iterrows():
        lines.append(
            f"| {row['asset_id']} | {row['threat_priority_tier']} | "
            f"{row['threat_priority_score']} | "
            f"{row['high_risk_probability']:.2%} | "
            f"{row['anomaly_flag']} | {row['attack_techniques']} |"
        )

    lines.extend(
        [
            "",
            "## Analyst Workflow",
            "",
            "1. Validate source telemetry and evidence references.",
            "2. Confirm whether the ATT&CK-aligned behavior is authorized or expected.",
            "3. Review identity blast radius, network reachability, and vulnerability context.",
            "4. Validate control effectiveness and remediation status.",
            "5. Escalate only when evidence supports a security event or unacceptable residual risk.",
            "",
            "## Governance Statement",
            "",
            "The correlation engine prioritizes review using synthetic portfolio data. "
            "It does not attribute activity, declare compromise, or initiate automated response.",
        ]
    )

    REPORT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[+] Phase D report created: {REPORT_FILE}")


if __name__ == "__main__":
    main()
