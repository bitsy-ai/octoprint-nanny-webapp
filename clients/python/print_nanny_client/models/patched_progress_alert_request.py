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


class PatchedProgressAlertRequest(object):
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
        'seen': 'bool',
        'sent': 'bool',
        'progress_percent': 'int',
        'octoprint_device': 'int',
        'device': 'int'
    }

    attribute_map = {
        'seen': 'seen',
        'sent': 'sent',
        'progress_percent': 'progress_percent',
        'octoprint_device': 'octoprint_device',
        'device': 'device'
    }

    def __init__(self, seen=None, sent=None, progress_percent=None, octoprint_device=None, device=None, local_vars_configuration=None):  # noqa: E501
        """PatchedProgressAlertRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._seen = None
        self._sent = None
        self._progress_percent = None
        self._octoprint_device = None
        self._device = None
        self.discriminator = None

        if seen is not None:
            self.seen = seen
        if sent is not None:
            self.sent = sent
        if progress_percent is not None:
            self.progress_percent = progress_percent
        self.octoprint_device = octoprint_device
        if device is not None:
            self.device = device

    @property
    def seen(self):
        """Gets the seen of this PatchedProgressAlertRequest.  # noqa: E501


        :return: The seen of this PatchedProgressAlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this PatchedProgressAlertRequest.


        :param seen: The seen of this PatchedProgressAlertRequest.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def sent(self):
        """Gets the sent of this PatchedProgressAlertRequest.  # noqa: E501


        :return: The sent of this PatchedProgressAlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this PatchedProgressAlertRequest.


        :param sent: The sent of this PatchedProgressAlertRequest.  # noqa: E501
        :type sent: bool
        """

        self._sent = sent

    @property
    def progress_percent(self):
        """Gets the progress_percent of this PatchedProgressAlertRequest.  # noqa: E501

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :return: The progress_percent of this PatchedProgressAlertRequest.  # noqa: E501
        :rtype: int
        """
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, progress_percent):
        """Sets the progress_percent of this PatchedProgressAlertRequest.

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :param progress_percent: The progress_percent of this PatchedProgressAlertRequest.  # noqa: E501
        :type progress_percent: int
        """
        if (self.local_vars_configuration.client_side_validation and
                progress_percent is not None and progress_percent > 100):  # noqa: E501
            raise ValueError("Invalid value for `progress_percent`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                progress_percent is not None and progress_percent < 1):  # noqa: E501
            raise ValueError("Invalid value for `progress_percent`, must be a value greater than or equal to `1`")  # noqa: E501

        self._progress_percent = progress_percent

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this PatchedProgressAlertRequest.  # noqa: E501


        :return: The octoprint_device of this PatchedProgressAlertRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this PatchedProgressAlertRequest.


        :param octoprint_device: The octoprint_device of this PatchedProgressAlertRequest.  # noqa: E501
        :type octoprint_device: int
        """

        self._octoprint_device = octoprint_device

    @property
    def device(self):
        """Gets the device of this PatchedProgressAlertRequest.  # noqa: E501


        :return: The device of this PatchedProgressAlertRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PatchedProgressAlertRequest.


        :param device: The device of this PatchedProgressAlertRequest.  # noqa: E501
        :type device: int
        """

        self._device = device

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
        if not isinstance(other, PatchedProgressAlertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedProgressAlertRequest):
            return True

        return self.to_dict() != other.to_dict()
