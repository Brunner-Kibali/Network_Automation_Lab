"""
Kelly Bwambok
"""
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
import time
import logging


logger = logging.getLogger('info_logger')
logger.setLevel(logging.DEBUG)
# Create file handler which logs even debug messages
fh = logging.FileHandler('Info.log', 'w')
fh.setLevel(logging.DEBUG)
# Create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# Add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)
logging.basicConfig(filename='test.log', level=logging.INFO)
logger = logging.getLogger("netmiko")


def open_ip_file():
    ip_file = open("ip_list.txt", "r")
    for ip in ip_file:
        send_config(ip.strip('\n'))
        time.sleep(3)
    ip_file.close()


def send_config(ip):
    print('Configuring node %s..............please wait' % ip)
    device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'wmutua',
        'password': 'Abu$dhabi321'
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
