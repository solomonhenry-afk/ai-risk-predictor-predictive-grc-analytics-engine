# Phase B — Telemetry Preparation and Feature Engineering

## Objective

Build a reproducible telemetry-preparation pipeline that converts enterprise security and governance signals into a model-ready risk dataset.

## Scope

This phase uses synthetic-but-realistic records because the portfolio environment must remain safe, reproducible, and free of sensitive operational data. The data model reflects telemetry and validation outputs produced across Lighthouse Technology Domains 1–4.

## Input Signal Categories

| Signal Category         | Example Inputs                                                                    | Lighthouse Source |
| ----------------------- | --------------------------------------------------------------------------------- | ----------------- |
| Identity telemetry      | Failed logons, privileged-group changes, stale administrative accounts            | Domain 1, Task 3  |
| Endpoint telemetry      | Suspicious PowerShell, Sysmon anomalies, endpoint investigation signals           | Domain 2          |
| Network telemetry       | Firewall policy exposure, blocked traffic, Suricata alerts, segmentation findings | Domain 3          |
| Attack-path telemetry   | Blast radius, toxic permissions, privilege-path exposure                          | Task 3            |
| Control telemetry       | Validation status, control effectiveness, evidence completeness                   | Task 2            |
| Remediation telemetry   | Residual risk, remediation effectiveness, resilience score                        | Task 4            |
| Vulnerability telemetry | Severity, exploitability, remediation age, asset criticality                      | Domain 4          |

## Pipeline

```text
Synthetic Raw Telemetry
        ↓
Schema Validation
        ↓
Asset and Identity Enrichment
        ↓
Feature Engineering
        ↓
Risk Label Generation
        ↓
Model-Ready Dataset
        ↓
Data-Quality Report
```

## Model-Ready Feature Set

| Feature                  | Description                                          |
| ------------------------ | ---------------------------------------------------- |
| asset_id                 | Canonical enterprise asset identifier                |
| asset_type               | Asset classification                                 |
| business_criticality     | Business impact rating from 1 to 5                   |
| failed_logons_24h        | Failed authentication attempts in the prior 24 hours |
| privileged_changes_7d    | Privileged-group changes in the prior seven days     |
| suspicious_powershell_7d | High-risk PowerShell events in the prior seven days  |
| suricata_high_alerts_7d  | High-severity network alerts in the prior seven days |
| firewall_policy_exposure | Firewall governance exposure score                   |
| attack_path_score        | Identity and lateral-movement exposure score         |
| vulnerability_score      | Vulnerability severity and exploitability score      |
| control_effectiveness    | Validated control effectiveness score                |
| residual_risk_score      | Remaining risk after remediation                     |
| evidence_integrity_score | Evidence quality and traceability score              |
| risk_trend_30d           | Rolling risk trend indicator                         |
| anomaly_signal_count     | Number of elevated telemetry indicators              |
| high_risk_label          | Historical-style training label                      |
| generated_at             | Dataset generation timestamp                         |

## Data-Quality Requirements

* No missing asset identifiers
* No duplicate asset and observation-date pairs
* Scores remain within documented ranges
* Labels are derived from explainable conditions
* Synthetic records must not contain real credentials, private IP addresses, personal data, or production identifiers
* Every generated output must include generation metadata

## Phase B Deliverables

* Synthetic raw telemetry dataset
* Model-ready feature dataset
* Feature-engineering script
* Data-quality validation script
* Data-quality report
