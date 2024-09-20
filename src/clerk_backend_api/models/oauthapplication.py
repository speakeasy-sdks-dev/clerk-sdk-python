"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import TypedDict


class OAuthApplicationObject(str, Enum):
    OAUTH_APPLICATION = "oauth_application"


class OAuthApplicationTypedDict(TypedDict):
    object: OAuthApplicationObject
    id: str
    instance_id: str
    name: str
    client_id: str
    public: bool
    scopes: str
    callback_url: str
    authorize_url: str
    token_fetch_url: str
    user_info_url: str
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """


class OAuthApplication(BaseModel):
    object: OAuthApplicationObject

    id: str

    instance_id: str

    name: str

    client_id: str

    public: bool

    scopes: str

    callback_url: str

    authorize_url: str

    token_fetch_url: str

    user_info_url: str

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """
