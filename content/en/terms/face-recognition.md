---
term: Face Recognition
slug: face-recognition
route: /face-recognition/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-211
concept_id: CON-face-recognition
safety_class: technical
canonical: https://zonules.com/face-recognition/
last_reviewed: 2026-06-14
claims: [CLM-824, CLM-825, CLM-826, CLM-827]
sources: [SRC-007, SRC-022, SRC-004]
related_terms: [face-perception, image-classification, dataset-bias, deepfake-detection]
seo_title: "Face Recognition | Zonules.com"
meta_description: "Face recognition is the machine task of identifying or verifying a person from an image of their face."
---

# Face Recognition

> Identity — the highest-stakes reading of a face.

## Definition

Face recognition is the machine task of identifying or verifying a person from an image of their face. [CLM-824]

## Scientific Grounding

Modern systems map a face to a compact embedding and compare embeddings by distance. [CLM-825] Performance can vary across demographic groups and capture conditions, reflecting bias in the training data. [CLM-826]

*Sources: SRC-007, SRC-022. See the source registry for classification.*

## Machine-Vision Role

Face recognition is an interpretation-layer judgment — it assigns identity, the highest-stakes reading of a face. [CLM-827]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Face Recognition is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Face Perception](/face-perception/) — related governed reference unit.
- [Image Classification](/image-classification/) — related governed reference unit.
- [Dataset Bias](/dataset-bias/) — related governed reference unit.
- [Deepfake Detection](/deepfake-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-022 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-824, CLM-825, CLM-826 sourced; CLM-827 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
