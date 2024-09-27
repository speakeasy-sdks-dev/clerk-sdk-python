"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class UpdateOrganizationMembershipMetadataPublicMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization membership, that is visible to both your frontend and backend.
    The new object will be merged with the existing value.
    """


class UpdateOrganizationMembershipMetadataPublicMetadata(BaseModel):
    r"""Metadata saved on the organization membership, that is visible to both your frontend and backend.
    The new object will be merged with the existing value.
    """


class UpdateOrganizationMembershipMetadataPrivateMetadataTypedDict(TypedDict):
    r"""Metadata saved on the organization membership that is only visible to your backend.
    The new object will be merged with the existing value.
    """


class UpdateOrganizationMembershipMetadataPrivateMetadata(BaseModel):
    r"""Metadata saved on the organization membership that is only visible to your backend.
    The new object will be merged with the existing value.
    """


class UpdateOrganizationMembershipMetadataRequestBodyTypedDict(TypedDict):
    public_metadata: NotRequired[
        UpdateOrganizationMembershipMetadataPublicMetadataTypedDict
    ]
    r"""Metadata saved on the organization membership, that is visible to both your frontend and backend.
    The new object will be merged with the existing value.
    """
    private_metadata: NotRequired[
        UpdateOrganizationMembershipMetadataPrivateMetadataTypedDict
    ]
    r"""Metadata saved on the organization membership that is only visible to your backend.
    The new object will be merged with the existing value.
    """


class UpdateOrganizationMembershipMetadataRequestBody(BaseModel):
    public_metadata: Optional[UpdateOrganizationMembershipMetadataPublicMetadata] = None
    r"""Metadata saved on the organization membership, that is visible to both your frontend and backend.
    The new object will be merged with the existing value.
    """

    private_metadata: Optional[UpdateOrganizationMembershipMetadataPrivateMetadata] = (
        None
    )
    r"""Metadata saved on the organization membership that is only visible to your backend.
    The new object will be merged with the existing value.
    """


class UpdateOrganizationMembershipMetadataRequestTypedDict(TypedDict):
    organization_id: str
    r"""The ID of the organization the membership belongs to"""
    user_id: str
    r"""The ID of the user that this membership belongs to"""
    request_body: UpdateOrganizationMembershipMetadataRequestBodyTypedDict


class UpdateOrganizationMembershipMetadataRequest(BaseModel):
    organization_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the organization the membership belongs to"""

    user_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the user that this membership belongs to"""

    request_body: Annotated[
        UpdateOrganizationMembershipMetadataRequestBody,
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ]
