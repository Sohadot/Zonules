#!/usr/bin/env python3
"""
Zonules.com multilingual governance validator.

Exit code 0 = pass, 1 = fail.

Run: python scripts/validate_multilingual.py
"""
import html
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://zonules.com"

VALID_LANG_CODES = {"en", "fr", "de", "es", "zh", "ar", "ja", "ru"}
OFFICIAL_ORDER = ["en", "fr", "de", "es", "zh", "ar", "ja", "ru"]
PILOT_OR_LAUNCHED = {"pilot", "launched"}

FR_SAFETY_MARKERS = [
    "uniquement \u00e9ducatif",
    "professionnel de sant\u00e9 oculaire qualifi\u00e9",
    "ne diagnostique",
    "ne remplace pas",
]

FR_AI_SAFETY_MARKERS = [
    "la d\u00e9tection n'est pas un diagnostic",
    "la d\u00e9tection n\u2019est pas un diagnostic",
    "d\u00e9tection n'est pas",
    "d\u00e9tection n\u2019est pas",
    "ne constitue pas un diagnostic",
]

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


class StatusTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_td = False
        self.current_cell = []
        self.current_row = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == "td":
            self.in_td = True
            self.current_cell = []

    def handle_data(self, data):
        if self.in_td:
            self.current_cell.append(data)

    def handle_endtag(self, tag):
        if tag == "td" and self.in_td:
            text = " ".join("".join(self.current_cell).split())
            self.current_row.append(html.unescape(text))
            self.in_td = False
        elif tag == "tr":
            if len(self.current_row) == 4:
                self.rows.append(self.current_row)
            self.current_row = []


class LinkTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.current_href = None
        self.current_text = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.current_href = dict(attrs).get("href")
            self.current_text = []

    def handle_data(self, data):
        if self.current_href is not None:
            self.current_text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.current_href is not None:
            text = " ".join("".join(self.current_text).split())
            self.links.append((self.current_href, html.unescape(text)))
            self.current_href = None
            self.current_text = []


