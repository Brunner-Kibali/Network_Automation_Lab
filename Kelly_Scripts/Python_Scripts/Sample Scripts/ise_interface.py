#!/usr/bin/env python
from netmiko import ConnectHandler
from getpass import getpass
from ciscoconfparse import CiscoConfParse

device = { 
    'device_type': 'cisco_ios',
    'ip': '10.1.1.12',
    'username': 'cisco',
    'password': getpass(),
} 

net_connect = ConnectHandler(**device)
net_connect.enable()
#print(net_connect.find_prompt())

run_config = net_connect.send_command("show run")
#run_config = run_config.splitlines()
print(run_config)
#cisco_cfg = CiscoConfParse(run_config)
#cisco_cfg = CiscoConfParse("cisco.cfg")
#config_obj = cisco_cfg.find_objects_w_all_children(parentspec=r"^interface",
                                                  #childspec=[r"authentication order dot1x mab",
                                                            # r"authentication order mab dot1x"])
for parent in config_obj:
    print(parent.text)
    mab_line = parent.re_search_children(r"authentication order mab dot1x")[0].linenum
    dot1x_line = parent.re_search_children(r"authentication order dot1x mab")[0].linenum
    # Check if mab_line comes later
    if mab_line > dot1x_line:
        print("Found")
        print(parent.text)