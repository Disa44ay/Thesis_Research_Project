Session Log

2026-08-09. Knowledge-base architecture clarified

The project owner decided to maintain two separate Obsidian knowledge
vaults.

The reusable vault contains the generic research system and AI pipeline.

This project vault contains only the active research journey, from topic
finding and literature review to publishing and defending the thesis in
front of the panel.

Non-negotiable rule: do not lose existing knowledge. The vault should
remain updated through the latest confirmed chat state so the research
history can survive loss of account access.

During this migration, topic-specific material was kept here and generic
workflow material was moved into the reusable system vault. Mixed
original notes were split by function, not deleted.

2026-08-10. Football candidate-title discovery session

Session objective

Narrow the active thesis search toward a defensible football research
topic and candidate title.

Confirmed project preferences and constraints

1.  Stay inside football.
2.  Prefer Computer Vision because the instructor specializes in CV.
3.  Multimodality is preferred but not mandatory and must be meaningful.
4.  Moderate paid Colab research compute may be considered.
5.  Large-scale raw-video training remains out of scope.
6.  Final deployment must have zero recurring cost.
7.  Avoid permanent server-side raw-video storage where possible.
8.  Directly downloadable public datasets are preferred, with
    request-based free academic access acceptable only when timing risk
    is manageable.
9.  Manual annotation is capped around 100 to 150 samples.
10. Plan execution around two continuously active team members.
11. Candidate titles are needed within two days, and the instructor
    permits multiple candidates.

User-interest branches

Strong interest was expressed in tactical analysis, future-gameplay
prediction, and intelligent search or retrieval inside football video.
The search remains open to other football topics that better satisfy the
constraints.

Research findings verified during the session

1.  SoccerNet Game State Reconstruction provides a short-sequence
    football CV benchmark with rich player and pitch state.
2.  FAANTRA establishes short-horizon football ball-action anticipation
    using five-second and ten-second windows.
3.  SoccerTrack v2 provides public full-pitch panoramic matches with
    game-state and ball-action labels.
4.  SoccerRAG already covers generic multimodal natural-language soccer
    information retrieval.
5.  FOOTPASS and 2026 PCBAS work already use tactical or graph-based
    player context, weakening the earlier generic tactical-prior gap.

Current candidate families

1.  [[07_topic_selection/candidates/Candidate 01 - Game State Aware
    Action Anticipation]]
2.  [[07_topic_selection/candidates/Candidate 02 - Tactical
    Spatiotemporal Retrieval]]
3.  [[07_topic_selection/candidates/Candidate 03 - Tactical State
    Forecasting]]

Preserved rejected or downgraded branches

1.  [[07_topic_selection/rejections/Generic Football RAG]]
2.  [[07_topic_selection/rejections/Exact 30 Second Future Prediction]]
3.  [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]]

Next session

Attack Candidate 01 first. Search recent literature for equivalent
game-state-aware anticipation, verify dataset alignment and baseline
reproducibility, then either kill, narrow, or promote it. After that,
perform the same process for Candidates 02 and 03 and prepare 2 to 3
instructor-facing titles.

Session 2026-08-12, Candidate 01 validation sprint

External AI research

1.  [[15_ai_configuration/research_runs/PR 001 - Gemini Adversarial
    Literature Hunt]] completed with metadata and reasoning corrections.
2.  [[15_ai_configuration/research_runs/PR 002 - Claude Deep
    Verification]] partially completed before Claude Free quota
    exhaustion.
3.  [[15_ai_configuration/research_runs/PR 003 - Gemini Targeted
    Verification]] completed with several factual corrections.
4.  [[15_ai_configuration/research_runs/PR 004 - Perplexity Novelty
    Audit]] completed in free Search mode and required a
    novelty-reasoning correction.

Dataset work

The user supplied the official SoccerTrack v2 Google Drive folder and
uploaded all 10 BAS JSON files. Direct audit produced 23,663 total
actions and exposed severe long-tail imbalance plus a small timeline
anomaly cluster.

Candidate evolution

The original game-state anticipation idea was narrowed to
[[07_topic_selection/candidates/Candidate 01B - Relation Aware
Multimodal BAA]]. Generic tactical forecasting was downgraded.

Compute decision

The project remains feasible only with one-time feature extraction and
compact structured preprocessing. End-to-end repeated 4K video training
is rejected.

Immediate next work

Related works, limitations, novelty boundary, benchmark design, title
lock, full proposal, hostile review.

2026-08-14 - Scientific lock

Claude PR-005 returned KEEP BUT NARROW. Independent re-verification
confirmed Candidate 01 but corrected context-window wording, mAP
tolerance interpretation, method novelty, SoccerTrack release
provenance, provisional BAS cleaning, and fold assignment.
Architecture/experiment ladder B0-B5 was locked.

2026-08-14 - Proposal and system architecture

Phase 5 selected the instructor-facing title. The research system was
extended from raw SoccerTrack v2 data through canonical revision
pinning, GSR streaming, visual feature extraction, alignment, compact
windowed training, grouped evaluation, a 100-unit soft budget, and a
10-minute feasibility pilot. A detailed academic proposal was
commissioned in LaTeX/PDF.

2026-08-14 to 2026-08-16 - Proposal simplification and feasibility handoff

1.  The first long-form proposal was judged too long and disorganized
    for the intended instructor-facing proposal.
2.  A concise verified proposal was produced instead.
3.  A separate citation/source audit was created to preserve evidence
    depth without cluttering the proposal.
4.  A short teammate brief was produced.
5.  The feasibility study was expanded into an operational step-by-step
    guide and self-contained context handoff.
6.  The common pilot was set to match 117093, approximately 10 minutes,
    unless the pinned canonical revision reveals a new issue.
