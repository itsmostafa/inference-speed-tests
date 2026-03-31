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
| gpt-oss-20b-MXFP4-Q8 | N/A | 73 | 556.55 ± 8.05 | 121.02 ± 0.14 | 0.197 ± 0.002 | 12.19 ± 0.00 | 4.44 ± 0.00 |

### Per-Iteration Details

#### gpt-oss-20b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 553.08 | 120.97 | 0.197 | 12.19 | 4.44 |
| 2 | 565.76 | 120.91 | 0.196 | 12.19 | 4.44 |
| 3 | 550.82 | 121.18 | 0.199 | 12.19 | 4.43 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-20b-MXFP4-Q8 | N/A | 21K | 1281.19 ± 5.31 | 91.09 ± 0.26 | 17.031 ± 0.064 | 13.42 ± 0.00 | 22.66 ± 0.08 |

### Per-Iteration Details

#### gpt-oss-20b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 1285.78 | 91.38 | 16.980 | 13.42 | 22.59 |
| 2 | 1282.41 | 91.01 | 17.011 | 13.42 | 22.64 |
| 3 | 1275.37 | 90.87 | 17.103 | 13.42 | 22.74 |
