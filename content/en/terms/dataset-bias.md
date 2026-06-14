---
term: Dataset Bias
slug: dataset-bias
route: /dataset-bias/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-202
concept_id: CON-dataset-bias
safety_class: technical
canonical: https://zonules.com/dataset-bias/
last_reviewed: 2026-06-14
claims: [CLM-788, CLM-789, CLM-790, CLM-791]
sources: [SRC-022, SRC-017, SRC-004]
related_terms: [image-classification, domain-shift, transfer-learning, face-recognition]
seo_title: "Dataset Bias | Zonules.com"
meta_description: "Dataset bias is the systematic non-representativeness of a training set relative to the conditions where the model will be used."
---

# Dataset Bias

> A model learns the data it is given, flaws and all.

## Definition

Dataset bias is the systematic non-representativeness of a training set relative to the conditions where the model will be used. [CLM-788]

## Scientific Grounding

Models can exploit incidental correlations in the data, such as backgrounds or capture conditions, instead of the intended object. [CLM-789] Bias in the data propagates into the model and surfaces as poor or unequal performance on under-represented cases. [CLM-790]

*Sources: SRC-022, SRC-017. See the source registry for classification.*

## Machine-Vision Role

Dataset bias is an interpretation-layer fault — the model learns to read the wrong evidence and reaches confident wrong conclusions. [CLM-791]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** robustness
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Dataset Bias is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Image Classification](/image-classification/) — related governed reference unit.
- [Domain Shift](/domain-shift/) — related governed reference unit.
- [Transfer Learning](/transfer-learning/) — related governed reference unit.
- [Face Recognition](/face-recognition/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-022, SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-788, CLM-789, CLM-790 sourced; CLM-791 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
