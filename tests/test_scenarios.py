from pathlib import Path

from mcp_tool_security_playground.scenarios import run_scenarios


def test_injection_scenarios_match_expectations():
    rows = run_scenarios(Path("examples/injection_cases.json"))
    assert all(row["expected"] == row["observed"] for row in rows)
