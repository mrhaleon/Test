#!/usr/bin/env python
from __future__ import print_function, unicode_literals

# ConnectHandler
from netmiko import Netmiko
from getpass import getpass

net_conn = Netmiko(host="cisco1.twb-tech.com", username='pyclass', password=getpass(), device_type='cisco_ios')

print(net_conn.find_prompt())
