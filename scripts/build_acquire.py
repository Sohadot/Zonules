#!/usr/bin/env python3
"""
Build the Zonules.com acquisition surface (/acquire/).

Governed by ACQUISITION_POSTURE.md. The surface shows the structure that
constitutes the asset, what is verifiable and what is not, the categories of
plausible fit, and one calm contact path — and never a price, an urgency cue,
a marketplace frame, a named buyer, or an unsupported claim. Those
prohibitions are enforced by the quality gate.

Output: acquire/index.html (repository root)

Usage:
  python scripts/build_acquire.py          # write the page
  python scripts/build_acquire.py --check  # exit 1 if the page is stale
"""
import html
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Published from the repository root at the canonical route directory (noindex).
OUT = os.path.join(ROOT, "acquire", "index.html")


def read(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as fh:
        return json.load(fh)


def facts():
    """Verifiable facts, computed from the governed registries at build time.

    Nothing on this surface is a hand-typed number: if the registries change,
    the page goes stale and the quality gate requires a rebuild.
    """
    routes = load("routes.json")["routes"]
    claims = load("claims.json")["claims"]
    sources = load("sources.json")["sources"]
    langs = {l["code"]: l for l in load("languages.json")["layers"]}
    units = [r for r in routes if r.get("page_type") == "reference-unit"]
    by_layer = {k: sum(1 for r in units if r["layer"] == k) for k in ("L1", "L2", "L3")}
    future = [l["name"] for l in langs.values() if l["status"] == "architecture_defined"]
    return {
        "pages": len(routes),
        "units": len(units),
        "l1": by_layer["L1"], "l2": by_layer["L2"], "l3": by_layer["L3"],
        "claims": len(claims),
        "sourced": sum(1 for c in claims if c["status"] == "sourced"),
        "framework": sum(1 for c in claims if c["status"] == "internal-framework"),
        "sources": len(sources),
        "external_sources": sum(1 for s in sources if s["type"] != "conceptual-internal"),
        "fio": load("focus-integrity-ontology.json")["version"],
        "fis": load("focus-integrity-standard.json")["version"],
        "fie": load("focus-integrity-engine.json")["version"],
        "fr": langs["fr"].get("pilot_page_count", 0),
        "ar": langs["ar"].get("pilot_page_count", 0),
        "future": ", ".join(future),
        "future_n": len(future),
    }


# The components a potential acquisition may include, with the basis on which
# each could be transferred. Scientific facts and terminology are never listed
# as owned.
COMPONENTS = [
    ("The domain", "zonules.com, transferable through the registrar under the agreed terms."),
    ("The Focus Integrity framework", "FIO v%(fio)s (five failure classes), FIS v%(fis)s (five criteria), and the FIA protocol: original project text, transferable by agreement."),
    ("The Focus Integrity Engine", "FIE v%(fie)s: original, dependency-free client-side code with reproducibility tests and three worked examples."),
    ("The reference corpus", "%(units)s English reference units written for the project, with %(claims)s registered claims and the internal link graph that binds them."),
    ("The governance record", "Thesis, reference architecture, decision log, version history, and the blocking validators that enforce them."),
    ("The multilingual architecture", "Language and translation registries, a %(fr)s-page French pilot, and an %(ar)s-page Arabic RTL pilot."),
    ("The build system", "Standard-library Python generators and validators; no third-party runtime dependency and no external service."),
]

PROBLEMS = [
    "Reliability of machine perception — whether a model's confidence tracks its correctness.",
    "Stability across operating conditions — whether behaviour survives the move from training data to the world.",
    "Separation of meaningful signal from noise, including adversarial and synthetic noise.",
    "Verification of content origin, now that convincing synthetic images are cheap to produce.",
    "Errors of interpretation — correct detection, wrong meaning.",
    "Fragmented terminology: anatomy, perception science, and machine vision describe related failures in unrelated vocabularies.",
]

FIT = [
    ("Ophthalmic AI and optical imaging",
     "The closest fit for the name: the zonules are ocular anatomy, and the corpus opens with a source-backed account of lens suspension and accommodation. The framework adds a structured vocabulary for describing failure modes; it is not a clinical tool."),
    ("Computer vision and machine-perception reliability",
     "The framework's criteria correspond to recognised problem areas — calibration, domain shift, adversarial robustness, and grounding — and could serve as a documentation or teaching vocabulary alongside existing benchmarks."),
    ("Visual verification and content provenance",
     "The framework treats provenance as one criterion among five and distinguishes it from sharpness, signal quality, and interpretation. It is complementary to provenance standards such as C2PA, not a replacement for them or for forensic methods."),
    ("Scientific reference and knowledge infrastructure",
     "A governed, claim-level corpus with registered sources, structured data, and multilingual registries is directly reusable as reference infrastructure."),
    ("Spatial computing",
     "A plausible but weaker fit: relevance rests on the perception and machine-vision layers rather than on the anatomical name."),
]

REBUILD = [
    "Terminology design that holds across anatomy, perception, and machine vision without collapsing distinct concepts.",
    "Source selection, claim-by-claim attribution, and separation of sourced fact from framework interpretation.",
    "A classification architecture with entry criteria, inverse criteria, and not-applicable handling.",
    "Reference relationships across %(units)s units, maintained without broken links or orphan pages.",
    "Version governance and a decision record that make every change traceable.",
    "Implementation, deterministic testing, and multilingual coordination under shared invariants.",
]


def build():
    css = read("static/css/acquire.css")
    f = facts()
    esc = html.escape
    components = "".join(
        '<div class="aq-item"><strong>%s</strong><span>%s</span></div>' % (t, esc(d % f))
        for t, d in COMPONENTS
    )
    problems = "".join("<li>%s</li>" % esc(p) for p in PROBLEMS)
    fit = "".join("<dt>%s</dt><dd>%s</dd>" % (esc(t), esc(d)) for t, d in FIT)
    rebuild = "".join("<li>%s</li>" % esc(r % f) for r in REBUILD)
    page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Acquisition — Zonules.com</title>
<meta name="description" content="Zonules.com is a developed, governed reference framework for focus, perception, and machine vision: domain, ontology, standard, deterministic engine, reference corpus, and governance record. Private strategic inquiries only.">
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://zonules.com/acquire/">
<style>%(css)s</style>
</head>
<body class="aq">
<main class="aq-wrap">
<p class="aq-eyebrow">For institutions exploring strategic ownership</p>
<h1 class="aq-title">Zonules.com is a developed reference framework, not a domain listing.</h1>
<p class="aq-lede">A seeing system is trusted because of the hidden structure that holds its focus. This page sets out the structure of the asset itself: what it is, what has been built and can be inspected, what remains conceptual, and how a private discussion can begin.</p>

<section class="aq-section">
<h2 class="aq-h">What the asset is</h2>
<p class="aq-p">Zonules.com is a governed, source-backed reference framework built on one anatomical idea: the zonules of Zinn suspend the lens of the eye so that it can hold and adjust focus. The project maps that structural logic across three layers — as anatomical fact, as a conceptual analogy in perception, and as a technical vocabulary in machine vision — and encodes it as a versioned ontology, a standard, and a deterministic assessment engine.</p>
<p class="aq-p">It is a static, inspectable website and repository. It is not a software service, a medical product, or an operational verification system.</p>
</section>

<section class="aq-section">
<h2 class="aq-h">Implemented and verifiable today</h2>
<ul class="aq-facts">
<li><strong>%(units)s</strong> English reference units (%(l1)s anatomy, %(l2)s perception, %(l3)s machine vision) within a %(pages)s-page governed English corpus</li>
<li><strong>%(claims)s</strong> registered claims: %(sourced)s attributed to external sources, %(framework)s explicitly marked as internal framework interpretation</li>
<li><strong>%(external_sources)s</strong> registered external sources — textbooks, peer-reviewed papers, institutions, and a standards body</li>
<li>Focus Integrity Ontology v%(fio)s · Standard v%(fis)s · Engine v%(fie)s, with reproducibility tests</li>
<li>French pilot of %(fr)s pages and Arabic RTL pilot of %(ar)s pages; %(future_n)s further languages (%(future)s) are architecture-defined only, with no published pages</li>
<li>Blocking validators for sourcing, links, safety language, multilingual consistency, and build freshness</li>
</ul>
<p class="aq-note">Not claimed: independent scientific validation of the framework, external endorsement, adoption by any standards body, traffic, revenue, or demonstrated market demand. Version numbers below 1.0 are deliberate.</p>
</section>

<section class="aq-section">
<h2 class="aq-h">The problem the framework organizes</h2>
<p class="aq-p">Modern visual systems face distinct challenges that are often discussed as one problem:</p>
<ul class="aq-list">
%(problems)s
</ul>
<p class="aq-p">Zonules.com does not solve these problems operationally. It offers a way to name, separate, and classify them — five failure classes, five inverse criteria, and traceable links from each class to the reference units that explain it.</p>
</section>

<section class="aq-section">
<h2 class="aq-h">Where the fit is plausible</h2>
<p class="aq-p">Three things are kept separate here: the natural fit of an anatomical name, the potential utility of the framework, and evidence of commercial demand. The first two are described below. The third has not been established.</p>
<dl class="aq-fit">
%(fit)s
</dl>
</section>

<section class="aq-section">
<h2 class="aq-h">What a potential acquisition may include</h2>
<div class="aq-grid">
%(components)s
</div>
<p class="aq-note">Not included and not claimed: ownership of established scientific terminology (including &ldquo;zonules&rdquo; and &ldquo;zonules of Zinn&rdquo;), of publicly known concepts, or of the third-party works cited as sources, which are referenced rather than reproduced. No registered trademark is represented. The scope of any transfer of domain, code, text, and associated rights is a matter for a written agreement and independent verification.</p>
</section>

<section class="aq-section">
<h2 class="aq-h">What recreating the package would involve</h2>
<p class="aq-p">Any part of this could be built independently. Rebuilding the integrated package would involve:</p>
<ul class="aq-list">
%(rebuild)s
</ul>
<p class="aq-note">Development effort is described here as a matter of record. It is not a statement of commercial value.</p>
</section>

<section class="aq-section">
<h2 class="aq-h">Due diligence</h2>
<p class="aq-p">The published site, its structured data, and its governance documents can be inspected directly. The repository, its version history, and the outputs of every validator can be reviewed in full as part of a mutually agreed process.</p>
</section>

<section class="aq-section" aria-labelledby="aq-escrow">
<h2 class="aq-h" id="aq-escrow">Secure transaction</h2>
<p class="aq-p">For an agreed strategic acquisition, an independent escrow service may be used, by mutual agreement, to facilitate a secure transaction. Transfer terms, verification conditions, and fund-release procedures would be established between the parties.</p>
<p class="aq-p">Escrow is a transaction mechanism, not evidence of ownership and not a substitute for a transfer agreement. Transfer of the domain and transfer of the framework, code, and content may require separate contractual provisions.</p>
</section>

<div class="aq-rule" aria-hidden="true"></div>

<section class="aq-section">
<div class="aq-contact">
<h2 class="aq-h">Private strategic inquiries</h2>
<p class="aq-p">Institutional and strategic inquiries are reviewed individually and in confidence. There is no listing, no public valuation, and no process beyond a direct, considered conversation. A useful first message names the organization, the intended use, and the components of interest.</p>
<p class="aq-p">Contact: <a href="mailto:agent@sohadot.com">agent@sohadot.com</a></p>
</div>
</section>

<p class="aq-foot">Return to the <a href="/">reference gateway</a> · inspect the <a href="/focus-integrity-engine/">Focus Integrity Engine</a> and its worked examples · read the <a href="/focus-integrity-ontology/">Focus Integrity Ontology</a> and the <a href="/methodology/">methodology</a>. Educational reference asset; not medical advice.</p>
</main>
</body>
</html>
""" % dict(f, css=css, components=components, problems=problems, fit=fit, rebuild=rebuild)
    return page


def main():
    page = build()
    if "--check" in sys.argv[1:]:
        if not os.path.exists(OUT) or open(OUT, encoding="utf-8").read() != page:
            print("STALE: /acquire/index.html does not match sources. Run scripts/build_acquire.py")
            return 1
        print("FRESH: /acquire/index.html matches governed sources.")
        return 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print("Built /acquire/index.html (%d bytes)" % len(page))
    return 0


if __name__ == "__main__":
    sys.exit(main())
