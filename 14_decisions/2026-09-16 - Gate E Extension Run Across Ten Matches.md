---
type: decision
status: decided
date: "2026-09-16/17"
related:
  - "[[../25_gate_validation/GATE_E_MULTI_MATCH_OFFSET_RESULTS]]"
  - "[[../26_implementation_architecture/QUARANTINE_MECHANISM_DESIGN]]"
---

# Decision: Gate E Extension Run Across Ten Matches

## Decision

Do not hard-code the Release 05 pilot's 1-second RGB/GSR offset as a
universal constant. Instead, treat alignment as a per-half property
that must be checked and, where needed, corrected or quarantined
individually.

## Reasoning

`claude/gate_e_multi_match_offset_check.py` re-ran the direct-overlay
offset check across all 10 matches / 20 halves. The 1-second offset
held in 14 of 20 halves and was absent in 6. A separate, previously
undocumented tail-loss defect (~10 seconds of missing video) was found
in 10 of 20 halves. One half could not be classified by the check.
Hard-coding a single constant would have silently misaligned the 6
halves without the offset and ignored the tail-loss defect entirely.

## Alternatives considered

- **Keep the Release 05 constant and proceed.** Rejected: directly
  contradicted by the measured distribution across halves.
- **Discard the offset finding entirely as unreliable.** Rejected: it
  is still correct for 14 of 20 halves; discarding it would lose real,
  confirmed information for the majority case.

## Consequences

- Alignment logic in `common.py` needs a per-half check, not a single
  constant — this is the direct motivation for the general quarantine
  mechanism, see [[../26_implementation_architecture/QUARANTINE_MECHANISM_DESIGN]].
- The one unresolved half is treated as open, not passing by default,
  pending further review (that review happened during N1 execution and
  is out of scope for this release).
- This result is generalized into
  [[../../Reusable_Research_OS/13_gate_extension_validation/MULTI_INSTANCE_GENERALIZATION_CHECK]].
