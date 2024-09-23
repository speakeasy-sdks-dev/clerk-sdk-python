"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from clerk_backend_api import models, utils
from clerk_backend_api._hooks import HookContext
from clerk_backend_api.types import BaseModel, OptionalNullable, UNSET
from jsonpath import JSONPath
from typing import Any, Dict, List, Optional, Union, cast


class Invitations(BaseSDK):
    def create(
        self,
        *,
        request: Optional[
            Union[
                models.CreateInvitationRequestBody,
                models.CreateInvitationRequestBodyTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.Invitation]:
        r"""Create an invitation

        Creates a new invitation for the given email address and sends the invitation email.
        Keep in mind that you cannot create an invitation if there is already one for the given email address.
        Also, trying to create an invitation for an email address that already exists in your application will result to an error.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, Optional[models.CreateInvitationRequestBody]
            )
        request = cast(Optional[models.CreateInvitationRequestBody], request)

        req = self.build_request(
            method="POST",
            path="/invitations",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request,
                False,
                True,
                "json",
                Optional[models.CreateInvitationRequestBody],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="CreateInvitation",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Invitation])
        if utils.match_response(http_res, ["400", "422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def create_async(
        self,
        *,
        request: Optional[
            Union[
                models.CreateInvitationRequestBody,
                models.CreateInvitationRequestBodyTypedDict,
            ]
        ] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.Invitation]:
        r"""Create an invitation

        Creates a new invitation for the given email address and sends the invitation email.
        Keep in mind that you cannot create an invitation if there is already one for the given email address.
        Also, trying to create an invitation for an email address that already exists in your application will result to an error.

        :param request: The request object to send.
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        if not isinstance(request, BaseModel):
            request = utils.unmarshal(
                request, Optional[models.CreateInvitationRequestBody]
            )
        request = cast(Optional[models.CreateInvitationRequestBody], request)

        req = self.build_request_async(
            method="POST",
            path="/invitations",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            get_serialized_body=lambda: utils.serialize_request_body(
                request,
                False,
                True,
                "json",
                Optional[models.CreateInvitationRequestBody],
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="CreateInvitation",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "422", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(http_res.text, Optional[models.Invitation])
        if utils.match_response(http_res, ["400", "422"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def list(
        self,
        *,
        limit: Optional[int] = 10,
        offset: Optional[int] = 0,
        status: Optional[models.ListInvitationsQueryParamStatus] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ListInvitationsResponse]:
        r"""List all invitations

        Returns all non-revoked invitations for your application, sorted by creation date

        :param limit: Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`.
        :param offset: Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`.
        :param status: Filter invitations based on their status
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListInvitationsRequest(
            limit=limit,
            offset=offset,
            status=status,
        )

        req = self.build_request(
            method="GET",
            path="/invitations",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="ListInvitations",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.ListInvitationsResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            offset = request.offset if not request.offset is None else 0

            if not http_res.text:
                return None
            results = JSONPath("$").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 0
            if len(results[0]) < limit:
                return None
            next_offset = offset + len(results[0])

            return self.list(
                limit=limit,
                offset=next_offset,
                status=status,
                retries=retries,
            )

        if utils.match_response(http_res, "200", "application/json"):
            return models.ListInvitationsResponse(
                result=utils.unmarshal_json(
                    http_res.text, Optional[List[models.Invitation]]
                ),
                next=next_func,
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def list_async(
        self,
        *,
        limit: Optional[int] = 10,
        offset: Optional[int] = 0,
        status: Optional[models.ListInvitationsQueryParamStatus] = None,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.ListInvitationsResponse]:
        r"""List all invitations

        Returns all non-revoked invitations for your application, sorted by creation date

        :param limit: Applies a limit to the number of results returned. Can be used for paginating the results together with `offset`.
        :param offset: Skip the first `offset` results when paginating. Needs to be an integer greater or equal to zero. To be used in conjunction with `limit`.
        :param status: Filter invitations based on their status
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.ListInvitationsRequest(
            limit=limit,
            offset=offset,
            status=status,
        )

        req = self.build_request_async(
            method="GET",
            path="/invitations",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=False,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="ListInvitations",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["4XX", "5XX"],
            retry_config=retry_config,
        )

        def next_func() -> Optional[models.ListInvitationsResponse]:
            body = utils.unmarshal_json(http_res.text, Dict[Any, Any])
            offset = request.offset if not request.offset is None else 0

            if not http_res.text:
                return None
            results = JSONPath("$").parse(body)
            if len(results) == 0 or len(results[0]) == 0:
                return None
            limit = request.limit if not request.limit is None else 0
            if len(results[0]) < limit:
                return None
            next_offset = offset + len(results[0])

            return self.list(
                limit=limit,
                offset=next_offset,
                status=status,
                retries=retries,
            )

        if utils.match_response(http_res, "200", "application/json"):
            return models.ListInvitationsResponse(
                result=utils.unmarshal_json(
                    http_res.text, Optional[List[models.Invitation]]
                ),
                next=next_func,
            )
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    def revoke(
        self,
        *,
        invitation_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.InvitationRevoked]:
        r"""Revokes an invitation

        Revokes the given invitation.
        Revoking an invitation will prevent the user from using the invitation link that was sent to them.
        However, it doesn't prevent the user from signing up if they follow the sign up flow.
        Only active (i.e. non-revoked) invitations can be revoked.

        :param invitation_id: The ID of the invitation to be revoked
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.RevokeInvitationRequest(
            invitation_id=invitation_id,
        )

        req = self.build_request(
            method="POST",
            path="/invitations/{invitation_id}/revoke",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                operation_id="RevokeInvitation",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[models.InvitationRevoked]
            )
        if utils.match_response(http_res, ["400", "404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )

    async def revoke_async(
        self,
        *,
        invitation_id: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
    ) -> Optional[models.InvitationRevoked]:
        r"""Revokes an invitation

        Revokes the given invitation.
        Revoking an invitation will prevent the user from using the invitation link that was sent to them.
        However, it doesn't prevent the user from signing up if they follow the sign up flow.
        Only active (i.e. non-revoked) invitations can be revoked.

        :param invitation_id: The ID of the invitation to be revoked
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url

        request = models.RevokeInvitationRequest(
            invitation_id=invitation_id,
        )

        req = self.build_request_async(
            method="POST",
            path="/invitations/{invitation_id}/revoke",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=False,
            request_has_path_params=True,
            request_has_query_params=True,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            security=self.sdk_configuration.security,
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                operation_id="RevokeInvitation",
                oauth2_scopes=[],
                security_source=self.sdk_configuration.security,
            ),
            request=req,
            error_status_codes=["400", "404", "4XX", "5XX"],
            retry_config=retry_config,
        )

        data: Any = None
        if utils.match_response(http_res, "200", "application/json"):
            return utils.unmarshal_json(
                http_res.text, Optional[models.InvitationRevoked]
            )
        if utils.match_response(http_res, ["400", "404"], "application/json"):
            data = utils.unmarshal_json(http_res.text, models.ClerkErrorsData)
            raise models.ClerkErrors(data=data)
        if utils.match_response(http_res, ["4XX", "5XX"], "*"):
            raise models.SDKError(
                "API error occurred", http_res.status_code, http_res.text, http_res
            )

        content_type = http_res.headers.get("Content-Type")
        raise models.SDKError(
            f"Unexpected response received (code: {http_res.status_code}, type: {content_type})",
            http_res.status_code,
            http_res.text,
            http_res,
        )
