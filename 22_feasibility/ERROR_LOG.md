---
type: error-log
status: active
updated: 2026-09-10
---

# Error Log

Per the operating instructions, failed approaches and caught errors are
preserved as research knowledge, not deleted once resolved.

## 2026-08-20 - Invalid short video artifact

**What happened:** the first downloaded "calibrated panorama" file for
match 117093 was only 47 frames (1.88 seconds) - clearly not a
full-half video.

**How it was caught:** basic frame-count sanity check before any
alignment work began.

**Resolution:** rejected the file and downloaded the canonical
first-half panorama instead (~3.35 GB, 2706.002s, matching the expected
full-half duration).

**Lesson:** always sanity-check a downloaded media file's basic
duration/frame-count before building any pipeline stage on top of it -
a corrupt or wrong-variant download can otherwise waste significant
downstream debugging time.

## 2026-08-20 - Naive frame-index RGB/GSR alignment (caught before use)

**What happened:** the natural first implementation assumption -
"GSR frame N corresponds to RGB decoded frame N," since both are
nominally 25 FPS - is wrong by a fixed one-second (25-frame) offset for
match 117093's first half. This was not an assumption ever written into
a production pipeline; it was tested and rejected during feasibility,
specifically because it was worth checking before scaling.

**How it was caught:** a controlled overlay comparison - GSR player
boxes for match time 30.0s drawn on (a) the timestamp-correct RGB frame
and (b) the naive equal-index RGB frame - visibly diverged for (b).
FFprobe frame-count comparison (67,625 vs. 67,650) was the first hint;
the PTS-origin diagnostic confirmed the mechanism.

**Resolution:** switched to timestamp-based alignment. See
[[BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]] and the decision record
[[../14_decisions/2026-08-20 - Timestamp Based RGB GSR Alignment Rule]].

**Severity if uncaught:** would have caused silent, systematic
one-second temporal misalignment between visual and structured inputs
across the entire multimodal dataset - the kind of error that does not
show up in shape or count checks and would likely have degraded or
invalidated any fusion-model comparison without an obvious cause.

**Lesson:** matching nominal frame rates and near-matching frame counts
are not sufficient evidence of aligned clocks. A direct visual/positional
overlay test against ground truth is the only test that actually caught
this.

## Open items not yet classified as errors or resolved

- Whether the one-second offset is consistent across all ten matches
  and both halves of each match is UNKNOWN - it has only been confirmed
  for match 117093's first half. Treat this as an open verification
  item, not a resolved universal constant, until checked.

------------------------------------------------------------------------
