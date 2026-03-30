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
# Benchmark a single model (1 iteration)
uv run src/main.py mlx-community/Qwen3-8B-4bit -n 1

# Benchmark multiple models with 3 iterations
uv run src/main.py mlx-community/Qwen3-8B-4bit mlx-community/Qwen3-14B-4bit

# Custom prompt, output file, and iteration count
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --prompt "Explain quantum computing" \
  --iterations 5 \
  --output my_results.md

# Multiple prompts in one run (results grouped by prompt)
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --prompt "Write a 500 word story" \
  --prompt "Summarize the history of Rome"

# Prompts from files
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --prompt-files prompts/500_word_story.md prompts/summarize-turbo-quant.md
```

Results are written as a Markdown file grouped by prompt, each with a summary table (mean ± stdev across iterations) and per-iteration details including model context size, prompt tps, generation tps, time-to-first-token, peak memory, and total time.

Results are automatically saved into a device-specific folder under `results/`, derived from your Mac model, chip, RAM, and GPU core count — for example:

```
results/macbook-pro-m5-max-128gb-40-core-gpu/
results/mac-mini-m4-pro-64gb-20-core-gpu/
```

This keeps results from different machines organized without any manual effort. To override the output location, pass a path that includes a directory to `-o` (e.g. `--output my-folder/results.md`).

## Contributing

Everyone is welcome and encouraged to contribute their benchmark results. The more devices represented, the more useful this becomes for the community.

**To submit your results:**

1. Fork this repo and clone it locally
2. Run the benchmark script on your machine (see above) — results will be saved into a device-specific folder automatically
3. Open a pull request with your new folder added to the repo

That's it. No special format required — just run the script and submit the output as-is.

If you're running models manually or on non-Apple-Silicon hardware, feel free to add results in whatever format makes sense. Open a PR or an issue and we'll figure it out.
