---
type: literature
status: migrated
tags: [papers, literature-review, needs-verification]
source: LITERATURE_FINDINGS.md
updated: 2026-08-10
---
# Literature Findings

## Literature workflow decided

### Phase 1 — Research landscape
Use Gemini Pro to identify research domains, not thesis topics.

Expected output:
- 30–50 domains,
- trends,
- publication activity,
- datasets,
- industry relevance,
- compute feasibility.

### Phase 2 — Dataset discovery
Use Gemini Pro to investigate datasets for the top domains.

Fields:
- name,
- official/download link,
- size,
- modalities,
- classes,
- labels,
- annotation quality,
- benchmark papers,
- code,
- license,
- strengths,
- weaknesses.

### Phase 3 — Literature collection
Use Gemini Pro to locate major papers from 2021 onward, prioritizing:
- CVPR
- ICCV
- ECCV
- NeurIPS
- AAAI
- ACM
- IEEE
- Springer
- Elsevier

Fields:
- title,
- year,
- venue,
- dataset,
- model,
- code,
- citations,
- problem,
- future work.

### Phase 4 — Literature analysis
Use Claude.

Claude should read the actual papers/PDFs and produce:
- problem,
- dataset,
- model,
- methodology,
- loss,
- metrics,
- strengths,
- weaknesses,
- limitations,
- future work,
- code,
- compute,
- novelty,
- publication quality.

### Phase 5 — Research-gap validation
Use Claude to identify gaps only when supported by multiple papers or explicit future-work statements.

### Phase 6 — Topic selection
Return to GPT after literature and gap validation.

GPT should generate candidate topics and score them.

## Important correction
A prior AI response claimed a large number of 2024–2026 PCBAS papers and some challenge results. Those claims have **not yet been independently validated** in this knowledge base.

Do not treat those claims as established facts.

## Core papers proposed for initial reading

1. SoccerNet-v2: A Dataset and Benchmarks for Holistic Understanding of Broadcast Soccer Videos
   - Silvio Giancola et al.
   - 2021
   - CVPR Workshops
   - arXiv: https://arxiv.org/abs/2104.09333

2. SoccerNet-Tracking: Multiple Object Tracking Dataset and Benchmark in Soccer Videos
   - Anthony Cioppa et al.
   - 2022
   - CVPR
   - arXiv: https://arxiv.org/abs/2204.06918

3. A Context-Aware Loss Function for Action Spotting in Soccer Videos
   - Anthony Cioppa et al.
   - 2020
   - CVPR
   - arXiv: https://arxiv.org/abs/2004.09546

4. E2E-Spot: End-to-End Action Spotting in Broadcast Soccer Videos
   - João Soares et al.
   - 2022
   - WACV
   - arXiv: https://arxiv.org/abs/2210.02409

5. SoccerNet 2023 Challenges Results
   - Anthony Cioppa et al.
   - 2023
   - ACM MMSports
   - arXiv: https://arxiv.org/abs/2309.06006

6. FOOTPASS: Player-Centric Ball Action Spotting
   - Listed as a recent SoccerNet PCBAS baseline.
   - Exact bibliographic metadata must be verified before citation.

7. SoccerNet 2026 Player-Centric Ball Action Spotting: Per-Player Attention with Agreement-Based Ensembling
   - Faisal Altawijri, Ismail Mathkour
   - 2026
   - arXiv: https://arxiv.org/abs/2606.28389
   - Metadata should be verified.

8. T-DEED: Temporal Deformable Encoder-Decoder for Action Spotting in Sports Videos
   - Arthur Piqueres et al.
   - 2024
   - WACV
   - Code availability should be verified.

9. Temporally-Aware Feature Pooling for Action Spotting / NetVLAD++
   - 2022
   - CVPR Workshop ecosystem
   - Exact bibliographic metadata should be verified.

10. ByteTrack: Multi-Object Tracking by Associating Every Detection Box
    - Yifu Zhang et al.
    - 2022
    - ECCV
    - arXiv: https://arxiv.org/abs/2110.06864

## Supporting concepts
- X3D for efficient video representation.
- RoIAlign for player-level feature extraction.
- temporal Transformers.
- graph neural networks for spatial/player relationships.
- multi-object tracking and re-identification.

## Verified literature update 2026-08-10

### [[04_literature/sources/SOURCE - SoccerNet GSR 2024]]
Game State Reconstruction was formalized for football broadcast video in 2024 with a public benchmark, metric, and baseline. It provides a strong enabling representation for tactical analysis.

### [[04_literature/sources/SOURCE - FAANTRA 2025]]
Football action anticipation is an established recent task using five-second and ten-second future windows. This weakens the need for an arbitrary exact thirty-second forecasting target and provides a possible benchmark path.

### [[04_literature/sources/SOURCE - SoccerTrack v2 2025]]
SoccerTrack v2 provides public panoramic full-pitch video, game-state annotations, and ball-action labels, creating a possible bridge between tactical state and action understanding.

### [[04_literature/sources/SOURCE - SoccerRAG 2024]]
Generic natural-language multimodal soccer retrieval already exists. Retrieval research must therefore become more specific than "football RAG."

### [[04_literature/sources/SOURCE - FOOTPASS 2025]] and [[04_literature/sources/SOURCE - PCBAS Extensions 2026]]
Recent PCBAS work already incorporates tactical or graph context. The earlier broad tactical-prior gap is no longer safe as a novelty claim.

### Evidence discipline
These verified sources update the candidate landscape but do not yet prove novelty for any of the three new candidates. Further 2023 to 2026 literature falsification is required.
