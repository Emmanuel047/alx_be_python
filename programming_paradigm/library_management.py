class Book:
    def __init__(self, title, author):
        self.title = title          # public attribute
        self.author = author        # public attribute
        self._is_checked_out = False  # private attribute to track availability

    def is_available(self):
        return not self._is_checked_out

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self._books = []  # private list to store Book instances

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"Checked out '{title}' successfully."
        return f"Book '{title}' is not available for checkout."

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"Returned '{title}' successfully."
        return f"Book '{title}' was not checked out."

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            return "No books available."
        return [f"{book.title} by {book.author}" for book in available_books]