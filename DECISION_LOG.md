# DECISION_LOG.md

**Zonules.com — Decision Log**
**Sohadot Portfolio · agent@sohadot.com**

This log is **append-only**. Entries are never edited or deleted; corrections are made by adding a new entry. Required by `Sohadot/sovereign-asset-system/docs/FOUNDATION_DOCTRINE.md` (No Silent Change). Every change to the thesis, ontology, standard, protocol, or a policy must appear here with a date and rationale.

---

## 2026-06-12 — Adopt Foundation Doctrine binding

- **Change:** Zonules.com declares binding to the Sovereign Asset System `FOUNDATION_DOCTRINE.md`.
- **Type:** Strengthens governance.
- **Rationale:** Establishes the constitutional layer — stricter-rule precedence, the ten non-negotiables, blocking quality gates, and this append-only log as inheritance requirements. The asset may be stricter than the methodology; never looser.
- **Affected:** repository-wide governance posture.

## 2026-06-12 — Ratify FIO v0.1 (Focus Integrity Ontology)

- **Change:** Establish the Focus Integrity Ontology v0.1 with five governed top-level classes (FIO-01 Suspension, FIO-02 Accommodation, FIO-03 Signal–Noise, FIO-04 Provenance, FIO-05 Interpretation), four entry criteria, and the structural→input→output grouping.
- **Type:** New governed structure (initial version).
- **Rationale:** The ontology is the classification layer required by the Intelligence Factory Doctrine. It maps every failure mode of focus across the three thesis layers and gives every future engine output a stable class to resolve to.
- **Affected:** `REFERENCE_ARCHITECTURE.md`, `data/focus-integrity-ontology.json`.

## 2026-06-12 — Ratify FIS v0.1 (Focus Integrity Standard)

- **Change:** Establish the Focus Integrity Standard v0.1 with five criteria (FIS-1…FIS-5), each the inverse of one FIO class, with per-layer applicability and four report states (`intact`, `at-risk`, `failed`, `not-applicable`).
- **Type:** New governed structure (initial version).
- **Rationale:** FIS defines what intact focus integrity is, against which the Focus Integrity Engine scores inputs. FIS-4 and FIS-5 are marked not-applicable at the anatomy layer to keep medical-safety discipline (no diagnostic phrasing).
- **Affected:** `REFERENCE_ARCHITECTURE.md`, `data/focus-integrity-standard.json`.

## 2026-06-12 — Establish data registries (sources, routes, claims) v0.1

- **Change:** Create the governed data registries required before any public page may exist: `data/sources.json` (4 classified sources), `data/routes.json` (route registry), `data/claims.json` (claim registry with sourced/conceptual/internal-framework status).
- **Type:** New governed infrastructure (initial version).
- **Rationale:** Foundation Doctrine forbids unregistered surfaces and ungoverned claims. No page may publish until its route, sources, and claims are registered and resolve.
- **Affected:** `data/sources.json`, `data/routes.json`, `data/claims.json`.

## 2026-06-12 — Publish first reference unit: Zonules of Zinn (FIO-01)

- **Change:** Approve the first complete governed reference unit, `content/en/terms/zonules-of-zinn.md`, as the approved template for all subsequent FIO class reference units. Maps the anatomical structure to FIO-01 / FIS-1 and to the perception and machine-vision layers as conceptual bridges.
- **Type:** New reference unit (approved); establishes the reference-unit format.
- **Rationale:** This is the anchor page of the asset — the literal instance of the suspension-layer thesis. Built to the Reference Unit Standard with all claims sourced or marked as internal framework. Cross-references validated: every claim resolves to a registered source; no unsourced scientific claim is published; medical-safety disclaimer present.
- **Affected:** `content/en/terms/zonules-of-zinn.md`, registries above.
- **Note:** Internal links to `/ciliary-body/`, `/crystalline-lens/`, `/lens-accommodation/`, `/lens-capsule/` are forward references to unbuilt pages. They are NOT yet live and must not enter navigation or sitemap until their target pages reach approved status (No Broken Structure non-negotiable).

## 2026-06-12 — Complete the lens-suspension cluster (3 reference units)

