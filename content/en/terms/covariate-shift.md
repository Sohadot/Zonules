---
term: Covariate Shift
slug: covariate-shift
route: /covariate-shift/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-02
fis_criterion: FIS-2
term_id: TRM-289
concept_id: CON-covariate-shift
safety_class: technical
canonical: https://zonules.com/covariate-shift/
last_reviewed: 2026-06-14
claims: [CLM-1152, CLM-1153, CLM-1154, CLM-1155]
sources: [SRC-027, SRC-017, SRC-004]
related_terms: [domain-shift, out-of-distribution-detection, test-time-adaptation, dataset-bias, spurious-correlation]
seo_title: "Covariate Shift | Zonules.com"
meta_description: "Covariate shift occurs when the distribution of inputs changes between training and deployment while the labeling rule stays the same."
---

# Covariate Shift

> Conditions move and the model's range no longer fits.

## Definition

Covariate shift occurs when the distribution of inputs changes between training and deployment while the labeling rule stays the same. [CLM-1152]

## Scientific Grounding

It is a common cause of silent performance degradation in deployed vision systems. [CLM-1153] Detecting and correcting covariate shift is central to reliable deployment. [CLM-1154]

*Sources: SRC-027, SRC-017. See the source registry for classification.*

## Machine-Vision Role

Covariate shift is an accommodation-layer failure: the operating conditions move and the model's range no longer fits. [CLM-1155]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** robustness
- **FIO class:** FIO-02 — Accommodation Failure
- **FIS criterion:** FIS-2 — Accommodation

## Relationship to the Governing Thesis

Covariate Shift is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-02 — Accommodation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Domain Shift](/domain-shift/) — related governed reference unit.
- [Out Of Distribution Detection](/out-of-distribution-detection/) — related governed reference unit.
- [Test-Time Adaptation](/test-time-adaptation/) — related governed reference unit.
- [Dataset Bias](/dataset-bias/) — related governed reference unit.
- [Spurious Correlation](/spurious-correlation/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-027, SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1152, CLM-1153, CLM-1154 sourced; CLM-1155 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
