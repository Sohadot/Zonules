# PUBLICATION_ARCHITECTURE.md

**Zonules.com — Public Site Publication Architecture and Migration Plan**
**Sohadot Portfolio · agent@sohadot.com**
**Version 0.1 — 2026-10-26 (Sprint 8C)**
**Governing documents:** `ASSET_THESIS.md` · `DECISION_LOG.md`

---

## Why internal documents were served

GitHub Pages is configured as **Deploy from a branch: `main` / (root)**, run by GitHub's built-in `pages-build-deployment` workflow. The repository root is therefore the published site. `.nojekyll` disables Jekyll processing, so every file in the root tree is served as-is. On 2026-10-26, `https://zonules.com/ASSET_THESIS.md`, `/ASSET_INTELLIGENCE_FACTORY_PLAN.md`, `/ACQUISITION_POSTURE.md`, `/DECISION_LOG.md`, `/docs/…`, and `/data/claims.json` all returned HTTP 200.

## New architecture (smallest safe change)

The build model is unchanged: generators still write the site into the repository root, and the root stays a complete, valid site (this is what makes rollback instant). What changes is **what is deployed**:

1. `scripts/build_public_site.py` copies only approved public files into `_site/`:
   - `index.html` for every approved route in `data/routes.json` (300),
   - `index.html` for every launched translation in `data/translation-map.json` (108),
   - `/languages/index.html`,
   - `CNAME`, `robots.txt`, `sitemap.xml`, `assets/css/reference.css`.
   Total: 413 files, identical bytes to the pages served today.
2. `scripts/validate_publication.py` checks the artifact **independently** against an explicit allowlist, a denylist (Markdown, Python, JSON, YAML, JS sources, internal directories), completeness against the registries, link/sitemap/hreflang integrity inside the artifact, and internal-strategy text markers. Any violation fails the deployment. It also runs inside `scripts/validate_all.py`.
3. `.github/workflows/publish-site.yml` runs all gates, assembles `_site/`, re-validates it, and deploys it with GitHub's official Pages actions. It triggers only on push to `main` or manual dispatch, and the deploy step runs only when the repository variable `PAGES_PUBLISH_MODE` equals `actions`. Until the owner sets that variable, the workflow builds and validates but deploys nothing.

No runtime dependency is added: the published site is the same static HTML and CSS. The workflow uses only GitHub's own actions (`actions/checkout`, `actions/upload-pages-artifact`, `actions/deploy-pages`).

## What will be public on zonules.com after migration

Exactly the 413 allowlisted files: the gateway, the engine, `/acquire/` (still `noindex`), 290 reference units, the policy, glossary, and ontology pages, 100 French and 8 Arabic pages, `/languages/`, the shared stylesheet, `sitemap.xml`, `robots.txt`, and `CNAME`. URLs, canonical tags, hreflang, structured data, and page bytes are unchanged.

No longer served: all root Markdown (thesis, plans, posture, decision log, README, reference architecture), `docs/`, `data/`, `scripts/`, `content/`, `static/`, `.github/`, `.nojekyll`.

## What remains visible through GitHub

**The website change does not make anything private.** The repository `Sohadot/Zonules` is public. Every file listed above, and every earlier version of it, remains readable on github.com, in clones and forks, and in any archive or cache that has already captured it. Removing a file from the website, or even from the current branch, does not remove it from Git history.

## Recommended source-repository privacy arrangement (owner decision)

Safest arrangement, in order of preference — check what the account's plan supports before choosing:

1. **Private source repository + separate public publication.** Make `Sohadot/Zonules` private and publish the artifact to Pages from it. GitHub Pages from a private repository requires a paid GitHub plan (Pro, Team, or Enterprise) for the owning account; confirm this for the account first. Making the repository private does not recall copies already cloned, forked, or cached.
2. **Private source repository + public artifact-only repository.** Keep governance in a private repository and push only `_site/` to a separate public repository that serves Pages. Works on free plans; adds a cross-repository deploy step and a token secret.
3. **Status quo (public repository, artifact-only website).** Acceptable if the governance record is intended to be inspectable by buyers. In that case keep pricing, negotiation, and buyer-specific material out of the repository permanently.

Do not rewrite history to remove files: it breaks the governance record, does not reach existing copies, and is not needed for any of the options above.

## Migration plan

**Preconditions:** the feature branch is merged to `main` (on merge, the legacy branch deployment publishes the updated root as it does today — internal files still served at that moment). The new workflow's first run on `main` builds and validates only.

**Steps (owner, in GitHub settings; do 2–4 back to back):**

1. Confirm the `Publish site` workflow's validation run on `main` is green (Actions tab).
2. Settings → Pages → Build and deployment → Source: change **Deploy from a branch** to **GitHub Actions**. Leave the custom domain `zonules.com` and **Enforce HTTPS** as they are.
3. Settings → Secrets and variables → Actions → Variables: add `PAGES_PUBLISH_MODE` = `actions`.
4. Actions → Publish site → Run workflow on `main`. Wait for the `deploy` job to succeed.
5. Verify: `/`, `/acquire/`, `/focus-integrity-engine/`, `/zonules-of-zinn/`, `/fr/zonules-de-zinn/`, `/ar/zonules-of-zinn/`, `/languages/`, `/sitemap.xml` return 200; `/ASSET_THESIS.md`, `/DECISION_LOG.md`, `/data/claims.json`, `/docs/PUBLICATION_ARCHITECTURE.md` return 404.
6. Cloudflare (if proxying with caching): purge the cached URLs of the removed files (or purge everything). DNS records do not change.

**Downtime risk:** low. Between steps 2 and 4 the previously deployed site normally continues to be served; if Pages briefly reports no deployment, completing step 4 resolves it. The custom-domain setting is stored in repository settings and survives the source change; the `CNAME` file is still included in the artifact. A failed gate in step 4 deploys nothing and leaves the last deployment live.

**Rollback (minutes):** Settings → Pages → Source → **Deploy from a branch**, `main`, `/ (root)`, then delete or change `PAGES_PUBLISH_MODE`. The root still contains the complete generated site, so the legacy builder republishes the previous behaviour exactly (internal files served again).
