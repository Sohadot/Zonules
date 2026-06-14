---
term: Open-Vocabulary Detection
slug: open-vocabulary-detection
route: /open-vocabulary-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: detection
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-297
concept_id: CON-open-vocabulary-detection
safety_class: technical
canonical: https://zonules.com/open-vocabulary-detection/
last_reviewed: 2026-06-14
claims: [CLM-1184, CLM-1185, CLM-1186, CLM-1187]
sources: [SRC-007, SRC-019, SRC-017, SRC-004]
related_terms: [object-detection, vision-language-models, zero-shot-learning, visual-grounding, multi-object-tracking, small-object-detection, foundation-models]
seo_title: "Open-Vocabulary Detection | Zonules.com"
meta_description: "Open-vocabulary detection localizes and names objects from categories not seen during training."
---

# Open-Vocabulary Detection

> Reading objects it was never trained to name.

## Definition

Open-vocabulary detection localizes and names objects from categories not seen during training. [CLM-1184]

## Scientific Grounding

It typically aligns visual regions with a language model's text embeddings to generalize beyond fixed labels. [CLM-1185] It extends detection from a closed label set toward arbitrary described categories. [CLM-1186]

*Sources: SRC-007, SRC-019, SRC-017. See the source registry for classification.*

## Machine-Vision Role

Open-vocabulary detection is an interpretation-layer reach: it reads objects it was never explicitly trained to name. [CLM-1187]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** detection
- **FIO class:** FIO-05 — Interpretation Failure
- **FIS criterion:** FIS-5 — Interpretation

## Relationship to the Governing Thesis

Open-Vocabulary Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Object Detection](/object-detection/) — related governed reference unit.
- [Vision Language Models](/vision-language-models/) — related governed reference unit.
- [Zero Shot Learning](/zero-shot-learning/) — related governed reference unit.
- [Visual Grounding](/visual-grounding/) — related governed reference unit.
- [Multi-Object Tracking](/multi-object-tracking/) — related governed reference unit.
- [Small Object Detection](/small-object-detection/) — related governed reference unit.
- [Vision Foundation Models](/foundation-models/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-007, SRC-019, SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1184, CLM-1185, CLM-1186 sourced; CLM-1187 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
