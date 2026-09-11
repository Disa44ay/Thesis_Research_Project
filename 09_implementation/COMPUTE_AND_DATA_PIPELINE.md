Compute and Data Pipeline

Feasibility judgment

Candidate 01B remains feasible under the expected Colab Pro research
budget only if expensive raw processing is performed once and ordinary
training uses compact derived features.

Structured branch

GSR raw JSON → streaming parser → retain needed player state →
downsample → derive velocity and relations → compact Parquet or NPZ →
lightweight model.

Visual branch

4K video → sample frames or clips → resize → frozen pretrained visual
encoder → save embeddings → reuse embeddings for every training run and
ablation.

Storage strategy

Process one match at a time. Do not require every raw video, GSR file,
processed feature, and model artifact to exist simultaneously on one
temporary Colab VM.

Rejected compute pattern

1.  End-to-end training from full 4K video.
2.  Repeated large-backbone fine-tuning across ablations.
3.  Reconstructing detection, tracking, ReID, calibration, and GSR when
    annotations already exist.
4.  Loading multi-gigabyte GSR JSON into memory as one object when
    streaming or chunking is possible.

Deployment consequence

The final zero-cost demo should process only small clips or preprocessed
examples and permanently store only compact structured outputs.

------------------------------------------------------------------------
