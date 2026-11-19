# Contributing to EVERYTHING FUTURE

**Project Owner & Original Creator:** DIVYESH BAMBHANIYA  
**Last Updated:** 2026-11-19

## Contribution Principles
1. **Micro-Utility First:** Every file or subfolder added must be independently understandable and useful without requiring the entire repository.
2. **Zero Empty Folders & Zero Filler:** Never add empty directories or boilerplate stub files.
3. **Verifiable Sourcing:** Every external fact, statistic, organization, or paper MUST cite a real, verifiable URL or DOI and record `last_verified` (ISO `YYYY-MM-DD`).
4. **Honest Status Labeling:** Use `VERIFIED`, `PARTIALLY_VERIFIED`, `UNVERIFIED`, `UNDER_RESEARCH`, or `OUTDATED` accurately. Never mark unverified claims as `VERIFIED`.
5. **Executable Code Quality:** All scripts in `07_SOURCE_CODE/` must specify dependencies, expected outputs, and pass automated unit tests.
6. **Licensing & Ownership Compliance:** Review `OWNERSHIP/PERMISSION_POLICY.md` before submitting or redistributing materials. Do not submit copyrighted third-party full texts.

## Verification Workflow
Before proposing changes, run the automated QA suite:
```bash
python3 VALIDATION/run_validation.py
```
