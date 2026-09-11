---
type: version-brief
status: active
public_release: "Release 05"
historical_basis: "post-Release-04 executed feasibility pilot, 2026-08-16 to 2026-08-20"
updated: 2026-09-10
tags: [release, history, git, obsidian, feasibility]
related:
  - "[[README]]"
  - "[[RELEASE_HISTORY]]"
  - "[[ARCHITECTURE]]"
  - "[[22_feasibility/FEASIBILITY_STUDY_REPORT]]"
---

# Version Brief — Release 05

## Release identity

**Project:** Thesis Research Project
**Public release:** Release 05 — Feasibility Executed and Experiment-Ready
**Historical basis:** the Release 04 execution-ready state, followed by
the actual execution of the previously-planned feasibility pilot,
2026-08-16 to 2026-08-20
**Previous public release:** Release 04

## Plain-language summary

Release 04 ended with a fully planned, but not yet run, feasibility
pilot. Release 05 records that the pilot was executed on representative
match 117093 from SoccerTrack v2, resulted in a GO decision with strict
scope control, and surfaced one genuinely new engineering finding: the
released panoramic video's presentation timeline starts one second
after match time zero, so RGB and GSR must be aligned by timestamp, not
by raw decoded frame index. This release also converts the experiment
matrix and publication framing from planned to ready-to-execute.

## Previous release summary

Release 04 selected the safest primary title, defined the raw-data-to-
feature-store architecture, and produced a concise verified proposal,
citation audit, and teammate brief — all before the pilot had run. It
explicitly recorded: "the feasibility study is planned and independently
reproducible, but it has not yet been executed, and no scientific model
result exists yet."

## What changed

1. Executed the previously-planned feasibility pilot on match 117093
   (Colab notebook `SoccerTrack_v2_Feasibility_01.ipynb`; report dated
   2026-08-20).
2. Verified the BAS-to-GSR timestamp mapping rule empirically:
   `local_ms = BAS_position - period_matchTimeStart`,
   `local_frame = round(local_ms / 40ms)`, confirmed with zero-frame
   boundary error.
3. Discovered and documented the RGB/GSR one-second presentation-offset
   issue: the panoramic video's PTS timeline begins at 1.000s while GSR
   represents match time from 0.00s, so naive equal-frame-index overlay
   produces visibly misaligned player boxes. Timestamp-based alignment
   resolves this with a measured residual error of ~1.07e-13s (floating
   point noise).
4. Constructed the first real (not simulated) 30s-observation /
   5s-anticipation benchmark for match 117093: 1,092 valid windows (535
   first half, 557 second half); 233 negative, 144 single-action, 715
   multi-action windows; 2,197 target assignments with zero duplicates.
5. Confirmed a leakage-free structured sample (`117093_H1_0006`):
   observation ends 59.96s, future window opens exactly at 60.00s.
6. Extracted and encoded 150 timestamp-synchronized RGB frames via a
   pretrained ResNet-18 probe on CPU, producing a finite (150, 512)
   feature matrix aligned to a (150, 22, 2) structured game-state
   tensor at the same 5 FPS grid.
7. Issued a formal Go/No-Go decision: **GO, with strict scope control**
   — the pipeline is buildable; whether fusion improves anticipation
   remains the untested research hypothesis.
8. Named the concrete remaining risks: only 10 matches total (evaluation
   variance), unresolved rare-class/loss-weighting policy, unresolved
   final visual backbone/resolution/sampling-rate, single-match
   validation not yet extended to the full dataset.
9. Converted the experiment framework and publication positioning notes
   from planning documents into an execution-ready protocol referencing
   the now-confirmed benchmark construction method.

## Why it changed

The team needed to know, before committing further compute and writing
time, whether the multimodal pipeline was actually buildable under real
constraints (Colab-scale compute, the true distributed file layout,
real annotation schemas) rather than the planned/assumed version
described in Release 04. Running the pilot surfaced one real defect
(the naive frame-index assumption) that would have silently corrupted
any RGB-GSR fusion sample had it not been caught before scaling.

## What we were trying to learn

Whether the previously-planned feasibility protocol actually survives
contact with the real dataset, and whether a single representative
match is sufficient evidence to greenlight building B0-B5 without first
processing all ten matches.

## Current understanding

The multimodal pipeline is technically feasible on one representative
match. The scientific question — whether explicit game state adds
predictive value beyond a visual-only baseline — is unaffected by this
result and remains fully open. The GO decision authorizes moving from
feasibility engineering into baseline implementation; it does not
authorize skipping the ten-match extension or the independent teammate
replication that Release 04 already required before treating the
pipeline as structurally validated project-wide.

## Remaining uncertainty

The ten-match extension has not been run. The canonical dataset revision
is still not pinned. Rare-class handling, final visual backbone,
resolution, and sampling rate remain implementation decisions. No model
has been trained. Independent teammate replication of the pilot has not
yet been confirmed as matching (see
[[22_feasibility/FEASIBILITY_REPLICATION_STATUS]]).

## Next direction

Extend the validated single-match pipeline to all ten matches, pin the
canonical dataset revision, lock the rare-class policy, obtain the
independent teammate replication match, then begin B0 through B5
baseline implementation per
[[08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]].

## Historical continuity

This release is a **complete repository snapshot**, not a patch. Every
Release 01-04 note remains present unmodified except where this brief,
`CURRENT_STATE.md`, and the decision/session/version-history logs are
explicitly updated to reflect the pilot's execution. No historical
reasoning has been rewritten to look more certain in hindsight; the
Release 04 "not yet executed" status is preserved as history and
superseded only going forward from this release.

## Preservation notes

Release 05 keeps the old PCBAS history, candidate alternatives, PR-001
through PR-005, the superseded long proposal, all dataset anomalies and
withdrawn counts/folds, and the full Release 04 architecture and
proposal material. The one open naming inconsistency carried forward
unmodified from Release 04 — `README.md`'s architecture diagram reads
"B1-B5" while `08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX.md`
defines six variants **B0-B5** (B0 is a statistical floor, not a fusion
model) — is noted here rather than silently corrected in the old file;
new Release 05 material uses the authoritative B0-B5 naming from the
experiment matrix.

For the original v1-v5 lineage and Releases 01-04, see
[[18_version_history/VERSION_HISTORY]] and [[RELEASE_HISTORY]].

------------------------------------------------------------------------
