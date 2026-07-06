# Phase E — Prediction Validation, Explainability, and Governance Report

**Generated:** 2026-07-06T09:16:38.952795+00:00

## Executive Summary

Phase E validates the baseline risk forecast against the known synthetic high-risk label, preserves asset-level explainability, and documents human oversight requirements. The model remains an advisory triage tool.

## Threshold Governance

- Decision threshold: **0.50**
- Assets at or above the threshold are routed for analyst review.
- Threshold changes require documented model-owner and GRC-lead review.

## Validation Outcomes

- True positives: **69**
- True negatives: **170**
- False positives: **8**
- False negatives: **3**
- High-confidence forecasts: **193**

## Explainability Evidence

- Asset-level explainability records generated: **250**
- Each record preserves the top feature contributions used by the baseline model.
- Feature contributions explain model behavior; they do not establish causation.

## False-Positive Review Queue

| Asset | Probability | Tier | Required Analyst Action |
|---|---:|---|---|
| LHT-Asset-028 | 74.87% | High | Validate contributing telemetry, document benign explanation if confirmed, and retain as model-improvement evidence. |
| LHT-Asset-031 | 71.86% | High | Validate contributing telemetry, document benign explanation if confirmed, and retain as model-improvement evidence. |
| LHT-Asset-035 | 70.22% | High | Validate contributing telemetry, document benign explanation if confirmed, and retain as model-improvement evidence. |
| LHT-Asset-123 | 94.41% | Critical | Validate contributing telemetry, document benign explanation if confirmed, and retain as model-improvement evidence. |
| LHT-Asset-185 | 53.40% | High | Validate contributing telemetry, document benign explanation if confirmed, and retain as model-improvement evidence. |

## False-Negative Review Queue

| Asset | Probability | Tier | Required Analyst Action |
|---|---:|---|---|
| LHT-Asset-064 | 37.44% | Medium | Review missed risk signals, validate feature coverage, and consider threshold or feature-engineering improvement. |
| LHT-Asset-166 | 40.70% | Medium | Review missed risk signals, validate feature coverage, and consider threshold or feature-engineering improvement. |
| LHT-Asset-224 | 40.96% | Medium | Review missed risk signals, validate feature coverage, and consider threshold or feature-engineering improvement. |

## High-Risk Explainability Sample

| Asset | Probability | Tier | Validation Outcome |
|---|---:|---|---|
| LHT-Asset-024 | 100.00% | Critical | True Positive |
| LHT-Asset-058 | 100.00% | Critical | True Positive |
| LHT-Asset-043 | 100.00% | Critical | True Positive |
| LHT-Asset-096 | 100.00% | Critical | True Positive |
| LHT-Asset-154 | 100.00% | Critical | True Positive |

## Governance Decision

The baseline model may support risk prioritization when its output is reviewed with supporting telemetry, ATT&CK correlation, control validation, remediation evidence, and analyst judgment. It must not be used as an autonomous enforcement or incident-declaration mechanism.

## Required Ongoing Controls

1. Re-run data-quality checks before each model execution.
2. Retain metrics, forecasts, explainability records, and review queues.
3. Review false positives and false negatives after each run.
4. Revalidate after changes to features, thresholds, source data, or models.
5. Require human approval for escalation and remediation decisions.
