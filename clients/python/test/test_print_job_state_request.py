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
from print_nanny_client.models.print_job_state_request import PrintJobStateRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPrintJobStateRequest(unittest.TestCase):
    """PrintJobStateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PrintJobStateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.print_job_state_request.PrintJobStateRequest()  # noqa: E501
        if include_optional :
            return PrintJobStateRequest(
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                client_event_type = 'plugin', 
                event_data = {
                    'key' : null
                    }, 
                device = 56, 
                plugin_version = '', 
                octoprint_version = '', 
                event_type = 'Error', 
                state = {
                    'key' : null
                    }, 
                current_z = 1.337, 
                progress = {
                    'key' : null
                    }, 
                job_data_file = '', 
                print_job = 56
            )
        else :
            return PrintJobStateRequest(
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                client_event_type = 'plugin',
                event_data = {
                    'key' : null
                    },
                device = 56,
                plugin_version = '',
                octoprint_version = '',
                event_type = 'Error',
                job_data_file = '',
        )

    def testPrintJobStateRequest(self):
        """Test PrintJobStateRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