def load_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def read_text(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


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
    layers_by_code = {layer.get("code"): layer for layer in layers}
    status_by_code = {code: layer.get("status") for code, layer in layers_by_code.items()}

    _check_language_registry(layers, status_by_code, errors)

    if not os.path.exists(routes_path):
        errors.append("data/routes.json not found")
        _report(errors)
        return 1 if errors else 0

    routes = load_json(routes_path).get("routes", [])
    routes_by_path = {r["path"]: r for r in routes}

    for route in routes:
        code = route.get("language", "en")
        if code not in status_by_code:
            errors.append(f"routes.json: {route['path']} uses unregistered language '{code}'")

    if not os.path.exists(map_path):
        _report(errors)
        if not errors:
            print("MULTILINGUAL GATE: PASS (languages.json validated; translation-map.json not yet present)")
            return 0
        return 1

    tmap = load_json(map_path)
    src_ids = _load_ids(sources_path, "sources")
    clm_ids = _load_ids(claims_path, "claims")

    _check_translation_map(tmap, routes_by_path, status_by_code, src_ids, clm_ids, errors)
    _check_registry_page_counts(layers_by_code, routes, tmap, errors)
    _check_languages_page(layers_by_code, routes, errors)
    _check_arabic_rtl_pages(errors)
    _check_arabic_hreflang_reciprocity(errors)
    _check_sitemap_hreflang_groups(tmap, errors)

    if errors:
        _report(errors)
        return 1

    lang_count = len(layers)
    launched = sum(1 for l in layers if l["status"] == "launched")
    pilot = sum(1 for l in layers if l["status"] == "pilot")
    arch_defined = sum(1 for l in layers if l["status"] == "architecture_defined")
    print("MULTILINGUAL GATE: PASS")
    print(f"  languages={lang_count} launched={launched} pilot={pilot} architecture_defined={arch_defined}")
    print("  language page counts, FIO/FIS immutability, safety notes, RTL checks, and sitemap hreflang groups confirmed.")
    return 0


def _load_ids(path, key):
    if not os.path.exists(path):
        return set()
    data = load_json(path)
    return {item["id"] for item in data.get(key, [])}


def _check_language_registry(layers, status_by_code, errors):
    for layer in layers:
        code = layer.get("code")
        if code not in VALID_LANG_CODES:
            errors.append(f"languages.json: invalid language code '{code}'")
        if code in OFFICIAL_ORDER:
            expected_priority = OFFICIAL_ORDER.index(code) + 1
            declared_priority = layer.get("priority", 99)
            if declared_priority != expected_priority:
                errors.append(
                    f"languages.json: '{code}' has priority {declared_priority}, expected {expected_priority}"
                )

    if status_by_code.get("en") != "launched":
        errors.append("languages.json: 'en' must have status 'launched'")

    for layer in layers:
        code = layer["code"]
        if layer["status"] != "launched" and layer.get("indexable", False):
            errors.append(
                f"languages.json: '{code}' is not launched but layer indexable=true "
                "(set indexable=false; individual pages are indexed via translation-map.json)"
            )


def _check_translation_map(tmap, routes_by_path, status_by_code, src_ids, clm_ids, errors):
    for entry in tmap.get("routes", []):
        en_path = entry.get("english_path")
        en_route = routes_by_path.get(en_path) if en_path else None

        if en_path and en_path != "/" and en_route is None:
            errors.append(f"translation-map.json: '{en_path}' not in routes.json")
            continue

        if en_route:
            for field in ("fio_class", "fis_criterion", "safety_class", "layer"):
                map_val = entry.get(field)
                route_val = en_route.get(field)
                if map_val is not None and map_val != route_val:
                    errors.append(
                        f"translation-map.json: '{en_path}' {field} mismatch: "
                        f"map={map_val} route={route_val}"
                    )

        for sid in entry.get("source_ids", []):
            if src_ids and sid not in src_ids:
                errors.append(f"translation-map.json: '{en_path}' cites unregistered source {sid}")

        for cid in entry.get("claim_ids", []):
            if clm_ids and cid not in clm_ids:
                errors.append(f"translation-map.json: '{en_path}' cites unregistered claim {cid}")

        for lang_code, trans in entry.get("translations", {}).items():
            if lang_code not in status_by_code:
                errors.append(f"translation-map.json: '{en_path}' uses unregistered language '{lang_code}'")
                continue

            lang_status = status_by_code[lang_code]
            trans_status = trans.get("status", "not_started")
            is_launched = trans_status == "launched"

            if trans.get("indexable") is True:
                if not is_launched:
                    errors.append(
                        f"translation-map.json: '{en_path}' lang={lang_code} is indexable "
                        f"but translation status is '{trans_status}' (requires 'launched')"
                    )
                if lang_status not in PILOT_OR_LAUNCHED:
                    errors.append(
                        f"translation-map.json: '{en_path}' lang={lang_code} is indexable "
                        f"but language status is '{lang_status}' (requires pilot or launched)"
                    )

            if trans.get("hreflang_active") is True and not trans.get("indexable"):
                errors.append(
                    f"translation-map.json: '{en_path}' lang={lang_code} has "
                    "hreflang_active=true but indexable=false"
                )

            if trans.get("indexable") is True and is_launched:
                _check_translation_html(entry, trans, lang_code, en_path, routes_by_path, errors)


def _check_translation_html(entry, trans, lang_code, en_path, routes_by_path, errors):
    trans_path = trans.get("path", "")
    if not trans_path or trans_path == "/":
        return

    html_path = os.path.join(ROOT, trans_path.strip("/"), "index.html")
    if not os.path.exists(html_path):
        errors.append(
            f"translation-map.json: '{en_path}' lang={lang_code} is indexed "
            f"but HTML not found at {trans_path}index.html"
        )
        return

    if lang_code == "fr":
        _check_french_page_quality(entry, trans, html_path, lang_code, en_path, errors)
        _check_fr_safety(html_path, en_path, entry.get("safety_class", ""), errors)
        fr_url = BASE + trans_path
        en_url = routes_by_path.get(en_path, {}).get("canonical", "") if en_path else ""
        _check_hreflang_reciprocity(html_path, fr_url, en_path, en_url, errors)


def _check_fr_safety(html_path, en_path, safety_class, errors):
    body = read_text(html_path).lower()
    if safety_class == "medical-educational":
        if not any(marker.lower() in body for marker in FR_SAFETY_MARKERS):
            errors.append(
                f"French page for '{en_path}' (medical-educational) missing safety note"
            )
    ai_diagnosis_paths = ("deepfake", "forensic", "detection", "ophthalmic-ai", "medical-imaging-ai")
    if any(fragment in en_path for fragment in ai_diagnosis_paths):
        if not any(marker.lower() in body for marker in FR_AI_SAFETY_MARKERS):
            errors.append(
                f"French page for '{en_path}' (AI safety) missing detection-is-not-diagnosis boundary"
            )


def _check_french_page_quality(entry, trans, html_path, lang_code, en_path, errors):
    body = read_text(html_path)
    trans_path = trans.get("path", "")
    canonical = BASE + trans_path

    if '<html lang="fr"' not in body:
        errors.append(f"French page {trans_path}: missing html lang=\"fr\"")
    if f'<link rel="canonical" href="{canonical}"' not in body:
        errors.append(f"French page {trans_path}: missing canonical {canonical}")
    if f'hreflang="{lang_code}" href="{canonical}"' not in body:
        errors.append(f"French page {trans_path}: missing self hreflang")

    for token in (entry.get("fio_class"), entry.get("fis_criterion")):
        if token and token not in body:
            errors.append(f"French page {trans_path}: missing invariant code {token}")

    visible = re.sub(r"<script.*?</script>|<style.*?</style>", " ", body, flags=re.S | re.I)
    visible = re.sub(r"<[^>]+>", " ", visible)
    visible = html.unescape(" ".join(visible.split()))
    letters = re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ]", visible)
    if len(letters) < 1500:
        errors.append(f"French page {trans_path}: appears thin ({len(letters)} letters)")

    english_section_markers = ("Scientific Grounding", "Safety Notes", "Source Notes", "Failure Mode")
    for marker in english_section_markers:
        if marker in body:
            errors.append(f"French page {trans_path}: contains untranslated English section marker '{marker}'")

    french_signal_markers = ("Définition", "Ancrage", "sécurité", "Source", "Référence", "Ce contenu")
    if not any(marker.lower() in body.lower() for marker in french_signal_markers):
        errors.append(f"French page {trans_path}: missing recognizable French governance sections")

    source_ids = entry.get("source_ids", [])
    if source_ids and not any(source_id in body for source_id in source_ids):
        errors.append(f"French page {trans_path}: no registered source IDs visible for {en_path}")

    link_parser = LinkTextParser()
    link_parser.feed(body)
    slug_label = re.compile(r"^[a-z]+(?:-[a-z0-9]+)+$")
    for href, text in link_parser.links:
        if href.startswith("/fr/") and slug_label.match(text):
            errors.append(
                f"French page {trans_path}: internal French link {href} uses untranslated slug label '{text}'"
            )


