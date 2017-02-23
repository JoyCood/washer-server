# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: washer_1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_1_pb2 as common__1__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='washer_1.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0ewasher_1.proto\x1a\x0e\x63ommon_1.proto\"<\n\x18Request_Authcode_Request\x12\r\n\x05phone\x18\x01 \x02(\t\x12\x11\n\tsignature\x18\x02 \x02(\t\"N\n\x19Request_Authcode_Response\x12\x10\n\x08\x61uthcode\x18\x01 \x01(\x05\x12\x1f\n\nerror_code\x18\x02 \x02(\x0e\x32\x0b.Error_Code\"\xa5\x01\n\x10Register_Request\x12\r\n\x05phone\x18\x01 \x02(\t\x12\x10\n\x08\x61uthcode\x18\x02 \x02(\x05\x12\x10\n\x08password\x18\x03 \x02(\t\x12\x11\n\tpassword2\x18\x04 \x02(\t\x12\x0c\n\x04nick\x18\x05 \x02(\t\x12\x11\n\tsignature\x18\x06 \x02(\t\x12\x1a\n\x04type\x18\x07 \x02(\x0e\x32\x0c.Washer_Type\x12\x0e\n\x06\x61vatar\x18\x08 \x01(\t\"M\n\x11Register_Response\x12\x17\n\x06washer\x18\x01 \x01(\x0b\x32\x07.Washer\x12\x1f\n\nerror_code\x18\x02 \x02(\x0e\x32\x0b.Error_Code\"Q\n\rLogin_Request\x12\r\n\x05phone\x18\x01 \x02(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04uuid\x18\x03 \x01(\t\x12\x11\n\tsignature\x18\x04 \x01(\t\"J\n\x0eLogin_Response\x12\x17\n\x06washer\x18\x01 \x01(\x0b\x32\x07.Washer\x12\x1f\n\nerror_code\x18\x03 \x02(\x0e\x32\x0b.Error_Code\"M\n\x17Verify_Authcode_Request\x12\r\n\x05phone\x18\x01 \x02(\t\x12\x10\n\x08\x61uthcode\x18\x02 \x02(\x05\x12\x11\n\tsignature\x18\x03 \x02(\t\";\n\x18Verify_Authcode_Response\x12\x1f\n\nerror_code\x18\x01 \x02(\x0e\x32\x0b.Error_Code\"P\n\x16\x46resh_Location_Request\x12\x11\n\tcity_code\x18\x01 \x02(\x05\x12\x11\n\tlongitude\x18\x02 \x02(\x02\x12\x10\n\x08latitude\x18\x03 \x02(\x02\":\n\x17\x46resh_Location_Response\x12\x1f\n\nerror_code\x18\x01 \x02(\x0e\x32\x0b.Error_Code\"L\n\x12Start_Work_Request\x12\x11\n\tcity_code\x18\x01 \x02(\x05\x12\x11\n\tlongitude\x18\x02 \x02(\x02\x12\x10\n\x08latitude\x18\x03 \x02(\x02\"6\n\x13Start_Work_Response\x12\x1f\n\nerror_code\x18\x01 \x02(\x0e\x32\x0b.Error_Code\"\x13\n\x11Stop_Work_Request\"5\n\x12Stop_Work_Response\x12\x1f\n\nerror_code\x18\x01 \x02(\x0e\x32\x0b.Error_Code\"\x10\n\x0eLogout_Request\"2\n\x0fLogout_Response\x12\x1f\n\nerror_code\x18\x01 \x02(\x0e\x32\x0b.Error_Code')
  ,
  dependencies=[common__1__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUEST_AUTHCODE_REQUEST = _descriptor.Descriptor(
  name='Request_Authcode_Request',
  full_name='Request_Authcode_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='Request_Authcode_Request.phone', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Request_Authcode_Request.signature', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=94,
)


_REQUEST_AUTHCODE_RESPONSE = _descriptor.Descriptor(
  name='Request_Authcode_Response',
  full_name='Request_Authcode_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authcode', full_name='Request_Authcode_Response.authcode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Request_Authcode_Response.error_code', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=96,
  serialized_end=174,
)


_REGISTER_REQUEST = _descriptor.Descriptor(
  name='Register_Request',
  full_name='Register_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='Register_Request.phone', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authcode', full_name='Register_Request.authcode', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='Register_Request.password', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password2', full_name='Register_Request.password2', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nick', full_name='Register_Request.nick', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Register_Request.signature', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='Register_Request.type', index=6,
      number=7, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='Register_Request.avatar', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=342,
)


_REGISTER_RESPONSE = _descriptor.Descriptor(
  name='Register_Response',
  full_name='Register_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='washer', full_name='Register_Response.washer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Register_Response.error_code', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=421,
)


_LOGIN_REQUEST = _descriptor.Descriptor(
  name='Login_Request',
  full_name='Login_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='Login_Request.phone', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='password', full_name='Login_Request.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='Login_Request.uuid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Login_Request.signature', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=423,
  serialized_end=504,
)


_LOGIN_RESPONSE = _descriptor.Descriptor(
  name='Login_Response',
  full_name='Login_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='washer', full_name='Login_Response.washer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Login_Response.error_code', index=1,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=506,
  serialized_end=580,
)


_VERIFY_AUTHCODE_REQUEST = _descriptor.Descriptor(
  name='Verify_Authcode_Request',
  full_name='Verify_Authcode_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phone', full_name='Verify_Authcode_Request.phone', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='authcode', full_name='Verify_Authcode_Request.authcode', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='Verify_Authcode_Request.signature', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=582,
  serialized_end=659,
)


_VERIFY_AUTHCODE_RESPONSE = _descriptor.Descriptor(
  name='Verify_Authcode_Response',
  full_name='Verify_Authcode_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Verify_Authcode_Response.error_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=661,
  serialized_end=720,
)


_FRESH_LOCATION_REQUEST = _descriptor.Descriptor(
  name='Fresh_Location_Request',
  full_name='Fresh_Location_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city_code', full_name='Fresh_Location_Request.city_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Fresh_Location_Request.longitude', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Fresh_Location_Request.latitude', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=722,
  serialized_end=802,
)


_FRESH_LOCATION_RESPONSE = _descriptor.Descriptor(
  name='Fresh_Location_Response',
  full_name='Fresh_Location_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Fresh_Location_Response.error_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=804,
  serialized_end=862,
)


_START_WORK_REQUEST = _descriptor.Descriptor(
  name='Start_Work_Request',
  full_name='Start_Work_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city_code', full_name='Start_Work_Request.city_code', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='Start_Work_Request.longitude', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='Start_Work_Request.latitude', index=2,
      number=3, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=864,
  serialized_end=940,
)


_START_WORK_RESPONSE = _descriptor.Descriptor(
  name='Start_Work_Response',
  full_name='Start_Work_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Start_Work_Response.error_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=942,
  serialized_end=996,
)


_STOP_WORK_REQUEST = _descriptor.Descriptor(
  name='Stop_Work_Request',
  full_name='Stop_Work_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=998,
  serialized_end=1017,
)


_STOP_WORK_RESPONSE = _descriptor.Descriptor(
  name='Stop_Work_Response',
  full_name='Stop_Work_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Stop_Work_Response.error_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1019,
  serialized_end=1072,
)


_LOGOUT_REQUEST = _descriptor.Descriptor(
  name='Logout_Request',
  full_name='Logout_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1074,
  serialized_end=1090,
)


_LOGOUT_RESPONSE = _descriptor.Descriptor(
  name='Logout_Response',
  full_name='Logout_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Logout_Response.error_code', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1092,
  serialized_end=1142,
)

_REQUEST_AUTHCODE_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_REGISTER_REQUEST.fields_by_name['type'].enum_type = common__1__pb2._WASHER_TYPE
_REGISTER_RESPONSE.fields_by_name['washer'].message_type = common__1__pb2._WASHER
_REGISTER_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_LOGIN_RESPONSE.fields_by_name['washer'].message_type = common__1__pb2._WASHER
_LOGIN_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_VERIFY_AUTHCODE_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_FRESH_LOCATION_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_START_WORK_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_STOP_WORK_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_LOGOUT_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
DESCRIPTOR.message_types_by_name['Request_Authcode_Request'] = _REQUEST_AUTHCODE_REQUEST
DESCRIPTOR.message_types_by_name['Request_Authcode_Response'] = _REQUEST_AUTHCODE_RESPONSE
DESCRIPTOR.message_types_by_name['Register_Request'] = _REGISTER_REQUEST
DESCRIPTOR.message_types_by_name['Register_Response'] = _REGISTER_RESPONSE
DESCRIPTOR.message_types_by_name['Login_Request'] = _LOGIN_REQUEST
DESCRIPTOR.message_types_by_name['Login_Response'] = _LOGIN_RESPONSE
DESCRIPTOR.message_types_by_name['Verify_Authcode_Request'] = _VERIFY_AUTHCODE_REQUEST
DESCRIPTOR.message_types_by_name['Verify_Authcode_Response'] = _VERIFY_AUTHCODE_RESPONSE
DESCRIPTOR.message_types_by_name['Fresh_Location_Request'] = _FRESH_LOCATION_REQUEST
DESCRIPTOR.message_types_by_name['Fresh_Location_Response'] = _FRESH_LOCATION_RESPONSE
DESCRIPTOR.message_types_by_name['Start_Work_Request'] = _START_WORK_REQUEST
DESCRIPTOR.message_types_by_name['Start_Work_Response'] = _START_WORK_RESPONSE
DESCRIPTOR.message_types_by_name['Stop_Work_Request'] = _STOP_WORK_REQUEST
DESCRIPTOR.message_types_by_name['Stop_Work_Response'] = _STOP_WORK_RESPONSE
DESCRIPTOR.message_types_by_name['Logout_Request'] = _LOGOUT_REQUEST
DESCRIPTOR.message_types_by_name['Logout_Response'] = _LOGOUT_RESPONSE

Request_Authcode_Request = _reflection.GeneratedProtocolMessageType('Request_Authcode_Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_AUTHCODE_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Request_Authcode_Request)
  ))
