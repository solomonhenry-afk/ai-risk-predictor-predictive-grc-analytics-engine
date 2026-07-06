# AI Risk Predictor - Predictive GRC Analytics Engine

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

# AI Risk Predictor — Predictive GRC Analytics Engine

> **Transforming validated enterprise telemetry into explainable cyber-risk forecasts, governance intelligence, and executive decision support.**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Command_Center-000000?logo=flask&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Executive_Analytics-3F4F75?logo=plotly&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine_Learning-Risk_Forecasting-FF6F00)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Governed_Automation-2088FF?logo=githubactions&logoColor=white)
![GRC Engineering](https://img.shields.io/badge/GRC_Engineering-Telemetry_Driven-2EA44F)

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

### To Run Locally

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
---

#  Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Command_Center-000000?logo=flask&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Executive_Analytics-3F4F75?logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Telemetry_Engineering-150458?logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Risk_Forecasting-F7931E?logo=scikitlearn&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Governed_Automation-2088FF?logo=githubactions&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Executive_Dashboard-000000?logo=flask&logoColor=white)
![MITRE ATT&CK](https://img.shields.io/badge/MITRE_ATT%26CK-Threat_Correlation-ED1C24)
![GRC Engineering](https://img.shields.io/badge/GRC_Engineering-Telemetry_Driven-2EA44F)

</div>

| Layer | Technologies and Capabilities |
|---|---|
| Application layer | Python, Flask, Jinja templates, HTML, CSS |
| Analytics layer | Pandas, scikit-learn, Joblib, risk forecasting, anomaly detection |
| Visualization layer | Plotly, executive KPI cards, risk distributions, analyst queues |
| Telemetry layer | Identity, endpoint, firewall, Suricata, vulnerability, control-validation, and remediation signals |
| Threat intelligence layer | MITRE ATT&CK correlation, attack-trend prioritization, threat-governance context |
| Governance layer | Data-quality validation, explainability, model validation, evidence manifests, human review gates |
| Automation layer | GitHub Actions, scheduled refresh, manual dispatch, artifact retention, least-privilege workflow permissions |
| Reporting layer | Executive operational metrics, downloadable governance reports, evidence packaging |

---

#  GitHub Analytics

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=solomonhenry-afk&show_icons=true&theme=tokyonight&hide_border=true&count_private=true)

![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=solomonhenry-afk&layout=compact&theme=tokyonight&hide_border=true)

![GitHub Streak](https://streak-stats.demolab.com?user=solomonhenry-afk&theme=tokyonight&hide_border=true)

</div>

---

#  Repository Visitors

<div align="center">

![Visitor Count](https://visitor-badge.laobi.icu/badge?page_id=solomonhenry-afk.ai-risk-predictor-predictive-grc-analytics-engine)

</div>

---

# 🤝 Connect With Me

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-solomonhenry--afk-181717?logo=github&logoColor=white)](https://github.com/solomonhenry-afk)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bassey-solomon-henry/)
[![Email](https://img.shields.io/badge/Email-Contact_Me-EA4335?logo=gmail&logoColor=white)](solomon_henry111@outlook.com)

</div>

---

##  Enterprise Security Evolution

This project is part of the **Lighthouse Technology Enterprise Security Evolution** portfolio: a practical, evidence-driven cybersecurity engineering program that connects infrastructure security, detection engineering, attack-surface intelligence, GRC automation, remediation validation, resilience scoring, and executive risk communication.

| Domain | Engineering Focus |
|---|---|
| Domain 1 | Enterprise infrastructure and security architecture |
| Domain 2 | Defensive operations, detection engineering, and threat visibility |
| Domain 3 | Offensive security validation, attack-path analysis, and remediation evidence |
| Domain 4 | Enterprise GRC intelligence, risk analytics, cyber resilience, and governance automation |

### Domain 4 Portfolio Tasks

| Task | Project |
|---|---|
| Task 1 | Enterprise Risk Telemetry Engineering |
| Task 2 | Automated GRC Control Validation Engine |
| Task 3 | Attack-Surface & IAM Governance Intelligence |
| Task 4 | Remediation Engineering & Resilience Scoring |
| Task 5 | AI Risk Predictor — Predictive GRC Analytics Engine |
| Task 6 | Live GRC Analytics Command Center & Insight Engine |

---
# Author
Bassey Solomon Henry

Cybersecurity | GRC Engineering | Security Automation | AI Governance | Risk Analytics
##  Personal Philosophy

> **Security is not measured by preventing every attack. It is measured by understanding systems deeply enough to detect, investigate, and continuously improve against evolving threats.**
>
> **— Solomon Henry**

The purpose of this project is not to replace security analysts or governance professionals with automation. It is to remove repetitive evidence-chasing, make risk signals easier to interpret, preserve traceability, and give human decision-makers a clearer basis for action.

---

##  Responsible Use

This repository is designed for education, portfolio demonstration, and authorized lab environments only.

- Telemetry is sanitized, simulated, or generated from authorized Lighthouse Technology lab infrastructure.
- No production credentials, private keys, sensitive personal data, or unredacted operational records are included.
- Model output is advisory and requires analyst validation.
- The application does not autonomously change infrastructure, access controls, policies, or incident status.

---

<div align="center">

### Built as part of the Lighthouse Technology Enterprise Security Evolution

**Telemetry-driven governance. Explainable risk intelligence. Human-led security decisions.**

[![Repository](https://img.shields.io/badge/View_on-GitHub-181717?logo=github&logoColor=white)](https://github.com/solomonhenry-afk/ai-risk-predictor-predictive-grc-analytics-engine)

</div>

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
