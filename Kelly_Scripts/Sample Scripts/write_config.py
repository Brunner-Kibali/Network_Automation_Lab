
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
import time
import logging

logging.basicConfig(filename='test.log', level=logging.INFO)
logger = logging.getLogger("netmiko")


def open_ip_file():
    ip_file = open("devices.txt", "r")
    for ip in ip_file:
        send_config(ip.strip('\n'))
        time.sleep(3)
    ip_file.close()


def send_config(ip):
    print('Configuring node %s..............please wait' % ip)
    device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'cisco',
        'password': 'cisco'
    }
    try:
        net_connect = ConnectHandler(**device)
        output = net_connect.send_config_from_file("change_file.txt")
        logger.info('%s has been successfully configured', ip)
        print('Awesome %s configured!!Moving to Nextone....' % ip)
        net_connect.disconnect()
    except NetMikoAuthenticationException:
        print('Configuration with Credential set 1 failed.. Trying credential set 2 for %s' % ip)
        device = {
            'device_type': 'cisco_ios',
            'ip': ip,
            'username': 'kcblanadmin',
            'password': 'Lock123*',
            'secret': 'Lock123*'
        }
        try:
            net_connect = ConnectHandler(**device)
            output = net_connect.send_config_from_file("change_file.txt")
            logger.info('%s has been successfully configured', ip)
            print('Awesome %s configured!!Moving to Nextone....' % ip)
            net_connect.disconnect()
        except NetMikoAuthenticationException:
            print('Both credentials Failed for %s ' % ip)

if __name__ == '__main__':
        open_ip_file()

