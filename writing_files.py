
vlans_file = open('vlans.cfg', 'r')
vlans_text = vlans_file.read()
vlans_list = vlans_text.splitlines()

vlans = []

add_vlan = {'id': '70', 'name': 'MISC'}
vlans.append(add_vlan)

write_file = open('vlans_new.cfg', 'w')

#With automatically closes the file
#with open('vlans_new.cfg', 'w') as write_file:
    #write_file.write('vlan 10\n')
    #write_file.write('name TEST_VLAN\n')

for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
    write_file.write('vlan ' + id + '\n')
    write_file.write(' name ' + name + '\n')

write_file.close()
