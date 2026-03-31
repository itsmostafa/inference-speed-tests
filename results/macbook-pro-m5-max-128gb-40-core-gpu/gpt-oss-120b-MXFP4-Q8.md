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
| gpt-oss-120b-MXFP4-Q8 | N/A | 73 | 352.44 ± 1.18 | 92.95 ± 0.02 | 0.270 ± 0.001 | 63.47 ± 0.00 | 5.78 ± 0.00 |

### Per-Iteration Details

#### gpt-oss-120b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 351.61 | 92.92 | 0.270 | 63.47 | 5.79 |
| 2 | 353.80 | 92.95 | 0.269 | 63.47 | 5.78 |
| 3 | 351.92 | 92.97 | 0.270 | 63.47 | 5.78 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-120b-MXFP4-Q8 | N/A | 21K | 1852.78 ± 16.41 | 68.64 ± 1.39 | 11.800 ± 0.103 | 65.01 ± 0.00 | 19.27 ± 0.17 |

### Per-Iteration Details

#### gpt-oss-120b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 1843.10 | 67.40 | 11.861 | 65.01 | 19.46 |
| 2 | 1871.73 | 68.38 | 11.680 | 65.01 | 19.18 |
| 3 | 1843.51 | 70.14 | 11.858 | 65.01 | 19.16 |
