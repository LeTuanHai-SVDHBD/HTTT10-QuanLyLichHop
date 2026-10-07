from sqlalchemy import create_engine


class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)

            connection_string = (
                "mssql+pyodbc://localhost/HTTT10"
                "?driver=ODBC+Driver+17+for+SQL+Server"
                "&trusted_connection=yes"
            )

            cls._instance.engine = create_engine(
                connection_string,
                echo=True
            )

        return cls._instance