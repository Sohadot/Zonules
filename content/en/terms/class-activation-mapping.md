---
term: Class Activation Mapping
slug: class-activation-mapping
route: /class-activation-mapping/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-198
concept_id: CON-class-activation-mapping
safety_class: technical
canonical: https://zonules.com/class-activation-mapping/
last_reviewed: 2026-06-14
claims: [CLM-772, CLM-773, CLM-774, CLM-775]
sources: [SRC-017, SRC-004]
related_terms: [saliency-maps, neural-network-interpretability, convolutional-neural-networks, image-classification]
seo_title: "Class Activation Mapping | Zonules.com"
meta_description: "Class activation mapping highlights the image regions a convolutional network used to support a particular class prediction."
---

# Class Activation Mapping

> Tracing a label back to the region that earned it.

## Definition

Class activation mapping highlights the image regions a convolutional network used to support a particular class prediction. [CLM-772]

## Scientific Grounding

It projects the weights of the output class back onto the spatial feature maps to produce a localization heatmap. [CLM-773] It offers coarse evidence of where a model looked without requiring location labels during training. [CLM-774]

*Sources: SRC-017. See the source registry for classification.*

## Machine-Vision Role

Class activation mapping is an interpretation-layer audit — it asks whether the right region drove the right answer. [CLM-775]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Class Activation Mapping is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Saliency Maps](/saliency-maps/) — related governed reference unit.
- [Neural Network Interpretability](/neural-network-interpretability/) — related governed reference unit.
- [Convolutional Neural Networks](/convolutional-neural-networks/) — related governed reference unit.
- [Image Classification](/image-classification/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-772, CLM-773, CLM-774 sourced; CLM-775 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