def _check_hreflang_reciprocity(fr_html_path, fr_url, en_path, en_url, errors):
    fr_body = read_text(fr_html_path)
    if en_url and f'hreflang="x-default" href="{en_url}"' not in fr_body:
        errors.append(
            f"French page {fr_html_path}: hreflang=\"x-default\" does not point to {en_url}"
        )

    if en_path and en_path != "/":
        en_html_path = os.path.join(ROOT, en_path.strip("/"), "index.html")
        if os.path.exists(en_html_path):
            en_body = read_text(en_html_path)
            if fr_url and f'hreflang="fr" href="{fr_url}"' not in en_body:
                errors.append(
                    f"English page {en_html_path}: missing hreflang=\"fr\" pointing to {fr_url}"
                )


def _check_registry_page_counts(layers_by_code, routes, tmap, errors):
    en_pages = sum(1 for route in routes if route.get("language", "en") == "en")
    if en_pages != 300:
        errors.append(f"routes.json: English master should have 300 registered pages, found {en_pages}")

    for code in ("fr", "ar"):
        layer = layers_by_code.get(code, {})
        launched = _launched_translation_count(tmap, code)
        expected = layer.get("pilot_page_count")
        if layer.get("status") != "pilot":
            errors.append(f"languages.json: '{code}' must have status 'pilot'")
        if expected != launched:
            errors.append(
                f"languages.json: '{code}' pilot_page_count={expected}, "
                f"but translation-map has {launched} launched indexed pages"
            )

    for code in ("de", "es", "zh", "ja", "ru"):
        layer = layers_by_code.get(code, {})
        launched = _launched_translation_count(tmap, code)
        if layer.get("status") != "architecture_defined":
            errors.append(f"languages.json: '{code}' must remain architecture_defined")
        if launched != 0:
            errors.append(f"translation-map.json: '{code}' should have 0 launched indexed pages, found {launched}")


