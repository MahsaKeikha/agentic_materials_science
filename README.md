# F83 Agentic Materials Science

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for materials-science research across problem formulation, materials modeling, experimental and computational evidence, uncertainty and risk analysis, reproducibility, and qualified human scientific review.

F83 is intended as a reusable research framework for studying relationships among composition, structure, processing, properties, and performance while keeping simulations, measurements, assumptions, provenance, uncertainty, and safety constraints explicit.

This repository supports research analysis and planning. It does not certify materials, claim experimental validation without evidence, authorize hazardous laboratory or manufacturing processes, replace laboratory safety systems, or substitute for qualified scientific, engineering, environmental, health, safety, quality, or regulatory judgment.

## Materials research lifecycle

```text
research question
      |
      v
problem formulation
      |
      v
materials modeling
      |
      v
evidence review
      |
      v
uncertainty + risk
      |
      v
qualified human review
```

The workflow is fail closed. Unsupported property claims, unverified simulations, unvalidated measurements, missing provenance, unresolved uncertainty, reproducibility gaps, or hazardous-process requests remain visible as blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Problem Agent | Defines material system, target property, constraints and research question | What material, structure, processing state, environment and performance question are actually being studied? |
| Modeling Agent | Reviews computational representation, assumptions and model validity | Is the selected model appropriate for the relevant length, time, chemistry and physics scales? |
| Evidence Agent | Reviews simulations, experiments, measurements, literature and provenance | What evidence supports the result, and is it traceable and independently interpretable? |
| Risk Agent | Reviews uncertainty, hazardous processes, environmental assumptions and research limitations | What could invalidate the result or make the proposed work unsafe or misleading? |
| Reviewer Agent | Represents qualified scientific synthesis and approval | Has an appropriately qualified human reviewed the evidence, uncertainty, reproducibility and safety boundaries? |

No specialist agent independently certifies a material or authorizes a hazardous process.

## Repository structure

```text
AGENTS/
├── problem_agent.py
├── modeling_agent.py
├── evidence_agent.py
├── risk_agent.py
└── reviewer_agent.py

SKILLS/
├── problem_decomposition.py
├── evidence_discipline.py
├── provenance_tracking.py
├── uncertainty_reasoning.py
└── human_review.py

TOOLS/
├── assumption_tracker.py
├── data_validator.py
├── evidence_register.py
├── result_formatter.py
└── review_gate.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The structure separates scientific reasoning from deterministic evidence handling, orchestration, state, safety controls, evaluation and observability.

## Define the material system

Materials claims require more than a material name.

A useful research record can include:

```text
material_id
composition
phase_or_phases
crystal_or_microstructure
processing_history
heat_treatment
surface_state
porosity
defect_state
geometry
orientation
temperature
pressure
humidity_or_environment
loading_condition
aging_condition
target_property
measurement_or_model_method
provenance
```

Properties can change substantially with processing, microstructure, environment, scale and test method. F83 therefore avoids treating a property as an intrinsic scalar detached from context.

## Composition, structure, processing, properties and performance

The reference workflow follows the central materials-science relationship:

```text
composition
    +
processing
    |
    v
structure / microstructure
    |
    v
properties
    |
    v
