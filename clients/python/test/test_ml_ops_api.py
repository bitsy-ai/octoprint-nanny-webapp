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
from print_nanny_client.api.ml_ops_api import MlOpsApi  # noqa: E501
from print_nanny_client.rest import ApiException


class TestMlOpsApi(unittest.TestCase):
    """MlOpsApi unit test stubs"""

    def setUp(self):
        self.api = print_nanny_client.api.ml_ops_api.MlOpsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_device_calibrations_list(self):
        """Test case for api_device_calibrations_list

        """
        pass

    def test_api_device_calibrations_partial_update(self):
        """Test case for api_device_calibrations_partial_update

        """
        pass

    def test_api_device_calibrations_retrieve(self):
        """Test case for api_device_calibrations_retrieve

        """
        pass

    def test_api_device_calibrations_update(self):
        """Test case for api_device_calibrations_update

        """
        pass

    def test_api_experiment_device_configs_list(self):
        """Test case for api_experiment_device_configs_list

        """
        pass

    def test_api_experiment_device_configs_retrieve(self):
        """Test case for api_experiment_device_configs_retrieve

        """
        pass

    def test_api_experiments_list(self):
        """Test case for api_experiments_list

        """
        pass

    def test_api_experiments_retrieve(self):
        """Test case for api_experiments_retrieve

        """
        pass

    def test_api_model_artifacts_list(self):
        """Test case for api_model_artifacts_list

        """
        pass

    def test_api_model_artifacts_retrieve(self):
        """Test case for api_model_artifacts_retrieve

        """
        pass

    def test_device_calibration_update_or_create(self):
        """Test case for device_calibration_update_or_create

        """
        pass


if __name__ == '__main__':
    unittest.main()
