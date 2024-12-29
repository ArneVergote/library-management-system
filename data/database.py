import sqlite3

# Path to your database
DATABASE_PATH = "data/database.db"

# Create a connection to the database
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

# Create the Books table
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

# Insert sample books
cursor.executemany("""
    INSERT INTO Books (title, author, genre, year, available) VALUES (?, ?, ?, ?, ?)
""", [
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 1),
    ('1984', 'George Orwell', 'Dystopian', 1949, 1),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classics', 1925, 1),
    ('Moby Dick', 'Herman Melville', 'Adventure', 1851, 1),
    ('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 1)
])

# Commit and close the connection
conn.commit()
conn.close()

print("Database and sample data created successfully!")