component performance
```

A change in manufacturing or heat treatment can alter microstructure and therefore change mechanical, thermal, electrical, magnetic, optical, chemical or degradation behavior.

The workflow should preserve these dependencies rather than comparing materials only by catalog values.

## Problem formulation

The Problem Agent defines the scientific question before simulation or property ranking begins.

A well-formed problem can identify:

- target property or response
- material family
- composition range
- processing state
- operating environment
- temperature and pressure range
- loading mode
- relevant length scale
- relevant time scale
- experimental reference
- performance constraint
- uncertainty tolerance
- safety constraints

A model cannot be judged appropriate until the intended claim is defined.

## Modeling assumptions

`TOOLS/assumption_tracker.py` provides deterministic tracking of modeling assumptions.

Typical assumptions can involve:

- crystal structure
- phase stability
- defect concentration
- boundary conditions
- periodicity
- continuum approximation
- isotropy or anisotropy
- elastic versus plastic response
- equilibrium assumptions
- temperature
- pressure
- chemical potential
- interface conditions
- surface effects
- grain structure
- transport mechanism

Assumptions should be visible in the final result, especially when they define the model's validity regime.

## Multiscale modeling

Materials behavior spans electronic, atomistic, mesoscale and continuum scales.

Potential modeling approaches include:

- electronic-structure calculations
- density functional theory
- molecular dynamics
- Monte Carlo methods
- phase-field modeling
- CALPHAD-style thermodynamic modeling
- crystal plasticity
- finite-element analysis
- continuum transport models
- surrogate and machine-learning models

F83 is method-neutral. It does not assume that a model validated at one scale automatically predicts behavior at another.

Cross-scale handoffs should identify which quantities are transferred and what uncertainty is introduced.

## Computational materials evidence

A computational result should record enough information to reproduce or critically assess the calculation.

Useful provenance can include:

```text
model_family
software
software_version
input_structure
composition
potential_or_functional
basis_or_discretization
mesh_or_cell
boundary_conditions
solver_settings
convergence_criteria
time_step
sampling_method
random_seed
hardware_environment
postprocessing
```

A figure or final scalar without computational provenance is insufficient evidence for a reproducible claim.

## Convergence and numerical verification

Numerical convergence should be distinguished from agreement with experiment.

Depending on the method, verification can include:

- mesh convergence
- time-step convergence
- k-point convergence
- basis-set convergence
- supercell-size effects
- simulation-time sufficiency
- finite-size effects
- solver tolerance
- initialization sensitivity
- stochastic sampling uncertainty

A numerically converged model can still be physically inappropriate. Verification and validation answer different questions.

## Simulation versus experiment

F83 keeps simulation evidence and experimental evidence explicitly separated.

```text
simulation
    -> model-consistent prediction

experiment
    -> measurement under defined conditions

agreement
    -> evidence about model validity within tested conditions
