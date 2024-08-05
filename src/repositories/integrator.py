from src.models.integrator import Integrator
from src.repositories.sqlalchemy import BaseSQLAlchemyRepository
from src.schemas.integrator import IIntegratorRead, IIntegratorCreate

class IntegratorRepository(BaseSQLAlchemyRepository[Integrator, IIntegratorRead, IIntegratorCreate]):
    _model = Integrator
