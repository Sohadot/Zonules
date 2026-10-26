---
term: Change Blindness
slug: change-blindness
route: /change-blindness/
language: en
page_type: reference-unit
status: approved
layer: L2
layer_name: Perception
cluster: attention
fio_class: FIO-03
fis_criterion: FIS-3
term_id: TRM-032
concept_id: CON-temporal-provenance
safety_class: educational
canonical: https://zonules.com/change-blindness/
last_reviewed: 2026-10-26
claims: [CLM-117, CLM-118, CLM-119, CLM-120]
sources: [SRC-005, SRC-006, SRC-004]
related_terms: [inattentional-blindness, visual-working-memory, selective-attention]
seo_title: "Change Blindness — When a Change Signal Is Masked | Zonules.com"
meta_description: "Change blindness is the failure to detect a large scene change across a brief disruption that masks the change signal. A governed reference unit on signal–noise failure across time (FIO-03)."
---

# Change Blindness

> Something in the scene changed. It was large, it was central, and you were looking right at it. You did not notice — because to notice a change, you must have stored what was there before.

## Definition

**Change blindness** is the failure to detect a substantial change in a visual scene when the change coincides with a brief visual disruption — a saccade (rapid eye movement), a flicker, a cut between images, or a momentary occlusion. [CLM-117] The change can be large and located in central vision, yet remain unnoticed for a surprisingly long time. The disruption breaks the continuity that would otherwise make the change pop out as motion.

## Scientific Grounding

Change blindness demonstrates that the visual system does not maintain a complete, detailed internal representation of a scene. [CLM-118] If it did, any change would be detectable by comparison against the stored copy. Instead, detection of a change depends on having attended to and stored the specific element that changed, before the disruption occurred. What was not stored cannot be compared, and what cannot be compared cannot be seen to have changed.

Consistent with this, changes to objects that are the current focus of attention are detected readily, while changes to unattended objects frequently go unnoticed even when they are large and occur in central vision. [CLM-119] Attention determines what enters the stored representation, and only what was stored can be checked against the new view.

*Sources: sensation and perception and vision science references (SRC-005, SRC-006). See the source registry for classification.*

## Signal–Noise Failure Across Time

Within the Focus Integrity framework, change blindness is a signal–noise failure across time (FIO-03). [CLM-120] Normally a change produces a local transient that draws attention to it. The disruption — a flicker, a cut, a saccade — produces transients across the whole scene at once, so the change signal is no longer separable from the surrounding noise. Unless the changed element was already attended and stored, nothing singles it out.

This places change blindness in FIO-03 alongside [inattentional blindness](/inattentional-blindness/), along a different axis: inattentional blindness is a present signal that is never selected; change blindness is a change signal masked by global disruption. It is not a provenance failure (FIO-04): no source is misattributed. *(Reclassified from FIO-04 to FIO-03 on 2026-10-26; see `DECISION_LOG.md`.)*

## Layer Classification

- **Layer:** L2 — Perception (attention as the second suspension)
- **Cluster:** attention
- **FIO class:** FIO-03 — Signal–Noise Failure (a global disruption masks the local change signal, so the change cannot be separated out)
- **FIS criterion:** FIS-3 — Separation (intact function separates a meaningful change from disruption across views)

## Relationship to the Governing Thesis

The governing thesis holds that focus is produced by hidden structural mechanisms. Change blindness reveals one such mechanism by its failure: the perceptual system maintains continuity through a sparse, attention-dependent record rather than a complete image. We feel as though we see everything stably; in fact we hold only what we attended, and the gap is invisible until a change falls into it.

## Relationship to Machine Vision (Layer 03)

In machine vision, the analogue is a change-detection system that fails when it lacks a reliable reference frame from the prior time step — it cannot flag what changed because it never adequately stored what was there. This is a conceptual mapping, marked as internal framework language.

## Related Terms

- [Inattentional blindness](/inattentional-blindness/) — the failure to register a present input; change blindness is its across-time counterpart
- [Visual working memory](/visual-working-memory/) — the limited store whose contents determine what changes can be detected
- [Selective attention](/selective-attention/) — the mechanism that determines what enters the stored representation

## Reference Notes

- **Sources:** SRC-005, SRC-006 (perceptual fact); SRC-004 (internal framework mapping).
- **Claims:** CLM-117, CLM-118, CLM-119 are sourced; CLM-120 is internal framework language.
- **FIO/FIS:** governed by `REFERENCE_ARCHITECTURE.md`.

## Safety Notes

This is **educational reference content only**. It describes perceptual science and does not diagnose or advise on any visual or neurological condition. Nothing on this page should be interpreted as medical advice or used to assess your own perceptual function.
