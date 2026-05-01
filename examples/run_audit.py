from mcp_tool_security_playground.audit import audit_requests
from mcp_tool_security_playground.policy import ToolRequest


if __name__ == "__main__":
    data = audit_requests(
        [
            ToolRequest("kb.search", {"query": "agent safety"}),
            ToolRequest("file.read", {"path": "workspace/private/token.txt"}),
            ToolRequest("network.post", {"url": "https://example.com"}),
            ToolRequest("shell.exec", {"command": "whoami"}),
        ]
    )
    print(data)
