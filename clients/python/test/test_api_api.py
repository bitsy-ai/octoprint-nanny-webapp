# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import print_nanny_client
from print_nanny_client.api.api_api import ApiApi  # noqa: E501
from print_nanny_client.rest import ApiException


class TestApiApi(unittest.TestCase):
    """ApiApi unit test stubs"""

    def setUp(self):
        self.api = print_nanny_client.api.api_api.ApiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_auth_token_create(self):
        """Test case for api_auth_token_create

        """
        pass

    def test_api_schema_retrieve(self):
        """Test case for api_schema_retrieve

        """
        pass

    def test_api_users_list(self):
        """Test case for api_users_list

        """
        pass

    def test_api_users_me_retrieve(self):
        """Test case for api_users_me_retrieve

        """
        pass

    def test_api_users_partial_update(self):
        """Test case for api_users_partial_update

        """
        pass

    def test_api_users_retrieve(self):
        """Test case for api_users_retrieve

        """
        pass

    def test_api_users_update(self):
        """Test case for api_users_update

        """
        pass


if __name__ == '__main__':
    unittest.main()
