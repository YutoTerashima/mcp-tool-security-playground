from __future__ import annotations

from .manifest import MANIFESTS


def classify_threat(tool: str, arguments: dict[str, str]) -> list[str]:
    manifest = MANIFESTS.get(tool)
    labels: list[str] = []
    if manifest is None:
        return ["unknown-capability"]
    if manifest.requires_review:
        labels.append("human-review-required")
    if "egress" in manifest.data_classes:
        labels.append("data-egress")
    if "execution" in manifest.data_classes:
        labels.append("code-execution")
    path = arguments.get("path", "")
    if path and "private" in path:
        labels.append("sensitive-path")
    return labels or ["low-risk"]
