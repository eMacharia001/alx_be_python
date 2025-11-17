# library_system.py

# Base Class
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}MB"


# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author}, Pages: {self.page_count}"


# Composition Class: Library
class Library:
    def __init__(self):
        self.books = []  # List to store Book instances

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)
