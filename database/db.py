import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                book_id TEXT PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                is_borrowed INTEGER DEFAULT 0
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                name TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS loans (
                loan_id TEXT PRIMARY KEY,
                book_id TEXT,
                user_id TEXT,
                borrow_date TEXT,
                return_date TEXT,
                FOREIGN KEY(book_id) REFERENCES books(book_id),
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )
        ''')
        self.conn.commit()

    def __del__(self):
        self.conn.close()