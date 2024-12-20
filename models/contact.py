from database import Database

class Contact:
    @classmethod
    def create_table(cls):
        db = Database()
        db.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        db.conn.commit()
