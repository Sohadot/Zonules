---
term: Medical Imaging AI
slug: medical-imaging-ai
route: /medical-imaging-ai/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-067
concept_id: CON-medical-imaging-ai
safety_class: medical-educational
canonical: https://zonules.com/medical-imaging-ai/
last_reviewed: 2026-06-13
claims: [CLM-216, CLM-217, CLM-218, CLM-219]
sources: [SRC-007]
related_terms: [ophthalmic-ai, domain-shift, model-calibration, semantic-segmentation, neural-network-interpretability]
seo_title: "Medical Imaging AI — High-Stakes Machine Interpretation of Clinical Images | Zonules.com"
meta_description: "Medical imaging AI applies machine vision to clinical images for diagnostic support. Carries the highest-stakes interpretation risks in the FIO framework. Classified FIO-05."
---
# Medical Imaging AI

> Benchmark accuracy is not deployment safety; the gap between them is an interpretation failure.

## Definition

Medical imaging AI has achieved expert-level benchmark performance across several modalities including radiology, pathology, and ophthalmology, on specific task-benchmark combinations. [CLM-216]

## Scientific Grounding

Performance gaps between benchmark conditions and clinical deployment have been documented across medical imaging AI, driven by distribution shift, patient population differences, and workflow integration factors. [CLM-217] Medical imaging AI outputs require integration with clinical context for appropriate use; autonomous AI decision-making in diagnosis is not supported by most current regulatory frameworks. [CLM-218]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

In the Zonules FIO framework, medical imaging AI is classified under FIO-05 Interpretation: translating image data into clinical meaning is the interpretation task, and the gap between benchmark and deployment is the interpretation failure mode. [CLM-219]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Medical Imaging AI is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 (Interpretation) concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Ophthalmic AI](/ophthalmic-ai/) — governed reference unit linked within this cluster.
- [Domain Shift](/domain-shift/) — governed reference unit linked within this cluster.
- [Model Calibration](/model-calibration/) — governed reference unit linked within this cluster.
- [Semantic Segmentation](/semantic-segmentation/) — governed reference unit linked within this cluster.
- [Neural Network Interpretability](/neural-network-interpretability/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-216, CLM-217, CLM-218 sourced; CLM-219 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes anatomy and physiology and does not diagnose, assess, or advise on any individual's eyes or vision. It is not a substitute for examination or advice from a qualified eye-care professional. Nothing on this page should be read as a description of a medical condition you may have.
