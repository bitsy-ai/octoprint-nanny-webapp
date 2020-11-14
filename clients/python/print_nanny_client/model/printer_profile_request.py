# coding: utf-8

"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from print_nanny_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
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
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
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
        ('volume_form_factor',): {
            'max_length': 255,
        },
        ('volume_origin',): {
            'max_length': 255,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'axes_e_inverted': (bool,),  # noqa: E501
            'axes_e_speed': (int,),  # noqa: E501
            'axes_x_speed': (int,),  # noqa: E501
            'axes_y_inverted': (bool,),  # noqa: E501
            'axes_y_speed': (int,),  # noqa: E501
            'axes_z_inverted': (bool,),  # noqa: E501
            'axes_z_speed': (int,),  # noqa: E501
            'extruder_count': (int,),  # noqa: E501
            'extruder_nozzle_diameter': (float,),  # noqa: E501
            'extruder_offsets': ([float],),  # noqa: E501
            'extruder_shared_nozzle': (bool,),  # noqa: E501
            'heated_bed': (bool,),  # noqa: E501
            'heated_chamber': (bool,),  # noqa: E501
            'model': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'volume_custom_box': (bool,),  # noqa: E501
            'volume_depth': (float,),  # noqa: E501
            'volume_form_factor': (str,),  # noqa: E501
            'volume_height': (float,),  # noqa: E501
            'volume_origin': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'axes_e_inverted': 'axes_e_inverted',  # noqa: E501
        'axes_e_speed': 'axes_e_speed',  # noqa: E501
        'axes_x_speed': 'axes_x_speed',  # noqa: E501
        'axes_y_inverted': 'axes_y_inverted',  # noqa: E501
        'axes_y_speed': 'axes_y_speed',  # noqa: E501
        'axes_z_inverted': 'axes_z_inverted',  # noqa: E501
        'axes_z_speed': 'axes_z_speed',  # noqa: E501
        'extruder_count': 'extruder_count',  # noqa: E501
        'extruder_nozzle_diameter': 'extruder_nozzleDiameter',  # noqa: E501
        'extruder_offsets': 'extruder_offsets',  # noqa: E501
        'extruder_shared_nozzle': 'extruder_sharedNozzle',  # noqa: E501
        'heated_bed': 'heatedBed',  # noqa: E501
        'heated_chamber': 'heatedChamber',  # noqa: E501
        'model': 'model',  # noqa: E501
        'name': 'name',  # noqa: E501
        'volume_custom_box': 'volume_customBox',  # noqa: E501
        'volume_depth': 'volume_depth',  # noqa: E501
        'volume_form_factor': 'volume_formFactor',  # noqa: E501
        'volume_height': 'volume_height',  # noqa: E501
        'volume_origin': 'volume_origin',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, axes_e_inverted, axes_e_speed, axes_x_speed, axes_y_inverted, axes_y_speed, axes_z_inverted, axes_z_speed, extruder_count, extruder_nozzle_diameter, extruder_offsets, extruder_shared_nozzle, heated_bed, heated_chamber, model, name, volume_custom_box, volume_depth, volume_form_factor, volume_height, volume_origin, *args, **kwargs):  # noqa: E501
        """PrinterProfileRequest - a model defined in OpenAPI

        Args:
            axes_e_inverted (bool):
            axes_e_speed (int):
            axes_x_speed (int):
            axes_y_inverted (bool):
            axes_y_speed (int):
            axes_z_inverted (bool):
            axes_z_speed (int):
            extruder_count (int):
            extruder_nozzle_diameter (float):
            extruder_offsets ([float]):
            extruder_shared_nozzle (bool):
            heated_bed (bool):
            heated_chamber (bool):
            model (str):
            name (str):
            volume_custom_box (bool):
            volume_depth (float):
            volume_form_factor (str):
            volume_height (float):
            volume_origin (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.axes_e_inverted = axes_e_inverted
        self.axes_e_speed = axes_e_speed
        self.axes_x_speed = axes_x_speed
        self.axes_y_inverted = axes_y_inverted
        self.axes_y_speed = axes_y_speed
        self.axes_z_inverted = axes_z_inverted
        self.axes_z_speed = axes_z_speed
        self.extruder_count = extruder_count
        self.extruder_nozzle_diameter = extruder_nozzle_diameter
        self.extruder_offsets = extruder_offsets
        self.extruder_shared_nozzle = extruder_shared_nozzle
        self.heated_bed = heated_bed
        self.heated_chamber = heated_chamber
        self.model = model
        self.name = name
        self.volume_custom_box = volume_custom_box
        self.volume_depth = volume_depth
        self.volume_form_factor = volume_form_factor
        self.volume_height = volume_height
        self.volume_origin = volume_origin
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
