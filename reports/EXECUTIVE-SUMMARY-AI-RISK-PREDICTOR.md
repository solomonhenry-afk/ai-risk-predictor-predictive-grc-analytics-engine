# Executive Summary — AI Risk Predictor

## Decision Context

Lighthouse Technology required a way to move from retrospective compliance reporting toward continuous, telemetry-driven governance intelligence.

The AI Risk Predictor provides an operational risk view built from validated infrastructure telemetry, control-validation outcomes, attack-surface signals, vulnerability intelligence, identity-risk indicators, and remediation evidence.

## What the Command Center Answers

- Which assets are predicted to become high risk?
- Which telemetry profiles are anomalous?
- Which findings require analyst review?
- Which threat signals have the highest governance priority?
- What evidence supports the current risk posture?
- Where should remediation effort be prioritized?
- How is predictive model output governed and validated?

## Operational Capabilities

| Capability | Outcome |
|---|---|
| Telemetry feature engineering | Converts validated Lighthouse infrastructure signals into model-ready risk features |
| Predictive risk scoring | Prioritizes assets by forecasted high-risk probability |
| Anomaly detection | Identifies unusual multi-signal telemetry profiles |
| Threat correlation | Connects risk forecasts to ATT&CK-aligned threat context |
| Explainability | Preserves feature-level contributors for analyst interpretation |
| Governance validation | Tracks false positives, false negatives, thresholds, and human-review requirements |
| Executive reporting | Produces downloadable operational metrics and governance reports |
| CI/CD automation | Validates, retrains, reports, and retains evidence artifacts through GitHub Actions |

## Governance Position

The system is advisory. Human analysts validate High and Critical findings before escalation, remediation, or governance reporting decisions are made.

## Enterprise Value

The project demonstrates a GRC engineering model in which evidence, risk forecasting, control effectiveness, threat context, and executive reporting are generated from operational telemetry rather than assembled manually after the fact.
