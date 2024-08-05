from src.models.integrator import IntegratorBase

class IIntegratorRead(IntegratorBase):
    id : int

class IIntegratorCreate(IntegratorBase):
    name : str