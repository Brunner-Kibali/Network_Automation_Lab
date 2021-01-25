import requests
import pprint

fortigate_user = 'admin'
fortigate_password = 'admin'

headers = {'Authorization': f'Bearer {api_token}'} #api_token is a place holder for initially generated token
params = {'scope': 'global'}

base_url = 'https://196.170.48.100'

s = requests.Session()

# Authenticate and obtain cookies, especially APSCOOKIE_ is important for subsequent GET request
s.post(base_url + "/logincheck", data={"username":fortigate_user, "secretkey":fortigate_password, "ajax":1}, verify=False)

def main(filename='Fortigate'):
    while True:
        action = input(" What to do with this fortigate api? get[i]nterface, get[a]dmin, change[h]ostname, e[x]it: ")

        if action == 'x' :
            print("Exiting...")
            break

        if action == 'i':
            get_interface()

        if action == 'a':
            get_admin()

        if action == 'h':
            change_hostname()

def get_interface():
    resp = s.get('https://%s/api/v2/monitor/system/interface/select/',
                 cookies=cookiejar, headers=headers, params=params, verify=False)

    if resp.status_code != 200:
        print("Error getting interface: {} {}".format(resp.status_code, resp.text))
        return False

    with open(filename, 'w') as f:
        f.write(resp.text)

    pprint.pprint(resp.content)

    return True


def get_admin():
    resp = s.get('https://%s/api/v2/monitor/system/admin/select/',
                 cookies=cookiejar, headers=headers, params=params, verify=False)

    if resp.status_code != 200:
        print("Error getting admins: {} {}".format(resp.status_code, resp.text))

        return False

    with open(filename, 'w') as f:
        f.write(resp.text)

    pprint.pprint(resp.content)

    return True



def change_hostname():
    resp = s.put('https://%s/api/v2/cmdb/system/hostname/hostname1 {"name":"hostname2"}',
                 cookies=cookiejar, headers=headers, params=params, verify=False)

    if resp.status_code != 204:
        print("Error changing hostname: {} {}".format(resp.status_code, resp.text))
        return False

    pprint.pprint("resp.content")

    return True

if __name__ == '__main__':
    main()
