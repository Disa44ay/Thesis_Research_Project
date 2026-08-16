---
type: ai-research-run
status: completed-corrected
created: 2026-08-14
updated: 2026-08-14
tags: [claude, pr-005, novelty-audit, benchmark-audit]
related:
  - "[[../../04_literature/RELATED_WORK_MATRIX]]"
  - "[[../../06_research_gaps/Gap - Multimodal Game State Fusion for BAA]]"
  - "[[../../08_experiments/BENCHMARK_PROTOCOL_LOCK]]"
  - "[[../../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]]"
---
# PR 005 - Claude Final Evidence Lock

## Purpose
Use the restored Claude Free quota for one adversarial pass over only four anchor sources: FAANTRA, SoccerNet 2026 BAA, Ochin et al. 2025, and SoccerTrack v2. The prompt explicitly prohibited broad discovery and asked for a claim audit, benchmark audit, contribution audit, hostile-review test, and final verdict.

## Claude verdict
**KEEP BUT NARROW.**

## High-value findings
1. The four anchor sources do not show explicit player-level metric geometry plus visual representations improving temporally localized prediction in an unobserved future interval.
2. Ochin is the most important architectural prior because video plus explicit game-state graph fusion already exists for action detection.
3. A flat-relations control is needed so any graph gain can be separated from simply supplying richer relational features.
4. Match-level cross-validation is safer than a single split with only ten matches.
5. Novelty should be framed as transfer of explicit game-state evidence from observed-action understanding to future anticipation, not as invention of video plus game-state fusion.

## Corrections after independent verification
1. Claude's concern that SoccerTrack v2 public availability was unconfirmed was stale. The current public repository and dataset distribution are available.
2. The suggestion to automatically exclude Header, Goal, and Free Kick from the only primary result was not adopted. Goal and Free Kick may be excluded for SN-BAA semantic compatibility, while full 12-class and rare-class reporting remain important.
3. Claude's four-source conclusion is evidence that the exact method is **not shown in those sources**, not proof of first-ever novelty across all literature.

## Resulting decisions
- Advance Candidate 01.
- Narrow novelty claim.
- Add flat-relations control.
- Use match-level grouped evaluation.
- Preserve negative-result value.

See [[../../19_verification/FULL_EVIDENCE_REVERIFICATION_2026-08-14]].
