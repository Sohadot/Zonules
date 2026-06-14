---
term: Knowledge Distillation
slug: knowledge-distillation
route: /knowledge-distillation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: representation-learning
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-206
concept_id: CON-knowledge-distillation
safety_class: technical
canonical: https://zonules.com/knowledge-distillation/
last_reviewed: 2026-06-14
claims: [CLM-804, CLM-805, CLM-806, CLM-807]
sources: [SRC-017, SRC-004]
related_terms: [transfer-learning, model-calibration, convolutional-neural-networks, few-shot-learning]
seo_title: "Knowledge Distillation | Zonules.com"
meta_description: "Knowledge distillation trains a smaller student model to reproduce the outputs of a larger teacher model."
---

# Knowledge Distillation

> A small model taught to read like a large one.

## Definition

Knowledge distillation trains a smaller student model to reproduce the outputs of a larger teacher model. [CLM-804]

## Scientific Grounding

The student learns from the teacher's full output distribution, which carries more information than hard labels alone. [CLM-805] It transfers much of the teacher's performance into a model that is cheaper to deploy. [CLM-806]

*Sources: SRC-017. See the source registry for classification.*

## Machine-Vision Role

Knowledge distillation is an interpretation-layer transfer — it copies how one model reads inputs into another. [CLM-807]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** representation-learning
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Knowledge Distillation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Transfer Learning](/transfer-learning/) — related governed reference unit.
- [Model Calibration](/model-calibration/) — related governed reference unit.
- [Convolutional Neural Networks](/convolutional-neural-networks/) — related governed reference unit.
- [Few Shot Learning](/few-shot-learning/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-804, CLM-805, CLM-806 sourced; CLM-807 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
