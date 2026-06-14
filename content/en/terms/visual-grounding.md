---
term: Visual Grounding
slug: visual-grounding
route: /visual-grounding/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: detection
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-064
concept_id: CON-visual-grounding
safety_class: technical
canonical: https://zonules.com/visual-grounding/
last_reviewed: 2026-06-13
claims: [CLM-204, CLM-205, CLM-206, CLM-207]
sources: [SRC-007]
related_terms: [scene-understanding, semantic-segmentation, object-detection, visual-inference, neural-network-interpretability]
seo_title: "Visual Grounding — Linking Language to the Visual World | Zonules.com"
meta_description: "Visual grounding is the task of linking linguistic expressions to their corresponding image regions. Classified FIO-05 Interpretation."
---
# Visual Grounding

> Linking a phrase to a region tests whether a model understands what language and image jointly specify.

## Definition

Visual grounding requires identifying the image region referred to by a natural-language expression, linking linguistic semantics to spatial location in the image. [CLM-204]

## Scientific Grounding

Referring expression comprehension is the canonical visual grounding task, requiring a model to localize a unique referent described by a natural-language phrase. [CLM-205] Visual grounding benchmarks reveal gaps in compositional understanding: models can succeed on individual words while failing on multi-attribute expressions requiring joint spatial and categorical reasoning. [CLM-206]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

In the Zonules FIO framework, visual grounding is classified under FIO-05 Interpretation: it requires the system to produce a correct interpretation of how language and image jointly specify a region. [CLM-207]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** detection
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Visual Grounding is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 (Interpretation) concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.
- [Semantic Segmentation](/semantic-segmentation/) — governed reference unit linked within this cluster.
- [Object Detection](/object-detection/) — governed reference unit linked within this cluster.
- [Visual Inference](/visual-inference/) — governed reference unit linked within this cluster.
- [Neural Network Interpretability](/neural-network-interpretability/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-204, CLM-205, CLM-206 sourced; CLM-207 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine-vision methods and their known failure modes and does not constitute engineering, clinical, or safety advice for any deployed system. Where machine vision is applied to the eye or to medicine, it is not a substitute for advice from a qualified eye-care professional.
