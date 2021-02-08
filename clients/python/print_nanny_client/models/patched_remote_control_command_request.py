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


class PatchedRemoteControlCommandRequest(object):
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
        'command': 'CommandEnum',
        'user': 'int',
        'device': 'int',
        'received': 'bool',
        'success': 'bool',
        'iotcore_response': 'dict(str, object)',
        'metadata': 'dict(str, object)'
    }

    attribute_map = {
        'command': 'command',
        'user': 'user',
        'device': 'device',
        'received': 'received',
        'success': 'success',
        'iotcore_response': 'iotcore_response',
        'metadata': 'metadata'
    }

    def __init__(self, command=None, user=None, device=None, received=None, success=None, iotcore_response=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """PatchedRemoteControlCommandRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._command = None
        self._user = None
        self._device = None
        self._received = None
        self._success = None
        self._iotcore_response = None
        self._metadata = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if user is not None:
            self.user = user
        if device is not None:
            self.device = device
        if received is not None:
            self.received = received
        self.success = success
        if iotcore_response is not None:
            self.iotcore_response = iotcore_response
        if metadata is not None:
            self.metadata = metadata

    @property
    def command(self):
        """Gets the command of this PatchedRemoteControlCommandRequest.  # noqa: E501


        :return: The command of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :rtype: CommandEnum
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this PatchedRemoteControlCommandRequest.


        :param command: The command of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :type command: CommandEnum
        """

        self._command = command

    @property
    def user(self):
        """Gets the user of this PatchedRemoteControlCommandRequest.  # noqa: E501


        :return: The user of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PatchedRemoteControlCommandRequest.


        :param user: The user of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def device(self):
        """Gets the device of this PatchedRemoteControlCommandRequest.  # noqa: E501


        :return: The device of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this PatchedRemoteControlCommandRequest.


        :param device: The device of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :type device: int
        """

        self._device = device

    @property
    def received(self):
        """Gets the received of this PatchedRemoteControlCommandRequest.  # noqa: E501


        :return: The received of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :rtype: bool
        """
        return self._received

    @received.setter
    def received(self, received):
        """Sets the received of this PatchedRemoteControlCommandRequest.


        :param received: The received of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :type received: bool
        """

        self._received = received

    @property
    def success(self):
        """Gets the success of this PatchedRemoteControlCommandRequest.  # noqa: E501


        :return: The success of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PatchedRemoteControlCommandRequest.


        :param success: The success of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :type success: bool
        """

        self._success = success

    @property
    def iotcore_response(self):
        """Gets the iotcore_response of this PatchedRemoteControlCommandRequest.  # noqa: E501


        :return: The iotcore_response of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._iotcore_response

    @iotcore_response.setter
    def iotcore_response(self, iotcore_response):
        """Sets the iotcore_response of this PatchedRemoteControlCommandRequest.


        :param iotcore_response: The iotcore_response of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :type iotcore_response: dict(str, object)
        """

        self._iotcore_response = iotcore_response

    @property
    def metadata(self):
        """Gets the metadata of this PatchedRemoteControlCommandRequest.  # noqa: E501


        :return: The metadata of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PatchedRemoteControlCommandRequest.


        :param metadata: The metadata of this PatchedRemoteControlCommandRequest.  # noqa: E501
        :type metadata: dict(str, object)
        """

        self._metadata = metadata

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
        if not isinstance(other, PatchedRemoteControlCommandRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedRemoteControlCommandRequest):
            return True

        return self.to_dict() != other.to_dict()