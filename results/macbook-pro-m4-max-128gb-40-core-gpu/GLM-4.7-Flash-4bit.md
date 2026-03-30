# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 2

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 198K | 11 | 178.17 ± 3.49 | 86.17 ± 2.43 | 0.115 ± 0.001 | 16.90 ± 0.00 | 6.06 ± 0.17 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 175.70 | 84.45 | 0.116 | 16.90 | 6.18 |
| 2 | 180.64 | 87.89 | 0.114 | 16.90 | 5.94 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 4

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 198K | N/A | 481.17 ± 22.94 | 46.02 ± 1.04 | 45.117 ± 2.247 | 23.96 ± 0.29 | 56.25 ± 2.50 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 486.85 | 46.51 | 44.508 | 23.82 | 55.52 |
| 2 | 493.70 | 46.53 | 43.899 | 23.82 | 54.91 |
| 3 | 447.33 | 44.46 | 48.441 | 24.39 | 59.96 |
| 4 | 496.81 | 46.57 | 43.618 | 23.82 | 54.62 |
