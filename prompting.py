#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# This script will delete a file from a router, showing how to handle prompts for additional input in response to commands

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

# Open Connection handler
net_conn = Netmiko(**my_device)

# Filename that we are deleting from a router
filename = "small_file_bim.txt"

# Command to delete the file
cmd = "delete flash:{}".format(filename)

# Use send_command_timing to look for a "confirm" prompt after a set period of time and issue an additional command (new line in this case) if it is there
output = net_conn.send_command_timing(cmd)
if 'confirm' in output:
        output += net_conn.send_command_timing("\n")

# Gracefully disconnect connection
net_conn.disconnect()

# Print the output
print(output)
