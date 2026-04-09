import requests
import json

def csr_int_conf(csr_url, csr_creds, csr_headers):
    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface IP address: ")
    int_mask = input("Enter the interface subnet mask: ")
    int_desc = input("Enter the interface description: ")

    int_payload = {
        "interface":{
            "name": int_name,
            "description": int_desc, 
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
            "address": [
                { 
                "ip": int_ip,
                "netmask": int_mask
                }
            ]
            },
            "ietf-ip:ipv6": {
            }
        }
    }

    int_conf = requests.post(url = csr_url, auth = csr_creds, headers = csr_headers, data = json.dumps(int_payload), verify = False)

    print(int_conf.status_code)
    print(int_conf.text)

def asa_int_conf(asa_url, asa_creds, asa_headers):
    int_name = input("Enter the interface name: ")
    int_ip = input("Enter the interface IP address: ")
    int_mask = input("Enter the interface subnet mask: ")
    int_desc = input("Enter the interface description: ")
    int_zone = input("Enter the interface zone name: ")

    int_payload = {
    "securityLevel": 100,
    "kind": "object#GigabitInterface",
    "channelGroupMode": "active",
    "flowcontrolLow": -1,
    "name": int_zone,
    "duplex": "auto",
    "forwardTrafficSFR": False,
    "hardwareID": int_name,
    "mtu": 1500,
    "lacpPriority": -1,
    "flowcontrolHigh": -1,
    "ipAddress": {
        "ip": {
        "kind": "IPv4Address",
        "value": int_ip
        },
        "kind": "StaticIP",
        "netMask": {
        "kind": "IPv4NetMask",
        "value": int_mask
        }
    },
    "flowcontrolOn": False,
    "shutdown": False,
    "interfaceDesc": int_desc,
    "managementOnly": False,
    "channelGroupID": "",
    "speed": "auto",
    "forwardTrafficCX": False,
    "flowcontrolPeriod": -1
    }

    int_conf = requests.put(url = asa_url, auth = asa_creds, headers = asa_headers, data = json.dumps(int_payload), verify = False)

    print(int_conf.status_code)

    
 
 
