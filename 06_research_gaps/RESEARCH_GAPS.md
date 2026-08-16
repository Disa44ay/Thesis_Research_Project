---
type: research-gaps
status: migrated
tags: [research-gap, hypotheses, needs-verification]
source: RESEARCH_GAPS.md
updated: 2026-08-10
---
# Candidate Research Gaps

## Important status
These are **candidate gaps generated during exploration**.

They are NOT yet proven research gaps.

Before thesis approval, each must be supported by original papers and preferably multiple independent sources.

## Gap A — Player ID / tracking-drop recovery

### Problem
PCBAS depends on tracking/player identity. During occlusion or crowded situations, player IDs may be lost or switched.

### Proposed direction
Use contextual information to recover/repair player identity after tracking failures.

Possible inputs:
- tracking history,
- player position,
- temporal context,
- action logits,
- team information,
- spatial relationships.

### Why attractive
- Can operate on structured data.
- Avoids retraining huge visual backbones.
- Strong backend engineering opportunity.
- Can be tested on Colab.
- Naturally connects tracking and action spotting.

### Main reviewer risk
If the experiment uses ground-truth tracking too heavily, reviewers may question real-world robustness.

Therefore evaluate:
- clean tracking,
- artificially corrupted tracking,
- realistic ID-drop scenarios,
- repaired vs unrepaired action assignment.

## Gap B — Tactical priors

### Problem
Player/context information may be represented as flat features rather than explicit tactical constraints.

### Possible direction
Inject soccer-specific context into temporal modeling.

Potential priors:
- team identity,
- player role,
- spatial relationships,
- ball proximity,
- field position,
- temporal continuity.

### Risk
Do not claim that "no one uses tactical priors" unless the literature proves it.

## Gap C — Single-backbone lightweight architecture

### Problem
Heavy pipeline:
tracking → visual feature extraction → temporal model.

### Status
High risk and currently rejected for this team.

Reason:
- end-to-end training can exceed free-tier compute,
- one-month timeline is too short,
- would shift focus away from system/research validation.

## Gap D — Audio-visual continuity

### Problem
Broadcast cuts/replays can disrupt visual player tracking while audio may remain informative.

### Possible direction
Use audio/crowd/whistle information to maintain temporal evidence.

### Status
Interesting but secondary.

Risks:
- exact audio availability,
- alignment complexity,
- scope expansion,
- multimodal preprocessing.

## Recommended gap priority

1. Gap A — tracking/player-ID recovery
2. Gap B — tactical-context integration
3. Gap D — audio-visual continuity
4. Gap C — reject for current constraints

## Validation rule
A gap becomes "validated" only if:
- multiple papers expose the limitation, OR
- a recent paper explicitly identifies it as future work, AND
- the dataset permits testing it, AND
- the proposed intervention is distinguishable from existing methods.

## Gap status update 2026-08-10

### Gap B tactical priors
**Status changed from candidate priority to DOWNGRADED AS BROAD CLAIM.**

Reason: verified FOOTPASS and 2026 PCBAS work already incorporate tactical or graph-based player context. See [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]].

This does not prove every tactical-context idea is exhausted. It means any surviving PCBAS tactical contribution must identify a narrower unresolved mechanism or failure mode.

### New candidate research questions
The active candidate-gap search has expanded beyond PCBAS into:
1. whether game-state context improves short-horizon action anticipation,
2. whether explicit spatiotemporal state improves tactical retrieval,
3. whether player trajectories can support objective short-term tactical-state forecasting.

These remain hypotheses and are represented in the candidate nodes under [[07_topic_selection/TOPIC_LOCK_STATUS]].

Historical rejected or high-risk branch: [[06_research_gaps/Candidate Gap C - Shared Backbone]].
