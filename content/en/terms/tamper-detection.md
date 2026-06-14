---
term: Tamper Detection
slug: tamper-detection
route: /tamper-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: provenance
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-284
concept_id: CON-tamper-detection
safety_class: technical
canonical: https://zonules.com/tamper-detection/
last_reviewed: 2026-06-14
claims: [CLM-1132, CLM-1133, CLM-1134, CLM-1135]
sources: [SRC-023, SRC-024, SRC-004]
related_terms: [media-forensics, splicing-detection, content-authenticity, image-provenance, copy-move-detection]
seo_title: "Tamper Detection | Zonules.com"
meta_description: "Tamper detection determines whether an image has been altered after capture."
---

# Tamper Detection

> Judging whether what is shown has been changed.

## Definition

Tamper detection determines whether an image has been altered after capture. [CLM-1132]

## Scientific Grounding

It combines cues such as inconsistent noise, lighting, and compression artifacts. [CLM-1133] Robust tamper detection must withstand benign edits like resizing while still catching malicious ones. [CLM-1134]

*Sources: SRC-023, SRC-024. See the source registry for classification.*

## Machine-Vision Role

Tamper detection is a provenance-layer verdict: it judges whether what is shown has been changed. [CLM-1135]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** provenance
- **FIO class:** FIO-04 — Provenance Failure
- **FIS criterion:** FIS-4 — Provenance

## Relationship to the Governing Thesis

Tamper Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-04 — Provenance concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Media Forensics](/media-forensics/) — related governed reference unit.
- [Splicing Detection](/splicing-detection/) — related governed reference unit.
- [Content Authenticity](/content-authenticity/) — related governed reference unit.
- [Image Provenance](/image-provenance/) — related governed reference unit.
- [Copy-Move Detection](/copy-move-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-023, SRC-024 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1132, CLM-1133, CLM-1134 sourced; CLM-1135 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
