from fastapi import APIRouter, status
from fastapi.responses import PlainTextResponse, Response

from src.api.v1 import integrator


home_router = APIRouter()


@home_router.get("/", response_description="Homepage", include_in_schema=False)
async def home() -> Response:
    return PlainTextResponse("SimpleAPI", status_code=status.HTTP_200_OK)


api_router = APIRouter()
api_router.include_router(integrator.router, tags=["Integrator"], prefix="/integrator")
