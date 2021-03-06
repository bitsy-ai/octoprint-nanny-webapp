# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: monitoring.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2

from .common_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='monitoring.proto',
  package='print_nanny.monitoring',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10monitoring.proto\x12\x16print_nanny.monitoring\x1a\x0c\x63ommon.proto\"n\n\x0fMonitoringImage\x12.\n\x08metadata\x18\x01 \x01(\x0b\x32\x1c.print_nanny.common.Metadata\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\"0\n\x03\x42ox\x12\n\n\x02xy\x18\x01 \x03(\x02\x12\x0e\n\x06height\x18\x02 \x01(\x05\x12\r\n\x05width\x18\x03 \x01(\x05\"i\n\x11\x44\x65viceCalibration\x12(\n\x03\x62ox\x18\x01 \x01(\x0b\x32\x1b.print_nanny.monitoring.Box\x12\x0b\n\x03\x66ps\x18\x02 \x01(\x02\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\r\n\x05width\x18\x04 \x01(\x05\"\xab\x01\n\x0e\x42oxAnnotations\x12\x16\n\x0enum_detections\x18\x02 \x01(\x05\x12\x18\n\x10\x64\x65tection_scores\x18\x03 \x03(\x02\x12\x19\n\x11\x64\x65tection_classes\x18\x04 \x03(\x05\x12\x34\n\x0f\x64\x65tection_boxes\x18\x05 \x03(\x0b\x32\x1b.print_nanny.monitoring.Box\x12\x16\n\x0ehealth_weights\x18\x06 \x03(\x02\"\xfc\x02\n\x18\x41nnotatedMonitoringImage\x12\x41\n\x10monitoring_image\x18\x01 \x01(\x0b\x32\'.print_nanny.monitoring.MonitoringImage\x12?\n\x0f\x61nnotations_all\x18\x02 \x01(\x0b\x32&.print_nanny.monitoring.BoxAnnotations\x12\x44\n\x14\x61nnotations_filtered\x18\x03 \x01(\x0b\x32&.print_nanny.monitoring.BoxAnnotations\x12\x17\n\x0fscore_threshold\x18\x04 \x01(\x02\x12$\n\x1cmin_calibration_area_overlap\x18\x05 \x01(\x02\x12>\n\x0b\x63\x61libration\x18\x06 \x01(\x0b\x32).print_nanny.monitoring.DeviceCalibration\x12\x17\n\x0f\x61nnotated_image\x18\x07 \x01(\x0c\"\xaf\x02\n\x1f\x41nnotatedMonitoringImagesWindow\x12J\n\x10\x61nnotated_images\x18\x01 \x03(\x0b\x32\x30.print_nanny.monitoring.AnnotatedMonitoringImage\x12\x14\n\x0cwindow_start\x18\x02 \x01(\x02\x12\x12\n\nwindow_end\x18\x03 \x01(\x02\x12W\n\x0bwindow_type\x18\x04 \x01(\x0e\x32\x42.print_nanny.monitoring.AnnotatedMonitoringImagesWindow.WindowType\"=\n\nWindowType\x12\n\n\x06GLOBAL\x10\x00\x12\t\n\x05\x46IXED\x10\x01\x12\x0b\n\x07SLIDING\x10\x02\x12\x0b\n\x07SESSION\x10\x03P\x00\x62\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,],
  public_dependencies=[common__pb2.DESCRIPTOR,])



_ANNOTATEDMONITORINGIMAGESWINDOW_WINDOWTYPE = _descriptor.EnumDescriptor(
  name='WindowType',
  full_name='print_nanny.monitoring.AnnotatedMonitoringImagesWindow.WindowType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GLOBAL', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIXED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SLIDING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SESSION', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1127,
  serialized_end=1188,
)
_sym_db.RegisterEnumDescriptor(_ANNOTATEDMONITORINGIMAGESWINDOW_WINDOWTYPE)


