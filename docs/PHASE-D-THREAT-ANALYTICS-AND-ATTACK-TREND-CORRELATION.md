# Phase D — Threat Analytics and Attack-Trend Correlation

## Objective

Correlate baseline risk forecasts and anomaly outputs with identity, endpoint, network, vulnerability, control, and remediation signals to produce explainable threat-priority intelligence.

## Core Question

Which assets require analyst attention because multiple security signals converge into a credible, evidence-backed risk scenario?

## Correlation Inputs

| Signal Area | Primary Indicators | Lighthouse Source |
|---|---|---|
| Identity | Failed logons, privileged changes, attack-path exposure | Domain 1, Task 3 |
| Endpoint | Suspicious PowerShell activity, anomaly indicators | Domain 2 |
| Network | Suricata alerts, firewall-policy exposure | Domain 3 |
| Vulnerability | Vulnerability score and asset criticality | Domain 4 |
| Governance | Control effectiveness, evidence integrity, residual risk | Tasks 2 and 4 |
| Predictive Analytics | High-risk probability, anomaly score, confidence | Task 5 Phase C |

## ATT&CK Correlation Logic

| Observed Signal | ATT&CK Technique | Correlation Meaning |
|---|---|---|
| Elevated failed logons | T1110 — Brute Force | Potential credential-access pressure |
| Privileged-group changes | T1098 — Account Manipulation | Potential account or privilege abuse |
| Suspicious PowerShell | T1059.001 — PowerShell | Potential execution or defense evasion |
| Attack-path exposure | T1021 — Remote Services | Potential lateral-movement opportunity |
| High-severity Suricata alerts | T1046 — Network Service Discovery | Potential reconnaissance or network discovery |
| Firewall-policy exposure | T1190 — Exploit Public-Facing Application | Increased external or unnecessary service exposure |
| High vulnerability score | T1190 / T1210 | Increased exploitation opportunity |

## Threat Priority Methodology

Threat priority is not a claim that an incident has occurred. It is a triage score based on:

- predictive high-risk probability;
- anomaly status;
- ATT&CK-aligned signal convergence;
- asset business criticality;
- identity and network exposure;
- control effectiveness;
- residual risk;
- evidence integrity.

## Governance Guardrails

- Correlated findings are analyst-review candidates, not incident declarations.
- ATT&CK mappings are behavioral context, not attribution.
- Each finding must preserve its contributing signals.
- Analysts validate supporting evidence before escalation.
- Findings are mapped to remediation ownership and control-review workflows.

## Phase D Deliverables

- ATT&CK correlation catalog
- Threat-priority dataset
- Attack-trend summary
- Analyst triage report
- Evidence-oriented correlation rationale
