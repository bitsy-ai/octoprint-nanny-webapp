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


class RemoteControlCommandAlert(object):
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
        'alert_subtype': 'AlertSubtypeEnum',
        'alert_methods': 'list[AlertMethodsEnum]',
        'alert_type': 'AlertTypeEnum',
        'color': 'str',
        'created_dt': 'datetime',
        'dashboard_url': 'str',
        'dismissed': 'bool',
        'metadata': 'str',
        'icon': 'str',
        'id': 'int',
        'time': 'str',
        'description': 'str',
        'seen': 'bool',
        'snapshot_url': 'str',
        'title': 'str',
        'updated_dt': 'datetime',
        'user': 'int'
    }

    attribute_map = {
        'alert_subtype': 'alert_subtype',
        'alert_methods': 'alert_methods',
        'alert_type': 'alert_type',
        'color': 'color',
        'created_dt': 'created_dt',
        'dashboard_url': 'dashboard_url',
        'dismissed': 'dismissed',
        'metadata': 'metadata',
        'icon': 'icon',
        'id': 'id',
        'time': 'time',
        'description': 'description',
        'seen': 'seen',
        'snapshot_url': 'snapshot_url',
        'title': 'title',
        'updated_dt': 'updated_dt',
        'user': 'user'
    }

    def __init__(self, alert_subtype=None, alert_methods=None, alert_type=None, color=None, created_dt=None, dashboard_url=None, dismissed=None, metadata=None, icon=None, id=None, time=None, description=None, seen=None, snapshot_url=None, title=None, updated_dt=None, user=None, local_vars_configuration=None):  # noqa: E501
        """RemoteControlCommandAlert - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alert_subtype = None
        self._alert_methods = None
        self._alert_type = None
        self._color = None
        self._created_dt = None
        self._dashboard_url = None
        self._dismissed = None
        self._metadata = None
        self._icon = None
        self._id = None
        self._time = None
        self._description = None
        self._seen = None
        self._snapshot_url = None
        self._title = None
        self._updated_dt = None
        self._user = None
        self.discriminator = None

        self.alert_subtype = alert_subtype
        if alert_methods is not None:
            self.alert_methods = alert_methods
        self.alert_type = alert_type
        self.color = color
        if created_dt is not None:
            self.created_dt = created_dt
        if dashboard_url is not None:
            self.dashboard_url = dashboard_url
        if dismissed is not None:
            self.dismissed = dismissed
        if metadata is not None:
            self.metadata = metadata
        self.icon = icon
        if id is not None:
            self.id = id
        if time is not None:
            self.time = time
        self.description = description
        if seen is not None:
            self.seen = seen
        if snapshot_url is not None:
            self.snapshot_url = snapshot_url
        self.title = title
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if user is not None:
            self.user = user

    @property
    def alert_subtype(self):
        """Gets the alert_subtype of this RemoteControlCommandAlert.  # noqa: E501


        :return: The alert_subtype of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: AlertSubtypeEnum
        """
        return self._alert_subtype

    @alert_subtype.setter
    def alert_subtype(self, alert_subtype):
        """Sets the alert_subtype of this RemoteControlCommandAlert.


        :param alert_subtype: The alert_subtype of this RemoteControlCommandAlert.  # noqa: E501
        :type alert_subtype: AlertSubtypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_subtype`, must not be `None`")  # noqa: E501

        self._alert_subtype = alert_subtype

    @property
    def alert_methods(self):
        """Gets the alert_methods of this RemoteControlCommandAlert.  # noqa: E501


        :return: The alert_methods of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: list[AlertMethodsEnum]
        """
        return self._alert_methods

    @alert_methods.setter
    def alert_methods(self, alert_methods):
        """Sets the alert_methods of this RemoteControlCommandAlert.


        :param alert_methods: The alert_methods of this RemoteControlCommandAlert.  # noqa: E501
        :type alert_methods: list[AlertMethodsEnum]
        """

        self._alert_methods = alert_methods

    @property
    def alert_type(self):
        """Gets the alert_type of this RemoteControlCommandAlert.  # noqa: E501


        :return: The alert_type of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this RemoteControlCommandAlert.


        :param alert_type: The alert_type of this RemoteControlCommandAlert.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_type`, must not be `None`")  # noqa: E501

        self._alert_type = alert_type

    @property
    def color(self):
        """Gets the color of this RemoteControlCommandAlert.  # noqa: E501


        :return: The color of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this RemoteControlCommandAlert.


        :param color: The color of this RemoteControlCommandAlert.  # noqa: E501
        :type color: str
        """
        if self.local_vars_configuration.client_side_validation and color is None:  # noqa: E501
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def created_dt(self):
        """Gets the created_dt of this RemoteControlCommandAlert.  # noqa: E501


        :return: The created_dt of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this RemoteControlCommandAlert.


        :param created_dt: The created_dt of this RemoteControlCommandAlert.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def dashboard_url(self):
        """Gets the dashboard_url of this RemoteControlCommandAlert.  # noqa: E501


        :return: The dashboard_url of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_url

    @dashboard_url.setter
    def dashboard_url(self, dashboard_url):
        """Sets the dashboard_url of this RemoteControlCommandAlert.


        :param dashboard_url: The dashboard_url of this RemoteControlCommandAlert.  # noqa: E501
        :type dashboard_url: str
        """

        self._dashboard_url = dashboard_url

    @property
    def dismissed(self):
        """Gets the dismissed of this RemoteControlCommandAlert.  # noqa: E501


        :return: The dismissed of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: bool
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        """Sets the dismissed of this RemoteControlCommandAlert.


        :param dismissed: The dismissed of this RemoteControlCommandAlert.  # noqa: E501
        :type dismissed: bool
        """

        self._dismissed = dismissed

    @property
    def metadata(self):
        """Gets the metadata of this RemoteControlCommandAlert.  # noqa: E501


        :return: The metadata of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this RemoteControlCommandAlert.


        :param metadata: The metadata of this RemoteControlCommandAlert.  # noqa: E501
        :type metadata: str
        """

        self._metadata = metadata

    @property
    def icon(self):
        """Gets the icon of this RemoteControlCommandAlert.  # noqa: E501


        :return: The icon of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this RemoteControlCommandAlert.


        :param icon: The icon of this RemoteControlCommandAlert.  # noqa: E501
        :type icon: str
        """
        if self.local_vars_configuration.client_side_validation and icon is None:  # noqa: E501
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this RemoteControlCommandAlert.  # noqa: E501


        :return: The id of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RemoteControlCommandAlert.


        :param id: The id of this RemoteControlCommandAlert.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def time(self):
        """Gets the time of this RemoteControlCommandAlert.  # noqa: E501


        :return: The time of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this RemoteControlCommandAlert.


        :param time: The time of this RemoteControlCommandAlert.  # noqa: E501
        :type time: str
        """

        self._time = time

    @property
    def description(self):
        """Gets the description of this RemoteControlCommandAlert.  # noqa: E501


        :return: The description of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RemoteControlCommandAlert.


        :param description: The description of this RemoteControlCommandAlert.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def seen(self):
        """Gets the seen of this RemoteControlCommandAlert.  # noqa: E501


        :return: The seen of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this RemoteControlCommandAlert.


        :param seen: The seen of this RemoteControlCommandAlert.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def snapshot_url(self):
        """Gets the snapshot_url of this RemoteControlCommandAlert.  # noqa: E501


        :return: The snapshot_url of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._snapshot_url

    @snapshot_url.setter
    def snapshot_url(self, snapshot_url):
        """Sets the snapshot_url of this RemoteControlCommandAlert.


        :param snapshot_url: The snapshot_url of this RemoteControlCommandAlert.  # noqa: E501
        :type snapshot_url: str
        """

        self._snapshot_url = snapshot_url

    @property
    def title(self):
        """Gets the title of this RemoteControlCommandAlert.  # noqa: E501


        :return: The title of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RemoteControlCommandAlert.


        :param title: The title of this RemoteControlCommandAlert.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def updated_dt(self):
        """Gets the updated_dt of this RemoteControlCommandAlert.  # noqa: E501


        :return: The updated_dt of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this RemoteControlCommandAlert.


        :param updated_dt: The updated_dt of this RemoteControlCommandAlert.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def user(self):
        """Gets the user of this RemoteControlCommandAlert.  # noqa: E501


        :return: The user of this RemoteControlCommandAlert.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RemoteControlCommandAlert.


        :param user: The user of this RemoteControlCommandAlert.  # noqa: E501
        :type user: int
        """

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
        if not isinstance(other, RemoteControlCommandAlert):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RemoteControlCommandAlert):
            return True

        return self.to_dict() != other.to_dict()
