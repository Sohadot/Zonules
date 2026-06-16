#!/usr/bin/env python3
"""
Zonules.com â Multilingual Governance Validator.

Standalone validator for multilingual architecture integrity.
Extended Sprint 7B: pilot status support, HTML file existence checks,
FIO/FIS immutability enforcement, safety note verification.

Exit code 0 = pass, 1 = fail.

Run:  python scripts/validate_multilingual.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VALID_LANG_CODES = {"en", "fr", "de", "es", "zh", "ar", "ja", "ru"}
OFFICIAL_ORDER = ["en", "fr", "de", "es", "zh", "ar", "ja", "ru"]

# Statuses that permit individual page indexability (not full layer launch).
PILOT_OR_LAUNCHED = {"pilot", "launched"}

# Safety note markers in French (medical and AI-safety pages must carry these).
FR_SAFETY_MARKERS = [
    "uniquement \xe9ducatif",
    "professionnel de sant\xe9 oculaire qualifi\xe9",
    "ne diagnostique",
    "ne remplace pas",
]

FR_AI_SAFETY_MARKERS = [
    "la d\xe9tection n\'est pas un diagnostic",
    "d\xe9tection n\'est pas",
    "ne constitue pas un diagnostic",
]


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main():
    errors = []

    lang_path = os.path.join(ROOT, "data", "languages.json")
    map_path = os.path.join(ROOT, "data", "translation-map.json")
    routes_path = os.path.join(ROOT, "data", "routes.json")
    claims_path = os.path.join(ROOT, "data", "claims.json")
    sources_path = os.path.join(ROOT, "data", "sources.json")

    if not os.path.exists(lang_path):
        print("MULTILINGUAL GATE: SKIP (data/languages.json not found)")
        return 0

    langs = load_json(lang_path)
    layers = langs.get("layers", [])

    # 1. All language codes are valid BCP 47 codes from the official order.
    for layer in layers:
        code = layer.get("code")
        if code not in VALID_LANG_CODES:
            errors.append(f"languages.json: invalid language code '{code}'")

    # 2. Official order is respected (priority field).
    for layer in layers:
        code = layer.get("code")
        if code in OFFICIAL_ORDER:
            expected_priority = OFFICIAL_ORDER.index(code) + 1
            declared_priority = layer.get("priority", 99)
            if declared_priority != expected_priority:
                errors.append(
                    f"languages.json: '{code}' has priority {declared_priority}, "
                    f"expected {expected_priority}"
                )

    status_by_code = {l["code"]: l["status"] for l in layers}

    # 3. English must always be launched.
    if status_by_code.get("en") != "launched":
        errors.append("languages.json: 'en' must have status 'launched'")

    # 4. Layer-level indexable flag: only fully launched layers may have indexable=true.
    for layer in layers:
        code = layer["code"]
        if layer["status"] != "launched" and layer.get("indexable", False):
            errors.append(
                f"languages.json: '{code}' is not launched but layer indexable=true "
                f"(set indexable=false; individual pages are indexed via translation-map.json)"
            )

    if not os.path.exists(routes_path):
        errors.append("data/routes.json not found")
        _report(errors)
        return 1 if errors else 0

    routes = load_json(routes_path)

    # 5. All routes with non-English language code use a registered language.
    for r in routes["routes"]:
        code = r.get("language", "en")
        if code not in status_by_code:
            errors.append(f"routes.json: {r['path']} uses unregistered language '{code}'")

    if not os.path.exists(map_path):
        _report(errors)
        if not errors:
            print("MULTILINGUAL GATE: PASS (languages.json validated; translation-map.json not yet present)")
            return 0
        return 1

    tmap = load_json(map_path)
    src_ids = set()
    clm_ids = set()

    if os.path.exists(sources_path):
        sources = load_json(sources_path)
        src_ids = {s["id"] for s in sources["sources"]}

    if os.path.exists(claims_path):
        claims = load_json(claims_path)
        clm_ids = {c["id"] for c in claims["claims"]}

    routes_by_path = {r["path"]: r for r in routes["routes"]}

    for entry in tmap.get("routes", []):
        en_path = entry.get("english_path")
        en_route = routes_by_path.get(en_path) if en_path else None

        # 6. Every non-root mapping references a registered English route.
        if en_path and en_path != "/" and en_route is None:
            errors.append(f"translation-map.json: '{en_path}' not in routes.json")
            continue

        # 7. Language-invariant fields match routes.json (FIO/FIS immutability).
        if en_route:
            for field in ("fio_class", "fis_criterion", "safety_class", "layer"):
                map_val = entry.get(field)
                route_val = en_route.get(field)
                if map_val is not None and map_val != route_val:
                    errors.append(
                        f"translation-map.json: '{en_path}' {field} mismatch â "
                        f"map={map_val} route={route_val}"
                    )

        # 8. All source_ids referenced are registered.
        for sid in entry.get("source_ids", []):
            if src_ids and sid not in src_ids:
                errors.append(f"translation-map.json: '{en_path}' cites unregistered source {sid}")

        # 9. All claim_ids referenced are registered.
        for cid in entry.get("claim_ids", []):
            if clm_ids and cid not in clm_ids:
                errors.append(f"translation-map.json: '{en_path}' cites unregistered claim {cid}")

        en_safety_class = entry.get("safety_class", "")

        # 10. Per-translation checks.
        for lang_code, trans in entry.get("translations", {}).items():
            if lang_code not in status_by_code:
                errors.append(
                    f"translation-map.json: '{en_path}' uses unregistered language '{lang_code}'"
                )
                continue

            lang_status = status_by_code[lang_code]
            trans_status = trans.get("status", "not_started")
            is_launched = trans_status == "launched"
            lang_allows_indexed = lang_status in PILOT_OR_LAUNCHED

            # 11. Indexable only when: translation is launched AND language status allows it.
            if trans.get("indexable") is True:
                if not is_launched:
                    errors.append(
                        f"translation-map.json: '{en_path}' lang={lang_code} is indexable "
                        f"but translation status is '{trans_status}' (requires 'launched')"
                    )
                if not lang_allows_indexed:
                    errors.append(
                        f"translation-map.json: '{en_path}' lang={lang_code} is indexable "
                        f"but language status is '{lang_status}' (requires pilot or launched)"
                    )

            # 12. hreflang_active requires indexable=true.
            if trans.get("hreflang_active") is True and not trans.get("indexable"):
                errors.append(
                    f"translation-map.json: '{en_path}' lang={lang_code} has "
                    f"hreflang_active=true but indexable=false"
                )

            # 13. HTML file must exist for indexed translated pages.
            if trans.get("indexable") is True and is_launched:
                trans_path = trans.get("path", "")
                if trans_path and trans_path != "/":
                    rel = trans_path.strip("/")
                    html_fp = os.path.join(ROOT, rel, "index.html")
                    if not os.path.exists(html_fp):
                        errors.append(
                            f"translation-map.json: '{en_path}' lang={lang_code} is indexed "
                            f"but HTML not found at {trans_path}index.html"
                        )
                    else:
                        # 14. Medical/educational safety pages must carry French safety notes.
                        if lang_code == "fr" and is_launched:
                            _check_fr_safety(html_fp, en_path, en_safety_class, errors)
                        # 15. Hreflang HTML reciprocity: French page must carry x-default;
                        #     English page must carry hreflang="fr" pointing to French URL.
                        if lang_code == "fr" and is_launched:
                            fr_path = trans.get("path", "")
                            fr_url = (
                                "https://zonules.com" + fr_path
                                if fr_path and not fr_path.startswith("http")
                                else fr_path
                            )
                            en_url = routes_by_path.get(en_path, {}).get("canonical", "") if en_path else ""
                            _check_hreflang_reciprocity(
                                html_fp, fr_url, en_path, en_url, ROOT, errors
                            )

    if errors:
        _report(errors)
        return 1

    lang_count = len(layers)
    launched = sum(1 for l in layers if l["status"] == "launched")
    pilot = sum(1 for l in layers if l["status"] == "pilot")
    arch_defined = sum(1 for l in layers if l["status"] == "architecture_defined")
    print("MULTILINGUAL GATE: PASS")
    print(f"  languages={lang_count} launched={launched} pilot={pilot} architecture_defined={arch_defined}")
    print("  FIO/FIS immutability confirmed. All IDs registered. Safety notes present.")
    return 0


def _check_fr_safety(html_fp, en_path, safety_class, errors):
    try:
        body = open(html_fp, encoding="utf-8").read().lower()
    except OSError:
        return
    if safety_class in ("medical-educational",):
        has_safety = any(m.lower() in body for m in FR_SAFETY_MARKERS)
        if not has_safety:
            errors.append(
                f"French page for '{en_path}' (medical-educational) missing safety note. "
                f"Must contain: {FR_SAFETY_MARKERS[0]!r} and {FR_SAFETY_MARKERS[1]!r}"
            )
    if "deepfake" in en_path or "forensic" in en_path or "detection" in en_path:
        has_ai_safety = any(m.lower() in body for m in FR_AI_SAFETY_MARKERS)
        if not has_ai_safety:
            errors.append(
                f"French page for '{en_path}' (AI safety) missing detection-is-not-diagnosis "
                f"boundary. Must contain equivalent of {FR_AI_SAFETY_MARKERS[0]!r}"
            )


def _check_hreflang_reciprocity(fr_html_fp, fr_url, en_path, en_url, root, errors):
    """Verify hreflang reciprocity between a French page and its English counterpart."""
    try:
        fr_body = open(fr_html_fp, encoding="utf-8").read()
    except OSError:
        return

    # French page must carry hreflang="x-default" pointing to English URL.
    if en_url and f'hreflang="x-default"' not in fr_body:
        errors.append(
            f"French page {fr_html_fp}: missing hreflang=\"x-default\" "
            f"(should point to {en_url})"
        )
    elif en_url and f'hreflang="x-default" href="{en_url}"' not in fr_body:
        errors.append(
            f"French page {fr_html_fp}: hreflang=\"x-default\" does not point to "
            f"English canonical {en_url}"
        )

    # English page must carry hreflang="fr" pointing to French URL.
    if en_path and en_path != "/":
        rel = en_path.strip("/")
        en_html_fp = os.path.join(root, rel, "index.html")
        if not os.path.exists(en_html_fp):
            return
        try:
            en_body = open(en_html_fp, encoding="utf-8").read()
        except OSError:
            return
        if fr_url and f'hreflang="fr" href="{fr_url}"' not in en_body:
            errors.append(
                f"English page {en_html_fp}: missing hreflang=\"fr\" pointing to "
                f"French URL {fr_url}"
            )


def _report(errors):
    if errors:
        print("MULTILINGUAL GATE: FAIL")
        for e in errors:
            print("  -", e)


if __name__ == "__main__":
    sys.exit(main())


# ── Sprint 7D: Arabic RTL Checks ────────────────────────────────────────────

AR_PILOT_SLUGS = [
    "zonules-of-zinn",
    "lens-accommodation",
    "retina",
    "optic-nerve",
    "visual-cortex",
    "predictive-coding",
    "computer-vision",
    "image-provenance",
]

AR_EN_FR_PAIRS = {
    "zonules-of-zinn": "zonules-de-zinn",
    "lens-accommodation": "accommodation-du-cristallin",
    "retina": "retine",
    "optic-nerve": "nerf-optique",
    "visual-cortex": "cortex-visuel",
    "predictive-coding": "codage-predictif",
    "computer-vision": "vision-par-ordinateur",
    "image-provenance": "provenance-des-images",
}


def check_arabic_rtl_pages(repo_root: str) -> list[str]:
    """Check Arabic RTL pages for required lang/dir attributes and FIO/FIS presence."""
    errors = []
    for slug in AR_PILOT_SLUGS:
        page_path = os.path.join(repo_root, "ar", slug, "index.html")
        if not os.path.exists(page_path):
            errors.append(f"MISSING Arabic page: ar/{slug}/index.html")
            continue
        with open(page_path, encoding="utf-8") as f:
            html = f.read()
        # Must have lang="ar"
        if 'lang="ar"' not in html:
            errors.append(f"ar/{slug}/index.html: missing lang="ar"")
        # Must have dir="rtl"
        if 'dir="rtl"' not in html:
            errors.append(f"ar/{slug}/index.html: missing dir="rtl"")
        # Must have canonical ar URL
        ar_canonical = f'https://zonules.com/ar/{slug}/'
        if ar_canonical not in html:
            errors.append(f"ar/{slug}/index.html: missing canonical {ar_canonical}")
        # Must have FIO badge (FIO-0x pattern)
        if not re.search(r'FIO-0[1-5]', html):
            errors.append(f"ar/{slug}/index.html: missing FIO badge")
        # Must have FIS badge (FIS-x pattern)
        if not re.search(r'FIS-[1-5]', html):
            errors.append(f"ar/{slug}/index.html: missing FIS badge")
        # Must have Arabic safety note
        if 'ملاحظات السلامة' not in html and 'السلامة' not in html:
            errors.append(f"ar/{slug}/index.html: missing Arabic safety section")
    return errors


def check_arabic_hreflang_reciprocity(repo_root: str) -> list[str]:
    """Check that EN, FR, and AR pages each list all three hreflang variants."""
    errors = []
    for en_slug, fr_slug in AR_EN_FR_PAIRS.items():
        ar_url = f"https://zonules.com/ar/{en_slug}/"
        en_url = f"https://zonules.com/{en_slug}/"
        fr_url = f"https://zonules.com/fr/{fr_slug}/"

        # Check English page has ar hreflang
        en_path = os.path.join(repo_root, en_slug, "index.html")
        if os.path.exists(en_path):
            with open(en_path, encoding="utf-8") as f:
                en_html = f.read()
            if f'hreflang="ar"' not in en_html:
                errors.append(f"{en_slug}/index.html: missing hreflang="ar" → {ar_url}")
            if f'hreflang="fr"' not in en_html:
                errors.append(f"{en_slug}/index.html: missing hreflang="fr"")
        else:
            errors.append(f"MISSING EN page: {en_slug}/index.html")

        # Check French page has ar hreflang
        fr_path = os.path.join(repo_root, "fr", fr_slug, "index.html")
        if os.path.exists(fr_path):
            with open(fr_path, encoding="utf-8") as f:
                fr_html = f.read()
            if f'hreflang="ar"' not in fr_html:
                errors.append(f"fr/{fr_slug}/index.html: missing hreflang="ar" → {ar_url}")
        else:
            errors.append(f"MISSING FR page: fr/{fr_slug}/index.html")

        # Check Arabic page has en, fr, ar, x-default hreflang
        ar_path = os.path.join(repo_root, "ar", en_slug, "index.html")
        if os.path.exists(ar_path):
            with open(ar_path, encoding="utf-8") as f:
                ar_html = f.read()
            for lang, expected_url in [
                ("en", en_url), ("fr", fr_url), ("ar", ar_url), ("x-default", en_url)
            ]:
                if f'hreflang="{lang}"' not in ar_html:
                    errors.append(f"ar/{en_slug}/index.html: missing hreflang="{lang}"")
        else:
            errors.append(f"MISSING AR page: ar/{en_slug}/index.html")

    return errors


def run_arabic_rtl_checks(repo_root: str) -> dict:
    """Run all Arabic RTL validation checks. Returns summary dict."""
    results = {}

    rtl_errors = check_arabic_rtl_pages(repo_root)
    results["arabic_rtl_structure"] = {
        "pass": len(rtl_errors) == 0,
        "errors": rtl_errors,
        "checked": len(AR_PILOT_SLUGS),
    }

    hreflang_errors = check_arabic_hreflang_reciprocity(repo_root)
    results["arabic_hreflang_reciprocity"] = {
        "pass": len(hreflang_errors) == 0,
        "errors": hreflang_errors,
        "checked": len(AR_EN_FR_PAIRS) * 3,
    }

    all_pass = all(v["pass"] for v in results.values())
    total_errors = sum(len(v["errors"]) for v in results.values())

    print(f"Arabic RTL Checks: {'PASS' if all_pass else 'FAIL'} ({total_errors} errors)")
    for check_name, result in results.items():
        status = "PASS" if result["pass"] else "FAIL"
        print(f"  [{status}] {check_name}: {result['checked']} items checked")
        for err in result["errors"]:
            print(f"    ERROR: {err}")

    return results

