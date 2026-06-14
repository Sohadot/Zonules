---
term: Media Forensics
slug: media-forensics
route: /media-forensics/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: provenance
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-279
concept_id: CON-media-forensics
safety_class: technical
canonical: https://zonules.com/media-forensics/
last_reviewed: 2026-06-14
claims: [CLM-1112, CLM-1113, CLM-1114, CLM-1115]
sources: [SRC-023, SRC-024, SRC-004]
related_terms: [deepfake-detection, image-provenance, tamper-detection, splicing-detection, content-authenticity]
seo_title: "Media Forensics | Zonules.com"
meta_description: "Media forensics is the analysis of images and video to determine their authenticity and detect manipulation."
---

# Media Forensics

> Asking whether an image is what it claims to be.

## Definition

Media forensics is the analysis of images and video to determine their authenticity and detect manipulation. [CLM-1112]

## Scientific Grounding

It looks for traces left by editing, recompression, or synthesis that are invisible to the eye. [CLM-1113] Benchmark datasets of manipulated media support the development of forensic detectors. [CLM-1114]

*Sources: SRC-023, SRC-024. See the source registry for classification.*

## Machine-Vision Role

Media forensics is a provenance-layer discipline: it asks whether an image is what it claims to be. [CLM-1115]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** provenance
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Media Forensics is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Deepfake Detection](/deepfake-detection/) — related governed reference unit.
- [Image Provenance](/image-provenance/) — related governed reference unit.
- [Tamper Detection](/tamper-detection/) — related governed reference unit.
- [Splicing Detection](/splicing-detection/) — related governed reference unit.
- [Content Authenticity](/content-authenticity/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-023, SRC-024 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1112, CLM-1113, CLM-1114 sourced; CLM-1115 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
