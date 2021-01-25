#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#    Class to store interface attribute data
#
#    This class allows you to create dict fields and store them in the object.

class InterfaceObject(dict):
    """
    This object is inherited from a Dictionary object. This allows us to dynamically create fields programmatically.
    """
    def __getattr__(self, attr):
        """
        If attr is not a key, fall-back and get the attr
        """
        if self.has_key(attr):
            return super(InterfaceObject, self).__getitem__(attr)
        else:
            return super(InterfaceObject, self).__getattr__(attr)


    def __setattr__(self, attr, value):
        """
        Output the dict in its entirety.
        """
        super(InterfaceObject, self).__setitem__(attr, value)



#       Class to construct element and interface data store
#
#       Easiest way to get this information is: show version | inc System serial|uptime|image|Model number
#
#       self._up_time = uptime
#       self._version = version
#       self._serial = serial
#       self._hostname = hostname
#       self._model = model
#
#       To get interface information, obtain an interface list that's up using:
#       
#       show interfaces | inc *
#
#       Then from that list, generate a list of "show interface X | inc address"
#
#       This information then needs to be parsed to form the object below.
#
#       self._interfaces = interfaces


class NetElement(dict):
    """
    This class loads some fields with data from a Cisco IOS network element governed by the list here
    #
    #       Easiest way to get this information is: show version | inc System serial|uptime|image|Model number
    #
    #       self._up_time = uptime
    #       self._version = version
    #       self._serial = serial
    #       self._hostname = hostname
    #       self._model = model
    #
    #       To get interface information, obtain an interface list that's up using:
    #       
    #       show interfaces | inc *
    #
    #       Then from that list, generate a list of "show interface X | inc address"
    #
    #       This information then needs to be parsed to form the object below.
    #
    #       self._interfaces = interfaces
    """
    
    _element_array = []          # Array that stores unstructured element data
    _interface_array = []        # Array that stores unstructured interface names
    _interface_attrib_array = [] # Array that stores unstructured interface attribute data
    interfaces = InterfaceObject()

    def __init__(self):
        pass
    
    def __getattr__(self, attr):
        """
        If attr is not a key, fall-back and get the attr
        """
        if self.has_key(attr):
            return super(NetElement, self).__getitem__(attr)
        else:
            return super(NetElement, self).__getattr__(attr)


    def __setattr__(self, attr, value):
        """
        Output the dict in its entirety.
        """
        super(NetElement, self).__setitem__(attr, value)
        super(NetElement, self).__setattr__(attr, value)
    
    def data_parse(self):
        
         # Create an updater object components
        
        _dname = "" 
        _daddress = "" 
        _dmtu = ""

        interface_attrib_key = {}
        
        # These dictionaries below represent where each keyword is in the output, not digit position!
        interface_attrib_key_svi = {"interface": 2, "address" : 7, "MTU" : 3}
        interface_attrib_key_hw = {"interface": 2, "address" : 8, "MTU" : 3}
        
        # Let's parse the element objects
        
        # We need a bit more control over the text we receive. I've generated a buffered stream and populated it with our text.
        # A buffered stream will allow us to readlines and do seek operations etc.
        # Now we have the data, let's find what we're looking for. 'keys' represents our search strings, keys_left 
        # and keys_right represents our actual text digit position.
         
        keys = ["hostname", "uptime", "flash", "Model", "serial"]        
        keys_left = [9, 20, 29, 34, 34]
        keys_right = [18, 56, 65, 49, 45]
                
        for element_data in self._element_array:
            # This loop scans each line for our 'key' word which identifies our content
         
            key_offset_counter = 0
            for key in keys:
                 
                try:
                    if element_data.find(key) != -1:
                        self[key.lower()] = element_data[keys_left[key_offset_counter]:keys_right[key_offset_counter]] 
                except:
                    pass
                 
                key_offset_counter += 1

        
        # Parse the interface attributes
    
        
        # Easiest way is to use a template like this {"NAME" " {"ATT_NAME": "ATT_VALUE"}
        # Then we can use a list of attrib keys to index in to the dict like this:
        # attrib_keys = ["address", "MTU"]        
   
        for _array in self._interface_attrib_array:
              
            interface_attrib_list_stream = io.BytesIO(_array)
         
            EOF = False
         
            while EOF != True:
                data = interface_attrib_list_stream.readline()
             
                if "Vlan" in data:
                    interface_attrib_key = interface_attrib_key_svi
                elif ("Eth") in data:
                    interface_attrib_key = interface_attrib_key_hw
                
                
                if data == '':
                    EOF = True
                if any([x in data for x in interface_attrib_key]):
                    
                    # This section could be so much more tidier.
                    # Instead of using this routine, it would be cleaner to decouple the actual search
                    # terms like 'interface' or 'address' and use a key &amp; value search method like the element
                    # information search method.
                    # However, it shows how attempts to keep code tidy and reusable isn't always possible
                    # when you just 'need' to get something done. Data decoupling and meta data would solve this issue.

                    split_array = data.split (" ")
                    
                    for key in interface_attrib_key.keys():
                        if key in split_array:
                        
                            _temp_field =  split_array[interface_attrib_key.get(key)]
                            if key == "interface":
                                _dname = _temp_field
                            elif key == "address":
                                _daddress = _temp_field
                            elif key == "MTU":
                                _dmtu = _temp_field
            
            dict_updater = { _dname : {'address' : _daddress, 'MTU' : _dmtu}}
            self.interfaces.update(dict_updater)    
            
        # We get to this level and we've parsed our interface attributes and interfaces   
                            
    
    def data_fetch(self, client):
        
        client_conn = client.invoke_shell()
        client_conn.send("term len 0n")
        print "[DEV] Logged in and setting terminal length"
        time.sleep(1)
        output = client_conn.recv(1000)
        client_conn.send("n")
        output = client_conn.recv(1000)
        client_conn.send("show version | inc System serial|uptime|image|Model numbern")
        print "[DEV] Submitted element regular expression"
        time.sleep(1)
        
        self._ssh_output = client_conn.recv(500000)
        
        # We need a bit more control over the text we receive. I've generated a buffered stream and populated it with our text.
        # A buffered stream will allow us to readlines and do seek operations etc.
        
        element_stream = io.BytesIO(self._ssh_output)

        # ELEMENT TEXT EDITING
        # We need to move the position in the buffer beyond the first line, which is the regex itself.
        element_stream.next()
        
        for x in range(0, 4):
            self._element_array.append (element_stream.readline()[:-1])
        
        
        client_conn.send("show run | inc hostname")
        print "[DEV] Submitted element hostname regular expression"
        time.sleep(5)
        
        self._ssh_output = client_conn.recv(500000)
        
        # We need a bit more control over the text we receive. I've generated a buffered stream and populated it with our text.
        # A buffered stream will allow us to readlines and do seek operations etc.
        
        element_stream = io.BytesIO(self._ssh_output)
        
        element_stream.next()
        
        self._element_array.append(element_stream.readline()[:-1]+"n")
        
        # Now to get the active interface list
        
        client_conn.send("show interface sum | inc *n")
        print "[DEV] Submitted interface list regular expression"
        time.sleep(1)
        
        self._ssh_output = client_conn.recv(500000)
        
        interface_list_stream = io.BytesIO(self._ssh_output)
        
        EOF = False
        
        interface_list_key = ["Vlan", "Eth"]
        
        while EOF != True:
            data = interface_list_stream.readline()
            
            if data == '':
                EOF = True
            if any([x in data for x in interface_list_key]):
                
                split_array = data.split (" ")
                self._interface_array.append(split_array[1])
            else:
                pass
        
        # Once we have the active interface list, we need to get attributes from them and store them in an unstructured array
        
        for interface in self._interface_array:
            
            client_conn.send("show interface " + interface + " | inc bia|MTUn")
            print "[DEV] Submitted interface regular expression for interface " + interface + " attributes"
            time.sleep(1)
        
            self._ssh_output = client_conn.recv(500000)
            
            self._interface_attrib_array.append(self._ssh_output)

        self.data_parse()



import paramiko, base64, time, io, code

key = paramiko.RSAKey(data=base64.decodestring('AAAA<*snip*>=='))

client = paramiko.SSHClient()
client.get_host_keys().add('10.1.1.1', 'ssh-rsa', key)
client.connect('10.1.1.1', username='cisco', password='cisco')



dev1 = NetElement()
dev1.data_fetch(client)

# Now let's print out the network element report

print "n"
print "=" * 64 + "n" + 20 * " " + "Network Element Reportn" + "=" * 64
print "Hostname:t" + dev1.get('hostname')
print "Model:tt" + dev1.get('model')
print "Serial:tt" + dev1.get('serial')
print "Uptime:tt" + dev1.get('uptime')
print "Version:t" + dev1.get('flash')
print ""

print "Active Interface List:"
print 32 * "-"
for key in dev1.interfaces.keys():
    print "Interface ", key, "nt", dev1.interfaces.get(key)
    
print "=" * 64 + "n"

# Finally, drop in to the interactive shell

print "nnWelcome to the interactive shell"
code.interact(local=locals())


# client.close()