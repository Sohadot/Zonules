---
term: Edge Detection
slug: edge-detection
route: /edge-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-192
concept_id: CON-edge-detection
safety_class: technical
canonical: https://zonules.com/edge-detection/
last_reviewed: 2026-06-14
claims: [CLM-748, CLM-749, CLM-750, CLM-751]
sources: [SRC-007, SRC-016, SRC-004]
related_terms: [feature-extraction, feature-matching, computer-vision, semantic-segmentation]
seo_title: "Edge Detection | Zonules.com"
meta_description: "Edge detection is the computer vision operation that locates points in an image where intensity changes sharply."
---

# Edge Detection

> Finding where intensity breaks is finding structure.

## Definition

Edge detection is the computer vision operation that locates points in an image where intensity changes sharply. [CLM-748]

## Scientific Grounding

Classic operators estimate the image gradient and mark edges at local maxima, often after smoothing to suppress noise. [CLM-749] Marr argued that such intensity changes are a primitive from which later visual representations are built. [CLM-750]

*Sources: SRC-007, SRC-016. See the source registry for classification.*

## Machine-Vision Role

Edge detection is a separation-layer operation — it pulls meaningful boundaries out of a field of pixels. [CLM-751]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-03 — Signal–Noise Failure
- **FIS criterion:** FIS-3 — Separation

## Relationship to the Governing Thesis

Edge Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-03 — Separation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Feature Extraction](/feature-extraction/) — related governed reference unit.
- [Feature Matching](/feature-matching/) — related governed reference unit.
- [Computer Vision](/computer-vision/) — related governed reference unit.
- [Semantic Segmentation](/semantic-segmentation/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-016 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-748, CLM-749, CLM-750 sourced; CLM-751 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
