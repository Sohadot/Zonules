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

## 2026-06-12 — Adopt the "Ocular Depth / Controlled Luminosity" color system

- **Change:** Replace the near-black background across the gateway and engine with a conceptual palette. The background is no longer a void but the luminous medium light travels through inside the eye, lit by a single focal source near the top and fading into ocular depth. The palette carries the thesis through temperature: cool (teal/cyan/silver) = focus held and the suspension intact; warm (amber → clay) = the system failing. In the gateway, cutting the fibers shifts them from cool to warm; in the engine, readings move intact→at-risk→failed along the same cool→warm axis. The revealed zonular fibers are the most luminous element on screen — the hidden structure rendered as the most precious thing in the system.
- **Type:** Interface/design-system change (strengthens thesis embodiment).
- **Rationale:** Per request, the interface should be conceptual and let colour serve the story rather than default to black. Temperature now encodes the focus-integrity argument directly, satisfying the Interface Governance rule that every colour has a function.
- **Verification:** Both generated pages rebuilt and fresh. WCAG contrast checked: body text 14.9:1; all functional text pairs ≥ 3:1 (AA-large minimum), most ≥ 7:1. Governance gate PASS (9 pages; zero broken links, orphans, unsafe patterns, or unsourced claims).
- **Affected:** `static/css/gateway.css`, `static/css/engine.css`, `static/gateway/index.html`, `static/engine/index.html`.

## 2026-06-12 — Sitemap and robots generation from the registry

- **Change:** Add `scripts/generate_sitemap.py`, producing `static/sitemap.xml` and `static/robots.txt` derived exclusively from the route registry. A page enters the sitemap only if registered, approved, and indexable; priority is assigned by page type and lastmod from the review date. robots.txt allows indexing and points to the sitemap. Gate enforces freshness.
- **Type:** New SEO/archival infrastructure.
- **Rationale:** Keeps search visibility governed — the sitemap can never contain a draft, non-indexable, or unregistered surface. Validated as well-formed XML matching the approved-and-indexable route set exactly.
- **Affected:** `scripts/generate_sitemap.py`, `static/sitemap.xml`, `static/robots.txt`, `scripts/validate_all.py`.

## 2026-06-12 — Add the /acquire/ strategic acquisition surface

- **Change:** Codify `ACQUISITION_POSTURE.md` and build `/acquire/` (`scripts/build_acquire.py`) — a calm, institutional surface that shows the structure constituting the asset and the categories of strategic buyer, with one contact path. The surface is `noindex` and excluded from the sitemap, reached deliberately rather than via search to protect reference authority from any for-sale signal. A calm "Strategic acquisition" link from the gateway footer provides the inbound path.
- **Type:** New strategic surface (Quality Gate item 15) and new governed standard.
- **Rationale & enforcement:** The acquisition surface is where a reference asset can destroy its own authority by sounding like a listing. The gate now blocks publication if the surface contains urgency/marketplace phrases (buy now, act now, limited time, make an offer, auction, for sale, …), any price or valuation figure, or lacks noindex. Negative test confirmed the enforcement blocks violations rather than passing silently.
- **Affected:** `ACQUISITION_POSTURE.md`, `static/acquire/index.html`, `static/css/acquire.css`, `scripts/build_acquire.py`, `scripts/build_gateway.py`, `scripts/validate_all.py`, `data/routes.json`.

## 2026-06-12 — Deepen the L2 and L3 clusters (4 reference units)

