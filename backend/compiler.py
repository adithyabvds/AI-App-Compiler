from stages.intent import extract_intent
from stages.architecture import generate_architecture
from stages.ui_generator import generate_ui
from stages.api_generator import generate_api
from stages.db_generator import generate_db
from stages.auth_generator import generate_auth

from stages.summary_generator import generate_summary
from stages.text_summary import generate_text_summary

from validators.schema_validator import validate_schema
from validators.consistency_validator import validate_consistency

from repair.repair_engine import repair_config
from runtime.simulator import simulate


def compile_app(prompt: str):

    # --------------------
    # Stage 1 - Intent Extraction
    # --------------------

    intent = extract_intent(prompt)

    # --------------------
    # Ambiguity Handling
    # --------------------

    if intent.get("needs_clarification"):

        return {
            "status": "needs_clarification",
            "intent": intent
        }

    # --------------------
    # Stage 2 - Architecture Design
    # --------------------

    architecture = generate_architecture(intent)

    # --------------------
    # Stage 3 - UI Generation
    # --------------------

    ui_schema = generate_ui(intent)

    # --------------------
    # Stage 4 - API Generation
    # --------------------

    api_schema = generate_api(intent)

    # --------------------
    # Stage 5 - Database Generation
    # --------------------

    db_schema = generate_db(intent)

    # --------------------
    # Stage 6 - Auth Generation
    # --------------------

    auth_schema = generate_auth(intent)

    # --------------------
    # Summary Generation
    # --------------------

    summary = generate_summary(
        intent,
        ui_schema,
        api_schema,
        db_schema
    )

    # --------------------
    # Combine Configuration
    # --------------------

    config = {
        "summary": summary,

        "intent": intent,

        "architecture": architecture,

        "ui": ui_schema,

        "api": api_schema,

        "database": db_schema,

        "auth": auth_schema
    }

    # --------------------
    # Stage 7 - Validation
    # --------------------

    schema_errors = validate_schema(config)

    consistency_errors = validate_consistency(config)

    # --------------------
    # Contradiction Detection
    # --------------------

    critical_errors = [
        "Payments require customers",
        "CRM requires users",
        "Orders require products",
        "Hospital system requires patients"
    ]

    found_critical_errors = [
        error
        for error in consistency_errors
        if error in critical_errors
    ]

    if found_critical_errors:

        return {
            "status": "validation_failed",
            "validation_errors": found_critical_errors
        }

    # --------------------
    # Validation Report
    # --------------------

    config["validation"] = {
        "schema_errors": schema_errors,
        "consistency_errors": consistency_errors
    }

    # --------------------
    # Stage 8 - Repair Engine
    # --------------------

    if schema_errors or consistency_errors:

        config = repair_config(
            config,
            schema_errors,
            consistency_errors
        )

    # --------------------
    # Stage 9 - Runtime Simulation
    # --------------------

    simulation_result = simulate(config)

    config["simulation"] = simulation_result

    # --------------------
    # Human Readable Output
    # --------------------

    config["human_readable_summary"] = (
        generate_text_summary(config)
    )

    # --------------------
    # Final Status
    # --------------------

    config["status"] = "success"

    return config