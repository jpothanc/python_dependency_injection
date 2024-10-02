# Python Dependency Injection

This project demonstrates how to implement and use dependency injection in Python.

## What is Dependency Injection?

Dependency Injection (DI) is a design pattern that allows us to develop loosely coupled code. It's a technique where one object supplies the dependencies of another object. This makes our code more modular, easier to test, and more maintainable.

## Why Use Dependency Injection?

1. **Decoupling**: It helps in reducing the dependencies between different parts of your code.
2. **Testability**: Makes unit testing easier by allowing mock objects to be injected.
3. **Flexibility**: Allows for easy swapping of implementations.
4. **Maintainability**: Makes the code easier to refactor and maintain.

## Implementation in Python
```python
def create_injector() -> Injector:
    return Injector([AppModule()])
```
```python
class AppModule(Module):
    def configure(self, binder):
        from book_cache import BookCache
        from book_memory_cache import MemoryCache
        from book_service import BookService
        # binder.bind(BookCache, DiskCache, scope=singleton)
        binder.bind(BookCache, MemoryCache, scope=singleton)
        binder.bind(BookService, BookService)
```python
class BookService:
    @inject
    def __init__(self, book_cache: BookCache):
        self.book_cache = book_cache
```

## Project Structure

```commandline
.
├── app_module.py
├── book_cache.py
├── book_disk_cache.py
├── book_memory_cache.py
├── book_service.py
└── README.md

```

## How to Run

```commandline
git clone
cd python-dependency-injection
pip install -r requirements.txt
python main.py
```

## Dependencies

injector: A Python dependency injection framework.


## License

None
