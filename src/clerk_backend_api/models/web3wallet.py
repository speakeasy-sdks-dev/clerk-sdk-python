"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from clerk_backend_api.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from enum import Enum
from pydantic import model_serializer
from typing import Optional, TypedDict, Union
from typing_extensions import NotRequired


class Web3WalletObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    WEB3_WALLET = "web3_wallet"

class AdminVerificationWeb3WalletStatus(str, Enum):
    VERIFIED = "verified"

class AdminVerificationWeb3WalletStrategy(str, Enum):
    ADMIN = "admin"
    FROM_OAUTH_DISCORD = "from_oauth_discord"

class Web3WalletVerificationAdminTypedDict(TypedDict):
    status: AdminVerificationWeb3WalletStatus
    strategy: AdminVerificationWeb3WalletStrategy
    attempts: NotRequired[Nullable[int]]
    expire_at: NotRequired[Nullable[int]]
    

class Web3WalletVerificationAdmin(BaseModel):
    status: AdminVerificationWeb3WalletStatus
    strategy: AdminVerificationWeb3WalletStrategy
    attempts: OptionalNullable[int] = UNSET
    expire_at: OptionalNullable[int] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["attempts", "expire_at"]
        nullable_fields = ["attempts", "expire_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class Web3SignatureVerificationStatus(str, Enum):
    VERIFIED = "verified"

class Web3SignatureVerificationStrategy(str, Enum):
    WEB3_METAMASK_SIGNATURE = "web3_metamask_signature"

class Nonce(str, Enum):
    NONCE = "nonce"

class Web3SignatureTypedDict(TypedDict):
    status: Web3SignatureVerificationStatus
    strategy: Web3SignatureVerificationStrategy
    nonce: Nonce
    attempts: NotRequired[Nullable[int]]
    expire_at: NotRequired[Nullable[int]]
    

class Web3Signature(BaseModel):
    status: Web3SignatureVerificationStatus
    strategy: Web3SignatureVerificationStrategy
    nonce: Nonce
    attempts: OptionalNullable[int] = UNSET
    expire_at: OptionalNullable[int] = UNSET
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["attempts", "expire_at"]
        nullable_fields = ["attempts", "expire_at"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

Web3WalletVerificationTypedDict = Union[Web3WalletVerificationAdminTypedDict, Web3SignatureTypedDict]


Web3WalletVerification = Union[Web3WalletVerificationAdmin, Web3Signature]


class Web3WalletTypedDict(TypedDict):
    object: Web3WalletObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    web3_wallet: str
    verification: Nullable[Web3WalletVerificationTypedDict]
    created_at: int
    r"""Unix timestamp of creation

    """
    updated_at: int
    r"""Unix timestamp of creation

    """
    id: NotRequired[str]
    

class Web3Wallet(BaseModel):
    object: Web3WalletObject
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    web3_wallet: str
    verification: Nullable[Web3WalletVerification]
    created_at: int
    r"""Unix timestamp of creation

    """
    updated_at: int
    r"""Unix timestamp of creation

    """
    id: Optional[str] = None
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["id"]
        nullable_fields = ["verification"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        
