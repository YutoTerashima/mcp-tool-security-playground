from mcp_tool_security_playground.audit import audit_requests
from mcp_tool_security_playground.policy import ToolRequest


def test_audit_scores_denied_requests():
    data = audit_requests([ToolRequest("file.read", {"path": "workspace/private/token.txt"})])
    assert data["denied"] == 1
    assert data["max_risk"] >= 3
