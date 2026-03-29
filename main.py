import argparse
import gc
import platform
import re
import statistics
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from mlx_lm import load, stream_generate

DEFAULT_PROMPT = "Write a 500 word story"
DEFAULT_MAX_TOKENS = 512
DEFAULT_ITERATIONS = 3


@dataclass
class IterationResult:
    prompt_tokens: int
    generation_tokens: int
    prompt_tps: float
    generation_tps: float
    peak_memory_gb: float
    time_to_first_token: float
    total_time: float


@dataclass
class ModelResult:
    model_id: str
    iterations: list[IterationResult] = field(default_factory=list)
    error: str | None = None


def get_device_info() -> dict:
    info = {}

    def sysctl(key):
        try:
            return subprocess.check_output(["sysctl", "-n", key], text=True).strip()
        except Exception:
            return "Unknown"

    info["chip"] = sysctl("machdep.cpu.brand_string")

    try:
        mem_bytes = int(sysctl("hw.memsize"))
        info["memory_gb"] = mem_bytes // (1024**3)
    except Exception:
        info["memory_gb"] = "Unknown"

    try:
        sp_output = subprocess.check_output(
            ["system_profiler", "SPDisplaysDataType"], text=True
        )
        gpu_cores = "Unknown"
        for line in sp_output.splitlines():
            if "Total Number of Cores" in line:
                gpu_cores = line.split(":")[-1].strip()
                break
        info["gpu_cores"] = gpu_cores
    except Exception:
        info["gpu_cores"] = "Unknown"

    try:
        sp_hw = subprocess.check_output(
            ["system_profiler", "SPHardwareDataType"], text=True
        )
        model_name = "Unknown"
        for line in sp_hw.splitlines():
            if "Model Name" in line:
                model_name = line.split(":")[-1].strip()
                break
        info["model_name"] = model_name
    except Exception:
        info["model_name"] = "Unknown"

    info["os"] = platform.platform()
    return info


def derive_device_folder(device_info: dict) -> str:
    model_name = device_info.get("model_name", "Unknown")
    chip = device_info.get("chip", "Unknown")
    memory_gb = device_info.get("memory_gb", "Unknown")
    gpu_cores = device_info.get("gpu_cores", "Unknown")

    # "MacBook Pro" → "macbook-pro", "Mac mini" → "mac-mini"
    model_slug = re.sub(r"\s+", "-", model_name.strip()).lower()

    # "Apple M5 Max" → "m5-max"
    chip_slug = re.sub(r"^apple\s+", "", chip.strip(), flags=re.IGNORECASE)
    chip_slug = re.sub(r"\s+", "-", chip_slug).lower()

    ram_part = f"{memory_gb}gb" if isinstance(memory_gb, int) else "unknown-ram"
    gpu_part = f"{gpu_cores}-core-gpu" if gpu_cores != "Unknown" else "unknown-gpu"

    return f"{model_slug}-{chip_slug}-{ram_part}-{gpu_part}"


def format_prompt(tokenizer, prompt: str) -> str:
    if hasattr(tokenizer, "apply_chat_template") and tokenizer.chat_template:
        try:
            messages = [{"role": "user", "content": prompt}]
            return tokenizer.apply_chat_template(
                messages, add_generation_prompt=True, tokenize=False
            )
        except Exception:
            pass
    return prompt


def benchmark_model(
    model_id: str,
    prompt: str,
    max_tokens: int,
    iterations: int,
    warmup: bool,
) -> ModelResult:
    result = ModelResult(model_id=model_id)

    print(f"\n[{model_id}] Loading...", file=sys.stderr)
    try:
        model, tokenizer = load(model_id, tokenizer_config={"trust_remote_code": True})
    except Exception as e:
        result.error = str(e)
        print(f"[{model_id}] Load failed: {e}", file=sys.stderr)
        return result

    formatted = format_prompt(tokenizer, prompt)

    if warmup:
        print(f"[{model_id}] Warming up...", file=sys.stderr)
        try:
            for _ in stream_generate(model, tokenizer, formatted, max_tokens=64):
                pass
        except Exception:
            pass

    for i in range(iterations):
        print(f"[{model_id}] Iteration {i + 1}/{iterations}...", file=sys.stderr)
        try:
            t_start = time.perf_counter()
            t_first = None
            response = None

            for response in stream_generate(
                model, tokenizer, formatted, max_tokens=max_tokens
            ):
                if t_first is None:
                    t_first = time.perf_counter()

            t_end = time.perf_counter()

            if response is None:
                print(f"[{model_id}] No tokens generated in iteration {i + 1}", file=sys.stderr)
                continue

            iter_result = IterationResult(
                prompt_tokens=response.prompt_tokens,
                generation_tokens=response.generation_tokens,
                prompt_tps=response.prompt_tps,
                generation_tps=response.generation_tps,
                peak_memory_gb=response.peak_memory,
                time_to_first_token=(t_first - t_start) if t_first else 0.0,
                total_time=t_end - t_start,
            )
            result.iterations.append(iter_result)
            print(
                f"[{model_id}] Iter {i + 1}: "
                f"gen_tps={iter_result.generation_tps:.1f}, "
                f"ttft={iter_result.time_to_first_token:.3f}s, "
                f"peak_mem={iter_result.peak_memory_gb:.2f}GB",
                file=sys.stderr,
            )
        except Exception as e:
            print(f"[{model_id}] Iteration {i + 1} failed: {e}", file=sys.stderr)
            if not result.iterations:
                result.error = str(e)

    del model, tokenizer
    gc.collect()
    return result


