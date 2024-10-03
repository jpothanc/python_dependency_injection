from dataclasses import dataclass



# Book class is a simple data class that represents a book.
@dataclass
class Book:
    id: int
    title: str
    author: str
    price: float

