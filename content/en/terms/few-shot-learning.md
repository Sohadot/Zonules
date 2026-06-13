---
term: Few-Shot Learning
slug: few-shot-learning
route: /few-shot-learning/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-02
fis_criterion: FIS-2
term_id: TRM-117
concept_id: CON-few-shot-learning
safety_class: technical
canonical: https://zonules.com/few-shot-learning/
last_reviewed: 2026-06-13
claims: [CLM-416, CLM-417, CLM-418, CLM-419]
sources: ["SRC-007"]
related_terms: ["transfer-learning", "domain-shift", "generative-models", "zero-shot-learning", "attention-mechanism"]
seo_title: "Few-Shot Learning | Zonules.com"
meta_description: "Few-shot learning is the ability of a model to recognize new categories or tasks from a small number of examples after pre-training on a large corpus."
---
# Few-Shot Learning

> Few-shot learning is an accommodation problem

## Definition

Few-shot learning is the ability of a model to recognize new categories or tasks from a small number of examples after pre-training on a large corpus. [CLM-416]

## Scientific Grounding

Few-shot learning methods include meta-learning, prototypical networks, and fine-tuning large pre-trained models on minimal labeled data. [CLM-417] The performance gap between human and machine few-shot learning reflects a fundamental difference in prior structure. [CLM-418]

*Sources: SRC-007. See the source registry for classification.*

## Technical Role

Few-shot learning is an accommodation problem (FIO-02): the system must extend its operating range to new categories from minimal signal without destabilizing what it already knows. [CLM-419]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-02 — Accommodation
- **FIS criterion:** FIS-2

## Relationship to the Governing Thesis

Few-Shot Learning is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-02 — Accommodation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Transfer Learning](/transfer-learning/) — governed reference unit linked within this cluster.
- [Domain Shift](/domain-shift/) — governed reference unit linked within this cluster.
- [Generative Models](/generative-models/) — governed reference unit linked within this cluster.
- [Zero Shot Learning](/zero-shot-learning/) — governed reference unit linked within this cluster.
- [Attention Mechanism](/attention-mechanism/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-416, CLM-417, CLM-418 sourced; CLM-419 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
