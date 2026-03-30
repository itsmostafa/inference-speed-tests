# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the benchmark

```bash
# Single model, 1 iteration
uv run main.py mlx-community/GLM-4.7-Flash-4bit -n 1 -o results.md

# Multiple models, 3 iterations (default), custom output file
uv run main.py mlx-community/Qwen2.5-7B-Instruct-4bit mlx-community/Qwen2.5-14B-Instruct-4bit -o my_results.md

# All options
uv run main.py MODEL_ID [-n ITERATIONS] [-p "inline prompt"] [--prompt-files FILE ...] [--max-tokens N] [-o output.md] [--no-warmup]

# Multiple prompts — --prompt is repeatable; results are grouped by prompt in the output
uv run main.py mlx-community/Qwen2.5-7B-Instruct-4bit \
  -p "Write a 500 word story" -p "Explain quantum computing"

# Prompts from files
uv run main.py mlx-community/Qwen2.5-7B-Instruct-4bit \
  --prompt-files prompts/500_word_story.md prompts/summarize-turbo-quant.md
```

## Architecture

This is a single-script project (`main.py`) with one dependency (`mlx-lm`). All logic lives in `main.py`.

**Benchmark flow:**
1. `main()` → builds the list of `(label, text)` prompt pairs, calls `get_device_info()`, then loops over prompts × models calling `benchmark_model()` for each combination
2. `benchmark_model()` — loads via `mlx_lm.load()`, captures `context_size` from `model.args.max_position_embeddings`, runs a warmup pass, then `n` timed iterations using `mlx_lm.stream_generate()`
3. Metrics come from the final `GenerationResponse` yielded by `stream_generate` (cumulative `prompt_tps`, `generation_tps`, `peak_memory`); TTFT and total time are wall-clock measurements
4. `format_results_markdown()` → groups results by `prompt_label`, writes `## Prompt:` sections each with a summary table and per-iteration details

**Key data types:**
- `IterationResult` — raw metrics for one run
- `ModelResult` — holds `prompt_label`, `context_size`, all iterations, and any error string

**Prompt handling:** `format_prompt()` applies the model's chat template if `tokenizer.chat_template` exists, otherwise falls back to the raw prompt string. The default prompt is loaded from `prompts/500_word_story.md`. Pass `--prompt` (repeatable) for inline strings or `--prompt-files` for file paths; both can be combined.

## Repository context

The `README.md` and `mac mini.md` contain hand-collected benchmark data from community contributors (tokens/s across various Apple Silicon devices). The standard test prompt used historically is `"Write a 500 word story"`, stored in `prompts/500_word_story.md` and used as the default when no `--prompt` or `--prompt-files` flag is provided. Additional prompt files live alongside it in `prompts/`.

All models used are MLX-format models from HuggingFace (typically under the `mlx-community/` org). This script only works on Apple Silicon (macOS, MLX framework).

## After making code changes

Always run `task check` at the end of any coding session to verify tests pass, linting is clean, and types are correct.
