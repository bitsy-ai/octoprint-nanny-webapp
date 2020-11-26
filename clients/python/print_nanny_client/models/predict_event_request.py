# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint  # noqa: F401
import re  # noqa: F401

import six  # noqa: F401

from print_nanny_client.exceptions import ApiValueError  # noqa: F401
from print_nanny_client.model_utils import (  # noqa: F401
    ModelNormal,
    ModelSimple,
    check_allowed_values,
    check_validations
)


class PredictEventRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      openapi_types (dict): The key is attribute name
          and the value is attribute type.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
    """

    allowed_values = {
    }

    attribute_map = {
        'dt': 'dt',  # noqa: E501
        'event_data': 'event_data',  # noqa: E501
        'predict_data': 'predict_data',  # noqa: E501
        'files': 'files',  # noqa: E501
        'print_job': 'print_job',  # noqa: E501
        'plugin_version': 'plugin_version',  # noqa: E501
        'octoprint_version': 'octoprint_version'  # noqa: E501
    }

    openapi_types = {
        'dt': 'datetime',
        'event_data': 'dict(str, object)',
        'predict_data': 'dict(str, object)',
        'files': 'int',
        'print_job': 'int',
        'plugin_version': 'str',
        'octoprint_version': 'str'
    }

    validations = {
        ('plugin_version',): {
            'max_length': 30,
        },
        ('octoprint_version',): {
            'max_length': 30,
        },
    }

    def __init__(self, dt=None, event_data=None, predict_data=None, files=None, print_job=None, plugin_version=None, octoprint_version=None):  # noqa: E501
        """PredictEventRequest - a model defined in OpenAPI"""  # noqa: E501

        self._dt = None
        self._event_data = None
        self._predict_data = None
        self._files = None
        self._print_job = None
        self._plugin_version = None
        self._octoprint_version = None
        self.discriminator = None

        if dt is not None:
            self.dt = (
                dt
            )
        self.event_data = event_data
        self.predict_data = predict_data
        self.files = files
        self.print_job = print_job
        self.plugin_version = plugin_version
        self.octoprint_version = octoprint_version

    @property
    def dt(self):
        """Gets the dt of this PredictEventRequest.  # noqa: E501


        :return: The dt of this PredictEventRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._dt

    @dt.setter
    def dt(self, dt):  # noqa: E501
        """Sets the dt of this PredictEventRequest.


        :param dt: The dt of this PredictEventRequest.  # noqa: E501
        :type: datetime
        """

        self._dt = (
            dt
        )

    @property
    def event_data(self):
        """Gets the event_data of this PredictEventRequest.  # noqa: E501


        :return: The event_data of this PredictEventRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._event_data

    @event_data.setter
    def event_data(self, event_data):  # noqa: E501
        """Sets the event_data of this PredictEventRequest.


        :param event_data: The event_data of this PredictEventRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._event_data = (
            event_data
        )

    @property
    def predict_data(self):
        """Gets the predict_data of this PredictEventRequest.  # noqa: E501


        :return: The predict_data of this PredictEventRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._predict_data

    @predict_data.setter
    def predict_data(self, predict_data):  # noqa: E501
        """Sets the predict_data of this PredictEventRequest.


        :param predict_data: The predict_data of this PredictEventRequest.  # noqa: E501
        :type: dict(str, object)
        """
        if predict_data is None:
            raise ApiValueError("Invalid value for `predict_data`, must not be `None`")  # noqa: E501

        self._predict_data = (
            predict_data
        )

    @property
    def files(self):
        """Gets the files of this PredictEventRequest.  # noqa: E501


        :return: The files of this PredictEventRequest.  # noqa: E501
        :rtype: int
        """
        return self._files

    @files.setter
    def files(self, files):  # noqa: E501
        """Sets the files of this PredictEventRequest.


        :param files: The files of this PredictEventRequest.  # noqa: E501
        :type: int
        """
        if files is None:
            raise ApiValueError("Invalid value for `files`, must not be `None`")  # noqa: E501

        self._files = (
            files
        )

    @property
    def print_job(self):
        """Gets the print_job of this PredictEventRequest.  # noqa: E501


        :return: The print_job of this PredictEventRequest.  # noqa: E501
        :rtype: int
        """
        return self._print_job

    @print_job.setter
    def print_job(self, print_job):  # noqa: E501
        """Sets the print_job of this PredictEventRequest.


        :param print_job: The print_job of this PredictEventRequest.  # noqa: E501
        :type: int
        """
        if print_job is None:
            raise ApiValueError("Invalid value for `print_job`, must not be `None`")  # noqa: E501

        self._print_job = (
            print_job
        )

    @property
    def plugin_version(self):
        """Gets the plugin_version of this PredictEventRequest.  # noqa: E501


        :return: The plugin_version of this PredictEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):  # noqa: E501
        """Sets the plugin_version of this PredictEventRequest.


        :param plugin_version: The plugin_version of this PredictEventRequest.  # noqa: E501
        :type: str
        """
        if plugin_version is None:
            raise ApiValueError("Invalid value for `plugin_version`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('plugin_version',),
            plugin_version
        )

        self._plugin_version = (
            plugin_version
        )

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this PredictEventRequest.  # noqa: E501


        :return: The octoprint_version of this PredictEventRequest.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):  # noqa: E501
        """Sets the octoprint_version of this PredictEventRequest.


        :param octoprint_version: The octoprint_version of this PredictEventRequest.  # noqa: E501
        :type: str
        """
        if octoprint_version is None:
            raise ApiValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('octoprint_version',),
            octoprint_version
        )

        self._octoprint_version = (
            octoprint_version
        )

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PredictEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
