# ATT&CK Correlation Catalog

| Correlation Rule | ATT&CK Technique | Trigger Condition | Analyst Interpretation |
|---|---|---|---|
| Credential pressure | T1110 — Brute Force | `failed_logons_24h >= 40` | Review authentication source, target, account pattern, and MFA evidence |
| Privilege manipulation | T1098 — Account Manipulation | `privileged_changes_7d >= 7` | Validate authorization, group-change evidence, and blast radius |
| PowerShell execution risk | T1059.001 — PowerShell | `suspicious_powershell_7d >= 5` | Review command-line telemetry, parent process, and detection coverage |
| Lateral-movement exposure | T1021 — Remote Services | `attack_path_score >= 70` | Review reachable administrative paths and segmentation controls |
| Network discovery signal | T1046 — Network Service Discovery | `suricata_high_alerts_7d >= 8` | Validate alert context, source, destination, and firewall evidence |
| External exposure risk | T1190 — Exploit Public-Facing Application | `firewall_policy_exposure >= 70` | Review exposed services, rule justification, and policy ownership |
| Exploitation opportunity | T1210 — Exploitation of Remote Services | `vulnerability_score >= 75` | Validate patch status, exploitability, and reachable services |
| Control-drift amplification | N/A — Governance Context | `control_effectiveness <= 55` | Review validation failures and remediation status |
| Residual-risk escalation | N/A — Governance Context | `residual_risk_score >= 70` | Prioritize treatment decision and accountable owner |