_MONITORINGIMAGE = _descriptor.Descriptor(
  name='MonitoringImage',
  full_name='print_nanny.monitoring.MonitoringImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='print_nanny.monitoring.MonitoringImage.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='print_nanny.monitoring.MonitoringImage.height', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='print_nanny.monitoring.MonitoringImage.width', index=2,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='print_nanny.monitoring.MonitoringImage.data', index=3,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=168,
)


_BOX = _descriptor.Descriptor(
  name='Box',
  full_name='print_nanny.monitoring.Box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xy', full_name='print_nanny.monitoring.Box.xy', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='print_nanny.monitoring.Box.height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='print_nanny.monitoring.Box.width', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=218,
)


_DEVICECALIBRATION = _descriptor.Descriptor(
  name='DeviceCalibration',
  full_name='print_nanny.monitoring.DeviceCalibration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='box', full_name='print_nanny.monitoring.DeviceCalibration.box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fps', full_name='print_nanny.monitoring.DeviceCalibration.fps', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='print_nanny.monitoring.DeviceCalibration.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='print_nanny.monitoring.DeviceCalibration.width', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=325,
)


_BOXANNOTATIONS = _descriptor.Descriptor(
  name='BoxAnnotations',
  full_name='print_nanny.monitoring.BoxAnnotations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_detections', full_name='print_nanny.monitoring.BoxAnnotations.num_detections', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_scores', full_name='print_nanny.monitoring.BoxAnnotations.detection_scores', index=1,
      number=3, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_classes', full_name='print_nanny.monitoring.BoxAnnotations.detection_classes', index=2,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='detection_boxes', full_name='print_nanny.monitoring.BoxAnnotations.detection_boxes', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='health_weights', full_name='print_nanny.monitoring.BoxAnnotations.health_weights', index=4,
      number=6, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=328,
  serialized_end=499,
)


_ANNOTATEDMONITORINGIMAGE = _descriptor.Descriptor(
  name='AnnotatedMonitoringImage',
  full_name='print_nanny.monitoring.AnnotatedMonitoringImage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='monitoring_image', full_name='print_nanny.monitoring.AnnotatedMonitoringImage.monitoring_image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations_all', full_name='print_nanny.monitoring.AnnotatedMonitoringImage.annotations_all', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotations_filtered', full_name='print_nanny.monitoring.AnnotatedMonitoringImage.annotations_filtered', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score_threshold', full_name='print_nanny.monitoring.AnnotatedMonitoringImage.score_threshold', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_calibration_area_overlap', full_name='print_nanny.monitoring.AnnotatedMonitoringImage.min_calibration_area_overlap', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calibration', full_name='print_nanny.monitoring.AnnotatedMonitoringImage.calibration', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='annotated_image', full_name='print_nanny.monitoring.AnnotatedMonitoringImage.annotated_image', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=502,
  serialized_end=882,
)


_ANNOTATEDMONITORINGIMAGESWINDOW = _descriptor.Descriptor(
  name='AnnotatedMonitoringImagesWindow',
  full_name='print_nanny.monitoring.AnnotatedMonitoringImagesWindow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='annotated_images', full_name='print_nanny.monitoring.AnnotatedMonitoringImagesWindow.annotated_images', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window_start', full_name='print_nanny.monitoring.AnnotatedMonitoringImagesWindow.window_start', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window_end', full_name='print_nanny.monitoring.AnnotatedMonitoringImagesWindow.window_end', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window_type', full_name='print_nanny.monitoring.AnnotatedMonitoringImagesWindow.window_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ANNOTATEDMONITORINGIMAGESWINDOW_WINDOWTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=885,
  serialized_end=1188,
)

