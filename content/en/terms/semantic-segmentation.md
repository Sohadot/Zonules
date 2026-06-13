---
term: Semantic Segmentation
slug: semantic-segmentation
route: /semantic-segmentation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-065
concept_id: CON-semantic-segmentation
safety_class: technical
canonical: https://zonules.com/semantic-segmentation/
last_reviewed: 2026-06-13
claims: [CLM-208, CLM-209, CLM-210, CLM-211]
sources: [SRC-007]
related_terms: [scene-understanding, object-detection, visual-grounding, visual-scene-parsing, ophthalmic-ai]
seo_title: "Semantic Segmentation — Dense Pixel-Level Scene Labelling | Zonules.com"
meta_description: "Semantic segmentation assigns a class label to every pixel in an image. The machine-vision instantiation of visual scene parsing at pixel level. Classified FIO-05."
---
# Semantic Segmentation

> Labelling every pixel is an act of interpretation that can fail silently on anything unfamiliar.

## Definition

Semantic segmentation assigns a class label to every pixel in an image, partitioning the image into regions corresponding to recognized categories. [CLM-208]

## Scientific Grounding

Instance segmentation extends semantic segmentation by distinguishing individual instances of the same class, assigning each pixel both a category label and an instance identity. [CLM-209] Semantic segmentation fails silently on out-of-vocabulary regions: pixels belonging to unrecognized categories are assigned to the nearest known class rather than flagged as unknown. [CLM-210]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

In the Zonules FIO framework, semantic segmentation is classified under FIO-05 Interpretation: assigning meaning to every pixel is an act of interpretation that can fail systematically without signalling failure. [CLM-211]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Semantic Segmentation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 (Interpretation) concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Scene Understanding](/scene-understanding/) — governed reference unit linked within this cluster.
- [Object Detection](/object-detection/) — governed reference unit linked within this cluster.
- [Visual Grounding](/visual-grounding/) — governed reference unit linked within this cluster.
- [Visual Scene Parsing](/visual-scene-parsing/) — governed reference unit linked within this cluster.
- [Ophthalmic AI](/ophthalmic-ai/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-208, CLM-209, CLM-210 sourced; CLM-211 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine-vision methods and their known failure modes and does not constitute engineering, clinical, or safety advice for any deployed system. Where machine vision is applied to the eye or to medicine, it is not a substitute for advice from a qualified eye-care professional.
