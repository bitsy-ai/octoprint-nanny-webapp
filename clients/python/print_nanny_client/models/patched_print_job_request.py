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


class PatchedPrintJobRequest(object):
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
        'print_session': 'int',
        'printer_profile': 'int',
        'name': 'str',
        'gcode_file': 'int',
        'progress': 'dict(str, object)',
        'octoprint_device': 'int'
    }

    attribute_map = {
        'print_session': 'print_session',
        'printer_profile': 'printer_profile',
        'name': 'name',
        'gcode_file': 'gcode_file',
        'progress': 'progress',
        'octoprint_device': 'octoprint_device'
    }

    def __init__(self, print_session=None, printer_profile=None, name=None, gcode_file=None, progress=None, octoprint_device=None, local_vars_configuration=None):  # noqa: E501
        """PatchedPrintJobRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._print_session = None
        self._printer_profile = None
        self._name = None
        self._gcode_file = None
        self._progress = None
        self._octoprint_device = None
        self.discriminator = None

        self.print_session = print_session
        if printer_profile is not None:
            self.printer_profile = printer_profile
        if name is not None:
            self.name = name
        self.gcode_file = gcode_file
        if progress is not None:
            self.progress = progress
        self.octoprint_device = octoprint_device

    @property
    def print_session(self):
        """Gets the print_session of this PatchedPrintJobRequest.  # noqa: E501


        :return: The print_session of this PatchedPrintJobRequest.  # noqa: E501
        :rtype: int
        """
        return self._print_session

    @print_session.setter
    def print_session(self, print_session):
        """Sets the print_session of this PatchedPrintJobRequest.


        :param print_session: The print_session of this PatchedPrintJobRequest.  # noqa: E501
        :type print_session: int
        """

        self._print_session = print_session

    @property
    def printer_profile(self):
        """Gets the printer_profile of this PatchedPrintJobRequest.  # noqa: E501


        :return: The printer_profile of this PatchedPrintJobRequest.  # noqa: E501
        :rtype: int
        """
        return self._printer_profile

    @printer_profile.setter
    def printer_profile(self, printer_profile):
        """Sets the printer_profile of this PatchedPrintJobRequest.


        :param printer_profile: The printer_profile of this PatchedPrintJobRequest.  # noqa: E501
        :type printer_profile: int
        """

        self._printer_profile = printer_profile

    @property
    def name(self):
        """Gets the name of this PatchedPrintJobRequest.  # noqa: E501


        :return: The name of this PatchedPrintJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchedPrintJobRequest.


        :param name: The name of this PatchedPrintJobRequest.  # noqa: E501
        :type name: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def gcode_file(self):
        """Gets the gcode_file of this PatchedPrintJobRequest.  # noqa: E501


        :return: The gcode_file of this PatchedPrintJobRequest.  # noqa: E501
        :rtype: int
        """
        return self._gcode_file

    @gcode_file.setter
    def gcode_file(self, gcode_file):
        """Sets the gcode_file of this PatchedPrintJobRequest.


        :param gcode_file: The gcode_file of this PatchedPrintJobRequest.  # noqa: E501
        :type gcode_file: int
        """

        self._gcode_file = gcode_file

    @property
    def progress(self):
        """Gets the progress of this PatchedPrintJobRequest.  # noqa: E501


        :return: The progress of this PatchedPrintJobRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this PatchedPrintJobRequest.


        :param progress: The progress of this PatchedPrintJobRequest.  # noqa: E501
        :type progress: dict(str, object)
        """

        self._progress = progress

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this PatchedPrintJobRequest.  # noqa: E501


        :return: The octoprint_device of this PatchedPrintJobRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this PatchedPrintJobRequest.


        :param octoprint_device: The octoprint_device of this PatchedPrintJobRequest.  # noqa: E501
        :type octoprint_device: int
        """

        self._octoprint_device = octoprint_device

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
        if not isinstance(other, PatchedPrintJobRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchedPrintJobRequest):
            return True

        return self.to_dict() != other.to_dict()