- **Change:** Add four governed reference units that build out the perception and machine-vision clusters around their anchors: `selective-attention.md` (L2, FIO-01 — attention as the perceptual suspension) and `figure-ground.md` (L2, FIO-03 — perceptual signal/noise); `deepfake-detection.md` (L3, FIO-04 — provenance as inference) and `image-provenance.md` (L3, FIO-04 — provenance as record). Claims registry to v0.5 (CLM-030…CLM-045). The two anchors now link down to their cluster children, and the Focus Integrity Engine's class-links for FIO-03 and FIO-04 resolve to these specialized units, deepening factory output.
- **Type:** New reference units (approved); cluster build toward the 300-page corpus.
- **Rationale:** Each unit extends the focus-integrity thesis into a concrete sub-problem while staying on-story: attention is the mind's suspension layer; figure-ground is perceptual signal separation; deepfake detection and image provenance are the two halves of the provenance failure class — inference versus record. The provenance pair carries the strategically newest claim: a failure mode biology never had to solve.
- **Verification:** Governance gate PASS — 14 pages, 45 claims, 8 sources; 13 indexable URLs in the sitemap; zero broken links, orphans, unsafe patterns, or unsourced claims.
- **Affected:** `content/en/terms/{selective-attention,figure-ground,deepfake-detection,image-provenance}.md`, `content/en/terms/{visual-perception,machine-vision}.md`, `data/{claims,routes,focus-integrity-engine}.json`, regenerated engine and sitemap.

## 2026-06-12 — Render the corpus to citable HTML + governance and glossary surfaces

- **Change:** Add `scripts/build_site.py`, a pure-stdlib renderer that turns every governed markdown unit into a structured, servable HTML page in `site/`. Each page carries breadcrumb navigation, a generated **References & claim provenance** section built from the claim and source registries (inline authoring markers are stripped; provenance is regenerated and classified), and **JSON-LD structured data** (DefinedTerm + isPartOf + BreadcrumbList + citations) so AI agents, search engines, and citation tools can read the asset reliably. Add the governance surfaces `/methodology/` and `/source-policy/`, and a `/glossary/` hub generated directly from the registry (its links can never break). Add `static/css/reference.css` as the shared reference styling.
- **Why this is the keystone:** Until now the reference units were governed content but not servable pages. This closes that gap — the corpus is now real, inspectable HTML with the trust, SEO, and agent-legibility layers the asset's strategy depends on: stable URLs, structured data, visible provenance, strong internal links, and a governance record a reader or agent can examine.
- **Second language layer, begun correctly:** Add `data/languages.json` registering French (`fr`) as `blocked` — the architecture is reserved but the layer is excluded from all public output (sitemap, hreflang, indexing) until every launch requirement is met. The gate now enforces the No Partial Language Doctrine: a route in a non-launched layer may not be indexable.
- **Verification:** Renderer accepts only the constrained markdown our content uses; no third-party code, no network. Rendered pages validated: well-formed HTML, valid JSON-LD, no leftover claim markers, all internal links resolve, no inline scripts or external resources. Governance gate PASS — 17 routes, 14 rendered pages, 16 indexable URLs; zero broken links, orphans, unsafe patterns, or unsourced claims. All five builders report fresh.
- **Affected:** `scripts/build_site.py`, `static/css/reference.css`, `content/en/pages/{methodology,source-policy}.md`, `data/{routes,languages}.json`, `scripts/validate_all.py`, `scripts/generate_sitemap.py`, rendered `site/`.

## 2026-06-12 — French nucleus drafted, then deferred to keep effort focused

- **Change:** A French anatomy reference unit was drafted, then removed (unregistered, uncommitted) at the portfolio owner's direction to complete the English layer fully before opening a second language. No French artifacts remain; `data/languages.json` keeps `fr` registered as `blocked`.
- **Rationale:** Avoid scattering effort across languages while the English layer is still being completed. French resumes as a complete, reviewed layer once English is done.

## 2026-06-12 — Publish the Focus Integrity Ontology hub (the governing spine)

