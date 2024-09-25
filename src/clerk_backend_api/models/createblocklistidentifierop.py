"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from typing import TypedDict


class CreateBlocklistIdentifierRequestBodyTypedDict(TypedDict):
    identifier: str
    r"""The identifier to be added in the block-list.
    This can be an email address, a phone number or a web3 wallet.
    """


class CreateBlocklistIdentifierRequestBody(BaseModel):
    identifier: str
    r"""The identifier to be added in the block-list.
    This can be an email address, a phone number or a web3 wallet.
    """
