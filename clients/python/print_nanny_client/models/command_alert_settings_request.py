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


class CommandAlertSettingsRequest(object):
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
        'alert_type': 'AlertTypeEnum',
        'alert_methods': 'list[AlertMethodsEnum]',
        'enabled': 'bool',
        'monitoring_stop': 'list[MoveNozzleEnum]',
        'monitoring_start': 'list[MoveNozzleEnum]',
        'print_start': 'list[MoveNozzleEnum]',
        'print_stop': 'list[MoveNozzleEnum]',
        'print_pause': 'list[MoveNozzleEnum]',
        'print_resume': 'list[MoveNozzleEnum]',
        'move_nozzle': 'list[MoveNozzleEnum]'
    }

    attribute_map = {
        'alert_type': 'alert_type',
        'alert_methods': 'alert_methods',
        'enabled': 'enabled',
        'monitoring_stop': 'monitoring_stop',
        'monitoring_start': 'monitoring_start',
        'print_start': 'print_start',
        'print_stop': 'print_stop',
        'print_pause': 'print_pause',
        'print_resume': 'print_resume',
        'move_nozzle': 'move_nozzle'
    }

    def __init__(self, alert_type=None, alert_methods=None, enabled=None, monitoring_stop=None, monitoring_start=None, print_start=None, print_stop=None, print_pause=None, print_resume=None, move_nozzle=None, local_vars_configuration=None):  # noqa: E501
        """CommandAlertSettingsRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._alert_type = None
        self._alert_methods = None
        self._enabled = None
        self._monitoring_stop = None
        self._monitoring_start = None
        self._print_start = None
        self._print_stop = None
        self._print_pause = None
        self._print_resume = None
        self._move_nozzle = None
        self.discriminator = None

        self.alert_type = alert_type
        if alert_methods is not None:
            self.alert_methods = alert_methods
        if enabled is not None:
            self.enabled = enabled
        if monitoring_stop is not None:
            self.monitoring_stop = monitoring_stop
        if monitoring_start is not None:
            self.monitoring_start = monitoring_start
        if print_start is not None:
            self.print_start = print_start
        if print_stop is not None:
            self.print_stop = print_stop
        if print_pause is not None:
            self.print_pause = print_pause
        if print_resume is not None:
            self.print_resume = print_resume
        if move_nozzle is not None:
            self.move_nozzle = move_nozzle

    @property
    def alert_type(self):
        """Gets the alert_type of this CommandAlertSettingsRequest.  # noqa: E501


        :return: The alert_type of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: AlertTypeEnum
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this CommandAlertSettingsRequest.


        :param alert_type: The alert_type of this CommandAlertSettingsRequest.  # noqa: E501
        :type alert_type: AlertTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and alert_type is None:  # noqa: E501
            raise ValueError("Invalid value for `alert_type`, must not be `None`")  # noqa: E501

        self._alert_type = alert_type

    @property
    def alert_methods(self):
        """Gets the alert_methods of this CommandAlertSettingsRequest.  # noqa: E501


        :return: The alert_methods of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[AlertMethodsEnum]
        """
        return self._alert_methods

    @alert_methods.setter
    def alert_methods(self, alert_methods):
        """Sets the alert_methods of this CommandAlertSettingsRequest.


        :param alert_methods: The alert_methods of this CommandAlertSettingsRequest.  # noqa: E501
        :type alert_methods: list[AlertMethodsEnum]
        """

        self._alert_methods = alert_methods

    @property
    def enabled(self):
        """Gets the enabled of this CommandAlertSettingsRequest.  # noqa: E501

        Enable or disable this alert type  # noqa: E501

        :return: The enabled of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CommandAlertSettingsRequest.

        Enable or disable this alert type  # noqa: E501

        :param enabled: The enabled of this CommandAlertSettingsRequest.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def monitoring_stop(self):
        """Gets the monitoring_stop of this CommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes.  # noqa: E501

        :return: The monitoring_stop of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._monitoring_stop

    @monitoring_stop.setter
    def monitoring_stop(self, monitoring_stop):
        """Sets the monitoring_stop of this CommandAlertSettingsRequest.

        Fires on <strong>MonitoringStop<strong> updates.   Helps debug unexpected Print Nanny crashes.  # noqa: E501

        :param monitoring_stop: The monitoring_stop of this CommandAlertSettingsRequest.  # noqa: E501
        :type monitoring_stop: list[MoveNozzleEnum]
        """

        self._monitoring_stop = monitoring_stop

    @property
    def monitoring_start(self):
        """Gets the monitoring_start of this CommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.  # noqa: E501

        :return: The monitoring_start of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._monitoring_start

    @monitoring_start.setter
    def monitoring_start(self, monitoring_start):
        """Sets the monitoring_start of this CommandAlertSettingsRequest.

        Fires on <strong>MonitoringStop</strong> updates. Helpful if you want to confirm monitoring started without a problem.  # noqa: E501

        :param monitoring_start: The monitoring_start of this CommandAlertSettingsRequest.  # noqa: E501
        :type monitoring_start: list[MoveNozzleEnum]
        """

        self._monitoring_start = monitoring_start

    @property
    def print_start(self):
        """Gets the print_start of this CommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>StartPrint</strong> updates. Get notified as soon as a print job finishes.   # noqa: E501

        :return: The print_start of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_start

    @print_start.setter
    def print_start(self, print_start):
        """Sets the print_start of this CommandAlertSettingsRequest.

        Fires on <strong>StartPrint</strong> updates. Get notified as soon as a print job finishes.   # noqa: E501

        :param print_start: The print_start of this CommandAlertSettingsRequest.  # noqa: E501
        :type print_start: list[MoveNozzleEnum]
        """

        self._print_start = print_start

    @property
    def print_stop(self):
        """Gets the print_stop of this CommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.  # noqa: E501

        :return: The print_stop of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_stop

    @print_stop.setter
    def print_stop(self, print_stop):
        """Sets the print_stop of this CommandAlertSettingsRequest.

        Fires on <strong>PrintStart</strong> command status changes. Helpful for verifying a print job started without a problem.  # noqa: E501

        :param print_stop: The print_stop of this CommandAlertSettingsRequest.  # noqa: E501
        :type print_stop: list[MoveNozzleEnum]
        """

        self._print_stop = print_stop

    @property
    def print_pause(self):
        """Gets the print_pause of this CommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.  # noqa: E501

        :return: The print_pause of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_pause

    @print_pause.setter
    def print_pause(self, print_pause):
        """Sets the print_pause of this CommandAlertSettingsRequest.

        Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.  # noqa: E501

        :param print_pause: The print_pause of this CommandAlertSettingsRequest.  # noqa: E501
        :type print_pause: list[MoveNozzleEnum]
        """

        self._print_pause = print_pause

    @property
    def print_resume(self):
        """Gets the print_resume of this CommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.  # noqa: E501

        :return: The print_resume of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._print_resume

    @print_resume.setter
    def print_resume(self, print_resume):
        """Sets the print_resume of this CommandAlertSettingsRequest.

        Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.  # noqa: E501

        :param print_resume: The print_resume of this CommandAlertSettingsRequest.  # noqa: E501
        :type print_resume: list[MoveNozzleEnum]
        """

        self._print_resume = print_resume

    @property
    def move_nozzle(self):
        """Gets the move_nozzle of this CommandAlertSettingsRequest.  # noqa: E501

        Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint  # noqa: E501

        :return: The move_nozzle of this CommandAlertSettingsRequest.  # noqa: E501
        :rtype: list[MoveNozzleEnum]
        """
        return self._move_nozzle

    @move_nozzle.setter
    def move_nozzle(self, move_nozzle):
        """Sets the move_nozzle of this CommandAlertSettingsRequest.

        Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint  # noqa: E501

        :param move_nozzle: The move_nozzle of this CommandAlertSettingsRequest.  # noqa: E501
        :type move_nozzle: list[MoveNozzleEnum]
        """

        self._move_nozzle = move_nozzle

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
        if not isinstance(other, CommandAlertSettingsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CommandAlertSettingsRequest):
            return True

        return self.to_dict() != other.to_dict()
