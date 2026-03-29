# Inference Speed Test Results

**Date**: 2026-03-28
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| gpt-oss-20b-MXFP4-Q8 | 792.34 ± 8.24 | 139.34 ± 0.21 | 0.160 ± 0.001 | 12.19 ± 0.00 | 3.84 ± 0.00 |

## Per-Iteration Details

### gpt-oss-20b-MXFP4-Q8

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 787.71 | 139.57 | 0.161 | 12.19 | 3.84 |
| 2 | 787.46 | 139.28 | 0.161 | 12.19 | 3.84 |
| 3 | 801.85 | 139.17 | 0.159 | 12.19 | 3.85 |
