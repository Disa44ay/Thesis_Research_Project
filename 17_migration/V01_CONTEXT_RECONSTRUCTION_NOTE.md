---
type: correction-note
status: resolved
verified: 2026-09-10
---

# V01 Context File Anomaly — Root Cause and Correction

## The anomaly (as originally flagged)

`Thesis_Project_V01_Context.txt`'s embedded `VERSION_BRIEF.md` extract
was byte-identical to `Thesis_Project_V04_Context.txt`'s, both showing
`public_release: "Release 04"`, despite the file being labeled Release
01.

## Root cause (confirmed)

The local working folder used to generate these context files -
`Thesis_Research_Project_Release_01_Foundation_and_Scope_Formation/Thesis_Research_Project/`
- is a live Git checkout, not a per-release static snapshot. At the
time the context extraction ran, that checkout was sitting at HEAD
(commit `eff3c29`, the Release 04 state), regardless of the folder's
Release-01 name. The extraction faithfully captured whatever was
actually checked out - it did not misread anything, the checkout
itself was pointed at the wrong commit for that folder's intended
purpose.

## Correct Release 01 content (recovered via `git show 4fcc926:VERSION_BRIEF.md`)

```
public_release: "Release 01"
historical_basis: "historical v1-v2 period, endpoint v2 (2026-08-10)"
```

Previous public release: None. The full recovered file summarizes the
project's original vault split and its earliest reorganization into a
graph-native Obsidian workflow, and states that the project began as a
broad computer-vision thesis search, that PCBAS was still provisional
at that point, that football had just been locked as the domain, and
that candidate search had expanded to include BAA, tactical retrieval,
and tactical forecasting.

## What this means for this repository

Nothing in Release 04 or Release 05 was built on the corrupted V01
extract - both were built forward from the actual, correctly-checked-
out Release 04 state. This anomaly affected only the standalone
`Thesis_Project_V01_Context.txt` reference file, not any release
package. It is documented here so a future session doesn't need to
re-discover it, and so anyone regenerating context files from the
local Git history checks out the correct commit per folder rather than
whatever happens to be at HEAD.

------------------------------------------------------------------------
