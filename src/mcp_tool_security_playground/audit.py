from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

from .policy import Decision, ToolRequest
from .scenarios import DEFAULT_POLICY


IMPACT = {
    "calculator.add": 0,
    "kb.search": 1,
    "file.read": 2,
    "network.post": 3,
    "shell.exec": 4,
}


@dataclass(frozen=True)
class AuditRecord:
    tool: str
    allowed: bool
    reason: str
    impact: int
    risk: int


def audit_request(request: ToolRequest, decision: Decision) -> AuditRecord:
    impact = IMPACT.get(request.name, 2)
    risk = impact if decision.allowed else max(1, impact - 1)
    if "outside allowed path" in decision.reason:
        risk += 2
    if "human review" in decision.reason:
        risk += 1
    return AuditRecord(request.name, decision.allowed, decision.reason, impact, risk)


def audit_requests(requests: list[ToolRequest]) -> dict[str, object]:
    records = [audit_request(request, DEFAULT_POLICY.decide(request)) for request in requests]
    reasons = Counter(record.reason for record in records)
    return {
        "records": [record.__dict__ for record in records],
        "denied": sum(not record.allowed for record in records),
        "max_risk": max((record.risk for record in records), default=0),
        "reasons": dict(sorted(reasons.items())),
    }
