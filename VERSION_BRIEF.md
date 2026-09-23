---
type: version-brief
status: active
public_release: "Release 06"
historical_basis: "Release 05 plus the pre-implementation Gate H (compute feasibility) and Gate E extension (multi-match offset) pre-tasks, and the four-notebook pipeline architecture decision, 2026-09-14 to 2026-09-17"
updated: 2026-09-22
tags: [release, thesis, gates, architecture, pipeline]
related:
  - "[[README]]"
  - "[[RELEASE_HISTORY]]"
  - "[[ARCHITECTURE]]"
  - "[[25_gate_validation/GATE_STATUS_SUMMARY]]"
  - "[[26_implementation_architecture/FOUR_NOTEBOOK_PIPELINE_DECISION]]"
---

# Version Brief — Release 06

## Release identity

**Project:** Thesis Research Project — Evaluating Game-State Fusion for
Short-Horizon Ball Action Anticipation in Football
**Public release:** Release 06 — Pre-Implementation Gate Extension
**Historical basis:** Release 05 plus the Gate H and Gate E extension
pre-tasks and the four-notebook pipeline architecture decision,
2026-09-14 to 2026-09-17
**Previous public release:** Release 05

## Plain-language summary

Release 05 confirmed, on one match, that the feasibility pilot works:
alignment can be checked, features can be extracted, windows can be
built. Before committing to the full B0-B5 model matrix, two things
still needed measuring rather than assuming — how much the
acquisition/validation stage actually costs to run, and whether the
single-match alignment offset holds across the whole ten-match dataset.
Release 06 records both measurements, the architecture decisions that
followed from them, and stops there — deliberately, before the N1
notebook's own execution.

## What changed

1. Added `25_gate_validation/` — Gate H results, Gate E extension
   results, and a combined status summary that also states an open
   tracking-sync discrepancy honestly rather than resolving it by
   assumption.
2. Added `26_implementation_architecture/` — the four-notebook pipeline
   decision, the shared `common.py` module's architecture, and the
   general quarantine-mechanism design (pattern only, no specific
   match's quarantine decision).
3. Added four decision records under `14_decisions/` covering the
   protocol, the pipeline split, and each gate's resolution.
4. Appended Release 06 entries to `14_decisions/DECISION_LOG.md`,
   `13_execution/ROADMAP.md`, `08_experiments/EXPERIMENT_LOG.md`,
   `18_version_history/VERSION_HISTORY.md`,
   `17_migration/MIGRATION_MANIFEST.md`, and
   `16_session_history/SESSION_LOG.md`.
5. Rewrote `README.md`, `ARCHITECTURE.md`, `GRAPH_AUDIT.md` and added a
   Release 06 row to `RELEASE_HISTORY.md`.
6. Added a new root-level `CURRENT_STATE.md` — a quick-navigation file
   this project did not have before (the existing
   `00_project_governance/CURRENT_STATE.md` is a different, older file
   and is unchanged), mirroring the equivalent file the companion
   Reusable Research OS added at its own Release 05.
7. Added three new diagrams under `docs/diagrams/`, each rendered to a
   PNG under `docs/images/thesis/`.
8. Regenerated `FILE_INTEGRITY_SHA256.txt` covering the full file tree.

## Why it changed

Two named blockers had to close before the model matrix could
responsibly start: unmeasured compute cost, and an unverified
single-match alignment offset. Both were closed by real execution
rather than by re-reading the Release 05 pilot report more carefully.

## What we were trying to learn

Whether the single-match feasibility pilot's results (compute
assumption, alignment offset) could be trusted to hold at full dataset
scale, or whether they needed independent, full-scale verification
first.

## Current understanding

They could not be trusted without verification, and both pre-tasks
changed the picture: compute cost dropped from "assume GPU-bound" to
"measured CPU-only, near-zero cost"; alignment went from "a fixed
1-second offset" to "present in most but not all halves, plus a
separate tail-loss defect the single-match pilot could not have found."

## Remaining uncertainty

The one unresolved half from the Gate E extension check needed further
review before the alignment code could treat every half as classified.
That review happened during N1 execution and is out of scope here. The
tracking-sync gap between this project's two state-tracking systems is
also still open as of this release.

## Next direction

Push Gate H and Gate E extension documentation to the git remote to
close the tracking-sync gap, then scope and package the N1-N5 release
covering the notebook executions themselves.

## Historical continuity

This release is a **complete repository snapshot**, not a patch and not
a reference to an earlier snapshot. Every Release 01-05 file is
physically present in this package, content-identical to the Release 05
snapshot, except where this brief and the specific
root/change-log/session-history files listed above are explicitly
appended to (the earlier release sections of those files are kept
intact above the new Release 06 section, never rewritten in place).
Anyone who opens this Release 06 package alone — without also opening
the Release 04 or Release 05 packages — has the complete project
history from v1 through Release 06 in front of them.

"Content-identical" is stated deliberately rather than "byte-for-byte":
these files were rebuilt from the Release 05 `COMPLETE_CONTEXT.txt` text
dump, and that round trip can normalize a trailing rule line or a curly
quote without changing the substance of a file. `FILE_INTEGRITY_SHA256.txt`
in this package is the authoritative record of the actual bytes shipped
here, computed by hashing this complete tree directly — it is not
assumed to match the original Release 05 repository's own file hashes
bit-for-bit, only its content.

The repository's `.gitignore` and `.obsidian/` vault-config folder were
copied forward unchanged from the Release 05 working copy for this
release. Neither travels through a `COMPLETE_CONTEXT.txt` text-dump
round trip, so an earlier build of this same package omitted them; that
gap is fixed here by copying the real files rather than reconstructing
their contents from scratch. `FILE_INTEGRITY_SHA256.txt` includes their
hashes.

## Preservation notes

Release 06 stops deliberately before N1's execution. Per explicit user
instruction: "up until n1, don't include anything related to n1 — keep
it until the structure update." N1's dataset inventory, alignment
table, window counts, GSR-array results, and the 132877 quarantine
decision are all excluded here, even though N1 has, per project memory,
already run (completed 2026-09-22). This is a scope boundary, not a
claim that the work does not exist.

For the original v1-v5 lineage and Releases 01-05, see
`18_version_history/VERSION_HISTORY.md` and [[RELEASE_HISTORY]].