```

Simulation alone should not be described as experimental validation.

Likewise, agreement at one condition does not establish universal validity across composition, temperature, loading, geometry, environment or processing state.

## Experimental provenance

Experimental materials data should preserve the conditions under which the specimen was created and measured.

Relevant provenance can include:

- raw-material source
- composition measurement
- synthesis route
- processing parameters
- heat treatment
- specimen preparation
- geometry
- surface finish
- orientation
- test standard
- instrument
- instrument calibration
- environmental conditions
- loading rate
- operator or laboratory
- replicate identifier
- raw-data location
- analysis pipeline

Without this information, apparently contradictory property values may simply describe different material states.

## Property measurements

`TOOLS/data_validator.py` provides deterministic validation support for structured research data.

Depending on the project, properties can include:

- elastic modulus
- yield strength
- tensile strength
- fracture toughness
- hardness
- fatigue behavior
- creep
- thermal conductivity
- thermal expansion
- electrical conductivity
- dielectric response
- magnetic properties
- optical response
- diffusion
- corrosion resistance
- permeability
- density
- porosity

Each measurement should retain units, test conditions, uncertainty, specimen state and method.

## Units and dimensional consistency

Materials datasets frequently combine values from multiple sources and unit systems.

Research review should verify:

- SI versus non-SI units
- stress units
- temperature scales
- density units
- conductivity conventions
- composition units
- strain conventions
- energy units
- length scales

Unit conversions should be deterministic and documented. A unit mismatch can produce apparently plausible but physically invalid comparisons.

## Mechanical-property interpretation

Mechanical properties are strongly condition-dependent.

Interpretation can depend on:

- strain rate
- temperature
- specimen geometry
- loading mode
- orientation
- grain size
- surface condition
- porosity
- heat treatment
- residual stress
- environment

F83 should not compare strength, fatigue, creep or fracture values without checking whether test conditions are meaningfully comparable.

## Thermal, electrical and transport properties

Transport properties can depend on temperature, phase, composition, microstructure and measurement direction.

The workflow should preserve:

- measurement temperature
- directionality
- phase state
- density or porosity
- contact or interface assumptions
- frequency where relevant
- measurement technique

Property tables without these qualifiers should be treated cautiously.

## Phase and microstructure evidence

Material performance often depends on phase fraction, grain structure, defects and interfaces.

Evidence can include:

- diffraction
- microscopy
- spectroscopy
- compositional mapping
- grain-size analysis
- porosity analysis
- phase-fraction estimation
- defect characterization

The repository can organize this evidence but does not independently authenticate laboratory measurements.

## Data-driven materials models

Machine-learning models can support property prediction, screening and surrogate modeling, but they introduce additional validity risks.

Review should consider:

- dataset provenance
- duplicate structures or samples
- train/test leakage
- composition leakage
- family-level leakage
- distribution shift
- extrapolation
- feature provenance
- target measurement quality
- uncertainty calibration
- baseline models
- domain of applicability

Random row splitting can overstate performance when near-identical compositions or structures appear in both training and test sets.

## Materials informatics and screening

High-throughput screening can rank large candidate spaces, but ranking should not be confused with experimental confirmation.

A candidate record should distinguish:

```text
predicted
simulated
experimentally_measured
independently_replicated
qualified_for_application
```

Each maturity state requires different evidence.

## Evidence discipline

`TOOLS/evidence_register.py` provides structured evidence registration.

Useful fields include:

```text
evidence_id
claim
source_type
source_reference
material_state
method
conditions
result
uncertainty
limitations
independence
review_state
```

Evidence can include literature, simulations, experiments, databases and reference standards. Conflicting evidence should be preserved rather than averaged away without explanation.

## Literature and database evidence

Published or database values should be evaluated for compatibility with the current material state and research question.

Questions include:

- Is the composition equivalent?
- Is the phase state equivalent?
- Is processing comparable?
- Are units and definitions consistent?
- Is the test method comparable?
- Are temperature and environment comparable?
- Is the data primary or derived?
- Is uncertainty reported?

A well-known handbook value can still be inappropriate for a specific processed material.

## Uncertainty

Uncertainty can arise from measurement, model form, parameters, sampling, processing variation, numerical approximation and environmental variability.

The Risk Agent should distinguish, where possible:

- measurement uncertainty
- numerical uncertainty
- parameter uncertainty
- model-form uncertainty
- sampling uncertainty
- batch-to-batch variation
- specimen variation
- environmental uncertainty

A precise numerical output should not imply greater confidence than the evidence supports.

## Sensitivity analysis

Sensitivity analysis can identify which assumptions or parameters dominate a predicted result.

Useful analyses can include:

- parameter perturbation
- boundary-condition variation
- model-choice comparison
- mesh or discretization variation
- material-property uncertainty propagation
- environmental variation
- processing variation

Sensitivity results should be reported together with the baseline assumptions.

## Reproducibility and replication

Reproducibility and experimental replication are related but distinct.

**Computational reproducibility** asks whether another researcher can reproduce the calculation from the recorded inputs, code and environment.

**Experimental replication** asks whether the material can be produced and measured again with compatible results.

A mature research claim should identify which type of evidence exists.

## Hazardous materials and processes

Materials research can involve hazardous chemicals, powders, high temperatures, high pressures, reactive atmospheres, radiation sources, energetic processes, toxic compounds, nanomaterials, vacuum equipment, furnaces, lasers, mechanical testing and other controlled hazards.

F83 does not authorize or provide operational approval for hazardous synthesis, processing or laboratory procedures.

The Risk Agent should flag when work requires appropriate institutional procedures, trained personnel, engineering controls, PPE, environmental health and safety review, or specialized facilities.

## Nanomaterials

Nanomaterials can exhibit properties and exposure pathways that differ from bulk materials.

Research review can consider:

- particle size and distribution
- surface area
- agglomeration
- surface chemistry
- inhalation or exposure potential
- containment
- disposal
- environmental release

The repository does not determine that a nanomaterial is safe for handling or human exposure.

## Environmental and lifecycle considerations

Material selection can involve tradeoffs beyond performance.

Research may consider:

- embodied energy
- critical-mineral dependence
- toxicity
- recyclability
- durability
- repairability
- corrosion
- end-of-life handling
- supply-chain constraints

These analyses require clearly defined system boundaries and data provenance.

## Application qualification boundary

A promising research result does not automatically qualify a material for an application.

Application qualification may require:

- application-specific standards
- representative manufacturing
- environmental testing
- fatigue and durability evidence
- lot variability
- scale-up evidence
- joining and interface validation
- component-level testing
- reliability analysis
- quality systems
- regulatory requirements

F83 can organize evidence requirements but cannot autonomously certify material suitability.

## Safety-critical applications

Materials used in aerospace, medical, structural, pressure, energy, transportation or other safety-critical applications require domain-specific qualification and engineering authority.

The system must not turn a literature property value or simulation result into an autonomous safety-critical material selection.

## Result formatting

`TOOLS/result_formatter.py` supports consistent presentation of research outputs.

A defensible result should separate:

- question
- assumptions
- methods
- evidence
- results
- uncertainty
- limitations
- safety concerns
- reproducibility state
- reviewer state

This makes it harder for limitations to disappear behind a headline property value.

## Fail-closed governance

`TOOLS/review_gate.py` supports the final research release gate.

Reference blockers include:

- problem definition incomplete
- material state inadequately specified
- modeling assumptions invalid or missing
- simulation unverified
- experimental provenance missing
- property measurement unvalidated
- units inconsistent
- evidence provenance missing
- uncertainty uncharacterized
- reproducibility incomplete
- conflicting evidence unresolved
- hazardous process unreviewed
- unsupported experimental-validation claim
- unsupported certification claim
- safety-critical selection requested without qualified engineering review
- qualified human approval missing

Human review is required after automated checks pass. Human approval does not convert failed evidence into valid evidence.

## Human authority boundaries

F83 must not autonomously:

- certify a material
- authorize a hazardous process
- approve laboratory safety
- claim experimental confirmation without evidence
- approve a safety-critical material selection
- approve manufacturing qualification
- determine regulatory compliance
- suppress conflicting evidence
- fabricate measurement or simulation results
- claim reproducibility that has not been demonstrated

Final authority remains with appropriately qualified scientists, engineers, laboratory personnel, EHS professionals, quality teams and regulatory authorities.

## End-to-end reference workflow

A typical F83 workflow follows this sequence:

1. Define the material, state, target property and intended research claim.
2. Record composition, processing, microstructure and environmental context.
3. Select a modeling approach appropriate to the relevant scales.
4. Register assumptions and validity limits.
5. Verify numerical convergence and computational provenance.
6. Register experimental and literature evidence separately.
7. Validate units, conditions and property definitions.
8. Compare simulation and experiment without conflating them.
9. Quantify uncertainty and perform sensitivity analysis where appropriate.
10. Review conflicting evidence and model limitations.
11. Review reproducibility and independent replication status.
12. Flag hazardous processes and safety-critical application boundaries.
13. Apply the fail-closed review gate.
14. Require qualified human scientific review before release.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and reference cases under `benchmarks/`.

Evaluation should test research integrity as well as plausible scientific output.

Useful dimensions include:

- assumption tracking
- material-state completeness
- simulation verification
- experimental provenance
- property-data validation
- unit consistency
- uncertainty enforcement
- reproducibility enforcement
- hazardous-process escalation
- unsupported-validation claim detection
- certification-boundary enforcement
- human-review enforcement

The held-out suite should include incomplete and misleading cases, not only clean examples.

## Failure states

Useful explicit states include:

```text
PROBLEM DEFINITION INCOMPLETE
MATERIAL STATE INCOMPLETE
MODELING ASSUMPTION INVALID
SIMULATION UNVERIFIED
EXPERIMENTAL PROVENANCE MISSING
PROPERTY DATA UNVALIDATED
UNIT INCONSISTENCY
EVIDENCE PROVENANCE MISSING
UNCERTAINTY UNCHARACTERIZED
REPRODUCIBILITY GAP
CONFLICTING EVIDENCE UNRESOLVED
HAZARDOUS PROCESS REVIEW REQUIRED
EXPERIMENTAL VALIDATION NOT ESTABLISHED
MATERIAL CERTIFICATION PROHIBITED
SAFETY-CRITICAL SELECTION REVIEW REQUIRED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate measurements, provenance, simulation convergence, experimental validation, safety approval, certification, or human review.

