class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"You borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' was not borrowed.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        print("\nAvailable books:")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"{book.title} by {book.author} - {status}")


library = Library()

library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))

library.show_books()

library.books[0].borrow()

library.show_books()

library.books[0].return_book()

library.show_books()
