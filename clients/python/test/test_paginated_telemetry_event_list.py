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
from print_nanny_client.models.paginated_telemetry_event_list import PaginatedTelemetryEventList  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPaginatedTelemetryEventList(unittest.TestCase):
    """PaginatedTelemetryEventList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedTelemetryEventList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.paginated_telemetry_event_list.PaginatedTelemetryEventList()  # noqa: E501
        if include_optional :
            return PaginatedTelemetryEventList(
                count = 123, 
                next = 'http://api.example.org/accounts/?page=4', 
                previous = 'http://api.example.org/accounts/?page=2', 
                results = [
                    print_nanny_client.models.telemetry_event.TelemetryEvent(
                        id = 56, 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        event_source = 'octoprint', 
                        event_data = {
                            'key' : null
                            }, 
                        plugin_version = '', 
                        client_version = '', 
                        octoprint_version = '', 
                        metadata = {
                            'key' : null
                            }, 
                        octoprint_job = {
                            'key' : null
                            }, 
                        polymorphic_ctype = 56, 
                        octoprint_device = 56, 
                        user = 56, 
                        print_session = 56, )
                    ]
            )
        else :
            return PaginatedTelemetryEventList(
        )

    def testPaginatedTelemetryEventList(self):
        """Test PaginatedTelemetryEventList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
