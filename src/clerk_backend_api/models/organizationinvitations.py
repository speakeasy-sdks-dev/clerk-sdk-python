"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .organizationinvitation import (
    OrganizationInvitation,
    OrganizationInvitationTypedDict,
)
from clerk_backend_api.types import BaseModel
from typing import List, TypedDict


class OrganizationInvitationsTypedDict(TypedDict):
    data: List[OrganizationInvitationTypedDict]
    total_count: int
    r"""Total number of organization invitations

    """


class OrganizationInvitations(BaseModel):
    data: List[OrganizationInvitation]

    total_count: int
    r"""Total number of organization invitations

    """
