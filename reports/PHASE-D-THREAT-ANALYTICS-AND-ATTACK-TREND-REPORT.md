# Phase D — Threat Analytics and Attack-Trend Correlation Report

**Generated:** 2026-07-06T09:16:36.680783+00:00

## Executive Summary

This report correlates predictive risk outputs with ATT&CK-aligned identity, endpoint, network, vulnerability, control, and remediation signals. Findings are analyst-review candidates, not incident declarations.

## Threat-Priority Distribution

- Critical: **81**
- High: **35**
- Medium: **122**
- Low: **12**
- Anomalous telemetry profiles: **30**

## Most Frequent ATT&CK-Aligned Correlations

- **T1059.001 PowerShell:** 127 correlated asset profiles
- **T1098 Account Manipulation:** 126 correlated asset profiles
- **T1046 Network Service Discovery:** 110 correlated asset profiles
- **T1021 Remote Services:** 81 correlated asset profiles
- **T1210 Exploitation of Remote Services:** 81 correlated asset profiles
- **T1190 Exploit Public-Facing Application:** 76 correlated asset profiles
- **T1110 Brute Force:** 74 correlated asset profiles

## Highest-Priority Analyst Triage Candidates

| Asset | Tier | Score | Probability | Anomaly | ATT&CK Context |
|---|---|---:|---:|---|---|
| LHT-Asset-024 | Critical | 100 | 100.00% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1210 Exploitation of Remote Services |
| LHT-Asset-043 | Critical | 100 | 100.00% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application |
| LHT-Asset-058 | Critical | 100 | 100.00% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application |
| LHT-Asset-096 | Critical | 100 | 100.00% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application |
| LHT-Asset-149 | Critical | 100 | 100.00% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application |
| LHT-Asset-154 | Critical | 100 | 100.00% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application |
| LHT-Asset-161 | Critical | 100 | 100.00% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application; T1210 Exploitation of Remote Services |
| LHT-Asset-049 | Critical | 100 | 99.99% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery |
| LHT-Asset-191 | Critical | 100 | 99.99% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application; T1210 Exploitation of Remote Services |
| LHT-Asset-192 | Critical | 100 | 99.99% | Yes | T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1190 Exploit Public-Facing Application; T1210 Exploitation of Remote Services |
| LHT-Asset-212 | Critical | 100 | 99.99% | Yes | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1190 Exploit Public-Facing Application |
| LHT-Asset-048 | Critical | 100 | 99.98% | No | T1110 Brute Force; T1098 Account Manipulation; T1059.001 PowerShell; T1021 Remote Services; T1046 Network Service Discovery; T1210 Exploitation of Remote Services |

## Analyst Workflow

1. Validate source telemetry and evidence references.
2. Confirm whether the ATT&CK-aligned behavior is authorized or expected.
3. Review identity blast radius, network reachability, and vulnerability context.
4. Validate control effectiveness and remediation status.
5. Escalate only when evidence supports a security event or unacceptable residual risk.

## Governance Statement

The correlation engine prioritizes review using synthetic portfolio data. It does not attribute activity, declare compromise, or initiate automated response.
