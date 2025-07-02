from datetime import datetime

class Loan:
    def __init__(self, db, book_id, user_id):
        self.db = db
        self.loan_id = str(uuid.uuid4())
        self.book_id = book_id
        self.user_id = user_id
        self.borrow_date = datetime.now().strftime('%Y-%m-%d')
        self.return_date = None

    def borrow_book(self):
        self.db.cursor.execute('SELECT is_borrowed FROM books WHERE book_id = ?', (self.book_id,))
        result = self.db.cursor.fetchone()
        if result and result[0] == 0:
            self.db.cursor.execute('''
                INSERT INTO loans (loan_id, book_id, user_id, borrow_date)
                VALUES (?, ?, ?, ?)
            ''', (self.loan_id, self.book_id, self.user_id, self.borrow_date))
            self.db.cursor.execute('UPDATE books SET is_borrowed = 1 WHERE book_id = ?', (self.book_id,))
            self.db.conn.commit()
            print("Book borrowed successfully.")
        else:
            print("Book is already borrowed or does not exist.")

    def return_book(self):
        self.db.cursor.execute('SELECT * FROM loans WHERE book_id = ? AND return_date IS NULL', (self.book_id,))
        result = self.db.cursor.fetchone()
        if result:
            self.return_date = datetime.now().strftime('%Y-%m-%d')
            self.db.cursor.execute('''
                UPDATE loans SET return_date = ? WHERE loan_id = ?
            ''', (self.return_date, result[0]))
            self.db.cursor.execute('UPDATE books SET is_borrowed = 0 WHERE book_id = ?', (self.book_id,))
            self.db.conn.commit()
            print("Book returned successfully.")
        else:
            print("No active loan found for this book.")