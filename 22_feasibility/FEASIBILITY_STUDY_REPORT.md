---
type: feasibility-report
status: executed
match: "117093"
report_date: 2026-08-20
source: Feasibility_Report_main.pdf; SoccerTrack_v2_Feasibility_01.ipynb
related:
  - "[[FEASIBILITY_REPLICATION_STATUS]]"
  - "[[BAA_BENCHMARK_CONSTRUCTION]]"
  - "[[BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]]"
  - "[[../20_system_architecture/FEASIBILITY_PILOT_PLAN]]"
  - "[[../14_decisions/2026-08-20 - Feasibility Pilot GO Decision]]"
---

# Feasibility Study Report — Executed

**Title:** Feasibility Study Report: Evaluating Game-State Fusion for
Short-Horizon Ball Action Anticipation in Football
**Date:** 20 August 2026
**Representative match:** 117093

## 1. Purpose and research direction

This feasibility study evaluated whether a small undergraduate thesis
team can construct and experimentally test a multimodal Ball Action
Anticipation (BAA) system using public SoccerTrack v2 data and limited
cloud compute. The research question tested for feasibility only (not
for outcome) is: does explicit player game-state information improve
short-horizon ball action anticipation compared with a visual-only
baseline? Input: a 30-second history of panoramic RGB video and
synchronized player game state. Target: one or more ball actions in the
following 5 seconds.

The feasibility objective was deliberately narrower than model
development. It did not attempt to prove fusion improves performance.
It tested: whether the required data exist; whether modalities can be
synchronized without leakage; whether valid anticipation samples can be
generated; whether visual and structured features can be produced under
Colab-level compute. A successful outcome means model comparison is
executable — improvement from fusion remains the open research
question.

## 2. Dataset and feasibility questions

SoccerTrack v2 was selected for full-match panoramic video, Ball Action
Spotting (BAS) annotations, and per-frame Game State Reconstruction
(GSR). The Google Drive release was used because it was accessible in
the working environment. Inventory identified ten matches with video,
GSR, BAS, and raw timing/calibration material: 117092, 117093, 118575,
118576, 118577, 118578, 128057, 128058, 132831, 132877. Match 117093 was
used as the representative deep-validation case.

Five feasibility questions structured the study:
1. Are BAS targets and GSR states available with compatible identities
   and timing?
2. Can 30-second observation / 5-second future windows be generated
   without crossing period boundaries or duplicating targets?
3. Can a complete player-state tensor be materialized without
   future-frame leakage?
4. Does the released panoramic video align with GSR at the same match
   timestamps?
5. Can synchronized visual features be extracted on free Colab-scale
   compute?

## 3. Validation procedure and results

### 3.1 Dataset inventory and annotation validation

The release inventory contained 22 video files, 20 GSR JSON files, and
11 BAS directory entries (including one non-data `.DS_Store` entry). All
ten match identifiers had the required BAS and GSR components. Missing
MOT files in the Drive mirror did not block the BAA route because
player identity, team, role, image boxes, and pitch coordinates are
already present in GSR.

For match 117093, the BAS file contained 2,252 actions involving 41
unique players. All twelve raw labels were present. Most frequent
classes: PASS (951), DRIVE (889), HIGH PASS (150); rarest: HEADER (3),
GOAL (5). This confirms severe class imbalance, so class handling is
treated as a later experimental decision rather than silently removing
rare classes at the feasibility stage.

### 3.2 GSR schema, identity coverage, and period timing

GSR JSON uses a COCO-like structure (`info`, `images`, `annotations`,
`categories`). Player annotations include `image_id`, `track_id`,
`player_id`, role, team, jersey number, image-space bounding boxes, and
pitch coordinates. Match 117093 contains 67,650 first-half GSR frames
and 70,475 second-half GSR frames at 25 FPS (durations 45:06 and 46:59).

BAS actor identities were checked against GSR: identity coverage was
**100%** for BAS actor IDs observed in both halves (23/23 first half,
27/27 second half). Raw period metadata provided exact `frameStart`,
`frameEnd`, `matchTimeStart`, `matchTimeEnd`; interval counts exactly
matched GSR sequence lengths at 40ms/frame, allowing a frame-exact
BAS-to-GSR mapping.

**Verified mapping rule:**
`local_ms = BAS_position - period_matchTimeStart`
`local_frame = round(local_ms / 40ms)`
`GSR image_id = first_image_id + local_frame`

