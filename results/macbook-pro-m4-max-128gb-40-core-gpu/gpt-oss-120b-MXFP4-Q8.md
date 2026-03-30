# Inference Speed Test Results

**Date**: 2026-03-29
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-120b-MXFP4-Q8 | 301.47 ± 7.16 | 81.47 ± 0.67 | 0.317 ± 0.007 | 63.47 ± 0.00 | 6.61 ± 0.04 |

## Per-Iteration Details

### gpt-oss-120b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 304.49 | 80.87 | 0.312 | 63.47 | 6.65 |
| 2 | 293.30 | 82.20 | 0.325 | 63.47 | 6.56 |
| 3 | 306.62 | 81.35 | 0.314 | 63.47 | 6.62 |
