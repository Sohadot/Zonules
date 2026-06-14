---
term: Super-Resolution
slug: super-resolution
route: /super-resolution/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: generative-vision
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-271
concept_id: CON-super-resolution
safety_class: technical
canonical: https://zonules.com/super-resolution/
last_reviewed: 2026-06-14
claims: [CLM-1080, CLM-1081, CLM-1082, CLM-1083]
sources: [SRC-007, SRC-017, SRC-023, SRC-004]
related_terms: [image-synthesis, image-quality-assessment, diffusion-models, generative-adversarial-networks, image-inpainting, neural-style-transfer]
seo_title: "Super-Resolution | Zonules.com"
meta_description: "Super-resolution reconstructs a high-resolution image from a lower-resolution input."
---

# Super-Resolution

> The detail it adds is invention, not fact.

## Definition

Super-resolution reconstructs a high-resolution image from a lower-resolution input. [CLM-1080]

## Scientific Grounding

Learned methods hallucinate plausible detail that was not present in the low-resolution source. [CLM-1081] Because invented detail can look authentic, super-resolution outputs must not be treated as recovered ground truth. [CLM-1082]

*Sources: SRC-007, SRC-017, SRC-023. See the source registry for classification.*

## Machine-Vision Role

Super-resolution is a provenance-layer caution: the detail it adds is plausible invention, not retrieved fact. [CLM-1083]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** generative-vision
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Super-Resolution is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Image Synthesis](/image-synthesis/) — related governed reference unit.
- [Image Quality Assessment](/image-quality-assessment/) — related governed reference unit.
- [Diffusion Models](/diffusion-models/) — related governed reference unit.
- [Generative Adversarial Networks](/generative-adversarial-networks/) — related governed reference unit.
- [Image Inpainting](/image-inpainting/) — related governed reference unit.
- [Neural Style Transfer](/neural-style-transfer/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-017, SRC-023 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1080, CLM-1081, CLM-1082 sourced; CLM-1083 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
