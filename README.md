# F83 | Agentic Materials Science | L3 Gold Standard | v1.0

A governed multi-agent reference system for materials research, modeling, property evidence, simulation and experiment review, risk analysis, and qualified human scientific synthesis.

## Research pipeline

- Problem formulation
- Materials modeling
- Evidence review
- Risk review
- Qualified human reviewer

## Gold-standard governance

F83 is fail closed. Research release requires problem review, reviewed modeling assumptions, simulation or experiment provenance, validated property measurements, evidence provenance, uncertainty review, reproducibility review, safety review, and explicit qualified human approval.

Release is blocked for invalid modeling assumptions, unverified simulation, unvalidated material-property measurements, missing evidence provenance, uncharacterized uncertainty, reproducibility gaps, unreviewed hazardous processes, or unsupported property claims.

The reference system cannot autonomously certify materials, claim experimental validation, fabricate evidence, hide uncertainty, or authorize hazardous processes.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out materials-science suite.

Author: Mahsa Keikha
