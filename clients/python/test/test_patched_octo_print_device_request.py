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
from print_nanny_client.models.patched_octo_print_device_request import PatchedOctoPrintDeviceRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPatchedOctoPrintDeviceRequest(unittest.TestCase):
    """PatchedOctoPrintDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchedOctoPrintDeviceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.patched_octo_print_device_request.PatchedOctoPrintDeviceRequest()  # noqa: E501
        if include_optional :
            return PatchedOctoPrintDeviceRequest(
                name = '', 
                configs = {
                    'key' : null
                    }, 
                model = '', 
                platform = '', 
                cpu_flags = [
                    ''
                    ], 
                hardware = '', 
                revision = '', 
                serial = '', 
                cores = -2147483648, 
                ram = -2147483648, 
                python_version = '', 
                pip_version = '', 
                virtualenv = '', 
                monitoring_active = True, 
                octoprint_version = '', 
                plugin_version = '', 
                print_nanny_client_version = ''
            )
        else :
            return PatchedOctoPrintDeviceRequest(
        )

    def testPatchedOctoPrintDeviceRequest(self):
        """Test PatchedOctoPrintDeviceRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