def _launched_translation_count(tmap, code):
    count = 0
    for entry in tmap.get("routes", []):
        trans = entry.get("translations", {}).get(code, {})
        if trans.get("status") == "launched" and trans.get("indexable") is True:
            count += 1
    return count


def _check_languages_page(layers_by_code, routes, errors):
    html_path = os.path.join(ROOT, "languages", "index.html")
    if not os.path.exists(html_path):
        errors.append("languages/index.html not found")
        return

    parser = StatusTableParser()
    parser.feed(read_text(html_path))
    rows = {row[1]: row for row in parser.rows}

    expected_codes = set(OFFICIAL_ORDER)
    missing = expected_codes - set(rows)
    if missing:
        errors.append("languages/index.html: missing rows for " + ", ".join(sorted(missing)))
        return

    expected_pages = {
        "en": sum(1 for route in routes if route.get("language", "en") == "en"),
        "fr": layers_by_code["fr"].get("pilot_page_count", 0),
        "ar": layers_by_code["ar"].get("pilot_page_count", 0),
        "de": 0,
        "es": 0,
        "zh": 0,
        "ja": 0,
        "ru": 0,
    }
    expected_status_fragments = {
        "en": ["Launched", "master"],
        "fr": ["Pilot/core expansion", "100 anchor/core pages"],
        "ar": ["Pilot", "8 RTL anchor pages"],
        "de": ["Architecture defined"],
        "es": ["Architecture defined"],
        "zh": ["Architecture defined"],
        "ja": ["Architecture defined"],
        "ru": ["Architecture defined"],
    }

    for code in OFFICIAL_ORDER:
        row = rows[code]
        status_text = row[2]
        pages_text = row[3]
        for fragment in expected_status_fragments[code]:
            if fragment not in status_text:
                errors.append(
                    f"languages/index.html: {code} status '{status_text}' missing '{fragment}'"
                )
        expected_count = expected_pages[code]
        if str(expected_count) not in pages_text:
            errors.append(
                f"languages/index.html: {code} pages '{pages_text}' does not match {expected_count}"
            )
        if code in ("fr", "ar") and "indexed" not in pages_text:
            errors.append(f"languages/index.html: {code} pages should say indexed")


def _check_arabic_rtl_pages(errors):
    for slug in AR_PILOT_SLUGS:
        page_path = os.path.join(ROOT, "ar", slug, "index.html")
        if not os.path.exists(page_path):
            errors.append(f"MISSING Arabic page: ar/{slug}/index.html")
            continue

        body = read_text(page_path)
        ar_canonical = f"{BASE}/ar/{slug}/"
        if 'lang="ar"' not in body:
            errors.append(f'ar/{slug}/index.html: missing lang="ar"')
        if 'dir="rtl"' not in body:
            errors.append(f'ar/{slug}/index.html: missing dir="rtl"')
        if ar_canonical not in body:
            errors.append(f"ar/{slug}/index.html: missing canonical {ar_canonical}")
        if not re.search(r"FIO-0[1-5]", body):
            errors.append(f"ar/{slug}/index.html: missing FIO badge")
        if not re.search(r"FIS-[1-5]", body):
            errors.append(f"ar/{slug}/index.html: missing FIS badge")
        if "\u0645\u0644\u0627\u062d\u0638\u0627\u062a \u0627\u0644\u0633\u0644\u0627\u0645\u0629" not in body:
            errors.append(f"ar/{slug}/index.html: missing Arabic safety section")


