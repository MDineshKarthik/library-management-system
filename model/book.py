class Book:
    def __init__(self, db, title, author):
        self.db = db
        self.book_id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.is_borrowed = 0

    def add_to_db(self):
        self.db.cursor.execute('''
            INSERT INTO books (book_id, title, author, is_borrowed)
            VALUES (?, ?, ?, ?)
        ''', (self.book_id, self.title, self.author, self.is_borrowed))
        self.db.conn.commit()
        print(f"Book '{self.title}' added successfully.")