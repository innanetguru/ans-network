#!/usr/bin/python

"""
This script is for declaring a new vlan_id for a new lab network request.
The script will make a RESTful API call to LibreNMS where all network device 
configuration and state data is contained and determine a vlan_id that is available.

"""
import requests
import json
import getpass 
import random 
import yaml 
from ansible.module_utils.basic import *

user=raw_input('username:')
token=getpass.getpass() #b6d91f0b35105993a2830fd4083d43cd
hostname=raw_input('Enter the hostname of the switch you wish to check: ')
#requester_input=open("request_data.yaml")

class VlanGenerator():
    pass


def set_vlan(used_vlans):
    vlans=[]
    requester_input=open("request_data.yaml")
    config_data=yaml.load(requester_input)
    while len(vlans) != len(config_data['subnets']):
        vlan=random.randrange(2,4096)
        if vlan in used_vlans: 
            continue
        else: 
            vlans.append(vlan)
            

    print(vlans)
    return 

def vlan_pool(vlan_list):
    id_pool=[]

    for vlan in vlan_list:
        id_pool.append(vlan['vlan_vlan'])

    #print(len(id_pool))
    #print(id_pool)
    return set_vlan(id_pool)

def libre_api(device):
    endpoints="http://bp2-librenms.otxlab.net/api/v0/devices/"+device+"/vlans"
    headers = {
        "X-Auth-Token": token
    }
    response=requests.get(endpoints,headers=headers)
    vlan_db=response.json().get('vlans')
    return vlan_pool(vlan_db)

def main():
    libre_api(hostname) 

if __name__ =="__main__":
    main()
