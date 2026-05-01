import json
from collections import Counter
from pathlib import Path

rows = [json.loads(line) for line in Path("datasets/external/prompt_injection_sample.jsonl").read_text(encoding="utf-8").splitlines()]
print({"rows": len(rows), "labels": Counter(row["label"] for row in rows), "with_patterns": sum(bool(row["pattern_hits"]) for row in rows)})