## Observability

The `observability/` layer records workflow events for audit and debugging.

Useful research telemetry includes:

- assumptions registered
- evidence records
- data-validation failures
- unit mismatches
- convergence status
- uncertainty flags
- conflicting evidence
- reproducibility gaps
- safety flags
- review-gate status
- human-review state

Observability is not a substitute for scientific evidence.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11 and 3.12.

## Reproducibility checklist

For a computational or experimental result intended to be reproduced, version at minimum:

- material composition
- processing history
- structural state
- environmental conditions
- raw data
- input files
- software and version
- model parameters
- numerical settings
- analysis code
- unit conventions
- experimental method
- instrument and calibration
- specimen metadata
- uncertainty method
- random seeds where relevant
- result tables

A changed model, processing route or dataset should create a new evidence version rather than silently replacing the prior result.

## L3 Gold Standard

F83 follows the library's L3 Gold Standard structure through specialist agents, deterministic evidence tools, explicit state and safety layers, observability, held-out governance evaluation, CI, fail-closed release gates and mandatory qualified human review.

This maturity designation describes the engineering and governance structure of the repository. It is not material certification, laboratory accreditation, experimental validation, manufacturing qualification, regulatory approval, or proof that a material is safe or suitable for a specific application.

## Extending F83

Common extensions include:

