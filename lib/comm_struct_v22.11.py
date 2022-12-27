import collections
from enum import Enum, unique
from sqlite3 import collections

@unique
class rte_flow_item_type(Enum):
    RTE_FLOW_ITEM_TYPE_END      = 0
    RTE_FLOW_ITEM_TYPE_VOID     = 1
    RTE_FLOW_ITEM_TYPE_INVERT   = 2
    RTE_FLOW_ITEM_TYPE_ANY      = 3
    RTE_FLOW_ITEM_TYPE_RAW      = 5
    RTE_FLOW_ITEM_TYPE_ETH      = 6
    RTE_FLOW_ITEM_TYPE_VLAN     = 7
    RTE_FLOW_ITEM_TYPE_IPV4     = 8
    RTE_FLOW_ITEM_TYPE_IPV6     = 9
    RTE_FLOW_ITEM_TYPE_ICMP     = 10
    RTE_FLOW_ITEM_TYPE_UDP      = 11
    RTE_FLOW_ITEM_TYPE_TCP      = 12
    RTE_FLOW_ITEM_TYPE_SCTP     = 13
    RTE_FLOW_ITEM_TYPE_VXLAN    = 14
    RTE_FLOW_ITEM_TYPE_E_TAG    = 15
    RTE_FLOW_ITEM_TYPE_NVGRE    = 16
    RTE_FLOW_ITEM_TYPE_MPLS     = 17
    RTE_FLOW_ITEM_TYPE_GRE      = 18
    RTE_FLOW_ITEM_TYPE_FUZZY    = 19
    RTE_FLOW_ITEM_TYPE_GTP      = 20
    RTE_FLOW_ITEM_TYPE_GTPC     = 21
    RTE_FLOW_ITEM_TYPE_GTPU     = 22
    RTE_FLOW_ITEM_TYPE_ESP      = 23
    RTE_FLOW_ITEM_TYPE_GENEVE   = 24
    RTE_FLOW_ITEM_TYPE_VXLAN_GPE= 25
    RTE_FLOW_ITEM_TYPE_ARP_ETH_IPV4 = 26
    RTE_FLOW_ITEM_TYPE_IPV6_EXT = 27
    RTE_FLOW_ITEM_TYPE_ICMP6    = 28
    RTE_FLOW_ITEM_TYPE_ICMP6_ND_NS=29
    RTE_FLOW_ITEM_TYPE_ICMP6_ND_NA=30
    RTE_FLOW_ITEM_TYPE_ICMP6_ND_OPT=31
    RTE_FLOW_ITEM_TYPE_ICMP6_ND_OPT_SLA_ETH=32
    RTE_FLOW_ITEM_TYPE_ICMP6_ND_OPT_TLA_ETH=33
    RTE_FLOW_ITEM_TYPE_MARK     = 34
    RTE_FLOW_ITEM_TYPE_META     = 35
    RTE_FLOW_ITEM_TYPE_GRE_KEY  = 36
    RTE_FLOW_ITEM_TYPE_GTP_PSC  = 37
    RTE_FLOW_ITEM_TYPE_PPPOES   = 38
    RTE_FLOW_ITEM_TYPE_PPPOED   = 39
    RTE_FLOW_ITEM_TYPE_PPPOE_PROTO_ID= 40
    RTE_FLOW_ITEM_TYPE_NSH      = 41
    RTE_FLOW_ITEM_TYPE_IGMP     = 42
    RTE_FLOW_ITEM_TYPE_AH       = 43
    RTE_FLOW_ITEM_TYPE_HIGIG2   = 44
    RTE_FLOW_ITEM_TYPE_TAG      = 45
    RTE_FLOW_ITEM_TYPE_PORT_REPRESENTOR = 53
    RTE_FLOW_ITEM_TYPE_REPRESENTED_PORT = 54

@unique
class rte_flow_action_type(Enum):
    RTE_FLOW_ACTION_TYPE_END        = 0
    RTE_FLOW_ACTION_TYPE_VOID       = 1
    RTE_FLOW_ACTION_TYPE_PASSTHRU   = 2
    RTE_FLOW_ACTION_TYPE_JUMP       = 3
    RTE_FLOW_ACTION_TYPE_MARK       = 4
    RTE_FLOW_ACTION_TYPE_FLAG       = 5
    RTE_FLOW_ACTION_TYPE_QUEUE      = 6
    RTE_FLOW_ACTION_TYPE_DROP       = 7
    RTE_FLOW_ACTION_TYPE_COUNT      = 8
    RTE_FLOW_ACTION_TYPE_RSS        = 9
    RTE_FLOW_ACTION_TYPE_METER      = 13
    RTE_FLOW_ACTION_TYPE_SECURITY   = 14
    RTE_FLOW_ACTION_TYPE_OF_DEC_NW_TTL = 15
    RTE_FLOW_ACTION_TYPE_OF_POP_VLAN = 16
    RTE_FLOW_ACTION_TYPE_OF_PUSH_VLAN = 17
    RTE_FLOW_ACTION_TYPE_OF_SET_VLAN_VID = 18
    RTE_FLOW_ACTION_TYPE_OF_SET_VLAN_PCP = 19
    RTE_FLOW_ACTION_TYPE_OF_POP_MPLS    = 20
    RTE_FLOW_ACTION_TYPE_OF_PUSH_MPLS   = 21
    RTE_FLOW_ACTION_TYPE_VXLAN_ENCAP    = 22
    RTE_FLOW_ACTION_TYPE_VXLAN_DECAP    = 23
    RTE_FLOW_ACTION_TYPE_NVGRE_ENCAP    = 24
    RTE_FLOW_ACTION_TYPE_NVGRE_DECAP    = 25
    RTE_FLOW_ACTION_TYPE_RAW_ENCAP      = 26
    RTE_FLOW_ACTION_TYPE_RAW_DECAP      = 27
    RTE_FLOW_ACTION_TYPE_SET_IPV4_SRC   = 28
    RTE_FLOW_ACTION_TYPE_SET_IPV4_DST   = 29
    RTE_FLOW_ACTION_TYPE_SET_IPV6_SRC   = 30
    RTE_FLOW_ACTION_TYPE_SET_IPV6_DST   = 31
    RTE_FLOW_ACTION_TYPE_SET_TP_SRC     = 32
    RTE_FLOW_ACTION_TYPE_SET_TP_DST     = 33
    RTE_FLOW_ACTION_TYPE_MAC_SWAP       = 34
    RTE_FLOW_ACTION_TYPE_DEC_TTL        = 35
    RTE_FLOW_ACTION_TYPE_SET_TTL        = 36
    RTE_FLOW_ACTION_TYPE_SET_MAC_SRC    = 37
    RTE_FLOW_ACTION_TYPE_SET_MAC_DST    = 38
    RTE_FLOW_ACTION_TYPE_INC_TCP_SEQ    = 39
    RTE_FLOW_ACTION_TYPE_DEC_TCP_SEQ    = 40
    RTE_FLOW_ACTION_TYPE_INC_TCP_ACK    = 41
    RTE_FLOW_ACTION_TYPE_DEC_TCP_ACK    = 42
    RTE_FLOW_ACTION_TYPE_SET_TAG        = 43
    RTE_FLOW_ACTION_TYPE_SET_META       = 44
    RTE_FLOW_ACTION_TYPE_REPRESENTED_PORT = 55