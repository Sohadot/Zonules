---
term: Ground Truth
slug: ground-truth
route: /ground-truth/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: verification
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-293
concept_id: CON-ground-truth
safety_class: technical
canonical: https://zonules.com/ground-truth/
last_reviewed: 2026-06-14
claims: [CLM-1168, CLM-1169, CLM-1170, CLM-1171]
sources: [SRC-022, SRC-017, SRC-004]
related_terms: [evaluation-metrics, dataset-bias, cross-validation, interactive-segmentation, error-analysis]
seo_title: "Ground Truth | Zonules.com"
meta_description: "Ground truth is the reference annotation against which a model's predictions are compared."
---

# Ground Truth

> The agreed reality a system's claims are checked against.

## Definition

Ground truth is the reference annotation against which a model's predictions are compared. [CLM-1168]

## Scientific Grounding

It is usually produced by human labeling and is treated as the standard of correctness. [CLM-1169] Errors or bias in the ground truth propagate directly into measured performance and into the model. [CLM-1170]

*Sources: SRC-022, SRC-017. See the source registry for classification.*

## Machine-Vision Role

Ground truth is a provenance-layer anchor: it is the agreed reality a system's claims are checked against. [CLM-1171]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** verification
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Ground Truth is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Evaluation Metrics](/evaluation-metrics/) — related governed reference unit.
- [Dataset Bias](/dataset-bias/) — related governed reference unit.
- [Cross-Validation](/cross-validation/) — related governed reference unit.
- [Interactive Segmentation](/interactive-segmentation/) — related governed reference unit.
- [Error Analysis](/error-analysis/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-022, SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1168, CLM-1169, CLM-1170 sourced; CLM-1171 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
