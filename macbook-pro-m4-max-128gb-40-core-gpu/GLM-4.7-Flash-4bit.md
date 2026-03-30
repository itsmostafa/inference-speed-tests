# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 6

### Summary

| Model | Context | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 198K | 180.74 ± 4.44 | 88.90 ± 1.85 | 0.113 ± 0.007 | 16.90 ± 0.00 | 5.88 ± 0.13 |

### Per-Iteration Details

#### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 184.44 | 90.81 | 0.108 | 16.90 | 5.75 |
| 2 | 182.38 | 90.25 | 0.110 | 16.90 | 5.79 |
| 3 | 182.03 | 90.55 | 0.111 | 16.90 | 5.77 |
| 4 | 182.90 | 88.04 | 0.110 | 16.90 | 5.93 |
| 5 | 180.68 | 87.09 | 0.115 | 16.90 | 6.00 |
| 6 | 172.03 | 86.67 | 0.126 | 16.90 | 6.04 |
