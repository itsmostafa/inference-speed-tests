# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 6

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3-8B-4bit | 40K | 16 | 233.59 ± 2.76 | 95.88 ± 0.63 | 0.126 ± 0.011 | 4.78 ± 0.00 | 5.48 ± 0.04 |

### Per-Iteration Details

#### Qwen3-8B-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 236.15 | 95.98 | 0.116 | 4.78 | 5.47 |
| 2 | 230.88 | 95.48 | 0.140 | 4.78 | 5.52 |
| 3 | 230.02 | 96.21 | 0.140 | 4.78 | 5.50 |
| 4 | 236.10 | 94.82 | 0.115 | 4.78 | 5.52 |
| 5 | 232.68 | 96.23 | 0.123 | 4.78 | 5.45 |
| 6 | 235.69 | 96.56 | 0.120 | 4.78 | 5.43 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3-8B-4bit | 40K | 21K | 557.30 ± 44.31 | 51.91 ± 5.48 | 40.397 ± 3.358 | 8.51 ± 0.00 | 50.35 ± 4.47 |

### Per-Iteration Details

#### Qwen3-8B-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 579.29 | 55.05 | 38.695 | 8.51 | 48.00 |
| 2 | 586.32 | 55.09 | 38.231 | 8.51 | 47.53 |
| 3 | 506.31 | 45.58 | 44.266 | 8.51 | 55.51 |