_sym_db.RegisterMessage(Request_Authcode_Request)

Request_Authcode_Response = _reflection.GeneratedProtocolMessageType('Request_Authcode_Response', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST_AUTHCODE_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Request_Authcode_Response)
  ))
_sym_db.RegisterMessage(Request_Authcode_Response)

Register_Request = _reflection.GeneratedProtocolMessageType('Register_Request', (_message.Message,), dict(
  DESCRIPTOR = _REGISTER_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Register_Request)
  ))
_sym_db.RegisterMessage(Register_Request)

Register_Response = _reflection.GeneratedProtocolMessageType('Register_Response', (_message.Message,), dict(
  DESCRIPTOR = _REGISTER_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Register_Response)
  ))
_sym_db.RegisterMessage(Register_Response)

Login_Request = _reflection.GeneratedProtocolMessageType('Login_Request', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Login_Request)
  ))
_sym_db.RegisterMessage(Login_Request)

Login_Response = _reflection.GeneratedProtocolMessageType('Login_Response', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Login_Response)
  ))
_sym_db.RegisterMessage(Login_Response)

Verify_Authcode_Request = _reflection.GeneratedProtocolMessageType('Verify_Authcode_Request', (_message.Message,), dict(
  DESCRIPTOR = _VERIFY_AUTHCODE_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Verify_Authcode_Request)
  ))
