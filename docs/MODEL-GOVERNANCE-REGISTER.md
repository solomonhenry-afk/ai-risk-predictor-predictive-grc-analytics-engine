# Model Governance Register

| Governance Area | Control Requirement | Evidence Artifact | Review Owner | Review Frequency |
|---|---|---|---|---|
| Model purpose | Model use is limited to advisory risk prioritization | Phase E validation report | GRC Lead | Quarterly |
| Data provenance | Inputs are traceable to documented Lighthouse telemetry datasets | Feature dataset and data-quality report | Security Engineering | Per run |
| Data quality | Required fields are complete and valid before model execution | Phase B quality-validation output | Data Owner | Per run |
| Explainability | Forecasts retain feature-level contribution context | Explainability dataset | Security Analyst | Per review |
| Human oversight | High and Critical findings require analyst validation | Analyst review queue | SOC / GRC Analyst | Per finding |
| Threshold governance | Risk thresholds are documented and reviewed | Threshold review section | Risk Owner | Quarterly |
| Performance monitoring | Accuracy, precision, recall, and ROC-AUC are retained | Model metrics JSON | Model Owner | Per run |
| Error review | False positives and false negatives are recorded and assessed | Prediction validation dataset | Security Analyst | Per run |
| Change management | Feature, threshold, and model changes require approval | Change record | GRC Lead | Per change |
| Retention | Model outputs and governance reports are retained | Output and report directories | Evidence Owner | Per run |
