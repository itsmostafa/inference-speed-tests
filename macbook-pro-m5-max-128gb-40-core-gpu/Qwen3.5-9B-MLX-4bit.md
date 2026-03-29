# Inference Speed Test Results

**Date**: 2026-03-28
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 4

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | 333.03 ± 1.20 | 105.17 ± 0.42 | 0.145 ± 0.000 | 5.14 ± 0.00 | 5.02 ± 0.02 |

## Per-Iteration Details

### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 331.93 | 105.40 | 0.145 | 5.14 | 5.01 |
| 2 | 334.13 | 104.60 | 0.145 | 5.14 | 5.05 |
| 3 | 332.04 | 105.12 | 0.145 | 5.14 | 5.03 |
| 4 | 334.01 | 105.55 | 0.144 | 5.14 | 5.01 |
