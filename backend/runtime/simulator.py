import sqlite3


def simulate(config):

    try:

        conn = sqlite3.connect(
            ":memory:"
        )

        cursor = conn.cursor()

        tables_created = []

        for table in config[
            "database"
        ]["tables"]:

            table_name = table["name"]

            columns = table["columns"]

            sql_columns = []

            for column in columns:

                sql_columns.append(
                    f"{column} TEXT"
                )

            query = f"""
            CREATE TABLE
            {table_name}
            (
                {",".join(sql_columns)}
            )
            """

            cursor.execute(query)

            tables_created.append(
                table_name
            )

        conn.commit()

        # Test query

        cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            """
        )

        result = cursor.fetchall()

        conn.close()

        return {
            "status": "passed",
            "tables_created":
                tables_created,
            "tables_count":
                len(result),
            "runtime":
                "sqlite"
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }