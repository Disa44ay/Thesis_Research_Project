#!/usr/bin/env python3
"""Minimal Obsidian/Git vault validator added during public-release reconstruction.

Checks Markdown wikilinks, local Markdown links, duplicate note stems,
basic orphan connectivity, and accidental machine-local paths.
It does not infer uncertain intended targets.
"""
from pathlib import Path
import re, sys, json

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
mds = list(root.rglob("*.md"))
by_stem = {}
for p in mds:
    by_stem.setdefault(p.stem, []).append(p)

dupe_stems = {k:[str(x.relative_to(root)) for x in v] for k,v in by_stem.items() if len(v)>1}
incoming = {p.resolve():0 for p in mds}
unresolved = []
bad_local_paths = []
wikire = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
mdlinkre = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

def resolve_wiki(src, target):
    target = target.strip()
    candidates = []
    # relative-path target first
    rel = src.parent / target
    if rel.suffix.lower() != ".md":
        rel = rel.with_suffix(".md")
    candidates.append(rel)
    # vault-root target
    rr = root / target
    if rr.suffix.lower() != ".md":
        rr = rr.with_suffix(".md")
    candidates.append(rr)
    # unique stem
    stem = Path(target).stem
    if stem in by_stem and len(by_stem[stem]) == 1:
        candidates.append(by_stem[stem][0])
    for c in candidates:
        if c.exists():
            return c.resolve()
    return None

for p in mds:
    text = p.read_text(encoding="utf-8", errors="ignore")
    if re.search(r"(?i)(?:/mnt/|/home/[^/\s]+/|[A-Z]:\\\\)", text):
        bad_local_paths.append(str(p.relative_to(root)))
    for m in wikire.finditer(text):
        t = m.group(1)
        q = resolve_wiki(p, t)
        if q is None:
            unresolved.append({"source":str(p.relative_to(root)),"target":t,"type":"wikilink"})
        elif q in incoming:
            incoming[q]+=1
    for m in mdlinkre.finditer(text):
        raw = m.group(1).strip().split("#",1)[0]
        if not raw or re.match(r"^(?:https?://|mailto:|#)", raw):
            continue
        # angle wrappers
        raw=raw.strip("<>")
        q=(p.parent/raw).resolve()
        if q.exists():
            if q.suffix.lower()==".md" and q in incoming:
                incoming[q]+=1
        else:
            unresolved.append({"source":str(p.relative_to(root)),"target":raw,"type":"markdown-link"})

navigation = {"README.md","VERSION_BRIEF.md","RELEASE_HISTORY.md","ARCHITECTURE.md","GRAPH_AUDIT.md"}
orphans=[str(p.relative_to(root)) for p,n in incoming.items() if n==0 and p.name not in navigation and "README_BEFORE_RELEASE_RECONSTRUCTION.md" not in p.name]

result={
    "root":str(root),
    "markdown_notes":len(mds),
    "duplicate_stems":dupe_stems,
    "unresolved_links":unresolved,
    "non_navigation_orphans":orphans,
    "machine_local_path_notes":sorted(set(bad_local_paths)),
}
print(json.dumps(result, indent=2))
sys.exit(1 if unresolved or dupe_stems else 0)
