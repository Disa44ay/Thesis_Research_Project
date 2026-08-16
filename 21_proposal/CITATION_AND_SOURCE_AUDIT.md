# Citation and Source Audit

**Proposal:** Evaluating Game-State Fusion for Short-Horizon Ball Action Anticipation in Football  
**Audit date:** 14 August 2026  
**Rule:** Primary papers and official project/repository documentation are used for claims that determine the proposal. Current platform claims are sourced from Google.

## 1. FAANTRA

**Citation:** Mohamad Dalal et al., *Action Anticipation from SoccerNet Football Video Broadcasts*, CVPR Workshops (CVSports), 2025.

**Primary sources**
- https://openaccess.thecvf.com/content/CVPR2025W/CVSPORTS/html/Dalal_Action_Anticipation_from_SoccerNet_Football_Video_Broadcasts_CVPRW_2025_paper.html
- https://arxiv.org/html/2504.12021v1

**Verified proposal claims**
1. Football Ball Action Anticipation predicts future actions from observed past frames while future frames are unavailable.
2. Each target action is represented by an action class and a timestamp in the anticipation window.
3. The original paper studies 5 s and 10 s anticipation windows.
4. Standardized test/challenge clips provide up to 30 s of context and use a stride equal to the anticipation horizon.
5. Goal and Free Kick were excluded from SN-BAA because their test counts were too small for stable AP.
6. The task uses mAP at temporal tolerances delta in {1,2,3,4,5,infinity}.
7. For finite delta, a prediction is correct when it lies within delta/2 seconds of the ground-truth timestamp.
8. FAANTRA uses a query-based output with actionness, class, and timestamp predictions.

**Status:** VERIFIED.

## 2. SoccerNet 2026 Challenges Results

**Citation:** Anthony Cioppa et al., *SoccerNet 2026 Challenges Results*, arXiv:2607.07320, 2026.

**Primary source**
- https://arxiv.org/html/2607.07320v1

**Verified proposal claims**
1. The 2026 BAA challenge observes 30 s and predicts the next 5 s over 10 action classes.
2. Nine teams participated in BAA and five supplied reviewed technical reports.
3. The published leaderboard includes only reviewed-report teams.
4. Reviewed methods primarily modify visual representations, temporal modeling, optimization, matching, or ensembling.
5. VLM-TCF adds semantic tactical context extracted by a frozen vision-language model.
6. The five reviewed technical reports do not document synchronized metric per-player GSR trajectories or explicit player-interaction graphs as BAA inputs.

**Qualification:** The last statement applies only to the five reviewed/publicly documented reports. It is not a claim about every undocumented submission.

**Status:** VERIFIED WITH NARROW WORDING.

## 3. Ochin et al. 2025

**Citation:** Jeremie Ochin, Guillaume Devineau, Bogdan Stanciulescu, Sotiris Manitsaris, *Game State and Spatio-Temporal Action Detection in Soccer Using Graph Neural Networks and 3D Convolutional Networks*, ICPRAM 2025, pp. 636-646, DOI 10.5220/0013161100003905.

**Primary source**
- https://www.scitepress.org/Papers/2025/131611/131611.pdf

**Verified proposal claims**
1. Explicit player game state has prior use in football action understanding.
2. The method combines visual features with structured game-state information through graph reasoning.
3. Positions, velocities, and team-related information are used.
4. The task is spatio-temporal action detection, not anticipation of unseen future actions.

**Status:** VERIFIED.

## 4. Beyond Pixels

**Citation:** Jeremie Ochin, Raphael Chekroun, Bogdan Stanciulescu, Sotiris Manitsaris, *Beyond Pixels: Leveraging the Language of Soccer to Improve Spatio-Temporal Action Detection in Broadcast Videos*, arXiv:2505.09455, 2025.

**Primary source**
- https://arxiv.org/abs/2505.09455

**Verified proposal claims**
1. Longer temporal context and structured game state are used to denoise soccer action sequences.
2. The method reasons over team-level/inter-player context.
3. The task remains action detection/sequence correction rather than Ball Action Anticipation.

