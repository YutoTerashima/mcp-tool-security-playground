from mcp_tool_security_playground.mock_server import demo


def test_policy_demo_denies_risky_tools():
    lines = demo()
    assert any(line.startswith("allow calculator.add") for line in lines)
    assert any("outside allowed path" in line for line in lines)
    assert any("human review" in line for line in lines)
