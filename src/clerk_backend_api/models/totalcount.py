"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing_extensions import TypedDict


class TotalCountObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    TOTAL_COUNT = "total_count"


class TotalCountTypedDict(TypedDict):
    r"""Success"""

    object: TotalCountObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    total_count: int


class TotalCount(BaseModel):
    r"""Success"""

    object: TotalCountObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    total_count: int
