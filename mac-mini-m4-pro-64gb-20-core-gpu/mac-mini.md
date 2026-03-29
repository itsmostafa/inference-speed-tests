Tests were done in the working environment(a couple of browsers with a lot of tabs, vscode, etc.)

Spec:
* Mac mini 2024
* M4 Pro (14 cores{10 perfomance + 4 efficiency})
* GPU: 20 cores
* Memory: 64 GB
* Storage: 1TB

prompt : `Write a 500 word story`


ollama spec:
* version: 0.5.12

ollama run {model_name} --verbose

models:
| name | model ref | quant | eval rate token/s |
| --- | --- | --- | --- |
|qwen2.5:7b | ollama pull qwen2.5:7b | 4bit | 37.25 |
|qwen2.5:14b | ollama pull qwen2.5:14b| 4bit | 19.97 |
|qwen2.5:32b | ollama pull qwen2.5:32b| 4bit | 10.3 |
|qwen2.5:72b | ollama pull qwen2.5:72b| 4bit | 4.61 |



lmstudio spec:
* version: 0.3.10 (build 6)
* metal llama cpp: 1.17.1
* lm studio mlx: 0.8.0

models:
| name | model ref | type | quant | token/s |
| --- | --- | --- | --- | --- |
| Qwen2.5-7B-Instruct | lmstudio-community/Qwen2.5-7B-Instruct-MLX-4bit | MLX | 4bit | 53.63 |
| Qwen2.5-14B-Instruct | lmstudio-community/Qwen2.5-14B-Instruct-MLX-4bit | MLX | 4bit | 26.7 |
| Qwen2.5-32B-Instruct | lmstudio-community/Qwen2.5-32B-Instruct-MLX-4bit | MLX | 4bit | 12.14 |
| Qwen2.5-32B-Instruct | lmstudio-community/Qwen2.5-32B-Instruct-MLX-8bit | MLX | 8bit | 6.58 |
| Qwen2.5-72B-Instruct | mlx-community/Qwen2.5-72B-Instruct-4bit | MLX | 4bit | 5.47 |
| Qwen2.5-7B-Instruct | lmstudio-community/Qwen2.5-7B-Instruct-GGUF/Qwen2.5-7B-Instruct-Q4_K_M.gguf | GGUF | 4bit | 42.74 |
| Qwen2.5-14B-Instruct | lmstudio-community/Qwen2.5-14B-Instruct-GGUF/Qwen2.5-14B-Instruct-Q4_K_M.gguf | GGUF | 4bit | 21.76 |
| Qwen2.5-32B-Instruct | lmstudio-community/Qwen2.5-32B-Instruct-GGUF/Qwen2.5-32B-Instruct-Q4_K_M.gguf | GGUF | 4bit | 10.19 |
| Qwen2.5-32B-Instruct | lmstudio-community/Qwen2.5-32B-Instruct-GGUF/Qwen2.5-32B-Instruct-Q8_0.gguf | GGUF | 8bit | 5.97 |
| Qwen2.5-72B-Instruct | lmstudio-community/Qwen2.5-72B-Instruct-GGUF/Qwen2.5-72B-Instruct-Q4_K_M.gguf | GGUF | 4bit | 3.92 |