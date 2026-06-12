#!/usr/bin/env python3
"""
Build the Zonules.com acquisition surface (/acquire/).

Governed by ACQUISITION_POSTURE.md. The surface shows the structure that
constitutes the asset and the categories of strategic buyer, with one calm
contact path — and never a price, an urgency cue, a marketplace frame, or a
named buyer. Those prohibitions are enforced by the quality gate.

Output: static/acquire/index.html

Usage:
  python scripts/build_acquire.py          # write the page
  python scripts/build_acquire.py --check  # exit 1 if the page is stale
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "acquire", "index.html")

# What a strategic buyer acquires — the structure, rendered as structure.
ACQUIRES = [
    ("The category name", "A one-word, established anatomical term that names the system beneath all vision."),
    ("The category language", "The originated vocabulary: focus integrity, the suspension layer, focus collapse."),
    ("The Focus Integrity Ontology", "A governed classification of how focus fails across anatomy, perception, and machine vision."),
    ("The Focus Integrity Standard", "The published definition of what intact focus integrity is."),
    ("The Focus Integrity Engine", "A deterministic, static assessment that turns the framework into governed output."),
    ("The reference corpus", "Source-backed reference units and the internal link graph that binds them."),
    ("The governance record", "Versioning, decision logs, and quality gates that make the asset trustworthy by construction."),
    ("The multilingual architecture", "A reference authority designed to extend across eight governed language layers."),
]

BUYERS = [
    "Visual verification and deepfake-detection platforms",
    "Ophthalmic-AI and medical-imaging companies",
    "Computer-vision and spatial-computing platforms",
    "Optical-science and precision-imaging companies",
    "Perception-science and AI-knowledge-infrastructure institutions",
]


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def build():
    css = read("static/css/acquire.css")
    items = "".join(
        '<div class="aq-item"><strong>%s</strong><span>%s</span></div>' % (t, d)
        for t, d in ACQUIRES
    )
    buyers = "".join("<li>%s</li>" % b for b in BUYERS)
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Acquisition — Zonules.com</title>
<meta name="description" content="Zonules.com is a developed category asset: a governed reference system and Category Intelligence Factory for focus, perception, and visual truth. Strategic inquiries only.">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://zonules.com/acquire/">
<style>%(css)s</style>
</head>
<body class="aq">
<main class="aq-wrap">
<p class="aq-eyebrow">Strategic acquisition</p>
<h1 class="aq-title">Zonules.com is a developed category asset, not a domain listing.</h1>
<p class="aq-lede">A seeing system is trusted because of the hidden structure that holds its focus. An asset is acquired because of the hidden structure that holds its value. What follows is that structure.</p>

<section class="aq-section">
<h2 class="aq-h">What this asset is</h2>
<p class="aq-p">Zonules.com is a sovereign visual reference system and Category Intelligence Factory for the hidden structures that make focus, perception, and visual truth possible. It maps one governing thesis across three layers — anatomy, perception, and machine vision — and produces governed intelligence rather than publishing content alone.</p>
</section>

<section class="aq-section">
<h2 class="aq-h">What a strategic buyer acquires</h2>
<div class="aq-grid">
%(items)s
</div>
</section>

<section class="aq-section">
<h2 class="aq-h">Where the asset is strategically relevant</h2>
<ul class="aq-list">
%(buyers)s
</ul>
</section>

<div class="aq-rule" aria-hidden="true"></div>

<section class="aq-section">
<div class="aq-contact">
<h2 class="aq-h">Strategic inquiries</h2>
<p class="aq-p">Serious institutional and strategic inquiries are reviewed individually. There is no listing, no public valuation, and no process beyond a direct, considered conversation.</p>
<p class="aq-p">Contact: <a href="mailto:agent@sohadot.com">agent@sohadot.com</a></p>
</div>
</section>

<p class="aq-foot">Return to the <a href="/">reference gateway</a> · explore the <a href="/focus-integrity-engine/">Focus Integrity Engine</a>. Educational reference asset; not medical advice.</p>
</main>
</body>
</html>
""" % {"css": css, "items": items, "buyers": buyers}
    return page


def main():
    page = build()
    if "--check" in sys.argv[1:]:
        if not os.path.exists(OUT) or open(OUT, encoding="utf-8").read() != page:
            print("STALE: static/acquire/index.html does not match sources. Run scripts/build_acquire.py")
            return 1
        print("FRESH: static/acquire/index.html matches governed sources.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("Built static/acquire/index.html (%d bytes)" % len(page))
    return 0


if __name__ == "__main__":
    sys.exit(main())
