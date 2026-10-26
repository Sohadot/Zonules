#!/usr/bin/env python3
"""
Build the Focus Integrity Engine page.

Assembles a single, self-contained, dependency-free static HTML file from
the governed JSON registries and the reviewed JS/CSS source. The data is
embedded as inert JSON script blocks, so the engine runs with no network
call, no fetch, and no runtime dependency — inspectable and reproducible.

Single source of truth: data/*.json + static/js + static/css.
Output: focus-integrity-engine/index.html (repository root)

Usage:
  python scripts/build_engine.py          # write the page
  python scripts/build_engine.py --check  # exit 1 if the page is stale
"""
import html
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Published from the repository root at the canonical route directory.
OUT = os.path.join(ROOT, "focus-integrity-engine", "index.html")


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
        "<p>The Focus Integrity Standard defines five criteria. Each layer applies the "
        "criteria within its scope: all five in perception and machine vision, three in "
        "anatomy, where provenance and interpretation are not anatomical properties. Each "
        "failed or at-risk criterion maps to one class in the Focus Integrity Ontology, and "
        "each class resolves to governed reference pages. The interactive reading enhances "
        "this framework; it does not replace it.</p>"
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


KIND_LABEL = {
    "published-empirical": "Published empirical phenomenon",
    "source-derived": "Source-derived educational scenario",
    "hypothetical": "Hypothetical demonstration",
}
APPLICATION_LABEL = {
    "literal": "literal application (anatomical fact)",
    "conceptual-analogy": "conceptual analogy",
    "technical": "technical application",
}
STATE_LABEL = {"intact": "intact", "at-risk": "at risk", "failed": "failed", None: "not assessed"}


def scope_html():
    """What the engine is, and what it is not. Rendered statically, no JS needed."""
    fie = json.loads(read("data/focus-integrity-engine.json"))
    sc = fie["scope_statement"]
    nots = "".join("<li>%s</li>" % html.escape(x) for x in sc["is_not"])
    return (
        '<section class="fie-scope" aria-labelledby="fie-scope-h">'
        '<h2 id="fie-scope-h">What this engine is — and is not</h2>'
        "<p>%s</p><p>It is not:</p><ul>%s</ul>"
        "</section>" % (html.escape(sc["is"]), nots)
    )


def examples_html():
    """The three worked examples, reproducible with the interactive engine.

    Expected readings are verified against the engine's own classify() by
    scripts/test_engine.js, so this static text cannot drift from behaviour.
    """
    fie = json.loads(read("data/focus-integrity-engine.json"))
    fis = {c["id"]: c for c in json.loads(read("data/focus-integrity-standard.json"))["criteria"]}
    fio = {c["id"]: c for c in json.loads(read("data/focus-integrity-ontology.json"))["classes"]}
    src = {s["id"]: s for s in json.loads(read("data/sources.json"))["sources"]}
    esc = html.escape
    cards = []
    for ex in fie.get("examples", []):
        layer = fie["layers"][ex["layer"]]
        inputs = "".join(
            "<li>%s %s — %s</li>" % (cid, esc(fis[cid]["name"]), STATE_LABEL[st])
            for cid, st in ex["inputs"].items()
        )
        for cid in layer.get("not_applicable", {}):
            inputs += "<li>%s %s — not applicable at this layer</li>" % (cid, esc(fis[cid]["name"]))
        classes = " · ".join(
            "%s %s (%s)" % (cid, esc(fio[cid]["name"]), STATE_LABEL[st])
            for cid, st in ex["expected"]["classes"].items()
        ) or "none"
        evidence = "; ".join(
            "%s — %s" % (sid, esc(src[sid]["citation"])) for sid in ex["evidence"]
        )
        refs = " · ".join('<a href="%s">%s</a>' % (h, h) for h in ex["references"])
        cards.append(
            '<article class="fie-example" id="%(id)s">'
            "<h3>%(id)s · %(title)s</h3>"
            '<p class="fie-example-tag">%(layer)s · %(kind)s · %(app)s</p>'
            "<dl>"
            "<dt>Context</dt><dd>%(context)s</dd>"
            "<dt>Evidence</dt><dd>%(evidence)s</dd>"
            "<dt>Structured inputs</dt><dd><ul>%(inputs)s</ul></dd>"
            "<dt>Applicable criteria</dt><dd>%(criteria)s</dd>"
            "<dt>Resulting classification</dt><dd><strong>%(verdict)s</strong> — %(classes)s</dd>"
            "<dt>Interpretation</dt><dd>%(interp)s</dd>"
            "<dt>Limitations</dt><dd>%(limits)s</dd>"
            "<dt>Reference units</dt><dd>%(refs)s</dd>"
            "</dl></article>"
            % {
                "id": ex["id"], "title": esc(ex["title"]),
                "layer": "%s %s" % (ex["layer"], esc(layer["label"])),
                "kind": KIND_LABEL[ex["kind"]], "app": APPLICATION_LABEL[ex["application"]],
                "context": esc(ex["context"]), "evidence": evidence, "inputs": inputs,
                "criteria": ", ".join(layer["criteria"]),
                "verdict": esc(fie["verdict_labels"][ex["expected"]["verdict"]]),
                "classes": classes, "interp": esc(ex["interpretation"]),
                "limits": esc(ex["limitations"]), "refs": refs,
            }
        )
    return (
        '<section class="fie-examples" aria-labelledby="fie-examples-h">'
        '<h2 id="fie-examples-h">Three worked examples</h2>'
        "<p>Each example can be loaded into the engine above and reproduces the reading shown here. "
        "Examples are labelled as published phenomena, source-derived scenarios, or hypothetical "
        "demonstrations; none reports new experimental results.</p>"
        + "".join(cards) +
        "</section>"
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
<meta name="description" content="Run the Focus Integrity Assessment: one shared framework, layer-specific criteria, traceable failure classifications across anatomy, perception, and machine vision. Deterministic, computed locally, no data collected.">
<link rel="canonical" href="https://zonules.com/focus-integrity-engine/">
<style>%(css)s</style>
%(fio)s
%(fis)s
%(fie)s
</head>
<body class="fie">
<main class="fie-wrap">
<p class="fie-eyebrow">Focus Integrity Engine</p>
<h1 class="fie-title">One shared framework. Layer-specific criteria. Traceable failure classifications.</h1>
<p class="fie-lede">The Focus Integrity Assessment applies the same standard to the eye, to perception, and to machine vision — literally in anatomy, by analogy in perception, as a technical vocabulary in machine vision. You supply structured judgements; the engine applies fixed rules and maps each finding to the ontology class and reference units that explain it.</p>
<div class="fie-rule" aria-hidden="true"></div>
<noscript>
<p><em>The interactive reading requires JavaScript. The governed framework below explains every criterion and every failure class, and links to each reference unit.</em></p>
</noscript>
<div id="fie-app" hidden></div>
<div id="fie-reading" class="fie-reading" hidden aria-live="polite"></div>
%(examples)s
%(scope)s
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
        "examples": examples_html(),
        "scope": scope_html(),
    }
    return page


def main():
    page = build()
    check = "--check" in sys.argv[1:]
    if check:
        if not os.path.exists(OUT) or open(OUT, encoding="utf-8").read() != page:
            print("STALE: /focus-integrity-engine/index.html does not match sources. Run scripts/build_engine.py")
            return 1
        print("FRESH: /focus-integrity-engine/index.html matches governed sources.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("Built /focus-integrity-engine/index.html (%d bytes)" % len(page))
    return 0


if __name__ == "__main__":
    sys.exit(main())
