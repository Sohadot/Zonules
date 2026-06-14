---
term: Optical Flow
slug: optical-flow
route: /optical-flow/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: detection
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-061
concept_id: CON-optical-flow
safety_class: technical
canonical: https://zonules.com/optical-flow/
last_reviewed: 2026-06-13
claims: [CLM-192, CLM-193, CLM-194, CLM-195]
sources: [SRC-007]
related_terms: [scene-understanding, semantic-segmentation, object-detection, model-calibration, visual-grounding]
seo_title: "Optical Flow — Tracking Motion Across the Visual Field | Zonules.com"
meta_description: "Optical flow is the pattern of apparent motion of image brightness computed from frame-to-frame differences. Classified FIO-01 Suspension."
---
# Optical Flow

> Motion is inferred from frame-to-frame change, and local motion is ambiguous without global context.

## Definition

Optical flow describes the apparent motion of image brightness patterns across a sequence of frames, computed from frame-to-frame differences in pixel intensity. [CLM-192]

## Scientific Grounding

Dense optical flow methods estimate a motion vector for every pixel in the image; sparse methods track selected feature points across frames. [CLM-193] Optical flow is subject to the aperture problem: local motion is inherently ambiguous without global context, because a moving edge seen through a small aperture is consistent with multiple motion directions. [CLM-194]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

In the Zonules FIO framework, optical flow is classified under FIO-01 Suspension: temporal coherence in motion estimation depends on maintaining a structural correspondence between frames that the aperture problem can undermine. [CLM-195]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** detection
- **FIO class:** FIO-01 — Suspension
- **FIS criterion:** FIS-1

## Relationship to the Governing Thesis

Optical Flow is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-01 (Suspension) concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.
- [Semantic Segmentation](/semantic-segmentation/) — governed reference unit linked within this cluster.
- [Object Detection](/object-detection/) — governed reference unit linked within this cluster.
- [Model Calibration](/model-calibration/) — governed reference unit linked within this cluster.
- [Visual Grounding](/visual-grounding/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-192, CLM-193, CLM-194 sourced; CLM-195 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine-vision methods and their known failure modes and does not constitute engineering, clinical, or safety advice for any deployed system. Where machine vision is applied to the eye or to medicine, it is not a substitute for advice from a qualified eye-care professional.
