import requests

fortigate_host = '198.51.100.1'
fortigate_user = 'admin'
fortigate_pass = 'pass'

login_url = 'https://%s/logincheck' % fortigate_host
login_payload = {'username': fortigate_user, 'secretkey': fortigate_pass}

r = requests.post(login_url, data = login_payload, verify=False)
cookiejar = r.cookies

print r.headers
print r.text

r = requests.get('https://%s/api/v2/cmdb/system/interface/' % fortigate_host,
                 cookies=cookiejar, verify=False)

print r.content

