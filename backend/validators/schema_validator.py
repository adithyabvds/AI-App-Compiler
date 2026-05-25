def validate_schema(config):

    errors = []

    required = [
        "intent",
        "architecture",
        "ui",
        "api",
        "database",
        "auth"
    ]

    # -------------------
    # Top Level Keys
    # -------------------

    for key in required:

        if key not in config:

            errors.append(
                f"Missing {key}"
            )

    if errors:
        return errors

    # -------------------
    # Intent
    # -------------------

    if "app_type" not in config["intent"]:

        errors.append(
            "Intent missing app_type"
        )

    # -------------------
    # Architecture
    # -------------------

    architecture_required = [
        "frontend",
        "backend",
        "database"
    ]

    for field in architecture_required:

        if field not in config["architecture"]:

            errors.append(
                f"Architecture missing {field}"
            )

    # -------------------
    # UI
    # -------------------

    if "pages" not in config["ui"]:

        errors.append(
            "UI missing pages"
        )

    elif not config["ui"]["pages"]:

        errors.append(
            "UI pages empty"
        )

    # -------------------
    # API
    # -------------------

    if "endpoints" not in config["api"]:

        errors.append(
            "API missing endpoints"
        )

    elif not config["api"]["endpoints"]:

        errors.append(
            "API endpoints empty"
        )

    # -------------------
    # Database
    # -------------------

    if "tables" not in config["database"]:

        errors.append(
            "Database missing tables"
        )

    elif not config["database"]["tables"]:

        errors.append(
            "Database tables empty"
        )

    # -------------------
    # Auth
    # -------------------

    if "roles" not in config["auth"]:

        errors.append(
            "Auth missing roles"
        )

    elif not config["auth"]["roles"]:

        errors.append(
            "Auth roles empty"
        )

    return errors