from src.models.book import BookBase

class IBookRead(BookBase):
    id : int

class IBookCreate(BookBase):
    name : str