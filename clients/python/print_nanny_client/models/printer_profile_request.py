# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint  # noqa: F401
import re  # noqa: F401

import six  # noqa: F401

from print_nanny_client.exceptions import ApiValueError  # noqa: F401
from print_nanny_client.model_utils import (  # noqa: F401
    ModelNormal,
    ModelSimple,
    check_allowed_values,
    check_validations
)


class PrinterProfileRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      openapi_types (dict): The key is attribute name
          and the value is attribute type.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
    """

    allowed_values = {
    }

    attribute_map = {
        'axes_e_inverted': 'axes_e_inverted',  # noqa: E501
        'axes_e_speed': 'axes_e_speed',  # noqa: E501
        'axes_x_speed': 'axes_x_speed',  # noqa: E501
        'axes_x_inverted': 'axes_x_inverted',  # noqa: E501
        'axes_y_inverted': 'axes_y_inverted',  # noqa: E501
        'axes_y_speed': 'axes_y_speed',  # noqa: E501
        'axes_z_inverted': 'axes_z_inverted',  # noqa: E501
        'axes_z_speed': 'axes_z_speed',  # noqa: E501
        'extruder_count': 'extruder_count',  # noqa: E501
        'extruder_nozzle_diameter': 'extruder_nozzle_diameter',  # noqa: E501
        'extruder_shared_nozzle': 'extruder_shared_nozzle',  # noqa: E501
        'heated_bed': 'heated_bed',  # noqa: E501
        'heated_chamber': 'heated_chamber',  # noqa: E501
        'model': 'model',  # noqa: E501
        'name': 'name',  # noqa: E501
        'volume_custom_box': 'volume_custom_box',  # noqa: E501
        'volume_depth': 'volume_depth',  # noqa: E501
        'volume_formfactor': 'volume_formfactor',  # noqa: E501
        'volume_height': 'volume_height',  # noqa: E501
        'volume_origin': 'volume_origin',  # noqa: E501
        'volume_width': 'volume_width'  # noqa: E501
    }

    openapi_types = {
        'axes_e_inverted': 'bool',
        'axes_e_speed': 'int',
        'axes_x_speed': 'int',
        'axes_x_inverted': 'bool',
        'axes_y_inverted': 'bool',
        'axes_y_speed': 'int',
        'axes_z_inverted': 'bool',
        'axes_z_speed': 'int',
        'extruder_count': 'int',
        'extruder_nozzle_diameter': 'float',
        'extruder_shared_nozzle': 'bool',
        'heated_bed': 'bool',
        'heated_chamber': 'bool',
        'model': 'str',
        'name': 'str',
        'volume_custom_box': 'bool',
        'volume_depth': 'float',
        'volume_formfactor': 'str',
        'volume_height': 'float',
        'volume_origin': 'str',
        'volume_width': 'float'
    }

    validations = {
        ('axes_e_speed',): {

            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('axes_x_speed',): {

            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('axes_y_speed',): {

            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('axes_z_speed',): {

            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('extruder_count',): {

            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
        ('model',): {
            'max_length': 255,
        },
        ('name',): {
            'max_length': 255,
        },
        ('volume_formfactor',): {
            'max_length': 255,
        },
        ('volume_origin',): {
            'max_length': 255,
        },
    }

    def __init__(self, axes_e_inverted=None, axes_e_speed=None, axes_x_speed=None, axes_x_inverted=None, axes_y_inverted=None, axes_y_speed=None, axes_z_inverted=None, axes_z_speed=None, extruder_count=None, extruder_nozzle_diameter=None, extruder_shared_nozzle=None, heated_bed=None, heated_chamber=None, model=None, name=None, volume_custom_box=None, volume_depth=None, volume_formfactor=None, volume_height=None, volume_origin=None, volume_width=None):  # noqa: E501
        """PrinterProfileRequest - a model defined in OpenAPI"""  # noqa: E501

        self._axes_e_inverted = None
        self._axes_e_speed = None
        self._axes_x_speed = None
        self._axes_x_inverted = None
        self._axes_y_inverted = None
        self._axes_y_speed = None
        self._axes_z_inverted = None
        self._axes_z_speed = None
        self._extruder_count = None
        self._extruder_nozzle_diameter = None
        self._extruder_shared_nozzle = None
        self._heated_bed = None
        self._heated_chamber = None
        self._model = None
        self._name = None
        self._volume_custom_box = None
        self._volume_depth = None
        self._volume_formfactor = None
        self._volume_height = None
        self._volume_origin = None
        self._volume_width = None
        self.discriminator = None

        self.axes_e_inverted = axes_e_inverted
        self.axes_e_speed = axes_e_speed
        self.axes_x_speed = axes_x_speed
        self.axes_x_inverted = axes_x_inverted
        self.axes_y_inverted = axes_y_inverted
        self.axes_y_speed = axes_y_speed
        self.axes_z_inverted = axes_z_inverted
        self.axes_z_speed = axes_z_speed
        self.extruder_count = extruder_count
        self.extruder_nozzle_diameter = extruder_nozzle_diameter
        self.extruder_shared_nozzle = extruder_shared_nozzle
        self.heated_bed = heated_bed
        self.heated_chamber = heated_chamber
        self.model = model
        self.name = name
        self.volume_custom_box = volume_custom_box
        self.volume_depth = volume_depth
        self.volume_formfactor = volume_formfactor
        self.volume_height = volume_height
        self.volume_origin = volume_origin
        self.volume_width = volume_width

    @property
    def axes_e_inverted(self):
        """Gets the axes_e_inverted of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_e_inverted of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._axes_e_inverted

    @axes_e_inverted.setter
    def axes_e_inverted(self, axes_e_inverted):  # noqa: E501
        """Sets the axes_e_inverted of this PrinterProfileRequest.


        :param axes_e_inverted: The axes_e_inverted of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if axes_e_inverted is None:
            raise ApiValueError("Invalid value for `axes_e_inverted`, must not be `None`")  # noqa: E501

        self._axes_e_inverted = (
            axes_e_inverted
        )

    @property
    def axes_e_speed(self):
        """Gets the axes_e_speed of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_e_speed of this PrinterProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._axes_e_speed

    @axes_e_speed.setter
    def axes_e_speed(self, axes_e_speed):  # noqa: E501
        """Sets the axes_e_speed of this PrinterProfileRequest.


        :param axes_e_speed: The axes_e_speed of this PrinterProfileRequest.  # noqa: E501
        :type: int
        """
        if axes_e_speed is None:
            raise ApiValueError("Invalid value for `axes_e_speed`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('axes_e_speed',),
            axes_e_speed
        )

        self._axes_e_speed = (
            axes_e_speed
        )

    @property
    def axes_x_speed(self):
        """Gets the axes_x_speed of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_x_speed of this PrinterProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._axes_x_speed

    @axes_x_speed.setter
    def axes_x_speed(self, axes_x_speed):  # noqa: E501
        """Sets the axes_x_speed of this PrinterProfileRequest.


        :param axes_x_speed: The axes_x_speed of this PrinterProfileRequest.  # noqa: E501
        :type: int
        """
        if axes_x_speed is None:
            raise ApiValueError("Invalid value for `axes_x_speed`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('axes_x_speed',),
            axes_x_speed
        )

        self._axes_x_speed = (
            axes_x_speed
        )

    @property
    def axes_x_inverted(self):
        """Gets the axes_x_inverted of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_x_inverted of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._axes_x_inverted

    @axes_x_inverted.setter
    def axes_x_inverted(self, axes_x_inverted):  # noqa: E501
        """Sets the axes_x_inverted of this PrinterProfileRequest.


        :param axes_x_inverted: The axes_x_inverted of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if axes_x_inverted is None:
            raise ApiValueError("Invalid value for `axes_x_inverted`, must not be `None`")  # noqa: E501

        self._axes_x_inverted = (
            axes_x_inverted
        )

    @property
    def axes_y_inverted(self):
        """Gets the axes_y_inverted of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_y_inverted of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._axes_y_inverted

    @axes_y_inverted.setter
    def axes_y_inverted(self, axes_y_inverted):  # noqa: E501
        """Sets the axes_y_inverted of this PrinterProfileRequest.


        :param axes_y_inverted: The axes_y_inverted of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if axes_y_inverted is None:
            raise ApiValueError("Invalid value for `axes_y_inverted`, must not be `None`")  # noqa: E501

        self._axes_y_inverted = (
            axes_y_inverted
        )

    @property
    def axes_y_speed(self):
        """Gets the axes_y_speed of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_y_speed of this PrinterProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._axes_y_speed

    @axes_y_speed.setter
    def axes_y_speed(self, axes_y_speed):  # noqa: E501
        """Sets the axes_y_speed of this PrinterProfileRequest.


        :param axes_y_speed: The axes_y_speed of this PrinterProfileRequest.  # noqa: E501
        :type: int
        """
        if axes_y_speed is None:
            raise ApiValueError("Invalid value for `axes_y_speed`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('axes_y_speed',),
            axes_y_speed
        )

        self._axes_y_speed = (
            axes_y_speed
        )

    @property
    def axes_z_inverted(self):
        """Gets the axes_z_inverted of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_z_inverted of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._axes_z_inverted

    @axes_z_inverted.setter
    def axes_z_inverted(self, axes_z_inverted):  # noqa: E501
        """Sets the axes_z_inverted of this PrinterProfileRequest.


        :param axes_z_inverted: The axes_z_inverted of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if axes_z_inverted is None:
            raise ApiValueError("Invalid value for `axes_z_inverted`, must not be `None`")  # noqa: E501

        self._axes_z_inverted = (
            axes_z_inverted
        )

    @property
    def axes_z_speed(self):
        """Gets the axes_z_speed of this PrinterProfileRequest.  # noqa: E501


        :return: The axes_z_speed of this PrinterProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._axes_z_speed

    @axes_z_speed.setter
    def axes_z_speed(self, axes_z_speed):  # noqa: E501
        """Sets the axes_z_speed of this PrinterProfileRequest.


        :param axes_z_speed: The axes_z_speed of this PrinterProfileRequest.  # noqa: E501
        :type: int
        """
        if axes_z_speed is None:
            raise ApiValueError("Invalid value for `axes_z_speed`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('axes_z_speed',),
            axes_z_speed
        )

        self._axes_z_speed = (
            axes_z_speed
        )

    @property
    def extruder_count(self):
        """Gets the extruder_count of this PrinterProfileRequest.  # noqa: E501


        :return: The extruder_count of this PrinterProfileRequest.  # noqa: E501
        :rtype: int
        """
        return self._extruder_count

    @extruder_count.setter
    def extruder_count(self, extruder_count):  # noqa: E501
        """Sets the extruder_count of this PrinterProfileRequest.


        :param extruder_count: The extruder_count of this PrinterProfileRequest.  # noqa: E501
        :type: int
        """
        if extruder_count is None:
            raise ApiValueError("Invalid value for `extruder_count`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('extruder_count',),
            extruder_count
        )

        self._extruder_count = (
            extruder_count
        )

    @property
    def extruder_nozzle_diameter(self):
        """Gets the extruder_nozzle_diameter of this PrinterProfileRequest.  # noqa: E501


        :return: The extruder_nozzle_diameter of this PrinterProfileRequest.  # noqa: E501
        :rtype: float
        """
        return self._extruder_nozzle_diameter

    @extruder_nozzle_diameter.setter
    def extruder_nozzle_diameter(self, extruder_nozzle_diameter):  # noqa: E501
        """Sets the extruder_nozzle_diameter of this PrinterProfileRequest.


        :param extruder_nozzle_diameter: The extruder_nozzle_diameter of this PrinterProfileRequest.  # noqa: E501
        :type: float
        """
        if extruder_nozzle_diameter is None:
            raise ApiValueError("Invalid value for `extruder_nozzle_diameter`, must not be `None`")  # noqa: E501

        self._extruder_nozzle_diameter = (
            extruder_nozzle_diameter
        )

    @property
    def extruder_shared_nozzle(self):
        """Gets the extruder_shared_nozzle of this PrinterProfileRequest.  # noqa: E501


        :return: The extruder_shared_nozzle of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._extruder_shared_nozzle

    @extruder_shared_nozzle.setter
    def extruder_shared_nozzle(self, extruder_shared_nozzle):  # noqa: E501
        """Sets the extruder_shared_nozzle of this PrinterProfileRequest.


        :param extruder_shared_nozzle: The extruder_shared_nozzle of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if extruder_shared_nozzle is None:
            raise ApiValueError("Invalid value for `extruder_shared_nozzle`, must not be `None`")  # noqa: E501

        self._extruder_shared_nozzle = (
            extruder_shared_nozzle
        )

    @property
    def heated_bed(self):
        """Gets the heated_bed of this PrinterProfileRequest.  # noqa: E501


        :return: The heated_bed of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._heated_bed

    @heated_bed.setter
    def heated_bed(self, heated_bed):  # noqa: E501
        """Sets the heated_bed of this PrinterProfileRequest.


        :param heated_bed: The heated_bed of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if heated_bed is None:
            raise ApiValueError("Invalid value for `heated_bed`, must not be `None`")  # noqa: E501

        self._heated_bed = (
            heated_bed
        )

    @property
    def heated_chamber(self):
        """Gets the heated_chamber of this PrinterProfileRequest.  # noqa: E501


        :return: The heated_chamber of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._heated_chamber

    @heated_chamber.setter
    def heated_chamber(self, heated_chamber):  # noqa: E501
        """Sets the heated_chamber of this PrinterProfileRequest.


        :param heated_chamber: The heated_chamber of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if heated_chamber is None:
            raise ApiValueError("Invalid value for `heated_chamber`, must not be `None`")  # noqa: E501

        self._heated_chamber = (
            heated_chamber
        )

    @property
    def model(self):
        """Gets the model of this PrinterProfileRequest.  # noqa: E501


        :return: The model of this PrinterProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):  # noqa: E501
        """Sets the model of this PrinterProfileRequest.


        :param model: The model of this PrinterProfileRequest.  # noqa: E501
        :type: str
        """
        check_validations(
            self.validations,
            ('model',),
            model
        )

        self._model = (
            model
        )

    @property
    def name(self):
        """Gets the name of this PrinterProfileRequest.  # noqa: E501


        :return: The name of this PrinterProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):  # noqa: E501
        """Sets the name of this PrinterProfileRequest.


        :param name: The name of this PrinterProfileRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ApiValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('name',),
            name
        )

        self._name = (
            name
        )

    @property
    def volume_custom_box(self):
        """Gets the volume_custom_box of this PrinterProfileRequest.  # noqa: E501


        :return: The volume_custom_box of this PrinterProfileRequest.  # noqa: E501
        :rtype: bool
        """
        return self._volume_custom_box

    @volume_custom_box.setter
    def volume_custom_box(self, volume_custom_box):  # noqa: E501
        """Sets the volume_custom_box of this PrinterProfileRequest.


        :param volume_custom_box: The volume_custom_box of this PrinterProfileRequest.  # noqa: E501
        :type: bool
        """
        if volume_custom_box is None:
            raise ApiValueError("Invalid value for `volume_custom_box`, must not be `None`")  # noqa: E501

        self._volume_custom_box = (
            volume_custom_box
        )

    @property
    def volume_depth(self):
        """Gets the volume_depth of this PrinterProfileRequest.  # noqa: E501


        :return: The volume_depth of this PrinterProfileRequest.  # noqa: E501
        :rtype: float
        """
        return self._volume_depth

    @volume_depth.setter
    def volume_depth(self, volume_depth):  # noqa: E501
        """Sets the volume_depth of this PrinterProfileRequest.


        :param volume_depth: The volume_depth of this PrinterProfileRequest.  # noqa: E501
        :type: float
        """
        if volume_depth is None:
            raise ApiValueError("Invalid value for `volume_depth`, must not be `None`")  # noqa: E501

        self._volume_depth = (
            volume_depth
        )

    @property
    def volume_formfactor(self):
        """Gets the volume_formfactor of this PrinterProfileRequest.  # noqa: E501


        :return: The volume_formfactor of this PrinterProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_formfactor

    @volume_formfactor.setter
    def volume_formfactor(self, volume_formfactor):  # noqa: E501
        """Sets the volume_formfactor of this PrinterProfileRequest.


        :param volume_formfactor: The volume_formfactor of this PrinterProfileRequest.  # noqa: E501
        :type: str
        """
        if volume_formfactor is None:
            raise ApiValueError("Invalid value for `volume_formfactor`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('volume_formfactor',),
            volume_formfactor
        )

        self._volume_formfactor = (
            volume_formfactor
        )

    @property
    def volume_height(self):
        """Gets the volume_height of this PrinterProfileRequest.  # noqa: E501


        :return: The volume_height of this PrinterProfileRequest.  # noqa: E501
        :rtype: float
        """
        return self._volume_height

    @volume_height.setter
    def volume_height(self, volume_height):  # noqa: E501
        """Sets the volume_height of this PrinterProfileRequest.


        :param volume_height: The volume_height of this PrinterProfileRequest.  # noqa: E501
        :type: float
        """
        if volume_height is None:
            raise ApiValueError("Invalid value for `volume_height`, must not be `None`")  # noqa: E501

        self._volume_height = (
            volume_height
        )

    @property
    def volume_origin(self):
        """Gets the volume_origin of this PrinterProfileRequest.  # noqa: E501


        :return: The volume_origin of this PrinterProfileRequest.  # noqa: E501
        :rtype: str
        """
        return self._volume_origin

    @volume_origin.setter
    def volume_origin(self, volume_origin):  # noqa: E501
        """Sets the volume_origin of this PrinterProfileRequest.


        :param volume_origin: The volume_origin of this PrinterProfileRequest.  # noqa: E501
        :type: str
        """
        if volume_origin is None:
            raise ApiValueError("Invalid value for `volume_origin`, must not be `None`")  # noqa: E501
        check_validations(
            self.validations,
            ('volume_origin',),
            volume_origin
        )

        self._volume_origin = (
            volume_origin
        )

    @property
    def volume_width(self):
        """Gets the volume_width of this PrinterProfileRequest.  # noqa: E501


        :return: The volume_width of this PrinterProfileRequest.  # noqa: E501
        :rtype: float
        """
        return self._volume_width

    @volume_width.setter
    def volume_width(self, volume_width):  # noqa: E501
        """Sets the volume_width of this PrinterProfileRequest.


        :param volume_width: The volume_width of this PrinterProfileRequest.  # noqa: E501
        :type: float
        """
        if volume_width is None:
            raise ApiValueError("Invalid value for `volume_width`, must not be `None`")  # noqa: E501

        self._volume_width = (
            volume_width
        )

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PrinterProfileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other