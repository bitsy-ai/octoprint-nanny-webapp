# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import print_nanny_client
from print_nanny_client.api.events_api import EventsApi  # noqa: E501
from print_nanny_client.rest import ApiException


class TestEventsApi(unittest.TestCase):
    """EventsApi unit test stubs"""

    def setUp(self):
        self.api = print_nanny_client.api.events_api.EventsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_octoprint_events_create(self):
        """Test case for octoprint_events_create

        """
        pass

    def test_octoprint_events_list(self):
        """Test case for octoprint_events_list

        """
        pass

    def test_octoprint_events_retrieve(self):
        """Test case for octoprint_events_retrieve

        """
        pass

    def test_octoprint_events_tracking_retrieve(self):
        """Test case for octoprint_events_tracking_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
