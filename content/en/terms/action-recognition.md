---
term: Action Recognition
slug: action-recognition
route: /action-recognition/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: detection
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-135
concept_id: CON-action-recognition
safety_class: technical
canonical: https://zonules.com/action-recognition/
last_reviewed: 2026-06-13
claims: [CLM-488, CLM-489, CLM-490, CLM-491]
sources: ["SRC-007"]
related_terms: ["video-understanding", "optical-flow", "pose-estimation", "motion-perception", "scene-understanding", 'gaze-estimation']
seo_title: "Action Recognition | Zonules.com"
meta_description: "Action recognition is the task of identifying the action being performed in a video or sequence of images based on the temporal pattern of motion and appea"
---
# Action Recognition

> Action recognition is an interpretation of motion

## Definition

Action recognition is the task of identifying the action being performed in a video or sequence of images based on the temporal pattern of motion and appearance. [CLM-488]

## Scientific Grounding

Modern systems use spatiotemporal convolutions or video transformers that process temporal patterns alongside spatial appearance features. [CLM-489] Action recognition requires distinguishing intentional from coincidental motion and is sensitive to viewpoint, speed variation, and occlusion of key body parts. [CLM-490]

*Sources: SRC-007. See the source registry for classification.*

## Technical Role

Action recognition is an interpretation of motion (FIO-05): the category (the action) is assigned to a temporal signal based on learned expectation about what motion patterns mean. [CLM-491]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** detection
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Action Recognition is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Video Understanding](/video-understanding/) — governed reference unit linked within this cluster.
- [Optical Flow](/optical-flow/) — governed reference unit linked within this cluster.
- [Pose Estimation](/pose-estimation/) — governed reference unit linked within this cluster.
- [Motion Perception](/motion-perception/) — governed reference unit linked within this cluster.
- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-488, CLM-489, CLM-490 sourced; CLM-491 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
