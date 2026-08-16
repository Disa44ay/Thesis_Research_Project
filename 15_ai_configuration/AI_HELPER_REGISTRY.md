---
type: ai-configuration
status: active
created: 2026-08-12
updated: 2026-08-12
tags: [ai, helpers, research]
related:
  - "[[15_ai_configuration/APPLIED_AI_RESEARCH_CONFIGURATION]]"
  - "[[15_ai_configuration/research_runs/PR 001 - Gemini Adversarial Literature Hunt]]"
  - "[[15_ai_configuration/research_runs/PR 002 - Claude Deep Verification]]"
  - "[[15_ai_configuration/research_runs/PR 003 - Gemini Targeted Verification]]"
  - "[[15_ai_configuration/research_runs/PR 004 - Perplexity Novelty Audit]]"
---
# AI Helper Registry

## Available helpers confirmed by the user
1. Gemini Pro, used as the primary broad literature and parallel-research worker.
2. Claude Free, treated as a scarce deep-reading resource. Prompts should be narrow and self-contained so one run can complete within quota.
3. Copilot, reserved mainly for repository analysis and implementation support.
4. Perplexity Free, used for independent source discovery and novelty audits.

## Optional tools discussed
Elicit Basic, Semantic Scholar, and Connected Papers may be used when they add discovery value. They are not currently required.

## Governance
No helper output becomes VERIFIED merely because the helper cites a paper. Load-bearing claims are checked against primary sources or official repositories.