**Status:** VERIFIED.

## 5. SoccerTrack v2 paper and project

**Citation:** Atom Scott, Ikuma Uchida, Kento Kuroda, Yufi Kim, Keisuke Fujii, *SoccerTrack v2: A Full-Pitch Multi-View Soccer Dataset for Game State Reconstruction*, arXiv:2508.01802, 2025.

**Primary sources**
- Paper: https://arxiv.org/abs/2508.01802
- Project: https://atomscott.github.io/SoccerTrack-v2/
- Repository: https://github.com/AtomScott/SoccerTrack-v2
- Canonical dataset: https://huggingface.co/datasets/atomscott/soccertrack-v2
- Drive mirror: https://drive.google.com/drive/folders/1N2Qx2qkFgRtpbHitl2Vh6sLVYGgqkWwn

**Verified proposal claims**
1. Ten full-length university-level matches.
2. Approximately 900 minutes of panoramic 4K video.
3. GSR annotations with pitch coordinates and player/game-state attributes.
4. BAS annotations over 12 classes.
5. The current project page identifies Hugging Face as the canonical distribution and states that mirrors may lag.
6. Code is MIT licensed and the dataset is CC BY 4.0 according to the current repository/project documentation.

**Status:** VERIFIED.

## 6. SoccerTrack v2 GSR format and alignment

**Primary source**
- https://github.com/AtomScott/SoccerTrack-v2/blob/main/docs/format-gsr.md

**Verified proposal claims**
1. GSR is aligned to source panoramic video at 25 fps.
2. Pitch coordinates are metric and centre-origin.
3. Track IDs are not guaranteed across halves and player IDs can be used for re-linking where available.
4. The repository currently warns that the released GSR files differ structurally from the simplified documented schema.
5. The current documentation reports files around 2.7 GB per half and warns that naïve full loading may require roughly 20 GB RAM.
6. The documentation records a second-half BAS position/alignment inconsistency and recommends the supported loader/helper logic.

**Status:** VERIFIED FROM CURRENT REPOSITORY DOCUMENTATION.

## 7. Match 132831 correction

**Primary source**
- https://github.com/AtomScott/SoccerTrack-v2/tree/main/data_corrections

**Verified proposal claims**
1. Two calibration keypoints for match 132831 were swapped.
2. The shipped calibration produced an RMS error of about 1260.95 px, compared with about 18.07 px after correction.
3. The repository states that the match's GSR labels were generated through the faulty calibration.
4. The current correction note states that the shared dataset copy still needs GSR regeneration from the corrected calibration.

**Proposal consequence:** Match 132831 is to be excluded or quarantined unless a corrected canonical GSR revision is verified before training.

**Status:** VERIFIED FROM CURRENT REPOSITORY DOCUMENTATION.

## 8. Google Colab

**Primary sources**
- Pricing: https://colab.research.google.com/signup
- FAQ: https://research.google.com/colaboratory/faq.html

**Verified proposal claims**
1. A current paid Colab option provides 100 compute units.
2. GPU/TPU type, availability, runtime limits, and usage limits can vary.
3. Google advises using a non-accelerated runtime when GPU/TPU acceleration is not required.

**Proposal consequence:** JSON processing and validation use CPU where practical. Accelerator time is reserved for one-time visual feature extraction and model training.

**Status:** VERIFIED AS OF 14 AUGUST 2026. SUBJECT TO FUTURE PLATFORM CHANGE.

# Final claim audit

## Safe central claim
The reviewed literature establishes visual football BAA and separately establishes game-state-assisted football action detection, but it does not establish whether synchronized explicit player game state improves temporally localized Ball Action Anticipation in an unseen future interval.

## Claims deliberately not made
1. First football model to fuse video and game state.
2. First football player graph model.
3. First future-event prediction system in football.
4. State of the art on the official SoccerNet BAA leaderboard.
5. Guaranteed improvement from game-state fusion.
6. Generalization to professional broadcast football without a separate experiment.

