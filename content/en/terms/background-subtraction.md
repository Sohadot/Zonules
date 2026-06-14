---
term: Background Subtraction
slug: background-subtraction
route: /background-subtraction/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: segmentation
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-275
concept_id: CON-background-subtraction
safety_class: technical
canonical: https://zonules.com/background-subtraction/
last_reviewed: 2026-06-14
claims: [CLM-1096, CLM-1097, CLM-1098, CLM-1099]
sources: [SRC-007, SRC-004]
related_terms: [semantic-segmentation, visual-tracking, anomaly-detection, optical-flow, superpixels, interactive-segmentation]
seo_title: "Background Subtraction | Zonules.com"
meta_description: "Background subtraction separates moving foreground objects from a static background in video."
---

# Background Subtraction

> The moving signal pulled from a static surround.

## Definition

Background subtraction separates moving foreground objects from a static background in video. [CLM-1096]

## Scientific Grounding

It maintains a model of the background scene and flags the pixels that deviate from it. [CLM-1097] Changing illumination and moving backgrounds are classic sources of error. [CLM-1098]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Background subtraction is a separation-layer operation: it pulls the relevant moving signal out of a static surround. [CLM-1099]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** segmentation
- **FIO class:** FIO-03 — Signal–Noise Failure
- **FIS criterion:** FIS-3 — Separation

## Relationship to the Governing Thesis

Background Subtraction is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-03 — Separation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Semantic Segmentation](/semantic-segmentation/) — related governed reference unit.
- [Visual Tracking](/visual-tracking/) — related governed reference unit.
- [Anomaly Detection](/anomaly-detection/) — related governed reference unit.
- [Optical Flow](/optical-flow/) — related governed reference unit.
- [Superpixels](/superpixels/) — related governed reference unit.
- [Interactive Segmentation](/interactive-segmentation/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1096, CLM-1097, CLM-1098 sourced; CLM-1099 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
