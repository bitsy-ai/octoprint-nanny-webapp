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
from print_nanny_client.models.partner3_d_geeks_alert import Partner3DGeeksAlert  # noqa: E501
from print_nanny_client.rest import ApiException

class TestPartner3DGeeksAlert(unittest.TestCase):
    """Partner3DGeeksAlert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Partner3DGeeksAlert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.partner3_d_geeks_alert.Partner3DGeeksAlert()  # noqa: E501
        if include_optional :
            return Partner3DGeeksAlert(
                event = '', 
                token = '', 
                printer = '', 
                _print = '', 
                current_time = '', 
                time_left = '', 
                percent = '', 
                image = '', 
                action = ''
            )
        else :
            return Partner3DGeeksAlert(
        )

    def testPartner3DGeeksAlert(self):
        """Test Partner3DGeeksAlert"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
