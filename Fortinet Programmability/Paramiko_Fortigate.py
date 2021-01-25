ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('10.10.10.2',username='fake_root',password='fake_pass')

stdin, stdout, stderr=ssh.exec_command("execute dhcp lease-list wifi")

stdout.readlines()

ssh.close()

#Option 2

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('1.1.1.254',username='admin',password='password')

stdin, stdout, stderr=ssh.exec_command("get system status")

type(stdin)

stdout.readlines()

#Python fabric

def view_dhcp_leases():
        print("Viewing dhcp leases")

        run("execute dhcp lease-list wifi")


#If you want to use fabric to run commands on fortigates you need to
#disable the shell wrapping used by fabric when connecting via SSH:

from fabric.api import run

def get_sys():
   run("get sys status",shell=False)
