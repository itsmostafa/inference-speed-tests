# Inference Speed Tests on Local LLMs

Inference speed tests on Local Large Language Models on various devices. Feel free to contribute your results.

**Note**: None of the following results are verified

## Automated Benchmarking (mlx-lm)

Run reproducible benchmarks on your Apple Silicon Mac using the included script.

**Requirements**: macOS with Apple Silicon, [uv](https://docs.astral.sh/uv/)

```bash
# Clone and install dependencies
git clone https://github.com/itsmostafa/inference-speed-tests
cd inference-speed-tests
uv sync
```

```bash
# Benchmark a single model (1 iteration, saves to results.md)
uv run python main.py mlx-community/Qwen2.5-7B-Instruct-4bit -n 1

# Benchmark multiple models with 3 iterations
uv run python main.py mlx-community/Qwen2.5-7B-Instruct-4bit mlx-community/Qwen2.5-14B-Instruct-4bit

# Custom prompt, output file, and iteration count
uv run python main.py mlx-community/Qwen2.5-32B-Instruct-4bit \
  --prompt "Write a 500 word story" \
  --iterations 5 \
  --output my_results.md
```

Results are written as a Markdown file with a summary table (mean ± stdev across iterations) and per-iteration details including prompt tps, generation tps, time-to-first-token, peak memory, and total time.
