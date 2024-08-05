import secrets
import redis.asyncio as aioredis
from redis.asyncio import Redis

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPAuthorizationCredentials, HTTPBearer

from sqlalchemy.ext.asyncio import AsyncSession
from src.db.session import get_session

from src.core.config import settings


async def get_redis_client(db_num=1) -> Redis:
    redis = await aioredis.from_url(
        f"redis://{settings.REDIS_MASTER_SERVICE_HOST}:{settings.REDIS_PORT}",
        password=settings.REDIS_PASSWORD,
        max_connections=10,
        encoding="utf8",
        decode_responses=True,
        db=db_num,
    )
    return redis


bearer_security = HTTPBearer()
basic_security = HTTPBasic()




async def verify_machine(
    credentials: HTTPBasicCredentials = Depends(basic_security)
):
    username = credentials.username.encode("utf8")
    machine_username = settings.MACHINE_USERNAME.encode("utf8")
    is_correct_username = secrets.compare_digest(
        username, machine_username
    )
    password = credentials.password.encode("utf8")
    machine_password = settings.MACHINE_PASSWORD.encode("utf8")
    is_correct_password = secrets.compare_digest(
        password, machine_password
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True
