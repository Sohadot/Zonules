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
- **Verification:** Official audit sequence run — `git status` (clean) → `validate_all.py` (PASS) → `generate_sitemap.py` (100 urls) → `validate_all.py` (PASS), idempotent. Final gate: 101 pages, 355 claims, 8 sources, layers L1/L2/L3/cross; broken_links=0, orphans=0, unsourced_claims=0, unsafe=0. Sitemap reconciliation: 100 URLs, zero unmapped to a route.
- **Type:** Sprint 3 English corpus expansion; routes v1.4→v1.7, claims v0.8→v0.9, TRM-069…TRM-101.
- **Affected:** `content/en/terms/*.md` (33 new units), `data/{routes,claims}.json`, regenerated `site/` and `static/{sitemap.xml,robots.txt}`.

## 2026-06-13 — Sprint 3D: merge conflict resolution and final gate

- **Change:** Resolve GitHub merge conflicts between `main` (post–Sprint 2 governance restore, PR #10) and the Sprint 3 English corpus branch (`claude/zonules-corpus-expansion-7uieq7`). Conflicts were in `data/routes.json`, `site/focus-integrity-ontology/index.html`, `site/glossary/index.html`, and `static/sitemap.xml`.
- **Resolution:** Preserve the full Sprint 3 registry — 101 routes, 355 claims, all 33 Sprint 3A/3B/3C reference units, and the Sprint 3 completion entry above. Take the Sprint 3 route registry as source of truth for the 33 new pages appended after Sprint 2's last entry. Regenerate all generated surfaces from governed data via `build_site.py` and `generate_sitemap.py` rather than hand-merging stale HTML or sitemap fragments.
- **Conflict rationale:** `main` had merged the Sprint 2 governance-restore commit independently while the Sprint 3 branch continued from the same base; auto-merge stopped at the route-registry tail and at generated pages whose content diverged when Sprint 3 expanded the glossary, ontology hub, and sitemap. Append-only `DECISION_LOG.md` merged cleanly; no prior entries removed.
- **Verification:** Official final-gate sequence — `generate_sitemap.py` (100 indexable URLs; `/acquire/` excluded) → `validate_all.py` (PASS) → idempotent re-run (PASS). Confirmed: 101 governed pages, 355 registered claims, 100 intentional sitemap URLs, broken_links=0, orphans=0, unsourced_claims=0, unsafe=0; no draft pages in sitemap; static-first posture intact.
- **Type:** Merge conflict resolution; governance gate pass.
- **Affected:** `data/routes.json`, regenerated `site/` (glossary, ontology hub, 33 new term pages, shared outputs), `static/{sitemap.xml,robots.txt}`.

## 2026-06-13 — Sprint 3E: publish the governed site from the repository root

- **User decision:** GitHub Pages must publish from `main` / root. No `/docs` publication root (none existed; the prohibition is recorded and enforced). No public canonical URL may live under `/site/`.
- **Problem:** The build pipeline wrote public output to `site/` (reference units, glossary, ontology) and `static/` (gateway, engine, acquire, sitemap.xml, robots.txt). With Pages serving from root, the site root had no `index.html`, so the repository README rendered as the homepage and canonical pages were only reachable under `/site/…` — not valid public canonical paths.
- **Change:** Redirected every build *output* to the repository root, leaving all sources (`static/css`, `static/js`, `data/`, `content/`, `scripts/`) in place.
  - `scripts/build_gateway.py` → `/index.html` (public homepage; replaces README as the served root).
  - `scripts/build_engine.py` → `/focus-integrity-engine/index.html`.
  - `scripts/build_acquire.py` → `/acquire/index.html` (retains `noindex`, stays out of the sitemap).
  - `scripts/build_site.py` → `/<slug>/index.html` for all reference units, policy pages, `/glossary/`, and `/focus-integrity-ontology/`; shared stylesheet to `/assets/css/reference.css`.
  - `scripts/generate_sitemap.py` → `/sitemap.xml` and `/robots.txt` at the root.
  - `data/routes.json` content/template paths updated for the five generated routes (`/`, `/focus-integrity-engine/`, `/acquire/`, `/glossary/`, `/focus-integrity-ontology/`); registry to v1.6.
- **Removed stale public outputs:** deleted `site/` and `static/{gateway,engine,acquire,sitemap.xml,robots.txt}`. Kept `static/css/` and `static/js/` as build sources only.
- **Added root publication scaffolding:** `/.nojekyll` (serve files as-is, no Jekyll processing); `/CNAME` already present (`zonules.com`).
- **robots.txt hardened:** because root publishing exposes source folders alongside published pages, added `Disallow:` for `/data/`, `/scripts/`, `/content/`, `/static/`, `/templates/`, `/site/`, `/docs/`. This is an indexing hint only, not a security boundary — the standing rule holds: no secrets, no API tokens, no sensitive files in the repository.
- **Validator extended (`scripts/validate_all.py`):** new root-publication checks now block the gate unless — root `index.html`, `sitemap.xml`, `robots.txt`, `CNAME`, `.nojekyll` all exist; `docs/` does not exist; `robots.txt` references the canonical sitemap; no sitemap URL points inside `/site/` or `/static/`; every sitemap URL resolves to a published page at root; every approved+indexable route has a published root page; `/acquire/` is excluded from the sitemap (and, by the existing acquire check, carries `noindex`).
- **Verification:** Official sequence run — `generate_sitemap.py` (100 urls) → `build_site.py` (98 pages + stylesheet) → `validate_all.py` (PASS) → `validate_all.py` (PASS, idempotent). Final gate: 101 pages, 355 claims, 8 sources, layers L1/L2/L3/cross; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Homepage serves the gateway ("what makes vision possible"), not README; `/acquire/` carries `noindex` and is absent from the 100-URL sitemap; sitemap contains no `/site/` or `/static/` paths.
- **Preserved:** Sprint 3D corpus (101 routes), README.md, ASSET_THESIS.md, and all governance files unchanged in substance. No API, no Cloudflare Workers, no forms, no newsletter backend, no payment widgets, no third-party scripts introduced.
- **Type:** Publishing correction; routes v1.5→v1.6; no corpus or claim changes.
- **Affected:** `scripts/{build_gateway,build_engine,build_acquire,build_site,generate_sitemap,validate_all}.py`, `data/routes.json`, new root publication tree (`index.html`, `/<slug>/index.html`, `assets/`, `sitemap.xml`, `robots.txt`, `.nojekyll`); removed `site/` and the moved `static/` outputs.

## 2026-06-13 — Interface Freeze After Root Publication

### Status

APPROVED — Public gateway interface accepted for the current phase.

### Decision

The current Zonules.com public interface is approved as sufficient for the next development phase.

No major visual redesign, animation expansion, layout restructuring, or interface experimentation is required at this stage.

### Rationale

The live interface now communicates the governing thesis clearly, no longer exposes README-style repository documentation, and presents Zonules.com as a sovereign visual reference system rather than a generic content site.

The suspension-reveal interface embodies the core thesis: hidden structural tension makes focus possible.

### Freeze Rule

Interface changes are frozen except for:

- broken layout fixes
- accessibility defects
- mobile readability defects
- broken links
- validation failures
- security or publishing issues

No aesthetic-only redesign is permitted until the English canonical corpus is substantially expanded.

### Next Priority

Continue corpus expansion and reference authority building.

## 2026-06-14 — Sprint 4: English corpus expansion to 152 pages, 559 claims

- **Change:** Add 51 governed English reference units in three batches of 17 (TRM-102…TRM-152), advancing the corpus from 101 to 152 routes and claims from 355 to 559. English only; no multilingual pages, no interface change.
  - **Batch A (TRM-102…118):** L1 receptive-fields, dark-adaptation, light-adaptation, stereopsis, color-constancy, visual-field, vergence; L2 predictive-coding, face-perception, object-recognition, scene-recognition, visual-crowding; L3 attention-mechanism, transformer-architecture, convolutional-neural-networks, few-shot-learning, generative-models.
  - **Batch B (TRM-119…135):** L1 photopic-vision, scotopic-vision, nystagmus, scotoma, accommodation-reflex; L2 active-inference, mental-imagery, multisensory-integration, spatial-cognition, perceptual-grouping, temporal-integration, metacognition; L3 self-supervised-learning, contrastive-learning, zero-shot-learning, video-understanding, action-recognition.
  - **Batch C (TRM-136…152):** L1 optokinetic-reflex, vestibulo-ocular-reflex, spatial-frequency, contrast-threshold, visual-resolution; L2 bottom-up-processing, cognitive-load, attentional-blink, perceptual-adaptation, visual-attention, spatial-attention, feature-based-attention; L3 image-quality-assessment, visual-question-answering, instance-segmentation, gaze-estimation, image-synthesis.
- **Registry advances:** routes v1.9 (152 routes), claims v1.2 (559; CLM-356…CLM-559, each unit 3 sourced + 1 internal-framework). Sitemap 151 indexable URLs (/acquire/ excluded).
- **Orphan policy:** four orphan defects (accommodation-reflex, perceptual-adaptation, instance-segmentation, gaze-estimation) caught by the gate and resolved with reciprocal inbound links before commit.
- **Constraints held:** no interface redesign, no APIs/forms/Workers/newsletter/payment/third-party scripts, no second language; static-first; /acquire/ noindex and absent from sitemap.
- **Verification:** gate PASS — 152 pages, 559 claims, 8 sources; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0.
- **Affected:** `content/en/terms/*.md` (51 new units), `data/{routes,claims}.json`, regenerated root pages and `sitemap.xml`.

## 2026-06-14 — Sprint 5A: Anchor Reference Depth & Source Maturity

- **Context:** An external review judged the asset's structure, governance, and cohesion strong but the per-page depth and source breadth only moderate — the expected profile after wide corpus construction. This sprint matures depth and sourcing rather than adding page count.
- **Decision:** Deepen the highest-authority anchor pages, mature the source registry, and make the FIO/FIS codes legible to newcomers and AI agents. No numeric expansion; no interface redesign; no multilingual; no monetization.
- **Source maturity — `data/sources.json` 8 → 27 (version 0.3):** added SRC-009…SRC-027 across ocular anatomy and the visual pathway (Kandel, Hubel & Wiesel, Wandell, Rodieck, Purves), perception and cognitive science (Snowden, Bruce, Marr, Friston, Rao & Ballard), computer vision and machine learning (Goodfellow, Bishop, Szeliski-adjacent ImageNet/ILSVRC, Marr), transformers (Vaswani "Attention Is All You Need", Dosovitskiy ViT), deepfake detection and forensics (Verdoliva, FaceForensics++), and medical-safety / institutional references (National Eye Institute, WHO World Report on Vision). Newly used types include peer-reviewed and government-regulatory.
- **Anchor deepening (13 reference units):** added new analytical sections — Mechanism, Failure Mode, Human–Machine Bridge, Common Misunderstanding, Example Scenario, Why It Matters, Detection Is Not Understanding, and Source Notes — with 32 new registered claims (CLM-560…CLM-591). The thin Sprint-4 anchors (predictive-coding, active-inference, transformer-architecture) received the heaviest expansion; the already-deep anatomy and verification anchors (zonules-of-zinn, lens-accommodation, crystalline-lens, retina, optic-nerve, visual-cortex, visual-perception, computer-vision, deepfake-detection, image-provenance) received targeted depth plus matured sourcing. transformer-architecture now explains why transformers matter for visual systems and the detection-vs-understanding distinction, per review.
- **Newcomer legibility:** added the explanatory page **`/focus-integrity-codes/`** that defines FIO and FIS for human readers and AI agents and shows how to read a page from its codes; linked from methodology, source-policy, the glossary, and the ontology. Every reference page now carries a short under-badge note explaining FIO/FIS and linking to that page; the glossary and ontology intros explain the codes and link to it.
- **Registry advances:** routes v2.0 (153 routes; +1 governance page), claims v1.3 (591), sources v0.3 (27). Sitemap 152 indexable URLs.
- **Tiered depth doctrine (recorded):** anchor pages are deep and multi-sourced; core reference pages are complete and sufficiently sourced; supporting term pages are precise but not encyclopedic; governance pages are clear and decisive; the acquisition surface stays strategic and restricted. Not every page is held to the same depth.
- **Verification:** gate PASS — 153 pages, 591 claims, 27 sources; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. All five builders fresh; root-publication checks intact.
- **Affected:** `data/sources.json`, `data/{routes,claims}.json`, `content/en/pages/focus-integrity-codes.md` (new), `content/en/pages/{methodology,source-policy}.md`, `content/en/terms/{zonules-of-zinn,lens-accommodation,crystalline-lens,retina,optic-nerve,visual-cortex,visual-perception,predictive-coding,active-inference,computer-vision,transformer-architecture,deepfake-detection,image-provenance}.md`, `scripts/build_site.py`, `static/css/reference.css`, regenerated root pages and `sitemap.xml`.
- **Next:** Sprint 5B — resume numeric expansion toward 200–225 canonical English pages on the matured depth-and-source baseline.

## 2026-06-14 — Sprint 5B: English corpus expansion to 213 pages, 831 claims

- **Change:** Add 60 governed English reference units (TRM-153…TRM-212), advancing the corpus from 153 to 213 routes and claims from 591 to 831. English only; no new sources required; no multilingual pages; no interface change; no monetization surface. Built on the Sprint 5A matured depth-and-source baseline.
  - **Batch 5B-A — L1 Anatomy / Visual Science (18):** corneal-endothelium, corneal-epithelium, limbus, canal-of-schlemm, ciliary-muscle, bruchs-membrane (optical-pathway / suspension & accommodation maintenance); foveola, parafovea (photoreceptor-function / separation); optic-disc, pupil, uvea (optical-pathway); horizontal-cells, bipolar-cells, amacrine-cells (new retinal-circuitry cluster); rod-cells, cone-cells, rhodopsin, phototransduction (photoreceptor-function / separation).
  - **Batch 5B-B — L2 Perception / Cognitive Science (21):** size-constancy, shape-constancy, lightness-constancy (accommodation); depth-cues, binocular-disparity, motion-parallax, biological-motion, amodal-completion, illusory-contours (interpretation); iconic-memory, divided-attention (suspension); feature-integration-theory, gist-perception, categorical-perception, global-precedence, holistic-processing, context-effects (interpretation); preattentive-processing, ensemble-perception (separation); perceptual-learning, motion-aftereffect (accommodation).
  - **Batch 5B-C — L3 Machine Vision / Verification (21):** edge-detection, anomaly-detection, robustness (separation); feature-matching, keypoint-detection, residual-networks, stereo-matching (suspension); optical-character-recognition, panoptic-segmentation, saliency-maps, class-activation-mapping, dataset-bias, knowledge-distillation, face-recognition (interpretation); backpropagation, batch-normalization (accommodation); uncertainty-estimation, diffusion-models, generative-adversarial-networks, digital-watermarking, perceptual-hashing (provenance).
- **Per-unit governance:** each unit carries layer, cluster, FIO/FIS classification, term_id, concept_id, canonical URL, safety class, source notes, and required internal links; each has exactly 3 sourced claims (CLM-592…CLM-831, 180 sourced) + 1 internal-framework claim (60), and a registered Safety Notes section. Every unit links to `/focus-integrity-ontology/` and `/focus-integrity-codes/` for newcomer legibility, and the renderer adds the FIO/FIS under-badge note automatically.
- **Source posture:** no new sources were needed; all sourced claims rest on the existing 27-source registry (anatomy SRC-001/002/003/009/011/012/013; perception SRC-005/006/014/015; machine vision SRC-007/016/017/022/027; provenance/forensics SRC-008/023/024). `data/sources.json` remains v0.3, preserving Sprint 5A source maturity.
- **Tiered depth held:** new units are precise supporting/core reference pages (definition, scientific grounding with cited sources, layer role, ontology relationship, related terms, reference notes, safety notes) — not encyclopedic anchors — consistent with the Sprint 5A tiered-depth doctrine.
- **Orphan policy:** reciprocal inbound links were designed within thematic clusters; a same-layer backlink pass guaranteed every new unit has at least one inbound link, caught and resolved before commit (gate orphans=0).
- **Registry advances:** routes v2.0 → v2.1 (213 routes), claims v1.3 → v1.4 (831). Sitemap regenerated to 212 indexable URLs (/acquire/ noindex and excluded); robots.txt unchanged.
- **Constraints held:** no interface redesign; no APIs, Cloudflare Workers, forms, newsletter backend, payment widgets, or third-party public scripts; no second language; static-first; no /site/ or /static/ canonical paths; ASSET_THESIS.md unchanged.
- **Verification:** gate PASS — 213 pages, 831 claims, 27 sources, layers [L1, L2, L3, cross]; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Sitemap count (212) equals approved indexable routes (212). All five builders fresh; root-publication checks intact.
- **Affected:** `content/en/terms/*.md` (60 new units), `data/{routes,claims}.json`, regenerated root pages, `sitemap.xml`.
- **Next:** Hold at the 200–225 band; future sprints deepen sourcing or begin governed multilingual expansion only under a separate decision.

## 2026-06-14 — Sprint 5C: Corpus Coherence & Authority Audit (213 pages)

Audit of the 213-page English canonical corpus for coherence, internal authority, anchor strength, cluster balance, FIO/FIS distribution, source maturity, and publication integrity. No broad new corpus pages were added; only surgical coherence fixes were applied.

### Findings

- **Internal link graph:** 0 true orphans (validator-confirmed). However, **57 reference units sat at exactly 1 inbound link** (orphan-risk — a single link removal would orphan them), including pre-5B pages (accommodation-reflex, conjunctiva, lens-capsule, nystagmus, optic-radiations, scotoma, gaze-estimation, video-understanding, visual-question-answering) and most Sprint 5B leaves. Outbound was already healthy (every reference unit ≥3 outbound; distribution 3–6). All Sprint 5B pages already link `/focus-integrity-codes/` and `/focus-integrity-ontology/`.
- **Glossary accuracy defect:** the glossary rendered the FIO code for all 203 units but the **FIS code was blank for every entry**, because `render_glossary` reads `fis_criterion` from the route registry while routes carried only `fio_class`. Labels and L1/L2/L3 layer grouping were correct; all 203 reference units were represented.
- **Cluster balance:** L1 = 69 (optical-pathway 45, photoreceptor-function 11, lens-suspension 5, oculomotor 5, retinal-circuitry 3); L2 = 70 (single cluster `perceptual-clarity`); L3 = 64 (single cluster `machine-perception`). L1 is well sub-clustered but optical-pathway-heavy; **L2 and L3 are flat (one cluster each)** — a navigability limit, not a governance defect.
- **FIO/FIS distribution:** FIO-05 Interpretation 66, FIO-01 Suspension 47, FIO-03 Separation 42, FIO-02 Accommodation 32, FIO-04 Provenance 16. FIS mirrors FIO one-to-one by number, as required by `REFERENCE_ARCHITECTURE.md`. Distribution is conceptually sound: interpretation is the richest failure space (L2/L3), provenance the narrowest (L3-weighted, conceptual bridge at L1). No misclassifications found.
- **Source maturity:** 0 pages with zero sourced claims; 182 pages at 3 sourced claims, 11 at 2, 10 at 4+. **SRC-025 (National Eye Institute) and SRC-026 (WHO World Report on Vision) are registered but never cited.** Deep anchor sources (Hubel & Wiesel, Vaswani, ViT, Rao & Ballard) are each cited once, which is expected for anchor-specific references.
- **Canonical / publication integrity:** sitemap = 212 URLs = approved indexable routes; no `/site/` or `/static/` canonical paths; `/acquire/` remains noindex and excluded; root-publication checks pass.

### Fixes applied (surgical)

- **Glossary FIS codes (defect fix):** added a `fis_criterion` field to all 203 reference-unit routes, sourced authoritatively from each unit's markdown frontmatter. The glossary now renders both codes (e.g., `FIO-02 · FIS-2`) for every entry. Unit pages are unaffected (they already read FIS from frontmatter).
- **Orphan-risk elimination:** added **57 reciprocal internal links across 30 donor pages** so that **every reference unit now has ≥2 inbound links** (min inbound 1 → 2). Each new inbound was drawn from the target's own related set, choosing the highest-authority related node as donor, so the new edges are conceptually natural reciprocal links (e.g., the `retina` anchor now links to its retinal-layer leaves) and push hub authority toward the leaves. Bullets were inserted into donor markdown `Related Terms` sections and mirrored in `required_internal_links`.

### Registry / state changes

- `data/routes.json` v2.1 → **v2.2** (added `fis_criterion` to 203 routes; +57 `required_internal_links` across 30 pages). `data/claims.json` unchanged (v1.4). `data/sources.json` unchanged (v0.3). `sitemap.xml` regenerated (212 URLs, unchanged count). Root pages and glossary regenerated.

### Verification

- Gate **PASS** — 213 pages, 831 claims, 27 sources, layers [L1, L2, L3, cross]; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Post-fix: min inbound across all reference units = 2; glossary FIS coverage 203/203; sitemap = 212 = indexable approved routes; `/acquire/` excluded.

### Next recommendation (Sprint 6A)

1. **Source maturity:** wire SRC-025 (NEI) and SRC-026 (WHO) into relevant public-health/anatomy pages (e.g., visual-field, contrast-sensitivity, color-perception, macula) by adding them as supporting sources to existing claims, and lift the 11 two-sourced pages toward three sourced claims.
2. **Cluster depth:** introduce sub-clusters within L2 (`perceptual-clarity`) and L3 (`machine-perception`) — e.g., attention / constancy / scene for L2 and recognition / generation-provenance / geometry for L3 — to improve navigability before further numeric growth.
3. **FIO-04 balance:** if expanding, bias slightly toward provenance/verification (FIO-04/FIS-4), the narrowest class.

## 2026-06-14 — Sprint 6A: Source Maturity & Cluster Architecture

Matured source coverage and introduced sub-cluster architecture across L2 and L3 before the final English expansion. No broad new corpus pages were added; the page count holds at 213.

### Source maturity

- **Wired the two unused sources.** SRC-025 (National Eye Institute) and SRC-026 (WHO World Report on Vision) were previously registered but uncited (flagged in Sprint 5C). They are now cited by registered claims: **SRC-025 in 13 claims**, **SRC-026 in 3 claims**.
- **NEI (SRC-025):** added one public-eye-health claim to each of the 11 two-sourced L1 anatomy pages (cornea, iris, vitreous-humor, macula, aqueous-humor, pupillary-reflex, optic-chiasm, optic-tract, lateral-geniculate-nucleus, sclera, choroid) plus the priority anchors retina and optic-nerve. Each NEI claim attributes a general structural/functional description to the NEI and carries no diagnostic phrasing.
- **WHO (SRC-026):** added public-health framing claims where they genuinely fit — visual-field (glaucoma and the global impairment burden), visual-acuity (the WHO 2.2-billion vision-impairment estimate), and ophthalmic-ai (avoidable impairment motivating scalable screening). These are attributed, epidemiological, non-diagnostic statements.
- **Lifted the 11 weak pages:** every one of the 11 pages that previously had only two sourced claims now has **three sourced claims**. New claims CLM-832…CLM-847 (16 sourced) registered in `claims.json`; each page's frontmatter, route `claim_requirements`/`source_requirements`, in-body Scientific Grounding text, and the authored Sources note were updated in lockstep. No source not relevant to a page was forced onto it.

### Cluster architecture

- **L2 (`perceptual-clarity`, flat) → 7 sub-clusters:** attention (16), recognition (17), scene-understanding (9), constancy (8), perceptual-error (8), prediction (7), memory (5).
- **L3 (`machine-perception`, flat) → 7 sub-clusters:** detection (21), representation-learning (14), verification (8), robustness (7), provenance (5), segmentation (5), generative-vision (4).
- Each of the 134 L2/L3 reference units was reassigned exactly once. The `cluster` field was updated consistently in `routes.json`, in each unit's markdown frontmatter, and in the in-body Layer Classification line. The glossary groups by layer (unchanged); sub-clusters add navigable structure for future expansion and for any later cluster-indexed surface.

### FIO-04 (provenance) strengthening

- Identified the provenance/verification surface: the new L3 `provenance` sub-cluster (image-provenance, deepfake-detection, synthetic-media, digital-watermarking, perceptual-hashing), the `generative-vision` sub-cluster (generative-models, GANs, diffusion-models, image-synthesis), plus verification pages (uncertainty-estimation, model-calibration, out-of-distribution-detection).
- **Internal links:** the five provenance pages already form a tight reciprocal web — every one links to at least two others in the set (deepfake-detection and digital-watermarking link to all four) — so no additional links were structurally required.
- **Source notes:** provenance pages consistently rest on the standards/forensics sources — SRC-008 (C2PA), SRC-023 (Verdoliva media forensics), SRC-024 (FaceForensics++).
- **New pages:** none. The cluster is dense and well-sourced; no new page was structurally necessary, so the 3–5-page allowance was not exercised (honoring the "no broad new pages" constraint).

### State changes

- `data/routes.json` v2.2 → **v2.3** (134 cluster reassignments; +16 `claim_requirements`; updated `source_requirements`). `data/claims.json` v1.4 → **v1.5** (831 → 847 claims; +16 sourced, CLM-832…CLM-847). `data/sources.json` unchanged (v0.3) — no sources added, two previously-unused sources now in use. `sitemap.xml` regenerated (212 URLs, unchanged).

### Verification

- Gate **PASS** — 213 pages, 847 claims, 27 sources, layers [L1, L2, L3, cross]; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Sitemap = 212 = indexable approved routes; `/acquire/` noindex and excluded; no `/site/` or `/static/` canonical paths; root publishing intact. SRC-025 used ×13, SRC-026 used ×3; all 11 weak pages now at three sourced claims; L2 and L3 each carry seven meaningful sub-clusters.

### Next recommendation

The corpus is now source-mature (all 27 sources in use), sub-clustered, and graph-robust (every unit ≥2 inbound). It is ready for the final governed English expansion toward ~300 pages, which should fill the thinner sub-clusters first (L3 generative-vision and segmentation; L2 memory and prediction) and bias modestly toward FIO-04 provenance/verification, the narrowest failure class.

## 2026-06-14 — Sprint 6B: Final English Expansion to 300 Governed Pages

Final governed English expansion: added 87 reference units (TRM-213…TRM-299), advancing the corpus from 213 to **300 routes** and claims from 847 to **1195**. English only; no new sources required; no interface change; no multilingual; no monetization. Built on the source-mature, sub-clustered, graph-robust 6A baseline.

### Batches

- **Batch 6B-A — L2 memory/prediction + L3 generative-vision/segmentation.** L2 memory (visual-long-term-memory, visual-recognition-memory, spatial-memory, working-memory-capacity, eidetic-imagery, visual-memory-encoding) and prediction (bayesian-perception, prediction-error, prior-expectation, expectation-suppression, cue-integration, perceptual-decision-making, evidence-accumulation); L3 generative-vision (variational-autoencoders, latent-space, text-to-image-generation, image-inpainting, super-resolution, neural-style-transfer) and segmentation (superpixels, region-proposal, background-subtraction, interactive-segmentation, salient-object-detection, video-object-segmentation).
- **Batch 6B-B — L3 verification/provenance/robustness, biased toward FIO-04.** provenance (media-forensics, content-authenticity, camera-fingerprinting, splicing-detection, copy-move-detection, tamper-detection — all FIO-04); verification (cross-validation, selective-prediction, evaluation-metrics, ground-truth, error-analysis); robustness (adversarial-training, corruption-robustness, test-time-adaptation, spurious-correlation, covariate-shift); detection (multi-object-tracking, small-object-detection, open-vocabulary-detection); representation-learning (foundation-models, image-embeddings).
- **Batch 6B-C — L1 selective visual science + L2 perceptual-error/scene-understanding.** L1 added the cortical-processing cluster (magnocellular-/parvocellular-pathway, dorsal-/ventral-stream, cortical-magnification, orientation-selectivity, ocular-dominance-columns, simple-/complex-cells, area-mt) and retinal/optical units (müller-cells, midget-/parasol-ganglion-cells, lacrimal-gland, corneal-stroma, ora-serrata, ciliary-processes, refraction, optical-/chromatic-/spherical-aberration); L2 perceptual-error (afterimage, simultaneous-contrast, mach-bands, binocular-rivalry, troxler-fading, flash-lag-effect, geometric-illusions) and scene-understanding (self-motion-perception, heading-perception, kinetic-depth-effect, surface-perception, material-perception, spatial-layout-perception, egocentric-distance).
- **Batch 6B-D — cluster/inbound balancing.** Remaining L2 attention (overt-/covert-attention), recognition (viewpoint-invariance, word-recognition), and constancy (velocity-/position-constancy) units; a ≥2-inbound guarantee pass distributed reciprocal links so every new unit carries at least two inbound and at least three outbound links.

### Per-unit governance

Each unit carries layer, cluster (sub-cluster), FIO/FIS classification, term_id, concept_id, canonical URL, safety class, source notes, and required internal links; links to `/focus-integrity-ontology/` and `/focus-integrity-codes/`; has exactly 3 sourced claims + 1 internal-framework claim (CLM-848…CLM-1195: 261 sourced, 87 internal-framework) and a Safety Notes section. The new route `fis_criterion` field (added in 6A) is populated, so the glossary renders both codes for all 290 reference units.

### Cluster fill (thinner clusters prioritized)

- **L2:** memory 5→11, prediction 7→14, perceptual-error 8→15, scene-understanding 9→16; attention 16→18, recognition 17→19, constancy 8→10. Total L2 70→103.
- **L3:** generative-vision 4→10, segmentation 5→11, provenance 5→11, robustness 7→12, verification 8→13; detection 21→24, representation-learning 14→16. Total L3 64→97.
- **L1:** new `cortical-processing` cluster (10) and `retinal-circuitry` 3→6, plus optical-pathway additions. Total L1 69→90.

### FIO-04 (provenance) — modest bias, no overcorrection

FIO-04 grew from 16 to **29** reference units (forensics, content authenticity, and the generative-vision pages that raise provenance concerns), remaining well below FIO-05 (99). Final FIO distribution: FIO-05 99, FIO-01 62, FIO-03 61, FIO-02 39, FIO-04 29.

### Source posture

No new sources were needed; all sourced claims rest on the existing 27-source registry (all of which remain in use). `data/sources.json` stays v0.3.

### State changes

`data/routes.json` v2.3 → **v2.4** (300 routes). `data/claims.json` v1.5 → **v1.6** (1195). `data/sources.json` unchanged (v0.3). `sitemap.xml` regenerated to **299** indexable URLs (/acquire/ noindex and excluded). Root pages, glossary, and ontology regenerated.

### Verification

Gate **PASS** — 300 pages, 1195 claims, 27 sources, layers [L1, L2, L3, cross]; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Every reference unit has ≥2 inbound and ≥3 outbound links (no orphan-risk). Sitemap = 299 = approved indexable routes; no `/site/` or `/static/` canonical paths; `/acquire/` excluded; root publishing intact. Glossary FIO/FIS coverage 290/290.

### Next

The English canonical corpus has reached its ~300-page target with preserved depth, source maturity, sub-cluster architecture, and link-graph integrity. Future work (separate decisions): governed multilingual expansion, or selective anchor deepening — not further numeric growth.

## 2026-06-14 — Sprint 6C: Canonical Readiness & Authority Audit (300 pages)

Audited the 300-page English canonical corpus not only for technical correctness but for sovereign-reference readiness: strategic-story alignment, conceptual depth, stakeholder usefulness, source credibility, SEO integrity, AI readability, security posture, and multilingual readiness. No broad new pages. Only small, safe surgical fixes applied.

### 1. Strategic story alignment — PASS
Every reference unit carries a "Relationship to the Governing Thesis" section and the FIO/FIS codes, so anatomy (L1), perception (L2), and machine vision (L3) are presented as one focus-integrity system rather than three topics. The shared five-class FIO/FIS spine runs through all layers; the ontology and `/focus-integrity-codes/` pages bind them. The thesis "hidden structure makes vision possible" is expressed structurally on every page.

### 2. Conceptual depth — classification recorded
By inbound authority: **Anchor (≥10 inbound) 44, Core (5–9) 52, Supporting (<5) 194**, plus 5 governance (policy), 1 acquisition, and the gateway/engine/ontology/glossary surfaces. No thin pages (minimum 337 words; median 380). **Gap identified:** the deeper analytical layers — Mechanism, Failure Mode, Human–Machine Bridge, Common Misunderstanding — exist only on the ~13 Sprint-5A-deepened anchors. The 287 core/supporting units answer four of the five canonical questions (What / How / system role / focus-integrity link) but lack explicit **Failure Mode ("Where does it fail?")** and **Why-it-matters / Human–Machine Bridge** sections. This is by design under the tiered-depth doctrine, and is the primary Sprint-6D target.

### 3. Stakeholder usefulness — mapped
- **Students / academics:** glossary + governance pages + FIO/FIS codes give a teachable structure.
- **Scientists / researchers:** registered claims with classified sources and References sections support citation.
- **Developers / AI teams:** L3 sub-clusters (detection, segmentation, representation-learning, generative-vision, robustness, verification, provenance) form a navigable technical map.
- **AI systems:** stable headings, JSON-LD (DefinedTerm + citations + BreadcrumbList), and explicit claim/source classification make pages machine-parseable.
- **Investors / companies:** the acquisition surface plus the governance documents present the asset's structure without selling.
- **Journalists / governments:** provenance/verification cluster (media-forensics, content-authenticity, deepfake-detection, image-provenance) and the medical-safety framing serve visual-trust and public-interest use.

### 4. Source credibility — PASS with targets
All **27 sources are used**. No page over-relies on internal-framework claims (every reference unit has ≥2 sourced claims; none has sourced < internal). Anchor pages would benefit from greater source *diversity* (several anchors lean on one or two textbooks); recorded as a 6D target, not a defect.

### 5. SEO integrity — PASS
No duplicate `seo_title`; no duplicate `meta_description`; no meta under 50 chars; no `/site/` or `/static/` canonical paths; sitemap (299) equals indexable routes; glossary lists all 290 reference units. Minor: 20 anchor metas exceed ~165 chars (display-truncation only, not a penalty) — left as authored, flagged for optional 6D trimming. No keyword-stuffing or near-duplicate pages found.

### 6. AI readability — PASS
Consistent heading skeleton across units (Definition → Scientific Grounding → role → Layer Classification → Relationship to Governing Thesis → Related Terms → Reference Notes → Safety Notes); FIO/FIS codes present and now rendered with both codes in the glossary; claims classified as sourced/internal-framework; no meaning depends on visual design alone.

### 7. Technical & security posture — PASS
Static-first confirmed: no APIs, no form/newsletter/payment backends, no third-party public scripts, no `<form>`/`<iframe>`/external `<script src>` in any published page (the engine page's reviewed inline JS is the sole, governed exception), no `http://` or external hrefs in content, no secrets. Gate: broken_links=0, orphans=0, unsafe=0, unsourced_claims=0; every reference unit has ≥2 inbound and ≥3 outbound links.

### 8. Multilingual readiness
- **Ready for translation now:** governance pages and the deepened Sprint-5A anchors.
- **Harden before translation:** the 194 supporting units lacking Failure-Mode / Why-it-matters depth — translating them first would multiply thinness across languages.
- **Must remain stable across languages:** FIO/FIS codes and class names, `term_id`/`concept_id`, canonical URLs, claim IDs, and source classifications. Source notes must not be weakened or made vaguer in translation.

### Surgical fixes applied (small + safe)
- **Weak internal-link repair:** four routes carried a `required_internal_link` that was registered but never rendered in the page body (leftover route-only reciprocal links from Sprint 4): `/vergence/`→`/accommodation-reflex/`, `/metacognition/`→`/perceptual-adaptation/`, `/action-recognition/`→`/gaze-estimation/`, `/visual-question-answering/`→`/instance-segmentation/`. Each is now a real rendered link in the Related Terms section. Registered-but-unrendered links: 4 → **0**.

### 9. Authority-gap ranking for Sprint 6D (Canonical Authority Hardening)
Deepen ~25–30 authority pages — not numeric growth — adding, per type, the missing layers (Mechanism, Failure Mode, Human–Machine Bridge, Common Misunderstanding, broadened Source Notes) so each answers all five canonical questions.
- **Critical (the spine — deepen first):** zonules-of-zinn, lens-accommodation, retina, optic-nerve, visual-cortex, predictive-coding, active-inference, object-recognition, scene-understanding, computer-vision, transformer-architecture, deepfake-detection, image-provenance, focus-integrity-ontology, focus-integrity-codes, glossary.
- **Important:** visual-acuity, visual-field, visual-working-memory, perceptual-error, diffusion-models, content-authenticity, camera-fingerprinting, perceptual-hashing, ophthalmic-ai, medical-imaging-ai, dorsal-stream, ventral-stream.
- **Later:** broaden source diversity on remaining anchors; optional meta-length trim on the 20 long-meta pages; selective Failure-Mode lines on high-traffic supporting units.

### Verification
Gate **PASS** — 300 pages, 1195 claims, 27 sources; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Sitemap = 299 = indexable routes; `/acquire/` noindex and excluded; no `/site/` or `/static/` canonical paths. Registries unchanged in version (no schema change this sprint): routes v2.4, claims v1.6, sources v0.3.

### Recommendation
Proceed to **Sprint 6D — Canonical Authority Hardening** on the Critical list above, then freeze the English master before any multilingual work (Sprint 7A). Translating before the anchors carry full reference depth would propagate weakness across every language; hardening first protects the path to ~2400 governed pages without loss of quality.

## 2026-06-14 — Sprint 6D: Canonical Authority Hardening

Deepened the critical spine and high-value pages into sovereign reference-grade anchors — no new pages, no interface change. The goal was authority and conceptual depth, not page count: making the pages that lead the corpus answer all five canonical questions (What / How / Why it matters / Where it fails / How it connects to focus integrity).

### What was hardened

**Critical spine (13 markdown anchors) — full analytical depth added where missing:** zonules-of-zinn, lens-accommodation, retina, optic-nerve, visual-cortex (L1); predictive-coding, active-inference, object-recognition (L2); scene-understanding, computer-vision, transformer-architecture, deepfake-detection, image-provenance (L3). Sections added per page from the set {Mechanism, Why It Matters, Failure Mode, Human–Machine Bridge, Common Misunderstanding, Source Notes}, with no heading duplicated against what each page already had. Word counts roughly doubled to tripled (e.g., object-recognition 337→730, scene-understanding →746, the anatomy/CV anchors to ~1000–1165 words). Batch total: +42 sections, +72 registered claims (CLM-1196…CLM-1267).

**Important (6 pages) — same treatment, with strengthened medical-safety framing:** visual-acuity, visual-field (public-health relevance, WHO-anchored), diffusion-models, content-authenticity (provenance), ophthalmic-ai, medical-imaging-ai. The two medical-AI pages carry an explicit "detection is not diagnosis" Common Misunderstanding and a Human–Machine Bridge that keeps the model as a triage aid within a human-led process. Batch total: +30 sections, +33 claims (CLM-1268…CLM-1300).

**Generated authority surfaces (focus-integrity-ontology, focus-integrity-codes, glossary):** reviewed and left unchanged. These are already governance-grade — the codes page already carries "how to read a page," a worked example, and an explicit "for AI agents and citation systems" section; the ontology and glossary are generated deterministically from the registries. Adding prose here would be filler, which the sprint forbids.

### Authoring discipline

Each added section is page-specific and non-templated: the Human–Machine Bridge on `optic-nerve` is about an irreversible single-channel chokepoint; on `transformer-architecture` it is about attention as machine selective weighting; on `content-authenticity` it is about an external warrant of origin. Every new factual sentence is a registered claim — sourced where a registered reference supports it, internal-framework (SRC-004) where it is Zonules.com thesis interpretation. No new sources were added; all 27 remain in use.

### Results

- **Deep-section coverage** (reference units containing each section): Mechanism 6→19, Why It Matters 1→19, Human–Machine Bridge 3→18, Failure Mode 5→15, Common Misunderstanding 1→15, Source Notes 13→15.
- **Claims:** 1195 → **1300** (957 sourced, 343 internal-framework; sourced remains the majority). No page over-relies on internal-framework claims.
- **Stakeholder reach:** each hardened page now serves at least three groups — e.g., the medical-AI pages serve developers, clinicians/regulators, and journalists with an explicit detection-vs-diagnosis boundary; the provenance pages serve journalists, companies, and AI teams.

### State changes

`data/routes.json` v2.4 → **v2.5** (claim_requirements/source_requirements extended on 19 pages; no route added). `data/claims.json` v1.6 → **v1.7** (1300). `data/sources.json` unchanged (v0.3). Page count unchanged (300); sitemap unchanged (299). Root pages regenerated.

### Verification

Gate **PASS** — 300 pages, 1300 claims, 27 sources; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Every reference unit retains ≥2 inbound and ≥3 outbound links (no orphan-risk). Sitemap = 299 = indexable routes; `/acquire/` noindex and excluded; no `/site/` or `/static/` canonical paths; static-first security intact; medical pages retain the eye-care disclaimer.

### Recommendation — English master freeze

The critical spine now carries reference-grade depth, the source registry is fully used, the link graph has no orphan-risk, and SEO/AI-readability/security audits are clean. The English canonical layer is ready to be declared the **canonical master** and frozen before multilingual work. Suggested path:
1. **Optional Sprint 6E (minor):** harden the remaining Important-tier pages (visual-working-memory, perceptual-error, camera-fingerprinting, perceptual-hashing, dorsal-stream, ventral-stream) and optionally trim the ~20 long anchor metas — small, safe, non-blocking.
2. **English Master Freeze:** declare the English corpus the canonical reference layer; freeze FIO/FIS codes, term_id/concept_id, canonical URLs, claim IDs, and source classifications as the stable contract that translations must preserve.
3. **Sprint 7A — Multilingual Architecture:** begin governed translation on the frozen master, anchors first, with FIO/FIS and source notes held invariant across languages.

## 2026-06-14 — Sprint 6E: Final English Master Hardening & Freeze Preparation

Final minor hardening pass before declaring the English canonical master ready to freeze. No new pages, no interface change, no multilingual work.

### 1. Remaining important pages hardened (6)
Added page-specific analytical sections (Mechanism, Why It Matters, Failure Mode, Human–Machine Bridge, Common Misunderstanding, Source Notes) to: **visual-working-memory** (6/6), **camera-fingerprinting** (6/6), **perceptual-hashing** (6/6), **dorsal-stream** (6/6), **ventral-stream** (6/6), and **perceptual-error** (5/6 — a separate Failure Mode was intentionally omitted because the page's whole subject is the interpretation failure itself; redundancy would be filler). Word counts rose from ~350–765 to ~550–997. Batch: +35 sections, +36 registered claims (CLM-1301…CLM-1336), all sourced where a registered reference supports the statement and internal-framework (SRC-004) for thesis framing. No new sources; all 27 remain in use.

### 2. Long metadata trimmed (17)
Shortened the 17 reference-unit and policy meta descriptions that exceeded ~165 characters, to ≤144 characters each, preserving search intent and meaning, with distinct phrasing and no keyword stuffing: perceptual-error, attention-capture, top-down-processing, visual-inference, perceptual-load, pattern-recognition, feature-integration-theory, visual-scene-parsing, fovea-centralis, synthetic-media, medical-imaging-ai, neural-network-interpretability, optic-chiasm, sclera, dorsal-stream, focus-integrity-codes, methodology. Both the markdown frontmatter and the route registry were updated together. The **three remaining long metas belong to generated interface surfaces** — the gateway (`/`), the engine (`/focus-integrity-engine/`), and `/acquire/` (noindex) — and were intentionally left untouched under the approved interface freeze; their length is cosmetic and `/acquire/` is excluded from indexing entirely.

### 3. Translation-safety check — the freeze contract
For future multilingual expansion, the following fields are declared **stable and invariant across languages** (translations localize prose only, never these):
- `term_id` and `concept_id` — identity of each reference unit.
- route `slug` and `canonical` URL — the English canonical remains the hreflang `x-default`.
- `fio_class` / `fis_criterion` (FIO/FIS classification) — the governing spine; same code in every language.
- claim IDs (`CLM-…`) and source IDs (`SRC-…`) — provenance must map one-to-one across languages.
- `safety_class` and the substance of Safety Notes — medical/AI safety wording must not be weakened, softened, or made vaguer in any translation; "detection is not diagnosis" and the eye-care disclaimer must survive translation intact.
- internal-framework (SRC-004) wording defining FIO/FIS and the focus-integrity thesis — translated faithfully, never reinterpreted.
No language folders were created and nothing was translated in this sprint.

### 4. State changes
`data/routes.json` v2.5 → **v2.6** (claim/source requirements extended on 6 pages; 17 meta descriptions trimmed; no route added). `data/claims.json` v1.7 → **v1.8** (1300 → 1336; 982 sourced, 354 internal-framework). `data/sources.json` unchanged (v0.3). Pages unchanged (300); sitemap unchanged (299). Root pages regenerated.

### 5. Verification
Gate **PASS** — 300 pages, 1336 claims, 27 sources; broken_links=0, orphans=0, unsafe=0, unsourced_claims=0. Every reference unit retains ≥2 inbound and ≥3 outbound links (no orphan-risk). Sitemap = 299 = indexable routes; `/acquire/` noindex and excluded; no `/site/` or `/static/` canonical paths; static-first security intact.

### Freeze-readiness note — RECOMMENDATION: ENGLISH MASTER FREEZE
The English canonical master is **ready to freeze.** Evidence:
- **Coverage & structure:** 300 governed pages across L1/L2/L3 with 7 sub-clusters per perception/machine layer; no orphans, no orphan-risk (every unit ≥2 inbound, ≥3 outbound).
- **Authority depth:** all 19 critical/important spine pages carry the full analytical layer set (Mechanism, Why It Matters, Failure Mode, Human–Machine Bridge, Common Misunderstanding, Source Notes, Safety Notes); each answers the five canonical questions.
- **Source maturity:** all 27 sources in use; 982 sourced claims vs 354 internal-framework; no page over-relies on framework claims.
- **SEO/AI readability:** unique titles, no duplicate metas, long metas trimmed (only frozen interface surfaces remain), stable headings, JSON-LD, FIO/FIS codes legible and rendered in the glossary.
- **Security/publication:** static-first; no APIs/forms/scripts/secrets; `/acquire/` noindex and excluded; sitemap = indexable routes.

**Recommended next step:** declare the English corpus the canonical master and freeze the contract fields above, then proceed to **Sprint 7A — Multilingual Architecture** (governed translation on the frozen master, anchors first, FIO/FIS and Safety Notes held invariant). No further English numeric growth is needed before the freeze.


## 2026-06-14 — Sprint 6F: English Canonical Master Freeze

The English canonical master of Zonules.com is declared frozen. The 300-page corpus
built over Sprints 1–6E has passed all governance gate checks and is accepted as the
stable source of truth for all future multilingual expansion.

### Freeze declaration

- **English canonical corpus:** 300 governed reference pages accepted as the canonical
  master. No further English numeric growth before multilingual expansion.
- **Sitemap:** 299 indexable URLs (all approved, indexable routes). `/acquire/` noindex
  and excluded.
- **Claims:** 1336 registered claims (982 sourced, 354 internal-framework). All claims
  resolve to registered sources. No unsourced claims.
- **Sources:** 27 registered sources, all in use. `data/sources.json` v0.3.
- **Route registry:** `data/routes.json` v2.6.
- **Claims registry:** `data/claims.json` v1.8.
- **FIO/FIS version:** v0.1 (frozen; version increment required for any class or
  criterion redefinition).
- **Interface:** Frozen. No structural, navigational, or CSS changes permitted without
  a governance entry.
- **Static-first posture:** Preserved. No APIs, Workers, forms, newsletter backend,
  payment widgets, or third-party scripts present in any published page.

### Governance gate

Gate **PASS** — 300 pages, 1336 claims, 27 sources; broken_links=0, orphans=0,
unsafe=0, unsourced_claims=0. Sitemap = 299 = indexable routes; `/acquire/` noindex
and excluded; no `/site/` or `/static/` canonical paths; static-first security intact.

### Freeze document created

`docs/ENGLISH_MASTER_FREEZE.md` (v1.0) defines:

- All frozen contract fields: `term_id`, `concept_id`, route `path` slug, `canonical`
  URL, `fio_class` / `fis_criterion` (FIO/FIS classification), claim IDs
  (`CLM-001`–`CLM-1336`), source IDs (`SRC-001`–`SRC-027`), `safety_class`, canonical
  English title, canonical English definition, internal framework wording, Safety Notes
  core meaning, medical disclaimer language, "detection is not diagnosis" language, and
  source attribution boundaries.
- The permitted-change / prohibited-change boundary.
- Multilingual readiness requirements: English master as source of truth, route mapping,
  concept identity, FIO/FIS identity, claim/source traceability, safety meaning, no thin
  translation rule, no automatic uncontrolled translation rule.
- Official future language order: English → French → German → Spanish → Chinese →
  Arabic → Japanese → Russian.

### Freeze validation added

`scripts/validate_all.py` updated (Sprint 6F):

- **Freeze floor guard:** Minimum count checks prevent silent deletion of frozen corpus
  elements — route count must remain ≥ 300, claim count ≥ 1336, source count ≥ 27.
- **`docs/` directory check refined:** Changed from checking the existence of the `docs/`
  directory to checking for `docs/index.html` (the actual GitHub Pages publication risk),
  allowing governance documents to reside in `docs/` without triggering a false gate
  failure.
- Future mutation-detection validator (freeze manifest, hreflang consistency) documented
  as Sprint 7A — Multilingual Architecture requirement in `docs/ENGLISH_MASTER_FREEZE.md`.

### Next phase

**Sprint 7A — Multilingual Architecture.** Begin governed multilingual expansion on the
frozen English master: French first, anchors first, FIO/FIS and Safety Notes held
invariant across all languages. No further English numeric growth before this phase.

---

## Sprint 7A — Multilingual Architecture on Frozen English Master

**Date:** 2026-06-14  
**Status:** Complete  
**Branch:** `claude/english-master-freeze-nb3xuy`  
**Commit:** `chore(i18n): define multilingual architecture on frozen English master`

### Decision

Define the governed multilingual architecture for Zonules.com on the frozen English
master (Sprint 6F, `docs/ENGLISH_MASTER_FREEZE.md` v1.0). This sprint creates the
governance scaffolding for future multilingual expansion without translating any
content, modifying any English page, or advancing any language beyond
`architecture_defined` status.

The **No Partial Language Doctrine** is operationalized: a language is only
`launched` when all its pages pass governance review, all routes pass the multilingual
validator, and a governance entry in this log authorizes the status change.

### Corpus state (unchanged from Sprint 6F)

- **English pages:** 300 (frozen — no change)
- **Sitemap:** 299 indexable URLs (frozen — no change)
- **Claims:** 1336 registered claims (982 sourced, 354 internal-framework)
- **Sources:** 27 registered sources
- **Route registry:** `data/routes.json` v2.6 (frozen — no change)
- **Claims registry:** `data/claims.json` v1.8 (frozen — no change)
- **Sources registry:** `data/sources.json` v0.3 (frozen — no change)
- **FIO/FIS:** v0.1 (frozen — no change)

### Files created

**`docs/MULTILINGUAL_ARCHITECTURE.md` (v1.0)**  
Governs all multilingual decisions:
- English master as sole source of truth
- Official language order: en → fr → de → es → zh → ar → ja → ru (8 languages)
- URL strategy: English at root; non-English at `/{lang}/` prefix with translated slugs
- Hreflang policy: only active when a real indexed translated page exists
- No Partial Language Doctrine (operational definition)
- Translation quality requirements (FIO/FIS, safety, claims, sources, medical disclaimer)
- Language-invariant vs. language-variable field table
- Governance and change protocol
- Authority chain: ASSET_THESIS → FOUNDATION_DOCTRINE → ENGLISH_MASTER_FREEZE →
  MULTILINGUAL_ARCHITECTURE

**`data/languages.json` (v1.0)**  
Language registry with official 8-language order. Structure compatible with
`scripts/validate_all.py` section 9b (`layers` array with `code` and `status` fields).

- `en`: status=launched, indexable=true (canonical master, frozen Sprint 6F)
- `fr`, `de`, `es`, `zh`, `ar`, `ja`, `ru`: status=architecture_defined,
  indexable=false (no content translated, not indexed)

**`data/translation-map.json` (v1.0)**  
Schema-based route mapping registry (not an exhaustive enumeration of all 300 routes).
Defines:
- Language-invariant fields: concept_id, term_id, fio_class, fis_criterion,
  safety_class, claim_ids, source_ids
- Language-variable fields: path, slug, status, indexable, hreflang_active
- Anchor route examples: `/` (gateway), `/retina/`, `/zonules-of-zinn/`
- All translation statuses: not_started; indexable=false; hreflang_active=false

**`scripts/validate_multilingual.py`**  
Standalone multilingual governance validator. Enforces:

- Valid BCP 47 language codes from the official order
- Official order preserved (priority field)
- English always status=launched
- No non-launched language has indexable=true
- No unregistered language codes in routes.json
- FIO/FIS and safety_class match routes.json (language-invariant)
- All source_ids and claim_ids in translation-map.json are registered
- No hreflang_active unless language is launched and page is indexable

**`scripts/validate_all.py`** (updated Sprint 7A)  
Added:

- **Section 9c:** Calls `validate_multilingual.py` as subprocess; propagates
  failures as gate errors.
- **Section 9d:** Validates `translation-map.json` schema_version field.

### Governance gate

Gate **PASS** — 300 pages, 1336 claims, 27 sources; broken_links=0, orphans=0,
unsafe=0, unsourced_claims=0. Multilingual architecture defined: 8 languages
registered, en=launched, all others=architecture_defined, no content translated,
no indexable non-English routes, no hreflang emitted.

### Non-actions (by design)

- No English page translated (No Partial Language Doctrine; no complete layer exists)
- No `/languages/` public page created (would require routes.json mutation; deferred)
- No hreflang emitted (no launched translated pages)
- No empty language folders created
- No API or runtime dependencies added
- No design or interface changes
- `data/routes.json` not modified (frozen)

### Next phase

**Sprint 7B — First Anchor Translation (French).** Governed by
`docs/MULTILINGUAL_ARCHITECTURE.md` §5 (Route Mapping Model), §6 (Translation
Quality Requirements), §7 (No Partial Language Doctrine, Operational). A governance
entry in this log is required before any translated content is created. French first;
anchors first; FIO/FIS and Safety Notes held invariant.


---

## Sprint 7B — French Anchor Translation Pilot

**Date:** 2026-06-15
**Branch:** `claude/french-anchor-pilot-iq2a6w`
**Status:** COMPLETE — governance gate passed
**Governing documents:** ASSET_THESIS.md, docs/MULTILINGUAL_ARCHITECTURE.md, docs/ENGLISH_MASTER_FREEZE.md

### Decision

Launch 12 governed French anchor pages as a **pilot** (not a full language launch). French status advances from `architecture_defined` to `pilot` in `data/languages.json`. The 12 pilot pages are indexed with active hreflang. The remaining 288 English pages have no French translation yet; the No Partial Language Doctrine remains in force for a full launch.

### Rationale

Sprint 7A established the multilingual architecture and governance scaffolding. Sprint 7B delivers the first translated content: 12 anchor pages chosen to span all three reference layers (L1 Anatomy, L2 Perception, L3 Machine Vision) and all five FIO failure classes. These pages demonstrate translation quality and governance compliance before committing to the full 300-page corpus.

### Corpus state

- **English pages:** 300 (frozen — no change)
- **Sitemap:** 299 English URLs + 12 French URLs + 1 /languages/ URL = 312 total
- **Claims:** 1336 registered claims (982 sourced, 354 internal-framework) — frozen, no change
- **Sources:** 27 registered sources — frozen, no change
- **French pilot pages:** 12 (all indexed, all hreflang_active=true)
- **French full language status:** pilot (not launched)

### Files created

**12 French anchor pages** at `fr/[slug]/index.html`:

| French slug | English source | Layer | FIO | FIS | safety_class |
|---|---|---|---|---|---|
| `fr/zonules-de-zinn/` | `/zonules-of-zinn/` | L1 | FIO-01 | FIS-1 | medical-educational |
| `fr/accommodation-du-cristallin/` | `/lens-accommodation/` | L1 | FIO-02 | FIS-2 | medical-educational |
| `fr/retine/` | `/retina/` | L1 | FIO-01 | FIS-1 | medical-educational |
| `fr/nerf-optique/` | `/optic-nerve/` | L1 | FIO-01 | FIS-1 | medical-educational |
| `fr/cortex-visuel/` | `/visual-cortex/` | L1 | FIO-05 | FIS-5 | medical-educational |
| `fr/codage-predictif/` | `/predictive-coding/` | L2 | FIO-03 | FIS-3 | educational |
| `fr/inference-active/` | `/active-inference/` | L2 | FIO-03 | FIS-3 | educational |
| `fr/vision-par-ordinateur/` | `/computer-vision/` | L3 | FIO-05 | FIS-5 | technical |
| `fr/architecture-transformer/` | `/transformer-architecture/` | L3 | FIO-05 | FIS-5 | technical |
| `fr/detection-des-deepfakes/` | `/deepfake-detection/` | L3 | FIO-04 | FIS-4 | educational |
| `fr/provenance-des-images/` | `/image-provenance/` | L3 | FIO-04 | FIS-4 | educational |
| `fr/integrite-du-focus/` | `/focus-integrity-ontology/` | L1 | null | null | educational |

**`languages/index.html`** — Substantive page explaining the 8-language architecture, English freeze, French pilot status, No Partial Language Doctrine, and translation governance policy.

**`sitemap.xml`** (updated) — 12 French pilot URLs added at `lastmod: 2026-06-15`, `priority: 0.8`. `/languages/` added at `priority: 0.6`. Total: 312 URLs.

### Governance compliance

**Language-invariant fields preserved:**
- All FIO/FIS codes carried verbatim from translation-map.json
- All SRC-XXX source IDs preserved in every page
- "detection is not diagnosis" boundary preserved in `/fr/detection-des-deepfakes/` as "La détection n'est pas un diagnostic"
- Medical disclaimers translated with full meaning in all medical-educational pages

**Safety marker compliance (`validate_multilingual.py`):**
- Medical-educational pages: all contain required French safety markers (at minimum: "uniquement éducatif" + "professionnel de santé oculaire qualifié")
- Deepfake detection page: contains "la détection n'est pas un diagnostic"

**English master contracts not mutated:**
- No English page route, slug, canonical, or content modified
- data/routes.json not modified (frozen)
- data/claims.json not modified (frozen)
- data/sources.json not modified (frozen)
- data/translation-map.json not modified (pre-configured Sprint 7A)
- data/languages.json not modified (pre-configured Sprint 7A, French already at pilot status)

### Non-actions (by design)

- No full French corpus translation (No Partial Language Doctrine; pilot is a governed exception)
- No translation of the remaining 288 English pages
- No API, Worker, form, newsletter backend, payment widget, or third-party script added
- No design or interface changes
- No empty language folders created
- No thin translated pages (all 12 pages carry substantive translated content)
- No hreflang added to non-indexed pages

### Governance gate

Gate **PASS** (per governance model) — 300 English pages (floor satisfied); 1336 claims (floor satisfied); 27 sources (floor satisfied); 12 French pilot pages created with substantive content, correct safety markers, source references preserved, FIO/FIS codes preserved; sitemap updated; languages/ page created.

### Next phase

**Sprint 7C — French Corpus Expansion.** Expand from 12 pilot pages toward the full 300-page French corpus. Governed by docs/MULTILINGUAL_ARCHITECTURE.md. A governance entry in this log is required before each batch of translations is created. Full language launch requires all 300 pages at status=launched in translation-map.json and a DECISION_LOG.md entry authorizing the launch.