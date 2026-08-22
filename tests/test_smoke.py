from orchestration.orchestrator import run
from safety.policy import authorize


def valid_context():
    return {
        "problem_reviewed": True,
        "modeling_assumptions_reviewed": True,
        "simulation_or_experiment_provenance_reviewed": True,
        "property_measurement_reviewed": True,
        "evidence_provenance_reviewed": True,
        "uncertainty_reviewed": True,
        "reproducibility_reviewed": True,
        "safety_reviewed": True,
        "human_approval": True,
    }


def test_reference_system_never_certifies_material_or_authorizes_hazardous_process():
    result = run(valid_context())
    assert result["autonomous_material_certification"] is False
    assert result["hazardous_process_authority"] is False


def test_complete_review_can_release_research_package():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_material_certification_claim_is_never_authorized():
    assert authorize("claim_material_certified", valid_context())["allowed"] is False


def test_invalid_model_assumption_blocks_release():
    context = valid_context()
    context["invalid_model_assumption"] = True
    assert run(context)["release_allowed"] is False


def test_unvalidated_property_measurement_blocks_release():
    context = valid_context()
    context["property_measurement_unvalidated"] = True
    assert run(context)["release_allowed"] is False


def test_missing_evidence_provenance_blocks_release():
    context = valid_context()
    context["evidence_provenance_missing"] = True
    assert run(context)["release_allowed"] is False


def test_unreviewed_hazardous_process_blocks_release():
    context = valid_context()
    context["hazardous_process_unreviewed"] = True
    assert run(context)["release_allowed"] is False
