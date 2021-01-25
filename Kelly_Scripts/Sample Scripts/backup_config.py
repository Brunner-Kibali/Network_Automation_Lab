#!/usr/bin/env python

import sys
import time
import paramiko
import os
import cmd
import datetime
import logging

logging.basicConfig(filename='test.log', level=logging.INFO)
logger = logging.getLogger("netmiko")

###set date and time
now = datetime.datetime.now()

###authentication
USER = 'cisco'
PASSWORD = 'cisco'

###start FOR ...in
f = open('devices.txt')
for ip in f.readlines():
	ip = ip.strip()
	###prefix files for backup
	filename_prefix ='' + ip
	print ('Taking Configuration of ' + ip)
	###session start
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect(ip, username=USER, password=PASSWORD)

	###ssh shell
	chan = client.invoke_shell()
	time.sleep(2)
	###terminal length for no paging
	chan.send('terminal length 0\n')
	time.sleep(1)
	###show config and write output
	chan.send('sh run\n')
	time.sleep(30)
	output = chan.recv(999999)
	###show output config and write file with prefix, date and time
	#print ('Taken Configuration ' + ip)
	#filename = "%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)
	filename = "%s.txt" % (filename_prefix)
	ff = open(filename, 'a')
	#ff.write(output)
	ff.write(output.decode("utf-8") )
	ff.close()
	###close ssh session
	client.close()

	f.close()
