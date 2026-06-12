#!/usr/bin/env python3
"""
Zonules.com — Governance Quality Gate.

Blocking validator. Exit code 0 = pass, 1 = fail.
Enforces the non-negotiables from the Sovereign Asset System Foundation
Doctrine against the governed registries and content units.

Run:  python scripts/validate_all.py
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as fh:
        return json.load(fh)


def main():
    routes = load("routes.json")
    claims = load("claims.json")
    sources = load("sources.json")

    src_ids = {s["id"] for s in sources["sources"]}
    clm_ids = {c["id"] for c in claims["claims"]}
    clm_by_id = {c["id"]: c for c in claims["claims"]}
    route_paths = {r["path"] for r in routes["routes"]}
    errors = []

    # 1. Every claim resolves to a registered source (No Ungoverned Claims).
    for c in claims["claims"]:
        for s in c["sources"]:
            if s not in src_ids:
                errors.append(f"claim {c['id']} cites unregistered source {s}")

    for r in routes["routes"]:
        path = r["path"]
        page_type = r.get("page_type", "reference-unit")
        content_path = os.path.join(ROOT, r["content"])

        # 2. Registered content file must exist (No Phantom Surfaces).
        if not os.path.exists(content_path):
            errors.append(f"{path} missing content file {r['content']}")
            continue
        body = open(content_path, encoding="utf-8").read()

        # 3. Route source/claim requirements are registered.
        for s in r["source_requirements"]:
            if s not in src_ids:
                errors.append(f"{path} requires unregistered source {s}")
        for cl in r["claim_requirements"]:
            if cl not in clm_ids:
                errors.append(f"{path} requires unregistered claim {cl}")

        # 5. Required internal links resolve (No Broken Structure).
        for link in r["required_internal_links"]:
            if link not in route_paths:
                errors.append(f"{path} required link to unregistered route {link}")

        # 7. Canonical matches path; metadata present.
        if not r["canonical"].endswith(path):
            errors.append(f"{path} canonical mismatch")
        if len(r.get("meta_description", "")) < 50:
            errors.append(f"{path} meta_description too short or missing")

        if page_type in ("engine", "gateway", "acquire"):
            # Generated pages (not markdown units): validate their internal links resolve.
            for href in re.findall(r'href="(/[a-z0-9-]*/?)"', body):
                if href not in route_paths:
                    errors.append(f"{path} {page_type} links to unregistered route {href}")
            if page_type == "engine":
                if "qualified eye-care professional" not in body:
                    errors.append(f"{path} engine missing medical guard text")
                if "no input left your device" not in body.lower():
                    errors.append(f"{path} engine missing local-only provenance statement")
            if page_type == "gateway":
                if "what makes vision possible" not in body:
                    errors.append(f"{path} gateway missing the governing sentence")
            if page_type == "acquire":
                # ACQUISITION_POSTURE.md: show the structure, never beg for the sale.
                low = body.lower()
                banned = ["buy now", "act now", "act fast", "limited time", "limited offer",
                          "hurry", "don't miss", "won't last", "best price", "discount",
                          "make an offer", "highest bidder", "auction", "for sale", "best offer"]
                for phrase in banned:
                    if phrase in low:
                        errors.append(f"{path} acquisition surface contains banned phrase '{phrase}'")
                if re.search(r"\$\s?\d|\b\d[\d,]*\s?(?:usd|eur|dollars)\b", low):
                    errors.append(f"{path} acquisition surface contains a price/valuation figure")
                if "noindex" not in low:
                    errors.append(f"{path} acquisition surface must be noindex")
        else:
            # 4. Every claim cited in the body is registered; sourced claims are used.
            refs = set(re.findall(r"CLM-\d+", body))
            for ref in refs:
                if ref not in clm_ids:
                    errors.append(f"{path} cites unregistered claim {ref}")
            for cl in r["claim_requirements"]:
                c = clm_by_id.get(cl)
                if c and c["status"] == "sourced" and cl not in refs:
                    errors.append(f"{path} sourced claim {cl} not used in body")
                if c and c["page"] != path:
                    errors.append(f"claim {cl} page mismatch ({c['page']} != {path})")

            # 6. Markdown body links resolve.
            for href in re.findall(r"]\((/[a-z0-9-]+/)\)", body):
                if href not in route_paths:
                    errors.append(f"{path} body links to unregistered route {href}")

            # 8. Safety classification (class-aware).
            if "## Safety Notes" not in body:
                errors.append(f"{path} missing Safety Notes section")
            if r["safety_class"] == "medical-educational" and "qualified eye-care professional" not in body:
                errors.append(f"{path} medical page missing eye-care disclaimer")

    # 9. No orphans: every page is linked to by at least one other page.
    #    The root gateway is the entry point, reached directly, and is exempt.
    linked = {link for r in routes["routes"] for link in r["required_internal_links"]}
    for r in routes["routes"]:
        if r["path"] == "/" or r.get("page_type") == "gateway":
            continue
        if r["path"] not in linked:
            errors.append(f"orphan page (no inbound link): {r['path']}")

    # 10a. Engine integrity: every FIO class-link resolves; engine page is fresh.
    engine_path = os.path.join(ROOT, "data", "focus-integrity-engine.json")
    if os.path.exists(engine_path):
        fie = load("focus-integrity-engine.json")
        if not fie.get("determinism_note"):
            errors.append("engine config missing determinism_note")
        for cls, links in fie.get("class_links", {}).items():
            for link in links:
                if link not in route_paths:
                    errors.append(f"engine class {cls} links to unregistered route {link}")
    # 10b. Generated pages must be freshly built from their governed sources.
    for builder_name in ("build_engine.py", "build_gateway.py", "build_acquire.py", "generate_sitemap.py"):
        builder = os.path.join(ROOT, "scripts", builder_name)
        if os.path.exists(builder):
            res = subprocess.run([sys.executable, builder, "--check"],
                                 capture_output=True, text=True)
            if res.returncode != 0:
                errors.append(f"{builder_name}: " + res.stdout.strip())

    # 10. Static-security scan of content and data (No Hidden Infrastructure).
    # The generated engine page legitimately contains reviewed inline JS/CSS and
    # is excluded from this markdown-surface scan; its integrity is covered by 10a.
    unsafe = re.compile(r"<script|onerror=|onclick=|javascript:|http://|api[_-]?key|BEGIN .*PRIVATE KEY", re.I)
    for base in ("content", "data"):
        for dirpath, _dirs, files in os.walk(os.path.join(ROOT, base)):
            for fn in files:
                fp = os.path.join(dirpath, fn)
                try:
                    text = open(fp, encoding="utf-8").read()
                except (UnicodeDecodeError, OSError):
                    continue
                if unsafe.search(text):
                    errors.append(f"unsafe pattern in {os.path.relpath(fp, ROOT)}")

    if errors:
        print("GOVERNANCE GATE: FAIL")
        for e in errors:
            print("  -", e)
        return 1

    layers = sorted({r["layer"] for r in routes["routes"]})
    print("GOVERNANCE GATE: PASS")
    print(f"  pages={len(routes['routes'])} claims={len(claims['claims'])} "
          f"sources={len(src_ids)} layers={layers}")
    print("  broken_links=0 orphans=0 unsafe=0 unsourced_claims=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
