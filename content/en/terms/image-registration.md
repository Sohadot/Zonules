---
term: Image Registration
slug: image-registration
route: /image-registration/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-01
fis_criterion: FIS-1
term_id: TRM-100
concept_id: CON-image-registration
safety_class: technical
canonical: https://zonules.com/image-registration/
last_reviewed: 2026-06-13
claims: [CLM-348, CLM-349, CLM-350, CLM-351]
sources: [SRC-007]
related_terms: [visual-slam, model-calibration, medical-imaging-ai, optical-flow]
seo_title: "Image Registration | Zonules.com"
meta_description: "Image registration is the process of aligning two or more images into a common spatial coordinate frame, critical in fields such as medical imaging."
---
# Image Registration

> Holding a consistent frame across many images.

## Definition

Image registration is the process of aligning two or more images into a common spatial coordinate frame. [CLM-348]

## Scientific Grounding

It is used to combine images taken at different times, from different viewpoints, or by different sensors. [CLM-349] Registration accuracy is critical in applications such as medical imaging and remote sensing. [CLM-350]

*Sources: SRC-007. See the source registry for classification.*

## Machine-Vision Role

Image registration is a suspension of spatial reference (FIO-01): it holds a consistent frame across images. [CLM-351]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-01 — Suspension
- **FIS criterion:** FIS-1

## Relationship to the Governing Thesis

Image Registration is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-01 — Suspension concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Visual Slam](/visual-slam/) — governed reference unit linked within this cluster.
- [Model Calibration](/model-calibration/) — governed reference unit linked within this cluster.
- [Medical Imaging Ai](/medical-imaging-ai/) — governed reference unit linked within this cluster.
- [Optical Flow](/optical-flow/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-348, CLM-349, CLM-350 sourced; CLM-351 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational and technical reference content**. It describes methods and a conceptual framework and makes no performance claims about any specific implementation, product, or system.
