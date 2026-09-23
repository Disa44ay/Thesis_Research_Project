---
type: gate-result
status: resolved
gate: "Gate E extension — Multi-Match RGB/GSR Offset Check"
resolved: 2026-09-16/17
related:
  - "[[../14_decisions/2026-09-16 - Gate E Extension Run Across Ten Matches]]"
  - "[[GATE_STATUS_SUMMARY]]"
  - "[[../../Reusable_Research_OS/13_gate_extension_validation/MULTI_INSTANCE_GENERALIZATION_CHECK]]"
---

# Gate E Extension — Multi-Match Offset Results

## Why this gate existed

The Release 05 feasibility pilot confirmed, on a single match (117093),
that the RGB video stream and the GSR game-state stream shared a
nominal frame rate but were offset by a fixed 1.000-second gap in
presentation timestamps. That result was confirmed on one match, one
half. Before hard-coding a 1-second correction into the shared
alignment code, the project needed to know whether that offset held
across the full ten-match dataset it intended to use.

## Method

`claude/gate_e_multi_match_offset_check.py` re-ran the same
direct-overlay offset check used in the Release 05 pilot against all 10
matches (20 halves) in the target dataset.

## Result

- The previously-confirmed 1-second offset was present in 14 of 20
  halves.
- It was absent in 6 of 20 halves.
- The offset is therefore **not a universal constant** across the
  dataset and cannot be safely hard-coded as a fixed correction applied
  to every match.

## A second, previously undocumented defect

The extended check independently surfaced a defect the single-match
pilot had no opportunity to find: approximately 10 seconds of video
missing from the tail of 10 of the 20 halves. This is a separate issue
from the presentation-timestamp offset and was not visible from a
single-instance test.

## Unresolved instance

One half (match 132877, first half) did not fit either the confirmed
offset pattern or the tail-loss pattern cleanly (a residual of +12
frames unexplained by either). Per this gate's own validation
principle, an instance the check cannot classify is left unresolved,
not passed by default. The final quarantine decision for this specific
half was made later, during N1 notebook execution (2026-09-22), and is
explicitly **out of scope for this release** — see the Scope note
below.

## What this changed

The alignment picture changed from "a fixed offset exists" (Release 05,
one instance) to "a fixed offset exists in most, but not all, instances,
and a second, unrelated defect exists in about half" (Release 06, full
population). This is a materially different and more useful result than
the single-instance version, and it means the alignment code needs a
per-half correction table or an explicit skip/quarantine mechanism
rather than one constant.

## Status

Resolved 2026-09-16/17 for the check itself. Generalized, without
thesis-specific numbers, into
[[../../Reusable_Research_OS/13_gate_extension_validation/MULTI_INSTANCE_GENERALIZATION_CHECK]].

## Scope note

This file documents the multi-match check and its aggregate findings,
which are pre-implementation and in scope for Release 06. The specific
quarantine decision applied to match 132877 during N1 execution, and
all other N1 dataset-inventory and window-count figures, are N1-era and
are explicitly out of scope for this release — reserved for the future
N1-N5 release.
