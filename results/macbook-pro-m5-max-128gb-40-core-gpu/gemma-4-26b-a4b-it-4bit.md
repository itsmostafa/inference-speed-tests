# Inference Speed Test Results

**Date**: 2026-04-15
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4.1-arm64-arm-64bit-Mach-O
**Max tokens**: 512

## Prompt: `prompts/500_word_story.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gemma-4-26b-a4b-it-4bit | N/A | 24 | 350.45 ± 41.02 | 124.70 ± 0.25 | 0.159 ± 0.005 | 14.68 ± 0.00 | 4.27 ± 0.01 |

### Per-Iteration Details

#### gemma-4-26b-a4b-it-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 343.80 | 124.99 | 0.156 | 14.68 | 4.26 |
| 2 | 394.40 | 124.56 | 0.155 | 14.68 | 4.27 |
| 3 | 313.16 | 124.54 | 0.164 | 14.68 | 4.28 |

## Prompt: `prompts/summarize-turbo-quant.md`

**Iterations**: 3

### Summary

| Model | Max Ctx | Prompt Tokens | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ------- | ------------- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gemma-4-26b-a4b-it-4bit | N/A | 20K | 3527.07 ± 151.40 | 94.27 ± 0.21 | 6.137 ± 0.259 | 17.65 ± 0.00 | 11.57 ± 0.27 |

### Per-Iteration Details

#### gemma-4-26b-a4b-it-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 3654.80 | 94.47 | 5.929 | 17.65 | 11.36 |
| 2 | 3566.58 | 94.30 | 6.055 | 17.65 | 11.49 |
| 3 | 3359.83 | 94.05 | 6.427 | 17.65 | 11.88 |
