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
| gpt-oss-120b-MXFP4-Q8 | N/A | 73 | 304.39 ± 3.36 | 81.34 ± 0.26 | 0.313 ± 0.009 | 63.47 ± 0.00 | 6.61 ± 0.02 |

### Per-Iteration Details

#### gpt-oss-120b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 308.14 | 81.37 | 0.302 | 63.47 | 6.60 |
| 2 | 303.38 | 81.58 | 0.318 | 63.47 | 6.60 |
| 3 | 301.65 | 81.07 | 0.318 | 63.47 | 6.64 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-120b-MXFP4-Q8 | N/A | 21K | 701.54 ± 32.67 | 58.31 ± 1.17 | 31.086 ± 1.493 | 65.01 ± 0.00 | 39.88 ± 1.67 |

### Per-Iteration Details

#### gpt-oss-120b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 726.44 | 59.28 | 29.970 | 65.01 | 38.61 |
| 2 | 713.62 | 58.64 | 30.506 | 65.01 | 39.24 |
| 3 | 664.55 | 57.01 | 32.783 | 65.01 | 41.77 |
