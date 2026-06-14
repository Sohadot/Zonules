---
term: Backpropagation
slug: backpropagation
route: /backpropagation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: representation-learning
fio_class: FIO-02
fis_criterion: FIS-2
term_id: TRM-203
concept_id: CON-backpropagation
safety_class: technical
canonical: https://zonules.com/backpropagation/
last_reviewed: 2026-06-14
claims: [CLM-792, CLM-793, CLM-794, CLM-795]
sources: [SRC-017, SRC-027, SRC-004]
related_terms: [convolutional-neural-networks, transfer-learning, residual-networks, transformer-architecture]
seo_title: "Backpropagation | Zonules.com"
meta_description: "Backpropagation is the algorithm that computes how a network's error changes with respect to each of its weights."
---

# Backpropagation

> How a network learns by tracing its own error.

## Definition

Backpropagation is the algorithm that computes how a network's error changes with respect to each of its weights. [CLM-792]

## Scientific Grounding

It applies the chain rule backward through the layers to obtain the gradients used to update the weights. [CLM-793] It is the engine of supervised training for almost all modern deep networks. [CLM-794]

*Sources: SRC-017, SRC-027. See the source registry for classification.*

## Machine-Vision Role

Backpropagation is an accommodation-layer mechanism — it is how a model adjusts itself to fit a new operating range. [CLM-795]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** representation-learning
- **FIO class:** FIO-02 — Accommodation Failure
- **FIS criterion:** FIS-2 — Accommodation

## Relationship to the Governing Thesis

Backpropagation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-02 — Accommodation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Convolutional Neural Networks](/convolutional-neural-networks/) — related governed reference unit.
- [Transfer Learning](/transfer-learning/) — related governed reference unit.
- [Residual Networks](/residual-networks/) — related governed reference unit.
- [Transformer Architecture](/transformer-architecture/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017, SRC-027 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-792, CLM-793, CLM-794 sourced; CLM-795 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
