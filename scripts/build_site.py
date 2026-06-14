#!/usr/bin/env python3
"""
Render the governed markdown corpus into structured, citable HTML.

Source of truth stays the markdown reference units and the data registries.
For each markdown-backed route this renderer produces a static HTML page with:
  - semantic HTML and the shared ocular-depth design
  - breadcrumb navigation
  - a generated References section built from the claim and source registries
  - JSON-LD structured data (DefinedTerm + isPartOf + BreadcrumbList + citations)
    so AI agents, search engines, and citation tools can read the asset reliably
  - canonical, Open Graph, and hreflang scaffolding

It also generates the glossary hub (/glossary/) directly from the registry, so
that index can never contain a broken or phantom link.

Pure standard library. No markdown dependency, no network, no third-party code.
The renderer accepts only the constrained markdown our governed content uses:
frontmatter, ATX headings, paragraphs, bold, internal/mailto links, unordered
lists, and blockquotes.

Output: site/<path>/index.html
Usage:
  python scripts/build_site.py            # render the corpus
  python scripts/build_site.py --check    # exit 1 if any rendered page is stale
"""
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Published from the repository root (GitHub Pages source = main / root):
# reference units render to /<slug>/index.html, never under /site/.
SITE = ROOT
BASE = "https://zonules.com"

# Shared stylesheet, emitted once inside the publish root and cached across all
# pages. Linked by a path relative to each page's depth so it resolves both on
# the deployed domain and when a page is opened locally.
CSS_REL = "assets/css/reference.css"
CSS_SRC = os.path.join(ROOT, "static", "css", "reference.css")
CSS_OUT = os.path.join(SITE, "assets", "css", "reference.css")


def css_href(route_path):
    depth = len([s for s in route_path.strip("/").split("/") if s])
    return ("../" * depth if depth else "./") + CSS_REL

LAYER_NAME = {
    "L1": "Anatomy", "L2": "Perception", "L3": "Machine Vision & Verification",
    "cross": "Reference", "": "Reference",
}


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as fh:
        return json.load(fh)


# ---------- constrained markdown ----------

def parse_frontmatter(text):
    """Parse the simple YAML subset our content uses."""
    meta, body = {}, text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            block = text[3:end].strip("\n")
            body = text[end + 4:].lstrip("\n")
            for line in block.split("\n"):
                if not line.strip() or ":" not in line:
                    continue
                k, v = line.split(":", 1)
                k, v = k.strip(), v.strip()
                if v.startswith("[") and v.endswith("]"):
                    v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
                else:
                    v = v.strip('"')
                meta[k] = v
    return meta, body


def render_inline(text):
    text = html.escape(text, quote=False)
    # strip authoring claim markers (provenance is regenerated as a References section)
    text = re.sub(r"\s*\[CLM-\d+\]", "", text)
    # bold
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    # links — internal (/...), anchors (#...), or mailto only
    def link(m):
        label, href = m.group(1), m.group(2)
        if not (href.startswith("/") or href.startswith("mailto:") or href.startswith("#")):
            return label  # external links are not permitted in the static corpus
        return '<a href="%s">%s</a>' % (html.escape(href, quote=True), label)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    return text


def render_markdown(body):
    lines = body.split("\n")
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            out.append("<h%d>%s</h%d>" % (level, render_inline(m.group(2).strip()), level))
            i += 1
            continue
        if line.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].startswith(">"):
                quote.append(lines[i].lstrip(">").strip())
                i += 1
            out.append("<blockquote>%s</blockquote>" % render_inline(" ".join(quote)))
            continue
        if re.match(r"^[-*]\s+", line):
            items = []
            while i < len(lines) and re.match(r"^[-*]\s+", lines[i]):
                items.append("<li>%s</li>" % render_inline(re.sub(r"^[-*]\s+", "", lines[i])))
                i += 1
            out.append("<ul>%s</ul>" % "".join(items))
            continue
        para = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,4}\s|>|[-*]\s)", lines[i]):
            para.append(lines[i].strip())
            i += 1
        out.append("<p>%s</p>" % render_inline(" ".join(para)))
    return "\n".join(out)


