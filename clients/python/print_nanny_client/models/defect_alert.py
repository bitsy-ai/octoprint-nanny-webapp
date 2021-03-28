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


class DefectAlert(object):
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
        'print_session': 'str',
        'octoprint_device': 'int',
        'seen': 'bool',
        'dismissed': 'bool',
        'user': 'int'
    }

    attribute_map = {
        'print_session': 'print_session',
        'octoprint_device': 'octoprint_device',
        'seen': 'seen',
        'dismissed': 'dismissed',
        'user': 'user'
    }

    def __init__(self, print_session=None, octoprint_device=None, seen=None, dismissed=None, user=None, local_vars_configuration=None):  # noqa: E501
        """DefectAlert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._print_session = None
        self._octoprint_device = None
        self._seen = None
        self._dismissed = None
        self._user = None
        self.discriminator = None

        self.print_session = print_session
        self.octoprint_device = octoprint_device
        if seen is not None:
            self.seen = seen
        if dismissed is not None:
            self.dismissed = dismissed
        self.user = user

    @property
    def print_session(self):
        """Gets the print_session of this DefectAlert.  # noqa: E501


        :return: The print_session of this DefectAlert.  # noqa: E501
        :rtype: str
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this DefectAlert.


        :param print_session: The print_session of this DefectAlert.  # noqa: E501
        :type print_session: str
        """
        if self.local_vars_configuration.client_side_validation and print_session is None:  # noqa: E501
            raise ValueError("Invalid value for `print_session`, must not be `None`")  # noqa: E501

        self._print_session = print_session

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this DefectAlert.  # noqa: E501


        :return: The octoprint_device of this DefectAlert.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this DefectAlert.


        :param octoprint_device: The octoprint_device of this DefectAlert.  # noqa: E501
        :type octoprint_device: int
        """

        self._octoprint_device = octoprint_device

    @property
    def seen(self):
        """Gets the seen of this DefectAlert.  # noqa: E501


        :return: The seen of this DefectAlert.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this DefectAlert.


        :param seen: The seen of this DefectAlert.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def dismissed(self):
        """Gets the dismissed of this DefectAlert.  # noqa: E501


        :return: The dismissed of this DefectAlert.  # noqa: E501
        :rtype: bool
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        """Sets the dismissed of this DefectAlert.


        :param dismissed: The dismissed of this DefectAlert.  # noqa: E501
        :type dismissed: bool
        """

        self._dismissed = dismissed

    @property
    def user(self):
        """Gets the user of this DefectAlert.  # noqa: E501


        :return: The user of this DefectAlert.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DefectAlert.


        :param user: The user of this DefectAlert.  # noqa: E501
        :type user: int
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, DefectAlert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DefectAlert):
            return True

        return self.to_dict() != other.to_dict()
