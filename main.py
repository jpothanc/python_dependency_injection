import logging
import os
from injector import Injector

from app_module import AppModule
from book import Book
from book_service import BookService


def create_injector() -> Injector:
    return Injector([AppModule()])


def setup_logging():
    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Set up logging configuration
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('logs/app.log'),
            logging.StreamHandler()
        ]
    )


if __name__ == '__main__':
    injector = create_injector()
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Application started")

    book_service = injector.get(BookService);

    # create 3 books and add them to the cache
    book1 = Book(id=1, title='To Kill a Mockingbird', author='Harper Lee', price=12.99)
    book_service.create_book(book1)

    book2 = Book(id=2, title='1984', author='George Orwell', price=10.99)
    book_service.create_book(book2)

    book3 = Book(id=3, title='The Alchemist', author='Paulo Coelho', price=9.99)
    book_service.create_book(book3)

    book1 = book_service.get_book_by_id(3)
    print(book1)

    logger.info("Application finished")
