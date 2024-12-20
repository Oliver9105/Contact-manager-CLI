from database import Database

class Group:
    @classmethod
    def create_table(cls):
        db = Database()
        db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS groups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """)
        db.conn.commit()
