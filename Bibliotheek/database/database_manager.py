import sqlite3
from settings.settings import DATABASE_PATH  # Import the database path from settings

def initialize_database():
    """Creates the database and necessary tables if they don't already exist."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create Books table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            genre TEXT,
            year INTEGER,
            available BOOLEAN DEFAULT 1
        )
    """)

    conn.commit()
    conn.close()

def get_all_books():
    """Returns a list of all books in the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    conn.close()
    return books

def add_book(title, author, genre, year):
    """Adds a new book to the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Books (title, author, genre, year)
        VALUES (?, ?, ?, ?)
    """, (title, author, genre, year))
    conn.commit()
    conn.close()

def borrow_book(book_id):
    """Marks a book as borrowed."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Books
        SET available = 0
        WHERE id = ? AND available = 1
    """, (book_id,))
    conn.commit()
    conn.close()

def return_book(book_id):
    """Marks a book as returned."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE Books
        SET available = 1
        WHERE id = ? AND available = 0
    """, (book_id,))
    conn.commit()
    conn.close()