# Automation Roadshow 101

This README contains information to experiment with Junos alongside automation discussions and workshops.

Use [this](https://hub.docker.com/r/davidjohngee/juniper-gitlab-container/) Docker container as a base of operations and mount this directory as a volume for the container.

Also do not forget to add the SSH key used for this demonstration to the container so that the tools can reach the virtual node remotely.

```bash
docker pull davidjohngee/juniper-gitlab-container:latest
docker run -d --name demo01 davidjohngee/juniper-gitlab-container
docker exec -it demo01 bash
```

## WorkflowIO

Checkout branch one: workflowIO_basics.

```bash
git checkout workflowIO_basics
```

From 12.4, Junos has supported JSON as an output type. XML has been built in from day one and should not be viewed as simple, dated or antiquated. It is feature rich and provides many capabilities.

```bash
# Task one
ssh demo@NODENAME
> show route table VR1.inet.0
VR1.inet.0: 4 destinations, 4 routes (4 active, 0 holddown, 0 hidden)
+ = Active Route, - = Last Active, * = Both

172.16.0.0/30      *[Direct/0] 01:04:54
                    > via ge-0/0/0.0
172.16.0.1/32      *[Local/0] 01:04:54
                      Local via ge-0/0/0.0
192.168.1.1/32     *[Direct/0] 01:04:54
                    > via lo0.10
192.168.1.2/32     *[IS-IS/18] 00:49:33, metric 1
                    > to 172.16.0.2 via ge-0/0/0.0
```

Easy for a human to read, but not a machine. If wanted to use any of this data in a mechanized process, we would have to parse it using word tokens and hope for the best! 

Let's try getting JSON or XML out of the system.

```bash
> show route table VR1.inet.0 | display json
{
    "route-information" : [
    {
        "attributes" : {"xmlns" : "http://xml.juniper.net/junos/18.3R1/junos-routing"},
        "route-table" : [
        {
            "comment" : "keepalive",
            "table-name" : [
            {
                "data" : "VR1.inet.0"
            }
            ],
            "destination-count" : [
            {
                "data" : "4"
            }
            ],
            "total-route-count" : [
            {
                "data" : "4"
            }
            ],
            "active-route-count" : [
            {
                "data" : "4"
            }
            ],
            "holddown-route-count" : [
            {
                "data" : "0"
            }
            ],
            "hidden-route-count" : [
            {
                "data" : "0"
            }
            ],
            "rt" : [
            {
                "attributes" : {"junos:style" : "brief"},
                "rt-destination" : [
                {
                    "data" : "172.16.0.0/30"
                }
                ],
                "rt-entry" : [
                {
                    "active-tag" : [
                    {
                        "data" : "*"
                    }
                    ],
                    "current-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "last-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "protocol-name" : [
                    {
                        "data" : "Direct"
                    }
                    ],
                    "preference" : [
                    {
                        "data" : "0"
                    }
                    ],
                    "age" : [
                    {
                        "data" : "01:06:37",
                        "attributes" : {"junos:seconds" : "3997"}
                    }
                    ],
                    "nh" : [
                    {
                        "selected-next-hop" : [
                        {
                            "data" : [null]
                        }
                        ],
                        "via" : [
                        {
                            "data" : "ge-0/0/0.0"
                        }
                        ]
                    }
                    ]
                }
                ]
            },
            {
                "attributes" : {"junos:style" : "brief"},
                "rt-destination" : [
                {
                    "data" : "172.16.0.1/32"
                }
                ],
                "rt-entry" : [
                {
                    "active-tag" : [
                    {
                        "data" : "*"
                    }
                    ],
                    "current-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "last-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "protocol-name" : [
                    {
                        "data" : "Local"
                    }
                    ],
                    "preference" : [
                    {
                        "data" : "0"
                    }
                    ],
                    "age" : [
                    {
                        "data" : "01:06:37",
                        "attributes" : {"junos:seconds" : "3997"}
                    }
                    ],
                    "nh-type" : [
                    {
                        "data" : "Local"
                    }
                    ],
                    "nh" : [
                    {
                        "nh-local-interface" : [
                        {
                            "data" : "ge-0/0/0.0"
                        }
                        ]
                    }
                    ]
                }
                ]
            },
            {
                "attributes" : {"junos:style" : "brief"},
                "rt-destination" : [
                {
                    "data" : "192.168.1.1/32"
                }
                ],
                "rt-entry" : [
                {
                    "active-tag" : [
                    {
                        "data" : "*"
                    }
                    ],
                    "current-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "last-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "protocol-name" : [
                    {
                        "data" : "Direct"
                    }
                    ],
                    "preference" : [
                    {
                        "data" : "0"
                    }
                    ],
                    "age" : [
                    {
                        "data" : "01:06:37",
                        "attributes" : {"junos:seconds" : "3997"}
                    }
                    ],
                    "nh" : [
                    {
                        "selected-next-hop" : [
                        {
                            "data" : [null]
                        }
                        ],
                        "via" : [
                        {
                            "data" : "lo0.10"
                        }
                        ]
                    }
                    ]
                }
                ]
            },
            {
                "attributes" : {"junos:style" : "brief"},
                "rt-destination" : [
                {
                    "data" : "192.168.1.2/32"
                }
                ],
                "rt-entry" : [
                {
                    "active-tag" : [
                    {
                        "data" : "*"
                    }
                    ],
                    "current-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "last-active" : [
                    {
                        "data" : [null]
                    }
                    ],
                    "protocol-name" : [
                    {
                        "data" : "IS-IS"
                    }
                    ],
                    "preference" : [
                    {
                        "data" : "18"
                    }
                    ],
                    "age" : [
                    {
                        "data" : "00:51:16",
                        "attributes" : {"junos:seconds" : "3076"}
                    }
                    ],
                    "metric" : [
                    {
                        "data" : "1"
                    }
                    ],
                    "nh" : [
                    {
                        "selected-next-hop" : [
                        {
                            "data" : [null]
                        }
                        ],
                        "to" : [
                        {
                            "data" : "172.16.0.2"
                        }
                        ],
                        "via" : [
                        {
                            "data" : "ge-0/0/0.0"
                        }
                        ]
                    }
                    ]
                }
                ]
            }
            ]
        }
        ]
    }
    ]
}
```

Ok, so lots of useable data here. What about XML?

```bash
> show route table VR1.inet.0 | display xml

<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.3R1/junos">
    <route-information xmlns="http://xml.juniper.net/junos/18.3R1/junos-routing">
        <!-- keepalive -->
        <route-table>
            <table-name>VR1.inet.0</table-name>
            <destination-count>4</destination-count>
            <total-route-count>4</total-route-count>
            <active-route-count>4</active-route-count>
            <holddown-route-count>0</holddown-route-count>
            <hidden-route-count>0</hidden-route-count>
            <rt junos:style="brief">
                <rt-destination>172.16.0.0/30</rt-destination>
                <rt-entry>
                    <active-tag>*</active-tag>
                    <current-active/>
                    <last-active/>
                    <protocol-name>Direct</protocol-name>
                    <preference>0</preference>
                    <age junos:seconds="4060">01:07:40</age>
                    <nh>
                        <selected-next-hop/>
                        <via>ge-0/0/0.0</via>
                    </nh>
                </rt-entry>
            </rt>
            <rt junos:style="brief">
                <rt-destination>172.16.0.1/32</rt-destination>
                <rt-entry>
                    <active-tag>*</active-tag>
                    <current-active/>
                    <last-active/>
                    <protocol-name>Local</protocol-name>
                    <preference>0</preference>
                    <age junos:seconds="4060">01:07:40</age>
                    <nh-type>Local</nh-type>
                    <nh>
                        <nh-local-interface>ge-0/0/0.0</nh-local-interface>
                    </nh>
                </rt-entry>
            </rt>
            <rt junos:style="brief">
                <rt-destination>192.168.1.1/32</rt-destination>
                <rt-entry>
                    <active-tag>*</active-tag>
                    <current-active/>
                    <last-active/>
                    <protocol-name>Direct</protocol-name>
                    <preference>0</preference>
                    <age junos:seconds="4060">01:07:40</age>
                    <nh>
                        <selected-next-hop/>
                        <via>lo0.10</via>
                    </nh>
                </rt-entry>
            </rt>
            <rt junos:style="brief">
                <rt-destination>192.168.1.2/32</rt-destination>
                <rt-entry>
                    <active-tag>*</active-tag>
                    <current-active/>
                    <last-active/>
                    <protocol-name>IS-IS</protocol-name>
                    <preference>18</preference>
                    <age junos:seconds="3139">00:52:19</age>
                    <metric>1</metric>
                    <nh>
                        <selected-next-hop/>
                        <to>172.16.0.2</to>
                        <via>ge-0/0/0.0</via>
                    </nh>
                </rt-entry>
            </rt>
        </route-table>
    </route-information>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```

Ignoring the opening and closing chevrons, XML contains enriched data that JSON does not. It's also more compact thanks to the lack of curly braces.

Junos was built from the ground up with this technology in mind and we don't have to do any horrid CLI scraping!

You may have noticed this is a little weird. As a human I can login to the CLI and ask Junos for machine encoded data. So what if I'm a machine and want to get the data? How do we do that?

The NETCONF protocol allows us to get information back currently encoded in XML and modelled by YANG. Let's do a simple hello to Junos and set up our transport channel.

Junos supports RFC6241 and RFC4741 for NETCONF and RFC6020 for YANG. Junos by default isn't RFC compliant, but it can be made to behave that way with a simple configuration switch.

```bash
set system services netconf rfc-compliant
```

We're going to connect via NETCONF to Junos and have a conversation. First, we must configure NETCONF to be available over SSH.

```bash
set system services netconf ssh
commit
```

Ok, let's setup a NETCONF transport and handle some simple XML.

```bash
# Junos says hello here
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:candidate:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:confirmed-commit:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:validate:1.0</capability>
    <capability>urn:ietf:params:netconf:capability:url:1.0?scheme=http,ftp,file</capability>
    <capability>urn:ietf:params:xml:ns:netconf:base:1.0</capability>
    <capability>urn:ietf:params:xml:ns:netconf:capability:candidate:1.0</capability>
    <capability>urn:ietf:params:xml:ns:netconf:capability:confirmed-commit:1.0</capability>
    <capability>urn:ietf:params:xml:ns:netconf:capability:validate:1.0</capability>
    <capability>urn:ietf:params:xml:ns:netconf:capability:url:1.0?protocol=http,ftp,file</capability>
    <capability>urn:ietf:params:xml:ns:yang:ietf-netconf-monitoring</capability>
    <capability>http://xml.juniper.net/netconf/junos/1.0</capability>
    <capability>http://xml.juniper.net/dmi/system/1.0</capability>
  </capabilities>
  <session-id>10951</session-id>
</hello>
]]>]]>

# We can say hello back quite simply
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <capabilities>
    <capability>urn:ietf:params:netconf:base:1.0</capability>
    <capability>urn:ietf:params:xml:ns:netconf:base:1.0</capability>
  </capabilities>
</hello>
]]>]]>
```

At this point, we now have a machine communication channel open with Junos and we can instantiate NETCONF operations like "\<get\>" and "\<edit\>" as we see fit.

```bash
<rpc>
    <get-route-information>
            <table>VR1</table>
    </get-route-information>
</rpc>
```

Note how our request has to be wrapped in an `<rpc>` element.

Secondly, you're probably wondering, how to find this RPC call information?

```bash
> show route table VR1.inet.0 | display xml rpc
<rpc-reply xmlns:junos="http://xml.juniper.net/junos/18.3R1/junos">
    <rpc>
        <get-route-information>
                <table>VR1</table>
        </get-route-information>
    </rpc>
    <cli>
        <banner></banner>
    </cli>
</rpc-reply>
```

Ignore the CLI information and `<rpc-reply>` elements; we're just interested in the actual `<rpc>` XML envelope.

What about JSON? It's possible to return JSON via NETCONF or via the REST interface. Developers tend to stick with what they know and developers find JSON a natural buddy to REST.

To retrieve JSON from NETCONF, just add `format="json"` to the RPC call like so.

```bash
<rpc>
    <get-route-information format="json">
            <table>VR1</table>
    </get-route-information>
</rpc>]]>]]>
```

Next we'll discover an alternative way to get JSON out of Junos by enabling the HTTP based REST server and the explorer web component which allows us to use a browser to explore the Junos REST interface.

```bash
set system services rest enable-explorer http port 8080
commit
```

Open a browser and point it to the IP address of the test node to the port and try the same thing again. You can also use CURL like below.

Note, with REST, it's important that you provide query parameters if for instance you want a data object sub-item, in this example that would be the contents of a specific route table.

```bash
curl http://demo01.ipengineer.net:8080/rpc/get-route-information?table=VR1.inet.0 -u "demo:Passw0rd" -H "Content-Type: application/xml" -H "Accept: application/json"
```

Up to now, you've seen XML and JSON, but no YAML.

YAML is best placed for configuration due to its easy nature to read.

## Basic Configuration Tasks with YAML & Templates

The automation world is alive and vibrant right now with the most simple things achieveing great results. One of those things is template based configuration and 99% of what a tool like Ansible is used for.

Weirdly, we're still using machine based tools to generate human readable configuration. This generated configuration is then merged on to the platform. Engineers like to be able to understand and read what's going on, so this shouldn't be a surprise.

In the `PythonJ2Example` directory there are two files called `demo01.config.template_01.j2` and `demo01.config.variables_01.yaml`. J2 is a file extension reserved for Jinja2 templates, the most recognisable automation templating type used with Python and Ansible. Note,`.yaml` or `.yml` extensions are reserved for files containing YAML.

We are going to generate a configuration snippet from running a template render process on our template with the variables as input.

```bash
cat demo01.config.template_01.j2
# File containing variables for interface config
interfaces {
    {{ interface }} {
        unit {{ unit }} {
            description {{ description }};
        }
    }
}


cat demo01.config.variables_1.yaml
# File containing variables for interface config
interface: ge-0/0/3
unit: 0
description: "cpe"
```

Here is a basic Python script which will render the template with the variables.

```python
# Simple Python script to load template, load variables and render
from jinja2 import Environment, FileSystemLoader

import yaml,sys,os

stream = file(sys.argv[1], 'r')

config_data = yaml.load(stream)

env = Environment(loader = FileSystemLoader(os.path.dirname(os.path.abspath(__file__))), trim_blocks=True, lstrip_blocks=True)
template = env.get_template(sys.argv[2])

print(template.render(config_data))
```

To call the code, you will require Python installed, with libraries jinja2 and the standard system libraries.

```bash
$ python demo01.py demo01.config.variables_01.yaml demo01.config.template_01.j2
# File containing variables for interface config
interfaces {
    ge-0/0/3 {
        unit 0 {
            description cpe;
        }
    }
}
```

Quite possibly the easiest template task of all time!

In other languages, templating modules of course exist. For Go, there is Moustache and for Java there are Velocity templates. Some of these languages also have bindings for J2. Try not to get trapped with Python, Ansible and J2. They're just a language, a tool and a template kind.

So, as the favourite go to tool for most engineers, Ansible would normally be used for this instead of a code call. Ansible along with being able to generate snippets from templates, can also push configuration to devices amongst other things. 

## Ansible Equivalent

Under the Ansible directory in this repository is everything required to carry this task out minus the setup of host keys/auth etc. Traverse to the AnsibleExample directory and run the Check playbook, followed by the template playbook.

```bash
ansible-playbook pb.template.yml --extra-vars target=demo01
ansible-playbook pb.check_connect.yml --extra-vars target=demo01
```

If your host file is setup correctly and you've loaded they .ssh key (I suggest you generate a new one with `ssh-keygen`), you should have a new `facts` and `inventory` file along with a file containing interface configuration!

## Ansible Extras

Ansible can be used for much more than just templating configuration and part of the ease of the tool is through the use of roles. A role in our case is `Juniper.junos` which allows us to do a number of actions against a Junos target, including pushing configuration and checking syntax before any run of playbooks like below:

```bash
ansible-playbook pb.template.yml --extra-vars target=demo01 --syntax-check
```













