# Engineering audit — 2026-10-26

Purpose: Commodity history exploration and forecasting.

Classification: **A** (single application/tool).
Final structure: app.py, data_pipeline.py, model_pipeline.py, tests/. Existing capabilities and source material were retained.

| Assessment | Result |
| --- | --- |
| Idea strength | 8/10 |
| Implementation strength | 7/10 |
| Core strength | Temporal regression coverage, CSV input and saved-model workflows. |
| Main limitation | Synthetic tests cannot establish real-market forecasting accuracy. |
| Readiness | Local prototype/tool with the verified baseline below; no production certification |

Scores are subjective engineering estimates, not measured product or model quality.

## Delivered

Added a repo-local run.cmd that activates the assigned existing environment, checks actual startup imports and forwards application arguments. README setup now uses this local launcher.

Assigned environment: **cnn**. Run `.\run.cmd --check`, then `.\run.cmd`.
The launcher installs nothing and preserves its child exit status. On this workstation
it selects the assigned interpreter; standalone clones fall back to active Python.
VS Code's local interpreter settings were aligned with the same assignment.

## Verification

- **Automated tests:** 29 passed; 0 reported skips; 0 private-report cases deselected.
- **Startup check:** `run.cmd --check` passed from outside the repository;
  required startup modules were imported in the assigned environment.
- **Tested runtime:** Windows; Conda cnn; Python 3.10.20.
- **Data handling:** tests used temporary/synthetic fixtures. No live transactions,
  provider generation, deployment, new model downloads or package installs were performed.
- **Repository check:** origin/main fetched before publication; no pre-existing local
  changes were present. A tracked-file scan found no matches for the high-confidence
  credential patterns checked. That scan is not a guarantee that all personal data
  or arbitrary secret formats are absent. Ignored local data was not staged.
- **Limits:** optional external workflows, representative real-data quality and all
  possible platform/version combinations remain unverified.

Test command from the repository root:

```powershell
conda activate cnn
python -m pytest tests -q -p no:cacheprovider
```

## Next three upgrades

1. Forecast provenance panel.
2. Seasonal-baseline comparisons with representative historical prices.
3. Source freshness and coverage indicators.

Expected benefit: clearer decisions, more reproducible workflows and stronger evidence
for quality. These are proposed upgrades, not implemented features or measured speedups.

External assets: Dated representative price history is needed for meaningful backtests; live fetching was not exercised.

No root license file is set. No license was selected or changed.

## Additional implementation pass

Backtest date/size/target guards, a last-training-price baseline, MAE skill, scored-window coverage and chronological split provenance, exposed in the chart and fold table.

Use: Backtest → Run Backtest. Compare the baseline trace and inspect Naive MAE, MAE Skill, Coverage and split dates.

Verification: the complete offline suite passed in the assigned **cnn**
environment after this change (29 tests). Regression fixtures remain
temporary/synthetic. Optional real-model/data quality and external integrations
remain unverified. No packages, models or additional environments were installed.

The earlier numeric scores are subjective historical assessments; new features do
not automatically establish a higher score or production readiness.
