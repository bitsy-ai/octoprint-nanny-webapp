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


class ManualVideoUploadAlert(object):
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
        'created_dt': 'datetime',
        'updated_dt': 'datetime',
        'user': 'int',
        'alert_type': 'AlertTypeEnum'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'user': 'user',
        'alert_type': 'alert_type'
    }

    def __init__(self, created_dt=None, updated_dt=None, user=None, alert_type=None, local_vars_configuration=None):  # noqa: E501
        """ManualVideoUploadAlert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._updated_dt = None
        self._user = None
        self._alert_type = None
        self.discriminator = None

        if created_dt is not None:
            self.created_dt = created_dt
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if user is not None:
            self.user = user
        self.alert_type = alert_type

    @property
    def created_dt(self):
        """Gets the created_dt of this ManualVideoUploadAlert.  # noqa: E501


        :return: The created_dt of this ManualVideoUploadAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ManualVideoUploadAlert.


        :param created_dt: The created_dt of this ManualVideoUploadAlert.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ManualVideoUploadAlert.  # noqa: E501


        :return: The updated_dt of this ManualVideoUploadAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ManualVideoUploadAlert.


        :param updated_dt: The updated_dt of this ManualVideoUploadAlert.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def user(self):
        """Gets the user of this ManualVideoUploadAlert.  # noqa: E501


        :return: The user of this ManualVideoUploadAlert.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ManualVideoUploadAlert.


        :param user: The user of this ManualVideoUploadAlert.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def alert_type(self):
        """Gets the alert_type of this ManualVideoUploadAlert.  # noqa: E501


        :return: The alert_type of this ManualVideoUploadAlert.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this ManualVideoUploadAlert.


        :param alert_type: The alert_type of this ManualVideoUploadAlert.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_type`, must not be `None`")  # noqa: E501

        self._alert_type = alert_type

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
        if not isinstance(other, ManualVideoUploadAlert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ManualVideoUploadAlert):
            return True

        return self.to_dict() != other.to_dict()
