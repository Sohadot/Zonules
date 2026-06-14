---
term: Multi-Object Tracking
slug: multi-object-tracking
route: /multi-object-tracking/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-295
concept_id: CON-multi-object-tracking
safety_class: technical
canonical: https://zonules.com/multi-object-tracking/
last_reviewed: 2026-06-14
claims: [CLM-1176, CLM-1177, CLM-1178, CLM-1179]
sources: [SRC-007, SRC-004]
related_terms: [visual-tracking, object-detection, video-object-segmentation, optical-flow, small-object-detection, open-vocabulary-detection]
seo_title: "Multi-Object Tracking | Zonules.com"
meta_description: "Multi-object tracking follows several objects across video frames while maintaining a consistent identity for each."
---

# Multi-Object Tracking

> Each object's identity held steady across time.

## Definition

Multi-object tracking follows several objects across video frames while maintaining a consistent identity for each. [CLM-1176]

## Scientific Grounding

It must associate detections over time and handle objects that occlude one another or leave the scene. [CLM-1177] Identity switches, where two tracks are swapped, are a characteristic failure. [CLM-1178]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Multi-object tracking is a suspension-layer task: it holds each object's identity steady across time and occlusion. [CLM-1179]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-01 — Suspension Failure
- **FIS criterion:** FIS-1 — Suspension

## Relationship to the Governing Thesis

Multi-Object Tracking is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Visual Tracking](/visual-tracking/) — related governed reference unit.
- [Object Detection](/object-detection/) — related governed reference unit.
- [Video Object Segmentation](/video-object-segmentation/) — related governed reference unit.
- [Optical Flow](/optical-flow/) — related governed reference unit.
- [Small Object Detection](/small-object-detection/) — related governed reference unit.
- [Open-Vocabulary Detection](/open-vocabulary-detection/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1176, CLM-1177, CLM-1178 sourced; CLM-1179 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
