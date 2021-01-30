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
from print_nanny_client.models.remote_control_command_alert_request import RemoteControlCommandAlertRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestRemoteControlCommandAlertRequest(unittest.TestCase):
    """RemoteControlCommandAlertRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RemoteControlCommandAlertRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.remote_control_command_alert_request.RemoteControlCommandAlertRequest()  # noqa: E501
        if include_optional :
            return RemoteControlCommandAlertRequest(
                alert_subtype = 'RECEIVED', 
                alert_method = 'UI', 
                alert_type = 'COMMAND', 
                color = '', 
                dismissed = True, 
                icon = '', 
                description = '', 
                seen = True, 
                title = ''
            )
        else :
            return RemoteControlCommandAlertRequest(
                alert_subtype = 'RECEIVED',
                alert_method = 'UI',
                alert_type = 'COMMAND',
                color = '',
                icon = '',
                description = '',
                title = '',
        )

    def testRemoteControlCommandAlertRequest(self):
        """Test RemoteControlCommandAlertRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
