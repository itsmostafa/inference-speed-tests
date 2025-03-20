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

### Mac Studio

#### Ollama

| GGUF models               | M1 Max (32GB RAM, 23-core GPU) | M3 Ultra (256GB, 80-core GPU) |
| ------------------------- | ------------------------------ | ----------------------------- |
| mistral-small:23b (4bit)  | 15.11 tokens/s                 | Didn't Test                   |
| mistral-large:123b (4bit) | Didn't Test                    | 8.42 tokens/s                 |
| llama3.1:8b (4bit)        | 38.73 tokens/s                 | 85.02 tokens/s                |
| llama3.2-vision:9b (4bit) | 39.05 tokens/s                 | Didn't Test                   |
| deepseek-r1:14b (4bit)    | 21.16 tokens/s                 | 46.50 tokens/s                |
| deepseek-r1:32b (4bit)    | Didn't Test                    | 25.58 tokens/s                |
| deepseek-r1:70b (4bit)    | Didn't Test                    | 13.16 tokens/s                |
| hermes3:405b (4bit)       | Didn't Test                    | 2.47 tokens/s                 |
| Qwen2.5:7B (4bit)         | Didn't Test                    | 88.87 tokens/s                |
| Qwen2.5:14B (4bit)        | Didn't Test                    | 47.25 tokens/s                |
| Qwen2.5:32B (4bit)        | Didn't Test                    | 26.02 tokens/s                |
| Qwen2.5:70B (4bit)        | Didn't Test                    | 12.21 tokens/s                |

## Contributing

### Using Ollama

1. Run your model with the verbose flag (e.g `ollama run mistral-small --verbose`)
2. Enter the prompt `Write a 500 word story`
3. In the column of your device add the TPS (tokens-per-second) output of `eval rate` in Ollama
4. If your device is not in the list add it
