#!/usr/bin/env python3
"""
Build the Focus Integrity Engine page.

Assembles a single, self-contained, dependency-free static HTML file from
the governed JSON registries and the reviewed JS/CSS source. The data is
embedded as inert JSON script blocks, so the engine runs with no network
call, no fetch, and no runtime dependency — inspectable and reproducible.

Single source of truth: data/*.json + static/js + static/css.
Output: static/engine/index.html

Usage:
  python scripts/build_engine.py          # write the page
  python scripts/build_engine.py --check  # exit 1 if the page is stale
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "engine", "index.html")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def data_block(block_id, rel):
    # json.dumps with ensure_ascii keeps the payload inert and ASCII-safe;
    # </script> cannot appear in JSON output, so no injection break-out.
    payload = json.dumps(json.loads(read(rel)), ensure_ascii=True, separators=(",", ":"))
    return '<script type="application/json" id="%s">%s</script>' % (block_id, payload)


def fallback_html():
    """Static, no-JS reference. The page is fully understandable without the engine."""
    fis = json.loads(read("data/focus-integrity-standard.json"))
    fio = json.loads(read("data/focus-integrity-ontology.json"))
    crit = "".join(
        "<li><strong>%s · %s.</strong> %s</li>" % (c["id"], c["name"], c["statement"])
        for c in fis["criteria"]
    )
    classes = "".join(
        "<li><strong>%s · %s.</strong> %s</li>" % (c["id"], c["name"], c["governing_claim"])
        for c in fio["classes"]
    )
    return (
        '<div class="fie-fallback">'
        "<h2>The Focus Integrity Assessment</h2>"
        "<p>Focus integrity is decided by five criteria. Each failure maps to one "
        "class in the Focus Integrity Ontology, and each class resolves to a governed "
        "reference page. The interactive reading enhances this framework; it does not "
        "replace it.</p>"
        "<h3>The five criteria (FIS)</h3><ul>" + crit + "</ul>"
        "<h3>The five failure classes (FIO)</h3><ul>" + classes + "</ul>"
        "<p>Reference units: "
        '<a href="/zonules-of-zinn/">Zonules of Zinn</a> · '
        '<a href="/ciliary-body/">Ciliary Body</a> · '
        '<a href="/crystalline-lens/">Crystalline Lens</a> · '
        '<a href="/lens-capsule/">Lens Capsule</a> · '
        '<a href="/lens-accommodation/">Lens Accommodation</a> · '
        '<a href="/visual-perception/">Visual Perception</a> · '
        '<a href="/machine-vision/">Machine Vision</a>.</p>'
        "</div>"
    )


def build():
    css = read("static/css/engine.css")
    js = read("static/js/focus-integrity-engine.js")
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Focus Integrity Engine — Zonules.com</title>
<meta name="description" content="Run the Focus Integrity Assessment: the same five criteria decide whether focus holds in the eye, in perception, or in a machine. Deterministic, computed locally, no data collected.">
<link rel="canonical" href="https://zonules.com/focus-integrity-engine/">
<style>%(css)s</style>
%(fio)s
%(fis)s
%(fie)s
</head>
<body class="fie">
<main class="fie-wrap">
<p class="fie-eyebrow">Focus Integrity Engine</p>
<h1 class="fie-title">The same five questions decide whether a system can be trusted to focus.</h1>
<p class="fie-lede">Whether the seeing system is made of tissue, of attention, or of silicon, focus is held by a hidden suspension layer. This engine runs the Focus Integrity Assessment and maps each finding to the structure that explains it.</p>
<div class="fie-rule" aria-hidden="true"></div>
<noscript>
<p><em>The interactive reading requires JavaScript. The governed framework below explains every criterion and every failure class, and links to each reference unit.</em></p>
</noscript>
<div id="fie-app" hidden></div>
<div id="fie-reading" class="fie-reading" hidden aria-live="polite"></div>
%(fallback)s
</main>
<script>%(js)s</script>
</body>
</html>
""" % {
        "css": css,
        "js": js,
        "fio": data_block("fio-data", "data/focus-integrity-ontology.json"),
        "fis": data_block("fis-data", "data/focus-integrity-standard.json"),
        "fie": data_block("fie-data", "data/focus-integrity-engine.json"),
        "fallback": fallback_html(),
    }
    return page


def main():
    page = build()
    check = "--check" in sys.argv[1:]
    if check:
        if not os.path.exists(OUT) or open(OUT, encoding="utf-8").read() != page:
            print("STALE: static/engine/index.html does not match sources. Run scripts/build_engine.py")
            return 1
        print("FRESH: static/engine/index.html matches governed sources.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("Built static/engine/index.html (%d bytes)" % len(page))
    return 0


if __name__ == "__main__":
    sys.exit(main())
