"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from enum import Enum
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class OAuthApplicationWithSecretObject(str, Enum):
    OAUTH_APPLICATION = "oauth_application"


class OAuthApplicationWithSecretTypedDict(TypedDict):
    object: OAuthApplicationWithSecretObject
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
    client_secret: NotRequired[str]
    r"""Empty if public client.

    """


class OAuthApplicationWithSecret(BaseModel):
    object: OAuthApplicationWithSecretObject

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

    client_secret: Optional[str] = None
    r"""Empty if public client.

    """
