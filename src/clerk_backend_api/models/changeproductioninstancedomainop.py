"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel
from typing import Optional
from typing_extensions import NotRequired, TypedDict


class ChangeProductionInstanceDomainRequestBodyTypedDict(TypedDict):
    home_url: NotRequired[str]
    r"""The new home URL of the production instance e.g. https://www.example.com"""


class ChangeProductionInstanceDomainRequestBody(BaseModel):
    home_url: Optional[str] = None
    r"""The new home URL of the production instance e.g. https://www.example.com"""
