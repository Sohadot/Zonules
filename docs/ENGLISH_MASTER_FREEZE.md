# ENGLISH_MASTER_FREEZE.md

**Zonules.com — English Canonical Master Freeze**
**Sohadot Portfolio · agent@sohadot.com**
**Version 1.0 — Sprint 6F — 2026-06-14**
**Governing document:** `ASSET_THESIS.md`

---

## Status

**FROZEN.**

The English canonical master of Zonules.com is declared frozen as of 2026-06-14.

This document defines the contracts that are locked, the changes that remain permitted,
and the requirements any future language layer must satisfy before it may inherit from
this master.

No downstream document — including any translation layer, any build script, or any
subsequent governance entry — may modify the frozen fields defined below without an
explicit entry in `DECISION_LOG.md` recording the change, its rationale, and its
governance authority.

---

## Frozen Corpus State

At the moment of freeze:

| Field | Value |
|-------|-------|
| Pages | 300 |
| Sitemap URLs (indexable) | 299 |
| Claims | 1336 (982 sourced, 354 internal-framework) |
| Sources | 27 (all in use) |
| Routes registry version | v2.6 |
| Claims registry version | v1.8 |
| Sources registry version | v0.3 |
| FIO/FIS version | v0.1 |
| Language | English (`en`) |
| Canonical base domain | `https://zonules.com` |
| Freeze date | 2026-06-14 |
| Validated by | `scripts/validate_all.py` — GOVERNANCE GATE: PASS |

---

## Frozen Contract Fields

The following fields are frozen. They establish the stable identity of each reference
unit. Translations must map to these fields without altering them.

### Per-Route Frozen Fields (`data/routes.json`)

| Field | Description | Example |
|-------|-------------|---------|
| `path` | Route slug. The English canonical path, which becomes the `x-default` hreflang reference. | `/zonules-of-zinn/` |
| `canonical` | Canonical URL. Must remain stable across all language layers. | `https://zonules.com/zonules-of-zinn/` |
| `fio_class` | FIO failure-class assignment. Cannot be reassigned without a governance entry and a version increment of the routes registry. | `FIO-01` |
| `fis_criterion` | FIS standard criterion pairing the FIO class. Cannot be changed without a corresponding governance entry. | `FIS-1` |
| `safety_class` | Safety classification: `medical-educational`, `educational`, `technical`, or `institutional`. Determines which validator checks apply. | `medical-educational` |
| `layer` | Reference layer: `L1`, `L2`, `L3`, or `cross`. | `L1` |
| `cluster` | Sub-cluster within the layer. | `lens-suspension` |
| `language` | Language code. English canonical is `en`. | `en` |

### Per-Term Frozen Fields (content markdown frontmatter)

| Field | Description |
|-------|-------------|
| `term_id` | Canonical identifier for the term. Frozen. Translations reference this ID without changing it. |
| `concept_id` | Concept identity across all language layers. Frozen. The same concept_id must appear in every language version of the page. |

### Canonical English Text Contracts (content markdown)

| Element | Contract |
|---------|----------|
| Canonical English title | The `seo_title` in `routes.json` and the `<h1>` in the published page. Frozen as the `hreflang x-default` reference title. |
| Canonical English definition | The opening definition paragraph. Frozen as the source-of-truth meaning all translations must preserve faithfully. |
| Internal framework wording | Zonules.com FIO/FIS framework language (sourced to SRC-004). The governing sentences are frozen: *"Zonules are not vision. They are what makes vision possible."* *"Focus is not a property of sight. It is a product of hidden structural tension."* *"Perception requires governance beneath visibility."* FIO and FIS class names and definitions (REFERENCE_ARCHITECTURE.md v0.1) are frozen. |
| Safety Notes core meaning | The Safety Notes section's essential meaning is frozen. No translation may weaken, soften, omit, or reframe safety language to reduce its protective effect. |
| Medical disclaimer language | The eye-care disclaimer — "consult a qualified eye-care professional" — must appear on all `medical-educational` pages in every language. The substance must not be weakened in translation. |
| "Detection is not diagnosis" language | This boundary statement — that AI-assisted detection is not equivalent to clinical diagnosis — must survive translation intact on all pages where it appears in English (including `ophthalmic-ai` and `medical-imaging-ai`). |
| Source attribution boundaries | Source citations must be preserved. See the Source Attribution Boundaries section below. |

### Registry-Level Frozen Fields

| Field | Description |
|-------|-------------|
| Claim IDs (`CLM-001`–`CLM-1336`) | Frozen. No claim may be renumbered. New claims must receive new sequential IDs starting at CLM-1337. |
| Source IDs (`SRC-001`–`SRC-027`) | Frozen. No source may be renumbered or reassigned to a different document. |
| Per-claim `sources` array | The source attribution of each claim is frozen. A sourced claim's `sources` array must not be emptied or reduced. |