Boundary events tested with this rule produced zero-frame differences.
**Second-half BAS times are absolute match times and must not be
treated as restarting from zero** — this corrects an earlier candidate
misreading from the Release 02/03 evidence trail.

### 3.3 Construction of the derived anticipation benchmark

30-second observation window, 5-second anticipation horizon, 5-second
stride. Windows allowed only when the full observation and future
interval remained inside the same half.

**Result for match 117093: 1,092 valid reference times** (535 first
half, 557 second half). Every observation had exactly 750 native GSR
frames.

Future windows were naturally multi-label: 715 windows (65.48%)
contained 2+ actions, 144 (13.19%) contained 1 action, 233 (21.34%)
contained none. The task cannot be simplified to positive
single-action windows only. A provisional 10-class compatibility view
excluding FREE KICK and GOAL was also generated for analysis (**not** a
final thesis class policy). 2,197 compatible target assignments were
produced, each covered action assigned exactly once, no duplicates. The
33 eligible actions not covered were all located too early in a half to
provide the required 30-second past context.

Full detail in [[BAA_BENCHMARK_CONSTRUCTION]].

### 3.4 Structured game-state materialization and leakage test

Sample `117093_H1_0006` materialized from 30.0s to 60.0s, future target
interval 60.0-65.0s. Future target: a CROSS occurring 4.56s after the
prediction reference time. Observation contained 750 GSR frames and 22
tactical entities per frame (20 field players, 2 goalkeepers) — no
missing frames, no missing coordinates, no duplicate player-frame
records, all 22 players present throughout.

Canonical structured representation: `positions_m` (750, 22, 2),
`positions_norm` (750, 22, 2), `presence_mask` (750, 22), role codes,
team codes. Latest represented GSR time: 59.96s. Future interval begins
60.00s. First target at 64.56s. **No future GSR frame leaked into the
observation.** A 5 FPS view retained 150 time steps as a lightweight
feasibility sampling rate — not yet claimed optimal.

### 3.5 RGB video validation and diagnosis of the frame-count mismatch

The first downloaded calibrated panorama was only 47 frames (1.88s) and
was rejected as an invalid full-half artifact. The canonical first-half
panorama for 117093 was then downloaded: ~3.35 GB, 4096x1080, 25 FPS,
2706.002s long. FFprobe reported **67,625 decoded video frames**, while
GSR contains **67,650 frames** — a 25-frame difference that initially
blocked a naive frame-index alignment assumption.

**A timestamp-level diagnostic resolved the discrepancy.** The RGB
stream begins at PTS 1.000s, ends at 2705.96s, has exactly 67,625
decoded frames, with consistent 0.04s frame intervals and no large
gaps. GSR represents the half from match time 0.00s. **The video is
internally continuous but its presentation timeline begins one second
later than match time.** Equal decoded-frame numbers therefore cannot
safely be used to synchronize the two modalities.

Full detail and the reusable synchronization principle in
[[BAS_GSR_RGB_SYNCHRONIZATION_FINDINGS]].

### 3.6 Direct RGB-GSR synchronization test

Tested at match time 30.0s. RGB frame nearest PTS 30.0s: decoded frame
725. GSR state for 30.0s: local frame 750 (image_id 3000751), with 22
tactical bounding boxes. Timestamp-aligned overlay was visually correct.
Control: same GSR boxes placed on RGB decoded frame 750 (true PTS
31.0s) — naive equal-index overlay showed visible displacement. Direct
empirical evidence that correct synchronization is timestamp-based, not
raw frame-index equality.

### 3.7 Common temporal grid and visual feature extraction

A common 5 FPS grid, 30.0-59.8s, yielded exactly 150 timestamps. RGB
indices advanced 5 decoded frames per step; GSR frames advanced 5
native frames per step. Maximum RGB timestamp matching error:
~1.07e-13s (floating-point noise). Both modalities share the same 150
observation times.

150 synchronized RGB frames, spatially reduced (panoramic aspect ratio
preserved), passed through a pretrained ResNet-18 feasibility probe.
Feature extraction succeeded on CPU: finite visual feature matrix,
shape **(150, 512)**. Structured branch at the same grid: (150, 22, 2)
position tensor. ResNet-18, 224px height, and 5 FPS are feasibility
probes only, not final architectural choices.

## 4. Consolidated feasibility evidence

