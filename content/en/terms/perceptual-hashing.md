---
term: Perceptual Hashing
slug: perceptual-hashing
route: /perceptual-hashing/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: provenance
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-210
concept_id: CON-perceptual-hashing
safety_class: technical
canonical: https://zonules.com/perceptual-hashing/
last_reviewed: 2026-06-14
claims: [CLM-820, CLM-821, CLM-822, CLM-823]
sources: [SRC-008, SRC-023, SRC-004]
related_terms: [image-provenance, digital-watermarking, deepfake-detection, image-registration]
seo_title: "Perceptual Hashing | Zonules.com"
meta_description: "Perceptual hashing computes a compact fingerprint of an image that stays similar when the image is altered slightly."
---

# Perceptual Hashing

> A fingerprint that survives the edits an image suffers.

## Definition

Perceptual hashing computes a compact fingerprint of an image that stays similar when the image is altered slightly. [CLM-820]

## Scientific Grounding

Unlike cryptographic hashes, perceptual hashes change gradually with the image, so near-duplicates produce near-identical fingerprints. [CLM-821] They are used to match and track images across the web for provenance and content-matching. [CLM-822]

*Sources: SRC-008, SRC-023. See the source registry for classification.*

## Machine-Vision Role

Perceptual hashing is a provenance-layer index — it lets a system ask whether it has seen an image before. [CLM-823]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** provenance
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Perceptual Hashing is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Image Provenance](/image-provenance/) — related governed reference unit.
- [Digital Watermarking](/digital-watermarking/) — related governed reference unit.
- [Deepfake Detection](/deepfake-detection/) — related governed reference unit.
- [Image Registration](/image-registration/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-008, SRC-023 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-820, CLM-821, CLM-822 sourced; CLM-823 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
