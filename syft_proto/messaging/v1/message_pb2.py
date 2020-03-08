# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: syft_proto/messaging/v1/message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from syft_proto.execution.v1 import computation_action_pb2 as syft__proto_dot_execution_dot_v1_dot_computation__action__pb2
from syft_proto.types.torch.v1 import tensor_pb2 as syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='syft_proto/messaging/v1/message.proto',
  package='syft_proto.messaging.v1',
  syntax='proto3',
  serialized_options=_b('\n$org.openmined.syftproto.messaging.v1'),
  serialized_pb=_b('\n%syft_proto/messaging/v1/message.proto\x12\x17syft_proto.messaging.v1\x1a\x1bgoogle/protobuf/empty.proto\x1a\x30syft_proto/execution/v1/computation_action.proto\x1a&syft_proto/types/torch/v1/tensor.proto\"\x98\x02\n\x0bSyftMessage\x12\x46\n\x12\x63ontents_empty_msg\x18\x01 \x01(\x0b\x32\x16.google.protobuf.EmptyH\x00R\x10\x63ontentsEmptyMsg\x12X\n\x13\x63ontents_object_msg\x18\x05 \x01(\x0b\x32&.syft_proto.messaging.v1.ObjectMessageH\x00R\x11\x63ontentsObjectMsg\x12[\n\x14\x63ontents_command_msg\x18\x07 \x01(\x0b\x32\'.syft_proto.messaging.v1.CommandMessageH\x00R\x12\x63ontentsCommandMsgB\n\n\x08\x63ontents\"O\n\rObjectMessage\x12>\n\x06tensor\x18\x01 \x01(\x0b\x32&.syft_proto.types.torch.v1.TorchTensorR\x06tensor\"T\n\x0e\x43ommandMessage\x12\x42\n\x06\x61\x63tion\x18\x01 \x01(\x0b\x32*.syft_proto.execution.v1.ComputationActionR\x06\x61\x63tionB&\n$org.openmined.syftproto.messaging.v1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,syft__proto_dot_execution_dot_v1_dot_computation__action__pb2.DESCRIPTOR,syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2.DESCRIPTOR,])




_SYFTMESSAGE = _descriptor.Descriptor(
  name='SyftMessage',
  full_name='syft_proto.messaging.v1.SyftMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents_empty_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_empty_msg', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsEmptyMsg', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_object_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_object_msg', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsObjectMsg', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents_command_msg', full_name='syft_proto.messaging.v1.SyftMessage.contents_command_msg', index=2,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='contentsCommandMsg', file=DESCRIPTOR),
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
    _descriptor.OneofDescriptor(
      name='contents', full_name='syft_proto.messaging.v1.SyftMessage.contents',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=186,
  serialized_end=466,
)


_OBJECTMESSAGE = _descriptor.Descriptor(
  name='ObjectMessage',
  full_name='syft_proto.messaging.v1.ObjectMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor', full_name='syft_proto.messaging.v1.ObjectMessage.tensor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tensor', file=DESCRIPTOR),
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
  serialized_start=468,
  serialized_end=547,
)


_COMMANDMESSAGE = _descriptor.Descriptor(
  name='CommandMessage',
  full_name='syft_proto.messaging.v1.CommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='syft_proto.messaging.v1.CommandMessage.action', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='action', file=DESCRIPTOR),
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
  serialized_start=549,
  serialized_end=633,
)

_SYFTMESSAGE.fields_by_name['contents_empty_msg'].message_type = google_dot_protobuf_dot_empty__pb2._EMPTY
_SYFTMESSAGE.fields_by_name['contents_object_msg'].message_type = _OBJECTMESSAGE
_SYFTMESSAGE.fields_by_name['contents_command_msg'].message_type = _COMMANDMESSAGE
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_empty_msg'])
_SYFTMESSAGE.fields_by_name['contents_empty_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_object_msg'])
_SYFTMESSAGE.fields_by_name['contents_object_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_SYFTMESSAGE.oneofs_by_name['contents'].fields.append(
  _SYFTMESSAGE.fields_by_name['contents_command_msg'])
_SYFTMESSAGE.fields_by_name['contents_command_msg'].containing_oneof = _SYFTMESSAGE.oneofs_by_name['contents']
_OBJECTMESSAGE.fields_by_name['tensor'].message_type = syft__proto_dot_types_dot_torch_dot_v1_dot_tensor__pb2._TORCHTENSOR
_COMMANDMESSAGE.fields_by_name['action'].message_type = syft__proto_dot_execution_dot_v1_dot_computation__action__pb2._COMPUTATIONACTION
DESCRIPTOR.message_types_by_name['SyftMessage'] = _SYFTMESSAGE
DESCRIPTOR.message_types_by_name['ObjectMessage'] = _OBJECTMESSAGE
DESCRIPTOR.message_types_by_name['CommandMessage'] = _COMMANDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SyftMessage = _reflection.GeneratedProtocolMessageType('SyftMessage', (_message.Message,), {
  'DESCRIPTOR' : _SYFTMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.SyftMessage)
  })
_sym_db.RegisterMessage(SyftMessage)

ObjectMessage = _reflection.GeneratedProtocolMessageType('ObjectMessage', (_message.Message,), {
  'DESCRIPTOR' : _OBJECTMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.ObjectMessage)
  })
_sym_db.RegisterMessage(ObjectMessage)

CommandMessage = _reflection.GeneratedProtocolMessageType('CommandMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMMANDMESSAGE,
  '__module__' : 'syft_proto.messaging.v1.message_pb2'
  # @@protoc_insertion_point(class_scope:syft_proto.messaging.v1.CommandMessage)
  })
_sym_db.RegisterMessage(CommandMessage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