| Feasibility item | Status | Evidence |
|---|---|---|
| Dataset availability | PASS | Ten matches contain the required video, BAS, GSR, and raw timing material |
| BAS target usability | PASS | 2,252 actions in match 117093; timing and actor IDs validated |
| GSR state usability | PASS | Per-frame player identity, team, role, boxes, pitch coordinates available |
| BAS-GSR synchronization | PASS | Exact period timing rule and actor identity coverage validated |
| 30s -> 5s benchmark | PASS | 1,092 valid windows; negatives and multi-action futures retained; no duplicate targets |
| Leakage control | PASS | Observation ends 59.96s, future begins 60.00s in the tested sample |
| RGB source usability | PASS | Full 4K, 25 FPS panoramic half-video successfully decoded |
| RGB-GSR alignment | PASS | Timestamp-aligned player-box overlay correct; naive equal-index control is misaligned |
| Common multimodal grid | PASS | 150 exact shared timestamps over 30s at provisional 5 FPS |
| Visual feature extraction | PASS | Pretrained ResNet-18 probe produced finite (150, 512) features on CPU |
| Fusion performance | NOT TESTED | This is the research experiment, not a feasibility question |

## 5. Go/No-Go decision

**Decision: GO, with strict scope control.**

The major execution risks that could have invalidated the thesis route
have been tested on a representative full-match case: data access,
annotation schemas, actor identity coverage, period timing,
anticipation-window construction, leakage control, structured-state
materialization, real video decoding, RGB-GSR synchronization, and
visual feature extraction. The multimodal pipeline can be built under
the available environment.

This GO decision does **not** claim multimodal fusion will outperform a
visual-only model. The remaining scientific uncertainty — whether
explicit player game-state information improves short-horizon
anticipation — is precisely the hypothesis to be tested. **The
representative-match validation must also be extended to all ten
matches during implementation; feasibility evidence from one match
should not be reported as full-dataset empirical validation.**

## 6. Experimental design implied by the feasibility study

The fair thesis comparison should use the same derived SoccerTrack
benchmark, the same match-level train/validation/test logic, the same
future targets, and the same visual preprocessing for all relevant
models. Minimum comparison: (A) visual-only, (B) game-state-only, (C)
visual + game-state fusion. If a relation-aware or graph model is
introduced, a flat game-state control must also be included so any
benefit from message passing can be separated from the benefit of
simply adding structured state.

Data splits must occur at the match level, never by randomly splitting
overlapping windows — 30-second windows with 5-second stride share
substantial temporal content and would otherwise leak near-duplicate
observations across partitions. Published visual BAA results from a
different dataset/domain are methodological references, not directly
comparable scores; the visual baseline and multimodal model should be
retrained or adapted on the same SoccerTrack-derived benchmark.

## 7. Remaining risks and scope boundaries

- Only ten matches are available; evaluation variance may be high.
  Match-level cross-validation or carefully justified match splits are
  important.
- Class imbalance is severe. Final rare-class policy, loss weighting,
  and whether to use the provisional 10-class compatibility view are
  not yet locked.
- The benchmark is derived from SoccerTrack BAS, not an official
  standardized BAA benchmark, and must be described transparently as a
  derived anticipation benchmark.
- Final RGB backbone, resolution, sampling rate, and
  frozen-vs-fine-tuned strategy are implementation decisions. The
  ResNet-18/5 FPS probe is not the final architecture.
- A positive fusion gain is not guaranteed. A null or negative result
  remains scientifically interpretable if the baseline, controls, and
  evaluation are rigorous.
- Whole-dataset preprocessing, production caching, substitution edge
  cases, and full training were intentionally left outside feasibility
  scope and belong to implementation.

## 8. Conclusion

The feasibility study demonstrates that the proposed multimodal Ball
Action Anticipation experiment is technically executable. On
representative match 117093, BAS actions and GSR player state were
synchronized, valid 30-second-to-5-second samples were constructed
without leakage or target duplication, a complete structured-state
sequence was materialized, the canonical panoramic video was decoded
and timestamp-aligned to GSR, and a synchronized visual feature
sequence was successfully extracted on CPU. The correct engineering
rule discovered during testing is to align RGB and GSR by
presentation/match timestamp rather than assuming identical raw frame
indices. With these risks resolved, the next phase is implementation of
fair visual-only, game-state-only, and fusion baselines rather than
additional feasibility engineering.

------------------------------------------------------------------------
