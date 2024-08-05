from datetime import datetime, timezone, date
import sqlalchemy as sa
from pydantic import ConfigDict
from sqlmodel import Field, Relationship, SQLModel
from typing import TYPE_CHECKING, Optional

class BookBase(SQLModel):
    name: str = Field(...)

class Book(BookBase , table=True):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        index=True,
    )

    updated_at: datetime | None = Field(
        default=None,
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={"onupdate": sa.func.now(), "server_default": sa.func.now()},
    )

    created_at: datetime | None = Field(
        default=None,
        sa_type=sa.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sa.func.now()},
        nullable=False,
    )