#Fortigate config backup via scp

def backup_config(ip, username, password, full=False, path=None):
    """
    Retrieve fortigate configuration and save it to the local path
    :param ip: a string for target ip address
    :param username: a string for username who has read access
    :param password: a string for password
    :param full: boolean . Get full config if True, Get minimum config(diff from the factory default conifg) if False
    :param path: path to save the backup file
    :return: Name of the file saved with full path
    """
    import paramiko
    from scp import SCPClient

    ssh = paramiko.client.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
    # ssh.load_system_host_keys()
    ssh.connect(ip, username=username, password=password)

    with SCPClient(ssh.get_transport()) as scp:
        if full:
            config = 'fgt_config'
        else:
            config = 'sys_config'
        scp.get(config)

    return "DONE!"
