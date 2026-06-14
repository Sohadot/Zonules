# MULTILINGUAL ARCHITECTURE — Zonules.com
**Version:** 1.0  
**Status:** Architecture Defined (Sprint 7A)  
**Authority:** Subordinate to ASSET_THESIS.md and FOUNDATION_DOCTRINE.md  
**English master freeze reference:** docs/ENGLISH_MASTER_FREEZE.md  
**Effective date:** 2026-06-14  

---

## 1. Governing Principle

The English canonical master (`docs/ENGLISH_MASTER_FREEZE.md` v1.0, frozen 2026-06-14)
is the sole source of truth for all multilingual content. No translation may alter
the scientific meaning, clinical safety language, FIO/FIS classification, or claim
provenance established in the English master.

A language version of Zonules.com exists when — and only when — a complete, governed
reference layer exists for that language. A partially translated site is not a language
version; it is an incomplete asset. Incomplete assets are not published, not indexed,
and not linked from the English master.

This is the **No Partial Language Doctrine** (see also DECISION_LOG.md Sprint 6D).

---

## 2. Official Language Order

Expansion follows this priority sequence. Language codes are BCP 47.

| Priority | Language | Code | Direction | Script | Status |
|----------|----------|------|-----------|--------|--------|
| 1 | English | en | ltr | Latin | launched |
| 2 | French | fr | ltr | Latin | architecture_defined |
| 3 | German | de | ltr | Latin | architecture_defined |
| 4 | Spanish | es | ltr | Latin | architecture_defined |
| 5 | Chinese (Simplified) | zh | ltr | Han | architecture_defined |
| 6 | Arabic | ar | rtl | Arabic | architecture_defined |
| 7 | Japanese | ja | ltr | CJK | architecture_defined |
| 8 | Russian | ru | ltr | Cyrillic | architecture_defined |

**Status definitions:**

- `launched` — Complete governed layer published, indexed, hreflang active.
- `architecture_defined` — Language registered, URL schema defined, no content
  translated, not indexed, no hreflang emitted.
- `in_progress` — Translation in progress under governance; not indexed, no hreflang.
- `review` — Translation complete, governance review pending; not indexed.
- `ready_to_launch` — Governance approved; deployment pending.

Only a governance entry in DECISION_LOG.md (authorized per ASSET_THESIS.md) may
advance a language from `architecture_defined` to a subsequent status.

---

## 3. URL Strategy

### 3.1 English (Root — Permanent)

English content is served at the root. This is permanent and immutable.

```
https://zonules.com/                         ← root gateway
https://zonules.com/retina/                  ← L1 anchor term
https://zonules.com/zonules-of-zinn/         ← L1 reference unit
https://zonules.com/accommodation/           ← L2 reference unit
```

English paths are frozen in `docs/ENGLISH_MASTER_FREEZE.md`. No English path may
be moved to a language prefix.

### 3.2 Future Language Prefixes

Non-English languages are served under a two-letter BCP 47 language prefix.

```
https://zonules.com/fr/retine/               ← French equivalent of /retina/
https://zonules.com/fr/zonules-de-zinn/      ← French equivalent of /zonules-of-zinn/
https://zonules.com/de/netzhaut/             ← German equivalent of /retina/
```

URL slugs in non-English routes are translated into the target language. They are
NOT English slugs with a language prefix. Each non-English slug is governed by
`data/translation-map.json`.

### 3.3 Root Stability Guarantee

No multilingual expansion may:

- Change any English path
- Remove any English page from the sitemap
- Alter the English canonical URL of any page
- Add a language prefix to an existing English path

---

## 4. Hreflang Policy

### 4.1 Governing Rule

`hreflang` attributes are emitted only when a real, indexed, published translated
equivalent exists for the specific page.

**Prohibited:**

- hreflang pointing to a non-existent page
- hreflang pointing to a page that is not indexed
- hreflang pointing to a page under `architecture_defined` or `in_progress` status
- Blanket hreflang across all pages when only a subset are translated
- `hreflang="x-default"` pointing to a non-English page

**Required (when active):**

- `hreflang="en"` self-referencing tag on all English pages
- `hreflang="x-default"` pointing to the English canonical URL
- Reciprocal hreflang: if `/fr/retine/` declares hreflang for `/retina/`,
  then `/retina/` must declare hreflang for `/fr/retine/`

### 4.2 Current State (Sprint 7A)

**No hreflang is currently emitted.** The English master is the only launched
layer. Hreflang activation requires:

1. At minimum one complete, indexed translated page for a specific route.
2. A governance entry in DECISION_LOG.md authorizing the hreflang group.
3. A `hreflang_group` value set in `data/routes.json` for the relevant routes.

---

## 5. Route Mapping Model

Each English route maps to zero or more translated routes via
`data/translation-map.json`.

### 5.1 Mapping Schema

```json
{
  "english_path": "/retina/",
  "concept_id": "ZONE-RETINA",
  "term_id": "retina",
  "layer": "L1",
  "fio_class": "FIO-01",
  "fis_criterion": "FIS-1",
  "safety_class": "medical-educational",
  "claim_ids": ["CLM-001"],
  "source_ids": ["SRC-001"],
  "translations": {
    "fr": {
      "path": "/fr/retine/",
      "slug": "retine",
      "status": "not_started",
      "indexable": false,
      "hreflang_active": false
    }
  }
}
```

### 5.2 Language-Invariant Fields

These fields are set once from the English master and must not change per translation:

