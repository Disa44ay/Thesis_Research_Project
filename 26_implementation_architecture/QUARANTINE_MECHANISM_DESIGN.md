---
type: architecture-decision
status: decided
decided: "pre-N1, generalized from the match 132831 calibration-defect precedent"
related:
  - "[[COMMON_PY_ARCHITECTURE]]"
  - "[[../25_gate_validation/GATE_E_MULTI_MATCH_OFFSET_RESULTS]]"
---

# Quarantine Mechanism — Design

## Why this exists

The Gate E extension confirmed the dataset is not uniform: the
RGB/GSR offset holds in most but not all halves, a separate tail-loss
defect affects about half the halves, and at least one half could not
be classified by the check at all. A pipeline that assumes every match
is clean will silently produce wrong alignment for the matches that are
not. The project already had one precedent for this problem — a
calibration defect in match 132831 that had to be excluded by hand
before Release 05 — and the Gate E extension result showed this was not
a one-off.

## Design

`common.py` defines a `QUARANTINE_MATCHES` (or equivalent per-half)
mechanism: a single, explicit, named list of dataset instances excluded
from default processing, together with the reason each entry is there.
Any notebook that iterates over matches or halves checks this list
before processing and skips (or flags) quarantined entries, rather than
each notebook re-implementing its own ad hoc exclusion logic.

## Requirements this mechanism must meet

1. **Single source of truth.** The list lives in `common.py` only; no
   notebook hard-codes its own separate exclusion list.
2. **Reasoned, not silent.** Each entry records why it is quarantined
   (calibration defect, unresolved alignment, tail loss) so a future
   reader does not have to reverse-engineer the reason.
3. **Additive, not destructive.** Quarantining an instance removes it
   from default processing paths; it does not delete the instance's
   underlying data or its record in the gate-validation results.
4. **Revisitable.** An instance can be un-quarantined if a later check
   resolves the reason it was excluded — the mechanism is a gate, not a
   permanent deletion.

## What this design does not decide

This file specifies the general mechanism only. It does not decide
which specific matches or halves are quarantined under it — that is a
per-instance decision made as each notebook actually runs and applies
the mechanism.

## Scope note

The match 132877 quarantine decision itself was made during N1
execution (2026-09-22) and is explicitly out of scope for this release.
This file documents only the general design pattern, decided
pre-implementation and generalized from the pre-existing 132831
precedent, which is in scope.
