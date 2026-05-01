from pathlib import Path

from mcp_tool_security_playground.scenarios import run_scenarios


if __name__ == "__main__":
    rows = run_scenarios(Path("examples/injection_cases.json"))
    for row in rows:
        print(row["case_id"], row["observed"], row["reason"])
