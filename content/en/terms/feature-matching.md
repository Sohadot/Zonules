---
term: Feature Matching
slug: feature-matching
route: /feature-matching/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-193
concept_id: CON-feature-matching
safety_class: technical
canonical: https://zonules.com/feature-matching/
last_reviewed: 2026-06-14
claims: [CLM-752, CLM-753, CLM-754, CLM-755]
sources: [SRC-007, SRC-016, SRC-004]
related_terms: [keypoint-detection, feature-extraction, image-registration, stereo-matching, edge-detection]
seo_title: "Feature Matching | Zonules.com"
meta_description: "Feature matching is the process of finding corresponding points or regions across different images of the same scene."
---

# Feature Matching

> Holding one point fixed across many views.

## Definition

Feature matching is the process of finding corresponding points or regions across different images of the same scene. [CLM-752]

## Scientific Grounding

Distinctive local features are described by vectors that stay stable under changes in scale, rotation, and illumination, then matched by similarity. [CLM-753] Reliable correspondences are the foundation of image registration, stereo, and structure-from-motion. [CLM-754]

*Sources: SRC-007, SRC-016. See the source registry for classification.*

## Machine-Vision Role

Feature matching is a suspension-layer operation — it holds a stable reference frame across views so the same point can be tracked. [CLM-755]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-01 — Suspension Failure
- **FIS criterion:** FIS-1 — Suspension

## Relationship to the Governing Thesis

Feature Matching is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Keypoint Detection](/keypoint-detection/) — related governed reference unit.
- [Feature Extraction](/feature-extraction/) — related governed reference unit.
- [Image Registration](/image-registration/) — related governed reference unit.
- [Stereo Matching](/stereo-matching/) — related governed reference unit.
- [Edge Detection](/edge-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-016 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-752, CLM-753, CLM-754 sourced; CLM-755 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
