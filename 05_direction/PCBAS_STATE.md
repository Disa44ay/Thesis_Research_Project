---
type: research-direction
status: migrated
tags: [football, SoccerNet, PCBAS]
source: PCBAS_STATE.md
updated: 2026-08-10
---
# Current Direction: Player-Centric Ball Action Spotting

## Task
Player-Centric Ball Action Spotting (PCBAS) aims to determine:
- when a ball-related action occurs,
- what the action is,
- which player performed it.

This is more specific than standard 17-class action spotting.

## Why it is attractive
- Strong alignment with football interest.
- Modern research direction.
- Strong industry relevance.
- Existing benchmark/baseline ecosystem.
- Can leverage structured/pre-extracted data to reduce compute.
- Allows backend + AI integration.
- Can demonstrate temporal modeling, tracking, spatial context, and multimodal fusion.

## Current perceived risks
- Tracking dependency.
- Player-ID switches.
- Occlusion.
- Broadcast camera cuts/replays.
- Visual ambiguity.
- Upstream feature dependence.
- Newness of some 2026 materials means metadata must be carefully verified.

## Candidate tasks considered

### A. Player-Centric Ball Action Spotting
Best current fit.

### B. Ball Action Anticipation
Predict future actions from a preceding temporal window.

Pros:
- modern,
- temporal modeling,
- potentially strong research opportunity.

Cons:
- difficult evaluation,
- inherently uncertain predictions,
- practical usefulness can be harder to demonstrate.

### C. Standard Action Spotting
Pros:
- very easy compute-wise with pre-extracted features.

Cons:
- mature/saturated,
- weaker novelty opportunity.

### D. Soccer Video VQA
Pros:
- multimodal,
- strong AI learning value,
- strong portfolio value.

Cons:
- VLM compute can become difficult on free Colab,
- risk of scope explosion.

### E. Camera Calibration / Pitch Localization
Pros:
- strong industry relevance.

Cons:
- geometry-heavy,
- less aligned with backend + AI transition.

## Current recommendation
PCBAS is the leading candidate, but it is **not yet locked**.

The topic must only be locked after validating:
1. exact dataset access,
2. exact benchmark,
3. exact baselines,
4. recent literature,
5. genuine gap,
6. one-month feasibility,
7. multimodal feasibility,
8. experimental reproducibility.

## Status update 2026-08-10
PCBAS is no longer treated as the sole strongest direction.

New evidence shows that FOOTPASS and 2026 PCBAS extensions already use tactical or graph-based context with per-player visual information. Therefore, the broad candidate gap "add tactical context to PCBAS" is downgraded. See [[07_topic_selection/downgraded/PCBAS Generic Tactical Context]].

PCBAS remains in the research space only if a narrower weakness is independently validated, such as identity robustness, missing detections, rare-class behavior, temporal association, or another specific measurable failure.
