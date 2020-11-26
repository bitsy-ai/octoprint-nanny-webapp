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


class PatchedGcodeFileRequest(ModelNormal):
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
        'name': 'name',  # noqa: E501
        'file': 'file',  # noqa: E501
        'file_hash': 'file_hash'  # noqa: E501
    }

    openapi_types = {
        'name': 'str',
        'file': 'file',
        'file_hash': 'str'
    }

    validations = {
        ('name',): {
            'max_length': 255,
        },
        ('file_hash',): {
            'max_length': 255,
        },
    }

    def __init__(self, name=None, file=None, file_hash=None):  # noqa: E501
        """PatchedGcodeFileRequest - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._file = None
        self._file_hash = None
        self.discriminator = None

        if name is not None:
            self.name = (
                name
            )
        if file is not None:
            self.file = (
                file
            )
        if file_hash is not None:
            self.file_hash = (
                file_hash
            )

    @property
    def name(self):
        """Gets the name of this PatchedGcodeFileRequest.  # noqa: E501


        :return: The name of this PatchedGcodeFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):  # noqa: E501
        """Sets the name of this PatchedGcodeFileRequest.


        :param name: The name of this PatchedGcodeFileRequest.  # noqa: E501
        :type: str
        """
        check_validations(
            self.validations,
            ('name',),
            name
        )

        self._name = (
            name
        )

    @property
    def file(self):
        """Gets the file of this PatchedGcodeFileRequest.  # noqa: E501


        :return: The file of this PatchedGcodeFileRequest.  # noqa: E501
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):  # noqa: E501
        """Sets the file of this PatchedGcodeFileRequest.


        :param file: The file of this PatchedGcodeFileRequest.  # noqa: E501
        :type: file
        """

        self._file = (
            file
        )

    @property
    def file_hash(self):
        """Gets the file_hash of this PatchedGcodeFileRequest.  # noqa: E501


        :return: The file_hash of this PatchedGcodeFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._file_hash

    @file_hash.setter
    def file_hash(self, file_hash):  # noqa: E501
        """Sets the file_hash of this PatchedGcodeFileRequest.


        :param file_hash: The file_hash of this PatchedGcodeFileRequest.  # noqa: E501
        :type: str
        """
        check_validations(
            self.validations,
            ('file_hash',),
            file_hash
        )

        self._file_hash = (
            file_hash
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
        if not isinstance(other, PatchedGcodeFileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
