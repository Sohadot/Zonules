---
term: Evaluation Metrics
slug: evaluation-metrics
route: /evaluation-metrics/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: verification
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-292
concept_id: CON-evaluation-metrics
safety_class: technical
canonical: https://zonules.com/evaluation-metrics/
last_reviewed: 2026-06-14
claims: [CLM-1164, CLM-1165, CLM-1166, CLM-1167]
sources: [SRC-022, SRC-007, SRC-027, SRC-004]
related_terms: [ground-truth, cross-validation, model-calibration, image-quality-assessment, selective-prediction, error-analysis]
seo_title: "Evaluation Metrics | Zonules.com"
meta_description: "Evaluation metrics quantify how well a vision model performs against reference labels."
---

# Evaluation Metrics

> What counts as reading the scene correctly.

## Definition

Evaluation metrics quantify how well a vision model performs against reference labels. [CLM-1164]

## Scientific Grounding

Different tasks use different metrics, such as accuracy, precision and recall, or intersection-over-union. [CLM-1165] A metric that misrepresents the goal can make a poor model look strong. [CLM-1166]

*Sources: SRC-022, SRC-007, SRC-027. See the source registry for classification.*

## Machine-Vision Role

Evaluation metrics are an interpretation-layer yardstick: they define what counts as reading the scene correctly. [CLM-1167]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** verification
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Evaluation Metrics is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Ground Truth](/ground-truth/) — related governed reference unit.
- [Cross-Validation](/cross-validation/) — related governed reference unit.
- [Model Calibration](/model-calibration/) — related governed reference unit.
- [Image Quality Assessment](/image-quality-assessment/) — related governed reference unit.
- [Selective Prediction](/selective-prediction/) — related governed reference unit.
- [Error Analysis](/error-analysis/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-022, SRC-007, SRC-027 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1164, CLM-1165, CLM-1166 sourced; CLM-1167 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
