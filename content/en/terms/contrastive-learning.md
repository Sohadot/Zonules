---
term: Contrastive Learning
slug: contrastive-learning
route: /contrastive-learning/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: representation-learning
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-132
concept_id: CON-contrastive-learning
safety_class: technical
canonical: https://zonules.com/contrastive-learning/
last_reviewed: 2026-06-13
claims: [CLM-476, CLM-477, CLM-478, CLM-479]
sources: ["SRC-007"]
related_terms: ["self-supervised-learning", "feature-extraction", "adversarial-examples", "data-augmentation", "domain-shift"]
seo_title: "Contrastive Learning | Zonules.com"
meta_description: "Contrastive learning is a self-supervised training objective that pulls representations of similar inputs together and pushes representations of dissimilar"
---
# Contrastive Learning

> Contrastive learning is a signal-noise operation

## Definition

Contrastive learning is a self-supervised training objective that pulls representations of similar inputs together and pushes representations of dissimilar inputs apart. [CLM-476]

## Scientific Grounding

Positive pairs (different views of the same image) are brought close in representation space; negative pairs are pushed apart, encouraging representations that capture class-relevant signal. [CLM-477] Large batch sizes are required because informative hard negatives — which share some features with the positive — are rare and their frequency grows with batch size. [CLM-478]

*Sources: SRC-007. See the source registry for classification.*

## Technical Role

Contrastive learning is a signal-noise operation (FIO-03): it trains representations to separate signal that identifies an instance from the noise of augmentation, viewpoint, and irrelevant variation. [CLM-479]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** representation-learning
- **FIO class:** FIO-03 — Signal-Noise
- **FIS criterion:** FIS-3

## Relationship to the Governing Thesis

Contrastive Learning is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-03 — Signal-Noise concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Self Supervised Learning](/self-supervised-learning/) — governed reference unit linked within this cluster.
- [Feature Extraction](/feature-extraction/) — governed reference unit linked within this cluster.
- [Adversarial Examples](/adversarial-examples/) — governed reference unit linked within this cluster.
- [Data Augmentation](/data-augmentation/) — governed reference unit linked within this cluster.
- [Domain Shift](/domain-shift/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-476, CLM-477, CLM-478 sourced; CLM-479 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
