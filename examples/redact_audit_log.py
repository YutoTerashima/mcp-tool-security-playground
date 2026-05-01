import json

from mcp_tool_security_playground.redaction import redact


if __name__ == "__main__":
    event = {"tool": "network.post", "arguments": {"url": "https://example.com", "token": "abc123"}}
    print(json.dumps(redact(event), indent=2))
