---
term: Anomaly Detection
slug: anomaly-detection
route: /anomaly-detection/
language: en
page_type: reference-unit
status: approved
layer: L3
layer_name: Machine Vision & Verification
cluster: machine-perception
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-200
concept_id: CON-anomaly-detection
safety_class: technical
canonical: https://zonules.com/anomaly-detection/
last_reviewed: 2026-06-14
claims: [CLM-780, CLM-781, CLM-782, CLM-783]
sources: [SRC-027, SRC-007, SRC-004]
related_terms: [out-of-distribution-detection, uncertainty-estimation, image-quality-assessment, medical-imaging-ai, robustness]
seo_title: "Anomaly Detection | Zonules.com"
meta_description: "Anomaly detection identifies inputs that deviate from a learned model of normal data."
---

# Anomaly Detection

> Flagging the input that does not belong.

## Definition

Anomaly detection identifies inputs that deviate from a learned model of normal data. [CLM-780]

## Scientific Grounding

It is often trained on normal examples alone, flagging inputs that fit the learned pattern poorly. [CLM-781] It supports inspection and monitoring tasks where rare defects must be caught without examples of every failure. [CLM-782]

*Sources: SRC-027, SRC-007. See the source registry for classification.*

## Machine-Vision Role

Anomaly detection is a separation-layer alarm — it marks the input that does not belong with the signal. [CLM-783]

## Layer Classification

- **Layer:** L3 — Machine Vision & Verification
- **Cluster:** machine-perception
- **FIO class:** FIO-03 — Signal–Noise Failure
- **FIS criterion:** FIS-3 — Separation

## Relationship to the Governing Thesis

Anomaly Detection is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as an FIO-03 — Separation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon. The [Focus Integrity Codes](/focus-integrity-codes/) page explains how to read these codes.

## Related Terms

- [Out Of Distribution Detection](/out-of-distribution-detection/) — related governed reference unit.
- [Uncertainty Estimation](/uncertainty-estimation/) — related governed reference unit.
- [Image Quality Assessment](/image-quality-assessment/) — related governed reference unit.
- [Medical Imaging Ai](/medical-imaging-ai/) — related governed reference unit.
- [Model Robustness](/robustness/) — related governed reference unit.

## Reference Notes

- **Sources:** SRC-027, SRC-007 (registered); SRC-004 (internal framework mapping).
- **Claims:** CLM-780, CLM-781, CLM-782 sourced; CLM-783 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes a machine-vision concept and does not make claims about the capabilities or limitations of any specific commercial product or system.
