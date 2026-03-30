"""Unit tests for main.py — pure/helper functions only."""

import argparse
from unittest.mock import MagicMock

import pytest

from main import (
    IterationResult,
    ModelResult,
    _fmt,
    _short_name,
    derive_device_folder,
    format_prompt,
    format_results_markdown,
    parse_existing_iterations,
)


# ---------------------------------------------------------------------------
# _fmt
# ---------------------------------------------------------------------------


class TestFmt:
    def test_empty_list_returns_na(self):
        assert _fmt([]) == "N/A"

    def test_single_value_no_stdev(self):
        assert _fmt([42.5]) == "42.50"

    def test_single_value_custom_precision(self):
        assert _fmt([1.0], precision=3) == "1.000"

    def test_multiple_values_mean_and_stdev(self):
        result = _fmt([10.0, 20.0])
        assert "±" in result
        assert "15.00" in result  # mean

    def test_identical_values_zero_stdev(self):
        result = _fmt([5.0, 5.0, 5.0])
        assert "5.00 ± 0.00" == result


# ---------------------------------------------------------------------------
# _short_name
# ---------------------------------------------------------------------------


class TestShortName:
    def test_strips_org_prefix(self):
        assert _short_name("mlx-community/Qwen2.5-7B-Instruct-4bit") == "Qwen2.5-7B-Instruct-4bit"

    def test_no_slash_returns_full_string(self):
        assert _short_name("local-model") == "local-model"

    def test_multiple_slashes_takes_last_segment(self):
        assert _short_name("a/b/c") == "c"


# ---------------------------------------------------------------------------
# derive_device_folder
# ---------------------------------------------------------------------------


class TestDeriveDeviceFolder:
    def _info(self, model_name, chip, memory_gb, gpu_cores):
        return {
            "model_name": model_name,
            "chip": chip,
            "memory_gb": memory_gb,
            "gpu_cores": gpu_cores,
        }

    def test_typical_macbook_pro(self):
        info = self._info("MacBook Pro", "Apple M4 Max", 128, "40")
        result = derive_device_folder(info)
        assert result == "macbook-pro-m4-max-128gb-40-core-gpu"

    def test_mac_mini(self):
        info = self._info("Mac mini", "Apple M2", 16, "10")
        result = derive_device_folder(info)
        assert result == "mac-mini-m2-16gb-10-core-gpu"

    def test_unknown_memory(self):
        info = self._info("MacBook Pro", "Apple M1", "Unknown", "8")
        result = derive_device_folder(info)
        assert "unknown-ram" in result

    def test_unknown_gpu(self):
        info = self._info("MacBook Pro", "Apple M1", 16, "Unknown")
        result = derive_device_folder(info)
        assert "unknown-gpu" in result

    def test_lowercase_and_hyphenated(self):
        info = self._info("MacBook Air", "Apple M3", 24, "18")
        result = derive_device_folder(info)
        assert result == "macbook-air-m3-24gb-18-core-gpu"


# ---------------------------------------------------------------------------
# format_prompt
# ---------------------------------------------------------------------------


class TestFormatPrompt:
    def test_uses_chat_template_when_available(self):
        tokenizer = MagicMock()
        tokenizer.chat_template = "<template>"
        tokenizer.apply_chat_template.return_value = "<formatted>"
        result = format_prompt(tokenizer, "hello")
        assert result == "<formatted>"
        tokenizer.apply_chat_template.assert_called_once_with(
            [{"role": "user", "content": "hello"}],
            add_generation_prompt=True,
            tokenize=False,
        )

    def test_falls_back_to_raw_prompt_when_no_chat_template(self):
        tokenizer = MagicMock()
        tokenizer.chat_template = None
        result = format_prompt(tokenizer, "raw prompt")
        assert result == "raw prompt"

    def test_falls_back_on_template_exception(self):
        tokenizer = MagicMock()
        tokenizer.chat_template = "<template>"
        tokenizer.apply_chat_template.side_effect = Exception("oops")
        result = format_prompt(tokenizer, "fallback")
        assert result == "fallback"

    def test_falls_back_when_tokenizer_lacks_attribute(self):
        tokenizer = object()  # no apply_chat_template attribute
        result = format_prompt(tokenizer, "raw")
        assert result == "raw"


# ---------------------------------------------------------------------------
# parse_existing_iterations
# ---------------------------------------------------------------------------


def _make_markdown(model_short_name: str, prompt_label: str, rows: list[tuple]) -> str:
    """Build a minimal results markdown string with iteration rows."""
    lines = [
        f"## Prompt: `{prompt_label}`",
        "",
        f"#### {model_short_name}",
        "",
        "| Run | Prompt tps | Generation tps | TTFT (s) | Peak Memory (GB) | Total Time (s) |",
        "| --- | ---------- | -------------- | -------- | ---------------- | -------------- |",
    ]
    for i, (ptps, gtps, ttft, mem, total) in enumerate(rows, 1):
        lines.append(f"| {i} | {ptps} | {gtps} | {ttft} | {mem} | {total} |")
    lines.append("")
    return "\n".join(lines)