- **Change:** Add three governed reference units completing the FIO-01 lens-suspension cluster: `ciliary-body.md` (force source / actuator), `crystalline-lens.md` (focal element), and `lens-accommodation.md` (FIO-02 / FIS-2, range). Registries advanced to routes v0.2 and claims v0.2; sources unchanged (v0.1 covers all claims).
- **Type:** New reference units (approved).
- **Rationale:** These three were the forward references from the anchor page. Building them closes those internal links and makes the suspension cluster a complete, mutually-linked sub-graph rather than a single page with dangling pointers.
- **Affected:** `content/en/terms/{ciliary-body,crystalline-lens,lens-accommodation}.md`, `data/routes.json`, `data/claims.json`.

## 2026-06-12 — Gate defect found and fixed: broken link to /lens-capsule/

- **Defect:** The anchor page `zonules-of-zinn.md` contained a Markdown link to `/lens-capsule/`, which has no registered route — a violation of the No Broken Structure non-negotiable.
- **Resolution:** De-linked the reference to plain text marked *(reference unit forthcoming)*. The link will be restored when the lens-capsule reference unit is built and registered.
- **Detection:** Caught by the automated governance gate (broken-Markdown-link check) before publication, not after. This is the enforcement model working as intended.
- **Security scan:** No secrets/tokens in tracked content (policy prose excepted); no inline scripts, event handlers, `javascript:`, or external `http://` assets in `content/` or `data/`. Static-first and No-API posture intact.

## 2026-06-12 — Close the anatomy cluster: lens-capsule reference unit

- **Change:** Add `lens-capsule.md` (FIO-01 / FIS-1), the transmission interface of the suspension layer, and restore the live `/lens-capsule/` link on the anchor page that was de-linked in the previous entry. Registries advanced to routes v0.3 and claims v0.3 (CLM-018…CLM-021).
- **Type:** New reference unit (approved); resolves prior forward reference.
- **Rationale:** The capsule was the last dangling forward link. Building it closes the L1 lens-suspension cluster as a complete, fully reciprocal sub-graph and makes the mechanical chain explicit: ciliary body → zonules → capsule → lens → focus.
- **Verification:** Governance gate PASS — 5 pages, 21 claims, 0 broken links, 0 orphans, all sourced claims used and resolved, every page safety-classified. Security scan of `content/` and `data/` clean: no inline scripts, event handlers, `javascript:`, external `http://` assets, or secrets.
- **Affected:** `content/en/terms/lens-capsule.md`, `content/en/terms/zonules-of-zinn.md`, `data/routes.json`, `data/claims.json`.

## 2026-06-12 — Establish Layer 02 and Layer 03 anchors

- **Change:** Add the two layer anchors that extend the asset beyond anatomy: `visual-perception.md` (L2, the perceptual suspension system) and `machine-vision.md` (L3, the artificial instance, routing to FIO-03/04/05). Expand sources to v0.2 (perception science, vision science, computer vision, and a content-provenance standards body), claims to v0.4, routes to v0.4. Add per-page safety classes `educational` and `technical`.
- **Type:** New reference units (approved); first L2 and L3 pages.
- **Rationale:** These anchors carry the focus-integrity thesis across all three layers and create the human-vs-machine comparison surface that is the asset's most strategically valuable ground for buyer logic. Each anchor links to anatomy and to the other, making the cross-layer graph reciprocal.
- **Affected:** `content/en/terms/{visual-perception,machine-vision}.md`, `data/{sources,claims,routes}.json`.

## 2026-06-12 — Commit the governance gate as a repeatable script

- **Change:** Replace the ad-hoc inline validation with `scripts/validate_all.py`, a blocking quality gate that enforces ten checks derived from the Foundation Doctrine non-negotiables: claim/source resolution, registered routes, used-and-resolved claims, internal-link integrity, no orphans, canonical/metadata presence, class-aware safety classification, and a static-security scan of content and data.
- **Type:** New governance infrastructure (replaces manual checks).
- **Rationale:** The thesis names `scripts/validate_all.py` as a core command. Committing the gate makes enforcement reproducible and version-controlled rather than dependent on manual review. Current run: PASS (7 pages, 29 claims, 8 sources, layers L1/L2/L3; zero broken links, orphans, unsafe patterns, or unsourced claims).
- **Affected:** `scripts/validate_all.py`.

## 2026-06-12 — Build the Focus Integrity Engine (FIE v0.1)

