from typing import List
import requests

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


from src.db.session import get_session
from src.models.book import Book
from src.repositories.book import IntegratorRepository
from src.schemas.common import IGetResponseBase
from src.schemas.book import IBookRead, IBookCreate


router = APIRouter()

@router.get(
    '/',
    response_description="Get all integrators",
    response_model=IGetResponseBase[List[IBookRead]],
)
async def get_integrators(
    session: AsyncSession = Depends(get_session),
)  -> IGetResponseBase[List[IBookRead]]:
    integrator_repo = IntegratorRepository(db=session)
    integrators = await integrator_repo.all()

    return IGetResponseBase[List[IBookRead]](data=integrators)

@router.post(
    '/',
    response_description="Create new integrator",
    response_model=IGetResponseBase[IBookCreate]
)
async def create_integrator(
    integrator: IBookCreate,
    session: AsyncSession = Depends(get_session),
) -> IGetResponseBase[IBookCreate]:
    integrator_repo = IntegratorRepository(db=session)
    integrator_resp = await integrator_repo.create(
        integrator
    )

    return IGetResponseBase[IBookCreate](data=integrator_resp)