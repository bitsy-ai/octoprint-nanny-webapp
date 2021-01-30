# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import print_nanny_client
from print_nanny_client.models.patched_remote_control_command_request import PatchedRemoteControlCommandRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPatchedRemoteControlCommandRequest(unittest.TestCase):
    """PatchedRemoteControlCommandRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedRemoteControlCommandRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.patched_remote_control_command_request.PatchedRemoteControlCommandRequest()  # noqa: E501
        if include_optional :
            return PatchedRemoteControlCommandRequest(
                command = 'MonitoringStop', 
                user = 56, 
                device = 56, 
                received = True, 
                success = True, 
                iotcore_response = {
                    'key' : null
                    }, 
                metadata = {
                    'key' : null
                    }
            )
        else :
            return PatchedRemoteControlCommandRequest(
        )

    def testPatchedRemoteControlCommandRequest(self):
        """Test PatchedRemoteControlCommandRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