def _check_arabic_hreflang_reciprocity(errors):
    for en_slug, fr_slug in AR_EN_FR_PAIRS.items():
        ar_url = f"{BASE}/ar/{en_slug}/"
        en_url = f"{BASE}/{en_slug}/"
        fr_url = f"{BASE}/fr/{fr_slug}/"

        en_path = os.path.join(ROOT, en_slug, "index.html")
        fr_path = os.path.join(ROOT, "fr", fr_slug, "index.html")
        ar_path = os.path.join(ROOT, "ar", en_slug, "index.html")

        if not os.path.exists(en_path):
            errors.append(f"MISSING EN page: {en_slug}/index.html")
        else:
            en_body = read_text(en_path)
            if f'hreflang="ar" href="{ar_url}"' not in en_body:
                errors.append(f'{en_slug}/index.html: missing hreflang="ar" to {ar_url}')
            if f'hreflang="fr" href="{fr_url}"' not in en_body:
                errors.append(f'{en_slug}/index.html: missing hreflang="fr" to {fr_url}')

        if not os.path.exists(fr_path):
            errors.append(f"MISSING FR page: fr/{fr_slug}/index.html")
        else:
            fr_body = read_text(fr_path)
            if f'hreflang="ar" href="{ar_url}"' not in fr_body:
                errors.append(f'fr/{fr_slug}/index.html: missing hreflang="ar" to {ar_url}')

        if not os.path.exists(ar_path):
            errors.append(f"MISSING AR page: ar/{en_slug}/index.html")
        else:
            ar_body = read_text(ar_path)
            for lang, expected_url in (
                ("en", en_url),
                ("fr", fr_url),
                ("ar", ar_url),
                ("x-default", en_url),
            ):
                if f'hreflang="{lang}" href="{expected_url}"' not in ar_body:
                    errors.append(
                        f'ar/{en_slug}/index.html: missing hreflang="{lang}" to {expected_url}'
                    )


def _check_sitemap_hreflang_groups(tmap, errors):
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        errors.append("sitemap.xml not found")
        return

    ns = {
        "sm": "http://www.sitemaps.org/schemas/sitemap/0.9",
        "xhtml": "http://www.w3.org/1999/xhtml",
    }

    try:
        tree = ET.parse(sitemap_path)
    except ET.ParseError as exc:
        errors.append(f"sitemap.xml: XML parse error: {exc}")
        return

    sitemap_hreflang = {}
    for url_node in tree.getroot().findall("sm:url", ns):
        loc_node = url_node.find("sm:loc", ns)
        if loc_node is None or not loc_node.text:
            continue
        links = {}
        for link_node in url_node.findall("xhtml:link", ns):
            hreflang = link_node.attrib.get("hreflang")
            href = link_node.attrib.get("href")
            if hreflang and href:
                links[hreflang] = href
        sitemap_hreflang[loc_node.text] = links

    blocked_langs = {"de", "es", "zh", "ja", "ru"}
    for loc, links in sitemap_hreflang.items():
        forbidden = blocked_langs & set(links)
        if forbidden:
            errors.append(
                f"sitemap.xml: {loc} has hreflang for non-launched language(s): "
                + ", ".join(sorted(forbidden))
            )

    for entry in tmap.get("routes", []):
        expected = _expected_hreflang_group(entry)
        if not expected:
            continue

        urls_to_check = [BASE + entry["english_path"]]
        for trans in entry.get("translations", {}).values():
            if _translation_is_active(trans):
                urls_to_check.append(BASE + trans["path"])

        for loc in urls_to_check:
            actual = sitemap_hreflang.get(loc)
            if actual is None:
                errors.append(f"sitemap.xml: missing indexed hreflang URL {loc}")
            elif actual != expected:
                errors.append(
                    f"sitemap.xml: hreflang group mismatch for {loc}; "
                    f"expected {expected}, found {actual}"
                )


def _expected_hreflang_group(entry):
    en_path = entry.get("english_path")
    if not en_path:
        return {}

    active = []
    for lang_code, trans in entry.get("translations", {}).items():
        if _translation_is_active(trans):
            active.append((lang_code, trans["path"]))

    if not active:
        return {}

    group = {"en": BASE + en_path}
    for lang_code, path in active:
        group[lang_code] = BASE + path
    group["x-default"] = BASE + en_path
    return group


def _translation_is_active(trans):
    return (
        trans.get("status") == "launched"
        and trans.get("indexable") is True
        and trans.get("hreflang_active") is True
    )


def _report(errors):
    if errors:
        print("MULTILINGUAL GATE: FAIL")
        for error in errors:
            print("  -", error)


if __name__ == "__main__":
    sys.exit(main())
