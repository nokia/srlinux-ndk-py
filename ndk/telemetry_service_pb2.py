# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndk/telemetry_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ndk import sdk_common_pb2 as ndk_dot_sdk__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bndk/telemetry_service.proto\x12\x0bsrlinux.sdk\x1a\x14ndk/sdk_common.proto\"\x1f\n\x0cTelemetryKey\x12\x0f\n\x07js_path\x18\x01 \x01(\t\"%\n\rTelemetryData\x12\x14\n\x0cjson_content\x18\x01 \x01(\t\"a\n\rTelemetryInfo\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.srlinux.sdk.TelemetryKey\x12(\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x1a.srlinux.sdk.TelemetryData\"D\n\x16TelemetryUpdateRequest\x12*\n\x06states\x18\x01 \x03(\x0b\x32\x1a.srlinux.sdk.TelemetryInfo\"W\n\x17TelemetryUpdateResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srlinux.sdk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t\"A\n\x16TelemetryDeleteRequest\x12\'\n\x04keys\x18\x01 \x03(\x0b\x32\x19.srlinux.sdk.TelemetryKey\"W\n\x17TelemetryDeleteResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srlinux.sdk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t2\xdd\x01\n\x16SdkMgrTelemetryService\x12\x63\n\x14TelemetryAddOrUpdate\x12#.srlinux.sdk.TelemetryUpdateRequest\x1a$.srlinux.sdk.TelemetryUpdateResponse\"\x00\x12^\n\x0fTelemetryDelete\x12#.srlinux.sdk.TelemetryDeleteRequest\x1a$.srlinux.sdk.TelemetryDeleteResponse\"\x00\x42%Z#github.com/nokia/srlinux-ndk-go/ndkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ndk.telemetry_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z#github.com/nokia/srlinux-ndk-go/ndk'
  _globals['_TELEMETRYKEY']._serialized_start=66
  _globals['_TELEMETRYKEY']._serialized_end=97
  _globals['_TELEMETRYDATA']._serialized_start=99
  _globals['_TELEMETRYDATA']._serialized_end=136
  _globals['_TELEMETRYINFO']._serialized_start=138
  _globals['_TELEMETRYINFO']._serialized_end=235
  _globals['_TELEMETRYUPDATEREQUEST']._serialized_start=237
  _globals['_TELEMETRYUPDATEREQUEST']._serialized_end=305
  _globals['_TELEMETRYUPDATERESPONSE']._serialized_start=307
  _globals['_TELEMETRYUPDATERESPONSE']._serialized_end=394
  _globals['_TELEMETRYDELETEREQUEST']._serialized_start=396
  _globals['_TELEMETRYDELETEREQUEST']._serialized_end=461
  _globals['_TELEMETRYDELETERESPONSE']._serialized_start=463
  _globals['_TELEMETRYDELETERESPONSE']._serialized_end=550
  _globals['_SDKMGRTELEMETRYSERVICE']._serialized_start=553
  _globals['_SDKMGRTELEMETRYSERVICE']._serialized_end=774
# @@protoc_insertion_point(module_scope)
