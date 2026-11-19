# Scientific Reproducibility Checklist

**Template Source:** EVERYTHING FUTURE (v1.0.0) | **Owner:** DIVYESH BAMBHANIYA

## Code & Environment
- [ ] All source code is version-controlled with an exact commit hash or release tag.
- [ ] All dependencies are pinned (`requirements.txt`, `environment.yml`, or container digest).
- [ ] Random seeds are explicitly set and logged for all stochastic steps.
- [ ] Single command reproduces key figures/tables from raw or documented input data.

## Data & Provenance
- [ ] Dataset version, access URL, and license are explicitly documented.
- [ ] Train/validation/test splits are strictly isolated (zero data leakage).
- [ ] Preprocessing, filtering, and outlier-removal rules are coded and justified.

## Evaluation & Statistical Rigor
- [ ] Baselines are tuned fairly under comparable compute/resource budgets.
- [ ] Results report variance, confidence intervals, or multi-seed distributions—not single cherry-picked runs.
- [ ] Negative results, edge cases, and failure modes are explicitly reported.

## Documentation & Traceability
- [ ] Every external claim cites a verifiable DOI, standard, or official documentation URL.
- [ ] Hardware specs, runtime, and cost/energy footprint are reported.
