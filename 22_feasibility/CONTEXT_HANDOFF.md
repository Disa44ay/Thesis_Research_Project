# Context Handoff: Football Ball Action Anticipation Thesis

**Purpose of this file:** Give any teammate or AI model enough verified context to understand the thesis, judge the feasibility study, and continue the work without reading the full research history.

**Current status:** Topic, research gap, benchmark direction, lightweight architecture, and feasibility-study design are defined. The next task is a small end-to-end feasibility pilot before spending the planned paid Colab budget.

**Verification date:** 2026-08-15

---

## 1. Thesis in one paragraph

We want to predict **ball-related football actions before they happen**. Given recent football context, the system should predict all ball actions that occur in the next **5 seconds**, with an action class, approximate future timestamp, and confidence. Existing football Ball Action Anticipation (BAA) work already predicts future actions mainly from video. Other football research has shown that explicit player game state, such as pitch coordinates, velocity, team information, and player relations, can help action detection when the action is already visible. Our thesis asks whether this explicit game state also provides useful information when the target action lies in an **unobserved future interval**.

### Current recommended title

**Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football**

### Core research questions

1. **RQ1:** Does explicit player-level game-state information improve short-horizon Ball Action Anticipation compared with visual-only anticipation?
2. **RQ2:** If game state helps, does explicit player-relation modeling add value beyond simple or flat game-state fusion when both methods receive the same underlying information?

---

## 2. What is different from prior work

### What already exists

1. **FAANTRA / SoccerNet BAA:** Future football Ball Action Anticipation already exists. Models predict future action class and time from observed video.
2. **SoccerNet 2026 BAA:** The official 2026 BAA task uses a 30-second observation window and predicts actions in the following 5 seconds over 10 classes. The five reviewed BAA technical reports are dominated by visual models and one VLM-derived tactical-context method.
3. **Ochin et al. 2025:** Explicit player game state plus visual information and graph reasoning already exists for football **spatio-temporal action detection**.
4. **Beyond Pixels 2025:** Longer-context game-state reasoning also exists for denoising and improving detected soccer actions.

### Our defensible gap

The reviewed literature does **not establish whether synchronized explicit player-level metric game state improves temporally localized prediction of ball actions that occur in an unobserved future interval**.

### Claims we must NOT make

- We are the first football action-anticipation model.
- We are the first football video plus game-state model.
- We are the first football GNN.
- We are the first future-event prediction system in football.
- We are state of the art on the SoccerNet leaderboard.
- Results from SoccerTrack v2 automatically generalize to professional broadcast football.

The scientific contribution is the **controlled empirical question**, not merely using a GNN.

---

## 3. Dataset: SoccerTrack v2

### Why it fits the thesis

SoccerTrack v2 provides the three synchronized resources we need:

1. **Panoramic 4K video**
2. **GSR (Game State Reconstruction)** with player pitch state
3. **BAS (Ball Action Spotting)** event annotations

The dataset contains 10 full-length university-level amateur matches, approximately 900 minutes in total, with 12 BAS classes.

### Canonical and supporting links

- Project page: https://atomscott.github.io/SoccerTrack-v2/
- GitHub repository: https://github.com/AtomScott/SoccerTrack-v2
- Canonical Hugging Face dataset: https://huggingface.co/datasets/atomscott/soccertrack-v2
- User-confirmed Google Drive mirror: https://drive.google.com/drive/folders/1N2Qx2qkFgRtpbHitl2Vh6sLVYGgqkWwn
- SoccerTrack v2 paper: https://arxiv.org/abs/2508.01802
- Current GSR format notes: https://github.com/AtomScott/SoccerTrack-v2/blob/main/docs/format-gsr.md
- Current BAS format notes: https://github.com/AtomScott/SoccerTrack-v2/blob/main/docs/format-bas.md
- Data corrections: https://github.com/AtomScott/SoccerTrack-v2/tree/main/data_corrections

### Important release rules

