from mcp_tool_security_playground.manifest import capability_matrix
from mcp_tool_security_playground.threats import classify_threat


def test_manifest_and_threat_labels():
    assert any(row["name"] == "network.post" for row in capability_matrix())
    assert "data-egress" in classify_threat("network.post", {"url": "https://example.com"})
    assert "sensitive-path" in classify_threat("file.read", {"path": "workspace/private/token.txt"})
