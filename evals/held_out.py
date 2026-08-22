from orchestration.orchestrator import run


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "invalid_model_assumption": True}, False),
    ({**base(), "simulation_not_verified": True}, False),
    ({**base(), "property_measurement_unvalidated": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "uncertainty_not_quantified": True}, False),
    ({**base(), "reproducibility_gap": True}, False),
    ({**base(), "hazardous_process_unreviewed": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
