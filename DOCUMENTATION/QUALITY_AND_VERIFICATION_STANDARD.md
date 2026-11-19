# Quality Assurance & Verification Standard

**Last Verified:** 2026-11-19

## Official Verification Status Labels

Every module, resource entry, and research record MUST carry one of the following five labels:

| Status Label | Definition |
| :--- | :--- |
| `VERIFIED` | Core facts, official URLs, DOIs, or executable code tests have been directly checked and validated on `last_verified` date. |
| `PARTIALLY_VERIFIED` | Structural framework and primary institutional links are verified, while deeper subdomain details or benchmarks require further review. |
| `UNVERIFIED` | Draft entry awaiting independent source verification. Never treated as authoritative. |
| `UNDER_RESEARCH` | Planned or actively researched topic/subdomain (e.g., Phase 2–4 extended taxonomy modules). |
| `OUTDATED` | Previously verified material superseded by newer standards, policies, or scientific results; flagged for refresh. |

## Non-Negotiable Integrity Rules
1. **Zero Fabrication:** Never invent DOIs, URLs, statistics, organizations, or test results.
2. **Zero Empty Folders:** Every directory in `MODULES/` must contain substantive, independently usable files.
3. **Executable Reproducibility:** Every script in `07_SOURCE_CODE/` must pass Python syntax compilation and automated unit tests run by `VALIDATION/run_validation.py`.
4. **Scientific Responsibility:** Distinguish established consensus from active hypotheses; never present speculative timelines as settled fact.
