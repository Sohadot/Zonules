---
term: Predictive Coding
slug: predictive-coding
route: /predictive-coding/
language: en
page_type: reference-unit
status: approved
layer: L2
layer_name: Perception
cluster: prediction
fio_class: FIO-05
fis_criterion: FIS-5
term_id: TRM-109
concept_id: CON-predictive-coding
safety_class: educational
canonical: https://zonules.com/predictive-coding/
last_reviewed: 2026-06-14
claims: [CLM-384, CLM-385, CLM-386, CLM-387, CLM-574, CLM-575, CLM-576, CLM-577, CLM-1243, CLM-1244]
sources: [SRC-005, SRC-006, SRC-021, SRC-020, SRC-017]
related_terms: ["top-down-processing", "visual-inference", "active-inference", "face-perception", "object-recognition"]
seo_title: "Predictive Coding | Zonules.com"
meta_description: "Predictive coding is a framework in which the brain continuously generates predictions about sensory input and propagates only the residual error signals n"
---
# Predictive Coding

> Predictive coding frames perception as interpretation

## Definition

Predictive coding is a framework in which the brain continuously generates predictions about sensory input and propagates only the residual error signals not explained by the current model. [CLM-384]

## Scientific Grounding

According to this framework, perception is driven primarily by top-down predictions rather than bottom-up signals, with sensory signals serving mainly to correct prediction errors. [CLM-385] The framework accounts for a wide range of perceptual phenomena including illusions, perceptual completion, and the efficiency of neural coding. [CLM-386]

*Sources: SRC-005, SRC-006. See the source registry for classification.*

## Perceptual Role

Predictive coding frames perception as interpretation (FIO-05): the perceived world is not a read-out of sensory input but the brain's best current model, revised at the margin by incoming signal. [CLM-387]

## Layer Classification

- **Layer:** L2 — Perception
- **Cluster:** prediction
- **FIO class:** FIO-05 — Interpretation
- **FIS criterion:** FIS-5

## Relationship to the Governing Thesis

Predictive Coding is one instance of the asset's governing claim: that focus is produced and held by structure that is not itself visible in the result. Its place in the [focus-integrity ontology](/focus-integrity-ontology/) is fixed as a FIO-05 — Interpretation concern, the same failure class whether the seeing system is made of tissue, attention, or silicon.

## Mechanism

In the predictive-coding model the cortex is arranged as a hierarchy that runs mostly top-down. Higher areas send predictions to lower areas, and the lower areas return only the residual prediction error — the portion of the input the current model failed to anticipate. [CLM-574] Rao and Ballard introduced this scheme to explain effects in the visual cortex that a purely bottom-up account could not. The framework is frequently placed inside the broader free-energy principle, under which both perception and action work to minimize long-run prediction error, or surprisal. [CLM-575]

## Failure Mode

Predictive coding makes a specific kind of error legible. When the system's priors are too strong relative to the evidence, prediction overrides veridical input and the observer perceives what was expected rather than what is present. [CLM-576] This is not blur and not noise: focus is held and the signal is clean, yet the meaning is wrong. It is the textbook shape of an Interpretation Failure (FIO-05), and it explains why confident misreading — not absence of detail — is the failure the asset treats as most dangerous.

## Human–Machine Bridge

The logic is not unique to brains. The same error-minimization principle underlies how machine-learning models are trained, adjusting their parameters to reduce the residual between prediction and target. [CLM-577] A model that has over-learned its training distribution will, like an over-confident perceiver, impose its expectations on ambiguous input. Reading predictive coding as a focus-integrity problem makes the human and machine versions of this failure the same problem viewed twice.

## Common Misunderstanding

Predictive coding does not claim the brain ignores the senses. Sensory input remains essential — but its role is to correct predictions rather than to assemble perception from scratch. The percept you experience is the model's current best explanation of the input, continuously revised at the margin, not a raw transcript of the retina.

## Source Notes

Cognitive-science claims rest on perception and neuroscience references (SRC-005, SRC-006, SRC-021) and the free-energy literature (SRC-020); the machine-learning parallel is sourced to a standard deep-learning reference (SRC-017). The focus-integrity mapping is internal framework language (SRC-004).


## Why It Matters

Predictive coding reframes perception as active inference rather than passive reception, which is why it matters far beyond neuroscience: it gives a single account of why expectation shapes what is seen. [CLM-1243] In the thesis it explains how focus is stabilized — by continuously comparing incoming signal against structured expectation and propagating only the difference. [CLM-1244]

## Related Terms

- [Top Down Processing](/top-down-processing/) — governed reference unit linked within this cluster.
- [Visual Inference](/visual-inference/) — governed reference unit linked within this cluster.
- [Active Inference](/active-inference/) — governed reference unit linked within this cluster.
- [Face Perception](/face-perception/) — governed reference unit linked within this cluster.
- [Object Recognition](/object-recognition/) — governed reference unit linked within this cluster.

## Reference Notes

- **Sources:** SRC-005, SRC-006 (registered).
- **Claims:** CLM-384, CLM-385, CLM-386 sourced; CLM-387 internal framework.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes perceptual science and a conceptual framework and does not diagnose, assess, or advise on any individual's vision. It is not medical advice.
