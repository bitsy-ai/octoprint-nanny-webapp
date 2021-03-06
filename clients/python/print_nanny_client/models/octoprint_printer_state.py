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


class OctoprintPrinterState(object):
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
        'text': 'str',
        'flags': 'OctoprintPrinterFlags'
    }

    attribute_map = {
        'text': 'text',
        'flags': 'flags'
    }

    def __init__(self, text=None, flags=None, local_vars_configuration=None):  # noqa: E501
        """OctoprintPrinterState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._text = None
        self._flags = None
        self.discriminator = None

        self.text = text
        self.flags = flags

    @property
    def text(self):
        """Gets the text of this OctoprintPrinterState.  # noqa: E501


        :return: The text of this OctoprintPrinterState.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this OctoprintPrinterState.


        :param text: The text of this OctoprintPrinterState.  # noqa: E501
        :type text: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def flags(self):
        """Gets the flags of this OctoprintPrinterState.  # noqa: E501


        :return: The flags of this OctoprintPrinterState.  # noqa: E501
        :rtype: OctoprintPrinterFlags
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this OctoprintPrinterState.


        :param flags: The flags of this OctoprintPrinterState.  # noqa: E501
        :type flags: OctoprintPrinterFlags
        """
        if self.local_vars_configuration.client_side_validation and flags is None:  # noqa: E501
            raise ValueError("Invalid value for `flags`, must not be `None`")  # noqa: E501

        self._flags = flags

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
        if not isinstance(other, OctoprintPrinterState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OctoprintPrinterState):
            return True

        return self.to_dict() != other.to_dict()
