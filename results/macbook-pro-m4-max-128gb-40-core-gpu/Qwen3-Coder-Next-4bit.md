# Inference Speed Test Results

**Date**: 2026-03-29
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3-Coder-Next-4bit | 210.92 ± 2.32 | 91.67 ± 0.81 | 0.125 ± 0.001 | 44.92 ± 0.00 | 5.71 ± 0.05 |

## Per-Iteration Details

### Qwen3-Coder-Next-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 211.20 | 90.82 | 0.126 | 44.92 | 5.77 |
| 2 | 208.48 | 92.44 | 0.125 | 44.92 | 5.67 |
| 3 | 213.09 | 91.77 | 0.124 | 44.92 | 5.71 |
