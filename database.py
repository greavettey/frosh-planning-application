import sqlite3

#singleton class is goated that way i'm not opening a new database connection every time i want to query something. 
class Database:
    """Singleton class representing a database connection. Use the get_instance() method to get the instance of this class."""

    def __init__(self, db_file: str):
        self.db_file = db_file
        self.conn = self.create_connection(db_file)

    @staticmethod
    def create_connection(db_file: str):
        """Create a database connection to the SQLite database. Creates it if no file exists with the given name."""
        with sqlite3.connect(db_file) as conn:
            return conn
    
    # I get so lazy doing sql. In node they have nice helper libraries to make pretty sql queries with lots of safety nets. I'm to lazy to do that here I'll just manually write my statements. 
    def execute(self, sql: str, parameters=()):
        """Execute a SQL statement with optional parameters."""
        try:
            c = self.conn.cursor()
            c.execute(sql, parameters)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
    def save(self):
        """Commit the current transaction."""
        self.conn.commit()

_instance = None 

def init_database(db_file: str):
    """Initialize the database connection. This should be called once at the start of the application."""
    global _instance
    if _instance is None:
        _instance = Database(db_file)
    else:
        raise Exception("Database has already been initialized.")

def get_database():
    """Get the database instance. This should be called after init_database() has been called."""
    global _instance
    if _instance is None:
        raise Exception("Database has not been initialized.")
    return _instance