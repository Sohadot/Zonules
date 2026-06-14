---
term: Corruption Robustness
slug: corruption-robustness
route: /corruption-robustness/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-286
concept_id: CON-corruption-robustness
safety_class: technical
canonical: https://zonules.com/corruption-robustness/
last_reviewed: 2026-06-14
claims: [CLM-1140, CLM-1141, CLM-1142, CLM-1143]
sources: [SRC-017, SRC-022, SRC-004]
related_terms: [robustness, data-augmentation, image-quality-assessment, out-of-distribution-detection, adversarial-training, test-time-adaptation]
seo_title: "Corruption Robustness | Zonules.com"
meta_description: "Corruption robustness is a model's resilience to common, non-adversarial image degradations such as blur, noise, and weather."
---

# Corruption Robustness

> Does meaning survive ordinary degradation?

## Definition

Corruption robustness is a model's resilience to common, non-adversarial image degradations such as blur, noise, and weather. [CLM-1140]

## Scientific Grounding

Standard benchmarks apply graded corruptions to test sets to measure this resilience. [CLM-1141] Models strong on clean data can still fail badly under mild corruption. [CLM-1142]

*Sources: SRC-017, SRC-022. See the source registry for classification.*

## Machine-Vision Role

Corruption robustness is a separation-layer measure: it asks whether meaning survives ordinary degradation of the input. [CLM-1143]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** robustness
- **FIO class:** FIO-03 — Signal–Noise Failure
- **FIS criterion:** FIS-3 — Separation

## Relationship to the Governing Thesis

Corruption Robustness is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-03 — Separation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Robustness](/robustness/) — related governed reference unit.
- [Data Augmentation](/data-augmentation/) — related governed reference unit.
- [Image Quality Assessment](/image-quality-assessment/) — related governed reference unit.
- [Out Of Distribution Detection](/out-of-distribution-detection/) — related governed reference unit.
- [Adversarial Training](/adversarial-training/) — related governed reference unit.
- [Test-Time Adaptation](/test-time-adaptation/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017, SRC-022 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1140, CLM-1141, CLM-1142 sourced; CLM-1143 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
