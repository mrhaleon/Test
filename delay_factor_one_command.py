#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

# Define dictionary with all the re-usable data for Netmiko calls in a single dictionary
my_device = {
        'host': "nxos1.twb-tech.com", 
        'username': 'pyclass', 
        'password': getpass(), 
        'device_type': 'cisco_nxos'
}


net_conn = Netmiko(**my_device)

output = net_conn.send_command("copy run start", delay_factor=2)

print(output)