_MONITORINGIMAGE.fields_by_name['metadata'].message_type = common__pb2._METADATA
_DEVICECALIBRATION.fields_by_name['box'].message_type = _BOX
_BOXANNOTATIONS.fields_by_name['detection_boxes'].message_type = _BOX
_ANNOTATEDMONITORINGIMAGE.fields_by_name['monitoring_image'].message_type = _MONITORINGIMAGE
_ANNOTATEDMONITORINGIMAGE.fields_by_name['annotations_all'].message_type = _BOXANNOTATIONS
_ANNOTATEDMONITORINGIMAGE.fields_by_name['annotations_filtered'].message_type = _BOXANNOTATIONS
_ANNOTATEDMONITORINGIMAGE.fields_by_name['calibration'].message_type = _DEVICECALIBRATION
_ANNOTATEDMONITORINGIMAGESWINDOW.fields_by_name['annotated_images'].message_type = _ANNOTATEDMONITORINGIMAGE
_ANNOTATEDMONITORINGIMAGESWINDOW.fields_by_name['window_type'].enum_type = _ANNOTATEDMONITORINGIMAGESWINDOW_WINDOWTYPE
_ANNOTATEDMONITORINGIMAGESWINDOW_WINDOWTYPE.containing_type = _ANNOTATEDMONITORINGIMAGESWINDOW
DESCRIPTOR.message_types_by_name['MonitoringImage'] = _MONITORINGIMAGE
DESCRIPTOR.message_types_by_name['Box'] = _BOX
DESCRIPTOR.message_types_by_name['DeviceCalibration'] = _DEVICECALIBRATION
DESCRIPTOR.message_types_by_name['BoxAnnotations'] = _BOXANNOTATIONS
DESCRIPTOR.message_types_by_name['AnnotatedMonitoringImage'] = _ANNOTATEDMONITORINGIMAGE
DESCRIPTOR.message_types_by_name['AnnotatedMonitoringImagesWindow'] = _ANNOTATEDMONITORINGIMAGESWINDOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MonitoringImage = _reflection.GeneratedProtocolMessageType('MonitoringImage', (_message.Message,), dict(
  DESCRIPTOR = _MONITORINGIMAGE,
  __module__ = 'print_nanny_client.protobuf.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny.monitoring.MonitoringImage)
  ))
_sym_db.RegisterMessage(MonitoringImage)

Box = _reflection.GeneratedProtocolMessageType('Box', (_message.Message,), dict(
  DESCRIPTOR = _BOX,
  __module__ = 'print_nanny_client.protobuf.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny.monitoring.Box)
  ))
_sym_db.RegisterMessage(Box)

DeviceCalibration = _reflection.GeneratedProtocolMessageType('DeviceCalibration', (_message.Message,), dict(
  DESCRIPTOR = _DEVICECALIBRATION,
  __module__ = 'print_nanny_client.protobuf.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny.monitoring.DeviceCalibration)
  ))
_sym_db.RegisterMessage(DeviceCalibration)

BoxAnnotations = _reflection.GeneratedProtocolMessageType('BoxAnnotations', (_message.Message,), dict(
  DESCRIPTOR = _BOXANNOTATIONS,
  __module__ = 'print_nanny_client.protobuf.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny.monitoring.BoxAnnotations)
  ))
_sym_db.RegisterMessage(BoxAnnotations)

AnnotatedMonitoringImage = _reflection.GeneratedProtocolMessageType('AnnotatedMonitoringImage', (_message.Message,), dict(
  DESCRIPTOR = _ANNOTATEDMONITORINGIMAGE,
  __module__ = 'print_nanny_client.protobuf.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny.monitoring.AnnotatedMonitoringImage)
  ))
_sym_db.RegisterMessage(AnnotatedMonitoringImage)

AnnotatedMonitoringImagesWindow = _reflection.GeneratedProtocolMessageType('AnnotatedMonitoringImagesWindow', (_message.Message,), dict(
  DESCRIPTOR = _ANNOTATEDMONITORINGIMAGESWINDOW,
  __module__ = 'print_nanny_client.protobuf.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny.monitoring.AnnotatedMonitoringImagesWindow)
  ))
_sym_db.RegisterMessage(AnnotatedMonitoringImagesWindow)


# @@protoc_insertion_point(module_scope)
