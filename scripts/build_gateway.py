#!/usr/bin/env python3
"""
Build the Zonules.com gateway page with the suspension-reveal interface.

Assembles a single, self-contained, dependency-free static HTML file from
reviewed JS/CSS source. The interface embodies the thesis: a lens held by
hidden fibers, revealed, then cut so focus visibly collapses. A no-JS
static triptych renders the same three states, so the page and its thesis
are fully understandable without JavaScript.

Output: index.html (repository root)

Usage:
  python scripts/build_gateway.py          # write the page
  python scripts/build_gateway.py --check  # exit 1 if the page is stale
"""
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Published from the repository root (GitHub Pages source = main / root).
OUT = os.path.join(ROOT, "index.html")

CX, CY, RING, LENS_RX, LENS_RY, N_FIBERS = 200, 150, 130, 46, 64, 24


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def fibers(cut=False):
    """Radial fibers from the ciliary ring to the lens equator."""
    out = []
    for i in range(N_FIBERS):
        a = (i / N_FIBERS) * 2 * math.pi
        x1 = CX + RING * math.cos(a)
        y1 = CY + RING * math.sin(a)
        # insert at the lens edge
        x2 = CX + LENS_RX * math.cos(a)
        y2 = CY + LENS_RY * math.sin(a)
        if cut:
            # cut fibers stop short, leaving a visible gap
            x2 = CX + (LENS_RX + 26) * math.cos(a)
            y2 = CY + (LENS_RY + 26) * math.sin(a)
        cls = "gw-fiber gw-fiber-cut" if cut else "gw-fiber"
        out.append('<line class="%s" x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f"/>'
                   % (cls, x1, y1, x2, y2))
    return "".join(out)


def svg(interactive=True, state_class=""):
    """The lens scene. The focal target behind the lens blurs when collapsed."""
    el_id = ' id="gw-svg"' if interactive else ""
    cls = "gw-svg" + ((" " + state_class) if state_class else "")
    return (
        '<svg%s class="%s" viewBox="0 0 400 300" role="img" '
        'aria-label="A lens suspended by fine fibers from a surrounding ring. '
        'When the fibers are cut, the lens drifts and the focal target blurs. A simplified illustration.">'
        '<defs><radialGradient id="gw-lensgrad" cx="50%%" cy="42%%" r="60%%">'
        '<stop offset="0%%" stop-color="#eaf4fb" stop-opacity="0.95"/>'
        '<stop offset="100%%" stop-color="#9fc1d8" stop-opacity="0.65"/>'
        "</radialGradient></defs>"
        '<circle class="gw-ciliary" cx="%d" cy="%d" r="%d"/>'
        "%s"
        '<g class="gw-focal">'
        '<circle class="gw-focal-ring" cx="%d" cy="%d" r="20"/>'
        '<circle class="gw-focal-ring" cx="%d" cy="%d" r="11"/>'
        '<circle class="gw-focal-core" cx="%d" cy="%d" r="3"/>'
        "</g>"
        '<ellipse class="gw-lens" cx="%d" cy="%d" rx="%d" ry="%d"/>'
        "</svg>"
    ) % (
        el_id, cls,
        CX, CY, RING,
        fibers(cut=(state_class == "is-collapsed")),
        CX, CY, CX, CY, CX, CY,
        CX, CY, LENS_RX, LENS_RY,
    )


def mini(state_class, label):
    return (
        '<figure><div class="gw-mini">%s</div><figcaption>%s</figcaption></figure>'
        % (svg(interactive=False, state_class=state_class), label)
    )


def build():
    css = read("static/css/gateway.css")
    js = read("static/js/suspension-reveal.js")
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zonules.com — The Hidden System That Makes Vision Possible</title>
<meta name="description" content="Zonules are not vision. They are what makes vision possible. A governed, source-backed reference framework mapping the hidden structures that hold focus across anatomy, perception, and machine vision.">
<link rel="canonical" href="https://zonules.com/">
<style>%(css)s</style>
</head>
<body class="gw">
<main class="gw-wrap">
<p class="gw-eyebrow">Zonules.com · Governed Visual Reference Framework</p>
<h1 class="gw-governing">Zonules are not vision. They are what makes vision possible.</h1>
<p class="gw-lede">Focus is not a property of sight. It is produced by hidden structural tension. In the eye that is anatomy; in perception and machine vision the same structural logic is used as a governed framework for describing how focus holds — and how it fails.</p>
<p class="gw-thesis-note">A conceptual thesis, not a literal claim: the zonules are one of many structures vision depends on. They name the hidden layer that holds focus in place.</p>

