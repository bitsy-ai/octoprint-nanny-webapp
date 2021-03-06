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


class PrintSessionRequest(object):
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
        'octoprint_device': 'int',
        'active': 'bool',
        'session': 'str',
        'filepos': 'int',
        'print_progress': 'int',
        'time_elapsed': 'int',
        'time_remaining': 'int',
        'printer_profile': 'int',
        'gcode_file': 'int',
        'gcode_filename': 'str',
        'octoprint_job': 'dict(str, object)',
        'print_job_status': 'PrintJobStatusEnum'
    }

    attribute_map = {
        'created_dt': 'created_dt',
        'octoprint_device': 'octoprint_device',
        'active': 'active',
        'session': 'session',
        'filepos': 'filepos',
        'print_progress': 'print_progress',
        'time_elapsed': 'time_elapsed',
        'time_remaining': 'time_remaining',
        'printer_profile': 'printer_profile',
        'gcode_file': 'gcode_file',
        'gcode_filename': 'gcode_filename',
        'octoprint_job': 'octoprint_job',
        'print_job_status': 'print_job_status'
    }

    def __init__(self, created_dt=None, octoprint_device=None, active=None, session=None, filepos=None, print_progress=None, time_elapsed=None, time_remaining=None, printer_profile=None, gcode_file=None, gcode_filename=None, octoprint_job=None, print_job_status=None, local_vars_configuration=None):  # noqa: E501
        """PrintSessionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._created_dt = None
        self._octoprint_device = None
        self._active = None
        self._session = None
        self._filepos = None
        self._print_progress = None
        self._time_elapsed = None
        self._time_remaining = None
        self._printer_profile = None
        self._gcode_file = None
        self._gcode_filename = None
        self._octoprint_job = None
        self._print_job_status = None
        self.discriminator = None

        self.created_dt = created_dt
        self.octoprint_device = octoprint_device
        if active is not None:
            self.active = active
        self.session = session
        self.filepos = filepos
        self.print_progress = print_progress
        self.time_elapsed = time_elapsed
        self.time_remaining = time_remaining
        self.printer_profile = printer_profile
        self.gcode_file = gcode_file
        self.gcode_filename = gcode_filename
        self.octoprint_job = octoprint_job
        self.print_job_status = print_job_status

    @property
    def created_dt(self):
        """Gets the created_dt of this PrintSessionRequest.  # noqa: E501


        :return: The created_dt of this PrintSessionRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this PrintSessionRequest.


        :param created_dt: The created_dt of this PrintSessionRequest.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def octoprint_device(self):
        """Gets the octoprint_device of this PrintSessionRequest.  # noqa: E501


        :return: The octoprint_device of this PrintSessionRequest.  # noqa: E501
        :rtype: int
        """
        return self._octoprint_device

    @octoprint_device.setter
    def octoprint_device(self, octoprint_device):
        """Sets the octoprint_device of this PrintSessionRequest.


        :param octoprint_device: The octoprint_device of this PrintSessionRequest.  # noqa: E501
        :type octoprint_device: int
        """
        if self.local_vars_configuration.client_side_validation and octoprint_device is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_device`, must not be `None`")  # noqa: E501

        self._octoprint_device = octoprint_device

    @property
    def active(self):
        """Gets the active of this PrintSessionRequest.  # noqa: E501


        :return: The active of this PrintSessionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PrintSessionRequest.


        :param active: The active of this PrintSessionRequest.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def session(self):
        """Gets the session of this PrintSessionRequest.  # noqa: E501


        :return: The session of this PrintSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this PrintSessionRequest.


        :param session: The session of this PrintSessionRequest.  # noqa: E501
        :type session: str
        """
        if self.local_vars_configuration.client_side_validation and session is None:  # noqa: E501
            raise ValueError("Invalid value for `session`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                session is not None and len(session) > 255):
            raise ValueError("Invalid value for `session`, length must be less than or equal to `255`")  # noqa: E501

        self._session = session

    @property
    def filepos(self):
        """Gets the filepos of this PrintSessionRequest.  # noqa: E501


        :return: The filepos of this PrintSessionRequest.  # noqa: E501
        :rtype: int
        """
        return self._filepos

    @filepos.setter
    def filepos(self, filepos):
        """Sets the filepos of this PrintSessionRequest.


        :param filepos: The filepos of this PrintSessionRequest.  # noqa: E501
        :type filepos: int
        """
        if (self.local_vars_configuration.client_side_validation and
                filepos is not None and filepos > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `filepos`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                filepos is not None and filepos < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `filepos`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._filepos = filepos

    @property
    def print_progress(self):
        """Gets the print_progress of this PrintSessionRequest.  # noqa: E501


        :return: The print_progress of this PrintSessionRequest.  # noqa: E501
        :rtype: int
        """
        return self._print_progress

    @print_progress.setter
    def print_progress(self, print_progress):
        """Sets the print_progress of this PrintSessionRequest.


        :param print_progress: The print_progress of this PrintSessionRequest.  # noqa: E501
        :type print_progress: int
        """
        if (self.local_vars_configuration.client_side_validation and
                print_progress is not None and print_progress > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `print_progress`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_progress is not None and print_progress < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `print_progress`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._print_progress = print_progress

    @property
    def time_elapsed(self):
        """Gets the time_elapsed of this PrintSessionRequest.  # noqa: E501


        :return: The time_elapsed of this PrintSessionRequest.  # noqa: E501
        :rtype: int
        """
        return self._time_elapsed

    @time_elapsed.setter
    def time_elapsed(self, time_elapsed):
        """Sets the time_elapsed of this PrintSessionRequest.


        :param time_elapsed: The time_elapsed of this PrintSessionRequest.  # noqa: E501
        :type time_elapsed: int
        """
        if (self.local_vars_configuration.client_side_validation and
                time_elapsed is not None and time_elapsed > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `time_elapsed`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_elapsed is not None and time_elapsed < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `time_elapsed`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._time_elapsed = time_elapsed

    @property
    def time_remaining(self):
        """Gets the time_remaining of this PrintSessionRequest.  # noqa: E501


        :return: The time_remaining of this PrintSessionRequest.  # noqa: E501
        :rtype: int
        """
        return self._time_remaining

    @time_remaining.setter
    def time_remaining(self, time_remaining):
        """Sets the time_remaining of this PrintSessionRequest.


        :param time_remaining: The time_remaining of this PrintSessionRequest.  # noqa: E501
        :type time_remaining: int
        """
        if (self.local_vars_configuration.client_side_validation and
                time_remaining is not None and time_remaining > 2147483647):  # noqa: E501
            raise ValueError("Invalid value for `time_remaining`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                time_remaining is not None and time_remaining < -2147483648):  # noqa: E501
            raise ValueError("Invalid value for `time_remaining`, must be a value greater than or equal to `-2147483648`")  # noqa: E501

        self._time_remaining = time_remaining

    @property
    def printer_profile(self):
        """Gets the printer_profile of this PrintSessionRequest.  # noqa: E501


        :return: The printer_profile of this PrintSessionRequest.  # noqa: E501
        :rtype: int
        """
        return self._printer_profile

    @printer_profile.setter
    def printer_profile(self, printer_profile):
        """Sets the printer_profile of this PrintSessionRequest.


        :param printer_profile: The printer_profile of this PrintSessionRequest.  # noqa: E501
        :type printer_profile: int
        """

        self._printer_profile = printer_profile

    @property
    def gcode_file(self):
        """Gets the gcode_file of this PrintSessionRequest.  # noqa: E501


        :return: The gcode_file of this PrintSessionRequest.  # noqa: E501
        :rtype: int
        """
        return self._gcode_file

    @gcode_file.setter
    def gcode_file(self, gcode_file):
        """Sets the gcode_file of this PrintSessionRequest.


        :param gcode_file: The gcode_file of this PrintSessionRequest.  # noqa: E501
        :type gcode_file: int
        """

        self._gcode_file = gcode_file

    @property
    def gcode_filename(self):
        """Gets the gcode_filename of this PrintSessionRequest.  # noqa: E501


        :return: The gcode_filename of this PrintSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._gcode_filename

    @gcode_filename.setter
    def gcode_filename(self, gcode_filename):
        """Sets the gcode_filename of this PrintSessionRequest.


        :param gcode_filename: The gcode_filename of this PrintSessionRequest.  # noqa: E501
        :type gcode_filename: str
        """
        if (self.local_vars_configuration.client_side_validation and
                gcode_filename is not None and len(gcode_filename) > 255):
            raise ValueError("Invalid value for `gcode_filename`, length must be less than or equal to `255`")  # noqa: E501

        self._gcode_filename = gcode_filename

    @property
    def octoprint_job(self):
        """Gets the octoprint_job of this PrintSessionRequest.  # noqa: E501


        :return: The octoprint_job of this PrintSessionRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._octoprint_job

    @octoprint_job.setter
    def octoprint_job(self, octoprint_job):
        """Sets the octoprint_job of this PrintSessionRequest.


        :param octoprint_job: The octoprint_job of this PrintSessionRequest.  # noqa: E501
        :type octoprint_job: dict(str, object)
        """

        self._octoprint_job = octoprint_job

    @property
    def print_job_status(self):
        """Gets the print_job_status of this PrintSessionRequest.  # noqa: E501


        :return: The print_job_status of this PrintSessionRequest.  # noqa: E501
        :rtype: PrintJobStatusEnum
        """
        return self._print_job_status

    @print_job_status.setter
    def print_job_status(self, print_job_status):
        """Sets the print_job_status of this PrintSessionRequest.


        :param print_job_status: The print_job_status of this PrintSessionRequest.  # noqa: E501
        :type print_job_status: PrintJobStatusEnum
        """

        self._print_job_status = print_job_status

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
        if not isinstance(other, PrintSessionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrintSessionRequest):
            return True

        return self.to_dict() != other.to_dict()