- **Change:** Add `/focus-integrity-ontology/`, a generated reference surface that makes the governing ontology and standard browsable and citable for the first time. It is generated by `build_site.py` directly from `focus-integrity-ontology.json` and `focus-integrity-standard.json` — single source of truth — listing the five FIS criteria (what intact focus is) and the five FIO failure classes (each the inverse of one criterion, with its three layer mappings and links to the reference units that carry it). Carries `DefinedTermSet` JSON-LD.
- **Type:** New generated reference surface (closes a structural gap); strengthens internal linking.
- **Rationale:** Until now the ontology and standard existed only inside the engine and the data files. This hub gives the system its spine as a public, indexable, agent-legible page, and binds every reference unit to its failure class. Every rendered term and policy page now links to the ontology in its footer; the glossary and methodology link to it; it links out to the units and the engine — a dense, governed internal graph.
- **Verification:** Generated from governed data with no new claims. Validated: valid JSON-LD, all five classes and criteria present, each class links to its units, no broken links, present in the sitemap, HTML parses cleanly. Governance gate PASS — 18 routes, 15 rendered pages, 17 indexable URLs; zero broken links, orphans, unsafe patterns, or unsourced claims.
- **Affected:** `scripts/build_site.py`, `static/css/reference.css`, `content/en/pages/methodology.md`, `data/routes.json`, `scripts/validate_all.py`, regenerated `site/` and sitemap.

## 2026-06-12 — English corpus expansion: 8 reference units + 2 governance pages

- **Change:** Add 10 new governed English pages, bringing the corpus to 28 routes and 74 registered claims:
  - **L1 Anatomy — optical pathway cluster (4 units):** `cornea.md` (FIO-03 — signal entry surface), `retina.md` (FIO-05 — interpretation surface), `photoreceptors.md` (FIO-03 — signal-noise boundary), `optic-nerve.md` (FIO-01 — structural conduit). These units complete a second L1 cluster covering the downstream optical and neural pathway, complementing the lens-suspension cluster.
  - **L2 Perception — perceptual clarity cluster (2 units):** `perceptual-constancy.md` (FIO-05 — stable interpretation across conditions) and `gestalt-principles.md` (FIO-03 — grammar of perceptual signal separation). These units deepen the perception layer around the existing `visual-perception`, `selective-attention`, and `figure-ground` anchors.
  - **L3 Machine Vision (2 units):** `computer-vision.md` (FIO-05 — machine layer where all five FIO classes can occur) and `image-classification.md` (FIO-05 — the foundational interpretation task). These units deepen the machine-perception cluster and make the full FIO map explicit at Layer 03.
  - **Governance surfaces (2 pages):** `/editorial-policy/` (entry rules, maintenance, removal criteria) and `/medical-disclaimer/` (educational-only scope statement). These close the governance trust layer.
- **Type:** English corpus growth; governance layer closure; routes registry to v0.9, claims to v0.6 (29 new claims CLM-046…CLM-074, 8 sources unchanged).
- **Rationale:** Per the explicit direction to complete the English layer with strict governance before any other language. Each unit earns its position: every scientific claim resolves to a registered source (SRC-001…SRC-008); every framework claim is marked as internal framework language; every medical-educational page carries its Safety Notes section; every page passes the full quality gate. The FIE class_links are expanded (FIO-01, FIO-03, FIO-05) so engine readings now surface these units as reference destinations.
- **Verification:** Governance gate PASS — 28 pages, 74 claims, 8 sources, layers L1/L2/L3/cross; 27 indexable URLs in sitemap; zero broken links, orphans, unsafe patterns, or unsourced claims. All five builders fresh.
- **Affected:** `content/en/terms/{cornea,retina,photoreceptors,optic-nerve,perceptual-constancy,gestalt-principles,computer-vision,image-classification}.md`, `content/en/pages/{editorial-policy,medical-disclaimer,methodology,source-policy}.md`, `data/{claims,routes,focus-integrity-engine}.json`, regenerated `site/` and sitemap.

## 2026-06-12 — English corpus second batch: 8 reference units

- **Change:** Add 8 more governed English reference units, bringing the corpus to 36 routes and 103 registered claims:
  - **L1 Anatomy — optical pathway cluster extended (3 units):** `iris.md` (FIO-02 — aperture and input accommodation), `vitreous-humor.md` (FIO-01 — structural medium preserving focal geometry), `macula.md` (FIO-03 — precision zone, the anatomical target of the entire optical system). These units complete the L1 optical-pathway cluster and make the full anatomical chain explicit from signal entry (cornea) through the structural medium (vitreous) to the precision landing zone (macula).
  - **L2 Perception — perceptual clarity cluster extended (3 units):** `depth-perception.md` (FIO-05 — 3D construction from 2D signal), `inattentional-blindness.md` (FIO-04 — first L2 provenance failure unit; the gorilla problem), `visual-working-memory.md` (FIO-02 — limited active holding capacity; the perceptual accommodation layer). These units complete all five FIO classes at the perception layer.
  - **L3 Machine Vision (2 units):** `object-detection.md` (FIO-05 — dual interpretation: what and where) and `adversarial-examples.md` (FIO-03 — structured noise that reveals mismatched signal boundaries). These units extend the L3 cluster and make the adversarial robustness problem legible within the focus-integrity frame.
