#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from netmiko import ConnectHandler

import sys
import time
import select
import paramiko
import re

platform = 'cisco_ios'
username = 'cisco'
password = 'cisco'
secret = 'cisco'

ip_add_file = open ("devices.txt") 

for host in ip_add_file:

    device = ConnectHandler(
                            device_type=platform, 
                            ip=host, 
                            username=username, 
                            password=password, 
                            secret=secret
                            )
    
    print ("Getting running-config " + (host))
    HOST = host.strip()
    device.enable()
    output = device.send_command_expect("show run")
    device.disconnect()

    saveoutput =  open(r"/home/osboxes/Desktop/Config_Comparison/configs/comparisons/" + HOST, "w")
    saveoutput.write(output)
    saveoutput.close 
    
