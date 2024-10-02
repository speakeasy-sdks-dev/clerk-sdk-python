"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class CreateOAuthApplicationRequestBodyTypedDict(TypedDict):
    name: str
    r"""The name of the new OAuth application"""
    callback_url: str
    r"""The callback URL of the new OAuth application"""
    scopes: NotRequired[str]
    r"""Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are `profile`, `email`, `public_metadata`, `private_metadata`. Provide the requested scopes as a string, separated by spaces."""
    public: NotRequired[bool]
    r"""If true, this client is public and cannot securely store a client secret.
    Only the authorization code flow with proof key for code exchange (PKCE) may be used.
    Public clients cannot be updated to be confidential clients, and vice versa.
    """


class CreateOAuthApplicationRequestBody(BaseModel):
    name: str
    r"""The name of the new OAuth application"""

    callback_url: str
    r"""The callback URL of the new OAuth application"""

    scopes: Optional[str] = "profile email"
    r"""Define the allowed scopes for the new OAuth applications that dictate the user payload of the OAuth user info endpoint. Available scopes are `profile`, `email`, `public_metadata`, `private_metadata`. Provide the requested scopes as a string, separated by spaces."""

    public: Optional[bool] = None
    r"""If true, this client is public and cannot securely store a client secret.
    Only the authorization code flow with proof key for code exchange (PKCE) may be used.
    Public clients cannot be updated to be confidential clients, and vice versa.
    """
