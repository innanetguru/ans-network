#!/usr/bin/python3

'''This plugin is intended for use with ansible jinja2 templating to generate
tunnel interface ID's dynamically yet predictively based on existing device state.  
The funcationlity of this plugin mirrors as closely as possible how
a network operator might perform these actions manually i.e. login to device,
check current interface definitions using cli, copy tunnel interface ID's to memory,
determine next tunnelID to use in upcoming/next vpn deployment, etc.  The plugin in
r1 currently only works with ansible_net_interfaces received from an ios_facts module run
as either a pre- or first task in a playbook run, but further iterations will include support
for multiple vendor appliance facts modules AND generic interface lists defintions in standard format
(json, yaml, etc).  Where you fetch or retrieve data regarding device state interface defintions
is ultimately an individual choice.

'''
import random
from ansible.errors import AnsibleError, AnsibleFilterError, AnsibleFilterTypeError

null=None #ansible_facts assings 'null' to empty dictionaries

class FilterModule(object):
    ''' Tunnel ID Generator filter'''

    def filters(self):
        return {
            'tunnelid': self.tunnelid

        }
    
    def tunnelid(self, interfaces, seed=None, step=None, start=1, end=2147483647):
        if not step:
            step = 1
        interface_list=list(interfaces.keys())
        tunnels=[]
        ids=[]
        #tunnelID=None
        ''' Discard PHYS interfaces and create list of tunnel interface names'''
        for i in interface_list:
            if i.startswith('Tun'):
                tunnels.append(i)
            else:
                tunnelID=r.randrange(start,end,step)
                tunnelID=str(tunnelID)
                return tunnelID
        '''split ID from 'tunnel' and convert to integer list'''  
        for t in tunnels:
            id=t.split('l')
            ids.append(id[1])
        ids=list(map(int, ids))
        '''Generate unique tunnelID and return'''
        if seed is not None:
            r = random.Random(seed)
            tunnelID=r.randrange(start,end,step)
        elif tunnelID in ids:
            seed = random.seed(a=seed + random.ranint(1, 1000000))
            

        while tunnelID in ids:
            if seed is None:
                seed = seed + random.randint(1,10000)
                r=random.Random(seed)
                tunnelID=r.randrange(start,end,step)
                if tunnelID in ids:
                    continue
            else:
                
        else:
            tunnelID=str(tunnelID)
            return tunnelID