class TestParseExistingIterations:
    def test_returns_empty_for_missing_file(self, tmp_path):
        result = parse_existing_iterations(tmp_path / "missing.md", "org/model", "my-prompt")
        assert result == []

    def test_parses_single_iteration(self, tmp_path):
        md = _make_markdown("model", "my-prompt", [(100.0, 50.0, 0.123, 4.50, 10.00)])
        path = tmp_path / "results.md"
        path.write_text(md)

        iters = parse_existing_iterations(path, "org/model", "my-prompt")
        assert len(iters) == 1
        assert iters[0].prompt_tps == 100.0
        assert iters[0].generation_tps == 50.0
        assert iters[0].time_to_first_token == pytest.approx(0.123)
        assert iters[0].peak_memory_gb == 4.50
        assert iters[0].total_time == 10.00

    def test_parses_multiple_iterations(self, tmp_path):
        rows = [(100.0, 50.0, 0.1, 4.0, 9.0), (110.0, 55.0, 0.2, 4.1, 9.5)]
        md = _make_markdown("model", "prompt", rows)
        path = tmp_path / "results.md"
        path.write_text(md)

        iters = parse_existing_iterations(path, "org/model", "prompt")
        assert len(iters) == 2
        assert iters[1].generation_tps == 55.0

    def test_returns_empty_for_wrong_prompt_label(self, tmp_path):
        md = _make_markdown("model", "correct-prompt", [(100.0, 50.0, 0.1, 4.0, 9.0)])
        path = tmp_path / "results.md"
        path.write_text(md)

        iters = parse_existing_iterations(path, "org/model", "wrong-prompt")
        assert iters == []

    def test_returns_empty_for_wrong_model(self, tmp_path):
        md = _make_markdown("other-model", "prompt", [(100.0, 50.0, 0.1, 4.0, 9.0)])
        path = tmp_path / "results.md"
        path.write_text(md)

        iters = parse_existing_iterations(path, "org/my-model", "prompt")
        assert iters == []


# ---------------------------------------------------------------------------
# format_results_markdown
# ---------------------------------------------------------------------------


def _make_iter(**kwargs) -> IterationResult:
    return IterationResult(
        prompt_tokens=int(kwargs.get("prompt_tokens", 10)),
        generation_tokens=int(kwargs.get("generation_tokens", 100)),
        prompt_tps=float(kwargs.get("prompt_tps", 500.0)),
        generation_tps=float(kwargs.get("generation_tps", 50.0)),
        peak_memory_gb=float(kwargs.get("peak_memory_gb", 4.0)),
        time_to_first_token=float(kwargs.get("time_to_first_token", 0.1)),
        total_time=float(kwargs.get("total_time", 2.0)),
    )


def _make_args(**kwargs) -> argparse.Namespace:
    defaults = dict(max_tokens=512, iterations=3)
    defaults.update(kwargs)
    return argparse.Namespace(**defaults)


class TestFormatResultsMarkdown:
    def test_contains_header(self):
        device_info = {"chip": "Apple M4", "memory_gb": 16, "gpu_cores": "10", "os": "macOS"}
        result = ModelResult(
            model_id="org/MyModel", prompt_label="my-prompt", iterations=[_make_iter()]
        )
        md = format_results_markdown(device_info, [result], _make_args())
        assert "# Inference Speed Test Results" in md

    def test_contains_device_info(self):
        device_info = {"chip": "Apple M4 Max", "memory_gb": 128, "gpu_cores": "40", "os": "macOS-15"}
        result = ModelResult(
            model_id="org/MyModel", prompt_label="p", iterations=[_make_iter()]
        )
        md = format_results_markdown(device_info, [result], _make_args())
        assert "Apple M4 Max" in md
        assert "128 GB" in md
        assert "40-core GPU" in md

    def test_contains_model_short_name(self):
        device_info = {"chip": "Apple M1", "memory_gb": 16, "gpu_cores": "8", "os": "macOS"}
        result = ModelResult(
            model_id="mlx-community/Qwen2.5-7B-Instruct-4bit",
            prompt_label="p",
            iterations=[_make_iter()],
        )
        md = format_results_markdown(device_info, [result], _make_args())
        assert "Qwen2.5-7B-Instruct-4bit" in md

    def test_failed_model_shows_error(self):
        device_info = {"chip": "Apple M1", "memory_gb": 8, "gpu_cores": "7", "os": "macOS"}
        result = ModelResult(
            model_id="org/BadModel", prompt_label="p", iterations=[], error="load failed"
        )
        md = format_results_markdown(device_info, [result], _make_args())
        assert "FAILED" in md
        assert "load failed" in md

    def test_multiple_prompts_grouped(self):
        device_info = {"chip": "Apple M2", "memory_gb": 16, "gpu_cores": "10", "os": "macOS"}
        r1 = ModelResult(model_id="org/M", prompt_label="prompt-a", iterations=[_make_iter()])
        r2 = ModelResult(model_id="org/M", prompt_label="prompt-b", iterations=[_make_iter()])
        md = format_results_markdown(device_info, [r1, r2], _make_args())
        assert "prompt-a" in md
        assert "prompt-b" in md

    def test_iteration_count_displayed(self):
        device_info = {"chip": "Apple M3", "memory_gb": 24, "gpu_cores": "18", "os": "macOS"}
        iters = [_make_iter(), _make_iter(), _make_iter()]
        result = ModelResult(model_id="org/M", prompt_label="p", iterations=iters)
        md = format_results_markdown(device_info, [result], _make_args(iterations=3))
        assert "**Iterations**: 3" in md
