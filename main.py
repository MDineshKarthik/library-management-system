from database.db import Database
from model.book import Book
from model.user import User
from model.loan import Loan
import uuid

class LibrarySystem:
    def __init__(self):
        self.db = Database()

    def add_book(self, title, author):
        book = Book(self.db, title, author)
        book.add_to_db()

    def add_user(self, name):
        user = User(self.db, name)
        user.add_to_db()

    def borrow_book(self, book_id, user_id):
        loan = Loan(self.db, book_id, user_id)
        loan.borrow_book()

    def return_book(self, book_id):
        loan = Loan(self.db, book_id, None)
        loan.return_book()

    def list_books(self):
        self.db.cursor.execute('SELECT book_id, title, author, is_borrowed FROM books')
        books = self.db.cursor.fetchall()
        if books:
            for book in books:
                status = "Borrowed" if book[3] == 1 else "Available"
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {status}")
        else:
            print("No books available.")

    def list_users(self):
        self.db.cursor.execute('SELECT user_id, name FROM users')
        users = self.db.cursor.fetchall()
        if users:
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}")
        else:
            print("No users registered.")

def main():
    library = LibrarySystem()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add User")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. List Books")
        print("6. List Users")
        print("7. Exit")
        choice = input("Enter choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '2':
            name = input("Enter user name: ")
            library.add_user(name)
        elif choice == '3':
            book_id = input("Enter book ID: ")
            user_id = input("Enter user ID: ")
            library.borrow_book(book_id, user_id)
        elif choice == '4':
            book_id = input("Enter book ID: ")
            library.return_book(book_id)
        elif choice == '5':
            library.list_books()
        elif choice == '6':
            library.list_users()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()