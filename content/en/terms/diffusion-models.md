---
term: Diffusion Models
slug: diffusion-models
route: /diffusion-models/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-207
concept_id: CON-diffusion-models
safety_class: technical
canonical: https://zonules.com/diffusion-models/
last_reviewed: 2026-06-14
claims: [CLM-808, CLM-809, CLM-810, CLM-811]
sources: [SRC-017, SRC-023, SRC-004]
related_terms: [generative-adversarial-networks, generative-models, image-synthesis, synthetic-media]
seo_title: "Diffusion Models | Zonules.com"
meta_description: "Diffusion models generate images by learning to reverse a gradual process that turns data into noise."
---

# Diffusion Models

> Images conjured from noise, with no real referent.

## Definition

Diffusion models generate images by learning to reverse a gradual process that turns data into noise. [CLM-808]

## Scientific Grounding

Starting from noise, the model denoises step by step to produce a sample resembling its training distribution. [CLM-809] They produce highly realistic synthetic imagery, which raises provenance and authentication concerns. [CLM-810]

*Sources: SRC-017, SRC-023. See the source registry for classification.*

## Machine-Vision Role

Diffusion models are a provenance-layer challenge — they manufacture convincing images with no real-world referent. [CLM-811]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Diffusion Models is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Generative Adversarial Networks](/generative-adversarial-networks/) — related governed reference unit.
- [Generative Models](/generative-models/) — related governed reference unit.
- [Image Synthesis](/image-synthesis/) — related governed reference unit.
- [Synthetic Media](/synthetic-media/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017, SRC-023 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-808, CLM-809, CLM-810 sourced; CLM-811 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
