from AGENTS.problem_agent import run as problem
from AGENTS.modeling_agent import run as modeling
from AGENTS.evidence_agent import run as evidence
from AGENTS.risk_agent import run as risk
from AGENTS.reviewer_agent import run as reviewer

def run(context: dict) -> dict:
    outputs = [problem(context), modeling(context), evidence(context), risk(context), reviewer(context)]
    return {"system": "F83", "outputs": outputs, "human_review_required": True}
