#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

# Have user input the password once and store as a variable - same value for password and secret
password = getpass()

# Define dictionary with all the re-usable data for Netmiko calls in a single dictionary
my_device = {
        'host': "cisco1.twb-tech.com", 
        'username': 'pyclass', 
        'password': password
        'secret': password
        'device_type': 'cisco_ios'
}


net_conn = Netmiko(**my_device)
net_conn.enable()
print(net_conn.find_prompt())
