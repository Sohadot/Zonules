---
term: Gaze Estimation
slug: gaze-estimation
route: /gaze-estimation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-151
concept_id: CON-gaze-estimation
safety_class: technical
canonical: https://zonules.com/gaze-estimation/
last_reviewed: 2026-06-13
claims: [CLM-552, CLM-553, CLM-554, CLM-555]
sources: ["SRC-007"]
related_terms: ["pose-estimation", "visual-tracking", "oculomotor-system", "fixation", "ophthalmic-ai"]
seo_title: "Gaze Estimation | Zonules.com"
meta_description: "Gaze estimation is the task of determining the direction in which a person is looking from an image or video of their face or eyes."
---
# Gaze Estimation

> Gaze estimation is a structural tracking problem

## Definition

Gaze estimation is the task of determining the direction in which a person is looking from an image or video of their face or eyes. [CLM-552]

## Scientific Grounding

Appearance-based gaze estimation uses deep learning to map from the cropped eye region or full face to gaze direction, without requiring calibration hardware. [CLM-553] Gaze estimation from monocular cameras remains challenging under varying head pose, illumination, and resolution, and errors increase with distance from the camera. [CLM-554]

*Sources: SRC-007. See the source registry for classification.*

## Technical Role

Gaze estimation is a structural tracking problem (FIO-01): the system must maintain a stable, accurate model of where attention is directed by tracking the oculomotor system of the observed person. [CLM-555]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-01 — Suspension
- **FIS criterion:** FIS-1

## Relationship to the Governing Thesis

Gaze Estimation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Pose Estimation](/pose-estimation/) — governed reference unit linked within this cluster.
- [Visual Tracking](/visual-tracking/) — governed reference unit linked within this cluster.
- [Oculomotor System](/oculomotor-system/) — governed reference unit linked within this cluster.
- [Fixation](/fixation/) — governed reference unit linked within this cluster.
- [Ophthalmic Ai](/ophthalmic-ai/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-552, CLM-553, CLM-554 sourced; CLM-555 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
