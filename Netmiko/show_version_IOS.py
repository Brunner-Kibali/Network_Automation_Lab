from netmiko import ConnectHandler
device = ConnectHandler(device_type='cisco_ios', ip='csr1',username='ntc',
password='ntc123')
output = device.send_command('show version')
print(output)
