Excellent—Phase G is proven: the workflow executed successfully, completed in 1m 5s, and retained one governance-artifact package. That is strong evidence of scheduled/manual CI/CD capability rather than a static dashboard.

## Phase H — Executive Risk Intelligence, Reporting, Evidence Packaging, and Portfolio Delivery

Phase H packages Task 5 as a recruiter-ready engineering project. The final deliverables are a polished README, an executive-facing report set, screenshot evidence, GitHub proof, and a substantive LinkedIn narrative.

Create the Phase H completion record:

```bash
nano docs/PHASE-H-EXECUTIVE-RISK-INTELLIGENCE-REPORTING-EVIDENCE-AND-PORTFOLIO-DELIVERY.md
```

```markdown
# Phase H — Executive Risk Intelligence, Reporting, Evidence, and Portfolio Delivery

## Objective

Package the AI Risk Predictor — Predictive GRC Analytics Engine as an enterprise-grade portfolio project demonstrating telemetry-driven GRC engineering, predictive cyber-risk analytics, executive reporting, and governed CI/CD automation.

## Final Product

The project delivers a Flask and Plotly command center that transforms validated Lighthouse Technology telemetry into:

- predicted enterprise risk tiers
- high-risk asset prioritization
- anomaly detection
- ATT&CK-aligned threat correlation
- explainable forecast evidence
- analyst review queues
- executive operational metrics
- downloadable governance reports
- CI/CD-generated evidence artifacts

## Evidence Captured

- Flask dashboard operating at `http://127.0.0.1:5000`
- executive KPI cards and risk distribution visualizations
- high-risk asset queue
- threat-priority correlation view
- prediction-validation and explainability outputs
- executive operations report
- GitHub Actions workflow success
- GitHub Actions artifact package
- workflow configuration showing `contents: read`

## Governance Boundary

The AI Risk Predictor is an advisory decision-support system. It does not autonomously declare incidents, attribute threat activity, alter access, modify controls, or initiate remediation.

## Portfolio Outcome

Task 5 demonstrates that GRC can be engineered as a live operational capability rather than maintained as retrospective compliance documentation.
```

Create a screenshot inventory:

```bash
nano docs/SCREENSHOT-INVENTORY.md
```

```markdown
# Screenshot Inventory — AI Risk Predictor

| ID | Screenshot | Evidence Demonstrated | Suggested Filename |
|---|---|---|---|
| H-01 | Flask terminal startup | Local application service running | `H-01-flask-dashboard-startup.png` |
| H-02 | AI Risk Predictor dashboard overview | Executive risk intelligence command center | `H-02-ai-risk-predictor-dashboard.png` |
| H-03 | KPI cards and risk distribution chart | Predictive risk prioritization | `H-03-executive-risk-kpis.png` |
| H-04 | High-risk asset queue | Analyst review and remediation prioritization | `H-04-high-risk-asset-queue.png` |
| H-05 | Threat-priority chart | Threat analytics and ATT&CK correlation | `H-05-threat-priority-correlation.png` |
| H-06 | Prediction validation results | Model validation and review evidence | `H-06-prediction-validation-results.png` |
| H-07 | Asset-level explainability output | Explainable AI governance evidence | `H-07-asset-level-explainability.png` |
| H-08 | Executive operations report | Board-ready governance reporting | `H-08-executive-operations-report.png` |
| H-09 | GitHub Actions successful workflow | CI/CD governance automation | `H-09-github-actions-success.png` |
| H-10 | GitHub Actions artifact package | Retained audit evidence | `H-10-governance-artifact-package.png` |
| H-11 | Workflow YAML permissions | Least-privilege CI/CD configuration | `H-11-workflow-read-only-permissions.png` |

## Screenshot Handling

