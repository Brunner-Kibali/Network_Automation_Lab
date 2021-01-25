
vlans_file = open('vlans.cfg', 'r')
vlans_text = vlans_file.read()

vlans_list = vlans_text.splitlines()

vlans = []

for item in vlans_list:
    if 'vlan' in item:
        temp = {}
        id = item.strip().strip('vlan').strip()
        temp['id'] = id

    elif 'name' in item:
        name = item.strip().strip('name').strip()
        temp['name'] = name
        vlans.append(temp)

print(vlans)

vlans_file.close()
