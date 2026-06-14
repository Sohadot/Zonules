---
term: Cross-Validation
slug: cross-validation
route: /cross-validation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: verification
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-290
concept_id: CON-cross-validation
safety_class: technical
canonical: https://zonules.com/cross-validation/
last_reviewed: 2026-06-14
claims: [CLM-1156, CLM-1157, CLM-1158, CLM-1159]
sources: [SRC-027, SRC-017, SRC-004]
related_terms: [model-calibration, evaluation-metrics, ground-truth, dataset-bias, selective-prediction]
seo_title: "Cross-Validation | Zonules.com"
meta_description: "Cross-validation estimates how well a model generalizes by repeatedly training and testing on different splits of the data."
---

# Cross-Validation

> Do a model's readings hold on data it did not see?

## Definition

Cross-validation estimates how well a model generalizes by repeatedly training and testing on different splits of the data. [CLM-1156]

## Scientific Grounding

It uses the available data more efficiently than a single train-test split. [CLM-1157] It helps detect overfitting and guides the choice of model and hyperparameters. [CLM-1158]

*Sources: SRC-027, SRC-017. See the source registry for classification.*

## Machine-Vision Role

Cross-validation is an interpretation-layer check: it asks whether a model's readings hold on data it did not see. [CLM-1159]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** verification
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Cross-Validation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Model Calibration](/model-calibration/) — related governed reference unit.
- [Evaluation Metrics](/evaluation-metrics/) — related governed reference unit.
- [Ground Truth](/ground-truth/) — related governed reference unit.
- [Dataset Bias](/dataset-bias/) — related governed reference unit.
- [Selective Prediction](/selective-prediction/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-027, SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1156, CLM-1157, CLM-1158 sourced; CLM-1159 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
