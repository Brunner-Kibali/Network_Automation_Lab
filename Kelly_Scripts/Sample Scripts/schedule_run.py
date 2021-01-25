from netmiko import ConnectHandler
def takebackup(cmd,rname):
 uname="cisco"
 passwd="cisco"
 device = ConnectHandler(device_type='cisco_ios', ip=rname,

username=uname, password=passwd)
 output=device.send_command(cmd)

# assuming we have two routers in network
devices="10.1.1.1, 10.1.1.254, 10.1.1.11, 10.1.1.12, 10.1.1.13, 10.1.1.14"
devices=devices.split(",")
for device in devices:
 takebackup("show run",device)

 fname=rname+".txt"
 file=open(fname,"w")
 print ('Taking Configuration of ' + fname)
 #print(output)
 file.write(output)
 file.close()

