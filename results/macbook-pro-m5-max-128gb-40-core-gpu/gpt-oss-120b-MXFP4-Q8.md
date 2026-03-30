# Inference Speed Test Results

**Date**: 2026-03-29
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-120b-MXFP4-Q8 | 355.12 ± 0.37 | 93.11 ± 0.14 | 0.265 ± 0.000 | 63.47 ± 0.00 | 5.77 ± 0.01 |

## Per-Iteration Details

### gpt-oss-120b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 354.71 | 93.25 | 0.266 | 63.47 | 5.76 |
| 2 | 355.19 | 93.11 | 0.265 | 63.47 | 5.77 |
| 3 | 355.45 | 92.96 | 0.266 | 63.47 | 5.78 |
