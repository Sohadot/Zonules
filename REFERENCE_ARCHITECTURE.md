# REFERENCE_ARCHITECTURE.md

**Zonules.com — Reference Architecture**
**Sohadot Portfolio · agent@sohadot.com**
**Version 0.1**
**Governing document:** `ASSET_THESIS.md` · **Methodology:** `Sohadot/sovereign-asset-system`

---

## Status

This document ratifies the two governed reference structures that the Focus Integrity Engine depends on:

- **FIO — the Focus Integrity Ontology** (what the failure modes of focus are)
- **FIS — the Focus Integrity Standard** (what intact focus integrity is)

It is subordinate to `ASSET_THESIS.md`. Where it conflicts with the thesis, the static-first doctrine, the No-API doctrine, or the medical-safety doctrine, those govern. It is bound by `Sohadot/sovereign-asset-system/docs/FOUNDATION_DOCTRINE.md`: the stricter rule always wins, and no change to FIO or FIS is valid without a `DECISION_LOG.md` entry and a version increment.

The machine-readable encodings of these structures live in:

- `data/focus-integrity-ontology.json`
- `data/focus-integrity-standard.json`

The Markdown in this document and the JSON encodings must agree. If they diverge, publication is frozen until they are reconciled (Foundation Doctrine, Enforcement clause 4).

---

## Versioning Rule

Both FIO and FIS are versioned `MAJOR.MINOR`.

- **MINOR** — adding a class, criterion, or relationship without redefining an existing one.
- **MAJOR** — redefining, merging, splitting, or removing an existing class or criterion.

Every increment is recorded in `DECISION_LOG.md` with date and rationale. The `version` field in the JSON must match the version named here.

---

## FIO — The Focus Integrity Ontology (v0.1)

The governed classification of how focus is held and how it fails, across the three thesis layers: **Anatomy (L1)**, **Perception (L2)**, **Machine Vision & Verification (L3)**.

### Entry Criteria for a Class

A phenomenon may enter FIO only if all four hold:

1. It is a failure or condition of **focus**, not of vision in general.
2. It maps to at least one thesis layer (L1, L2, or L3).
3. It is source-backed, or explicitly marked as conceptual interpretation.
4. It connects to at least two existing reference units.

A phenomenon that fails any criterion is excluded, regardless of how interesting it is. This is the imitation barrier: the ontology resists casual expansion.

### Top-Level Classes

#### FIO-01 — Suspension Failure

The holding structures that keep the focal element in position themselves fail.

- **L1 (Anatomy):** zonular weakness, dislocation, or rupture compromising lens position. *(Educational reference only — never a diagnosis.)*
- **L2 (Perception):** collapse of attentional anchoring; the mind cannot hold a focal target steady against competing stimuli.
- **L3 (Machine):** loss of calibration or spatial grounding; the model's reference frame for "where to look" degrades.
- **Governing claim:** when the suspension layer fails, the focal element is present but unstable.

#### FIO-02 — Accommodation Failure

The system cannot adjust focus across its intended operating range.

- **L1:** loss of accommodative range. *(Educational reference only.)*
- **L2:** failure of perceptual constancy — the percept does not remain stable as conditions change.
- **L3:** domain shift — the model focuses correctly in training conditions but cannot adjust to new ones.
- **Governing claim:** intact focus is range-dependent; a system that focuses at one setting only does not have focus integrity.

#### FIO-03 — Signal–Noise Failure

The system cannot separate meaningful signal from noise.

- **L1:** optical scatter / media opacity reducing contrast at the receptor. *(Educational reference only.)*
- **L2:** figure-ground collapse; salience misallocation.
- **L3:** adversarial perturbation, synthetic noise, low signal-to-noise input defeating the model.
- **Governing claim:** focus without separation produces sharp noise, not meaning.

#### FIO-04 — Provenance Failure

The system cannot establish whether what it sees is real or where it came from.

- **L1:** *not strongly applicable at the anatomical layer; recorded as a conceptual bridge only.*
- **L2:** misattributed source of a percept; false confidence in an illusion.
- **L3:** deepfake and synthetic media; absent or broken image provenance; unverifiable visual claims.
- **Governing claim:** in an age of synthetic images, focus without provenance cannot yield visual truth.

#### FIO-05 — Interpretation Failure

Focus is held and signal is clean, but the resulting meaning is wrong.

- **L1:** *conceptual bridge only — interpretation is not an anatomical property.*
- **L2:** perceptual error; correct sharp percept, incorrect meaning.
- **L3:** machine sight without machine understanding; correct detection, wrong interpretation or grounding.
- **Governing claim:** the final failure of focus is not blur — it is confident misreading.

### Class Relationships (governed)

- FIO-01 and FIO-02 are **structural** failures (the holding/adjusting mechanism).
- FIO-03 and FIO-04 are **input** failures (what reaches the system).
- FIO-05 is the **output** failure (what the system concludes).
- A reading may identify multiple classes. The five classes are ordered from mechanism → input → output and are not mutually exclusive.

---

## FIS — The Focus Integrity Standard (v0.1)

FIO says what the failures are. FIS defines what **intact focus integrity** is. A seeing system has focus integrity when all five criteria hold. Each FIS criterion is the inverse of one FIO class.

| Criterion | Statement | Inverse of |
|-----------|-----------|-----------|
| **FIS-1 Suspension** | The structures holding the focal element are identified and stable. | FIO-01 |
| **FIS-2 Accommodation** | The system adjusts focus across its intended operating range. | FIO-02 |
| **FIS-3 Separation** | The system separates signal from noise within stated tolerances. | FIO-03 |
| **FIS-4 Provenance** | The system can establish the origin/authenticity of what it sees to a stated confidence. | FIO-04 |
| **FIS-5 Interpretation** | Held, clean focus yields correct interpretation, not merely sharp signal. | FIO-05 |

### Application Rule

FIS is the criterion set the engine scores an input against. It governs **structural reasoning about focus** — never clinical assessment of any individual's eyes. Any anatomy-layer application must carry the educational-reference disclaimer and must not produce diagnostic phrasing.

A criterion is reported as one of: `intact`, `at-risk`, `failed`, or `not-applicable` (for layers where the criterion is a conceptual bridge only, e.g. FIS-4/FIS-5 at L1).

---

## The Focus Integrity Assessment (FIA) — Protocol Summary

The reproducible procedure the engine executes:

1. Identify the layer (L1 / L2 / L3).
2. Test each applicable FIS criterion against the structured input.
3. Map each failed or at-risk criterion to its FIO class.
4. Resolve each finding to the reference units that explain it.

Reproducibility requirement: two operators applying FIA to the same structured input must reach the same FIO mapping. The protocol is rule-based; it contains no interpretive discretion.

The full engine specification is in `ASSET_INTELLIGENCE_FACTORY_PLAN.md` §6. The engine remains static, deterministic, client-side, and free of any network call or data collection.

---

> **The ontology says what the failures are. The standard says what good is. The engine returns the reading. The reference layer holds the meaning.**
