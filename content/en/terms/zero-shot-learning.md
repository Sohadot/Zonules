---
term: Zero-Shot Learning
slug: zero-shot-learning
route: /zero-shot-learning/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-133
concept_id: CON-zero-shot-learning
safety_class: technical
canonical: https://zonules.com/zero-shot-learning/
last_reviewed: 2026-06-13
claims: [CLM-480, CLM-481, CLM-482, CLM-483]
sources: ["SRC-007"]
related_terms: ["few-shot-learning", "vision-language-models", "out-of-distribution-detection", "domain-shift", "self-supervised-learning"]
seo_title: "Zero-Shot Learning | Zonules.com"
meta_description: "Zero-shot learning is the ability of a model to correctly classify or describe inputs from categories it has never seen during training, using semantic des"
---
# Zero-Shot Learning

> Zero-shot learning is an interpretation problem

## Definition

Zero-shot learning is the ability of a model to correctly classify or describe inputs from categories it has never seen during training, using semantic descriptions or attribute embeddings. [CLM-480]

## Scientific Grounding

Vision-language models achieve zero-shot classification by matching image embeddings against text embeddings of category names without category-specific training examples. [CLM-481] Zero-shot performance can degrade significantly on fine-grained distinctions or distribution shifts not covered by semantic descriptions used at training time. [CLM-482]

*Sources: SRC-007. See the source registry for classification.*

## Technical Role

Zero-shot learning is an interpretation problem (FIO-05): the model must assign a category to an input using only structural knowledge from training, with no direct signal from examples of the target category. [CLM-483]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Zero-Shot Learning is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Few Shot Learning](/few-shot-learning/) — governed reference unit linked within this cluster.
- [Vision Language Models](/vision-language-models/) — governed reference unit linked within this cluster.
- [Out Of Distribution Detection](/out-of-distribution-detection/) — governed reference unit linked within this cluster.
- [Domain Shift](/domain-shift/) — governed reference unit linked within this cluster.
- [Self Supervised Learning](/self-supervised-learning/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-480, CLM-481, CLM-482 sourced; CLM-483 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
