# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: order_1.proto

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
  name='order_1.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\rorder_1.proto\x1a\x0e\x63ommon_1.proto\"(\n\x14Order_Finish_Request\x12\x10\n\x08order_id\x18\x01 \x02(\t\"8\n\x15Order_Finish_Response\x12\x1f\n\nerror_code\x18\x01 \x02(\x0e\x32\x0b.Error_Code\"(\n\x14Order_Cancel_Request\x12\x10\n\x08order_id\x18\x01 \x02(\t\"8\n\x15Order_Cancel_Response\x12\x1f\n\nerror_code\x18\x01 \x02(\x0e\x32\x0b.Error_Code\"w\n\x13\x41llocate_Order_Push\x12\x1b\n\x08\x63ustomer\x18\x01 \x02(\x0b\x32\t.Customer\x12\x10\n\x08order_id\x18\x02 \x02(\t\x12\x10\n\x08quantity\x18\x03 \x02(\x05\x12\x1f\n\nerror_code\x18\x04 \x02(\x0e\x32\x0b.Error_Code')
  ,
  dependencies=[common__1__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ORDER_FINISH_REQUEST = _descriptor.Descriptor(
  name='Order_Finish_Request',
  full_name='Order_Finish_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Order_Finish_Request.order_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=33,
  serialized_end=73,
)


_ORDER_FINISH_RESPONSE = _descriptor.Descriptor(
  name='Order_Finish_Response',
  full_name='Order_Finish_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Order_Finish_Response.error_code', index=0,
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
  serialized_start=75,
  serialized_end=131,
)


_ORDER_CANCEL_REQUEST = _descriptor.Descriptor(
  name='Order_Cancel_Request',
  full_name='Order_Cancel_Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Order_Cancel_Request.order_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=133,
  serialized_end=173,
)


_ORDER_CANCEL_RESPONSE = _descriptor.Descriptor(
  name='Order_Cancel_Response',
  full_name='Order_Cancel_Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Order_Cancel_Response.error_code', index=0,
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
  serialized_start=175,
  serialized_end=231,
)


_ALLOCATE_ORDER_PUSH = _descriptor.Descriptor(
  name='Allocate_Order_Push',
  full_name='Allocate_Order_Push',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='customer', full_name='Allocate_Order_Push.customer', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='Allocate_Order_Push.order_id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='Allocate_Order_Push.quantity', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='Allocate_Order_Push.error_code', index=3,
      number=4, type=14, cpp_type=8, label=2,
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
  serialized_start=233,
  serialized_end=352,
)

_ORDER_FINISH_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_ORDER_CANCEL_RESPONSE.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
_ALLOCATE_ORDER_PUSH.fields_by_name['customer'].message_type = common__1__pb2._CUSTOMER
_ALLOCATE_ORDER_PUSH.fields_by_name['error_code'].enum_type = common__1__pb2._ERROR_CODE
DESCRIPTOR.message_types_by_name['Order_Finish_Request'] = _ORDER_FINISH_REQUEST
DESCRIPTOR.message_types_by_name['Order_Finish_Response'] = _ORDER_FINISH_RESPONSE
DESCRIPTOR.message_types_by_name['Order_Cancel_Request'] = _ORDER_CANCEL_REQUEST
DESCRIPTOR.message_types_by_name['Order_Cancel_Response'] = _ORDER_CANCEL_RESPONSE
DESCRIPTOR.message_types_by_name['Allocate_Order_Push'] = _ALLOCATE_ORDER_PUSH

Order_Finish_Request = _reflection.GeneratedProtocolMessageType('Order_Finish_Request', (_message.Message,), dict(
  DESCRIPTOR = _ORDER_FINISH_REQUEST,
  __module__ = 'order_1_pb2'
  # @@protoc_insertion_point(class_scope:Order_Finish_Request)
  ))
_sym_db.RegisterMessage(Order_Finish_Request)

Order_Finish_Response = _reflection.GeneratedProtocolMessageType('Order_Finish_Response', (_message.Message,), dict(
  DESCRIPTOR = _ORDER_FINISH_RESPONSE,
  __module__ = 'order_1_pb2'
  # @@protoc_insertion_point(class_scope:Order_Finish_Response)
  ))
_sym_db.RegisterMessage(Order_Finish_Response)

Order_Cancel_Request = _reflection.GeneratedProtocolMessageType('Order_Cancel_Request', (_message.Message,), dict(
  DESCRIPTOR = _ORDER_CANCEL_REQUEST,
  __module__ = 'order_1_pb2'
  # @@protoc_insertion_point(class_scope:Order_Cancel_Request)
  ))
_sym_db.RegisterMessage(Order_Cancel_Request)

Order_Cancel_Response = _reflection.GeneratedProtocolMessageType('Order_Cancel_Response', (_message.Message,), dict(
  DESCRIPTOR = _ORDER_CANCEL_RESPONSE,
  __module__ = 'order_1_pb2'
  # @@protoc_insertion_point(class_scope:Order_Cancel_Response)
  ))
_sym_db.RegisterMessage(Order_Cancel_Response)

Allocate_Order_Push = _reflection.GeneratedProtocolMessageType('Allocate_Order_Push', (_message.Message,), dict(
  DESCRIPTOR = _ALLOCATE_ORDER_PUSH,
  __module__ = 'order_1_pb2'
  # @@protoc_insertion_point(class_scope:Allocate_Order_Push)
  ))
_sym_db.RegisterMessage(Allocate_Order_Push)


# @@protoc_insertion_point(module_scope)
