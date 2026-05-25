def generate_db(intent):

    app_type = intent["app_type"]

    if app_type == "crm":

        return {
            "tables": [
                {
                    "name": "users",
                    "columns": [
                        "id",
                        "email",
                        "password"
                    ]
                },
                {
                    "name": "contacts",
                    "columns": [
                        "id",
                        "name",
                        "email",
                        "phone"
                    ]
                },
                {
                    "name": "leads",
                    "columns": [
                        "id",
                        "name",
                        "status"
                    ]
                }
            ]
        }

    elif app_type == "hospital_management":

        return {
            "tables": [
                {
                    "name": "patients",
                    "columns": [
                        "id",
                        "name",
                        "age",
                        "phone"
                    ]
                },
                {
                    "name": "doctors",
                    "columns": [
                        "id",
                        "name",
                        "specialization"
                    ]
                },
                {
                    "name": "appointments",
                    "columns": [
                        "id",
                        "patient_id",
                        "doctor_id",
                        "date"
                    ]
                }
            ]
        }

    elif app_type == "food_delivery":

        return {
            "tables": [
                {
                    "name": "restaurants",
                    "columns": [
                        "id",
                        "name",
                        "rating"
                    ]
                },
                {
                    "name": "customers",
                    "columns": [
                        "id",
                        "name",
                        "phone"
                    ]
                },
                {
                    "name": "orders",
                    "columns": [
                        "id",
                        "customer_id",
                        "amount"
                    ]
                }
            ]
        }

    elif app_type == "ecommerce":

        return {
            "tables": [
                {
                    "name": "products",
                    "columns": [
                        "id",
                        "name",
                        "price"
                    ]
                },
                {
                    "name": "customers",
                    "columns": [
                        "id",
                        "name",
                        "email"
                    ]
                },
                {
                    "name": "orders",
                    "columns": [
                        "id",
                        "customer_id",
                        "total"
                    ]
                }
            ]
        }

    return {
        "tables": []
    }