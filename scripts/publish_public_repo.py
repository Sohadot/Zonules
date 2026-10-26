#!/usr/bin/env python3
"""
Synchronise the allowlisted public artifact into a checkout of the public
publication repository (Sohadot/zonules-public) and commit it there.

This is the only path by which anything reaches the public repository. It:
  1. refuses to run unless the target checkout's origin is the public repo;
  2. replaces the checkout's working tree (never its .git) with the artifact;
  3. re-runs the publication gate on the exact tree to be committed;
  4. refuses if any commit in the public repository also exists in the
     private source repository (no shared history, ever);
  5. commits as a single new commit with a neutral identity and message.

It never pushes. Pushing is a separate, explicit step (see the workflow), and
it is always a normal fast-forward push of the public checkout's own branch —
never a mirror push and never a push from the source repository.

Usage:
  python scripts/publish_public_repo.py --artifact _site --repo PUBLIC_CHECKOUT \
      [--source .] [--allow-init]
"""
import argparse
import datetime
import importlib.util
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUBLIC_REPO = "Sohadot/zonules-public"
BOT_NAME = "zonules-publisher"
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"


def git(repo, *args, check=True):
    res = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True)
    if check and res.returncode != 0:
        raise SystemExit("git %s failed: %s" % (" ".join(args), res.stderr.strip()))
    return res


def load_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_publication", os.path.join(ROOT, "scripts", "validate_publication.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ORIGIN_RE = re.compile(r"^(?:https://(?:[^@/]+@)?github\.com/|git@github\.com:|ssh://git@github\.com/)"
                       r"sohadot/zonules-public(?:\.git)?/?$", re.I)


def check_origin(repo):
    url = git(repo, "config", "--get", "remote.origin.url", check=False).stdout.strip()
    if not ORIGIN_RE.match(url):
        shown = re.sub(r"//[^@/]+@", "//***@", url)  # never print embedded credentials
        raise SystemExit("refusing: origin of %s is %r, not github.com/%s" % (repo, shown, PUBLIC_REPO))


def check_no_shared_history(repo, source):
    public = git(repo, "rev-list", "--all", check=False).stdout.split()
    shared = [c for c in public
              if subprocess.run(["git", "-C", source, "cat-file", "-e", c + "^{commit}"],
                                capture_output=True).returncode == 0]
    if shared:
        raise SystemExit("refusing: public repository shares %d commit(s) with the source "
                         "repository, e.g. %s" % (len(shared), shared[0]))
    return len(public)


def sync_tree(artifact, repo):
    for name in os.listdir(repo):
        if name == ".git":
            continue
        path = os.path.join(repo, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    for dirpath, _dirs, names in os.walk(artifact):
        for n in names:
            src = os.path.join(dirpath, n)
            rel = os.path.relpath(src, artifact)
            dst = os.path.join(repo, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(src, dst)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--source", default=ROOT)
    ap.add_argument("--allow-init", action="store_true",
                    help="allow committing into a repository with no commits yet")
    a = ap.parse_args()
    artifact, repo, source = (os.path.abspath(x) for x in (a.artifact, a.repo, a.source))

    if os.path.realpath(repo) == os.path.realpath(source):
        raise SystemExit("refusing: target is the source repository")
    if not os.path.isdir(os.path.join(repo, ".git")):
        raise SystemExit("refusing: %s is not a git checkout" % repo)
    check_origin(repo)
    has_commits = git(repo, "rev-parse", "--verify", "HEAD", check=False).returncode == 0
    if not has_commits and not a.allow_init:
        raise SystemExit("refusing: public repository has no commits; pass --allow-init for the first publish")
    n_public = check_no_shared_history(repo, source)

    validator = load_validator()
    errors, _ = validator.validate(artifact)
    if errors:
        raise SystemExit("refusing: artifact fails the publication gate:\n  - " + "\n  - ".join(errors[:20]))

    sync_tree(artifact, repo)
    errors, n_files = validator.validate(repo, repo_mode=True)
    if errors:
        raise SystemExit("refusing: synced tree fails the publication gate:\n  - " + "\n  - ".join(errors[:20]))

    git(repo, "add", "-A")
    if not git(repo, "status", "--porcelain").stdout.strip():
        print("No changes to publish (%d files, %d existing public commits)." % (n_files, n_public))
        return 0
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    git(repo, "-c", "user.name=" + BOT_NAME, "-c", "user.email=" + BOT_EMAIL,
        "-c", "commit.gpgsign=false",
        "commit", "-q", "-m", "Publish zonules.com (%s)" % stamp)
    check_no_shared_history(repo, source)
    print("Committed %d public files to %s; ready for a normal push." % (n_files, PUBLIC_REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
