---
term: Optical Character Recognition
slug: optical-character-recognition
route: /optical-character-recognition/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-195
concept_id: CON-optical-character-recognition
safety_class: technical
canonical: https://zonules.com/optical-character-recognition/
last_reviewed: 2026-06-14
claims: [CLM-760, CLM-761, CLM-762, CLM-763]
sources: [SRC-007, SRC-017, SRC-004]
related_terms: [image-classification, semantic-segmentation, scene-understanding, pattern-recognition, panoptic-segmentation]
seo_title: "Optical Character Recognition | Zonules.com"
meta_description: "Optical character recognition is the machine task of converting images of text into machine-readable characters."
---

# Optical Character Recognition

> Marks resolved into the symbols they were meant to be.

## Definition

Optical character recognition is the machine task of converting images of text into machine-readable characters. [CLM-760]

## Scientific Grounding

Modern systems detect text regions and then recognize character sequences, often with neural networks trained end to end. [CLM-761] Accuracy degrades with distortion, unusual fonts, and low resolution, which blur the boundaries between characters. [CLM-762]

*Sources: SRC-007, SRC-017. See the source registry for classification.*

## Machine-Vision Role

OCR is an interpretation-layer task — it must resolve marks into the correct symbols, not merely detect that marks are present. [CLM-763]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Optical Character Recognition is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Image Classification](/image-classification/) — related governed reference unit.
- [Semantic Segmentation](/semantic-segmentation/) — related governed reference unit.
- [Scene Understanding](/scene-understanding/) — related governed reference unit.
- [Pattern Recognition](/pattern-recognition/) — related governed reference unit.
- [Panoptic Segmentation](/panoptic-segmentation/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-760, CLM-761, CLM-762 sourced; CLM-763 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
