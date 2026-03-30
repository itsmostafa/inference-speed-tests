# Inference Speed Test Results

**Date**: 2026-03-28
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| GLM-4.7-Flash-4bit | 204.77 ± 0.93 | 98.32 ± 0.80 | 0.102 ± 0.000 | 16.90 ± 0.00 | 5.31 ± 0.04 |

## Per-Iteration Details

### GLM-4.7-Flash-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 205.77 | 97.40 | 0.102 | 16.90 | 5.36 |
| 2 | 204.60 | 98.65 | 0.102 | 16.90 | 5.30 |
| 3 | 203.94 | 98.91 | 0.102 | 16.90 | 5.28 |
