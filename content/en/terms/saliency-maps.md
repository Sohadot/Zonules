---
term: Saliency Maps
slug: saliency-maps
route: /saliency-maps/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: verification
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-197
concept_id: CON-saliency-maps
safety_class: technical
canonical: https://zonules.com/saliency-maps/
last_reviewed: 2026-06-14
claims: [CLM-768, CLM-769, CLM-770, CLM-771]
sources: [SRC-017, SRC-004]
related_terms: [neural-network-interpretability, class-activation-mapping, visual-saliency, model-calibration]
seo_title: "Saliency Maps | Zonules.com"
meta_description: "Saliency maps are visualizations that estimate how much each input pixel influenced a model's output."
---

# Saliency Maps

> A picture of where a model claims it looked.

## Definition

Saliency maps are visualizations that estimate how much each input pixel influenced a model's output. [CLM-768]

## Scientific Grounding

They are computed from gradients or related signals to highlight the regions a network appears to rely on. [CLM-769] Saliency maps can mislead, sometimes looking plausible even when they do not faithfully reflect the model's reasoning. [CLM-770]

*Sources: SRC-017. See the source registry for classification.*

## Machine-Vision Role

Saliency maps are an interpretation-layer probe — an attempt to check whether a model focused on the right evidence. [CLM-771]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** verification
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Saliency Maps is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Neural Network Interpretability](/neural-network-interpretability/) — related governed reference unit.
- [Class Activation Mapping](/class-activation-mapping/) — related governed reference unit.
- [Visual Saliency](/visual-saliency/) — related governed reference unit.
- [Model Calibration](/model-calibration/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-768, CLM-769, CLM-770 sourced; CLM-771 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