# ---------- references + structured data ----------

def references_section(meta, claims_by_id, sources_by_id):
    ids = meta.get("claims", [])
    if not ids:
        return "", []
    rows, cited_sources = [], []
    for cid in ids:
        c = claims_by_id.get(cid)
        if not c:
            continue
        srcs = []
        for sid in c["sources"]:
            s = sources_by_id.get(sid)
            if s:
                srcs.append(s["citation"])
                if s["type"] != "conceptual-internal":
                    cited_sources.append(s)
        tag = {"sourced": "Sourced", "internal-framework": "Framework",
               "conceptual": "Conceptual"}.get(c["status"], c["status"])
        src_txt = "; ".join(html.escape(x) for x in srcs)
        rows.append(
            '<li><span class="ref-tag">%s</span> %s <span class="ref-src">%s</span></li>'
            % (tag, html.escape(c["statement"]), src_txt)
        )
    # de-duplicate cited sources, preserve order
    seen, uniq = set(), []
    for s in cited_sources:
        if s["id"] not in seen:
            seen.add(s["id"])
            uniq.append(s)
    section = ('<section class="rl-refs"><h2>References &amp; claim provenance</h2>'
               '<p class="rl-refs-note">Every claim below is registered and classified. '
               '&ldquo;Sourced&rdquo; claims rest on the listed references; '
               '&ldquo;Framework&rdquo; claims are internal conceptual mappings, not external fact.</p>'
               '<ul class="rl-reflist">%s</ul></section>') % "".join(rows)
    return section, uniq


def json_ld(meta, route, cited_sources):
    name = meta.get("term") or meta.get("title") or "Zonules.com"
    desc = meta.get("meta_description", "")
    url = BASE + route["path"]
    term = {
        "@context": "https://schema.org",
        "@type": "DefinedTerm",
        "name": name,
        "description": desc,
        "url": url,
        "inDefinedTermSet": BASE + "/glossary/",
        "termCode": meta.get("term_id", ""),
        "isPartOf": {"@type": "WebSite", "name": "Zonules.com", "url": BASE + "/"},
    }
    if cited_sources:
        term["citation"] = [s["citation"] for s in cited_sources]
    crumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Zonules.com", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2,
             "name": LAYER_NAME.get(meta.get("layer", ""), "Reference"),
             "item": BASE + "/glossary/"},
            {"@type": "ListItem", "position": 3, "name": name, "item": url},
        ],
    }
    blocks = []
    for obj in (term, crumbs):
        blocks.append('<script type="application/ld+json">%s</script>'
                      % json.dumps(obj, ensure_ascii=True, separators=(",", ":")))
    return "\n".join(blocks)


# ---------- page assembly ----------

def head(meta, route, extra=""):
    title = meta.get("seo_title") or route.get("seo_title") or meta.get("term", "Zonules.com")
    desc = meta.get("meta_description") or route.get("meta_description", "")
    url = BASE + route["path"]
    return """<!DOCTYPE html>
<html lang="%(lang)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<link rel="alternate" hreflang="en" href="%(url)s">
<link rel="alternate" hreflang="x-default" href="%(url)s">
<meta property="og:type" content="article">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s">
<link rel="stylesheet" href="%(css)s">
%(extra)s
</head>""" % {
        "lang": meta.get("language", "en"),
        "title": html.escape(title, quote=True),
        "desc": html.escape(desc, quote=True),
        "url": url,
        "css": css_href(route["path"]),
        "extra": extra,
    }


def breadcrumb(meta, name):
    layer = LAYER_NAME.get(meta.get("layer", ""), "Reference")
    return ('<nav class="rl-crumb" aria-label="Breadcrumb"><a href="/">Zonules.com</a>'
            ' <span aria-hidden="true">/</span> <a href="/glossary/">%s</a>'
            ' <span aria-hidden="true">/</span> <span aria-current="page">%s</span></nav>'
            % (html.escape(layer), html.escape(name)))


