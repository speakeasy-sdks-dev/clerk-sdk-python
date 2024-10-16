"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .samlconnections import SAMLConnections, SAMLConnectionsTypedDict
from clerk_backend_api.types import BaseModel
from clerk_backend_api.utils import FieldMetadata, QueryParamMetadata
from typing import Callable, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class ListSAMLConnectionsRequestTypedDict(TypedDict):
    limit: NotRequired[float]
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: NotRequired[float]
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    

class ListSAMLConnectionsRequest(BaseModel):
    limit: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Applies a limit to the number of results returned.
    Can be used for paginating the results together with `offset`.
    """
    offset: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    r"""Skip the first `offset` results when paginating.
    Needs to be an integer greater or equal to zero.
    To be used in conjunction with `limit`.
    """
    

class ListSAMLConnectionsResponseTypedDict(TypedDict):
    result: SAMLConnectionsTypedDict
    

class ListSAMLConnectionsResponse(BaseModel):
    next: Callable[[], Optional[ListSAMLConnectionsResponse]]
    
    result: SAMLConnections
    
