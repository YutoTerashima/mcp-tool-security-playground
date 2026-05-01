from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ToolRequest:
    name: str
    arguments: dict[str, str]


@dataclass(frozen=True)
class Decision:
    allowed: bool
    reason: str


class ToolPolicy:
    def __init__(self, allowed_tools: set[str], review_tools: set[str], allowed_prefixes: tuple[str, ...]):
        self.allowed_tools = allowed_tools
        self.review_tools = review_tools
        self.allowed_prefixes = allowed_prefixes

    def decide(self, request: ToolRequest) -> Decision:
        if request.name in self.review_tools:
            return Decision(False, "tool requires human review")
        if request.name not in self.allowed_tools:
            return Decision(False, "tool is not allowlisted")
        path = request.arguments.get("path")
        if path and not path.startswith(self.allowed_prefixes):
            return Decision(False, "outside allowed path")
        return Decision(True, "policy passed")
