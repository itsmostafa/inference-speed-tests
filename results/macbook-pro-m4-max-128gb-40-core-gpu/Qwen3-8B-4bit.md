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
| Qwen3-8B-4bit | 40K | 16 | 232.35 ± 3.32 | 95.89 ± 0.37 | 0.132 ± 0.014 | 4.78 ± 0.00 | 5.49 ± 0.02 |

### Per-Iteration Details

#### Qwen3-8B-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 236.15 | 95.98 | 0.116 | 4.78 | 5.47 |
| 2 | 230.88 | 95.48 | 0.140 | 4.78 | 5.52 |
| 3 | 230.02 | 96.21 | 0.140 | 4.78 | 5.50 |