def _fmt(vals: list[float], precision: int = 2) -> str:
    if not vals:
        return "N/A"
    if len(vals) == 1:
        return f"{vals[0]:.{precision}f}"
    mean = statistics.mean(vals)
    stdev = statistics.stdev(vals)
    return f"{mean:.{precision}f} ± {stdev:.{precision}f}"


def _short_name(model_id: str) -> str:
    return model_id.split("/")[-1]


def format_results_markdown(
    device_info: dict,
    results: list[ModelResult],
    args: argparse.Namespace,
) -> str:
    lines = []

    chip = device_info.get("chip", "Unknown")
    mem = device_info.get("memory_gb", "Unknown")
    gpu = device_info.get("gpu_cores", "Unknown")
    os_str = device_info.get("os", "Unknown")
    mem_str = f"{mem} GB" if isinstance(mem, int) else mem
    gpu_str = f"{gpu}-core GPU" if gpu != "Unknown" else "Unknown GPU"

    lines.append("# Inference Speed Test Results\n")
    lines.append(f"**Date**: {date.today()}")
    lines.append(f"**Device**: {chip} | {mem_str} RAM | {gpu_str}")
    lines.append(f"**OS**: {os_str}")
    lines.append(f"**Prompt**: `{args.prompt}`")
    lines.append(f"**Max tokens**: {args.max_tokens} | **Iterations**: {args.iterations}")
    lines.append("")

    lines.append("## Summary\n")
    header = "| Model | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |"
    sep =    "| ----- | ---------- | -------------- | -------- | ---------------- | -------------- |"
    lines.append(header)
    lines.append(sep)

    for r in results:
        name = _short_name(r.model_id)
        if r.error and not r.iterations:
            lines.append(f"| {name} | FAILED: {r.error} | | | | |")
            continue
        iters = r.iterations
        lines.append(
            f"| {name} "
            f"| {_fmt([i.prompt_tps for i in iters])} "
            f"| {_fmt([i.generation_tps for i in iters])} "
            f"| {_fmt([i.time_to_first_token for i in iters], 3)} "
            f"| {_fmt([i.peak_memory_gb for i in iters])} "
            f"| {_fmt([i.total_time for i in iters])} |"
        )

    lines.append("")
    lines.append("## Per-Iteration Details\n")

    for r in results:
        name = _short_name(r.model_id)
        lines.append(f"### {name}\n")
        if r.error and not r.iterations:
            lines.append(f"**Error**: {r.error}\n")
            continue
        lines.append("| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |")
        lines.append("| --- | ---------- | -------------- | -------- | ---------------- | -------------- |")
        for n, it in enumerate(r.iterations, 1):
            lines.append(
                f"| {n} "
                f"| {it.prompt_tps:.2f} "
                f"| {it.generation_tps:.2f} "
                f"| {it.time_to_first_token:.3f} "
                f"| {it.peak_memory_gb:.2f} "
                f"| {it.total_time:.2f} |"
            )
        lines.append("")

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Benchmark MLX-LM inference speed across multiple models."
    )
    parser.add_argument(
        "models",
        nargs="+",
        help="HuggingFace MLX model IDs (e.g. mlx-community/Qwen2.5-7B-Instruct-4bit)",
    )
    parser.add_argument(
        "--prompt", "-p",
        default=DEFAULT_PROMPT,
        help=f'Prompt string (default: "{DEFAULT_PROMPT}")',
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help=f"Max tokens to generate (default: {DEFAULT_MAX_TOKENS})",
    )
    parser.add_argument(
        "--iterations", "-n",
        type=int,
        default=DEFAULT_ITERATIONS,
        help=f"Timed runs per model (default: {DEFAULT_ITERATIONS})",
    )
    parser.add_argument(
        "--output", "-o",
        default="results.md",
        help="Output markdown file path (default: results.md)",
    )
    parser.add_argument(
        "--no-warmup",
        action="store_true",
        help="Skip warmup run before timed iterations",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print("Collecting device info...", file=sys.stderr)
    device_info = get_device_info()
    gpu = device_info.get("gpu_cores", "Unknown")
    print(
        f"Device: {device_info.get('model_name')} | "
        f"{device_info.get('chip')} | "
        f"{device_info.get('memory_gb')} GB | "
        f"{gpu}-core GPU",
        file=sys.stderr,
    )

    # Place output in the device folder unless the user specified a directory
    output_path = Path(args.output)
    if not output_path.parent.name or output_path.parent == Path("."):
        device_folder = Path(derive_device_folder(device_info))
        device_folder.mkdir(parents=True, exist_ok=True)
        output_path = device_folder / output_path.name
    print(f"Output path: {output_path}", file=sys.stderr)

    results: list[ModelResult] = []
    try:
        for model_id in args.models:
            result = benchmark_model(
                model_id=model_id,
                prompt=args.prompt,
                max_tokens=args.max_tokens,
                iterations=args.iterations,
                warmup=not args.no_warmup,
            )
            results.append(result)
    except KeyboardInterrupt:
        print("\nInterrupted — writing partial results...", file=sys.stderr)

    if not results or all(r.error and not r.iterations for r in results):
        print("No successful results to write.", file=sys.stderr)
        return

    markdown = format_results_markdown(device_info, results, args)
    with open(output_path, "w") as f:
        f.write(markdown)

    print(f"\nResults written to {output_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
