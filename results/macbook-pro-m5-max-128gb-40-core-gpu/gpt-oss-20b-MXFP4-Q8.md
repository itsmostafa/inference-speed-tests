# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-20b-MXFP4-Q8 | N/A | 73 | 789.64 ± 1.64 | 137.76 ± 0.24 | 0.153 ± 0.002 | 12.19 ± 0.00 | 3.88 ± 0.01 |

### Per-Iteration Details

#### gpt-oss-20b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 790.60 | 137.71 | 0.151 | 12.19 | 3.88 |
| 2 | 790.57 | 138.02 | 0.153 | 12.19 | 3.87 |
| 3 | 787.74 | 137.55 | 0.155 | 12.19 | 3.88 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-20b-MXFP4-Q8 | N/A | 21K | 4211.48 ± 310.15 | 105.86 ± 0.37 | 5.250 ± 0.387 | 13.42 ± 0.00 | 10.09 ± 0.40 |

### Per-Iteration Details

#### gpt-oss-20b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 4513.75 | 106.19 | 4.884 | 13.42 | 9.71 |
| 2 | 4226.68 | 105.92 | 5.211 | 13.42 | 10.05 |
| 3 | 3894.01 | 105.47 | 5.655 | 13.42 | 10.52 |
