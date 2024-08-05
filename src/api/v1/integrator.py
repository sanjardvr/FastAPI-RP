from typing import List
import requests

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from src.db.session import get_session
from src.models.integrator import Integrator
from src.repositories.integrator import IntegratorRepository
from src.schemas.common import IGetResponseBase
from src.schemas.integrator import IIntegratorRead, IIntegratorCreate


router = APIRouter()

@router.get(
    '/',
    response_description="Get all integrators",
    response_model=IGetResponseBase[List[IIntegratorRead]],
)
async def get_integrators(
    session: AsyncSession = Depends(get_session),
)  -> IGetResponseBase[List[IIntegratorRead]]:
    integrator_repo = IntegratorRepository(db=session)
    integrators = await integrator_repo.all()

    return IGetResponseBase[List[IIntegratorRead]](data=integrators)

@router.post(
    '/',
    response_description="Create new integrator",
    response_model=IGetResponseBase[IIntegratorCreate]
)
async def create_integrator(
    integrator: IIntegratorCreate,
    session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[IIntegratorCreate]:
    integrator_repo = IntegratorRepository(db=session)
    integrator_resp = await integrator_repo.create(
        integrator
    )

    return IGetResponseBase[IIntegratorCreate](data=integrator_resp)