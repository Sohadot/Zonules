---
term: Spurious Correlation
slug: spurious-correlation
route: /spurious-correlation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-288
concept_id: CON-spurious-correlation
safety_class: technical
canonical: https://zonules.com/spurious-correlation/
last_reviewed: 2026-06-14
claims: [CLM-1148, CLM-1149, CLM-1150, CLM-1151]
sources: [SRC-017, SRC-027, SRC-004]
related_terms: [dataset-bias, domain-shift, robustness, out-of-distribution-detection, covariate-shift]
seo_title: "Spurious Correlation | Zonules.com"
meta_description: "A spurious correlation is a statistical association in training data that does not reflect the true cause of the label."
---

# Spurious Correlation

> The model reads the wrong evidence and is sure of it.

## Definition

A spurious correlation is a statistical association in training data that does not reflect the true cause of the label. [CLM-1148]

## Scientific Grounding

A model may learn to rely on a background or texture that happens to correlate with the class. [CLM-1149] Such shortcuts break when the spurious feature is absent or changed at deployment. [CLM-1150]

*Sources: SRC-017, SRC-027. See the source registry for classification.*

## Machine-Vision Role

Spurious correlation is an interpretation-layer trap: the model reads the wrong evidence and is confidently wrong off-distribution. [CLM-1151]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** robustness
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Spurious Correlation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Dataset Bias](/dataset-bias/) — related governed reference unit.
- [Domain Shift](/domain-shift/) — related governed reference unit.
- [Robustness](/robustness/) — related governed reference unit.
- [Out Of Distribution Detection](/out-of-distribution-detection/) — related governed reference unit.
- [Covariate Shift](/covariate-shift/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017, SRC-027 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1148, CLM-1149, CLM-1150 sourced; CLM-1151 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
