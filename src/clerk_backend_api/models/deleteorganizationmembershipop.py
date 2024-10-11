"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata
from typing_extensions import Annotated, TypedDict


class DeleteOrganizationMembershipRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization the membership belongs to"""
    user_id: str
    r"""The ID of the user that this membership belongs to"""


class DeleteOrganizationMembershipRequest(BaseModel):
    organization_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the organization the membership belongs to"""

    user_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the user that this membership belongs to"""
