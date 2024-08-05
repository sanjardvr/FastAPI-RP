import logging
from typing import Any, List, Optional

from pydantic import AnyHttpUrl, Field, PostgresDsn, field_validator, ValidationInfo
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    # SERVER_NAME: Optional[str] = Field(..., env="NGINX_HOST")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    API_URL: str = Field(default="", env="API_URL")
    API_TOKEN: str = Field(default="", env="API_TOKEN")
    LOG_LEVEL: int = Field(default=logging.INFO, env="LOG_LEVEL")

    VERSION: str = Field(default="0.1.0", env="VERSION")
    API_PREFIX: str = Field(default="api", env="API_PREFIX")
    DEBUG: bool = Field(default=True, env="DEBUG")

    JWT_SECRET: str = Field(default="", env="JWT_SECRET")
    JWT_ALGORITHM: str = Field(default="", env="JWT_ALGORITHM")
    JWT_REFRESH_SECRET: str = Field(default="", env="JWT_REFRESH_SECRET")
    SALT: str = Field(default="", env="SALT")

    POSTGRES_USER: str = Field(default="", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(default="", env="POSTGRES_PASSWORD")
    POSTGRES_HOST: str = Field(default="", env="POSTGRES_HOST")
    POSTGRES_PORT: str = Field(default="", env="POSTGRES_PORT")
    POSTGRES_DB: str = Field(default="", env="POSTGRES_DB")
    POSTGRES_URL: Optional[str] = None

    MAIL_USERNAME: str = Field(default="", env="MAIL_USERNAME")
    MAIL_PASSWORD: str = Field(default="", env="MAIL_PASSWORD")
    MAIL_FROM: str = Field(default="", env="MAIL_FROM")
    MAIL_PORT: str = Field(default="", env="MAIL_PORT")
    MAIL_SERVER: str = Field(default="", env="MAIL_SERVER")
    MAIL_FROM_NAME: str = Field(default="", env="MAIL_FROM_NAME")

    AWS_ACCESS_KEY_ID: str = Field(default="", env="AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = Field(default="", env="AWS_SECRET_ACCESS_KEY")
    AWS_DEFAULT_REGION: str = Field(default="", env="AWS_DEFAULT_REGION")

    MACHINE_USERNAME: str = Field(default="", env="MACHINE_USERNAME")
    MACHINE_PASSWORD: str = Field(default="", env="MACHINE_PASSWORD")

    REDIS_MASTER_SERVICE_HOST: str = Field(default="", env="REDIS_MASTER_SERVICE_HOST")
    REDIS_PORT: str = Field(default="", env="REDIS_PORT")
    REDIS_PASSWORD: str = Field(default="", env="REDIS_PASSWORD")

    DB_POOL_SIZE: int = Field(default=83, env="DB_POOL_SIZE")
    WEB_CONCURRENCY: int = Field(default=9, env="WEB_CONCURRENCY")
    MAX_OVERFLOW: int = Field(default=64, env="MAX_OVERFLOW")
    POOL_SIZE: Optional[int] = None

    @field_validator("POOL_SIZE", mode="before")
    def build_pool(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, int):
            return v

        return max(values.data.get("DB_POOL_SIZE") // values.data.get("WEB_CONCURRENCY"), 5)  # type: ignore

    @field_validator("POSTGRES_URL", mode="plain")
    def build_db_connection(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_HOST"),
            port=int(values.data.get("POSTGRES_PORT")),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        ).unicode_string()


settings = Settings()
