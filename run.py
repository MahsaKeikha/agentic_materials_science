from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
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

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
