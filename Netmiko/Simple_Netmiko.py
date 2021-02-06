from netmiko import ConnectHandler  # connecthandler = functions
import getpass

cisco_device123 = {
    "device_type": "cisco_ios",
    "ip": "192.168.32.132",
    "username": input("enter your username:"),
    "password": getpass.getpass(),
    "port": 22,
    "secret": "cisco"
}
connection123 = ConnectHandler(**cisco_device123)
output123 = connection123.send_command('show run')
print(output123)
