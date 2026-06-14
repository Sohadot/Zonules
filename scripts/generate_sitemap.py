#!/usr/bin/env python3
"""
Generate sitemap.xml and robots.txt for Zonules.com.

The sitemap is derived from the route registry (English pages) and from
data/translation-map.json (completed translated pages). A page enters the
sitemap if and only if it is registered (or translated), status == "approved"
(or "launched"), and indexable == true. Draft, non-indexable, or unregistered
surfaces can never appear.

Output: sitemap.xml, robots.txt (repository root)

Usage:
  python scripts/generate_sitemap.py          # write both files
  python scripts/generate_sitemap.py --check   # exit 1 if either is stale
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://zonules.com"
SITEMAP = os.path.join(ROOT, "sitemap.xml")
ROBOTS = os.path.join(ROOT, "robots.txt")

PRIORITY = {"gateway": "1.0", "engine": "0.9", "reference-unit": "0.8"}
DEFAULT_PRIORITY = "0.6"


def load_routes():
    with open(os.path.join(ROOT, "data", "routes.json"), encoding="utf-8") as fh:
        return json.load(fh)["routes"]


def load_tmap():
    path = os.path.join(ROOT, "data", "translation-map.json")
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def eligible_english(routes):
    rows = [r for r in routes if r.get("status") == "approved" and r.get("indexable") is True]
    return sorted(rows, key=lambda r: (r["path"] != "/", r["path"]))


def build_hreflang_groups(tmap):
    """Return dict: english_path -> list of {lang, url} for active hreflang pairs."""
    groups = {}
    if not tmap:
        return groups
    for entry in tmap.get("routes", []):
        en_path = entry.get("english_path")
        if not en_path:
            continue
        active = []
        for lang, trans in entry.get("translations", {}).items():
            if trans.get("hreflang_active") and trans.get("indexable"):
                active.append({"lang": lang, "url": BASE + trans["path"]})
        if active:
            groups[en_path] = active
    return groups


def translated_pages(tmap):
    """Return list of completed translated page entries for sitemap."""
    pages = []
    if not tmap:
        return pages
    for entry in tmap.get("routes", []):
        en_path = entry.get("english_path", "")
        for lang, trans in entry.get("translations", {}).items():
            if trans.get("status") == "launched" and trans.get("indexable") is True:
                pages.append({
                    "path": trans["path"],
                    "lang": lang,
                    "english_path": en_path,
                })
    pages.sort(key=lambda p: (p["lang"], p["path"]))
    return pages


def build_sitemap(routes, tmap):
    hreflang_groups = build_hreflang_groups(tmap)
    trans_pages = translated_pages(tmap)
    has_hreflang = bool(hreflang_groups)

    if has_hreflang:
        ns = ('<?xml version="1.0" encoding="UTF-8"?>\n'
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
              '        xmlns:xhtml="http://www.w3.org/1999/xhtml">')
    else:
        ns = ('<?xml version="1.0" encoding="UTF-8"?>\n'
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    lines = [ns]

    def hreflang_block(en_path):
        group = hreflang_groups.get(en_path, [])
        if not group:
            return []
        block = []
        en_url = BASE + en_path
        block.append('    <xhtml:link rel="alternate" hreflang="en" href="%s"/>' % en_url)
        for item in group:
            block.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (item["lang"], item["url"]))
        block.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % en_url)
        return block

    for r in eligible_english(routes):
        loc = BASE + r["path"]
        prio = PRIORITY.get(r.get("page_type"), DEFAULT_PRIORITY)
        lines.append("  <url>")
        lines.append("    <loc>%s</loc>" % loc)
        if r.get("last_reviewed"):
            lines.append("    <lastmod>%s</lastmod>" % r["last_reviewed"])
        lines.append("    <priority>%s</priority>" % prio)
        lines.extend(hreflang_block(r["path"]))
        lines.append("  </url>")

    for tp in trans_pages:
        loc = BASE + tp["path"]
        group = hreflang_groups.get(tp["english_path"], [])
        lines.append("  <url>")
        lines.append("    <loc>%s</loc>" % loc)
        lines.append("    <lastmod>2026-06-14</lastmod>")
        lines.append("    <priority>0.8</priority>")
        if group:
            en_url = BASE + tp["english_path"]
            lines.append('    <xhtml:link rel="alternate" hreflang="en" href="%s"/>' % en_url)
            lines.append('    <xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (tp["lang"], loc))
            lines.append('    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>' % en_url)
        lines.append("  </url>")

    languages_html = os.path.join(ROOT, "languages", "index.html")
    if os.path.exists(languages_html):
        lines.append("  <url>")
        lines.append("    <loc>%s/languages/</loc>" % BASE)
        lines.append("    <lastmod>2026-06-14</lastmod>")
        lines.append("    <priority>0.6</priority>")
        lines.append("  </url>")

    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def build_robots():
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /data/\n"
        "Disallow: /scripts/\n"
        "Disallow: /content/\n"
        "Disallow: /static/\n"
        "Disallow: /templates/\n"
        "Disallow: /site/\n"
        "Disallow: /docs/\n"
        "\n"
        "Sitemap: %s/sitemap.xml\n"
    ) % BASE


def main():
    routes = load_routes()
    tmap = load_tmap()
    sitemap = build_sitemap(routes, tmap)
    robots = build_robots()

    if "--check" in sys.argv[1:]:
        stale = []
        if not os.path.exists(SITEMAP) or open(SITEMAP, encoding="utf-8").read() != sitemap:
            stale.append("sitemap.xml")
        if not os.path.exists(ROBOTS) or open(ROBOTS, encoding="utf-8").read() != robots:
            stale.append("robots.txt")
        if stale:
            print("STALE: " + ", ".join(stale) + ". Run scripts/generate_sitemap.py")
            return 1
        print("FRESH: sitemap.xml and robots.txt match the route registry.")
        return 0

    with open(SITEMAP, "w", encoding="utf-8") as fh:
        fh.write(sitemap)
    with open(ROBOTS, "w", encoding="utf-8") as fh:
        fh.write(robots)
    en_count = len(eligible_english(routes))
    tr_count = len(translated_pages(tmap))
    print("Built sitemap.xml (%d English + %d translated = %d urls) and robots.txt" % (en_count, tr_count, en_count + tr_count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
