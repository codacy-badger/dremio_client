# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: command.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='command.proto',
  package='com.dremio.proto.flight.commands',
  syntax='proto2',
  serialized_options=_b('\n com.dremio.proto.flight.commandsH\001'),
  serialized_pb=_b('\n\rcommand.proto\x12 com.dremio.proto.flight.commands\"L\n\x07\x43ommand\x12\r\n\x05query\x18\x01 \x02(\t\x12\x10\n\x08parallel\x18\x02 \x02(\x08\x12\x10\n\x08\x63oalesce\x18\x03 \x02(\x08\x12\x0e\n\x06ticket\x18\x04 \x02(\x0c\x42$\n com.dremio.proto.flight.commandsH\x01')
)




_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='com.dremio.proto.flight.commands.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='com.dremio.proto.flight.commands.Command.query', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parallel', full_name='com.dremio.proto.flight.commands.Command.parallel', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coalesce', full_name='com.dremio.proto.flight.commands.Command.coalesce', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ticket', full_name='com.dremio.proto.flight.commands.Command.ticket', index=3,
      number=4, type=12, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'command_pb2'
  # @@protoc_insertion_point(class_scope:com.dremio.proto.flight.commands.Command)
  ))
_sym_db.RegisterMessage(Command)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)