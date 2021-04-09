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


class PrintSessionAlertRequest(object):
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
        'dismissed': 'bool',
        'alert_subtype': 'PrintSessionAlertAlertSubtypeEnum',
        'annotated_video': 'file',
        'print_session': 'int'
    }

    attribute_map = {
        'seen': 'seen',
        'sent': 'sent',
        'dismissed': 'dismissed',
        'alert_subtype': 'alert_subtype',
        'annotated_video': 'annotated_video',
        'print_session': 'print_session'
    }

    def __init__(self, seen=None, sent=None, dismissed=None, alert_subtype=None, annotated_video=None, print_session=None, local_vars_configuration=None):  # noqa: E501
        """PrintSessionAlertRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._seen = None
        self._sent = None
        self._dismissed = None
        self._alert_subtype = None
        self._annotated_video = None
        self._print_session = None
        self.discriminator = None

        if seen is not None:
            self.seen = seen
        if sent is not None:
            self.sent = sent
        if dismissed is not None:
            self.dismissed = dismissed
        if alert_subtype is not None:
            self.alert_subtype = alert_subtype
        self.annotated_video = annotated_video
        self.print_session = print_session

    @property
    def seen(self):
        """Gets the seen of this PrintSessionAlertRequest.  # noqa: E501


        :return: The seen of this PrintSessionAlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._seen

    @seen.setter
    def seen(self, seen):
        """Sets the seen of this PrintSessionAlertRequest.


        :param seen: The seen of this PrintSessionAlertRequest.  # noqa: E501
        :type seen: bool
        """

        self._seen = seen

    @property
    def sent(self):
        """Gets the sent of this PrintSessionAlertRequest.  # noqa: E501


        :return: The sent of this PrintSessionAlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """Sets the sent of this PrintSessionAlertRequest.


        :param sent: The sent of this PrintSessionAlertRequest.  # noqa: E501
        :type sent: bool
        """

        self._sent = sent

    @property
    def dismissed(self):
        """Gets the dismissed of this PrintSessionAlertRequest.  # noqa: E501


        :return: The dismissed of this PrintSessionAlertRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dismissed

    @dismissed.setter
    def dismissed(self, dismissed):
        """Sets the dismissed of this PrintSessionAlertRequest.


        :param dismissed: The dismissed of this PrintSessionAlertRequest.  # noqa: E501
        :type dismissed: bool
        """

        self._dismissed = dismissed

    @property
    def alert_subtype(self):
        """Gets the alert_subtype of this PrintSessionAlertRequest.  # noqa: E501


        :return: The alert_subtype of this PrintSessionAlertRequest.  # noqa: E501
        :rtype: PrintSessionAlertAlertSubtypeEnum
        """
        return self._alert_subtype

    @alert_subtype.setter
    def alert_subtype(self, alert_subtype):
        """Sets the alert_subtype of this PrintSessionAlertRequest.


        :param alert_subtype: The alert_subtype of this PrintSessionAlertRequest.  # noqa: E501
        :type alert_subtype: PrintSessionAlertAlertSubtypeEnum
        """

        self._alert_subtype = alert_subtype

    @property
    def annotated_video(self):
        """Gets the annotated_video of this PrintSessionAlertRequest.  # noqa: E501


        :return: The annotated_video of this PrintSessionAlertRequest.  # noqa: E501
        :rtype: file
        """
        return self._annotated_video

    @annotated_video.setter
    def annotated_video(self, annotated_video):
        """Sets the annotated_video of this PrintSessionAlertRequest.


        :param annotated_video: The annotated_video of this PrintSessionAlertRequest.  # noqa: E501
        :type annotated_video: file
        """
        if self.local_vars_configuration.client_side_validation and annotated_video is None:  # noqa: E501
            raise ValueError("Invalid value for `annotated_video`, must not be `None`")  # noqa: E501

        self._annotated_video = annotated_video

    @property
    def print_session(self):
        """Gets the print_session of this PrintSessionAlertRequest.  # noqa: E501


        :return: The print_session of this PrintSessionAlertRequest.  # noqa: E501
        :rtype: int
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this PrintSessionAlertRequest.


        :param print_session: The print_session of this PrintSessionAlertRequest.  # noqa: E501
        :type print_session: int
        """
        if self.local_vars_configuration.client_side_validation and print_session is None:  # noqa: E501
            raise ValueError("Invalid value for `print_session`, must not be `None`")  # noqa: E501

        self._print_session = print_session

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
        if not isinstance(other, PrintSessionAlertRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintSessionAlertRequest):
            return True

        return self.to_dict() != other.to_dict()