1. **Use Hugging Face as canonical.** The project page explicitly says mirrors may lag.
2. **Pin the exact dataset/repository revision** and record file hashes for experiments.
3. The current GSR developer documentation warns that the released files do not match the older simplified schema. Use the shipped structure or the repository loader, not assumptions from old examples.
4. Raw GSR is 25 fps.
5. Current docs say `track_id` is guaranteed within a half, not necessarily across halves. Use `player_id` where available for continuity across halves.
6. BAS-to-GSR second-half alignment has a documented timestamp caveat. Prefer the repository helper such as `Event.t_ms_in_half` instead of manually assuming `position` is half-relative.
7. Match **132831** has a documented calibration problem. Its distributed GSR labels were generated through the faulty calibration and the current correction notes say regeneration is still outstanding. Do not use 132831 in the pilot. Quarantine it for the full benchmark until a corrected GSR revision is confirmed.

### User-provided BAS snapshot findings

A Google Drive BAS snapshot was inspected earlier and contained 23,663 events. These counts are useful historical observations but must **not** be treated as canonical current-release statistics until the Hugging Face revision is checked. The older Drive schema also differed from current documentation. Do not reuse the earlier provisional "21,438 clean events" estimate. It was withdrawn.

---

## 4. BAA task definition we are targeting

### Community reference

SoccerNet 2026 BAA:

- Observation: 30 seconds of video available
- Future interval: 5 seconds
- Output: future ball-action class and temporal location
- Classes: 10
- Metrics: mAP at temporal tolerances 1, 2, 3, 4, 5, and infinity, summarized by mAPavg

For our initial feasibility pilot, we intentionally use a smaller **5-second past -> 5-second future** setup because the objective is pipeline validation, not final scientific performance.

### Full thesis output

A prediction should eventually look conceptually like:

```text
+0.8 s -> PASS  (confidence 0.82)
+2.6 s -> DRIVE (confidence 0.65)
+4.3 s -> CROSS (confidence 0.58)
```

Multiple actions may occur in a future window, so final modeling is a multi-event set-prediction problem rather than one-label classification.

---

## 5. Planned full research comparison

The thesis should compare controlled models rather than one complicated architecture.

1. **B1 Visual-only:** frozen visual embeddings -> temporal encoder -> future-event decoder.
2. **B2 Game-state-only:** player state -> temporal encoder -> future-event decoder.
3. **B3 Simple fusion:** visual context + flat/pooled game state.
4. **B4 Flat-relations:** same explicit pairwise relation features as the graph model but aggregated without graph message passing.
5. **B5 Relation-aware fusion:** visual context + relation-aware player graph + temporal state encoder.

The critical interpretations are:

- B3 > B1 supports the claim that game state adds predictive value.
- B4 > B3 supports the value of explicit relation features.
- B5 > B4 supports the value of graph/message-passing reasoning beyond merely supplying relation features.

The feasibility pilot does **not** need to implement B1-B5. It only needs a tiny simple-fusion model that proves the pipeline can train and output future class/time predictions.

---

## 6. Compute strategy

The team has no local GPU and plans to use free Colab first, with a possible paid Colab budget of roughly **100 compute units** later. Google states that Colab GPU/TPU availability, runtime limits, and hardware types are dynamic. Therefore the project must be budgeted from **measured pilot cost**, not assumed GPU hours.

### CPU work

- Download/version checking
- BAS parsing
- GSR streaming
- Timestamp alignment
- Downsampling
- Velocity derivation
- Window generation
- Statistics and validation

### GPU work

- One-time visual feature extraction
- Tiny feasibility training
- Later full model training

### Core efficiency rule

**Never repeatedly train on raw 4K video.**

Raw video is processed once:

```text
4K video -> sample frames -> frozen visual encoder -> compact embeddings
```

Raw GSR is processed once:

```text
multi-GB GSR JSON -> streaming parser -> required fields -> downsample -> compact tensors
```

