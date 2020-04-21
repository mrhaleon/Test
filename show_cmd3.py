#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

# Define dictionary with all the re-usable data for Netmiko calls in a single dictionary
my_device = {
        'host': "cisco1.twb-tech.com", 
        'username': 'pyclass', 
        'password': getpass(), 
        'device_type': 'cisco_ios'
}


net_conn = Netmiko(**my_device)

# Use send_command, but set expect string to look for a "#"
output = net_conn.send_command("show arp", expect_string=r'#')

print(output)