''' tunnelid receives ansible_net_interfaces from ansible_facts:
  tasks:
    - name:  Gather Initial Interface Facts Pre-Deployment
      ios_facts:
        gather_subset: "interfaces"

    - name: Print Interfaces
      ansible.builtin.debug:
        msg: "tunnel{{ ansible_net_interfaces | tunnelid(seed=inventory_hostname, step=1, start=30, end=40) }}"
      #when: "'Tunnel22' not in ansible_net_interfaces"
      #loop: {{ somelist }}

  # example        
ansible_net_interfaces= {
        "GigabitEthernet0": {
            "bandwidth": 100000,
            "description": null,
            "duplex": "Full",
            "ipv4": [
                {
                    "address": "10.9.1.21",
                    "subnet": "24"
                }
            ],
            "lineprotocol": "up",
            "macaddress": "70db.985d.5bff",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "RP management port"
        },
        "GigabitEthernet0/0/0": {
            "bandwidth": 1000000,
            "description": "bp2-lfsw01-l001-Eth1/14",
            "duplex": "Full",
            "ipv4": [],
            "lineprotocol": "up",
            "macaddress": "70db.985d.5bb9",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "ISR4451-X-4x1GE"
        },
        "GigabitEthernet0/0/1": {
            "bandwidth": 1000000,
            "description": "bp2-lfsw01-l002-Eth1/14",
            "duplex": "Full",
            "ipv4": [],
            "lineprotocol": "up",
            "macaddress": "70db.985d.5bb9",
            "mediatype": "RJ45",
            "mtu": 1500,
            "operstatus": "up",
            "type": "ISR4451-X-4x1GE"
        },
        "GigabitEthernet0/0/2": {
            "bandwidth": 1000000,
            "description": "bp2-lfsw01-l001-Eth1/16",
            "duplex": "Full",
            "ipv4": [
                {
                    "address": "10.9.8.242",
                    "subnet": "30"
                }
            ],
            "lineprotocol": "up",
            "macaddress": "70db.985d.5b72",
            "mediatype": "RJ45",
            "mtu": 9050,
            "operstatus": "up",
            "type": "ISR4451-X-4x1GE"
        },
        "GigabitEthernet0/0/3": {
            "bandwidth": 1000000,
            "description": "bp2-lfsw01-l002-Eth1/16",
            "duplex": "Full",
            "ipv4": [
                {
                    "address": "10.9.8.246",
                    "subnet": "30"
                }
            ],
            "lineprotocol": "up",
            "macaddress": "70db.985d.5b73",
            "mediatype": "RJ45",
            "mtu": 9050,
            "operstatus": "up",
            "type": "ISR4451-X-4x1GE"
        },
        "Loopback5": {
            "bandwidth": 8000000,
            "description": "FOR_ROUTING_PROCESS",
            "duplex": null,
            "ipv4": [
                {
                    "address": "10.9.8.253",
                    "subnet": "32"
                }
            ],
            "lineprotocol": "up",
            "macaddress": null,
            "mediatype": null,
            "mtu": 1514,
            "operstatus": "up",
            "type": null
        },
        "Port-channel10": {
            "bandwidth": 2000000,
            "description": "bp2-lfsw01-l001-l002-Po (vPC)",
            "duplex": null,
            "ipv4": [
                {
                    "address": "204.90.140.69",
                    "subnet": "29"
                }
            ],
            "lineprotocol": "up",
            "macaddress": "70db.985d.5bb9",
            "mediatype": null,
            "mtu": 1500,
            "operstatus": "up",
            "type": "GEChannel"
        },
        "Tunnel10": {
            "bandwidth": 200000,
            "description": "DMVPN-DCI Tunnel Interface",
            "duplex": null,
            "ipv4": [
                {
                    "address": "10.129.8.2",
                    "subnet": "24"
                }
            ],
            "lineprotocol": "up",
            "macaddress": null,
            "mediatype": null,
            "mtu": 9972,
            "operstatus": "up",
            "type": null
        },
        "Tunnel20": {
            "bandwidth": 100,
            "description": null,
            "duplex": null,
            "ipv4": [
                {
                    "address": "169.254.0.6",
                    "subnet": "30"
                }
            ],
            "lineprotocol": "up",
            "macaddress": null,
            "mediatype": null,
            "mtu": 9938,
            "operstatus": "up",
            "type": null
        },
        "Tunnel21": {
            "bandwidth": 100,
            "description": null,
            "duplex": null,
            "ipv4": [
                {
                    "address": "169.254.15.166",
                    "subnet": "30"
                }
            ],
            "lineprotocol": "up",
            "macaddress": null,
            "mediatype": null,
            "mtu": 9938,
            "operstatus": "up",
            "type": null
        },
        "Tunnel30": {
            "bandwidth": 100,
            "description": null,
            "duplex": null,
            "ipv4": [
                {
                    "address": "169.254.160.78",
                    "subnet": "30"
                }
            ],
            "lineprotocol": "up",
            "macaddress": null,
            "mediatype": null,
            "mtu": 9922,
            "operstatus": "up",
            "type": null
        },
        "Tunnel40": {
            "bandwidth": 100,
            "description": null,
            "duplex": null,
            "ipv4": [
                {
                    "address": "169.254.253.50",
                    "subnet": "30"
                }
            ],
            "lineprotocol": "up",
            "macaddress": null,
            "mediatype": null,
            "mtu": 9922,
            "operstatus": "up",
            "type": null
        },
        "Tunnel90": {
            "bandwidth": 100,
            "description": "AZR-US-EAST",
            "duplex": null,
            "ipv4": [
                {
                    "address": "169.254.21.6",
                    "subnet": "30"
                }
            ],
            "lineprotocol": "up",
            "macaddress": null,
            "mediatype": null,
            "mtu": 9938,
            "operstatus": "up",
            "type": null
        }
    }
'''
