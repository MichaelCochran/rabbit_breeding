import sqlite3

class DatabaseHelper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS rabbits (
                name TEXT,
                last_bred TEXT,
                buck TEXT,
                palpatate TEXT,
                nest_date TEXT,
                due_date TEXT,
                comments TEXT
            )
        ''')

    def insert_data(self, name, bred, buck, palpitating, nest, due, comments):
        try:
            self.cur.execute("INSERT INTO rabbits VALUES (?, ?, ?, ?, ?, ?, ?)", 
                             (name, bred, buck, palpitating, nest, due, comments))
            self.conn.commit()
            print("\nData added to file")
        except Exception as e:
            print("Error:", e)

    def view_data(self):
        self.cur.execute("SELECT * FROM rabbits")
        return self.cur.fetchall()

    def close_connection(self):
        self.conn.close()