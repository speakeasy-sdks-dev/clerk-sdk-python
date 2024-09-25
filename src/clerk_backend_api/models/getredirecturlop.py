"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class GetRedirectURLRequestTypedDict(TypedDict):
    id: str
    r"""The ID of the redirect URL"""


class GetRedirectURLRequest(BaseModel):
    id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the redirect URL"""
