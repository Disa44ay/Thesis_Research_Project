---
type: decision
status: active
created: 2026-08-12
updated: 2026-08-12
tags: [decision, ai, orchestration]
caused_by:
  - "[[15_ai_configuration/AI_HELPER_REGISTRY]]"
results_in:
  - "[[15_ai_configuration/research_runs/PR 001 - Gemini Adversarial Literature Hunt]]"
  - "[[15_ai_configuration/research_runs/PR 002 - Claude Deep Verification]]"
  - "[[15_ai_configuration/research_runs/PR 003 - Gemini Targeted Verification]]"
  - "[[15_ai_configuration/research_runs/PR 004 - Perplexity Novelty Audit]]"
---
# 2026-08-12: External AI Helper Strategy

Gemini Pro is the broad parallel research worker. Claude Free is reserved for narrow deep verification because quota is scarce. Perplexity Free is an independent novelty and citation checker. Copilot is reserved mainly for implementation and repository work.

All helper findings require primary-source verification before they become thesis evidence.