- Redact secrets, tokens, internal IP addresses, hostnames, usernames, and personally identifiable information.
- Keep filenames consistent with this inventory.
- Store final screenshots in `screenshots/`.
- Use screenshots as evidence pointers in the README and LinkedIn post, not as a substitute for technical explanation.
```

Create the final executive summary:

```bash
nano reports/EXECUTIVE-SUMMARY-AI-RISK-PREDICTOR.md
```

```markdown
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
```

Create the final Task 5 README:

```bash
nano README.md
```

````markdown
# AI Risk Predictor — Predictive GRC Analytics Engine

> **Transforming validated enterprise telemetry into explainable cyber-risk forecasts, governance intelligence, and executive decision support.**

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Command%20Center-black?logo=flask)
![Plotly](https://img.shields.io/badge/Plotly-Executive%20Analytics-3f4f75?logo=plotly)
![Machine Learning](https://img.shields.io/badge/ML-Risk%20Forecasting-orange)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-Governed%20Automation-2088FF?logo=githubactions)
![GRC Engineering](https://img.shields.io/badge/GRC-Telemetry--Driven-success)

## Enterprise Security Evolution

This repository is part of the **Lighthouse Technology Enterprise Security Evolution**, a practical security-engineering portfolio built around live infrastructure telemetry, adversary simulation, control validation, attack-surface analysis, remediation engineering, and executive cyber-resilience reporting.

The AI Risk Predictor is Task 5 of Domain 4: **Enterprise GRC Intelligence, Risk Analytics & Cyber Resilience Engineering**.

---

## The Problem

Traditional GRC programs often rely on manually assembled evidence, spreadsheet risk registers, point-in-time control reviews, and retrospective reporting.

That approach cannot answer operational questions quickly enough:

- Which assets are most likely to become high risk?
- Which control gaps are emerging before an audit failure?
- Which identity, network, vulnerability, and detection signals are converging?
- Which findings need analyst review now?
- Which remediation actions are most likely to reduce residual risk?
- How can executive reporting remain traceable to operational evidence?

This project addresses those questions through a telemetry-driven predictive GRC analytics engine.

---

## Solution Overview

The AI Risk Predictor ingests model-ready features derived from validated Lighthouse Technology telemetry and produces:

- predictive high-risk probability scoring
- anomaly detection
- risk-tier prioritization
- threat and ATT&CK correlation
- analyst review queues
- feature-level explainability evidence
- executive operational metrics
- governance reports
- CI/CD-retained evidence artifacts

```text
Validated Lighthouse Telemetry
        │
        ├── Identity and authentication signals
        ├── Sysmon and PowerShell telemetry
        ├── Firewall and Suricata events
        ├── Vulnerability intelligence
        ├── Attack-path and IAM exposure
        ├── Control-validation outcomes
        └── Remediation and resilience evidence
        │
        ▼
Feature Engineering + Data Quality Validation
        │
        ▼
Risk Forecasting + Anomaly Detection
        │
        ▼
Threat Correlation + Explainability
        │
        ▼
Flask + Plotly Executive Command Center
        │
        ├── Executive KPIs
        ├── Predicted risk distribution
        ├── High-risk asset queue
        ├── Threat-priority analytics
        ├── Governance evidence
        └── Downloadable reports
        │
        ▼
GitHub Actions Governance Refresh
        ├── Validation
        ├── Retraining
        ├── Reporting
        └── Artifact retention
````

---

## Dashboard

The Flask command center provides an executive-facing view of:

* Critical and High predicted-risk assets
* anomalous telemetry profiles
* analyst-review requirements
* predicted enterprise risk distribution
* threat-priority correlation
* prioritized high-risk asset queue
* governance boundaries for model use

### Run Locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Engineering Phases

| Phase | Focus                     | Deliverable                                                     |
| ----- | ------------------------- | --------------------------------------------------------------- |
| A     | Telemetry source design   | Lighthouse telemetry inventory and ingestion design             |
| B     | Feature engineering       | Validated model-ready risk feature dataset                      |
| C     | Baseline forecasting      | Risk prediction and anomaly-detection model                     |
| D     | Threat analytics          | ATT&CK-aligned threat-priority correlation                      |
| E     | Validation and governance | Explainability, review queues, threshold governance             |
| F     | Command center            | Flask + Plotly AI Risk Predictor dashboard                      |
| G     | CI/CD automation          | Scheduled validation, retraining, reporting, artifact retention |
| H     | Portfolio delivery        | Executive reporting, evidence package, GitHub documentation     |

---

## Governance Controls

| Control Area          | Implementation                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------- |
| Data quality          | Required schema, completeness, uniqueness, and numeric-field validation                           |
| Human oversight       | High and Critical forecasts require analyst validation                                            |
| Explainability        | Feature-level model contribution records retained per asset                                       |
| Model validation      | False-positive and false-negative review queues generated                                         |
| Threshold governance  | Decision threshold documented and subject to review                                               |
| Evidence integrity    | SHA-256 evidence manifest generated for outputs, reports, and models                              |
| CI/CD least privilege | GitHub Actions uses `contents: read` and retains artifacts instead of committing generated output |
| Decision boundary     | The model does not autonomously declare incidents or execute remediation                          |

---

## Key Artifacts

| Artifact                                                   | Purpose                                     |
| ---------------------------------------------------------- | ------------------------------------------- |
| `output/baseline_risk_forecasts.csv`                       | Asset-level predictive risk forecasts       |
| `output/threat_priority_correlations.csv`                  | Threat and governance-priority correlation  |
| `output/prediction_validation_results.csv`                 | Validation outcomes for model review        |
| `output/asset_level_explainability.csv`                    | Feature-level forecast explanation evidence |
| `output/false_positive_review_queue.csv`                   | Model-improvement review queue              |
| `output/false_negative_review_queue.csv`                   | Missed-risk review queue                    |
| `output/task5_evidence_manifest.json`                      | Evidence-integrity manifest                 |
| `output/executive_operational_metrics.json`                | Executive risk metrics                      |
| `reports/EXECUTIVE-AI-RISK-PREDICTOR-OPERATIONS-REPORT.md` | Automated executive operations report       |
| `reports/EXECUTIVE-SUMMARY-AI-RISK-PREDICTOR.md`           | Leadership summary                          |
| `.github/workflows/ai-risk-predictor-refresh.yml`          | Governed CI/CD refresh workflow             |

