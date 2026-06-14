---
term: Region Proposal
slug: region-proposal
route: /region-proposal/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: segmentation
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-274
concept_id: CON-region-proposal
safety_class: technical
canonical: https://zonules.com/region-proposal/
last_reviewed: 2026-06-14
claims: [CLM-1092, CLM-1093, CLM-1094, CLM-1095]
sources: [SRC-007, SRC-004]
related_terms: [object-detection, instance-segmentation, superpixels, semantic-segmentation, background-subtraction]
seo_title: "Region Proposal | Zonules.com"
meta_description: "Region proposal generates candidate image regions that may contain objects, for later classification."
---

# Region Proposal

> Deciding where the scene is worth reading closely.

## Definition

Region proposal generates candidate image regions that may contain objects, for later classification. [CLM-1092]

## Scientific Grounding

It narrows an intractable search over all possible windows to a manageable set of likely regions. [CLM-1093] Proposal quality bounds the performance of the detection systems built on top of it. [CLM-1094]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Region proposal is an interpretation-layer shortlist: it decides where the scene is worth reading closely. [CLM-1095]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** segmentation
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Region Proposal is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Object Detection](/object-detection/) — related governed reference unit.
- [Instance Segmentation](/instance-segmentation/) — related governed reference unit.
- [Superpixels](/superpixels/) — related governed reference unit.
- [Semantic Segmentation](/semantic-segmentation/) — related governed reference unit.
- [Background Subtraction](/background-subtraction/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1092, CLM-1093, CLM-1094 sourced; CLM-1095 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
