import sqlite3

class Database:
    def __init__(self, db_name="db/contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()
