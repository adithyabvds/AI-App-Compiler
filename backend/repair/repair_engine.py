def repair_config(
    config,
    schema_errors,
    consistency_errors
):

    fixes = []

    all_errors = (
        schema_errors +
        consistency_errors
    )

    # -------------------
    # Schema Repairs
    # -------------------

    if "Intent missing app_type" in all_errors:

        config["intent"]["app_type"] = "generic_app"

        fixes.append(
            "Added default app_type"
        )

    if "UI missing pages" in all_errors:

        config["ui"]["pages"] = []

        fixes.append(
            "Added empty pages list"
        )

    if "API missing endpoints" in all_errors:

        config["api"]["endpoints"] = []

        fixes.append(
            "Added empty endpoints list"
        )

    if "Database missing tables" in all_errors:

        config["database"]["tables"] = []

        fixes.append(
            "Added empty tables list"
        )

    if "Auth missing roles" in all_errors:

        config["auth"]["roles"] = {
            "admin": ["*"]
        }

        fixes.append(
            "Added default admin role"
        )

    # -------------------
    # Consistency Repairs
    # -------------------

    tables = [
        table["name"]
        for table in config["database"]["tables"]
    ]

    # CRM

    if (
        "Contacts endpoint missing contacts table"
        in all_errors
    ):

        if "contacts" not in tables:

            config["database"]["tables"].append(
                {
                    "name": "contacts",
                    "columns": [
                        "id",
                        "name",
                        "email",
                        "phone"
                    ]
                }
            )

            fixes.append(
                "Added contacts table"
            )

    if (
        "Leads endpoint missing leads table"
        in all_errors
    ):

        if "leads" not in tables:

            config["database"]["tables"].append(
                {
                    "name": "leads",
                    "columns": [
                        "id",
                        "name",
                        "status"
                    ]
                }
            )

            fixes.append(
                "Added leads table"
            )

    # Hospital

    if (
        "Patients endpoint missing patients table"
        in all_errors
    ):

        config["database"]["tables"].append(
            {
                "name": "patients",
                "columns": [
                    "id",
                    "name",
                    "age",
                    "phone"
                ]
            }
        )

        fixes.append(
            "Added patients table"
        )

    if (
        "Doctors endpoint missing doctors table"
        in all_errors
    ):

        config["database"]["tables"].append(
            {
                "name": "doctors",
                "columns": [
                    "id",
                    "name",
                    "specialization"
                ]
            }
        )

        fixes.append(
            "Added doctors table"
        )

    if (
        "Appointments endpoint missing appointments table"
        in all_errors
    ):

        config["database"]["tables"].append(
            {
                "name": "appointments",
                "columns": [
                    "id",
                    "patient_id",
                    "doctor_id",
                    "date"
                ]
            }
        )

        fixes.append(
            "Added appointments table"
        )

    # Ecommerce

    if (
        "Products endpoint missing products table"
        in all_errors
    ):

        config["database"]["tables"].append(
            {
                "name": "products",
                "columns": [
                    "id",
                    "name",
                    "price"
                ]
            }
        )

        fixes.append(
            "Added products table"
        )

    if (
        "Orders endpoint missing orders table"
        in all_errors
    ):

        config["database"]["tables"].append(
            {
                "name": "orders",
                "columns": [
                    "id",
                    "customer_id",
                    "total"
                ]
            }
        )

        fixes.append(
            "Added orders table"
        )

    # Food Delivery

    if (
        "Restaurants endpoint missing restaurants table"
        in all_errors
    ):

        config["database"]["tables"].append(
            {
                "name": "restaurants",
                "columns": [
                    "id",
                    "name",
                    "rating"
                ]
            }
        )

        fixes.append(
            "Added restaurants table"
        )

    # -------------------
    # Repair Summary
    # -------------------

    config["repair"] = {
        "performed": len(fixes) > 0,
        "fixes": fixes
    }

    return config