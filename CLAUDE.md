# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the benchmark

```bash
# Single model, 1 iteration
uv run main.py mlx-community/GLM-4.7-Flash-4bit -n 1 -o results.md

# Multiple models, 3 iterations (default), custom output file
uv run main.py mlx-community/Qwen2.5-7B-Instruct-4bit mlx-community/Qwen2.5-14B-Instruct-4bit -o my_results.md

# All options
uv run main.py MODEL_ID [-n ITERATIONS] [-p "prompt"] [--max-tokens N] [-o output.md] [--no-warmup]
```

## Architecture

This is a single-script project (`main.py`) with one dependency (`mlx-lm`). All logic lives in `main.py`.

**Benchmark flow:**
1. `main()` → calls `get_device_info()`, then loops over models calling `benchmark_model()` for each
2. `benchmark_model()` — loads via `mlx_lm.load()`, runs a warmup pass, then `n` timed iterations using `mlx_lm.stream_generate()`
3. Metrics come from the final `GenerationResponse` yielded by `stream_generate` (cumulative `prompt_tps`, `generation_tps`, `peak_memory`); TTFT and total time are wall-clock measurements
4. `format_results_markdown()` → writes summary + per-iteration tables to disk

**Key data types:**
- `IterationResult` — raw metrics for one run
- `ModelResult` — holds all iterations for a model plus any error string

**Prompt handling:** `format_prompt()` applies the model's chat template if `tokenizer.chat_template` exists, otherwise falls back to the raw prompt string.

## Repository context

The `README.md` and `mac mini.md` contain hand-collected benchmark data from community contributors (tokens/s across various Apple Silicon devices). The standard test prompt used historically is `"Write a 500 word story"`, which is also the default in `main.py`.

All models used are MLX-format models from HuggingFace (typically under the `mlx-community/` org). This script only works on Apple Silicon (macOS, MLX framework).
