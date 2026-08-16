---
type: applied-configuration
status: active
tags: [ai-workflow, project-configuration]
updated: 2026-08-10
---
# Applied AI Research Configuration

This note records how the reusable research system is instantiated for this thesis. Generic pipeline instructions belong in the separate Reusable Research OS vault.

## Team and execution profile used in the original prompts
CSE undergraduate team of three. Strong backend and software engineering background. Transitioning toward AI, ML, computer vision, multimodal AI, and data engineering. Comfortable reading deep-learning papers. No local GPU. Use free or university-access Colab and Kaggle resources. Public datasets only. End-to-end deployable system desired. Approximately 60 percent coding and 40 percent research. Maximum practical execution target around one month.

## Original priority domains used during landscape search
1. Football Video Understanding.
2. Satellite Vision or Remote Sensing.
3. General Computer Vision, including Document AI.

## Original AI role assignment
Gemini Pro for broad discovery, datasets, papers, links, and initial tables.

Claude for deep paper reading, literature matrices, limitation extraction, gap validation, synthesis, scientific writing, and critique.

GPT for verified synthesis, topic scoring, architecture, experiments, implementation planning, and reviewer-style critique.

GitHub Copilot for coding after architecture and research contribution are fixed.

These assignments are workflow history. They are not evidence about the scientific topic and should be adjusted when tooling changes, while preserving the decision history.

## 2026-08-10 operating update
During active topic discovery, Markdown synchronization may be deferred when explicitly requested by the project owner. AI systems should maintain the distinction between discussion-time hypotheses and durable vault state.

For the current topic-search stage, every candidate should be actively falsified against 2023 to 2026 primary literature before being promoted.

The active search must respect the atomic graph nodes under `01_goals_constraints/constraints`, `04_literature/sources`, `07_topic_selection`, and `14_decisions`.
