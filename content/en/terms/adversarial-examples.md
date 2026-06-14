---
term: Adversarial Examples
slug: adversarial-examples
route: /adversarial-examples/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: robustness
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-027
concept_id: CON-structured-noise
safety_class: technical
canonical: https://zonules.com/adversarial-examples/
last_reviewed: 2026-06-12
claims: [CLM-100, CLM-101, CLM-102, CLM-103]
sources: [SRC-007, SRC-004]
related_terms: [object-detection, computer-vision, image-classification]
seo_title: "Adversarial Examples — Structured Noise That Defeats Machine Focus | Zonules.com"
meta_description: "Adversarial examples are imperceptible perturbations that cause machine vision systems to fail. They are signal-noise failures: the noise is structured to defeat separation. A governed reference unit."
---

# Adversarial Examples

> The image looks correct. To any human observer it is unchanged. But the model produces the wrong answer. The noise is invisible to one visual system and devastating to the other — because their signal boundaries do not coincide.

## Definition

**Adversarial examples** are inputs to machine learning models that have been modified by small, often imperceptible perturbations designed to cause the model to produce incorrect outputs. [CLM-100] The modifications are typically so small that a human observer would not notice them — the image of a panda that a human recognizes as a panda, the model classifies as a gibbon. Yet to the model, the perturbation shifts the input across a decision boundary.

## Scientific Grounding

The existence of adversarial examples demonstrates a structural property of learned representations: high accuracy on standard benchmarks does not guarantee robustness. A model can fail catastrophically on an input that a human sees as normal, correctly classified, and unmodified. [CLM-101] This is not a matter of model size or training data volume — the phenomenon appears in well-trained, high-performing models and reflects the geometry of their learned decision surfaces.

**Adversarial robustness** — the ability to maintain correct output under adversarial perturbation — is a distinct property from accuracy that must be specifically designed for. [CLM-102] A model that achieves 97% accuracy on a benchmark may achieve 0% accuracy on an adversarially perturbed version of the same benchmark. Standard training does not produce adversarial robustness as a byproduct; it requires additional objectives, regularization, or adversarial training during the training process itself.

*Source: computer vision reference (SRC-007). See the source registry for classification.*

## Signal Boundaries That Do Not Coincide

Adversarial examples are signal-noise failures of a specific and revealing kind. [CLM-103] The perturbations that defeat the model are imperceptible to a human because they fall below the human visual system's signal-noise boundary: they are noise to a human. But they are not noise to the model — they are signal, specifically structured signal, that the model's learned decision boundaries are sensitive to.

This exposes a fundamental asymmetry: the machine and human visual systems have different signal-noise boundaries. The model's boundary is a mathematical surface in a high-dimensional space; the human's is a biological structure evolved for the natural statistics of the world. Adversarial noise is designed to cross the machine's boundary without crossing the human's. Signal-noise integrity (FIS-3) fails not because the noise is strong, but because the model's separation criterion is fragile where the human's is robust.

## Layer Classification

- **Layer:** L3 — Machine Vision and Verification
- **Cluster:** robustness
- **FIO class:** FIO-03 — Signal–Noise Failure (adversarial perturbations are noise structured to defeat signal-noise separation in machine models; they do not defeat human separation)
- **FIS criterion:** FIS-3 — Separation (a model with intact FIS-3 correctly separates signal from structured noise, including adversarial noise)

## Relationship to the Governing Thesis

The governing thesis locates the failure of focus in hidden structural conditions. Adversarial examples reveal a hidden structural condition of machine vision that is invisible in normal operation: the mismatch between the machine's learned signal boundaries and the human's evolved ones. The model appears to see correctly; the flaw is not detectable from normal output; it only surfaces when the hidden structure is deliberately exploited. This is the machine form of the thesis: the fragility is structural, invisible, and consequential.

## Related Terms

- [Object detection](/object-detection/) — a task particularly vulnerable to adversarial perturbation of localization boundaries
- [Computer vision](/computer-vision/) — the field in which adversarial robustness is an active research problem
- [Image classification](/image-classification/) — the benchmark task on which adversarial fragility was first demonstrated at scale

## Reference Notes

- **Sources:** SRC-007 (technical fact); SRC-004 (internal framework mapping).
- **Claims:** CLM-100, CLM-101, CLM-102 are sourced; CLM-103 is internal framework language.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes the adversarial examples phenomenon and does not make claims about the capabilities or limitations of any specific commercial product or system.
