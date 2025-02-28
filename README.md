# inference-speed-tests

Local LLM inference speed tests on various devices

### Macbook Pro

| GGUF models (Ollama) | M4 Max (128 GB RAM, 40-core GPU) | M1 Pro (32GB RAM, 16-core GPU) |
| -------------------- | -------------------------------- | ------------------------------ |
| Qwen2.5:7B (4bit)    | 72.50 tokens/s                   | 26.85 tokens/s                 |
| Qwen2.5:14B (4bit)   | 38.23 tokens/s                   | 14.66 tokens/s                 |
| Qwen2.5:32B (4bit)   | 19.35 tokens/s                   | 6.95 tokens/s                  |
| Qwen2.5:72B (4bit)   | 8.76 tokens/s                    | Didn't Test                    |
