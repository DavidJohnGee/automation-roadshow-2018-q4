## README

This Robot test queries the REST API on a Juniper vMX (tested with 18.1).

Install Robot and build Junos with enough configuration for the test to work. The vMX will require two data-plane interfaces for this to work! Here is some configuration which will help. Ensure you set the demo user password to something you will remember.

```bash
set system login user demo uid 2000
set system login user demo class super-user
set system host-name demo01
set system domain-name ipengineer.net
set system services ssh root-login allow
set system services extension-service request-response grpc clear-text port 50051
set system services extension-service notification port 1883
set system services extension-service notification allow-clients address 0.0.0.0/0
set system services netconf ssh
set system services rest http port 8080
set system services rest enable-explorer
set system syslog user * any emergency
set system syslog file messages any notice
set system syslog file messages authorization info
set system syslog file interactive-commands interactive-commands any
set system processes dhcp-service traceoptions file dhcp_logfile
set system processes dhcp-service traceoptions file size 10m
set system processes dhcp-service traceoptions level all
set system processes dhcp-service traceoptions flag packet
set chassis fpc 0 lite-mode
set chassis fpc 0 number-of-ports 8
set interfaces ge-0/0/0 unit 0 description "(VR1)<-Eth-> VR2"
set interfaces ge-0/0/0 unit 0 family inet address 172.16.0.1/30
set interfaces ge-0/0/0 unit 0 family inet address 10.0.0.10/24
set interfaces ge-0/0/0 unit 0 family iso
set interfaces ge-0/0/1 unit 0 description "(VR2)<-Eth-> VR1"
set interfaces ge-0/0/1 unit 0 family inet address 172.16.0.2/30
set interfaces ge-0/0/1 unit 0 family iso
set interfaces fxp0 unit 0 family inet address 81.138.165.211/29
set interfaces lo0 unit 10 description "VR1 routerid"
set interfaces lo0 unit 10 family inet address 192.168.1.1/32
set interfaces lo0 unit 10 family iso address 49.0001.0000.0000.0001.00
set interfaces lo0 unit 11 description "VR2 routerid"
set interfaces lo0 unit 11 family inet address 192.168.1.2/32
set interfaces lo0 unit 11 family iso address 49.0001.0000.0000.0002.00
set routing-options static route 0.0.0.0/0 next-hop 81.138.165.214
set routing-options autonomous-system 64532
set routing-options programmable-rpd purge-timeout 10
set protocols bgp group internal type internal
set protocols bgp group internal family inet unicast add-path send path-count 6
set protocols bgp group internal allow 0.0.0.0/0
set policy-options policy-statement ISIS_EXPORT from protocol direct
set policy-options policy-statement ISIS_EXPORT then accept
set routing-instances VR1 instance-type virtual-router
set routing-instances VR1 interface ge-0/0/0.0
set routing-instances VR1 interface lo0.10
set routing-instances VR1 routing-options router-id 192.168.1.1
set routing-instances VR1 protocols isis level 1 disable
set routing-instances VR1 protocols isis level 2 wide-metrics-only
set routing-instances VR1 protocols isis interface ge-0/0/0.0 level 2 metric 1
set routing-instances VR1 protocols isis interface lo0.10
set routing-instances VR2 instance-type virtual-router
set routing-instances VR2 interface ge-0/0/1.0
set routing-instances VR2 interface lo0.11
set routing-instances VR2 routing-options router-id 192.168.1.2
set routing-instances VR2 protocols isis level 1 disable
set routing-instances VR2 protocols isis level 2 wide-metrics-only
set routing-instances VR2 protocols isis interface ge-0/0/1.0 level 2 metric 1
set routing-instances VR2 protocols isis interface lo0.11
```


