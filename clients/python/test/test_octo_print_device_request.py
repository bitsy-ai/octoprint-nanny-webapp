# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import print_nanny_client
from print_nanny_client.models.octo_print_device_request import OctoPrintDeviceRequest  # noqa: E501
from print_nanny_client.rest import ApiException

class TestOctoPrintDeviceRequest(unittest.TestCase):
    """OctoPrintDeviceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OctoPrintDeviceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.octo_print_device_request.OctoPrintDeviceRequest()  # noqa: E501
        if include_optional :
            return OctoPrintDeviceRequest(
                model = '', 
                platform = '', 
                mac_address = '', 
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
                octoprint_version = '', 
                plugin_version = ''
            )
        else :
            return OctoPrintDeviceRequest(
                model = '',
                platform = '',
                mac_address = '',
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
                octoprint_version = '',
                plugin_version = '',
        )

    def testOctoPrintDeviceRequest(self):
        """Test OctoPrintDeviceRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
