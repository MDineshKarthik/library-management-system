# Library Management System

A simple Library Management System built with Python and SQLite. This project provides an interactive command-line interface (CLI) to manage books, users, and loans for a library.

---

## Features

- **Add Book**: Register new books with title and author.
- **Add User**: Register library users.
- **Borrow Book**: Borrow a book by providing its ID and the user ID.
- **Return Book**: Return a borrowed book.
- **List Books**: Display all books with their status (Available/Borrowed).
- **List Users**: Display all registered users.

---

## Tech Stack

- **Language**: Python
- **Database**: SQLite (via `sqlite3` module)
- **Structure**:
  - `main.py`: Main CLI and application entry point
  - `database/db.py`: Database initialization and connection
  - `model/book.py`: Book model and database logic
  - `model/user.py`: User model and database logic
  - `model/loan.py`: Loan (borrow/return) logic

---

## Getting Started

### Prerequisites

- Python 3.x installed

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/MDineshKarthik/library-management-system.git
   cd library-management-system
   ```

2. **Install dependencies:**
   No external dependencies required; uses Python standard library (`sqlite3`, `uuid`, `datetime`).

### Running the Application

```sh
python main.py
```

You will see a menu with options to add books, add users, borrow/return books, list books/users, or exit.

---

## Usage

- **Add Book**: Enter book title and author when prompted.
- **Add User**: Enter the user's name.
- **Borrow Book**: Enter the book ID and user ID (IDs are shown in the list).
- **Return Book**: Enter the book ID to return it.
- **List Books/Users**: Displays current records.

---

## Project Structure

```
library-management-system/
├── main.py
├── database/
│   └── db.py
└── model/
    ├── book.py
    ├── user.py
    └── loan.py
```

---

## License

This project is open source. See [LICENSE](LICENSE) for details.

---

## Author

- [MDineshKarthik](https://github.com/MDineshKarthik)