- **Type:** English corpus growth; routes registry to v1.0, claims to v0.7 (29 new claims CLM-075…CLM-103).
- **Structural note:** All five FIO classes are now instantiated in all three layers — every cell of the 3×5 matrix (layers × failure classes) has at least one reference unit. This is the structural milestone of the corpus.
- **Rationale:** Each unit earns its position on thesis-relevance: the iris and vitreous complete the anatomical chain; working memory and inattentional blindness explain what happens at the perceptual boundary when focus fails to record; adversarial examples make the machine signal-noise problem concrete and strategically timely. FIE class_links updated across all five FIO classes.
- **Verification:** Governance gate PASS — 36 pages, 103 claims, 8 sources, layers L1/L2/L3/cross; 35 indexable URLs; zero broken links, orphans, unsafe patterns, or unsourced claims. All five builders fresh.
- **Affected:** `content/en/terms/{iris,vitreous-humor,macula,depth-perception,inattentional-blindness,visual-working-memory,object-detection,adversarial-examples}.md`, `data/{claims,routes,focus-integrity-engine}.json`, regenerated `site/` and sitemap.

## 2026-06-12 — English density pass: 8 units, every matrix cell now has a real unit

- **Change:** Add 8 reference units that deepen thin cells and fill the two cells that previously existed only as engine class-links rather than reference units. Corpus to 44 routes and 132 registered claims:
  - **L1 Anatomy (3 units):** `aqueous-humor.md` (FIO-01 — maintenance fluid sustaining optical geometry), `visual-cortex.md` (FIO-05 — the cortical terminus where interpretation begins; deepens the previously single-unit L1 FIO-05 cell), `pupillary-reflex.md` (FIO-02 — involuntary accommodation, the consensual light-reflex arc).
  - **L2 Perception (3 units):** `sustained-attention.md` (FIO-01 — the temporal dimension of perceptual suspension; the vigilance decrement), `change-blindness.md` (FIO-04 — provenance failure across time, paired with inattentional blindness), `visual-saliency.md` (FIO-03 — the bottom-up signal-prioritization stage; a genuine functional bridge to machine vision).
  - **L3 Machine Vision (2 units, both filling empty cells):** `model-calibration.md` (FIO-01 — the suspension system of machine vision; spatial reference frame that drifts) and `domain-shift.md` (FIO-02 — the accommodation failure of machine vision; the trained-envelope boundary). These were the last two empty cells of the 3×5 matrix.
- **Milestone:** Every cell of the 3 layers × 5 FIO classes matrix now contains at least one governed reference unit, with the structural and machine layers reaching parity. The thesis is now demonstrable, not asserted, across the entire matrix.
- **Type:** English corpus density pass; routes registry to v1.1, claims to v0.8 (29 new claims CLM-104…CLM-132).
- **Gate defects found and fixed before publication:** (1) `/visual-cortex/` Safety Notes omitted the exact required eye-care disclaimer phrase — corrected. (2) Four new units (`aqueous-humor`, `visual-cortex`, `pupillary-reflex`, `change-blindness`) were orphaned (linked out but no inbound link). Resolved by adding genuine reciprocal links in the natural parent units (`ciliary-body`→aqueous-humor, `optic-nerve`→visual-cortex, `iris`→pupillary-reflex, `inattentional-blindness`→change-blindness) in both the route registry and the rendered Related Terms, keeping the internal graph truly reciprocal rather than gate-satisfying. The gate caught both before publication — enforcement working as intended.
- **Verification:** Governance gate PASS — 44 pages, 132 claims, 8 sources, layers L1/L2/L3/cross; 43 indexable URLs; zero broken links, orphans, unsafe patterns, or unsourced claims. All five builders fresh.
- **Affected:** `content/en/terms/{aqueous-humor,visual-cortex,pupillary-reflex,sustained-attention,change-blindness,visual-saliency,model-calibration,domain-shift}.md`, `content/en/terms/{ciliary-body,optic-nerve,iris,inattentional-blindness}.md`, `data/{claims,routes,focus-integrity-engine}.json`, regenerated `site/` and sitemap.

