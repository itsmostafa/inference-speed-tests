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
| Qwen3-Coder-Next-4bit | 256K | 16 | 303.19 ± 0.38 | 105.86 ± 0.70 | 0.096 ± 0.000 | 44.92 ± 0.00 | 4.94 ± 0.03 |

### Per-Iteration Details

#### Qwen3-Coder-Next-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 303.61 | 105.15 | 0.096 | 44.92 | 4.97 |
| 2 | 303.10 | 105.87 | 0.096 | 44.92 | 4.94 |
| 3 | 302.85 | 106.56 | 0.096 | 44.92 | 4.90 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3-Coder-Next-4bit | 256K | 21K | 2442.00 ± 83.93 | 91.59 ± 0.16 | 9.231 ± 0.317 | 48.73 ± 0.00 | 14.83 ± 0.33 |

### Per-Iteration Details

#### Qwen3-Coder-Next-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 2526.96 | 91.75 | 8.914 | 48.73 | 14.50 |
| 2 | 2439.91 | 91.59 | 9.230 | 48.73 | 14.82 |
| 3 | 2359.13 | 91.43 | 9.549 | 48.73 | 15.15 |
