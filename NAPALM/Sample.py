# And you can get the interfaces’ ip address with small script as follows:
from pprint import pprint


def get_interfaces_ip(ip):

    import napalm

    driver = napalm.get_network_driver('ios')
    device = driver(hostname=ip, username='api-user', password='*******' )

    device.open()
    interfaces = device.get_interfaces_ip()
    device.close()

    return interfaces


if __name__ == "__main__":
    pprint(get_interfaces_ip("<ip_address or hostname>"))
