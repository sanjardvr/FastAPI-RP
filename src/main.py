import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.api import routes
from src.api.deps import get_redis_client
from src.core.config import settings
from src.db.session import add_postgresql_extension


logger = logging.getLogger(__name__)


# tags_metadata = [
#     {
#         "name": "health",
#         "description": "Health check for api",
#     },
# ]

app = FastAPI(
    title="Simple API",
    description="api on FastAPI python Repository Pattern",
    version=settings.VERSION,
    openapi_url=f"/{settings.API_PREFIX}/openapi.json",
    # openapi_tags=tags_metadata,
)


async def on_startup() -> None:
    await add_postgresql_extension()
    redis_client = await get_redis_client()
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    logger.info("FastAPI app running...")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", on_startup)

app.include_router(routes.home_router)

app.include_router(routes.api_router, prefix=f"/{settings.API_PREFIX}")
