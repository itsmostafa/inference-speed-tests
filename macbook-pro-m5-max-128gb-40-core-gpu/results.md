# Inference Speed Test Results

**Date**: 2026-03-28
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | 333.61 ± 1.19 | 105.22 ± 0.25 | 0.144 ± 0.000 | 5.14 ± 0.00 | 5.02 ± 0.01 |

## Per-Iteration Details

### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 334.71 | 105.51 | 0.144 | 5.14 | 5.01 |
| 2 | 332.35 | 105.05 | 0.145 | 5.14 | 5.03 |
| 3 | 333.78 | 105.11 | 0.144 | 5.14 | 5.03 |
