---
term: Test-Time Adaptation
slug: test-time-adaptation
route: /test-time-adaptation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-02
fis_criterion: FIS-2
term_id: TRM-287
concept_id: CON-test-time-adaptation
safety_class: technical
canonical: https://zonules.com/test-time-adaptation/
last_reviewed: 2026-06-14
claims: [CLM-1144, CLM-1145, CLM-1146, CLM-1147]
sources: [SRC-017, SRC-027, SRC-004]
related_terms: [domain-shift, out-of-distribution-detection, robustness, transfer-learning, adversarial-training, corruption-robustness, spurious-correlation, covariate-shift]
seo_title: "Test-Time Adaptation | Zonules.com"
meta_description: "Test-time adaptation adjusts a model to new data during deployment, without labeled examples from the new domain."
---

# Test-Time Adaptation

> Retuning a model's range to conditions it now faces.

## Definition

Test-time adaptation adjusts a model to new data during deployment, without labeled examples from the new domain. [CLM-1144]

## Scientific Grounding

It can update statistics or parameters using the unlabeled test inputs themselves. [CLM-1145] It targets the performance drop that distribution shift causes after training. [CLM-1146]

*Sources: SRC-017, SRC-027. See the source registry for classification.*

## Machine-Vision Role

Test-time adaptation is an accommodation-layer mechanism: it retunes a model's range to the conditions it now faces. [CLM-1147]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** robustness
- **FIO class:** FIO-02 — Accommodation Failure
- **FIS criterion:** FIS-2 — Accommodation

## Relationship to the Governing Thesis

Test-Time Adaptation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-02 — Accommodation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Domain Shift](/domain-shift/) — related governed reference unit.
- [Out Of Distribution Detection](/out-of-distribution-detection/) — related governed reference unit.
- [Robustness](/robustness/) — related governed reference unit.
- [Transfer Learning](/transfer-learning/) — related governed reference unit.
- [Adversarial Training](/adversarial-training/) — related governed reference unit.
- [Corruption Robustness](/corruption-robustness/) — related governed reference unit.
- [Spurious Correlation](/spurious-correlation/) — related governed reference unit.
- [Covariate Shift](/covariate-shift/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017, SRC-027 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1144, CLM-1145, CLM-1146 sourced; CLM-1147 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
