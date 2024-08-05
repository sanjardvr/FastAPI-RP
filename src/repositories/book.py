from src.models.book import Book
from src.repositories.sqlalchemy import BaseSQLAlchemyRepository
from src.schemas.book import IBookCreate, IBookRead

class IntegratorRepository(BaseSQLAlchemyRepository[Book, IBookRead, IBookCreate]):
    _model = Book
