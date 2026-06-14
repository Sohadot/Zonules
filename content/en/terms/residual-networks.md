---
term: Residual Networks
slug: residual-networks
route: /residual-networks/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: representation-learning
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-204
concept_id: CON-residual-networks
safety_class: technical
canonical: https://zonules.com/residual-networks/
last_reviewed: 2026-06-14
claims: [CLM-796, CLM-797, CLM-798, CLM-799]
sources: [SRC-017, SRC-004]
related_terms: [convolutional-neural-networks, backpropagation, batch-normalization, image-classification]
seo_title: "Residual Networks | Zonules.com"
meta_description: "Residual networks add shortcut connections that let a layer learn a change to its input rather than a full transformation."
---

# Residual Networks

> Shortcuts that hold the signal across great depth.

## Definition

Residual networks add shortcut connections that let a layer learn a change to its input rather than a full transformation. [CLM-796]

## Scientific Grounding

These connections ease the training of very deep networks by letting gradients flow more directly. [CLM-797] They made networks of hundreds of layers practical and improved image classification substantially. [CLM-798]

*Sources: SRC-017. See the source registry for classification.*

## Machine-Vision Role

Residual connections are a suspension-layer device — they hold the signal stable as it passes through great depth. [CLM-799]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** representation-learning
- **FIO class:** FIO-01 — Suspension Failure
- **FIS criterion:** FIS-1 — Suspension

## Relationship to the Governing Thesis

Residual Networks is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Convolutional Neural Networks](/convolutional-neural-networks/) — related governed reference unit.
- [Backpropagation](/backpropagation/) — related governed reference unit.
- [Batch Normalization](/batch-normalization/) — related governed reference unit.
- [Image Classification](/image-classification/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-796, CLM-797, CLM-798 sourced; CLM-799 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