7.  Independent teammate replication was added as a structural
    validation rule.
8.  No feasibility experiment or scientific model result had been
    executed by the end of this state.

2026-08-16 - Feasibility handoff and public-release reconstruction

1.  Audited historical v1-v5 and preserved the original lineage.
2.  Grouped public Git history into four synchronized semantic releases.
3.  Added release-management documentation without rewriting historical
    research findings.
4.  Release 04 synchronized verified post-v5 proposal and feasibility
    artifacts.

2026-08-20 - Feasibility pilot executed

1.  Ran the SoccerTrack v2 feasibility pipeline on representative match
    117093 in Google Colab.
2.  Verified dataset inventory (10 matches), BAS schema (2,252 events,
    41 players), and GSR schema (67,650 / 70,475 frames, 100% identity
    coverage).
3.  Verified the BAS-to-GSR timestamp mapping rule with zero boundary
    error.
4.  Constructed the first real 30s/5s benchmark: 1,092 windows, no
    duplicate targets, leakage-free structured sample.
5.  Diagnosed and resolved a one-second RGB/GSR presentation-timestamp
    offset that would otherwise have silently misaligned the modalities.
6.  Extracted synchronized visual features (ResNet-18 probe, CPU) at a
    common 5 FPS grid.
7.  Issued a formal decision: GO, with strict scope control. Did not
    claim fusion improves anticipation; RQ1/RQ2 remain open.
8.  Did not yet extend the pipeline to the other nine matches and did
    not yet arrange independent teammate replication.

2026-09-10 - Release 05 mapping and packaging

1.  Mapped all available Release 01-04 material and the existing thin
    Release 05A/05B draft packages against the primary feasibility
    evidence (notebook + report).
2.  Traced every headline feasibility number to a live computation cell
    in the notebook; confirmed internal arithmetic consistency
    (535+557=1092; 233+144+715=1092).
3.  Flagged a data-integrity anomaly in the V01 context files (embedded
    version brief duplicated from Release 04) for human confirmation,
    without silently correcting it.
4.  Resolved the B0-B5 vs. B1-B5 naming question by consulting
    [[08_experiments/PHASE_4_MODEL_AND_EXPERIMENT_MATRIX]]: B0-B5 is
    authoritative (six variants; B0 is a statistical floor).
5.  Built this Release 05 complete-repository snapshot, carrying
    forward all Release 04 content unmodified except for the specific
    files listed in [[17_migration/MIGRATION_MANIFEST]].

2026-09-10 - Verification pass against local repository

1.  Confirmed via local Git history that the V01 context-file anomaly
    (embedded Release 04 version brief mislabeled as Release 01) was
    caused by a live Git checkout sitting at HEAD rather than the
    intended per-release commit. Recovered the true Release 01
    `VERSION_BRIEF.md` content via `git show`. See
    [[../17_migration/V01_CONTEXT_RECONSTRUCTION_NOTE]].
2.  Confirmed no ten-match extension, no pinned dataset revision, no
    independent teammate replication, and no RGB/GSR offset
    verification beyond match 117093 first half exist anywhere locally
    - all four remain open exactly as previously documented.
3.  Retrieved the full, sourced detail behind match 132831's previously
    vague "documented correction issue": two swapped calibration
    keypoints (upstream GitHub `data_corrections`), ~1260.95px shipped
    RMS error vs. ~18.07px corrected, GSR not yet regenerated. See
    [[../22_feasibility/MATCH_132831_CALIBRATION_DEFECT]]. Usable
    match count for the extension is now stated as 8, not 9.
4.  Discovered that the `RELATED_WORK_MATRIX.md` wikilink garbling
    flagged in the Release 05 mapping report was mis-diagnosed as a
    pre-existing Release 04 defect; a local Git diff shows it was
    actually introduced during this rebuild's own text extraction. Fix
    is pending the clean source text. See
    [[../17_migration/RELATED_WORK_MATRIX_FIX_PENDING]].
5.  Confirmed B0-B5 (per `PHASE_4_MODEL_AND_EXPERIMENT_MATRIX.md`)
    remains the sole model-matrix definition anywhere in the local
    repository.
6.  Confirmed the Reusable Research OS repository does have a
    `.gitignore`; it was only omitted from the Release 04 file-list
    enumeration, not actually missing. Added it to this release for
    consistency.

------------------------------------------------------------------------

# Session Log — Release 06 Addition

## 2026-09-14 — Gate protocol and pipeline architecture session

Established the Gate H / Gate E extension protocol
(`claude/PROTOCOL_gate_h_and_multi_match_offset.md`) and decided the
four-notebook pipeline split with a shared `common.py` module.

## 2026-09-15 — Gate H execution

Ran `claude/gate_h_compute_feasibility_probe.py`. Measured ~5.8
min/match, ~0.73 compute units/match, GPU at ~0.34% utilization. Fixed
a per-window tensorization bug found during measurement. Gate H
resolved: CPU-only feasible.

## 2026-09-16/17 — Gate E extension execution

Ran `claude/gate_e_multi_match_offset_check.py` across all 10 matches /
20 halves. Found the Release-05 1-second offset in 14/20 halves,
absent in 6/20. Found a new tail-loss defect (~10s missing video) in
10/20 halves. One half left unresolved by the check.

## 2026-09-22 — Release 06 packaging session

Built the Release 06 public package for both the Reusable Research OS
and this project, scoped to everything through the pre-implementation
gate-extension and architecture decisions above, explicitly excluding
N1's execution and all of N2-N5.

**Scope decision (user-confirmed):** stop at the structure-update phase
that preceded N1; N1 execution and later notebooks are reserved for a
future release.