## 2026-06-13 — Sprint 2: English corpus expansion to 68 pages, 223 claims, 67 sitemap URLs

- **Change:** Complete the Sprint 2 English corpus expansion. Add 24 new governed reference units across all three layers, advancing the corpus from 44 to 68 routes and claims from 159 to 223:
  - **L1 Anatomy — optical-pathway extended cluster (8 units):** `fovea-centralis.md` (FIO-03 — the anatomical zero-point of focus integrity; TRM-045), `optic-chiasm.md` (FIO-01 — structural routing for binocular signal integration; TRM-046), `optic-tract.md` (FIO-01 — non-redundant conduit from chiasm to LGN; TRM-047), `lateral-geniculate-nucleus.md` (FIO-01 — thalamic relay and active gating station; TRM-048), `binocular-vision.md` (FIO-05 — depth construction from disparity; TRM-049), `oculomotor-system.md` (FIO-02 — gaze accommodation envelope; TRM-050), `sclera.md` (FIO-01 — the geometric shell of the optical system; TRM-051), `choroid.md` (FIO-01 — metabolic suspension of phototransduction; TRM-052). These eight units complete the L1 optical-pathway cluster and establish a fully governed anatomical chain from signal entry through transmission, relay, and cortical reception.
  - **L2 Perception — perceptual-clarity cluster extended (8 units):** `pattern-recognition.md` (FIO-05 — template matching as the primary site of interpretation failure; TRM-053), `visual-inference.md` (FIO-05 — expectation-driven inference that can override signal fidelity; TRM-054), `perceptual-load.md` (FIO-02 — attentional aperture as accommodation mechanism; TRM-055), `top-down-processing.md` (FIO-05 — prior knowledge as systematic interpretation distorter; TRM-056), `attention-capture.md` (FIO-03 — salient noise competing with signal for attentional resources; TRM-057), `perceptual-error.md` (FIO-05 — the observable output of interpretation failure; TRM-058), `signal-ambiguity.md` (FIO-03 — signal definition insufficient for stable read; TRM-059), `visual-scene-parsing.md` (FIO-05 — meaning assignment as interpretation-layer risk; TRM-060). These eight units complete the L2 perceptual-clarity cluster.
  - **L3 Machine Vision — machine-perception cluster extended (8 units):** `optical-flow.md` (FIO-01 — temporal coherence broken by the aperture problem; TRM-061), `scene-understanding.md` (FIO-05 — integration failure persisting despite per-component accuracy; TRM-062), `synthetic-media.md` (FIO-04 — appearance-origin divorce requiring an independent provenance chain; TRM-063), `visual-grounding.md` (FIO-05 — compositional interpretation gap between language and image; TRM-064), `semantic-segmentation.md` (FIO-05 — silent out-of-vocabulary failure on every pixel; TRM-065), `ophthalmic-ai.md` (FIO-05 — clinical consequence of interpretation failure in retinal diagnosis; TRM-066), `medical-imaging-ai.md` (FIO-05 — benchmark-to-deployment gap as interpretation failure; TRM-067), `neural-network-interpretability.md` (FIO-05 — explanation of models whose correct outputs can be reached for incorrect reasons; TRM-068). These eight units complete the L3 machine-perception cluster.
- **Registry advances:**
  - `data/routes.json` → v1.4 (64 routes)
  - `data/claims.json` → v0.8 (223 claims; CLM-133…CLM-159 for L1 Sprint 2 pages, CLM-160…CLM-191 for L2 pages, CLM-192…CLM-223 for L3 pages)
  - `static/sitemap.xml` → 67 indexable URLs (43 pre-Sprint 2 + 24 new; /acquire/ excluded per governance)
