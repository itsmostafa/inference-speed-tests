# Inference Speed Test Results

**Date**: 2026-03-28
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 174.52 ± 15.01 | 90.56 ± 1.05 | 0.116 ± 0.010 | 16.90 ± 0.00 | 5.78 ± 0.08 |

## Per-Iteration Details

### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 157.19 | 89.36 | 0.127 | 16.90 | 5.86 |
| 2 | 183.30 | 91.28 | 0.109 | 16.90 | 5.72 |
| 3 | 183.07 | 91.05 | 0.113 | 16.90 | 5.74 |
