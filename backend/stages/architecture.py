def generate_architecture(intent):

    return {
        "frontend": "react",
        "backend": "fastapi",
        "database": "sqlite",
        "app_type": intent["app_type"]
    }