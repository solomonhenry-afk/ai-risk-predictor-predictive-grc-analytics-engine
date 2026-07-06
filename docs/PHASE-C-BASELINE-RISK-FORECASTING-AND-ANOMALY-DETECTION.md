# Phase C — Baseline Risk Forecasting and Anomaly Detection

## Objective

Build explainable baseline analytics that forecast elevated asset risk and identify anomalous telemetry patterns from the Phase B model-ready risk dataset.

## Analytical Outputs

| Output | Purpose |
|---|---|
| High-risk probability | Estimates the likelihood that an asset belongs in the high-risk category |
| Predicted risk tier | Converts probability into Low, Medium, High, or Critical triage categories |
| Anomaly score | Identifies unusual telemetry combinations requiring analyst review |
| Anomaly flag | Marks records whose telemetry profile differs materially from the baseline |
| Model confidence | Shows the confidence level associated with the risk prediction |
| Feature importance | Explains which engineered features most influenced the baseline forecast |

## Baseline Models

| Model | Role | Reason for Use |
|---|---|---|
| Logistic Regression | High-risk probability forecasting | Explainable, auditable, and suitable for a baseline governance model |
| Isolation Forest | Anomaly detection | Identifies unusual multi-signal telemetry patterns without requiring labels |

## Governance Guardrails

- Predictions are advisory and require analyst review.
- The model does not block accounts, alter firewall rules, or perform autonomous remediation.
- Synthetic data is used for reproducibility and privacy protection.
- Every output includes a confidence score and evidence-oriented feature context.
- Model performance, false positives, and false negatives must be reviewed before operational use.
- Model artifacts and reports are retained for auditability.

## Risk Tier Thresholds

| Probability | Tier | Recommended Action |
|---:|---|---|
| 0.00–0.24 | Low | Continue monitoring |
| 0.25–0.49 | Medium | Review during normal risk triage |
| 0.50–0.74 | High | Assign analyst review and remediation consideration |
| 0.75–1.00 | Critical | Prioritize immediate analyst and governance review |

## Phase C Deliverables

- Trained baseline risk-forecast model
- Trained anomaly-detection model
- Risk forecast output dataset
- Model performance metrics
- Feature-importance report
- Governance-ready anomaly summary