---

## Source Attribution Boundaries

The following source-attribution rules are frozen as of this document:

1. **No claim may lose its source attribution.** A claim registered as `"status": "sourced"`
   must remain sourced; its `sources` array must not be emptied or reduced.

2. **No source ID may be reassigned** to a different publication, institution, or document.
   SRC-001 is Forrester et al. *The Eye.* It remains so.

3. **Translation may add source context** — for example, linking to a translated edition of
   a cited work — but must never remove the original English citation.

4. **Internal-framework claims** (`"status": "internal-framework"`, sourced to SRC-004)
   represent Zonules.com's Focus Integrity thesis interpretation. Their status may not be
   changed to `"sourced"` without a new registered source, and may not be changed to
   `"conceptual"` if they carry specific FIO/FIS class assertions.

5. **No new source may substitute for a registered source.** New sources extend coverage;
   they do not replace existing attributions.

---

## What May Change After Freeze

### Permitted Without Governance Entry

The following changes may be made to the English master without a DECISION_LOG.md entry,
provided they do not alter frozen field values:

- **Typo corrections** in prose text
- **Broken link fixes** (replacing a dead external URL with an equivalent live one)
- **Source record corrections** (fixing a bibliographic detail — publisher, year, edition —
  without changing the source's identity, scope, or ID)
- **Safety clarifications** (strengthening safety language — making it more protective, never
  less; no strength reduction is permitted even as a "permitted" change)
- **Metadata corrections** (fixing a misspelled `meta_description` that does not change SEO
  intent and does not alter frozen fields)
- **Translation mapping entries** (adding `hreflang_group`, `language`, or translation-mapping
  metadata fields to a route; these are additive, not mutations of existing fields)
- **Non-semantic wording cleanup** (rewording a sentence to improve clarity without changing
  its meaning, subject to the constraint that no safety or medical language is weakened)

### Not Permitted Without Explicit Governance Entry

The following changes require a `DECISION_LOG.md` entry — with date, rationale, and
governance authority — before they may be made:

| Prohibited change | Governance reason |
|-------------------|-------------------|
| Route slug changes (`path` field) | Breaks canonical URLs and all language hreflang mappings. |
| `term_id` or `concept_id` changes | Breaks multilingual concept identity. |
| FIO/FIS reassignment (`fio_class`, `fis_criterion`) | Changes the term's position in the focus-integrity system; affects all language layers. |
| Claim ID rewriting | Breaks claim traceability and cross-language attribution. |
| Source ID reassignment | Breaks attribution integrity across the entire corpus. |
| Weakening safety notes | Violates the medical-safety doctrine in `ASSET_THESIS.md`. |
| Weakening or removing medical disclaimers | Violates the medical-safety doctrine. |
| Removing source attribution from a claim | Violates the No Ungoverned Claims doctrine. |
| Translating content before mapping rules exist | Violates the No Partial Language Doctrine. |
| Adding pages to the English corpus beyond 300 | The canonical corpus is considered complete; additions require a governance entry. |

---

## Multilingual Readiness

The English canonical master is the **source of truth** for the Zonules.com multilingual
architecture. The following requirements govern every future language layer.

### English Master as Source of Truth

- Every translated page must trace directly to an English source page via matching
  `term_id`, `concept_id`, and `hreflang` mapping.
- No new term may be introduced in a secondary language without first being registered
  in the English canonical master (or in a governed English corpus extension with a
  DECISION_LOG.md entry).
- The English `path` and `canonical` URL become the `hreflang x-default` references for
  all language variants of that page.

### Route Mapping

- Each secondary language must map its routes one-to-one with English routes.
- No secondary-language route may exist without a corresponding English canonical route.
- Route slugs in secondary languages must follow the hreflang convention defined in the
  route registry at the time translation begins.

### Concept Identity

- `term_id` and `concept_id` are language-invariant identifiers. The same values appear
  in every language version of a page.
- Translations do not create new concepts; they localise existing ones.
- Concept identity is established by the English canonical master and must not be
  redefined in translation.

### FIO/FIS Identity

- The `fio_class` and `fis_criterion` assigned in English carry to every language version
  unchanged.
- A page classified `FIO-01 · FIS-1` in English is classified `FIO-01 · FIS-1` in
  French, German, Spanish, Chinese, Arabic, Japanese, and Russian.
- FIO class names and FIS criterion names may be translated into the target language but
  must remain semantically equivalent to the English definitions in
  `REFERENCE_ARCHITECTURE.md` v0.1.

### Claim and Source Traceability

- Each language's claim registry must reference the English claim IDs (`CLM-…`) as source
  identifiers, maintaining provenance traceability across languages.
- Source attributions (SRC-001 through SRC-027) carry into every language. A translated
  page may cite a translated edition of a source but must retain the original SRC-ID
  reference alongside it.
- No language layer may introduce a factual claim that has no equivalent in the English
  layer without a new registered claim and a governance entry.

### Safety Meaning

- All `safety_class` designations carry unchanged into every language.
- Medical disclaimers must be translated faithfully and must not be weakened, shortened
  to the point of losing protective meaning, or omitted.
- The "detection is not diagnosis" boundary statement must survive translation intact in
  every language where it appears in English.
- The eye-care professional consultation disclaimer must appear in full in every language
  on `medical-educational` pages.

### No Thin Translation Rule

A language is not launched when it is translated. A language is launched when it becomes
a complete governed reference layer.

A partial language layer — missing foundational navigation, missing core reference pages,
missing translated disclaimers, having unverified machine-translated text, or having
broken cross-language hreflang references — must not be made publicly indexable.

### No Automatic Uncontrolled Translation Rule

No page may be published in a secondary language using only machine translation without
human review of:

- Scientific and anatomical terminology
- Safety and medical disclaimer language
- FIO/FIS class name translations

Machine translation is permitted as a draft-production tool. Human review is required
before any page is classified as approved and made indexable.

### Official Future Language Order

Future language layers shall be developed and launched in the following governed order:

| Priority | Language | Code | Strategic position |
|----------|----------|------|--------------------|
| 1 | English | `en` | Canonical master — **frozen** |
| 2 | French | `fr` | Francophone scientific, medical, philosophical, and AI reference |
| 3 | German | `de` | Optics, ophthalmology, engineering, terminology precision |
| 4 | Spanish | `es` | Scientific accessibility across Spain, Latin America, medicine |
| 5 | Chinese | `zh` | AI, computer vision, optics, manufacturing, research ecosystem |
| 6 | Arabic | `ar` | MENA ophthalmology, AI, education, visual literacy |
| 7 | Japanese | `ja` | Precision optics, robotics, imaging systems, medical technology |
| 8 | Russian | `ru` | Scientific, mathematical, engineering, optical research |

No language outside this list may be added without a DECISION_LOG.md entry and a
version increment of the language policy.

---

## Freeze Enforcement

### Current Enforcement (Sprint 6F)

`scripts/validate_all.py` enforces the following freeze-related checks at every build:

- **Minimum count floor:** Route count must not fall below 300; claim count must not fall
  below 1336; source count must not fall below 27. This prevents silent deletion of
  registered corpus elements.
- **No orphaned pages:** Every page must remain linked (≥1 inbound, ≥3 outbound). Link-graph
  integrity from the frozen state is enforced.
- **No unsafe claims:** Every claim must remain sourced or classified.
- **No broken internal links:** All `required_internal_links` must resolve to registered routes.
- **Static-first security scan:** The validator detects `<script>` injection, API keys, and
  `http://` links in content and data files.
- **Acquisition surface discipline:** `/acquire/` must remain noindex and excluded from the
  sitemap.
- **Governance pages present:** `index.html`, `sitemap.xml`, `robots.txt`, `CNAME`,
  `.nojekyll` must exist at the repository root.
- **No GitHub Pages `/docs` publication:** `docs/index.html` must not exist (governance
  documents such as this freeze document may reside in `docs/`, but an `index.html` would
  trigger GitHub Pages to serve from `/docs/` instead of the root).

### Future Validator Requirements (Sprint 7A)

The following freeze checks are recommended for implementation before or during
Sprint 7A — Multilingual Architecture:

1. **Frozen field mutation detection.** Load `data/freeze-manifest.json` and verify that
   `path`, `canonical`, `fio_class`, `fis_criterion`, and `safety_class` match the frozen
   values for all 300 English routes. Any deviation raises a governance error.
2. **Claim source integrity check.** Verify that no claim's `sources` array has been emptied
   or reduced since the freeze state.
3. **Hreflang consistency check** (once secondary languages exist). Verify reciprocal
   `hreflang` references between English and each launched language layer; flag any
   asymmetric or missing pairs.

---

## Authority

This document is governed by `ASSET_THESIS.md`. Any conflict between this document and
`ASSET_THESIS.md` is resolved in favour of `ASSET_THESIS.md`.

This document is subordinate to:

1. `ASSET_THESIS.md`
2. `Sohadot/sovereign-asset-system/docs/FOUNDATION_DOCTRINE.md`

Any change to this document must be recorded in `DECISION_LOG.md` as an explicit
governance entry.

---

**Zonules.com · Sovereign Visual Reference System**
**Sohadot Portfolio · agent@sohadot.com**
**Sprint 6F — English Canonical Master Freeze — 2026-06-14**
