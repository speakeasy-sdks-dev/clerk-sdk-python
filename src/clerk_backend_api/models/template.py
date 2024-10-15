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
from typing import List, Optional
from typing_extensions import NotRequired, TypedDict


class TemplateObject(str, Enum):
    r"""String representing the object's type. Objects of the same type share the same value."""

    TEMPLATE = "template"


class TemplateTypedDict(TypedDict):
    r"""Success"""

    id: NotRequired[str]
    object: NotRequired[TemplateObject]
    r"""String representing the object's type. Objects of the same type share the same value.

    """
    instance_id: NotRequired[Nullable[str]]
    r"""the id of the instance the template belongs to"""
    resource_type: NotRequired[str]
    r"""whether this is a system (default) or user overridden) template"""
    template_type: NotRequired[str]
    r"""whether this is an email or SMS template"""
    name: NotRequired[str]
    r"""user-friendly name of the template"""
    slug: NotRequired[str]
    r"""machine-friendly name of the template"""
    position: NotRequired[int]
    r"""position with the listing of templates"""
    can_revert: NotRequired[bool]
    r"""whether this template can be reverted to the corresponding system default"""
    can_delete: NotRequired[bool]
    r"""whether this template can be deleted"""
    can_disable: NotRequired[bool]
    r"""whether this template can be disabled, true only for notification SMS templates"""
    subject: NotRequired[Nullable[str]]
    r"""email subject"""
    markup: NotRequired[str]
    r"""the editor markup used to generate the body of the template"""
    body: NotRequired[str]
    r"""the template body before variable interpolation"""
    available_variables: NotRequired[List[str]]
    r"""list of variables that are available for use in the template body"""
    required_variables: NotRequired[List[str]]
    r"""list of variables that must be contained in the template body"""
    from_email_name: NotRequired[str]
    reply_to_email_name: NotRequired[str]
    delivered_by_clerk: NotRequired[bool]
    updated_at: NotRequired[int]
    r"""Unix timestamp of last update.

    """
    created_at: NotRequired[int]
    r"""Unix timestamp of creation.

    """


class Template(BaseModel):
    r"""Success"""

    id: Optional[str] = None

    object: Optional[TemplateObject] = None
    r"""String representing the object's type. Objects of the same type share the same value.

    """

    instance_id: OptionalNullable[str] = UNSET
    r"""the id of the instance the template belongs to"""

    resource_type: Optional[str] = None
    r"""whether this is a system (default) or user overridden) template"""

    template_type: Optional[str] = None
    r"""whether this is an email or SMS template"""

    name: Optional[str] = None
    r"""user-friendly name of the template"""

    slug: Optional[str] = None
    r"""machine-friendly name of the template"""

    position: Optional[int] = None
    r"""position with the listing of templates"""

    can_revert: Optional[bool] = None
    r"""whether this template can be reverted to the corresponding system default"""

    can_delete: Optional[bool] = None
    r"""whether this template can be deleted"""

    can_disable: Optional[bool] = None
    r"""whether this template can be disabled, true only for notification SMS templates"""

    subject: OptionalNullable[str] = UNSET
    r"""email subject"""

    markup: Optional[str] = None
    r"""the editor markup used to generate the body of the template"""

    body: Optional[str] = None
    r"""the template body before variable interpolation"""

    available_variables: Optional[List[str]] = None
    r"""list of variables that are available for use in the template body"""

    required_variables: Optional[List[str]] = None
    r"""list of variables that must be contained in the template body"""

    from_email_name: Optional[str] = None

    reply_to_email_name: Optional[str] = None

    delivered_by_clerk: Optional[bool] = None

    updated_at: Optional[int] = None
    r"""Unix timestamp of last update.

    """

    created_at: Optional[int] = None
    r"""Unix timestamp of creation.

    """

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "id",
            "object",
            "instance_id",
            "resource_type",
            "template_type",
            "name",
            "slug",
            "position",
            "can_revert",
            "can_delete",
            "can_disable",
            "subject",
            "markup",
            "body",
            "available_variables",
            "required_variables",
            "from_email_name",
            "reply_to_email_name",
            "delivered_by_clerk",
            "updated_at",
            "created_at",
        ]
        nullable_fields = ["instance_id", "subject"]
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
