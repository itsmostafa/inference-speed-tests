# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 198K | 11 | 180.53 ± 2.73 | 87.53 ± 1.99 | 0.109 ± 0.003 | 16.90 ± 0.00 | 5.97 ± 0.13 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 182.06 | 89.74 | 0.106 | 16.90 | 5.82 |
| 2 | 182.15 | 86.99 | 0.109 | 16.90 | 6.00 |
| 3 | 177.37 | 85.88 | 0.112 | 16.90 | 6.08 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 198K | 21K | 514.78 ± 7.31 | 46.59 ± 0.11 | 42.100 ± 0.598 | 23.82 ± 0.00 | 53.10 ± 0.57 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 517.11 | 46.61 | 41.904 | 23.82 | 52.90 |
| 2 | 520.64 | 46.48 | 41.625 | 23.82 | 52.65 |
| 3 | 506.60 | 46.69 | 42.771 | 23.82 | 53.74 |
