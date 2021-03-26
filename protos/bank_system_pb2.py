# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/bank_system.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/bank_system.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18protos/bank_system.proto\":\n\x06\x45vents\x12\x16\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x06.Event\x12\x18\n\x10number_of_fellow\x18\x02 \x01(\x05\"5\n\x05\x45vent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\tinterface\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x05\")\n\x06Output\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x04recv\x18\x02 \x03(\x0b\x32\x05.Recv\"8\n\x04Recv\x12\x11\n\tinterface\x18\x01 \x01(\t\x12\x0e\n\x06result\x18\x02 \x01(\t\x12\r\n\x05money\x18\x03 \x01(\x05\x32\xc5\x01\n\rBranchService\x12!\n\x0bMsgDelivery\x12\x07.Events\x1a\x07.Output\"\x00\x12$\n\x11Propogate_Deposit\x12\x06.Event\x1a\x05.Recv\"\x00\x12%\n\x12Propogate_Withdraw\x12\x06.Event\x1a\x05.Recv\"\x00\x12#\n\x0fgetFinalBalance\x12\x06.Event\x1a\x06.Event\"\x00\x12\x1f\n\tgetOutput\x12\x07.Output\x1a\x07.Output\"\x00\x62\x06proto3'
)




_EVENTS = _descriptor.Descriptor(
  name='Events',
  full_name='Events',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='Events.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='number_of_fellow', full_name='Events.number_of_fellow', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=86,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Event.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interface', full_name='Event.interface', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='money', full_name='Event.money', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=88,
  serialized_end=141,
)


_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Output.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recv', full_name='Output.recv', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=143,
  serialized_end=184,
)


_RECV = _descriptor.Descriptor(
  name='Recv',
  full_name='Recv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='interface', full_name='Recv.interface', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='result', full_name='Recv.result', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='money', full_name='Recv.money', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=186,
  serialized_end=242,
)

_EVENTS.fields_by_name['events'].message_type = _EVENT
_OUTPUT.fields_by_name['recv'].message_type = _RECV
DESCRIPTOR.message_types_by_name['Events'] = _EVENTS
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['Recv'] = _RECV
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Events = _reflection.GeneratedProtocolMessageType('Events', (_message.Message,), {
  'DESCRIPTOR' : _EVENTS,
  '__module__' : 'protos.bank_system_pb2'
  # @@protoc_insertion_point(class_scope:Events)
  })
_sym_db.RegisterMessage(Events)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'protos.bank_system_pb2'
  # @@protoc_insertion_point(class_scope:Event)
  })
_sym_db.RegisterMessage(Event)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'protos.bank_system_pb2'
  # @@protoc_insertion_point(class_scope:Output)
  })
_sym_db.RegisterMessage(Output)

Recv = _reflection.GeneratedProtocolMessageType('Recv', (_message.Message,), {
  'DESCRIPTOR' : _RECV,
  '__module__' : 'protos.bank_system_pb2'
  # @@protoc_insertion_point(class_scope:Recv)
  })
_sym_db.RegisterMessage(Recv)



_BRANCHSERVICE = _descriptor.ServiceDescriptor(
  name='BranchService',
  full_name='BranchService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=245,
  serialized_end=442,
  methods=[
  _descriptor.MethodDescriptor(
    name='MsgDelivery',
    full_name='BranchService.MsgDelivery',
    index=0,
    containing_service=None,
    input_type=_EVENTS,
    output_type=_OUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Propogate_Deposit',
    full_name='BranchService.Propogate_Deposit',
    index=1,
    containing_service=None,
    input_type=_EVENT,
    output_type=_RECV,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Propogate_Withdraw',
    full_name='BranchService.Propogate_Withdraw',
    index=2,
    containing_service=None,
    input_type=_EVENT,
    output_type=_RECV,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getFinalBalance',
    full_name='BranchService.getFinalBalance',
    index=3,
    containing_service=None,
    input_type=_EVENT,
    output_type=_EVENT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='getOutput',
    full_name='BranchService.getOutput',
    index=4,
    containing_service=None,
    input_type=_OUTPUT,
    output_type=_OUTPUT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BRANCHSERVICE)

DESCRIPTOR.services_by_name['BranchService'] = _BRANCHSERVICE

# @@protoc_insertion_point(module_scope)
