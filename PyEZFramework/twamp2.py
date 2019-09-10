from jnpr.junos import Device
from jnpr.junos.factory.factory_loader import FactoryLoader
import yaml

TWAMPTable = """
---
TWAMPTable:
    rpc: twamp-get-probe-results
    args:
        control-connection: "c1"
        test-session: "t1"
    item: probe-test-results
    view: TWAMPView
TWAMPView:
    fields:
        avg_delay: probe-test-global-results/probe-test-generic-results/probe-test-rtt/probe-summary-results/avg-delay
        jitter_delay: probe-test-global-results/probe-test-generic-results/probe-test-rtt/probe-summary-results/jitter-delay
"""

globals().update(FactoryLoader().load(yaml.load(TWAMPTable)))

with Device(host="ce1.simpledemo.net", user="root", passwd="Passw0rd") as dev:
    TWAMPS = TWAMPTable(dev)
    TWAMPS.get()

    for item in TWAMPS:
        print item.avg_delay
        print item.jitter_delay