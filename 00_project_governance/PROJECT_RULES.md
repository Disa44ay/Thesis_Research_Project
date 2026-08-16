---
type: governance
status: active
tags: [rules, no-loss, project-history]
updated: 2026-08-10
---
# Project Rules

## Rule 1. This vault is topic-specific
Store the actual research journey here. Do not turn this vault into the generic reusable pipeline.

## Rule 2. Never lose knowledge
Do not delete old findings, rejected topics, failed experiments, superseded assumptions, or earlier decisions. Change their status and record why they changed.

## Rule 3. Preserve the full journey
The vault should be capable of reconstructing how the project moved from domain exploration to the final research question, implementation, publication attempt, and defense.

## Rule 4. Update through the current confirmed chat state
Important decisions, findings, corrections, and state changes discussed in chat must be written into durable notes during the working session. Chat history must never be the only copy of important project knowledge.

## Rule 5. Evidence states
Use `VERIFIED`, `SECONDARY`, `HYPOTHESIS`, `REJECTED`, `UNKNOWN`, and `SUPERSEDED` where useful.

## Rule 6. Never invent research evidence
Unverified paper metadata, dataset details, benchmark results, modalities, code links, novelty claims, or venue claims stay unverified until checked against original sources.

## Rule 8. Atomic graph reasoning
Important constraints, decisions, candidate topics, datasets, primary sources, rejections, and downgrades must have their own linked nodes when they materially affect the project. Long narrative notes remain preserved.

## Rule 9. Deferred-update instruction
During the 2026-08-10 session, the project owner explicitly requested that Markdown files not be modified during active discussion. Updates should be accumulated and written when the owner says to update or at the end of the session.

## Rule 10. Research compute is not deployment budget
Temporary paid research compute may be allowed, but final deployment must follow the project's current cost constraint. Never infer that willingness to pay for training implies willingness to pay recurring hosting or storage costs.

## Update 2026-08-12: snapshot and helper provenance
1. The two vaults remain separate. Reusable methodology belongs in Reusable Research OS. Topic-specific history belongs here.
2. External AI prompts and consequential outputs must be tracked as research-run nodes.
3. Corrections must be linked, not silently erased.
4. Historical vault versions must remain immutable and serially recoverable.
5. The authoritative dataset link supplied by the user must be preserved in the dataset node.
