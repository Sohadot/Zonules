#!/usr/bin/env python3
"""
Generate sitemap.xml and robots.txt for Zonules.com.

The sitemap is derived ONLY from the route registry. A page enters the
sitemap if and only if it is registered, status == "approved", and
indexable == true. Draft, non-indexable, or unregistered surfaces can
never appear — the registry is the single source of truth.

Output: static/sitemap.xml, static/robots.txt

Usage:
  python scripts/generate_sitemap.py          # write both files
  python scripts/generate_sitemap.py --check   # exit 1 if either is stale
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://zonules.com"
SITEMAP = os.path.join(ROOT, "static", "sitemap.xml")
ROBOTS = os.path.join(ROOT, "static", "robots.txt")

# Priority by page type — the gateway and engine lead, reference units follow.
PRIORITY = {"gateway": "1.0", "engine": "0.9", "reference-unit": "0.8"}
DEFAULT_PRIORITY = "0.6"


def load_routes():
    with open(os.path.join(ROOT, "data", "routes.json"), encoding="utf-8") as fh:
        return json.load(fh)["routes"]


def eligible(routes):
    """Only approved, indexable, registered routes — sorted for deterministic output."""
    rows = [r for r in routes if r.get("status") == "approved" and r.get("indexable") is True]
    # Stable order: gateway first, then by path.
    return sorted(rows, key=lambda r: (r["path"] != "/", r["path"]))


def build_sitemap(routes):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for r in eligible(routes):
        loc = BASE + r["path"]
        prio = PRIORITY.get(r.get("page_type"), DEFAULT_PRIORITY)
        lines.append("  <url>")
        lines.append("    <loc>%s</loc>" % loc)
        if r.get("last_reviewed"):
            lines.append("    <lastmod>%s</lastmod>" % r["last_reviewed"])
        lines.append("    <priority>%s</priority>" % prio)
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def build_robots():
    # Static-first posture: allow indexing of the public asset; point to the sitemap.
    # No crawl traps, no private surfaces, no API endpoints to disallow.
    return (
        "User-agent: *\n"
        "Allow: /\n"
        "\n"
        "Sitemap: %s/sitemap.xml\n"
    ) % BASE


def main():
    routes = load_routes()
    sitemap = build_sitemap(routes)
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

    os.makedirs(os.path.dirname(SITEMAP), exist_ok=True)
    with open(SITEMAP, "w", encoding="utf-8") as fh:
        fh.write(sitemap)
    with open(ROBOTS, "w", encoding="utf-8") as fh:
        fh.write(robots)
    print("Built sitemap.xml (%d urls) and robots.txt" % len(eligible(routes)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
