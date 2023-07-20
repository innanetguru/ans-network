#!/usr/bin/python3

DOCUMENTATION = r'''
---
module: libre_add_device
short_description: Add systems to Libre NMS monitoring application via web API
version_added: "1.0.0."
description: add new devices to LibreNMS via web API
options:
    url:
        description: Libre NMS API base URL for adding new devices
        required: true
        type: str
    hostname:
        description: hostname or IP address of device to add
        required: true
        type: str
    community:
        description: SNMP v1/2c community string 
        required: true
        type: str
    token:
        description: API token
        required: True
        type: str
    port:
        description: SNMP port
        required: false
        default: 161
        type: int
    snmpver:
        description: SNMP version
        required: false
        default: v2c
        type: str
author:
    - Dominic Giardina (innanetguru)
connection_type: local
notes:
    - Module will iterate through inventory hosts, adding each host to the NMS via the main function
    - Module handles connection establishment
'''
import json
from ansible.module_utils.urls import fetch_url
from ansible.module_utils.basic import AnsibleModule

def main():
    args = {
        "url": {"required": True, "type": "str"},
        "hostname":  {"required": True,"type": "str"},
        "community":  {"required":  True, "type": "str"},
        "token":  {"required": True, "type": "str"},
        "port":  {"required": False, "default": 161, "type": "int"},
        "snmpver":  {"required": False, "default": "v2c", "type": "str"}
}

    module = AnsibleModule(
        argument_spec=args,
        supports_check_mode=False
    )

    json_data = {
        "hostname": module.params['hostname'],
        "community": module.params['community'],
        "port": module.params['port'],
        "version": module.params['snmpver'],
    }

    headers = {
        "X-Auth-Token": module.params['token']
    }

    api = "{}/api/v0/devices".format(module.params['url'])

    resp, info = fetch_url(module, api, data=module.jsonify(json_data), headers=headers, method="POST",)

    result = {}

    if info['status'] == 201:
        result['changed'] = True
        response = json.loads(resp.read())
        #print(response)
        result['msg'] = response['message']
        module.exit_json(**result)
    elif info['status'] == 500:
        result['changed'] = False
        status = json.loads(info['body'])
        #print(status)
        result['msg'] = status['message']
        module.exit_json(**result)
    else:
        result['changed'] = False
        result['msg'] = 'Module Failure'
        module.fail_json(**result)

if __name__ == '__main__':
    main()