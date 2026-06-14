---
term: Stereo Matching
slug: stereo-matching
route: /stereo-matching/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-212
concept_id: CON-stereo-matching
safety_class: technical
canonical: https://zonules.com/stereo-matching/
last_reviewed: 2026-06-14
claims: [CLM-828, CLM-829, CLM-830, CLM-831]
sources: [SRC-007, SRC-016, SRC-004]
related_terms: [depth-estimation, feature-matching, binocular-disparity, visual-slam]
seo_title: "Stereo Matching | Zonules.com"
meta_description: "Stereo matching computes depth by finding corresponding points in two images taken from slightly different viewpoints."
---

# Stereo Matching

> Two views held together to recover where things are.

## Definition

Stereo matching computes depth by finding corresponding points in two images taken from slightly different viewpoints. [CLM-828]

## Scientific Grounding

The horizontal shift between matched points, the disparity, is inversely related to distance. [CLM-829] Matching is hardest in textureless or repetitive regions where correspondences are ambiguous. [CLM-830]

*Sources: SRC-007, SRC-016. See the source registry for classification.*

## Machine-Vision Role

Stereo matching is a suspension-layer computation — it holds two views in a common frame to recover where things are. [CLM-831]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-01 — Suspension Failure
- **FIS criterion:** FIS-1 — Suspension

## Relationship to the Governing Thesis

Stereo Matching is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Depth Estimation](/depth-estimation/) — related governed reference unit.
- [Feature Matching](/feature-matching/) — related governed reference unit.
- [Binocular Disparity](/binocular-disparity/) — related governed reference unit.
- [Visual Slam](/visual-slam/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-016 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-828, CLM-829, CLM-830 sourced; CLM-831 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
