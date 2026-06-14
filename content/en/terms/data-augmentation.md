---
term: Data Augmentation
slug: data-augmentation
route: /data-augmentation/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-02
fis_criterion: FIS-2
term_id: TRM-099
concept_id: CON-data-augmentation
safety_class: technical
canonical: https://zonules.com/data-augmentation/
last_reviewed: 2026-06-13
claims: [CLM-344, CLM-345, CLM-346, CLM-347]
sources: [SRC-007]
related_terms: [transfer-learning, domain-shift, out-of-distribution-detection, image-classification]
seo_title: "Data Augmentation | Zonules.com"
meta_description: "Data augmentation expands training data by applying label-preserving transformations to existing images, improving robustness to input variation."
---
# Data Augmentation

> Widening the range over which a model holds focus.

## Definition

Data augmentation is the practice of expanding training data by applying label-preserving transformations to existing images. [CLM-344]

## Scientific Grounding

Common transformations include cropping, flipping, rotation, and color changes. [CLM-345] Augmentation can improve a model's robustness to variation in its inputs. [CLM-346]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Data augmentation is an accommodation strategy (FIO-02): it widens the range over which a model holds focus. [CLM-347]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** robustness
- **FIO class:** FIO-02 — Accommodation
- **FIS criterion:** FIS-2

## Relationship to the Governing Thesis

Data Augmentation is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-02 — Accommodation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Transfer Learning](/transfer-learning/) — governed reference unit linked within this cluster.
- [Domain Shift](/domain-shift/) — governed reference unit linked within this cluster.
- [Out of Distribution Detection](/out-of-distribution-detection/) — governed reference unit linked within this cluster.
- [Image Classification](/image-classification/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-344, CLM-345, CLM-346 sourced; CLM-347 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational and technical reference content**. It describes methods and a conceptual framework and makes no performance claims about any specific implementation, product, or system.
