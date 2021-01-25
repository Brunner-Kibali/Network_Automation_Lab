
# Ansible module to manage configuration on fortios devices

# EXAMPLE
""""
name: Update configuration from file
  fortios_config:
    host: 192.168.0.254
    username: admin
    password: password
    src: new_configuration.conf.j2
"""

# The I(src) argument provides a path to the configuration template to load into the remote device.

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.fortios.fortios import fortios_argument_spec, fortios_required_if

# check for pyFG lib
try:
    from pyFG import FortiOS, FortiConfig
    from pyFG.fortios import logger
    from pyFG.exceptions import CommandExecutionException, FailedCommit, ForcedCommit

    HAS_PYFG = True

except Exception:

    HAS_PYFG = False

# define device
f = FortiOS(module.params['host'],
                username=module.params['username'],
                password=module.params['password'],
                timeout=module.params['timeout'],
                vdom=module.params['vdom'])

# connect
try:
    f.open()

except Exception:
    module.fail_json(msg='Error connecting device')

# get  config
try:
    f.load_config(path=module.params['filter'])
    result['running_config'] = f.running_config.to_text()

except Exception:
    module.fail_json(msg='Error reading running config')
