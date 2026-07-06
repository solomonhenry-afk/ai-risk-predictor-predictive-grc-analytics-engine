# Phase C — Baseline Risk Forecasting and Anomaly Detection Summary

**Generated:** 2026-07-06T07:52:58.986428+00:00

## Purpose

This report summarizes advisory baseline risk forecasts and anomaly detection results. Outputs support analyst triage and governance review; they do not authorize autonomous remediation or enforcement.

## Model Performance

- Accuracy: **93.65%**
- Precision: **88.89%**
- Recall: **88.89%**
- ROC-AUC: **0.9864**

## Forecast Distribution

- Critical: **62**
- High: **15**
- Medium: **17**
- Low: **156**
- Anomalous telemetry profiles: **30**
- Assets requiring analyst review: **80**

## Highest-Priority Analyst Review Candidates

| Asset | Type | Risk Probability | Tier | Anomaly | Residual Risk |
|---|---|---:|---|---|---:|
| LHT-Asset-096 | workstation | 100.00% | Critical | Yes | 100 |
| LHT-Asset-043 | windows_server | 100.00% | Critical | Yes | 100 |
| LHT-Asset-154 | domain_controller | 100.00% | Critical | Yes | 100 |
| LHT-Asset-024 | firewall | 100.00% | Critical | Yes | 100 |
| LHT-Asset-161 | linux_server | 100.00% | Critical | Yes | 96 |
| LHT-Asset-058 | domain_controller | 100.00% | Critical | Yes | 84 |
| LHT-Asset-149 | workstation | 100.00% | Critical | Yes | 83 |
| LHT-Asset-212 | firewall | 99.99% | Critical | Yes | 81 |
| LHT-Asset-191 | linux_server | 99.99% | Critical | Yes | 100 |
| LHT-Asset-049 | application_server | 99.99% | Critical | Yes | 93 |

## Governance Interpretation

The highest-priority records should be reviewed alongside their identity, network, detection, vulnerability, control-validation, and remediation evidence. A high probability or anomaly flag is a triage signal, not proof of compromise.

## Required Analyst Actions

1. Validate the supporting telemetry and evidence references.
2. Confirm whether the predicted exposure is current.
3. Check for control drift or incomplete remediation.
4. Assign remediation ownership when residual risk is unacceptable.
5. Record false positives and false negatives for future model review.
