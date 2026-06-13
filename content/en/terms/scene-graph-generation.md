---
term: Scene Graph Generation
slug: scene-graph-generation
route: /scene-graph-generation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-101
concept_id: CON-scene-graph-generation
safety_class: technical
canonical: https://zonules.com/scene-graph-generation/
last_reviewed: 2026-06-13
claims: [CLM-352, CLM-353, CLM-354, CLM-355]
sources: [SRC-007]
related_terms: [scene-understanding, vision-language-models, object-detection, visual-grounding, semantic-segmentation]
seo_title: "Scene Graph Generation | Zonules.com"
meta_description: "Scene graph generation is the machine vision task of producing a structured graph of objects and their relationships in an image to support reasoning."
---
# Scene Graph Generation

> Structured meaning assembled from detected parts.

## Definition

Scene graph generation is the machine vision task of producing a structured graph of objects and their relationships in an image. [CLM-352]

## Scientific Grounding

Nodes represent objects and edges represent the relationships between them. [CLM-353] Scene graphs support higher-level reasoning such as visual question answering. [CLM-354]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Scene graph generation is an interpretation layer (FIO-05): structured meaning is assembled from detected parts. [CLM-355]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Scene Graph Generation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.
- [Vision Language Models](/vision-language-models/) — governed reference unit linked within this cluster.
- [Object Detection](/object-detection/) — governed reference unit linked within this cluster.
- [Visual Grounding](/visual-grounding/) — governed reference unit linked within this cluster.
- [Semantic Segmentation](/semantic-segmentation/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-352, CLM-353, CLM-354 sourced; CLM-355 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational and technical reference content**. It describes methods and a conceptual framework and makes no performance claims about any specific implementation, product, or system.
