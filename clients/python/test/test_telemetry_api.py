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
from print_nanny_client.api.telemetry_api import TelemetryApi  # noqa: E501
from print_nanny_client.rest import ApiException


class TestTelemetryApi(unittest.TestCase):
    """TelemetryApi unit test stubs"""

    def setUp(self):
        self.api = print_nanny_client.api.telemetry_api.TelemetryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_telemetry_octoprint_events_create(self):
        """Test case for telemetry_octoprint_events_create

        """
        pass

    def test_telemetry_octoprint_events_list(self):
        """Test case for telemetry_octoprint_events_list

        """
        pass

    def test_telemetry_octoprint_events_retrieve(self):
        """Test case for telemetry_octoprint_events_retrieve

        """
        pass

    def test_telemetry_octoprint_plugin_events_list(self):
        """Test case for telemetry_octoprint_plugin_events_list

        """
        pass

    def test_telemetry_octoprint_plugin_events_retrieve(self):
        """Test case for telemetry_octoprint_plugin_events_retrieve

        """
        pass

    def test_telemetry_print_status_events_list(self):
        """Test case for telemetry_print_status_events_list

        """
        pass

    def test_telemetry_print_status_events_retrieve(self):
        """Test case for telemetry_print_status_events_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()