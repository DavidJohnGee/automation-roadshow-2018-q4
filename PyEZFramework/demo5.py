import sys
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

config = {
    'interfaces': ['ge-0/0/0.0', 'ge-0/0/1.0'],
    'family': 'mpls'
}

hostname = input("Device hostname: ")
username = input("Device username: ")
password = getpass("Device password: ")

dev = Device(host=hostname, user=username, passwd=password).open()
with Config(dev, mode='private') as cu:
    conf_file = "configs/junos-config-interfaces-mpls.conf"
    cu.load(template_path=conf_file, template_vars=config, merge=True)

    cu.pdiff()
    cu.commit()

sys.exit(0)
