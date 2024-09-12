"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing import TypedDict
from typing_extensions import Annotated


class DeleteSAMLConnectionRequestTypedDict(TypedDict):
    saml_connection_id: str
    r"""The ID of the SAML Connection to delete"""


class DeleteSAMLConnectionRequest(BaseModel):
    saml_connection_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the SAML Connection to delete"""
