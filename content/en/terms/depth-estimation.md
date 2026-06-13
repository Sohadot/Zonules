---
term: Depth Estimation
slug: depth-estimation
route: /depth-estimation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-093
concept_id: CON-depth-estimation
safety_class: technical
canonical: https://zonules.com/depth-estimation/
last_reviewed: 2026-06-13
claims: [CLM-320, CLM-321, CLM-322, CLM-323]
sources: [SRC-007]
related_terms: [pose-estimation, visual-slam, optical-flow, depth-perception, scene-understanding]
seo_title: "Depth Estimation | Zonules.com"
meta_description: "Depth estimation is the machine vision task of inferring distance to scene points from images, using stereo, motion, or learned monocular cues."
---
# Depth Estimation

> The machine instance of inferring 3D from 2D.

## Definition

Depth estimation is the machine vision task of inferring distance to scene points from images. [CLM-320]

## Scientific Grounding

It can use stereo disparity, motion parallax, or monocular cues learned from data. [CLM-321] Monocular depth estimation is inherently ambiguous and relies on learned priors. [CLM-322]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Depth estimation is the machine instance of depth perception (FIO-05): three-dimensional structure inferred from two-dimensional input. [CLM-323]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Depth Estimation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Pose Estimation](/pose-estimation/) — governed reference unit linked within this cluster.
- [Visual Slam](/visual-slam/) — governed reference unit linked within this cluster.
- [Optical Flow](/optical-flow/) — governed reference unit linked within this cluster.
- [Depth Perception](/depth-perception/) — governed reference unit linked within this cluster.
- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-320, CLM-321, CLM-322 sourced; CLM-323 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational and technical reference content**. It describes methods and a conceptual framework and makes no performance claims about any specific implementation, product, or system.