_sym_db.RegisterMessage(Verify_Authcode_Request)

Verify_Authcode_Response = _reflection.GeneratedProtocolMessageType('Verify_Authcode_Response', (_message.Message,), dict(
  DESCRIPTOR = _VERIFY_AUTHCODE_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Verify_Authcode_Response)
  ))
_sym_db.RegisterMessage(Verify_Authcode_Response)

Fresh_Location_Request = _reflection.GeneratedProtocolMessageType('Fresh_Location_Request', (_message.Message,), dict(
  DESCRIPTOR = _FRESH_LOCATION_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Fresh_Location_Request)
  ))
_sym_db.RegisterMessage(Fresh_Location_Request)

Fresh_Location_Response = _reflection.GeneratedProtocolMessageType('Fresh_Location_Response', (_message.Message,), dict(
  DESCRIPTOR = _FRESH_LOCATION_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Fresh_Location_Response)
  ))
_sym_db.RegisterMessage(Fresh_Location_Response)

Start_Work_Request = _reflection.GeneratedProtocolMessageType('Start_Work_Request', (_message.Message,), dict(
  DESCRIPTOR = _START_WORK_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Start_Work_Request)
  ))
_sym_db.RegisterMessage(Start_Work_Request)

Start_Work_Response = _reflection.GeneratedProtocolMessageType('Start_Work_Response', (_message.Message,), dict(
  DESCRIPTOR = _START_WORK_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Start_Work_Response)
  ))
_sym_db.RegisterMessage(Start_Work_Response)

Stop_Work_Request = _reflection.GeneratedProtocolMessageType('Stop_Work_Request', (_message.Message,), dict(
  DESCRIPTOR = _STOP_WORK_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Stop_Work_Request)
  ))
_sym_db.RegisterMessage(Stop_Work_Request)

Stop_Work_Response = _reflection.GeneratedProtocolMessageType('Stop_Work_Response', (_message.Message,), dict(
  DESCRIPTOR = _STOP_WORK_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Stop_Work_Response)
  ))
_sym_db.RegisterMessage(Stop_Work_Response)

Logout_Request = _reflection.GeneratedProtocolMessageType('Logout_Request', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUT_REQUEST,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Logout_Request)
  ))
_sym_db.RegisterMessage(Logout_Request)

Logout_Response = _reflection.GeneratedProtocolMessageType('Logout_Response', (_message.Message,), dict(
  DESCRIPTOR = _LOGOUT_RESPONSE,
  __module__ = 'washer_1_pb2'
  # @@protoc_insertion_point(class_scope:Logout_Response)
  ))
_sym_db.RegisterMessage(Logout_Response)


# @@protoc_insertion_point(module_scope)
