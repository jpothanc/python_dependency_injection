import logging
from book_cache import BookCache


class MemoryCache(BookCache):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.info("MemoryCache initialized")
        self.books = {}

    def get_all_books(self):
        return list(self.books.values())

    def get_book_by_id(self, book_id):
        return self.books.get(book_id)

    def create_book(self, book):
        self.books[book.id] = book
        return book

    def update_book(self, book):
        self.books[book.id] = book
        return book

    def delete_book(self, book_id):
        return self.books.pop(book_id, None) is not None
    
    