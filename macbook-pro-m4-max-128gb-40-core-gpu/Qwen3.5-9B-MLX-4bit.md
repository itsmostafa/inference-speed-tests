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
| Qwen3.5-9B-MLX-4bit | N/A | 18 | 242.48 ± 19.33 | 90.45 ± 0.09 | 0.182 ± 0.007 | 5.14 ± 0.00 | 5.85 ± 0.01 |

### Per-Iteration Details

#### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 220.16 | 90.45 | 0.178 | 5.14 | 5.85 |
| 2 | 253.15 | 90.54 | 0.179 | 5.14 | 5.84 |
| 3 | 254.14 | 90.36 | 0.190 | 5.14 | 5.87 |
