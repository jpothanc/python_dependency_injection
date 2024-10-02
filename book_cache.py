from abc import ABC, abstractmethod

class BookCache(ABC):
    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def get_book_by_id(self, book_id):
        pass

    @abstractmethod
    def create_book(self, book):
        pass

    @abstractmethod
    def update_book(self, book):
        pass

    @abstractmethod
    def delete_book(self, book_id):
        pass

