# PUBLICATION_ARCHITECTURE.md

**Zonules.com — Private Source / Public Publication Architecture and Cutover Runbook**
**Sohadot Portfolio · agent@sohadot.com**
**Version 0.2 — 2026-10-26 (Sprint 8D; supersedes v0.1, Sprint 8C)**
**Governing documents:** `ASSET_THESIS.md` · `DECISION_LOG.md`

---

## Decision

Internal Zonules.com files must not remain accessible in any public GitHub repository. Publishing an allowlisted artifact from a public source repository (v0.1) was necessary but not sufficient.

| Repository | Visibility (target) | Contents | History |
|---|---|---|---|
| `Sohadot/Zonules` | **Private** | Everything: source, governance, registries, decision log, strategy, scripts, generated site, all branches | Full, unchanged, never rewritten |
| `Sohadot/zonules-public` | **Public**, GitHub Pages | Only the 414-file allowlisted artifact | Independent; created empty; only `zonules-publisher` commits |

## Audit (2026-10-26)

- **Pages:** `Sohadot/Zonules`, legacy "Deploy from a branch" (`main` / root) with `.nojekyll`; every repository file is served. One workflow exists (GitHub's dynamic `pages-build-deployment`); all 29 runs were on `main`; feature-branch pushes trigger nothing.
- **Domain and DNS:** `zonules.com` nameservers are Cloudflare; apex A/AAAA records are Cloudflare-proxied (orange cloud), with GitHub Pages as origin. There is no `www` record. **No GitHub account-level verified-domain TXT record** (`_github-pages-challenge-Sohadot.zonules.com`) exists.
- **Access:** the only collaborator on `Sohadot/Zonules` is the owner (admin).
- **Forks:** `forks_count` = 0 and a fork search for "zonules" returns none.
- **Secrets in history:** a pattern scan of all 113 commits found no credentials or private keys. Author emails are `agent@sohadot.com` (already public on the owner's profile) and `noreply@anthropic.com`.
- **`Sohadot/zonules-public`:** does not exist yet. The session's GitHub integration cannot create repositories (HTTP 403), so the owner creates it.

## Publication pipeline

1. `scripts/build_public_site.py` assembles the allowlisted artifact: 300 route pages, 108 launched translations, `/languages/`, `CNAME`, `.nojekyll`, `robots.txt`, `sitemap.xml`, `assets/css/reference.css`.
2. `scripts/validate_publication.py` (blocking) enforces the explicit allowlist, a denylist, completeness, in-artifact link/sitemap/hreflang integrity, and strategy-marker absence. `--repo` mode validates a checkout of the public repository, skipping only its own `.git`.
3. `scripts/publish_public_repo.py` is the only path into the public repository. It:
   - refuses unless the checkout's configured origin is exactly `github.com/Sohadot/zonules-public`, and never prints embedded credentials;
   - refuses if any public commit also exists in the source repository;
   - replaces the working tree (never `.git`) with the artifact and re-validates the exact tree;
   - commits as `zonules-publisher` with a neutral message that contains no source hash;
   - never pushes.
4. `.github/workflows/publish-site.yml` (in the private repository):
   - **build** job: all gates, assemble, re-validate, retain the artifact privately for 90 days.
   - **publish** job (only on `main`, only when the variable `PUBLIC_PUBLISH_MODE=repo` is set): clones the public repository with a write deploy key scoped to that single repository (`PUBLIC_SITE_DEPLOY_KEY`), pins GitHub's published SSH host key, runs the publisher, makes a normal fast-forward push of the public checkout, and deletes the key.
   - No mirror push, no force push, no push from the source tree. A non-fast-forward is rejected, not overridden.

**Least privilege:** a repository deploy key can read and write `Sohadot/zonules-public` only; it cannot reach `Sohadot/Zonules` or any other repository and carries no account scope. Rotate it by replacing both halves. (A GitHub App installed only on `zonules-public` with `contents: write` is an equivalent alternative.)

## What will be public, and what will not

- **Public:** `zonules.com` and `github.com/Sohadot/zonules-public`. Both expose the same 414 static files (the website itself) and the publisher commit history (timestamps only).
- **Private after cutover:** all of `Sohadot/Zonules` — governance documents, thesis, plans, acquisition posture, decision log, research registries, content sources, scripts, workflows, branches, and the full history.
- **Not access control:** `robots.txt` and `noindex` only ask crawlers not to index. `/acquire/` is public by design and is reachable by anyone with the URL.

## Unavoidable historical exposure

`Sohadot/Zonules` has been public since 2026-05-17, and its files have been served at `zonules.com/<path>` since Pages was enabled. Making it private does **not** recall copies already made. Assume that anything ever pushed may persist in:

- personal clones (unknown);
- public web and code archives (for example the Wayback Machine, Software Heritage, Common Crawl);
- search-engine and Cloudflare caches;
- datasets derived from public repositories.

No public forks exist; if one had existed, making the parent private would detach it, and it would stay public. No credentials were found in history, so no rotation is required.

## Cutover runbook

### Phase 1 — Preparation (no production effect; owner actions)

1. **Verify the domain at account level (takeover protection).** In GitHub, go to profile Settings → Pages → *Add a verified domain* → `zonules.com`. Add the shown TXT record `_github-pages-challenge-Sohadot.zonules.com` in Cloudflare. It is additive, DNS-only, and does not affect traffic. Complete verification. This prevents any other account from claiming `zonules.com` while it is briefly unassigned during cutover.
2. **Create `Sohadot/zonules-public`:** owner account, **Private for now**, completely empty (no README, licence, or .gitignore).
3. **Create the deploy key** on a trusted machine: `ssh-keygen -t ed25519 -N "" -C zonules-public-deploy -f zonules_public_deploy`.
   - In `zonules-public` → Settings → Deploy keys → Add: paste `zonules_public_deploy.pub` and tick **Allow write access**.
   - In `Zonules` → Settings → Secrets and variables → Actions → New repository secret `PUBLIC_SITE_DEPLOY_KEY`: paste the private key.
   - Securely delete both local key files.
4. **Approve and merge** the feature branch into `Zonules/main`. The legacy branch deployment republishes the root exactly as today. The workflow's build job runs validation only.
5. **First publish:** add the repository variable `PUBLIC_PUBLISH_MODE` = `repo`, then Actions → Publish site → Run workflow on `main`. Expect one commit by `zonules-publisher` and 414 files in `zonules-public`.
6. **Check the cutover settings.**
   - Cloudflare SSL/TLS mode: if it is **Full (strict)**, set it to **Full** for the cutover window. While GitHub issues the certificate for the new repository, the origin briefly presents a `*.github.io` certificate.
   - Note the current Pages settings of `Zonules` (custom domain, HTTPS) for rollback.

### Phase 2 — Cutover (production; do steps 7–9 back to back, about 5 minutes)

7. `zonules-public` → Settings → General → Change visibility → **Public**.
8. `Zonules` → Settings → Pages → Custom domain → **Remove**. `zonules.com` returns a GitHub 404 from this moment until step 9 completes.
9. `zonules-public` → Settings → Pages → Source: **Deploy from a branch**, `main`, `/ (root)` → Save. Custom domain: `zonules.com` → Save. Tick **Enforce HTTPS** once the certificate is issued.
10. Purge the Cloudflare cache (everything).
11. **Verify:**
    - These return 200: `/`, `/acquire/`, `/focus-integrity-engine/`, `/zonules-of-zinn/`, `/fr/zonules-de-zinn/`, `/ar/zonules-of-zinn/`, `/languages/`, `/sitemap.xml`, `/assets/css/reference.css`.
    - These return 404: `/ASSET_THESIS.md`, `/ASSET_INTELLIGENCE_FACTORY_PLAN.md`, `/DECISION_LOG.md`, `/README.md`, `/data/claims.json`, `/docs/PUBLICATION_ARCHITECTURE.md`, `/scripts/build_site.py`.
    - Spot-check canonical tags, hreflang, and the engine's worked examples.
12. If step 6 changed it, return Cloudflare SSL to **Full (strict)** once the GitHub certificate is valid.

### Phase 3 — Privatize the source repository (irreversible in effect)

13. `Zonules` → Settings → Pages: set Source to **None** (or Unpublish) so no legacy deployment remains.
14. `Zonules` → Settings → General → Change visibility → **Private**.
15. Confirm `zonules.com` still serves (it now comes from `zonules-public`).
16. Signed out, confirm that `github.com/Sohadot/Zonules` and `raw.githubusercontent.com/Sohadot/Zonules/main/ASSET_THESIS.md` return 404.
17. Push a trivial change to `Zonules/main`, or re-run the workflow, and confirm a new publisher commit appears in `zonules-public`. Secrets and variables survive the visibility change. Private-repository Actions minutes count against the plan's quota.

**Downtime:** about 1–5 minutes of 404 between steps 8 and 9, plus possible HTTPS errors until the certificate is issued (mitigated by step 6). DNS never changes, because both repositories belong to the same account.

## Rollback

- **During Phase 2, before privatization:** remove the custom domain from `zonules-public` and re-add `zonules.com` to `Zonules` Pages. That repository is still public at this point, so nothing is republished.
- **After privatization** (the internal repository is never made public again):
  - *Bad content:* revert in `Zonules` and push, so the workflow republishes; or revert the publisher commit directly in `zonules-public` (`git revert`, normal push).
  - *Pipeline failure:* download the retained `zonules-public-site` artifact from a previous successful run (private, 90 days) and commit it to `zonules-public` manually. Then run `scripts/validate_publication.py --repo` on that checkout.
  - *Pages or host failure:* the same artifact can be served by any static host behind Cloudflare. It has no runtime dependencies.

## Governance

The public allowlist and this architecture are governed publication decisions; changing either requires a `DECISION_LOG.md` entry. The root-publication doctrine checks in `validate_all.py` are retained: they keep the generated site complete in the source tree, which the artifact builder requires.
