# MCP Tool Security Playground V2 Research Report

## Abstract

This V2 upgrade turns the repository into a reproducible project-level experiment suite. The run records the dataset, device, experiment matrix, metrics, figures, failure analysis, and reproduction commands in committed small artifacts.

## Dataset

- Source path: `data/processed/classification_examples.jsonl`
- Profile: `full`
- Runtime: `2.024` seconds
- Device: `cuda` / `NVIDIA GeForce RTX 5090 Laptop GPU`

## Methods

Experiments declared in `configs/experiment_matrix.yaml`:

- `static_policy`: `static_policy`
- `tfidf_detector`: `tfidf_word`
- `char_detector`: `tfidf_char`
- `hybrid_policy_detector`: `hybrid_policy`

## Experiments

The matrix produced `4` result rows. Best observed `macro_f1`: `0.9635` from `char_detector`.

## Results

Key artifacts:

- `reports\results\v2_main_results.csv`
- `reports\results\v2_ablation_results.csv`
- `reports\results\v2_failure_cases.json`
- `reports\figures\v2_ablation_macro_f1.png`
- `reports\figures\v2_confusion_matrix.png`
- `reports\figures\v2_model_macro_f1.png`

## Ablations

Configured ablations: roleplay_wrapper, hidden_instruction, unicode_casing, tool_exfiltration. The generated ablation files quantify threshold, perturbation, architecture, retrieval, or metric sensitivity depending on the project.

## Failure Analysis

Failure records: `80`.

Top clusters:

- `false_negative`: 78
- `false_positive`: 2

## Discussion

Tool safety is a routing problem rather than just a classifier problem. V2 measures detector recall, benign pass rate, and the cost of moving decisions from allow/deny into review.

## Limitations

- Full raw caches, model weights, and optimizer states are intentionally excluded from GitHub.
- Results are designed for reproducible portfolio research; they are not production safety, medical, or compliance guarantees.
- Some V2 experiments use compact local artifacts to keep the repository lightweight.

## Reproduction

```powershell
conda run -n Transformers python scripts/run_matrix.py --device cuda --profile full
conda run -n Transformers python scripts/analyze_failures.py
conda run -n Transformers python scripts/make_report.py
conda run -n Transformers python -m pytest
```
