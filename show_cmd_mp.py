#!/usr/bin/env python
from __future__ import print_function, unicode_literals

password = getpass()

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

# Define dictionary with all the re-usable data for Netmiko calls in a single dictionary
cisco1 = {
        'host': "cisco1.twb-tech.com", 
        'username': 'pyclass', 
        'password': password,
        'device_type': 'cisco_ios'
}


arista1 = {
        'host': "arista1.twb-tech.com", 
        'username': 'pyclass', 
        'password': password,
        'device_type': 'arista_eos'
}


juniper1 = {
        'host': "srx1.twb-tech.com", 
        'username': 'pyclass', 
        'password': password,
        'device_type': 'juniper_junos'
}


for device in (cisco1, arista1, srx1):
    net_conn = Netmiko(**device)
    output = net_conn.send_command("show ip arp")
    print(output)
