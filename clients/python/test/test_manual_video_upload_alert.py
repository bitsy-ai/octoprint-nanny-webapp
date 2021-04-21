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
from print_nanny_client.models.manual_video_upload_alert import ManualVideoUploadAlert  # noqa: E501
from print_nanny_client.rest import ApiException

class TestManualVideoUploadAlert(unittest.TestCase):
    """ManualVideoUploadAlert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ManualVideoUploadAlert
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.manual_video_upload_alert.ManualVideoUploadAlert()  # noqa: E501
        if include_optional :
            return ManualVideoUploadAlert(
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user = 56, 
                alert_type = 'COMMAND'
            )
        else :
            return ManualVideoUploadAlert(
                alert_type = 'COMMAND',
        )

    def testManualVideoUploadAlert(self):
        """Test ManualVideoUploadAlert"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
