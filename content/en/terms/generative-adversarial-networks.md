---
term: Generative Adversarial Networks
slug: generative-adversarial-networks
route: /generative-adversarial-networks/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: generative-vision
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-208
concept_id: CON-generative-adversarial-networks
safety_class: technical
canonical: https://zonules.com/generative-adversarial-networks/
last_reviewed: 2026-06-14
claims: [CLM-812, CLM-813, CLM-814, CLM-815]
sources: [SRC-017, SRC-024, SRC-004]
related_terms: [diffusion-models, generative-models, synthetic-media, deepfake-detection]
seo_title: "Generative Adversarial Networks | Zonules.com"
meta_description: "Generative adversarial networks pit a generator that creates images against a discriminator that tries to tell real from fake."
---

# Generative Adversarial Networks

> Two networks in a duel until the fake looks real.

## Definition

Generative adversarial networks pit a generator that creates images against a discriminator that tries to tell real from fake. [CLM-812]

## Scientific Grounding

The two networks train in competition until the generator's outputs become difficult to distinguish from real data. [CLM-813] They were central to early photorealistic face synthesis and the rise of deepfakes. [CLM-814]

*Sources: SRC-017, SRC-024. See the source registry for classification.*

## Machine-Vision Role

Generative adversarial networks are a provenance-layer threat — they were built to make the synthetic indistinguishable from the real. [CLM-815]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** generative-vision
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Generative Adversarial Networks is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Diffusion Models](/diffusion-models/) — related governed reference unit.
- [Generative Models](/generative-models/) — related governed reference unit.
- [Synthetic Media](/synthetic-media/) — related governed reference unit.
- [Deepfake Detection](/deepfake-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017, SRC-024 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-812, CLM-813, CLM-814 sourced; CLM-815 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