- materials databases
- electronic-structure packages
- molecular-dynamics systems
- phase-field tools
- thermodynamic databases
- finite-element systems
- laboratory information systems
- microscopy pipelines
- diffraction analysis
- spectroscopy workflows
- experiment tracking
- provenance databases
- materials informatics models
- uncertainty quantification
- digital twins
- quality systems

New integrations should preserve provenance, versioning, unit consistency, uncertainty, reproducibility and human scientific review.

## Example applications

F83 can serve as a reference architecture for research involving:

- metals and alloys
- polymers
- ceramics
- composites
- semiconductors
- electronic materials
- battery materials
- biomaterials research
- nanomaterials
- coatings
- structural materials
- functional materials
- computational materials science
- materials informatics

Each domain requires its own methods, standards and safety controls.

## Design principles

1. Define material state and operating context before comparing properties.
2. Preserve composition, processing, structure, property and performance relationships.
3. Make modeling assumptions and validity regimes explicit.
4. Separate numerical verification from physical validation.
5. Separate simulation evidence from experimental evidence.
6. Preserve units, methods, specimen state and provenance for every property value.
7. Quantify uncertainty and expose sensitivity to assumptions.
8. Distinguish computational reproducibility from experimental replication.
9. Fail closed for hazardous processes, unsupported certification and safety-critical claims.
10. Keep final scientific, engineering, laboratory and safety authority with qualified humans.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted and extended subject to its license terms.

## Responsible use

Use F83 as a materials-science research and multi-agent governance reference. Validate material state, models, measurements, uncertainty, reproducibility, safety requirements and application-specific qualification against the actual research or engineering program before relying on results. Final scientific, engineering, laboratory, safety, quality and regulatory decisions remain with appropriately qualified and authorized professionals.