#!/usr/bin/python3

import requests as req
import pandas as pd
import xlwings as xw
import json 
import getpass
import traceback, sys

IB_WAPI_VER="2.11.5"

def get_subnets(url="infoblox.otxlab.net", data=None):
    return 

def get_vlans(url="infoblox.otxlab.net", data=None):
    return

def post_resources():
    return

def main():
    print("Enter your infoblox username:")
    username = input('username:')
    print("Enter infoblox your password")
    password = getpass.getpass()
    wb = xw.Book.caller()
    df = pd.read_csv(r"C:\Users\dgiardin\Desktop\projects\ans-network-cloud\network_build_sheet.csv")
    for vlan in df['VLAN']:
        print(vlan)
    wb.sheets[0].range('L1').value = 'TEST'
    return print('infoblox WAPI version:', IB_WAPI_VER)

if __name__ == '__main__':
    main()