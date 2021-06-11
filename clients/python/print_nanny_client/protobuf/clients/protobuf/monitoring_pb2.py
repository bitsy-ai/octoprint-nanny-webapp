# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clients/protobuf/monitoring.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='clients/protobuf/monitoring.proto',
  package='print_nanny_client.monitoring',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!clients/protobuf/monitoring.proto\x12\x1dprint_nanny_client.monitoring\"\x8c\x01\n\x12VideoRenderRequest\x12\x15\n\rprint_session\x18\x01 \x01(\t\x12\x18\n\x10print_session_id\x18\x02 \x01(\x05\x12\x0f\n\x07user_id\x18\x03 \x01(\x05\x12\x14\n\x0coctoprint_id\x18\x04 \x01(\x05\x12\x1e\n\x16\x63loudiot_device_num_id\x18\x05 \x01(\x05\x62\x06proto3')
)




_VIDEORENDERREQUEST = _descriptor.Descriptor(
  name='VideoRenderRequest',
  full_name='print_nanny_client.monitoring.VideoRenderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='print_session', full_name='print_nanny_client.monitoring.VideoRenderRequest.print_session', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='print_session_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.print_session_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.user_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='octoprint_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.octoprint_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cloudiot_device_num_id', full_name='print_nanny_client.monitoring.VideoRenderRequest.cloudiot_device_num_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=69,
  serialized_end=209,
)

DESCRIPTOR.message_types_by_name['VideoRenderRequest'] = _VIDEORENDERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoRenderRequest = _reflection.GeneratedProtocolMessageType('VideoRenderRequest', (_message.Message,), dict(
  DESCRIPTOR = _VIDEORENDERREQUEST,
  __module__ = 'clients.protobuf.monitoring_pb2'
  # @@protoc_insertion_point(class_scope:print_nanny_client.monitoring.VideoRenderRequest)
  ))
_sym_db.RegisterMessage(VideoRenderRequest)


# @@protoc_insertion_point(module_scope)
