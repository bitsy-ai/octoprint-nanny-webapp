# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from print_nanny_client.api_client import ApiClient
from print_nanny_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AuthApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def auth_verify_create(self, callback_token_verification_request, **kwargs):  # noqa: E501
        """auth_verify_create  # noqa: E501

        This verifies an alias on correct callback token entry using the same logic as auth. Should be refactored at some point.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_verify_create(callback_token_verification_request, async_req=True)
        >>> result = thread.get()

        :param callback_token_verification_request: (required)
        :type callback_token_verification_request: CallbackTokenVerificationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CallbackTokenVerification
        """
        kwargs['_return_http_data_only'] = True
        return self.auth_verify_create_with_http_info(callback_token_verification_request, **kwargs)  # noqa: E501

    def auth_verify_create_with_http_info(self, callback_token_verification_request, **kwargs):  # noqa: E501
        """auth_verify_create  # noqa: E501

        This verifies an alias on correct callback token entry using the same logic as auth. Should be refactored at some point.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.auth_verify_create_with_http_info(callback_token_verification_request, async_req=True)
        >>> result = thread.get()

        :param callback_token_verification_request: (required)
        :type callback_token_verification_request: CallbackTokenVerificationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(CallbackTokenVerification, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = [
            'callback_token_verification_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_verify_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'callback_token_verification_request' is set
        if self.api_client.client_side_validation and ('callback_token_verification_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['callback_token_verification_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `callback_token_verification_request` when calling `auth_verify_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'callback_token_verification_request' in local_var_params:
            body_params = local_var_params['callback_token_verification_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['cookieAuth', 'tokenAuth']  # noqa: E501
        
        response_types_map = {
            200: "CallbackTokenVerification",
        }

        return self.api_client.call_api(
            '/auth/verify/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
