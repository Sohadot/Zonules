#!/usr/bin/env python3
"""
Zonules.com — Multilingual Governance Validator.

Standalone validator for multilingual architecture integrity.
Exit code 0 = pass, 1 = fail.

Run:  python scripts/validate_multilingual.py
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VALID_LANG_CODES = {"en", "fr", "de", "es", "zh", "ar", "ja", "ru"}
OFFICIAL_ORDER = ["en", "fr", "de", "es", "zh", "ar", "ja", "ru"]


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

    # 4. No non-launched language has indexable=true.
    for layer in layers:
        code = layer["code"]
        if layer["status"] != "launched" and layer.get("indexable", False):
            errors.append(
                f"languages.json: '{code}' is not launched but indexable=true"
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

        # 7. Language-invariant fields match routes.json.
        if en_route:
            for field in ("fio_class", "fis_criterion", "safety_class", "layer"):
                map_val = entry.get(field)
                route_val = en_route.get(field)
                if map_val is not None and map_val != route_val:
                    errors.append(
                        f"translation-map.json: '{en_path}' {field} mismatch — "
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

        # 10. Per-translation checks.
        for lang_code, trans in entry.get("translations", {}).items():
            if lang_code not in status_by_code:
                errors.append(
                    f"translation-map.json: '{en_path}' uses unregistered language '{lang_code}'"
                )
                continue

            lang_status = status_by_code[lang_code]

            # 11. indexable must be false unless language is launched.
            if trans.get("indexable") is True and lang_status != "launched":
                errors.append(
                    f"translation-map.json: '{en_path}' lang={lang_code} is indexable "
                    f"but language status is '{lang_status}'"
                )

            # 12. hreflang_active must be false unless language is launched and page is indexable.
            if trans.get("hreflang_active") is True:
                if lang_status != "launched":
                    errors.append(
                        f"translation-map.json: '{en_path}' lang={lang_code} has "
                        f"hreflang_active=true but language is not launched"
                    )
                if not trans.get("indexable"):
                    errors.append(
                        f"translation-map.json: '{en_path}' lang={lang_code} has "
                        f"hreflang_active=true but indexable=false"
                    )

    if errors:
        _report(errors)
        return 1

    lang_count = len(layers)
    launched = sum(1 for l in layers if l["status"] == "launched")
    arch_defined = sum(1 for l in layers if l["status"] == "architecture_defined")
    print("MULTILINGUAL GATE: PASS")
    print(f"  languages={lang_count} launched={launched} architecture_defined={arch_defined}")
    print("  No indexable non-launched layers. No hreflang violations. All IDs registered.")
    return 0


def _report(errors):
    if errors:
        print("MULTILINGUAL GATE: FAIL")
        for e in errors:
            print("  -", e)


if __name__ == "__main__":
    sys.exit(main())
