from abc import ABC, abstractmethod


# The BookCache abstract class defines the interface that all cache implementations must implement.
# This ensures that all cache implementations have the same set of methods,
# making it easy to switch between different implementations


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
