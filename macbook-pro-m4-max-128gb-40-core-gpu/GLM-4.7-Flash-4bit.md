# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 3

### Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 182.95 ± 1.30 | 90.54 ± 0.28 | 0.110 ± 0.002 | 16.90 ± 0.00 | 5.77 ± 0.02 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 184.44 | 90.81 | 0.108 | 16.90 | 5.75 |
| 2 | 182.38 | 90.25 | 0.110 | 16.90 | 5.79 |
| 3 | 182.03 | 90.55 | 0.111 | 16.90 | 5.77 |

## Prompt: `prompts/turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 500.79 ± 8.86 | 46.12 ± 0.50 | 43.281 ± 0.758 | 23.82 ± 0.00 | 54.39 ± 0.84 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 510.82 | 46.39 | 42.425 | 23.82 | 53.47 |
| 2 | 497.50 | 46.42 | 43.554 | 23.82 | 54.59 |
| 3 | 494.04 | 45.54 | 43.864 | 23.82 | 55.11 |
