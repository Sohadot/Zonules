# DUE_DILIGENCE_INVENTORY.md

**Zonules.com — Acquisition-Readiness Inventory**
**Sohadot Portfolio · agent@sohadot.com**
**Version 0.1 — 2026-10-26**
**Governing documents:** `ASSET_THESIS.md` · `ACQUISITION_POSTURE.md`

---

## Status and Scope

This is a factual inventory of the components in this repository, the apparent basis on which each exists, and what would need independent verification before any transfer. It is **not a legal opinion**. Nothing here asserts ownership, licensing, or transferability beyond what the repository itself shows.

This file is public (the repository is public and the site is published from the repository root). It therefore contains **no pricing, negotiation posture, buyer names, or confidential assumptions**, and must never do so.

Status key: **Verified in repo** — checkable from repository contents · **Needs external verification** — depends on records outside the repository.

---

## Component Inventory

| Component | Source / ownership basis | Known licence | Transfer consideration | Status |
|---|---|---|---|---|
| Domain `zonules.com` | Registrant of record (outside repo). `CNAME` points GitHub Pages at the domain. | n/a | Registrar transfer under agreed terms; confirm registrant identity, expiry, and absence of liens or disputes. | Needs external verification |
| Governing documents (`ASSET_THESIS.md`, `REFERENCE_ARCHITECTURE.md`, `ACQUISITION_POSTURE.md`, `DECISION_LOG.md`, plans, `docs/`) | Written for the project. | No licence file in repository. | Copyright assignment by written agreement. | Verified in repo (authorship); rights need external verification |
| Reference corpus (`content/en/`, generated pages) | Original prose written for the project; describes scientific facts. | No licence file. | Expression is transferable by agreement; the underlying scientific facts and terminology are not ownable. | Verified in repo; rights need external verification |
| French pilot (100 pages) and Arabic RTL pilot (8 pages) | Translations produced for the project. | No licence file. | As above; confirm who produced each translation and on what terms. | Needs external verification |
| FIO / FIS / FIA / FIE (`data/focus-integrity-*.json`, `static/js/focus-integrity-engine.js`) | Original framework and code. | No licence file. | Transferable by agreement. The framework is a vocabulary and rule set; it does not confer rights over the problem areas it describes. | Verified in repo; rights need external verification |
| Registries (`data/routes.json`, `claims.json`, `sources.json`, `languages.json`, `translation-map.json`) | Original structured data. | No licence file. | Transferable by agreement. | Verified in repo |
| Build and validation scripts (`scripts/`) | Original code. Python standard library only; Node.js used only for the optional engine test. | No licence file. | Transferable by agreement. No third-party package licences to carry. | Verified in repo |
| Stylesheets and inline SVG illustrations | Original. No web fonts, images, or icon libraries are loaded. | No licence file. | Transferable by agreement. | Verified in repo |
| Cited works (27 external sources, `data/sources.json`) | Third-party textbooks, papers, institutional and standards-body material. | Owned by their publishers. | **Not transferable and not included.** The corpus cites them; it does not reproduce them. | Verified in repo (citation only) |
| Scientific terminology ("zonules", "zonules of Zinn", "ciliary zonule", etc.) | Public scientific vocabulary. | n/a | **Not ownable and not included.** | n/a |
| Third-party standards referenced (e.g. C2PA) | Owned by their bodies. | Their own terms. | Referenced only; Zonules.com is not affiliated with, and does not replace, any standard. | Verified in repo |
| Trademarks | None represented in the repository. | n/a | Any trademark position would need independent search and verification. | Needs external verification |
| Version history (Git) | 110 commits at the time of writing, authored under the owner's accounts and by AI coding agents (commits attributed to "Claude"; two with a Cursor co-author trailer). | n/a | Confirm that AI-assisted contributions were made at the owner's direction under the tools' terms of service. | Needs external verification |
| Hosting | GitHub Pages, published from the repository root. | GitHub terms. | Repository transfer or re-hosting; no runtime service, database, or credentials to migrate. | Verified in repo |

---

## Runtime and Data Posture (verified in repo)

- No third-party runtime scripts, analytics, fonts, or APIs on any published page.
- The engine runs client-side; no visitor input is transmitted or stored.
- No credentials or secrets are stored in the repository (validated by `scripts/validate_all.py`, which scans `content/` and `data/` for key patterns).

---

## Open Questions for a Transaction

1. Registrant-of-record details and domain history.
2. Written confirmation of authorship and rights for all prose, translations, and code, including AI-assisted work.
3. Whether a licence (or an explicit all-rights-reserved notice) should be added before any transfer, since the repository is public without one.
4. Treatment of public Git history, which includes earlier internal strategy language (see below).

---

## Disclosure Note: Public Governance Documents

Because the repository is public and served from its root, files such as `ASSET_THESIS.md`, `ASSET_INTELLIGENCE_FACTORY_PLAN.md`, `ACQUISITION_POSTURE.md`, and `DECISION_LOG.md` are readable by anyone (each returned HTTP 200 as `text/markdown` from `https://zonules.com/` on 2026-10-26), and earlier versions remain in Git history. They contain internal positioning language — the "Inevitability Principle" (`ASSET_THESIS.md`), and in `ASSET_INTELLIGENCE_FACTORY_PLAN.md` the "Banana Problem" analogy (which cites a six-million-dollar artwork sale and could be read as a price anchor), "moat" language, an income plan, and "The Loss Question" — but no prices for this asset, buyer names, or credentials.

Minimal forward-looking mitigations, none applied without owner decision:

- Keep all pricing, negotiation, and buyer-specific material out of this repository permanently.
- Optionally publish the site from a build directory or separate branch so that governance Markdown is no longer served on `zonules.com`. This changes the root-publication doctrine and needs a `DECISION_LOG.md` entry.
- Do not rewrite Git history; treat it as part of the inspectable governance record.
