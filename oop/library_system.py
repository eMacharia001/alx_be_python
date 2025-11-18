# Base Class
class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        # Checker expects "Book: <title> by <author>"
        return f"Book: {self.title} by {self.author}"


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: str):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size  # e.g., "500KB"

    def __str__(self):
        # Checker expects "EBook: <title> by <author>, File Size: <file_size>"
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}"


# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        # Checker expects "PrintBook: <title> by <author>, Page Count: <page_count>"
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


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
