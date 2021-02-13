# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class PatchedDeviceCalibrationRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'device': 'int',
        'fpm': 'int',
        'coordinates': 'dict(str, object)',
        'mask': 'dict(str, object)'
    }

    attribute_map = {
        'device': 'device',
        'fpm': 'fpm',
        'coordinates': 'coordinates',
        'mask': 'mask'
    }

    def __init__(self, device=None, fpm=None, coordinates=None, mask=None, local_vars_configuration=None):  # noqa: E501
        """PatchedDeviceCalibrationRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._device = None
        self._fpm = None
        self._coordinates = None
        self._mask = None
        self.discriminator = None

        if device is not None:
            self.device = device
        self.fpm = fpm
        self.coordinates = coordinates
        self.mask = mask

    @property
    def device(self):
        """Gets the device of this PatchedDeviceCalibrationRequest.  # noqa: E501


        :return: The device of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PatchedDeviceCalibrationRequest.


        :param device: The device of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :type device: int
        """

        self._device = device

    @property
    def fpm(self):
        """Gets the fpm of this PatchedDeviceCalibrationRequest.  # noqa: E501


        :return: The fpm of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :rtype: int
        """
        return self._fpm

    @fpm.setter
    def fpm(self, fpm):
        """Sets the fpm of this PatchedDeviceCalibrationRequest.


        :param fpm: The fpm of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :type fpm: int
        """
        if (self.local_vars_configuration.client_side_validation and
                fpm is not None and fpm > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `fpm`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                fpm is not None and fpm < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `fpm`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._fpm = fpm

    @property
    def coordinates(self):
        """Gets the coordinates of this PatchedDeviceCalibrationRequest.  # noqa: E501


        :return: The coordinates of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this PatchedDeviceCalibrationRequest.


        :param coordinates: The coordinates of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :type coordinates: dict(str, object)
        """

        self._coordinates = coordinates

    @property
    def mask(self):
        """Gets the mask of this PatchedDeviceCalibrationRequest.  # noqa: E501


        :return: The mask of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this PatchedDeviceCalibrationRequest.


        :param mask: The mask of this PatchedDeviceCalibrationRequest.  # noqa: E501
        :type mask: dict(str, object)
        """

        self._mask = mask

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PatchedDeviceCalibrationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedDeviceCalibrationRequest):
            return True

        return self.to_dict() != other.to_dict()
