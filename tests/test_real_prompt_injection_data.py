import json
from pathlib import Path


def test_real_prompt_injection_sample_has_labels_and_patterns():
    rows = [json.loads(line) for line in Path("datasets/external/prompt_injection_sample.jsonl").read_text(encoding="utf-8").splitlines()]
    assert len(rows) >= 300
    assert len({row["label"] for row in rows}) >= 2
    assert any(row["pattern_hits"] for row in rows)
