# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@bitsy.ai
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from print_nanny_client.configuration import Configuration


class TelemetryEventEventTypeEnum(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    PLUGIN_OCTOPRINT_NANNY_MONITORING_START = "plugin_octoprint_nanny_monitoring_start"
    PLUGIN_OCTOPRINT_NANNY_MONITORING_STOP = "plugin_octoprint_nanny_monitoring_stop"
    PLUGIN_OCTOPRINT_NANNY_MONITORING_RESET = "plugin_octoprint_nanny_monitoring_reset"
    PLUGIN_OCTOPRINT_NANNY_DEVICE_REGISTER_START = "plugin_octoprint_nanny_device_register_start"
    PLUGIN_OCTOPRINT_NANNY_DEVICE_REGISTER_DONE = "plugin_octoprint_nanny_device_register_done"
    PLUGIN_OCTOPRINT_NANNY_DEVICE_REGISTER_FAILED = "plugin_octoprint_nanny_device_register_failed"
    PLUGIN_OCTOPRINT_NANNY_DEVICE_RESET = "plugin_octoprint_nanny_device_reset"
    PLUGIN_OCTOPRINT_NANNY_PRINTER_PROFILE_SYNC_START = "plugin_octoprint_nanny_printer_profile_sync_start"
    PLUGIN_OCTOPRINT_NANNY_PRINTER_PROFILE_SYNC_DONE = "plugin_octoprint_nanny_printer_profile_sync_done"
    PLUGIN_OCTOPRINT_NANNY_PRINTER_PROFILE_SYNC_FAILED = "plugin_octoprint_nanny_printer_profile_sync_failed"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_REST_API = "plugin_octoprint_nanny_connect_test_rest_api"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_REST_API_FAILED = "plugin_octoprint_nanny_connect_test_rest_api_failed"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_REST_API_SUCCESS = "plugin_octoprint_nanny_connect_test_rest_api_success"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PING = "plugin_octoprint_nanny_connect_test_mqtt_ping"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PING_FAILED = "plugin_octoprint_nanny_connect_test_mqtt_ping_failed"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PING_SUCCESS = "plugin_octoprint_nanny_connect_test_mqtt_ping_success"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PONG = "plugin_octoprint_nanny_connect_test_mqtt_pong"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PONG_FAILED = "plugin_octoprint_nanny_connect_test_mqtt_pong_failed"
    PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PONG_SUCCESS = "plugin_octoprint_nanny_connect_test_mqtt_pong_success"
    CLIENTAUTHED = "ClientAuthed"
    CLIENTCLOSED = "ClientClosed"
    CLIENTDEAUTHED = "ClientDeauthed"
    CLIENTOPENED = "ClientOpened"
    SETTINGSUPDATED = "SettingsUpdated"
    USERLOGGEDIN = "UserLoggedIn"
    USERLOGGEDOUT = "UserLoggedOut"
    FILEADDED = "FileAdded"
    FILEREMOVED = "FileRemoved"
    FOLDERADDED = "FolderAdded"
    FOLDERREMOVED = "FolderRemoved"
    TRANSFERDONE = "TransferDone"
    TRANSFERFAILED = "TransferFailed"
    TRANSFERSTARTED = "TransferStarted"
    UPDATEDFILES = "UpdatedFiles"
    UPLOAD = "Upload"
    CAPTUREDONE = "CaptureDone"
    CAPTUREFAILED = "CaptureFailed"
    CAPTURESTART = "CaptureStart"
    MOVIEDONE = "MovieDone"
    MOVIEFAILED = "MovieFailed"
    MOVIERENDERING = "MovieRendering"
    POSTROLLEND = "PostRollEnd"
    POSTROLLSTART = "PostRollStart"
    SLICINGCANCELLED = "SlicingCancelled"
    SLICINGDONE = "SlicingDone"
    SLICINGFAILED = "SlicingFailed"
    SLICINGPROFILEADDED = "SlicingProfileAdded"
    SLICINGPROFILEDELETED = "SlicingProfileDeleted"
    SLICINGPROFILEMODIFIED = "SlicingProfileModified"
    SLICINGSTARTED = "SlicingStarted"
    CONNECTED = "Connected"
    DISCONNECTED = "Disconnected"
    PRINTERRESET = "PrinterReset"
    FIRMWAREDATA = "FirmwareData"
    PRINTERSTATECHANGED = "PrinterStateChanged"
    PRINTERPROFILEADDED = "PrinterProfileAdded"
    PRINTERPROFILEDELETED = "PrinterProfileDeleted"
    PRINTERPROFILEMODIFIED = "PrinterProfileModified"
    PRINTPROGRESS = "PrintProgress"
    PLUGIN_PI_SUPPORT_THROTTLE_STATE = "plugin_pi_support_throttle_state"
    SHUTDOWN = "Shutdown"
    STARTUP = "Startup"
    REMOTE_COMMAND_RECEIVED = "remote_command_received"
    REMOTE_COMMAND_FAILED = "remote_command_failed"
    REMOTE_COMMAND_SUCCESS = "remote_command_success"
    PRINTCANCELLED = "PrintCancelled"
    PRINTCANCELLING = "PrintCancelling"
    PRINTDONE = "PrintDone"
    PRINTFAILED = "PrintFailed"
    PRINTPAUSED = "PrintPaused"
    PRINTRESUMED = "PrintResumed"
    PRINTSTARTED = "PrintStarted"

    allowable_values = [PLUGIN_OCTOPRINT_NANNY_MONITORING_START, PLUGIN_OCTOPRINT_NANNY_MONITORING_STOP, PLUGIN_OCTOPRINT_NANNY_MONITORING_RESET, PLUGIN_OCTOPRINT_NANNY_DEVICE_REGISTER_START, PLUGIN_OCTOPRINT_NANNY_DEVICE_REGISTER_DONE, PLUGIN_OCTOPRINT_NANNY_DEVICE_REGISTER_FAILED, PLUGIN_OCTOPRINT_NANNY_DEVICE_RESET, PLUGIN_OCTOPRINT_NANNY_PRINTER_PROFILE_SYNC_START, PLUGIN_OCTOPRINT_NANNY_PRINTER_PROFILE_SYNC_DONE, PLUGIN_OCTOPRINT_NANNY_PRINTER_PROFILE_SYNC_FAILED, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_REST_API, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_REST_API_FAILED, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_REST_API_SUCCESS, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PING, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PING_FAILED, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PING_SUCCESS, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PONG, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PONG_FAILED, PLUGIN_OCTOPRINT_NANNY_CONNECT_TEST_MQTT_PONG_SUCCESS, CLIENTAUTHED, CLIENTCLOSED, CLIENTDEAUTHED, CLIENTOPENED, SETTINGSUPDATED, USERLOGGEDIN, USERLOGGEDOUT, FILEADDED, FILEREMOVED, FOLDERADDED, FOLDERREMOVED, TRANSFERDONE, TRANSFERFAILED, TRANSFERSTARTED, UPDATEDFILES, UPLOAD, CAPTUREDONE, CAPTUREFAILED, CAPTURESTART, MOVIEDONE, MOVIEFAILED, MOVIERENDERING, POSTROLLEND, POSTROLLSTART, SLICINGCANCELLED, SLICINGDONE, SLICINGFAILED, SLICINGPROFILEADDED, SLICINGPROFILEDELETED, SLICINGPROFILEMODIFIED, SLICINGSTARTED, CONNECTED, DISCONNECTED, PRINTERRESET, FIRMWAREDATA, PRINTERSTATECHANGED, PRINTERPROFILEADDED, PRINTERPROFILEDELETED, PRINTERPROFILEMODIFIED, PRINTPROGRESS, PLUGIN_PI_SUPPORT_THROTTLE_STATE, SHUTDOWN, STARTUP, REMOTE_COMMAND_RECEIVED, REMOTE_COMMAND_FAILED, REMOTE_COMMAND_SUCCESS, PRINTCANCELLED, PRINTCANCELLING, PRINTDONE, PRINTFAILED, PRINTPAUSED, PRINTRESUMED, PRINTSTARTED]  # noqa: E501

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self, local_vars_configuration=None):  # noqa: E501
        """TelemetryEventEventTypeEnum - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration
        self.discriminator = None

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
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
        if not isinstance(other, TelemetryEventEventTypeEnum):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TelemetryEventEventTypeEnum):
            return True

        return self.to_dict() != other.to_dict()