"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class JWTTemplateObject(str, Enum):
    JWT_TEMPLATE = "jwt_template"


class ClaimsTypedDict(TypedDict):
    pass


class Claims(BaseModel):
    pass


class JWTTemplateTypedDict(TypedDict):
    r"""List of JWT templates"""

    object: JWTTemplateObject
    id: str
    name: str
    claims: ClaimsTypedDict
    lifetime: int
    allowed_clock_skew: int
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    custom_signing_key: NotRequired[bool]
    signing_algorithm: NotRequired[str]


class JWTTemplate(BaseModel):
    r"""List of JWT templates"""

    object: JWTTemplateObject

    id: str

    name: str

    claims: Claims

    lifetime: int

    allowed_clock_skew: int

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """

    custom_signing_key: Optional[bool] = None

    signing_algorithm: Optional[str] = None
