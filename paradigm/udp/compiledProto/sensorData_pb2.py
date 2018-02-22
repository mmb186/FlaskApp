# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sensorData.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sensorData.proto',
  package='tutorial',
  serialized_pb=_b('\n\x10sensorData.proto\x12\x08tutorial\"\xa1\x01\n\x06Sensor\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x05\x12\x0c\n\x04time\x18\x03 \x02(\x05\x12/\n\x06status\x18\x04 \x01(\x0e\x32\x19.tutorial.Sensor.statuses:\x04GOOD\x12\x0f\n\x07message\x18\x05 \x01(\t\"*\n\x08statuses\x12\x08\n\x04GOOD\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\t\n\x05\x41LERT\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_SENSOR_STATUSES = _descriptor.EnumDescriptor(
  name='statuses',
  full_name='tutorial.Sensor.statuses',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GOOD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALERT', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=150,
  serialized_end=192,
)
_sym_db.RegisterEnumDescriptor(_SENSOR_STATUSES)


_SENSOR = _descriptor.Descriptor(
  name='Sensor',
  full_name='tutorial.Sensor',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tutorial.Sensor.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tutorial.Sensor.value', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='tutorial.Sensor.time', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='tutorial.Sensor.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='tutorial.Sensor.message', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SENSOR_STATUSES,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=192,
)

_SENSOR.fields_by_name['status'].enum_type = _SENSOR_STATUSES
_SENSOR_STATUSES.containing_type = _SENSOR
DESCRIPTOR.message_types_by_name['Sensor'] = _SENSOR

Sensor = _reflection.GeneratedProtocolMessageType('Sensor', (_message.Message,), dict(
  DESCRIPTOR = _SENSOR,
  __module__ = 'sensorData_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Sensor)
  ))
_sym_db.RegisterMessage(Sensor)


# @@protoc_insertion_point(module_scope)