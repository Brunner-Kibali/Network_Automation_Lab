
import requests

fortigate_host = '196.100.0.76'

fortigate_user = 'admin'

fortigate_password = 'admin'

headers = {'Accept': 'application/json'}

login_url = 'https://%s/logincheck' % fortigate_host

login_payload = {'username': fortigate_user, 'secretkey': fortigate_password}

resp = requests.post(login_url, data = login_payload, verify=False)

cookiejar = resp.cookies

def main():
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
    resp = requests.get('https://%s/api/v2/cmdb/system/interface/' % fortigate_host,
                 cookies=cookiejar, data = login_payload, verify=False)

    if resp.status_code != 200:
        print("Error getting interface: {} {}".format(resp.status_code, resp.text))
        return
    print("resp.content")

def get_admin():
    resp = requests.get('https://%s/api/v2/cmdb/system/admin/' % fortigate_host,
                 cookies=cookiejar, verify=False)

    if resp.status_code != 200:
        print("Error getting admins: {} {}".format(resp.status_code, resp.text))
        return

    print("resp.content")

def change_hostname():
    resp = requests.put('https://%s/api/v2/cmdb/system/hostname/hostname1 {"name":"hostname2"}' % fortigate_host,
                 cookies=cookiejar, verify=False)

    if resp.status_code != 204:
        print("Error changing hostname: {} {}".format(resp.status_code, resp.text))
        return

    print("resp.content")


if __name__ == '__main__':
    main()
