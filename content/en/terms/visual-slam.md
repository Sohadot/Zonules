---
term: Visual SLAM
slug: visual-slam
route: /visual-slam/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-094
concept_id: CON-visual-slam
safety_class: technical
canonical: https://zonules.com/visual-slam/
last_reviewed: 2026-06-13
claims: [CLM-324, CLM-325, CLM-326, CLM-327]
sources: [SRC-007]
related_terms: [optical-flow, depth-estimation, image-registration, visual-tracking, model-calibration]
seo_title: "Visual SLAM | Zonules.com"
meta_description: "Visual SLAM is the technique by which a system builds a map of an environment while tracking its own position using camera input."
---
# Visual SLAM

> Holding a stable spatial frame while everything moves.

## Definition

Visual SLAM (simultaneous localization and mapping) is the technique by which a system builds a map of an environment while tracking its own position using camera input. [CLM-324]

## Scientific Grounding

It estimates camera motion and scene structure jointly over time. [CLM-325] Positional drift accumulates without loop closure or an external reference. [CLM-326]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Visual SLAM is a suspension mechanism (FIO-01): it holds a stable spatial frame as the camera moves through the world. [CLM-327]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-01 — Suspension
- **FIS criterion:** FIS-1

## Relationship to the Governing Thesis

Visual SLAM is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Optical Flow](/optical-flow/) — governed reference unit linked within this cluster.
- [Depth Estimation](/depth-estimation/) — governed reference unit linked within this cluster.
- [Image Registration](/image-registration/) — governed reference unit linked within this cluster.
- [Visual Tracking](/visual-tracking/) — governed reference unit linked within this cluster.
- [Model Calibration](/model-calibration/) — governed reference unit linked within this cluster.
- [Stereo Matching](/stereo-matching/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-324, CLM-325, CLM-326 sourced; CLM-327 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational and technical reference content**. It describes methods and a conceptual framework and makes no performance claims about any specific implementation, product, or system.
