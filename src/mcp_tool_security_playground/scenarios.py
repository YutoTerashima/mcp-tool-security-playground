from __future__ import annotations

import json
from pathlib import Path

from .policy import ToolPolicy, ToolRequest


DEFAULT_POLICY = ToolPolicy(
    allowed_tools={"calculator.add", "file.read", "kb.search"},
    review_tools={"network.post", "shell.exec"},
    allowed_prefixes=("workspace/public/",),
)


def run_scenarios(path: Path) -> list[dict[str, str]]:
    cases = json.loads(path.read_text(encoding="utf-8"))
    rows: list[dict[str, str]] = []
    for case in cases:
        decision = DEFAULT_POLICY.decide(ToolRequest(case["tool"], case["arguments"]))
        observed = "allow" if decision.allowed else "deny"
        rows.append(
            {
                "case_id": case["case_id"],
                "expected": case["expected"],
                "observed": observed,
                "reason": decision.reason,
            }
        )
    return rows
