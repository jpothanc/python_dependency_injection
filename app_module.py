from typing import Annotated
from injector import Module, singleton


# This is the main module that binds the interfaces to the implementations This approach allows you to centralize and
# manage all your dependency bindings in one place, making it easier to maintain and modify your application's
# dependency structure. By subclassing Module and implementing the configure method, you're essentially telling the
# injector library, "Here's how I want my application's dependencies to be set up." This is a key part of the
# dependency injection pattern, allowing you to decouple the configuration of objects from their usage.

class AppModule(Module):
    def configure(self, binder):
        from book_cache import BookCache
        from book_memory_cache import MemoryCache
        from book_disk_cache import DiskCache
        from book_service import BookService

        # binder.bind(BookCache, DiskCache, scope=singleton)
        binder.bind(BookCache, MemoryCache, scope=singleton)

        # Bind both cache implementations with annotations
        # binder.bind(Annotated[BookCache, "memory"], MemoryCache)
        # binder.bind(Annotated[BookCache, "disk"], DiskCache)

        binder.bind(BookService, BookService)
