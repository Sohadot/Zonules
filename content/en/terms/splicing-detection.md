---
term: Splicing Detection
slug: splicing-detection
route: /splicing-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: provenance
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-282
concept_id: CON-splicing-detection
safety_class: technical
canonical: https://zonules.com/splicing-detection/
last_reviewed: 2026-06-14
claims: [CLM-1124, CLM-1125, CLM-1126, CLM-1127]
sources: [SRC-023, SRC-024, SRC-004]
related_terms: [media-forensics, copy-move-detection, tamper-detection, camera-fingerprinting]
seo_title: "Splicing Detection | Zonules.com"
meta_description: "Splicing detection identifies regions of an image that were copied in from a different source image."
---

# Splicing Detection

> Finding the part that came from somewhere else.

## Definition

Splicing detection identifies regions of an image that were copied in from a different source image. [CLM-1124]

## Scientific Grounding

Spliced regions often differ in noise, lighting, or compression history from the host image. [CLM-1125] Detecting these inconsistencies is a core task of image forensics. [CLM-1126]

*Sources: SRC-023, SRC-024. See the source registry for classification.*

## Machine-Vision Role

Splicing detection is a provenance-layer check: it finds the part of an image that came from somewhere else. [CLM-1127]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** provenance
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Splicing Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Media Forensics](/media-forensics/) — related governed reference unit.
- [Copy-Move Detection](/copy-move-detection/) — related governed reference unit.
- [Tamper Detection](/tamper-detection/) — related governed reference unit.
- [Camera Fingerprinting](/camera-fingerprinting/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-023, SRC-024 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1124, CLM-1125, CLM-1126 sourced; CLM-1127 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
