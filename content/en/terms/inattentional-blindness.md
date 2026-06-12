---
term: Inattentional Blindness
slug: inattentional-blindness
route: /inattentional-blindness/
language: en
page_type: reference-unit
status: approved
layer: L2
layer_name: Perception
cluster: perceptual-clarity
fio_class: FIO-04
fis_criterion: FIS-4
term_id: TRM-024
concept_id: CON-provenance-failure
safety_class: educational
canonical: https://zonules.com/inattentional-blindness/
last_reviewed: 2026-06-12
claims: [CLM-088, CLM-089, CLM-090, CLM-091]
sources: [SRC-005, SRC-004]
related_terms: [selective-attention, visual-working-memory, depth-perception]
seo_title: "Inattentional Blindness — When What You See Has No Provenance | Zonules.com"
meta_description: "Inattentional blindness is the failure to notice a fully visible unexpected stimulus. The input was present but formed no record. A governed reference unit on perceptual provenance failure."
---

# Inattentional Blindness

> The input was present. The eyes were open. The visual cortex was active. And still, it was not seen. That is not a failure of vision — it is a failure of provenance.

## Definition

**Inattentional blindness** is the failure to notice a fully visible but unexpected stimulus when attention is engaged elsewhere. [CLM-088] The term distinguishes the phenomenon from ordinary failures of vision: in inattentional blindness, there is nothing wrong with the eyes or the visual pathway. The stimulus is present in the visual field, falls on functioning retina, and is neurally processed to some degree — but it does not reach conscious awareness.

The phenomenon is counterintuitive: most people believe they would notice a large, salient, unexpected object in their visual field. The evidence shows they often do not.

## Scientific Grounding

Inattentional blindness demonstrates that visual awareness requires attention as a condition, not merely sensory input. [CLM-089] Objects outside the current focus of attention are processed in the early stages of visual analysis — their basic features can influence response times and low-level neural activity — but they do not become consciously reportable because they have not been selected for further processing.

The probability that an unexpected stimulus will be missed increases when it is dissimilar to the attended target (because attention is tuned to features of the target) and when it appears in the peripheral visual field rather than at the attended location. [CLM-090] The gorilla in the gorilla experiment — a person in a gorilla suit walking through a basketball game — is unexpected, unlike the attended players, and briefly peripheral to the attended action, which predicts exactly the observed blindness.

*Source: sensation and perception reference (SRC-005). See the source registry for classification.*

## Provenance Failure

Inattentional blindness is a provenance failure in the perceptual system. [CLM-091] The visual signal was present — photons arrived, the retina responded — but the system has no record of it. No attended representation was formed, no trace enters working memory, and no content is available for subsequent report or comparison. In the focus-integrity sense, the input has no provenance: it existed in the world but not in the perceptual record.

This maps inattentional blindness to FIO-04 (Provenance Failure): the issue is not that the signal was too weak (signal-noise), not that it was interpreted wrongly (interpretation), but that it was never registered as having a representational origin.

## Layer Classification

- **Layer:** L2 — Perception (attention as the second suspension)
- **Cluster:** Perceptual clarity
- **FIO class:** FIO-04 — Provenance Failure (the input was present but the perceptual system holds no record of it; it has no representational origin)
- **FIS criterion:** FIS-4 — Provenance (intact perception means the source of attended inputs is correctly tracked and recorded)

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
