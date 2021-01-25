from getpass import getpass
import netmiko
import re

def make_connection (ip, username, password):
		return netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)

	
ips = []
    get_ips("devices.txt")

username = raw_input("Username: ")
password = getpass()

for ip in ips:
 net_connect = make_connection(ip, username, password)
 output = net_connect.send_command_expect('show ver')
 print(output)
 device.disconnect()