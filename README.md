# Inference Speed Tests on Local LLMs

Inference speed tests on Local Large Language Models on various devices. Feel free to contribute your results.

**Note**: None of the following results are verified

All models have been tested with the following Prompt: `Write a 500 word story`

### Macbook Pro

#### Ollama

| GGUF models        | M4 Max (128 GB RAM, 40-core GPU) | M1 Pro (32GB RAM, 16-core GPU) |
| ------------------ | -------------------------------- | ------------------------------ |
| Qwen2.5:7B (4bit)  | 72.50 tokens/s                   | 26.85 tokens/s                 |
| Qwen2.5:14B (4bit) | 38.23 tokens/s                   | 14.66 tokens/s                 |
| Qwen2.5:32B (4bit) | 19.35 tokens/s                   | 6.95 tokens/s                  |
| Qwen2.5:72B (4bit) | 8.76 tokens/s                    | Didn't Test                    |

#### LM Studio

| MLX models                  | M4 Max (128 GB RAM, 40-core GPU) | M1 Pro (32GB RAM, 16-core GPU) |
| --------------------------- | -------------------------------- | ------------------------------ |
| Qwen2.5-7B-Instruct (4bit)  | 101.87 tokens/s                  | 38.99 tokens/s                 |
| Qwen2.5-14B-Instruct (4bit) | 52.22 tokens/s                   | 18.88 tokens/s                 |
| Qwen2.5-32B-Instruct (4bit) | 24.46 tokens/s                   | 9.10 tokens/s                  |
| Qwen2.5-32B-Instruct (8bit) | 13.75 tokens/s                   | Won’t Complete (Crashed)       |
| Qwen2.5-72B-Instruct (4bit) | 10.86 tokens/s                   | Didn't Test                    |

| GGUF models                 | M4 Max (128 GB RAM, 40-core GPU) | M1 Pro (32GB RAM, 16-core GPU) |
| --------------------------- | -------------------------------- | ------------------------------ |
| Qwen2.5-7B-Instruct (4bit)  | 71.73 tokens/s                   | 26.12 tokens/s                 |
| Qwen2.5-14B-Instruct (4bit) | 39.04 tokens/s                   | 14.67 tokens/s                 |
| Qwen2.5-32B-Instruct (4bit) | 19.56 tokens/s                   | 4.53 tokens/s                  |
| Qwen2.5-72B-Instruct (4bit) | 8.31 tokens/s                    | Didn't Test                    |
