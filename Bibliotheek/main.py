import os
from database.database_manager import initialize_database, get_all_books, add_book, borrow_book, return_book
from reports.report_generator import generate_books_report  # For generating reports
from settings.settings import DATABASE_PATH

def display_menu():
    """Displays the main menu options to the user."""
    print("\n=== Library Management System ===")
    print("1. Add a new book")
    print("2. List all books")
    print("3. Search for a book")
    print("4. Borrow a book")
    print("5. Return a book")
    print("6. Generate books report")
    print("7. Exit")

def add_new_book():
    """Add a new book to the database."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    genre = input("Enter book genre: ")
    year = input("Enter year of publication: ")

    # Add book to database using helper function from db_manager
    add_book(title, author, genre, year)
    print("Book added successfully!")

def list_books():
    """List all books in the library."""
    books = get_all_books()
    if books:
        print("\n=== List of Books ===")
        for book in books:
            print(book)
    else:
        print("No books found.")

def search_books():
    """Search for books by title, author, or genre."""
    keyword = input("Enter a keyword to search (title, author, genre): ")

    books = search_books_in_db(keyword)
    if books:
        print("\n=== Search Results ===")
        for book in books:
            print(book)
    else:
        print("No books matched your search.")

def borrow_a_book():
    """Borrow a book from the library."""
    book_id = input("Enter the ID of the book to borrow: ")
    borrow_book(book_id)
    print("Book borrowed successfully!")

def return_a_book():
    """Return a borrowed book to the library."""
    book_id = input("Enter the ID of the book to return: ")
    return_book(book_id)
    print("Book returned successfully!")

def main():
    """Main function to run the library management application."""
    # Initialize the database (create tables if not already created)
    initialize_database()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_new_book()
        elif choice == "2":
            list_books()
        elif choice == "3":
            search_books()
        elif choice == "4":
            borrow_a_book()
        elif choice == "5":
            return_a_book()
        elif choice == "6":
            generate_books_report()  # Generate books report (CSV or Excel)
        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()