from __future__ import annotations

"""Report metadata for the mature portfolio iteration."""

PROJECT_TITLE = 'MCP Tool Security Playground'
RESEARCH_PROBLEM = 'How should an agent route tool calls when prompt injection, tool risk, and overblocking costs interact?'
DATASET_SUMMARY = 'S-Labs prompt-injection train, validation, and test splits with 15,291 prompts.'
TAKEAWAYS = ['Detector-based routing strongly outperforms static policy on real prompt-injection data.', 'Hybrid routing increases unsafe recall but creates measurable benign-pass-rate cost.', 'Attack perturbations expose the difference between secure routing and indiscriminate blocking.']
NEXT_EXPERIMENTS = ['Add MCP server integration smoke tests with real tool manifests.', 'Introduce path traversal and prompt-leak attack scenarios as first-class test cases.', 'Benchmark review queues separately from hard deny routes.']


def report_outline() -> list[str]:
    return [
        "Abstract",
        "Research question",
        "Dataset card",
        "Methods",
        "Experiment matrix",
        "Results",
        "Ablations",
        "Failure analysis",
        "Engineering notes",
        "Limitations",
        "Reproduction",
    ]


def maturity_claims() -> dict[str, object]:
    return {
        "title": PROJECT_TITLE,
        "problem": RESEARCH_PROBLEM,
        "dataset": DATASET_SUMMARY,
        "takeaways": TAKEAWAYS,
        "next_experiments": NEXT_EXPERIMENTS,
    }
