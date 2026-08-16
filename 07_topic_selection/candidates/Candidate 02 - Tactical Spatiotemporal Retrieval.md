---
type: candidate-topic
status: hypothesis-top-tier
created: 2026-08-10
updated: 2026-08-10
tags: [candidate, retrieval, tactical, backend, multimodal]
depends_on:
  - "[[01_goals_constraints/constraints/Football Domain Scope]]"
  - "[[01_goals_constraints/constraints/Zero Cost Deployment]]"
  - "[[01_goals_constraints/constraints/Annotation Budget]]"
  - "[[03_datasets/datasets/SoccerTrack v2]]"
supported_by:
  - "[[04_literature/sources/SOURCE - SoccerRAG 2024]]"
  - "[[04_literature/sources/SOURCE - SoccerTrack v2 2025]]"
related:
  - "[[05_direction/concepts/Tactical Retrieval]]"
  - "[[07_topic_selection/rejections/Generic Football RAG]]"
---
# Candidate 02: Tactical Spatiotemporal Retrieval

## Working title
**Spatiotemporal Tactical Retrieval from Football Video Using Game State Reconstruction and Natural Language Queries**

## Candidate research question
Can explicit spatial and temporal game-state representations improve retrieval of tactical football situations from natural-language or structured queries compared with generic semantic or metadata retrieval?

## Why it survived the first sweep
1. SoccerRAG proves generic natural-language multimodal soccer retrieval already exists, forcing this candidate toward a narrower research problem.
2. SoccerRAG reports limitations involving complex queries and large data volumes and discusses future clip retrieval and deeper video understanding.
3. SoccerTrack v2 provides structured full-pitch state that could support spatial and temporal tactical queries.
4. The topic has unusually strong natural backend integration through indexing, query APIs, result ranking, lightweight metadata persistence, and a user-facing search system.
5. The team's 100 to 150 annotation budget could support a small expert query-relevance evaluation set instead of a new training dataset.

## Research contribution hypothesis
Create a retrieval representation or ranking method that combines tactical game-state structure with semantic query information and test it on difficult spatial-temporal football queries.

## Major unresolved risks
1. A retrieval contribution can easily collapse into system engineering without enough research novelty.
2. Tactical query ground truth may require careful annotation and inter-annotator agreement.
3. Existing sports retrieval literature beyond SoccerRAG must be searched deeply.

## Kill conditions
Reject if the only contribution is a vector database or RAG wrapper, if a reliable evaluation set cannot be built within 100 to 150 annotations, or if recent work already benchmarks equivalent tactical retrieval.
