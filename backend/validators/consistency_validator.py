def validate_consistency(config):

    errors = []

    tables = [
        table["name"]
        for table in config["database"]["tables"]
    ]

    endpoints = [
        endpoint["path"]
        for endpoint in config["api"]["endpoints"]
    ]

    pages = [
        page["name"]
        for page in config["ui"]["pages"]
    ]

    prompt = config["intent"][
        "original_prompt"
    ].lower()

    # --------------------
    # Database Exists
    # --------------------

    if not tables:
        errors.append(
            "Database schema missing"
        )

    # --------------------
    # API -> Database
    # --------------------

    if "/contacts" in endpoints and "contacts" not in tables:
        errors.append(
            "Contacts endpoint missing contacts table"
        )

    if "/leads" in endpoints and "leads" not in tables:
        errors.append(
            "Leads endpoint missing leads table"
        )

    if "/patients" in endpoints and "patients" not in tables:
        errors.append(
            "Patients endpoint missing patients table"
        )

    if "/doctors" in endpoints and "doctors" not in tables:
        errors.append(
            "Doctors endpoint missing doctors table"
        )

    if "/appointments" in endpoints and "appointments" not in tables:
        errors.append(
            "Appointments endpoint missing appointments table"
        )

    if "/products" in endpoints and "products" not in tables:
        errors.append(
            "Products endpoint missing products table"
        )

    if "/orders" in endpoints and "orders" not in tables:
        errors.append(
            "Orders endpoint missing orders table"
        )

    if "/restaurants" in endpoints and "restaurants" not in tables:
        errors.append(
            "Restaurants endpoint missing restaurants table"
        )

    # --------------------
    # UI -> API
    # --------------------

    if "Contacts" in pages and "/contacts" not in endpoints:
        errors.append(
            "Contacts page missing contacts endpoint"
        )

    if "Leads" in pages and "/leads" not in endpoints:
        errors.append(
            "Leads page missing leads endpoint"
        )

    if "Patients" in pages and "/patients" not in endpoints:
        errors.append(
            "Patients page missing patients endpoint"
        )

    if "Doctors" in pages and "/doctors" not in endpoints:
        errors.append(
            "Doctors page missing doctors endpoint"
        )

    if "Appointments" in pages and "/appointments" not in endpoints:
        errors.append(
            "Appointments page missing appointments endpoint"
        )

    if "Products" in pages and "/products" not in endpoints:
        errors.append(
            "Products page missing products endpoint"
        )

    if "Restaurants" in pages and "/restaurants" not in endpoints:
        errors.append(
            "Restaurants page missing restaurants endpoint"
        )

    # --------------------
    # Auth Check
    # --------------------

    if "Login" in pages:

        if not config.get("auth"):
            errors.append(
                "Login page exists but auth missing"
            )

    # --------------------
    # Contradiction Detection
    # --------------------

    if (
        "payment" in prompt and
        "without customer" in prompt
    ):
        errors.append(
            "Payments require customers"
        )

    if (
        "crm" in prompt and
        "without user" in prompt
    ):
        errors.append(
            "CRM requires users"
        )

    if (
        "order" in prompt and
        "without product" in prompt
    ):
        errors.append(
            "Orders require products"
        )

    if (
        "hospital" in prompt and
        "without patient" in prompt
    ):
        errors.append(
            "Hospital system requires patients"
        )

    return errors