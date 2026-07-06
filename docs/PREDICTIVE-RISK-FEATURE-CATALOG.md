# Predictive Risk Feature Catalog

| Feature Group | Example Features | Source Domains |
|---|---|---|
| Identity Risk | Failed logons, privileged-group changes, stale admin accounts, service-account exposure | Domain 1, Task 3 |
| Endpoint Risk | Sysmon process anomalies, PowerShell activity, suspicious parent-child relationships | Domain 2 |
| Network Risk | Firewall policy exposure, blocked connections, Suricata severity, segmentation gaps | Domain 3 |
| Detection Risk | Alert coverage, rule effectiveness, investigation volume, telemetry gaps | Domain 2 |
| Vulnerability Risk | Severity, exploitability, asset criticality, remediation age | Domain 4 |
| Attack-Path Risk | Reachable privileged paths, toxic permissions, blast radius | Task 3 |
| Control Risk | Validation status, drift findings, evidence completeness | Task 2 |
| Resilience Risk | Residual-risk score, remediation effectiveness, resilience score | Task 4 |
| Temporal Risk | Event frequency, trend direction, rolling anomaly count | Task 5 |

## Initial Prediction Features

| Feature | Type | Description |
|---|---|---|
| failed_logons_24h | Numeric | Failed authentication attempts in the prior 24 hours |
| privileged_changes_7d | Numeric | Privileged-group changes in the prior seven days |
| suspicious_powershell_7d | Numeric | High-risk PowerShell events in the prior seven days |
| suricata_high_alerts_7d | Numeric | High-severity network alerts in the prior seven days |
| firewall_policy_exposure | Numeric | Exposure score derived from firewall governance |
| attack_path_score | Numeric | Identity and lateral-movement exposure score |
| vulnerability_score | Numeric | Vulnerability severity and exploitability score |
| control_effectiveness | Numeric | Validated control effectiveness score |
| residual_risk_score | Numeric | Post-remediation residual-risk score |
| evidence_integrity_score | Numeric | Evidence quality and traceability score |
| risk_trend_30d | Numeric | Rolling risk trend indicator |
| high_risk_label | Boolean | Historical outcome label for model training |
