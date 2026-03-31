# Inference Speed Tests on Local LLMs

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![GitHub Stars](https://img.shields.io/github/stars/itsmostafa/inference-speed-tests)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/itsmostafa/inference-speed-tests/pulls)

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
# Default prompt: 1 sample from tatsu-lab/alpaca (instruction field)
uv run src/main.py mlx-community/Qwen3-8B-4bit -n 1

# Benchmark multiple models with 3 iterations
uv run src/main.py mlx-community/Qwen3-8B-4bit mlx-community/Qwen3-14B-4bit

# Custom inline prompt, output file, and iteration count
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --prompt "Explain quantum computing" \
  --iterations 5 \
  --output my_results.md

# Multiple inline prompts in one run (results grouped by prompt)
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --prompt "Write a 500 word story" \
  --prompt "Summarize the history of Rome"

# Prompts from files
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --prompt-files prompts/500_word_story.md prompts/summarize-turbo-quant.md

# Sample prompts from a HuggingFace dataset
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --dataset EdinburghNLP/xsum --dataset-field document --dataset-samples 3

# Long-form prompts (CNN/DailyMail articles, ~600–1200 tokens)
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --dataset cnn_dailymail --dataset-config 3.0.0 --dataset-field article

# Reasoning prompts (GSM8K math questions)
uv run src/main.py mlx-community/Qwen3-8B-4bit \
  --dataset gsm8k --dataset-config main --dataset-field question
```

**Dataset flags** (all optional when `--dataset` is set):

| Flag | Default | Description |
|------|---------|-------------|
| `--dataset DATASET_ID` | — | HuggingFace dataset to sample from |
| `--dataset-field FIELD` | — | Column to use as prompt text (required with `--dataset`) |
| `--dataset-config CONFIG` | — | Dataset config/subset (e.g. `3.0.0` for `cnn_dailymail`) |
| `--dataset-split SPLIT` | `train` | Dataset split to sample from |
| `--dataset-samples N` | `1` | Number of samples to draw |
| `--dataset-seed SEED` | `42` | Random seed for reproducible sampling |

**Recommended datasets** for varying prompt lengths:

| Length | Dataset | Config | Field | Avg tokens |
|--------|---------|--------|-------|------------|
| Short (default) | `tatsu-lab/alpaca` | — | `instruction` | ~30–80 |
| Medium | `EdinburghNLP/xsum` | — | `document` | ~200–400 |
| Long | `cnn_dailymail` | `3.0.0` | `article` | ~600–1200 |
| Reasoning | `gsm8k` | `main` | `question` | ~50–200 |

Only a small shuffle buffer (~1000 rows) is downloaded — not the full dataset. Results are cached locally by the `datasets` library, so repeated runs with the same seed skip re-downloading.

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
