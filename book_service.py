import logging
from injector import inject
from book import Book
from book_cache import BookCache


# The BookService class is the main service class that interacts with the BookCache.
class BookService:

    @inject
    def __init__(self, book_cache: BookCache):
        """
        Constructor for BookService
        :param book_cache:
        The @inject decorator tells the injector
        which BookCache implementation to use.
        """
        self.book_cache = book_cache
        self.logger = logging.getLogger(__name__)
        self.logger.info("BookService initialized")

    def get_all_books(self) -> list[Book]:
        return self.book_cache.get_all_books()

    def get_book_by_id(self, book_id) -> Book:
        return self.book_cache.get_book_by_id(book_id)

    def create_book(self, book) -> Book:
        return self.book_cache.create_book(book)

    def update_book(self, book) -> Book:
        return self.book_cache.update_book(book)

    def delete_book(self, book_id) -> bool:
        return self.book_cache.delete_book(book_id)