<section class="gw-stage" aria-labelledby="gw-stage-h">
<h2 id="gw-stage-h" class="gw-eyebrow">The suspension, revealed</h2>
<figure class="gw-figure">
%(interactive)s
</figure>
<div id="gw-controls" class="gw-controls" role="group" aria-label="Reveal the suspension">
<button type="button" class="gw-step" data-state="held" aria-pressed="true"><span class="gw-step-n">1</span> See the lens</button>
<button type="button" class="gw-step" data-state="revealed" aria-pressed="false"><span class="gw-step-n">2</span> Reveal the zonules</button>
<button type="button" class="gw-step" data-state="collapsed" aria-pressed="false"><span class="gw-step-n">3</span> Cut the fibers</button>
</div>
<p id="gw-caption" class="gw-caption" aria-live="polite">This is the lens, apparently in focus. <strong>Nothing visible is holding it.</strong></p>
<div class="gw-static">
%(mini_held)s
%(mini_revealed)s
%(mini_collapsed)s
</div>
</section>

<div class="gw-rule" aria-hidden="true"></div>

<h2 class="gw-eyebrow">Three layers, one hidden system</h2>
<nav class="gw-layers" aria-label="Reference layers">
<a class="gw-layer" href="/zonules-of-zinn/"><span class="gw-layer-id">Layer 01 · Anatomy</span><p class="gw-layer-title">The biological suspension of focus</p><p class="gw-layer-desc">The zonules of Zinn, the ciliary body, the lens, and the capsule — the structures that suspend the lens and adjust its focus.</p><span class="gw-kind">Anatomical fact · source-backed</span></a>
<a class="gw-layer" href="/visual-perception/"><span class="gw-layer-id">Layer 02 · Perception</span><p class="gw-layer-title">Attention as the second suspension</p><p class="gw-layer-desc">How the mind holds an interpretation steady — and what it means when that anchoring collapses.</p><span class="gw-kind">Perception science · read through a conceptual analogy</span></a>
<a class="gw-layer" href="/machine-vision/"><span class="gw-layer-id">Layer 03 · Machine vision</span><p class="gw-layer-title">Focus integrity in machines</p><p class="gw-layer-desc">Detection is not understanding; seeing is not provenance. Reliability, robustness, and trust in machine perception.</p><span class="gw-kind">Technical application of the framework</span></a>
</nav>

<section class="gw-now" aria-labelledby="gw-now-h">
<h2 id="gw-now-h" class="gw-eyebrow">Why this matters now</h2>
<p>Machine vision now reads medical images, steers vehicles, and screens visual evidence, while synthetic media makes convincing images cheap to produce. The questions that matter are different questions: <em>Is the image sharp? Is the perception reliable? Is the content authentic? Where did it come from? Is it being read correctly?</em> A sharp image can be synthetic. An authentic, well-sourced image can still be misread.</p>
<p><strong>In an era of synthetic media, focus without provenance is no longer sufficient</strong> — and provenance without sound interpretation is not sufficient either. The Focus Integrity framework keeps separation of signal from noise, provenance, and interpretation as distinct criteria, so that a failure in one is never mistaken for a failure in another. It is a vocabulary for describing these problems, not a tool that solves them.</p>
</section>

<section class="gw-key" aria-labelledby="gw-key-h">
<h2 id="gw-key-h" class="gw-eyebrow">How to read this reference</h2>
<dl class="gw-key-list">
<div><dt>Anatomical fact</dt><dd>Established ocular anatomy, cited to registered sources.</dd></div>
<div><dt>Conceptual analogy</dt><dd>The suspension logic applied to perception. An interpretive framework, not a proven law.</dd></div>
<div><dt>Technical application</dt><dd>The framework&rsquo;s criteria used to describe documented machine-vision failures.</dd></div>
<div><dt>Strategic hypothesis</dt><dd>That one shared vocabulary across these domains is useful. Not yet independently validated.</dd></div>
</dl>
</section>

<p class="gw-cta"><a href="/focus-integrity-engine/">Run the Focus Integrity Assessment &rarr;</a></p>

<p class="gw-own">For institutions exploring strategic ownership of the framework, its reference corpus, and the domain: <a href="/acquire/">Strategic acquisition overview</a>.</p>

<p class="gw-foot">A governed, source-backed reference framework. Educational reference only — not medical advice; not a substitute for a qualified eye-care professional.</p>
</main>
<script>%(js)s</script>
</body>
</html>
""" % {
        "css": css,
        "js": js,
        "interactive": svg(interactive=True),
        "mini_held": mini("", "1 · The lens appears to hold its place. Nothing visible holds it."),
        "mini_revealed": mini("is-revealed", "2 · The zonular fibers that suspend it and transmit accommodative tension."),
        "mini_collapsed": mini("is-collapsed", "3 · Without that support the lens can shift and lose its ability to adjust; the image degrades."),
    }
    return page


def main():
    page = build()
    if "--check" in sys.argv[1:]:
        if not os.path.exists(OUT) or open(OUT, encoding="utf-8").read() != page:
            print("STALE: /index.html does not match sources. Run scripts/build_gateway.py")
            return 1
        print("FRESH: /index.html matches governed sources.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("Built /index.html (%d bytes)" % len(page))
    return 0


if __name__ == "__main__":
    sys.exit(main())
