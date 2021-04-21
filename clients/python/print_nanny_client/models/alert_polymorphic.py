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


class AlertPolymorphic(object):
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
        'time': 'str',
        'seen': 'bool',
        'alert_subtype': 'PrintSessionAlertAlertSubtypeEnum',
        'alert_methods': 'list[AlertMethodsEnum]',
        'alert_type': 'AlertTypeEnum',
        'color': 'str',
        'dashboard_url': 'str',
        'metadata': 'str',
        'icon': 'str',
        'id': 'int',
        'description': 'str',
        'title': 'str',
        'sent': 'bool',
        'progress_percent': 'int',
        'polymorphic_ctype': 'int',
        'octoprint_device': 'int',
        'device': 'int',
        'needs_review': 'bool',
        'annotated_video': 'str',
        'print_session': 'int'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'updated_dt': 'updated_dt',
        'user': 'user',
        'time': 'time',
        'seen': 'seen',
        'alert_subtype': 'alert_subtype',
        'alert_methods': 'alert_methods',
        'alert_type': 'alert_type',
        'color': 'color',
        'dashboard_url': 'dashboard_url',
        'metadata': 'metadata',
        'icon': 'icon',
        'id': 'id',
        'description': 'description',
        'title': 'title',
        'sent': 'sent',
        'progress_percent': 'progress_percent',
        'polymorphic_ctype': 'polymorphic_ctype',
        'octoprint_device': 'octoprint_device',
        'device': 'device',
        'needs_review': 'needs_review',
        'annotated_video': 'annotated_video',
        'print_session': 'print_session'
    }

    discriminator_value_class_map = {
    }

    def __init__(self, created_dt=None, updated_dt=None, user=None, time=None, seen=None, alert_subtype=None, alert_methods=None, alert_type=None, color=None, dashboard_url=None, metadata=None, icon=None, id=None, description=None, title=None, sent=None, progress_percent=None, polymorphic_ctype=None, octoprint_device=None, device=None, needs_review=None, annotated_video=None, print_session=None, local_vars_configuration=None):  # noqa: E501
        """AlertPolymorphic - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._updated_dt = None
        self._user = None
        self._time = None
        self._seen = None
        self._alert_subtype = None
        self._alert_methods = None
        self._alert_type = None
        self._color = None
        self._dashboard_url = None
        self._metadata = None
        self._icon = None
        self._id = None
        self._description = None
        self._title = None
        self._sent = None
        self._progress_percent = None
        self._polymorphic_ctype = None
        self._octoprint_device = None
        self._device = None
        self._needs_review = None
        self._annotated_video = None
        self._print_session = None
        self.discriminator = 'type'

        if created_dt is not None:
            self.created_dt = created_dt
        if updated_dt is not None:
            self.updated_dt = updated_dt
        if user is not None:
            self.user = user
        if time is not None:
            self.time = time
        if seen is not None:
            self.seen = seen
        self.alert_subtype = alert_subtype
        if alert_methods is not None:
            self.alert_methods = alert_methods
        self.alert_type = alert_type
        self.color = color
        if dashboard_url is not None:
            self.dashboard_url = dashboard_url
        if metadata is not None:
            self.metadata = metadata
        self.icon = icon
        if id is not None:
            self.id = id
        self.description = description
        self.title = title
        if sent is not None:
            self.sent = sent
        if progress_percent is not None:
            self.progress_percent = progress_percent
        if polymorphic_ctype is not None:
            self.polymorphic_ctype = polymorphic_ctype
        if octoprint_device is not None:
            self.octoprint_device = octoprint_device
        self.device = device
        if needs_review is not None:
            self.needs_review = needs_review
        self.annotated_video = annotated_video
        self.print_session = print_session

    @property
    def created_dt(self):
        """Gets the created_dt of this AlertPolymorphic.  # noqa: E501


        :return: The created_dt of this AlertPolymorphic.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this AlertPolymorphic.


        :param created_dt: The created_dt of this AlertPolymorphic.  # noqa: E501
        :type created_dt: datetime
        """

        self._created_dt = created_dt

    @property
    def updated_dt(self):
        """Gets the updated_dt of this AlertPolymorphic.  # noqa: E501


        :return: The updated_dt of this AlertPolymorphic.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this AlertPolymorphic.


        :param updated_dt: The updated_dt of this AlertPolymorphic.  # noqa: E501
        :type updated_dt: datetime
        """

        self._updated_dt = updated_dt

    @property
    def user(self):
        """Gets the user of this AlertPolymorphic.  # noqa: E501


        :return: The user of this AlertPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AlertPolymorphic.


        :param user: The user of this AlertPolymorphic.  # noqa: E501
        :type user: int
        """

        self._user = user

    @property
    def time(self):
        """Gets the time of this AlertPolymorphic.  # noqa: E501


        :return: The time of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this AlertPolymorphic.


        :param time: The time of this AlertPolymorphic.  # noqa: E501
        :type time: str
        """

        self._time = time

    @property
    def seen(self):
        """Gets the seen of this AlertPolymorphic.  # noqa: E501


        :return: The seen of this AlertPolymorphic.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this AlertPolymorphic.


        :param seen: The seen of this AlertPolymorphic.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def alert_subtype(self):
        """Gets the alert_subtype of this AlertPolymorphic.  # noqa: E501


        :return: The alert_subtype of this AlertPolymorphic.  # noqa: E501
        :rtype: PrintSessionAlertAlertSubtypeEnum
        """
        return self._alert_subtype

    @alert_subtype.setter
    def alert_subtype(self, alert_subtype):
        """Sets the alert_subtype of this AlertPolymorphic.


        :param alert_subtype: The alert_subtype of this AlertPolymorphic.  # noqa: E501
        :type alert_subtype: PrintSessionAlertAlertSubtypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_subtype is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_subtype`, must not be `None`")  # noqa: E501

        self._alert_subtype = alert_subtype

    @property
    def alert_methods(self):
        """Gets the alert_methods of this AlertPolymorphic.  # noqa: E501


        :return: The alert_methods of this AlertPolymorphic.  # noqa: E501
        :rtype: list[AlertMethodsEnum]
        """
        return self._alert_methods

    @alert_methods.setter
    def alert_methods(self, alert_methods):
        """Sets the alert_methods of this AlertPolymorphic.


        :param alert_methods: The alert_methods of this AlertPolymorphic.  # noqa: E501
        :type alert_methods: list[AlertMethodsEnum]
        """

        self._alert_methods = alert_methods

    @property
    def alert_type(self):
        """Gets the alert_type of this AlertPolymorphic.  # noqa: E501


        :return: The alert_type of this AlertPolymorphic.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this AlertPolymorphic.


        :param alert_type: The alert_type of this AlertPolymorphic.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_type`, must not be `None`")  # noqa: E501

        self._alert_type = alert_type

    @property
    def color(self):
        """Gets the color of this AlertPolymorphic.  # noqa: E501


        :return: The color of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this AlertPolymorphic.


        :param color: The color of this AlertPolymorphic.  # noqa: E501
        :type color: str
        """
        if self.local_vars_configuration.client_side_validation and color is None:  # noqa: E501
            raise ValueError("Invalid value for `color`, must not be `None`")  # noqa: E501

        self._color = color

    @property
    def dashboard_url(self):
        """Gets the dashboard_url of this AlertPolymorphic.  # noqa: E501


        :return: The dashboard_url of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_url

    @dashboard_url.setter
    def dashboard_url(self, dashboard_url):
        """Sets the dashboard_url of this AlertPolymorphic.


        :param dashboard_url: The dashboard_url of this AlertPolymorphic.  # noqa: E501
        :type dashboard_url: str
        """

        self._dashboard_url = dashboard_url

    @property
    def metadata(self):
        """Gets the metadata of this AlertPolymorphic.  # noqa: E501


        :return: The metadata of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this AlertPolymorphic.


        :param metadata: The metadata of this AlertPolymorphic.  # noqa: E501
        :type metadata: str
        """

        self._metadata = metadata

    @property
    def icon(self):
        """Gets the icon of this AlertPolymorphic.  # noqa: E501


        :return: The icon of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this AlertPolymorphic.


        :param icon: The icon of this AlertPolymorphic.  # noqa: E501
        :type icon: str
        """
        if self.local_vars_configuration.client_side_validation and icon is None:  # noqa: E501
            raise ValueError("Invalid value for `icon`, must not be `None`")  # noqa: E501

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this AlertPolymorphic.  # noqa: E501


        :return: The id of this AlertPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlertPolymorphic.


        :param id: The id of this AlertPolymorphic.  # noqa: E501
        :type id: int
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this AlertPolymorphic.  # noqa: E501


        :return: The description of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AlertPolymorphic.


        :param description: The description of this AlertPolymorphic.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def title(self):
        """Gets the title of this AlertPolymorphic.  # noqa: E501


        :return: The title of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AlertPolymorphic.


        :param title: The title of this AlertPolymorphic.  # noqa: E501
        :type title: str
        """
        if self.local_vars_configuration.client_side_validation and title is None:  # noqa: E501
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def sent(self):
        """Gets the sent of this AlertPolymorphic.  # noqa: E501


        :return: The sent of this AlertPolymorphic.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this AlertPolymorphic.


        :param sent: The sent of this AlertPolymorphic.  # noqa: E501
        :type sent: bool
        """

        self._sent = sent

    @property
    def progress_percent(self):
        """Gets the progress_percent of this AlertPolymorphic.  # noqa: E501

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :return: The progress_percent of this AlertPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._progress_percent

    @progress_percent.setter
    def progress_percent(self, progress_percent):
        """Sets the progress_percent of this AlertPolymorphic.

        Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress  # noqa: E501

        :param progress_percent: The progress_percent of this AlertPolymorphic.  # noqa: E501
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
    def polymorphic_ctype(self):
        """Gets the polymorphic_ctype of this AlertPolymorphic.  # noqa: E501


        :return: The polymorphic_ctype of this AlertPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._polymorphic_ctype

    @polymorphic_ctype.setter
    def polymorphic_ctype(self, polymorphic_ctype):
        """Sets the polymorphic_ctype of this AlertPolymorphic.


        :param polymorphic_ctype: The polymorphic_ctype of this AlertPolymorphic.  # noqa: E501
        :type polymorphic_ctype: int
        """

        self._polymorphic_ctype = polymorphic_ctype

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this AlertPolymorphic.  # noqa: E501


        :return: The octoprint_device of this AlertPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this AlertPolymorphic.


        :param octoprint_device: The octoprint_device of this AlertPolymorphic.  # noqa: E501
        :type octoprint_device: int
        """

        self._octoprint_device = octoprint_device

    @property
    def device(self):
        """Gets the device of this AlertPolymorphic.  # noqa: E501


        :return: The device of this AlertPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this AlertPolymorphic.


        :param device: The device of this AlertPolymorphic.  # noqa: E501
        :type device: int
        """
        if self.local_vars_configuration.client_side_validation and device is None:  # noqa: E501
            raise ValueError("Invalid value for `device`, must not be `None`")  # noqa: E501

        self._device = device

    @property
    def needs_review(self):
        """Gets the needs_review of this AlertPolymorphic.  # noqa: E501


        :return: The needs_review of this AlertPolymorphic.  # noqa: E501
        :rtype: bool
        """
        return self._needs_review

    @needs_review.setter
    def needs_review(self, needs_review):
        """Sets the needs_review of this AlertPolymorphic.


        :param needs_review: The needs_review of this AlertPolymorphic.  # noqa: E501
        :type needs_review: bool
        """

        self._needs_review = needs_review

    @property
    def annotated_video(self):
        """Gets the annotated_video of this AlertPolymorphic.  # noqa: E501


        :return: The annotated_video of this AlertPolymorphic.  # noqa: E501
        :rtype: str
        """
        return self._annotated_video

    @annotated_video.setter
    def annotated_video(self, annotated_video):
        """Sets the annotated_video of this AlertPolymorphic.


        :param annotated_video: The annotated_video of this AlertPolymorphic.  # noqa: E501
        :type annotated_video: str
        """
        if self.local_vars_configuration.client_side_validation and annotated_video is None:  # noqa: E501
            raise ValueError("Invalid value for `annotated_video`, must not be `None`")  # noqa: E501

        self._annotated_video = annotated_video

    @property
    def print_session(self):
        """Gets the print_session of this AlertPolymorphic.  # noqa: E501


        :return: The print_session of this AlertPolymorphic.  # noqa: E501
        :rtype: int
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this AlertPolymorphic.


        :param print_session: The print_session of this AlertPolymorphic.  # noqa: E501
        :type print_session: int
        """
        if self.local_vars_configuration.client_side_validation and print_session is None:  # noqa: E501
            raise ValueError("Invalid value for `print_session`, must not be `None`")  # noqa: E501

        self._print_session = print_session

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, AlertPolymorphic):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AlertPolymorphic):
            return True

        return self.to_dict() != other.to_dict()
