#Modules / standard
import requests

#Functions
def collect_all_devices(INPUT_DATA):
    """
    This function collects the main information about the devices
    """
    URL = "http://%s:%s/api/dcim/devices/" % (INPUT_DATA['url'], INPUT_DATA['port'])
    HEADERS = {'Authorization': 'Token %s' % INPUT_DATA['token']}

    RESPONSE = requests.get(url=URL, headers=HEADERS)
    return RESPONSE.json()

def collect_all_prefixes(INPUT_DATA):
    """
    This function collects all created IPv4/IPv6 prefixes
    """
    URL = "http://%s:%s/api/ipam/prefixes/" % (INPUT_DATA['url'], INPUT_DATA['port'])
    HEADERS = {'Authorization': 'Token %s' % INPUT_DATA['token']}

    RESPONSE = requests.get(url=URL, headers=HEADERS)

    return RESPONSE.json()

def collect_all_interfaces(INPUT_DATA, DEVICE_LIST):
    """
    This function collects all interfaces from devices
    """
    ALL_INTERFACES = []

    for DEVICE_ENTRY in DEVICE_LIST:
        URL = "http://%s:%s/api/dcim/interfaces/?device=%s" % (INPUT_DATA['url'], INPUT_DATA['port'],
                                                               DEVICE_ENTRY['name'])
        HEADERS = {'Authorization': 'Token %s' % INPUT_DATA['token']}