- **Security and governance constraints enforced throughout:**
  - No newsletter, paid surfaces, directory, WebGL, complex animations, new tools, or second languages published.
  - /acquire/ page remains noindex, excluded from sitemap, zero for-sale/buy-now/price language.
  - Every scientific claim sourced to SRC-001…SRC-008; every framework claim marked internal-framework.
  - Every new page registered in routes.json before publication; no orphans.
  - Static-first maintained: no API, no network calls, no data collection, no third-party scripts.
- **Structural milestone:** The L1 optical-pathway cluster is now fully governed from cornea through fovea, with the entire visual pathway (chiasm → tract → LGN → cortex) documented as FIO-01 suspension elements. The L2 perceptual-clarity cluster is complete across all five FIO classes. The L3 machine-perception cluster extends the thesis into clinical and applied AI domains (ophthalmic AI, medical imaging AI, interpretability).
- **Type:** Sprint 2 English corpus expansion; routes v1.2→v1.4, claims v0.6→v0.8, TRM-045…TRM-068.
- **Affected:** `site/{fovea-centralis,optic-chiasm,optic-tract,lateral-geniculate-nucleus,binocular-vision,oculomotor-system,sclera,choroid,pattern-recognition,visual-inference,perceptual-load,top-down-processing,attention-capture,perceptual-error,signal-ambiguity,visual-scene-parsing,optical-flow,scene-understanding,synthetic-media,visual-grounding,semantic-segmentation,ophthalmic-ai,medical-imaging-ai,neural-network-interpretability}/index.html`, `data/{routes,claims}.json`, `static/sitemap.xml`.

## 2026-06-13 — Sprint 3: English corpus expansion to 101 pages, 355 claims, 100 sitemap URLs

