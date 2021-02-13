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
from print_nanny_client.models.device_calibration import DeviceCalibration  # noqa: E501
from print_nanny_client.rest import ApiException

class TestDeviceCalibration(unittest.TestCase):
    """DeviceCalibration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceCalibration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.device_calibration.DeviceCalibration()  # noqa: E501
        if include_optional :
            return DeviceCalibration(
                id = 56, 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                device = 56, 
                fpm = -2147483648, 
                mask = {
                    'key' : null
                    }, 
                url = ''
            )
        else :
            return DeviceCalibration(
                device = 56,
        )

    def testDeviceCalibration(self):
        """Test DeviceCalibration"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
