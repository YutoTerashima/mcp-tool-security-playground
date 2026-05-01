from __future__ import annotations

from .policy import ToolPolicy, ToolRequest


def run_requests(policy: ToolPolicy, requests: list[ToolRequest]) -> list[str]:
    lines: list[str] = []
    for request in requests:
        decision = policy.decide(request)
        verdict = "allow" if decision.allowed else "deny"
        lines.append(f"{verdict} {request.name}: {decision.reason}")
    return lines


def demo() -> list[str]:
    policy = ToolPolicy(
        allowed_tools={"calculator.add", "file.read", "kb.search"},
        review_tools={"network.post", "shell.exec"},
        allowed_prefixes=("workspace/public/",),
    )
    requests = [
        ToolRequest("calculator.add", {"a": "2", "b": "3"}),
        ToolRequest("file.read", {"path": "workspace/private/token.txt"}),
        ToolRequest("network.post", {"url": "https://example.com"}),
    ]
    return run_requests(policy, requests)
