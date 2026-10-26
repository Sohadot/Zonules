#!/usr/bin/env python3
"""
Zonules.com — Publication Safety Gate.

Blocking validator for the deployment artifact. Exit code 0 = pass, 1 = fail.
It checks a built artifact directory independently of the script that built it:

  1. Allowlist: every file must be explicitly allowed — a fixed list of root
     and asset files, plus <page>/index.html for registered public pages.
  2. Denylist (defence in depth): no Markdown, Python, JSON, YAML, JavaScript
     sources, Git metadata, or files under internal directories, whatever the
     allowlist says.
  3. Completeness: every registered public page is present, so the artifact
     can never silently drop part of the reference.
  4. Integrity: every internal link, stylesheet, sitemap URL, and hreflang
     alternate in the artifact resolves to a file in the artifact.
  5. Content: no published page contains internal strategy markers.

Usage:
  python scripts/validate_publication.py          # build to a temp dir and check
  python scripts/validate_publication.py DIR      # check an existing artifact
  python scripts/validate_publication.py --repo DIR   # check a public-repo checkout
"""
import importlib.util
import json
import os
import re
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://zonules.com"

# The explicit public-output allowlist. Changing it is a publication decision
# and requires a DECISION_LOG.md entry.
ALLOWED_FILES = {"CNAME", ".nojekyll", "robots.txt", "sitemap.xml", "assets/css/reference.css"}
ALLOWED_EXTRA_PAGES = {"/languages/"}

DENY_EXTENSIONS = (".md", ".py", ".json", ".yml", ".yaml", ".js", ".mjs", ".ts",
                   ".sh", ".toml", ".ini", ".env", ".pem", ".key", ".log")
DENY_DIRS = ("data/", "scripts/", "content/", "static/", "docs/", "templates/",
             ".git/", ".github/", "site/")
# Phrases that appear only in internal governance and strategy documents.
STRATEGY_MARKERS = ("Inevitability Principle", "Banana Problem", "The Loss Question",
                    "Loss-in-Not-Acquiring", "Respectable Income", "BUYER_LOGIC_AND_VALUE")


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as fh:
        return json.load(fh)


def registered_pages():
    pages = {r["path"] for r in load("routes.json")["routes"] if r.get("status") == "approved"}
    for entry in load("translation-map.json")["routes"]:
        for trans in entry.get("translations", {}).values():
            if trans.get("status") == "launched" and trans.get("path"):
                pages.add(trans["path"])
    return pages | ALLOWED_EXTRA_PAGES


def page_file(path):
    rel = path.strip("/")
    return rel + "/index.html" if rel else "index.html"


def resolve(href, page_rel):
    """Map an href on a page to an artifact-relative file, or None if external."""
    href = href.split("#", 1)[0].split("?", 1)[0]
    if not href or href.startswith(("mailto:", "tel:")):
        return None
    if href.startswith(BASE):
        href = href[len(BASE):] or "/"
    elif re.match(r"^[a-z]+:", href) or href.startswith("//"):
        return None
    if href.startswith("/"):
        rel = href.lstrip("/")
    else:
        rel = os.path.normpath(os.path.join(os.path.dirname(page_rel), href)).replace(os.sep, "/")
    if rel in ("", "."):
        return "index.html"
    return rel + "index.html" if rel.endswith("/") else rel


def validate(art, repo_mode=False):
    """repo_mode: art is a checkout of the public publication repository; its
    own top-level .git directory is skipped (and nothing else is)."""
    errors = []
    files = set()
    for dirpath, dirs, names in os.walk(art):
        if repo_mode and os.path.abspath(dirpath) == os.path.abspath(art) and ".git" in dirs:
            if not os.path.isdir(os.path.join(art, ".git")):
                errors.append(".git is not a directory")
            dirs.remove(".git")
        for n in names:
            files.add(os.path.relpath(os.path.join(dirpath, n), art).replace(os.sep, "/"))

    pages = registered_pages()
    allowed = ALLOWED_FILES | {page_file(p) for p in pages}

    # 1-2. Allowlist and denylist.
    for f in sorted(files):
        if f not in allowed:
            errors.append(f"not on the public allowlist: {f}")
        if f.lower().endswith(DENY_EXTENSIONS) or any(f.startswith(d) or ("/" + d) in f for d in DENY_DIRS):
            errors.append(f"restricted file in artifact: {f}")

    # 3. Completeness.
    for f in sorted(allowed - files):
        errors.append(f"public file missing from artifact: {f}")

    # 4-5. Integrity and content of every published page.
    for f in sorted(x for x in files if x.endswith(".html")):
        text = open(os.path.join(art, f), encoding="utf-8").read()
        for marker in STRATEGY_MARKERS:
            if marker in text:
                errors.append(f"{f} contains internal strategy marker '{marker}'")
        for href in sorted(set(re.findall(r'(?:href|src)="([^"]+)"', text))):
            target = resolve(href, f)
            if target and target not in files:
                errors.append(f"{f} links to {href}, which is not in the artifact")

    if "sitemap.xml" in files:
        sm = open(os.path.join(art, "sitemap.xml"), encoding="utf-8").read()
        for url in set(re.findall(r'<loc>([^<]+)</loc>', sm) + re.findall(r'href="([^"]+)"', sm)):
            target = resolve(url, "sitemap.xml")
            if target and target not in files:
                errors.append(f"sitemap URL {url} is not in the artifact")
    if "CNAME" in files and open(os.path.join(art, "CNAME")).read().strip() != "zonules.com":
        errors.append("CNAME must contain exactly zonules.com")
    return errors, len(files)


def main():
    args = [a for a in sys.argv[1:] if a != "--repo"]
    if args:
        art = os.path.abspath(args[0])
        errors, n = validate(art, repo_mode="--repo" in sys.argv)
    else:
        spec = importlib.util.spec_from_file_location(
            "build_public_site", os.path.join(ROOT, "scripts", "build_public_site.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        with tempfile.TemporaryDirectory() as tmp:
            art = os.path.join(tmp, "_site")
            mod.assemble(art)
            errors, n = validate(art)
    if errors:
        print("PUBLICATION GATE: FAIL")
        for e in errors[:200]:
            print("  -", e)
        return 1
    print("PUBLICATION GATE: PASS")
    print(f"  files={n} allowlist-only, no restricted files, all links/sitemap/hreflang resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
