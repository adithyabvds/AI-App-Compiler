def generate_ui(intent):

    app_type = intent["app_type"]

    if app_type == "crm":

        return {
            "pages": [
                {
                    "name": "Login",
                    "components": [
                        "email",
                        "password",
                        "login_button"
                    ]
                },
                {
                    "name": "Dashboard",
                    "components": [
                        "lead_count",
                        "contact_count",
                        "sales_chart",
                        "analytics_cards"
                    ]
                },
                {
                    "name": "Contacts",
                    "components": [
                        "search_bar",
                        "contacts_table",
                        "add_contact_button"
                    ]
                },
                {
                    "name": "Leads",
                    "components": [
                        "lead_table",
                        "lead_status",
                        "convert_to_customer"
                    ]
                }
            ]
        }

    elif app_type == "hospital_management":

        return {
            "pages": [
                {
                    "name": "Login",
                    "components": [
                        "email",
                        "password",
                        "login_button"
                    ]
                },
                {
                    "name": "Patients",
                    "components": [
                        "patient_table",
                        "search_bar",
                        "add_patient_button"
                    ]
                },
                {
                    "name": "Doctors",
                    "components": [
                        "doctor_table",
                        "doctor_schedule"
                    ]
                },
                {
                    "name": "Appointments",
                    "components": [
                        "appointment_calendar",
                        "book_appointment_button"
                    ]
                }
            ]
        }

    elif app_type == "food_delivery":

        return {
            "pages": [
                {
                    "name": "Login",
                    "components": [
                        "email",
                        "password",
                        "login_button"
                    ]
                },
                {
                    "name": "Restaurants",
                    "components": [
                        "restaurant_cards",
                        "search_bar",
                        "filters"
                    ]
                },
                {
                    "name": "Cart",
                    "components": [
                        "cart_items",
                        "price_summary",
                        "checkout_button"
                    ]
                },
                {
                    "name": "Checkout",
                    "components": [
                        "address_form",
                        "payment_method",
                        "confirm_order"
                    ]
                }
            ]
        }

    elif app_type == "ecommerce":

        return {
            "pages": [
                {
                    "name": "Login",
                    "components": [
                        "email",
                        "password",
                        "login_button"
                    ]
                },
                {
                    "name": "Products",
                    "components": [
                        "product_grid",
                        "search_bar",
                        "filters"
                    ]
                },
                {
                    "name": "Cart",
                    "components": [
                        "cart_items",
                        "price_summary"
                    ]
                },
                {
                    "name": "Orders",
                    "components": [
                        "orders_table",
                        "tracking_status"
                    ]
                }
            ]
        }

    else:

        return {
            "pages": [
                {
                    "name": "Login",
                    "components": [
                        "email",
                        "password",
                        "login_button"
                    ]
                },
                {
                    "name": "Dashboard",
                    "components": [
                        "cards",
                        "table"
                    ]
                }
            ]
        }