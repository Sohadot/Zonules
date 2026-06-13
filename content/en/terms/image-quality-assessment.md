---
term: Image Quality Assessment
slug: image-quality-assessment
route: /image-quality-assessment/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision
cluster: machine-perception
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-148
concept_id: CON-image-quality-assessment
safety_class: technical
canonical: https://zonules.com/image-quality-assessment/
last_reviewed: 2026-06-13
claims: [CLM-540, CLM-541, CLM-542, CLM-543]
sources: ["SRC-007"]
related_terms: ["contrast-sensitivity", "adversarial-examples", "image-registration", "model-calibration", "contrastive-learning"]
seo_title: "Image Quality Assessment | Zonules.com"
meta_description: "Image quality assessment is the task of measuring or predicting the perceptual quality of an image, including degradations from noise, blur, compression, a"
---
# Image Quality Assessment

> Image quality assessment is a signal-noise measurement

## Definition

Image quality assessment is the task of measuring or predicting the perceptual quality of an image, including degradations from noise, blur, compression, and distortion. [CLM-540]

## Scientific Grounding

No-reference (blind) image quality metrics predict quality without access to a pristine reference image, using learned statistical regularities of natural images. [CLM-541] Full-reference metrics such as SSIM compare a degraded image to an undegraded reference across luminance, contrast, and structure channels. [CLM-542]

*Sources: SRC-007. See the source registry for classification.*

## Technical Role

Image quality assessment is a signal-noise measurement (FIO-03): it quantifies how far the signal channel has degraded from the intact signal, the machine analogue of contrast sensitivity measurement in biological vision. [CLM-543]

## Layer Classification

- **Layer:** L3 — Machine Vision
- **Cluster:** machine-perception
- **FIO class:** FIO-03 — Signal-Noise
- **FIS criterion:** FIS-3

## Relationship to the Governing Thesis

Image Quality Assessment is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-03 — Signal-Noise concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Related Terms

- [Contrast Sensitivity](/contrast-sensitivity/) — governed reference unit linked within this cluster.
- [Adversarial Examples](/adversarial-examples/) — governed reference unit linked within this cluster.
- [Image Registration](/image-registration/) — governed reference unit linked within this cluster.
- [Model Calibration](/model-calibration/) — governed reference unit linked within this cluster.
- [Contrastive Learning](/contrastive-learning/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-007 (registered).
- **Claims:** CLM-540, CLM-541, CLM-542 sourced; CLM-543 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes machine vision methods and a conceptual framework. It does not constitute professional engineering or medical advice.
