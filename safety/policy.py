"""Fail-closed research governance for F83 materials science."""

REQUIRED_REVIEWS = (
    "problem_reviewed",
    "modeling_assumptions_reviewed",
    "simulation_or_experiment_provenance_reviewed",
    "property_measurement_reviewed",
    "evidence_provenance_reviewed",
    "uncertainty_reviewed",
    "reproducibility_reviewed",
    "safety_reviewed",
    "human_approval",
)

BLOCKED_ACTIONS = {
    "claim_material_certified",
    "claim_experimentally_validated",
    "fabricate_evidence",
    "hide_uncertainty",
    "authorize_hazardous_process",
}


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {"allowed": False, "reason": "unsupported scientific or hazardous-process authority is outside scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required materials-science review", "missing": missing}

    blockers = []
    if context.get("invalid_model_assumption"):
        blockers.append("modeling assumption invalid or unresolved")
    if context.get("simulation_not_verified"):
        blockers.append("simulation verification incomplete")
    if context.get("property_measurement_unvalidated"):
        blockers.append("material property measurement not validated")
    if context.get("evidence_provenance_missing"):
        blockers.append("evidence provenance incomplete")
    if context.get("uncertainty_not_quantified"):
        blockers.append("material uncertainty not characterized")
    if context.get("reproducibility_gap"):
        blockers.append("reproducibility gap unresolved")
    if context.get("hazardous_process_unreviewed"):
        blockers.append("hazardous process lacks safety review")
    if context.get("unsupported_property_claim"):
        blockers.append("unsupported material property claim")

    if blockers:
        return {"allowed": False, "reason": "materials-science governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "research package approved after qualified human review"}


def check(context: dict) -> dict:
    return authorize("research_release", context)
