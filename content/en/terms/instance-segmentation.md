---
term: Instance Segmentation
slug: instance-segmentation
route: /instance-segmentation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-150
concept_id: CON-instance-segmentation
safety_class: technical
canonical: https://zonules.com/instance-segmentation/
last_reviewed: 2026-06-13
claims: [CLM-548, CLM-549, CLM-550, CLM-551]
sources: ["SRC-007"]
related_terms: ["semantic-segmentation", "object-detection", "scene-understanding", "visual-question-answering", "image-quality-assessment"]
seo_title: "Instance Segmentation | Zonules.com"
meta_description: "Instance segmentation is the task of simultaneously detecting, classifying, and producing pixel-level masks for each individual instance of each object cla"
---
# Instance Segmentation

> Instance segmentation is an interpretation task

## Definition

Instance segmentation is the task of simultaneously detecting, classifying, and producing pixel-level masks for each individual instance of each object class in an image. [CLM-548]

## Scientific Grounding

Instance segmentation combines the challenges of object detection (where?) and semantic segmentation (what shape?), distinguishing individual instances of the same class. [CLM-549] Transformer-based methods such as Mask2Former attend to object queries and achieve state-of-the-art accuracy across diverse object categories. [CLM-550]

*Sources: SRC-007. See the source registry for classification.*

## Technical Role

Instance segmentation is an interpretation task (FIO-05): the system must not only label each pixel but assign each pixel to a specific individual object — a judgment that goes beyond the input signal. [CLM-551]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Instance Segmentation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Semantic Segmentation](/semantic-segmentation/) — governed reference unit linked within this cluster.
- [Object Detection](/object-detection/) — governed reference unit linked within this cluster.
- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.
- [Visual Question Answering](/visual-question-answering/) — governed reference unit linked within this cluster.
- [Image Quality Assessment](/image-quality-assessment/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-548, CLM-549, CLM-550 sourced; CLM-551 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
