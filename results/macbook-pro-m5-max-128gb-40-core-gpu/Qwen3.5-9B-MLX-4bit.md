# Inference Speed Test Results

**Date**: 2026-03-30
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 6

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | N/A | 18 | 310.75 ± 32.95 | 104.31 ± 1.04 | 0.139 ± 0.005 | 5.14 ± 0.00 | 5.06 ± 0.05 |

### Per-Iteration Details

#### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 272.78 | 103.04 | 0.144 | 5.14 | 5.12 |
| 2 | 324.10 | 103.37 | 0.138 | 5.14 | 5.10 |
| 3 | 331.83 | 103.77 | 0.137 | 5.14 | 5.08 |
| 4 | 264.60 | 105.31 | 0.145 | 5.14 | 5.02 |
| 5 | 336.02 | 105.35 | 0.134 | 5.14 | 5.00 |
| 6 | 335.18 | 105.04 | 0.134 | 5.14 | 5.02 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 6

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | N/A | 22K | 2613.59 ± 92.41 | 91.44 ± 1.03 | 8.735 ± 0.302 | 8.85 ± 0.00 | 14.34 ± 0.35 |

### Per-Iteration Details

#### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 2649.89 | 91.14 | 8.606 | 8.85 | 14.23 |
| 2 | 2544.63 | 90.68 | 8.962 | 8.85 | 14.62 |
| 3 | 2523.47 | 89.92 | 9.034 | 8.85 | 14.74 |
| 4 | 2757.87 | 92.49 | 8.274 | 8.85 | 13.82 |
| 5 | 2663.89 | 92.33 | 8.563 | 8.85 | 14.12 |
| 6 | 2541.80 | 92.08 | 8.971 | 8.85 | 14.54 |
