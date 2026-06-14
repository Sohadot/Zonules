---
term: Error Analysis
slug: error-analysis
route: /error-analysis/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: verification
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-294
concept_id: CON-error-analysis
safety_class: technical
canonical: https://zonules.com/error-analysis/
last_reviewed: 2026-06-14
claims: [CLM-1172, CLM-1173, CLM-1174, CLM-1175]
sources: [SRC-017, SRC-027, SRC-004]
related_terms: [evaluation-metrics, dataset-bias, model-calibration, robustness]
seo_title: "Error Analysis | Zonules.com"
meta_description: "Error analysis is the systematic study of the cases a model gets wrong."
---

# Error Analysis

> Not how often a model is right, but how it is wrong.

## Definition

Error analysis is the systematic study of the cases a model gets wrong. [CLM-1172]

## Scientific Grounding

Grouping errors by type reveals failure patterns that aggregate metrics hide. [CLM-1173] It guides targeted improvements more effectively than a single accuracy number. [CLM-1174]

*Sources: SRC-017, SRC-027. See the source registry for classification.*

## Machine-Vision Role

Error analysis is an interpretation-layer audit: it asks not how often a model is right but how and why it is wrong. [CLM-1175]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** verification
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Error Analysis is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Evaluation Metrics](/evaluation-metrics/) — related governed reference unit.
- [Dataset Bias](/dataset-bias/) — related governed reference unit.
- [Model Calibration](/model-calibration/) — related governed reference unit.
- [Robustness](/robustness/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017, SRC-027 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1172, CLM-1173, CLM-1174 sourced; CLM-1175 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
