import sqlite3


class DatabaseConnection:
    """
    A class to manage database connection using SQLite3.

    This class helps establish a connection to the database, execute queries,
    and close the connection properly.
    """

    def __init__(self, db_file):
        """
        Initializes the database connection.

        Args:
            db_file (str): Path to the SQLite3 database file.
        """
        self.connection = None
        self.cursor = None
        self.db_file = db_file

        try:
            self.connect()
        except Exception as e:
            print(f"Error connecting to database: {e}")
        finally:
            self.close()

    def connect(self):
        """
        Establishes a connection to the database.
        """
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()

    def execute(self, query, params=()):
        """
        Executes a provided SQL query with optional parameters.

        Args:
            query (str): The SQL query to execute.
            params (tuple, optional): Parameters for the query (default: ()).

        Returns:
            Cursor object or None: The cursor object if the query is successful, None otherwise.
        """
        try:
            self.cursor.execute(query, params)
            return self.cursor
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            self.close()

    def commit(self):
        """
        Commits changes made to the database.
        """
        try:
            self.connection.commit()
        except Exception as e:
            print(f"Error committing changes: {e}")
        finally:
            self.close()

    def close(self):
        """
        Closes the database connection and cursor.
        """
        if self.connection:
            self.cursor.close()
            self.connection.close()