Training then uses compact visual features + compact structured state.

---

## 7. Feasibility study: purpose and scope

### Purpose

The pilot must prove that the full research pipeline is technically executable and resource-feasible. It is **not** meant to produce a publication-quality accuracy score.

### Pilot match

Use **match 117093** unless the canonical revision shows a new issue.

Do not use 132831 for the pilot.

### Pilot duration

Start with the first valid **10 minutes of one half**.

### Pilot inputs

- Canonical BAS for match 117093
- Corresponding GSR half
- Matching panoramic video segment

### Pilot outputs

```text
pilot_manifest.json
pilot_events.parquet
pilot_state.npz
pilot_visual.npy
pilot_windows.parquet
pilot_alignment_audit.csv
pilot_model.pt
pilot_training_log.csv
pilot_predictions.json
resource_usage.json
feasibility_report.md
```

---

## 8. Feasibility architecture

```text
                 CANONICAL SOCCERTRACK v2
                           |
              +------------+------------+
              |            |            |
             BAS          GSR          VIDEO
              |            |            |
       schema/time     stream parse   sample frames
         validator      25 -> 5 Hz     ~6.25 fps
              |            |            |
              |       compact state   frozen encoder
              |          tensor          |
              |            |        visual embeddings
              +------------+------------+
                           |
                    TIME ALIGNMENT
                           |
                    WINDOW BUILDER
                   past 5s -> next 5s
                           |
                     TINY FUSION MODEL
                           |
                 class + time + confidence
                           |
                    RESOURCE REPORT
                           |
                   GO / MODIFY / NO-GO
```

---

## 9. Mandatory feasibility validation gates

### Gate A: provenance

PASS only if the exact repository revision, dataset revision/source, filenames, sizes, and hashes are recorded.

### Gate B: BAS validity

PASS only if selected events have valid classes and valid times inside the pilot segment.

### Gate C: GSR streaming

PASS only if the relevant GSR can be processed without loading the entire multi-GB JSON into RAM. Current developer docs warn that a half can be around 2.7 GB and naive loading can require roughly 20 GB RAM.

### Gate D: spatial plausibility

PASS only if sampled GSR player coordinates make sense on a pitch plot and are plausible against the corresponding video frames.

### Gate E: temporal alignment

PASS only if BAS, GSR, and video agree on time for manually inspected samples. Any systematic offset is a STOP condition until explained.

### Gate F: compression

PASS only if compact state and visual representations are dramatically smaller than raw inputs.

### Gate G: tiny training

PASS only if a tiny model can overfit 16-32 windows, the loss decreases strongly, checkpoints save/load, and future class/time outputs are produced without NaNs or broken targets.

### Gate H: resource feasibility

PASS only if measured pilot costs extrapolate to the full mandatory pipeline with meaningful safety headroom. The team's planning rule is to keep mandatory projected work around 70-80 compute units or less if the available paid balance is about 100, leaving reserve for failures and reruns. This is a project-management threshold, not a Google guarantee.

---

## 10. Independent replication rule

Two teammates may run the same pilot independently on separate Colab sessions.

They should use the **same pinned dataset/repo revision, same match, same 10-minute interval, same preprocessing rates, and same validation checklist**.

Compare these outputs across runs:

- retained BAS event count
- GSR sampled timestamp count
- state tensor shape
- visual embedding shape
- generated window count
- manual alignment results
- parse time and peak RAM
- visual extraction time and peak VRAM
- output file sizes
- tiny-model overfit behavior

Small runtime differences are normal. Data counts and shapes should match exactly unless the environment or pinned revision differs.

If two independent runs disagree on event counts, alignment, or tensor shapes, treat the pipeline as **not validated** until the discrepancy is resolved.

---

## 11. What the feasibility study can and cannot conclude

### It CAN conclude

