---
term: Selective Prediction
slug: selective-prediction
route: /selective-prediction/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: verification
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-291
concept_id: CON-selective-prediction
safety_class: technical
canonical: https://zonules.com/selective-prediction/
last_reviewed: 2026-06-14
claims: [CLM-1160, CLM-1161, CLM-1162, CLM-1163]
sources: [SRC-027, SRC-017, SRC-004]
related_terms: [uncertainty-estimation, model-calibration, out-of-distribution-detection, evaluation-metrics]
seo_title: "Selective Prediction | Zonules.com"
meta_description: "Selective prediction lets a model abstain from answering when its confidence is too low."
---

# Selective Prediction

> A system that can say it is not sure.

## Definition

Selective prediction lets a model abstain from answering when its confidence is too low. [CLM-1160]

## Scientific Grounding

By declining uncertain cases, it can raise accuracy on the cases it does answer. [CLM-1161] The trade-off between coverage and accuracy is set by a confidence threshold. [CLM-1162]

*Sources: SRC-027, SRC-017. See the source registry for classification.*

## Machine-Vision Role

Selective prediction is a provenance-layer discipline: a system that can say it is not sure rather than assert blindly. [CLM-1163]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** verification
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Selective Prediction is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Uncertainty Estimation](/uncertainty-estimation/) — related governed reference unit.
- [Model Calibration](/model-calibration/) — related governed reference unit.
- [Out Of Distribution Detection](/out-of-distribution-detection/) — related governed reference unit.
- [Evaluation Metrics](/evaluation-metrics/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-027, SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1160, CLM-1161, CLM-1162 sourced; CLM-1163 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
