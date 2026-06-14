---
term: Pose Estimation
slug: pose-estimation
route: /pose-estimation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-092
concept_id: CON-pose-estimation
safety_class: technical
canonical: https://zonules.com/pose-estimation/
last_reviewed: 2026-06-13
claims: [CLM-316, CLM-317, CLM-318, CLM-319]
sources: [SRC-007]
related_terms: [object-detection, depth-estimation, visual-tracking, scene-understanding]
seo_title: "Pose Estimation | Zonules.com"
meta_description: "Pose estimation is the machine vision task of inferring the spatial configuration of objects or human bodies, such as joint keypoints, from images."
---
# Pose Estimation

> Spatial structure inferred from flat appearance.

## Definition

Pose estimation is the machine vision task of inferring the spatial configuration of objects or human bodies from images. [CLM-316]

## Scientific Grounding

Human pose estimation localizes body keypoints such as joints to recover posture. [CLM-317] Accuracy degrades under occlusion and unusual viewpoints. [CLM-318]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Pose estimation is an interpretation (FIO-05): spatial structure is inferred from appearance rather than measured directly. [CLM-319]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Pose Estimation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Object Detection](/object-detection/) — governed reference unit linked within this cluster.
- [Depth Estimation](/depth-estimation/) — governed reference unit linked within this cluster.
- [Visual Tracking](/visual-tracking/) — governed reference unit linked within this cluster.
- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-316, CLM-317, CLM-318 sourced; CLM-319 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational and technical reference content**. It describes methods and a conceptual framework and makes no performance claims about any specific implementation, product, or system.
