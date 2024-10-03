import json
import logging
import os

from book_cache import BookCache

# The DiskCache class is a cache implementation that stores books in a JSON file on disk.
class DiskCache(BookCache):
    def __init__(self, file_path='books_cache.json'):
        self.logger = logging.getLogger(__name__)
        self.logger.info("DiskCache initialized")
        self.file_path = file_path
        self.books = {}
        self.load_from_disk()

    def load_from_disk(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                self.books = json.load(f)

    def save_to_disk(self):
        with open(self.file_path, 'w') as f:
            json.dump(self.books, f, indent=2)

    def get_all_books(self):
        return list(self.books.values())

    def get_book_by_id(self, book_id):
        return self.books.get(str(book_id))

    def create_book(self, book):
        self.books[str(book.id)] = book.__dict__
        self.save_to_disk()
        return book

    def update_book(self, book):
        self.books[str(book.id)] = book.__dict__
        self.save_to_disk()
        return book

    def delete_book(self, book_id):
        result = self.books.pop(str(book_id), None) is not None
        if result:
            self.save_to_disk()
        return result

