from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

EthPortTable = """
---
EthPortTable:
  rpc: get-interface-information
  args:
    media: True
    interface_name: '[afgxe][et]-*'
  args_key: interface_name
  item: physical-interface
  view: EthPortView

EthPortView:
  groups:
    mac_stats: ethernet-mac-statistics
    flags: if-device-flags
  fields:
    oper: oper-status
    admin: admin-status
    description: description
    mtu: { mtu : int }
    link_mode: link-mode
    macaddr: current-physical-address
  fields_mac_stats:
    rx_bytes: input-bytes
    rx_packets: input-packets
    tx_bytes: output-bytes
    tx_packets: output-packets
  fields_flags:
    running: { ifdf-running: flag }
    present: { ifdf-present: flag }
"""

globals().update(FactoryLoader().load(yaml.load(EthPortTable)))

with Device(host="ce1.simpledemo.net", user="root", passwd="Passw0rd") as dev:
    eths = EthPortTable(dev)
    eths.get()
    for item in eths:
        print (item.name)
        print (item.oper)
        print (item.admin)
        print (item.mtu)
        print (item.rx_bytes)