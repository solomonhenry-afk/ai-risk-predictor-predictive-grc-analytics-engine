# Phase A — Predictive-Risk Architecture and Data Design

## Objective

Design the architecture, prediction targets, telemetry inputs, governance boundaries, and feature model for the Lighthouse Technology AI Risk Prediction and Threat Analytics Engine.

## Core Principle

The engine does not replace analyst judgment, incident response, or governance accountability.

It prioritizes security attention by transforming validated enterprise telemetry into explainable risk predictions, anomaly indicators, and confidence-scored recommendations.

## Prediction Targets

| Prediction Target | Question Answered | Example Output |
|---|---|---|
| Asset risk probability | Which asset is likely to become high risk? | 0–100 risk probability |
| Identity exposure probability | Which identity may create elevated blast radius? | Privilege-risk likelihood |
| Detection-gap probability | Where may visibility be insufficient? | Detection coverage risk |
| Compliance-drift probability | Which control may drift from expected operation? | Drift likelihood score |
| Remediation urgency | Which unresolved issue should be treated first? | Priority and treatment recommendation |
| Threat anomaly score | Which event pattern deserves investigation? | Anomaly score and evidence |

## Architecture

```text
Domain 1–4 Evidence
        ↓
Telemetry Preparation
        ↓
Feature Engineering
        ↓
Risk and Threat Models
        ↓
Prediction, Anomaly, and Confidence Scores
        ↓
Governance Correlation
        ↓
Executive Risk Forecasting and Analyst Triage
