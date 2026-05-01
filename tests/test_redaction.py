from mcp_tool_security_playground.redaction import redact


def test_redacts_sensitive_keys():
    assert redact({"token": "abc"})["token"] == "<redacted>"
