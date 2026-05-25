def detect_ambiguity(prompt):

    prompt = prompt.lower().strip()

    # Very vague prompts
    ambiguous_prompts = [
        "build something",
        "create an app",
        "make an application",
        "build software"
    ]

    if prompt in ambiguous_prompts:

        return {
            "needs_clarification": True,
            "questions": [
                "Can you describe the application in more detail?"
            ]
        }

    # Doctor-related ambiguity
    if (
        "doctor" in prompt or
        "doctors" in prompt
    ):

        if (
            "hospital" not in prompt and
            "appointment" not in prompt and
            "clinic" not in prompt
        ):

            return {
                "needs_clarification": True,
                "questions": [
                    "Hospital management system?",
                    "Appointment booking system?",
                    "Clinic management system?"
                ]
            }

    return None


def extract_intent(prompt):

    # -------------------
    # Ambiguity Detection
    # -------------------

    ambiguity = detect_ambiguity(prompt)

    if ambiguity:
        return ambiguity

    prompt = prompt.lower()

    # -------------------
    # App Type Detection
    # -------------------

    app_type = "general_app"

    if "food" in prompt:
        app_type = "food_delivery"

    elif "hospital" in prompt:
        app_type = "hospital_management"

    elif "crm" in prompt:
        app_type = "crm"

    elif "ecommerce" in prompt:
        app_type = "ecommerce"

    # -------------------
    # Feature Detection
    # -------------------

    features = []

    if "login" in prompt:
        features.append("login")

    if "payment" in prompt or "payments" in prompt:
        features.append("payment")

    if "dashboard" in prompt:
        features.append("dashboard")

    if "analytics" in prompt:
        features.append("analytics")

    if "contacts" in prompt:
        features.append("contacts")

    if "roles" in prompt or "role" in prompt:
        features.append("role_based_access")

    # -------------------
    # Return Intent
    # -------------------

    return {
        "app_type": app_type,
        "features": features,
        "original_prompt": prompt
    }