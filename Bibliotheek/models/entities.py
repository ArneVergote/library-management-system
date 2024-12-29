class Book:
    """Represents a book in the library."""
    def __init__(self, id, title, author, genre, year, available=True):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} ({self.year}) - {status}"