---

## CI/CD Governance Automation

The GitHub Actions workflow supports:

* manual execution through `workflow_dispatch`
* scheduled Monday refresh at 06:00 UTC
* telemetry dataset validation
* model retraining
* threat correlation refresh
* explainability and validation output generation
* executive-report generation
* artifact retention for 90 days

The workflow intentionally uses read-only repository access:

```yaml
permissions:
  contents: read
```

Generated governance outputs are retained as GitHub Actions artifacts rather than automatically committed to the repository.

---

## Evidence Package

See:

* [`docs/SCREENSHOT-INVENTORY.md`](docs/SCREENSHOT-INVENTORY.md)
* [`docs/PHASE-H-EXECUTIVE-RISK-INTELLIGENCE-REPORTING-EVIDENCE-AND-PORTFOLIO-DELIVERY.md`](docs/PHASE-H-EXECUTIVE-RISK-INTELLIGENCE-REPORTING-EVIDENCE-AND-PORTFOLIO-DELIVERY.md)
* [`reports/EXECUTIVE-SUMMARY-AI-RISK-PREDICTOR.md`](reports/EXECUTIVE-SUMMARY-AI-RISK-PREDICTOR.md)

---

## Tech Stack

* Python
* Flask
* Plotly
* Pandas
* Scikit-learn
* Joblib
* GitHub Actions
* GitHub Actions Artifacts
* MITRE ATT&CK correlation
* GRC control validation and evidence engineering

---

## Project Structure

```text
.
├── app/                    # Flask command center
├── datasets/               # Validated model-ready telemetry features
├── docs/                   # Architecture, governance, evidence, phase records
├── models/                 # Baseline model artifacts
├── output/                 # Forecasts, explainability, metrics, evidence manifest
├── reports/                # Executive and governance reports
├── scripts/                # Pipeline, model, validation, reporting automation
├── screenshots/            # Curated portfolio evidence
├── .github/workflows/      # CI/CD governance automation
├── requirements.txt
├── run.py
└── README.md
```

---

## Author

**Solomon Henry**
Cybersecurity | GRC Engineering | Security Automation | AI Governance | Risk Analytics

> Security is not measured by preventing every attack. It is measured by understanding systems deeply enough to detect, investigate, and continuously improve against evolving threats.

---

## Connect

* GitHub: [https://github.com/solomonhenry-afk](https://github.com/solomonhenry-afk)
* LinkedIn: Add your LinkedIn profile URL here

---

## License

This project is provided for educational, portfolio, and authorized-lab demonstration purposes. It uses sanitized and simulated Lighthouse Technology telemetry artifacts and does not contain production secrets or sensitive operational data.

````

Project Artifact:

:::writing{variant="social_post" id="58419"}
I built an AI Risk Predictor from validated security telemetry—not a spreadsheet risk register.

The project is part of my Lighthouse Technology Enterprise Security Evolution portfolio: a telemetry-driven GRC engineering environment designed to show how security operations, governance, risk, remediation, and executive reporting can work as one operating model.

The problem I wanted to solve was straightforward:

Most GRC reporting is retrospective. Evidence is collected manually. Risk is reviewed after the control gap, the audit finding, or the security event has already happened.

That model does not answer the questions leaders need answered now:

- Which assets are most likely to become high risk?
- Which telemetry signals are converging into a control or resilience concern?
- Which anomalies need analyst validation?
- Which remediation actions should be prioritized first?
- What evidence supports the current risk posture?

So I built the AI Risk Predictor — Predictive GRC Analytics Engine.

It uses validated Lighthouse Technology telemetry features derived from identity activity, authentication failures, privileged changes, suspicious PowerShell activity, Suricata alerts, firewall exposure, vulnerability intelligence, attack-path exposure, control effectiveness, evidence integrity, and residual-risk indicators.

The result is a Flask and Plotly command center that provides:

• predicted enterprise risk tiers  
• high-risk asset prioritization  
• anomaly detection  
• ATT&CK-aligned threat correlation  
• analyst review queues  
• feature-level explainability  
• executive operational metrics  
• downloadable governance reports  

The engineering work did not stop at a dashboard.

I built the governance controls around the model:

• data-quality validation before every run  
• false-positive and false-negative review queues  
• documented decision thresholds  
• asset-level explainability records  
• human review requirements for High and Critical findings  
• SHA-256 evidence manifests  
• executive reporting artifacts  

Then I operationalized it with GitHub Actions.

The CI/CD workflow now validates the dataset, retrains the baseline model, refreshes threat analytics, regenerates explainability and governance reports, and retains the complete evidence package as an artifact. The workflow completed successfully and uses read-only repository permissions, so automation can generate auditable outputs without being allowed to alter source-controlled files.

This is the GRC direction I am building toward:

Not compliance documentation assembled after the fact.

Operational governance intelligence generated from real telemetry, controlled by evidence, explainability, human oversight, and automation.

GRC practitioners do not need to become software engineers.

They need to become engineers of governance systems: people who can see a manual process, understand the risk it creates, and build a better operating model.
