# Inference Speed Test Results

**Date**: 2026-03-28
**Device**: Apple M4 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.2-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3.5-9B-MLX-4bit | 241.12 ± 21.66 | 90.81 ± 0.14 | 0.178 ± 0.006 | 5.14 ± 0.00 | 5.83 ± 0.01 |

## Per-Iteration Details

### Qwen3.5-9B-MLX-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 216.14 | 90.78 | 0.182 | 5.14 | 5.83 |
| 2 | 254.67 | 90.69 | 0.171 | 5.14 | 5.83 |
| 3 | 252.55 | 90.97 | 0.181 | 5.14 | 5.82 |
