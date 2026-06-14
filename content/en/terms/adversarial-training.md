---
term: Adversarial Training
slug: adversarial-training
route: /adversarial-training/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-285
concept_id: CON-adversarial-training
safety_class: technical
canonical: https://zonules.com/adversarial-training/
last_reviewed: 2026-06-14
claims: [CLM-1136, CLM-1137, CLM-1138, CLM-1139]
sources: [SRC-017, SRC-004]
related_terms: [adversarial-examples, robustness, data-augmentation, domain-shift, corruption-robustness]
seo_title: "Adversarial Training | Zonules.com"
meta_description: "Adversarial training improves robustness by including adversarially perturbed examples in the training data."
---

# Adversarial Training

> Teaching a model to hold signal against deliberate noise.

## Definition

Adversarial training improves robustness by including adversarially perturbed examples in the training data. [CLM-1136]

## Scientific Grounding

The model learns to resist the small, structured perturbations that would otherwise fool it. [CLM-1137] Robustness gained this way often comes at some cost to accuracy on clean inputs. [CLM-1138]

*Sources: SRC-017. See the source registry for classification.*

## Machine-Vision Role

Adversarial training is a separation-layer defense: it teaches the model to hold the signal against deliberate noise. [CLM-1139]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** robustness
- **FIO class:** FIO-03 — Signal–Noise Failure
- **FIS criterion:** FIS-3 — Separation

## Relationship to the Governing Thesis

Adversarial Training is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-03 — Separation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Adversarial Examples](/adversarial-examples/) — related governed reference unit.
- [Robustness](/robustness/) — related governed reference unit.
- [Data Augmentation](/data-augmentation/) — related governed reference unit.
- [Domain Shift](/domain-shift/) — related governed reference unit.
- [Corruption Robustness](/corruption-robustness/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-017 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-1136, CLM-1137, CLM-1138 sourced; CLM-1139 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
