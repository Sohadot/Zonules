#!/usr/bin/env python3
"""
Assemble the public publication artifact for zonules.com.

The repository root holds the generated site *and* the project's governance,
registries, scripts, and source content. Publishing the root directly serves
all of it. This script copies only the approved public pages into a separate
output directory, which is what the Pages workflow uploads and deploys.

What is copied (and nothing else):
  - index.html for every registered English route (data/routes.json)
  - index.html for every launched translation (data/translation-map.json)
  - index.html for each explicitly approved extra page (EXTRA_PAGES)
  - the explicitly approved root and asset files (PUBLIC_FILES)

Governance Markdown, scripts, data registries, content sources, docs, and
static sources are never copied. scripts/validate_publication.py then checks
the result independently against its own allowlist.

Pure standard library. No network.
Usage:
  python scripts/build_public_site.py              # writes ./_site
  python scripts/build_public_site.py --out DIR
"""
import json
import os
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Files outside page directories that the public site needs.
PUBLIC_FILES = ["CNAME", ".nojekyll", "robots.txt", "sitemap.xml", "assets/css/reference.css"]
# Public pages that are generated but not held in a route registry.
EXTRA_PAGES = ["/languages/"]


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as fh:
        return json.load(fh)


def public_pages():
    pages = {r["path"] for r in load("routes.json")["routes"] if r.get("status") == "approved"}
    for entry in load("translation-map.json")["routes"]:
        for trans in entry.get("translations", {}).values():
            if trans.get("status") == "launched" and trans.get("path"):
                pages.add(trans["path"])
    pages.update(EXTRA_PAGES)
    return sorted(pages)


def page_file(path):
    rel = path.strip("/")
    return os.path.join(rel, "index.html") if rel else "index.html"


def assemble(out):
    if os.path.exists(out):
        # Only ever clear a previous artifact, never a source tree.
        if any(os.path.exists(os.path.join(out, x)) for x in (".git", "scripts", "data", "content")):
            raise SystemExit("build_public_site: refusing to clear %s (looks like a source tree)" % out)
        shutil.rmtree(out)
    files = [page_file(p) for p in public_pages()] + PUBLIC_FILES
    missing = [f for f in files if not os.path.isfile(os.path.join(ROOT, f))]
    if missing:
        raise SystemExit("build_public_site: missing source files: " + ", ".join(missing[:10]))
    for rel in files:
        dst = os.path.join(out, rel)
        os.makedirs(os.path.dirname(dst) or out, exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, rel), dst)
    return files


def main():
    out = os.path.join(ROOT, "_site")
    if "--out" in sys.argv:
        out = os.path.abspath(sys.argv[sys.argv.index("--out") + 1])
    if os.path.realpath(out) == os.path.realpath(ROOT):
        raise SystemExit("build_public_site: refusing to write into the repository root")
    files = assemble(out)
    print("Assembled public site: %d files into %s" % (len(files), os.path.relpath(out, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
