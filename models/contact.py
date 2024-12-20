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

    @classmethod
    def delete_contact(cls, contact_id):
        db = Database()
        db.cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        db.conn.commit()
