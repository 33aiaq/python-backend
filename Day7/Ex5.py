class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book.title}")
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            return "No books in the library."
        return "\n".join(book.display_info() for book in self.books)


library = Library()

book1 = Book("The Hobbit", "J.R.R. Tolkien", "978-0547928227")
book2 = Book("1984", "George Orwell", "978-0451524935")
library.add_book(book1)
library.add_book(book2)

print("\nBooks in library:")
print(library.list_books())

library.remove_book("978-0547928227")

print("\nBooks after removal:")
print(library.list_books())
