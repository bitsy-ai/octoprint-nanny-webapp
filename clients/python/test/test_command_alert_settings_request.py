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
from print_nanny_client.models.command_alert_settings_request import CommandAlertSettingsRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestCommandAlertSettingsRequest(unittest.TestCase):
    """CommandAlertSettingsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CommandAlertSettingsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.command_alert_settings_request.CommandAlertSettingsRequest()  # noqa: E501
        if include_optional :
            return CommandAlertSettingsRequest(
                alert_type = 'COMMAND', 
                alert_methods = [
                    'UI'
                    ], 
                enabled = True, 
                snapshot = [
                    'RECEIVED'
                    ], 
                stop_monitoring = [
                    'RECEIVED'
                    ], 
                start_monitoring = [
                    'RECEIVED'
                    ], 
                stop_print = [
                    'RECEIVED'
                    ], 
                start_print = [
                    'RECEIVED'
                    ], 
                move_nozzle = [
                    'RECEIVED'
                    ], 
                pause_print = [
                    'RECEIVED'
                    ], 
                resume_print = [
                    'RECEIVED'
                    ]
            )
        else :
            return CommandAlertSettingsRequest(
                alert_type = 'COMMAND',
        )

    def testCommandAlertSettingsRequest(self):
        """Test CommandAlertSettingsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
