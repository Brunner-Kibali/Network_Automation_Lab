#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from netmiko import ConnectHandler

import sys
import time
import select
import paramiko
import re
import getpass
import logging

logging.basicConfig(filename='test.log', level=logging.INFO)
logger = logging.getLogger("netmiko")

platform = 'cisco_ios'
username = 'cisco'
password = getpass.getpass()


ip_add_file = open ("devices.txt") 

for host in ip_add_file:

    device = ConnectHandler(
                            device_type=platform, 
                            ip=host, 
                            username=username, 
                            password=password
                            )
    
    print ("Getting running-config " + (host))
    HOST = host.strip()
    logger.info('%s has been successfully configured', device)
    device.enable()
    output = device.send_command("show run | in snmp")
    #print(output)
    device.disconnect()

    saveoutput =  open(r"" + HOST, "w")
    saveoutput.write(output)
    saveoutput.close 
    

