---
term: Inattentional Blindness
slug: inattentional-blindness
route: /inattentional-blindness/
language: en
page_type: reference-unit
status: approved
layer: L2
layer_name: Perception
cluster: attention
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-024
concept_id: CON-provenance-failure
safety_class: educational
canonical: https://zonules.com/inattentional-blindness/
last_reviewed: 2026-10-26
claims: [CLM-088, CLM-089, CLM-090, CLM-091]
sources: [SRC-005, SRC-004]
related_terms: [selective-attention, visual-working-memory, depth-perception]
seo_title: "Inattentional Blindness — When a Visible Signal Is Never Selected | Zonules.com"
meta_description: "Inattentional blindness is the failure to notice a fully visible unexpected stimulus while attention is engaged elsewhere. A governed reference unit on salience misallocation (FIO-03)."
---

# Inattentional Blindness

> The input was present. The eyes were open. The visual cortex was active. And still, it was not seen. That is not a failure of the eye — it is a failure of selection.

## Definition

**Inattentional blindness** is the failure to notice a fully visible but unexpected stimulus when attention is engaged elsewhere. [CLM-088] The term distinguishes the phenomenon from ordinary failures of vision: in inattentional blindness, there is nothing wrong with the eyes or the visual pathway. The stimulus is present in the visual field, falls on functioning retina, and is neurally processed to some degree — but it does not reach conscious awareness.

The phenomenon is counterintuitive: most people believe they would notice a large, salient, unexpected object in their visual field. The evidence shows they often do not.

## Scientific Grounding

Inattentional blindness demonstrates that visual awareness requires attention as a condition, not merely sensory input. [CLM-089] Objects outside the current focus of attention are processed in the early stages of visual analysis — their basic features can influence response times and low-level neural activity — but they do not become consciously reportable because they have not been selected for further processing.

The probability that an unexpected stimulus will be missed increases when it is dissimilar to the attended target (because attention is tuned to features of the target) and when it appears in the peripheral visual field rather than at the attended location. [CLM-090] The gorilla in the gorilla experiment — a person in a gorilla suit walking through a basketball game — is unexpected, unlike the attended players, and briefly peripheral to the attended action, which predicts exactly the observed blindness.

*Source: sensation and perception reference (SRC-005). See the source registry for classification.*

## Signal–Noise Failure (Salience Misallocation)

Within the Focus Integrity framework, inattentional blindness is a signal–noise failure of the salience-misallocation kind (FIO-03). [CLM-091] The unexpected stimulus is a real, visible signal, but attention is tuned to the features of the task target, so the stimulus is treated as part of the ground rather than separated out as figure. The dependence on dissimilarity from the attended target is exactly what a misallocation of salience predicts.

This is not a provenance failure (FIO-04): nothing is misattributed and no source is mistaken — the stimulus is simply never selected. Nor is it an interpretation failure (FIO-05), because no percept is formed to be misread. *(Reclassified from FIO-04 to FIO-03 on 2026-10-26; see `DECISION_LOG.md`.)*

## Layer Classification

- **Layer:** L2 — Perception (attention as the second suspension)
- **Cluster:** attention
- **FIO class:** FIO-03 — Signal–Noise Failure (salience misallocation: a visible signal is not separated from the ground because attention is tuned elsewhere)
- **FIS criterion:** FIS-3 — Separation (intact perception separates meaningful signal from the background within the limits of attention)

## Relationship to the Governing Thesis

Selective attention — the perceptual suspension system — holds a focal target in place. When attention is fully committed to one target, inattentional blindness shows what the cost of that focus is: the rest of the scene becomes untracked and effectively unrecorded. The same tension that produces focused vision produces blind spots. Focus has a price, and inattentional blindness is that price made explicit.

## Relationship to Machine Vision (Layer 03)

In machine vision, the analogue of inattentional blindness is out-of-distribution input: a machine system focused on one class of input may produce no representation of inputs outside its training distribution. The input arrives, passes through early layers, but produces no interpretable output — no record in the machine's "awareness." This is a conceptual mapping, marked as internal framework language.

## Related Terms

- [Selective attention](/selective-attention/) — the mechanism whose engagement creates the conditions for inattentional blindness
- [Visual working memory](/visual-working-memory/) — the system that fails to receive a record of the unattended input
- [Depth perception](/depth-perception/) — a spatial interpretation failure contrasting with the representational failure of inattentional blindness
- [Change blindness](/change-blindness/) — the across-time counterpart: failure to register that a stimulus has changed

## Reference Notes

- **Sources:** SRC-005 (perceptual fact); SRC-004 (internal framework mapping).
- **Claims:** CLM-088, CLM-089, CLM-090 are sourced; CLM-091 is internal framework language.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes perceptual science and does not diagnose or advise on any visual or neurological condition. Nothing on this page should be interpreted as medical advice or used to assess your own perceptual function.
