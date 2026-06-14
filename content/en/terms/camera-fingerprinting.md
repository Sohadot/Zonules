---
term: Camera Fingerprinting
slug: camera-fingerprinting
route: /camera-fingerprinting/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: provenance
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-281
concept_id: CON-camera-fingerprinting
safety_class: technical
canonical: https://zonules.com/camera-fingerprinting/
last_reviewed: 2026-06-14
claims: [CLM-1120, CLM-1121, CLM-1122, CLM-1123]
sources: [SRC-023, SRC-024, SRC-004]
related_terms: [media-forensics, image-provenance, perceptual-hashing, splicing-detection]
seo_title: "Camera Fingerprinting | Zonules.com"
meta_description: "Camera fingerprinting identifies the source device of an image from sensor-specific noise patterns."
---

# Camera Fingerprinting

> An image tied back to the device that made it.

## Definition

Camera fingerprinting identifies the source device of an image from sensor-specific noise patterns. [CLM-1120]

## Scientific Grounding

The photo-response non-uniformity of a sensor acts as a stable, device-unique signature. [CLM-1121] A mismatch between a region's fingerprint and the rest of an image can reveal tampering. [CLM-1122]

*Sources: SRC-023, SRC-024. See the source registry for classification.*

## Machine-Vision Role

Camera fingerprinting is a provenance-layer trace: it ties an image back to the device that captured it. [CLM-1123]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** provenance
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Camera Fingerprinting is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Media Forensics](/media-forensics/) — related governed reference unit.
- [Image Provenance](/image-provenance/) — related governed reference unit.
- [Perceptual Hashing](/perceptual-hashing/) — related governed reference unit.
- [Splicing Detection](/splicing-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-023, SRC-024 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1120, CLM-1121, CLM-1122 sourced; CLM-1123 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
