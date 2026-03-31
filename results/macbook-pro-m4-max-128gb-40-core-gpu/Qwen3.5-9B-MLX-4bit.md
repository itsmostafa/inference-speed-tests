# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `Given the following input, classify the verb as transitiv...`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | N/A | 26 | 339.30 ± 28.99 | 89.76 ± 0.34 | 0.180 ± 0.005 | 5.16 ± 0.00 | 5.90 ± 0.03 |

### Per-Iteration Details

#### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 305.84 | 89.55 | 0.182 | 5.16 | 5.91 |
| 2 | 355.04 | 89.59 | 0.184 | 5.16 | 5.91 |
| 3 | 357.03 | 90.15 | 0.175 | 5.16 | 5.87 |

## Prompt: `prompts/500_word_story.md`

**Iterations**: 6

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | N/A | 18 | 241.74 ± 17.27 | 90.27 ± 0.49 | 0.180 ± 0.007 | 5.14 ± 0.00 | 5.86 ± 0.03 |

### Per-Iteration Details

#### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 220.16 | 90.45 | 0.178 | 5.14 | 5.85 |
| 2 | 253.15 | 90.54 | 0.179 | 5.14 | 5.84 |
| 3 | 254.14 | 90.36 | 0.190 | 5.14 | 5.87 |
| 4 | 218.87 | 89.52 | 0.179 | 5.14 | 5.91 |
| 5 | 250.22 | 89.89 | 0.186 | 5.14 | 5.89 |
| 6 | 253.88 | 90.88 | 0.171 | 5.14 | 5.82 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | N/A | N/A | 722.85 ± 50.27 | 72.62 ± 4.88 | 31.426 ± 2.264 | 8.85 ± 0.00 | 38.52 ± 2.76 |

### Per-Iteration Details

#### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 760.00 | 76.56 | 29.793 | 8.85 | 36.50 |
| 2 | 742.90 | 74.13 | 30.475 | 8.85 | 37.39 |
| 3 | 665.65 | 67.16 | 34.011 | 8.85 | 41.66 |
