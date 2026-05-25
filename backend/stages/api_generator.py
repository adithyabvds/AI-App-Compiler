def generate_api(intent):

    app_type = intent["app_type"]

    if app_type == "crm":

        return {
            "endpoints": [
                {
                    "path": "/login",
                    "method": "POST"
                },
                {
                    "path": "/contacts",
                    "method": "GET"
                },
                {
                    "path": "/contacts",
                    "method": "POST"
                },
                {
                    "path": "/leads",
                    "method": "GET"
                }
            ]
        }

    elif app_type == "hospital_management":

        return {
            "endpoints": [
                {
                    "path": "/patients",
                    "method": "GET"
                },
                {
                    "path": "/doctors",
                    "method": "GET"
                },
                {
                    "path": "/appointments",
                    "method": "POST"
                }
            ]
        }

    elif app_type == "food_delivery":

        return {
            "endpoints": [
                {
                    "path": "/restaurants",
                    "method": "GET"
                },
                {
                    "path": "/orders",
                    "method": "POST"
                }
            ]
        }

    elif app_type == "ecommerce":

        return {
            "endpoints": [
                {
                    "path": "/products",
                    "method": "GET"
                },
                {
                    "path": "/orders",
                    "method": "POST"
                }
            ]
        }

    return {
        "endpoints": []
    }