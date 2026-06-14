---
term: Copy-Move Detection
slug: copy-move-detection
route: /copy-move-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: provenance
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-283
concept_id: CON-copy-move-detection
safety_class: technical
canonical: https://zonules.com/copy-move-detection/
last_reviewed: 2026-06-14
claims: [CLM-1128, CLM-1129, CLM-1130, CLM-1131]
sources: [SRC-023, SRC-024, SRC-004]
related_terms: [splicing-detection, media-forensics, tamper-detection, perceptual-hashing]
seo_title: "Copy-Move Detection | Zonules.com"
meta_description: "Copy-move detection finds regions of an image that were duplicated from elsewhere within the same image."
---

# Copy-Move Detection

> A forgery built from the image's own pixels.

## Definition

Copy-move detection finds regions of an image that were duplicated from elsewhere within the same image. [CLM-1128]

## Scientific Grounding

Duplication is used to conceal content by covering it with a copied patch. [CLM-1129] Detectors search for suspiciously similar regions while allowing for small post-processing changes. [CLM-1130]

*Sources: SRC-023, SRC-024. See the source registry for classification.*

## Machine-Vision Role

Copy-move detection is a provenance-layer check: it exposes a forgery built from the image's own pixels. [CLM-1131]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** provenance
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Copy-Move Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Splicing Detection](/splicing-detection/) — related governed reference unit.
- [Media Forensics](/media-forensics/) — related governed reference unit.
- [Tamper Detection](/tamper-detection/) — related governed reference unit.
- [Perceptual Hashing](/perceptual-hashing/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-023, SRC-024 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1128, CLM-1129, CLM-1130 sourced; CLM-1131 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