- The raw dataset can be reduced into model-ready data.
- BAS/GSR/video can or cannot be aligned reliably.
- Memory/storage requirements are manageable or not.
- Visual feature extraction cost is acceptable or needs reduction.
- A small future-action model can consume the derived inputs.
- Full-scale work is likely feasible, needs modification, or should be rejected.

### It CANNOT conclude

- Game state improves BAA.
- A GNN is better than flat fusion.
- The final model is publication quality.
- The final model generalizes beyond SoccerTrack v2.

Those require proper match-level held-out experiments later.

---

## 12. Feasibility decision rule

### GO

Use when all critical gates pass and full-scale cost has sufficient headroom.

### MODIFY

Use when the concept is feasible but one or more technical choices must change, for example:

- lower GSR rate from 5 Hz to 2.5 Hz
- lower video sampling from 6.25 fps to 3.125 fps
- use a smaller frozen visual backbone
- reduce input resolution
- exclude or quarantine a problematic match
- simplify the full relation model

### NO-GO

Use only if a core requirement cannot be made reliable within the constraints, for example persistent BAS/GSR/video misalignment, inaccessible canonical data, or projected mandatory compute far beyond the available budget even after reasonable reductions.

---

## 13. Key literature and reference links

### Ball Action Anticipation

- FAANTRA paper: https://arxiv.org/abs/2504.12021
- FAANTRA code: https://github.com/MohamadDalal/FAANTRA
- SoccerNet 2026 challenge report: https://arxiv.org/abs/2607.07320
- SoccerNet 2026 BAA page: https://www.soccer-net.org/challenges/2026

### Game-state prior work

- Ochin et al., Game State and Spatio-Temporal Action Detection: https://www.scitepress.org/PublishedPapers/2025/131611/
- Direct PDF: https://www.scitepress.org/Papers/2025/131611/131611.pdf
- Beyond Pixels: https://arxiv.org/abs/2505.09455

### SoccerTrack v2

- Paper: https://arxiv.org/abs/2508.01802
- Project: https://atomscott.github.io/SoccerTrack-v2/
- GitHub: https://github.com/AtomScott/SoccerTrack-v2
- Hugging Face: https://huggingface.co/datasets/atomscott/soccertrack-v2
- Google Drive mirror: https://drive.google.com/drive/folders/1N2Qx2qkFgRtpbHitl2Vh6sLVYGgqkWwn
- GSR format/current release warnings: https://github.com/AtomScott/SoccerTrack-v2/blob/main/docs/format-gsr.md
- BAS format: https://github.com/AtomScott/SoccerTrack-v2/blob/main/docs/format-bas.md
- Data corrections: https://github.com/AtomScott/SoccerTrack-v2/tree/main/data_corrections

### Compute

- Google Colab FAQ: https://research.google.com/colaboratory/faq.html

---

## 14. Instructions to any AI model receiving this file

1. Treat this file as project context, not as proof of current external facts.
2. Before changing the feasibility plan, verify time-sensitive SoccerTrack and Colab claims against the official links above.
3. Prefer primary papers and official repository documentation.
4. Do not silently resolve contradictions. Record them and state which source/revision you choose.
5. Do not use match 132831 unless a corrected GSR revision is confirmed.
6. Do not use the older Drive BAS statistics as canonical current-release counts.
7. Do not claim scientific success from the feasibility pilot. The pilot is only a technical and resource validation.
8. Preserve provenance: dataset revision, repo commit, hashes, parameters, runtime, hardware, and all exclusions.
9. When judging feasibility, return one of **GO / MODIFY / NO-GO** with evidence for every failed or uncertain gate.
10. If generating code, make each stage restartable and write intermediate compact outputs so a Colab disconnect does not destroy completed work.

---

## 15. One-sentence project summary

**The thesis tests whether explicit player game state adds predictive value to short-horizon football Ball Action Anticipation, and the immediate feasibility study must prove that SoccerTrack v2 video, GSR, and BAS can be versioned, aligned, compressed, trained on at small scale, and projected to full-scale execution within the team's Colab constraints.**
