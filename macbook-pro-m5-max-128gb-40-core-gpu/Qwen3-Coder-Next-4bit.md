# Inference Speed Test Results

**Date**: 2026-03-29
**Device**: Apple M5 Max | 128 GB RAM | 40-core GPU
**OS**: macOS-26.4-arm64-arm-64bit-Mach-O
**Prompt**: `Write a 500 word story`
**Max tokens**: 512 | **Iterations**: 3

## Summary

| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |
| Qwen3-Coder-Next-4bit | 306.91 ± 0.72 | 105.75 ± 1.83 | 0.094 ± 0.000 | 44.92 ± 0.00 | 4.94 ± 0.08 |

## Per-Iteration Details

### Qwen3-Coder-Next-4bit

| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |
| --- | ---------- | -------------- | -------- | ---------------- | -------------- |
| 1 | 307.62 | 106.92 | 0.094 | 44.92 | 4.89 |
| 2 | 306.17 | 106.69 | 0.094 | 44.92 | 4.90 |
| 3 | 306.94 | 103.65 | 0.094 | 44.92 | 5.04 |
