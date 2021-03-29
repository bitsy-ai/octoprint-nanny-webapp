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
from print_nanny_client.models.experiment import Experiment  # noqa: E501
from print_nanny_client.rest import ApiException

class TestExperiment(unittest.TestCase):
    """Experiment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Experiment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = print_nanny_client.models.experiment.Experiment()  # noqa: E501
        if include_optional :
            return Experiment(
                id = 56, 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                active = True, 
                name = '', 
                hypothesis = '', 
                control = None, 
                treatments = [
                    print_nanny_client.models.nested.Nested(
                        id = 56, 
                        created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        session = '', 
                        progress = {
                            'key' : null
                            }, 
                        gcode_filename = '', 
                        supress_alerts = True, 
                        octoprint_device = 56, 
                        user = 56, 
                        printer_profile = 56, 
                        gcode_file = 56, )
                    ], 
                notion_url = ''
            )
        else :
            return Experiment(
                name = '',
                hypothesis = '',
        )

    def testExperiment(self):
        """Test Experiment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
