---
term: Keypoint Detection
slug: keypoint-detection
route: /keypoint-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-194
concept_id: CON-keypoint-detection
safety_class: technical
canonical: https://zonules.com/keypoint-detection/
last_reviewed: 2026-06-14
claims: [CLM-756, CLM-757, CLM-758, CLM-759]
sources: [SRC-007, SRC-004]
related_terms: [feature-matching, feature-extraction, pose-estimation, visual-slam, optical-character-recognition]
seo_title: "Keypoint Detection | Zonules.com"
meta_description: "Keypoint detection finds distinctive, repeatable points in an image, such as corners and blobs, that can be reliably located again."
---

# Keypoint Detection

> Distinctive points a system can always find again.

## Definition

Keypoint detection finds distinctive, repeatable points in an image, such as corners and blobs, that can be reliably located again. [CLM-756]

## Scientific Grounding

Good keypoints are invariant to scale and rotation and stable under moderate viewpoint and lighting change. [CLM-757] They anchor tasks ranging from image alignment to pose estimation. [CLM-758]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Keypoints are suspension-layer anchors — fixed reference points that hold a spatial frame steady. [CLM-759]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-01 — Suspension Failure
- **FIS criterion:** FIS-1 — Suspension

## Relationship to the Governing Thesis

Keypoint Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Feature Matching](/feature-matching/) — related governed reference unit.
- [Feature Extraction](/feature-extraction/) — related governed reference unit.
- [Pose Estimation](/pose-estimation/) — related governed reference unit.
- [Visual Slam](/visual-slam/) — related governed reference unit.
- [Optical Character Recognition](/optical-character-recognition/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-756, CLM-757, CLM-758 sourced; CLM-759 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
