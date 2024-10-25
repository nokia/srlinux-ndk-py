# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndk/nexthop_group_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ndk import sdk_common_pb2 as ndk_dot_sdk__common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fndk/nexthop_group_service.proto\x12\x0bsrlinux.sdk\x1a\x14ndk/sdk_common.proto\"L\n\x19NextHopGroupDeleteRequest\x12/\n\tgroup_key\x18\x01 \x03(\x0b\x32\x1c.srlinux.sdk.NextHopGroupKey\"Z\n\x1aNextHopGroupDeleteResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srlinux.sdk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t\"H\n\x13NextHopGroupRequest\x12\x31\n\ngroup_info\x18\x01 \x03(\x0b\x32\x1d.srlinux.sdk.NextHopGroupInfo\"T\n\x14NextHopGroupResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srlinux.sdk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t\"h\n\x0bMplsNextHop\x12,\n\nip_nexthop\x18\x01 \x01(\x0b\x32\x18.srlinux.sdk.IpAddressPb\x12+\n\x0blabel_stack\x18\x02 \x03(\x0b\x32\x16.srlinux.sdk.MplsLabel\"\xcd\x02\n\x07NextHop\x12\x36\n\nresolve_to\x18\x01 \x01(\x0e\x32\".srlinux.sdk.NextHop.ResolveToType\x12\x31\n\x04type\x18\x02 \x01(\x0e\x32#.srlinux.sdk.NextHop.ResolutionType\x12.\n\nip_nexthop\x18\x03 \x01(\x0b\x32\x18.srlinux.sdk.IpAddressPbH\x00\x12\x30\n\x0cmpls_nexthop\x18\x04 \x01(\x0b\x32\x18.srlinux.sdk.MplsNextHopH\x00\"4\n\rResolveToType\x12\t\n\x05LOCAL\x10\x00\x12\n\n\x06\x44IRECT\x10\x01\x12\x0c\n\x08INDIRECT\x10\x02\"4\n\x0eResolutionType\x12\x0b\n\x07INVALID\x10\x00\x12\x0b\n\x07REGULAR\x10\x01\x12\x08\n\x04MPLS\x10\x02\x42\t\n\x07nexthop\"6\n\x0cNextHopGroup\x12&\n\x08next_hop\x18\x01 \x03(\x0b\x32\x14.srlinux.sdk.NextHop\">\n\x0fNextHopGroupKey\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1d\n\x15network_instance_name\x18\x02 \x01(\t\"f\n\x10NextHopGroupInfo\x12)\n\x03key\x18\x01 \x01(\x0b\x32\x1c.srlinux.sdk.NextHopGroupKey\x12\'\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x19.srlinux.sdk.NextHopGroup\"L\n\x1fNextHopGroupSubscriptionRequest\x12)\n\x03key\x18\x01 \x01(\x0b\x32\x1c.srlinux.sdk.NextHopGroupKey\"z\n\x18NextHopGroupNotification\x12(\n\x02op\x18\x01 \x01(\x0e\x32\x1c.srlinux.sdk.SdkMgrOperation\x12\x0b\n\x03key\x18\x02 \x01(\x04\x12\'\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x19.srlinux.sdk.NextHopGroup2\xec\x02\n\x19SdkMgrNextHopGroupService\x12`\n\x17NextHopGroupAddOrUpdate\x12 .srlinux.sdk.NextHopGroupRequest\x1a!.srlinux.sdk.NextHopGroupResponse\"\x00\x12g\n\x12NextHopGroupDelete\x12&.srlinux.sdk.NextHopGroupDeleteRequest\x1a\'.srlinux.sdk.NextHopGroupDeleteResponse\"\x00\x12\x42\n\tSyncStart\x12\x18.srlinux.sdk.SyncRequest\x1a\x19.srlinux.sdk.SyncResponse\"\x00\x12@\n\x07SyncEnd\x12\x18.srlinux.sdk.SyncRequest\x1a\x19.srlinux.sdk.SyncResponse\"\x00\x42%Z#github.com/nokia/srlinux-ndk-go/ndkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ndk.nexthop_group_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z#github.com/nokia/srlinux-ndk-go/ndk'
  _globals['_NEXTHOPGROUPDELETEREQUEST']._serialized_start=70
  _globals['_NEXTHOPGROUPDELETEREQUEST']._serialized_end=146
  _globals['_NEXTHOPGROUPDELETERESPONSE']._serialized_start=148
  _globals['_NEXTHOPGROUPDELETERESPONSE']._serialized_end=238
  _globals['_NEXTHOPGROUPREQUEST']._serialized_start=240
  _globals['_NEXTHOPGROUPREQUEST']._serialized_end=312
  _globals['_NEXTHOPGROUPRESPONSE']._serialized_start=314
  _globals['_NEXTHOPGROUPRESPONSE']._serialized_end=398
  _globals['_MPLSNEXTHOP']._serialized_start=400
  _globals['_MPLSNEXTHOP']._serialized_end=504
  _globals['_NEXTHOP']._serialized_start=507
  _globals['_NEXTHOP']._serialized_end=840
  _globals['_NEXTHOP_RESOLVETOTYPE']._serialized_start=723
  _globals['_NEXTHOP_RESOLVETOTYPE']._serialized_end=775
  _globals['_NEXTHOP_RESOLUTIONTYPE']._serialized_start=777
  _globals['_NEXTHOP_RESOLUTIONTYPE']._serialized_end=829
  _globals['_NEXTHOPGROUP']._serialized_start=842
  _globals['_NEXTHOPGROUP']._serialized_end=896
  _globals['_NEXTHOPGROUPKEY']._serialized_start=898
  _globals['_NEXTHOPGROUPKEY']._serialized_end=960
  _globals['_NEXTHOPGROUPINFO']._serialized_start=962
  _globals['_NEXTHOPGROUPINFO']._serialized_end=1064
  _globals['_NEXTHOPGROUPSUBSCRIPTIONREQUEST']._serialized_start=1066
  _globals['_NEXTHOPGROUPSUBSCRIPTIONREQUEST']._serialized_end=1142
  _globals['_NEXTHOPGROUPNOTIFICATION']._serialized_start=1144
  _globals['_NEXTHOPGROUPNOTIFICATION']._serialized_end=1266
  _globals['_SDKMGRNEXTHOPGROUPSERVICE']._serialized_start=1269
  _globals['_SDKMGRNEXTHOPGROUPSERVICE']._serialized_end=1633
# @@protoc_insertion_point(module_scope)
