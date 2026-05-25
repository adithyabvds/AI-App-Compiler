def generate_summary(
    intent,
    ui,
    api,
    database
):

    pages = [
        page["name"]
        for page in ui["pages"]
    ]

    endpoints = list(
        set(
            endpoint["path"]
            for endpoint in api["endpoints"]
        )
    )

    tables = [
        table["name"]
        for table in database["tables"]
    ]

    return {
        "application_type":
            intent["app_type"],

        "features":
            intent["features"],

        "pages":
            pages,

        "api_endpoints":
            endpoints,

        "database_tables":
            tables,

        "description":
            f"{intent['app_type']} application generated successfully"
    }