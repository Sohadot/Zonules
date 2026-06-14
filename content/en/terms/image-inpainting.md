---
term: Image Inpainting
slug: image-inpainting
route: /image-inpainting/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: generative-vision
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-270
concept_id: CON-image-inpainting
safety_class: technical
canonical: https://zonules.com/image-inpainting/
last_reviewed: 2026-06-14
claims: [CLM-1076, CLM-1077, CLM-1078, CLM-1079]
sources: [SRC-007, SRC-017, SRC-023, SRC-004]
related_terms: [image-synthesis, diffusion-models, generative-adversarial-networks, tamper-detection, text-to-image-generation, super-resolution, neural-style-transfer]
seo_title: "Image Inpainting | Zonules.com"
meta_description: "Image inpainting fills in missing or removed regions of an image with plausible content."
---

# Image Inpainting

> It can repair an image or quietly rewrite it.

## Definition

Image inpainting fills in missing or removed regions of an image with plausible content. [CLM-1076]

## Scientific Grounding

Learned inpainting models synthesize the missing pixels conditioned on the surrounding context. [CLM-1077] The same technique that restores damaged photos can seamlessly erase or alter real content. [CLM-1078]

*Sources: SRC-007, SRC-017, SRC-023. See the source registry for classification.*

## Machine-Vision Role

Image inpainting is a provenance-layer tool: it can repair an image or quietly rewrite what it shows. [CLM-1079]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** generative-vision
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Image Inpainting is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Image Synthesis](/image-synthesis/) — related governed reference unit.
- [Diffusion Models](/diffusion-models/) — related governed reference unit.
- [Generative Adversarial Networks](/generative-adversarial-networks/) — related governed reference unit.
- [Tamper Detection](/tamper-detection/) — related governed reference unit.
- [Text-to-Image Generation](/text-to-image-generation/) — related governed reference unit.
- [Super-Resolution](/super-resolution/) — related governed reference unit.
- [Neural Style Transfer](/neural-style-transfer/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-017, SRC-023 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1076, CLM-1077, CLM-1078 sourced; CLM-1079 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
