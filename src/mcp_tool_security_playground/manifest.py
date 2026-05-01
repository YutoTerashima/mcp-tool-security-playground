from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ToolManifest:
    name: str
    description: str
    read_only: bool
    requires_review: bool
    data_classes: tuple[str, ...]


MANIFESTS = {
    "calculator.add": ToolManifest("calculator.add", "Add two numbers.", True, False, ("none",)),
    "kb.search": ToolManifest("kb.search", "Search public knowledge base.", True, False, ("public",)),
    "file.read": ToolManifest("file.read", "Read allowlisted workspace files.", True, False, ("public", "local_path")),
    "network.post": ToolManifest("network.post", "Send data to a remote endpoint.", False, True, ("network", "egress")),
    "shell.exec": ToolManifest("shell.exec", "Execute local shell command.", False, True, ("execution", "environment")),
}


def capability_matrix() -> list[dict[str, object]]:
    return [manifest.__dict__ for manifest in MANIFESTS.values()]
