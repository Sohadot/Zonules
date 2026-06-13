---
term: Generative Models
slug: generative-models
route: /generative-models/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-118
concept_id: CON-generative-models
safety_class: technical
canonical: https://zonules.com/generative-models/
last_reviewed: 2026-06-13
claims: [CLM-420, CLM-421, CLM-422, CLM-423]
sources: ["SRC-007", "SRC-008"]
related_terms: ["deepfake-detection", "image-provenance", "synthetic-media", "few-shot-learning", "image-synthesis"]
seo_title: "Generative Models | Zonules.com"
meta_description: "A generative model is a statistical model that learns the joint distribution of inputs and can produce new samples indistinguishable from training data."
---
# Generative Models

> Generative models are a provenance failure at scale

## Definition

A generative model is a statistical model that learns the joint distribution of inputs and can produce new samples indistinguishable from training data. [CLM-420]

## Scientific Grounding

Generative adversarial networks, variational autoencoders, and diffusion models are the primary architectures; diffusion models dominate recent image synthesis benchmarks. [CLM-421] The near-perfect visual fidelity of outputs from modern generative models severs the assumed link between image appearance and image origin. [CLM-422]

*Sources: SRC-007, SRC-008. See the source registry for classification.*

## Technical Role

Generative models are a provenance failure at scale (FIO-04): they produce appearance without origin, making the appearance-provenance link impossible to assume. [CLM-423]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-04 — Provenance
- **FIS criterion:** FIS-4

## Relationship to the Governing Thesis

Generative Models is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Deepfake Detection](/deepfake-detection/) — governed reference unit linked within this cluster.
- [Image Provenance](/image-provenance/) — governed reference unit linked within this cluster.
- [Synthetic Media](/synthetic-media/) — governed reference unit linked within this cluster.
- [Few Shot Learning](/few-shot-learning/) — governed reference unit linked within this cluster.
- [Image Synthesis](/image-synthesis/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007, SRC-008 (registered).
- **Claims:** CLM-420, CLM-421, CLM-422 sourced; CLM-423 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
