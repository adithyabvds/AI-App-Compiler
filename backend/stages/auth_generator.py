def generate_auth(intent):

    return {
        "roles": {
            "admin": [
                "*"
            ],
            "user": [
                "view"
            ]
        }
    }