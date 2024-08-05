from typing import Any, Dict, Generic, Optional, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class IResponseBase(BaseModel, Generic[T]):
    message: str = ""
    meta: Optional[Dict[str, Any]] = {}
    data: Optional[T] = None


class IGetResponseBase(IResponseBase[T], Generic[T]):
    message: str = "Success"
    data: Optional[T] = None


class IPostResponseBase(IResponseBase[T], Generic[T]):
    message: str = "Created successfully"
