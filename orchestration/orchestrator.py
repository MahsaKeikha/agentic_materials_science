from AGENTS.evidence_agent import run as evidence
from AGENTS.modeling_agent import run as modeling
from AGENTS.problem_agent import run as problem
from AGENTS.reviewer_agent import run as reviewer
from AGENTS.risk_agent import run as risk
from safety.policy import authorize


def run(context: dict) -> dict:
    """Run the materials science pipeline and apply fail-closed governance."""
    outputs = [problem(context), modeling(context), evidence(context), risk(context), reviewer(context)]
    governance = authorize("research_release", context)
    return {
        "system": "F83",
        "outputs": outputs,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_material_certification": False,
        "hazardous_process_authority": False,
    }