- **Change:** Complete the Sprint 3 English canonical corpus expansion in three governed batches, advancing the corpus from 68 to 101 routes (92 reference units across L1/L2/L3 plus 9 cross/governance pages) and claims from 223 to 355. No multilingual pages; English only.
  - **Sprint 3A — Anatomy completion (11 units; TRM-069…TRM-079):** `retinal-ganglion-cells.md` (FIO-05 — the retina's output-encoding gateway), `blind-spot.md` (FIO-04 — a provenance gap filled without signal), `saccades.md` (FIO-02), `smooth-pursuit.md` (FIO-02), `extraocular-muscles.md` (FIO-02 — the gaze actuators), `optic-radiations.md` (FIO-01 — LGN-to-cortex suspension pathway), `retinal-pigment-epithelium.md` (FIO-01 — photoreceptor maintenance layer), `conjunctiva.md` (FIO-03), `trabecular-meshwork.md` (FIO-01 — intraocular-pressure regulation), `fixation.md` (FIO-01 — active gaze stabilization), `tear-film.md` (FIO-03 — the first optical surface).
  - **Sprint 3B — Perception expansion (11 units; TRM-080…TRM-090):** `contrast-sensitivity.md` (FIO-03), `visual-acuity.md` (FIO-03), `motion-perception.md` (FIO-05), `color-perception.md` (FIO-05), `visual-masking.md` (FIO-03), `visual-search.md` (FIO-01), `apparent-motion.md` (FIO-05), `binding-problem.md` (FIO-05), `bistable-perception.md` (FIO-03), `perceptual-priming.md` (FIO-05), `visual-illusions.md` (FIO-05).
  - **Sprint 3C — Technology expansion (11 units; TRM-091…TRM-101):** `vision-language-models.md` (FIO-05 — grounding failure across modalities), `pose-estimation.md` (FIO-05), `depth-estimation.md` (FIO-05 — the machine instance of depth perception), `visual-slam.md` (FIO-01 — stable spatial frame under motion), `feature-extraction.md` (FIO-03), `transfer-learning.md` (FIO-02), `out-of-distribution-detection.md` (FIO-04 — input-provenance check), `visual-tracking.md` (FIO-01 — identity held across frames), `data-augmentation.md` (FIO-02), `image-registration.md` (FIO-01), `scene-graph-generation.md` (FIO-05 — structured meaning from detected parts).
- **Registry advances:**
  - `data/routes.json` → v1.7 (101 routes; v1.5 after 3A, v1.6 after 3B, v1.7 after 3C)
  - `data/claims.json` → v0.9 (355 claims; CLM-224…CLM-267 for 3A, CLM-268…CLM-311 for 3B, CLM-312…CLM-355 for 3C; each unit carries 3 sourced + 1 internal-framework claim)
  - `static/sitemap.xml` → 100 indexable URLs (101 routes − 1 for noindex /acquire/)
- **Layer distribution (reference units):** L1 = 34, L2 = 30, L3 = 28.
- **Orphan policy:** Every new page is reachable via an inbound `required_internal_links` entry from a sibling reference unit, with matching rendered Related Terms. No existing pages were modified; the internal graph is reciprocal within each batch and connects to existing anchor units. Gate reported orphans=0 after each batch.
- **Security and governance constraints enforced throughout:**
  - No newsletter, paid surfaces, directory, WebGL, complex animations, new tools, or second languages published.
  - /acquire/ remains noindex and excluded from the sitemap; sitemap scan shows zero acquire entries.
  - Every scientific claim sourced to SRC-001…SRC-008; every framework claim marked internal-framework (SRC-004).
  - Every page registered in routes.json before publication; no phantom surfaces.
  - Static-first maintained: no API, no network calls, no data collection, no third-party scripts.
- **Verification:** Official audit sequence run — `git status` (clean) → `validate_all.py` (PASS) → `generate_sitemap.py` (100 urls) → `validate_all.py` (PASS), idempotent. Final gate: 101 pages, 355 claims, 8 sources, layers L1/L2/L3/cross; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Sitemap reconciliation: 100 URLs, zero unmapped to a route.
- **Type:** Sprint 3 English corpus expansion; routes v1.4→v1.7, claims v0.8→v0.9, TRM-069…TRM-101.
- **Affected:** `content/en/terms/*.md` (33 new units), `data/{routes,claims}.json`, regenerated `site/` and `static/{sitemap.xml,robots.txt}`.

## 2026-06-13 — Sprint 3D: merge conflict resolution and final gate

- **Change:** Resolve GitHub merge conflicts between `main` (post–Sprint 2 governance restore, PR #10) and the Sprint 3 English corpus branch (`claude/zonules-corpus-expansion-7uieq7`). Conflicts were in `data/routes.json`, `site/focus-integrity-ontology/index.html`, `site/glossary/index.html`, and `static/sitemap.xml`.
- **Resolution:** Preserve the full Sprint 3 registry — 101 routes, 355 claims, all 33 Sprint 3A/3B/3C reference units, and the Sprint 3 completion entry above. Take the Sprint 3 route registry as source of truth for the 33 new pages appended after Sprint 2's last entry. Regenerate all generated surfaces from governed data via `build_site.py` and `generate_sitemap.py` rather than hand-merging stale HTML or sitemap fragments.
- **Conflict rationale:** `main` had merged the Sprint 2 governance-restore commit independently while the Sprint 3 branch continued from the same base; auto-merge stopped at the route-registry tail and at generated pages whose content diverged when Sprint 3 expanded the glossary, ontology hub, and sitemap. Append-only `DECISION_LOG.md` merged cleanly; no prior entries removed.
- **Verification:** Official final-gate sequence — `generate_sitemap.py` (100 indexable URLs; `/acquire/` excluded) → `validate_all.py` (PASS) → idempotent re-run (PASS). Confirmed: 101 governed pages, 355 registered claims, 100 intentional sitemap URLs, broken_links=0, orphans=0, unsourced_claims=0, unsafe=0; no draft pages in sitemap; static-first posture intact.
- **Type:** Merge conflict resolution; governance gate pass.
- **Affected:** `data/routes.json`, regenerated `site/` (glossary, ontology hub, 33 new term pages, shared outputs), `static/{sitemap.xml,robots.txt}`.