def render_unit(route, meta, body, claims_by_id, sources_by_id):
    name = meta.get("term") or meta.get("title", "")
    refs_html, cited = references_section(meta, claims_by_id, sources_by_id)
    badges = ""
    if meta.get("layer") in ("L1", "L2", "L3"):
        badges = ('<p class="rl-badges">'
                  '<span class="rl-badge">Layer %s · %s</span>'
                  '<span class="rl-badge">%s</span>'
                  '<span class="rl-badge">%s</span></p>'
                  % (meta["layer"][-1], html.escape(LAYER_NAME[meta["layer"]]),
                     html.escape(meta.get("fio_class", "")),
                     html.escape(meta.get("fis_criterion", ""))))
    codes_note = ""
    if meta.get("layer") in ("L1", "L2", "L3"):
        codes_note = ('<p class="rl-codes-note">These are '
                      '<a href="/focus-integrity-codes/">Focus Integrity Codes</a>: '
                      '<strong>FIO</strong> names the failure class this term belongs to in the '
                      'ontology; <strong>FIS</strong> names the matching standard criterion. '
                      '<a href="/focus-integrity-codes/">What do these codes mean?</a></p>')
    article = render_markdown(body)
    return (head(meta, route, json_ld(meta, route, cited)) +
            '\n<body class="rl">\n<main class="rl-wrap">\n' +
            breadcrumb(meta, name) + badges + codes_note + '<article class="rl-article">' +
            article + refs_html +
            '</article>\n'
            '<footer class="rl-foot"><a href="/glossary/">All reference units</a> · '
            '<a href="/focus-integrity-ontology/">Ontology</a> · '
            '<a href="/methodology/">Methodology</a> · '
            '<a href="/source-policy/">Source policy</a> · '
            '<a href="/focus-integrity-engine/">Focus Integrity Engine</a></footer>\n'
            '</main>\n</body>\n</html>\n')


def render_glossary(routes, by_path):
    """Generate the glossary hub from the registry — links can never break."""
    groups = {"L1": [], "L2": [], "L3": [], "cross": []}
    for r in routes:
        if r.get("page_type") != "reference-unit":
            continue
        groups.setdefault(r.get("layer", "cross"), []).append(r)
    sections = []
    order = [("L1", "Layer 01 · Anatomy — the biological suspension of focus"),
             ("L2", "Layer 02 · Perception — attention as the second suspension"),
             ("L3", "Layer 03 · Machine Vision — focus integrity in machines")]
    for key, title in order:
        rows = sorted(groups.get(key, []), key=lambda r: r["path"])
        if not rows:
            continue
        items = "".join(
            '<li><a href="%s">%s</a><span>%s · %s</span></li>'
            % (r["path"], html.escape(r["seo_title"].split(" — ")[0].split(" | ")[0]),
               html.escape(r.get("fio_class", "")), html.escape(r.get("fis_criterion", "")))
            for r in rows
        )
        sections.append('<section class="gl-group"><h2>%s</h2><ul class="gl-list">%s</ul></section>'
                        % (html.escape(title), items))
    meta = {"language": "en", "layer": "cross",
            "seo_title": "Glossary — The Governed Reference Index | Zonules.com",
            "meta_description": "The complete governed index of Zonules.com reference units across anatomy, perception, and machine vision — each a node in the focus-integrity system."}
    route = {"path": "/glossary/", "seo_title": meta["seo_title"],
             "meta_description": meta["meta_description"]}
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet",
          "name": "Zonules.com Reference Glossary", "url": BASE + "/glossary/",
          "hasDefinedTerm": [BASE + r["path"] for r in routes if r.get("page_type") == "reference-unit"]}
    extra = '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=True, separators=(",", ":"))
    return (head(meta, route, extra) +
            '\n<body class="rl">\n<main class="rl-wrap">\n' +
            breadcrumb(meta, "Glossary") +
            '<article class="rl-article"><h1>The Reference Index</h1>'
            '<p>Every unit below is a governed node in the focus-integrity system: '
            'registered, source-classified, internally linked, and safety-checked. '
            'No page exists here that does not earn its place.</p>'
            '<p>Each unit is tagged with two <a href="/focus-integrity-codes/">Focus Integrity '
            'Codes</a>. The <strong>FIO</strong> code names the failure class the term belongs to; '
            'the <strong>FIS</strong> code names the matching standard criterion. New readers can '
            'start with <a href="/focus-integrity-codes/">what the codes mean</a> or the '
            '<a href="/focus-integrity-ontology/">ontology</a> that defines them.</p>' +
            "".join(sections) +
            '</article>\n<footer class="rl-foot"><a href="/">Gateway</a> · '
            '<a href="/focus-integrity-ontology/">Ontology</a> · '
            '<a href="/focus-integrity-codes/">Focus Integrity Codes</a> · '
            '<a href="/methodology/">Methodology</a> · <a href="/source-policy/">Source policy</a>'
            '</footer>\n</main>\n</body>\n</html>\n')


