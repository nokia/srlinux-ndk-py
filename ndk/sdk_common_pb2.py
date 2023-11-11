# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndk/sdk_common.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ndk/sdk_common.proto\x12\x0bsrlinux.sdk\"\x1b\n\x0bIpAddressPb\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\x0c\"S\n\x0fIpAddrPrefLenPb\x12)\n\x07ip_addr\x18\x01 \x01(\x0b\x32\x18.srlinux.sdk.IpAddressPb\x12\x15\n\rprefix_length\x18\x02 \x01(\r\"s\n\x17IpInterfaceAddrPrefixPb\x12,\n\x06prefix\x18\x01 \x01(\x0b\x32\x1c.srlinux.sdk.IpAddrPrefLenPb\x12*\n\x05state\x18\x02 \x01(\x0e\x32\x1b.srlinux.sdk.IpAddressState\"#\n\x0cMacAddressPb\x12\x13\n\x0bmac_address\x18\x01 \x01(\x0c\"\"\n\nGlobalIfId\x12\x14\n\x0cglobal_if_id\x18\x01 \x01(\r\"$\n\rNetInstanceId\x12\x13\n\x0binstance_id\x18\x01 \x01(\r\"\x1b\n\x08PortIdPb\x12\x0f\n\x07port_id\x18\x01 \x01(\x04\"\x1f\n\tMplsLabel\x12\x12\n\nmpls_label\x18\x01 \x01(\r\"\x0c\n\nAgentReply\"\r\n\x0bSyncRequest\"L\n\x0cSyncResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.srlinux.sdk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t\"\x1f\n\x0e\x45vpnEthSegIdPb\x12\r\n\x05\x65s_id\x18\x01 \x01(\x0c*\xa3\x01\n\x0bIfMgrIfType\x12\x0c\n\x08\x45THERNET\x10\x00\x12\x0c\n\x08LOOPBACK\x10\x01\x12\x0e\n\nMANAGEMENT\x10\x02\x12\r\n\tAGGREGATE\x10\x03\x12\x07\n\x03IRB\x10\x04\x12\n\n\x06SYSTEM\x10\x05\x12\x07\n\x03LIF\x10\x06\x12\x07\n\x03NIC\x10\x07\x12\t\n\x05VHOST\x10\x08\x12\t\n\x05KKLIF\x10\t\x12\x0b\n\x07KKVHOST\x10\n\x12\x0f\n\x0bIF_TYPE_MAX\x10\x0b*\xbb\x01\n\x0eIpAddressState\x12\x18\n\x14IPADDR_STATE_UNKNOWN\x10\x00\x12\x1a\n\x16IPADDR_STATE_TENTATIVE\x10\x01\x12\x1b\n\x17IPADDR_STATE_DUPLICATED\x10\x02\x12\x1d\n\x19IPADDR_STATE_INACCESSIBLE\x10\x03\x12\x1b\n\x17IPADDR_STATE_DEPRECATED\x10\x04\x12\x1a\n\x16IPADDR_STATE_PREFERRED\x10\x05*\xd3\x01\n\x0fIfOperStateType\x12\x14\n\x10IF_OPER_STATE_UP\x10\x00\x12\x16\n\x12IF_OPER_STATE_DOWN\x10\x01\x12\x19\n\x15IF_OPER_STATE_TESTING\x10\x02\x12\x19\n\x15IF_OPER_STATE_UNKNOWN\x10\x03\x12\x19\n\x15IF_OPER_STATE_DORMANT\x10\x04\x12\x1d\n\x19IF_OPER_STATE_NOT_PRESENT\x10\x05\x12\"\n\x1eIF_OPER_STATE_LOWER_LAYER_DOWN\x10\x06*\x9b\x07\n\x10IfOperDownReason\x12\x15\n\x11IF_OPER_DOWN_NONE\x10\x00\x12$\n IF_OPER_DOWN_PORT_ADMIN_DISABLED\x10\x01\x12#\n\x1fIF_OPER_DOWN_MDA_ADMIN_DISABLED\x10\x02\x12%\n!IF_OPER_DOWN_TRANS_LASER_DISABLED\x10\x03\x12 \n\x1cIF_OPER_DOWN_MDA_NOT_PRESENT\x10\x04\x12\"\n\x1eIF_OPER_DOWN_TRANS_NOT_PRESENT\x10\x05\x12\x19\n\x15IF_OPER_DOWN_PHY_INIT\x10\x06\x12!\n\x1dIF_OPER_DOWN_LOWER_LAYER_DOWN\x10\x07\x12\x1e\n\x1aIF_OPER_DOWN_MTU_RESOURCES\x10\x08\x12\"\n\x1eIF_OPER_DOWN_UNSUPPORTED_SPEED\x10\t\x12&\n\"IF_OPER_DOWN_UNSUPPORTED_TRANS_FEC\x10\n\x12\x16\n\x12IF_OPER_DOWN_OTHER\x10\x0b\x12!\n\x1dIF_OPER_DOWN_PORT_NOT_PRESENT\x10\x0c\x12$\n IF_OPER_DOWN_FABRIC_AVAILABILITY\x10\r\x12 \n\x1cIF_OPER_DOWN_NO_ACTIVE_LINKS\x10\x0e\x12#\n\x1fIF_OPER_DOWN_MIN_LINK_THRESHOLD\x10\x0f\x12$\n IF_OPER_DOWN_9_12_SPEED_MISMATCH\x10\x10\x12\x1e\n\x1aIF_OPER_DOWN_LAG_RESOURCES\x10\x11\x12%\n!IF_OPER_DOWN_LAG_MEMBER_RESOURCES\x10\x12\x12\"\n\x1eIF_OPER_DOWN_STANDBY_SIGNALING\x10\x13\x12$\n IF_OPER_DOWN_HOLD_TIME_UP_ACTIVE\x10\x14\x12#\n\x1fIF_OPER_DOWN_RELOAD_TIME_ACTIVE\x10\x15\x12\x1f\n\x1bIF_OPER_DOWN_CONNECTOR_DOWN\x10\x16\x12\"\n\x1eIF_OPER_DOWN_AUTO_NEG_MISMATCH\x10\x17\x12\x1e\n\x1aIF_OPER_DOWN_EVENT_HANDLER\x10\x18\x12%\n!IF_OPER_DOWN_UNSUPPORTED_BREAKOUT\x10\x19*\xe1\x02\n\x17IfEthernetPortSpeedType\x12\x1b\n\x17IF_ETH_PORT_SPEED_UNSET\x10\x00\x12\x19\n\x15IF_ETH_PORT_SPEED_10M\x10\x01\x12\x1a\n\x16IF_ETH_PORT_SPEED_100M\x10\x02\x12\x18\n\x14IF_ETH_PORT_SPEED_1G\x10\x03\x12\x19\n\x15IF_ETH_PORT_SPEED_10G\x10\x04\x12\x19\n\x15IF_ETH_PORT_SPEED_25G\x10\x05\x12\x19\n\x15IF_ETH_PORT_SPEED_40G\x10\x06\x12\x19\n\x15IF_ETH_PORT_SPEED_50G\x10\x07\x12\x1a\n\x16IF_ETH_PORT_SPEED_100G\x10\x08\x12\x1a\n\x16IF_ETH_PORT_SPEED_200G\x10\t\x12\x1a\n\x16IF_ETH_PORT_SPEED_400G\x10\n\x12\x18\n\x14IF_ETH_PORT_SPEED_1T\x10\x0b*r\n\x18IfEthernetDuplexModeType\x12\x1c\n\x18IF_ETH_DUPLEX_MODE_UNSET\x10\x00\x12\x1b\n\x17IF_ETH_DUPLEX_MODE_FULL\x10\x01\x12\x1b\n\x17IF_ETH_DUPLEX_MODE_HALF\x10\x02*\x89\x01\n\x12IfLoopbackModeType\x12\x1a\n\x16IF_LOOPBACK_MODE_UNSET\x10\x00\x12\x19\n\x15IF_LOOPBACK_MODE_NONE\x10\x01\x12\x1d\n\x19IF_LOOPBACK_MODE_FACILITY\x10\x02\x12\x1d\n\x19IF_LOOPBACK_MODE_TERMINAL\x10\x03*\xa9\x01\n\x14IfTransceiverFecType\x12\x16\n\x12IF_TRANS_FEC_UNSET\x10\x00\x12\x19\n\x15IF_TRANS_FEC_DISABLED\x10\x01\x12\x16\n\x12IF_TRANS_FEC_RS528\x10\x02\x12\x16\n\x12IF_TRANS_FEC_RS544\x10\x03\x12\x16\n\x12IF_TRANS_FEC_BASER\x10\x04\x12\x16\n\x12IF_TRANS_FEC_RS108\x10\x05*5\n\x0fSdkMgrOperation\x12\n\n\x06\x43reate\x10\x00\x12\n\n\x06Update\x10\x01\x12\n\n\x06\x44\x65lete\x10\x02*5\n\x0cSdkMgrStatus\x12\x12\n\x0ekSdkMgrSuccess\x10\x00\x12\x11\n\rkSdkMgrFailed\x10\x01\x42%Z#github.com/nokia/srlinux-ndk-go/ndkb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ndk.sdk_common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z#github.com/nokia/srlinux-ndk-go/ndk'
  _globals['_IFMGRIFTYPE']._serialized_start=582
  _globals['_IFMGRIFTYPE']._serialized_end=745
  _globals['_IPADDRESSSTATE']._serialized_start=748
  _globals['_IPADDRESSSTATE']._serialized_end=935
  _globals['_IFOPERSTATETYPE']._serialized_start=938
  _globals['_IFOPERSTATETYPE']._serialized_end=1149
  _globals['_IFOPERDOWNREASON']._serialized_start=1152
  _globals['_IFOPERDOWNREASON']._serialized_end=2075
  _globals['_IFETHERNETPORTSPEEDTYPE']._serialized_start=2078
  _globals['_IFETHERNETPORTSPEEDTYPE']._serialized_end=2431
  _globals['_IFETHERNETDUPLEXMODETYPE']._serialized_start=2433
  _globals['_IFETHERNETDUPLEXMODETYPE']._serialized_end=2547
  _globals['_IFLOOPBACKMODETYPE']._serialized_start=2550
  _globals['_IFLOOPBACKMODETYPE']._serialized_end=2687
  _globals['_IFTRANSCEIVERFECTYPE']._serialized_start=2690
  _globals['_IFTRANSCEIVERFECTYPE']._serialized_end=2859
  _globals['_SDKMGROPERATION']._serialized_start=2861
  _globals['_SDKMGROPERATION']._serialized_end=2914
  _globals['_SDKMGRSTATUS']._serialized_start=2916
  _globals['_SDKMGRSTATUS']._serialized_end=2969
  _globals['_IPADDRESSPB']._serialized_start=37
  _globals['_IPADDRESSPB']._serialized_end=64
  _globals['_IPADDRPREFLENPB']._serialized_start=66
  _globals['_IPADDRPREFLENPB']._serialized_end=149
  _globals['_IPINTERFACEADDRPREFIXPB']._serialized_start=151
  _globals['_IPINTERFACEADDRPREFIXPB']._serialized_end=266
  _globals['_MACADDRESSPB']._serialized_start=268
  _globals['_MACADDRESSPB']._serialized_end=303
  _globals['_GLOBALIFID']._serialized_start=305
  _globals['_GLOBALIFID']._serialized_end=339
  _globals['_NETINSTANCEID']._serialized_start=341
  _globals['_NETINSTANCEID']._serialized_end=377
  _globals['_PORTIDPB']._serialized_start=379
  _globals['_PORTIDPB']._serialized_end=406
  _globals['_MPLSLABEL']._serialized_start=408
  _globals['_MPLSLABEL']._serialized_end=439
  _globals['_AGENTREPLY']._serialized_start=441
  _globals['_AGENTREPLY']._serialized_end=453
  _globals['_SYNCREQUEST']._serialized_start=455
  _globals['_SYNCREQUEST']._serialized_end=468
  _globals['_SYNCRESPONSE']._serialized_start=470
  _globals['_SYNCRESPONSE']._serialized_end=546
  _globals['_EVPNETHSEGIDPB']._serialized_start=548
  _globals['_EVPNETHSEGIDPB']._serialized_end=579
# @@protoc_insertion_point(module_scope)