- **Change:** Ship the Focus Integrity Engine — the operational surface that turns the asset from a reference system into a Category Intelligence Factory. It runs the Focus Integrity Assessment (FIA): the user picks a seeing system (eye / perception / machine) and rates each applicable FIS criterion; the engine deterministically inverts each non-intact criterion into its FIO class and links the finding to the governing reference units.
- **Form (doctrine-compliant):** Fully static, deterministic, client-side. The page is generated by `scripts/build_engine.py` from the governed JSON with all data embedded as inert script blocks — no fetch, no network, no API, no data collection, no third-party script. Single source of truth: `data/*.json`. Output: `static/engine/index.html` (self-contained, file://-inspectable).
- **Conceptual framing:** The engine embodies the thesis rather than decorating it — its governing line is "the same five questions decide focus integrity, whether the system is made of tissue, attention, or silicon." Each reading restates the hidden-suspension argument across the layer the user chose.
- **Safety & trust:** L1 readings carry the educational-reference medical guard; every reading ends with a local-only provenance line ("No input left your device"). A full no-JS fallback renders the five criteria, five classes, and all reference links, so the page is understandable without the engine (passes the interface test).
- **Governance:** New files `data/focus-integrity-engine.json` (FIE v0.1), `static/js/focus-integrity-engine.js`, `static/css/engine.css`, `scripts/build_engine.py`. The gate was extended: engine class-links must resolve to registered routes, the built page must be fresh (`build_engine.py --check`), and engine pages are validated by page-type-aware rules. Engine logic verified by simulation against FIO/FIS/FIE (correct inversion, correct reference resolution, determinism confirmed).
- **Verification:** Governance gate PASS — 8 pages across layers L1/L2/L3/cross; zero broken links, orphans, unsafe patterns, or unsourced claims.
- **Affected:** `data/focus-integrity-engine.json`, `data/routes.json`, `static/engine/index.html`, `static/js/focus-integrity-engine.js`, `static/css/engine.css`, `scripts/build_engine.py`, `scripts/validate_all.py`, `content/en/terms/{visual-perception,machine-vision}.md`.

## 2026-06-12 — Ship the suspension-reveal gateway interface (route /)

- **Change:** Build the homepage gateway (`/`) whose interface embodies the thesis rather than decorating it. The suspension-reveal interaction moves through three meaningful states: the lens apparently in focus (nothing visible holds it) → the hidden zonular fibers revealed → the fibers cut, the lens drifting and the focal target visibly blurring. The visitor feels the thesis: focus was never a property of the lens; it is produced by hidden tension.
- **Form (doctrine-compliant):** Fully static, generated by `scripts/build_gateway.py` from reviewed CSS/JS into a self-contained `static/gateway/index.html`. Inline SVG + CSS + a tiny vanilla JS interaction; zero external resources, no fonts, no trackers, no network. The SVG carries an `aria-label`; controls are real buttons with `aria-pressed`; the caption is `aria-live`; `prefers-reduced-motion` disables transitions.
- **Interface test (passed):** explains something (the suspension thesis); serves the asset thesis; the page is fully understandable without the interaction — a no-JS static triptych renders all three states with captions and the governing sentence is real heading text; does not break mobile (responsive); does not weaken SEO (semantic headings, internal link graph to the three layers and the engine); does not slow load (~21 KB, no requests); does not harm accessibility; raises trust rather than entertaining. SVG/CSS chosen over WebGL because it survives the test without 3D.
- **Governance:** New files `static/css/gateway.css`, `static/js/suspension-reveal.js`, `scripts/build_gateway.py`, `static/gateway/index.html`. Route `/` registered (page_type `gateway`). Gate generalized to validate generated pages (engine + gateway): internal links resolve, the gateway carries the governing sentence, build freshness enforced for both builders, and the root gateway is exempt from the orphan rule as the entry point.
- **Verification:** Governance gate PASS — 9 pages (L1/L2/L3/cross); zero broken links, orphans, unsafe patterns, or unsourced claims. Gateway HTML parses cleanly with no external resource references.
- **Affected:** `static/gateway/index.html`, `static/css/gateway.css`, `static/js/suspension-reveal.js`, `scripts/build_gateway.py`, `scripts/validate_all.py`, `data/routes.json`.

---

*Execution sequence (Factory Plan §11) is now complete: FIO/FIS ratified, anatomy cluster built, L2/L3 anchors established, Focus Integrity Engine shipped, suspension-reveal interface shipped, quality gate enforced. Next phase: deepen the L2/L3 clusters toward the 300-page corpus, add sitemap generation, and prepare the /acquire/ surface.*
