---
term: Visual Tracking
slug: visual-tracking
route: /visual-tracking/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-098
concept_id: CON-visual-tracking
safety_class: technical
canonical: https://zonules.com/visual-tracking/
last_reviewed: 2026-06-13
claims: [CLM-340, CLM-341, CLM-342, CLM-343]
sources: [SRC-007]
related_terms: [optical-flow, object-detection, visual-slam, pose-estimation]
seo_title: "Visual Tracking | Zonules.com"
meta_description: "Visual tracking is the machine vision task of following the position of one or more targets across video frames despite appearance change and occlusion."
---
# Visual Tracking

> Identity and position held across frames.

## Definition

Visual tracking is the machine vision task of following the position of one or more targets across video frames. [CLM-340]

## Scientific Grounding

Trackers must handle appearance change, occlusion, and motion of the target. [CLM-341] Errors accumulate when a target is lost and then re-acquired incorrectly. [CLM-342]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Visual tracking is a suspension over time (FIO-01): target identity and position are held across frames. [CLM-343]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-01 — Suspension
- **FIS criterion:** FIS-1

## Relationship to the Governing Thesis

Visual Tracking is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Optical Flow](/optical-flow/) — governed reference unit linked within this cluster.
- [Object Detection](/object-detection/) — governed reference unit linked within this cluster.
- [Visual Slam](/visual-slam/) — governed reference unit linked within this cluster.
- [Pose Estimation](/pose-estimation/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-340, CLM-341, CLM-342 sourced; CLM-343 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational and technical reference content**. It describes methods and a conceptual framework and makes no performance claims about any specific implementation, product, or system.
