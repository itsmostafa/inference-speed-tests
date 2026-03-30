# Inference Speed Test Results

**Date**: 2026-03-28
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-20b-MXFP4-Q8 | 623.97 ± 0.88 | 121.61 ± 0.73 | 0.188 ± 0.004 | 12.19 ± 0.00 | 4.41 ± 0.02 |

## Per-Iteration Details

### gpt-oss-20b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 623.70 | 120.96 | 0.183 | 12.19 | 4.42 |
| 2 | 623.26 | 122.39 | 0.189 | 12.19 | 4.38 |
| 3 | 624.96 | 121.47 | 0.191 | 12.19 | 4.41 |