| Field | Frozen Source |
|-------|---------------|
| `concept_id` | Markdown frontmatter (English master) |
| `term_id` | Markdown frontmatter (English master) |
| `fio_class` | `data/routes.json` (English master) |
| `fis_criterion` | `data/routes.json` (English master) |
| `safety_class` | `data/routes.json` (English master) |
| `claim_ids` | `data/claims.json` (English master) |
| `source_ids` | `data/sources.json` (English master) |

### 5.3 Language-Variable Fields

These fields are set per translation:

| Field | Description |
|-------|-------------|
| `path` | Full URL path including language prefix |
| `slug` | Translated slug (not a copy of English) |
| `status` | not_started / in_progress / review / ready_to_launch / launched |
| `indexable` | false until status = launched and governance authorizes |
| `hreflang_active` | false until governance authorizes post-launch |

---

## 6. Translation Quality Requirements

### 6.1 Mandatory Preservation

Every translated page MUST preserve the following without alteration of meaning:

1. **FIO/FIS Classification** — The FIO class and FIS criterion apply to the
   concept, not the language. A page about FIO-01 (Suspension) in French is
   still FIO-01.

2. **Safety Notes meaning** — The clinical safety message (e.g., "detection is
   not diagnosis", "consult a qualified eye-care professional") must be
   translated accurately. Any translation that weakens, omits, or ambiguates
   safety meaning is prohibited.

3. **Medical disclaimer** — The medical disclaimer must appear in the translated
   language with equivalent clinical warning strength. No translation may omit
   the disclaimer.

4. **Claim traceability** — Claims cited in the English master (CLM-001 through
   CLM-1336) remain traceable in translated pages. The claim IDs are
   language-invariant identifiers.

5. **Source attribution** — Sources (SRC-001 through SRC-027) are cited from the
   English master. A translated page must attribute the same source material.
   Source IDs are language-invariant.

6. **"Detection is not diagnosis" principle** — This exact conceptual boundary
   must appear in every translated page that carries it in the English master.
   The phrasing may be translated; the boundary may not be weakened.

### 6.2 Prohibited in Translation

- Translating a medical disclaimer into weaker language
- Adding new claims not registered in `data/claims.json`
- Citing sources not registered in `data/sources.json`
- Reassigning a page to a different FIO class or FIS criterion
- Changing the `concept_id` or `term_id`
- Publishing a translated page before its status reaches `launched`
- Using machine translation without human governance review
- Adding monetization surfaces not present in the English master

### 6.3 AI Readability

Translated pages must maintain the same structured, unambiguous prose style as
the English master. Content must be parseable by AI agents (web crawlers, LLM
context retrievers) with equivalent fidelity to the English version. Translations
that introduce ambiguity not present in the English master are rejected.

---

## 7. No Partial Language Doctrine (Operational)

A language is considered **launched** only when ALL of the following are true:

1. Every page mapped in `data/translation-map.json` with `status != "not_started"`
   for that language has reached `status = "launched"`.
2. Every launched translated page has passed `scripts/validate_multilingual.py`.
3. Every launched translated page has a published HTML file at its root path.
4. The language entry in `data/languages.json` has been advanced to
   `status = "launched"` by a governance entry in DECISION_LOG.md.
5. Hreflang is activated only after all four conditions above are met.

Partial completion — even 299 of 300 pages — does not constitute a launched
language.

---

## 8. Governance and Change Protocol

Any change that advances a language beyond `architecture_defined` requires:

1. A new DECISION_LOG.md entry (append-only).
2. A re-run of `scripts/validate_all.py` and `scripts/validate_multilingual.py`.
3. A new commit on the active governance branch.

**Permitted without a governance entry:**

- Adding a new route mapping to `data/translation-map.json` for a route not
  yet mapped (all statuses default to `not_started`).
- Updating `status` from `not_started` to `in_progress` (does not affect
  indexability).
- Correcting a typo in a slug without altering meaning.

**Requires a governance entry:**

- Advancing any language from `architecture_defined` to a higher status.
- Activating hreflang for any page.
- Adding a new language to the official order.
- Changing the `concept_id` or `term_id` mapping for any route.
- Setting any translated route to `indexable: true`.

---

## 9. Validator Requirements

`scripts/validate_multilingual.py` enforces:

1. All language codes in `data/languages.json` are valid BCP 47 codes from the
   official order.
2. No translated route is `indexable: true` unless its language has
   `status = "launched"` in `languages.json`.
3. No `hreflang_active: true` unless the target page exists and is indexed.
4. All `fio_class` and `fis_criterion` values in `translation-map.json` match
   those in `routes.json`.
5. All `term_id` and `concept_id` values in `translation-map.json` are stable
   (not mutated from the English master).
6. `safety_class` is not weakened in any translation mapping.
7. All `source_ids` referenced in a mapping appear in `data/sources.json`.
8. All `claim_ids` referenced in a mapping appear in `data/claims.json`.

---

## 10. Authority Chain

```
ASSET_THESIS.md
  └── FOUNDATION_DOCTRINE.md
        └── docs/ENGLISH_MASTER_FREEZE.md (v1.0)
              └── docs/MULTILINGUAL_ARCHITECTURE.md (v1.0)  ← this document
                    ├── data/languages.json (v1.0)
                    ├── data/translation-map.json (v1.0)
                    └── scripts/validate_multilingual.py
```

No multilingual decision may contradict a higher authority in this chain.

---

*Zonules.com — Multilingual Architecture v1.0 — Sprint 7A — 2026-06-14*
