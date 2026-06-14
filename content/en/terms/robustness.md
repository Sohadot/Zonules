---
term: Model Robustness
slug: robustness
route: /robustness/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-201
concept_id: CON-robustness
safety_class: technical
canonical: https://zonules.com/robustness/
last_reviewed: 2026-06-14
claims: [CLM-784, CLM-785, CLM-786, CLM-787]
sources: [SRC-017, SRC-004]
related_terms: [adversarial-examples, domain-shift, out-of-distribution-detection, data-augmentation]
seo_title: "Model Robustness | Zonules.com"
meta_description: "Robustness is a model's ability to maintain performance under input perturbations, distribution change, and noise."
---

# Model Robustness

> Accuracy that survives noise, shift, and attack.

## Definition

Robustness is a model's ability to maintain performance under input perturbations, distribution change, and noise. [CLM-784]

## Scientific Grounding

High accuracy on clean test data does not guarantee robustness, since small structured perturbations can cause large errors. [CLM-785] Robustness must be measured and engineered explicitly, for example through adversarial training or augmentation. [CLM-786]

*Sources: SRC-017. See the source registry for classification.*

## Machine-Vision Role

Robustness is a separation-layer property — it measures whether signal survives when noise is added to the input. [CLM-787]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-03 — Signal–Noise Failure
- **FIS criterion:** FIS-3 — Separation

## Relationship to the Governing Thesis

Model Robustness is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-03 — Separation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Adversarial Examples](/adversarial-examples/) — related governed reference unit.
- [Domain Shift](/domain-shift/) — related governed reference unit.
- [Out Of Distribution Detection](/out-of-distribution-detection/) — related governed reference unit.
- [Data Augmentation](/data-augmentation/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-784, CLM-785, CLM-786 sourced; CLM-787 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
