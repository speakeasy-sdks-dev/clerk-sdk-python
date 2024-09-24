"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, PathParamMetadata, RequestMetadata
from typing import Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class VerifySessionRequestBodyTypedDict(TypedDict):
    r"""Parameters."""

    token: NotRequired[str]
    r"""The JWT that is sent via the `__session` cookie from your frontend.
    Note: this JWT must be associated with the supplied session ID.
    """


class VerifySessionRequestBody(BaseModel):
    r"""Parameters."""

    token: Optional[str] = None
    r"""The JWT that is sent via the `__session` cookie from your frontend.
    Note: this JWT must be associated with the supplied session ID.
    """


class VerifySessionRequestTypedDict(TypedDict):
    session_id: str
    r"""The ID of the session"""
    request_body: NotRequired[VerifySessionRequestBodyTypedDict]
    r"""Parameters."""


class VerifySessionRequest(BaseModel):
    session_id: Annotated[
        str, FieldMetadata(path=PathParamMetadata(style="simple", explode=False))
    ]
    r"""The ID of the session"""

    request_body: Annotated[
        Optional[VerifySessionRequestBody],
        FieldMetadata(request=RequestMetadata(media_type="application/json")),
    ] = None
    r"""Parameters."""
