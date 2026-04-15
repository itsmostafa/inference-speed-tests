# Inference Speed Test Results

**Date**: 2026-04-15
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4.1-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gemma-4-31b-it-mxfp4 | N/A | 24 | 112.99 ± 0.83 | 28.30 ± 0.73 | 0.305 ± 0.006 | 17.12 ± 0.00 | 18.42 ± 0.47 |

### Per-Iteration Details

#### gemma-4-31b-it-mxfp4

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 113.72 | 28.96 | 0.299 | 17.12 | 17.99 |
| 2 | 112.08 | 28.41 | 0.304 | 17.12 | 18.34 |
| 3 | 113.17 | 27.53 | 0.311 | 17.12 | 18.92 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gemma-4-31b-it-mxfp4 | N/A | 20K | 542.97 ± 28.85 | 20.72 ± 0.31 | 39.267 ± 2.078 | 24.17 ± 0.00 | 63.99 ± 2.43 |

### Per-Iteration Details

#### gemma-4-31b-it-mxfp4

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 572.43 | 21.08 | 37.182 | 24.17 | 61.49 |
| 2 | 541.71 | 20.58 | 39.281 | 24.17 | 64.17 |
| 3 | 514.78 | 20.49 | 41.337 | 24.17 | 66.33 |
