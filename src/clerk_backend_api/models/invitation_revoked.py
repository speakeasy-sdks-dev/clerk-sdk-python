"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import (
    BaseModel,
    Nullable,
    OptionalNullable,
    UNSET,
    UNSET_SENTINEL,
)
from enum import Enum
from pydantic import model_serializer
from typing import Optional, TypedDict
from typing_extensions import NotRequired


class InvitationRevokedObject(str, Enum):
    INVITATION = "invitation"


class InvitationRevokedPublicMetadataTypedDict(TypedDict):
    pass


class InvitationRevokedPublicMetadata(BaseModel):
    pass


class InvitationRevokedStatus(str, Enum):
    REVOKED = "revoked"


class InvitationRevokedTypedDict(TypedDict):
    r"""Success"""

    object: InvitationRevokedObject
    id: str
    email_address: str
    status: InvitationRevokedStatus
    created_at: int
    r"""Unix timestamp of creation.

    """
    updated_at: int
    r"""Unix timestamp of last update.

    """
    public_metadata: NotRequired[InvitationRevokedPublicMetadataTypedDict]
    revoked: NotRequired[bool]
    url: NotRequired[Nullable[str]]


class InvitationRevoked(BaseModel):
    r"""Success"""

    object: InvitationRevokedObject

    id: str

    email_address: str

    status: InvitationRevokedStatus

    created_at: int
    r"""Unix timestamp of creation.

    """

    updated_at: int
    r"""Unix timestamp of last update.

    """

    public_metadata: Optional[InvitationRevokedPublicMetadata] = None

    revoked: Optional[bool] = None

    url: OptionalNullable[str] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["public_metadata", "revoked", "url"]
        nullable_fields = ["url"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
