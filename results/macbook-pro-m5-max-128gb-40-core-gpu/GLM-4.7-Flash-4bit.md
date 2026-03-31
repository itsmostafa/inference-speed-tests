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
| GLM-4.7-Flash-4bit | 198K | 11 | 205.35 ± 2.05 | 101.17 ± 0.20 | 0.097 ± 0.001 | 16.90 ± 0.00 | 5.16 ± 0.01 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 207.61 | 100.95 | 0.095 | 16.90 | 5.17 |
| 2 | 204.85 | 101.21 | 0.097 | 16.90 | 5.16 |
| 3 | 203.60 | 101.34 | 0.098 | 16.90 | 5.15 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 198K | 21K | 1028.55 ± 2.26 | 59.18 ± 0.17 | 21.093 ± 0.046 | 23.82 ± 0.00 | 29.75 ± 0.06 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 1028.21 | 58.99 | 21.100 | 23.82 | 29.79 |
| 2 | 1026.48 | 59.23 | 21.135 | 23.82 | 29.79 |
| 3 | 1030.95 | 59.31 | 21.044 | 23.82 | 29.68 |
