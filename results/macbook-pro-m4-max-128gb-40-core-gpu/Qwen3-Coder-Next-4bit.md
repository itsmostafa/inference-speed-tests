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
| Qwen3-Coder-Next-4bit | 256K | 16 | 247.21 ± 2.17 | 90.59 ± 0.43 | 0.114 ± 0.001 | 44.92 ± 0.00 | 5.77 ± 0.03 |

### Per-Iteration Details

#### Qwen3-Coder-Next-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 247.93 | 91.08 | 0.113 | 44.92 | 5.74 |
| 2 | 248.93 | 90.41 | 0.114 | 44.92 | 5.78 |
| 3 | 244.77 | 90.29 | 0.115 | 44.92 | 5.79 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3-Coder-Next-4bit | 256K | 21K | 986.67 ± 17.45 | 72.63 ± 0.40 | 22.755 ± 0.403 | 48.73 ± 0.00 | 29.81 ± 0.44 |

### Per-Iteration Details

#### Qwen3-Coder-Next-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 967.13 | 72.19 | 23.207 | 48.73 | 30.30 |
| 2 | 1000.70 | 72.99 | 22.432 | 48.73 | 29.45 |
| 3 | 992.19 | 72.71 | 22.626 | 48.73 | 29.67 |
