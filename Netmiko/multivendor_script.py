from netmiko import ConnectHandler

multiple_device = ["192.168.32.191", "192.168.32.200"]

for device in multiple_device:
    cisco_devices123 = {
        "device_type": "cisco_ios",
        "ip": device,
        "username": input("enter your username for " + device + ": "),
        "password": input("enter your password for " + device + ": "),
        "port": 22
    }

connection123 = ConnectHandler(**cisco_devices123)

print("#" * 25 + "Connecting to Cisco_IOS " + device + "#" * 25)

# ssh
output123 = connection123.send_command("show ip int br")
print(output123)

# save
location = "/home/brunner/PycharmProjects/Network-Automation-Labs/customerxyz//backup_"
saveoutput123 = open(location + device + ".txt", "w")
saveoutput123.write(output123)
print("#" * 25 + "Disconnected from Cisco_IOS " + device + "#" * 25)
# end of ios family

# start of asa firewall
# cisco asa
cisco_asa123 = {
    "device_type": "cisco_asa",
    "ip": "192.168.32.199",
    "username": input("enter your username for CISCO ASA: "),
    "password": input("enter your password for CISCO ASA: "),
    "port": 22
}
connection123 = ConnectHandler(**cisco_asa123)
# ssh_open
print("#" * 25 + "Connecting to Cisco_ASA " + "#" * 25)
output123 = connection123.send_command("show int ip br")
print(output123)

# start of arista_switch
# cisco arista_switch
cisco_arista123 = {
    "device_type": "arista_eos",
    "ip": "192.168.32.198",
    "username": input("enter your username for ARISTA: "),
    "password": input("enter your password for ARISTA: "),
    "port": 22
}
connection123 = ConnectHandler(**cisco_arista123)
# ssh_open
print("#" * 25 + "Connecting to Arista " + "#" * 25)
output123 = connection123.send_command("show ip int brief ")
print(output123)

# start of junos_vsrx
# cisco junos_vsrx
cisco_junosvsrx = {
    "device_type": "juniper_junos",
    "ip": "192.168.32.197",
    "username": input("enter your username for Junos_vSRX: "),
    "password": input("enter your password for Junos_vSRX: "),
    "port": 22
}
connection123 = ConnectHandler(**cisco_junosvsrx)
# ssh_open
print("#" * 25 + "Connecting to Junos_vSRX " + "#" * 25)
output123 = connection123.send_command("show interface terse")
print(output123)
