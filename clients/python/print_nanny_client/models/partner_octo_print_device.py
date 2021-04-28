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


class PartnerOctoPrintDevice(object):
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
        'name': 'str',
        'model': 'str',
        'platform': 'str',
        'octoprint_version': 'str',
        'plugin_version': 'str',
        'print_nanny_client_version': 'str',
        'verified': 'str'
    }

    attribute_map = {
        'name': 'name',
        'model': 'model',
        'platform': 'platform',
        'octoprint_version': 'octoprint_version',
        'plugin_version': 'plugin_version',
        'print_nanny_client_version': 'print_nanny_client_version',
        'verified': 'verified'
    }

    def __init__(self, name=None, model=None, platform=None, octoprint_version=None, plugin_version=None, print_nanny_client_version=None, verified=None, local_vars_configuration=None):  # noqa: E501
        """PartnerOctoPrintDevice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._model = None
        self._platform = None
        self._octoprint_version = None
        self._plugin_version = None
        self._print_nanny_client_version = None
        self._verified = None
        self.discriminator = None

        self.name = name
        self.model = model
        self.platform = platform
        self.octoprint_version = octoprint_version
        self.plugin_version = plugin_version
        self.print_nanny_client_version = print_nanny_client_version
        if verified is not None:
            self.verified = verified

    @property
    def name(self):
        """Gets the name of this PartnerOctoPrintDevice.  # noqa: E501


        :return: The name of this PartnerOctoPrintDevice.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PartnerOctoPrintDevice.


        :param name: The name of this PartnerOctoPrintDevice.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

    @property
    def model(self):
        """Gets the model of this PartnerOctoPrintDevice.  # noqa: E501


        :return: The model of this PartnerOctoPrintDevice.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PartnerOctoPrintDevice.


        :param model: The model of this PartnerOctoPrintDevice.  # noqa: E501
        :type model: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                model is not None and len(model) > 255):
            raise ValueError("Invalid value for `model`, length must be less than or equal to `255`")  # noqa: E501

        self._model = model

    @property
    def platform(self):
        """Gets the platform of this PartnerOctoPrintDevice.  # noqa: E501


        :return: The platform of this PartnerOctoPrintDevice.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this PartnerOctoPrintDevice.


        :param platform: The platform of this PartnerOctoPrintDevice.  # noqa: E501
        :type platform: str
        """
        if self.local_vars_configuration.client_side_validation and platform is None:  # noqa: E501
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                platform is not None and len(platform) > 255):
            raise ValueError("Invalid value for `platform`, length must be less than or equal to `255`")  # noqa: E501

        self._platform = platform

    @property
    def octoprint_version(self):
        """Gets the octoprint_version of this PartnerOctoPrintDevice.  # noqa: E501


        :return: The octoprint_version of this PartnerOctoPrintDevice.  # noqa: E501
        :rtype: str
        """
        return self._octoprint_version

    @octoprint_version.setter
    def octoprint_version(self, octoprint_version):
        """Sets the octoprint_version of this PartnerOctoPrintDevice.


        :param octoprint_version: The octoprint_version of this PartnerOctoPrintDevice.  # noqa: E501
        :type octoprint_version: str
        """
        if self.local_vars_configuration.client_side_validation and octoprint_version is None:  # noqa: E501
            raise ValueError("Invalid value for `octoprint_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                octoprint_version is not None and len(octoprint_version) > 255):
            raise ValueError("Invalid value for `octoprint_version`, length must be less than or equal to `255`")  # noqa: E501

        self._octoprint_version = octoprint_version

    @property
    def plugin_version(self):
        """Gets the plugin_version of this PartnerOctoPrintDevice.  # noqa: E501


        :return: The plugin_version of this PartnerOctoPrintDevice.  # noqa: E501
        :rtype: str
        """
        return self._plugin_version

    @plugin_version.setter
    def plugin_version(self, plugin_version):
        """Sets the plugin_version of this PartnerOctoPrintDevice.


        :param plugin_version: The plugin_version of this PartnerOctoPrintDevice.  # noqa: E501
        :type plugin_version: str
        """
        if self.local_vars_configuration.client_side_validation and plugin_version is None:  # noqa: E501
            raise ValueError("Invalid value for `plugin_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                plugin_version is not None and len(plugin_version) > 255):
            raise ValueError("Invalid value for `plugin_version`, length must be less than or equal to `255`")  # noqa: E501

        self._plugin_version = plugin_version

    @property
    def print_nanny_client_version(self):
        """Gets the print_nanny_client_version of this PartnerOctoPrintDevice.  # noqa: E501


        :return: The print_nanny_client_version of this PartnerOctoPrintDevice.  # noqa: E501
        :rtype: str
        """
        return self._print_nanny_client_version

    @print_nanny_client_version.setter
    def print_nanny_client_version(self, print_nanny_client_version):
        """Sets the print_nanny_client_version of this PartnerOctoPrintDevice.


        :param print_nanny_client_version: The print_nanny_client_version of this PartnerOctoPrintDevice.  # noqa: E501
        :type print_nanny_client_version: str
        """
        if self.local_vars_configuration.client_side_validation and print_nanny_client_version is None:  # noqa: E501
            raise ValueError("Invalid value for `print_nanny_client_version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                print_nanny_client_version is not None and len(print_nanny_client_version) > 255):
            raise ValueError("Invalid value for `print_nanny_client_version`, length must be less than or equal to `255`")  # noqa: E501

        self._print_nanny_client_version = print_nanny_client_version

    @property
    def verified(self):
        """Gets the verified of this PartnerOctoPrintDevice.  # noqa: E501


        :return: The verified of this PartnerOctoPrintDevice.  # noqa: E501
        :rtype: str
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this PartnerOctoPrintDevice.


        :param verified: The verified of this PartnerOctoPrintDevice.  # noqa: E501
        :type verified: str
        """

        self._verified = verified

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
        if not isinstance(other, PartnerOctoPrintDevice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartnerOctoPrintDevice):
            return True

        return self.to_dict() != other.to_dict()
