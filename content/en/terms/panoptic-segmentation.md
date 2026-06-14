---
term: Panoptic Segmentation
slug: panoptic-segmentation
route: /panoptic-segmentation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-196
concept_id: CON-panoptic-segmentation
safety_class: technical
canonical: https://zonules.com/panoptic-segmentation/
last_reviewed: 2026-06-14
claims: [CLM-764, CLM-765, CLM-766, CLM-767]
sources: [SRC-007, SRC-004]
related_terms: [semantic-segmentation, instance-segmentation, scene-understanding, object-detection]
seo_title: "Panoptic Segmentation | Zonules.com"
meta_description: "Panoptic segmentation assigns every pixel in an image both a class label and, for countable objects, an instance identity."
---

# Panoptic Segmentation

> Every pixel given one, and only one, explanation.

## Definition

Panoptic segmentation assigns every pixel in an image both a class label and, for countable objects, an instance identity. [CLM-764]

## Scientific Grounding

It unifies semantic segmentation of amorphous regions with instance segmentation of distinct objects into one coherent labeling. [CLM-765] Each pixel receives exactly one explanation, leaving no part of the scene unaccounted for. [CLM-766]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Panoptic segmentation is an interpretation-layer completion — every region of the scene must receive a correct reading. [CLM-767]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Panoptic Segmentation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Semantic Segmentation](/semantic-segmentation/) — related governed reference unit.
- [Instance Segmentation](/instance-segmentation/) — related governed reference unit.
- [Scene Understanding](/scene-understanding/) — related governed reference unit.
- [Object Detection](/object-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-764, CLM-765, CLM-766 sourced; CLM-767 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
