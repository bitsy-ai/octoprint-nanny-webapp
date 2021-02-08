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


class RemoteControlSnapshotCreateResponse(object):
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
        'url': 'str',
        'id': 'int',
        'created_dt': 'datetime'
    }

    attribute_map = {
        'url': 'url',
        'id': 'id',
        'created_dt': 'created_dt'
    }

    def __init__(self, url=None, id=None, created_dt=None, local_vars_configuration=None):  # noqa: E501
        """RemoteControlSnapshotCreateResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._id = None
        self._created_dt = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if id is not None:
            self.id = id
        if created_dt is not None:
            self.created_dt = created_dt

    @property
    def url(self):
        """Gets the url of this RemoteControlSnapshotCreateResponse.  # noqa: E501


        :return: The url of this RemoteControlSnapshotCreateResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RemoteControlSnapshotCreateResponse.


        :param url: The url of this RemoteControlSnapshotCreateResponse.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def id(self):
        """Gets the id of this RemoteControlSnapshotCreateResponse.  # noqa: E501


        :return: The id of this RemoteControlSnapshotCreateResponse.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RemoteControlSnapshotCreateResponse.


        :param id: The id of this RemoteControlSnapshotCreateResponse.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def created_dt(self):
        """Gets the created_dt of this RemoteControlSnapshotCreateResponse.  # noqa: E501


        :return: The created_dt of this RemoteControlSnapshotCreateResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this RemoteControlSnapshotCreateResponse.


        :param created_dt: The created_dt of this RemoteControlSnapshotCreateResponse.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

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
        if not isinstance(other, RemoteControlSnapshotCreateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteControlSnapshotCreateResponse):
            return True

        return self.to_dict() != other.to_dict()