def render_ontology(routes, fio, fis):
    """Generate the ontology hub from FIO + FIS — the governing spine, browsable and citable."""
    fis_by_inv = {c["inverse_of"]: c for c in fis["criteria"]}
    units_by_class = {}
    for r in routes:
        if r.get("page_type") == "reference-unit" and r.get("language", "en") == "en":
            units_by_class.setdefault(r.get("fio_class"), []).append(r)

    crit_rows = "".join(
        '<li><strong>%s · %s.</strong> %s</li>' % (
            html.escape(c["id"]), html.escape(c["name"]), html.escape(c["statement"]))
        for c in fis["criteria"]
    )

    class_blocks = []
    for c in fio["classes"]:
        fis_c = fis_by_inv.get(c["id"])
        layers = "".join(
            '<li><span class="ont-layer">%s</span> %s</li>' % (lk, html.escape(lv))
            for lk, lv in c["layers"].items()
        )
        units = units_by_class.get(c["id"], [])
        unit_links = "".join(
            '<a href="%s">%s</a>' % (u["path"], html.escape(u["seo_title"].split(" — ")[0].split(" | ")[0]))
            for u in sorted(units, key=lambda r: r["path"])
        )
        unit_html = ('<p class="ont-units"><span>Reference units:</span> %s</p>' % unit_links) if unit_links else ""
        inv = (' <span class="ont-inv">Inverse of %s · %s</span>'
               % (html.escape(fis_c["id"]), html.escape(fis_c["name"]))) if fis_c else ""
        class_blocks.append(
            '<section class="ont-class" id="%s">'
            '<h3>%s · %s%s</h3>'
            '<p class="ont-def">%s</p>'
            '<blockquote>%s</blockquote>'
            '<ul class="ont-layers">%s</ul>%s</section>' % (
                html.escape(c["id"]).lower(),
                html.escape(c["id"]), html.escape(c["name"]), inv,
                html.escape(c["definition"]),
                html.escape(c["governing_claim"]),
                layers, unit_html,
            )
        )

    meta = {"language": "en", "layer": "cross",
            "seo_title": "The Focus Integrity Ontology — How Focus Fails and What Holds It | Zonules.com",
            "meta_description": "The Focus Integrity Ontology classifies how focus fails across anatomy, perception, and machine vision; the Focus Integrity Standard defines what intact focus is. The governing spine of Zonules.com."}
    route = {"path": "/focus-integrity-ontology/", "seo_title": meta["seo_title"],
             "meta_description": meta["meta_description"]}
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet",
          "name": "Focus Integrity Ontology", "url": BASE + "/focus-integrity-ontology/",
          "description": meta["meta_description"],
          "hasDefinedTerm": [{"@type": "DefinedTerm", "termCode": c["id"], "name": c["name"],
                              "description": c["definition"]} for c in fio["classes"]]}
    extra = '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=True, separators=(",", ":"))
    return (head(meta, route, extra) +
            '\n<body class="rl">\n<main class="rl-wrap">\n' +
            breadcrumb(meta, "Focus Integrity Ontology") +
            '<article class="rl-article"><h1>The Focus Integrity Ontology</h1>'
            '<p>This is the governing spine of the asset. The <strong>Focus Integrity Standard</strong> '
            'defines what intact focus is; the <strong>Focus Integrity Ontology</strong> classifies how it '
            'fails. The same five-part structure runs through anatomy, perception, and machine vision — '
            'because the logic of held focus is one logic across all three.</p>'
            '<p>Every reference unit is tagged with an <strong>FIO</strong> class and an '
            '<strong>FIS</strong> criterion from this page. If you are meeting these codes for the '
            'first time, the <a href="/focus-integrity-codes/">Focus Integrity Codes</a> page '
            'explains what they are and how to read them.</p>'
            '<h2>The Focus Integrity Standard — what intact focus is</h2>'
            '<p>A seeing system has focus integrity when all five criteria hold (FIS v%s):</p>'
            '<ul class="ont-crit">%s</ul>'
            '<h2>The Focus Integrity Ontology — how focus fails</h2>'
            '<p>Each failure class is the inverse of one standard criterion (FIO v%s). Every class '
            'resolves to the governed reference units that explain it.</p>'
            '%s'
            '</article>\n'
            '<footer class="rl-foot"><a href="/glossary/">All reference units</a> · '
            '<a href="/focus-integrity-codes/">Focus Integrity Codes</a> · '
            '<a href="/focus-integrity-engine/">Run the assessment</a> · '
            '<a href="/methodology/">Methodology</a></footer>\n'
            '</main>\n</body>\n</html>\n'
            % (html.escape(fis["version"]), crit_rows, html.escape(fio["version"]), "".join(class_blocks)))


