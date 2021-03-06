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
from print_nanny_client.api.remote_control_api import RemoteControlApi  # noqa: E501
from print_nanny_client.rest import ApiException


class TestRemoteControlApi(unittest.TestCase):
    """RemoteControlApi unit test stubs"""

    def setUp(self):
        self.api = print_nanny_client.api.remote_control_api.RemoteControlApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_commands_list(self):
        """Test case for api_commands_list

        """
        pass

    def test_api_commands_partial_update(self):
        """Test case for api_commands_partial_update

        """
        pass

    def test_api_commands_retrieve(self):
        """Test case for api_commands_retrieve

        """
        pass

    def test_api_commands_update(self):
        """Test case for api_commands_update

        """
        pass

    def test_api_gcode_files_list(self):
        """Test case for api_gcode_files_list

        """
        pass

    def test_api_gcode_files_partial_update(self):
        """Test case for api_gcode_files_partial_update

        """
        pass

    def test_api_gcode_files_retrieve(self):
        """Test case for api_gcode_files_retrieve

        """
        pass

    def test_api_gcode_files_update(self):
        """Test case for api_gcode_files_update

        """
        pass

    def test_api_octoprint_devices_create(self):
        """Test case for api_octoprint_devices_create

        """
        pass

    def test_api_octoprint_devices_list(self):
        """Test case for api_octoprint_devices_list

        """
        pass

    def test_api_octoprint_devices_retrieve(self):
        """Test case for api_octoprint_devices_retrieve

        """
        pass

    def test_api_print_sessions_create(self):
        """Test case for api_print_sessions_create

        """
        pass

    def test_api_print_sessions_list(self):
        """Test case for api_print_sessions_list

        """
        pass

    def test_api_print_sessions_retrieve(self):
        """Test case for api_print_sessions_retrieve

        """
        pass

    def test_api_printer_profiles_list(self):
        """Test case for api_printer_profiles_list

        """
        pass

    def test_api_printer_profiles_partial_update(self):
        """Test case for api_printer_profiles_partial_update

        """
        pass

    def test_api_printer_profiles_retrieve(self):
        """Test case for api_printer_profiles_retrieve

        """
        pass

    def test_api_printer_profiles_update(self):
        """Test case for api_printer_profiles_update

        """
        pass

    def test_gcode_files_create(self):
        """Test case for gcode_files_create

        """
        pass

    def test_gcode_files_update_or_create(self):
        """Test case for gcode_files_update_or_create

        """
        pass

    def test_octoprint_devices_partial_update(self):
        """Test case for octoprint_devices_partial_update

        """
        pass

    def test_octoprint_devices_update(self):
        """Test case for octoprint_devices_update

        """
        pass

    def test_octoprint_devices_update_or_create(self):
        """Test case for octoprint_devices_update_or_create

        """
        pass

    def test_print_session_partial_update(self):
        """Test case for print_session_partial_update

        """
        pass

    def test_print_session_update(self):
        """Test case for print_session_update

        """
        pass

    def test_printer_profiles_create(self):
        """Test case for printer_profiles_create

        """
        pass

    def test_printer_profiles_update_or_create(self):
        """Test case for printer_profiles_update_or_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
