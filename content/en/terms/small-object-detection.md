---
term: Small Object Detection
slug: small-object-detection
route: /small-object-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-296
concept_id: CON-small-object-detection
safety_class: technical
canonical: https://zonules.com/small-object-detection/
last_reviewed: 2026-06-14
claims: [CLM-1180, CLM-1181, CLM-1182, CLM-1183]
sources: [SRC-007, SRC-004]
related_terms: [object-detection, image-classification, region-proposal, feature-extraction, multi-object-tracking, open-vocabulary-detection]
seo_title: "Small Object Detection | Zonules.com"
meta_description: "Small object detection addresses the difficulty of finding objects that occupy very few pixels."
---

# Small Object Detection

> Can faint signal still be correctly read?

## Definition

Small object detection addresses the difficulty of finding objects that occupy very few pixels. [CLM-1180]

## Scientific Grounding

Small objects carry little feature information and are easily lost in downsampling. [CLM-1181] Higher input resolution and multi-scale features are common remedies. [CLM-1182]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Small object detection is an interpretation-layer limit: it tests whether faint signal can still be correctly read. [CLM-1183]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Small Object Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Object Detection](/object-detection/) — related governed reference unit.
- [Image Classification](/image-classification/) — related governed reference unit.
- [Region Proposal](/region-proposal/) — related governed reference unit.
- [Feature Extraction](/feature-extraction/) — related governed reference unit.
- [Multi-Object Tracking](/multi-object-tracking/) — related governed reference unit.
- [Open-Vocabulary Detection](/open-vocabulary-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1180, CLM-1181, CLM-1182 sourced; CLM-1183 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