def outputs():
    routes = load("routes.json")["routes"]
    claims = {c["id"]: c for c in load("claims.json")["claims"]}
    sources = {s["id"]: s for s in load("sources.json")["sources"]}
    fio = load("focus-integrity-ontology.json")
    fis = load("focus-integrity-standard.json")
    by_path = {r["path"]: r for r in routes}
    pages = {}
    for r in routes:
        if r.get("page_type") not in ("reference-unit", "policy"):
            continue
        src = os.path.join(ROOT, r["content"])
        with open(src, encoding="utf-8") as fh:
            meta, body = parse_frontmatter(fh.read())
        pages[r["path"]] = render_unit(r, meta, body, claims, sources)
    pages["/glossary/"] = render_glossary(routes, by_path)
    pages["/focus-integrity-ontology/"] = render_ontology(routes, fio, fis)
    return pages


def path_to_file(path):
    rel = path.strip("/")
    return os.path.join(SITE, rel, "index.html") if rel else os.path.join(SITE, "index.html")


def main():
    pages = outputs()
    css = open(CSS_SRC, encoding="utf-8").read()
    if "--check" in sys.argv[1:]:
        stale = []
        for path, content in pages.items():
            fp = path_to_file(path)
            if not os.path.exists(fp) or open(fp, encoding="utf-8").read() != content:
                stale.append(path)
        if not os.path.exists(CSS_OUT) or open(CSS_OUT, encoding="utf-8").read() != css:
            stale.append(CSS_REL)
        if stale:
            print("STALE rendered output: " + ", ".join(sorted(stale)) + ". Run scripts/build_site.py")
            return 1
        print("FRESH: %d rendered pages + shared stylesheet match governed sources." % len(pages))
        return 0
    for path, content in pages.items():
        fp = path_to_file(path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        with open(fp, "w", encoding="utf-8") as fh:
            fh.write(content)
    os.makedirs(os.path.dirname(CSS_OUT), exist_ok=True)
    with open(CSS_OUT, "w", encoding="utf-8") as fh:
        fh.write(css)
    print("Rendered %d pages + shared stylesheet into the repository root" % len(pages))
    return 0


if __name__ == "__main__":
    sys.exit(main())
